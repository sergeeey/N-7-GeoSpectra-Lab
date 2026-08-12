"""C90 -- structural analysis of why C79-C89's ENTIRE coupling-postulate
family cannot produce genuine inter-Peter-Weyl-level mixing, and a
verified characterization of what construction WOULD.

Context: an external reviewer proposed assembling C86/C87/C89's
per-level tests into one block-tridiagonal Peter-Weyl Dirac matrix
D_PW (diagonal D_k, off-diagonal T_{k,k+1}) and testing truncation
convergence as K grows. Before building this, a direct check of how
T_k is actually constructed (build_coupling_on_full_level, C86) found
a structural obstruction: T_k is built SEPARATELY for each k, as
I_q (x) I_p (x) Z_i (x) Leibniz(g_i) on level k's own (p,q,r) space.
Different k have genuinely different-dimensional (p,q) ranges, and Z_i
acts as literal IDENTITY on (p,q) -- there is no shared index for a
cross-term T_{k,k+1} to act on. This is not a coding gap; it reflects a
deeper representation-theoretic fact.

THE STRUCTURAL FACT: Z_i and l_{e_i} (round67's Clifford generator and
Meier's orbital generator, the only two building blocks used throughout
C74-C89) are both infinitesimal generators of the group's own left/right
REGULAR representation. Peter-Weyl levels are, by definition, the
ISOTYPIC COMPONENTS of that same representation -- invariant subspaces
under left AND right translation. Any operator built purely from these
generators is therefore NECESSARILY block-diagonal across levels: this
is not a limitation of a specific postulate, it is what "isotypic
component" means. Consequently, C86/C87/C89's per-level tests (each an
isolated eps-sweep on one level's own space) are NOT merely a sample of
what a combined block-tridiagonal D_PW would show -- for THIS coupling
family, the combined matrix, if built honestly, reduces to a direct sum
of exactly the same independent blocks already tested. A truncation-
convergence experiment on it would not add information.

THE VERIFIED ALTERNATIVE: for a genuinely level-bridging operator, one
needs something that is NOT a translation generator -- the natural
candidate is a POINTWISE MULTIPLICATION operator (multiply the S3
wavefunction by a level-1 matrix-coefficient function, e.g. the
fundamental representation's own D^{1/2}_{ab}(g)). By Clebsch-Gordan,
level_k (x) level_1 = level_{k-1} (+) level_k (+) level_{k+1} -- this
DOES connect adjacent levels. This script verifies the CG coefficients
directly via sympy's own exact CG class (not hand-derived) for k=1,2,3,
confirming the coupling is generically nonzero -- i.e. this alternative
construction is mathematically viable, though NOT built to a certified,
usable operator in this round (a substantial, separate undertaking,
named explicitly as the next step, not attempted here).
"""

from __future__ import annotations

import json
from pathlib import Path

from sympy import S
from sympy.physics.quantum.cg import CG

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c90.json"


def verify_translation_generators_are_level_preserving() -> dict:
    """[VERIFIED-by-construction] Confirm, by direct inspection of how T_k
    is built (C86's build_coupling_on_full_level), that it has no defined
    action connecting different k -- a structural, dimensional fact, not
    requiring numerical computation: T_k's domain and codomain are BOTH
    level k's own (p,q,r) space of dimension 2*(k+1)^2, and this dimension
    differs for different k, so "T_k applied to a level k' != k state" is
    not even a well-formed expression without an ad hoc embedding that the
    construction itself never defines."""
    dims = {k: 2 * (k + 1) ** 2 for k in range(5)}
    return {
        "level_dimensions": dims,
        "finding": (
            "T_k is defined on level k's own (p,q,r) space alone (dimension "
            "2*(k+1)^2, different for each k). Z_i acts as literal identity "
            "on (p,q) by construction, so it cannot, even in principle, map "
            "a state's (p,q) content into a different level's (p,q) range. "
            "This holds for l_{e_i} too (Meier's own construction: a "
            "(k+1)-dim matrix acting entirely within level k's own p-index). "
            "Both are infinitesimal generators of the group's own left/right "
            "regular representation; Peter-Weyl levels are the isotypic "
            "components of that same representation, invariant under left "
            "and right translation by definition -- so any operator built "
            "purely from these generators is necessarily block-diagonal "
            "across levels, structurally, not as a limitation of a specific "
            "postulate."
        ),
    }


def verify_multiplication_operator_bridges_levels() -> dict:
    """[VERIFIED-sympy] Confirm, via sympy's own exact Clebsch-Gordan class
    (not hand-derived), that combining Peter-Weyl level k (spin j1=k/2)
    with a level-1 matrix-coefficient multiplication function (spin
    j2=1/2) decomposes into level k+1 (j=j1+1/2) with a GENERICALLY
    NONZERO coefficient, for k=1,2,3 -- confirming a multiplication-type
    operator is mathematically capable of bridging adjacent Peter-Weyl
    levels, unlike Z_i/l_{e_i}."""
    results = {}
    for k in (1, 2, 3):
        j1 = S(k) / 2
        j2 = S(1) / 2
        m1 = j1
        m2 = S(1) / 2
        m = m1 + m2
        j_target = j1 + S(1) / 2
        cg = CG(j1, m1, j2, m2, j_target, m)
        val = cg.doit()
        results[str(k)] = {
            "source_level_k": k,
            "source_level_dim_2j1_plus_1": k + 1,
            "target_level_k_plus_1": k + 1,
            "target_level_dim": k + 2,
            "cg_coefficient": str(val),
            "nonzero": bool(val != 0),
        }
    all_nonzero = all(r["nonzero"] for r in results.values())
    return {"per_k": results, "all_nonzero_k_to_kplus1": all_nonzero}


def main() -> None:
    print("=== Part 1: why Z_i/l_{e_i}-based couplings cannot bridge Peter-Weyl levels ===")
    part1 = verify_translation_generators_are_level_preserving()
    print(part1["finding"])
    print()

    print("=== Part 2: does a multiplication-type operator genuinely bridge levels? ===")
    print("(verified via sympy's own exact Clebsch-Gordan class, k=1,2,3)\n")
    part2 = verify_multiplication_operator_bridges_levels()
    for k, r in part2["per_k"].items():
        print(
            f"  k={k}: level {r['source_level_dim_2j1_plus_1']}-dim -> "
            f"level {r['target_level_dim']}-dim, CG coefficient = {r['cg_coefficient']} "
            f"(nonzero={r['nonzero']})"
        )
    print(f"\nall CG coefficients nonzero (k->k+1, k=1,2,3): {part2['all_nonzero_k_to_kplus1']}")

    verdict = (
        "STRUCTURAL_NOGO_FOR_TRANSLATION_GENERATOR_COUPLINGS__"
        "MULTIPLICATION_OPERATOR_ALTERNATIVE_VERIFIED_VIABLE_NOT_YET_BUILT"
    )
    out = {
        "part1_structural_finding": part1,
        "part2_cg_verification": part2,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")


if __name__ == "__main__":
    main()
