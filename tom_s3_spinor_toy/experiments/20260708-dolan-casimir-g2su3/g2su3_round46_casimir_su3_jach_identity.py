"""
POST-SKEPTIC CORRECTION (2026-07-13): this round is a REDUNDANT
REDISCOVERY of `g2su3_round30_ch_casimir_structural.py` (2026-07-11,
same directory), which already established this exact identity, at
this exact scope, with a stronger structural derivation, through two
independent review passes (FL Step 8a + `/boyko-triangle-audit`). This
script's own `jac_h`/`h_bracket_action_on`/`clifford_quad` functions
are verbatim copies of Round 26's functions -- and Round 30's own STEP
E already imported and ran that exact code at this exact scope. The
"independent primitive sources" framing below is FALSE:
AD_NU_M_BIVECTOR and SU3_GENERATORS are byte-identical (Round 30's own
docstring already disclosed this). See round46_claim.md for the full
correction -- this round adds NO new mathematics; it is kept only as a
harmless, non-load-bearing regression re-check.

Round 46 (2026-07-13): does Casimir_su3 = the operator induced by Jac_h
(Agricola's Prop 3.3 object C~h), EXACTLY, on the FULL 8-dim Sigma --
not fitted, not block-restricted?

WHY THIS ROUND. Round 39's own closed form (step2_remainder =
(5/2)*Id - 2*Casimir_su3 + H) needed Casimir_su3 (built from su3_action,
this project's own su(3) generator representation acting on Sigma,
Round 17's own C_2) as an ingredient. A skeptic review of that round
(Round 39) found a genuine textual clue neither the original claim nor
this project had connected: g2su3_H_element.py's own docstring
explicitly ties Agricola's "Jac_h" term (built from curv_h, the
su(3)/isotropy-bracket structure constants -- literally "su(3)-valued
curvature" per that docstring) to the SAME algebraic family
Casimir_su3 belongs to. Round 39 left this explicitly open ("does NOT
determine whether Casimir_su3 IS or merely resembles Agricola's own
Jac_h term"). This round tests the identity directly, per the user's
own anti-circularity gate (informed by Round 45's own true-kill
lesson): PASS only if the identity is DERIVED FROM DEFINITIONS and
CONFIRMED ON THE FULL 8-DIM MODULE, not fitted on one block or argued
from textual similarity alone.

ANTI-CIRCULARITY PROTOCOL (explicit, per user's own Round 46 gate):
  FORBIDDEN: using coincidence on a single (e.g. 2-dim) block as proof.
  FORBIDDEN: fitting a coefficient to an already-known target matrix.
  FORBIDDEN: treating textual similarity ("both are su(3)-valued") as
    a proof of operator equality.
  REQUIRED: build BOTH operators independently from their OWN
    primitive definitions (Casimir_su3 from su3_action/L_k; C~h/Jac_h
    from curv_h/Round 26's own jac_h+Qh_sum machinery), compare on the
    FULL 8x8 matrix, not a restriction.

WHAT IS BEING COMPARED (precise scope, decided BEFORE computing
anything, to avoid post-hoc redefinition of "the Jac_h operator"):
Agricola 2002's own Proposition 3.3 defines a single Clifford element
C~h := (C~h)_0 * Id + (C~h)_4 (degree-0 scalar piece + degree-4 piece),
built ENTIRELY from curv_h (the [Z_i,Z_j]_h structure constants) via
Qh_sum (the degree-0 part) and Jac_h(Z_j,Z_k,Z_l) (the degree-4 part,
already built and verified in Round 26's own script,
g2su3_round26_jach_derivation.py STEP 1). This C~h IS "the operator
induced by Jac_h" in the sense the user's gate specifies -- it is the
UNIQUE, ALREADY-ESTABLISHED object in this project's own prior work
that Agricola's own Theorem 3.2 built from Jac_h data. Re-derived here
independently (not imported from Round 26's script, to avoid any
accidental shared-state circularity), then compared to Casimir_su3
(independently built from su3_action, unrelated code path).

Evidence markers: every claim is re-computed and asserted in main()
below ([VERIFIED-tool] on run).
"""

