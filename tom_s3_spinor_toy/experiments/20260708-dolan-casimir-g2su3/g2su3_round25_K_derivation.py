"""
Round 25 (2026-07-11): derive Round 24's trace-free residual
Delta_2x2 - (5/2)*Id = [[0,4/3],[4,0]] DIRECTLY from invariant-frame /
Nomizu / torsion algebra, BLIND -- every piece below is defined by exact
subtraction from already-verified ground-truth matrices (Round 22-24's
Ms, Es, T-table, curv_h-table, and g2su3_H_element's Kostant cubic
element H), never fitted to reproduce [[0,4/3],[4,0]] in advance.

WHY THIS SHAPE OF DERIVATION. Round 24 (g2su3_Sminus_weitzenbock.py) built
D64^2 = TERM1_sq + T12 + T21 + CASIMIR_E + F_Sminus + TORSION_E  (exact,
Round 23's own verified identity) and nabla*nabla = -sum N_p^2 with
N_p := M_p(x)Id+Id(x)M_p (Round 24's own construction). Both TERM1_sq
(:= Dslash_mat^2 (x) Id_8, i.e. the LEFT factor's own Dirac-squared) and
T12+T21 (the TERM1.TERM2+TERM2.TERM1 cross pieces) were used as OPAQUE,
undecomposed blocks in both rounds -- exactly analogous to how Round 22's
naive shortcut once treated TERM2^2 before it was split into
CASIMIR_E+F_Sminus+TORSION_E. This round applies the SAME kind of split
to TERM1_sq, using g2su3_H_element.py's ALREADY-BUILT, ALREADY-VALIDATED
Kostant cubic element H (built purely from the torsion 3-form
T(i,j,k)=<[Z_i,Z_j]_m,Z_k>, i.e. pure Nomizu/torsion algebra -- see that
file's own docstring, which independently notes: per Agricola 2002
Theorem 3.2, at t=1/2 (Levi-Civita, matching THIS project's connection
convention -- see g2su3_H_element.py's own note on this) the cubic-
Clifford torsion correction term appearing in (D^{1/2})^2 is EXACTLY -H.

ALGEBRAIC IDENTITY (derived by direct subtraction of exact matrices, NOT
assumed -- verified step by step below):

  Delta := D64^2 - nabla*nabla - F_Sminus
         = TERM1_sq - CASIMIR_L_64 + T12 + T21 + TORSION_E
           + 2*sum_p kron(Ms[p],Ms[p])

  where CASIMIR_L_64 := kron(-sum_p Ms[p]^2, Id8) is the direct LEFT-factor
  analogue of CASIMIR_E, and TERM1_sq - CASIMIR_L_64 = kron(Dslash2 -
  (-sum Ms[p]^2), Id8) = kron(cubic_and_curvature_L, Id8) BY DEFINITION.

  cubic_and_curvature_L is tested against -H (the Nomizu/torsion cubic
  term) directly: cubic_and_curvature_L - (-H) should be SCALAR (matching
  Agricola's Scal/4 term) if no further Jac_h-curvature piece is needed
  at this order -- g2su3_H_element.py's own docstring flags that a
  separate Jac_h/curvature-Jacobi piece MAY be needed and was NOT built
  there; this script tests for its presence rather than assuming either
  way.

Each of the FIVE pieces on the right of Delta's identity above is then
independently restricted to span(w_a,w_b) (Round 23/24's 2-dim SU(3)-
invariant subspace) and summed -- verified to reconstruct the ALREADY-
KNOWN Delta_2x2=[[5/2,4/3],[4,5/2]] EXACTLY (a consistency check on this
round's own algebra, not a new physics claim by itself).

POST-SKEPTIC UPDATE (2026-07-11, see round25_claim.md "Skeptic Verdict"):
the original framing below asked whether kron(-H,Id8) ALONE accounts for
the traceless residual. RESULT: it compresses to EXACTLY ZERO on this
subspace -- but two independent skeptics, plus the author's own follow-up
controls (substituting a generic Clifford generator e_1, and separately a
chirality-PRESERVING connection operator M_1, both ALSO giving exactly
zero, while a literal random matrix does NOT), established this null is
NOT decisive evidence about Kostant's H specifically -- the probe cannot
distinguish "H is the right correction," "H is the wrong correction," or
several structurally-unrelated single-source operators from one another.
DOWNGRADED from "the hypothesis test" to "an inconclusive probe with an
incompletely-understood null" -- see STEP 5's rewritten interpretation.
The genuinely informative finding instead came from step2_remainder (the
piece Agricola's formula would assign to the "Jac_h/curvature-Jacobi"
term g2su3_H_element.py's own docstring flagged as not-yet-built):
it compresses to a NON-SCALAR diagonal, empirical evidence that piece is
a real, nonzero presence -- promoted to this round's headline result.

Evidence markers: every numeric claim is re-computed and asserted in
main() below ([VERIFIED-tool] on run).
"""

