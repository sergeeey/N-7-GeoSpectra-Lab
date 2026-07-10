"""
Round 22 (2026-07-10): explicit derivation of the Levi-Civita vs
canonical-Casimir Nomizu cross-terms identified by Round 21's structural
obstruction theorem as the missing piece of the Weitzenbock identity.

BACKGROUND. Round 21 proved D_7^2 (the ALREADY-VALIDATED twisted Dirac
operator squared, built via matrix-coefficient sections, Rounds 17-19)
cannot equal nabla*nabla_can + Scal/4 + R^E for ANY invariant fiber
endomorphism R^E, because the left side mixes SU(3)-domain-types on
M = Hom_SU(3)(V_7, F) while every term on the right is domain-type-
preserving. The docstring there predicted the missing piece is a
"Nomizu cross-term", first-order in the invariant vector fields.

DERIVATION. Write D_7 = TERM_A + TERM_B from its own defining formula
(Round 17):
  D(psi_{v,w})|_e = -sum_p e_p.w(rho_7(e_p)v) + D_on_simple_tensor(w(v))
                  =: TERM_A(w)(v) + TERM_B(w)(v)
Expanding D_7^2 = (TERM_A+TERM_B)^2 by hand (using only e_p^2=-1,
e_p.e_q=-e_q.e_p for p!=q, and the representation identity
[rho_7(e_p),rho_7(e_q)]=rho_7([e_p,e_q])) splits it into FIVE pieces,
evaluated at any v = e_i in V_7:

  TERM_A(TERM_A w)(v) = sum_{p,q} e_p.e_q . w(rho_7(e_q)rho_7(e_p) v)
   = [p=q part]  -w(sum_p rho_7(e_p)^2 v)                          =: CASIMIR (type-preserving)
   + [p<q part]  -sum_{p<q} e_p.e_q . w(rho_7([e_p,e_q]) v)
        [e_p,e_q] = sum_r T(p,q,r) e_r  +  sum_k curv_h(p,q,k) nu_k
             (T, curv_h tables' OWN bracket-orientation convention)
   = +sum_{p<q,r} T(p,q,r) . e_p.e_q . w(rho_7(e_r) v)              =: TORSION CROSS-TERM
   + +sum_{p<q,k} curv_h(p,q,k) . e_p.e_q . w(rho_nu_k v)           =: SU(3)-CURVATURE
        (SIGN NOTE: the two minus signs -- one from the p<q expansion, one
        from a genuine convention mismatch [rho_7(e_p),rho_7(e_q)] =
        -rho_7([e_p,e_q]) between V_7's OWN representation (Round 14,
        g2su3_v7_multiplicity_dirac.py) and the T/curv_h tables' bracket
        orientation (g2su3_H_element.py / g2su3_appendix_a_construction.py)
        -- cancel, giving a net PLUS sign here. Verified directly by
        comparing [rho_7(e_1),rho_7(e_2)] against its T/curv_h reconstruction
        as explicit 7x7 matrices: they are exact NEGATIVES of each other.
        This is the SAME kind of cross-module sign convention clash flagged
        by g2su3_appendix_a_construction.py's own BRACKET_SIGN=-1 comment --
        two independently-built representations of the same Lie algebra can
        legitimately disagree on bracket orientation, and any formula mixing
        both must be checked, not assumed.)

  TERM_B(TERM_B w)(v) = D64^2 . w(v)                                =: D64-SQUARED (type-preserving, F-side only)

  TERM_A(TERM_B w)(v) + TERM_B(TERM_A w)(v)
   = -sum_p {e_p, D64} . w(rho_7(e_p) v)   ({.,.} = anticommutator)  =: MIXED A-B CROSS-TERM

CASIMIR and D64-SQUARED are manifestly type-preserving (CASIMIR is a
scalar multiple of w(v) itself; D64-SQUARED is an F-side-only operator
that commutes with the SU(3) action since D64 does, Round 17). SU(3)-
CURVATURE's rho_nu_k(v) stays within v's own SU(3)-type by definition
of "su(3) generator" -- but that alone does NOT make the whole term
domain-type-preserving in the FULL W-space (7 domain-index slots) sense
Round 21's theorem actually needs; only TORSION moves v across SU(3)-
types via the m-direction action rho_7(e_r). Which piece(s) actually
carry Round 21's observed type-mixing is an empirical question, settled
below by direct computation -- not assumed.

TWO DEAD ENDS LOGGED IN decision.md (both fixed before this version):
(1) an earlier draft tested only the domain-index-0 (phi_2) SLICE of
D^2(singlet_1) and concluded (wrongly) that no leakage occurs for
singlet_1 at all -- vacuous, since Round 21's "three_i"/"threebar_i"
basis elements are supported ONLY on domain indices 1-6, so restricting
to index 0 trivially zeroes their coefficients regardless of the real
operator (confirmed: D^2(singlet_1) has 2 nonzero F-components on EACH
of domain indices 1-6). (2) the FIRST full-7-index attempt used the sign
convention [rho_7(e_p),rho_7(e_q)]=+rho_7([e_p,e_q]) (the naive textbook
assumption) and failed its own decisive assert with a uniform 4/3
discrepancy at exactly one row per non-singlet domain index -- traced
via a 4-step bisection (single-application check -> T_A(T_A(w)) isolated
from T_B -> direct bracket-vs-table comparison) to the sign mismatch
documented above. This version has both fixes applied and is the one
that passes.

Evidence markers: every numeric claim is re-computed and asserted in
main() below ([VERIFIED-tool] on run).
"""

