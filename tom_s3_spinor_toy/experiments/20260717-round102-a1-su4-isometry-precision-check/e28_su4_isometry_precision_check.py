"""E28 (round102, A1): precision check of gate G97's literal wording
("no SU(4) subgroup in Iso(S3xS6)=SO(4)xSO(7)") against two distinct
candidate symmetry groups: (a) the round-metric isometry SO(7) [as
literally cited], and (b) the G2-holonomy group actually used to derive
SU(3)_c in preprint.tex:195-196,274-277 ("the G2 holonomy of
S6=G2/SU(3) provides SU(3)_c").

Part 1: explicit so(6)-in-so(7) closure check (abstract Lie algebra,
21x21... actually 7x7 antisymmetric matrices, real, numeric).
Part 2: dimension-count argument for the G2-holonomy-based version.
"""

import numpy as np

print("=" * 92)
print("PART 1 -- so(6) subalgebra of so(7): explicit closure check")
print("=" * 92)


def antisym_basis(n):
    """Standard basis of so(n): E_ab = e_a e_b^T - e_b e_a^T, a<b."""
    basis = []
    idx_pairs = []
    for a in range(n):
        for b in range(a + 1, n):
            M = np.zeros((n, n))
            M[a, b] = 1
            M[b, a] = -1
            basis.append(M)
            idx_pairs.append((a, b))
    return basis, idx_pairs


so7_basis, so7_pairs = antisym_basis(7)
dim_so7 = len(so7_basis)
print(f"  dim so(7) = {dim_so7}  (expected 21 = 7*6/2)")

# so(6) = subalgebra of so(7) fixing the 7th coordinate (index 6, 0-indexed)
# i.e. all E_ab with a,b in {0,...,5} (excluding index 6 entirely)
so6_indices = [i for i, (a, b) in enumerate(so7_pairs) if a < 6 and b < 6]
dim_so6_found = len(so6_indices)
print(
    f"  dim so(6) (as subset of so(7) basis, indices 0-5 only) = {dim_so6_found}"
    f"  (expected 15 = 6*5/2)"
)


def bracket(A, B):
    return A @ B - B @ A


# verify closure: [E_ab, E_cd] for a,b,c,d all in {0..5} stays within the
# so(6) subspace (i.e. has zero entries in row/col 6) -- check for ALL pairs
all_closed = True
violations = []
for i in so6_indices:
    for j in so6_indices:
        comm = bracket(so7_basis[i], so7_basis[j])
        # closure means comm[6,:] and comm[:,6] are all zero
        row6_zero = np.allclose(comm[6, :], 0)
        col6_zero = np.allclose(comm[:, 6], 0)
        if not (row6_zero and col6_zero):
            all_closed = False
            violations.append((so7_pairs[i], so7_pairs[j]))

print(f"  so(6) (indices 0-5) closed under [.,.] within so(7)? {all_closed}")
if not all_closed:
    print(f"  Violations: {violations[:5]}")
print()
print("  Interpretation: so(6) (the isotropy/stabilizer subalgebra of so(7) at")
print("  a point of S^6, i.e. fixing coordinate index 6) is a genuine Lie")
print("  SUBALGEBRA of so(7) -- standard, elementary fact (so(n-1) subset so(n)")
print("  always, for any sphere S^{n-1} subset R^n under its round-metric")
print("  isometry group). Since so(6) is isomorphic to su(4) (classical D3=A3")
print("  exceptional Lie-algebra isomorphism, [DOCS], NOT independently proven")
print("  here -- standard classification fact), this means su(4) DOES embed")
print("  abstractly in so(7), contradicting a LITERAL reading of 'no SU(4)")
print("  subgroup in SO(4)xSO(7)' if that phrase means pure abstract group theory.")
print()

print("=" * 92)
print("PART 2 -- dimension count: does su(4) fit in G2 (the ACTUAL holonomy group")
print("used by preprint.tex to derive SU(3)_c, not the broader SO(7) isometry)?")
print("=" * 92)
dim_g2 = 14  # [DOCS] standard fact, G2 is the 14-dimensional exceptional Lie group
dim_su4 = 15  # dim(su(n)) = n^2-1 = 15 for n=4
dim_so4 = 6  # dim(so(4)) = dim(su(2)+su(2)) = 3+3 = 6
print(f"  dim(G2) = {dim_g2}   [DOCS, standard]")
print(f"  dim(su(4)) = {dim_su4}   [n^2-1, n=4]")
print(f"  dim(so(4)) = {dim_so4}   [dim su(2)+su(2)]")
su4_fits_in_g2_alone = dim_su4 <= dim_g2
print(f"  Can su(4) (dim {dim_su4}) fit inside G2 (dim {dim_g2}) ALONE? {su4_fits_in_g2_alone}")
print("  -- NO, by dimension alone: a 15-dim subalgebra cannot embed in a")
print("  14-dim ambient algebra. This is a CLEANER, more robust argument than")
print("  the SO(7)-isometry-based wording, IF G2-holonomy (not full SO(7)")
print("  isometry) is really the physically relevant comparison group -- which")
print("  preprint.tex's OWN text (lines 195-196, 274-277) states IS the actual")
print("  mechanism used to derive SU(3)_c ('the G2 holonomy of S6=G2/SU(3)")
print("  provides SU(3)_c'), not the broader round-metric SO(7) isometry group")
print("  that gate G97's literal wording cites.")
print()

verdict = {
    "so6_is_genuine_subalgebra_of_so7": bool(all_closed),
    "su4_abstractly_embeds_in_so7_via_so6": bool(all_closed),  # given so6~su4 (DOCS)
    "su4_fits_in_g2_alone_by_dimension": bool(su4_fits_in_g2_alone),
    "g2_holonomy_based_no_go_more_robust_than_so7_isometry_wording": True,
}
print("=" * 92)
print("VERDICT")
print("=" * 92)
for k, v in verdict.items():
    print(f"  {k}: {v}")

label = "WORDING_IMPRECISE__PHYSICS_CONCLUSION_LIKELY_UNCHANGED_VIA_G2_DIMENSION_ARGUMENT"
print(f"  label = '{label}'")
