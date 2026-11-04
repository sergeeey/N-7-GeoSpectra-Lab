"""C239: bookkeeping checks of the one-generation construction on the SciForum poster
T. Lawrence, 'Symmetries of field configurations on compact spaces, spinors and no-go theorems', IOCSYM 2026 (https://sciforum.net/paper/34762; poster PDF read 2026-11-04).

Statements of the poster checked here (poster wording in quotes, no formula is taken from memory):
  S1 'Spinor rep of SO(4): 4 components = right-handed spinor (2, SU(2)_R) + left-handed spinor (2, SU(2)_L)'.
  S2 'Spinor rep of SO(7): 8 components = right-handed spinor rep of SO(6) (4) + left-handed (4)'.
  S3 '1st generation has 32 states: quarks 2x2x3x2 = 24, electron 2x2 = 4, neutrino 2x2 = 4'; assembled into a 32-dimensional space with
      boosts K_i = (i/2)(sigma_i (x) sigma_1 (x) 1_2 (x) 1_4), weak isospin T_i = (1/2)(1_2 (x) P_L (x) sigma_i (x) 1_4), colour C_i' = (1/2)(1_2 (x) 1_2 (x) 1_2 (x) lambda_i').
  S4 'Right-handed neutrino is then invariant under SU(3)_C x SU(2)_L x U(1)_Y' (no hypercharge generator is printed on the poster: NOT checkable here).

Predictions written BEFORE running:
  B1. With J_i = (1/2) sigma_i (x) 1 (x) 1 (x) 1 the generators J, K close into the Lorentz algebra; T_i form su(2) (needs P_L a projector, P_L = (1 - sigma_1)/2 in this chirality basis);
      C_i' (lambda embedded in 4x4 as the SU(3) acting on the first three components) form su(3); the three groups commute with each other.
  B2. Under Lorentz x SU(2)_L x SU(3)_C the 32 states split as: left-handed Weyl (1/2,0) x doublet x (3 + 1) = 16 states and right-handed (0,1/2) x two singlets x (3 + 1) = 16 states,
      which is the content of the standard model for one generation with a right-handed neutrino: this holds BY CONSTRUCTION of the matrices (they are built from the known charges), so it is bookkeeping, not a derivation.
  B3. Spin(4) Dirac spinor (4 components) = (2,1) + (1,2) under su(2)_L + su(2)_R.
  B4. Spin(7) 8-component spinor restricted to Spin(6) = 4 + 4bar with INEQUIVALENT blocks (different Cartan weight sets); the poster's colour generator acts with the same lambda on both isospin copies, so the second
      copy must be the charge conjugate of the 4bar for '2 (x) 4' to hold: that identification is not stated on the poster.
  B5. The factorisation 32 = 4 (spin x chirality of SO(4)) x 2 (isospin) x 4 (colour+lepton) uses a factor of 2 (isospin) that is not the SU(2)_L of S^3 on the poster: on the poster SU(2)_L comes from SO(4) acting on the 4-component SO(4) spinor, while the generator T_i acts on the separate 2-dimensional 'isospin' factor.
      So the identification of T_i with the S^3 isometry generator J3L-type quantum number is an extra step. Checked here only as: T_i commutes with K_i, J_i and C_i' (no relation to so(4)).
Self-controls (must be CAUGHT): P_L not a projector -> T_i not su(2); wrong boost sign; claim 4 and 4bar have equal weight sets; claim T_i acts on the right-handed block.
"""

import itertools
import sys

import numpy as np

FAILS = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAILS.append(name)


def expect_caught(name, cond):
    print(("CAUGHT " if not cond else "MISSED ") + name)
    if cond:
        FAILS.append("self-control not caught: " + name)


s0 = np.eye(2, dtype=complex)
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
SIG = [s1, s2, s3]


def kron(*ms):
    out = np.array([[1]], dtype=complex)
    for m in ms:
        out = np.kron(out, m)
    return out


def comm(a, b):
    return a @ b - b @ a


def close(a, b, tol=1e-12):
    return np.allclose(a, b, atol=tol)


eps = {(0, 1): 2, (1, 2): 0, (2, 0): 1}
I4 = np.eye(4, dtype=complex)
PL = (s0 - s1) / 2

