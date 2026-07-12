"""
Round 35 (2026-07-12): derive the SPECIFIC proportionality constants
`c=1` (Ch_4) and `c'=-5/4` (degree4_term) that Round 33 explicitly left
unexplained -- "does NOT explain the SPECIFIC numeric value of the
proportionality constant `c` ... that still requires the direct
combinatorial computation from Rounds 26/29/31/32. This round explains
the SUPPORT (which quadruples, why equal across them), not the VALUE."

CORE FINDING (post-skeptic, framing corrected -- see below): Ch_4's
own `c=1` does NOT require Round 33's OWN 3x3-solve-on-Ch_4 -- it is a
LOGICAL CONSEQUENCE of THREE ALREADY-ESTABLISHED, STRUCTURAL facts,
assembled here for the first time in this direction:

  (1) Ch_0 = Tr(Ch_tilde)/DIM [Round 26 STEP 1: Ch_4 is pure degree-4,
      hence traceless BY CONSTRUCTION -- a structural/degree fact, not
      a computation]
  (2) Ch_tilde = Casimir_su3 EXACTLY [Round 30: C~h is, by Agricola's
      OWN definition (Prop 3.3), literally the su(3) Casimir operator
      for a Qh-orthonormal basis -- a STRUCTURAL identity between two
      OPERATOR DEFINITIONS, established INDEPENDENTLY of Ch_4's own
      numeric value]
  (3) Tr(Casimir_su3)/DIM = 1 [Round 29/33: Casimir_su3 = Id + X/3
      where X:=Z1234+Z1256+Z3456 is a genuine degree-4 Clifford element,
      hence traceless BY CONSTRUCTION -- again structural, not computed]

Combining: Ch_0 = Tr(Ch_tilde)/DIM = Tr(Casimir_su3)/DIM = 1, so
Ch_4 = Ch_tilde - Ch_0*Id = Casimir_su3 - Id = 1*(Casimir_su3-Id) --
c=1 FOLLOWS from facts (1)-(3), it is not separately solved for on
Ch_4's own quartic matrix.

FL STEP 8a CAVEAT (both skeptics + synthesis, CONFIRMED-REAL but
framing WEAKENED -- read before trusting "FULLY structurally derived"
language anywhere else in this file): the IN-SCRIPT STEP C below is
MECHANICALLY TAUTOLOGICAL with STEP A -- since Ch_tilde is DEFINED in
STEP A as Ch_0_direct*Id+Ch_4, and Ch_4 is traceless, STEP C's own
Ch_0_derived:=Tr(Ch_tilde)/DIM collapses right back to Ch_0_direct by
construction, and the resulting "Ch_4==Casimir_su3-Ch_0*Id" check is
algebraically forced by STEP A alone, adding ZERO fresh independent
evidence in-code. This does NOT falsify the underlying MATHEMATICAL
claim (both skeptics independently verified Round 30's own S1-S9
structural chain, STEPs A-D of g2su3_round30_ch_casimir_structural.py,
NEVER references Ch_4 -- only Round 30's OWN STEP E, its own labeled
"sanity cross-check", does -- so the claimed dependency direction is
real at the mathematical level) -- but it means STEP C below is kept
as a PEDAGOGICAL walkthrough of the algebraic chain, not an
independent numerical check (see its own inline comment). The
synthesis agent additionally found: Ch_0=1 was ALREADY directly
computable via Qh_sum=8 since Round 26 itself (plain curv_h
summation) -- so the genuinely NEW content this round adds is a
SECOND, independent route to the same number (via Casimir_su3=Id+X/3,
pure degree-counting, no curv_h summation) -- a more modest and
accurate characterization than "the value c=1 was previously unknown."

IMPORTANT CORRECTION TO ROUND 33's OWN FRAMING: Round 33's STEP D used
the SOLVED c=1 (from its own STEP B combinatorial solve) to re-derive
Ch_tilde=Casimir_su3 as a "bonus", explicitly flagged (after Round 33's
own skeptic review) as using a "plugged-in" solved value, NOT a
structural derivation of c. This round shows the LOGICAL DEPENDENCY
actually runs the OTHER WAY: Ch_tilde=Casimir_su3 (Round 30) is PRIOR
and INDEPENDENT of Ch_4's own combinatorial value -- it is Ch_4's c=1
that is DERIVED FROM Ch_tilde=Casimir_su3 (plus the two traceless facts
above), not the reverse. Round 33's STEP D had the dependency direction
backwards (a fact its own claim.md already flagged as a scope caveat,
not a discovered error -- this round completes what that caveat left
open).

SECOND FINDING (RELOCATION, not reduction in solve-count -- framing
corrected post-skeptic): degree4_term = Ch_4 - (9/8)*Jm4 EXACTLY, where
Jm4 is the quartic matrix built PURELY from jac_m (Round 26's m-part
Jacobiator, T-table only, curv_h-INDEPENDENT) -- a clean algebraic
decomposition not previously stated explicitly. Jm4 satisfies the SAME
three premises Round 28's theorem needs (SU(3)-equivariant,
Swap-symmetric, Hermitian, traceless) and is therefore ALSO forced into
span{Casimir_su3-Id} by Round 33's OWN degree-counting argument,
applied here to a NEW object Round 33 never considered. Solving gives
Jm4 = 2*(Casimir_su3-Id) EXACTLY (d=2) -- via a fresh, non-vacuous 3x3
solve (same method as Round 33). Combining: degree4_term's own
c' = 1 - (9/8)*2 = -5/4, matching Round 26/31's independently-computed
value EXACTLY -- but per both skeptics + synthesis (CONFIRMED-REAL,
framing WEAKENED): this is a RELOCATION of the SAME combinatorial 3x3
solve from degree4_term (which mixes curv_h+jac_m) onto Jm4 (curv_h-
independent only) -- NOT a reduction in the NUMBER of solves performed.
The object solved is genuinely cleaner (one fewer input table), which
is real progress, but "why is degree4_term's coefficient -5/4" is not
reduced to a "simpler" open question in the sense of requiring LESS
combinatorial work -- only a DIFFERENT, more isolated one. `d=2` itself
is NOT derived from a deeper principle here.

HONEST SCOPE (post-skeptic): c=1 (Ch_4) is a LOGICAL CONSEQUENCE of 3
already-established structural facts (Round 29/30/33) -- but the
in-script demonstration of this (STEP C) is tautological with STEP A,
and the underlying independence rests entirely on TRUSTING Round 30's
own S1-S9 chain (itself citing 2 textbook Lie-theory facts + a
back-solved k=8 case) -- NOT on any fresh numerical evidence Round 35
itself contributes. What Round 35 genuinely adds for Ch_4: a SECOND,
independent route to Ch_0=1 (via degree-counting on Casimir_su3=Id+X/3,
not via direct Qh_sum summation, which already gave the same number in
Round 26). c'=-5/4 (degree4_term) is RELOCATED, not reduced -- the
SAME combinatorial solve now runs on a cleaner, curv_h-independent
object (Jm4) instead of degree4_term directly; the solve is not
eliminated.
"""

