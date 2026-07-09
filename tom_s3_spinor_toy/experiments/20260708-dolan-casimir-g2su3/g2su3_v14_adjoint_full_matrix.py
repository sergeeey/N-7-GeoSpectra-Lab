"""
Round 20 (2026-07-09): the rho=14 danger zone -- G2's own 14-dim adjoint
representation. Builds the full multiplicity space M_14 = Hom_SU(3)(V_14,F)
and the complete D^2_14 matrix on it, reusing Rounds 17-19's already-
reviewed machinery wherever the abstract representation theory allows.

V_14 = adjoint(g2), restricted to the isotropy SU(3): the standard
REDUCTIVE decomposition g2 = h (+) m (h=su(3), 8-dim; m, 6-dim) gives
14 = 8 (adjoint of su(3) on itself) (+) 3 (+) 3bar (m's own branching,
IDENTICAL su(3)-representation data to what has been used since Round 8
via SU3_GENERATORS/AD_NU_M_BIVECTOR/ad_nu_m_trusted -- not rederived,
reused).

A GENUINE SIGN-CONVENTION BUG, CAUGHT AND FIXED THIS ROUND (before
reaching any downstream computation): the raw NU-matrix commutator
[nu_i,nu_j] (i,j=1..14), decomposed via decompose_g2, does NOT directly
satisfy the su(3) structure constants against itself when compared using
the SAME raw commutator as the "structure constant" -- initial attempts
to match V_14's own su(3)-action against Sigma's y1,y2,y3/y12,y13,y23
(via Sigma's OWN already-established su3_action convention) gave ONLY
the trivial (zero) Schur-intertwiner solution, for EVERY candidate
pairing tried. Diagnosed via a from-scratch self-consistency check
([ad(nu_i),ad(nu_j)] should equal a structure-constant combination of
ad(nu_k), tested independently of any target-matching): this test
FAILED for ad_nu_m_trusted's own e-basis matrices too, using UNSIGNED
raw structure constants -- but PASSED exactly when the RHS structure
constants were negated. This is Round 13's own "BRACKET_SIGN=-1" finding
(previously believed to apply only to m x m brackets), now shown to
apply UNIFORMLY to ALL raw-NU-commutator brackets relative to AHL2023's
own convention, including su(3) x su(3) structure constants.

CORRECTION (caught by skeptic review, this round): an earlier draft of
this docstring claimed "Sigma's own su3_action ... ALWAYS built via a RAW
matrix slice or RAW commutator" -- this is FACTUALLY WRONG. su3_action's
SU3_GENERATORS table (g2su3_twisted_kernel.py) is IDENTICAL to
AD_NU_M_BIVECTOR (g2su3_appendix_a_construction.py) -- i.e. su3_action is
built from the SAME independently-sourced AHL2023 Remark-5.2 bivector
formula that ad_nu_m_trusted uses (Clifford-LIFTED onto Sigma, rather than
applied as a vector-action on m, but the SAME source data), NOT a raw
NU-matrix commutator at all. It is neither "RAW" nor "BRACKET_SIGN-
corrected" in the sense those terms are used for nu-matrix-commutator
constructions -- it is a third, independent construction, and whether its
Clifford-LIFT of a given bivector carries the same relative sign as that
bivector's VECTOR-action (ad_nu_m_trusted) on m is exactly the kind of
lift-dependent convention question that is NOT resolved by inspection --
only by direct empirical matching (STEP 3/4, STEP 6, below).

RESOLUTION: Round 17-18's V_7 construction (rho7_nuk, rho7_ep) WAS built
via a RAW matrix slice (not a commutator at all -- V_7's e_p-action is a
direct NU[8+p] slice, no bracket involved). V_14's own su(3)-generator
action (needed for STEP 2-6, to find the 8/3/3bar branching and verify
equivariance) empirically matches su3_action ONLY under the RAW
(unsigned) nu-commutator convention -- verified directly, not assumed
(see (a)/(b) below). IMPORTANT SCOPE NOTE on what the
self-consistency check does and does NOT establish: negating a Lie
bracket globally gives an ISOMORPHIC algebra (X |-> -X is always a valid
automorphism g -> g^op), so BOTH the RAW and the BRACKET_SIGN-corrected
conventions are, EACH IN ISOLATION, internally self-consistent (verified
directly, tool -- both pass the same 91-pair check independently). Self-
consistency alone therefore does NOT prove RAW is the convention that
matches Sigma's side specifically -- it only rules out a construction
bug that would break the Lie algebra structure outright. The ACTUAL
proof that RAW is the correct choice HERE is the combination of: (a) the
Schur-intertwiner solves in STEP 3/4 against Sigma's independently-
established su3_action return genuine NONZERO solutions (det(T)!=0,
checked) only under RAW, never under BRACKET_SIGN-corrected (the
falsification signal that first surfaced this issue -- BRACKET_SIGN-
corrected gave ONLY the trivial solution against every candidate target
tried), and (b) STEP 6's full generic-symbolic-vector equivariance check
of the ASSEMBLED w_i intertwiners against build_su3_matrix64 (F's own,
independently-verified action) -- passing for all 12 basis elements
under a fully generic v is not explicable by coincidence.

V_14's OWN "3"/"3bar" (within m, RAW convention): diagonalized the
commuting Cartan pair on m exactly as Round 18 did for V_7 -- SAME
weight pattern found (0,-sqrt3 i/3),(-+i/2,sqrt3 i/6) etc, grouped by
sum-of-weights=0, closure-verified under all 8 generators. IMPORTANT:
the labeling came out SWAPPED relative to Round 18's V_7 naming
convention -- group1={B14,C14,D14} matches Sigma's "3bar" pattern
(y12,y13,y23), group2={A14,E14,F14} matches "3" (y1,y2,y3). (Verified,
not assumed -- both pairings tried, only one gives a nonzero Schur
solution each time, exactly the structural safety net this project's
prior rounds have relied on.)

V_14's OWN "8" (su(3) acting on itself): the raw structure constants
directly, an 8x8 representation, Casimir=3 confirmed.

F's SIDE: reuses Round 19's c1..c5 ("3"-copies) and d1..d5 ("3bar"-
copies) UNCHANGED -- no new F-side "3"/"3bar" construction needed, since
these are copies of the SAME abstract su(3) irreps regardless of which
G2-representation (V_7 or V_14) they intertwine with. NEW: F's "8"-
content, extracted from Lambda^1(x)Lambda^2 = 3(x)3bar = 8 (+) 1 (the
"1" part is Round 17's v_a) and Lambda^2(x)Lambda^1 = 3bar(x)3 = 8 (+) 1
(v_a's swap) -- Casimir spectrum on each 9-dim space confirmed
{0:mult1, 3:mult8} exactly, matching 8(+)1; the Casimir=3 nullspace (8
independent vectors each) gives the two "8"-copies, VERIFIED via the SU(3)
Casimir spectrum on F's full 64-dim space (Round 18: eigenvalue 3 has
mult 16 = 2*8, confirming these two ARE the full Hom(8,F), not a subset).

THE INTERTWINERS: T3 (V_14's group1="3bar" -> any di), T4 (V_14's
group2="3" -> any ci), T5/T6 (V_14's own 8 -> F's two 8-copies) -- all
SOLVED (Schur, sp.linsolve, not guessed), all nonzero (det!=0 checked).

THE D_14 FORMULA: identical structure to D_7's (Round 17, reused
verbatim: D(psi_{v,w})|_e = -sum_p e_p.w(rho_V(e_p)v) + D_on_simple_
tensor(w(v))) -- only "rho_V(e_p)" changes, now meaning ad(e_p) acting on
the FULL 14-dim adjoint via matrix commutator (the FORCED, unambiguous
meaning of "e_p's action" for the adjoint representation specifically --
unlike V_7, where rho7_ep required an independent slice-vs-e_action
calibration choice, V_14's ad(e_p) has no such freedom: it IS [e_p, -]
by definition of "adjoint representation").

OPEN CONCERN, RAISED BY SKEPTIC REVIEW, NOT FULLY CLOSED: is ADE[p]'s
RELATIVE SIGN against e_action(p) (the Clifford-multiplication half of
D_14's term1, via clifford_left_64, an INDEPENDENTLY-sourced convention
calibrated against AHL2023 Theorem 5.1) actually correct? Neither STEP
6's su(3)-equivariance check (which never touches ADE at all) nor STEP
9's self-adjointness check (D=+A+B and D=-A+B are BOTH self-adjoint if
A,B individually are -- self-adjointness cannot discriminate the sign)
constitute proof either way. TESTED DIRECTLY (not in this file --
recorded in decision.md Round 20): flipping ADE's sign and rebuilding
the full 12x12 matrix gives a DIFFERENT, IRRATIONAL spectrum
{6, 5-sqrt(217)/3, 5+sqrt(217)/3} (the ORIGINAL sign used here gives the
clean RATIONAL {6,20/3,10/3}, sharing 20/3 and 10/3 EXACTLY with rho=7's
own spectrum). Every Casimir-derived quantity found across this entire
20-round investigation has been rational in this normalization (Kostant-
Parthasarathy-type formulas produce Casimir DIFFERENCES, never generic
algebraic irrationals) -- the appearance of sqrt(217) under the flipped
sign is a strong plausibility argument AGAINST that sign, and FOR the
sign used here. This is STRUCTURAL/PLAUSIBILITY evidence, not a full
independent re-derivation via an actual twisted Kostant-Parthasarathy
formula for rho=14 (which would be fully decisive but was not attempted
this round -- the original literature search for exactly such a formula,
Round 15, found none exists in closed form for this specific twisted
setting). Status: STRONGLY SUPPORTED, not airtight -- see decision.md
Round 20 "Net assessment" for the full, honest scope statement.

RESULT: see main() for the actual 12x12 matrix and its eigenvalues.
"""

