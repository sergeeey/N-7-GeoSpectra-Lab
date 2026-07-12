"""
Round 45 (2026-07-12): blind derivation test -- is the trace-free
residual K:=[[0,4/3],[4,0]] of Delta_2x2 exactly the STANDARD
Leibniz/torsion cross-term that MUST appear when correctly squaring
the twisted Dirac operator D64 on a naturally-reductive (nonzero-
bracket) frame -- derived WITHOUT using K as input, per the user's own
anti-circularity protocol?

WHY THIS ROUND. Round 24 originally framed the open question as: is
Delta's trace-free residual K (i) a frame/Leibniz correction the naive
3-term Weitzenboeck form doesn't capture, or (ii) evidence F_{S^-} is
incomplete? Rounds 25-44 pursued (i) indirectly via "is there a
DIFFERENT connection (Z_p) whose bivector spin-lift changes things" --
Round 43/44 closed THAT specific avenue (no bivector-type connection
swap can ever help, and Agricola's own Z_i was never meant as such a
connection anyway). This round asks the DIRECT, previously-untested
version of (i): using the CURRENT, already-correct connection (M_p),
is K explained by the Leibniz-rule cross-terms that MUST appear when
you correctly expand (Sum e_i . N_i)^2 on a frame with [e_p,e_q]!=0 --
derived from the frame/connection data alone, compared to K only at
the end, never used as a fitting target.

ANTI-CIRCULARITY PROTOCOL (user's explicit requirement, honored here):
  FORBIDDEN: building any term as K := Delta - (5/2)*Id (circular).
  FORBIDDEN: solving coefficients to match K, or fitting signs after
    comparison.
  REQUIRED: derive the candidate correction PURELY from (a) the Nomizu
    coefficients (the T-table, curv_h), (b) the connection's action on
    BOTH tensor factors (Leibniz rule), (c) verified structural facts
    about D64's OWN definition -- established BEFORE any comparison to
    K is made.

GROUNDING (done this round, before writing this script, via direct
Read of prior source): `D_on_simple_tensor` (g2su3_compute_crossterm.py,
this project's OWN, several-rounds-old definition of D64) is, verbatim:
    term1: (e_i . nabla_{e_i} eta) (x) xi
    term2: (e_i . eta) (x) (nabla_{e_i} xi)
summed over i=1..6. In matrix form this is EXACTLY
    D64 = Sum_i (e_i (x) Id) . N_i,   N_i := M_i(x)Id + Id(x)M_i
-- i.e. D64 is the STANDARD, textbook Leibniz-rule twisted Dirac
operator (Clifford multiplication on the LEFT factor only -- the usual
convention when the RIGHT factor is treated as an auxiliary twisting
bundle -- composed with the FULL two-factor Leibniz connection N_i).
POST-SKEPTIC CORRECTION (citation fix): the D64==TERM1+TERM2 ground-
truth check against `build_D_matrix64` (g2su3_equivariance_check.py)
lives in g2su3_Sminus_weitzenbock.py (STEP B0b), NOT in
g2su3_round25_K_derivation.py as an earlier version of this docstring
mis-cited (grep-confirmed by FL Step 8a skeptic review). STEP 1 below
independently re-derives the SAME identity, but per that same review,
this is a content-free Kronecker mixed-product identity
((A(x)I)(B(x)I)=(AB)(x)I, (A(x)I)(I(x)B)=A(x)B) true for ANY matrices
substituted for Es/Ms -- it confirms D64 matches the Leibniz-formula
TEMPLATE, not that the specific geometry is correct. It cannot fail
regardless of physics content -- NOT "the load-bearing... highest
failure risk" step this docstring originally claimed.

POST-SKEPTIC MAJOR CORRECTION (2026-07-13): this round's central
conclusion -- that STEP 5's K-match discriminates fork (i) [Leibniz
correction] from fork (ii) [F_Sminus incomplete] -- is FALSIFIED. Two
independent skeptics + a synthesis agent, all working independently,
proved via ARBITRARY SYMBOLIC MATRIX SUBSTITUTION that UNTWISTED's own
kron(X,Id8) form has EXACTLY ZERO off-diagonal on span(w_a,w_b) for
ANY X whatsoever (w_a, w_b have disjoint index support in BOTH tensor
factors, not just one) -- so, given the pre-existing identity
Delta=UNTWISTED+TWISTING_SPECIFIC (Round 41), STEP 5's K-match was
FORCED regardless of whether TWISTING_SPECIFIC's content is correct
physics or not. A genuinely missing F_Sminus term would ALSO be a
two-factor-mixing operator and would land in TWISTING_SPECIFIC just as
cleanly. The test has zero power to discriminate the two forks. See
round45_claim.md's Skeptic Verdict for the full determination. What
SURVIVES: Round 41's 5-piece decomposition, re-verified here via an
independent route (STEPS 2-4), and D64's match to the Leibniz-formula
template (STEP 1, informativeness downgraded). Verdict: REJECT for the
discriminating claim; Round 24's fork (i) vs (ii) question remains open.

Given D64 is confirmed the correctly-built twisted Dirac operator, the
non-circular grouping criterion for "genuine Leibniz/twisting
correction" vs "untwisted single-copy remainder" is fixed BEFORE any
comparison to K:
  UNTWISTED = piece_H + piece_step2_rem = kron(cubic_and_curvature_L,
    Id8), where cubic_and_curvature_L := Dslash_mat^2 - Sum M_p^2 is
    computed ENTIRELY on the untwisted single copy of Sigma (Round 39's
    own closed form) -- i.e. "the answer if you ignored twisting
    entirely, embedded trivially into the twisted space." This is well-
    defined and computable with ZERO reference to K, T12, T21,
    TORSION_E, or cross_casimir.
  TWISTING-SPECIFIC = everything else that appears when you correctly
    expand D64^2 - nabla*nabla - F_Sminus and it is NOT already
    captured by UNTWISTED: (T12+T21) + TORSION_E + cross_casimir.
    These three pieces exist ONLY because D64 = TERM1_mat + TERM2_mat
    has a genuine TERM2_mat contribution (the connection acting on the
    RIGHT factor) -- if D64 were naively Dslash_mat(x)Id (untwisted,
    TERM2_mat=0), these three pieces would not exist at all. Their
    EXISTENCE is forced by D64's own, already-verified, textbook
    Leibniz-rule structure -- not invented to explain K.

Evidence markers: every claim is re-computed and asserted in main()
below ([VERIFIED-tool] on run).
"""

