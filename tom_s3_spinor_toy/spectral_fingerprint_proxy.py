"""Spectral-fingerprint proxy test — v0.2.0 spinor-geometry pivot.

Tests whether the Dirac/spinor sector distinguishes S², S³, S⁶ through
SPECTRAL observables (eigenvalue ladder, |λ_min| = d/2, spectral distance),
NOT through IPR. IPR appears only as a secondary exploratory observable.

Method
------
Radial reduction of the squared Dirac operator on S^d in geodesic polar
angle θ ∈ (0, π). After flattening the volume measure (u = sin^{(d-1)/2}θ·f),
the angular sector with S^{d-1} Dirac eigenvalue κ = l + (d-1)/2 obeys a
Schrödinger-form Sturm-Liouville problem

    H u = -u'' + V(θ) u = λ² u,   V(θ) = κ(κ + cosθ) / sin²θ .

Analytic targets (Camporesi-Higuchi gr-qc/9505009, VERIFIED_FROM_PDF):
    λ = n + d/2,  n ≥ l,   |λ_min| = d/2,
    degeneracy on S³: D₃(n) = (n+1)(n+2)  [eq 3.58].

Operator verification: the discretized H reproduces λ = n + d/2 to
~7e-7 relative error for d=3 and d=6 at N_grid=4000 [VERIFIED-tool
2026-06-10]. The match across two dimensions and 5 levels with no fitted
parameters rules out coincidence; the operator construction (superpotential
W = κ/sinθ) and the target spectrum are independent inputs.

KNOWN LIMITATION (discretization survival, recorded per estimand §7):
    For d=2, lowest sector κ = 1/2 the endpoint coefficient κ(κ-1) = -1/4
    is the critical (limit-circle) value; uniform-grid finite differences
    converge only logarithmically (~5% error at N=4000, rate ~h^0.1).
    The shooting solver with correct indicial exponents (u ~ θ^{κ+1} at 0,
    u ~ (π-θ)^κ at π) is used for this case instead.

Scientific status: research_only. No physical promotion. λ (coupling in the
V-operator branch) remains FREE_COUPLING_PARAMETER — this module does not
touch it. No claim of gauge-group emergence.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field

import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import eigh, eigh_tridiagonal
from scipy.optimize import brentq

SPHERES = (2, 3, 6)


# ---------------------------------------------------------------------------
# Analytic targets (independent ground truth — Camporesi-Higuchi)
# ---------------------------------------------------------------------------

def analytic_dirac_ladder(d: int, n_levels: int, l_sector: int = 0) -> list[float]:
    """λ = n + d/2 for n = l_sector, l_sector+1, ... (CH eq 3.26)."""
    return [n + d / 2.0 for n in range(l_sector, l_sector + n_levels)]


def analytic_lambda_min(d: int) -> float:
    """|λ_min| = d/2 on S^d."""
    return d / 2.0


def analytic_scalar_eigenvalues(d: int, n_levels: int) -> list[float]:
    """Scalar Laplacian: λ_L = L(L+d-1), L = 0, 1, 2, ..."""
    return [float(L * (L + d - 1)) for L in range(n_levels)]


def analytic_degeneracy_s3_dirac(n: int) -> int:
    """D₃(n) = (n+1)(n+2) per chirality branch (CH eq 3.58). [ANALYTIC-INPUT]"""
    return (n + 1) * (n + 2)


def angular_degeneracy_s2_dirac(l: int) -> int:
    """Degeneracy of S² Dirac eigenvalue ±(l+1): 2(l+1). [ANALYTIC-INPUT]"""
    return 2 * (l + 1)


# ---------------------------------------------------------------------------
# Discretized radial operators
# ---------------------------------------------------------------------------

def dirac_potential(theta: np.ndarray, kappa: float) -> np.ndarray:
    """V(θ) = κ(κ + cosθ)/sin²θ — radial Dirac² potential in flat measure."""
    return kappa * (kappa + np.cos(theta)) / np.sin(theta) ** 2


def radial_dirac_sq_tridiag(
    d: int, l_sector: int, n_grid: int
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Finite-difference tridiagonal for H = -d²/dθ² + V on interior nodes.

    Returns (diag, offdiag, theta_grid). Dirichlet boundary conditions.
    """
    kappa = l_sector + (d - 1) / 2.0
    h = np.pi / n_grid
    theta = h * np.arange(1, n_grid)
    diag = 2.0 / h**2 + dirac_potential(theta, kappa)
    off = -np.ones(n_grid - 2) / h**2
    return diag, off, theta


