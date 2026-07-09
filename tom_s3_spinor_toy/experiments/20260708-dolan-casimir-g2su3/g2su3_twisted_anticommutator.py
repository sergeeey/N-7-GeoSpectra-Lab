"""
Re-derivation of the twisted anticommutator {D^0_twisted, H_twisted}
(2026-07-09, continuing Round 6-8).

SETUP: D^t_twisted(eta (x) xi) = sum_i e_i.nabla^t_{e_i}eta (x) xi
                                 + sum_i e_i.eta (x) nabla^t_{e_i}xi
Exact Leibniz-rule identity (not assumed): D^t_twisted = D^0_twisted + t*H_twisted,
  D^0_twisted(eta(x)xi) = sum_i e_i.e_i(eta)(x)xi + sum_i e_i.eta(x)e_i(xi)
  H_twisted = H(x)Id + Id(x)H   [H acting on each factor separately]

HAND DERIVATION (this file's docstring documents it; code verifies the
consequence, not the full general formula):
Expanding {D^0_twisted, H_twisted}(eta(x)xi) term-by-term (8 pieces: A..J
minus overlaps) shows EVERY piece contains an explicit e_i(eta) or e_i(xi)
factor (true derivative). Consequence: if eta AND xi are BOTH trivial
G2-isotype sections (i.e. SU(3)-invariant fiber vectors, realized as
CONSTANT equivariant functions with e_i(eta)=e_i(xi)=0 identically -- this
is what "trivial isotype" means via Frobenius reciprocity), then:
  - D^0_twisted(eta(x)xi) = 0 (both terms vanish, e_i(eta)=e_i(xi)=0)
  - H(eta), H(xi) are ALSO trivial-isotype (H commutes with SU(3), proven
    via H^2's block-scalar structure on SU(3) isotypic pieces, Round 6) --
    so D^0_twisted(H_twisted(eta(x)xi)) = 0 too (same reason, one more step)
  - Hence {D^0_twisted,H_twisted}(eta(x)xi) = 0 EXACTLY for trivial-isotype
    inputs, and moreover (D^0_twisted)^2(eta(x)xi) = D^0_twisted(0) = 0.

CONSEQUENCE (testable prediction): for eta,xi BOTH trivial-isotype,
  (D^t_twisted)^2 (eta(x)xi) = t^2 * H_twisted^2 (eta(x)xi)   EXACTLY, all t.

This is checked DIRECTLY below against the ALREADY-COMPUTED L4B data (v_a,
v_b, w=1(x)1 are all trivial-isotype), by comparing:
  (a) D_on_simple_tensor applied TWICE (fully independent, uses only the
      already-calibrated Levi-Civita connection machinery, no new theory)
  (b) (1/4) * H_twisted^2 applied once (uses the Kronecker-sum H_twisted,
      built purely from the already-validated single-copy H)
If (a) == (b), this validates BOTH the anticommutator derivation above AND
that mixed cross-terms genuinely vanish on trivial isotype as predicted --
a real, falsifiable check, not assumed.
"""

import sympy as sp
from g2su3_explicit_clifford import DIM, SUBSETS, IDX, vec_from_subsets
from g2su3_H_element import build_T_table, build_H_matrix
from g2su3_compute_crossterm import D_on_simple_tensor

sqrt = sp.sqrt


def dict_to_vec64(d):
    """Convert a {(subset_L,subset_R): coeff} dict into a 64-dim sympy vector,
    index = 8*IDX[subset_L] + IDX[subset_R]."""
    v = sp.zeros(64, 1)
    for (sL, sR), c in d.items():
        v[8 * IDX[sL] + IDX[sR]] = c
    return v


