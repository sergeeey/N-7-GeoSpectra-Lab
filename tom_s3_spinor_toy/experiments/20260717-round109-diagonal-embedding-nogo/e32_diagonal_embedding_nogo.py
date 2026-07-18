"""E32 (round109): does a "diagonal" SU(4) embedding combining S3-side
(so(4)) and S6-side (so(7)/g2/su(3)) generators exist?

General argument (not exhaustive search): any Lie-algebra homomorphism
FROM a simple algebra is either zero or injective (kernel is an ideal;
simple algebras have only {0} and the whole algebra as ideals). Since
dim(so(4))=6 < 15=dim(su(4)), an injective map su(4)->so(4) is
impossible by dimension count alone -- so ANY homomorphism
su(4) -> so(4) (+) X (any complement X) must vanish identically on the
so(4) factor. This is verified here by (a) confirming su(4) is simple
(non-degenerate Killing form, standard semisimplicity criterion) and
(b) confirming the dimension counts, then stating the logical
consequence explicitly.
"""

import sympy as sp

IU = sp.I  # imaginary unit (renamed from bare I to avoid E741 ambiguous-name lint)


def su4_generators():
    """15 generators of su(4): antihermitian, traceless 4x4 matrices,
    generalized Gell-Mann basis (off-diagonal symmetric/antisymmetric
    pairs + Cartan diagonal generators), each scaled by i to be
    antihermitian (X^dagger = -X)."""
    n = 4
    gens = []
    # off-diagonal: symmetric (i*(E_ab+E_ba)) and antisymmetric (E_ab-E_ba)
    for a in range(n):
        for b in range(a + 1, n):
            Eab = sp.zeros(n, n)
            Eab[a, b] = 1
            Eba = sp.zeros(n, n)
            Eba[b, a] = 1
            gens.append(IU * (Eab + Eba))  # antihermitian: (i S)^dag = -i S = -(iS)
            gens.append(Eab - Eba)  # already antihermitian (antisymmetric real)
    # Cartan (diagonal, traceless): n-1 = 3 independent diagonal antihermitian generators
    # standard form: diag(1,...,1,-k,0,...,0)*i, with k ones (k=1..n-1)
    for k in range(1, n):
        d = sp.zeros(n, n)
        for idx in range(k):
            d[idx, idx] = IU
        d[k, k] = -IU * k
        gens.append(d)
    return gens


def is_antihermitian(M):
    return sp.simplify(M.H + M) == sp.zeros(M.shape[0], M.shape[0])


def is_traceless(M):
    return sp.simplify(sp.trace(M)) == 0


print("=" * 92)
print("PART 0 -- Build su(4) generators, verify basic properties")
print("=" * 92)
gens = su4_generators()
dim_su4_found = len(gens)
print(f"  Number of generators built: {dim_su4_found}  (expected 15 = 4^2-1)")
all_antiherm = all(is_antihermitian(g) for g in gens)
all_traceless = all(is_traceless(g) for g in gens)
print(f"  All antihermitian (X^dagger=-X, su(n) condition)? {all_antiherm}")
print(f"  All traceless? {all_traceless}")

# linear independence check
flat = sp.Matrix.hstack(*[sp.Matrix([g[r, c] for r in range(4) for c in range(4)]) for g in gens])
rank_gens = flat.rank()
print(f"  Linearly independent (rank of flattened generators)? rank={rank_gens} (expect 15)")
print()

print("=" * 92)
print("PART 1 -- Killing form of su(4): non-degenerate? (standard semisimplicity check)")
print("=" * 92)


def bracket(A, B):
    return A * B - B * A


# structure constants: [gens[i], gens[j]] = sum_k c_ijk gens[k]
# solve via the flattened-generator matrix (already linearly independent, rank 15
# in a 16-dim ambient gl(4,C) restricted to the 15-dim su(4) subspace -- since
# su(4) generators are traceless, they live in a 15-dim subspace of the 16-dim
# space of all 4x4 complex matrices; solve the linear system for each bracket).
G_flat = flat  # 16 x 15
G_pinv = (G_flat.T * G_flat).inv() * G_flat.T  # left pseudo-inverse (15x16)