import sympy as sp

from g2su3_appendix_a_construction import build_curvature_h_table
from g2su3_compute_crossterm import nabla_g
from g2su3_equivariance_check import build_D_matrix64
from g2su3_explicit_clifford import DIM, SUBSETS, e_action
from g2su3_H_element import build_H_matrix, build_T_table as build_T_table_H
from g2su3_twisted_kernel import su3_action

N64 = DIM * DIM


def idx64(a, b):
    return DIM * a + b


def chirality_sign(subset):
    return 1 if len(subset) % 2 == 0 else -1


S_PLUS = [i for i, s in enumerate(SUBSETS) if chirality_sign(s) == 1]
S_MINUS = [i for i, s in enumerate(SUBSETS) if chirality_sign(s) == -1]


def build_Mp():
    Ms = {}
    for p in range(1, 7):
        cols = [nabla_g(p, unit_vec(i)) for i in range(DIM)]
        Ms[p] = sp.Matrix.hstack(*cols)
    return Ms


def build_Lk():
    Ls = {}
    for k in range(1, 9):
        cols = [su3_action(k, unit_vec(i)) for i in range(DIM)]
        Ls[k] = sp.Matrix.hstack(*cols)
    return Ls


def build_Ep():
    Es = {}
    for p in range(1, 7):
        cols = [e_action(p, unit_vec(i)) for i in range(DIM)]
        Es[p] = sp.Matrix.hstack(*cols)
    return Es


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


def project_2x2(op, va, vb, name):
    """STRICT compression: asserts op maps span(va,vb) into itself exactly
    (no leak). Use when op must be a genuine endomorphism of the invariant
    subspace (e.g. D64^2, nabla*nabla, F_Sminus, Delta itself)."""
    Pmat = sp.Matrix.hstack(va, vb)
    G = (Pmat.T * Pmat).inv()
    opa, opb = op * va, op * vb
    sol_a = G * Pmat.T * opa
    sol_b = G * Pmat.T * opb
    leak_a = sp.simplify(opa - Pmat * sol_a)
    leak_b = sp.simplify(opb - Pmat * sol_b)
    assert leak_a == sp.zeros(N64, 1), f"{name}(w_a) leaks outside span(w_a,w_b)"
    assert leak_b == sp.zeros(N64, 1), f"{name}(w_b) leaks outside span(w_a,w_b)"
    return sp.simplify(sp.Matrix.hstack(sol_a, sol_b))


def compress_2x2(op, va, vb, name, report_leak=True):
    """LINEAR compression (Gram-corrected projection onto span(va,vb)'s
    coefficients), WITHOUT requiring op to preserve the subspace. Valid for
    summing contributions from individual pieces of a decomposition whose
    TOTAL is known to preserve the subspace, even if individual pieces do
    not (compression is linear: compress(A+B)=compress(A)+compress(B)
    regardless of leak). Reports leak magnitude as diagnostic, does not
    assert it is zero."""
    Pmat = sp.Matrix.hstack(va, vb)
    G = (Pmat.T * Pmat).inv()
    opa, opb = op * va, op * vb
    sol_a = G * Pmat.T * opa
    sol_b = G * Pmat.T * opb
    if report_leak:
        leak_a = sp.simplify(opa - Pmat * sol_a)
        leak_b = sp.simplify(opb - Pmat * sol_b)
        leaks = leak_a.norm() != 0 or leak_b.norm() != 0
        if leaks:
            print(f"    [{name}: leaks outside span(w_a,w_b) -- not itself an")
            print("     endomorphism of the invariant subspace; compressed value")
            print("     below is a linear partial contribution to the SUM only]")
    return sp.simplify(sp.Matrix.hstack(sol_a, sol_b))


