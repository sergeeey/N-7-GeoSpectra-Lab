"""E31 (round108): stabilizer of the FULL background (round metric g +
associative 3-form phi, the standard G2-structure on R^7/S^6) within
so(7), NOT just the metric alone -- Codex/round105's item 1.

Standard fact being checked BY DIRECT COMPUTATION (not merely cited):
G2 = Stab(phi) in GL(7,R), a 14-dim subalgebra of so(7) (21-dim) --
this is confirmed here numerically, not assumed.
"""

import itertools

import sympy as sp

N = 7


def antisym_basis(n):
    """Standard basis of so(n): E_ab, +1 at [a,b], -1 at [b,a], a<b."""
    basis = []
    idx_pairs = []
    for a in range(n):
        for b in range(a + 1, n):
            M = sp.zeros(n, n)
            M[a, b] = 1
            M[b, a] = -1
            basis.append(M)
            idx_pairs.append((a, b))
    return basis, idx_pairs


so7_basis, so7_pairs = antisym_basis(N)
dim_so7 = len(so7_basis)
print("=" * 92)
print("PART 0 -- so(7) generators")
print("=" * 92)
print(f"  dim so(7) = {dim_so7}  (expected 21)")
print()

# ---------------------------------------------------------------------------
# Standard associative 3-form phi_0 on R^7 (0-indexed here, i.e. index
# 0..6 corresponds to the usual 1..7 in the literature convention):
# phi = e^123 + e^145 + e^167 + e^246 - e^257 - e^347 - e^356
# (Bryant 2005 "Some remarks on G2-structures", standard convention;
# indices below shifted to 0-indexed: 1->0, 2->1, ..., 7->6)
# ---------------------------------------------------------------------------
PHI_TERMS = [
    (+1, (0, 1, 2)),  # e^123
    (+1, (0, 3, 4)),  # e^145
    (+1, (0, 5, 6)),  # e^167
    (+1, (1, 3, 5)),  # e^246
    (-1, (1, 4, 6)),  # e^257
    (-1, (2, 3, 6)),  # e^347
    (-1, (2, 4, 5)),  # e^356
]


def build_phi():
    """Fully antisymmetric (0,3) tensor from the signed basis terms above."""

    def eps_sign(perm):
        # sign of the permutation taking sorted(perm) -> perm
        p = list(perm)
        sign = 1
        for i in range(len(p)):
            for j in range(len(p) - 1 - i):
                if p[j] > p[j + 1]:
                    p[j], p[j + 1] = p[j + 1], p[j]
                    sign = -sign
        return sign

    phi = {}
    for coeff, (i, j, k) in PHI_TERMS:
        for perm in itertools.permutations((i, j, k)):
            phi[perm] = coeff * eps_sign(perm)
    return phi


PHI = build_phi()


def phi_val(i, j, k):
    return PHI.get((i, j, k), 0)


print("=" * 92)
print("PART 1 -- Sanity check: does the tensor-action formula preserve the METRIC")
print("(g=delta_ij), for ALL 21 so(7) generators?  [MUST pass before trusting phi]")
print("=" * 92)


def action_on_metric(X):
    """(X.g)_{ij} = -X_{il}*g_{lj} - X_{jl}*g_{il}, g=delta."""
    Xg = sp.zeros(N, N)
    for i in range(N):
        for j in range(N):
            val = 0
            for m in range(N):
                val += -X[i, m] * (1 if m == j else 0)
                val += -X[j, m] * (1 if m == i else 0)
            Xg[i, j] = val
    return Xg


metric_preserved_all = True
for idx, X in enumerate(so7_basis):
    Xg = action_on_metric(X)
    ok = Xg == sp.zeros(N, N)
    metric_preserved_all = metric_preserved_all and ok
print(f"  ALL 21 so(7) generators preserve the metric (X.g=0)? {metric_preserved_all}")
if not metric_preserved_all:
    print("  !!! FORMULA/SIGN ERROR -- STOPPING before trusting the phi computation !!!")
print()

print("=" * 92)
print("PART 2 -- Action of each so(7) generator on phi (associative 3-form)")
print("=" * 92)


def action_on_phi(X):
    """(X.phi)_{ijk} = -X_{il}*phi_{ljk} - X_{jl}*phi_{ilk} - X_{kl}*phi_{ijl},
    computed at all C(7,3)=35 independent index triples (antisymmetric tensor,
    fully determined by i<j<k values)."""
    result = {}
    for i, j, k in itertools.combinations(range(N), 3):
        val = 0
        for m in range(N):
            val += -X[i, m] * phi_val(m, j, k)
            val += -X[j, m] * phi_val(i, m, k)
            val += -X[k, m] * phi_val(i, j, m)
        result[(i, j, k)] = sp.nsimplify(val)
    return result


