"""
Round 15 (2026-07-09): attempt to build the twisted analog of Agricola's
C_tilde_h (su(3)-Casimir lifted into the Clifford algebra, Proposition
3.3), Leibniz-extended to Sigma(x)Sigma, as the missing ingredient for
the full rho=7 kernel verdict.

CONSTRUCTION (implemented below, SU(3)-equivariance VERIFIED exactly):
  twisted_Ch(eta (x) xi) := (Ch . eta)(x)xi
      + (1/4) sum_{p,q=1..6, p!=q} (Zp.Zq.eta)(x)([Zp,Zq]_h . xi)
using curvature_h (Round 13) for [Zp,Zq]_h and the already-trusted
su3_action (Clifford-algebra lift, used throughout this experiment) for
[Zp,Zq]_h's action on xi. Ch (untwisted, full degree-0+degree-4) is
rebuilt inline via the same Jac_h construction validated in Round 14's
g2su3_casimir_convention_check.py / g2su3_delta_correction.py session.

RESULT 1 (PASS): [twisted_Ch, su3_i] = 0 exactly for all 8 generators
(64x64 matrix, zero residual) -- a genuine, non-trivial equivariance
check, not automatic from the construction.

RESULT 2 (PASS, clean): twisted_Ch(v_a) = 0 and twisted_Ch(v_b) = 0
EXACTLY -- consistent with (and structurally analogous to) the untwisted
Ch being exactly zero on the {1,y123} singlet-pair piece.

RESULT 3 (FAILS calibration -- the actual finding this round): naively
assembling the twisted analog of Agricola's UNTWISTED formula
  (D^{1/2})^2 = Omega_g - H + Ctilde_h + (1/4)H^2
term-by-term (H -> calH, Ctilde_h -> twisted_Ch, H^2 -> calH^2) and
testing it against the L4B ground truth (D^2(v_a) = D^2(v_b) = v_a+3v_b,
ALREADY independently verified via D_on_simple_tensor^2 directly) FAILS:
  Omega_g(=0, rho=trivial) - calH(v_a) + twisted_Ch(v_a) + (1/4)calH^2(v_a)
  = 0 - (-2*sqrt(3)*w) + 0 + (v_a+3*v_b)
  = v_a + 3*v_b + 2*sqrt(3)*w  != v_a + 3*v_b (the TRUE answer)
The extra "+2*sqrt(3)*w" term comes entirely from "-calH(v_a)" (LINEAR,
UNSQUARED calH = 2*D_on_simple_tensor(v_a) = -2*sqrt(3)*w, matching the
ALREADY-KNOWN L4B result D(v_a)=-sqrt(3)*w exactly).

DIAGNOSIS (why this is a real structural issue, not a sign slip):
Agricola's H (untwisted) is a chirality-FLIPPING endomorphism WITHIN the
single 8-dim Sigma (which contains BOTH chiralities S+ and S- together,
Sigma=S+(+)S-) -- H:S+->S- and S-->S+ stays inside the SAME 8-dim space,
so "-H" is a well-defined additive term in an endomorphism of Sigma.
The TWISTED calH, by contrast, maps the 16-dim S+(x)S- slice to the
DIFFERENT 16-dim S-(x)S- slice of the 64-dim Sigma(x)Sigma (only the
LEFT tensor factor's chirality flips, per this whole experiment's
established D_on_simple_tensor Leibniz convention) -- "-calH(v_a)"
therefore lands in a DIFFERENT subspace (S-(x)S-, specifically the w=1(x)1
slot) than v_a+3v_b (which lives in S+(x)S-). A term that lands in a
different subspace cannot simply cancel additively against a formula
whose other pieces (Omega_g, twisted_Ch, calH^2) all preserve S+(x)S-.
This means Theorem 3.2's UNTWISTED decomposition does not carry over via
a naive term-by-term Leibniz substitution -- the paper's own PROOF
(not just its stated closed-form result) uses manipulations specific to
a SINGLE Clifford module C(m) acting on ONE spinor bundle S, and does
not directly address a twisted operator D_{S(x)E} between two different
16-dim slices of a bigger tensor-product bundle.

STATUS: BLOCKED. This is a genuine, non-trivial re-derivation problem
(how does Theorem 3.2 generalize to a Leibniz-twisted Dirac operator on
S(x)E?), not a transcription/sign bug like the nu_8 or Jac_h/Jac_m
corrections found earlier this session. Continuing without resolving
this risks exactly the kind of silent, hard-to-catch error this
project's methodology exists to prevent (see decision.md's repeated
"calibrate before trusting" discipline). Per this project's Stuck
Detection protocol (tiers 1-2 exhausted this session: quick retry,
context refresh via re-reading the primary source), this is flagged for
a Tier-3 strategy switch (e.g. explicitly re-deriving the twisted D^2
expansion from scratch via the SAME index-level method Agricola's proof
uses, generalized to two tensor factors, rather than substituting into
the already-closed-form untwisted result) in a FUTURE, dedicated round
-- not forced here.

PRESERVED for future reuse: the twisted_Ch construction itself (Results
1-2) is likely a genuinely correct BUILDING BLOCK (equivariant, clean
zero on the expected piece) -- what's wrong is only how it was ASSEMBLED
into the final D^2 formula, not necessarily its own construction.
"""