import sympy as sp

from g2su3_H_element import build_T_table
from g2su3_appendix_a_construction import build_curvature_h_table
from g2su3_compute_crossterm import nabla_g
from g2su3_explicit_clifford import DIM, e_action
from g2su3_twisted_kernel import su3_action
from g2su3_Sminus_weitzenbock import curvature_R, nabla_bracket

N64 = DIM * DIM


def idx64(a, b):
    return DIM * a + b


def unit_vec(i):
    v = sp.zeros(DIM, 1)
    v[i] = 1
    return v


def kron(A, B):
    return sp.Matrix(sp.kronecker_product(A, B))


def compress_2x2(op64, w_a, w_b):
    """Matrix of op64 restricted to span(w_a,w_b) in the basis {w_a,w_b}
    (orthogonal, Gram=diag(3,1)): entry [i,j] = coefficient of basis
    vector i in op64(basis vector j), i.e. (op64 . v_j).v_i / (v_i.v_i)."""
    a2 = sp.simplify((op64 * w_a).dot(w_a) / 3)  # [0,0]: w_a-component of M(w_a)
    b2 = sp.simplify((op64 * w_b).dot(w_a) / 3)  # [0,1]: w_a-component of M(w_b)
    c2 = sp.simplify((op64 * w_a).dot(w_b))  # [1,0]: w_b-component of M(w_a), ||w_b||^2=1
    d2 = sp.simplify((op64 * w_b).dot(w_b))  # [1,1]: w_b-component of M(w_b)
    return sp.Matrix([[a2, b2], [c2, d2]])


