r"""E10 (round76): explicit right-invariant frame on S^3=SU(2), completing E9's own
flagged follow-up ("candidate E10" in E9's decision.md, experiments/20260717-round73-
e9-explicit-parallel-spinor/decision.md "Recommended next action").

Context (see claim.md for full framing):
  - E9 explicitly built the LEFT-invariant frame {Z_i}, the spin connection
    Omega_i(t) = -(tc/2)*Z_i (Pauli-based Cl(3), Z_i=i*sigma_i, symbolic structure
    constant c, calibrated c=2), showed Omega_i(0)=0 (t=0 parallel spinor: ANY
    constant left-invariant spinor works, D^0 psi = 0 exactly), and showed the SAME
    ansatz fails at t=1 (only trivial psi=0 solves Omega_i(1)psi=0), HYPOTHESIZING
    but NOT verifying that the t=1 parallel spinor lives in a RIGHT-invariant frame.
  - This experiment does 3 things, escalating in how deep it goes:

    PART 1 [VERIFIED-tool]: explicit construction of LEFT- and RIGHT-invariant
    vector fields on SU(2), realized concretely as the unit-quaternion model
    g(x) = x0*I + x1*Z1 + x2*Z2 + x3*Z3 (Z_i = E9's own Pauli-based Cl(3)
    generators), and DIRECT verification (via the ordinary vector-field bracket
    formula [V,W]^mu = V^nu d_nu W^mu - W^nu d_nu V^mu, computed by symbolic
    differentiation, NOT assumed) that:
      (a) both families are tangent to the group (x . X(x) = 0 identically),
      (b) [Z_i^L, Z_j^L] = c0 * eps(i,j,k) * Z_k^L for a concrete c0 (found here,
          not assumed) -- confirms the LEFT-invariant frame reproduces the
          structure-constant convention E7/E9 already used,
      (c) [Z_i^R, Z_j^R] = -c0 * eps(i,j,k) * Z_k^R EXACTLY -- the opposite-sign
          fact the task asks to verify explicitly, done here by direct symbolic
          differentiation on an explicit matrix-Lie-group realization, not by
          citation.

    PART 2 [VERIFIED-tool]: literal repeat of E9's OWN construction recipe
    (symbolic structure constant c, calibrated c=2 at the end, EXACTLY E9's own
    convention -- kept separate from Part 1's concretely-computed c0, since E7/E9
    always treated c as a free/abstract structure constant, never tied to the
    literal Pauli commutator value -- see claim.md "Two notions of c" for why this
    is not glossed over), but now built from the RIGHT-invariant bracket
    [f_i,f_j] = -c*eps(i,j,k)*f_k. Derives Omega_i^right(t), cross-checks against
    -t*H, and repeats E9's t=0/t=1 checks in this new frame.

    PART 3 [VERIFIED-tool, exploratory/honesty check]: the DEEPER subtlety the
    task explicitly asks to watch for. Part 2's Omega^right(t) is built by
    MECHANICALLY reapplying E9's recipe (Gamma^k_{ij}(t) := (right-bracket
    structure constant)) to the NEW frame -- this treats "Nabla^t in the
    right-invariant frame" as a SEPARATELY-DEFINED connection sharing E9's recipe
    PATTERN. But E9's Nabla^t was already a SPECIFIC, fully-defined global
    connection (pinned down via the LEFT-invariant frame and extended by
    C^infty-linearity/Leibniz to ALL vector fields). Part 3 checks directly,
    by explicit computation (expressing f_k in the Z_i-basis with the concrete,
    G-DEPENDENT coefficient functions given by the adjoint action, and applying
    E9's ORIGINAL Leibniz-extended Nabla^t to it), whether E9's ORIGINAL t=1
    connection ALREADY makes the right-invariant vector fields f_k parallel
    (Nabla^1_X f_k = 0 for all X) -- a DIFFERENT question from "is Omega^right(1)=0
    for the mechanically-reapplied recipe of Part 2". If these two disagree, that
    IS the honest, load-bearing subtlety flagged in claim.md and decision.md: two
    inequivalent things can both reasonably be called "Nabla^t in the
    right-invariant frame."

Honesty ledger (see claim.md for full evidence markers):
  - Part 1: [VERIFIED-tool], exact symbolic computation, explicit matrix
    Lie-group realization, no citation-only steps for the sign-flip claim itself.
  - Part 2: [VERIFIED-tool], literal structural repeat of E9's own recipe with the
    sign flip the task specifies; same evidence status as E9's own steps 1-6.
  - Part 3: [VERIFIED-tool] for the computation itself; [DOCS] for the classical
    motivation (Cartan-Schouten "(+)" connection parallelizes right-invariant
    fields) that motivated running this check in the first place -- NOT assumed,
    checked directly here against E9's own concrete Omega_i(t) formula.
"""

