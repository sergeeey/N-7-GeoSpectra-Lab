"""E30 (round107): does the physical twisted-kernel vector k_vec span a
1-dim (SU(4) singlet) or larger (nontrivial multiplet) orbit under the
FULL 15-generator so(6)=su(4) action, Leibniz-lifted to the 64-dim
Sigma(x)Sigma fibre?

Reuses, by direct import, unchanged:
 - round59_route_b_consistency.py: DIM, N, fidx, herm, vec64_from_pairs,
   leibniz64, D_full
 - g2su3_explicit_clifford.py: SUBSETS, IDX
 - g15_hypercharge.py: BmL (for the permutation sanity-check only)
 - g10_s6_so6_gauge.py: so6_generators, complex_structure
 - g11_block_generators.py: lift_to_spinor

CRITICAL BASIS SUBTLETY (must be handled explicitly, unlike round94's
diagonal-only BmL case): so6_generators()+lift_to_spinor build matrices
in the SAME 3-qubit kron-index basis as G15's BmL (g11_block_generators.py's
G_so6 = kron(Pauli,Pauli,Pauli), the SAME convention family as G6/G15) --
NOT dolan-casimir's own SUBSETS/exterior-algebra basis used by
leibniz64/D_full/k_vec. round94 sidestepped this because BmL is DIAGONAL
(a pure degree formula, basis-bijection-invariant on the diagonal); the
so(6) generators are NOT diagonal (genuine raising/lowering operators),
so a full PERMUTATION MATRIX is constructed here and validated by
reproducing round94's own BmL result BEFORE trusting it on new
generators.
"""

import os
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.abspath(os.path.join(_HERE, "..", ".."))

_ROUND59 = os.path.join(_REPO, "experiments", "20260714-round59-trivial-rank-certification")
_DOLAN = os.path.join(_REPO, "experiments", "20260708-dolan-casimir-g2su3")
_G15 = os.path.join(_REPO, "experiments", "20260619-g15-hypercharge")
_G10 = os.path.join(_REPO, "experiments", "20260617-g10-s6-so6-gauge")
_G11 = os.path.join(_REPO, "experiments", "20260618-g11-block-generators")

for _p in (_ROUND59, _DOLAN, _G15, _G10, _G11):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from round59_route_b_consistency import (  # noqa: E402
    DIM,
    N,
    herm,
    vec64_from_pairs,
    leibniz64,
    D_full,
)
from g2su3_explicit_clifford import SUBSETS, IDX  # noqa: E402
from g15_hypercharge import BmL as BmL_g15  # noqa: E402
from g10_s6_so6_gauge import so6_generators  # noqa: E402
from g11_block_generators import lift_to_spinor  # noqa: E402
from g10b_su3_explicit import su3_generators  # noqa: E402
from round59_route_b_consistency import su3_matrix_on_sigma  # noqa: E402

sqrt = sp.sqrt
assert DIM == 8

print("=" * 92)
print("PART 0 -- Basis-conversion permutation matrix P (qubit-index -> SUBSETS-index)")
print("=" * 92)


def g15_index_to_subset(j):
    """Reused unchanged from round94 (e24_bl_twisted_kernel_eigenvalue.py:69-78)."""
    i1 = (j >> 2) & 1
    i2 = (j >> 1) & 1
    i3 = j & 1
    return tuple(k for k, bit in zip((1, 2, 3), (i1, i2, i3)) if bit)


P = sp.zeros(8, 8)
for j in range(8):
    subset = g15_index_to_subset(j)
    P[IDX[subset], j] = 1
print("  P (permutation, qubit-index j -> SUBSETS-index IDX[subset]) built.")
print(
    f"  P is a genuine permutation matrix (P*P.T == I)? {sp.simplify(P * P.T - sp.eye(8)) == sp.zeros(8, 8)}"
)
print()

print("=" * 92)
print("PART 1 -- SANITY CHECK: does permuting BmL_g15 via P reproduce round94's own")
print("BL_sigma (diagonal, degree-formula) construction? [must PASS before trusting P]")
print("=" * 92)


