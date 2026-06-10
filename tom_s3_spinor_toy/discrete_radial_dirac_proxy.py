"""E0_DISCRETE_RADIAL_DIRAC_EIGENVALUE_RECOVERY — v0.2.0 pivot, gate E0.

Builds the minimal discrete radial Dirac² operator on the Hopf α-grid and
verifies recovery of the analytic eigenvalues λ_n = n + d/2 (Camporesi-Higuchi)
AND of the verified Phase 2 eigenfunctions `phi_nl_hopf`.

Operator (flat measure, Hopf angle α = θ_geodesic / 2, α ∈ (0, π/2)):

    H_χ u = -(1/4) u'' + V_χ(α) u = λ² u
    V_χ(α) = κ (κ + χ·cos 2α) / sin² 2α,   κ = l + (d-1)/2,  χ = ±1

The two chirality blocks χ = ±1 share the spectrum λ = n + d/2 (n ≥ l) and
host the two radial spinor components [VERIFIED-tool 2026-06-10, cosine
similarity 1.0000000000 at N=4000]:

    χ = -1:  u_n(α) ∝ sin(2α) · φ_{nl}(α)   (upper, = phi_nl_hopf, CH eq 3.25)
    χ = +1:  u_n(α) ∝ sin(2α) · g_{nl}(α)   (lower/partner, mirror of 3.25)

Kill-test (pre-registered): max relative ladder error > 5% at the chosen grid
→ verdict REDESIGN_DISCRETIZATION. Otherwise PASS.

Order of execution: S³ first; generalization (d=6) runs ONLY if S³ passes.
d=2 lowest sector is EXCLUDED from the FD path — κ = 1/2 endpoint coefficient
κ(κ-1) = -1/4 is the critical limit-circle value where uniform FD converges
only logarithmically; see `spectral_fingerprint_proxy.dirac_ladder_shooting`.

Hard constraints honored (recorded in run_e0() output):
- IPR is NOT used as an endpoint anywhere in this module.
- No claim that this resolves the S³×S¹ GEOMETRY_AGNOSTIC verdict: HA-4 OPEN.
- No physical promotion: research_only.
- tom_ansatz → phi_11 is recorded as a RADIAL PROJECTION finding only,
  not a full spinor identification (angular sector unverified).
"""

from __future__ import annotations

import json

import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.special import eval_jacobi

from tom_s3_spinor_toy.geometry_s3_hopf import weighted_inner_product
from tom_s3_spinor_toy.reference_spinor_harmonics import phi_nl_hopf

KILL_TEST_REL_TOL = 0.05  # pre-registered: above this → REDESIGN_DISCRETIZATION


# ---------------------------------------------------------------------------
# Partner radial component — Camporesi-Higuchi eq 3.27 (VERIFIED_FROM_PDF)
# ---------------------------------------------------------------------------

def g_nl_hopf(n: int, l: int, alpha: np.ndarray) -> np.ndarray:
    """Lower/partner radial Dirac component on S³ (unnormalized).

        g_{nl}(α) = sinα^{l+1} · cosα^l · P^{(l+3/2, l+1/2)}_{n-l}(cos 2α)

    VERIFIED_FROM_PDF 2026-06-10: this IS Camporesi-Higuchi eq 3.27 with
    α = θ/2, N = 3 (references/camporesi_higuchi_grqc9505009.pdf).
    Mirror identity eq 3.28: g_nl(α) = (−1)^{n−l} φ_nl(π/2 − α).
    Coupled to phi_nl_hopf by the first-order system eqs 3.29-3.30.
    See experiments/.../source_register_av2.md and
    tests/test_ch_first_order_system.py.
    """
    if n < l or l < 0:
        raise ValueError(f"Require n ≥ l ≥ 0, got n={n}, l={l}")
    jac = eval_jacobi(n - l, l + 1.5, l + 0.5, np.cos(2.0 * alpha))
    return (np.sin(alpha) ** (l + 1)) * (np.cos(alpha) ** l) * jac


