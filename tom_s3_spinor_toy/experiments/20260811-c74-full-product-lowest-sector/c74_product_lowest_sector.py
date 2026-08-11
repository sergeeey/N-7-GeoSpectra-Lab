"""C74 -- full product lowest sector, KT-8-aware framing.

SCOPE, fixed by reading predictions_before_data.md's own P5 description and
an Explore-agent scoping pass before writing any code:

1. This is NOT a re-run of KT-8 (already NULL: dim ker D_{S3xS6}=0 for the
   full 9D product operator) -- the physically relevant object is
   ker(D_S6,twisted) (x) (lowest S3 KK level), not ker(D_full).
2. This does NOT use the t=0/1 torsion-crossing multiplicity trick (already
   shown, C52/C64, to never give a clean factor-of-3 -- crossings kill whole
   (n+1)(n+2)>=2-dim eigenspaces, never a single generation cleanly). The S3
   lowest KK level used here is the natural n=0 mode at the physical
   Levi-Civita connection (t=1/2), reused by citation from round67's own
   closed-form spectrum, not re-derived.
3. Per OB10's documented lesson (docs/clifford_convention_registry.md: never
   trust a Cl(p,q) label, assert both anticommutator signs in-script before
   tensoring), this script explicitly verifies round59's Cl(0,6) generators
   and round67's Cl(0,3) generators share the same anticommutator sign
   (E_k^2 = Z_i^2 = -I) before using them together -- this specific pairing
   has never been checked in this codebase (the OB10 registry only documents
   a DIFFERENT S6 construction, s6-harm-g0, which has the OPPOSITE sign).
4. "Three distinguishable sectors" is explicitly split into two questions,
   per the round-table's own division of labor (predictions_before_data.md):
   C74 (this round) is CONSTRUCTIVE -- build the actual lowest-sector object,
   one copy per triality channel, using C70/C71's own verified intertwiners
   (NOT their tautological monodromy composition -- each intertwiner is used
   ONCE here, independently, not chained). Whether these three constructed
   objects are PHYSICALLY distinguishable (not merely three labeled vector
   spaces, which would be tautologically "distinguishable" and uninformative)
   is explicitly deferred to C75's adversarial observable-distinguishability
   test, not attempted here.

Reuses round59_route_a_independent.py, round67's e2_s3_torsion_deformation.py,
C70's c70_bridge_diagnostics.py, C71 step 1's c71_step1_triality_bridge.py,
and C73's c73_dirac_battery.py unmodified.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c74.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


R59 = load_module(
    "round59_route_a_independent",
    HERE.parent / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py",
)
E2_S3 = load_module(
    "e2_s3_torsion_deformation",
    HERE.parent / "20260717-round67-e2-s3-torsion-deformation" / "e2_s3_torsion_deformation.py",
)
C70 = load_module(
    "c70_bridge_diagnostics",
    HERE.parent
    / "20260811-c70-independent-bridge-fingerprint-and-direct-solve"
    / "c70_bridge_diagnostics.py",
)
C71S1 = load_module(
    "c71_step1_triality_bridge",
    HERE.parent
    / "20260811-c71-triality-bridge-extension-and-mixing-test"
    / "c71_step1_triality_bridge.py",
)
C73 = load_module(
    "c73_dirac_battery",
    HERE.parent / "20260811-c73-round59-real-twisted-dirac-battery" / "c73_dirac_battery.py",
)


def verify_clifford_sign_match() -> dict:
    """OB10 lesson: assert, don't assume. round59's E (Cl(0,6)) and round67's
    Z (Cl(0,3)) must share the same anticommutator sign before being used
    together -- this exact pairing was never checked anywhere in this repo."""
    E = R59.build_clifford(conj=False)
    e_signs = []
    for k in range(1, 7):
        sq = sp.simplify(E[k] * E[k])
        e_signs.append(bool(sq == -sp.eye(8)))

    z_gens = E2_S3.clifford_generators()
    z_signs = []
    for i in range(3):
        sq = sp.simplify(z_gens[i] * z_gens[i])
        z_signs.append(bool(sq == -sp.eye(2)))

    return {
        "round59_E_k_squared_is_minus_I": e_signs,
        "round67_Z_i_squared_is_minus_I": z_signs,
        "all_match_Cl0_convention": all(e_signs) and all(z_signs),
    }


def s3_lowest_kk_level() -> dict:
    """Reused by citation from round67's own closed-form spectrum (not
    re-derived): n=0, Levi-Civita t=1/2, eigenvalues +-3/2 each with
    multiplicity (n+1)(n+2)=2. Explicitly NOT using t=0/1 crossings."""
    h_h = E2_S3.calibrate_h_H()
    levi_civita_t = sp.Rational(1, 2)
    eigenvalues = {}
    for sigma in (1, -1):
        val = E2_S3.eigenvalue_family(0, sigma, levi_civita_t, h_h)
        eigenvalues[str(sigma)] = {"eigenvalue": str(val), "multiplicity": (0 + 1) * (0 + 2)}
    return {
        "n": 0,
        "t_levi_civita": str(levi_civita_t),
        "h_H": str(h_h),
        "eigenvalues_by_sigma": eigenvalues,
        "total_dim_n0_level": sum(row["multiplicity"] for row in eigenvalues.values()),
    }


def get_s6_kernel_vector(E, gens64) -> np.ndarray:
    """The explicit 1-dim kernel vector of D+ (forward map domain_inv(2) ->
    target_inv(1)), reusing C73's own machinery."""
    domain_inv = C73.invariant_basis(gens64, R59.block_global(R59.ODD_IDX, R59.EVEN_IDX))
    d_mat = C73.build_numeric_dirac(E, R59.NOMIZU)
    target_inv = C73.invariant_basis(gens64, R59.block_global(R59.EVEN_IDX, R59.EVEN_IDX))
    forward = target_inv.conj().T @ d_mat @ domain_inv  # 1x2
    _, _, vh = np.linalg.svd(forward)
    kernel_coeffs = vh.conj().T[:, -1]  # nullspace of the rank-1 map (2-dim domain)
    kernel_vec_64 = domain_inv @ kernel_coeffs  # embed into 64-dim Sigma(x)Sigma
    residual = float(np.max(np.abs(d_mat @ kernel_vec_64)))
    return kernel_vec_64, residual