from itertools import combinations

import sympy as sp

from g2su3_appendix_a_construction import ad_nu_m_trusted, build_curvature_h_table
from g2su3_explicit_clifford import DIM, e_action
from g2su3_twisted_kernel import su3_action

N64 = DIM * DIM


def unit_vec(i):
    v = sp.zeros(DIM, 1)
    v[i] = 1
    return v


def clifford_quad(i, j, k, ll, vec):
    """Z_i.Z_j.Z_k.Z_l acting on an 8-dim Sigma vector."""
    return e_action(i, e_action(j, e_action(k, e_action(ll, vec))))


def build_quartic_matrix(coeff_ijkl):
    """Assemble sum_{i<j<k<ll} coeff_ijkl(i,j,k,ll) * Zi.Zj.Zk.Zl as an 8x8 matrix."""
    M = sp.zeros(DIM, DIM)
    basis = [unit_vec(c) for c in range(DIM)]
    for i, j, k, ll in combinations(range(1, 7), 4):
        c = coeff_ijkl(i, j, k, ll)
        if c == 0:
            continue
        for col, bvec in enumerate(basis):
            out = c * clifford_quad(i, j, k, ll, bvec)
            for row in range(DIM):
                M[row, col] += out[row]
    return sp.simplify(M)


def h_bracket_action_on(curv_h, a, b, target):
    """ad([Z_a,Z_b]_h)(Z_target), i.e. [[Z_a,Z_b]_h, Z_target]_m, as a 6-vector."""
    out = sp.zeros(6, 1)
    for k in range(1, 9):
        if a < b:
            coeff = curv_h.get((a, b, k), 0)
        elif a > b:
            coeff = -curv_h.get((b, a, k), 0)
        else:
            coeff = 0
        if coeff != 0:
            out += coeff * ad_nu_m_trusted(k, target)
    return out


def jac_h(curv_h, j, k, ll):
    """Jac_h(Z_j,Z_k,Z_l) = [Zj,[Zk,Zl]_h] + [Zk,[Zl,Zj]_h] + [Zl,[Zj,Zk]_h],
    as a 6-vector -- Agricola 2002's own definition (page 5), reused
    identically from Round 26's own construction (independently
    re-derived here from curv_h alone, not imported)."""
    out = sp.zeros(6, 1)
    out += -h_bracket_action_on(curv_h, k, ll, j)
    out += -h_bracket_action_on(curv_h, ll, j, k)
    out += -h_bracket_action_on(curv_h, j, k, ll)
    return out


