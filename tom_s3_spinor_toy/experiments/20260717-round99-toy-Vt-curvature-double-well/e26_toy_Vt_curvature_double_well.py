"""E26 (round99, B4): explicit curvature R^t of the Cartan-Schouten family
on su(2), and a toy curvature-penalty potential V(t) proportional to
||R^t||^2 -- checking whether it has the double-well shape (minima at
t=0,1, matching this project's own established "flat at t=0,1" fact).

Generators reused unchanged from
experiments/20260717-round67-e2-s3-torsion-deformation/
e2_s3_torsion_deformation.py:93-107 (Z_i = i*sigma_i).
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


print("=" * 92)
print("PART 0 -- Generators (reused unchanged, round67 e2_s3_torsion_deformation.py)")
print("=" * 92)
Z = clifford_generators()
for i, Zi in enumerate(Z, start=1):
    print(f"  Z{i} =")
    sp.pprint(Zi)
print()


def bracket(A, B):
    return sp.simplify(A * B - B * A)


print("=" * 92)
print("PART 1 -- [Zi,Zj] structure constants (tool-verified, not assumed)")
print("=" * 92)
comm = {}
for i in range(3):
    for j in range(3):
        comm[(i, j)] = bracket(Z[i], Z[j])
# check [Z1,Z2] = -2*Z3 (cyclic), matching c0=-2 (round76)
check_12 = sp.simplify(comm[(0, 1)] - (-2 * Z[2]))
check_23 = sp.simplify(comm[(1, 2)] - (-2 * Z[0]))
check_31 = sp.simplify(comm[(2, 0)] - (-2 * Z[1]))
c0_minus2_confirmed = (
    check_12 == sp.zeros(2, 2) and check_23 == sp.zeros(2, 2) and check_31 == sp.zeros(2, 2)
)
print(f"  [Z1,Z2]=-2*Z3, [Z2,Z3]=-2*Z1, [Z3,Z1]=-2*Z2 (c0=-2 convention)? {c0_minus2_confirmed}")
print()

print("=" * 92)
print("PART 2 -- Curvature R^t(Zi,Zj)Zk, direct computation vs t(t-1)[[Zi,Zj],Zk]")
print("=" * 92)


def nabla_t(X, Y, tt):
    """nabla^t_X Y = tt*[X,Y] for left-invariant X,Y (Cartan-Schouten family)."""
    return tt * bracket(X, Y)


all_match = True
sample_reports = []
for i in range(3):
    for j in range(3):
        for k in range(3):
            Zi, Zj, Zk = Z[i], Z[j], Z[k]
            # R^t(X,Y)Z = nabla^t_X(nabla^t_Y Z) - nabla^t_Y(nabla^t_X Z) - nabla^t_[X,Y] Z
            # nabla^t_Y Z = t*[Y,Z] is itself a matrix (Lie-algebra element);
            # nabla^t_X(t*[Y,Z]) = t*[X, t*[Y,Z]] = t^2*[X,[Y,Z]]
            term1 = t * bracket(Zi, t * bracket(Zj, Zk))
            term2 = t * bracket(Zj, t * bracket(Zi, Zk))
            bracket_ij = bracket(Zi, Zj)
            term3 = t * bracket(bracket_ij, Zk)
            R_direct = sp.expand(term1 - term2 - term3)
            R_predicted = sp.expand(t * (t - 1) * bracket_ij * Zk - t * (t - 1) * Zk * bracket_ij)
            # R_predicted should equal t(t-1)*[[Zi,Zj],Zk] = t(t-1)*bracket(bracket_ij, Zk)
            R_predicted = sp.expand(t * (t - 1) * bracket(bracket_ij, Zk))
            diff = sp.simplify(R_direct - R_predicted)
            matches = diff == sp.zeros(2, 2)
            all_match = all_match and matches
            if (i, j, k) in [(0, 1, 2), (0, 1, 0), (1, 2, 0)]:
                sample_reports.append((i + 1, j + 1, k + 1, matches))

print("  R^t(Zi,Zj)Zk == t(t-1)*[[Zi,Zj],Zk] for ALL 27 (i,j,k) triples?", all_match)
print("  Sample checks (i,j,k,matches):", sample_reports)
print()

print("=" * 92)
print("PART 3 -- Flatness check at t=0,1 (must match project's established fact)")
print("=" * 92)
# NOTE: (i,j,k)=(1,2,3) [i.e. R^t(Z1,Z2)Z3] is a DEGENERATE choice here --
# [Z1,Z2]=-2*Z3 is already proportional to Z3, so [[Z1,Z2],Z3]=[-2*Z3,Z3]=0
# identically (self-commutator), for EVERY t, not just t=0,1. This is a
# genuine feature of su(2)'s totally-antisymmetric structure constants (R(X,Y)
# vanishes on the vector "dual" to the X-Y plane in 3 dimensions), not a bug --
# but it is the WRONG representative for illustrating "curved at t=1/2", since
# it is trivially zero everywhere. The correct, non-degenerate choice is
# (i,j,k)=(1,2,1) [R^t(Z1,Z2)Z1], which is the sectional-curvature-type
# component (Z appearing among X,Y themselves), verified explicitly below.
R_121_formula = t * (t - 1) * bracket(bracket(Z[0], Z[1]), Z[0])
R_at_0 = R_121_formula.subs(t, 0)
R_at_1 = R_121_formula.subs(t, 1)
R_at_half = sp.simplify(R_121_formula.subs(t, sp.Rational(1, 2)))
flat_at_0 = sp.simplify(R_at_0) == sp.zeros(2, 2)
flat_at_1 = sp.simplify(R_at_1) == sp.zeros(2, 2)
nonzero_at_half = sp.simplify(R_at_half) != sp.zeros(2, 2)
print(f"  R^t(Z1,Z2)Z1 at t=0 is zero (flat)? {flat_at_0}")
print(f"  R^t(Z1,Z2)Z1 at t=1 is zero (flat)? {flat_at_1}")
print(f"  R^t(Z1,Z2)Z1 at t=1/2 is nonzero (Levi-Civita, curved)? {nonzero_at_half}")
print("  R^t(Z1,Z2)Z1 at t=1/2 explicit matrix:")
sp.pprint(R_at_half)
print()

print("=" * 92)
print("PART 4 -- Toy curvature-penalty potential V(t) ~ ||R^t||^2 ~ [t(t-1)]^2")
print("=" * 92)
# Since R^t(Zi,Zj)Zk = t(t-1)*[[Zi,Zj],Zk] exactly (Part 2, verified for all 27
# triples), the SQUARED FROBENIUS NORM of the genuinely nonzero R^t(Z1,Z2)Z1
# component is computed directly here (not merely asserted symbolically):
# ||R^t(Z1,Z2)Z1)||^2 = [t(t-1)]^2 * ||[[Z1,Z2],Z1]||^2, and
# ||[[Z1,Z2],Z1]||^2 is a fixed, t-independent nonzero matrix norm.
bracket_121_fixed = bracket(bracket(Z[0], Z[1]), Z[0])  # t-independent part
norm_sq_fixed = sp.simplify(sp.trace(bracket_121_fixed * bracket_121_fixed.conjugate().T))
print(f"  ||[[Z1,Z2],Z1]||^2 (Frobenius, t-independent) = {norm_sq_fixed}")
V = (t * (t - 1)) ** 2 * norm_sq_fixed  # genuine curvature-norm-squared, not a bare guess
V_shape = (t * (t - 1)) ** 2  # normalized shape, proportionality constant factored out
V0 = V_shape.subs(t, 0)
V1 = V_shape.subs(t, 1)
Vhalf = V_shape.subs(t, sp.Rational(1, 2))
dV = sp.diff(V, t)
critical_points = sp.solve(sp.Eq(dV, 0), t)
print("  V(t) = [t(t-1)]^2  (proportionality constant = ||[[Z1,Z2],Z3]||^2, t-independent)")
print(f"  V(0) = {V0}, V(1) = {V1}, V(1/2) = {Vhalf}")
print(f"  V'(t) = {sp.expand(dV)}, critical points: {sorted(critical_points)}")
is_double_well = (V0 == 0) and (V1 == 0) and (Vhalf > 0)
d2V_at_0 = sp.diff(V, t, 2).subs(t, 0)
d2V_at_1 = sp.diff(V, t, 2).subs(t, 1)
minima_confirmed_by_second_derivative = (d2V_at_0 > 0) and (d2V_at_1 > 0)
print(f"  V''(0) = {d2V_at_0}, V''(1) = {d2V_at_1}  (>0 confirms local minima, not just V=0)")
print(f"  Double-well shape (V=0 minima at t=0,1, positive barrier at t=1/2)? {is_double_well}")
print()

verdict = {
    "c0_minus2_convention_confirmed": c0_minus2_confirmed,
    "curvature_formula_R_t_equals_t_t-1_confirmed_all_27_triples": all_match,
    "flat_at_t0": flat_at_0,
    "flat_at_t1": flat_at_1,
    "curved_at_t_half": nonzero_at_half,
    "V0": int(V0),
    "V1": int(V1),
    "Vhalf": str(Vhalf),
    "critical_points": [str(c) for c in sorted(critical_points, key=str)],
    "double_well_shape_confirmed": bool(is_double_well),
    "minima_confirmed_by_second_derivative": bool(minima_confirmed_by_second_derivative),
}
print("=" * 92)
print("VERDICT INPUTS")
print("=" * 92)
for k, v in verdict.items():
    print(f"  {k}: {v}")

label = (
    "CONFIRMED__DOUBLE_WELL_PLAUSIBLE_FROM_CLASSICAL_CURVATURE"
    if (is_double_well and all_match and flat_at_0 and flat_at_1)
    else "REFUTED_OR_INCONCLUSIVE"
)
print()
print(f"label = '{label}'")
