"""C192 -- independent cross-check of C191's SO(4)xSO(4) branching (P8-P10),
built from pygae/clifford's OWN left-regular representation of Cl(8) instead
of the project's hand-rolled numpy Kronecker-product gamma matrices
(so4xso4_branching.py, reused by C191).

This is NOT the same code re-typed in a different library. The 256x256
matrices below come mechanically from clifford's own geometric-product
structure constants (the `*` operator on MultiVector objects, backed by
layout.gmt) -- a genuinely different code path computing the same abstract
algebra, per falsification-ladder.md's Independent Verification Strength
Ladder ("independently-written code" = Strong, a rung this project had not
occupied before this round -- every prior "independent" check was the same
hand-rolled construction re-run, not independently-written code).

Representation used: Cl(8,0)'s LEFT-REGULAR representation on itself
(256-dim, real) -- 16 direct copies of the 16-dim Dirac spinor rep C191's
own script uses. Every multiplicity below is expected to come out exactly
16x C191's numbers if the underlying claim is representation-independent (as
it must be: it is a statement about the abstract algebra, not about one
particular matrix realization of it).

Run:  python c192_pygae_clifford_crosscheck.py
"""

import clifford
import numpy as np

PASS, FAIL = [], []


def check(label, condition, detail=""):
    (PASS if condition else FAIL).append(label)
    print(f"  [{'PASS' if condition else 'FAIL'}] {label}")
    if detail:
        print(f"         {detail}")


print("=" * 78)
print("0  build Cl(8,0) via pygae/clifford, extract left-regular 256x256 matrices")
print("=" * 78)

layout, blades = clifford.Cl(8)
basis_list = list(blades.values())
N = len(basis_list)
check(
    "Q0 clifford.Cl(8) has all-positive signature, 256 blades",
    list(layout.sig) == [1] * 8 and N == 256,
)


def left_mult_matrix(x_mv):
    """Matrix of left multiplication by x_mv on the 256-dim regular rep."""
    cols = [(x_mv * b).value for b in basis_list]
    return np.array(cols, dtype=float).T


GAMMA = {i: left_mult_matrix(blades[f"e{i}"]) for i in range(1, 9)}

anticomm_ok = True
for i in range(1, 9):
    for j in range(1, 9):
        anticomm = GAMMA[i] @ GAMMA[j] + GAMMA[j] @ GAMMA[i]
        expected = 2 * np.eye(N) if i == j else np.zeros((N, N))
        if not np.allclose(anticomm, expected, atol=1e-8):
            anticomm_ok = False
check(
    "Q1 {Gamma_i,Gamma_j}=2 delta_ij on ALL 256x256 matrices (clifford's own"
    " geometric product, not the project's numpy Kronecker construction)",
    anticomm_ok,
)

symmetric_ok = all(np.allclose(GAMMA[i], GAMMA[i].T) for i in range(1, 9))
check(
    "Q2 each Gamma_i is symmetric (forced: orthogonal + Gamma_i^2=I on a real"
    " signed-permutation representation -- a structural check the project's"
    " own Hermitian complex construction could not even pose)",
    symmetric_ok,
)

print()
print("=" * 78)
print("A  chirality split: Gamma_A, Gamma_B, Gamma_9 on the 256-dim regular rep")
print("=" * 78)

GAMMA_A = GAMMA[1] @ GAMMA[2] @ GAMMA[3] @ GAMMA[4]
GAMMA_B = GAMMA[5] @ GAMMA[6] @ GAMMA[7] @ GAMMA[8]
GAMMA_9 = GAMMA_A @ GAMMA_B

check("Q3 Gamma_A^2=I", np.allclose(GAMMA_A @ GAMMA_A, np.eye(N), atol=1e-8))
check("Q4 Gamma_B^2=I", np.allclose(GAMMA_B @ GAMMA_B, np.eye(N), atol=1e-8))
check(
    "Q5 [Gamma_A,Gamma_B]=0",
    np.allclose(GAMMA_A @ GAMMA_B - GAMMA_B @ GAMMA_A, 0, atol=1e-8),
)
check("Q6 Gamma_9^2=I", np.allclose(GAMMA_9 @ GAMMA_9, np.eye(N), atol=1e-8))


