"""
THE DECISIVE COMPUTATION: twisted Levi-Civita Dirac operator D^+_{S^-} acting
on v_a and v_b, projected onto the unique G2/SU(3)-invariant of S^- (x) S-,
w = 1 (x) 1.

D(eta (x) xi) = sum_i (e_i . nabla^g_{e_i} eta) (x) xi
              + sum_i (e_i . eta) (x) (nabla^g_{e_i} xi)

v_a = y1(x)y23 - y2(x)y13 + y3(x)y12   (verified SU(3)-invariant, computed)
v_b = y123 (x) 1                        (singlet (x) singlet)

If D(v_a) and D(v_b) both come out proportional to w=1(x)1 with coefficients
(c_a, c_b), rank(D+|_trivial) = 0 iff c_a=c_b=0, else rank=1.
"""

import sympy as sp
from g2su3_explicit_clifford import (
    DIM,
    SUBSETS,
    IDX,
    e_action,
    vec_from_subsets,
)
from g2su3_explicit_clifford import LEVI_CIVITA_NOMIZU, clifford_mult_bivector_direct

sqrt = sp.sqrt


def nabla_g(i, vec):
    terms = LEVI_CIVITA_NOMIZU[i]
    coeff = sp.Rational(1, 2) / sqrt(3)
    out = sp.zeros(DIM, 1)
    for sign, a, b in terms:
        out += sign * clifford_mult_bivector_direct(a, b, vec)
    return coeff * out


def tensor_coeff_dict(vec):
    """Return {subset: coeff} for nonzero entries of an 8-dim Sigma vector."""
    d = {}
    for s in SUBSETS:
        c = sp.simplify(vec[IDX[s]])
        if c != 0:
            d[s] = c
    return d


def D_on_simple_tensor(eta, xi):
    """Twisted Dirac operator on a simple tensor eta (x) xi, eta,xi 8-dim
    Sigma vectors (living in Sigma_odd, Sigma_even respectively in our usage,
    but the formula is chirality-agnostic). Returns dict {(subset_L, subset_R): coeff}
    representing the result as an element of Sigma (x) Sigma."""
    result = {}

    def add(dL, dR, factor):
        for sL, cL in dL.items():
            for sR, cR in dR.items():
                key = (sL, sR)
                result[key] = result.get(key, 0) + factor * cL * cR

    for i in range(1, 7):
        # term 1: (e_i . nabla_{e_i} eta) (x) xi
        nab_eta = nabla_g(i, eta)
        e_nab_eta = e_action(i, nab_eta)
        add(tensor_coeff_dict(e_nab_eta), tensor_coeff_dict(xi), 1)

        # term 2: (e_i . eta) (x) (nabla_{e_i} xi)
        e_eta = e_action(i, eta)
        nab_xi = nabla_g(i, xi)
        add(tensor_coeff_dict(e_eta), tensor_coeff_dict(nab_xi), 1)

    # simplify
    for k in list(result.keys()):
        result[k] = sp.simplify(result[k])
        if result[k] == 0:
            del result[k]
    return result


def add_dicts(*dicts):
    out = {}
    for d in dicts:
        for k, v in d.items():
            out[k] = out.get(k, 0) + v
    for k in list(out.keys()):
        out[k] = sp.simplify(out[k])
        if out[k] == 0:
            del out[k]
    return out


def scale_dict(d, factor):
    return {k: sp.simplify(factor * v) for k, v in d.items()}


def main():
    print("=" * 70)
    print("DECISIVE COMPUTATION: D(v_a), D(v_b) projected onto w=1(x)1")
    print("=" * 70)

    y1 = vec_from_subsets({(1,): 1})
    y2 = vec_from_subsets({(2,): 1})
    y3 = vec_from_subsets({(3,): 1})
    y12 = vec_from_subsets({(1, 2): 1})
    y13 = vec_from_subsets({(1, 3): 1})
    y23 = vec_from_subsets({(2, 3): 1})
    one = vec_from_subsets({(): 1})
    y123 = vec_from_subsets({(1, 2, 3): 1})

    print("\n--- Computing D(v_a), v_a = y1(x)y23 - y2(x)y13 + y3(x)y12 ---")
    Dva = add_dicts(
        D_on_simple_tensor(y1, y23),
        scale_dict(D_on_simple_tensor(y2, y13), -1),
        D_on_simple_tensor(y3, y12),
    )
    print("D(v_a) nonzero components (subset_L, subset_R): coeff")
    for k, v in Dva.items():
        print(f"  {k}: {v}")
    w_coeff_a = Dva.get(((), ()), 0)
    print(f"\n  Coefficient of w=1(x)1 in D(v_a): {w_coeff_a}")
    other_terms_a = {k: v for k, v in Dva.items() if k != ((), ())}
    print(f"  Other (non-w) terms present: {len(other_terms_a)}  -> {other_terms_a}")

    print("\n--- Computing D(v_b), v_b = y123 (x) 1 ---")
    Dvb = D_on_simple_tensor(y123, one)
    print("D(v_b) nonzero components (subset_L, subset_R): coeff")
    for k, v in Dvb.items():
        print(f"  {k}: {v}")
    w_coeff_b = Dvb.get(((), ()), 0)
    print(f"\n  Coefficient of w=1(x)1 in D(v_b): {w_coeff_b}")
    other_terms_b = {k: v for k, v in Dvb.items() if k != ((), ())}
    print(f"  Other (non-w) terms present: {len(other_terms_b)}  -> {other_terms_b}")

    print("\n" + "=" * 70)
    print("VERDICT")
    print("=" * 70)
    print(f"c_a (coefficient for v_a) = {w_coeff_a}")
    print(f"c_b (coefficient for v_b) = {w_coeff_b}")
    rank = 0 if (w_coeff_a == 0 and w_coeff_b == 0) else 1
    print("\nIf both other-terms lists are empty (pure multiples of w), this is exact.")
    print(
        f"Implied rank(D+|_trivial) = {rank}  =>  dim ker(D+_S-) = {2 - rank if rank in (0, 1) else '?'}"
    )


if __name__ == "__main__":
    main()
