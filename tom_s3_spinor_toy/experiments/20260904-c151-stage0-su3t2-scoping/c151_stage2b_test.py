r"""
C151 STAGE 2b -- THE TEST. Computes c on SU(3)/T^2 and confronts it with the
prediction frozen in PREREGISTRATION.md BEFORE any of this was computed:

    c(J.nabla) = +- i * c(nabla),  AS MATRICES, entry-by-entry,
    with a SINGLE consistent sign across the whole family.

Everything this test needs was fixed in advance and is imported, not chosen
here:
  * J_NK          -- pinned in Stage 1a by the Nijenhuis tensor (eps=(-1,1,-1))
  * the family    -- Hom_{T^2}(m, Lambda^2 m), dim 6 (Stage 0)
  * sector dims   -- (3,3) (Stage 1b, re-derived independently in Stage 2a)
  * the geometry  -- built and calibrated in Stage 2a (Killing pair, |mu| = 3)

SIGN-CONVENTION GATE (the trap C139 caught in itself)
  C139 found that its spin lift and its vector representation encoded the SAME
  so(6) generator with OPPOSITE signs under the e_k^2 = -1 convention, and had
  to negate one of them. Rather than inherit that fix blindly, this file
  DERIVES the correct relative sign from the Clifford algebra itself:
      [spin_lift(L), e_j]  must equal  sum_k L_kj e_k   (up to an overall sign)
  The sign is measured, asserted to be consistent across all generators, and
  then used. If it is not consistent, the script raises.

Run:  python c151_stage2b_test.py
"""