# ---- B1: the poster's generators
J = [kron(0.5 * SIG[i], s0, s0, I4) for i in range(3)]
K = [kron(0.5j * SIG[i], s1, s0, I4) for i in range(3)]
T = [kron(s0, PL, 0.5 * SIG[i], I4) for i in range(3)]
# SU(3) Gell-Mann matrices embedded in 4x4 (act on the first three components, lepton = singlet)
lam = np.zeros((8, 3, 3), dtype=complex)
lam[0][0, 1] = lam[0][1, 0] = 1
lam[1][0, 1], lam[1][1, 0] = -1j, 1j
lam[2][0, 0], lam[2][1, 1] = 1, -1
lam[3][0, 2] = lam[3][2, 0] = 1
lam[4][0, 2], lam[4][2, 0] = -1j, 1j
lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2], lam[6][2, 1] = -1j, 1j
lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
L4 = []
for a in range(8):
    m = np.zeros((4, 4), dtype=complex)
    m[:3, :3] = lam[a]
    L4.append(m)
C = [kron(s0, s0, s0, 0.5 * L4[a]) for a in range(8)]
check(
    "B1: [J_i, J_j] = i eps J_k",
    all(close(comm(J[i], J[j]), 1j * J[k]) for (i, j), k in eps.items()),
)
check(
    "B1: [J_i, K_j] = i eps K_k",
    all(close(comm(J[i], K[j]), 1j * K[k]) for (i, j), k in eps.items()),
)
check(
    "B1: [K_i, K_j] = -i eps J_k (Lorentz algebra)",
    all(close(comm(K[i], K[j]), -1j * J[k]) for (i, j), k in eps.items()),
)
check("B1: P_L = (1 - sigma_1)/2 is a projector", close(PL @ PL, PL))
check(
    "B1: T_i close into su(2): [T_i, T_j] = i eps T_k",
    all(close(comm(T[i], T[j]), 1j * T[k]) for (i, j), k in eps.items()),
)
fabc_ok = True
# su(3): structure constants from the 3x3 lambda matrices: check closure of the span
span = [0.5 * lam[a] for a in range(8)]
M = np.array([m.reshape(-1) for m in span]).T
for a, b in itertools.combinations(range(8), 2):
    cm = comm(span[a], span[b]).reshape(-1)
    coef, res, rk, sv = np.linalg.lstsq(M, cm, rcond=None)
    fabc_ok = fabc_ok and np.allclose(M @ coef, cm, atol=1e-12)
check("B1: the eight C_i' = (1/2) lambda close under commutation (su(3))", fabc_ok)
check(
    "B1: T, C, J, K mutually commute where required (T,C vs J,K; T vs C)",
    all(close(comm(T[i], C[a]), 0) for i in range(3) for a in range(8))
    and all(
        close(comm(T[i], K[j]), 0) and close(comm(T[i], J[j]), 0)
        for i in range(3)
        for j in range(3)
    )
    and all(
        close(comm(C[a], K[j]), 0) and close(comm(C[a], J[j]), 0)
        for a in range(8)
        for j in range(3)
    ),
)
badK = [kron(0.5 * SIG[i], s1, s0, I4) for i in range(3)]  # boost without the factor i
expect_caught(
    "B1 control: boost without the factor i satisfies [K,K] = -i eps J",
    all(close(comm(badK[i], badK[j]), -1j * J[k]) for (i, j), k in eps.items()),
)
badPL = (s0 + 0.3 * s1) / 2
Tbad = [kron(s0, badPL, 0.5 * SIG[i], I4) for i in range(3)]
expect_caught(
    "B1 control: with a non-projector P_L the T_i close into su(2)",
    all(close(comm(Tbad[i], Tbad[j]), 1j * Tbad[k]) for (i, j), k in eps.items()),
)

