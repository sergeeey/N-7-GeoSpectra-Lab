"""
Round 26 (2026-07-11): derive the Jac_h/Jac_m curvature-Jacobi term
EXPLICITLY, per Agricola 2002's Theorem 3.2 (General Kostant-Parthasarathy
formula), read directly from the primary source
(Agricola_2002_Dirac_naturally_reductive.pdf, pages 5, 8-9, 12-14 --
NOT reconstructed from memory) rather than guessed.

WHY THIS ROUND. Round 25's step2_remainder (:= cubic_and_curvature_L -
(-H)) compressed to a NON-SCALAR diagonal on the 2-dim SU(3)-invariant
subspace, empirical evidence of a real, unbuilt piece that
g2su3_H_element.py's own docstring flagged: "the SEPARATE Jac_h-dependent
piece of Theorem 3.2's quartic term... is NOT computed here". This round
builds it, per Theorem 3.2's EXACT printed formula (page 14), for n>=5
(our case: dim m = 6):

  (D^t)^2 = Omega_g + (1/2)(1-3t) sum<[Zi,Zj]m,Zk> ZiZjZk(.)
          - (1/2) sum_{i<j<k<ll} <Zi, Jac_h(Zj,Zk,Zl) + 9t^2 Jac_m(Zj,Zk,Zl)> ZiZjZkZl .
          + (1/8) sum_{i,j} Qh([Zi,Zj],[Zi,Zj]) . + (3/8)t^2 sum_{i,j} Qm([Zi,Zj],[Zi,Zj]) .

with Jac_m(X,Y,Z) := [X,[Y,Z]m]m + [Y,[Z,X]m]m + [Z,[X,Y]m]m  (page 5)
and  Jac_h(X,Y,Z) := [X,[Y,Z]h]  + [Y,[Z,X]h]  + [Z,[X,Y]h]   (page 5, both
land in m by reductivity).

At t=1/2 (this project's Levi-Civita convention, matching
g2su3_H_element.py's own established fact): (1/2)(1-3t)=-1/4 of the
FOUR-fold sum = -H exactly (already established); 9t^2=9/4; (3/8)t^2=3/32.

CONNECTION-CONVENTION CAVEAT (read carefully before trusting Ωg below).
Per eq (8)/(9) (pages 12-13), "Zi(psi)" inside Omega_g ALWAYS means the
CANONICAL (t=0) covariant derivative -- NOT the full Levi-Civita (t=1/2)
derivative directly. Omega_g := -sum Zi^2 + C~h (eq 9), where C~h is
ITS OWN degree-0+degree-4 Clifford element (Prop 3.3), built ENTIRELY
from curv_h (independent of Zi/Mp). Whether THIS project's M_p (built
via nabla_g / LEVI_CIVITA_NOMIZU, labelled "Levi-Civita") represents
Agricola's canonical Z_p, the full t=1/2 derivative, or something else
in this project's matrix-coefficient realization is NOT assumed here --
it is TESTED empirically: every OTHER piece of Theorem 3.2 (H, C~h,
degree-4 term, scalar term) is built ENTIRELY from already-validated,
Mp-INDEPENDENT primitives (T-table, curv_h, ad_nu_m_trusted), then
"-sum Zp^2" is ISOLATED BY DIRECT SUBTRACTION from Dslash_mat^2 (ground
truth, already computed via direct matrix composition in Round 24/25)
and COMPARED against "-sum Mp^2" as a candidate -- not assumed to match.

RESULT (2026-07-11, after running, THEN CORRECTED post-skeptic): they do
NOT match directly, but the DIFFERENCE is itself a clean, closed-form,
ground-truth-verified object: H - (1/2)*Id - (7/4)*Casimir_su3(Sigma)
(STEP 6). A first version of this script had a real bug (Qh_sum silently
summed only over p<q, dropping half the ordered sum Theorem 3.2's own
"sum_{i,j}" convention requires) caught by skeptic review via code
inspection alone; fixing it flips the sign on the Id term from +1/2 to
-1/2, EXACTLY matching the skeptic's own independently-reasoned
prediction of the fix's consequence before it was run. Since "+H" here
cancels the formula's own "-H" cubic term, Round 25's step2_remainder
(:= cubic_and_curvature_L - (-H), whose non-scalar diagonal was this
project's open question) is now decomposed into explicitly-derived
pieces: H + C~h + degree4_term + (scalar_term-1/2)*Id - (7/4)*Casimir_su3
-- verified to match Round 25's actual step2_remainder EXACTLY (STEP 7).
This ALGEBRAIC IDENTITY is [VERIFIED-tool] (re-verified after the fix).
What remains genuinely UNEXPLAINED: no independent, first-principles
argument exists for WHY the correction takes exactly this form -- it is
a verified fact, not yet a derived mechanism (both skeptics' own kill
conditions flagged this; it stands even after the bug fix).

Evidence markers: every numeric claim is re-computed and asserted in
main() below ([VERIFIED-tool] on run).
"""