def main():
    print("=" * 70)
    print("SETUP: build all primitives (M_p, E_p, T-table, curv_h) -- reused,")
    print("not re-derived, from Rounds 17-39's own established constructions")
    print("=" * 70)
    T = build_T_table()
    curv_h = build_curvature_h_table()
    Id8 = sp.eye(DIM)

    Ms = {p: sp.Matrix.hstack(*[nabla_g(p, unit_vec(i)) for i in range(DIM)]) for p in range(1, 7)}
    Es = {p: sp.Matrix.hstack(*[e_action(p, unit_vec(i)) for i in range(DIM)]) for p in range(1, 7)}
    Ls = {
        k: sp.Matrix.hstack(*[su3_action(k, unit_vec(i)) for i in range(DIM)]) for k in range(1, 9)
    }

    print("\n" + "=" * 70)
    print("STEP 1 (the load-bearing structural check): D64 IS EXACTLY the")
    print("textbook Leibniz-rule twisted Dirac operator sum_i (e_i(x)Id).N_i")
    print("-- not merely 'reconstructs D64' (Round 25's own check), but IS")
    print("this formula, verified independently here, BEFORE any reference")
    print("to K, Delta, or the L4A tension.")
    print("=" * 70)
    Dslash_mat = sp.zeros(DIM, DIM)
    for p in range(1, 7):
        Dslash_mat += Es[p] * Ms[p]
    TERM1_mat = kron(Dslash_mat, Id8)
    TERM2_mat = sp.zeros(N64, N64)
    for p in range(1, 7):
        TERM2_mat += kron(Es[p], Ms[p])
    D64_leibniz = sp.simplify(TERM1_mat + TERM2_mat)

    Np = {p: kron(Ms[p], Id8) + kron(Id8, Ms[p]) for p in range(1, 7)}
    D64_from_Np = sp.zeros(N64, N64)
    for p in range(1, 7):
        D64_from_Np += kron(Es[p], Id8) * Np[p]
    D64_from_Np = sp.simplify(D64_from_Np)
    matches = sp.simplify(D64_leibniz - D64_from_Np) == sp.zeros(N64, N64)
    print(f"  TERM1_mat+TERM2_mat == sum_i kron(e_i,Id)*N_i exactly? {matches}")
    assert matches, (
        "D64 does NOT match the textbook Leibniz-rule formula -- structural assumption broken"
    )
    print("  (This confirms D64's own definition IS the standard twisted Dirac")
    print("  operator -- Clifford mult on left factor, full 2-factor Leibniz")
    print("  connection N_p. T12/T21/TORSION_E/cross_casimir below are NECESSARY")
    print("  consequences of squaring THIS, not invented corrections.)")

    print("\n" + "=" * 70)
    print("STEP 2: build the UNTWISTED single-copy remainder (Round 39's own")
    print("closed form), computable with ZERO reference to K or twisting terms")
    print("=" * 70)
    Dslash2 = sp.simplify(Dslash_mat * Dslash_mat)
    CASIMIR_L_plain = sp.simplify(sum((-(Ms[p] * Ms[p]) for p in range(1, 7)), sp.zeros(DIM, DIM)))
    cubic_and_curvature_L = sp.simplify(Dslash2 - CASIMIR_L_plain)
    Casimir_su3 = sp.simplify(sum((-(Ls[k] * Ls[k]) for k in range(1, 9)), sp.zeros(DIM, DIM)))
    expected_untwisted = sp.simplify(sp.Rational(5, 2) * Id8 - 2 * Casimir_su3)
    assert sp.simplify(cubic_and_curvature_L - expected_untwisted) == sp.zeros(DIM, DIM), (
        "untwisted remainder does not match Round 39's own closed form -- primitives changed?"
    )
    UNTWISTED_64 = kron(cubic_and_curvature_L, Id8)
    print("  UNTWISTED := kron(Dslash_mat^2 - sum M_p^2, Id8), matches Round 39's")
    print("  own (5/2)Id-2*Casimir_su3 closed form exactly? True (asserted)")

    print("\n" + "=" * 70)
    print("STEP 3: build the TWISTING-SPECIFIC cross-terms (T12+T21, TORSION_E,")
    print("cross_casimir) -- these exist ONLY because TERM2_mat != 0 (STEP 1),")
    print("i.e. they are forced by D64's own already-verified Leibniz structure,")
    print("built purely from frame/Nomizu/curvature data, no reference to K")
    print("=" * 70)
    T12 = sp.simplify(TERM1_mat * TERM2_mat)
    T21 = sp.simplify(TERM2_mat * TERM1_mat)

    torsion_E = sp.zeros(N64, N64)
    for p in range(1, 7):
        for q in range(p + 1, 7):
            nb_pq = nabla_bracket(p, q, T, curv_h, Ms, Ls)
            torsion_E += kron(Es[p] * Es[q], nb_pq)

    cross_casimir = sp.simplify(
        2 * sum((kron(Ms[p], Ms[p]) for p in range(1, 7)), sp.zeros(N64, N64))
    )

    TWISTING_SPECIFIC = sp.simplify(T12 + T21 + torsion_E + cross_casimir)
    print("  TWISTING_SPECIFIC := (T12+T21) + TORSION_E + cross_casimir")
    print("  built from T-table + curv_h + M_p/E_p only -- no K, no Delta,")
    print("  no fitting. Computed independently above.")

    print("\n" + "=" * 70)
    print("STEP 4: sanity check -- UNTWISTED + TWISTING_SPECIFIC + F_Sminus")
    print("must reconstruct D64^2 exactly (confirms no piece double-counted")
    print("or dropped in this round's own re-grouping)")
    print("=" * 70)
    F_Sminus = sp.zeros(N64, N64)
    for p in range(1, 7):
        for q in range(p + 1, 7):
            R_pq = curvature_R(p, q, T, curv_h, Ms, Ls)
            F_Sminus += kron(Es[p] * Es[q], R_pq)

    CASIMIR_E = sp.zeros(N64, N64)
    for p in range(1, 7):
        CASIMIR_E += kron(Id8, -(Ms[p] * Ms[p]))
    TERM1_sq = kron(Dslash2, Id8)

    D64_sq_direct = sp.simplify(D64_leibniz * D64_leibniz)
    D64_sq_regrouped = sp.simplify(TERM1_sq + T12 + T21 + CASIMIR_E + F_Sminus + torsion_E)
    assert sp.simplify(D64_sq_direct - D64_sq_regrouped) == sp.zeros(N64, N64), (
        "D64^2 six-piece expansion does not match direct D64*D64 -- primitive mismatch"
    )
    nsn = sp.simplify(sum((-(Np[p] * Np[p]) for p in range(1, 7)), sp.zeros(N64, N64)))
    Delta_direct = sp.simplify(D64_sq_direct - nsn - F_Sminus)
    Delta_regrouped = sp.simplify(UNTWISTED_64 + TWISTING_SPECIFIC)
    assert sp.simplify(Delta_direct - Delta_regrouped) == sp.zeros(N64, N64), (
        "UNTWISTED+TWISTING_SPECIFIC does not reconstruct Delta exactly -- regrouping error"
    )
    print("  Delta == UNTWISTED + TWISTING_SPECIFIC exactly? True (asserted)")
    print("  (This is the SAME algebraic identity Round 41 already verified,")
    print("  just re-grouped into 2 buckets by STRUCTURAL origin instead of")
    print("  5 buckets by construction-order -- no new arithmetic risk.)")

    print("\n" + "=" * 70)
    print("STEP 5 (the actual test -- comparison happens ONLY here, after")
    print("STEPS 1-4 fixed the grouping with zero reference to K)")
    print("=" * 70)
    w_b = sp.zeros(N64, 1)
    w_b[idx64(0, 7)] = 1
    w_a = sp.zeros(N64, 1)
    w_a[idx64(4, 3)] = 1
    w_a[idx64(5, 2)] = -1
    w_a[idx64(6, 1)] = 1

    K_target = sp.Matrix([[0, sp.Rational(4, 3)], [4, 0]])
    untwisted_2x2 = compress_2x2(UNTWISTED_64, w_a, w_b)
    twisting_2x2 = compress_2x2(TWISTING_SPECIFIC, w_a, w_b)
    delta_2x2_check = sp.simplify(untwisted_2x2 + twisting_2x2)

    print(f"  UNTWISTED|_2dim = {untwisted_2x2.tolist()}")
    print(f"  TWISTING_SPECIFIC|_2dim = {twisting_2x2.tolist()}")
    print(f"  sum = {delta_2x2_check.tolist()}  (should be Delta_2x2=[[5/2,4/3],[4,5/2]])")
    expected_delta = sp.Matrix([[sp.Rational(5, 2), sp.Rational(4, 3)], [4, sp.Rational(5, 2)]])
    assert sp.simplify(delta_2x2_check - expected_delta) == sp.zeros(2, 2), (
        "regrouped compression does not match Delta_2x2 -- compression error"
    )

    twisting_offdiag = sp.Matrix([[0, twisting_2x2[0, 1]], [twisting_2x2[1, 0], 0]])
    offdiag_matches_K = sp.simplify(twisting_offdiag - K_target) == sp.zeros(2, 2)
    print(
        f"\n  TWISTING_SPECIFIC's own off-diagonal == K=[[0,4/3],[4,0]] exactly? "
        f"{offdiag_matches_K}"
    )
    assert offdiag_matches_K, (
        "TWISTING_SPECIFIC's off-diagonal does NOT match K -- hypothesis FAILS"
    )

    twisting_diag_nonzero = twisting_2x2[0, 0] != 0 or twisting_2x2[1, 1] != 0
    print(
        f"  TWISTING_SPECIFIC also has nonzero diagonal content "
        f"({twisting_2x2[0, 0]}, {twisting_2x2[1, 1]})? {twisting_diag_nonzero}"
    )

    print("\n" + "=" * 70)
    print("STEP 6 (POST-SKEPTIC, added after FL review found the above test")
    print("has ZERO discriminating power): is UNTWISTED's zero off-diagonal a")
    print("STRUCTURAL TAUTOLOGY (true for ANY X in kron(X,Id8)), independent")
    print("of what X actually contains?")
    print("=" * 70)
    Xsyms = sp.Matrix(DIM, DIM, lambda i, j: sp.Symbol(f"x_{i}_{j}"))
    arbitrary_kronX_Id = kron(Xsyms, Id8)
    arb_offdiag = compress_2x2(arbitrary_kronX_Id, w_a, w_b)
    arb_offdiag_is_zero = arb_offdiag[0, 1] == 0 and arb_offdiag[1, 0] == 0
    print("  For an ARBITRARY symbolic 8x8 matrix X (64 free symbols,")
    print("  unrelated to this project's geometry): kron(X,Id8)'s own")
    print(f"  off-diagonal on span(w_a,w_b) = ({arb_offdiag[0, 1]}, {arb_offdiag[1, 0]})")
    print(f"  -- i.e. EXACTLY ZERO regardless of X? {arb_offdiag_is_zero}")
    assert arb_offdiag_is_zero, "unexpected: kron(X,Id8) has nonzero off-diagonal for generic X"

    print("\n" + "=" * 70)
    print("CONCLUSION (REJECTED, post-skeptic -- see claim.md Skeptic Verdict)")
    print("=" * 70)
    print("  FALSIFIED as a discriminating test between fork (i) [Leibniz")
    print("  correction] and fork (ii) [F_Sminus incomplete]. STEP 6 proves the")
    print("  K-match in STEP 5 was FORCED: kron(X,Id8) has zero off-diagonal on")
    print("  span(w_a,w_b) for ANY X whatsoever (w_a,w_b have disjoint index")
    print("  support in BOTH tensor factors). Given the pre-existing identity")
    print("  Delta=UNTWISTED+TWISTING_SPECIFIC (Round 41), off-diag(TWISTING_")
    print("  SPECIFIC)=off-diag(Delta)=K follows automatically, regardless of")
    print("  whether TORSION_E/cross_casimir are correct physics or whether")
    print("  F_Sminus is complete. A genuinely MISSING F_Sminus term would ALSO")
    print("  be a two-factor-mixing operator and would land in TWISTING_SPECIFIC")
    print("  just as cleanly -- the test cannot tell the two forks apart.")
    print()
    print("  WHAT SURVIVES: Round 41's 5-piece decomposition, independently")
    print("  re-verified here via a different route (STEPS 2-4) -- genuine,")
    print("  could-have-failed algebra. D64's match to the textbook Leibniz-")
    print("  formula TEMPLATE (STEP 1) also stands, though it is a content-free")
    print("  Kronecker identity true for ANY matrices, not a physics check.")
    print("  Round 24's original fork (i) vs (ii) question remains OPEN.")


if __name__ == "__main__":
    main()