def bl_degree_formula(subset):
    k = len(subset)
    return sp.Rational(2 * k - 3, 3)


BL_sigma_round94 = sp.zeros(8, 8)
for s in SUBSETS:
    BL_sigma_round94[IDX[s], IDX[s]] = bl_degree_formula(s)

BmL_permuted = sp.simplify(P * BmL_g15 * P.T)
permutation_sanity_check_ok = sp.simplify(BmL_permuted - BL_sigma_round94) == sp.zeros(8, 8)
print(
    f"  P*BmL_g15*P.T == round94's BL_sigma (diagonal, SUBSETS-order)? {permutation_sanity_check_ok}"
)
if not permutation_sanity_check_ok:
    print(
        "  !!! PERMUTATION CONSTRUCTION FAILED SANITY CHECK -- STOPPING, do not trust Part 2+ !!!"
    )
print()

print("=" * 92)
print("PART 1b -- STRONGER SANITY CHECK (skeptic-recommended): off-diagonal cross-check")
print("using a NON-diagonal SU(3) generator, comparing P-permuted lift_to_spinor(...)")
print("against round59's OWN independently-built, SUBSETS-native su3_matrix_on_sigma(i)")
print("(built via su3_action, no kron/qubit convention involved -- independent route).")
print("=" * 92)
su3_vec_gens = su3_generators()
permuted_su3 = []
reference_su3 = []
per_generator_match = True
for i in range(8):
    su3_qubit = lift_to_spinor(su3_vec_gens[i])
    su3_permuted = sp.simplify(P * su3_qubit * P.T)
    su3_reference = su3_matrix_on_sigma(i + 1)  # su3_action is 1-indexed (AHL2023 convention)
    permuted_su3.append(su3_permuted)
    reference_su3.append(su3_reference)
    matches = sp.simplify(su3_permuted - su3_reference) == sp.zeros(8, 8)
    per_generator_match = per_generator_match and matches
    print(
        f"  SU(3) generator {i + 1}/8: P-permuted lift_to_spinor == su3_matrix_on_sigma? {matches}"
    )
print(f"  ALL 8 generators match ONE-TO-ONE (same labeling/normalization)? {per_generator_match}")


# Fallback: the two modules may use different generator LABELING/normalization
# conventions for su(3) (both valid bases of the same algebra) even if P is
# correct -- check the two 8-generator SETS span the SAME 8-dim subspace of
# 8x8 matrices (stack each generator's 64 entries as a column, compare ranks).
def flatten(M):
    return sp.Matrix([M[r, c] for r in range(8) for c in range(8)])


permuted_stack = sp.Matrix.hstack(*[flatten(M) for M in permuted_su3])
reference_stack = sp.Matrix.hstack(*[flatten(M) for M in reference_su3])
combined_stack = sp.Matrix.hstack(permuted_stack, reference_stack)
rank_permuted = permuted_stack.rank()
rank_reference = reference_stack.rank()
rank_combined = combined_stack.rank()
same_span = (rank_permuted == rank_reference == rank_combined) and rank_combined <= 8
print(
    f"  Fallback SPAN check: rank(permuted)={rank_permuted}, rank(reference)={rank_reference}, "
    f"rank(combined)={rank_combined} -- same 8-dim span? {same_span}"
)
all_su3_ok = per_generator_match or same_span
print(f"  ALL 8 off-diagonal SU(3) generators validated (one-to-one OR same span)? {all_su3_ok}")
print("  (B-L's diagonal-with-degenerate-eigenvalues check alone could not detect a")
print("  wrong permutation WITHIN a degenerate eigenspace; a non-diagonal generator's")
print("  off-diagonal entries can, and do, here.)")
print()

print("=" * 92)
print("PART 2 -- Build all 15 so(6) generators, qubit basis, then permute to SUBSETS basis")
print("=" * 92)
so6_vec_gens = [M for (_, M) in so6_generators()]
so6_spin_gens_qubit = [lift_to_spinor(M) for M in so6_vec_gens]
so6_spin_gens_sigma = [sp.simplify(P * G * P.T) for G in so6_spin_gens_qubit]
print(
    f"  Built {len(so6_spin_gens_sigma)} generators (expect 15), permuted to SUBSETS/Sigma basis."
)
print()