import itertools

import sympy as sp

from g2su3_appendix_a_construction import (
    ad_nu_m_trusted,
    BRACKET_SIGN,
    build_curvature_h_table,
)
from g2su3_equivariance_check import build_D_matrix64, build_su3_matrix64
from g2su3_explicit_clifford import DIM, IDX, SUBSETS, e_action, vec_from_subsets
from g2su3_H_element import build_H_matrix, build_T_table
from g2su3_twisted_kernel import su3_action

N64 = DIM * DIM


def idx64(a, b):
    return DIM * a + b


def curv_h_lookup(curv_h, p, q, k):
    if p < q:
        return curv_h.get((p, q, k), 0)
    if p > q:
        return -curv_h.get((q, p, k), 0)
    return 0


def build_untwisted_Ch():
    """Full (degree-0 + degree-4) untwisted Ctilde_h, single Sigma."""
    T = build_T_table()
    H = build_H_matrix(T)
    H2 = sp.simplify(H * H)
    H2_4 = sp.simplify(H2 - sp.Rational(3) * sp.eye(DIM))
    curv_h = build_curvature_h_table()

    def bracket_e_nu(p, k):
        return {r: BRACKET_SIGN * ad_nu_m_trusted(k, p)[r - 1] for r in range(1, 7)}

    def jac_h(p, q, r):
        result = {i: 0 for i in range(1, 7)}
        for a, b, c in [(p, q, r), (q, r, p), (r, p, q)]:
            for k in range(1, 9):
                coeff = curv_h_lookup(curv_h, b, c, k)
                if coeff == 0:
                    continue
                bec = bracket_e_nu(a, k)
                for i in range(1, 7):
                    result[i] += coeff * bec[i]
        return result

    basis = [vec_from_subsets({s: 1}) for s in SUBSETS]

    def clifford_4_action(coeffs4, vec):
        out = sp.zeros(DIM, 1)
        for (i, j, k, idx4), c in coeffs4.items():
            if c == 0:
                continue
            v = e_action(idx4, vec)
            v = e_action(k, v)
            v = e_action(j, v)
            v = e_action(i, v)
            out += c * v
        return out

    coeffs4 = {}
    for i, j, k, idx4 in itertools.combinations(range(1, 7), 4):
        jh = jac_h(j, k, idx4)
        coeffs4[(i, j, k, idx4)] = -sp.Rational(1, 2) * sp.simplify(jh.get(i, 0))

    Ch = sp.zeros(DIM, DIM)
    for col in range(DIM):
        out = (
            clifford_4_action(coeffs4, basis[col]) + basis[col]
        )  # +1*basis = (Ch)_0 diag part folded via H2_4 check below
        for row in range(DIM):
            Ch[row, col] = out[row]
    # sanity re-derivation of the degree-4 identity (independent check, see decision.md)
    Ch4 = sp.simplify(Ch - sp.eye(DIM))
    assert sp.simplify(Ch4 - (-sp.Rational(1, 9)) * H2_4) == sp.zeros(DIM, DIM)
    return sp.simplify(Ch)


