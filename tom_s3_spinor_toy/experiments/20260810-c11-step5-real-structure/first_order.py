"""C11 step 5: the real structure J and the first-order condition.

WHY THIS IS NOW DECISIVE, not decorative. Steps 3+4 found that the block admits a
two-parameter family of self-adjoint, gamma-anticommuting off-diagonal deformations
alpha*(I (x) s2) + beta*(D^{1/2} (x) s1), and that the 4-dim kernel matching C38's
Spin(4) spinor survives at EXACTLY ONE point of it. Its own verdict named the stake:

  "If the first-order condition forbids the off-diagonal terms, the kernel's isolation
   stops being a fragility and becomes a SELECTION."

Step 1's Relaxation Map named the hope in the other direction: V2, "J + first-order
could exclude the SMALL subalgebras and earn the maximal one WITHOUT an axiom of
convenience." Both are tested here, and they are not both going to survive.

THE SETUP. J = J_M (x) j on H = L2(S3,S) (x) C^2_sector, with j = k o conj antilinear
on the sector index. INPUTS from S^3's KO-dimension 3, declared not re-derived:
J_M^2 = -1 and J_M D_M = D_M J_M. The NEW content is entirely in the sector factor.

For a = f (x) m and b = g (x) m', with m'' := k (m')^T k^-1:
  order-zero    [a, J b* J^-1] = 0            <=>  [m, m''] = 0
  first-order   [[D,a], J b* J^-1] = 0        <=>  [[s3,m], m''] = 0  and
                                                   alpha [[s2,m], m''] = 0
(the classical piece [D^{1/2},f] is a bundle endomorphism, so it commutes with
multiplication by g and contributes the SAME condition [m,m''] = 0.)

PREDICTIONS, recorded before running:
  R1  the beta term makes [D,a] UNBOUNDED unless [s1,m] = 0 for every m in A, because
      [beta D^{1/2}(x)s1, f(x)m] contains f D^{1/2} (x) [s1,m]. The bounded-commutator
      axiom -- BLIND to the sectors in step 1 -- becomes SHARP the moment an unbounded
      off-diagonal term is switched on. Prediction: beta = 0 is FORCED.
  R2  order-zero FAILS for the maximal algebra T4, whose sector part is all of M2(C):
      its commutant is only C*I, so no k can work. J EXCLUDES THE MAXIMAL ALGEBRA.
      This is the OPPOSITE of step 1's hope V2 and is recorded as such.
  R3  order-zero HOLDS for T7 (twisted diagonal, sector part span{I,s3}) and T6.
  R4  first-order then FORCES alpha = 0, because [s2,s3] ~ s1 and [s1, +-s3] != 0.
  R5  therefore (alpha,beta) = (0,0) is FORCED by the axioms, and steps 3+4's
      isolation of the 4-dim kernel becomes a SELECTION rather than a fragility.

WHAT THIS CANNOT SHOW. ANSATZ J1: J is assumed to be a simple tensor J_M (x) j. A
general antilinear J on H_M (x) C^2 need not factor, and nothing here rules the
non-factoring ones out. Flagged, not silently assumed.
"""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_step5.json"
results: dict = {}

I2 = np.eye(2, dtype=complex)
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3 = np.array([[-1, 0], [0, 1]], dtype=complex)
BASIS = {"I": I2, "s1": S1, "s2": S2, "s3": S3}

# sector parts of the three admissible algebras from step 1
A_SECTOR = {
    "T4 crossed product": ["I", "s1", "s2", "s3"],
    "T7 twisted diagonal": ["I", "s3"],
    "T6 A+ (x) I": ["I"],
}

print("=" * 78)
print("C11 step 5 -- the real structure J and the first-order condition")
print("=" * 78)

# --- R1: does the beta term destroy boundedness? -----------------------------
print("\nR1 -- [D,a] bounded? The beta term carries f*D^{1/2} (x) [s1, m], unbounded")
print("      unless [s1, m] = 0 for every m in the algebra.")
r1 = {}
for name, syms in A_SECTOR.items():
    bad = [s for s in syms if not np.allclose(S1 @ BASIS[s] - BASIS[s] @ S1, 0)]
    r1[name] = {"elements_not_commuting_with_s1": bad, "beta_forced_zero": bool(bad)}
    print(
        f"    {name:22s} non-commuting with s1: {bad or '(none)'!s:22s}"
        f" beta = 0 forced: {bool(bad)}"
    )
r1_ok = (
    r1["T4 crossed product"]["beta_forced_zero"] and r1["T7 twisted diagonal"]["beta_forced_zero"]
)
print(f"\n    R1: beta = 0 is FORCED for both T4 and T7: {r1_ok}")
print("        The bounded-commutator axiom was BLIND to the sector index in step 1")
print("        (because D^0 - D^1 = -3*Id is bounded) and is SHARP here. Same axiom.")
results["r1"] = r1
results["r1_beta_forced_zero"] = bool(r1_ok)

