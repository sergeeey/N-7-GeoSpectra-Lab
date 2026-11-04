"""C241 (Q3): hypercharge on the 32 states of the poster's one-generation construction (C239), under the STANDARD left-right definition.

Source for the definition (opened 2026-11-04): L. Di Luzio, 'Pati-Salam Axion', arXiv:2005.00012v3, eq. (2.2): Y = T^3_R + (B-L)/2, with SU(3)_C x U(1)_{B-L} inside SU(4)_PS and fermions Q_L ~ (4,2,1), Q_R ~ (4,1,2).
The poster prints NO hypercharge generator and NO T3R. What is added here by me (and not on the poster):
   T3R = (1/2)(1_2 (x) P_R (x) sigma_3 (x) 1_4), P_R = (1 + sigma_1)/2   (mirror of the poster's T_i with P_L -> P_R)
   (B-L)/2 = 1 (x) 1 (x) 1 (x) diag(1/6, 1/6, 1/6, -1/2)                (B-L = 1/3 on the three colours, -1 on the lepton component)
   Y = T3R + (B-L)/2,   Q = T3L + Y with T3L = T_3 of the poster.
Generators J, K, T, C are exactly those of C239 (poster's printed forms).

Predictions written BEFORE running:
  H1. Q has the standard charges on the 32 states: +2/3 on 12 states (u, both chiralities, 3 colours, 2 spins), -1/3 on 12 (d), 0 on 4 (nu), -1 on 4 (e).
  H2. Y on left-handed states: +1/6 (12 states: Q_L doublet) and -1/2 (4: L_L doublet); on right-handed: +2/3 (6), -1/3 (6), 0 (2), -1 (2).
  H3. Y commutes with J, K, T_i, C_i' (hypercharge commutes with the Lorentz, SU(2)_L and SU(3)_C generators) and Q commutes with T3L, T3R, Y, C.
  H4. The states invariant under SU(3)_C x SU(2)_L with Y = 0 are exactly 2 (spin up/down): the right-handed neutrino; that is the poster's statement 'right-handed neutrino is invariant under SU(3)_C x SU(2)_L x U(1)_Y', checked under the definition above (not on the poster).
  H5. Without the (B-L) term (Y = T3R only) the charges are NOT standard: the (B-L)/2 term is needed.
Self-controls (must be CAUGHT): charge of the up quark = 1/3; Y(nu_R) != 0 claimed; Y = T3R alone reproduces the standard charges.
"""

import itertools
import sys
from collections import Counter
from fractions import Fraction

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
I4 = np.eye(4, dtype=complex)
PL = (s0 - s1) / 2
PR = (s0 + s1) / 2


def kron(*ms):
    out = np.array([[1]], dtype=complex)
    for m in ms:
        out = np.kron(out, m)
    return out


def comm(a, b):
    return a @ b - b @ a


def close(a, b, tol=1e-12):
    return np.allclose(a, b, atol=tol)


J = [kron(0.5 * SIG[i], s0, s0, I4) for i in range(3)]
K = [kron(0.5j * SIG[i], s1, s0, I4) for i in range(3)]
T = [kron(s0, PL, 0.5 * SIG[i], I4) for i in range(3)]
lam = np.zeros((8, 3, 3), dtype=complex)
lam[0][0, 1] = lam[0][1, 0] = 1
lam[1][0, 1], lam[1][1, 0] = -1j, 1j
lam[2][0, 0], lam[2][1, 1] = 1, -1
lam[3][0, 2] = lam[3][2, 0] = 1
lam[4][0, 2], lam[4][2, 0] = -1j, 1j
lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2], lam[6][2, 1] = -1j, 1j
lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
C = []
for a in range(8):
    m = np.zeros((4, 4), dtype=complex)
    m[:3, :3] = lam[a]
    C.append(kron(s0, s0, s0, 0.5 * m))

T3L = T[2]
T3R = kron(s0, PR, 0.5 * s3, I4)
BL2 = kron(s0, s0, s0, np.diag([1 / 6, 1 / 6, 1 / 6, -1 / 2]).astype(complex))
Y = T3R + BL2
Q = T3L + Y

# H3
check("H3: Y commutes with J, K, T_i and C_i'", all(close(comm(Y, g), 0) for g in J + K + T + C))
check(
    "H3: T3R commutes with J, K, T_i, C_i' and with T3L",
    all(close(comm(T3R, g), 0) for g in J + K + T + C + [T3L]),
)
check(
    "H3: Q commutes with T3L, T3R, Y, B-L and the colour generators",
    all(close(comm(Q, g), 0) for g in [T3L, T3R, Y, BL2] + C),
)