def dirac_ladder_fd(
    d: int, l_sector: int = 0, n_grid: int = 4000, n_levels: int = 5
) -> np.ndarray:
    """Lowest |λ| ladder via finite differences. Accurate for κ ≥ 1."""
    diag, off, _ = radial_dirac_sq_tridiag(d, l_sector, n_grid)
    lam_sq = eigh_tridiagonal(
        diag, off, select="i", select_range=(0, n_levels - 1), eigvals_only=True
    )
    return np.sqrt(np.abs(lam_sq))


def dirac_ladder_shooting(
    d: int,
    l_sector: int = 0,
    n_levels: int = 4,
    e_max: float = 25.0,
    n_scan: int = 600,
) -> np.ndarray:
    """Lowest |λ| ladder via two-sided shooting with indicial asymptotics.

    Required for the critical case d=2, l_sector=0 (κ = 1/2), where the
    endpoint coefficient κ(κ-1) = -1/4 makes uniform FD converge only
    logarithmically. Eigenvalues located by sign-change scan of the
    matching Wronskian — no analytic targets are used as seeds.
    """
    kappa = l_sector + (d - 1) / 2.0

    def wronskian(E: float, eps: float = 1e-6, theta_match: float = 1.4) -> float:
        def rhs(t, y):
            return [y[1], (dirac_potential(np.array([t]), kappa)[0] - E) * y[0]]

        # left endpoint: u ~ θ^{κ+1}
        y_left = [eps ** (kappa + 1), (kappa + 1) * eps**kappa]
        sol_l = solve_ivp(rhs, [eps, theta_match], y_left, rtol=1e-10, atol=1e-14)
        u_l, du_l = sol_l.y[0, -1], sol_l.y[1, -1]
        # right endpoint: u ~ (π-θ)^κ
        y_right = [eps**kappa, -kappa * eps ** (kappa - 1)]
        sol_r = solve_ivp(
            rhs, [np.pi - eps, theta_match], y_right, rtol=1e-10, atol=1e-14
        )
        u_r, du_r = sol_r.y[0, -1], sol_r.y[1, -1]
        return u_l * du_r - du_l * u_r

    # Lazy scan with early exit: stop as soon as n_levels roots are bracketed.
    energies = np.linspace(0.05, e_max, n_scan)
    roots: list[float] = []
    w_prev = wronskian(energies[0])
    for i in range(1, len(energies)):
        w_cur = wronskian(energies[i])
        if w_prev * w_cur < 0:
            roots.append(
                brentq(wronskian, energies[i - 1], energies[i], xtol=1e-10)
            )
            if len(roots) >= n_levels:
                break
        w_prev = w_cur
    return np.sqrt(np.asarray(roots))


def dirac_ladder(
    d: int, l_sector: int = 0, n_grid: int = 4000, n_levels: int = 4
) -> np.ndarray:
    """Dispatch: shooting for the critical κ = 1/2 case, FD otherwise."""
    kappa = l_sector + (d - 1) / 2.0
    if abs(kappa - 0.5) < 1e-12:
        return dirac_ladder_shooting(d, l_sector, n_levels=n_levels)
    return dirac_ladder_fd(d, l_sector, n_grid=n_grid, n_levels=n_levels)


def scalar_radial_eigenvalues(
    d: int, n_grid: int = 4000, n_levels: int = 4
) -> np.ndarray:
    """Scalar Laplacian radial sector (l=0): eigen = L(L+d-1).

    Flat-measure form: H_s = -d²/dθ² + p(p-1)/sin²θ, p = (d-1)/2;
    scalar eigenvalue = H_s eigenvalue - p².
    Verified exact for d=3 ([0,3,8,15]) and d=6 ([0,6,14,24]) at N=4000.
    """
    p = (d - 1) / 2.0
    h = np.pi / n_grid
    theta = h * np.arange(1, n_grid)
    diag = 2.0 / h**2 + p * (p - 1) / np.sin(theta) ** 2
    off = -np.ones(n_grid - 2) / h**2
    vals = eigh_tridiagonal(
        diag, off, select="i", select_range=(0, n_levels - 1), eigvals_only=True
    )
    return vals - p**2


# ---------------------------------------------------------------------------
# Fingerprint and spectral distance
# ---------------------------------------------------------------------------

@dataclass
class Fingerprint:
    d: int
    lambda_min: float
    ladder: list[float]
    ladder_source: str  # "fd" | "shooting"
    degeneracy_s3: list[int] = field(default_factory=list)  # [ANALYTIC-INPUT] except sector count


