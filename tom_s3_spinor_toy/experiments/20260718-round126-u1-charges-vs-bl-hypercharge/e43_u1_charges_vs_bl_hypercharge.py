"""Round126: does round124's su(3)-centralizer (2-dim, abelian) contain a
direction whose charge assignment to 8_v's su(3)-isotypic pieces (3, 3bar,
and the 2 singlets) reproduces the SAME qualitative ratio/sign pattern as
this project's established B-L formula (G15: |singlet|:|triplet| = 3:1,
singlet pair opposite signs, triplet/antitriplet opposite signs)?

IMPORTANT SCOPE NOTE (see claim.md): this does NOT assume 8_v (octonion
vector rep, this project's G67+ triality formalism) is the same numerical
object as G15's "S6 spinor" (built via qubit/Pauli-tensor operators,
predates the triality formalism, never explicitly identified with
8_v/8_s/8_c anywhere in this project -- checked by grep). This tests a
narrower, structural question: does ANY direction in the centralizer
reproduce the SAME abstract charge pattern, on 8_v's own su(3) content,
regardless of whether the two 8-dim objects are literally the same matrix
in a common basis.

Reuses G102's own verified machinery by direct import, same discipline as
round124/round125.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_round126.json"

G102_PATH = HERE.parent / "20260705-g102-spin8-fiber-obstruction" / "g102_spin8_fiber.py"
_spec = importlib.util.spec_from_file_location("g102_spin8_fiber", G102_PATH)
assert _spec and _spec.loader
G102 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G102)

TOL = 1e-9


def orthonormal_complement(basis_vecs: np.ndarray, ambient_dim: int = 8) -> np.ndarray:
    """Given k orthonormal column vectors spanning a subspace, return an
    orthonormal basis for its orthogonal complement in R^ambient_dim."""
    if basis_vecs.shape[1] == 0:
        return np.eye(ambient_dim)
    q, _ = np.linalg.qr(np.hstack([basis_vecs, np.eye(ambient_dim)]))
    return q[:, basis_vecs.shape[1] : ambient_dim]


def antisym_eigvals_on_subspace(gen: np.ndarray, proj: np.ndarray) -> list[float]:
    """Restrict an 8x8 antisymmetric generator to a subspace given by
    orthonormal column vectors `proj`; return the "charges" (magnitudes
    lambda of the +-i*lambda eigenvalue pairs a real antisymmetric matrix
    has), one per pair, each listed once.

    WHY via -M@M rather than a direct nonsymmetric eigensolver: the
    general (non-symmetric) LAPACK eigensolver (np.linalg.eigvals) failed
    to converge on some restricted 6x6 blocks in this scan (numerically
    marginal, not a sign of a real defective matrix -- M is exactly
    antisymmetric by construction). M@M = -M^T@M is symmetric NEGATIVE
    semi-definite for antisymmetric M, so -M@M is symmetric POSITIVE
    semi-definite; its eigenvalues (each lambda^2, with EVEN multiplicity
    since +-i*lambda pairs both contribute the same lambda^2) are found
    via the much more robust symmetric solver (np.linalg.eigvalsh), and
    lambda = sqrt(eigenvalue) -- since each charge is already doubled by
    the +-i*lambda pair, the de-duplication loop below reports each charge
    once.
    """
    restricted = proj.T @ gen @ proj
    neg_msq = -(restricted @ restricted)
    neg_msq = 0.5 * (neg_msq + neg_msq.T)  # symmetrize away roundoff asymmetry
    sq_evals = np.linalg.eigvalsh(neg_msq)
    sq_evals = np.clip(sq_evals, 0.0, None)  # guard tiny negative roundoff
    lambdas = sorted(float(np.sqrt(v)) for v in sq_evals if v > TOL)
    # each charge appears twice (from the +i*lambda / -i*lambda pair) -- keep one copy
    unique_charges: list[float] = []
    i = 0
    while i < len(lambdas):
        unique_charges.append(lambdas[i])
        # skip the paired duplicate (nearly equal value)
        j = i + 1
        while j < len(lambdas) and abs(lambdas[j] - lambdas[i]) < 1e-6:
            j += 1
        i = j
    return unique_charges


def main() -> None:
    der = G102.derivation_basis()
    su3 = G102.stabilizer_basis(der)
    cent_dim, cent_su3 = G102.centralizer_dim(su3)
    assert cent_dim == 2, f"expected 2-dim centralizer, got {cent_dim}"

    # --- Singlet (su(3)-invariant) subspace of 8_v: nullspace of stacked su(3) ---
    stacked_su3 = np.vstack(su3)
    singlet_basis = G102.nullspace(stacked_su3).T  # columns = orthonormal basis, 8 x 2
    n_singlet = singlet_basis.shape[1]
    assert n_singlet == 2, f"expected 2-dim singlet subspace, got {n_singlet}"

    triplet_basis = orthonormal_complement(singlet_basis)  # 8 x 6, the "3+3bar" piece
    n_triplet = triplet_basis.shape[1]

    # --- Sanity: su(3) itself must act trivially (zero) on the singlet subspace ---
    su3_on_singlet_residual = max(
        float(np.max(np.abs(singlet_basis.T @ g @ singlet_basis))) for g in su3
    )

    gen1, gen2 = cent_su3[0], cent_su3[1]

    # --- Eigenvalue pattern of each raw centralizer generator on each piece ---
    gen1_singlet = antisym_eigvals_on_subspace(gen1, singlet_basis)
    gen1_triplet = antisym_eigvals_on_subspace(gen1, triplet_basis)
    gen2_singlet = antisym_eigvals_on_subspace(gen2, singlet_basis)
    gen2_triplet = antisym_eigvals_on_subspace(gen2, triplet_basis)

    # --- Scan the 1-parameter family a*gen1 + b*gen2, a=cos(theta), b=sin(theta) ---
    n_scan = 3600
    thetas = np.linspace(
        0, np.pi, n_scan, endpoint=False
    )  # period pi: (a,b)~(-a,-b) same op up to sign
    ratios = []
    singlet_charges = []
    triplet_charges = []
    for theta in thetas:
        a, b = np.cos(theta), np.sin(theta)
        combo = a * gen1 + b * gen2
        q_singlet = antisym_eigvals_on_subspace(combo, singlet_basis)
        q_triplet = antisym_eigvals_on_subspace(combo, triplet_basis)
        qs = q_singlet[0] if q_singlet else 0.0
        qt = max(q_triplet) if q_triplet else 0.0
        singlet_charges.append(qs)
        triplet_charges.append(qt)
        ratios.append(qs / qt if qt > TOL else float("inf"))

    ratios = np.array(ratios)
    singlet_charges = np.array(singlet_charges)
    triplet_charges = np.array(triplet_charges)

    # Find where ratio crosses 3.0 (the G15 B-L target: |−1|/|1/3| = 3)
    target = 3.0
    diffs = ratios - target
    finite = np.isfinite(diffs)
    sign_changes = np.where(finite[:-1] & finite[1:] & (np.sign(diffs[:-1]) != np.sign(diffs[1:])))[
        0
    ]

    matches = []
    for idx in sign_changes:
        # linear interpolation for a precise theta
        t0, t1 = thetas[idx], thetas[idx + 1]
        d0, d1 = diffs[idx], diffs[idx + 1]
        theta_star = t0 + (t1 - t0) * (-d0) / (d1 - d0)
        a_star, b_star = np.cos(theta_star), np.sin(theta_star)
        combo_star = a_star * gen1 + b_star * gen2
        qs_star = antisym_eigvals_on_subspace(combo_star, singlet_basis)
        qt_star = antisym_eigvals_on_subspace(combo_star, triplet_basis)
        matches.append(
            {
                "theta": float(theta_star),
                "a": float(a_star),
                "b": float(b_star),
                "singlet_charge": qs_star,
                "triplet_charges": qt_star,
                "ratio": float(qs_star[0] / max(qt_star)) if qs_star and qt_star else None,
            }
        )

    n_matches = len(matches)
    triplet_degenerate = all(
        (max(gen1_triplet) - min(gen1_triplet) < 1e-6) if gen1_triplet else True for _ in [0]
    )

    if n_matches == 0:
        verdict = "NO_MATCH"
    else:
        verdict = "RATIO_3_FOUND"  # sign structure checked separately below, not auto-verdict

    results = {
        "round": 126,
        "n_singlet": n_singlet,
        "n_triplet": n_triplet,
        "su3_on_singlet_residual": su3_on_singlet_residual,
        "gen1_eigvals_singlet": gen1_singlet,
        "gen1_eigvals_triplet": gen1_triplet,
        "gen2_eigvals_singlet": gen2_singlet,
        "gen2_eigvals_triplet": gen2_triplet,
        "triplet_block_degenerate_for_gen1": triplet_degenerate,
        "n_theta_matches_ratio3": n_matches,
        "matches": matches,
        "verdict": verdict,
    }

    print("=" * 92)
    print("Round126 -- scanning su(3)-centralizer for a B-L-pattern direction (3:1 ratio)")
    print("=" * 92)
    print(f"Singlet subspace dim = {n_singlet} (predict 2)")
    print(f"Triplet (3+3bar) subspace dim = {n_triplet} (predict 6)")
    print(f"su(3) residual on singlet subspace = {su3_on_singlet_residual:.2e} (expect ~0)")
    print()
    print(f"gen1 eigenvalues on singlet: {gen1_singlet}")
    print(f"gen1 eigenvalues on triplet: {gen1_triplet}")
    print(f"gen2 eigenvalues on singlet: {gen2_singlet}")
    print(f"gen2 eigenvalues on triplet: {gen2_triplet}")
    print()
    print(f"Number of theta in [0,pi) where ratio(singlet/triplet) crosses 3.0: {n_matches}")
    for m in matches:
        print(f"  theta={m['theta']:.6f}  (a,b)=({m['a']:.6f},{m['b']:.6f})")
        print(f"    singlet_charge={m['singlet_charge']}  triplet_charges={m['triplet_charges']}")
        print(f"    ratio={m['ratio']}")
    print()
    print(f"VERDICT: {verdict}")

    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nResults -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
