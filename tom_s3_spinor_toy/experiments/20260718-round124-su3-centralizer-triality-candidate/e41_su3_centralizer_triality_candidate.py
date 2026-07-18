"""Round124: does su(3) COMBINED WITH its own centralizer in so(8) (a rank-4
algebra su(3)+u(1)+u(1), since su(3) has rank 2) distinguish the three
triality channels 8_v, 8_s, 8_c -- even though su(3) ALONE provably does
not (G102's own Hom_su(3)=6 for all pairs, unchanged and not reopened
here)?

Reuses G102's own verified machinery (octonion table, g2/su(3) bases, the
Cl(0,8)-built v/s/c representations, the centralizer computation, and the
hom_dim intertwiner-space tool) by direct import -- none of it is
re-derived, matching this project's own established reuse discipline
(G102 itself reused G68 the same way).
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_round124.json"

G102_PATH = HERE.parent / "20260705-g102-spin8-fiber-obstruction" / "g102_spin8_fiber.py"
_spec = importlib.util.spec_from_file_location("g102_spin8_fiber", G102_PATH)
assert _spec and _spec.loader
G102 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G102)

TOL = 1e-9


def main() -> None:
    der = G102.derivation_basis()  # g2, 14-dim
    su3 = G102.stabilizer_basis(der)  # su(3), 8-dim (reconfirm dim below)
    n_su3 = len(su3)

    cent_dim, cent_su3 = G102.centralizer_dim(su3)  # c_so(8)(su(3)), predict dim 2
    cent_abelian = G102.is_abelian(cent_su3) if cent_su3 else True

    # Sanity: the centralizer must genuinely commute with su(3) (re-verify directly,
    # not just trust the dimension count from G102's own already-passing S4 check).
    commute_residual = 0.0
    for x in su3:
        for y in cent_su3:
            commute_residual = max(commute_residual, float(np.max(np.abs(x @ y - y @ x))))

    combined = su3 + cent_su3  # su(3) + u(1) + u(1), rank 2+1+1=4, 10 generators total

    # Restrict all three reps (v, s, c) to su(3) ALONE (reproduces G102 S7 as a
    # control -- must match the already-established Hom=6 for all pairs) and to
    # the COMBINED su(3)+centralizer algebra (the new question).
    reps_su3_alone = G102.restrict_to_subalgebra(su3)
    reps_combined = G102.restrict_to_subalgebra(combined)
    labels = ("v", "s", "c")

    hom_su3_alone = {
        f"{la}-{lb}": G102.hom_dim(reps_su3_alone[i], reps_su3_alone[j])
        for i, la in enumerate(labels)
        for j, lb in enumerate(labels)
    }
    hom_combined = {
        f"{la}-{lb}": G102.hom_dim(reps_combined[i], reps_combined[j])
        for i, la in enumerate(labels)
        for j, lb in enumerate(labels)
    }

    # Rank-4-escapes-SO(7) check: does su(3)+centralizer fix ANY nonzero vector in
    # the 8-dim vector representation? (SO(7) = stabilizer of a vector; su(3) alone
    # fixes a 2-dim singlet subspace inside 8_v = 3+3bar+1+1, but if the centralizer
    # rotates that subspace nontrivially, the COMBINED algebra may fix nothing.)
    vec_gens = combined  # these ARE already 8x8 antisymmetric matrices (so(8) elements)
    # nullspace of the stacked map v -> (X_1 v, X_2 v, ...) = common fixed vectors
    stacked_op = np.vstack(vec_gens) if vec_gens else np.zeros((0, 8))
    fixed_vectors = G102.nullspace(stacked_op)
    n_fixed = len(fixed_vectors)

    off_diag_keys = ["v-s", "v-c", "s-c"]
    off_diag_su3_alone = [hom_su3_alone[k] for k in off_diag_keys]
    off_diag_combined = [hom_combined[k] for k in off_diag_keys]

    su3_alone_matches_g102 = all(v == 6 for v in hom_su3_alone.values())
    distinguishes_fully = any(v == 0 for v in off_diag_combined)
    shrinks_partially = (
        any(c < a for c, a in zip(off_diag_combined, off_diag_su3_alone))
        and not distinguishes_fully
    )
    unchanged = off_diag_combined == off_diag_su3_alone

    if distinguishes_fully:
        verdict = "CANDIDATE_FOUND"
    elif shrinks_partially:
        verdict = "PARTIAL"
    elif unchanged:
        verdict = "NULL"
    else:
        verdict = "INCONCLUSIVE"

    results = {
        "round": 124,
        "n_su3_generators": n_su3,
        "centralizer_dim": cent_dim,
        "centralizer_abelian": cent_abelian,
        "commute_residual_su3_vs_centralizer": commute_residual,
        "hom_su3_alone": hom_su3_alone,
        "hom_su3_plus_centralizer": hom_combined,
        "su3_alone_matches_g102_baseline_all6": su3_alone_matches_g102,
        "n_fixed_vectors_in_8v_under_combined_algebra": n_fixed,
        "verdict": verdict,
    }

    print("=" * 92)
    print("Round124 -- su(3) + centralizer as a rank-4 triality-distinguishing candidate")
    print("=" * 92)
    print(f"n_su3_generators = {n_su3} (predict 8)")
    print(f"centralizer_dim  = {cent_dim} (predict 2, from G102 S4)")
    print(f"centralizer_abelian = {cent_abelian}")
    print(f"[su(3), centralizer] commute residual = {commute_residual:.2e} (expect ~0)")
    print()
    print(f"Hom_su(3) ALONE, all pairs        = {hom_su3_alone}")
    print(f"  matches G102 baseline (all 6)?    {su3_alone_matches_g102}")
    print(f"Hom_(su(3)+centralizer), all pairs = {hom_combined}")
    print()
    print(f"Off-diagonal Hom, su(3) alone:     {off_diag_su3_alone}")
    print(f"Off-diagonal Hom, su(3)+centralizer: {off_diag_combined}")
    print()
    print(f"Fixed vectors in 8_v under the combined 10-generator algebra: {n_fixed}")
    print("  (0 would mean the algebra fixes no vector -- escapes confinement to SO(7),")
    print("   the same structural feature that let SO(4)xSO(4) work in round119)")
    print()
    print(f"VERDICT: {verdict}")

    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"\nResults -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