# --- R2/R3: does an antilinear J with order-zero exist, per algebra? ----------
print("\nR2/R3 -- order-zero: is there k with [m, k m'^T k^-1] = 0 for all m, m' in A?")
# search over a spanning set of invertible k: unit-modulus-diagonal and Pauli-type
KS = {
    "diag(1,1)": I2,
    "diag(1,i)": np.diag([1, 1j]),
    "diag(1,-1)": np.diag([1, -1]),
    "s1": S1,
    "s2": S2,
    "s3": S3,
    "s1+is2": S1 + 1j * S2,
}
order_zero = {}
for name, syms in A_SECTOR.items():
    good = []
    for kname, k in KS.items():
        if abs(np.linalg.det(k)) < 1e-12:
            continue
        ki = np.linalg.inv(k)
        ok = all(
            np.allclose(BASIS[a] @ (k @ BASIS[b].T @ ki) - (k @ BASIS[b].T @ ki) @ BASIS[a], 0)
            for a, b in product(syms, syms)
        )
        if ok:
            good.append(kname)
    order_zero[name] = good
    print(f"    {name:22s} admissible k: {good or 'NONE'}")
r2 = order_zero["T4 crossed product"] == []
r3 = bool(order_zero["T7 twisted diagonal"]) and bool(order_zero["T6 A+ (x) I"])
print(f"\n    R2: order-zero FAILS for the maximal algebra T4: {r2}")
print("        (its sector part is all of M2(C), whose commutant is only C*I --")
print("         a genuine M2 bimodule needs a 4-dim sector space, i.e. ANOTHER doubling)")
print(f"    R3: order-zero HOLDS for T7 and T6: {r3}")
print("        => J EXCLUDES THE MAXIMAL ALGEBRA. This is the OPPOSITE of step 1's")
print("           hope V2 ('first-order could exclude the SMALL subalgebras').")
results["order_zero_admissible_k"] = order_zero
results["r2_J_excludes_maximal"] = bool(r2)
results["r3_J_keeps_small"] = bool(r3)

# --- R4: with A = T7, does first-order force alpha = 0? ----------------------
print("\nR4 -- first-order for T7: does alpha survive? need alpha*[[s2,m], m''] = 0")
syms = A_SECTOR["T7 twisted diagonal"]
alpha_forced = {}
for kname in order_zero["T7 twisted diagonal"]:
    k = KS[kname]
    ki = np.linalg.inv(k)
    viol = []
    for a, b in product(syms, syms):
        mpp = k @ BASIS[b].T @ ki
        inner = S2 @ BASIS[a] - BASIS[a] @ S2
        if not np.allclose(inner @ mpp - mpp @ inner, 0):
            viol.append(f"[[s2,{a}],{b}'']")
    alpha_forced[kname] = viol
    print(
        f"    k = {kname:12s} violating pairs: {viol or '(none)'}  -> alpha = 0 forced: {bool(viol)}"
    )
r4 = all(bool(v) for v in alpha_forced.values())
print(f"\n    R4: alpha = 0 is FORCED for EVERY admissible k: {r4}")
results["r4_alpha_violations"] = alpha_forced
results["r4_alpha_forced_zero"] = bool(r4)

# --- SCOPE BOUNDARY: does the alpha-forcing depend on WHICH algebra? ---------
print("\n    scope -- is alpha = 0 forced for the SMALLEST algebra T6 as well?")
t6 = A_SECTOR["T6 A+ (x) I"]
t6_viol = []
for kname in order_zero["T6 A+ (x) I"]:
    k, ki = KS[kname], np.linalg.inv(KS[kname])
    for a, b in product(t6, t6):
        mpp = k @ BASIS[b].T @ ki
        inner = S2 @ BASIS[a] - BASIS[a] @ S2
        if not np.allclose(inner @ mpp - mpp @ inner, 0):
            t6_viol.append(f"{kname}:[[s2,{a}],{b}'']")
t6_forces = bool(t6_viol)
print(f"    T6 violating pairs: {t6_viol or '(none)'}  -> alpha = 0 forced: {t6_forces}")
print("    => NO. alpha survives for T6, whose sector part is just {I}. The forcing")
print("       of alpha needs the algebra to be at least the TWISTED DIAGONAL, i.e. to")
print("       contain a genuinely S^3-worth of functions. Recorded as a scope limit,")
print("       not buried: T6 is the degenerate case where only iota-EVEN functions act")
print("       and the 'geometry' is no longer S^3.")
results["scope_alpha_forced_for_T6"] = t6_forces