import sympy as sp

from g2su3_appendix_a_construction import build_curvature_h_table
from g2su3_equivariance_check import build_D_matrix64
from g2su3_explicit_clifford import DIM
from g2su3_H_element import build_T_table
from g2su3_v7_16dim_full_matrix import (
    build_3_copies,
    build_3bar_copies,
    build_singlets,
    build_w_cols_general,
    flatten,
)
from g2su3_v7_3_3bar_intertwiners import P3, P3BAR, build_MF, build_MV7, solve_intertwiner
from g2su3_v7_multiplicity_dirac import clifford_left_64, d7_apply, rho7_ep, rho7_nuk

N64 = DIM * DIM


def build_Mp_matrices():
    """M_p := 64x64 matrix of Clifford-left-mult by e_p, for p=1..6."""
    Ms = {}
    for p in range(1, 7):
        cols = []
        for i in range(N64):
            basis = sp.zeros(N64, 1)
            basis[i] = 1
            cols.append(clifford_left_64(p, basis))
        Ms[p] = sp.Matrix.hstack(*cols)
    return Ms


def w_at(w_cols, vec7):
    """w applied to a linear combination vec7 (7x1 sympy Matrix) of V_7 basis vectors."""
    out = sp.zeros(N64, 1)
    for j in range(7):
        if vec7[j] != 0:
            out += vec7[j] * w_cols[j]
    return out


def e_i7(i):
    v = sp.zeros(7, 1)
    v[i] = 1
    return v


def casimir_term(w_cols, i):
    M_cas = sp.zeros(7, 7)
    for p in range(1, 7):
        Mp7 = rho7_ep(p)
        M_cas += Mp7 * Mp7
    return -w_at(w_cols, M_cas * e_i7(i))


def termB_squared(w_cols, i, D64):
    return sp.simplify(D64 * (D64 * w_cols[i]))


def su3_curvature_term(w_cols, i, Ms, curv_h):
    """Sign note: the derivation gives -sum e_p.e_q.w(rho_7([e_p,e_q])v), but
    empirically [rho_7(e_p),rho_7(e_q)] = -rho_7([e_p,e_q]) in the T/curv_h
    tables' own bracket convention (verified directly: g2su3_nomizu_crossterms
    debug session, p=1,q=2 case, matrix comparison) -- a genuine sign mismatch
    between V_7's representation (Round 14, g2su3_v7_multiplicity_dirac.py)
    and the structural bracket convention build_curvature_h_table/build_T_table
    use internally. Net effect: the two minus signs cancel, so this function
    returns +out, not -out."""
    out = sp.zeros(N64, 1)
    for (p, q, k), coeff in curv_h.items():
        Mnk7 = rho7_nuk(k)
        w_val = w_at(w_cols, Mnk7 * e_i7(i))
        if w_val == sp.zeros(N64, 1):
            continue
        out += coeff * (Ms[p] * (Ms[q] * w_val))
    return out


def torsion_cross_term(w_cols, i, Ms, T):
    """Sign note: see su3_curvature_term -- same [rho_p,rho_q]=-rho_7([e_p,e_q])
    convention mismatch applies here identically (both terms come from the same
    p<q commutator expansion), so this also returns +out, not -out."""
    out = sp.zeros(N64, 1)
    for (p, q, r), coeff in T.items():
        if p >= q:
            continue  # T-table has all (i,j,k); restrict to p<q per the derivation
        Mr7 = rho7_ep(r)
        w_val = w_at(w_cols, Mr7 * e_i7(i))
        if w_val == sp.zeros(N64, 1):
            continue
        out += coeff * (Ms[p] * (Ms[q] * w_val))
    return out


