"""
Round 27 (2026-07-11, CORRECTED post-skeptic -- see below): Dslash_mat
(this project's own S^6-intrinsic twisted Dirac operator, built from
Rounds 14-26's M_p := nabla_g(p,.)) equals EXACTLY -(1/2)*H, Kostant's
cubic torsion element, as OPERATORS (not just their squares). This is a
clean, verified matrix identity that reframes Round 26's "M_p-vs-Zp
correction" derivation. It is a VERIFIED NUMERICAL REALIZATION of a
theoretically-expected identity (Agricola 2002 eq. 5 at t=1/2, combined
with the standard vanishing/non-vanishing structure of the canonical
Dirac operator on nearly-Kahler invariant spinors) -- NOT, as originally
claimed, a "cross-confirmation between two independent sources".

POST-SKEPTIC CORRECTION (2026-07-11): the original version of this file
claimed (a) M_p and H are anchored to two INDEPENDENT published sources
(AHL2023 for M_p vs Agricola 2002 for H), and (b) a sign convention
"H_ours = -H_Agricola" that was used to derive "D^0 = 0". BOTH claims
were WRONG, caught by skeptic review (one skeptic had no execution
access and still found this from code inspection + algebra alone):

(a) M_p and H are NOT independently anchored. `build_T_table` (feeding
    H) is built via `lambda_half`, which uses the SAME LEVI_CIVITA_NOMIZU
    data `nabla_g` (feeding M_p) uses. Both trace back to ONE source
    (AHL2023 page 42's Nomizu map). The "cross-confirmation" framing
    overstated independence and is retracted.

(b) The sign claim did not algebraically close: matching "cubic term =
    -H_ours" (this project's own established fact) against Agricola's
    own "cubic term = -H_Agricola" (her eq. 5 at t=1/2) gives H_ours =
    H_Agricola DIRECTLY -- NOT H_ours = -H_Agricola. Independently
    re-verified via `torsion_T`'s own docstring (`g2su3_H_element.py`):
    "T(i,j,k) = <[Z_i,Z_j]_m,Z_k> = 2*Lambda_m^{1/2}(e_i)e_j.e_k", which
    matches Agricola's own convention (eq. 1, page 4:
    Lambda_m^t(X)(Y):=t[X,Y]_m) with NO sign flip. So H_ours = H_Agricola.

CORRECTED CONSEQUENCE: with H_ours = H_Agricola (not negated), D^t =
D^0 + t*H_Agricola = D^0 + t*H_ours (Agricola eq. 5). At t=1/2:
Dslash_mat = D^0 + (1/2)*H_ours. Given Dslash_mat = -(1/2)*H_ours
(this round's own verified fact), this now gives D^0 = -H_ours -- NOT
zero. This is arguably a CLEANER structural picture than the original
(wrong) "D^0=0" claim: both D^0 and D^{1/2} are proportional to the SAME
H, with coefficients -1 and -1/2 respectively (consistent with the
general pattern D^t = (t-1)*H_ours, which reproduces both endpoints
exactly -- though this general-t formula is NOT independently verified
here beyond the two points t=0,1/2 checked). As before, this is an
ARITHMETIC consequence of Dslash_mat=-H/2 plus Agricola's eq. 5, NOT an
independent geometric derivation of why D^0 takes this value -- that
remains open.

Evidence markers: every numeric claim is re-computed and asserted in
main() below ([VERIFIED-tool] on run).
"""

import sympy as sp

from g2su3_appendix_a_construction import build_curvature_h_table
from g2su3_explicit_clifford import DIM, e_action
from g2su3_H_element import build_H_matrix, build_T_table
from g2su3_round26_jach_derivation import build_Mp, build_quartic_matrix, jac_h, jac_m
from g2su3_twisted_kernel import su3_action

sqrt = sp.sqrt


def unit_vec(i):
    v = sp.zeros(DIM, 1)
    v[i] = 1
    return v


