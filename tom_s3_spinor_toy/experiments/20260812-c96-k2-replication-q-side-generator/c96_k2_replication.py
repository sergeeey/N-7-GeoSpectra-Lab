"""C96 -- tests whether C95's q-side generator formula (L_i=+l_{e_i}
directly, R_i=-l_{e_i}^T) generalizes from k=1 (the defining/self-
conjugate representation, a special case) to k=2 (spin-1, genuinely
independent replication, as the reviewer's own original proposal
named as required before trusting the k=1 result).

Method: build D^{(2)}(g) as the symmetric square of the defining
representation g=[[a,b],[-conj(b),conj(a)]], with the standard
binomial-normalized basis e_p := v0^{k-p} v1^p / sqrt(C(k,p)). Apply
C95's exact fully-symbolic coefficient-extraction method (sympy's own
Poly.coeff_monomial, zero manual index-tracking) to this D^{(2)}(g)
instead of g itself. Calibrate against C85's certified l_{e_i}(2) via
the R-side (p) result BEFORE trusting anything about the L-side (q)
result -- if the symmetric-square normalization is wrong, R will not
cleanly match a candidate, and that is caught here, not assumed away.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c96.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _build_d2_matrix_raw(a: sp.Expr, b: sp.Expr) -> sp.Matrix:
    """Naive construction: substitute v0->a*v0+b*v1, v1->-conj(b)*v0+
    conj(a)*v1 into the degree-2 monomials v0^2,v0*v1,v1^2 and read off
    coefficients in the ORIGINAL v0,v1. This is a PULLBACK-style
    construction and is NOT by itself the group representation D^{(2)}
    -- verified directly (see build_d2_matrix docstring) to satisfy
    D(g1)*D(g2) = D(g2*g1), an ANTI-homomorphism (composition order
    reversed), not D(g1)*D(g2) = D(g1*g2). Do not call this directly for
    anything requiring a genuine representation; use build_d2_matrix."""
    ac = sp.conjugate(a)
    bc = sp.conjugate(b)
    v0, v1 = sp.symbols("v0 v1")
    v0p = a * v0 + b * v1
    v1p = -bc * v0 + ac * v1

    raw_targets = [v0**2, v0 * v1, v1**2]
    raw_new = [v0p**2, v0p * v1p, v1p**2]

    D = sp.zeros(3, 3)
    for col, expr in enumerate(raw_new):
        expr = sp.expand(expr)
        poly = sp.Poly(expr, v0, v1)
        for row, _target in enumerate(raw_targets):
            monom = [(2, 0), (1, 1), (0, 2)][row]
            coeff = poly.coeff_monomial(v0 ** monom[0] * v1 ** monom[1])
            D[row, col] = sp.simplify(coeff)
    return D


def build_d2_matrix(a: sp.Expr, b: sp.Expr) -> sp.Matrix:
    """D^{(2)}(g), the symmetric-square (spin-1, k=2) representation, as
    an explicit 3x3 matrix in terms of g's own entries a,b,conj(a),
    conj(b), in the RAW (unnormalized) monomial basis |p> = v0^{2-p}
    v1^p, p=0,1,2 -- deliberately NOT the standard unitary-normalized
    basis (e_p = v0^{2-p} v1^p / sqrt(binomial(2,p))).

    Basis-convention correction #1 (same-session, self-caught): an
    earlier draft applied an S=diag(1,1/sqrt(2),1) similarity transform
    to force this matrix to be unitary (D^dagger @ D == I), on the
    unstated assumption that "unitary" is the right/textbook convention.
    That assumption was never checked against what C85's OWN
    build_l_matrices actually uses. Comparing the two directly (P0
    calibration in this round's main()) showed C85's l_{e_i}(2) matrices
    are NOT anti-Hermitian in their own |p> basis (e.g. l2[0,1]=1 but
    l2[1,0]=-2, not antisymmetric) -- i.e. C85 already uses the RAW,
    non-unitary monomial basis (matching Meier's own eq 6.1-6.3), not a
    unitary one. Removed the S-transform so this matrix is expressed in
    the SAME basis convention as C85's l matrices.

    Basis-convention correction #2 (same-session, self-caught, more
    serious): even after fix #1, the P0/P1/P2 checks in main() found
    P0 matched a candidate ("-l" uniformly, not "-lT") that is
    ALGEBRAICALLY GUARANTEED to fail the su(2) bracket check given any
    l_i satisfying [l1,l2]=2l3 (a pure Lie-algebra fact, independent of
    any specific matrix values -- only "+l_i" and "-l_i^T" survive
    [R1,R2]=2R3; "-l_i" and "+l_i^T" generically do not). And indeed
    P2's OWN bracket check on the freshly-computed L_op/R_op (not just
    candidate-label matching) failed for both. Traced to the root:
    _build_d2_matrix_raw(a,b), built by literally substituting
    v0->a*v0+b*v1 etc and reading off coefficients, is an
    ANTI-homomorphism: D(g1)*D(g2) = D(g2*g1), verified directly by
    symbolic composition of two independent SU(2) elements (not
    D(g1)*D(g2) = D(g1*g2) as a genuine representation requires). This
    is the classic pullback-vs-pushforward sign trap: substituting the
    transformed variables into a polynomial computes the DUAL/pullback
    action, which composes in reverse order. The standard fix: a genuine
    (order-preserving) representation is recovered via D(g) :=
    D_raw(g^{-1}). For g=[[a,b],[-conj(b),conj(a)]] in SU(2), g^{-1} has
    (A,B) = (conj(a), -b) in the same parametrization -- verified
    directly: D_raw(conj(a),-b) satisfies D(g1)*D(g2) = D(g1*g2) exactly
    for two independent symbolic SU(2) elements, confirming the fix."""
    return _build_d2_matrix_raw(sp.conjugate(a), -b)


def coefficient_space_generator_general(
    action: str, X: sp.Matrix, D: sp.Matrix, eps: sp.Symbol, dim: int
) -> sp.Matrix:
    """Generalizes C95's coefficient_space_generator to arbitrary dim.
    D is the (dim x dim) representation matrix (symbols for its own
    entries substituted via build_d2_matrix's own a,b symbols)."""
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
    D2 = build_d2_matrix(a, b)
    print("D^{(2)}(g) built. Verifying it's genuinely 3x3 and depends on a,b:")
    print(D2)

    l1, l2, l3 = c85.build_l_matrices(2, "repaired")
    l_mats = {"e1_i": l1, "e2_j": l2, "e3_k": l3}

    # D_sym: abstract free-symbol stand-in for D^{(2)}(g)'s own matrix
    # entries, matching C95's g00/g01/g10/g11 convention exactly. This is
    # NOT the same object as D2_generic (build_d2_matrix's literal
    # polynomial-in-a,b output) -- coefficient_space_generator_general
    # needs D's entries to be free symbols so that, after sp.expand,
    # Poly.coeff_monomial can still recognize them as generators. Using
    # D2_generic directly here was a genuine bug in the first draft: its
    # entries are compound polynomials in aw,ax,bw,bx, which sp.expand
    # dissolves into raw aw/ax/bw/bx monomials, so no coefficient of any
    # D[i,j] "generator" could ever be found -- coeff_monomial silently
    # returned 0 for everything, producing all-zero L_op/R_op that passed
    # the bracket check only because 0=0 trivially. Caught because P0
    # (calibration against C85's certified l_{e_i}(2)) failed outright,
    # per this round's own kill_criterion.
    D_sym = sp.Matrix(3, 3, sp.symbols("D0:3(0:3)"))

    eps = sp.symbols("eps", real=True)
    per_unit = {}
    for name, R_i in l_mats.items():
        # X3x3 IS correctly obtained by differentiating the true, nonlinear
        # D2_h(a(eps),b(eps)) directly -- this is the standard fact that
        # matrix-coefficient functions of any representation D(g) transform
        # under left/right translation via D(g)'s OWN generator X, linearly
        # in the coefficients, regardless of D(g)'s nonlinearity in g's own
        # parameters. Only the SECOND step (coefficient extraction) needs
        # the abstract D_sym treatment above.
        w0, x0, y0, z0 = {
            "e1_i": (0, 1, 0, 0),
            "e2_j": (0, 0, 1, 0),
            "e3_k": (0, 0, 0, 1),
        }[name]
        a_eps = 1 + eps * w0 + sp.I * eps * x0
        b_eps = eps * y0 + sp.I * eps * z0
        D2_h = build_d2_matrix(a_eps, b_eps)
        X3x3 = sp.simplify(D2_h.applyfunc(lambda e: sp.diff(e, eps).subs(eps, 0)))

        candidates = {"+l": R_i, "-l": -R_i, "+lT": R_i.T, "-lT": -R_i.T}
        L_op = coefficient_space_generator_general("L", X3x3, D_sym, eps, 3)
        R_op = coefficient_space_generator_general("R", X3x3, D_sym, eps, 3)
        L_match = [n for n, c in candidates.items() if sp.simplify(L_op - c) == sp.zeros(3, 3)]
        R_match = [n for n, c in candidates.items() if sp.simplify(R_op - c) == sp.zeros(3, 3)]
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
    print(f"P1 (L common candidate): {sorted(L_common)}")

    # p0_holds is the LITERAL kill_criterion from claim.md: "does R match
    # ONE of the four candidates uniformly, with the bracket holding" --
    # NOT "does it match the specific -lT guess written in the P0 table
    # row". That guess was carried over from C95's k=1 result without
    # re-derivation and turned out wrong (see p0_matches_prediction
    # below) -- an honest miss recorded the same way C95 recorded its
    # own P2 miss ("-l" predicted, "-lT" found), not a redefinition of
    # what "calibration passing" means after the fact.
    p0_matches_prediction = "-lT" in R_common
    p1_matches_prediction = "+l" in L_common

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
    L_bracket_ok = bool(sp.simplify(L1 * L2 - L2 * L1 - 2 * L3_) == sp.zeros(3, 3))
    R_bracket_ok = bool(sp.simplify(R1 * R2 - R2 * R1 - 2 * R3_) == sp.zeros(3, 3))
    print(f"\nP2: L bracket [L1,L2]==2*L3? {L_bracket_ok}")
    print(f"P2: R bracket [R1,R2]==2*R3? {R_bracket_ok}")

    p0_calibration_ok = len(R_common) == 1 and R_bracket_ok
    p1_matches_k1_pattern = p1_matches_prediction and L_bracket_ok
    fully_confirmed = p0_calibration_ok and p1_matches_k1_pattern

    if not p0_calibration_ok:
        verdict = "P0_CALIBRATION_FAILED_CONSTRUCTION_BROKEN_NOT_INFORMATIVE_ABOUT_C95"
    elif fully_confirmed:
        verdict = "K2_REPLICATION_CONFIRMED__C95_FORMULA_GENERALIZES"
    else:
        verdict = "K2_REPLICATION_DIVERGES_FROM_K1__C95_FORMULA_IS_K_SPECIFIC"

    out = {
        "per_unit": per_unit,
        "p0_calibration_ok_uniform_bracket_consistent_R": p0_calibration_ok,
        "p0_matches_specific_prediction_minus_lT": p0_matches_prediction,
        "p1_matches_specific_prediction_plus_l": p1_matches_prediction,
        "p2_L_bracket_consistent": L_bracket_ok,
        "p2_R_bracket_consistent": R_bracket_ok,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")


if __name__ == "__main__":
    main()