import sympy as sp

from g2su3_appendix_a_construction import BRACKET_SIGN, E_SIGN, decompose_g2, e, nu
from g2su3_equivariance_check import build_D_matrix64, build_su3_matrix64
from g2su3_explicit_clifford import DIM, IDX
from g2su3_v7_16dim_full_matrix import build_3_copies, build_3bar_copies
from g2su3_v7_3_3bar_intertwiners import build_MF
from g2su3_v7_multiplicity_dirac import clifford_left_64, idx64

N64 = DIM * DIM


def bv(a, b):
    v = sp.zeros(N64, 1)
    v[idx64(a, b)] = 1
    return v


def ad_gen_raw(a):
    """ad(nu_a) on the full 14-dim g2, RAW commutator (no BRACKET_SIGN) --
    the convention consistent with Sigma's own su3_action / V_7's rho7_ep
    (see docstring). a=1..14."""
    M = sp.zeros(14, 14)
    for k in range(1, 15):
        comm = sp.simplify(nu(a) * nu(k) - nu(k) * nu(a))
        coeffs = decompose_g2(comm)
        for idx_l, v in coeffs.items():
            M[idx_l - 1, k - 1] = v
    return M


def verify_full_adjoint_self_consistent(AD_RAW):
    def structure_const_raw(a, b):
        comm = sp.simplify(nu(a) * nu(b) - nu(b) * nu(a))
        return decompose_g2(comm)

    for a in range(1, 15):
        for b in range(a + 1, 15):
            lhs = sp.simplify(AD_RAW[a] * AD_RAW[b] - AD_RAW[b] * AD_RAW[a])
            c = structure_const_raw(a, b)
            rhs = sum((v * AD_RAW[d] for d, v in c.items()), sp.zeros(14, 14))
            if sp.simplify(lhs - rhs) != sp.zeros(14, 14):
                return False
    return True


