"""
Round 16 (2026-07-09), UPDATED after independent review: this file does
NOT resolve the rho=7 danger-zone question. A reviewer pass confirmed
every arithmetic/sign step here is correct (including the fix for a
previously-hardcoded R^E value, see RE_3 below) -- but an adversarial,
context-blind skeptic pass found a DECISIVE flaw in the calibration
logic: the L4B ground-truth check (Step 3) only constrains the
(Scal+R^E) coefficient, because nabla*nabla=0 identically at the
rho=trivial calibration point -- it says NOTHING about the coefficient
on nabla*nabla itself, the ONE term that actually depends on rho.
"Interp A" and "Interp B" below are two arbitrary samples from an
UNCONSTRAINED one-parameter family, not two independent hypotheses whose
agreement constitutes evidence. See decision.md's "Round 16 continued"
section (FALSIFIED verdict, Concern 3) for the full finding and the
task list for what would actually resolve this. Task #7 remains OPEN.

The rest of this docstring documents what WAS verified (a genuinely
useful, reusable, well-calibrated R^E construction) -- kept for
reference, not as a claim that the headline conclusion holds.

---

ORIGINAL (now-superseded) framing: the twisted Schrodinger-
Lichnerowicz-Weitzenbock route for the rho=7 danger-zone verdict,
following the literature-search lead from Round 15 continued
(decision.md): since t=1/2 is EXACTLY the torsion-free Levi-Civita
connection, the standard twisted formula

    D^2_{S(x)E} = nabla*nabla + (1/4)*Scal_g + R^E

applies directly, with NO need for Agricola's torsion-family machinery
(hence no analog of the problematic "-calH" linear term that broke
Round 15's g2su3_twisted_Ch_attempt.py).

INGREDIENTS (all built/verified in this file):
1. R_half(p,q,r): the FULL Riemann curvature tensor R^{1/2}(e_p,e_q)e_r
   of the Levi-Civita connection, via Agricola 2002 Lemma 2.2 (the
   GENERAL formula, not just the sectional-curvature contraction used
   in earlier rounds):
     R^t(X,Y)Z = t^2[X,[Y,Z]_m]_m + t^2[Y,[Z,X]_m]_m + t[Z,[X,Y]_m]_m
                 + [Z,[X,Y]_h]
   built from T (torsion) and curvature_h (Round 13), using the bracket
   sign convention [e_p,e_q]_m = -sum_k T(p,q,k) e_k -- discovered THIS
   round by directly comparing against the already-calibrated
   LEVI_CIVITA_NOMIZU data (T's sign convention is opposite to a naive
   reading of Agricola's own T(X,Y,Z)=<[X,Y]_m,Z> -- consistent with
   AHL2023 using a different convention than Agricola 2002, the SAME
   kind of convention mismatch already found and resolved for the
   G2 Casimir normalization earlier this session).

   VERIFIED (structural, non-trivial):
   - R(p,q,r) = -R(q,p,r) for all tested triples (antisymmetry in the
     first two arguments)
   - <R(p,q)e_r,e_s> = -<R(p,q)e_s,e_r> (skew-symmetry as an so(6)
     operator)
   - The Ricci tensor obtained by contracting R_half EXACTLY reproduces
     Agricola's OWN independently-stated Ricci formula (Lemma 2.2's
     second display) -- Ric(e_p,e_p)=5/3, off-diagonal 0, for all
     tested p. Scal^{1/2}=10 (trace), matching the SEPARATE, simpler
     scalar-curvature-only formula computed independently.

2. R^E (64x64): the curvature-endomorphism term of the standard twisted
   Lichnerowicz formula, R^E(eta(x)xi) = sum_{p<q} (e_p.e_q.eta)(x)
   (Rspin_half(p,q).xi), where Rspin_half is R_half's spin(6)/Clifford
   lift (via the SAME general lift pattern independently calibrated
   against nabla_g_action -- see spin_lift_so6 below, corrected for a
   double-counted 1/2 factor found and fixed this round).

   VERIFIED: exactly SU(3)-equivariant (all 8 generators, zero
   residual) -- non-automatic, non-trivial pass.

CALIBRATION (the decisive test): the assembled formula
  D^2(rho,sigma) "=" [C_2(G2;rho)-C_2(SU(3);sigma)] + (1/4)*Scal + R^E
tested against the L4B ground truth (rho=trivial, D^2(v_a)=v_a+3*v_b
and D^2(v_b)=v_a+3*v_b, independently established via direct matrix
squaring of D_on_simple_tensor) gives EXACTLY (2/3) of the true answer,
for BOTH v_a and v_b independently -- a clean, uniform, non-coincidental
scale factor (not a structural mismatch: the RELATIVE proportions
between v_a/v_b components already match the truth exactly).

REMAINING AMBIGUITY (honestly flagged, does NOT affect the conclusion):
it is not yet resolved from first principles whether the missing 3/2
factor applies ONLY to (Scal+R^E) [Interpretation A -- since the
Casimir-eigenvalue relation "nabla*nabla=C_2(G2;rho)-C_2(SU(3);sigma)"
rests on Agricola's own proven theorem plus this session's independent
verification that Ctilde_h's eigenvalues equal C_2(SU(3);sigma) exactly,
giving no a priori reason to expect it needs the SAME empirical scale
correction], or to the WHOLE formula uniformly [Interpretation B -- a
Clifford-algebra normalization convention mismatch would plausibly hit
every term the same way]. BOTH interpretations were tested on ALL THREE
SU(3)-pieces relevant to rho=7's branching (7|SU(3)=3(+)3bar(+)1) and
give STRICTLY POSITIVE eigenvalues in every case -- see main().
"""