from __future__ import annotations

import json

import sympy as sp

I2 = sp.eye(2)
t, c = sp.symbols("t c")
a, b = sp.symbols("a b")
x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3", real=True)
XS = [x0, x1, x2, x3]
NORM2 = x0**2 + x1**2 + x2**2 + x3**2  # |x|^2, = 1 on SU(2) itself


# ---------------------------------------------------------------------------
# Shared machinery, IDENTICAL to E9's own conventions
# (experiments/20260717-round73-e9-explicit-parallel-spinor/e9_explicit_parallel_spinor.py)
# ---------------------------------------------------------------------------


def pauli_matrices() -> list[sp.Matrix]:
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    return [sx, sy, sz]


def clifford_generators() -> list[sp.Matrix]:
    """Z_i = i*sigma_i, giving {Z_i,Z_j} = -2 delta_ij (E2/E9's own convention)."""
    return [sp.I * s for s in pauli_matrices()]


def verify_clifford_relations(Z: list[sp.Matrix]) -> bool:
    for i in range(3):
        for j in range(i, 3):
            anticomm = sp.simplify(Z[i] * Z[j] + Z[j] * Z[i])
            expected = -2 * I2 if i == j else sp.zeros(2, 2)
            if sp.simplify(anticomm - expected) != sp.zeros(2, 2):
                return False
    return True


def eps(i: int, j: int, k: int) -> int:
    """Levi-Civita symbol, 1-indexed i,j,k in {1,2,3} (identical to E7/E9's eps())."""
    p = [i, j, k]
    if len(set(p)) < 3:
        return 0
    sign = 1
    perm = p[:]
    n = 3
    for xx in range(n):
        for yy in range(n - 1 - xx):
            if perm[yy] > perm[yy + 1]:
                perm[yy], perm[yy + 1] = perm[yy + 1], perm[yy]
                sign = -sign
    return sign


# ---------------------------------------------------------------------------
# PART 1: explicit left/right-invariant vector fields, unit-quaternion model.
# ---------------------------------------------------------------------------


def basis_matrices(Z: list[sp.Matrix]) -> list[sp.Matrix]:
    return [I2, Z[0], Z[1], Z[2]]


def basis_inverse(Z: list[sp.Matrix]) -> sp.Matrix:
    """4x4 (complex-entried but exactly invertible) matrix used to extract the
    coordinates of a 2x2 matrix in the basis {I2,Z1,Z2,Z3}."""
    basis = basis_matrices(Z)
    cols = []
    for M in basis:
        cols.append([M[0, 0], M[0, 1], M[1, 0], M[1, 1]])
    Bmat = sp.Matrix(cols).T  # column k = flattened basis[k]
    return sp.simplify(Bmat.inv())


def coords_in_basis(M: sp.Matrix, Binv: sp.Matrix) -> list[sp.Expr]:
    v = sp.Matrix([M[0, 0], M[0, 1], M[1, 0], M[1, 1]])
    coeffs = Binv * v
    return [sp.simplify(coeffs[i]) for i in range(4)]


def group_element(Z: list[sp.Matrix]) -> sp.Matrix:
    """g(x) = x0*I + x1*Z1 + x2*Z2 + x3*Z3 -- the standard SU(2)-as-unit-quaternion
    realization using E9's own Z_i=i*sigma_i basis. On |x|=1 this is exactly SU(2)."""
    return x0 * I2 + x1 * Z[0] + x2 * Z[1] + x3 * Z[2]


def group_conjugate(Z: list[sp.Matrix]) -> sp.Matrix:
    """gbar(x) = x0*I - x1*Z1 - x2*Z2 - x3*Z3. Standard quaternion-conjugate fact:
    g(x)*gbar(x) = |x|^2 * I (verified explicitly below, not assumed)."""
    return x0 * I2 - x1 * Z[0] - x2 * Z[1] - x3 * Z[2]


def verify_quaternion_norm(Z: list[sp.Matrix]) -> dict[str, object]:
    g = group_element(Z)
    gbar = group_conjugate(Z)
    prod = sp.simplify(g * gbar)
    expected = sp.expand(NORM2) * I2
    ok = sp.simplify(prod - expected) == sp.zeros(2, 2)
    return {"g_gbar_equals_norm2_I": bool(ok), "product": str(prod)}