# joint diagonalisation of commuting operators: diagonalise a generic combination of commuting ones
G5 = kron(s0, s1, s0, I4)
cas_C = sum(c @ c for c in C)
cas_T = sum(t @ t for t in T)
Hg = Q + 0.31 * Y + 0.17 * T3R + 0.043 * cas_C + 0.0071 * cas_T + 0.0019 * G5 + 0.00063 * J[2]
w, V = np.linalg.eigh((Hg + Hg.conj().T) / 2)


def val(op, v):
    return float(np.real(v.conj() @ op @ v))


states = []
for k in range(32):
    v = V[:, k]
    states.append(
        dict(
            Q=round(val(Q, v), 6),
            Y=round(val(Y, v), 6),
            cC=round(val(cas_C, v), 6),
            cT=round(val(cas_T, v), 6),
            g5=round(val(G5, v), 6),
        )
    )

cntQ = Counter(s["Q"] for s in states)
exp = Counter({round(2 / 3, 6): 12, round(-1 / 3, 6): 12, 0.0: 4, -1.0: 4})
check(
    f"H1: electric charges {dict(cntQ)} = standard {dict(exp)} (u: 12, d: 12, nu: 4, e: 4)",
    cntQ == exp,
)

cntYL = Counter(s["Y"] for s in states if s["g5"] < 0)
cntYR = Counter(s["Y"] for s in states if s["g5"] > 0)
expL = Counter({round(1 / 6, 6): 12, round(-1 / 2, 6): 4})
expR = Counter({round(2 / 3, 6): 6, round(-1 / 3, 6): 6, 0.0: 2, -1.0: 2})
check(f"H2: Y on the g5 = -1 block {dict(cntYL)} = {dict(expL)}", cntYL == expL)
check(f"H2: Y on the g5 = +1 block {dict(cntYR)} = {dict(expR)}", cntYR == expR)
print(
    "   note: which g5 sign is 'left-handed' is fixed by P_L = (1 - sigma_1)/2 on the poster (g5 = sigma_1 on the chirality factor: P_L projects on g5 = -1)."
)

nuR = [s for s in states if abs(s["cC"]) < 1e-6 and abs(s["cT"]) < 1e-6 and abs(s["Y"]) < 1e-6]
check(
    f"H4: number of states with SU(3)_C Casimir 0, SU(2)_L Casimir 0 and Y = 0: {len(nuR)} = 2 (nu_R, two spins)",
    len(nuR) == 2,
)
check(
    "H4: these two states have Q = 0 and sit in the g5 = +1 block (right-handed)",
    all(abs(s["Q"]) < 1e-6 and s["g5"] > 0 for s in nuR),
)
others = [s for s in states if abs(s["cC"]) < 1e-6 and abs(s["cT"]) < 1e-6 and abs(s["Y"]) > 1e-6]
check(
    "H4: the other colourless SU(2)_L-singlets are the right-handed electron states (Y = -1), 2 of them",
    len(others) == 2 and all(abs(s["Y"] + 1) < 1e-6 for s in others),
)

# H5: Y = T3R only
Yb = T3R
Qb = T3L + Yb
wb, Vb = np.linalg.eigh(
    (
        Qb
        + 0.31 * Yb
        + 0.043 * cas_C
        + 0.0071 * cas_T
        + 0.0019 * G5
        + 0.00063 * J[2]
        + 0.17 * T3R
        + 0.0003 * BL2
        + 0.00001 * T3L
    )
)
cb = Counter(round(float(np.real(Vb[:, k].conj() @ Qb @ Vb[:, k])), 6) for k in range(32))
check(f"H5: with Y = T3R alone the charges are {dict(cb)}, not the standard set", cb != exp)
expect_caught("control: Y = T3R alone reproduces the standard charges", cb == exp)
expect_caught(
    "control: the up-quark charge is 1/3 (12 states with Q = 1/3)",
    cntQ.get(round(1 / 3, 6), 0) == 12,
)
# Skeptic review: the former control "Y(nu_R) != 0" was built on a list filtered by |Y| < 1e-6 and could never fire; replaced by a check that documents what H3 does NOT test.
Ynon = T3R + kron(s0, s0, s0, np.diag([1 / 6, 1 / 6, 1 / 6, -5]).astype(complex))
check(
    "H3 weakness: a nonsense Y (lepton value -5 instead of -1/2) commutes with all printed generators too, so H3 carries no evidential weight",
    all(close(comm(Ynon, g), 0) for g in J + K + T + C),
)

print("\nFAILS:", FAILS if FAILS else "none")
sys.exit(1 if FAILS else 0)