def orth_basis_of_eigenspace(sym_mat, sign):
    """Orthonormal real basis of the sign-eigenspace of a symmetric involution."""
    proj = 0.5 * (np.eye(sym_mat.shape[0]) + sign * sym_mat)
    evals, evecs = np.linalg.eigh(proj)
    return evecs[:, evals > 0.5]


V_S = orth_basis_of_eigenspace(GAMMA_9, +1)
V_C = orth_basis_of_eigenspace(GAMMA_9, -1)
check(
    "Q7 8_s-block (Gamma_9=+1) and 8_c-block (Gamma_9=-1) each dim 128"
    " (16 copies of C191's 8-dim 8_s/8_c)",
    V_S.shape[1] == 128 and V_C.shape[1] == 128,
    f"got {V_S.shape[1]}, {V_C.shape[1]}",
)

print()
print("=" * 78)
print("B  so(4)_1's su(2)_L x su(2)_R generators (indices 1-4), REAL convention")
print("   (no i-factor needed here -- Gamma_i is symmetric, not Hermitian-complex,")
print("   so Gamma_i@Gamma_j for i!=j is already real antisymmetric, the natural")
print("   real so(n) generator; calibrated against the KNOWN row-58 result below,")
print("   not assumed correct.)")
print("=" * 78)


def M(i, j):
    return 0.5 * (GAMMA[i] @ GAMMA[j] - GAMMA[j] @ GAMMA[i])


M12, M13, M14 = M(1, 2), M(1, 3), M(1, 4)
M23, M24, M34 = M(2, 3), M(2, 4), M(3, 4)

L1, L2, L3 = (M23 + M14) / 2, (-M13 + M24) / 2, (M12 + M34) / 2
R1, R2, R3 = (M23 - M14) / 2, (-M13 - M24) / 2, (M12 - M34) / 2


def comm(a, b):
    return a @ b - b @ a


EPS = {
    (0, 1, 2): 1,
    (1, 2, 0): 1,
    (2, 0, 1): 1,
    (0, 2, 1): -1,
    (2, 1, 0): -1,
    (1, 0, 2): -1,
}
L_OPS, R_OPS = [L1, L2, L3], [R1, R2, R3]

# Real-antisymmetric generators close with a REAL structure constant (no i
# needed -- that i-factor in C186/C191's construction exists only to turn an
# anti-Hermitian complex combination into a Hermitian one; here Gamma_i is
# already real-symmetric, so Gamma_i@Gamma_j for i!=j is already the natural
# real generator). First run of this script found comm(L1,L2) = -2*L3 EXACTLY
# (ratio std=0 across every nonzero entry, diagnosed in a standalone scratch
# probe before writing this check, not guessed) -- a single global scale
# factor, not a structural break. C186 already names exactly this trap ("a
# Casimir is quadratic and could not see it, but a commutator can") -- so this
# checks for a SINGLE CONSISTENT scale (whatever it turns out to be), not an
# assumed +-1, and Q13's independent empirical calibration is what actually
# licenses trusting the final content comparison either way.


def closes_proportionally(ops):
    ratios = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                if (a, b, c) not in EPS:
                    continue
                lhs = comm(ops[a], ops[b])
                rhs = EPS[(a, b, c)] * ops[c]
                nz = np.abs(rhs) > 1e-8
                if not nz.any():
                    continue
                r = lhs[nz] / rhs[nz]
                if r.std() > 1e-6:
                    return False, None
                ratios.append(r.mean())
    if not ratios:
        return False, None
    ratios_arr = np.array(ratios)
    return (ratios_arr.std() < 1e-6), (ratios_arr.mean() if len(ratios_arr) else None)


su2_l_ok, k_l = closes_proportionally(L_OPS)
su2_r_ok, k_r = closes_proportionally(R_OPS)
check(
    "Q8 su(2)_L closes with a SINGLE consistent global scale k"
    " (empirically found, not assumed +-1)",
    su2_l_ok,
    f"k={k_l}",
)
check(
    "Q9 su(2)_R closes with the SAME scale k as su(2)_L",
    su2_r_ok and k_l is not None and k_r is not None and abs(k_l - k_r) < 1e-6,
    f"k_L={k_l} k_R={k_r}",
)
check(
    "Q10 [L_a,R_b]=0 for all a,b (genuine so(4)=su(2)+su(2) split)",
    all(
        np.allclose(comm(L_OPS[a], R_OPS[b]), 0, atol=1e-6)
        for a in range(3)
        for b in range(3)
    ),
)