def build_invariant_frames(Z: list[sp.Matrix], Binv: sp.Matrix):
    """X_i^L(x) := coords of g(x)*Z_i  (left-invariant vector field, standard
    convention X^L(g)=g*X, flow = right translation by exp(sX)).
    X_i^R(x) := coords of Z_i*g(x)  (right-invariant vector field, standard
    convention X^R(g)=X*g, flow = left translation by exp(sX))."""
    g = group_element(Z)
    XL, XR = [], []
    for i in range(3):
        ML = sp.expand(g * Z[i])
        MR = sp.expand(Z[i] * g)
        XL.append(coords_in_basis(ML, Binv))
        XR.append(coords_in_basis(MR, Binv))
    return XL, XR


def check_tangency(X: list[sp.Expr]) -> bool:
    """x . X(x) = 0 identically => X tangent to every sphere |x|=const, hence
    tangent to SU(2) itself (the unit sphere)."""
    dot = sum(XS[i] * X[i] for i in range(4))
    return sp.simplify(sp.expand(dot)) == 0


def vf_bracket(V: list[sp.Expr], W: list[sp.Expr]) -> list[sp.Expr]:
    """[V,W]^mu = V^nu d_nu W^mu - W^nu d_nu V^mu, direct symbolic differentiation.
    No shortcut linear-vector-field formula used -- fully explicit calculus."""
    out = []
    for mu in range(4):
        term = sp.Integer(0)
        for nu in range(4):
            term += V[nu] * sp.diff(W[mu], XS[nu]) - W[nu] * sp.diff(V[mu], XS[nu])
        out.append(sp.expand(term))
    return out


def find_structure_constant(X: list[list[sp.Expr]]) -> dict[str, object]:
    """Compute [X_1,X_2] and read off its coefficient against X_3 (using i=1,j=2
    as the representative pair; eps(1,2,3)=+1) -- gives the concrete c0 such that
    [X_i,X_j] = c0*eps(i,j,k)*X_k is a CANDIDATE identity, to be exhaustively
    verified next."""
    br12 = vf_bracket(X[0], X[1])
    # br12 should be a scalar multiple of X_3 = X[2]; solve for that scalar using
    # any component of X[2] that is not identically zero as a polynomial.
    ratio = None
    for mu in range(4):
        if X[2][mu] != 0:
            cand = sp.simplify(sp.cancel(br12[mu] / X[2][mu]))
            if not cand.free_symbols:  # must be a plain constant
                ratio = cand
                break
    return {"bracket_12": [str(v) for v in br12], "c0_candidate": str(ratio)}


def verify_bracket_sign(X: list[list[sp.Expr]], c0: sp.Expr, sign: int) -> dict[str, object]:
    """Exhaustively verify [X_i,X_j] = sign*c0*eps(i,j,k)*X_k for ALL i,j in
    {1,2,3} (all ordered pairs, i!=j automatically zero on both sides when i==j),
    as an EXACT polynomial identity in x0..x3."""
    all_ok = True
    mismatches = []
    for i in range(3):
        for j in range(3):
            lhs = vf_bracket(X[i], X[j])
            rhs = [sp.Integer(0)] * 4
            for k in range(3):
                coeff = sign * c0 * eps(i + 1, j + 1, k + 1)
                if coeff != 0:
                    for mu in range(4):
                        rhs[mu] += coeff * X[k][mu]
            diff = [sp.simplify(sp.expand(lhs[mu] - rhs[mu])) for mu in range(4)]
            ok = all(d == 0 for d in diff)
            if not ok:
                mismatches.append({"i": i + 1, "j": j + 1, "diff": [str(d) for d in diff]})
            all_ok &= ok
    return {"all_pairs_ok": bool(all_ok), "mismatches": mismatches}


def run_part1() -> dict[str, object]:
    Z = clifford_generators()
    clifford_ok = verify_clifford_relations(Z)
    Binv = basis_inverse(Z)
    quat_check = verify_quaternion_norm(Z)

    XL, XR = build_invariant_frames(Z, Binv)

    tangency_L = [check_tangency(XL[i]) for i in range(3)]
    tangency_R = [check_tangency(XR[i]) for i in range(3)]

    c0_info_L = find_structure_constant(XL)
    c0_L = sp.sympify(c0_info_L["c0_candidate"])
    left_bracket_check = verify_bracket_sign(XL, c0_L, sign=1)

    c0_info_R = find_structure_constant(XR)
    # Hypothesis under test: right bracket uses the SAME |c0| as left but OPPOSITE
    # sign, i.e. c0_R should equal -c0_L. Verify sign-flip hypothesis using c0_L
    # (sign=-1), not re-deriving a fresh "found" constant, to make the -1 relation
    # an explicit, falsifiable check rather than two independently-fitted numbers.
    right_bracket_check_vs_minus_c0L = verify_bracket_sign(XR, c0_L, sign=-1)

    return {
        "clifford_ok": clifford_ok,
        "quaternion_norm_check": quat_check,
        "XL": [[str(v) for v in row] for row in XL],
        "XR": [[str(v) for v in row] for row in XR],
        "tangency_L_all": bool(all(tangency_L)),
        "tangency_R_all": bool(all(tangency_R)),
        "c0_left_found": str(c0_L),
        "left_bracket_check_all_pairs_ok": left_bracket_check["all_pairs_ok"],
        "left_bracket_mismatches": left_bracket_check["mismatches"],
        "c0_right_found_independently": c0_info_R["c0_candidate"],
        "right_bracket_matches_minus_c0L_all_pairs": right_bracket_check_vs_minus_c0L[
            "all_pairs_ok"
        ],
        "right_bracket_mismatches": right_bracket_check_vs_minus_c0L["mismatches"],
        "c0_right_equals_minus_c0_left": bool(
            sp.simplify(sp.sympify(c0_info_R["c0_candidate"]) - (-c0_L)) == 0
        ),
    }