def transport_kernel_to_channels(E, gens64, kernel_vec_64: np.ndarray) -> dict:
    """Construct the explicit lowest-sector vector in EACH triality channel,
    reusing C70/C71's own verified intertwiners -- each used ONCE,
    independently (NOT composed in a cycle, avoiding C71's tautology trap).

    kernel_vec_64 lives in the odd_even bigrading block of Sigma(x)Sigma, but
    C70/C71's U_v/U_s/U_c intertwine the su(3) action on Sigma ALONE (the
    8-dim single-factor space), not Sigma(x)Sigma. The physically meaningful
    object to transport is the FIRST-FACTOR content of the kernel vector
    (the "eta" spinor being twisted), projected out of the 64-dim vector.
    """
    gens_v = C70.C68.su3_g102_on_channel_v()
    gens_s = C71S1.su3_g102_on_channel_s()
    gens_c = C71S1.su3_g102_on_channel_c()

    solve_v = C70.run_direct_solve(
        C70.C68.to_numpy_su3_r59(), gens_v, n_trials=3, norm_weight=5.0, seed=42
    )
    phi_v = solve_v["best"]["phi"]
    phi_inv = np.linalg.inv(phi_v)
    m_matrices = [
        sum(phi_inv[a, k] * C70.C68.to_numpy_su3_r59()[a] for a in range(8)) for k in range(8)
    ]

    results = {}
    for name, gens_target in [("v", gens_v), ("s", gens_s), ("c", gens_c)]:
        basis = C70.C68.hom_basis(m_matrices, gens_target)
        u, best_det = C70.C68.search_nonzero_intertwiner(basis, n_trials=300, seed=0)
        results[name] = {"hom_dim": basis.shape[1], "u_found": u is not None, "u_det": best_det}
        results[name]["u"] = u

    # HEURISTIC STEP, flagged explicitly, not rigorously derived: the kernel
    # vector is a genuinely entangled SU(3)-invariant combination in
    # Sigma_odd (x) Sigma_even, not a simple product state "eta (x) xi". There
    # is no first-principles derivation here for what "the base spinor's own
    # state" should mean given an entangled invariant combination -- summing
    # over the second (twist) factor is ONE natural choice (a marginal), but
    # is NOT shown to be the physically correct extraction. Treat everything
    # downstream of this line as EXPLORATORY, not rigorously established.
    kernel_mat = kernel_vec_64.reshape(8, 8)
    eta_content = kernel_mat.sum(axis=1)  # 8-dim, first-factor marginal -- HEURISTIC

    transported = {}
    for name in ("v", "s", "c"):
        u = results[name]["u"]
        if u is None:
            transported[name] = None
            continue
        w = u @ eta_content
        transported[name] = {
            "norm": float(np.linalg.norm(w)),
            "nonzero": bool(np.linalg.norm(w) > 1e-8),
        }
    return {
        "bridge_results": {
            k: {kk: vv for kk, vv in v.items() if kk != "u"} for k, v in results.items()
        },
        "transported": transported,
    }