# ---- B2: content under Lorentz x SU(2)_L x SU(3)
# chirality operator on the 2x2 (spin x chirality) factors: gamma5 ~ sigma_1 on the chirality factor
G5 = kron(s0, s1, s0, I4)
check(
    "B2: gamma5 = 1 (x) sigma_1 commutes with J and K",
    all(close(comm(G5, J[i]), 0) and close(comm(G5, K[i]), 0) for i in range(3)),
)
PLfull = (np.eye(32) - G5) / 2
PRfull = (np.eye(32) + G5) / 2
check(
    "B2: T_i vanish on the right-handed block and are nonzero on the left-handed block",
    all(close(T[i] @ PRfull, 0) for i in range(3))
    and any(not close(T[i] @ PLfull, 0) for i in range(3)),
)
expect_caught(
    "B2 control: T_i act on the right-handed block",
    not all(close(T[i] @ PRfull, 0) for i in range(3)),
)
cas_T = sum(t @ t for t in T)
cas_C = sum(c @ c for c in C)
evT = np.round(np.linalg.eigvalsh((cas_T + cas_T.conj().T) / 2), 6)
check(
    "B2: SU(2)_L Casimir = 3/4 on 16 states (left-handed) and 0 on 16 states (right-handed)",
    sorted(set(np.round(evT, 6))) == [0.0, 0.75]
    and int((np.abs(evT - 0.75) < 1e-6).sum()) == 16
    and int((np.abs(evT) < 1e-6).sum()) == 16,
)
evC = np.round(np.linalg.eigvalsh((cas_C + cas_C.conj().T) / 2), 6)
check(
    "B2: SU(3) Casimir eigenvalues: 4/3 on 24 states (colour triplets) and 0 on 8 (leptons)",
    int((np.abs(evC - 4 / 3) < 1e-6).sum()) == 24 and int((np.abs(evC) < 1e-6).sum()) == 8,
)
check(
    "B3-count: 2 x 2 x 3 x 2 = 24, 2 x 2 = 4, 2 x 2 = 4, total 32 = 2 x 2 x 2 x 4",
    2 * 2 * 3 * 2 == 24 and 24 + 4 + 4 == 32 and 2 * 2 * 2 * 4 == 32,
)


# ---- B3: Spin(4) Dirac spinor
def gammas(n):
    """Euclidean gamma matrices of Cl(n) (n even: 2^(n/2); n odd: 2^((n-1)/2)), hermitian, {g_a, g_b} = 2 delta"""
    if n == 1:
        return [np.array([[1]], dtype=complex)]
    if n == 2:
        return [s1, s2]
    if n % 2 == 0:
        sub = gammas(n - 2)
        gs = [np.kron(g, s3) for g in sub]
        d = sub[0].shape[0]
        gs.append(np.kron(np.eye(d), s1))
        gs.append(np.kron(np.eye(d), s2))
        return gs
    # odd: use even-dim n-1 plus chirality
    sub = gammas(n - 1)
    chi = np.eye(sub[0].shape[0], dtype=complex)
    for g in sub:
        chi = chi @ g
    # normalise so that chi^2 = 1
    ph = np.sqrt(chi @ chi)[0, 0] if False else None
    w = np.linalg.eigvals(chi @ chi)
    c2 = chi @ chi
    scale = np.sqrt(c2[0, 0])
    chi = chi / scale
    return sub + [chi]


def spin_gens(n, dim=None):
    gs = gammas(n)
    out = {}
    for a, b in itertools.combinations(range(n), 2):
        out[(a, b)] = (1j / 4) * (gs[a] @ gs[b] - gs[b] @ gs[a])
    return gs, out


g4, S4 = spin_gens(4)
check("B3: Spin(4) Dirac spinor has 4 components", g4[0].shape[0] == 4)
L_ = [
    0.5 * (S4[(1, 2)] + S4[(0, 3)]),
    0.5 * ((-S4[(0, 2)]) + S4[(1, 3)]),
    0.5 * (S4[(0, 1)] + S4[(2, 3)]),
]
R_ = [
    0.5 * (S4[(1, 2)] - S4[(0, 3)]),
    0.5 * ((-S4[(0, 2)]) - S4[(1, 3)]),
    0.5 * (S4[(0, 1)] - S4[(2, 3)]),
]
check(
    "B3: the two triples close into su(2)_L and su(2)_R and commute",
    all(
        close(comm(L_[i], L_[j]), 1j * L_[k]) or close(comm(L_[i], L_[j]), -1j * L_[k])
        for (i, j), k in eps.items()
    )
    and all(close(comm(L_[i], R_[j]), 0) for i in range(3) for j in range(3)),
)
casL = sum(x @ x for x in L_)
casR = sum(x @ x for x in R_)
evs = sorted(
    zip(
        np.round(np.linalg.eigvalsh((casL + casL.conj().T) / 2), 6),
        np.round(np.linalg.eigvalsh((casR + casR.conj().T) / 2), 6),
    )
)
# joint eigenvalues: need simultaneous; casL and casR commute and are diagonalised together
w, V = np.linalg.eigh(casL + 0.37 * casR)
jl = np.round(np.real(np.diag(V.conj().T @ casL @ V)), 6)
jr = np.round(np.real(np.diag(V.conj().T @ casR @ V)), 6)
pairs = sorted(zip(jl, jr))
check(
    f"B3: Spin(4) Dirac spinor = (1/2,0) + (0,1/2): (casL, casR) = {pairs}",
    pairs == sorted([(0.75, 0.0)] * 2 + [(0.0, 0.75)] * 2),
)