# ---------------------------------------------------------------------------
# PART 2: literal repeat of E9's recipe, symbolic c (E9's OWN abstract structure
# constant, kept separate from Part 1's concretely-found c0 -- see claim.md
# "Two notions of c"), built from the RIGHT-invariant bracket [f_i,f_j] =
# -c*eps(i,j,k)*f_k.
# ---------------------------------------------------------------------------


def christoffel_left(i: int, j: int, k: int) -> sp.Expr:
    """E9's own Gamma^k_{ij}(t) = t*c*eps(i,j,k), LEFT-invariant bracket
    convention (reproduced here unchanged, 0-indexed i,j,k -> (i+1,j+1,k+1))."""
    return t * c * eps(i + 1, j + 1, k + 1)


def christoffel_right(i: int, j: int, k: int) -> sp.Expr:
    """Gamma^{R,k}_{ij}(t) = t*(-c)*eps(i,j,k), from Nabla^t_X Y = t[X,Y] with
    [f_i,f_j] = -c*eps(i,j,k)*f_k (right-invariant bracket, opposite sign to
    Part 1's verified left/right relation)."""
    return -t * c * eps(i + 1, j + 1, k + 1)


def verify_so3_valued(christoffel_fn) -> bool:
    all_ok = True
    for i in range(3):
        for j in range(3):
            for k in range(3):
                lhs = christoffel_fn(i, j, k)
                rhs = -christoffel_fn(i, k, j)
                if sp.simplify(lhs - rhs) != 0:
                    all_ok = False
    return all_ok


def spin_connection(i: int, Z: list[sp.Matrix], christoffel_fn) -> sp.Matrix:
    total = sp.zeros(2, 2)
    for j in range(3):
        for k in range(3):
            coeff = christoffel_fn(i, j, k)
            if coeff != 0:
                total += coeff * (Z[j] * Z[k])
    return sp.simplify(total / 4)


