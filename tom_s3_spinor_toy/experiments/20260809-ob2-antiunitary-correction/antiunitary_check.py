"""OB2 -- C30's "internal Z2 exchange symmetry" is orbit equivalence, and the
real symmetry is ANTIUNITARY.

An external red-team audit (2026-08-09) made two claims about C30:

  (a) C30 established only that for EACH rank-one projector T(n) there exists
      SOME unitary U_n with U_n T(n) U_n^-1 = 1-T(n). That is pointwise ORBIT
      EQUIVALENCE, not a symmetry. A symmetry needs ONE fixed operator working
      for all T simultaneously.
  (b) No such single unitary exists: T(n) -> 1-T(n) = T(-n) is the antipodal
      map n -> -n on the Bloch sphere, i.e. R = -I_3 with det = -1, which is
      not in SO(3) -- and unitary conjugation of Pauli matrices only ever
      induces proper rotations. But the ANTIUNITARY Theta = i*sigma_2*K does
      it globally, with Theta^2 = -I.

Both are checked here rather than accepted, per audit-verification-gate.md.

If (b) holds it is not a demotion but an UPGRADE: PARENT_ACTION_GATE.md's OB2
checklist lists "real structure J" as NOT ATTEMPTED, and C30 separately
recorded that its naive grading candidate FAILED {gamma,D}=0. An antiunitary
Theta with Theta^2 = -1 is exactly the object that checklist field asks for,
and it explains the grading failure instead of leaving it unexplained.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_antiunitary.json"

I2 = np.eye(2, dtype=complex)
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
results: dict = {}


def T(n):
    return (I2 + n[0] * s1 + n[1] * s2 + n[2] * s3) / 2


rng = np.random.default_rng(17)
pts = []
for _ in range(8):
    v = rng.normal(size=3)
    pts.append(v / np.linalg.norm(v))

print("=" * 74)
print("OB2: is C30's Z2 a symmetry, or only pointwise orbit equivalence?")
print("=" * 74)

# --- claim (a): reproduce C30's own pointwise result -------------------------
print("\nSTEP 1: reproduce C30 -- for EACH n, does SOME unitary map T(n)->1-T(n)?")
pointwise_ok = True
for n in pts:
    ref = np.array([0.0, 0.0, 1.0]) if abs(n[2]) < 0.9 else np.array([1.0, 0.0, 0.0])
    m = np.cross(n, ref)
    m /= np.linalg.norm(m)
    S = m[0] * s1 + m[1] * s2 + m[2] * s3
    if not np.allclose(S @ T(n) @ np.linalg.inv(S), I2 - T(n), atol=1e-10):
        pointwise_ok = False
print(f"  per-point unitary exists at all {len(pts)} points: {pointwise_ok}")
print("  (this is C30's result, and it is correct -- note S depends on n)")
results["step1_pointwise_unitary_exists"] = bool(pointwise_ok)

# --- claim (b1): is there ONE unitary that works for all n? -------------------
print("\nSTEP 2: is there a SINGLE unitary U working for ALL n simultaneously?")
print("  (a) exhaustive over the factorized Pauli set C30 itself searched")
found_fixed = []
for coeffs in itertools.product([0, 1, -1, 1j, -1j], repeat=4):
    if all(c == 0 for c in coeffs):
        continue
    U = coeffs[0] * I2 + coeffs[1] * s1 + coeffs[2] * s2 + coeffs[3] * s3
    if abs(np.linalg.det(U)) < 1e-12:
        continue
    if all(np.allclose(U @ T(n) @ np.linalg.inv(U), I2 - T(n), atol=1e-9) for n in pts):
        found_fixed.append(coeffs)
print(f"      candidates found: {len(found_fixed)}")

print("  (b) random search over general 2x2 unitaries")
rand_found = None
for _ in range(40000):
    H = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    u, _, vh = np.linalg.svd(H)
    U = u @ vh
    if all(np.allclose(U @ T(n) @ U.conj().T, I2 - T(n), atol=1e-8) for n in pts):
        rand_found = U
        break
print(f"      found: {rand_found is not None}")
single_unitary_exists = bool(found_fixed) or (rand_found is not None)
print(f"\n  SINGLE global unitary exists: {single_unitary_exists}")
results["step2_single_global_unitary_exists"] = single_unitary_exists

# --- claim (b2): WHY not -- the determinant obstruction ----------------------
print("\nSTEP 3: the audit's reason -- unitary conjugation induces SO(3), and")
print("        n -> -n is det = -1, hence NOT reachable.")
det_antipodal = np.linalg.det(-np.eye(3))
print(f"  det(-I_3) = {det_antipodal:+.0f}   in SO(3) (det must be +1): {det_antipodal > 0}")
results["step3_antipodal_det"] = float(det_antipodal)
results["step3_antipodal_in_SO3"] = bool(det_antipodal > 0)

# --- the antiunitary that DOES work -----------------------------------------
print("\nSTEP 4: the antiunitary Theta = i*sigma_2*K (K = complex conjugation)")
Th = 1j * s2  # linear part; the K is applied explicitly below
theta_ok = True
for n in pts:
    lhs = Th @ np.conj(T(n)) @ np.linalg.inv(Th)
    if not np.allclose(lhs, I2 - T(n), atol=1e-12):
        theta_ok = False
print(f"  Theta T(n) Theta^-1 = 1 - T(n) at ALL {len(pts)} points: {theta_ok}")
Th2 = Th @ np.conj(Th)
theta_sq_minus = bool(np.allclose(Th2, -I2))
print(f"  Theta^2 = {np.round(np.real(Th2), 10).tolist()}  -> equals -I: {theta_sq_minus}")
print("  => ONE fixed operator, no n-dependence. This is the genuine symmetry.")
results["step4_theta_works_globally"] = bool(theta_ok)
results["step4_theta_squared_is_minus_I"] = theta_sq_minus

# --- also check Theta flips ALL three Paulis (the structural reason) ---------
flips_all = all(np.allclose(Th @ np.conj(s) @ np.linalg.inv(Th), -s) for s in (s1, s2, s3))
print(f"\n  structural reason: Theta sigma_i Theta^-1 = -sigma_i for all i: {flips_all}")
print("  (that is exactly what sends n.sigma -> -n.sigma, hence T -> 1-T)")
results["step4_theta_flips_all_paulis"] = bool(flips_all)

# --- NEGATIVE CONTROL: can this framework tell a working Theta from a broken one?
print("\nSTEP 5: NEGATIVE CONTROL -- does a WRONG antiunitary get rejected?")
bad = 1j * s1  # flips only sigma_2,sigma_3 under conjugation+conj, not all three
bad_ok = all(
    np.allclose(bad @ np.conj(T(n)) @ np.linalg.inv(bad), I2 - T(n), atol=1e-10) for n in pts
)
print(f"  wrong candidate (i*sigma_1) satisfies the relation: {bad_ok}  (must be False)")
control_ok = not bad_ok
print(f"  NEGATIVE CONTROL PASSES: {control_ok}")
results["step5_wrong_antiunitary_rejected"] = bool(control_ok)

# --- topological remark, checked concretely ---------------------------------
print("\nSTEP 6: the audit's topology point -- can the per-point axis be chosen")
print("        continuously over the whole sphere?")
print("  The per-point unitary needs an axis m PERPENDICULAR to n, chosen for")
print("  every n in S^2. That is a nonvanishing tangent vector field on S^2,")
print("  which the hairy-ball theorem forbids. The construction in C30 used")
print("  cross(n, ref) with a ref chosen by a CASE SPLIT on |n_z| < 0.9 --")
print("  i.e. it silently patched two charts, which is exactly what a global")
print("  obstruction looks like when you do not name it.")
ref_switches = sum(1 for n in pts if abs(n[2]) >= 0.9)
print(f"  (of {len(pts)} sample points, {ref_switches} would have used the OTHER chart)")
results["step6_construction_used_a_case_split"] = True

verdict = (
    pointwise_ok and (not single_unitary_exists) and theta_ok and theta_sq_minus and control_ok
)
print("\n" + "=" * 74)
print(
    f"VERDICT: {'C30_DEMOTED_TO_ORBIT_EQUIVALENCE__THETA_IS_THE_SYMMETRY' if verdict else 'INCONCLUSIVE'}"
)
print("=" * 74)
if verdict:
    print("C30 established pointwise ORBIT EQUIVALENCE, not an internal symmetry.")
    print("No single unitary can do it (det obstruction, confirmed). The genuine")
    print("global operator is ANTIUNITARY, Theta = i*sigma_2*K, with Theta^2 = -I.")
    print("This is an UPGRADE, not just a demotion: PARENT_ACTION_GATE's 'real")
    print("structure J' field for OB2 was NOT ATTEMPTED, and Theta is exactly that")
    print("object -- and its Theta^2 = -1 also explains why C30's naive LINEAR")
    print("grading candidate failed {gamma,D}=0.")
results["verdict"] = (
    "C30_DEMOTED_TO_ORBIT_EQUIVALENCE__THETA_IS_THE_SYMMETRY" if verdict else "INCONCLUSIVE"
)

RESULTS_PATH.write_text(json.dumps(results, indent=2))
print(f"\nResults -> {RESULTS_PATH}")