def verify_bracket_sign_convention_also_self_consistent():
    """Demonstrates in-file (not just asserted in the docstring) that
    self-consistency ALONE cannot discriminate RAW from BRACKET_SIGN-
    corrected: negating a Lie bracket globally gives an isomorphic
    algebra (X |-> -X is always an automorphism g -> g^op), so BOTH
    conventions pass this test independently. The REAL discriminator
    (which convention matches Sigma's own su3_action) is the nonzero-
    Schur-intertwiner check in STEP 3/4 and the equivariance check in
    STEP 6, not this self-consistency check."""

    def ad_gen_corrected(a):
        M = sp.zeros(14, 14)
        for k in range(1, 15):
            comm = BRACKET_SIGN * sp.simplify(nu(a) * nu(k) - nu(k) * nu(a))
            coeffs = decompose_g2(comm)
            for idx_l, v in coeffs.items():
                M[idx_l - 1, k - 1] = v
        return M

    ad_corr = {a: ad_gen_corrected(a) for a in range(1, 15)}

    def structure_const_corrected(a, b):
        comm = BRACKET_SIGN * sp.simplify(nu(a) * nu(b) - nu(b) * nu(a))
        return decompose_g2(comm)

    for a in range(1, 15):
        for b in range(a + 1, 15):
            lhs = sp.simplify(ad_corr[a] * ad_corr[b] - ad_corr[b] * ad_corr[a])
            c = structure_const_corrected(a, b)
            rhs = sum((v * ad_corr[d] for d, v in c.items()), sp.zeros(14, 14))
            if sp.simplify(lhs - rhs) != sp.zeros(14, 14):
                return False
    return True


