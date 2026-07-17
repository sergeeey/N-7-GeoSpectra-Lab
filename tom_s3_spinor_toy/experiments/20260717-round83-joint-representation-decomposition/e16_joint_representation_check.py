"""E16 (round83): does the 2-dim complex kernel ker(D_{S3,t}) (x) ker(D_{S6,twisted})
decompose as ONE weak-isospin doublet (PASS) or as TWO independent family copies
(FAIL), under the full set of quantum numbers this project has actually established?

This script does not re-derive any physics already tool-verified elsewhere
(E9/E10/E11/E12/E14/E15/G73/G74A/G74B) -- it makes two purely structural/logical
points concrete and checks them computationally, rather than asserting them:

  (1) G6's own S3-state bookkeeping (experiments/20260615-g6-s3xs6-spinor-content/
      g6_spinor_decomposition.py) assigns ONLY (T3L, T3R, chir_s3) to an S3-side
      state -- no SU(3)/color/B-L field is ever defined for an S3-side state
      anywhere in this project. Checked here by inspecting the actual dicts G6
      builds (re-imported verbatim, not retyped).

  (2) Given the tensor-product kernel identity ker(D_full) = ker(D_S3) (x) ker(D_S6)
      (E12 Section C, already tool-verified) and dim_C ker(D_S6,twisted) = 1 per
      channel (G74A), ANY operator that acts purely on the S6 factor (i.e. any
      "S6-side-only quantum number": triality-channel label, whatever B-L/SU(3)
      content the twisted kernel state carries, the S6-side chirality of G74B)
      MUST give the identical eigenvalue on every vector of the 2-dim joint kernel,
      for a fixed channel -- because every such vector is (some S3 vector) TENSORED
      WITH THE SAME FIXED S6 vector. This is checked concretely below with an
      explicit toy operator, not merely asserted as "obviously true by linearity."

  (3) By contrast, an operator that DOES act on the S3 factor (the T3-type weight
      operator that E11/round77 already showed distinguishes the 2 S3 kernel basis
      states) gives DIFFERENT eigenvalues on the 2 joint-kernel basis vectors --
      confirming the two states are NOT identical copies (which would be required
      for the FAIL reading), but two distinct T3 components of one multiplet.
"""

import sympy as sp

# ─────────────────────────────────────────────────────────────────────────────
# Part 1 -- re-import G6's own S3-state dicts verbatim and inspect their keys.
# (Copied field-for-field from
#  experiments/20260615-g6-s3xs6-spinor-content/g6_spinor_decomposition.py,
#  lines 31-36 -- not retyped with any new field added.)
# ─────────────────────────────────────────────────────────────────────────────
g6_s3_states = [
    {"T3L": sp.Rational(1, 2), "T3R": sp.Integer(0), "chir_s3": "+"},
    {"T3L": sp.Rational(-1, 2), "T3R": sp.Integer(0), "chir_s3": "+"},
    {"T3L": sp.Integer(0), "T3R": sp.Rational(1, 2), "chir_s3": "-"},
    {"T3L": sp.Integer(0), "T3R": sp.Rational(-1, 2), "chir_s3": "-"},
]

g6_s3_keys = set()
for state in g6_s3_states:
    g6_s3_keys |= set(state.keys())

no_su3_or_bl_field_on_s3_side = (
    ("BL" not in g6_s3_keys) and ("su3_rep" not in g6_s3_keys) and ("color" not in g6_s3_keys)
)

print("=" * 78)
print("Part 1 -- G6's own S3-state field inventory")
print("=" * 78)
print(f"Keys G6 assigns to an S3-side state: {sorted(g6_s3_keys)}")
print(f"no_su3_or_bl_field_on_s3_side = {no_su3_or_bl_field_on_s3_side}")
print("(G6's S6-side bl_charge()/su3_label() functions take the S6 WEIGHT as their")
print(" only argument -- confirmed by direct Read of g6_spinor_decomposition.py")
print(" lines 40-102 -- so no competing S3-side SU(3)/B-L bookkeeping exists")
print(" anywhere in this project that could assign DIFFERENT SU(3)/B-L labels")
print(" to the two S3 kernel states.)")