import itertools

import sympy as sp

from g2su3_appendix_a_construction import ad_nu_m_trusted, BRACKET_SIGN, build_curvature_h_table
from g2su3_equivariance_check import build_D_matrix64, build_su3_matrix64
from g2su3_explicit_clifford import (
    DIM,
    IDX,
    SUBSETS,
    clifford_mult_bivector_direct,
    e_action,
    vec_from_subsets,
)
from g2su3_H_element import build_T_table

N64 = DIM * DIM


def idx64(a, b):
    return DIM * a + b


def curv_h_lookup(curv_h, p, q, k):
    if p < q:
        return curv_h.get((p, q, k), 0)
    if p > q:
        return -curv_h.get((q, p, k), 0)
    return 0


def bracket_e_nu(a, k):
    """[e_a, nu_k] as a 6-dim m-vector (already-trusted data, reused from
    the Round 14/15 curvature_h construction)."""
    return {r: BRACKET_SIGN * ad_nu_m_trusted(k, a)[r - 1] for r in range(1, 7)}


def build_R_half(T, curv_h):
    """R^{1/2}(e_p,e_q)e_r via Agricola 2002 Lemma 2.2 at t=1/2, using
    [e_a,e_b]_m = -sum_k T(a,b,k) e_k (sign convention pinned down this
    round by direct comparison against LEVI_CIVITA_NOMIZU)."""

    def R_half(p, q, r):
        result = {s: sp.Integer(0) for s in range(1, 7)}
        for k in range(1, 7):
            tqr = T.get((q, r, k), 0)
            if tqr == 0:
                continue
            for s in range(1, 7):
                tpk = T.get((p, k, s), 0)
                if tpk == 0:
                    continue
                result[s] += sp.Rational(1, 4) * tqr * tpk
        for k in range(1, 7):
            trp = T.get((r, p, k), 0)
            if trp == 0:
                continue
            for s in range(1, 7):
                tqk = T.get((q, k, s), 0)
                if tqk == 0:
                    continue
                result[s] += sp.Rational(1, 4) * trp * tqk
        for k in range(1, 7):
            tpq = T.get((p, q, k), 0)
            if tpq == 0:
                continue
            for s in range(1, 7):
                trk = T.get((r, k, s), 0)
                if trk == 0:
                    continue
                result[s] += sp.Rational(1, 2) * tpq * trk
        for k in range(1, 9):
            c = curv_h_lookup(curv_h, p, q, k)
            if c == 0:
                continue
            ben = bracket_e_nu(r, k)
            for s in range(1, 7):
                result[s] += c * ben[s]
        return {s: sp.simplify(v) for s, v in result.items()}

    return R_half


def Rmat(R_half, p, q):
    M = sp.zeros(6, 6)
    for r in range(1, 7):
        Rr = R_half(p, q, r)
        for s in range(1, 7):
            M[r - 1, s - 1] = Rr[s]
    return M


def spin_lift_so6(M6, vec):
    """Lift of an so(6) operator M (M6[i-1,j-1]=<M(e_i),e_j> for i<j) into
    spin(6)/Clifford algebra, acting on vec. Calibrated this round: this
    formula (with NO extra prefactor -- clifford_mult_bivector_direct
    already carries the needed 1/2) exactly reproduces nabla_g_action
    when M = Lambda_m^{1/2}(e_p), built directly from LEVI_CIVITA_NOMIZU."""
    out = sp.zeros(DIM, 1)
    for i in range(1, 7):
        for j in range(i + 1, 7):
            c = M6[i - 1, j - 1]
            if c == 0:
                continue
            out += c * clifford_mult_bivector_direct(i, j, vec)
    return out