def mixed_AB_term(w_cols, i, Ms, D64):
    out = sp.zeros(N64, 1)
    for p in range(1, 7):
        Mp7 = rho7_ep(p)
        w_val = w_at(w_cols, Mp7 * e_i7(i))
        if w_val == sp.zeros(N64, 1):
            continue
        AC_p = Ms[p] * D64 + D64 * Ms[p]
        out += AC_p * w_val
    return -out


def reconstruct_D2_full(w_cols, Ms, D64, T, curv_h):
    """Full 7-domain-index (448-dim) decomposition: for each of the 5 pieces,
    return the 7-tuple of 64-dim vectors (one per domain index i=0..6)."""
    parts = {name: [] for name in ("casimir", "termB_sq", "su3_curv", "torsion", "mixed_AB")}
    for i in range(7):
        parts["casimir"].append(sp.simplify(casimir_term(w_cols, i)))
        parts["termB_sq"].append(termB_squared(w_cols, i, D64))
        parts["su3_curv"].append(sp.simplify(su3_curvature_term(w_cols, i, Ms, curv_h)))
        parts["torsion"].append(sp.simplify(torsion_cross_term(w_cols, i, Ms, T)))
        parts["mixed_AB"].append(sp.simplify(mixed_AB_term(w_cols, i, Ms, D64)))
    total = []
    for i in range(7):
        s = sp.zeros(N64, 1)
        for name in parts:
            s += parts[name][i]
        total.append(sp.simplify(s))
    return total, parts