import sympy as sp

from g2su3_appendix_a_construction import build_curvature_h_table
from g2su3_explicit_clifford import DIM
from g2su3_H_element import build_H_matrix, build_T_table
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
    print("SETUP: rebuild T, curv_h, H, Casimir_su3, Swap, Ch_4, degree4_term")
    print("(all via the ALREADY-established Rounds 26-33 constructions)")
    print("=" * 70)
    T = build_T_table()
    curv_h = build_curvature_h_table()
    H = build_H_matrix(T)
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

    print("\n" + "=" * 70)
    print("STEP A: re-verify Ch_tilde = Casimir_su3 EXACTLY (Round 30's own")
    print("STRUCTURAL finding -- an identity between two operator")
    print("DEFINITIONS, established INDEPENDENTLY of Ch_4's numeric value)")
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
    Ch_0_direct = sp.Rational(1, 8) * Qh_sum
    Ch_tilde = sp.simplify(Ch_0_direct * Id8 + Ch_4)
    ch_tilde_eq_cas = sp.simplify(Ch_tilde - Casimir_su3) == sp.zeros(DIM, DIM)
    print(f"  Ch_tilde == Casimir_su3 exactly (re-confirming Round 30)? {ch_tilde_eq_cas}")
    assert ch_tilde_eq_cas, "Round 30's own Ch_tilde=Casimir_su3 finding did not reproduce"

    print("\n" + "=" * 70)
    print("STEP B: re-verify trace(Casimir_su3)/DIM=1 via Casimir_su3=Id+X/3")
    print("(Round 29/33's OWN structural fact: X is a genuine degree-4")
    print("Clifford element, hence traceless BY CONSTRUCTION, not computed)")
    print("=" * 70)
    X1234 = sp.zeros(DIM, DIM)
    from g2su3_explicit_clifford import e_action

    for a, b, c, d in [(1, 2, 3, 4), (1, 2, 5, 6), (3, 4, 5, 6)]:
        cols = [e_action(a, e_action(b, e_action(c, e_action(d, unit_vec(i))))) for i in range(DIM)]
        X1234 += sp.Matrix.hstack(*cols)
    x_traceless = sp.simplify(sp.trace(X1234)) == 0
    print(f"  X:=Z1234+Z1256+Z3456 is traceless (pure degree-4, structural)? {x_traceless}")
    assert x_traceless, "X is not traceless -- structural premise fails"

    cas_minus_scalar = sp.simplify(Casimir_su3 - sp.trace(Casimir_su3) / DIM * Id8)
    x_over_3_matches = sp.simplify(cas_minus_scalar - X1234 / 3) == sp.zeros(DIM, DIM)
    print(f"  Casimir_su3 - (its own scalar part) == X/3 exactly? {x_over_3_matches}")
    assert x_over_3_matches, "Casimir_su3 != Id + X/3 -- load-bearing premise fails"

    trace_cas_over_8 = sp.simplify(sp.trace(Casimir_su3) / DIM)
    print("  => trace(Casimir_su3)/DIM = trace(Id)/DIM + trace(X/3)/DIM")
    print(f"     = 1 + 0 = {trace_cas_over_8} -- STRUCTURAL, no computation of the")
    print("     underlying su(3) generator matrices' trace was needed for THIS step.")
    assert trace_cas_over_8 == 1, f"trace(Casimir_su3)/DIM={trace_cas_over_8}, expected 1"

    print("\n" + "=" * 70)
    print("STEP C: walk through Ch_4's c=1 as a LOGICAL CONSEQUENCE of Ch_0 =")
    print("Tr(Ch_tilde)/DIM (Round 26, structural) = Tr(Casimir_su3)/DIM (STEP")
    print("A) = 1 (STEP B) -- NOTE (post-skeptic): this in-script check is")
    print("MECHANICALLY TAUTOLOGICAL with STEP A (Ch_tilde is DEFINED there as")
    print("Ch_0_direct*Id+Ch_4, so Ch_0_derived collapses back to Ch_0_direct")
    print("since Ch_4 is traceless) -- it adds ZERO fresh numeric evidence,")
    print("kept as a PEDAGOGICAL walkthrough of the dependency chain, not an")
    print("independent check. The genuine independence lives in Round 30's own")
    print("S1-S9 chain (which never references Ch_4) -- see claim.md.")
    print("=" * 70)
    Ch_0_derived = sp.simplify(sp.trace(Ch_tilde) / DIM)
    print(f"  Ch_0 derived as Tr(Ch_tilde)/DIM = {Ch_0_derived}")
    Ch_4_derived = sp.simplify(Casimir_su3 - Ch_0_derived * Id8)
    ch4_matches = sp.simplify(Ch_4_derived - Ch_4) == sp.zeros(DIM, DIM)
    print(
        f"  Ch_4 == Casimir_su3 - Ch_0*Id EXACTLY (c=1, algebraic corollary of STEP A)? {ch4_matches}"
    )
    assert ch4_matches, "derived Ch_4 does not match the actual Ch_4 -- derivation chain broken"
    print("  => Ch_4's c=1 follows from the dependency chain assembled in STEPs")
    print("  A-B, correcting Round 33 STEP D's backwards framing (that step")
    print("  used the SOLVED c=1 to re-derive Ch_tilde=Casimir_su3; the true")
    print("  dependency runs the other way) -- but the independence rests on")
    print("  TRUSTING Round 30's own structural chain, not on fresh evidence")
    print("  from this step itself.")

    print("\n" + "=" * 70)
    print("STEP D: NEW exact decomposition degree4_term = Ch_4 - (9/8)*Jm4,")
    print("where Jm4 is built PURELY from jac_m (T-table only, curv_h-")
    print("INDEPENDENT) -- not previously stated explicitly")
    print("=" * 70)

    def jm_coeff(i, j, k, ll):
        jm = jac_m(T, j, k, ll)
        return jm[i - 1]

    Jm4 = build_quartic_matrix(jm_coeff)
    decomp_ok = sp.simplify(degree4_term - (Ch_4 - sp.Rational(9, 8) * Jm4)) == sp.zeros(DIM, DIM)
    print(f"  degree4_term == Ch_4 - (9/8)*Jm4 exactly? {decomp_ok}")
    assert decomp_ok, "degree4_term does not decompose as Ch_4 - (9/8)*Jm4"

    print("\n" + "=" * 70)
    print("STEP E: Jm4 satisfies the SAME 3 premises Round 28's theorem needs")
    print("(SU(3)-equivariant, Swap-symmetric, Hermitian, traceless) -- so it")
    print("is ALSO forced into span{Casimir_su3-Id} by Round 33's degree-")
    print("counting argument, applied here to a NEW object")
    print("=" * 70)
    jm4_equiv_ok = True
    for k in range(1, 9):
        comm = sp.simplify(Ls[k] * Jm4 - Jm4 * Ls[k])
        if comm != sp.zeros(DIM, DIM):
            jm4_equiv_ok = False
    print(f"  Jm4 SU(3)-equivariant (all 8 generators)? {jm4_equiv_ok}")
    assert jm4_equiv_ok, "Jm4 is not SU(3)-equivariant"

    jm4_swap_ok = sp.simplify(Swap * Jm4 * Swap - Jm4) == sp.zeros(DIM, DIM)
    print(f"  Jm4 Swap-symmetric? {jm4_swap_ok}")
    assert jm4_swap_ok, "Jm4 is not Swap-symmetric"

    jm4_herm_ok = sp.simplify(Jm4.H - Jm4) == sp.zeros(DIM, DIM)
    print(f"  Jm4 Hermitian? {jm4_herm_ok}")
    assert jm4_herm_ok, "Jm4 is not Hermitian"

    jm4_trace_ok = sp.simplify(sp.trace(Jm4)) == 0
    print(f"  Jm4 traceless (pure degree-4, by construction)? {jm4_trace_ok}")
    assert jm4_trace_ok, "Jm4 is not traceless"

    print("\n" + "=" * 70)
    print("STEP F: solve for Jm4's own (a,b,c) in {H,Id,Casimir_su3} -- this")
    print("part is NOT yet structurally derived, same combinatorial-solve")
    print("status as Round 33's original c=1/c'=-5/4, just for a cleaner,")
    print("curv_h-independent object")
    print("=" * 70)

    def flat(M):
        return [M[r, c] for r in range(DIM) for c in range(DIM)]

    basis_mats = [H, Id8, Casimir_su3]
    Bcols = [sp.Matrix(flat(M)) for M in basis_mats]
    Basis_mat = sp.Matrix.hstack(*Bcols)
    rhs = sp.Matrix(flat(Jm4))

    import itertools

    found_rows = None
    for rows in itertools.combinations(range(Basis_mat.rows), 3):
        sub = Basis_mat[list(rows), :]
        if sub.det() != 0:
            found_rows = rows
            break
    assert found_rows is not None, "could not find 3 independent rows to solve the 3x3 system"
    sub = Basis_mat[list(found_rows), :]
    rhs_sub = rhs[list(found_rows), :]
    abc = sub.solve(rhs_sub)
    a_jm4, b_jm4, d_jm4 = abc
    print(f"  Jm4 -> (a,b,c) = ({a_jm4}, {b_jm4}, {d_jm4})")
    recon = sp.simplify(a_jm4 * H + b_jm4 * Id8 + d_jm4 * Casimir_su3)
    recon_ok = sp.simplify(recon - Jm4) == sp.zeros(DIM, DIM)
    print(f"  full 64-entry reconstruction exact? {recon_ok}")
    assert recon_ok, "Jm4 reconstruction from solved (a,b,c) does not match"
    assert a_jm4 == 0, f"expected a=0 (degree-counting), got a={a_jm4}"
    print(f"  Jm4 = {d_jm4}*(Casimir_su3 - Id) -- d={d_jm4}, matching the")
    print("  degree-counting argument (a=0, b=-c) exactly, same as Ch_4/")
    print("  degree4_term in Round 33.")

    print("\n" + "=" * 70)
    print("STEP G: ALGEBRAICALLY derive degree4_term's own c' from c=1 (STEP")
    print("C) and d=2 (STEP F) -- WITHOUT solving Round 28's 3x3 system for")
    print("degree4_term itself")
    print("=" * 70)
    c_ch4 = sp.Integer(1)
    c_prime_derived = sp.simplify(c_ch4 - sp.Rational(9, 8) * d_jm4)
    print(f"  c' = c(Ch_4) - (9/8)*d(Jm4) = {c_ch4} - (9/8)*{d_jm4} = {c_prime_derived}")
    degree4_reconstructed = sp.simplify(c_prime_derived * (Casimir_su3 - Id8))
    degree4_matches = sp.simplify(degree4_reconstructed - degree4_term) == sp.zeros(DIM, DIM)
    print(f"  c'*(Casimir_su3-Id) == degree4_term exactly? {degree4_matches}")
    assert degree4_matches, "algebraically-derived degree4_term does not match the actual object"
    assert c_prime_derived == sp.Rational(-5, 4), f"c'={c_prime_derived}, expected -5/4"
    print("  => degree4_term's c'=-5/4 is ALGEBRAICALLY REPRODUCED from c=1")
    print("  (STEP C, a corollary of STEP A -- see its own caveat) and d=2")
    print("  (STEP F, a genuine fresh combinatorial solve) -- the SAME 3x3")
    print("  solve is RELOCATED from degree4_term onto the cleaner, curv_h-")
    print("  independent Jm4, not eliminated. 'why -5/4' becomes 'why Jm4's")
    print("  own d=2' -- a different, more isolated question, not fewer solves.")

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("  Ch_4's c=1: a LOGICAL CONSEQUENCE (STEPS A-C) of 3 already-")
    print("  established facts (Ch_tilde=Casimir_su3, Casimir_su3=Id+X/3, both")
    print("  Rounds 29-30), correcting Round 33 STEP D's backwards framing --")
    print("  but the in-script STEP C demonstration is tautological with STEP")
    print("  A (see its own caveat); the independence rests on TRUSTING Round")
    print("  30's own structural chain (2 cited Lie-theory facts + a")
    print("  back-solved k=8 case), not on fresh evidence from this round.")
    print()
    print("  degree4_term's c'=-5/4: RELOCATED (STEPS D-G), not reduced in")
    print("  solve-count -- exact linear decomposition degree4_term=Ch_4-")
    print("  (9/8)*Jm4 moves the SAME combinatorial 3x3 solve onto a cleaner,")
    print("  curv_h-independent object (Jm4=2*(Casimir_su3-Id)). That fact")
    print("  (d=2) is NOT derived from a deeper principle here -- HONEST, not")
    print("  fully closed, and NOT fewer solves than before.")


if __name__ == "__main__":
    main()
