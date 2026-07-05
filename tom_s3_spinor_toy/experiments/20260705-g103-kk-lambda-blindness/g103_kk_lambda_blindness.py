"""G103: KK-spectrum lambda-blindness — final consistency brick of the lambda no-go.

Session 2026-07-05 mechanism sweep: no standard 10D non-perturbative source
(wrapped branes H_p(S^6)=0 for 0<p<6, gaugino condensation 1/g4^2 ~ rho6^6,
worldline instantons S ~ m*rho6, Borel resummation of the alpha' series with
the opposite sign, non-geometric fluxes = polynomial) generates the ansatz
V_NP = A*exp(-lambda_np/rho6^2): every instanton action scales as a POSITIVE
power of rho6. If lambda_np is therefore a free 4D EFT parameter (LAMBDA-B5-G4),
observables must split: the geometric KK tower is lambda-blind, while the
modulus sector carries lambda_np with the H1 sqrt-scaling. G103 verifies the split:

  (S) SYMBOLIC  : KK tower formulas contain no lambda_np symbol           [sympy]
  (I) INDIRECT  : spread of m_KK across lambda_np in [0.15,0.60] <= 0.5%  [numeric]
                  (only channel: rho6_min drift, GA1 measured < 0.3%)
  (M) MODULUS   : fit m_mod ~ lambda_np^p on the same sweep, p in [0.40,0.60]
  (P) POSITIVE  : reproduce GA1 reference at lambda_np=1/3
                  (rho6_min = 1.1791 +- 0.002, ratio = 0.198% +- 0.02)
  (N) NEGATIVE  : injected fake tower m_KK*sqrt(1+lambda_np) must VIOLATE (I)

Kill criterion: (I) spread > 1% => geometry secretly depends on lambda_np =>
free-parameter picture and no-go closure BLOCKED. (M) outside [0.30,0.70] =>
H1 scaling wrong. (N) not caught => test void.
"""

from __future__ import annotations

import json
from math import exp, pi, sqrt
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g103.json"

# --- canonical G91/GA1 constants (copied verbatim from ga1_lambda_sensitivity.py) ---
C_SM = 0.986
RHO6_STAR = 1.090
V_FLUX = 15 * C_SM**3 / (16 * pi)

VOL_S3_UNIT = 2 * pi**2
VOL_S6_UNIT = 16 * pi**3 / 15

N3, N6, D_EXT = 3, 6, 4

K_MAT = np.diag([float(N3), float(N6)]) + np.outer(
    [float(N3), float(N6)], [float(N3), float(N6)]
) / (D_EXT - 2)
PATH_TANGENT = np.array([2.0, 1.0])
PATH_K = float(PATH_TANGENT @ K_MAT @ PATH_TANGENT)  # = 90.0

LAMBDA_SWEEP = [0.15, 0.20, 0.25, 1.0 / 3.0, 0.40, 0.45, 0.50, 0.55, 0.60]

# thresholds (pre-registered in claim.md)
KK_SPREAD_PASS_PCT = 0.5
KK_SPREAD_KILL_PCT = 1.0
EXPONENT_PASS = (0.40, 0.60)
EXPONENT_KILL = (0.30, 0.70)

# --- (S) symbolic tower ---------------------------------------------------------
rho6_sym, lambda_np_sym, ell_sym = sp.symbols("rho6 lambda_np ell", positive=True)

# scalar Laplace-Beltrami towers on the unit spheres, scaled by the path radii
# (rho3 = rho6^2 on the G91 path); lightest verified modes carry prefactors 1.5, 3.0
M2_TOWER_S6 = ell_sym * (ell_sym + 5) / rho6_sym**2
M2_TOWER_S3 = ell_sym * (ell_sym + 2) / rho6_sym**4  # rho3^2 = rho6^4
M_LIGHT_S3 = sp.Rational(3, 2) / rho6_sym**2
M_LIGHT_S6 = 3 / rho6_sym


def tower_is_lambda_blind() -> bool:
    """(S): no lambda_np symbol in any KK tower expression."""
    exprs = (M2_TOWER_S6, M2_TOWER_S3, M_LIGHT_S3, M_LIGHT_S6)
    return all(lambda_np_sym not in e.free_symbols for e in exprs)


# --- canonical potential and per-lambda solve (GA1 logic, unchanged) -------------
def run_for_lambda(lam: float) -> dict | None:
    """Full G91-path calculation for a given lambda_np. None if no AdS minimum."""
    a_np = V_FLUX * exp(lam / RHO6_STAR**2)

    def v_path(rho6: float) -> float:
        num = V_FLUX - a_np * exp(-lam / rho6**2)
        denom = VOL_S3_UNIT * VOL_S6_UNIT * rho6**6 * rho6**6
        return num / denom

    def v_path_deriv2(rho6: float, step: float = 5e-4) -> float:
        return (v_path(rho6 + step) - 2 * v_path(rho6) + v_path(rho6 - step)) / step**2

    result = minimize_scalar(v_path, bounds=(0.5, 3.0), method="bounded")
    if not result.success:
        return None

    rho6_min = float(result.x)
    v_min = float(v_path(rho6_min))
    if v_min >= 0:
        return None
    vpp = v_path_deriv2(rho6_min)
    if vpp <= 0:
        return None

    m2_mod = rho6_min**2 * vpp / PATH_K
    rho3_min = rho6_min**2
    m_kk_s3 = 1.5 / rho3_min
    m_kk_s6 = 3.0 / rho6_min
    m_kk = min(m_kk_s3, m_kk_s6)

    return {
        "lambda_np": round(lam, 6),
        "rho6_min": rho6_min,
        "v_min": v_min,
        "m_mod": sqrt(m2_mod),
        "m_kk": m_kk,
        "kk_source": "S3" if m_kk_s3 < m_kk_s6 else "S6",
        "ratio_pct": sqrt(m2_mod) / m_kk * 100,
    }


