"""Round113: reconciles the two t-parameter conventions flagged as a risk
in PARENT_ACTION_GATE.md field F3.

Convention A (round67/e2_s3_torsion_deformation.py, preprint.tex's KT-8
escape route): states the connection as Nabla^t_X Y = t*[X,Y], torsion
T^t=(2t-1)*[X,Y], vanishing at t=1/2.

Convention B (round99/round111): curvature R^t(X,Y)Z = t*(t-1)*[[X,Y],Z].

Both use the IDENTICAL Cl(3) generator convention (Z_i = i*sigma_i). This
script computes the standard curvature tensor DIRECTLY from convention A's
own stated connection formula and checks it against convention B's formula,
term by term, on all independent basis triples -- not via the Jacobi-
identity hand-derivation alone (kept here as a documented cross-check, not
the sole evidence).
"""

import itertools

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
    return sp.expand(A * B - B * A)


print("=" * 92)
print("PART 0 -- confirm {Z_i,Z_j}=-2delta_ij (same convention as round67/round99/round111)")
print("=" * 92)
clifford_ok = True
for i in range(3):
    for j in range(3):
        anticomm = sp.simplify(Z[i] * Z[j] + Z[j] * Z[i])
        expected = -2 * sp.eye(2) if i == j else sp.zeros(2, 2)
        ok = bool(sp.simplify(anticomm - expected) == sp.zeros(2, 2))
        clifford_ok = clifford_ok and ok
print(f"  Clifford relations confirmed (same generators as round67/99/111)? {clifford_ok}")
print()

print("=" * 92)
print("PART 1 -- Convention A's connection: Nabla^t_X Y := t*[X,Y] (round67's own stated formula)")
print("Standard curvature definition: R^t(X,Y)Z := Nabla^t_X Nabla^t_Y Z")
print("                                          - Nabla^t_Y Nabla^t_X Z")
print("                                          - Nabla^t_{[X,Y]} Z")
print("applied DIRECTLY to convention A's connection -- not assumed equal to convention B.")
print("=" * 92)


def nabla_t(X, Y, tt):
    """Nabla^t_X Y := t*[X,Y], round67's own stated formula, extended
    bilinearly (X,Y any Lie-algebra elements, not just basis vectors)."""
    return tt * bracket(X, Y)


def curvature_from_connection_A(X, Y, Zarg, tt):
    """R^t(X,Y)Z computed DIRECTLY from convention A's own nabla_t,
    via the textbook curvature definition -- no shortcut formula assumed."""
    term1 = nabla_t(X, nabla_t(Y, Zarg, tt), tt)
    term2 = nabla_t(Y, nabla_t(X, Zarg, tt), tt)
    term3 = nabla_t(bracket(X, Y), Zarg, tt)
    return sp.expand(term1 - term2 - term3)


def curvature_convention_B(X, Y, Zarg, tt):
    """Round99/round111's own stated formula, R^t(X,Y)Z = t*(t-1)*[[X,Y],Z]."""
    return sp.expand(tt * (tt - 1) * bracket(bracket(X, Y), Zarg))


print("  Checking R^t_A(Z_i,Z_j)Z_k == R^t_B(Z_i,Z_j)Z_k for all independent (i,j,k) triples:")
all_match = True
mismatches = []
checked = 0
for i, j, k in itertools.product(range(3), repeat=3):
    R_A = curvature_from_connection_A(Z[i], Z[j], Z[k], t)
    R_B = curvature_convention_B(Z[i], Z[j], Z[k], t)
    diff = sp.expand(R_A - R_B)
    match = bool(sp.simplify(diff) == sp.zeros(2, 2))
    checked += 1
    if not match:
        all_match = False
        mismatches.append((i + 1, j + 1, k + 1, str(diff)))

print(f"  Triples checked: {checked} (all 27 ordered triples (i,j,k) in {{1,2,3}}^3)")
print(f"  ALL match (Convention A's curvature == Convention B's formula)? {all_match}")
if mismatches:
    print(f"  Mismatches found: {mismatches}")
print()

print("=" * 92)
print("PART 2 -- Torsion check: does Convention A's own stated torsion T^t=(2t-1)*[X,Y]")
print("match the standard torsion definition applied to the SAME nabla_t?")
print("T^t(X,Y) := Nabla^t_X Y - Nabla^t_Y X - [X,Y]")
print("=" * 92)


def torsion_from_connection_A(X, Y, tt):
    return sp.expand(nabla_t(X, Y, tt) - nabla_t(Y, X, tt) - bracket(X, Y))


def torsion_convention_stated(X, Y, tt):
    return sp.expand((2 * tt - 1) * bracket(X, Y))


torsion_all_match = True
for i, j in itertools.product(range(3), repeat=2):
    T_from_def = torsion_from_connection_A(Z[i], Z[j], t)
    T_stated = torsion_convention_stated(Z[i], Z[j], t)
    match = bool(sp.simplify(sp.expand(T_from_def - T_stated)) == sp.zeros(2, 2))
    torsion_all_match = torsion_all_match and match
print(
    f"  Torsion T^t=(2t-1)*[X,Y] matches the standard definition applied to Nabla^t=t*[X,Y]? {torsion_all_match}"
)
print()

print("=" * 92)
print("PART 3 -- Cross-check against Jacobi-identity hand-derivation")
print("(documented reasoning, not the sole evidence): R^t=t^2*[X,[Y,Z]]-t^2*[Y,[X,Z]]-t*[[X,Y],Z]")
print("Jacobi identity: [X,[Y,Z]]-[Y,[X,Z]] = [[X,Y],Z]  =>  R^t = t*(t-1)*[[X,Y],Z]")
print("=" * 92)
jacobi_ok = True
for i, j, k in itertools.product(range(3), repeat=3):
    lhs = sp.expand(bracket(Z[i], bracket(Z[j], Z[k])) - bracket(Z[j], bracket(Z[i], Z[k])))
    rhs = bracket(bracket(Z[i], Z[j]), Z[k])
    jacobi_ok = jacobi_ok and bool(sp.simplify(sp.expand(lhs - rhs)) == sp.zeros(2, 2))
print(f"  Jacobi identity confirmed on all 27 triples (independent check)? {jacobi_ok}")
print()

verdict = {
    "clifford_relations_confirmed": clifford_ok,
    "curvature_conventions_A_and_B_agree_exactly": all_match,
    "torsion_definition_matches_stated_formula": torsion_all_match,
    "jacobi_identity_independent_check": jacobi_ok,
    "triples_checked": checked,
}
print("=" * 92)
print("VERDICT")
print("=" * 92)
for k, v in verdict.items():
    print(f"  {k}: {v}")

print()
if all_match and torsion_all_match:
    label = "RESOLVED__CONVENTIONS_A_AND_B_ARE_THE_SAME_CONNECTION_FAMILY_SAME_T__F3_FALSE_ALARM"
elif not all_match:
    label = "CONFIRMED_MISMATCH__F3_RISK_REAL__RECONCILIATION_MAP_REQUIRED"
else:
    label = "PARTIAL__CURVATURE_MATCHES_BUT_TORSION_DEFINITION_DIVERGES__NEEDS_FOLLOWUP"
print(f"  label = '{label}'")
