"""G70: stress-test the non-perturbative exponent in the G62 potential.

For
    V(rho; p) = [V_flux - A_np exp(-a_p / rho**p)] / (K_vol rho**(2 n)),
the scan varies p while holding
    u_star = a_p / rho_star**p
fixed.  This preserves both the NP strength at the UV anchor and the
Minkowski condition V(rho_star) = 0, isolating the functional-form change.

This is a sensitivity analysis of the effective model, not validation of the
model against physical data.
"""

from __future__ import annotations

import csv
from dataclasses import asdict, dataclass
from math import exp, pi, sqrt
from pathlib import Path

from scipy.optimize import minimize_scalar

P_VALUES = [1.0, 1.5, 2.0, 2.5, 3.0]

C_SM = 0.986
V_FLUX = 15 * C_SM**3 / (16 * pi)
RHO_STAR = 1.090
N_VOLUME = 6
VOLUME_POWER = 2 * N_VOLUME
K_VOL = (2 * pi**2) * (16 * pi**3 / 15)

BASE_LAMBDA = 1.0 / 3.0
BASE_P = 2.0
U_STAR = BASE_LAMBDA / RHO_STAR**BASE_P

KAPPA_TARGET = sqrt(7 / 6)
MAX_RELATIVE_DEVIATION = 0.005  # preregistered 0.5% relative tolerance


@dataclass(frozen=True)
class ScanRow:
    p: float
    a_p: float
    u_star: float
    rho_min: float
    kappa: float
    kappa_analytic: float
    relative_deviation: float
    v_min: float
    second_derivative: float


def exponent_coefficient(p: float) -> float:
    """Choose a_p so a_p / rho_star**p equals the G62 anchor U_STAR."""
    if p <= 0:
        raise ValueError("p must be positive")
    return U_STAR * RHO_STAR**p


def a_np_minkowski() -> float:
    """Minkowski-normalized NP amplitude; independent of p at fixed U_STAR."""
    return V_FLUX * exp(U_STAR)


def potential(rho: float, p: float) -> float:
    """Generalized G62 Einstein-frame potential without the Casimir correction."""
    if rho <= 0:
        raise ValueError("rho must be positive")
    a_p = exponent_coefficient(p)
    numerator = V_FLUX - a_np_minkowski() * exp(-a_p / rho**p)
    return numerator / (K_VOL * rho**VOLUME_POWER)


def second_derivative(rho: float, p: float, step: float = 5e-4) -> float:
    """Centered coordinate-space second derivative used as a local-minimum check."""
    return (
        potential(rho + step, p)
        - 2 * potential(rho, p)
        + potential(rho - step, p)
    ) / step**2


def find_minimum(p: float) -> tuple[float, float]:
    """Find the interior AdS minimum above the UV-selection radius."""
    result = minimize_scalar(
        lambda rho: potential(rho, p),
        bounds=(RHO_STAR + 1e-7, 2.5),
        method="bounded",
        options={"xatol": 1e-13},
    )
    if not result.success:
        raise RuntimeError(f"minimum search failed for p={p}: {result.message}")
    return float(result.x), float(result.fun)


def analytic_kappa(p: float) -> float:
    """Leading small-U_STAR/N_VOLUME prediction for arbitrary exponent p."""
    if p <= 0:
        raise ValueError("p must be positive")
    return (1 + p / (2 * N_VOLUME)) ** (1 / p)


def evaluate(p: float) -> ScanRow:
    rho_min, v_min = find_minimum(p)
    kappa = rho_min / RHO_STAR
    kappa_analytic = analytic_kappa(p)
    relative_deviation = abs(kappa - KAPPA_TARGET) / KAPPA_TARGET
    return ScanRow(
        p=p,
        a_p=exponent_coefficient(p),
        u_star=U_STAR,
        rho_min=rho_min,
        kappa=kappa,
        kappa_analytic=kappa_analytic,
        relative_deviation=relative_deviation,
        v_min=v_min,
        second_derivative=second_derivative(rho_min, p),
    )


def run_scan(p_values: list[float] | None = None) -> list[ScanRow]:
    """Evaluate the preregistered exponent family."""
    values = P_VALUES if p_values is None else p_values
    return [evaluate(p) for p in values]


def write_csv(path: str | Path, rows: list[ScanRow] | None = None) -> Path:
    """Write a deterministic CSV artifact for audit and publication tables."""
    output = Path(path)
    data = run_scan() if rows is None else rows
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(data[0]).keys()))
        writer.writeheader()
        for row in data:
            writer.writerow(asdict(row))
    return output


def _print_table(rows: list[ScanRow]) -> None:
    print("p    a_p        rho_min    kappa     rel.dev     analytic")
    for row in rows:
        print(
            f"{row.p:3.1f}  {row.a_p:.6f}  {row.rho_min:.6f}  "
            f"{row.kappa:.6f}  {row.relative_deviation:.4%}  "
            f"{row.kappa_analytic:.6f}"
        )


if __name__ == "__main__":
    scan = run_scan()
    csv_path = write_csv(Path(__file__).with_name("results.csv"), scan)
    _print_table(scan)
    print(f"\nWrote {csv_path}")