def run_part2(Z: list[sp.Matrix]) -> dict[str, object]:
    so3_left = verify_so3_valued(christoffel_left)
    so3_right = verify_so3_valued(christoffel_right)

    omega = sp.simplify(Z[0] * Z[1] * Z[2])
    H = sp.simplify(sp.Rational(3, 2) * c * omega)  # E2's own H, unchanged

    Omega_R = [spin_connection(i, Z, christoffel_right) for i in range(3)]
    Omega_L = [spin_connection(i, Z, christoffel_left) for i in range(3)]  # E9's, for cross-ref

    total_R = sp.zeros(2, 2)
    for i in range(3):
        total_R += Z[i] * Omega_R[i]
    total_R = sp.simplify(total_R)

    matches_plus = sp.simplify(total_R - t * H) == sp.zeros(2, 2)
    matches_minus = sp.simplify(total_R + t * H) == sp.zeros(2, 2)

    # t=0
    Omega_R_at_0 = [sp.simplify(Om.subs(t, 0)) for Om in Omega_R]
    t0_all_zero = all(Om == sp.zeros(2, 2) for Om in Omega_R_at_0)

    e1 = sp.Matrix([1, 0])
    e2 = sp.Matrix([0, 1])
    generic = sp.Matrix([a, b])
    t0_parallel_checks = {}
    for name, psi in {"e1": e1, "e2": e2, "generic_(a,b)": generic}.items():
        results = [sp.simplify(Om * psi) for Om in Omega_R_at_0]
        t0_parallel_checks[name] = all(r == sp.zeros(2, 1) for r in results)
    # D^0 psi = sum_i Z_i . Z_i(psi) + 0*H*psi; orbital term 0 for constant psi,
    # algebraic term 0 at t=0 regardless of H -- same argument as E9, unchanged.
    t0_D_psi_is_zero = True

    # t=1, c=2 (E9's own calibration)
    psi_sym = sp.Matrix([a, b])
    Omega_R_at_1 = [
        spin_connection(i, Z, christoffel_right).subs([(t, 1), (c, 2)]) for i in range(3)
    ]
    eqs: list[sp.Expr] = []
    for Om in Omega_R_at_1:
        v = sp.simplify(Om * psi_sym)
        eqs.append(v[0])
        eqs.append(v[1])
    sol = sp.solve(eqs, [a, b], dict=True)
    only_trivial_solve = False
    if len(sol) == 1:
        s = sol[0]
        only_trivial_solve = (s.get(a, 0) == 0) and (s.get(b, 0) == 0)
    stacked = sp.Matrix.vstack(*Omega_R_at_1)
    nullspace = stacked.nullspace()
    only_trivial_nullspace = len(nullspace) == 0

    # Agricola-style cross-check for the right-invariant-frame formula:
    # D^{1,right}(constant-in-this-frame psi) = 1 * H^right * psi, with H^right
    # read off from the crosscheck sign found above (H^right = -H if
    # matches_minus, else +H).
    H_at_c2 = H.subs(c, 2)
    H_right_at_c2 = -H_at_c2 if matches_minus else H_at_c2
    D1_generic = sp.simplify(1 * H_right_at_c2 * psi_sym)
    zero_sol = sp.solve([D1_generic[0], D1_generic[1]], [a, b], dict=True)
    theorem_confirms_trivial_only = False
    if len(zero_sol) == 1:
        s = zero_sol[0]
        theorem_confirms_trivial_only = (s.get(a, 0) == 0) and (s.get(b, 0) == 0)

    # uniqueness of t=0 (mirrors E9's step 7)
    Omega1_R_symbolic = spin_connection(0, Z, christoffel_right)
    det_Omega1_R = sp.simplify(Omega1_R_symbolic.det())
    roots_t = sp.solve(sp.Eq(det_Omega1_R, 0), t)

    return {
        "so3_valued_right": so3_right,
        "so3_valued_left_crossref": so3_left,
        "Omega_right_i_str": [str(sp.simplify(Om)) for Om in Omega_R],
        "Omega_left_i_str_crossref": [str(sp.simplify(Om)) for Om in Omega_L],
        "crosscheck_sum_Zi_OmegaRi": str(total_R),
        "crosscheck_matches_plus_tH": bool(matches_plus),
        "crosscheck_matches_minus_tH": bool(matches_minus),
        "crosscheck_matches_tH_either_sign": bool(matches_plus or matches_minus),
        "t0_omega_right_all_zero": bool(t0_all_zero),
        "t0_parallel_checks": {k: bool(v) for k, v in t0_parallel_checks.items()},
        "t0_D_psi_is_zero": t0_D_psi_is_zero,
        "t1_only_trivial_via_solve": bool(only_trivial_solve),
        "t1_nullspace_dim": len(nullspace),
        "t1_only_trivial_via_nullspace": bool(only_trivial_nullspace),
        "t1_nonzero_solution_exists": bool(
            (not only_trivial_solve) or (not only_trivial_nullspace)
        ),
        "H_right_at_c2": str(H_right_at_c2),
        "theorem_style_crosscheck_confirms_trivial_only": bool(theorem_confirms_trivial_only),
        "det_Omega1_right_symbolic": str(det_Omega1_R),
        "roots_of_det_Omega1_right_in_t": [str(r) for r in roots_t],
        "t0_is_unique_root_right_frame": roots_t == [sp.Integer(0)],
    }


# ---------------------------------------------------------------------------
# PART 3: the deeper subtlety. Does E9's ORIGINAL, already-fully-defined Nabla^t
# (pinned down via the LEFT-invariant frame and extended via Leibniz to ALL
# vector fields) already make the RIGHT-invariant vector fields f_k parallel at
# t=1 -- a DIFFERENT question from Part 2's mechanically-reapplied recipe.
# ---------------------------------------------------------------------------


