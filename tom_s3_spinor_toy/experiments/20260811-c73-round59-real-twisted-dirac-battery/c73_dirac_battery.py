"""C73 -- round59's real twisted D_S6 battery: chirality, scope-clarification,
deformation, negative-control attempts.

PRECISE TARGET (established by reading preprint.tex sec:kernel + round59's own
decision.md, not assumed): the headline "kernel=1" claim is about D restricted
to the SU(3)-INVARIANT sub-blocks specifically -- domain = invariants of
Sigma_odd(x)Sigma_even (dim 2, representing Gamma(S+(x)S-)'s trivial isotype),
target = invariants of Sigma_even(x)Sigma_even (dim 1, representing
Gamma(S-(x)S-)'s trivial isotype). It is NOT the raw kernel of the full 64x64
D (which is much larger and includes physically-irrelevant non-singlet
content) -- this distinction is verified directly below, not assumed, because
an initial naive computation of the raw kernel gave 36, which does not match
"1" until the SU(3)-invariant restriction is applied correctly.

Reuses round59_route_a_independent.py's build_clifford, build_dirac, spin_lift,
ADNU, NOMIZU, EVEN_IDX/ODD_IDX, block_global unmodified.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c73.json"
R59_PATH = (
    HERE.parent / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


R59 = load_module("round59_route_a_independent", R59_PATH)


def build_numeric_dirac(E, nomizu) -> np.ndarray:
    return np.array(R59.build_dirac(E, nomizu).evalf(), dtype=complex)


def invariant_basis(gens64: list[np.ndarray], block_idx: list[int]) -> np.ndarray:
    """SU(3)-invariant subspace within a given 64-dim bigrading block, embedded
    back into the full 64-dim space. Reuses round59's own block_global indexing."""
    dimb = len(block_idx)
    proj = np.zeros((64, dimb), dtype=complex)
    for col, g in enumerate(block_idx):
        proj[g, col] = 1
    stacked = np.vstack([proj.T @ gen @ proj for gen in gens64])
    _, sv, vh = np.linalg.svd(stacked)
    basis = vh.conj().T[:, np.abs(sv) < 1e-8]
    return proj @ basis


def su3_gens64(E) -> list[np.ndarray]:
    su3_ops = [R59.spin_lift(R59.ADNU[a], E) for a in range(1, 9)]
    return [np.array(R59.leibniz(op).evalf(), dtype=complex) for op in su3_ops]


def test_ground_truth_reproduction(E, gens64) -> dict:
    """Positive control: reproduce round59's own certified (a,b,s)=(-1,-sqrt3,4)
    numerically, independent of its sympy exact-arithmetic route."""
    D = build_numeric_dirac(E, R59.NOMIZU)
    domain_inv = invariant_basis(gens64, R59.block_global(R59.ODD_IDX, R59.EVEN_IDX))
    target_inv = invariant_basis(gens64, R59.block_global(R59.EVEN_IDX, R59.EVEN_IDX))
    block = target_inv.conj().T @ D @ domain_inv
    a, b = block[0, 0], block[0, 1]
    s = float(np.sum(np.abs(block) ** 2))
    return {
        "a": complex(a),
        "b": complex(b),
        "s": s,
        "matches_round59": bool(
            abs(abs(a) - 1.0) < 1e-8 and abs(abs(b) - np.sqrt(3)) < 1e-8 and abs(s - 4.0) < 1e-8
        ),
    }


def test_chirality(E, gens64) -> dict:
    """Direct numerical verification of G74B/C21's "purely left-handed" claim
    from round59's OWN matrix (not the abstract dimension-counting argument
    G74B originally used) -- forward map ("D+": domain_inv=2 -> target_inv=1)
    should have rank 1, kernel 1; adjoint map ("D-": target_inv=1 -> domain_inv=2,
    by Hermiticity D=D^dagger) should have rank 1, kernel 0."""
    D = build_numeric_dirac(E, R59.NOMIZU)
    domain_inv = invariant_basis(gens64, R59.block_global(R59.ODD_IDX, R59.EVEN_IDX))
    target_inv = invariant_basis(gens64, R59.block_global(R59.EVEN_IDX, R59.EVEN_IDX))
    forward = target_inv.conj().T @ D @ domain_inv  # "D+", 1x2
    backward = domain_inv.conj().T @ D @ target_inv  # "D-", 2x1 (adjoint by Hermiticity)
    rank_fwd = int(np.sum(np.linalg.svd(forward, compute_uv=False) > 1e-8))
    rank_bwd = int(np.sum(np.linalg.svd(backward, compute_uv=False) > 1e-8))
    return {
        "forward_domain_dim": 2,
        "forward_target_dim": 1,
        "forward_rank": rank_fwd,
        "ker_D_plus": 2 - rank_fwd,
        "backward_domain_dim": 1,
        "backward_target_dim": 2,
        "backward_rank": rank_bwd,
        "ker_D_minus": 1 - rank_bwd,
        "purely_left_handed": (2 - rank_fwd == 1) and (1 - rank_bwd == 0),
        "hermiticity_check_forward_is_adjoint_of_backward": float(
            np.max(np.abs(forward - backward.conj().T))
        ),
    }


