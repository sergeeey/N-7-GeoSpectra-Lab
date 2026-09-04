r"""
C152 STEP 8 -- can Step 7's confirmation FAIL? Run before the confirmation is
reported anywhere.

C151 has already produced one false "PREDICTION CONFIRMED" in this exact
place, over a quantity that was identically zero. Step 7 clears that specific
trap (its vacuity gate is first, and max|c| is 1.0-2.7, not 0). This file
clears the OTHER trap: a test that passes for every input is not a test.

FOUR CONTROLS
  N1  a RANDOM almost-complex structure J' (J'^2 = -1) in place of J_NK.
      If c(J'v) = i c(v) holds for an arbitrary J', the identity says nothing
      about J_NK and the confirmation is empty.
  N2  the OTHER five invariant a.c.s. of the flag manifold (sign tuples).
      Sharper than N1: same family, same symmetry class, different J.
  N3  a random REAL-linear map of the same shape as c. Must fail, or the
      criterion is satisfied by generic maps.
  N4  the OLD (C151) sector. Must be vacuous, confirming that the sign
      correction is what made the test live rather than something else.

Run:  python c152_step8_falsifiability.py
"""

import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
S7 = importlib.util.spec_from_file_location("s7", HERE / "c152_step7_c151_rerun.py")
m7 = importlib.util.module_from_spec(S7)
S7.loader.exec_module(m7)

family, c_of, n_pairs = m7.family, m7.c_of, m7.n_pairs
E, spin, T2_M, LAM, I6, I8 = m7.E, m7.spin, m7.T2_M, m7.LAM, m7.I6, m7.I8
np_ = np
rng = np.random.default_rng(818)


def is_c_linear(Jmat, ndraw=6):
    """Does c(J.v) = +-i c(v) hold, entrywise, on random family elements?"""
    devs = []
    for _ in range(ndraw):
        v = family @ rng.normal(size=6)
        cv = c_of(v)
        cJ = c_of((Jmat.T @ v.reshape(6, n_pairs)).reshape(-1))
        n = float(np.max(np.abs(cv)))
        if n < 1e-8:
            return None, None
        devs.append(min(float(np.max(np.abs(cJ - 1j * cv))) / n,
                        float(np.max(np.abs(cJ + 1j * cv))) / n))
    return max(devs) < 1e-8, max(devs)


def acs_from_eps(eps):
    Jm = np.zeros((6, 6))
    for k, e in enumerate(eps):
        Jm[2 * k, 2 * k + 1], Jm[2 * k + 1, 2 * k] = -e, e
    return Jm


print()
print("=" * 78)
print("N2  the 8 invariant almost-complex structures (J_NK is eps=(1,1,1) here,")
print("    because Stage 2a ALREADY aligned J_NK to the standard J_0)")
print("=" * 78)
hold = []
for e1 in (1, -1):
    for e2 in (1, -1):
        for e3 in (1, -1):
            eps = (e1, e2, e3)
            ok, dev = is_c_linear(acs_from_eps(eps))
            hold.append((eps, ok))
            print(f"  eps={eps!s:>14}  C-linear: {ok!s:<5}  max rel. deviation = {dev:.3e}")

n_hold = sum(1 for _, ok in hold if ok)
print(f"\n  C-linear for {n_hold} of 8 invariant a.c.s.")

print()
print("=" * 78)
print("N1  random almost-complex structures (J'^2 = -1, no invariance imposed)")
print("=" * 78)
rand_hold = 0
for t in range(5):
    A = rng.normal(size=(6, 6))
    Q, _ = np.linalg.qr(A - A.T + 1e-9 * np.eye(6))
    S = np.zeros((6, 6))
    for k in range(3):
        S[2 * k, 2 * k + 1], S[2 * k + 1, 2 * k] = -1, 1
    Jr = Q @ S @ Q.T
    assert np.max(np.abs(Jr @ Jr + np.eye(6))) < 1e-8
    ok, dev = is_c_linear(Jr)
    rand_hold += bool(ok)
    print(f"  random J' #{t}:  C-linear: {ok!s:<5}  max rel. deviation = {dev:.3e}")