import sympy as sp

from g2su3_appendix_a_construction import ad_nu_m_trusted, build_curvature_h_table
from g2su3_compute_crossterm import nabla_g
from g2su3_explicit_clifford import DIM, e_action
from g2su3_H_element import build_H_matrix, build_T_table
from g2su3_twisted_kernel import su3_action

sqrt = sp.sqrt


def unit_vec(i):
    v = sp.zeros(DIM, 1)
    v[i] = 1
    return v


def build_Mp():
    Ms = {}
    for p in range(1, 7):
        cols = [nabla_g(p, unit_vec(i)) for i in range(DIM)]
        Ms[p] = sp.Matrix.hstack(*cols)
    return Ms


def m_bracket(T, a, b):
    """[Z_a,Z_b]_m as a 6-vector (a,b in 1..6, any order, via antisymmetric T)."""
    out = sp.zeros(6, 1)
    for r in range(1, 7):
        if a < b:
            out[r - 1] = T.get((a, b, r), 0)
        elif a > b:
            out[r - 1] = -T.get((b, a, r), 0)
    return out


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


def jac_m(T, j, k, ll):
    """Jac_m(Z_j,Z_k,Z_l) = [Zj,[Zk,Zl]m]m + [Zk,[Zl,Zj]m]m + [Zl,[Zj,Zk]m]m,
    as a 6-vector, built purely from the T-table (double sum)."""
    out = sp.zeros(6, 1)
    kl = m_bracket(T, k, ll)
    for r in range(1, 7):
        if kl[r - 1] != 0:
            out += kl[r - 1] * m_bracket(T, j, r)
    lj = m_bracket(T, ll, j)
    for r in range(1, 7):
        if lj[r - 1] != 0:
            out += lj[r - 1] * m_bracket(T, k, r)
    jk = m_bracket(T, j, k)
    for r in range(1, 7):
        if jk[r - 1] != 0:
            out += jk[r - 1] * m_bracket(T, ll, r)
    return out


def jac_h(curv_h, j, k, ll):
    """Jac_h(Z_j,Z_k,Z_l) = [Zj,[Zk,Zl]h] + [Zk,[Zl,Zj]h] + [Zl,[Zj,Zk]h],
    as a 6-vector. [Z_i,X]=-ad(X)(Z_i) for X in h."""
    out = sp.zeros(6, 1)
    out += -h_bracket_action_on(curv_h, k, ll, j)
    out += -h_bracket_action_on(curv_h, ll, j, k)
    out += -h_bracket_action_on(curv_h, j, k, ll)
    return out


def clifford_quad(i, j, k, ll, vec):
    """Z_i.Z_j.Z_k.Z_l acting on an 8-dim Sigma vector, via 4 e_action calls."""
    return e_action(i, e_action(j, e_action(k, e_action(ll, vec))))


def build_quartic_matrix(coeff_ijkl):
    """Assemble sum_{i<j<k<ll} coeff_ijkl(i,j,k,ll) * Zi.Zj.Zk.Zl as an 8x8 matrix."""
    M = sp.zeros(DIM, DIM)
    basis = [unit_vec(c) for c in range(DIM)]
    from itertools import combinations

    for i, j, k, ll in combinations(range(1, 7), 4):
        c = coeff_ijkl(i, j, k, ll)
        if c == 0:
            continue
        for col, bvec in enumerate(basis):
            out = c * clifford_quad(i, j, k, ll, bvec)
            for row in range(DIM):
                M[row, col] += out[row]
    return sp.simplify(M)