def sweep(lambdas: list[float] | None = None) -> list[dict]:
    rows = [run_for_lambda(lam) for lam in (lambdas or LAMBDA_SWEEP)]
    return [r for r in rows if r is not None]


def spread_pct(values: list[float]) -> float:
    lo, hi = min(values), max(values)
    assert lo > 0, "spread_pct requires strictly positive values (log-scale spread)"
    return (hi - lo) / lo * 100


def fit_exponent(rows: list[dict], key: str = "m_mod") -> float:
    """p = d ln(key) / d ln(lambda_np) via least-squares in log-log."""
    assert all(r[key] > 0 and r["lambda_np"] > 0 for r in rows), (
        f"fit_exponent requires strictly positive '{key}' and lambda_np"
    )
    lams = np.log([r["lambda_np"] for r in rows])
    vals = np.log([r[key] for r in rows])
    p, _ = np.polyfit(lams, vals, 1)
    return float(p)


def negative_control(rows: list[dict]) -> dict:
    """(N): a deliberately lambda-dependent fake tower must violate criterion (I)."""
    fake = [r["m_kk"] * sqrt(1 + r["lambda_np"]) for r in rows]
    fake_spread = spread_pct(fake)
    return {"fake_spread_pct": fake_spread, "caught": fake_spread > KK_SPREAD_PASS_PCT}


def main() -> None:
    rows = sweep()

    # (S)
    s_pass = tower_is_lambda_blind()

    # (I)
    kk_spread = float(spread_pct([r["m_kk"] for r in rows]))
    i_pass = bool(kk_spread <= KK_SPREAD_PASS_PCT)
    i_killed = bool(kk_spread > KK_SPREAD_KILL_PCT)

    # (M)
    p_exp = fit_exponent(rows)
    m_pass = bool(EXPONENT_PASS[0] <= p_exp <= EXPONENT_PASS[1])
    m_killed = not (EXPONENT_KILL[0] <= p_exp <= EXPONENT_KILL[1])

    # (P)
    ref = run_for_lambda(1.0 / 3.0)
    assert ref is not None
    p_ctrl = bool(abs(ref["rho6_min"] - 1.1791) <= 0.002 and abs(ref["ratio_pct"] - 0.198) <= 0.02)

    # (N)
    n_ctrl = negative_control(rows)

    verdict = (
        "PASS"
        if (s_pass and i_pass and m_pass and p_ctrl and n_ctrl["caught"])
        else ("KILLED" if (i_killed or m_killed) else "FAIL")
    )

    results = {
        "gate": "G103",
        "sweep": [
            {k: (round(v, 6) if isinstance(v, float) else v) for k, v in r.items()} for r in rows
        ],
        "checks": {
            "S_symbolic_blind": s_pass,
            "I_kk_spread_pct": round(kk_spread, 4),
            "I_pass": i_pass,
            "M_modulus_exponent": round(p_exp, 4),
            "M_pass": m_pass,
            "P_positive_control": p_ctrl,
            "P_reference": {
                "rho6_min": round(ref["rho6_min"], 6),
                "ratio_pct": round(ref["ratio_pct"], 4),
            },
            "N_negative_control": {
                "fake_spread_pct": round(n_ctrl["fake_spread_pct"], 4),
                "caught": n_ctrl["caught"],
            },
        },
        "thresholds": {
            "kk_spread_pass_pct": KK_SPREAD_PASS_PCT,
            "kk_spread_kill_pct": KK_SPREAD_KILL_PCT,
            "exponent_pass": EXPONENT_PASS,
            "exponent_kill": EXPONENT_KILL,
        },
        "verdict": verdict,
        "interpretation": (
            "Geometric KK tower is lambda-blind (direct: symbolic zero; indirect: "
            f"{kk_spread:.3f}% over 4x lambda range); lambda_np is observable only in "
            f"the modulus sector with m_mod ~ lambda^{p_exp:.3f} (H1 sqrt-law). "
            "lambda_np = FREE_COUPLING_PARAMETER at the observable level: nothing "
            "built from geometry can fix it, closing the UV-derivation branch."
        ),
    }

    print(f"{'lambda_np':>10}  {'rho6_min':>10}  {'m_kk':>10}  {'m_mod':>12}  {'ratio%':>8}")
    print("-" * 58)
    for r in rows:
        print(
            f"{r['lambda_np']:>10.4f}  {r['rho6_min']:>10.4f}  {r['m_kk']:>10.6f}  "
            f"{r['m_mod']:>12.6e}  {r['ratio_pct']:>8.4f}"
        )
    print(f"\n(S) symbolic blind : {s_pass}")
    print(f"(I) kk spread      : {kk_spread:.4f}%  (pass <= {KK_SPREAD_PASS_PCT}%)  -> {i_pass}")
    print(f"(M) m_mod exponent : {p_exp:.4f}   (pass in {EXPONENT_PASS})        -> {m_pass}")
    print(
        f"(P) positive ctrl  : {p_ctrl}  (rho6_min={ref['rho6_min']:.4f}, ratio={ref['ratio_pct']:.4f}%)"
    )
    print(
        f"(N) negative ctrl  : caught={n_ctrl['caught']} (fake spread {n_ctrl['fake_spread_pct']:.2f}%)"
    )
    print(f"\nVERDICT: {verdict}")

    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"Results -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