print("=" * 92)
print("PART 3 -- Reconstruct k_vec (EXACT reuse of round94's construction)")
print("=" * 92)
v_a = vec64_from_pairs({((1,), (2, 3)): 1, ((2,), (1, 3)): -1, ((3,), (1, 2)): 1})
v_b = vec64_from_pairs({((1, 2, 3), ()): 1})
nrm_va = sp.sqrt(sp.simplify(herm(v_a, v_a)))
nrm_vb = sp.sqrt(sp.simplify(herm(v_b, v_b)))
u1 = sp.Matrix([sp.simplify(x / nrm_va) for x in v_a])
u2 = sp.Matrix([sp.simplify(x / nrm_vb) for x in v_b])
w = vec64_from_pairs({((), ()): 1})
nrm_w = sp.sqrt(sp.simplify(herm(w, w)))
w_hat = sp.Matrix([sp.simplify(x / nrm_w) for x in w])
Du1 = D_full(u1)
Du2 = D_full(u2)
a_coeff = sp.simplify(herm(w_hat, Du1))
b_coeff = sp.simplify(herm(w_hat, Du2))
alpha, beta = b_coeff, -a_coeff
k_vec = sp.Matrix([sp.simplify(alpha * u1[i] + beta * u2[i]) for i in range(N)])
Dk = D_full(k_vec)
k_is_kernel = sp.simplify(Dk) == sp.zeros(N, 1)
print(
    f"  a_coeff={a_coeff}, b_coeff={b_coeff}; D_full(k_vec)==0 (k_vec IS the physical kernel)? {k_is_kernel}"
)
print()

print("=" * 92)
print("PART 4 -- Leibniz-lift all 15 so(6) generators to 64-dim, apply to k_vec")
print("=" * 92)
images = []
for idx, G in enumerate(so6_spin_gens_sigma):
    G64 = leibniz64(G)
    Gk = sp.simplify(G64 * k_vec)
    is_zero = Gk == sp.zeros(N, 1)
    images.append(Gk)
    print(f"  generator {idx + 1}/15: G_{idx + 1}.k_vec == 0 (annihilates k_vec)? {is_zero}")
print()

print("=" * 92)
print("PART 5 -- Dimension of span{k_vec, G_1.k_vec, ..., G_15.k_vec}")
print("=" * 92)
all_vectors = [k_vec] + images
M_span = sp.Matrix.hstack(*all_vectors)
rank_span = M_span.rank()
print(
    f"  span dimension (rank of [k_vec | G_1.k_vec | ... | G_15.k_vec], 64x16 matrix) = {rank_span}"
)
print()

verdict = {
    "P_is_permutation_matrix": bool(sp.simplify(P * P.T - sp.eye(8)) == sp.zeros(8, 8)),
    "permutation_sanity_check_against_round94_BmL_ok": bool(permutation_sanity_check_ok),
    "stronger_offdiagonal_su3_sanity_check_ok": bool(all_su3_ok),
    "k_vec_confirmed_physical_kernel": bool(k_is_kernel),
    "span_dimension_of_su4_orbit": int(rank_span),
    "k_vec_is_su4_singlet": bool(rank_span == 1),
}
print("=" * 92)
print("VERDICT")
print("=" * 92)
for kk, vv in verdict.items():
    print(f"  {kk}: {vv}")

if not permutation_sanity_check_ok or not all_su3_ok:
    label = "BLOCKED__PERMUTATION_SANITY_CHECK_FAILED"
elif rank_span == 1:
    label = "SU4_SINGLET_CONFIRMED__PATI_SALAM_INCOMPATIBLE"
else:
    label = "NONTRIVIAL_SU4_ORBIT__NOT_A_PURE_SINGLET"
print(f"  label = '{label}'")