def build_v14_m_weight_vectors():
    """Diagonalize the commuting Cartan pair (ad(nu_7),ad(nu_8)) restricted
    to m (rows/cols 9..14 of the 14-dim adjoint), RAW convention. Returns
    (group1, group2) each a 6-vector basis (embedded in the 6-dim m-block)."""

    def ad_nuk_m_block_raw(i):
        M = sp.zeros(6, 6)
        for qcol in range(1, 7):
            comm = sp.simplify(nu(i) * nu(8 + qcol) - nu(8 + qcol) * nu(i))
            coeffs = decompose_g2(comm)
            for idx_l, v in coeffs.items():
                if idx_l > 8:
                    M[idx_l - 9, qcol - 1] = v
        return M

    mblock = {i: ad_nuk_m_block_raw(i) for i in range(1, 9)}
    sqrt = sp.sqrt
    H = sp.simplify(mblock[7] + sp.I * sqrt(2) * mblock[8])
    ev = H.eigenvects()
    weight_vecs = []
    for _val, _mult, vecs in ev:
        for v in vecs:
            idx = next(i for i in range(6) if v[i] != 0)
            w7 = sp.simplify((mblock[7] * v)[idx] / v[idx])
            w8 = sp.simplify((mblock[8] * v)[idx] / v[idx])
            weight_vecs.append((v, w7, w8))
    assert len(weight_vecs) == 6, f"expected 6 weight vectors, got {len(weight_vecs)}"

    # group by sum-of-weights == 0 (the su(3)-fundamental defining property)
    from itertools import combinations

    zero_sum_triples = []
    for combo in combinations(range(6), 3):
        wsum7 = sum(weight_vecs[i][1] for i in combo)
        wsum8 = sum(weight_vecs[i][2] for i in combo)
        if sp.simplify(wsum7) == 0 and sp.simplify(wsum8) == 0:
            zero_sum_triples.append(combo)
    assert len(zero_sum_triples) == 2, (
        f"expected exactly 2 complementary zero-weight-sum triples, got {len(zero_sum_triples)}"
    )
    combo1 = zero_sum_triples[0]
    combo2 = tuple(i for i in range(6) if i not in combo1)
    group1 = [weight_vecs[i][0] for i in combo1]
    group2 = [weight_vecs[i][0] for i in combo2]
    return group1, group2, mblock


def verify_closure_m(mblock, P_group, other_rows, Pinv):
    for i in range(1, 9):
        coeffs = Pinv * (mblock[i] * P_group)
        leak = coeffs[other_rows, :]
        if sp.simplify(leak) != sp.zeros(3, 3):
            return False
    return True


def build_MV14_m(mblock, P_group, row_slice, Pinv):
    out = {}
    for k in range(1, 9):
        coeffs = Pinv * (mblock[k] * P_group)
        out[k] = sp.simplify(coeffs[row_slice, :])
    return out


def solve_intertwiner_general(MV, MF, n, sol_index_hint=None):
    t = sp.symbols(f"t0:{n * n}")
    T = sp.Matrix(n, n, t)
    eqs = []
    for k in range(1, 9):
        diff = T * MV[k] - MF[k] * T
        for i in range(n):
            for j in range(n):
                if diff[i, j] != 0:
                    eqs.append(diff[i, j])
    sol_list = list(sp.linsolve(eqs, list(t)))
    sol = sol_list[0]
    free_syms = set()
    for c in sol:
        free_syms |= c.free_symbols
    assert free_syms, "solve_intertwiner_general found only the trivial solution -- wrong pairing"
    fs = list(free_syms)[0]
    return sp.Matrix(n, n, [c.subs(fs, 1) for c in sol])


def check_only_trivial_solution(MV, MF, n):
    """Companion to solve_intertwiner_general: verifies the REVERSE pairing
    (which Schur's lemma predicts must fail, given the forward pairing
    already found a nonzero solution) genuinely gives ONLY the trivial
    solution -- reviewer flagged (Round 20) that "both pairings tried"
    was previously only true in prose, not literally executed in-file."""
    t = sp.symbols(f"r0:{n * n}")
    T = sp.Matrix(n, n, t)
    eqs = []
    for k in range(1, 9):
        diff = T * MV[k] - MF[k] * T
        for i in range(n):
            for j in range(n):
                if diff[i, j] != 0:
                    eqs.append(diff[i, j])
    sol_list = list(sp.linsolve(eqs, list(t)))
    sol = sol_list[0]
    free_syms = set()
    for c in sol:
        free_syms |= c.free_symbols
    return not free_syms