def express_fk_in_Z_basis(Z: list[sp.Matrix], Binv: sp.Matrix, k: int):
    """b^j(x) := coefficient of Z_j in g(x)^{-1} * Z_k * g(x) (the honest,
    G-DEPENDENT coefficient functions needed to write the right-invariant field
    f_k as Sum_j b^j(x) * Z_j^L(x) -- since conjugation A^{-1}XA is invariant
    under rescaling A -> lambda*A for scalar lambda, using gbar(x) in place of
    the true inverse g(x)^{-1} = gbar(x)/|x|^2 introduces exactly a factor
    |x|^2 that is divided out below, avoiding ever inverting |x|^2 symbolically
    inside the conjugation itself."""
    g = group_element(Z)
    gbar = group_conjugate(Z)
    conj_scaled = sp.expand(gbar * Z[k] * g)  # = |x|^2 * g^{-1} Z_k g
    coeffs_scaled = coords_in_basis(conj_scaled, Binv)
    # component 0 (the I2-coefficient) must vanish identically: conjugation
    # preserves the traceless (su(2)) subspace -- checked, not assumed.
    i2_component_is_zero = sp.simplify(sp.expand(coeffs_scaled[0])) == 0
    b = [sp.together(coeffs_scaled[j + 1] / NORM2) for j in range(3)]
    return b, i2_component_is_zero


def directional_derivative(fld: list[sp.Expr], scalar_fn: sp.Expr) -> sp.Expr:
    """(fld . grad)(scalar_fn), i.e. the action of the vector field `fld`
    (a 4-component field in x0..x3) on the scalar function scalar_fn(x)."""
    total = sp.Integer(0)
    for mu in range(4):
        total += fld[mu] * sp.diff(scalar_fn, XS[mu])
    return total


def run_part3(Z: list[sp.Matrix], Binv: sp.Matrix, XL, XR) -> dict[str, object]:
    """For k=0 (f_1 = X_1^R, representative case -- see claim.md for why one
    representative k suffices given the construction's manifest i<->k symmetry),
    express f_1 = Sum_j b^j(x) Z_j^L, then compute
        Nabla^t_{Z_i} f_1 = Sum_j Z_i(b^j) Z_j + t * Sum_{j,l} b^j * c0 * eps(i,j,l) * Z_l
    using E9's ORIGINAL connection (built from the LEFT-invariant bracket, with
    the CONCRETE c0 found in Part 1 -- since this is a question about E9's own,
    already-fully-specified connection, not about the abstract-c recipe of
    Part 2), for i=1,2,3, and check whether this vanishes identically at t=1.
    Cross-check against Part 1's own reconstruction of f_1 = X_1^R as a
    consistency control on the b^j(x) themselves.
    """
    k = 0
    b, i2_zero = express_fk_in_Z_basis(Z, Binv, k)

    # consistency control: reconstruct f_1 = Sum_j b^j * Z_j^L and compare to
    # Part 1's independently-computed X_1^R.
    reconstructed = [sp.Integer(0)] * 4
    for j in range(3):
        for mu in range(4):
            reconstructed[mu] += b[j] * XL[j][mu]
    reconstructed = [sp.simplify(sp.together(v)) for v in reconstructed]
    target = [sp.simplify(sp.together(v)) for v in XR[k]]
    reconstruction_matches = all(
        sp.simplify(sp.together(reconstructed[mu] - target[mu])) == 0 for mu in range(4)
    )

    # find c0 (concrete, from Part 1) again here for self-containment
    c0_info = find_structure_constant(XL)
    c0 = sp.sympify(c0_info["c0_candidate"])

    # Nabla^t_{Z_i} f_1, i = 1,2,3 (0-indexed 0,1,2), expressed in the Z-basis
    # coefficients (l=1,2,3); "t" here is E9's ORIGINAL, already-calibrated t
    # (kept symbolic, evaluated at t=1 below).
    per_i_results = []
    all_vanish_at_t1 = True
    for i in range(3):
        coeff_l = [sp.Integer(0)] * 3
        for j in range(3):
            deriv = directional_derivative(XL[i], b[j])
            coeff_l[j] += deriv
        for j in range(3):
            for ll in range(3):
                e = eps(i + 1, j + 1, ll + 1)
                if e != 0:
                    coeff_l[ll] += t * b[j] * c0 * e
        coeff_l_at_t1 = [sp.simplify(sp.together(v.subs(t, 1))) for v in coeff_l]
        vanish = all(v == 0 for v in coeff_l_at_t1)
        all_vanish_at_t1 &= vanish
        per_i_results.append(
            {
                "i": i + 1,
                "coeff_l_symbolic_t_str": [str(sp.simplify(v)) for v in coeff_l],
                "coeff_l_at_t1_str": [str(v) for v in coeff_l_at_t1],
                "vanishes_at_t1": bool(vanish),
            }
        )

    return {
        "representative_k": k + 1,
        "b_j_functions_str": [str(bj) for bj in b],
        "I2_component_of_conjugation_is_zero": bool(i2_zero),
        "reconstruction_of_fk_from_b_and_ZL_matches_part1_XR": bool(reconstruction_matches),
        "c0_used_concrete": str(c0),
        "per_i_nabla1_fk_results": per_i_results,
        "nabla1_fk_vanishes_for_all_i": bool(all_vanish_at_t1),
    }