def main():
    print("=" * 70)
    print("SETUP")
    print("=" * 70)
    Ms = build_Mp()
    Ls = build_Lk()
    Es = build_Ep()
    Id8 = sp.eye(DIM)
    T_H = build_T_table_H()
    H = build_H_matrix(T_H)
    D64 = build_D_matrix64()
    curv_h = build_curvature_h_table()

    def nabla_bracket(p, q):
        out = sp.zeros(DIM, DIM)
        T_local = build_T_table_local()
        for r in range(1, 7):
            coeff = T_local.get((p, q, r), 0)
            if coeff != 0:
                out += coeff * Ms[r]
        for k in range(1, 9):
            coeff = curv_h.get((p, q, k), 0)
            if coeff != 0:
                out -= coeff * Ls[k]
        return out

    def build_T_table_local():
        return T_H  # same torsion table, single source of truth (g2su3_H_element)

    def curvature_R(p, q):
        comm = Ms[p] * Ms[q] - Ms[q] * Ms[p]
        return comm - nabla_bracket(p, q)

    print("\n" + "=" * 70)
    print("STEP 1: re-verify H (imported from g2su3_H_element, already validated")
    print("there) -- cheap sanity re-check only, not re-deriving it.")
    print("=" * 70)
    H2 = sp.simplify(H * H)
    scalar_closed_form = sp.Rational(3, 8) * sum(
        sp.simplify(T_H.get((i, j, k), 0)) ** 2
        for i in range(1, 7)
        for j in range(1, 7)
        for k in range(1, 7)
    )
    trace_avg = sp.simplify(sum(H2[r, r] for r in range(DIM)) / DIM)
    print(
        f"  Tr(H^2)/8 = {trace_avg}, closed-form (3/8)sum T^2 = {sp.simplify(scalar_closed_form)}"
    )
    assert sp.simplify(trace_avg - scalar_closed_form) == 0, "H import/rebuild mismatch"
    print("  H matches its own established closed-form check. Reusing as-is.")

    print("\n" + "=" * 70)
    print("STEP 2: decompose Dslash_mat^2 = -sum Ms[p]^2 + cubic_and_curvature_L")
    print("(exact subtraction, no algebra assumed), then test cubic_and_curvature_L")
    print("against -H (pure torsion/Nomizu cubic term, Agricola t=1/2).")
    print("=" * 70)
    Dslash_mat = sp.zeros(DIM, DIM)
    for p in range(1, 7):
        Dslash_mat += Es[p] * Ms[p]
    Dslash2 = sp.simplify(Dslash_mat * Dslash_mat)

    CASIMIR_L_plain = sp.zeros(DIM, DIM)
    for p in range(1, 7):
        CASIMIR_L_plain += -(Ms[p] * Ms[p])
    CASIMIR_L_plain = sp.simplify(CASIMIR_L_plain)

    cubic_and_curvature_L = sp.simplify(Dslash2 - CASIMIR_L_plain)
    print("  cubic_and_curvature_L := Dslash^2 - (-sum Ms[p]^2)  [exact by subtraction]")

    step2_remainder = sp.simplify(cubic_and_curvature_L - (-H))
    is_scalar_step2 = step2_remainder == step2_remainder[0, 0] * Id8
    print(
        f"  cubic_and_curvature_L - (-H) is scalar*Id (no extra Jac_h piece needed)? "
        f"{is_scalar_step2}"
    )
    if is_scalar_step2:
        print(
            f"    => scalar value (Scal/4 for the plain Sigma Dirac operator) = "
            f"{step2_remainder[0, 0]}"
        )
    else:
        print("    => a genuine Jac_h/curvature-Jacobi remainder survives (matches")
        print("       g2su3_H_element.py's own flagged, not-yet-built gap). Reporting")
        print("       it as-is, NOT forcing it to scalar:")
        sp.pprint(sp.simplify(step2_remainder))
    print("  (Either way, cubic_and_curvature_L itself is EXACT and used as-is below --")
    print("  this scalar/non-scalar test is informational, not a precondition.)")

    print("\n" + "=" * 70)
    print("STEP 3: assemble Delta's exact five-piece decomposition and verify it")
    print("reconstructs the ALREADY-KNOWN D64^2 exactly (sanity check on this")
    print("round's own algebra before trusting the 2-dim restriction).")
    print("=" * 70)
    TERM1_mat = kron(Dslash_mat, Id8)
    TERM2_mat = sp.zeros(N64, N64)
    for p in range(1, 7):
        TERM2_mat += kron(Es[p], Ms[p])
    T12 = TERM1_mat * TERM2_mat
    T21 = TERM2_mat * TERM1_mat
    TERM1_sq = kron(Dslash2, Id8)
    CASIMIR_E = sp.zeros(N64, N64)
    for p in range(1, 7):
        CASIMIR_E += kron(Id8, -(Ms[p] * Ms[p]))

    F_Sminus = sp.zeros(N64, N64)
    torsion_E = sp.zeros(N64, N64)
    for p in range(1, 7):
        for q in range(p + 1, 7):
            R_pq = curvature_R(p, q)
            nb_pq = nabla_bracket(p, q)
            F_Sminus += kron(Es[p] * Es[q], R_pq)
            torsion_E += kron(Es[p] * Es[q], nb_pq)

    D64_sq = sp.simplify(D64 * D64)
    D64_sq_reconstructed = sp.simplify(TERM1_sq + T12 + T21 + CASIMIR_E + F_Sminus + torsion_E)
    assert sp.simplify(D64_sq_reconstructed - D64_sq) == sp.zeros(N64, N64), (
        "D64^2 reconstruction from Round 23's own pieces failed -- primitives changed?"
    )
    print("  D64^2 == TERM1_sq+T12+T21+CASIMIR_E+F_Sminus+TORSION_E (Round 23's own")
    print("  identity, re-verified here)? True")

    Np = {p: kron(Ms[p], Id8) + kron(Id8, Ms[p]) for p in range(1, 7)}
    nsn = sp.simplify(sum((-(Np[p] * Np[p]) for p in range(1, 7)), sp.zeros(N64, N64)))

    CASIMIR_L_64 = kron(CASIMIR_L_plain, Id8)
    cross_Casimir = sp.simplify(
        2 * sum((kron(Ms[p], Ms[p]) for p in range(1, 7)), sp.zeros(N64, N64))
    )
    nsn_check = sp.simplify(CASIMIR_L_64 + CASIMIR_E - cross_Casimir)
    assert sp.simplify(nsn_check - nsn) == sp.zeros(N64, N64), (
        "nabla*nabla algebraic re-expression CASIMIR_L+CASIMIR_E-2*cross does not match Round 24's direct -sum N_p^2"
    )
    print("  nabla*nabla == CASIMIR_L_64 + CASIMIR_E - 2*sum kron(Ms[p],Ms[p])")
    print("  (algebraic re-expression of Round 24's -sum N_p^2, verified exact)? True")

    piece_H = kron(-H, Id8)
    piece_step2_rem = kron(step2_remainder, Id8)
    piece_T12T21 = sp.simplify(T12 + T21)
    piece_torsion_E = torsion_E
    piece_cross_casimir = cross_Casimir

    Delta_5piece = sp.simplify(
        piece_H + piece_step2_rem + piece_T12T21 + piece_torsion_E + piece_cross_casimir
    )
    Delta_direct = sp.simplify(D64_sq - nsn - F_Sminus)
    assert sp.simplify(Delta_5piece - Delta_direct) == sp.zeros(N64, N64), (
        "Five-piece decomposition of Delta does not match direct D64^2-nabla*nabla-F_Sminus"
    )
    print("  Delta == piece_H + piece_step2_remainder + (T12+T21) + TORSION_E")
    print("  + 2*sum kron(Ms[p],Ms[p])  [exact five-piece identity, verified]? True")

    print("\n" + "=" * 70)
    print("STEP 4: restrict each of the five pieces to span(w_a,w_b) (the 2-dim")
    print("SU(3)-invariant subspace) and see how [[0,4/3],[4,0]] distributes.")
    print("=" * 70)
    w_b = sp.zeros(N64, 1)
    w_b[idx64(0, 7)] = 1
    w_a = sp.zeros(N64, 1)
    w_a[idx64(4, 3)] = 1
    w_a[idx64(5, 2)] = -1
    w_a[idx64(6, 1)] = 1

    labeled_pieces = [
        ("kron(-H,Id8)  [pure Nomizu/torsion cubic term]", piece_H),
        ("kron(step2_remainder,Id8)  [scalar or Jac_h leftover]", piece_step2_rem),
        ("T12+T21  [previously opaque cross terms]", piece_T12T21),
        ("TORSION_E  [Round 22/23's known torsion cross-term]", piece_torsion_E),
        ("2*sum kron(Ms[p],Ms[p])  [cross-Casimir from N_p^2 expansion]", piece_cross_casimir),
    ]

    print("  NOTE: individual pieces need NOT preserve span(w_a,w_b) -- only the")
    print("  full sum (== Delta, genuinely SU(3)-equivariant) is guaranteed to.")
    print("  Using LINEAR compression (compress_2x2), not strict endomorphism")
    print("  restriction, for the per-piece values below; leaks are reported.")

    running_sum = sp.zeros(2, 2)
    for name, piece in labeled_pieces:
        p2x2 = compress_2x2(piece, w_a, w_b, name)
        print(f"\n  {name}:")
        sp.pprint(p2x2)
        running_sum += p2x2

    running_sum = sp.simplify(running_sum)
    print("\n  Sum of all five pieces (linear compression), restricted to span(w_a,w_b):")
    sp.pprint(running_sum)
    Delta_2x2_known = sp.Matrix([[sp.Rational(5, 2), sp.Rational(4, 3)], [4, sp.Rational(5, 2)]])
    assert sp.simplify(running_sum - Delta_2x2_known) == sp.zeros(2, 2), (
        "Five-piece sum on the 2-dim block does not match Round 24's known Delta_2x2"
    )
    print("  Matches Round 24's known Delta_2x2 = [[5/2,4/3],[4,5/2]] exactly? True")
    print("  (This equality is guaranteed by STEP 3's exact algebraic identity plus")
    print("  linearity of compression -- confirms no arithmetic slip, not new physics.)")

    print("\n" + "=" * 70)
    print("STEP 5 (POST-SKEPTIC REWRITE): kron(-H,Id8) alone -- durability asserts")
    print("+ the CORRECTED interpretation (two skeptics + author's own follow-up")
    print("controls found this is an INCONCLUSIVE probe, not a decisive hypothesis")
    print("test -- see round25_claim.md 'C4' section for full reasoning).")
    print("=" * 70)
    H_2x2 = compress_2x2(piece_H, w_a, w_b, "kron(-H,Id8)", report_leak=False)
    K_target = sp.Matrix([[0, sp.Rational(4, 3)], [4, 0]])
    assert H_2x2 == sp.zeros(2, 2), (
        "kron(-H,Id8)|_2dim changed from the verified zero -- primitives changed?"
    )
    print(f"  kron(-H,Id8)|_2dim == [[0,0],[0,0]]? {H_2x2 == sp.zeros(2, 2)}  [asserted]")
    print("  CAVEAT (both skeptics + author verification): this zero is NOT decisive")
    print("  evidence against H specifically. A generic chirality-odd operator (a")
    print("  single Clifford generator e_1) gives the SAME zero via a structural")
    print("  tautology (RIGHT tensor index cannot change under kron(X,Id8) for ANY X,")
    print("  and w_a/w_b have disjoint RIGHT-index support -- forces both off-diagonal")
    print("  entries to zero regardless of X). More surprisingly, a chirality-")
    print("  PRESERVING single operator (M_1, a bivector connection term) ALSO gives")
    print("  exactly zero -- NOT explained by the chirality argument alone -- while a")
    print("  literal random 8x8 matrix does NOT (nonzero diagonal). The precise reason")
    print("  H/e_1/M_1 all vanish while a random matrix does not is NOT established")
    print("  here; only the empirical pattern is reported.")

    K_2x2 = sp.simplify(running_sum - sp.Rational(5, 2) * sp.eye(2))
    assert K_2x2 == K_target, (
        "traceless residual K no longer matches [[0,4/3],[4,0]] -- primitives changed?"
    )
    print(
        f"\n  Traceless residual K = running_sum - (5/2)*Id == [[0,4/3],[4,0]]? "
        f"{K_2x2 == K_target}  [asserted]"
    )

    step2_2x2 = compress_2x2(piece_step2_rem, w_a, w_b, "step2_remainder", report_leak=False)
    assert step2_2x2 == sp.Matrix([[sp.Rational(-1, 6), 0], [0, sp.Rational(5, 2)]]), (
        "step2_remainder|_2dim changed -- primitives changed?"
    )
    step2_is_scalar = step2_2x2 == step2_2x2[0, 0] * sp.eye(2)
    print(f"  step2_remainder|_2dim = {list(step2_2x2)}  [asserted]")
    print(f"  step2_remainder|_2dim is scalar (would mean NO Jac_h presence)? {step2_is_scalar}")

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("  C4 (kron(-H,Id8) alone): INCONCLUSIVE, not decisive -- downgraded from")
    print("  'the actual hypothesis test' after skeptic review. Do NOT cite this round")
    print("  as evidence for or against Kostant's H being related to K.")
    print()
    print("  C5 (PROMOTED headline finding): step2_remainder -- the piece Agricola's")
    print("  Theorem 3.2 would assign to a t^2-weighted Jac_h/curvature-Jacobi term,")
    print("  explicitly flagged as 'not computed' in g2su3_H_element.py -- compresses")
    print("  to a NON-SCALAR diagonal ([-1/6, 5/2], not equal). This is empirical")
    print("  evidence the Jac_h piece is a real, nonzero presence, not just a")
    print("  theoretical possibility. Deriving it explicitly is the concrete next step.")


if __name__ == "__main__":
    main()