# ---------------------------------------------------------------------------
# Discrete operator on the α-grid
# ---------------------------------------------------------------------------

def dirac_sq_alpha_tridiag(
    d: int, l_sector: int, n_grid: int, chirality: int = -1
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Tridiagonal FD form of H_χ on interior α-nodes, Dirichlet BCs.

    Returns (diag, offdiag, alpha_grid); h = (π/2)/n_grid.
    """
    if chirality not in (-1, +1):
        raise ValueError("chirality must be ±1")
    kappa = l_sector + (d - 1) / 2.0
    h = (np.pi / 2.0) / n_grid
    alpha = h * np.arange(1, n_grid)
    pot = kappa * (kappa + chirality * np.cos(2 * alpha)) / np.sin(2 * alpha) ** 2
    diag = 2.0 / (4.0 * h**2) + pot
    off = -np.ones(n_grid - 2) / (4.0 * h**2)
    return diag, off, alpha


def recover_ladder(
    d: int,
    l_sector: int = 0,
    n_grid: int = 4000,
    n_levels: int = 5,
    chirality: int = -1,
    return_vectors: bool = False,
):
    """Lowest |λ| ladder (and optionally eigenvectors) of the discrete H_χ."""
    diag, off, alpha = dirac_sq_alpha_tridiag(d, l_sector, n_grid, chirality)
    if return_vectors:
        vals, vecs = eigh_tridiagonal(
            diag, off, select="i", select_range=(0, n_levels - 1)
        )
        return np.sqrt(np.abs(vals)), vecs, alpha
    vals = eigh_tridiagonal(
        diag, off, select="i", select_range=(0, n_levels - 1), eigvals_only=True
    )
    return np.sqrt(np.abs(vals))


# ---------------------------------------------------------------------------
# Eigenvector correspondence with verified Phase 2 reference functions
# ---------------------------------------------------------------------------

def eigenvector_correspondence_s3(
    n_grid: int = 4000, n_levels: int = 3, l_sector: int = 0
) -> dict[str, list[float]]:
    """Cosine similarity of discrete eigenvectors vs analytic components.

    χ = -1 block ↔ sin(2α)·phi_nl_hopf (VERIFIED Phase 2 reference),
    χ = +1 block ↔ sin(2α)·g_nl_hopf (partner).
    """
    out: dict[str, list[float]] = {"chi_minus_vs_phi_nl": [], "chi_plus_vs_g_nl": []}
    for chirality, ref_fn, key in (
        (-1, phi_nl_hopf, "chi_minus_vs_phi_nl"),
        (+1, g_nl_hopf, "chi_plus_vs_g_nl"),
    ):
        _, vecs, alpha = recover_ladder(
            3, l_sector, n_grid, n_levels, chirality, return_vectors=True
        )
        for i in range(n_levels):
            n = l_sector + i
            ref = np.sin(2 * alpha) * ref_fn(n, l_sector, alpha)
            cos = abs(vecs[:, i] @ ref) / (
                np.linalg.norm(vecs[:, i]) * np.linalg.norm(ref)
            )
            out[key].append(float(cos))
    return out


# ---------------------------------------------------------------------------
# Kill-test and E0 orchestration
# ---------------------------------------------------------------------------

def kill_test(d: int, n_grid: int = 4000, n_levels: int = 5) -> dict[str, object]:
    """Pre-registered kill-test: ladder error vs λ = n + d/2.

    Verdict REDESIGN_DISCRETIZATION if max relative error > 5%.
    """
    ladder = recover_ladder(d, 0, n_grid, n_levels)
    target = np.array([n + d / 2.0 for n in range(n_levels)])
    max_rel_err = float(np.max(np.abs(ladder - target) / target))
    return {
        "d": d,
        "n_grid": n_grid,
        "ladder_computed": [float(x) for x in ladder],
        "ladder_analytic": [float(x) for x in target],
        "max_rel_err": max_rel_err,
        "threshold": KILL_TEST_REL_TOL,
        "verdict": "PASS" if max_rel_err <= KILL_TEST_REL_TOL else "REDESIGN_DISCRETIZATION",
    }


def tom_ansatz_radial_projection(
    n_alpha: int = 500, n_max: int = 4
) -> dict[str, object]:
    """RADIAL PROJECTION FINDING (not a full spinor identification).

    tom_ansatz √sin(2α) projects dominantly onto phi_{11} under the weighted
    radial inner product. The angular sector of the ansatz is NOT verified —
    this is a statement about radial profiles only.
    """
    alpha = np.linspace(0.01, np.pi / 2 - 0.01, n_alpha)
    f = np.sqrt(np.sin(2.0 * alpha))
    f_norm2 = weighted_inner_product(f, f, alpha)
    best: tuple[float, int, int] = (0.0, -1, -1)
    table: dict[str, float] = {}
    for n in range(1, n_max + 1):
        for l in range(n + 1):
            phi = phi_nl_hopf(n, l, alpha)
            proj = weighted_inner_product(f, phi, alpha) ** 2 / (
                weighted_inner_product(phi, phi, alpha) * f_norm2
            )
            table[f"phi_{n}{l}"] = float(proj)
            if proj > best[0]:
                best = (float(proj), n, l)
    return {
        "status": "RADIAL_PROJECTION_FINDING_ONLY — angular sector unverified, "
        "NOT a full spinor identification",
        "dominant_mode": {"n": best[1], "l": best[2], "projection": best[0]},
        "projection_table": table,
    }


def run_e0(n_grid: int = 4000) -> dict[str, object]:
    """E0 gate: S³ first; generalize to d=6 only if S³ passes. d=2 excluded."""
    s3 = kill_test(3, n_grid=n_grid)
    s3["eigenvector_correspondence"] = eigenvector_correspondence_s3(n_grid)
    s3["chirality_spectra_identical"] = bool(
        np.allclose(
            recover_ladder(3, 0, n_grid, 5, chirality=-1),
            recover_ladder(3, 0, n_grid, 5, chirality=+1),
            atol=1e-6,
        )
    )

    generalization: dict[str, object] = {}
    if s3["verdict"] == "PASS":
        generalization["d6"] = kill_test(6, n_grid=n_grid)
        generalization["d2"] = (
            "EXCLUDED_FROM_FD — κ=1/2 endpoint coefficient κ(κ-1)=-1/4 is the "
            "critical limit-circle value (uniform FD rate ~h^0.1, ~5% error even "
            "at N=32000); use spectral_fingerprint_proxy.dirac_ladder_shooting "
            "[VERIFIED-tool 2026-06-10]."
        )
    else:
        generalization["skipped"] = "S3 kill-test failed — generalization not run"

    return {
        "experiment": "E0_DISCRETE_RADIAL_DIRAC_EIGENVALUE_RECOVERY",
        "version": "v0.2.0",
        "primary_endpoint": "spectral (eigenvalue ladder + eigenvector "
        "correspondence); IPR not used",
        "s3": s3,
        "generalization": generalization,
        "findings": {"tom_ansatz": tom_ansatz_radial_projection()},
        "scope": {
            "HA-4": "OPEN — pure-sphere ladder recovery does not address the "
            "original S3xS1 GEOMETRY_AGNOSTIC verdict",
            "promotion": "NONE — research_only",
            "disorder": "W>0 untested (KT-3 pending)",
        },
    }


def main() -> None:
    result = run_e0()
    out_path = (
        "experiments/20260610-spinor-geometry-pivot-v0.2.0/"
        "e0_discrete_radial_dirac_results.json"
    )
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, default=str)
    print(json.dumps(result, indent=2, default=str))
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