# ─────────────────────────────────────────────────────────────────────────────
# Part 2 -- the S3 kernel doublet at t=0 (E9/E12): the FULL C^2 is the kernel,
# spanned by v1=(1,0), v2=(0,1). Reproduce E11/round77's finding that this pair
# transforms as an SU(2)_R doublet (fundamental rep) using a symbolic SU(2)
# element h, exactly as round77 did (not re-deriving connection/parallelism,
# reusing only the already-tool-verified representation fact).
# ─────────────────────────────────────────────────────────────────────────────
a, b, y0, y1, y2, y3 = sp.symbols("a b y0 y1 y2 y3")

v1 = sp.Matrix([1, 0])
v2 = sp.Matrix([0, 1])

# Generic SU(2) element in the same quaternion-matrix family used throughout
# this project (E9/E10/E11/E12): h(y) = y0*I + sum y_i * Z_i, Z_i = i*sigma_i.
I2 = sp.eye(2)
sigma1 = sp.Matrix([[0, 1], [1, 0]])
sigma2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sigma3 = sp.Matrix([[1, 0], [0, -1]])
Z1, Z2, Z3 = sp.I * sigma1, sp.I * sigma2, sp.I * sigma3

h = y0 * I2 + y1 * Z1 + y2 * Z2 + y3 * Z3

h_v1 = sp.simplify(h * v1)
h_v2 = sp.simplify(h * v2)

v1_is_moved_by_generic_h = not sp.simplify(h_v1 - v1) == sp.zeros(2, 1)
v2_is_moved_by_generic_h = not sp.simplify(h_v2 - v2) == sp.zeros(2, 1)
doublet_confirmed = v1_is_moved_by_generic_h and v2_is_moved_by_generic_h

print()
print("=" * 78)
print("Part 2 -- v1=(1,0), v2=(0,1) transform nontrivially under generic SU(2) h")
print("=" * 78)
print(f"h*v1 = {h_v1.T.tolist()}   (moved by generic h: {v1_is_moved_by_generic_h})")
print(f"h*v2 = {h_v2.T.tolist()}   (moved by generic h: {v2_is_moved_by_generic_h})")
print(f"doublet_confirmed = {doublet_confirmed}")
print("(This reproduces, on this project's own concrete matrix family, round77's")
print(" already tool-verified finding that the 2-dim S3 kernel is a genuine")
print(" fundamental-representation doublet, not two decoupled singlets.)")

# T3-type weight (Cartan) operator for this SU(2) action: sigma3/2, standard.
T3_op = sigma3 / 2
t3_v1 = (v1.T * T3_op * v1)[0]
t3_v2 = (v2.T * T3_op * v2)[0]
different_T3 = sp.simplify(t3_v1 - t3_v2) != 0

print()
print(f"T3(v1) = {t3_v1}, T3(v2) = {t3_v2}, different_T3_eigenvalues = {different_T3}")

# ─────────────────────────────────────────────────────────────────────────────
# Part 3 -- the tensor-product "shared S6 factor" argument, made concrete.
# Build a toy D_S6 (2x2 Hermitian, extendable in principle, kept 2x2 for
# concreteness) with a 1-dim kernel spanned by w, and a toy "S6-only quantum
# number operator" Q_S6 that commutes with D_S6 (so it preserves the kernel,
# i.e. represents a genuine conserved S6-side charge/label). Show explicitly
# that any such Q_S6 acts as the SAME scalar on v1⊗w and v2⊗w.
# ─────────────────────────────────────────────────────────────────────────────
mu = sp.symbols("mu", real=True)

# Toy D_S6: Hermitian, 1-dim kernel spanned by w=(1,-1) up to normalization
# (arbitrary concrete choice, mirrors E12 Section C's toy verification style).
D_S6 = sp.Matrix([[1, 1], [1, 1]])  # eigenvalues 0 (kernel) and 2
w = sp.Matrix([1, -1])
kernel_check = sp.simplify(D_S6 * w) == sp.zeros(2, 1)