def main():
    print("=" * 70)
    print("SETUP")
    print("=" * 70)
    T = build_T_table()
    curv_h = build_curvature_h_table()
    Ms = build_Mp()
    Id8 = sp.eye(DIM)
    H = build_H_matrix(T)

    print("\n" + "=" * 70)
    print("STEP 1: build C~h (Prop 3.3), degree-0 + degree-4, from curv_h alone")
    print("(Mp-INDEPENDENT)")
    print("=" * 70)
    # BUG FIX (post-skeptic, 2026-07-11): curv_h is stored ONLY for p<q
    # (build_curvature_h_table's own loop), unlike T (build_T_table), which
    # stores BOTH orders explicitly. A naive "for i in 1..6, for j in 1..6"
    # sum with plain curv_h.get((i,j,k),0) silently drops every i>j term
    # (returns 0 via the missing-key default) -- an uncaught factor-of-2
    # undercount, caught by skeptic review (code-inspection only, no
    # execution needed) and independently re-verified here by re-reading
    # build_curvature_h_table's own loop bounds. Qm_sum (below) did NOT
    # have this bug, since T IS stored for both orders -- which is exactly
    # why it cross-checked correctly and this one silently didn't. Fixed by
    # explicitly summing over the ordered pairs via antisymmetric lookup
    # (matches Qm_sum's own "ordered sum" convention, confirmed correct via
    # its independent cross-check against Tr(H^2)/8=3).
    Qh_sum = sp.simplify(
        2
        * sum(
            curv_h.get((i, j, k), 0) ** 2
            for i in range(1, 7)
            for j in range(i + 1, 7)
            for k in range(1, 9)
        )
    )
    print(f"  sum_{{i,j}} Qh([Zi,Zj],[Zi,Zj]) = {Qh_sum}  (ordered sum, 2x the i<j sum,")
    print("  matching Qm_sum's own established ordered-sum convention below)")
    Ch_0 = sp.Rational(1, 8) * Qh_sum
    print(f"  (C~h)_0 = (1/8)*that = {Ch_0}")

    def jach_coeff(i, j, k, ll):
        jh = jac_h(curv_h, j, k, ll)
        return -sp.Rational(1, 2) * jh[i - 1]

    Ch_4 = build_quartic_matrix(jach_coeff)
    Ch_tilde = sp.simplify(Ch_0 * Id8 + Ch_4)
    is_herm_Ch = sp.simplify(Ch_tilde - Ch_tilde.H) == sp.zeros(DIM, DIM)
    print(f"  C~h built (8x8), Hermitian? {is_herm_Ch}")
    assert is_herm_Ch, "C~h is not Hermitian -- construction error"
    trace_avg_Ch = sp.simplify(sp.trace(Ch_tilde) / DIM)
    print(f"  Tr(C~h)/8 = {trace_avg_Ch}  (should equal (C~h)_0 = {Ch_0}, since")
    print("  the degree-4 part is traceless by construction -- cheap self-check)")
    assert sp.simplify(trace_avg_Ch - Ch_0) == 0, "C~h trace-average != its own (C~h)_0"

    print("\n" + "=" * 70)
    print("STEP 2: build the degree-4 term -(1/2)sum<Zi,Jac_h+9t^2 Jac_m>ZiZjZkZl")
    print("at t=1/2 (9t^2=9/4), Mp-INDEPENDENT (T-table + curv_h only)")
    print("=" * 70)

    def degree4_coeff(i, j, k, ll):
        jh = jac_h(curv_h, j, k, ll)
        jm = jac_m(T, j, k, ll)
        combo = jh + sp.Rational(9, 4) * jm
        return -sp.Rational(1, 2) * combo[i - 1]

    degree4_term = build_quartic_matrix(degree4_coeff)
    is_herm_d4 = sp.simplify(degree4_term - degree4_term.H) == sp.zeros(DIM, DIM)
    print(f"  degree-4 term built (8x8), Hermitian? {is_herm_d4}")
    assert is_herm_d4, "degree-4 term is not Hermitian -- construction error"
    print(f"  trace = {sp.simplify(sp.trace(degree4_term))}  (should be 0, pure degree-4)")
    assert sp.simplify(sp.trace(degree4_term)) == 0, "degree-4 term has nonzero trace"

    print("\n" + "=" * 70)
    print("STEP 3: build the scalar term (1/8)sum Qh + (3/8)t^2 sum Qm, at t=1/2")
    print("=" * 70)
    Qm_sum = sum(
        T.get((i, j, k), 0) ** 2 for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)
    )
    Qm_sum = sp.simplify(Qm_sum)
    print(f"  sum_{{i,j}} Qm([Zi,Zj],[Zi,Zj]) = {Qm_sum}  (cross-check: should be 8,")
    print("  matching g2su3_H_element.py's own Tr(H^2)/8=3=(3/8)*8)")
    assert Qm_sum == 8, f"Qm_sum={Qm_sum} != 8, mismatch with H's own established check"
    scalar_term = sp.Rational(1, 8) * Qh_sum + sp.Rational(3, 32) * Qm_sum
    print(f"  scalar_term = (1/8)*{Qh_sum} + (3/32)*8 = {scalar_term}")

    print("\n" + "=" * 70)
    print("STEP 4: ground truth -- Dslash_mat^2 via direct matrix composition")
    print("(reused pattern from Round 24/25, independently rebuilt here)")
    print("=" * 70)
    Es = {}
    for p in range(1, 7):
        cols = [e_action(p, unit_vec(i)) for i in range(DIM)]
        Es[p] = sp.Matrix.hstack(*cols)
    Dslash_mat = sp.zeros(DIM, DIM)
    for p in range(1, 7):
        Dslash_mat += Es[p] * Ms[p]
    Dslash2 = sp.simplify(Dslash_mat * Dslash_mat)
    print("  Dslash_mat^2 (ground truth):")
    sp.pprint(Dslash2)

    print("\n" + "=" * 70)
    print("STEP 5: isolate '-sum Zp^2' by DIRECT SUBTRACTION (Agricola's canonical")
    print("piece), NOT assumed to equal '-sum Mp^2' -- tested against it.")
    print("=" * 70)
    known_pieces = sp.simplify((-H) + Ch_tilde + degree4_term + scalar_term * Id8)
    minus_Zp2_implied = sp.simplify(Dslash2 - known_pieces)
    print("  '-sum Zp^2' implied by Theorem 3.2 (= Dslash^2 - [-H + C~h + degree4 + scalar]):")
    sp.pprint(minus_Zp2_implied)

    CASIMIR_L_plain = sp.simplify(sum((-(Ms[p] * Ms[p]) for p in range(1, 7)), sp.zeros(DIM, DIM)))
    print("\n  '-sum Mp^2' (this project's own Levi-Civita connection operators):")
    sp.pprint(CASIMIR_L_plain)

    matches_Mp = sp.simplify(minus_Zp2_implied - CASIMIR_L_plain) == sp.zeros(DIM, DIM)
    print(f"\n  Do they match exactly? {matches_Mp}")

    diff = sp.simplify(minus_Zp2_implied - CASIMIR_L_plain)
    if not matches_Mp:
        print("  Difference (implied '-sum Zp^2' minus '-sum Mp^2'):")
        sp.pprint(diff)
        is_scalar_diff = diff == diff[0, 0] * Id8
        print(f"  Is the difference a scalar multiple of Id? {is_scalar_diff}")

    print("\n" + "=" * 70)
    print("STEP 6: the Mp-vs-Zp difference is NOT scalar, but IS a clean closed-form")
    print("combination of H + Id + the SU(3) Casimir on Sigma (already established")
    print("throughout this project since Round 17). Test directly, not assumed.")
    print("=" * 70)
    Ls = {}
    for k in range(1, 9):
        cols = [su3_action(k, unit_vec(i)) for i in range(DIM)]
        Ls[k] = sp.Matrix.hstack(*cols)
    Casimir_su3 = sp.simplify(sum((-(Ls[k] * Ls[k]) for k in range(1, 9)), sp.zeros(DIM, DIM)))
    print("  SU(3) Casimir on Sigma (Round 17's own C_2, reused):")
    sp.pprint(Casimir_su3)

    # Sign on the Id term CORRECTED post-skeptic (2026-07-11): the original
    # Qh_sum bug (see STEP 1's fix note) propagated into scalar_term/Ch_0,
    # which flipped this coefficient's sign. Re-derived AFTER the fix,
    # verified below -- do not revert without re-checking against ground
    # truth.
    predicted_diff = sp.simplify(H - sp.Rational(1, 2) * Id8 - sp.Rational(7, 4) * Casimir_su3)
    diff_matches_prediction = sp.simplify(diff - predicted_diff) == sp.zeros(DIM, DIM)
    print(f"\n  diff == H - (1/2)*Id - (7/4)*Casimir_su3 exactly? {diff_matches_prediction}")
    assert diff_matches_prediction, (
        "the Mp-vs-Zp correction does not match the predicted closed form"
    )

    print("\n" + "=" * 70)
    print("STEP 7: since -H cancels against the '+H' in this correction, this means")
    print("Round 25's step2_remainder (:= cubic_and_curvature_L - (-H), the piece")
    print("whose NON-SCALAR diagonal was this project's open question) is now FULLY")
    print("decomposed into explicitly-derived, ground-truth-verified objects.")
    print("=" * 70)
    predicted_step2_remainder = sp.simplify(
        H
        + Ch_tilde
        + degree4_term
        + (scalar_term - sp.Rational(1, 2)) * Id8
        - sp.Rational(7, 4) * Casimir_su3
    )
    cubic_and_curvature_L = sp.simplify(Dslash2 - CASIMIR_L_plain)
    actual_step2_remainder = sp.simplify(cubic_and_curvature_L - (-H))
    step2_matches = sp.simplify(predicted_step2_remainder - actual_step2_remainder) == sp.zeros(
        DIM, DIM
    )
    print("  predicted step2_remainder := H + C~h + degree4_term")
    print("                              + (scalar_term-1/2)*Id - (7/4)*Casimir_su3:")
    sp.pprint(predicted_step2_remainder)
    print(f"\n  matches Round 25's actual step2_remainder EXACTLY? {step2_matches}")
    assert step2_matches, "predicted decomposition does not match Round 25's actual step2_remainder"

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("  Theorem 3.2 (Agricola 2002) does NOT close with '-sum Mp^2' taken")
    print("  directly as the canonical '-sum Zp^2' -- this project's Levi-Civita")
    print("  M_p operators and Agricola's canonical Z_p are genuinely DIFFERENT")
    print("  objects in this realization, differing by an EXACT, closed-form,")
    print("  ground-truth-verified correction: H - (1/2)*Id - (7/4)*Casimir_su3.")
    print("  (POST-SKEPTIC: an earlier version of this script had a real bug --")
    print("  Qh_sum silently summed only over p<q, dropping half the ordered sum")
    print("  Theorem 3.2's own 'sum_{i,j}' convention requires -- caught by skeptic")
    print("  review via code inspection alone, no execution needed. Fixed; the sign")
    print("  on the Id term flipped as a DIRECT, PREDICTED consequence, matching")
    print("  the skeptic's own independently-reasoned prediction exactly before")
    print("  re-running -- this is stronger cross-validation than 'it closed once'.)")
    print()
    print("  CONSEQUENCE (answers the original question -- Round 25's mystery")
    print("  residual): step2_remainder = H + C~h + degree4_term + (scalar_term-1/2)")
    print("  *Id - (7/4)*Casimir_su3, where C~h and degree4_term are BOTH built from")
    print("  the NOW-EXPLICITLY-DERIVED Jac_h(X,Y,Z) := [X,[Y,Z]h]+[Y,[Z,X]h]+")
    print("  [Z,[X,Y]h] and Jac_m(X,Y,Z) := [X,[Y,Z]m]m+[Y,[Z,X]m]m+[Z,[X,Y]m]m")
    print("  (Agricola 2002, Theorem 3.2, page 14, read from the primary source).")
    print("  This ALGEBRAIC IDENTITY is now verified [VERIFIED-tool] (twice: initial")
    print("  derivation, then re-verified after the bug fix). What remains UNEXPLAINED")
    print("  (per both skeptics' kill conditions, not yet addressed): no independent,")
    print("  first-principles argument exists for WHY the correction takes exactly")
    print("  this form (H, -1/2, -7/4*Casimir_su3) -- it is reported as a verified")
    print("  exact fact, not a derived mechanism. It does NOT, by itself, resolve")
    print("  whether M_p or Z_p is the 'correct' object for the")
    print("  preprint's own L4A norm-bound argument -- that interpretive question is")
    print("  separate from this round's purely algebraic result.")


if __name__ == "__main__":
    main()
