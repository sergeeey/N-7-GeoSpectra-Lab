"""
Round 39 (2026-07-12): give Round 25's "step2_remainder" -- the piece
Round 25 flagged as evidence for an unbuilt "Jac_h/curvature-Jacobi"
term (Agricola Thm 3.2, t^2-weighted piece) -- a FULL CLOSED FORM using
Round 38's newly-derived Dslash_mat^2 = 3*Id-(9/4)*Casimir_su3 and
sum_p M_p^2 = -(1/2)*Id+(1/4)*Casimir_su3.

INVESTIGATION FIRST (research agent + own file reads, no code changes):
Round 24's own docstring left open whether Delta's traceless residual
[[0,4/3],[4,0]] is (i) a missing frame/Leibniz correction (Scal/4=5/2
stays fine) or (ii) F_{S^-} being an incomplete twist curvature. A
research agent traced the actual state further: Round 25 (already
closed, merged `main@811cb2b`, NOT reflected in Round 38's own
"Background" section -- a stale-summary correction, see round39_claim.md)
found `step2_remainder := (Dslash_mat^2 - CASIMIR_L_plain) - (-H)`
(CASIMIR_L_plain := -sum_p M_p^2, H := Kostant's cubic torsion element,
g2su3_H_element.py) compresses to a NON-SCALAR diagonal [-1/6, 5/2] on
Round 23/24's 2-dim SU(3)-invariant subspace span(w_a,w_b) -- promoted
as "empirical evidence the Jac_h piece is a real, nonzero presence."
Round 25 ALSO separately, independently verified kron(-H,Id8) alone
compresses to EXACTLY ZERO on this same subspace (its own STEP 5).

THIS ROUND'S FINDING: `step2_remainder = cubic_and_curvature_L + H`
where `cubic_and_curvature_L := Dslash_mat^2 - CASIMIR_L_plain =
Dslash_mat^2 + sum_p M_p^2`. Substituting Round 38's two closed forms:
  cubic_and_curvature_L = [3*Id-(9/4)*Cas] + [-(1/2)*Id+(1/4)*Cas]
                         = (5/2)*Id - 2*Casimir_su3          EXACTLY
So step2_remainder = (5/2)*Id - 2*Casimir_su3 + H, a FULL closed form
on the 8-dim Sigma (not just the compressed 2-dim block). Since Round
25's own w_b touches ONLY Sigma's LEFT-factor SU(3)-SINGLET content
(basis index 0, "1") where Casimir_su3=0, while w_a touches ONLY the
LEFT-factor SU(3)-SEXTET content (basis indices 4,5,6, "12"/"13"/"23")
where Casimir_su3=4/3 -- and since Round 25's own STEP 5 already
verified kron(H,Id8) contributes EXACTLY ZERO on this subspace -- the
predicted compressed value is: w_a-diagonal = 5/2-2*(4/3) = -1/6,
w_b-diagonal = 5/2-2*0 = 5/2. This EXACTLY matches Round 25's own
asserted [-1/6, 5/2] -- with ZERO contribution from H.

POST-SKEPTIC REWRITE (2026-07-12, see round39_claim.md "Skeptic
Verdict"): the ORIGINAL version of this docstring claimed the above as
a "CORRECTION" of Round 25's headline finding via an "independent
cross-check via a different route" for H's zero contribution. FL Step
8a (2 context-blind skeptics + a tool-using synthesis agent) found this
overclaimed in two ways: (1) `compress_2x2` is R-linear, so H's zero
contribution here is algebraically FORCED by Round 25's own STEP 5
result (sign-flipped), not independent evidence; (2) the off-diagonal-
zero half of the finding is ALSO structurally forced for ANY kron(X,
Id8) (confirmed by a random-matrix control, this round's new STEP F),
carrying no Casimir_su3-specific content -- ONLY the diagonal split
(-8/3 vs 0) is genuinely informative. The synthesis agent additionally
found direct textual evidence in g2su3_H_element.py's own docstring
tying Agricola's "Jac_h" term to "su(3)-valued curvature" -- the SAME
algebraic family Casimir_su3 is built from -- meaning Casimir_su3 may
BE Agricola's Jac_h term, not a "different, mundane" explanation of it.

REFRAMED CONCLUSION: this round DERIVES a closed form for
step2_remainder (`(5/2)*Id - 2*Casimir_su3 + H`), showing its diagonal
non-scalarity traces to Casimir_su3's own eigenvalue split (0 on
singlets, 4/3 on the sextet). Whether Casimir_su3 IS or merely
resembles Agricola's own Jac_h term is an OPEN question NOT resolved
here -- if it IS, this round has DERIVED Jac_h in closed form, not
shown it unnecessary, and Round 25's original finding would be
VALIDATED, not corrected. What IS refuted is narrower: Round 25's
"not-yet-built" framing -- step2_remainder's closed form uses only
PRE-EXISTING ingredients (Casimir_su3, H, a scalar), nothing new needed
to construct it.

HONEST LIMIT: this does NOT resolve Delta's FULL non-scalarity -- Round
25's own 5-piece decomposition of Delta also includes T12+T21,
TORSION_E, and cross-Casimir pieces (2*sum kron(Ms[p],Ms[p])), NONE of
which are touched by this round. It does NOT resolve the 8/45-vs-~1
L4A norm-bound tension, and does NOT touch preprint.tex.
"""