def test_scope_clarification(E, gens64) -> dict:
    """The raw, unrestricted kernel of D (all 64 dims, all bigrading sectors,
    all su(3)-isotypic content) is NOT the same quantity as the headline
    "kernel=1" claim -- verified directly, not assumed, because a naive first
    attempt at this round computed the raw kernel and got 36, inconsistent
    with "1" until the su(3)-invariant restriction (tested above) is applied."""
    D = build_numeric_dirac(E, R59.NOMIZU)
    evals = np.linalg.eigvalsh(D)
    raw_kernel_dim = int(np.sum(np.abs(evals) < 1e-8))

    oe = R59.block_global(R59.ODD_IDX, R59.EVEN_IDX)
    ee = R59.block_global(R59.EVEN_IDX, R59.EVEN_IDX)
    d_block = D[np.ix_(ee, oe)]
    block_rank = int(np.sum(np.linalg.svd(d_block, compute_uv=False) > 1e-8))
    block_kernel_dim = 16 - block_rank

    return {
        "raw_64dim_kernel": raw_kernel_dim,
        "full_odd_even_to_even_even_block_kernel": block_kernel_dim,
        "su3_invariant_sector_kernel": 1,
        "note": (
            "raw and full-block kernel counts include non-su(3)-invariant "
            "content, addressed separately by Rounds 52-56's certified "
            "Casimir-difference bound (K_cert=2sqrt(6)/3, cited not "
            "re-derived here) -- NOT independently re-verified in this round"
        ),
    }


def test_structural_parity_check(E, gens64) -> dict:
    """Sanity check on D's own algebraic structure: does D ever connect
    sectors that differ in SECOND-factor Clifford parity? (term1, term2 in
    build_dirac both act via E_i on the FIRST factor only and via bivector-
    built NAB_i, which preserves parity, on whichever factor it touches --
    so D should preserve second-factor parity exactly, an algebraic fact,
    not new physics.)"""
    D = build_numeric_dirac(E, R59.NOMIZU)
    oe = R59.block_global(R59.ODD_IDX, R59.EVEN_IDX)
    oo = R59.block_global(R59.ODD_IDX, R59.ODD_IDX)
    mismatched = D[np.ix_(oo, oe)]
    return {
        "max_abs_D_odd_even_to_odd_odd": float(np.max(np.abs(mismatched))),
        "second_factor_parity_preserved_exactly": bool(np.max(np.abs(mismatched)) < 1e-12),
    }


def test_deformation(E, gens64) -> dict:
    """D is EXACTLY LINEAR in NOMIZU's coefficients (spin_lift is linear in its
    bivector-term argument), so D(t) = t*D(1) for NOMIZU scaled by t. Proven
    algebraically; verified numerically at several t values below (not merely
    asserted). Kernel dimension of the invariant-sector map is therefore
    EXACTLY 1 for all t != 0, degenerating to 2 only at the singular point
    t=0. HONEST LIMITATION: this is a 1-parameter uniform-scale family only --
    no genuinely different admissible S6 connection (e.g. a characteristic
    nearly-Kahler connection distinct from Levi-Civita) exists anywhere in
    this project to test a richer deformation against."""
    domain_inv = invariant_basis(gens64, R59.block_global(R59.ODD_IDX, R59.EVEN_IDX))
    target_inv = invariant_basis(gens64, R59.block_global(R59.EVEN_IDX, R59.EVEN_IDX))
    sweep = {}
    for t in [-1.0, 0.0, 0.5, 0.9, 1.0, 1.1, 1.5, 2.0]:
        nomizu_t = {i: [(t * cf, a, b) for (cf, a, b) in R59.NOMIZU[i]] for i in R59.NOMIZU}
        D_t = build_numeric_dirac(E, nomizu_t)
        block_t = target_inv.conj().T @ D_t @ domain_inv
        b_t = complex(block_t[0, 1])
        rank_t = int(np.sum(np.linalg.svd(block_t, compute_uv=False) > 1e-8))
        calib_ok, _ = R59.run_calibration(E, nomizu_t)
        sweep[str(t)] = {
            "b": b_t,
            "rank": rank_t,
            "kernel_dim": 2 - rank_t,
            "calibration_passes": bool(calib_ok),
        }
    linearity_check = float(abs(complex(sweep["2.0"]["b"]) - 2.0 * complex(sweep["1.0"]["b"])))
    return {"sweep": sweep, "linearity_residual_at_t=2": linearity_check}


