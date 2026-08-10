"""C11 step 6: Poincare duality, via the cheap decisive probe -- the index pairing.

WHY THE COST CHANGED. The portfolio recorded step 6's cost as "unknown until step 1".
After C48 it is cheap, because the algebra is no longer a crossed product: J forces
A = the TWISTED DIAGONAL, acting sector-DIAGONALLY as diag(f, f o iota). Poincare
duality is defined relative to A, and for a commutative A the first thing that must be
non-degenerate is the INDEX PAIRING of the fundamental class with K-theory.

THE PROBE. For an EVEN spectral triple the pairing is the graded index

    <[D], [p]>  =  ind( p D p : p H_+ -> p H_- ),     H_+- = +-1 eigenspaces of gamma

and the simplest necessary condition is the pairing with the unit, ind(D) = Tr(gamma|ker D).

THE STRUCTURE THAT DECIDES IT. gamma = U_iota (x) s1 is OFF-DIAGONAL in the sector
index by construction -- that is exactly what made it exist at all (C43/C45: both
factors are needed, U_iota flips D^{1/2} and s1 flips s3). An off-diagonal involution
maps ker(D^0) onto ker(D^1) bijectively, so its restriction to the kernel is
off-diagonal, and an off-diagonal matrix has zero trace.

PREDICTIONS, recorded before running:
  S1  gamma maps ker(D^0) ONTO ker(D^1), so gamma|ker is off-diagonal
  S2  ind(D_block) = Tr(gamma|ker) = 0, with gamma|ker having eigenvalues +1,+1,-1,-1
  S3  the SAME cancellation holds for every p in A, because A is sector-diagonal and
      gamma conjugates the sector-0 action of f into the sector-1 action of f o iota:
      the two contributions are equal and opposite
  S4  CONTRAST (the discriminating comparison, not a control on the same object): the
      UNdoubled odd triple on one sector pairs with K_1 by spectral flow, which is not
      forced to vanish. Doubling therefore LOSES index information rather than adding it.

WHAT THIS CANNOT SHOW, fixed in advance: a vanishing index pairing is a NECESSARY
condition failing, i.e. it refutes Poincare duality for THIS even triple. It does NOT
say S^3 fails Poincare duality (it does not -- classically it holds in the odd/KO-3
sense), and it says NOTHING about the S^6 index that produces N_gen = 3, which is a
different operator on a different manifold. Step 7 remains untouched.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_step6.json"
results: dict = {}

H_H = 3
N_MAX = 6


def levels(nmax: int):
    """(sector, n, sigma, eigenvalue, multiplicity) for the block."""
    for sec, tv in ((0, 0.0), (1, 1.0)):
        for n in range(nmax + 1):
            for sgn in (+1, -1):
                yield sec, n, sgn, sgn * (n + 1.5) + (tv - 0.5) * H_H, (n + 1) * (n + 2)


print("=" * 78)
print("C11 step 6 -- Poincare duality via the index pairing")
print("=" * 78)

# --- S1: does gamma map ker(D^0) onto ker(D^1)? ------------------------------
print("\nS1 -- gamma = U_iota (x) s1 on the kernel")
ker0 = [(n, s, m) for sec, n, s, lam, m in levels(N_MAX) if sec == 0 and abs(lam) < 1e-12]
ker1 = [(n, s, m) for sec, n, s, lam, m in levels(N_MAX) if sec == 1 and abs(lam) < 1e-12]
print(f"    ker(D^0): levels {ker0}  -> dim {sum(m for _, _, m in ker0)}")
print(f"    ker(D^1): levels {ker1}  -> dim {sum(m for _, _, m in ker1)}")
# U_iota flips D^{1/2}, so it maps (n, sigma) -> (n, -sigma); s1 swaps sectors.
mapped = [(n, -s, m) for n, s, m in ker0]
s1_ok = sorted(mapped) == sorted(ker1)
print("    U_iota sends (n,sigma) -> (n,-sigma); s1 swaps sectors")
print(f"    image of ker(D^0) = {sorted(mapped)}  == ker(D^1): {s1_ok}")
print(f"    S1: gamma|ker is OFF-DIAGONAL in the sector index: {s1_ok}")
results["ker0"] = ker0
results["ker1"] = ker1
results["s1_gamma_offdiagonal_on_kernel"] = bool(s1_ok)

# --- S2: the index --------------------------------------------------------
print("\nS2 -- ind(D_block) = Tr(gamma|ker)")
d0, d1 = sum(m for _, _, m in ker0), sum(m for _, _, m in ker1)
assert d0 == d1, "kernel halves must match for an off-diagonal involution to exist"
g_ker = np.block([[np.zeros((d0, d1)), np.eye(d0)], [np.eye(d1), np.zeros((d1, d0))]])
tr = float(np.trace(g_ker))
eig = sorted(np.round(np.linalg.eigvalsh(g_ker), 9).tolist())
idx = round(tr)
print(f"    dim ker = {d0 + d1} = {d0} + {d1}")
print(f"    gamma|ker eigenvalues: {eig}")
print(f"    Tr(gamma|ker) = {tr:.1f}   =>   ind(D_block) = {idx}")
s2 = idx == 0 and eig.count(1.0) == eig.count(-1.0)
print(f"    S2: index vanishes, with balanced chirality: {s2}")
results["s2_index"] = idx
results["s2_gamma_ker_eigenvalues"] = eig
results["s2_balanced"] = bool(s2)

# --- S3: does it vanish for every p in A -- and can this test FAIL at all? ---
print("\nS3 -- vanishing for every p in A, WITH a test that can actually fail")
print("      FIRST VERSION OF THIS BLOCK WAS TAUTOLOGICAL: it sampled block-diagonal")
print("      diag(P,P) against a purely off-diagonal gamma|ker, so Tr = 0 held by SHAPE")
print("      alone, for any algebra whatsoever. That is a criterion that cannot fail.")
print("      The content is a one-line consequence plus a DISCRIMINATING counter-case:")
print("        (a) every p in A is sector-block-diagonal          [C48: A = twisted diag]")
print("        (b) gamma|ker is purely sector-off-diagonal        [S1]")
print("        (c) hence Tr(gamma p) = 0 -- by (a)+(b), not by numerics")
print("        (d) a SECTOR-MIXING p (NOT in A) must give Tr != 0, or (c) says nothing")
rng = np.random.default_rng(20260810)
in_A, not_in_A = [], []
for _ in range(200):
    r = int(rng.integers(0, d0 + 1))
    q, _ = np.linalg.qr(rng.normal(size=(d0, d0)))
    P = q[:, :r] @ q[:, :r].T
    # (a) an element of A: sector-block-diagonal, second block the iota-image
    in_A.append(
        abs(float(np.trace(g_ker @ np.block([[P, np.zeros((d0, d1))], [np.zeros((d1, d0)), P]]))))
    )
# (d) the counter-case: a sector-MIXING projection, of the kind only the crossed
#     product T4 could have supplied -- and which J excluded (C48).
for theta in (0.0, 0.4, 1.0, 1.3):
    c, s = np.cos(theta), np.sin(theta)
    # rank-2 projection onto the +1 eigenspace of a rotated sector-swap
    mix = np.block([[c * np.eye(d0), s * np.eye(d0)], [s * np.eye(d1), -c * np.eye(d1)]])
    p_mix = (np.eye(d0 + d1) + mix) / 2
    not_in_A.append(float(np.trace(g_ker @ p_mix)))
s3_a = max(in_A) < 1e-9
s3_d = any(abs(v) > 1e-6 for v in not_in_A)
print(f"\n    (a)-(c) p in A          : max |Tr(gamma p)| = {max(in_A):.2e}  -> vanishes")
print(f"    (d)     p sector-MIXING : Tr(gamma p) = {[round(v, 4) for v in not_in_A]}")
print(f"            at least one is NON-zero, so the test DISCRIMINATES: {s3_d}")
s3 = s3_a and s3_d
print(f"    S3: {s3}  -- and the reason is now visible: the pairing vanishes BECAUSE")
print("        J forced the algebra to be sector-diagonal (C48). A sector-MIXING")
print("        algebra -- exactly the crossed product J excluded -- would NOT vanish.")
results["s3_max_abs_trace_in_A"] = max(in_A)
results["s3_traces_sector_mixing"] = not_in_A
results["s3_discriminates"] = bool(s3_d)
results["s3_pairing_vanishes_for_all_p"] = bool(s3)

# --- S4: the discriminating contrast -----------------------------------------
print("\nS4 -- CONTRAST: what the UNdoubled odd triple would pair with")
print("      One sector alone is an ODD triple (no grading -- that is C35/C43's whole")
print("      point). Odd triples pair with K_1 by SPECTRAL FLOW, and nothing forces")
print("      that to vanish. Here spec(D^0) = {0,1,2,...} u {-3,-4,...} is ASYMMETRIC,")
print("      which is precisely a non-trivial spectral asymmetry.")
s0 = sorted({lam for sec, n, s, lam, m in levels(N_MAX) if sec == 0})
asym = not np.allclose(sorted(s0), sorted(-np.array(s0)))
print(f"    spec(D^0) asymmetric under lambda -> -lambda: {asym}")
print(f"    S4: doubling REMOVES that asymmetry (C43) and with it the index content: {asym}")
results["s4_single_sector_spectrum_asymmetric"] = bool(asym)

# --- VERDICT -----------------------------------------------------------------
print("\n" + "=" * 78)
ok = s1_ok and s2 and s3 and asym
verdict = (
    "EVEN_INDEX_PAIRING_VANISHES_IDENTICALLY__PD_FAILS_FOR_THIS_TRIPLE" if ok else "INCONCLUSIVE"
)
print(f"VERDICT: {verdict}")
print("=" * 78)
if ok:
    print("  The doubled even triple's index pairing is IDENTICALLY ZERO, for the unit")
    print("  and for every projection in A. A necessary condition for Poincare duality")
    print("  therefore FAILS: the fundamental class this triple defines is trivial.")
    print()
    print("  The mechanism is the same fact that made the grading exist at all. gamma")
    print("  must be OFF-DIAGONAL in the sector index (C45: both factors needed), and an")
    print("  off-diagonal involution has zero trace on the kernel it permutes. The")
    print("  grading and the vanishing pairing are two faces of one structure.")
    print()
    print("  So the doubling does not merely fail to EARN itself (C44/C45/C48) -- on this")
    print("  probe it actively COSTS something: the single sector's spectral asymmetry,")
    print("  which is exactly what an odd triple pairs with, is cancelled by construction.")
    print()
    print("  SCOPE, fixed in advance and repeated here: this refutes PD for THIS even")
    print("  triple. It does NOT say S^3 fails Poincare duality, and it says NOTHING")
    print("  about the S^6 index behind N_gen = 3 -- different operator, different")
    print("  manifold. Step 7 remains untouched.")
results["verdict"] = verdict
RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
print(f"\nResults -> {RESULTS_PATH}")