import random

import sympy as sp

from g2su3_appendix_a_construction import build_curvature_h_table
from g2su3_compute_crossterm import nabla_g
from g2su3_explicit_clifford import DIM, e_action
from g2su3_H_element import build_H_matrix, build_T_table
from g2su3_twisted_kernel import su3_action

N64 = DIM * DIM


def idx64(a, b):
    return DIM * a + b


def unit_vec(i):
    v = sp.zeros(DIM, 1)
    v[i] = 1
    return v


def kron(A, B):
    rA, cA = A.shape
    rB, cB = B.shape
    out = sp.zeros(rA * rB, cA * cB)
    for i in range(rA):
        for j in range(cA):
            if A[i, j] != 0:
                out[i * rB : (i + 1) * rB, j * cB : (j + 1) * cB] += A[i, j] * B
    return out


def compress_2x2(op, va, vb):
    Pmat = sp.Matrix.hstack(va, vb)
    G = (Pmat.T * Pmat).inv()
    opa, opb = op * va, op * vb
    sol_a = G * Pmat.T * opa
    sol_b = G * Pmat.T * opb
    return sp.simplify(sp.Matrix.hstack(sol_a, sol_b))


def main():
    print("=" * 70)
    print("SETUP: rebuild Dslash_mat, M_p, H, Casimir_su3 (all via ALREADY-")
    print("established Rounds 4-38 constructions)")
    print("=" * 70)
    T = build_T_table()
    H = build_H_matrix(T)
    Id8 = sp.eye(DIM)

    Ms = {}
    for p in range(1, 7):
        cols = [nabla_g(p, unit_vec(i)) for i in range(DIM)]
        Ms[p] = sp.Matrix.hstack(*cols)
    Es = {}
    for p in range(1, 7):
        cols = [e_action(p, unit_vec(i)) for i in range(DIM)]
        Es[p] = sp.Matrix.hstack(*cols)
    Dslash_mat = sp.zeros(DIM, DIM)
    for p in range(1, 7):
        Dslash_mat += Es[p] * Ms[p]
    Dslash2 = sp.simplify(Dslash_mat * Dslash_mat)

    CASIMIR_L_plain = sp.simplify(sum((-(Ms[p] * Ms[p]) for p in range(1, 7)), sp.zeros(DIM, DIM)))
    sumMp2 = sp.simplify(-CASIMIR_L_plain)

    Ls = {}
    for k in range(1, 9):
        cols = [su3_action(k, unit_vec(i)) for i in range(DIM)]
        Ls[k] = sp.Matrix.hstack(*cols)
    Casimir_su3 = sp.simplify(sum((-(Ls[k] * Ls[k]) for k in range(1, 9)), sp.zeros(DIM, DIM)))

    print("\n" + "=" * 70)
    print("STEP A: re-verify Round 38's own two closed forms (cited unchanged)")
    print("=" * 70)
    dslash2_ok = sp.simplify(Dslash2 - (3 * Id8 - sp.Rational(9, 4) * Casimir_su3)) == sp.zeros(
        DIM, DIM
    )
    summp2_ok = sp.simplify(
        sumMp2 - (-sp.Rational(1, 2) * Id8 + sp.Rational(1, 4) * Casimir_su3)
    ) == sp.zeros(DIM, DIM)
    print(f"  Dslash_mat^2 == 3*Id-(9/4)*Casimir_su3 (Round 38)? {dslash2_ok}")
    print(f"  sum_p M_p^2 == -(1/2)*Id+(1/4)*Casimir_su3 (Round 38)? {summp2_ok}")
    assert dslash2_ok, "Round 38's Dslash_mat^2 closed form did not reproduce"
    assert summp2_ok, "Round 38's sum M_p^2 closed form did not reproduce"

    print("\n" + "=" * 70)
    print("STEP B (the core new finding): cubic_and_curvature_L := Dslash_mat^2")
    print("- CASIMIR_L_plain = Dslash_mat^2 + sum_p M_p^2 = (5/2)*Id -")
    print("2*Casimir_su3 EXACTLY -- a direct algebraic consequence of Round 38's")
    print("two separate closed forms, verified here as a single combined identity")
    print("=" * 70)
    cubic_and_curvature_L = sp.simplify(Dslash2 - CASIMIR_L_plain)
    closed_form_ccL = sp.simplify(sp.Rational(5, 2) * Id8 - 2 * Casimir_su3)
    ccL_ok = sp.simplify(cubic_and_curvature_L - closed_form_ccL) == sp.zeros(DIM, DIM)
    print(f"  cubic_and_curvature_L == (5/2)*Id - 2*Casimir_su3 exactly? {ccL_ok}")
    assert ccL_ok, "cubic_and_curvature_L does not match the new closed form"

    print("\n" + "=" * 70)
    print("STEP C: Round 25's own step2_remainder := cubic_and_curvature_L -")
    print("(-H) = cubic_and_curvature_L + H, now in closed form:")
    print("  step2_remainder = (5/2)*Id - 2*Casimir_su3 + H")
    print("=" * 70)
    step2_remainder = sp.simplify(cubic_and_curvature_L - (-H))
    step2_closed = sp.simplify(sp.Rational(5, 2) * Id8 - 2 * Casimir_su3 + H)
    step2_ok = sp.simplify(step2_remainder - step2_closed) == sp.zeros(DIM, DIM)
    print(f"  step2_remainder == (5/2)*Id - 2*Casimir_su3 + H exactly? {step2_ok}")
    assert step2_ok, "step2_remainder does not match the new closed form"

    print("\n" + "=" * 70)
    print("STEP D: reproduce Round 25's own compressed value on span(w_a,w_b)")
    print("(2-dim SU(3)-invariant subspace of the 64-dim Gamma(S^+ (x) S^-)),")
    print("using Round 25's EXACT w_a/w_b definitions and compression method")
    print("=" * 70)
    w_b = sp.zeros(N64, 1)
    w_b[idx64(0, 7)] = 1
    w_a = sp.zeros(N64, 1)
    w_a[idx64(4, 3)] = 1
    w_a[idx64(5, 2)] = -1
    w_a[idx64(6, 1)] = 1

    piece_step2_rem = kron(step2_remainder, Id8)
    step2_2x2 = compress_2x2(piece_step2_rem, w_a, w_b)
    print(f"  step2_remainder|_2dim (recomputed via this round's closed form): {list(step2_2x2)}")
    expected_round25 = sp.Matrix([[sp.Rational(-1, 6), 0], [0, sp.Rational(5, 2)]])
    matches_round25 = step2_2x2 == expected_round25
    print(f"  matches Round 25's own asserted [[-1/6,0],[0,5/2]] exactly? {matches_round25}")
    assert matches_round25, "closed-form recomputation does not match Round 25's known value"

    print("\n" + "=" * 70)
    print("STEP E (the decisive split): decompose step2_remainder's compressed")
    print("value into its THREE closed-form pieces -- (5/2)*Id, -2*Casimir_su3,")
    print("and H -- to show WHICH piece carries the non-scalarity")
    print("=" * 70)
    piece_scalar = kron(sp.Rational(5, 2) * Id8, Id8)
    piece_cas = kron(-2 * Casimir_su3, Id8)
    piece_H = kron(H, Id8)

    scalar_2x2 = compress_2x2(piece_scalar, w_a, w_b)
    cas_2x2 = compress_2x2(piece_cas, w_a, w_b)
    H_2x2 = compress_2x2(piece_H, w_a, w_b)
    print(f"  (5/2)*Id contribution|_2dim:      {list(scalar_2x2)}")
    print(f"  -2*Casimir_su3 contribution|_2dim: {list(cas_2x2)}")
    print(f"  H contribution|_2dim:              {list(H_2x2)}")

    H_is_zero = H_2x2 == sp.zeros(2, 2)
    print(f"\n  H's own contribution is exactly zero (matches Round 25's own STEP 5")
    print(f"  finding, kron(-H,Id8)|_2dim==0, sign-flipped)? {H_is_zero}")
    assert H_is_zero, "H's contribution is not zero -- contradicts Round 25's own STEP 5"

    reconstructed = sp.simplify(scalar_2x2 + cas_2x2 + H_2x2)
    reconstruction_ok = reconstructed == expected_round25
    print(f"  scalar + cas + H reconstructs step2_remainder|_2dim exactly? {reconstruction_ok}")
    assert reconstruction_ok, "three-piece split does not sum to step2_remainder|_2dim"

    cas_is_source = cas_2x2[0, 0] != cas_2x2[1, 1] and cas_2x2[0, 1] == 0 and cas_2x2[1, 0] == 0
    print(f"\n  ALL of step2_remainder's non-scalarity traces to -2*Casimir_su3 alone")
    print(f"  (diagonal but unequal entries, zero off-diagonal)? {cas_is_source}")
    assert cas_is_source, "non-scalarity does not cleanly trace to Casimir_su3 alone"

    print("\n" + "=" * 70)
    print("STEP F (post-skeptic addition): control test -- is the OFF-DIAGONAL")
    print("zero in STEP E specific to Casimir_su3/H, or structurally forced for")
    print("ANY kron(X,Id8)-type operator by w_a/w_b's disjoint RIGHT-tensor-index")
    print("support (the SAME mechanism Round 25's own STEP 5 controls found for")
    print("H, e_1, M_1)? Both FL Step 8a skeptics + the synthesis agent flagged")
    print("this; confirming it explicitly here rather than leaving it implicit.")
    print("=" * 70)
    random.seed(39)
    X_random = sp.Matrix(DIM, DIM, lambda i, j: random.randint(-5, 5))
    piece_random = kron(X_random, Id8)
    random_2x2 = compress_2x2(piece_random, w_a, w_b)
    random_offdiag_zero = random_2x2[0, 1] == 0 and random_2x2[1, 0] == 0
    print(
        f"  compress(kron(random_X, Id8))|_2dim off-diagonal entries: "
        f"[{random_2x2[0, 1]}, {random_2x2[1, 0]}]"
    )
    print(f"  off-diagonal zero for an UNRELATED random X too? {random_offdiag_zero}")
    assert random_offdiag_zero, "off-diagonal-zero pattern is NOT structural after all"
    print("  => CONFIRMED structural: off-diagonal vanishing in STEP E carries NO")
    print("  Casimir_su3-specific content -- it holds for ANY kron(X,Id8), a")
    print("  consequence of w_a/w_b's disjoint RIGHT-tensor-index support alone")
    print("  (same mechanism as Round 25's own H/e_1/M_1 null controls). Only the")
    print("  DIAGONAL entries (-8/3 from -2*Casimir_su3, vs 0) carry genuine")
    print("  Casimir_su3-specific information.")

    print("\n" + "=" * 70)
    print("CONCLUSION (POST-SKEPTIC REWRITE)")
    print("=" * 70)
    print("  step2_remainder now has a FULL CLOSED FORM: (5/2)*Id - 2*Casimir_su3")
    print("  + H. FL Step 8a (2 context-blind skeptics + synthesis) found the")
    print("  ORIGINAL framing below overclaimed in two ways -- both fixed:")
    print("  (1) H's zero contribution is NOT an 'independent cross-check via a")
    print("  different route' -- compress_2x2 is R-linear, so this is a sign-")
    print("  flipped restatement of Round 25's OWN STEP 5 computation, not fresh")
    print("  evidence (confirmed above, STEP E).")
    print("  (2) The off-diagonal-zero half of the finding carries NO Casimir-")
    print("  specific content (STEP F above) -- it is structural for ANY kron(X,")
    print("  Id8). ONLY the diagonal split (-8/3 vs 0, from Casimir_su3's own")
    print("  0/4-3 eigenvalues) is genuinely informative.")
    print()
    print("  REFRAMED (not 'CORRECTS'): this round DERIVES a closed form for")
    print("  step2_remainder, showing its diagonal non-scalarity traces to")
    print("  Casimir_su3's eigenvalue split. Whether Casimir_su3 (built from")
    print("  su3_action, the su(3)-generator family) IS or merely RESEMBLES")
    print("  Agricola's own 'Jac_h/curvature-Jacobi' term (g2su3_H_element.py's")
    print("  own docstring ties that term to 'su(3)-valued curvature') is an")
    print("  OPEN question this round does NOT resolve. If Casimir_su3 IS that")
    print("  term, this round has DERIVED Jac_h in closed form, not shown it")
    print("  unnecessary -- Round 25's original finding would then be VALIDATED,")
    print("  not corrected. What IS refuted: Round 25's 'not-yet-built' framing")
    print("  -- step2_remainder's closed form uses only PRE-EXISTING ingredients.")
    print()
    print("  HONEST LIMIT: this does NOT resolve Delta's FULL non-scalarity --")
    print("  Round 25's own 5-piece decomposition also has T12+T21, TORSION_E,")
    print("  and cross-Casimir pieces, NONE touched by this round. Does NOT")
    print("  resolve the 8/45-vs-~1 L4A tension. Does NOT touch preprint.tex.")


if __name__ == "__main__":
    main()