def build_RE(R_half):
    basis = [vec_from_subsets({s: 1}) for s in SUBSETS]
    RE = sp.zeros(N64, N64)
    for a in range(DIM):
        eta = basis[a]
        for b in range(DIM):
            xi = basis[b]
            col = idx64(a, b)
            out = sp.zeros(N64, 1)
            for p in range(1, 7):
                for q in range(p + 1, 7):
                    Rspin_xi = spin_lift_so6(Rmat(R_half, p, q), xi)
                    if Rspin_xi == sp.zeros(DIM, 1):
                        continue
                    epeq_eta = e_action(p, e_action(q, eta))
                    for r in range(DIM):
                        if epeq_eta[r] == 0:
                            continue
                        for s in range(DIM):
                            if Rspin_xi[s] == 0:
                                continue
                            out[idx64(r, s)] += epeq_eta[r] * Rspin_xi[s]
            RE[:, col] = out
    return sp.simplify(RE)


def main():
    T = build_T_table()
    curv_h = build_curvature_h_table()
    R_half = build_R_half(T, curv_h)

    print("=" * 70)
    print("STEP 1: Ricci/Scalar cross-check against Agricola's own Lemma 2.2")
    print("=" * 70)

    def ricci_via_R(p, q):
        return sp.simplify(sum(R_half(p, i, i)[q] for i in range(1, 7)))

    def ricci_via_formula(p, q):
        total_m = sum(
            T.get((p, i, k), 0) * T.get((q, i, k), 0) for i in range(1, 7) for k in range(1, 7)
        )
        total_h = sum(
            curv_h_lookup(curv_h, p, i, k) * curv_h_lookup(curv_h, q, i, k)
            for i in range(1, 7)
            for k in range(1, 9)
        )
        return sp.simplify(sp.Rational(1, 4) * total_m + total_h)

    ricci_ok = all(
        sp.simplify(ricci_via_R(p, q) - ricci_via_formula(p, q)) == 0
        for p, q in itertools.product(range(1, 7), range(1, 7))
    )
    print(f"  Ricci contraction of R_half matches Agricola's own formula exactly? {ricci_ok}")
    scal = sp.simplify(sum(ricci_via_R(p, p) for p in range(1, 7)))
    print(f"  Scal^(1/2) = {scal}")

    print("\n" + "=" * 70)
    print("STEP 2: build R^E (64x64), check SU(3)-equivariance")
    print("=" * 70)
    RE = build_RE(R_half)
    equivariant = True
    for i in range(1, 9):
        S = build_su3_matrix64(i)
        comm = sp.simplify(RE * S - S * RE)
        nz = sum(1 for r in range(N64) for c in range(N64) if sp.simplify(comm[r, c]) != 0)
        equivariant &= nz == 0
    print(f"  R^E exactly SU(3)-equivariant (all 8 generators)? {equivariant}")

    print("\n" + "=" * 70)
    print("STEP 3: calibrate against L4B ground truth (rho=trivial)")
    print("=" * 70)
    y1, y2, y3 = IDX[(1,)], IDX[(2,)], IDX[(3,)]
    y12, y13, y23 = IDX[(1, 2)], IDX[(1, 3)], IDX[(2, 3)]
    one, y123 = IDX[()], IDX[(1, 2, 3)]

    v_a = sp.zeros(N64, 1)
    v_a[idx64(y1, y23)] = 1
    v_a[idx64(y2, y13)] = -1
    v_a[idx64(y3, y12)] = 1
    v_b = sp.zeros(N64, 1)
    v_b[idx64(y123, one)] = 1

    D = build_D_matrix64()
    D2 = sp.simplify(D * D)
    D2_va, D2_vb = sp.simplify(D2 * v_a), sp.simplify(D2 * v_b)
    RE_va, RE_vb = sp.simplify(RE * v_a), sp.simplify(RE * v_b)

    naive_va = sp.simplify(sp.Rational(scal, 4) * v_a + RE_va)
    naive_vb = sp.simplify(sp.Rational(scal, 4) * v_b + RE_vb)
    scale_va = sp.simplify(sp.Rational(3, 2) * naive_va - D2_va) == sp.zeros(N64, 1)
    scale_vb = sp.simplify(sp.Rational(3, 2) * naive_vb - D2_vb) == sp.zeros(N64, 1)
    print(f"  (3/2)*[(1/4)Scal+R^E](v_a) == TRUE D^2(v_a)? {scale_va}")
    print(f"  (3/2)*[(1/4)Scal+R^E](v_b) == TRUE D^2(v_b)? {scale_vb}")
    print("  (uniform residual scale factor 3/2, same on two independent test vectors)")

    print("\n" + "=" * 70)
    print("STEP 4: assemble rho=7 verdict on all 3 relevant SU(3) pieces")
    print("=" * 70)
    M = sp.Matrix(
        [
            [RE_va[idx64(y1, y23)], RE_vb[idx64(y1, y23)]],
            [RE_va[idx64(y123, one)], RE_vb[idx64(y123, one)]],
        ]
    )
    C2_G2_7 = 2  # this session's resolved value, AHL2023/B_0-basis units
    C2_SU3_1, C2_SU3_3 = 0, sp.Rational(4, 3)

    def interp_A(c2_g2, base):
        return c2_g2 * sp.eye(base.shape[0]) + sp.Rational(3, 2) * (
            sp.Rational(scal, 4) * sp.eye(base.shape[0]) + base
        )

    def interp_B(c2_g2, base):
        return sp.Rational(3, 2) * (
            c2_g2 * sp.eye(base.shape[0]) + sp.Rational(scal, 4) * sp.eye(base.shape[0]) + base
        )

    D2_A_singlet = interp_A(C2_G2_7 - C2_SU3_1, M)
    D2_B_singlet = interp_B(C2_G2_7 - C2_SU3_1, M)
    print(f"  singlet piece, Interp A eigenvalues: {D2_A_singlet.eigenvals()}")
    print(f"  singlet piece, Interp B eigenvalues: {D2_B_singlet.eigenvals()}")

    # Round 16 continued (reviewer P1 fix): RE_3 was a bare hardcoded
    # literal here, unverified within this file. Now derived live: R^E
    # on all three "3"-piece basis vectors (y1(x)1, y2(x)1, y3(x)1) must
    # agree exactly (Schur's lemma -- SU(3)-equivariant operator on a
    # multiplicity-1 irrep is forced to act as a scalar), matching the
    # SAME live-derivation pattern already used for the singlet M matrix.
    RE_3_candidates = []
    for a in (y1, y2, y3):
        v3 = sp.zeros(N64, 1)
        v3[idx64(a, one)] = 1
        RE_v3 = sp.simplify(RE * v3)
        RE_3_candidates.append(sp.simplify(RE_v3[idx64(a, one)]))
        off_diagonal = sp.simplify(RE_v3 - RE_3_candidates[-1] * v3)
        assert off_diagonal == sp.zeros(N64, 1), f"R^E not scalar on '3' piece at a={a}"
    assert RE_3_candidates[0] == RE_3_candidates[1] == RE_3_candidates[2], (
        f"R^E disagrees across the '3' piece's 3 basis vectors: {RE_3_candidates}"
    )
    RE_3 = RE_3_candidates[0]
    print(f"  R^E on '3' piece (y1(x)1,y2(x)1,y3(x)1), verified scalar and equal: {RE_3}")

    D2_A_3 = (C2_G2_7 - C2_SU3_3) + sp.Rational(3, 2) * (sp.Rational(scal, 4) + RE_3)
    D2_B_3 = sp.Rational(3, 2) * ((C2_G2_7 - C2_SU3_3) + sp.Rational(scal, 4) + RE_3)
    print(f"  '3'/'3bar' piece, Interp A: {D2_A_3}")
    print(f"  '3'/'3bar' piece, Interp B: {D2_B_3}")

    all_positive = (
        all(v > 0 for v in D2_A_singlet.eigenvals())
        and all(v > 0 for v in D2_B_singlet.eigenvals())
        and D2_A_3 > 0
        and D2_B_3 > 0
    )
    print(f"\n  ALL eigenvalues strictly positive under Interp A and Interp B? {all_positive}")
    print("  ")
    print("  NOTE (post-skeptic-review, do not delete this caveat): this positivity")
    print("  check across 2 sampled points does NOT establish the rho=7 verdict.")
    print("  The L4B calibration (Step 3) constrains ONLY the (Scal+R^E) coefficient,")
    print("  since nabla*nabla=0 identically at rho=trivial -- it says nothing about")
    print("  the coefficient on nabla*nabla itself (the ONE term that actually depends")
    print("  on rho=7), which Interp A and B fix at two arbitrary values (1 and 3/2)")
    print("  out of an unconstrained continuum. See decision.md 'Round 16 continued'")
    print("  for the full skeptic finding (Concern 3, FALSIFIED verdict on the core")
    print("  predicate) -- task #7 remains OPEN, this script does NOT resolve it.")


if __name__ == "__main__":
    main()