def test_negative_control_attempts(E, gens64) -> dict:
    """HONEST report of attempted negative controls -- none of the following,
    all constructed from round59's OWN fixed su(3)-generator/bigrading
    structure, discriminate physical-from-wrong-twist:
    (a) Nomizu sign flip (t=-1): |b| unchanged (just sign-flipped), same rank
        -- NOT a real negative control for kernel structure (only for the
        Killing-spinor calibration sign convention, which round59 already
        knew fails there).
    (b) alternate bigrading pairing even_odd->odd_odd: gives EXACTLY THE SAME
        (a,b)=(-1,-sqrt3) as the physical odd_even->even_even pairing --
        Sigma's even/odd pieces are related by a hidden duality, so this is
        a relabeling of the same physics, not an independent test.
    (c) mismatched-parity pairing odd_even->odd_odd: identically zero, but by
        ALGEBRAIC/STRUCTURAL FORCE (second-factor parity preservation, see
        test_structural_parity_check), not because the twist is "wrong" in
        any physically meaningful sense.
    CONCLUSION: a genuine wrong-twist negative control requires twisting by a
    DIFFERENT representation than Sigma itself -- a new construction, not
    attempted here, honestly left open."""
    D = build_numeric_dirac(E, R59.NOMIZU)

    domain_inv = invariant_basis(gens64, R59.block_global(R59.ODD_IDX, R59.EVEN_IDX))
    target_inv = invariant_basis(gens64, R59.block_global(R59.EVEN_IDX, R59.EVEN_IDX))
    physical = target_inv.conj().T @ D @ domain_inv

    domain_eo = invariant_basis(gens64, R59.block_global(R59.EVEN_IDX, R59.ODD_IDX))
    target_oo = invariant_basis(gens64, R59.block_global(R59.ODD_IDX, R59.ODD_IDX))
    alt_pairing = target_oo.conj().T @ D @ domain_eo

    return {
        "physical_pairing_ab": [complex(physical[0, 0]), complex(physical[0, 1])],
        "alt_pairing_even_odd_to_odd_odd_ab": [
            complex(alt_pairing[0, 0]),
            complex(alt_pairing[0, 1]),
        ],
        "alt_pairing_is_identical_not_independent": bool(
            np.max(np.abs(alt_pairing - physical)) < 1e-8
        ),
        "genuine_wrong_twist_control": "NOT ATTEMPTED -- requires twisting by a "
        "different representation than Sigma, a new construction beyond this round's scope",
    }


def main() -> None:
    E = R59.build_clifford(conj=False)
    gens64 = su3_gens64(E)

    print("=== Ground-truth reproduction (positive control) ===")
    r1 = test_ground_truth_reproduction(E, gens64)
    print(r1)

    print("\n=== Chirality (direct, from round59's own matrix) ===")
    r2 = test_chirality(E, gens64)
    print(r2)

    print("\n=== Scope clarification (raw vs invariant-sector kernel) ===")
    r3 = test_scope_clarification(E, gens64)
    print(r3)

    print("\n=== Structural parity check ===")
    r4 = test_structural_parity_check(E, gens64)
    print(r4)

    print("\n=== Deformation sweep ===")
    r5 = test_deformation(E, gens64)
    for t, row in r5["sweep"].items():
        print(f"  t={t}: {row}")
    print(f"  linearity residual at t=2: {r5['linearity_residual_at_t=2']:.3e}")

    print("\n=== Negative control attempts (honest report) ===")
    r6 = test_negative_control_attempts(E, gens64)
    print(r6)

    results = {
        "ground_truth_reproduction": r1,
        "chirality": r2,
        "scope_clarification": r3,
        "structural_parity_check": r4,
        "deformation": r5,
        "negative_control_attempts": r6,
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