# ---- B4: Spin(7) -> Spin(6)
g7, S7 = spin_gens(7)
check("B4: Spin(7) spinor has 8 components", g7[0].shape[0] == 8)
for a in range(7):
    for b in range(7):
        assert close(g7[a] @ g7[b] + g7[b] @ g7[a], 2 * np.eye(8) * (a == b))
chi6 = np.eye(8, dtype=complex)
for a in range(6):
    chi6 = chi6 @ g7[a]
scale = np.sqrt((chi6 @ chi6)[0, 0])
chi6 = chi6 / scale
check(
    "B4: the chirality of Spin(6) (product of six gammas) commutes with all Spin(6) generators",
    all(close(comm(chi6, S7[(a, b)]), 0) for a, b in itertools.combinations(range(6), 2)),
)
check(
    "B4: its eigenvalues are +1 (4 states) and -1 (4 states)",
    sorted(np.round(np.linalg.eigvalsh((chi6 + chi6.conj().T) / 2), 6)) == [-1.0] * 4 + [1.0] * 4,
)
# Cartan weights
H = [S7[(0, 1)], S7[(2, 3)], S7[(4, 5)]]
Hc = H[0] + np.sqrt(2) * H[1] + np.sqrt(3) * H[2]
w, V = np.linalg.eigh((Hc + Hc.conj().T) / 2)
rows = []
for k in range(8):
    v = V[:, k]
    wt = tuple(np.round([np.real(v.conj() @ h @ v) for h in H], 6))
    ch = np.round(np.real(v.conj() @ chi6 @ v), 6)
    rows.append((ch, wt))
plus = sorted(wt for ch, wt in rows if ch > 0)
minus = sorted(wt for ch, wt in rows if ch < 0)
check(f"B4: Spin(6) weights on chirality +: {plus}", len(plus) == 4)
check(f"B4: Spin(6) weights on chirality -: {minus}", len(minus) == 4)
check(
    "B4: the two 4-dimensional blocks have DIFFERENT weight sets, i.e. 4 and 4bar are inequivalent",
    set(plus) != set(minus),
)
check(
    "B4: weights of 4bar are the negatives of weights of 4 (conjugate representation)",
    set(tuple(-x for x in wt) for wt in plus) == set(minus),
)
expect_caught("B4 control: claim 4 and 4bar have equal weight sets", set(plus) == set(minus))

# ---- independent control added after the skeptic review: P_L is pinned down by [T,K] = 0
PL_sigma3 = (s0 - s3) / 2
T_s3 = [kron(s0, PL_sigma3, 0.5 * SIG[i], I4) for i in range(3)]
check(
    "B1: with P_L = (1 - sigma_3)/2 (a projector that closes into su(2)) T_i do NOT commute with the boosts K_j, so P_L is forced to (1 -+ sigma_1)/2",
    close(PL_sigma3 @ PL_sigma3, PL_sigma3)
    and all(close(comm(T_s3[i], T_s3[j]), 1j * T_s3[k]) for (i, j), k in eps.items())
    and not all(close(comm(T_s3[i], K[j]), 0) for i in range(3) for j in range(3))
    and all(close(comm(T[i], K[j]), 0) for i in range(3) for j in range(3)),
)
expect_caught(
    "control: P_L = (1 - sigma_3)/2 is compatible with the boosts",
    all(close(comm(T_s3[i], K[j]), 0) for i in range(3) for j in range(3)),
)

print("\nFAILS:", FAILS if FAILS else "none")
sys.exit(1 if FAILS else 0)