def build_eight_copy(left_indices, right_indices, MV14_8):
    """Extract the Casimir=3 ('8') piece of Lambda(left)(x)Lambda(right)
    (either 3(x)3bar or 3bar(x)3), and solve the Schur intertwiner against
    V_14's own adjoint action MV14_8."""
    basis9 = [bv(a, b) for a in left_indices for b in right_indices]
    P9 = sp.Matrix.hstack(*basis9)
    Sk = {k: build_su3_matrix64(k) for k in range(1, 9)}
    MV9 = {}
    for k in range(1, 9):
        img = Sk[k] * P9
        MV9[k] = sp.simplify((P9.H * P9).inv() * (P9.H * img))
    Cas9 = sp.zeros(9, 9)
    for k in range(1, 9):
        Cas9 += -(MV9[k] * MV9[k])
    Cas9 = sp.simplify(Cas9)
    ns = (Cas9 - 3 * sp.eye(9)).nullspace()
    assert len(ns) == 8, f"expected 8-dim Casimir=3 nullspace, got {len(ns)}"

    def embed(v9):
        out = sp.zeros(N64, 1)
        for i in range(9):
            out += v9[i] * basis9[i]
        return sp.simplify(out)

    eight = [embed(v) for v in ns]
    P8 = sp.Matrix.hstack(*eight)
    MF_8 = {}
    for k in range(1, 9):
        img = Sk[k] * P8
        MF_8[k] = sp.simplify((P8.H * P8).inv() * (P8.H * img))
    T = solve_intertwiner_general(MV14_8, MF_8, 8)
    assert sp.simplify(T.det()) != 0
    return eight, T


def build_ad_ep_raw():
    """ad(e_p) on the full 14-dim g2, p=1..6, RAW convention (E_SIGN-
    corrected), for the D_14 formula's first term. Self-consistency with
    the full g2 bracket verified in main()."""
    ADE = {}
    for p in range(1, 7):
        M = sp.zeros(14, 14)
        for k in range(1, 15):
            comm = sp.simplify(e(p) * nu(k) - nu(k) * e(p))
            coeffs = decompose_g2(comm)
            for idx_l, v in coeffs.items():
                M[idx_l - 1, k - 1] = v
        ADE[p] = M
    return ADE


def d14_apply(w_cols, D64, ADE, ade_sign=1):
    """w_cols: list of 14 vectors in F, w_cols[i] = w(basis vector i of
    V_14, i=0..13 <-> nu_1..nu_14). Same D_14 formula as d7_apply, with
    V_7's rho7_ep replaced by V_14's own ad(e_p) (ADE). ADE[p] is already
    built directly from e(p) = E_SIGN[p]*nu_{8+p} (see build_ad_ep_raw),
    so it already IS ad(e_p) -- no further E_SIGN scaling here (an
    earlier draft double-applied E_SIGN, caught by the ADE-vs-AD_RAW
    self-consistency check in main()). ade_sign is a diagnostic-only
    override (default +1, the reviewed/used value) -- see main() STEP 10,
    which uses ade_sign=-1 to test the skeptic-flagged relative-sign
    concern against e_action; NOT a free parameter of the physics."""
    new_cols = []
    for i in range(14):
        v = sp.zeros(14, 1)
        v[i] = 1
        term2 = sp.simplify(D64 * w_cols[i])
        term1 = sp.zeros(N64, 1)
        for p in range(1, 7):
            Mp = ade_sign * ADE[p]
            ad_ep_v = Mp * v
            w_of_that = sp.zeros(N64, 1)
            for j in range(14):
                if ad_ep_v[j] != 0:
                    w_of_that += ad_ep_v[j] * w_cols[j]
            term1 += clifford_left_64(p, w_of_that)
        new_cols.append(sp.simplify(-term1 + term2))
    return new_cols


def flatten14(w_cols):
    return sp.Matrix.vstack(*w_cols)