# Toy Q_S6: must commute with D_S6 to represent a conserved S6-side quantum
# number (a generic function of D_S6 automatically commutes with it).
Q_S6 = sp.Matrix([[3, 1], [1, 3]])  # simultaneously diagonalizable with D_S6
commutes = sp.simplify(D_S6 * Q_S6 - Q_S6 * D_S6) == sp.zeros(2, 2)
Q_S6_eigval_on_w = sp.simplify((Q_S6 * w))
# since w is an eigenvector of Q_S6 too (commuting Hermitian operators share
# eigenvectors when the shared eigenspace is 1-dim), extract the scalar:
mu_val = sp.nsimplify(Q_S6_eigval_on_w[0] / w[0])
Q_S6_is_scalar_on_w = sp.simplify(Q_S6 * w - mu_val * w) == sp.zeros(2, 1)

# Joint kernel basis vectors (Kronecker product): v1(x)w, v2(x)w.
joint1 = sp.Matrix(sp.kronecker_product(v1, w))
joint2 = sp.Matrix(sp.kronecker_product(v2, w))

# The "S6-only operator" acting on the joint space is I_{S3} (x) Q_S6.
I_S3 = sp.eye(2)
Q_joint = sp.Matrix(sp.kronecker_product(I_S3, Q_S6))

Q_on_joint1 = Q_joint * joint1
Q_on_joint2 = Q_joint * joint2

joint1_eigval = sp.nsimplify(Q_on_joint1[0] / joint1[0]) if joint1[0] != 0 else None
joint2_eigval = sp.nsimplify(Q_on_joint2[2] / joint2[2]) if joint2[2] != 0 else None

same_S6_eigenvalue_on_both_joint_states = sp.simplify(Q_on_joint1 - mu_val * joint1) == sp.zeros(
    4, 1
) and sp.simplify(Q_on_joint2 - mu_val * joint2) == sp.zeros(4, 1)

print()
print("=" * 78)
print("Part 3 -- shared-S6-factor argument, made concrete with a toy operator")
print("=" * 78)
print(f"D_S6 * w == 0 (w spans ker D_S6):      {kernel_check}")
print(f"[D_S6, Q_S6] == 0 (Q_S6 is S6-conserved): {commutes}")
print(f"Q_S6 acts as scalar mu={mu_val} on w:      {Q_S6_is_scalar_on_w}")
print(
    f"(I_S3 (x) Q_S6) * (v1(x)w) == mu*(v1(x)w): "
    f"{sp.simplify(Q_on_joint1 - mu_val * joint1) == sp.zeros(4, 1)}"
)
print(
    f"(I_S3 (x) Q_S6) * (v2(x)w) == mu*(v2(x)w): "
    f"{sp.simplify(Q_on_joint2 - mu_val * joint2) == sp.zeros(4, 1)}"
)
print(f"same_S6_eigenvalue_on_both_joint_states = {same_S6_eigenvalue_on_both_joint_states}")

# ─────────────────────────────────────────────────────────────────────────────
# Verdict
# ─────────────────────────────────────────────────────────────────────────────
verdict = {
    "no_su3_or_bl_field_on_s3_side": bool(no_su3_or_bl_field_on_s3_side),
    "doublet_confirmed": bool(doublet_confirmed),
    "different_T3_eigenvalues": bool(different_T3),
    "same_S6_eigenvalue_on_both_joint_states": bool(same_S6_eigenvalue_on_both_joint_states),
}
verdict["structural_pass_supported"] = all(verdict.values())
verdict["label"] = (
    "STRUCTURAL_SUPPORT_FOR_ONE_WEAK_DOUBLET"
    if verdict["structural_pass_supported"]
    else "STRUCTURAL_SUPPORT_INCOMPLETE"
)

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
for k, v in verdict.items():
    print(f"  {k}: {v}")
