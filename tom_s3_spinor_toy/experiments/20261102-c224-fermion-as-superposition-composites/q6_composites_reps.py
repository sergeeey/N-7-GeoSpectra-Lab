"""Q6 (second pass): representation-theoretic content of 'fermion = superposition of composite bosons'.

Four separate claims are tested; each is labelled by what it establishes.

  R1. Composites of TWO spinors: V_{1/2} (x) V_{1/2} = V_0 (+) V_1. Every two-spinor composite has integer spin.
      Numerically: Casimir of the tensor product has eigenvalues {0, 2}.
  R2. Composites of THREE spinors: V_{1/2} (x) V_{1/2} (x) V_{1/2} contains V_{1/2} with multiplicity 2.
      So a spin-1/2 state CAN be a composite of an odd number of spinor factors; a bosonic (integer spin)
      superposition cannot produce it equivariantly (see R3).
  R3. No equivariant (SU(2)-intertwining) linear map from the integer-spin space (bosons) to V_{1/2}:
      solve T J_k = J_k' T (k = x, y, z) for T : V_0 (+) V_1 -> V_{1/2}. The null space is {0}.
      This is the representation-level content of 'a fermion is not a linear superposition of bosons'.
  R4. Rotation by 2 pi: exp(-2 pi i J_z) = +1 on integer spins and -1 on half-integer spins (exact),
      so R4 is the representation-level reason for R3 (the 2 pi element separates the two spaces).
  R5. Contrast with the L^2 interval expansion of e^{i ph/2} (q6_fourier_superposition.py): there the
      sum exists but is not equivariant; it is not an intertwiner, so it does not contradict R3.
  Statistics (commutation vs anticommutation) is NOT a consequence of any of these (OPEN, outside the group theory).
"""

import numpy as np
from scipy.linalg import null_space

fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


def spin_ops(j):
    d = int(round(2 * j + 1))
    m = np.array([j - k for k in range(d)])
    Jz = np.diag(m).astype(complex)
    Jp = np.zeros((d, d), dtype=complex)
    for k in range(1, d):
        mm = m[k]
        Jp[k - 1, k] = np.sqrt(j * (j + 1) - mm * (mm + 1))
    Jm = Jp.conj().T
    Jx = (Jp + Jm) / 2
    Jy = (Jp - Jm) / (2j)
    return [Jx, Jy, Jz]


def kron_sum(A, B):
    """Total angular momentum on a tensor product."""
    ia = np.eye(A[0].shape[0])
    ib = np.eye(B[0].shape[0])
    return [np.kron(a, ib) + np.kron(ia, b) for a, b in zip(A, B)]


def casimir(J):
    return J[0] @ J[0] + J[1] @ J[1] + J[2] @ J[2]


half = spin_ops(0.5)

# R1
two = kron_sum(half, half)
ev2 = np.round(np.linalg.eigvalsh(casimir(two)), 9)
check(
    "R1 two-spinor composites: Casimir eigenvalues are {0, 2} (integer spins only): %s"
    % sorted(set(ev2.tolist())),
    sorted(set(ev2.tolist())) == [0.0, 2.0],
)

# R2
three = kron_sum(two, half)
ev3 = np.round(np.linalg.eigvalsh(casimir(three)), 9)
mult_half = int(np.sum(np.abs(ev3 - 0.75) < 1e-9))
check(
    "R2 three-spinor composites contain j=1/2 with multiplicity 2 (4 states total): got %d states"
    % mult_half,
    mult_half == 4,
)

# R3 no intertwiner from integer-spin space to V_{1/2}
bos = [np.zeros((4, 4), dtype=complex) for _ in range(3)]
# bosonic space V_0 (+) V_1 (dim 4): build spin-1 and spin-0 blocks
s1 = spin_ops(1.0)
s0 = [np.zeros((1, 1), dtype=complex) for _ in range(3)]
bos = []
for k in range(3):
    M = np.zeros((4, 4), dtype=complex)
    M[1:, 1:] = s1[k]
    bos.append(M)
half_ops = half
# unknown T: 2 x 4 complex matrix; equations T bos_k = half_k T
dim_src = 4
dim_tgt = 2
rows = []
for k in range(3):
    # vec(T A) = (A^T kron I) vec(T), vec(B T) = (I kron B) vec(T) with column-major order
    A = bos[k]
    B = half_ops[k]
    M = np.kron(A.T, np.eye(dim_tgt)) - np.kron(np.eye(dim_src), B)
    rows.append(M)
big = np.vstack(rows)
ns = null_space(big, rcond=1e-10)
check(
    "R3 no nonzero SU(2)-intertwiner from integer spins V_0+V_1 to V_{1/2} (null space dim %d)"
    % ns.shape[1],
    ns.shape[1] == 0,
)

# R4 2 pi rotation
from scipy.linalg import expm

R_half = expm(-2j * np.pi * half[2])
check("R4a exp(-2 pi i J_z) = -1 on spin 1/2", np.allclose(R_half, -np.eye(2)))
R_bos = expm(-2j * np.pi * bos[2])
check("R4b exp(-2 pi i J_z) = +1 on V_0 (+) V_1", np.allclose(R_bos, np.eye(4)))

# control: R3 is not vacuous: an intertwiner between V_{1/2} and itself exists (identity)
rows_c = []
for k in range(3):
    A = half_ops[k]
    B = half_ops[k]
    rows_c.append(np.kron(A.T, np.eye(2)) - np.kron(np.eye(2), B))
ns_c = null_space(np.vstack(rows_c), rcond=1e-10)
check(
    "R3-control the same solver finds the identity on V_{1/2} (null space dim %d)" % ns_c.shape[1],
    ns_c.shape[1] == 1,
)

print("\nFAILS:", fails if fails else "none")