def vec64_to_dict(v):
    d = {}
    for i in range(64):
        c = sp.simplify(v[i])
        if c != 0:
            sL = SUBSETS[i // 8]
            sR = SUBSETS[i % 8]
            d[(sL, sR)] = c
    return d


def D_twisted_on_dict(d):
    """Apply D^{1/2}_twisted to a general element of Sigma(x)Sigma given as
    a {(subset_L,subset_R):coeff} dict, via linearity + D_on_simple_tensor."""
    out = {}

    def add(dd, factor=1):
        for k, v in dd.items():
            out[k] = out.get(k, 0) + factor * v

    for (sL, sR), c in d.items():
        eta = vec_from_subsets({sL: 1})
        xi = vec_from_subsets({sR: 1})
        res = D_on_simple_tensor(eta, xi)
        add(res, c)
    for k in list(out.keys()):
        out[k] = sp.simplify(out[k])
        if out[k] == 0:
            del out[k]
    return out


def main():
    print("=" * 70)
    print("Building H_twisted = H (x) Id + Id (x) H  (64x64)")
    print("=" * 70)
    T = build_T_table()
    H = build_H_matrix(T)
    Id8 = sp.eye(DIM)
    H_twisted = sp.Matrix(sp.KroneckerProduct(H, Id8).doit()) + sp.Matrix(
        sp.KroneckerProduct(Id8, H).doit()
    )
    H_twisted = sp.simplify(H_twisted)
    print("H_twisted built (64x64).")

    H_twisted_sq = sp.simplify(H_twisted * H_twisted)
    print("H_twisted^2 built.")

    print("\n" + "=" * 70)
    print("TEST 1: v_a = y1(x)y23 - y2(x)y13 + y3(x)y12 (trivial isotype)")
    print("=" * 70)
    v_a_dict = {((1,), (2, 3)): 1, ((2,), (1, 3)): -1, ((3,), (1, 2)): 1}
    v_a_64 = dict_to_vec64(v_a_dict)

    print("Route (a): apply D_on_simple_tensor TWICE (fully independent)")
    Dv_a = D_twisted_on_dict(v_a_dict)
    print(f"  D(v_a) = {Dv_a}")
    DDv_a = D_twisted_on_dict(Dv_a)
    print(f"  D(D(v_a)) = {DDv_a}")
    DDv_a_64 = dict_to_vec64(DDv_a)

    print("\nRoute (b): (1/4) * H_twisted^2 (v_a)")
    pred = sp.simplify(sp.Rational(1, 4) * H_twisted_sq * v_a_64)
    pred_dict = vec64_to_dict(pred)
    print(f"  (1/4)H_twisted^2(v_a) = {pred_dict}")

    diff = sp.simplify(DDv_a_64 - pred)
    match = diff == sp.zeros(64, 1)
    print(f"\nMATCH (route a == route b)? {match}")
    if not match:
        print("DIFFERENCE (nonzero components):")
        for i in range(64):
            if sp.simplify(diff[i]) != 0:
                sL = SUBSETS[i // 8]
                sR = SUBSETS[i % 8]
                print(f"  [{sL},{sR}]: {diff[i]}")

    print("\n" + "=" * 70)
    print("TEST 2: v_b = y123 (x) 1 (trivial isotype)")
    print("=" * 70)
    v_b_dict = {((1, 2, 3), ()): 1}
    v_b_64 = dict_to_vec64(v_b_dict)

    Dv_b = D_twisted_on_dict(v_b_dict)
    print(f"  D(v_b) = {Dv_b}")
    DDv_b = D_twisted_on_dict(Dv_b)
    print(f"  D(D(v_b)) = {DDv_b}")
    DDv_b_64 = dict_to_vec64(DDv_b)

    pred_b = sp.simplify(sp.Rational(1, 4) * H_twisted_sq * v_b_64)
    pred_b_dict = vec64_to_dict(pred_b)
    print(f"  (1/4)H_twisted^2(v_b) = {pred_b_dict}")

    diff_b = sp.simplify(DDv_b_64 - pred_b)
    match_b = diff_b == sp.zeros(64, 1)
    print(f"\nMATCH (route a == route b)? {match_b}")
    if not match_b:
        print("DIFFERENCE (nonzero components):")
        for i in range(64):
            if sp.simplify(diff_b[i]) != 0:
                sL = SUBSETS[i // 8]
                sR = SUBSETS[i % 8]
                print(f"  [{sL},{sR}]: {diff_b[i]}")

    print("\n" + "=" * 70)
    print("OVERALL VERDICT")
    print("=" * 70)
    print(f"Test 1 (v_a): {'PASS' if match else 'FAIL'}")
    print(f"Test 2 (v_b): {'PASS' if match_b else 'FAIL'}")


if __name__ == "__main__":
    main()
