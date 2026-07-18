"""E34 (round111): actual scalar curvature Scal(t) of the Cartan-Schouten
family (not a curvature-norm toy, per Codex/round105's item 6), using
round99's own established R^t(X,Y)Z=t(t-1)[[X,Y],Z], cross-checked
against the standard bi-invariant-metric Levi-Civita Ricci formula at
t=1/2.
"""

import sympy as sp

t = sp.symbols("t", real=True)


def pauli_matrices():
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    return [sx, sy, sz]


def clifford_generators():
    return [sp.I * s for s in pauli_matrices()]


Z = clifford_generators()


def bracket(A, B):
    return sp.simplify(A * B - B * A)


print("=" * 92)
print("PART 0 -- Metric: <X,Y> := -1/2 Tr(XY); verify {Z_i} is orthonormal")
print("=" * 92)


def inner(X, Y):
    return sp.simplify(-sp.Rational(1, 2) * sp.trace(X * Y))


metric = sp.Matrix(3, 3, lambda i, j: inner(Z[i], Z[j]))
print("  <Z_i,Z_j> matrix =")
sp.pprint(metric)
metric_is_identity = metric == sp.eye(3)
print(f"  {{Z_i}} orthonormal (metric == I)? {metric_is_identity}")
print()

print("=" * 92)
print("PART 1 -- Ricci^t(Z_a,Z_b) := sum_c <R^t(Z_c,Z_a)Z_b, Z_c>, using")
print("R^t(X,Y)Z = t(t-1)*[[X,Y],Z]  (round99, re-verified there)")
print("=" * 92)


def R_t(X, Y, Zarg):
    return sp.expand(t * (t - 1) * bracket(bracket(X, Y), Zarg))


Ricci_t = sp.zeros(3, 3)
for a in range(3):
    for b in range(3):
        val = sp.Integer(0)
        for c in range(3):
            val += inner(R_t(Z[c], Z[a], Z[b]), Z[c])
        Ricci_t[a, b] = sp.simplify(val)
print("  Ricci^t(Z_a,Z_b) matrix =")
sp.pprint(Ricci_t)
ricci_is_diagonal_multiple_of_metric = sp.simplify(Ricci_t - Ricci_t[0, 0] * sp.eye(3)) == sp.zeros(
    3, 3
)
print(
    f"  Ricci^t proportional to the metric (Einstein, as expected by symmetry)? "
    f"{ricci_is_diagonal_multiple_of_metric}"
)
print()

Scal_t = sp.simplify(sp.trace(Ricci_t))
print(f"  Scal(t) = trace(Ricci^t) = {Scal_t}")
print()

print("=" * 92)
print("PART 2 -- MANDATORY cross-check at t=1/2 (Levi-Civita) via the STANDARD,")
print("independently-sourced bi-invariant-metric formula: Ric_LC(X,X) = -(1/4)*B(X,X),")
print("B(X,Y):=Tr(ad_X * ad_Y) the Killing form (textbook fact, not derived from R^t)")
print("=" * 92)


def ad_matrix(X):
    """3x3 matrix of ad_X: Z_b -> [X,Z_b], expressed in the {Z_i} basis."""
    M = sp.zeros(3, 3)
    for b in range(3):
        comm = bracket(X, Z[b])
        for a in range(3):
            M[a, b] = inner(Z[a], comm)  # coefficient of Z_a in [X,Z_b]
    return M


ad = [ad_matrix(Z[i]) for i in range(3)]
Killing = sp.zeros(3, 3)
for a in range(3):
    for b in range(3):
        Killing[a, b] = sp.simplify(sp.trace(ad[a] * ad[b]))
print("  Killing form B(Z_a,Z_b) matrix =")
sp.pprint(Killing)
Ric_LC = sp.simplify(-sp.Rational(1, 4) * Killing)
Scal_LC = sp.simplify(sp.trace(Ric_LC))
print("  Ric_LC(Z_a,Z_b) = -1/4 * Killing =")
sp.pprint(Ric_LC)
print(f"  Scal_LC (independent route) = {Scal_LC}")
print()

Scal_at_half = sp.simplify(Scal_t.subs(t, sp.Rational(1, 2)))
print(f"  Scal(t) [general formula] at t=1/2 = {Scal_at_half}")
cross_check_ok = sp.simplify(Scal_at_half - Scal_LC) == 0
print(f"  Two independent routes AGREE at t=1/2? {cross_check_ok}")
print()

print("=" * 92)
print("PART 3 -- Shape of Scal(t): is it double-well (minima at t=0,1) or a single")
print("dip/peak at t=1/2 (opposite of round99's hoped-for shape)?")
print("=" * 92)
Scal_0 = sp.simplify(Scal_t.subs(t, 0))
Scal_1 = sp.simplify(Scal_t.subs(t, 1))
dScal = sp.expand(sp.diff(Scal_t, t))
critical_points = sp.solve(sp.Eq(dScal, 0), t)
d2Scal = sp.diff(Scal_t, t, 2)
print(f"  Scal(0) = {Scal_0}, Scal(1) = {Scal_1}, Scal(1/2) = {Scal_at_half}")
print(f"  dScal/dt = {dScal}")
print(f"  critical points: {critical_points}")
print(f"  d2Scal/dt^2 (constant, since Scal is quadratic in t) = {sp.simplify(d2Scal)}")
is_extremum_at_half = sp.Rational(1, 2) in critical_points
print(f"  t=1/2 is the (unique) critical point? {is_extremum_at_half}")
print()

verdict = {
    "metric_orthonormal_confirmed": bool(metric_is_identity),
    "Ricci_t_proportional_to_metric": bool(ricci_is_diagonal_multiple_of_metric),
    "Scal_t_formula": str(Scal_t),
    "crosscheck_two_independent_routes_agree_at_t_half": bool(cross_check_ok),
    "Scal_0": int(Scal_0),
    "Scal_1": int(Scal_1),
    "Scal_half": str(Scal_at_half),
    "unique_critical_point_is_t_half": bool(is_extremum_at_half),
}
print("=" * 92)
print("VERDICT")
print("=" * 92)
for k, v in verdict.items():
    print(f"  {k}: {v}")

if not cross_check_ok:
    label = "BLOCKED__CROSSCHECK_FAILED"
elif Scal_0 == 0 and Scal_1 == 0 and is_extremum_at_half:
    label = "OPPOSITE_SHAPE__SCAL_EXTREMIZED_AT_T_HALF_NOT_AT_ENDPOINTS__ROUND99_HOPE_REFUTED_AT_LEADING_ORDER"
else:
    label = "UNEXPECTED_SHAPE__NEEDS_FOLLOWUP"
print(f"  label = '{label}'")