print()
print("=" * 78)
print("N3  a random REAL-linear map of the same shape as c")
print("=" * 78)
M = rng.normal(size=(9, 6)) + 1j * rng.normal(size=(9, 6))
coeff = np.linalg.pinv(family) @ np.eye(family.shape[0])
J0 = acs_from_eps((1, 1, 1))
fake_hold = 0
for t in range(3):
    Mt = rng.normal(size=(9, 6)) + 1j * rng.normal(size=(9, 6))
    devs = []
    for _ in range(6):
        a = rng.normal(size=6)
        v = family @ a
        aJ = np.linalg.lstsq(family, (J0.T @ v.reshape(6, n_pairs)).reshape(-1), rcond=None)[0]
        cv, cJ = Mt @ a, Mt @ aJ
        n = float(np.max(np.abs(cv)))
        devs.append(min(float(np.max(np.abs(cJ - 1j * cv))) / n,
                        float(np.max(np.abs(cJ + 1j * cv))) / n))
    ok = max(devs) < 1e-8
    fake_hold += bool(ok)
    print(f"  random real-linear map #{t}:  C-linear: {ok!s:<5}  max dev = {max(devs):.3e}")

print()
print("=" * 78)
print("N4  the OLD (C151, wrong-sign) sector -- must be vacuous")
print("=" * 78)

GENS_OLD = [np.kron(spin(T2_M[k]), I6) + np.kron(I8, +T2_M[k]) for k in range(2)]


def sector_old(first_idx):
    bi = [i * 6 + j for i in first_idx for j in range(6)]
    proj = np.zeros((48, len(bi)))
    for col, g in enumerate(bi):
        proj[g, col] = 1
    _, s, vt = np.linalg.svd(np.vstack([proj.T @ g @ proj for g in GENS_OLD]))
    pad = np.concatenate([s, np.zeros(len(bi) - len(s))])
    return proj @ vt.conj().T[:, np.abs(pad) < 1e-8]



R59 = m7.R59
dO, tO = sector_old(R59.ODD_IDX), sector_old(R59.EVEN_IDX)
old_mags = []
for k in range(6):
    T = (family[:, k]).reshape(6, n_pairs)
    lam = {i + 1: m7.row_to_6x6(T[i]) for i in range(6)}
    D = sum(np.kron(E[i] @ spin(lam[i]), I6) + np.kron(E[i], -lam[i]) for i in range(1, 7))
    old_mags.append(float(np.max(np.abs(tO.conj().T @ D @ dO))))
print(f"  max|c| on the OLD sector, 6 basis vectors: {[f'{m:.2e}' for m in old_mags]}")
print(f"  OLD sector is vacuous (all zero): {all(m < 1e-10 for m in old_mags)}")

print()
print("=" * 78)
print("IS STEP 7's CONFIRMATION FALSIFIABLE?")
print("=" * 78)
print(f"  holds for {n_hold}/8 invariant a.c.s.        (if 8/8 -> J is irrelevant)")
print(f"  holds for {rand_hold}/5 random a.c.s.         (if 5/5 -> the test is empty)")
print(f"  holds for {fake_hold}/3 random linear maps    (if >0 -> criterion too weak)")
print()
if rand_hold == 0 and fake_hold == 0 and n_hold < 8:
    print("  -> FALSIFIABLE AND PASSED. The identity fails for random J, for the")
    print("     other invariant a.c.s., and for generic linear maps of the same")
    print("     shape. Step 7's confirmation carries information.")
elif rand_hold == 5 or fake_hold > 0:
    print("  *** NOT A TEST. It passes for arbitrary inputs. Step 7's")
    print("      confirmation is WITHDRAWN. ***")
else:
    print("  -> Mixed. Read the tables; do not summarise.")
