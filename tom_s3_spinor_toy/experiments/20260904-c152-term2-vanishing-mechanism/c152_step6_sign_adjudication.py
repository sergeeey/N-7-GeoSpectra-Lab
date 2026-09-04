r"""
C152 STEP 6 -- adjudicate the skeptic's KILL by an INTERNAL, sign-sensitive
test that needs no external number.

THE SKEPTIC'S CLAIM (FL Step 8a, context-blind, code-only, DERIVED not run)
  c151_stage2_construct.py:205 builds the T^2 generator on Sigma (x) W as
      kron(spin_lift(T2_M), I) + kron(I, +T2_M)
  while the S^6 side (C139/C145) uses
      kron(spin_lift(ADNU),  I) + kron(I, -bivec(ADNU))
  Since the scripts' own gate measures [spin_lift(L), e_j] = -(L e_j), i.e.
  spin_lift(L) generates the vector action MINUS L, the consistent pairing is
  (spin_lift(L), -L). If so, SU(3)/T^2's invariant sector is built from an
  inconsistent action, and C151's "c == 0" -- not merely C152 -- is an
  artifact of a weight-mismatched sector.

THE ADJUDICATOR
  The twisted Dirac operator D is, by construction, equivariant for the TRUE
  group action. So the correct generator G is the one satisfying [D, G] = 0.
  This is internal, needs no calibration constant, and cannot be satisfied by
  both signs (T2_M is nonzero). It decides the question outright.

  Secondary check: the connection term on W already uses SPIN_VS_VEC*LAM.
  Whatever sign the adjudicator picks for the sector MUST agree with it, or
  the pipeline is internally inconsistent regardless of which is "right".

Run:  python c152_step6_sign_adjudication.py
"""

import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
S2A_PATH = HERE.parent / "20260904-c151-stage0-su3t2-scoping" / "c151_stage2_construct.py"
R59_PATH = (
    HERE.parent / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


S2A = load_module("c151_stage2_construct", S2A_PATH)
R59 = load_module("round59_route_a_independent", R59_PATH)
E, spin = S2A.E, S2A.spin_lift_np
LAM = {i: S2A.NOMIZU_LC[i].astype(complex) for i in range(1, 7)}
T2_M = S2A.T2_M
I6, I8 = np.eye(6), np.eye(8)

D_full = sum(
    np.kron(E[i] @ spin(LAM[i]), I6) + np.kron(E[i], -LAM[i]) for i in range(1, 7)
)

print("=" * 78)
print("ADJUDICATOR: which sector generator does D actually commute with?")
print("=" * 78)
res = {}
for sgn in (+1, -1):
    worst = 0.0
    for k in range(2):
        G = np.kron(spin(T2_M[k]), I6) + np.kron(I8, sgn * T2_M[k])
        worst = max(worst, float(np.max(np.abs(D_full @ G - G @ D_full))))
    res[sgn] = worst
    tag = "C151's choice" if sgn == +1 else "skeptic's proposal"
    print(f"  G with {sgn:+d}*T2_M in the W slot ({tag:<18}) : max|[D,G]| = {worst:.3e}")

winner = min(res, key=lambda s: res[s])
print()
print(f"  -> D is equivariant for the {winner:+d} convention "
      f"({res[winner]:.2e} vs {res[-winner]:.2e})")

# Cross-check the same question on S^6, where an external calibration exists.
E6_sym = R59.build_clifford(conj=False)
E6 = {i: np.array(E6_sym[i].evalf(), dtype=complex) for i in range(1, 7)}


def spin6(L):
    out = np.zeros((8, 8), dtype=complex)
    for a in range(6):
        for b in range(a + 1, 6):
            if abs(L[a, b]) > 1e-14:
                out += L[a, b] * 0.5 * (E6[a + 1] @ E6[b + 1])
    return out


def bivec(terms):
    m = np.zeros((6, 6), dtype=complex)
    for c, a, b in terms:
        m[a - 1, b - 1] += float(c)
        m[b - 1, a - 1] -= float(c)
    return m


LAM6 = {i: bivec(R59.NOMIZU[i]) for i in range(1, 7)}
AD6 = {a: bivec(R59.ADNU[a]) for a in range(1, 9)}
D6 = sum(np.kron(E6[i] @ spin6(LAM6[i]), I6) + np.kron(E6[i], -LAM6[i]) for i in range(1, 7))
print()
print("  same adjudication on S^6 (where C145's 1.154701 independently fixes it):")
for sgn in (+1, -1):
    worst = max(
        float(np.max(np.abs(D6 @ (g := np.kron(spin6(AD6[a]), I6) + np.kron(I8, sgn * AD6[a]))
                             - g @ D6)))
        for a in range(1, 9)
    )
    tag = "= C139/C145's choice" if sgn == -1 else ""
    print(f"    G with {sgn:+d}*ADNU  : max|[D,G]| = {worst:.3e}  {tag}")

# ---------------------------------------------------------------------------
# Now REBUILD the SU(3)/T^2 sector with the adjudicated sign and recompute.
# ---------------------------------------------------------------------------
EVEN, ODD = R59.EVEN_IDX, R59.ODD_IDX


def sector(first_idx, sgn):
    gens = [np.kron(spin(T2_M[k]), I6) + np.kron(I8, sgn * T2_M[k]) for k in range(2)]
    bi = [i * 6 + j for i in first_idx for j in range(6)]
    proj = np.zeros((48, len(bi)))
    for col, g in enumerate(bi):
        proj[g, col] = 1
    _, s, vt = np.linalg.svd(np.vstack([proj.T @ g @ proj for g in gens]))
    pad = np.concatenate([s, np.zeros(len(bi) - len(s))])
    return proj @ vt.conj().T[:, np.abs(pad) < 1e-8]


print()
print("=" * 78)
print("CONSEQUENCE FOR C151 AND C152")
print("=" * 78)
for sgn in (+1, -1):
    d, t = sector(ODD, sgn), sector(EVEN, sgn)
    t1 = float(np.max(np.abs(t.conj().T @ sum(
        np.kron(E[i] @ spin(LAM[i]), I6) for i in range(1, 7)) @ d)))
    t2 = float(np.max(np.abs(t.conj().T @ sum(
        np.kron(E[i], -LAM[i]) for i in range(1, 7)) @ d)))
    tag = "C151's" if sgn == +1 else "skeptic's"
    print(f"  {tag:<10} sector (sgn={sgn:+d}): dims ({d.shape[1]},{t.shape[1]})  "
          f"max|Term1| = {t1:.3e}  max|Term2| = {t2:.3e}")

print()
print("  VERDICT:")
if res[+1] < 1e-10 and res[-1] > 1e-10:
    print("    D commutes with C151's +T2_M generator. The skeptic's KILL is")
    print("    REFUTED: the two spaces differ in how the generator is STORED")
    print("    (bivector on S^6, vector action on SU(3)/T^2), not in convention.")
elif res[-1] < 1e-10 and res[+1] > 1e-10:
    print("    *** D does NOT commute with C151's generator. THE SKEPTIC IS RIGHT. ***")
    print("    C151's invariant sector is built from an inconsistent action, so")
    print("    C151's c == 0 AND every C152 conclusion resting on that sector")
    print("    must be withdrawn, not merely weakened.")
else:
    print("    Neither or both -- do not summarise, read the numbers above.")
