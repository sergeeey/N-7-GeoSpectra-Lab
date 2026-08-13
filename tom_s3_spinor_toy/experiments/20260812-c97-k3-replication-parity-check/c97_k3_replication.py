"""C97 -- tests whether the L/R role-swap found between C95 (k=1) and
C96 (k=2) follows a parity pattern: does k=3 (dim=4) match k=1's
pattern (L=+l directly, R=-l^T) or k=2's pattern (L=-l^T, R=+l)?

Reuses C96's now-debugged construction unchanged in its logic,
generalized from k=2 (dim=3) to general k (dim=k+1):
  - D^{(k)}(g) built via RAW (unnormalized) monomial substitution,
    matching C85's own |p> basis convention.
  - D_correct(g) := D_raw(g^{-1}) -- the fix for the anti-homomorphism
    bug C96 found and verified directly (D_raw(g1)*D_raw(g2)=
    D_raw(g2*g1), corrected via (a,b)->(conj(a),-b), i.e. using g^{-1}
    in the same [[a,b],[-conj(b),conj(a)]] parametrization). This fix
    is k-independent -- it corrects the pullback/pushforward direction
    of the raw monomial-substitution trick itself, not something
    specific to the degree of the symmetric power -- so it is reused
    here unchanged, not re-derived.
  - Coefficient-space generator extraction via an abstract free-symbol
    D_sym (matching C95/C96's own convention), NOT the concrete
    a,b-polynomial D -- this is what fixed C96's own all-zero bug.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c97.json"
K = 3
DIM = K + 1


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _build_dk_matrix_raw(a: sp.Expr, b: sp.Expr, k: int) -> sp.Matrix:
    """Naive (pullback-style, anti-homomorphic) construction -- see
    C96's own _build_d2_matrix_raw docstring for why this alone is NOT
    yet the genuine representation. Not to be called directly."""
    ac = sp.conjugate(a)
    bc = sp.conjugate(b)
    v0, v1 = sp.symbols("v0 v1")
    v0p = a * v0 + b * v1
    v1p = -bc * v0 + ac * v1

    dim = k + 1
    raw_new = [sp.expand(v0p ** (k - p) * v1p**p) for p in range(dim)]

    D = sp.zeros(dim, dim)
    for col, expr in enumerate(raw_new):
        poly = sp.Poly(expr, v0, v1)
        for row in range(dim):
            monom = (k - row, row)
            coeff = poly.coeff_monomial(v0 ** monom[0] * v1 ** monom[1])
            D[row, col] = sp.simplify(coeff)
    return D


def build_dk_matrix(a: sp.Expr, b: sp.Expr, k: int) -> sp.Matrix:
    """D^{(k)}(g), the k-th symmetric power representation, in the RAW
    (unnormalized) |p> basis matching C85's own convention -- using the
    SAME D_correct(g):=D_raw(g^{-1}) fix C96 found and verified for the
    k=2 anti-homomorphism bug, applied here unchanged for general k."""
    return _build_dk_matrix_raw(sp.conjugate(a), -b, k)


def coefficient_space_generator_general(
    action: str, X: sp.Matrix, D: sp.Matrix, eps: sp.Symbol, dim: int
) -> sp.Matrix:
    """Unchanged from C96 -- reused verbatim (already generic in dim)."""
    entries = sp.symbols(f"d0:{dim}(0:{dim})")
    entries = sp.Matrix(dim, dim, entries)

    if action == "L":
        Dnew = (sp.eye(dim) - eps * X) * D
    elif action == "R":
        Dnew = D * (sp.eye(dim) + eps * X)
    else:
        raise ValueError(action)

    fixed = 0
    result = sp.zeros(dim, dim)
    for axis_val in range(dim):
        i, j = (axis_val, fixed) if action == "L" else (fixed, axis_val)
        c = entries[i, j]
        F = c * D[i, j]
        Fnew = sp.expand(F.subs(D[i, j], Dnew[i, j]))
        d_syms = [D[r, cc] for r in range(dim) for cc in range(dim)]
        poly = sp.Poly(Fnew, *d_syms)
        for other_val in range(dim):
            i2, j2 = (other_val, fixed) if action == "L" else (fixed, other_val)
            monom = [0] * (dim * dim)
            monom[i2 * dim + j2] = 1
            coeff = poly.coeff_monomial(tuple(monom))
            deriv = sp.diff(coeff, eps).subs(eps, 0)
            if action == "L":
                result[i2, i] = deriv / c
            else:
                result[j2, j] = deriv / c
    return sp.simplify(result)


def main() -> None:
    c85 = load_module(
        "c85_certification",
        HERE.parent
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )

    a, b = sp.symbols("a b")
    Dk = build_dk_matrix(a, b, K)
    print(f"D^{{({K})}}(g) built, {DIM}x{DIM}:")
    print(Dk)

    l1, l2, l3 = c85.build_l_matrices(K, "repaired")
    l_mats = {"e1_i": l1, "e2_j": l2, "e3_k": l3}

    D_sym = sp.Matrix(DIM, DIM, sp.symbols(f"D0:{DIM}(0:{DIM})"))
    eps = sp.symbols("eps", real=True)
    per_unit = {}
    for name, R_i in l_mats.items():
        w0, x0, y0, z0 = {
            "e1_i": (0, 1, 0, 0),
            "e2_j": (0, 0, 1, 0),
            "e3_k": (0, 0, 0, 1),
        }[name]
        a_eps = 1 + eps * w0 + sp.I * eps * x0
        b_eps = eps * y0 + sp.I * eps * z0
        Dk_h = build_dk_matrix(a_eps, b_eps, K)
        X = sp.simplify(Dk_h.applyfunc(lambda e: sp.diff(e, eps).subs(eps, 0)))

        candidates = {"+l": R_i, "-l": -R_i, "+lT": R_i.T, "-lT": -R_i.T}
        L_op = coefficient_space_generator_general("L", X, D_sym, eps, DIM)
        R_op = coefficient_space_generator_general("R", X, D_sym, eps, DIM)
        L_match = [n for n, c in candidates.items() if sp.simplify(L_op - c) == sp.zeros(DIM, DIM)]
        R_match = [n for n, c in candidates.items() if sp.simplify(R_op - c) == sp.zeros(DIM, DIM)]
        per_unit[name] = {
            "L_op": L_op.tolist(),
            "R_op": R_op.tolist(),
            "L_matches": L_match,
            "R_matches": R_match,
        }
        print(f"--- {name} ---")
        print(f"  R_op matches {R_match}")
        print(f"  L_op matches {L_match}")

    R_common = set.intersection(*(set(v["R_matches"]) for v in per_unit.values()))
    L_common = set.intersection(*(set(v["L_matches"]) for v in per_unit.values()))
    print(f"\nP0 (calibration, R common candidate): {sorted(R_common)}")
    print(f"P1 (parity hypothesis, L common candidate): {sorted(L_common)}")

    p0_calibration_ok = len(R_common) == 1
    p1_matches_k1_parity = "+l" in L_common
    p1_matches_k2_parity = "-lT" in L_common

    L1, L2, L3_ = (
        sp.Matrix(per_unit["e1_i"]["L_op"]),
        sp.Matrix(per_unit["e2_j"]["L_op"]),
        sp.Matrix(per_unit["e3_k"]["L_op"]),
    )
    R1, R2, R3_ = (
        sp.Matrix(per_unit["e1_i"]["R_op"]),
        sp.Matrix(per_unit["e2_j"]["R_op"]),
        sp.Matrix(per_unit["e3_k"]["R_op"]),
    )
    L_bracket_ok = bool(sp.simplify(L1 * L2 - L2 * L1 - 2 * L3_) == sp.zeros(DIM, DIM))
    R_bracket_ok = bool(sp.simplify(R1 * R2 - R2 * R1 - 2 * R3_) == sp.zeros(DIM, DIM))
    print(f"\nP2: L bracket [L1,L2]==2*L3? {L_bracket_ok}")
    print(f"P2: R bracket [R1,R2]==2*R3? {R_bracket_ok}")

    p0_calibration_ok = p0_calibration_ok and R_bracket_ok

    if not p0_calibration_ok:
        verdict = "P0_CALIBRATION_FAILED_CONSTRUCTION_BROKEN_NOT_INFORMATIVE"
    elif p1_matches_k1_parity and L_bracket_ok:
        verdict = "K3_MATCHES_K1_PARITY__CONSISTENT_WITH_PARITY_RULE"
    elif p1_matches_k2_parity and L_bracket_ok:
        verdict = "K3_MATCHES_K2_PARITY__PARITY_HYPOTHESIS_FALSIFIED"
    else:
        verdict = "K3_MATCHES_NEITHER__NO_CLEAN_PATTERN_ACROSS_K1_K2_K3"

    out = {
        "per_unit": per_unit,
        "p0_calibration_ok_uniform_bracket_consistent_R": p0_calibration_ok,
        "p1_matches_k1_parity_L_equals_plus_l": p1_matches_k1_parity,
        "p1_matches_k2_parity_L_equals_minus_lT": p1_matches_k2_parity,
        "p2_L_bracket_consistent": L_bracket_ok,
        "p2_R_bracket_consistent": R_bracket_ok,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")


if __name__ == "__main__":
    main()