import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
STAGE2A = HERE / "c151_stage2_construct.py"
C73B_PATH = (
    HERE.parent
    / "20260811-c73b-torsion-family-genuine-deformation-and-twist-control"
    / "c73b_torsion_family.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


S2A = load_module("c151_stage2_construct", STAGE2A)  # re-runs its own gates
C73B = load_module("c73b_torsion_family", C73B_PATH)

E = S2A.E
spin_lift_np = S2A.spin_lift_np
T2_M = S2A.T2_M
RHO_SIGMA = S2A.RHO_SIGMA
EVEN, ODD = S2A.EVEN, S2A.ODD
dom, tgt = S2A.dom, S2A.tgt

print()
print("=" * 78)
print("STAGE 2b  (Stage 2a's gates re-ran above and passed)")
print("=" * 78)

# ---------------------------------------------------------------------------
# SIGN GATE -- derive the spin-vs-vector relative sign, do not assume it
# ---------------------------------------------------------------------------
signs = []
for L in T2_M + [S2A.NOMIZU_LC[i] for i in range(1, 7)]:
    S = spin_lift_np(L)
    for j in range(6):
        lhs = S @ E[j + 1] - E[j + 1] @ S
        rhs = sum((L[k, j] * E[k + 1] for k in range(6)), np.zeros((8, 8), dtype=complex))
        if np.max(np.abs(rhs)) < 1e-12:
            continue
        for s in (+1, -1):
            if np.max(np.abs(lhs - s * rhs)) < 1e-8:
                signs.append(s)
                break
        else:
            raise AssertionError("spin lift is not a multiple of the vector rep -- STOP")
assert signs and all(s == signs[0] for s in signs), f"inconsistent sign: {set(signs)}"
SPIN_VS_VEC = signs[0]
print(f"  SIGN GATE: [spin_lift(L), e_j] = ({SPIN_VS_VEC:+d}) * sum_k L_kj e_k, consistently")
print(
    f"             across {len(signs)} generator/index pairs  -> vector-rep sign = {SPIN_VS_VEC:+d}"
)

# ---------------------------------------------------------------------------
# The admissible family, in the SAME J-aligned basis as the geometry
# ---------------------------------------------------------------------------
family = C73B.equivariant_torsion_basis([g.astype(complex) for g in T2_M])
n_fam = family.shape[1]
n_pairs = len(C73B.PAIRS)
print(f"  admissible family dim (J-aligned basis) = {n_fam}   (Stage 0 found 6)")
assert n_fam == 6, "family dimension changed under the J-alignment -- inconsistent"

J_NK = np.zeros((6, 6))
for k in range(3):
    J_NK[2 * k, 2 * k + 1] = -1
    J_NK[2 * k + 1, 2 * k] = 1
print("  J_NK in this basis is the STANDARD J_0 (that is what the alignment achieved)")


def nomizu_from_vec(vec: np.ndarray) -> dict[int, np.ndarray]:
    """A family vector -> {i: Lambda(e_i) as a 6x6 antisymmetric matrix}."""
    T = vec.reshape(6, n_pairs)
    return {i + 1: C73B.bivec_to_6x6(C73B.matrix_to_bivec_row(T[i])) for i in range(6)}


# C73b stores each row as coefficients over PAIRS; rebuild the 6x6 directly.
def row_to_6x6(row: np.ndarray) -> np.ndarray:
    M = np.zeros((6, 6), dtype=complex)
    for idx, (a, b) in enumerate(C73B.PAIRS):
        M[a, b] += row[idx]
        M[b, a] -= row[idx]
    return M


def c_of(vec: np.ndarray) -> np.ndarray:
    """The 3x3 coefficient matrix of the twisted Dirac operator on the
    invariant sector, for the connection given by this family vector."""
    T = vec.reshape(6, n_pairs)
    lam = {i + 1: row_to_6x6(T[i]) for i in range(6)}
    I6 = np.eye(6)
    D = np.zeros((48, 48), dtype=complex)
    for i in range(1, 7):
        D += np.kron(E[i] @ spin_lift_np(lam[i]), I6)
        D += np.kron(E[i], SPIN_VS_VEC * lam[i])
    return tgt.conj().T @ D @ dom


def apply_J(vec: np.ndarray) -> np.ndarray:
    """Precomposition with J on the SOURCE index: (T o J)(e_i) = T(J e_i)."""
    T = vec.reshape(6, n_pairs)
    return (J_NK.T @ T).reshape(-1)


# ---------------------------------------------------------------------------
# THE TEST
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("THE FROZEN PREDICTION:  c(J.nabla) = +-i c(nabla), as 3x3 matrices,")
print("                        one consistent sign across the whole family")
print("=" * 78)

results = []
for k in range(n_fam):
    v = family[:, k]
    c0, cJ = c_of(v), c_of(apply_J(v))
    scale = max(np.max(np.abs(c0)), np.max(np.abs(cJ)), 1e-30)
    dev_plus = np.max(np.abs(cJ - 1j * c0)) / scale
    dev_minus = np.max(np.abs(cJ + 1j * c0)) / scale
    best = "+i" if dev_plus < dev_minus else "-i"
    results.append((k, np.max(np.abs(c0)), dev_plus, dev_minus, best))
    print(f"  family vector {k}:  max|c| = {np.max(np.abs(c0)):.6f}")
    print(f"      rel.dev from  +i*c : {dev_plus:.3e}")
    print(f"      rel.dev from  -i*c : {dev_minus:.3e}   -> closer: {best}")

best_signs = {r[4] for r in results}
worst = max(min(r[2], r[3]) for r in results)
consistent = len(best_signs) == 1
nonzero_c = all(r[1] > 1e-8 for r in results)

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print(f"  all c matrices nonzero (test not vacuous) : {nonzero_c}")
print(f"  a SINGLE sign fits every family vector    : {consistent}  {best_signs}")
print(f"  worst relative deviation                  : {worst:.3e}")
print()

# --- VACUITY GATE (added after the first run of this file printed a FALSE
# "PREDICTION CONFIRMED" on c == 0 for every family vector: 0 = i*0 satisfies
# the identity trivially).  The non-vacuity check existed but was NOT wired
# into the verdict.  It is now the FIRST gate, and it dominates. ------------
if not nonzero_c:
    print("  *** VACUOUS -- NOT A CONFIRMATION. ***")
    print("  c vanishes identically on the entire family, so c(J.nabla) = i c(nabla)")
    print("  reduces to 0 = i*0 and carries no information about C-linearity.")
    print("  Per the pre-registration's third pre-committed outcome, this is NOT")
    print("  evidence either way for the prediction.")
    print()
    print("  Diagnosed (see decision.md): the vanishing is STRUCTURAL, not a bug --")
    print("  the Levi-Civita connection IS in the family (residual 3.3e-16), the")
    print("  operator is nonzero elsewhere (max|Dv| = 6.38 on a random odd-block")
    print("  vector, rank 15/24), yet it ANNIHILATES the whole invariant domain,")
    print("  with Term1 and Term2 vanishing SEPARATELY rather than cancelling.")
elif consistent and worst < 1e-8:
    print("  PREDICTION CONFIRMED on SU(3)/T^2. c is C-linear w.r.t. the")
    print("  nearly-Kahler J, as matrices -- so C147's holomorphy is NOT a")
    print("  G2/SU(3) accident but survives on a second, independent NK coset.")
elif consistent:
    print("  PREDICTION FAILS quantitatively: a single sign is preferred but the")
    print(f"  deviation is {worst:.3e}, far above numerical noise. c is NOT")
    print("  C-linear w.r.t. J here -> the S^6 holomorphy is LOCALIZED.")
else:
    print("  PREDICTION FAILS structurally: no single sign fits the whole family,")
    print("  so c does not intertwine J with multiplication by i at all ->")
    print("  the S^6 holomorphy is LOCALIZED to G2/SU(3).")