def compute_fingerprint(d: int, n_levels: int = 4, n_grid: int = 4000) -> Fingerprint:
    """Numerical spectral fingerprint of S^d from the lowest angular sector."""
    kappa = (d - 1) / 2.0
    ladder = dirac_ladder(d, 0, n_grid=n_grid, n_levels=n_levels)
    source = "shooting" if abs(kappa - 0.5) < 1e-12 else "fd"
    return Fingerprint(
        d=d,
        lambda_min=float(ladder[0]),
        ladder=[float(x) for x in ladder],
        ladder_source=source,
    )


def spectral_distance(fp_a: Fingerprint, fp_b: Fingerprint) -> float:
    """Mean absolute ladder difference. Analytic value = |d_a - d_b| / 2."""
    k = min(len(fp_a.ladder), len(fp_b.ladder))
    a = np.asarray(fp_a.ladder[:k])
    b = np.asarray(fp_b.ladder[:k])
    return float(np.mean(np.abs(a - b)))


def fingerprint_match_score(
    ladder: np.ndarray, target: list[float], rel_tol: float = 0.05
) -> float:
    """Fraction of target levels recovered within rel_tol."""
    hits = sum(
        1
        for t in target
        if np.any(np.abs(np.asarray(ladder) - t) / t < rel_tol)
    )
    return hits / len(target)


# ---------------------------------------------------------------------------
# S³ sector structure — partial numerical degeneracy reconstruction
# ---------------------------------------------------------------------------

def s3_sector_structure(
    max_l: int = 2, n_grid: int = 4000, n_levels: int = 4
) -> dict[str, object]:
    """Verify λ = n + 3/2 appears in sectors l = 0..n (numerical content),
    then reconstruct D₃(n) = Σ_{l≤n} 2(l+1) = (n+1)(n+2).

    Honest split: sector membership is NUMERICALLY verified; the angular
    factor 2(l+1) per sector is an ANALYTIC INPUT (S² Dirac degeneracy).
    """
    sectors = {l: dirac_ladder_fd(3, l, n_grid, n_levels) for l in range(max_l + 1)}
    result: dict[str, object] = {"sectors": {l: list(map(float, v)) for l, v in sectors.items()}}
    reconstruction = []
    for n in range(max_l + 1):
        lam_n = n + 1.5
        members = [
            l for l, lad in sectors.items() if np.any(np.abs(lad - lam_n) < 0.01)
        ]
        deg = sum(angular_degeneracy_s2_dirac(l) for l in members)
        reconstruction.append(
            {
                "n": n,
                "lambda": lam_n,
                "sectors_containing": members,
                "sector_count_expected": n + 1,
                "degeneracy_reconstructed": deg,
                "degeneracy_analytic": analytic_degeneracy_s3_dirac(n),
            }
        )
    result["degeneracy_reconstruction"] = reconstruction
    return result


# ---------------------------------------------------------------------------
# Negative controls
# ---------------------------------------------------------------------------

def ipr_of_matrix(m: np.ndarray) -> float:
    """Mean IPR over all eigenvectors: mean(Σ_i |ψ_i|⁴). SECONDARY/EXPLORATORY."""
    _, vec = eigh(m)
    return float(np.mean(np.sum(np.abs(vec) ** 4, axis=0)))


def ipr_shift_invariance_gap(n: int = 200, shift: float = 1.5, seed: int = 42) -> float:
    """NC-A: |IPR(H+W) - IPR(H+W+c·I)| — must be ~0 (R/4 channel closed).

    Permanent regression: H -> H + cI preserves eigenvectors exactly,
    therefore a constant curvature term R/4·I cannot affect IPR.
    """
    rng = np.random.default_rng(seed)
    h = rng.normal(size=(n, n))
    h = (h + h.T) / 2.0
    w = np.diag(rng.uniform(-10.0, 10.0, n))
    a = h + w
    return abs(ipr_of_matrix(a) - ipr_of_matrix(a + shift * np.eye(n)))


def random_hermitian_match_score(
    d_target: int = 3, n: int = 60, n_levels: int = 4, seed: int = 7
) -> float:
    """NC-B: random Hermitian ladder vs analytic Dirac targets — should be low."""
    rng = np.random.default_rng(seed)
    h = rng.normal(size=(n, n))
    h = (h + h.T) / np.sqrt(2 * n)  # GOE normalization, spectrum ~ [-2, 2]
    vals = np.sort(np.abs(np.linalg.eigvalsh(h)))[:n_levels]
    return fingerprint_match_score(vals, analytic_dirac_ladder(d_target, n_levels))