CASIMIR_L = -(L1 @ L1 + L2 @ L2 + L3 @ L3)
CASIMIR_R = -(R1 @ R1 + R2 @ R2 + R3 @ R3)
check(
    "Q11 [Casimir_L,Casimir_R]=0",
    np.allclose(comm(CASIMIR_L, CASIMIR_R), 0, atol=1e-6),
)
check(
    "Q12 Casimir_L, Casimir_R symmetric (so eigh is valid)",
    np.allclose(CASIMIR_L, CASIMIR_L.T) and np.allclose(CASIMIR_R, CASIMIR_R.T),
)

print()
print("=" * 78)
print("C  joint (j_L,j_R) content on V_S / V_C -- calibrate scale against row58,")
print("   THEN read off the actual finding (does NOT assume the calibration works)")
print("=" * 78)


def joint_content(basis, cl_op, cr_op, scale=1.0):
    cl = basis.T @ cl_op @ basis
    cr = basis.T @ cr_op @ basis
    combo = cl + np.pi * cr
    _evals, evecs = np.linalg.eigh(combo)
    content: dict[tuple[float, float], int] = {}
    for k in range(combo.shape[0]):
        vec = evecs[:, k]
        jl = float(vec @ cl @ vec) * scale
        jr = float(vec @ cr @ vec) * scale
        jl_val = round((-1 + np.sqrt(max(0.0, 1 + 4 * jl))) / 2, 2)
        jr_val = round((-1 + np.sqrt(max(0.0, 1 + 4 * jr))) / 2, 2)
        key = (jl_val, jr_val)
        content[key] = content.get(key, 0) + 1
    return content


raw_cl_s = V_S.T @ CASIMIR_L @ V_S
raw_evals = np.round(np.linalg.eigvalsh(raw_cl_s), 6)
distinct = sorted(set(raw_evals.tolist()))
print(f"  raw Casimir_L eigenvalues on V_S (uncalibrated): {distinct}")

nonzero = [v for v in distinct if abs(v) > 1e-6]
check(
    "Q13 exactly one nonzero distinct Casimir_L eigenvalue on V_S (needed to"
    " calibrate scale unambiguously against the known j=1/2 value)",
    len(nonzero) == 1,
    f"got {nonzero}",
)

SCALE = 0.75 / nonzero[0] if len(nonzero) == 1 else 1.0
print(f"  calibration: SCALE = 0.75 / {nonzero[0] if nonzero else 'N/A'} = {SCALE}")

joint_s = joint_content(V_S, CASIMIR_L, CASIMIR_R, scale=SCALE)
joint_c = joint_content(V_C, CASIMIR_L, CASIMIR_R, scale=SCALE)
print(f"  8_s-block joint (j_L,j_R) content (128-dim, 16 copies): {joint_s}")
print(f"  8_c-block joint (j_L,j_R) content (128-dim, 16 copies): {joint_c}")

EXPECTED_S_x16 = {(0.5, 0.0): 64, (0.0, 0.5): 64}
check(
    "Q14 8_s content = 16x C191's row-58-restricted result (4x(1/2,0)+4x(0,1/2)"
    " -> 64x(1/2,0)+64x(0,1/2)) -- CALIBRATION CHECK, must pass before"
    " Q15/Q16 mean anything",
    joint_s == EXPECTED_S_x16,
    f"got {joint_s}",
)

print()
print("=" * 78)
print("D  the actual cross-check: does 8_c ALSO match (reproducing C191's P9/P10)")
print("=" * 78)

check(
    "Q15 8_c ALSO matches the same 16x-scaled row-58 content (mirrors C191's"
    " own P9 -- checking the postulate does NOT distinguish s from c)",
    joint_c == EXPECTED_S_x16,
    f"got {joint_c}",
)

IDENTICAL = joint_s == joint_c
check(
    "Q16 [THE CROSS-CHECK] 8_s and 8_c have IDENTICAL (j_L,j_R) content under"
    " so(4)_1 alone, independently reproduced via pygae/clifford's own"
    " left-regular Cl(8) representation -- reproduces C191's P10",
    IDENTICAL,
)

print()
print("=" * 78)
print(f"C192: {len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    for f in FAIL:
        print(f"  FAILED: {f}")
print("=" * 78)