stabilizer_indices = []
for idx, X in enumerate(so7_basis):
    Xphi = action_on_phi(X)
    annihilates = all(v == 0 for v in Xphi.values())
    if annihilates:
        stabilizer_indices.append(idx)

dim_stabilizer = len(stabilizer_indices)
print(f"  Number of so(7) BASIS generators individually annihilating phi: {dim_stabilizer}")
print("  (Note: this counts basis generators annihilating phi directly, a lower bound")
print("  on the stabilizer's dimension if the stabilizer is not aligned with the raw")
print("  antisymmetric basis -- Part 3 computes the TRUE dimension via the general")
print("  linear map's kernel, not just this basis-aligned count.)")
print()

print("=" * 92)
print("PART 3 -- TRUE stabilizer dimension: kernel of the linear map so(7) -> Lambda^3,")
print("X |-> X.phi (35-dim target, exact linear-algebra kernel computation)")
print("=" * 92)
triples = list(itertools.combinations(range(N), 3))
# Build the 35x21 matrix: columns = so(7) basis generators, rows = the 35
# independent components of X.phi
M = sp.zeros(len(triples), dim_so7)
for col, X in enumerate(so7_basis):
    Xphi = action_on_phi(X)
    for row, t in enumerate(triples):
        M[row, col] = Xphi[t]

kernel_basis = M.nullspace()
true_stabilizer_dim = len(kernel_basis)
print(f"  dim(Lambda^3(R^7)*) = {len(triples)} (expected 35)")
print(f"  TRUE stabilizer dimension (nullspace of the 35x21 map X->X.phi) = {true_stabilizer_dim}")
print(f"  Consistent with G2 (dim=14)? {true_stabilizer_dim == 14}")
print()

print("=" * 92)
print("PART 4 -- SKEPTIC-FLAGGED FOLLOW-UP: stabilizer of phi AND a chosen point x0")
print("(the almost-complex structure J is POINT-DEPENDENT, J_x(v)=x-cross-v; a Killing")
print("vector already in G2=Stab(phi) preserves the octonion cross-product EVERYWHERE,")
print("but only fixing x0 too gives the ISOTROPY subgroup at x0 -- i.e. SU(3), the")
print("actual LOCAL unbroken group after the G2/SU(3) coset reduction, matching")
print("preprint.tex's own S6=G2/SU(3) framing directly.)")
print("=" * 92)
x0 = sp.Matrix([1, 0, 0, 0, 0, 0, 0])  # base point, S^6 subset R^7
# Build the 14-dim G2 subspace explicitly from the nullspace basis, then find
# the further subspace that ALSO satisfies X*x0 = 0 (fixes the point).
G2_basis_matrices = []
for vec in kernel_basis:
    Xg2 = sp.zeros(N, N)
    for col, X in enumerate(so7_basis):
        Xg2 += vec[col] * X
    G2_basis_matrices.append(Xg2)

# Stack: for each G2 basis element, X*x0 is a 7-vector; find combinations of
# the 14 basis elements whose resulting X*x0 = 0 (7 equations, 14 unknowns).
Fix_matrix = sp.zeros(N, len(G2_basis_matrices))
for col, Xg2 in enumerate(G2_basis_matrices):
    v = Xg2 * x0
    for row in range(N):
        Fix_matrix[row, col] = v[row]

isotropy_coeffs = Fix_matrix.nullspace()
dim_isotropy_at_x0 = len(isotropy_coeffs)
print(f"  dim(stabilizer of phi AND x0) = {dim_isotropy_at_x0}  (expected 8, matching su(3))")
print()

verdict = {
    "metric_preserved_by_all_21_generators": bool(metric_preserved_all),
    "basis_aligned_count_annihilating_phi": int(dim_stabilizer),
    "true_stabilizer_dimension": int(true_stabilizer_dim),
    "stabilizer_consistent_with_G2_dim14": bool(true_stabilizer_dim == 14),
    "isotropy_at_x0_dimension": int(dim_isotropy_at_x0),
    "isotropy_consistent_with_su3_dim8": bool(dim_isotropy_at_x0 == 8),
    "su4_dim15_exceeds_G2_dim14_AND_su3_dim8_either_reading": True,
}
print("=" * 92)
print("VERDICT")
print("=" * 92)
for k, v in verdict.items():
    print(f"  {k}: {v}")

if not metric_preserved_all:
    label = "BLOCKED__SANITY_CHECK_FAILED"
elif true_stabilizer_dim == 14:
    label = "STABILIZER_IS_14DIM__CONSISTENT_WITH_G2__CONFIRMS_G2_NOT_SO7_IS_PHYSICALLY_RELEVANT_AMBIENT"
else:
    label = f"STABILIZER_IS_{true_stabilizer_dim}DIM__UNEXPECTED__NEEDS_FOLLOWUP"
print(f"  label = '{label}'")