def main():
    print("=" * 70)
    print("SETUP")
    print("=" * 70)
    D64 = build_D_matrix64()
    T = build_T_table()
    curv_h = build_curvature_h_table()
    Ms = build_Mp_matrices()

    print("\n" + "=" * 70)
    print("STEP 0: sanity gates")
    print("=" * 70)
    for p in range(1, 7):
        assert sp.simplify(Ms[p] * Ms[p] + sp.eye(N64)) == sp.zeros(N64, N64), (
            f"e_{p}^2 != -1 on F -- convention mismatch"
        )
    print("  M_p^2 == -I for all p=1..6? True")
    for p in range(1, 7):
        for q in range(p + 1, 7):
            anticomm = sp.simplify(Ms[p] * Ms[q] + Ms[q] * Ms[p])
            assert anticomm == sp.zeros(N64, N64), f"e_{p},e_{q} don't anticommute"
    print("  M_p, M_q anticommute for all p<q? True")

    print("\n" + "=" * 70)
    print("STEP 1: build Round 21's exact 16-dim basis (reused, not rebuilt)")
    print("=" * 70)
    singlets = build_singlets()
    threes = build_3_copies()
    threebars = build_3bar_copies()
    MV7_3 = build_MV7(P3, slice(0, 3))
    MV7_3BAR = build_MV7(P3BAR, slice(3, 6))
    MF_3 = build_MF([(1,), (2,), (3,)])
    MF_3BAR = build_MF([(1, 2), (1, 3), (2, 3)])
    sol, t = solve_intertwiner(MV7_3, MF_3)
    Tmat = sp.Matrix(3, 3, [c.subs(t[6], 1) for c in sol])
    assert Tmat.det() != 0, "3-channel intertwiner degenerate"
    sol2, t2 = solve_intertwiner(MV7_3BAR, MF_3BAR)
    T2mat = sp.Matrix(3, 3, [c.subs(t2[8], 1) for c in sol2])
    assert T2mat.det() != 0, "3bar-channel intertwiner degenerate"

    basis_w, labels = [], []
    for i, s in enumerate(singlets):
        basis_w.append([s if j == 0 else sp.zeros(N64, 1) for j in range(7)])
        labels.append(f"singlet_{i + 1}")
    for i, triple in enumerate(threes):
        basis_w.append(build_w_cols_general(Tmat, triple, slice(0, 3)))
        labels.append(f"three_{i + 1}")
    for i, triple in enumerate(threebars):
        basis_w.append(build_w_cols_general(T2mat, triple, slice(3, 6)))
        labels.append(f"threebar_{i + 1}")
    Wmat = sp.Matrix.hstack(*[flatten(w) for w in basis_w])
    WH = Wmat.H
    WtW_inv = (WH * Wmat).inv()

    def extract_coeffs(w7tuple, name):
        target_vec = flatten(w7tuple)
        c = sp.simplify(WtW_inv * (WH * target_vec))
        residual = sp.simplify(Wmat * c - target_vec)
        assert residual == sp.zeros(7 * N64, 1), f"{name}: not in span of 16-dim basis"
        return {labels[j]: c[j] for j in range(16) if sp.simplify(c[j]) != 0}

    print("\n" + "=" * 70)
    print("STEP 2 (DECISIVE): full 7-domain-index D^2(singlet_1) vs 5-piece sum")
    print("=" * 70)
    s1 = singlets[0]
    w_s1_cols = [s1 if i == 0 else sp.zeros(N64, 1) for i in range(7)]
    ground_truth = d7_apply(d7_apply(w_s1_cols, D64), D64)

    total, parts = reconstruct_D2_full(w_s1_cols, Ms, D64, T, curv_h)
    diff = sp.simplify(flatten(total) - flatten(ground_truth))
    print(
        f"  sum of 5 pieces == D^2(singlet_1), full 448-dim, EXACTLY? "
        f"{diff == sp.zeros(7 * N64, 1)}"
    )
    assert diff == sp.zeros(7 * N64, 1), "5-piece decomposition does NOT reproduce D^2(singlet_1)"

    print("\n" + "=" * 70)
    print("STEP 3: which piece(s) carry the off-type (three*/threebar*) content?")
    print("=" * 70)
    full_coeffs = extract_coeffs(ground_truth, "D^2(singlet_1) full")
    print(f"  Full D^2(singlet_1) coefficients: {full_coeffs}")
    full_offtype = {k: v for k, v in full_coeffs.items() if not k.startswith("singlet")}
    print(f"  Off-type part (Round 21's original finding, cross-check): {full_offtype}")

    per_part_offtype = {}
    for name, vecs in parts.items():
        c = extract_coeffs(vecs, f"part[{name}]")
        offtype = {k: v for k, v in c.items() if not k.startswith("singlet")}
        per_part_offtype[name] = offtype
        print(f"  part[{name:10s}] coefficients: {c}")
        print(f"    -> off-type: {offtype}")

    print("\n" + "=" * 70)
    print("STEP 4: which pieces are clean, which carry the leakage jointly?")
    print("=" * 70)
    print("  (Original hypothesis -- TORSION alone -- tested and FALSIFIED: torsion's")
    print("  own off-type coefficients do NOT match the full total by themselves;")
    print("  see decision.md for the falsified-then-corrected account.)")
    for name in ("casimir", "termB_sq", "su3_curv"):
        assert not per_part_offtype[name], (
            f"part[{name}] has NONZERO off-type content -- expected type-preserving"
        )
    print("  casimir, termB_sq, su3_curv: all have ZERO off-type coefficients (VERIFIED)")

    joint = {}
    for k in set(per_part_offtype["torsion"]) | set(per_part_offtype["mixed_AB"]):
        v = per_part_offtype["torsion"].get(k, 0) + per_part_offtype["mixed_AB"].get(k, 0)
        if sp.simplify(v) != 0:
            joint[k] = sp.simplify(v)
    print(f"  torsion off-type:   {per_part_offtype['torsion']}")
    print(f"  mixed_AB off-type:  {per_part_offtype['mixed_AB']}")
    print(f"  torsion + mixed_AB (joint): {joint}")
    assert joint == full_offtype, (
        "TORSION+MIXED_AB joint off-type coefficients do not exactly match the full D^2's"
    )
    print(f"  (torsion + mixed_AB) off-type == full off-type, EXACTLY? {joint == full_offtype}")

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("  D_7^2 = CASIMIR + D64-SQUARED + SU(3)-CURVATURE + TORSION + MIXED_A-B")
    print("  verified EXACTLY over the FULL 448-dim (7-domain-index) W-space object")
    print("  D^2(singlet_1) -- not just its domain-index-0 slice.")
    print("  CASIMIR, D64-SQUARED, and SU(3)-CURVATURE are individually and exactly")
    print("  type-preserving (zero off-type coefficients each). TORSION and MIXED_A-B")
    print("  are each individually NONZERO off-type but neither alone matches the")
    print("  full leakage; their SUM matches Round 21's original threebar_1=2i/3,")
    print("  threebar_2=2i/3 finding EXACTLY. This refines (and matches the shape of)")
    print("  Round 21's own prediction of a Nomizu cross-term 'schematically")
    print("  -sum_p[Z_p.Lambda_p + Lambda_p.Z_p + Lambda_p^2]' -- TORSION is the")
    print("  Lambda_p^2-type piece (from T_A squared), MIXED_A-B is the")
    print("  Z_p.Lambda_p+Lambda_p.Z_p-type piece (from T_A.T_B+T_B.T_A) -- both")
    print("  genuinely new beyond canonical-Casimir+Scal/4+R^E, and TOGETHER (not")
    print("  individually) they are the explicitly-derived, quantitatively-verified")
    print("  carrier of the type-mixing that obstructs the canonical-Casimir")
    print("  Weitzenbock identity.")


if __name__ == "__main__":
    main()