def main():
    print("=" * 70)
    print("SETUP: build Casimir_su3 (from su3_action) and curv_h (from")
    print("Appendix A) -- two INDEPENDENT primitive sources, no shared state")
    print("=" * 70)
    curv_h = build_curvature_h_table()
    Id8 = sp.eye(DIM)

    Ls = {
        k: sp.Matrix.hstack(*[su3_action(k, unit_vec(i)) for i in range(DIM)]) for k in range(1, 9)
    }
    Casimir_su3 = sp.simplify(sum((-(Ls[k] * Ls[k]) for k in range(1, 9)), sp.zeros(DIM, DIM)))
    print("  Casimir_su3 built from su3_action (Round 17's own C_2):")
    sp.pprint(Casimir_su3)
    print(f"  eigenvalues: {Casimir_su3.eigenvals()}")

    print("\n" + "=" * 70)
    print("STEP 1: build C~h = (C~h)_0 * Id + (C~h)_4 (Agricola 2002 Prop 3.3),")
    print("re-derived independently from curv_h, NOT imported from Round 26")
    print("=" * 70)
    # (C~h)_0: degree-0 scalar part, Qh_sum built as an ORDERED double sum
    # (matches Theorem 3.2's own "sum_{i,j}" convention -- Round 26's own
    # bug-fix lesson: curv_h is stored only for p<q, so an explicit
    # antisymmetric-lookup ordered sum is required, not a naive double loop).
    Qh_sum = sp.simplify(
        2
        * sum(
            curv_h.get((i, j, k), 0) ** 2
            for i in range(1, 7)
            for j in range(i + 1, 7)
            for k in range(1, 9)
        )
    )
    Ch_0 = sp.Rational(1, 8) * Qh_sum
    print(f"  (C~h)_0 = (1/8)*Qh_sum = {Ch_0}")

    def jach_coeff(i, j, k, ll):
        jh = jac_h(curv_h, j, k, ll)
        return -sp.Rational(1, 2) * jh[i - 1]

    Ch_4 = build_quartic_matrix(jach_coeff)
    Ch_tilde = sp.simplify(Ch_0 * Id8 + Ch_4)
    is_herm = sp.simplify(Ch_tilde - Ch_tilde.H) == sp.zeros(DIM, DIM)
    print(f"  C~h built (8x8), Hermitian? {is_herm}")
    assert is_herm, "C~h is not Hermitian -- construction error"
    print("  C~h:")
    sp.pprint(Ch_tilde)
    print(f"  eigenvalues: {Ch_tilde.eigenvals()}")

    print("\n" + "=" * 70)
    print("STEP 2 (the actual test -- FULL 8x8 comparison, no block")
    print("restriction, no fitting): is C~h == Casimir_su3 EXACTLY?")
    print("=" * 70)
    diff = sp.simplify(Ch_tilde - Casimir_su3)
    is_exact_match = diff == sp.zeros(DIM, DIM)
    print(f"  C~h - Casimir_su3 == 0 (all 64 entries)? {is_exact_match}")
    if not is_exact_match:
        print("  Nonzero difference:")
        sp.pprint(diff)
    assert is_exact_match, "C~h != Casimir_su3 -- identity FAILS, hypothesis falsified"

    print("\n" + "=" * 70)
    print("STEP 3 (negative control -- per the user's own PASS/FAIL gate:")
    print("'found at least one vector/block where operators differ' would")
    print("FAIL this. Verify a KNOWN-DIFFERENT pair (Casimir_su3 vs H) does")
    print("NOT match, confirming this test can actually discriminate)")
    print("=" * 70)
    from g2su3_H_element import build_H_matrix, build_T_table

    T = build_T_table()
    H = build_H_matrix(T)
    diff_control = sp.simplify(H - Casimir_su3)
    control_differs = diff_control != sp.zeros(DIM, DIM)
    print("  H != Casimir_su3 (sanity: these are known to be genuinely")
    print(f"  different objects -- degree-3 vs degree-0+4)? {control_differs}")
    assert control_differs, "negative control failed -- H should differ from Casimir_su3"

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("  Casimir_su3 == C~h EXACTLY, all 64 entries, full 8-dim Sigma.")
    print("  POST-SKEPTIC CORRECTION: this is NOT a novel finding -- three")
    print("  independent reviewers (2 skeptics + synthesis) found")
    print("  g2su3_round30_ch_casimir_structural.py (2026-07-11, two days")
    print("  earlier, same directory) ALREADY established this exact")
    print("  identity at this exact scope, with a stronger structural")
    print("  derivation, surviving two review passes. This script's own")
    print("  jac_h/h_bracket_action_on/clifford_quad are verbatim copies of")
    print("  Round 26's functions -- Round 30's own STEP E already ran that")
    print("  exact code. AD_NU_M_BIVECTOR and SU3_GENERATORS are byte-")
    print("  identical (NOT independent sources, contrary to this script's")
    print("  own original docstring claim). See round46_claim.md for the")
    print("  full correction -- this round adds no new mathematics.")


if __name__ == "__main__":
    main()