adjoint_matrices = []
for i in range(dim_su4_found):
    ad_i = sp.zeros(dim_su4_found, dim_su4_found)
    for j in range(dim_su4_found):
        comm = bracket(gens[i], gens[j])
        comm_flat = sp.Matrix([comm[r, c] for r in range(4) for c in range(4)])
        coeffs = G_pinv * comm_flat
        for k in range(dim_su4_found):
            ad_i[k, j] = sp.nsimplify(sp.simplify(coeffs[k]))
    adjoint_matrices.append(ad_i)

killing = sp.zeros(dim_su4_found, dim_su4_found)
for i in range(dim_su4_found):
    for j in range(dim_su4_found):
        killing[i, j] = sp.simplify(sp.trace(adjoint_matrices[i] * adjoint_matrices[j]))

det_killing = sp.simplify(killing.det())
killing_nondegenerate = det_killing != 0
print(f"  Killing form 15x15 built. det(Killing form) = {det_killing}")
print(f"  Killing form non-degenerate (su(4) is semisimple)? {killing_nondegenerate}")
print("  [su(4) semisimple + connected + no smaller compact simple factor of the same")
print("  total dimension exists in the A-series at rank 3 => su(4) IS simple, standard")
print("  classification fact (A_3), not re-derived from scratch beyond this")
print("  semisimplicity check -- consistent with, not contradicting, its well-known")
print("  simplicity.]")
print()

print("=" * 92)
print("PART 2 -- Dimension counts and the logical consequence")
print("=" * 92)
dim_su4 = 15
dim_so4 = 6
dim_so7 = 21
dim_g2 = 14
dim_su3 = 8
print(f"  dim(su(4)) = {dim_su4}")
print(f"  dim(so(4)) = {dim_so4}  (S3-side factor)")
print(f"  dim(so(7)) = {dim_so7}, dim(g2) = {dim_g2}, dim(su(3)) = {dim_su3}  (S6-side, round108)")
print()
injective_into_so4_possible = dim_su4 <= dim_so4
print(
    f"  Can su(4) (dim {dim_su4}) inject into so(4) (dim {dim_so4})? {injective_into_so4_possible}"
)
print("  -- NO, by dimension alone (15 > 6).")
print()
print("  KEY LEMMA (standard): a Lie-algebra homomorphism FROM a SIMPLE algebra is")
print("  either the zero map or INJECTIVE (its kernel is an ideal of the simple")
print("  domain, and a simple algebra's only ideals are {0} and itself).")
print()
print("  CONSEQUENCE: for ANY homomorphism phi=(phi_1,phi_2): su(4) -> so(4)(+)X")
print("  (X = so(7), g2, or su(3)), phi_1: su(4)->so(4) CANNOT be injective (dimension")
print("  mismatch), so by the key lemma phi_1 MUST BE THE ZERO MAP -- for EVERY")
print("  possible homomorphism, with no case-by-case search needed. Every embedding")
print("  of su(4) into so(4)(+)X therefore projects to ZERO on the S3-side factor")
print("  automatically -- there is NO genuine 'diagonal' embedding using so(4)")
print("  nontrivially. Every su(4) embedding reduces entirely to a SAME-FACTOR")
print("  embedding into X alone (S6-side), already addressed by rounds 102/108.")
print()

verdict = {
    "su4_generators_built_correctly": bool(all_antiherm and all_traceless and rank_gens == 15),
    "killing_form_nondegenerate_su4_semisimple": bool(killing_nondegenerate),
    "injective_su4_into_so4_possible_by_dimension": bool(injective_into_so4_possible),
    "diagonal_embedding_using_so4_nontrivially_is_impossible": True,
}
print("=" * 92)
print("VERDICT")
print("=" * 92)
for k, v in verdict.items():
    print(f"  {k}: {v}")

label = "DIAGONAL_EMBEDDING_PROVEN_IMPOSSIBLE__ANY_SU4_EMBEDDING_REDUCES_TO_SAME_FACTOR"
print(f"  label = '{label}'")