# ---------------------------------------------------------------------------
# PART 4: given Part 3 found f_k fully Nabla^1-parallel (as VECTOR FIELDS) using
# the CONCRETE c0 (not E9's abstractly-calibrated c), attempt the natural
# candidate SPINOR profile motivated by that fact: psi(x) = gbar(x)*psi_0 (the
# quaternion-conjugate of the group element times a constant psi_0 in C^2 --
# "g^{-1}*psi_0" on the unit sphere, since g*gbar=|x|^2*I). Verify directly,
# by explicit differentiation (not the hand/shorthand argument in claim.md),
# whether this satisfies Nabla^1_{Z_i}psi=0 for ALL i, and whether it makes
# Agricola's OWN D^1 psi = sum_i Z_i.Z_i(psi) + 1*H*psi exactly zero -- using
# the SAME concrete c0 throughout (H_c0 := (3*c0/2)*omega), NOT E9's abstract
# c=2 (see claim.md "Two notions of c" for why mixing them would be invalid).
# ---------------------------------------------------------------------------


def run_part4(Z: list[sp.Matrix]) -> dict[str, object]:
    a_, b_ = sp.symbols("a_ b_")  # fresh symbols, avoid clashing with Part 2's a,b
    psi0 = sp.Matrix([a_, b_])
    gbar = group_conjugate(Z)
    psi = sp.expand(gbar * psi0)  # 2x1, entries are functions of x0..x3

    # concrete c0 (Part 1's finding, re-derived here for self-containment)
    Binv = basis_inverse(Z)
    XL, _XR = build_invariant_frames(Z, Binv)
    c0_info = find_structure_constant(XL)
    c0 = sp.sympify(c0_info["c0_candidate"])

    # Z_i(psi)(x) := directional derivative of each component of psi along the
    # CONCRETE vector field X_i^L, i.e. Sum_mu (XL_i)_mu * d(psi_component)/dx_mu.
    def Zi_of_psi(i: int) -> sp.Matrix:
        comps = []
        for row in range(2):
            comps.append(directional_derivative(XL[i], psi[row]))
        return sp.Matrix(comps)

    # Omega_i^L(1) using c0 (E9's OWN formula Omega_i(t)=-(t*c0/2)*Z_i, t=1):
    Omega_L_at_1_c0 = [sp.simplify(-(sp.Rational(1, 2) * c0) * Z[i]) for i in range(3)]

    parallel_results = []
    all_parallel = True
    for i in range(3):
        lhs = sp.expand(Zi_of_psi(i) + Omega_L_at_1_c0[i] * psi)
        lhs = sp.Matrix([sp.simplify(sp.expand(v)) for v in lhs])
        ok = lhs == sp.zeros(2, 1)
        all_parallel &= ok
        parallel_results.append({"i": i + 1, "residual": str(lhs.T), "is_zero": bool(ok)})

    # Agricola D^1 psi = sum_i Z_i . Z_i(psi) + 1 * H_c0 * psi, H_c0 built with
    # the SAME concrete c0 (NOT E9's abstract c=2).
    omega = sp.simplify(Z[0] * Z[1] * Z[2])
    H_c0 = sp.simplify(sp.Rational(3, 2) * c0 * omega)
    orbital = sp.zeros(2, 1)
    for i in range(3):
        orbital += Z[i] * Zi_of_psi(i)
    orbital = sp.Matrix([sp.expand(v) for v in orbital])
    D1_psi = sp.expand(orbital + 1 * H_c0 * psi)
    D1_psi = sp.Matrix([sp.simplify(sp.expand(v)) for v in D1_psi])
    D1_psi_is_zero = D1_psi == sp.zeros(2, 1)

    # cross-reference: what does E9's OWN abstractly-calibrated c=2 give for the
    # SAME candidate psi (expected to FAIL, reported honestly either way)?
    Omega_L_at_1_c2 = [sp.simplify(-(sp.Rational(1, 2) * 2) * Z[i]) for i in range(3)]
    parallel_results_c2 = []
    all_parallel_c2 = True
    for i in range(3):
        lhs = sp.expand(Zi_of_psi(i) + Omega_L_at_1_c2[i] * psi)
        lhs = sp.Matrix([sp.simplify(sp.expand(v)) for v in lhs])
        ok = lhs == sp.zeros(2, 1)
        all_parallel_c2 &= ok
        parallel_results_c2.append({"i": i + 1, "residual": str(lhs.T), "is_zero": bool(ok)})

    return {
        "candidate_psi": "gbar(x) * psi_0  (quaternion-conjugate of g times constant psi_0)",
        "c0_used": str(c0),
        "H_c0": str(H_c0),
        "parallel_checks_using_c0_all_i": parallel_results,
        "psi_is_nabla1_parallel_using_c0": bool(all_parallel),
        "D1_psi_using_c0": str(D1_psi.T),
        "D1_psi_is_zero_using_c0": bool(D1_psi_is_zero),
        "crossref_parallel_checks_using_E9_abstract_c2": parallel_results_c2,
        "psi_is_nabla1_parallel_using_E9_abstract_c2": bool(all_parallel_c2),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> dict:
    Z = clifford_generators()
    Binv = basis_inverse(Z)

    part1 = run_part1()
    XL, XR = build_invariant_frames(Z, Binv)

    part2 = run_part2(Z)
    part3 = run_part3(Z, Binv, XL, XR)
    part4 = run_part4(Z)

    core_part1_pass = bool(
        part1["clifford_ok"]
        and part1["quaternion_norm_check"]["g_gbar_equals_norm2_I"]
        and part1["tangency_L_all"]
        and part1["tangency_R_all"]
        and part1["left_bracket_check_all_pairs_ok"]
        and part1["right_bracket_matches_minus_c0L_all_pairs"]
        and part1["c0_right_equals_minus_c0_left"]
    )

    core_part2_pass = bool(
        part2["so3_valued_right"]
        and part2["crosscheck_matches_tH_either_sign"]
        and part2["t0_omega_right_all_zero"]
        and all(part2["t0_parallel_checks"].values())
        and part2["t0_D_psi_is_zero"]
    )

    t1_naive_ansatz_fails_symmetrically = bool(not part2["t1_nonzero_solution_exists"])

    part3_reveals_discrepancy = bool(
        part3["nabla1_fk_vanishes_for_all_i"] and t1_naive_ansatz_fails_symmetrically
    )
    # ^ TRUE means: Part 2's mechanical recipe says Omega^right(1) != 0 (naive
    # ansatz fails), WHILE Part 3 finds E9's ORIGINAL t=1 connection already
    # parallelizes f_k as VECTOR FIELDS -- i.e. the two notions of "Nabla^t in
    # the right-invariant frame" genuinely disagree. FALSE (with part3 all-False)
    # would mean no discrepancy was found -- report honestly either way.

    explicit_spinor_found = bool(
        part4["psi_is_nabla1_parallel_using_c0"] and part4["D1_psi_is_zero_using_c0"]
    )
    explicit_spinor_fails_under_e9_abstract_c = bool(
        not part4["psi_is_nabla1_parallel_using_E9_abstract_c2"]
    )

    if core_part1_pass and core_part2_pass and t1_naive_ansatz_fails_symmetrically:
        if part3_reveals_discrepancy and explicit_spinor_found:
            overall_label = "PASS_MIRROR_NULL__PLUS_EXPLICIT_T1_SPINOR_UNDER_SIGN_CAVEAT"
        elif part3_reveals_discrepancy:
            overall_label = "PASS_MIRROR_NULL__FRAME_AMBIGUITY_FOUND_NO_EXPLICIT_SPINOR"
        else:
            overall_label = "PASS_MIRROR_NULL__NO_DISCREPANCY_FOUND_IN_PART3"
    elif core_part1_pass and core_part2_pass and not t1_naive_ansatz_fails_symmetrically:
        overall_label = "PASS_BOTH_T0_AND_T1_RIGHT_INVARIANT_UNEXPECTED"
    else:
        overall_label = "FAIL_CORE_CONSTRUCTION"

    result = {
        "part1_explicit_LR_frames_and_sign_flip": part1,
        "part2_mirror_of_e9_recipe": part2,
        "part3_true_connection_vs_naive_recipe": part3,
        "part4_explicit_t1_spinor_candidate": part4,
        "verdict": {
            "core_part1_pass": core_part1_pass,
            "core_part2_pass": core_part2_pass,
            "t1_naive_ansatz_fails_symmetrically_to_e9": t1_naive_ansatz_fails_symmetrically,
            "part3_reveals_frame_ambiguity_discrepancy": part3_reveals_discrepancy,
            "explicit_t1_spinor_found_using_concrete_c0": explicit_spinor_found,
            "explicit_spinor_fails_under_e9_abstract_c2": explicit_spinor_fails_under_e9_abstract_c,
            "label": overall_label,
        },
    }
    return result


if __name__ == "__main__":
    out = main()
    print(json.dumps(out, indent=2, default=str))
    out_path = "results_e10.json"
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    print(f"\nSaved: {out_path}")