def main() -> None:
    print("=== Step 1: Clifford sign-convention check (OB10 lesson) ===")
    sign_check = verify_clifford_sign_match()
    print(sign_check)

    print("\n=== Step 2: S3 lowest KK level (n=0, Levi-Civita, cited from round67) ===")
    s3_level = s3_lowest_kk_level()
    print(s3_level)

    print("\n=== Step 3: explicit S6 kernel vector ===")
    E = R59.build_clifford(conj=False)
    gens64 = C73.su3_gens64(E)
    kernel_vec, kernel_residual = get_s6_kernel_vector(E, gens64)
    print(
        f"kernel vector norm: {np.linalg.norm(kernel_vec):.6f}, "
        f"D@kernel_vec residual: {kernel_residual:.3e}"
    )

    print("\n=== Step 4: transport kernel content to each triality channel ===")
    transport = transport_kernel_to_channels(E, gens64, kernel_vec)
    print(transport)

    n_channels_with_nonzero_content = sum(
        1 for t in transport["transported"].values() if t is not None and t["nonzero"]
    )
    total_lowest_sector_dim = n_channels_with_nonzero_content * 1 * s3_level["total_dim_n0_level"]

    print("\n=== Summary ===")
    print(f"channels with explicit nonzero S6-kernel content: {n_channels_with_nonzero_content}/3")
    print(f"S3 n=0 level dimension (both chiralities): {s3_level['total_dim_n0_level']}")
    print(
        f"candidate total 'lowest sector' dimension "
        f"(channels x S6-kernel-dim x S3-n0-dim): {total_lowest_sector_dim}"
    )
    print(
        "NOTE: this is a CONSTRUCTIVE count, not a distinguishability proof -- "
        "whether the 3 channels' content is PHYSICALLY distinguishable (not "
        "merely three labeled vector spaces) is explicitly deferred to C75."
    )

    results = {
        "clifford_sign_check": sign_check,
        "s3_lowest_kk_level": s3_level,
        "s6_kernel_vector_norm": float(np.linalg.norm(kernel_vec)),
        "s6_kernel_residual": kernel_residual,
        "channel_transport": transport,
        "n_channels_with_nonzero_content": n_channels_with_nonzero_content,
        "candidate_total_lowest_sector_dim": total_lowest_sector_dim,
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