# --- also check the s3 part of first-order is satisfied (else T7 dies too) ----
print("\n    sanity: the UNdeformed first-order condition [[s3,m], m''] = 0 must HOLD")
sane = {}
for kname in order_zero["T7 twisted diagonal"]:
    k, ki = KS[kname], np.linalg.inv(KS[kname])
    ok = all(
        np.allclose(
            (S3 @ BASIS[a] - BASIS[a] @ S3) @ (k @ BASIS[b].T @ ki)
            - (k @ BASIS[b].T @ ki) @ (S3 @ BASIS[a] - BASIS[a] @ S3),
            0,
        )
        for a, b in product(syms, syms)
    )
    sane[kname] = ok
    print(f"    k = {kname:12s} undeformed first-order holds: {ok}")
sane_ok = all(sane.values())
print(f"    => the test discriminates: it kills alpha but NOT the undeformed triple: {sane_ok}")
results["undeformed_first_order_holds"] = sane

# --- sign tuple of the resulting J, honestly reported ------------------------
print("\nSIGN TUPLE -- J^2, JD vs DJ, J gamma vs gamma J, in the SECTOR factor")
print("  inputs from S^3 KO-dim 3, declared not re-derived: J_M^2 = -1, J_M D_M = D_M J_M")
tuples = {}
for kname in order_zero["T7 twisted diagonal"]:
    k = KS[kname]
    j_sq = k @ k.conj()  # (k conj)^2 = k conj(k)
    e_j = "+1" if np.allclose(j_sq, I2) else ("-1" if np.allclose(j_sq, -I2) else "other")
    # j s3 = eps3 s3 j  <=>  k conj(s3) = eps3 s3 k ; s3 real
    e_d = "+1" if np.allclose(k @ S3, S3 @ k) else ("-1" if np.allclose(k @ S3, -S3 @ k) else "?")
    # gamma's sector factor is s1 (real)
    e_g = "+1" if np.allclose(k @ S1, S1 @ k) else ("-1" if np.allclose(k @ S1, -S1 @ k) else "?")
    total_j = "-1" if e_j == "+1" else "+1"  # times J_M^2 = -1
    tuples[kname] = {"j^2": e_j, "J^2_total": total_j, "eps_D_sector": e_d, "eps_gamma_sector": e_g}
    print(
        f"    k = {kname:12s} j^2 = {e_j:5s} J^2 = {total_j:3s} (x)J_M^2   "
        f"eps_D(sector) = {e_d:3s}  eps_gamma(sector) = {e_g}"
    )
print("  NOT a KO-dimension claim: only the sector-factor signs are computed here, and")
print("  combining them with S^3's own tuple is exactly the step C36 showed is easy to")
print("  get wrong. Left OPEN rather than asserted.")
results["sign_tuples_sector_only"] = tuples

# --- VERDICT -----------------------------------------------------------------
print("\n" + "=" * 78)
ok = r1_ok and r2 and r3 and r4 and sane_ok
verdict = "AXIOMS_FORCE_ALPHA_BETA_ZERO__BUT_J_KILLS_THE_MAXIMAL_ALGEBRA" if ok else "INCONCLUSIVE"
print(f"VERDICT: {verdict}")
print("=" * 78)
if ok:
    print("  TWO results, pulling in opposite directions, both recorded.")
    print()
    print("  1. THE DEFORMATION IS KILLED. beta = 0 by boundedness, alpha = 0 by")
    print("     first-order. So (alpha,beta) = (0,0) is FORCED, and steps 3+4's")
    print("     isolation of the 4-dim kernel is a SELECTION, not a fragility --")
    print("     exactly the branch that file named in advance as the favourable one.")
    print()
    print("  2. J EXCLUDES THE MAXIMAL ALGEBRA, not the small ones. Step 1's hope V2")
    print("     was that first-order would kill the subalgebras and earn the crossed")
    print("     product without an axiom of convenience. The opposite happened: the")
    print("     crossed product's sector part is all of M2(C), whose commutant is C*I,")
    print("     so order-zero has no solution. What survives is the TWISTED DIAGONAL,")
    print("     which acts sector-DIAGONALLY.")
    print()
    print("  CONSEQUENCE, stated plainly: with J imposed, the algebra no longer mixes")
    print("  the sectors at all. So the algebra cannot force the doubling in any form.")
    print("  The doubling rests on wanting a GRADING and nothing else -- and C44 already")
    print("  showed a grading is available for EVERY mirror pair. The t=0/t=1 doubling")
    print("  remains UNEARNED, and now provably so from three independent directions.")
results["verdict"] = verdict
RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
print(f"\nResults -> {RESULTS_PATH}")