def scalar_vs_dirac_same_sphere(d: int = 3, n_levels: int = 4) -> dict[str, object]:
    """NC-C: scalar and Dirac ladders on the SAME sphere must differ.

    NOTE (honest framing): the scalar SPECTRUM is itself geometry-sensitive
    (λ₁ = d). What was geometry-agnostic in v0.1.22 was the vector/IPR
    observable channel on lattice products — NOT the scalar spectrum.
    This control shows the two OPERATORS are spectrally distinguishable
    on one sphere, i.e. the fingerprint detects operator structure.
    """
    scalar = scalar_radial_eigenvalues(d, n_levels=n_levels)
    dirac = dirac_ladder(d, 0, n_levels=n_levels)
    # compare on common footing: sqrt of scalar eigenvalues (skip L=0 zero mode)
    scalar_sqrt = np.sqrt(np.abs(scalar[1:]))
    cross = fingerprint_match_score(
        scalar_sqrt, analytic_dirac_ladder(d, n_levels - 1), rel_tol=0.05
    )
    return {
        "scalar_eigenvalues": [float(x) for x in scalar],
        "dirac_ladder": [float(x) for x in dirac],
        "cross_match_score": float(cross),
    }


# ---------------------------------------------------------------------------
# Discretization survival (estimand §7 gate C9 / SA-1)
# ---------------------------------------------------------------------------

def discretization_survival(
    d: int, grids: tuple[int, ...] = (1000, 2000, 4000), n_levels: int = 4
) -> dict[int, float]:
    """Max relative ladder error vs analytic targets per grid size (FD path)."""
    target = np.asarray(analytic_dirac_ladder(d, n_levels))
    out: dict[int, float] = {}
    for n_grid in grids:
        ladder = dirac_ladder_fd(d, 0, n_grid, n_levels)
        out[n_grid] = float(np.max(np.abs(ladder - target) / target))
    return out


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def run_proxy(n_levels: int = 4, n_grid: int = 4000) -> dict[str, object]:
    """Full proxy run. Returns a JSON-serializable result dict."""
    fps = {d: compute_fingerprint(d, n_levels, n_grid) for d in SPHERES}

    ladder_errors = {}
    for d, fp in fps.items():
        target = analytic_dirac_ladder(d, len(fp.ladder))
        ladder_errors[d] = float(
            np.max(np.abs(np.asarray(fp.ladder) - target) / np.asarray(target))
        )

    distances = {}
    for i, da in enumerate(SPHERES):
        for db in SPHERES[i + 1 :]:
            computed = spectral_distance(fps[da], fps[db])
            analytic = abs(da - db) / 2.0
            distances[f"S{da}-S{db}"] = {
                "computed": computed,
                "analytic": analytic,
                "rel_err": abs(computed - analytic) / analytic,
            }

    return {
        "version": "v0.2.0",
        "primary_endpoint": "spectral_fingerprint",
        "fingerprints": {
            d: {
                "lambda_min": fp.lambda_min,
                "lambda_min_analytic": analytic_lambda_min(d),
                "ladder": fp.ladder,
                "ladder_source": fp.ladder_source,
                "max_rel_ladder_error": ladder_errors[d],
            }
            for d, fp in fps.items()
        },
        "spectral_distances": distances,
        "s3_sector_structure": s3_sector_structure(),
        "negative_controls": {
            "NC-A_ipr_shift_invariance_gap": ipr_shift_invariance_gap(),
            "NC-B_random_hermitian_match": random_hermitian_match_score(),
            "NC-C_scalar_vs_dirac": scalar_vs_dirac_same_sphere(),
        },
        "discretization_survival_fd": {
            d: discretization_survival(d) for d in (3, 6)
        },
        "known_limitations": [
            "d=2 lowest sector (kappa=1/2) is the critical limit-circle case: "
            "uniform FD converges only logarithmically (~5% at N=4000, rate h^0.1); "
            "shooting solver used instead [VERIFIED-tool 2026-06-10].",
            "Degeneracy pattern uses ANALYTIC angular factors 2(l+1); only the "
            "sector-membership structure is numerically verified.",
            "Disorder (W>0) not yet tested — fingerprint survival under disorder "
            "is KT-3, out of scope for this proxy.",
            "Radial proxy only: no lattice product S^d x S^1; HA-4 scope gap "
            "(pure-sphere discrimination != original S3xS1 question) remains open.",
        ],
        "status": "research_only — no physical promotion, no gauge-group claim",
    }


def main() -> None:
    result = run_proxy()
    out_path = (
        "experiments/20260610-spinor-geometry-pivot-v0.2.0/proxy_results_v0.2.0.json"
    )
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, default=str)
    print(json.dumps(result, indent=2, default=str))
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