def main():
    print("=" * 70)
    print("SETUP")
    print("=" * 70)
    T = build_T_table()
    curv_h = build_curvature_h_table()
    Ms = build_Mp()
    Id8 = sp.eye(DIM)
    H = build_H_matrix(T)

    Es = {}
    for p in range(1, 7):
        cols = [e_action(p, unit_vec(i)) for i in range(DIM)]
        Es[p] = sp.Matrix.hstack(*cols)
    Dslash_mat = sp.zeros(DIM, DIM)
    for p in range(1, 7):
        Dslash_mat += Es[p] * Ms[p]

    print("\n" + "=" * 70)
    print("STEP 1: Dslash_mat == -H/2 exactly? (direct computation, both sides")
    print("built independently -- Dslash_mat from Es*Ms matrix composition,")
    print("H from the T-table via build_H_matrix -- NO subtraction anywhere)")
    print("=" * 70)
    print("  Dslash_mat:")
    sp.pprint(Dslash_mat)
    print("\n  -H/2:")
    sp.pprint(sp.simplify(-H / 2))
    matches = sp.simplify(Dslash_mat - (-H / 2)) == sp.zeros(DIM, DIM)
    print(f"\n  Dslash_mat == -H/2 exactly? {matches}")
    assert matches, "Dslash_mat != -H/2 -- the headline finding of this round failed to reproduce"

    print("\n" + "=" * 70)
    print("STEP 2: consequence -- Dslash_mat^2 == H^2/4 identically (trivial")
    print("given STEP 1, re-verified directly as an independent sanity check)")
    print("=" * 70)
    Dslash2 = sp.simplify(Dslash_mat * Dslash_mat)
    H2 = sp.simplify(H * H)
    matches2 = sp.simplify(Dslash2 - H2 / 4) == sp.zeros(DIM, DIM)
    print(f"  Dslash_mat^2 == H^2/4 exactly? {matches2}")
    assert matches2, "Dslash_mat^2 != H^2/4 -- inconsistent with STEP 1"

    print("\n" + "=" * 70)
    print("STEP 3: re-derive Round 26's Omega_g and the Mp-vs-Zp correction via")
    print("H alone (Dslash^2 = H^2/4, NOT via Mp-based subtraction) -- a cleaner")
    print("route to the SAME identity, cross-checked against Round 26's result.")
    print("=" * 70)
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

    def jach_coeff(i, j, k, ll):
        jh = jac_h(curv_h, j, k, ll)
        return -sp.Rational(1, 2) * jh[i - 1]

    Ch_4 = build_quartic_matrix(jach_coeff)
    Ch_tilde = sp.simplify(Ch_0 * Id8 + Ch_4)

    def degree4_coeff(i, j, k, ll):
        jh = jac_h(curv_h, j, k, ll)
        jm = jac_m(T, j, k, ll)
        combo = jh + sp.Rational(9, 4) * jm
        return -sp.Rational(1, 2) * combo[i - 1]

    degree4_term = build_quartic_matrix(degree4_coeff)
    Qm_sum = 8
    scalar_term = sp.Rational(1, 8) * Qh_sum + sp.Rational(3, 32) * Qm_sum

    Omega_g_clean = sp.simplify(H2 / 4 + H - degree4_term - scalar_term * Id8)
    print("  Omega_g, derived via H^2/4 + H - degree4_term - scalar_term*Id")
    print("  (NO Mp-based subtraction anywhere in this derivation):")
    sp.pprint(Omega_g_clean)

    minus_Zp2_clean = sp.simplify(Omega_g_clean - Ch_tilde)
    print("\n  '-sum Zp^2' (:= Omega_g - C~h, eq 9's own definition):")
    sp.pprint(minus_Zp2_clean)

    CASIMIR_L_plain = sp.simplify(sum((-(Ms[p] * Ms[p]) for p in range(1, 7)), sp.zeros(DIM, DIM)))
    diff_clean = sp.simplify(minus_Zp2_clean - CASIMIR_L_plain)
    print("\n  diff := '-sum Zp^2' - '-sum Mp^2' (clean route):")
    sp.pprint(diff_clean)

    Ls = {}
    for k in range(1, 9):
        cols = [su3_action(k, unit_vec(i)) for i in range(DIM)]
        Ls[k] = sp.Matrix.hstack(*cols)
    Casimir_su3 = sp.simplify(sum((-(Ls[k] * Ls[k]) for k in range(1, 9)), sp.zeros(DIM, DIM)))
    predicted_diff = sp.simplify(H - sp.Rational(1, 2) * Id8 - sp.Rational(7, 4) * Casimir_su3)
    diff_matches = sp.simplify(diff_clean - predicted_diff) == sp.zeros(DIM, DIM)
    print("\n  matches Round 26's H-(1/2)Id-(7/4)Casimir_su3 exactly (CONSISTENCY")
    print("  REWRITE under STEP 1/2, NOT an independent cross-check -- per skeptic")
    print(f"  review, Route B here is Route A with Dslash^2 -> H^2/4 substituted)? {diff_matches}")
    assert diff_matches, "clean-route diff does not match Round 26's subtraction-route diff"

    print("\n" + "=" * 70)
    print("STEP 4 (CORRECTED post-skeptic): D^0 = -H_ours -- arithmetic")
    print("consequence, checked, NOT geometrically explained")
    print("=" * 70)
    print("  Per Agricola 2002 eq.(5): D^t = D^0 + t*H_Agricola. This project's")
    print("  H_ours = H_Agricola DIRECTLY (no sign flip -- re-verified via")
    print("  torsion_T's own docstring matching Agricola's eq.1 convention exactly;")
    print("  the earlier 'H_ours=-H_Agricola' claim was WRONG, caught by skeptic")
    print("  review). IF Dslash_mat = D^{1/2}_Agricola, then Dslash_mat = D^0 +")
    print("  (1/2)*H_ours. STEP 1 gives Dslash_mat = -(1/2)*H_ours exactly, so:")
    D0_corrected = sp.simplify(Dslash_mat - H / 2)
    d0_matches_negH = sp.simplify(D0_corrected - (-H)) == sp.zeros(DIM, DIM)
    print(f"  D^0 := Dslash_mat - (1/2)*H_ours == -H_ours exactly? {d0_matches_negH}")
    assert d0_matches_negH, "corrected D^0 does not equal -H_ours"
    print("  D^0 = -H_ours (NOT zero as originally, wrongly, claimed). This is an")
    print("  ARITHMETIC consequence of STEP 1 + Agricola's eq.5 with the CORRECTED")
    print("  sign, not an independent construction of D^0 to check against -- WHY")
    print("  the canonical (t=0) operator takes exactly this value remains a")
    print("  genuinely OPEN geometric question, not resolved by this round.")

    print("\n" + "=" * 70)
    print("CONCLUSION (post-skeptic corrected)")
    print("=" * 70)
    print("  VERIFIED matrix identity: Dslash_mat = -H/2 EXACTLY (STEP 1) --")
    print("  Kostant's cubic torsion element, up to a scalar, IS this project's")
    print("  own S^6-intrinsic twisted Dirac operator, built from Rounds 14-26's")
    print("  M_p. This is a VERIFIED NUMERICAL REALIZATION of what Agricola 2002")
    print("  eq.5 + the standard nearly-Kahler Killing-spinor structure predicts --")
    print("  NOT a 'cross-confirmation between independent sources' as originally")
    print("  (wrongly) framed: M_p and H share the SAME LEVI_CIVITA_NOMIZU data")
    print("  source (AHL2023 page 42), retracted per skeptic review.")
    print()
    print("  STEP 3 is a CONSISTENCY REWRITE of Round 26's formula under STEP 1/2")
    print("  (not an independent cross-check, per skeptic review -- Route B is")
    print("  Route A with Dslash^2->H^2/4 substituted).")
    print()
    print("  STEP 4 CORRECTED: D^0 = -H_ours (NOT zero -- the original sign-")
    print("  convention argument was wrong, caught by skeptic review, re-derived")
    print("  correctly here). WHY D^0 takes exactly this value remains a genuinely")
    print("  OPEN geometric question, not resolved by this round.")


if __name__ == "__main__":
    main()