def main():
    print("=" * 70)
    print("STEP 1: sign-convention self-consistency check (RAW adjoint rep)")
    print("=" * 70)
    AD_RAW = {a: ad_gen_raw(a) for a in range(1, 15)}
    consistent = verify_full_adjoint_self_consistent(AD_RAW)
    print(f"  full 14x14 RAW adjoint representation self-consistent (91 pairs): {consistent}")
    assert consistent
    consistent_corr = verify_bracket_sign_convention_also_self_consistent()
    print(f"  BRACKET_SIGN-corrected convention ALSO self-consistent: {consistent_corr}")
    print(
        "  (both pass -- self-consistency alone cannot pick RAW; STEP 3/4's nonzero"
        " Schur intertwiners + STEP 6's equivariance check are the real discriminator)"
    )

    print("\n" + "=" * 70)
    print("STEP 2: V_14's own m -- weight-diagonalize, group, verify closure")
    print("=" * 70)
    group1_vecs, group2_vecs, mblock = build_v14_m_weight_vectors()
    P_g1 = sp.Matrix.hstack(*group1_vecs)
    P_g2 = sp.Matrix.hstack(*group2_vecs)
    Pfull = sp.Matrix.hstack(*group1_vecs, *group2_vecs)
    Pinv = Pfull.inv()
    ok1 = verify_closure_m(mblock, P_g1, slice(3, 6), Pinv)
    ok2 = verify_closure_m(mblock, P_g2, slice(0, 3), Pinv)
    print(f"  group1 closed under su(3): {ok1}")
    print(f"  group2 closed under su(3): {ok2}")
    assert ok1 and ok2

    MV14_g1 = build_MV14_m(mblock, P_g1, slice(0, 3), Pinv)
    MV14_g2 = build_MV14_m(mblock, P_g2, slice(3, 6), Pinv)
    MF_3 = build_MF([(1,), (2,), (3,)])
    MF_3bar = build_MF([(1, 2), (1, 3), (2, 3)])

    print("\n" + "=" * 70)
    print("STEP 3: solve which group is '3' vs '3bar' -- forward pairing solved,")
    print("reverse pairing explicitly checked to give ONLY the trivial solution")
    print("(reviewer flagged: previously only claimed in prose, not executed)")
    print("=" * 70)
    T3 = solve_intertwiner_general(MV14_g1, MF_3bar, 3)
    T4 = solve_intertwiner_general(MV14_g2, MF_3, 3)
    print(f"  group1 -> '3bar' via T3, det(T3)={sp.simplify(T3.det())}")
    print(f"  group2 -> '3' via T4, det(T4)={sp.simplify(T4.det())}")
    rev1_trivial = check_only_trivial_solution(MV14_g1, MF_3, 3)
    rev2_trivial = check_only_trivial_solution(MV14_g2, MF_3bar, 3)
    print(f"  reverse group1 -> '3' gives ONLY trivial solution: {rev1_trivial}")
    print(f"  reverse group2 -> '3bar' gives ONLY trivial solution: {rev2_trivial}")
    assert rev1_trivial and rev2_trivial

    print("\n" + "=" * 70)
    print("STEP 4: V_14's own '8' (su(3) on itself), F's two '8'-copies")
    print("=" * 70)

    def ad_nuk_su3block_raw(i):
        M = sp.zeros(8, 8)
        for k in range(1, 9):
            comm = sp.simplify(nu(i) * nu(k) - nu(k) * nu(i))
            coeffs = decompose_g2(comm)
            for idx_l, v in coeffs.items():
                if idx_l <= 8:
                    M[idx_l - 1, k - 1] = v
        return M

    MV14_8 = {i: ad_nuk_su3block_raw(i) for i in range(1, 9)}
    y1i, y2i, y3i = IDX[(1,)], IDX[(2,)], IDX[(3,)]
    y12i, y13i, y23i = IDX[(1, 2)], IDX[(1, 3)], IDX[(2, 3)]
    eight_L, T5 = build_eight_copy([y1i, y2i, y3i], [y23i, y13i, y12i], MV14_8)
    eight_R, T6 = build_eight_copy([y23i, y13i, y12i], [y1i, y2i, y3i], MV14_8)
    print(f"  eight_L (from Lambda1(x)Lambda2): det(T5)={sp.simplify(T5.det())}")
    print(f"  eight_R (from Lambda2(x)Lambda1): det(T6)={sp.simplify(T6.det())}")

    print("\n" + "=" * 70)
    print("STEP 5: reuse Round 19's F-side '3'/'3bar' copies, build 12 w_i's")
    print("=" * 70)
    threes = build_3_copies()  # c1..c5, reused unchanged
    threebars = build_3bar_copies()  # d1..d5, reused unchanged

    # V_14 basis ordering: local index 0..7 = nu_1..nu_8 (su(3)), 8..13 = m
    def build_w14_su3(T, eight_target):
        cols = []
        for j in range(8):
            ej3 = sp.zeros(8, 1)
            ej3[j] = 1
            mapped = T * ej3
            vecF = sum((mapped[row] * eight_target[row] for row in range(8)), sp.zeros(N64, 1))
            cols.append(sp.simplify(vecF))
        cols += [sp.zeros(N64, 1) for _ in range(6)]
        return cols

    def build_w14_m(T, target_vecs, group_P, this_rows):
        cols = [sp.zeros(N64, 1) for _ in range(8)]
        I6 = sp.eye(6)
        for j in range(6):
            ej = I6[:, j]
            coeffs = Pinv * ej
            group_coeffs = coeffs[this_rows, :]
            mapped = T * group_coeffs
            vecF = sum((mapped[row] * target_vecs[row] for row in range(3)), sp.zeros(N64, 1))
            cols.append(sp.simplify(vecF))
        return cols

    basis_w = []
    labels = []
    basis_w.append(build_w14_su3(T5, eight_L))
    labels.append("eight_L")
    basis_w.append(build_w14_su3(T6, eight_R))
    labels.append("eight_R")
    for i, triple in enumerate(threes):
        basis_w.append(build_w14_m(T4, triple, P_g2, slice(3, 6)))
        labels.append(f"three_{i + 1}")
    for i, triple in enumerate(threebars):
        basis_w.append(build_w14_m(T3, triple, P_g1, slice(0, 3)))
        labels.append(f"threebar_{i + 1}")
    print(f"  built {len(basis_w)} intertwiners: {labels}")

    print("\n" + "=" * 70)
    print("STEP 6: verify all 12 are SU(3)-equivariant (symbolic, generic v)")
    print("=" * 70)

    def verify_v14_equivariance(w_cols, label):
        c = sp.symbols("c0:14")
        v_generic = sp.Matrix(c)
        ok = True
        for k in range(1, 9):
            Mk_su3 = MV14_8.get(k)
            Mk_m = mblock[k]
            rho_v_su3 = Mk_su3 * v_generic[0:8, :]
            rho_v_m = Mk_m * v_generic[8:14, :]
            rho_v = sp.Matrix.vstack(rho_v_su3, rho_v_m)
            w_of_rho_v = sp.zeros(N64, 1)
            for j in range(14):
                if rho_v[j] != 0:
                    w_of_rho_v += rho_v[j] * w_cols[j]
            Sk = build_su3_matrix64(k)
            w_v = sp.zeros(N64, 1)
            for j in range(14):
                if v_generic[j] != 0:
                    w_v += v_generic[j] * w_cols[j]
            rhs = Sk * w_v
            if sp.simplify(w_of_rho_v - rhs) != sp.zeros(N64, 1):
                ok = False
        print(f"  {label}: equivariant = {ok}")
        assert ok
        return ok

    for w, label in zip(basis_w, labels, strict=True):
        verify_v14_equivariance(w, label)

    print("\n" + "=" * 70)
    print("STEP 7: e_p-action self-consistency + build ADE for D_14")
    print("=" * 70)
    ADE = build_ad_ep_raw()
    # cross-check: ADE[p] = ad(e_p) = ad(E_SIGN[p]*nu_{8+p}) = E_SIGN[p]*
    # ad(nu_{8+p}) = E_SIGN[p]*AD_RAW[8+p] -- confirms build_ad_ep_raw
    # (built directly from e(p)) and ad_gen_raw (built from nu_{8+p} alone)
    # agree once the E_SIGN factor is accounted for correctly.
    consistent2 = all(
        sp.simplify(ADE[p] - E_SIGN[p] * AD_RAW[8 + p]) == sp.zeros(14, 14) for p in range(1, 7)
    )
    print(f"  ADE[p] == E_SIGN[p]*AD_RAW[8+p] (consistency): {consistent2}")
    assert consistent2

    print("\n" + "=" * 70)
    print("STEP 8: build W (896x12), apply D_14 twice, extract 12x12 matrix")
    print("=" * 70)
    D64 = build_D_matrix64()
    W = sp.Matrix.hstack(*[flatten14(w) for w in basis_w])
    print(f"  W shape: {W.shape}, rank: {W.rank()} (want 12)")
    WH = W.H
    WtW_inv = (WH * W).inv()

    D2_cols = []
    for i, w in enumerate(basis_w):
        w_prime = d14_apply(w, D64, ADE)
        w_double = d14_apply(w_prime, D64, ADE)
        target = flatten14(w_double)
        c = sp.simplify(WtW_inv * (WH * target))
        residual = sp.simplify(W * c - target)
        exact = residual == sp.zeros(14 * N64, 1)
        print(f"  D^2_14({labels[i]}): exact-in-span={exact}")
        assert exact, f"D^2_14({labels[i]}) is NOT exactly in span(basis)"
        D2_cols.append(c)

    D2_MAT = sp.Matrix.hstack(*D2_cols)
    print("\nFull 12x12 matrix of D^2_14 on M_14:")
    sp.pprint(D2_MAT)

    print("\n" + "=" * 70)
    print("STEP 9: eigenvalues + trace cross-check + self-adjointness")
    print("=" * 70)
    eigs = D2_MAT.eigenvals()
    for val, mult in eigs.items():
        print(f"  eigenvalue = {sp.simplify(val)}   multiplicity = {mult}")
    trace = sp.simplify(sum(sp.simplify(v) * m for v, m in eigs.items()))
    trace_direct = sp.simplify(sum(D2_MAT[i, i] for i in range(12)))
    print(f"  trace (from eigenvalue sum) = {trace}, trace (direct) = {trace_direct}")
    assert sp.simplify(trace - trace_direct) == 0

    G = sp.simplify(WH * W)
    GD = sp.simplify(G * D2_MAT)
    is_hermitian = sp.simplify(GD.H - GD) == sp.zeros(12, 12)
    print(
        f"  D_14 self-adjoint w.r.t. natural L2 inner product (G.D2_MAT Hermitian): {is_hermitian}"
    )
    assert is_hermitian, "D_14 not self-adjoint -- reviewer flagged this was only printed before"

    has_zero = any(sp.simplify(val) == 0 for val in eigs)
    print(f"\nZero eigenvalue present (unwanted zero mode in rho=14): {has_zero}")
    assert not has_zero, "zero eigenvalue found -- reviewer flagged this was only printed before"

    print("\n" + "=" * 70)
    print("STEP 10: skeptic-flagged concern -- is ADE's sign (relative to")
    print("e_action, the Clifford half of term1) actually pinned down? Self-")
    print("adjointness (STEP 9) canNOT discriminate: D=+A+B and D=-A+B are")
    print("BOTH self-adjoint if A,B individually are. Test: flip ADE's sign,")
    print("rebuild the full matrix, compare the resulting spectrum.")
    print("=" * 70)
    D2_cols_flipped = []
    for w in basis_w:
        w_prime = d14_apply(w, D64, ADE, ade_sign=-1)
        w_double = d14_apply(w_prime, D64, ADE, ade_sign=-1)
        target = flatten14(w_double)
        c = sp.simplify(WtW_inv * (WH * target))
        D2_cols_flipped.append(c)
    D2_MAT_flipped = sp.Matrix.hstack(*D2_cols_flipped)
    eigs_flipped = D2_MAT_flipped.eigenvals()
    print(f"  ORIGINAL (ade_sign=+1) eigenvalues: {dict(eigs)}")
    print(f"  FLIPPED  (ade_sign=-1) eigenvalues: {dict(eigs_flipped)}")
    orig_rational = all(v.is_rational for v in eigs)
    flipped_rational = all(v.is_rational for v in eigs_flipped)
    print(f"  ORIGINAL spectrum all rational: {orig_rational}")
    print(f"  FLIPPED  spectrum all rational: {flipped_rational}")
    print(
        "  Every Casimir-derived quantity found across this entire 20-round"
        " investigation has been rational in this normalization (Kostant-"
        "Parthasarathy-type formulas give Casimir DIFFERENCES, never generic"
        " algebraic irrationals) -- ORIGINAL being rational and FLIPPED not"
        " is a real, but NOT fully decisive, plausibility argument FOR the"
        " sign used in this file. This is STRUCTURAL evidence, not an"
        " independent re-derivation via an actual closed-form twisted"
        " Kostant-Parthasarathy formula for rho=14 (none was found in"
        " Round 15's literature search) -- see decision.md Round 20 for"
        " the full, honestly-scoped status."
    )


if __name__ == "__main__":
    main()
