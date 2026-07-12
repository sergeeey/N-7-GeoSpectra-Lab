"""
Round 36 (2026-07-12): close the gap Round 35 explicitly left open --
"Jm4's own d=2 is NOT derived from a deeper principle here" and
degree4_term's c'=-5/4 is "RELOCATED, not reduced in solve-count."

CORE FINDING: `jac_h(j,k,l) + jac_m(j,k,l) = 0` EXACTLY, for ALL
ordered triples (j,k,l) in 1..6.

ATTRIBUTION CORRECTION (post-skeptic, IMPORTANT -- read before trusting
any "elementary, no citation needed" framing elsewhere in this file):
this identity is NOT a fresh discovery of this round. It is Agricola
2002's OWN theorem, Section 2 (pages 5-6, in the proof leading to Lemma
2.3): "the summands of Jac_h(X,Y,Z) automatically lie in m ... The
Jacobi identity for g implies <Jac_m(X,Y,Z)+Jac_h(X,Y,Z), m> = 0" --
since both are m-valued and their sum is orthogonal to all of m, the
sum is IDENTICALLY ZERO: Jac_h = -Jac_m ALWAYS, for any naturally
reductive space. This EXACT identity was ALREADY found, quoted from the
primary source, and USED in THIS project on 2026-07-09 --
`g2su3_delta_correction.py` (predating Round 26 by two days) builds a
general "quartic_term(t)" directly via H^2 using Jac_h=-Jac_m, and
`decision.md` (~line 525-560, "Round 6") documents the citation and a
non-trivial cross-check (Delta(1/3)=0 exactly, 64/64 entries). This
project's OWN synthesis agent (Round 36 FL Step 8a review, task
`wji4ntu3g`) caught that neither this round's original framing nor
Rounds 26/33/35 (which each independently rebuilt Ch_4/degree4_term/Jm4
via harder combinatorial routes) ever connected back to this
already-on-record shortcut -- a genuine methodology lag, not a new
result. What THIS round genuinely, newly contributes: (a) an
independent RE-DERIVATION of the SAME identity via a cleaner, more
explicit route (the direct-sum decomposition below, which arrives at
the identical conclusion as Agricola's terser remark); (b) the FIRST
APPLICATION of this identity specifically to Ch_4/Jm4/degree4_term as
NAMED, SEPARATE matrix objects (Round 26's own introduction, which
g2su3_delta_correction.py predates and never named).

ABSTRACT ARGUMENT (re-derivation, matching Agricola's own mechanism):
for X,Y,Z in m, the ambient Jacobi identity gives
  0 = sum_cyc [X,[Y,Z]] = sum_cyc [X,[Y,Z]_h] + sum_cyc [X,[Y,Z]_m].
[X,[Y,Z]_h] lies ENTIRELY in m (reductivity: [m,h] subset m, ALREADY
established since Round 12/13 -- ad_nu_m_trusted's very existence IS
this property in action), so sum_cyc [X,[Y,Z]_h] = jac_h(X,Y,Z) exactly
(Round 26's own definition, verified by direct code-level comparison
below). [X,[Y,Z]_m] can have BOTH an m-part and an h-part in general
(this coset is reductive but NOT symmetric -- [m,m] is not confined to
h, precisely the nonzero-torsion/nearly-Kahler feature of
S6=G2/SU(3)); write it as beta(X,Y,Z) [m-part] + gamma(X,Y,Z) [h-part].
Since g=h(+)m is a DIRECT SUM, the total zero vector 0=jac_h+beta+gamma
splits into TWO SEPARATE zero-equations (one per subspace): gamma-sum=0
(an automatic bonus fact, not used further here) AND jac_h+beta=0.
Since beta(X,Y,Z) IS Round 26's own jac_m(X,Y,Z) (m_bracket used twice,
exactly the m-part of [X,[Y,Z]_m] by construction) -- this gives
jac_h+jac_m=0 DIRECTLY, matching Agricola's own (terser) mechanism.

CONSEQUENCES (via LINEARITY of build_quartic_matrix, already
established/used since Round 26 -- verified directly below, not merely
asserted from linearity):

  Jm4 = 2*Ch_4                  EXACTLY (matrix identity)
  degree4_term = -5/4*Ch_4      EXACTLY (matrix identity)

Combined with Round 35's OWN Ch_4=1*(Casimir_su3-Id) (itself a logical
consequence of Round 30's structural chain, NOT re-derived here -- see
Round 35's own honest scope, unaffected by this round):

  Jm4 = 2*(Casimir_su3-Id)              [d=2, matches Round 35 EXACTLY]
  degree4_term = -5/4*(Casimir_su3-Id)  [c'=-5/4, matches Round 26/31/33/35]

THIS SUPERSEDES Round 35's "RELOCATED, not reduced" framing for
degree4_term: there is NO LONGER any separate 3x3 combinatorial solve
needed for Jm4 or degree4_term AT ALL -- both are DIRECT scalar
multiples of Ch_4 via the Jacobi identity alone, and Ch_4's own value
traces ONLY to Round 30's structural chain (unchanged, still the sole
remaining dependency for this whole degree-4 story). Round 33's
original 3x3-solve route to degree4_term's c'=-5/4 remains VALID (an
independent cross-check, both giving the identical value) but is no
longer NECESSARY.

HONEST SCOPE: does NOT re-derive Ch_4's own c=1 (still rests on Round
30's structural chain: Ch_tilde=Casimir_su3 + 2 cited Lie-theory facts
+ one back-solved case, per Round 35's own caveat, untouched here).
Does NOT change any previously-established numeric value from Rounds
4-35 -- Jm4=2*(Casimir_su3-Id) and degree4_term=-5/4*(Casimir_su3-Id)
already matched these exact numbers via Round 35's combinatorial
3x3-solve route; this round provides a SECOND, more direct, solve-free
derivation route to the SAME numbers, not new numbers.
"""