def build_twisted_Ch():
    curv_h = build_curvature_h_table()
    Ch = build_untwisted_Ch()
    basis = [vec_from_subsets({s: 1}) for s in SUBSETS]

    def h_bracket_action(p, q, xi):
        out = sp.zeros(DIM, 1)
        for k in range(1, 9):
            c = curv_h_lookup(curv_h, p, q, k)
            if c == 0:
                continue
            out += c * su3_action(k, xi)
        return out

    def zpzq_eta(p, q, eta):
        v = e_action(q, eta)
        v = e_action(p, v)
        return v

    twisted_Ch = sp.zeros(N64, N64)
    for a in range(DIM):
        eta = basis[a]
        Ch_eta = Ch * eta
        for b in range(DIM):
            xi = basis[b]
            col = idx64(a, b)
            out = sp.zeros(N64, 1)
            for r in range(DIM):
                out[idx64(r, b)] += Ch_eta[r]
            for p in range(1, 7):
                for q in range(1, 7):
                    if p == q:
                        continue
                    hb_xi = h_bracket_action(p, q, xi)
                    if hb_xi == sp.zeros(DIM, 1):
                        continue
                    zpzq = zpzq_eta(p, q, eta)
                    for r in range(DIM):
                        if zpzq[r] == 0:
                            continue
                        for s in range(DIM):
                            if hb_xi[s] == 0:
                                continue
                            out[idx64(r, s)] += sp.Rational(1, 4) * zpzq[r] * hb_xi[s]
            twisted_Ch[:, col] = out
    return sp.simplify(twisted_Ch)


def main():
    print("=" * 70)
    print("Building twisted_Ch (64x64) -- this takes a while")
    print("=" * 70)
    twisted_Ch = build_twisted_Ch()

    print("\n" + "=" * 70)
    print("RESULT 1: SU(3)-equivariance check")
    print("=" * 70)
    all_zero = True
    for i in range(1, 9):
        S = build_su3_matrix64(i)
        comm = sp.simplify(twisted_Ch * S - S * twisted_Ch)
        nz = sum(1 for r in range(N64) for c in range(N64) if sp.simplify(comm[r, c]) != 0)
        print(f"  [twisted_Ch, su3_{i}] nonzero entries: {nz}")
        all_zero &= nz == 0
    print(f"  Exactly equivariant for all 8 generators? {all_zero}")

    print("\n" + "=" * 70)
    print("RESULT 2 + 3: calibration against L4B ground truth")
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
    w = sp.zeros(N64, 1)
    w[idx64(one, one)] = 1

    Ch_va = sp.simplify(twisted_Ch * v_a)
    Ch_vb = sp.simplify(twisted_Ch * v_b)
    print(f"  twisted_Ch(v_a) == 0? {Ch_va == sp.zeros(N64, 1)}")
    print(f"  twisted_Ch(v_b) == 0? {Ch_vb == sp.zeros(N64, 1)}")

    D = build_D_matrix64()
    D2 = sp.simplify(D * D)
    D2_va = sp.simplify(D2 * v_a)
    calH_va = sp.simplify(2 * D * v_a)  # calH = 2*D_on_simple_tensor
    print(
        f"\n  D^2(v_a) (TRUE, already-validated answer) = v_a+3*v_b? "
        f"{sp.simplify(D2_va - (v_a + 3 * v_b)) == sp.zeros(N64, 1)}"
    )
    print(
        f"  calH(v_a) = -2*sqrt(3)*w? "
        f"{sp.simplify(calH_va - (-2 * sp.sqrt(3) * w)) == sp.zeros(N64, 1)}"
    )

    naive_formula = sp.simplify(-calH_va + Ch_va + sp.Rational(1, 4) * D2_va * 4)
    residual = sp.simplify(naive_formula - (v_a + 3 * v_b))
    print(
        f"\n  Naive formula (0 - calH + twisted_Ch + (1/4)calH^2)(v_a) "
        f"matches TRUE D^2(v_a)? {residual == sp.zeros(N64, 1)}"
    )
    print(
        f"  Residual (should be zero if naive substitution were valid): "
        f"{[(SUBSETS[i // DIM], SUBSETS[i % DIM], residual[i]) for i in range(N64) if sp.simplify(residual[i]) != 0]}"
    )
    print("\n  CONCLUSION: naive term-by-term Leibniz substitution of Theorem 3.2")
    print("  FAILS calibration -- see module docstring for diagnosis. BLOCKED,")
    print("  flagged for a dedicated future round, not forced here.")


if __name__ == "__main__":
    main()