import sympy as sp

from g2su3_appendix_a_construction import build_curvature_h_table
from g2su3_explicit_clifford import DIM
from g2su3_H_element import build_T_table
from g2su3_round26_jach_derivation import build_quartic_matrix, jac_h, jac_m
from g2su3_round28_coefficient_uniqueness import build_swap
from g2su3_twisted_kernel import su3_action

sqrt = sp.sqrt


def unit_vec(i):
    v = sp.zeros(DIM, 1)
    v[i] = 1
    return v


def main():
    print("=" * 70)
    print("SETUP: rebuild T, curv_h, Casimir_su3, Swap, Ch_4, degree4_term")
    print("(all via the ALREADY-established Rounds 26-35 constructions)")
    print("=" * 70)
    T = build_T_table()
    curv_h = build_curvature_h_table()
    Id8 = sp.eye(DIM)

    Ls = {}
    for k in range(1, 9):
        cols = [su3_action(k, unit_vec(i)) for i in range(DIM)]
        Ls[k] = sp.Matrix.hstack(*cols)
    Casimir_su3 = sp.simplify(sum((-(Ls[k] * Ls[k]) for k in range(1, 9)), sp.zeros(DIM, DIM)))
    Swap = build_swap()

    def jach_coeff(i, j, k, ll):
        jh = jac_h(curv_h, j, k, ll)
        return -sp.Rational(1, 2) * jh[i - 1]

    Ch_4 = build_quartic_matrix(jach_coeff)

    def degree4_coeff(i, j, k, ll):
        jh = jac_h(curv_h, j, k, ll)
        jm = jac_m(T, j, k, ll)
        combo = jh + sp.Rational(9, 4) * jm
        return -sp.Rational(1, 2) * combo[i - 1]

    degree4_term = build_quartic_matrix(degree4_coeff)

    def jm_coeff(i, j, k, ll):
        jm = jac_m(T, j, k, ll)
        return jm[i - 1]

    Jm4 = build_quartic_matrix(jm_coeff)

    print("\n" + "=" * 70)
    print("STEP A: verify jac_h(j,k,l) + jac_m(j,k,l) = 0 EXACTLY for THIS")
    print("project's own explicit T/curv_h data -- Agricola 2002's OWN")
    print("theorem (Sec 2, p.5-6), already cited+used pre-Round-26 in")
    print("g2su3_delta_correction.py (2026-07-09) for a DIFFERENT purpose,")
    print("re-verified here as the load-bearing premise for STEPs B-C below")
    print("=" * 70)
    from itertools import combinations, permutations

    ordered_ok = True
    for j, k, ll in combinations(range(1, 7), 3):
        jh = jac_h(curv_h, j, k, ll)
        jm = jac_m(T, j, k, ll)
        if sp.simplify(jh + jm) != sp.zeros(6, 1):
            ordered_ok = False
    print(f"  jac_h+jac_m==0 for all 20 ordered (j<k<l) triples? {ordered_ok}")
    assert ordered_ok, "jac_h+jac_m != 0 -- core finding does not hold"

    all_perms_ok = True
    for j, k, ll in permutations(range(1, 7), 3):
        jh = jac_h(curv_h, j, k, ll)
        jm = jac_m(T, j, k, ll)
        if sp.simplify(jh + jm) != sp.zeros(6, 1):
            all_perms_ok = False
    print(f"  jac_h+jac_m==0 for ALL orderings (120 permutations)? {all_perms_ok}")
    assert all_perms_ok, "jac_h+jac_m != 0 under some permutation"
    print("  => this is the m-component of the AMBIENT Lie algebra's own")
    print("  Jacobi identity (an axiom), decomposed via the reductive split")
    print("  g=h(+)m ([h,m] subset m, already established since Round 12/13)")
    print("  -- matches Agricola 2002's own (terser) mechanism exactly. A")
    print("  general fact for ANY naturally reductive homogeneous space,")
    print("  NOT a fresh discovery of this round -- see docstring's")
    print("  ATTRIBUTION CORRECTION for the full lineage.")

    print("\n" + "=" * 70)
    print("STEP B: DIRECT consequence (via linearity of build_quartic_matrix,")
    print("established/used since Round 26) -- Jm4 = 2*Ch_4 EXACTLY, no 3x3")
    print("solve needed (supersedes Round 35's STEPs E-F for this object)")
    print("=" * 70)
    jm4_eq_2ch4 = sp.simplify(Jm4 - 2 * Ch_4) == sp.zeros(DIM, DIM)
    print(f"  Jm4 == 2*Ch_4 exactly? {jm4_eq_2ch4}")
    assert jm4_eq_2ch4, "Jm4 != 2*Ch_4 -- linearity consequence failed"

    print("\n" + "=" * 70)
    print("STEP C: DIRECT consequence -- degree4_term = -5/4*Ch_4 EXACTLY, no")
    print("3x3 solve needed (supersedes Round 33's original STEP B route for")
    print("this specific object -- that route remains valid as an")
    print("independent cross-check, not required any more)")
    print("=" * 70)
    d4_eq_m54ch4 = sp.simplify(degree4_term - sp.Rational(-5, 4) * Ch_4) == sp.zeros(DIM, DIM)
    print(f"  degree4_term == -5/4*Ch_4 exactly? {d4_eq_m54ch4}")
    assert d4_eq_m54ch4, "degree4_term != -5/4*Ch_4 -- linearity consequence failed"

    print("\n" + "=" * 70)
    print("STEP D: combine with Round 35's OWN Ch_4=Casimir_su3-Id (c=1, a")
    print("logical consequence of Round 30's structural chain -- NOT")
    print("re-derived here, cited unchanged) to get the FULLY closed forms")
    print("=" * 70)
    Ch_4_expected = sp.simplify(Casimir_su3 - Id8)
    ch4_matches = sp.simplify(Ch_4 - Ch_4_expected) == sp.zeros(DIM, DIM)
    print(f"  Ch_4 == Casimir_su3 - Id (Round 35's own result, re-cited)? {ch4_matches}")
    assert ch4_matches, "Round 35's own Ch_4=Casimir_su3-Id result did not reproduce"

    Jm4_closed = sp.simplify(2 * Ch_4_expected)
    jm4_closed_ok = sp.simplify(Jm4 - Jm4_closed) == sp.zeros(DIM, DIM)
    print(f"  Jm4 == 2*(Casimir_su3-Id) exactly (d=2, matches Round 35)? {jm4_closed_ok}")
    assert jm4_closed_ok, "Jm4 does not match the fully-closed form"

    d4_closed = sp.simplify(sp.Rational(-5, 4) * Ch_4_expected)
    d4_closed_ok = sp.simplify(degree4_term - d4_closed) == sp.zeros(DIM, DIM)
    print(
        f"  degree4_term == -5/4*(Casimir_su3-Id) exactly (matches Rounds 26/31/33/35)? {d4_closed_ok}"
    )
    assert d4_closed_ok, "degree4_term does not match the fully-closed form"

    print("\n" + "=" * 70)
    print("STEP E (sanity cross-check): Jm4 and degree4_term still satisfy")
    print("Round 28's theorem premises (equivariance/Swap/Hermiticity),")
    print("consistent with -- but no longer NEEDED to derive -- their values")
    print("=" * 70)
    jm4_equiv_ok = True
    for k in range(1, 9):
        comm = sp.simplify(Ls[k] * Jm4 - Jm4 * Ls[k])
        if comm != sp.zeros(DIM, DIM):
            jm4_equiv_ok = False
    jm4_swap_ok = sp.simplify(Swap * Jm4 * Swap - Jm4) == sp.zeros(DIM, DIM)
    jm4_herm_ok = sp.simplify(Jm4.H - Jm4) == sp.zeros(DIM, DIM)
    print(
        f"  Jm4 SU(3)-equivariant/Swap-symmetric/Hermitian? {jm4_equiv_ok, jm4_swap_ok, jm4_herm_ok}"
    )
    assert jm4_equiv_ok and jm4_swap_ok and jm4_herm_ok, "Jm4 premises failed"

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("  jac_h + jac_m = 0 EXACTLY -- Agricola 2002's OWN theorem (Sec 2,")
    print("  p.5-6), already cited+used in this project pre-Round-26")
    print("  (g2su3_delta_correction.py, 2026-07-09) for a general H^2-based")
    print("  quartic_term(t) formula, but never connected to Ch_4/Jm4/")
    print("  degree4_term as named objects across Rounds 26-35. This round")
    print("  independently re-derives the SAME identity (matching")
    print("  Agricola's own mechanism) and, for the first time, APPLIES it")
    print("  to these specific objects -- a FOUNDATIONAL-STOP fact (general")
    print("  for ANY naturally reductive homogeneous space), NOT a fresh")
    print("  discovery.")
    print()
    print("  CONSEQUENCE: Jm4=2*Ch_4 and degree4_term=-5/4*Ch_4 EXACTLY, by")
    print("  linearity alone -- NO 3x3 combinatorial solve is needed for")
    print("  EITHER object any more. Round 35's 'RELOCATED, not reduced'")
    print("  framing for degree4_term is SUPERSEDED: the solve is now fully")
    print("  ELIMINATED, not merely moved to a cleaner object.")
    print()
    print("  REMAINING DEPENDENCY: the ENTIRE degree-4 story (Ch_4, Jm4,")
    print("  degree4_term) now rests on EXACTLY ONE fact requiring trust")
    print("  beyond elementary Lie theory -- Round 30's own structural chain")
    print("  for Ch_4's own c=1 (2 cited textbook Lie-theory facts + one")
    print("  back-solved case, k=8) -- unchanged, still open, but now")
    print("  ISOLATED as the SOLE remaining gap for this whole story.")


if __name__ == "__main__":
    main()
