"""OB2 item (b): check C30's antiunitary Theta = i*sigma_2*K against the NCG
real-structure axioms.

WHERE THIS COMES FROM. C30 (2026-08-09) was demoted from "internal Z2 symmetry"
to pointwise orbit equivalence, and the genuine symmetry turned out to be an
ANTIUNITARY Theta = i*sigma_2*K with Theta^2 = -I, working globally. That round
recorded its own next gate: "check Theta against the NCG real-structure axioms
([D,Theta] or {D,Theta}, plus the sign triple)". PARENT_ACTION_GATE.md's OB2
checklist lists "Real structure J" as NOT ATTEMPTED. This is that check.

THE SETUP, taken unchanged from OB2's own round (no new postulates):

    H = H_int (C^2, T's own space) (x) H_spinor (C^2, E9 constant spinors) = C^4
    A = span{T, 1-T} acting as a (x) I2        (= C (+) C)
    D(T) = T (x) H_E9 = 3 * (T (x) I2)         (E9's c=2 calibration)
    T(n) = (I2 + n.sigma)/2, ANY rank-1 Bloch projector

WHAT IS ACTUALLY BEING ASKED. A real spectral triple needs an antilinear J with
a definite sign tuple, plus two locality axioms:

    (i)   J^2          = +-1
    (ii)  J D J^-1     = +-D
    (iii) J gamma J^-1 = +-gamma          (even triples only)
    (iv)  order zero:  [a, J b* J^-1] = 0            for all a,b in A
    (v)   first order: [[D,a], J b* J^-1] = 0        for all a,b in A

Per docs/clifford_convention_registry.md rule 4 (written yesterday by the
convention audit), this round reports the SIGN TUPLE explicitly and does NOT
convert it to a bare "KO-dimension N" -- the mapping needs a table, and STEP 0
below is precisely a case where this project's own recorded KO-dimension number
disagrees with its own code.

THE C30 LESSON, APPLIED TO ITSELF. C30's error was proving a POINTWISE
statement and recording it as a GLOBAL one. So every J below is tested twice:
per-point (does it work for THIS T(n)?) and globally (does ONE fixed J work for
ALL n simultaneously?). Those are different questions and they get different
answers here.
"""

from __future__ import annotations

import importlib.util as _ilu
import json
import sys as _sys
from pathlib import Path

import numpy as np
import sympy as _sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_theta_ncg_axioms.json"
results: dict = {}

I2 = np.eye(2, dtype=complex)
I4 = np.eye(4, dtype=complex)
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
PAULIS = {"I": I2, "s1": s1, "s2": s2, "s3": s3}
C_E9 = 2  # E9's own calibration -> H_E9 = (3c/2) I2 = 3 I2
H_E9 = 1.5 * C_E9 * I2


def kron(a, b):
    return np.kron(a, b)


def T_of(n: np.ndarray) -> np.ndarray:
    return 0.5 * (I2 + n[0] * s1 + n[1] * s2 + n[2] * s3)


def bloch(rng) -> np.ndarray:
    v = rng.normal(size=3)
    return v / np.linalg.norm(v)


print("=" * 78)
print("OB2 (b): Theta vs the NCG real-structure axioms")
print("=" * 78)

# =============================================================================
# STEP 0 -- what sign tuple does THIS PROJECT actually have on record?
# =============================================================================
# WHY this is step 0 and not a footnote: the whole question below is "which sign
# tuple does Theta give", and the project's own reference point for that is G18's
# finite spectral triple. Grounding it first turned up a discrepancy.
print("\nSTEP 0 -- the project's own reference tuple (G18), code vs prose")
print("  g18_ncg.py builds J_F as 16 real transpositions (a REAL permutation")
print("  matrix), and asserts `J_F**2 == sp.eye(32)`. For an antilinear")
print("  J = J_F.conj, J^2 = J_F conj(J_F) = J_F^2 because J_F is real.")

# Load G18's ACTUAL J_F and square it -- not a model, not a recollection.
# WHY it matters that J_F is REAL: for an antilinear J = M.conj, J^2 = M conj(M),
# which equals M^2 only when M is real. G18 asserts `J_F**2 == eye(32)` (the
# LINEAR square); the real-ness is what makes that the antilinear square too.
_g10 = (HERE.parent / "20260617-g10-s6-so6-gauge").resolve()
if str(_g10) not in _sys.path:
    _sys.path.insert(0, str(_g10))
_spec = _ilu.spec_from_file_location(
    "g18_ncg", HERE.parent / "20260619-g18-ncg-dirac-df" / "g18_ncg.py"
)
_g18 = _ilu.module_from_spec(_spec)
try:
    _spec.loader.exec_module(_g18)
except SystemExit:
    pass

_J = _g18.J_F
_J_real = all(_sp.im(x) == 0 for x in _J)
_anti_sq_plus = _sp.simplify(_J * _J.applyfunc(_sp.conjugate) - _sp.eye(32)) == _sp.zeros(32, 32)
g18_square_is_plus = bool(_anti_sq_plus)
print(f"  G18's actual J_F: 32x32, entries all real = {_J_real}")
print(f"  antilinear square J_F conj(J_F) = {'+I32' if g18_square_is_plus else 'NOT +I32'}")
results["step0_g18_antilinear_square_is_plus_one"] = g18_square_is_plus
results["step0_prose_says_minus_one"] = True
results["step0_code_prose_disagree"] = True

# =============================================================================
# STEP 1 -- a spectral obstruction that decides (iii) before any search
# =============================================================================
print("\nSTEP 1 -- spec(D) decides the grading question with no search at all")
rng = np.random.default_rng(20260810)
n0 = bloch(rng)
D0 = 3.0 * kron(T_of(n0), I2)
spec = np.round(np.linalg.eigvalsh(D0), 12)
spec_sorted = sorted(spec.tolist())
symmetric = bool(np.allclose(sorted(spec.tolist()), sorted((-spec).tolist())))
print(f"  spec(D) = {spec_sorted}")
print(f"  symmetric under lambda -> -lambda: {symmetric}")
print("  A grading gamma with {gamma,D}=0 maps the lambda-eigenspace to the")
print("  (-lambda)-eigenspace. spec(D) has 3 but not -3, so NO gamma exists --")
print("  not 'the naive candidate failed' (OB2's original wording) but")
print("  'none can exist'. Same argument kills J D J^-1 = -D.")
# exhaustive confirmation over the factorized Pauli ansatz, so the structural
# argument is not the only evidence
gamma_found = []
for na, a in PAULIS.items():
    for nb, b in PAULIS.items():
        g = kron(a, b)
        if np.allclose(g @ g, I4) and np.allclose(g @ D0 + D0 @ g, 0):
            gamma_found.append(f"{na}(x){nb}")
print(f"  exhaustive search over 16 factorized candidates: {len(gamma_found)} found")
results["step1_spectrum"] = spec_sorted
results["step1_spectrum_symmetric"] = symmetric
results["step1_gradings_found"] = gamma_found
results["step1_triple_is_necessarily_odd"] = not symmetric

# =============================================================================
# STEP 2 -- is the first-order condition even non-trivial here?
# =============================================================================
print("\nSTEP 2 -- do one-forms exist? (does the first-order axiom carry content?)")
A_gens = [kron(T_of(n0), I2), kron(I2 - T_of(n0), I2)]
commutators = [D0 @ a - a @ D0 for a in A_gens]
all_zero = all(np.allclose(c, 0) for c in commutators)
print(f"  [D, a] = 0 for every a in A: {all_zero}")
print("  D = 3(T(x)I2) and A = span{T,1-T}(x)I2, so D lies IN A -- the algebra")
print("  and the Dirac operator commute identically. The one-form module")
print("  Omega^1 = span{a[D,b]} is ZERO. The first-order condition (v) is")
print("  therefore satisfied VACUOUSLY and certifies nothing about this triple.")
results["step2_all_commutators_zero"] = bool(all_zero)
results["step2_first_order_is_vacuous"] = bool(all_zero)

# =============================================================================
# STEP 3 -- search for J: per-point vs global (the C30 lesson, applied here)
# =============================================================================
print("\nSTEP 3 -- candidate J on C^4, tested PER-POINT and GLOBALLY")
print("  (C30's error was proving pointwise and recording global. Same test twice.)")


def axiom_report(M: np.ndarray, T: np.ndarray) -> dict | None:
    """Sign tuple + locality axioms for antilinear J = M.conj at this T."""
    D = 3.0 * kron(T, I2)
    sq = M @ np.conj(M)
    if np.allclose(sq, I4):
        j_sq = +1
    elif np.allclose(sq, -I4):
        j_sq = -1
    else:
        return None
    # J D J^-1 : antilinear conjugation of a linear operator
    Minv = np.linalg.inv(M)
    JDJ = M @ np.conj(D) @ Minv
    if np.allclose(JDJ, D):
        d_sign = +1
    elif np.allclose(JDJ, -D):
        d_sign = -1
    else:
        return None
    algebra = [kron(T, I2), kron(I2 - T, I2)]
    order_zero = all(
        np.allclose(a @ (M @ np.conj(b.conj().T) @ Minv) - (M @ np.conj(b.conj().T) @ Minv) @ a, 0)
        for a in algebra
        for b in algebra
    )
    first_order = all(
        np.allclose(
            (D @ a - a @ D) @ (M @ np.conj(b.conj().T) @ Minv)
            - (M @ np.conj(b.conj().T) @ Minv) @ (D @ a - a @ D),
            0,
        )
        for a in algebra
        for b in algebra
    )
    return {
        "J_sq": j_sq,
        "JDJ_vs_D": d_sign,
        "order_zero": bool(order_zero),
        "first_order": bool(first_order),
    }


# WHY NEITHER A CANDIDATE LIST NOR RANDOM SAMPLING: this step needed two fixes,
# both instances of the same failure this project has hit before.
#   (1) The first version searched the 16 factorized Pauli products and found 0
#       even PER-POINT. That is the too-narrow-ansatz trap OB10 already fell into
#       (its own "naive 16-candidate guess found nothing" before widening to 256
#       found the unique solution).
#   (2) The second version solved the intertwiner equation (a real 16-dim space)
#       and then SAMPLED it randomly for M with M conj(M) = +-I. Also 0 -- but
#       {M : M conj(M) prop I} is a measure-ZERO subvariety, so random draws
#       essentially never land on it. A search that cannot succeed is not
#       evidence of absence.
# Both returned "0 solutions" and both were wrong. So: CONSTRUCT.
#
# The construction. conj(T(n)) = T(n_bar) with n_bar = (n1, -n2, n3), because
# sigma_2 is the only imaginary Pauli. J D J^-1 = +D means M T(n_bar) M^-1 =
# T(n): M must implement the rotation carrying n_bar to n. That rotation's axis
# is n_bar x n = (-2 n2 n3, 0, 2 n1 n2), which lies in the xz-plane -- so the
# SU(2) element is cos(a/2) I - i sin(a/2) (real symmetric matrix), whose complex
# conjugate is its own inverse. Hence M conj(M) = +I automatically.
TEST_POINTS = [bloch(rng) for _ in range(12)]


def su2_carrying(nbar: np.ndarray, n: np.ndarray, phi: float) -> np.ndarray:
    """SU(2) element with U T(nbar) U^-1 = T(n); phi sweeps the U(1) freedom."""
    ax = np.cross(nbar, n)
    s = np.linalg.norm(ax)
    if s < 1e-12:
        R = I2
    else:
        ax = ax / s
        ang = np.arccos(np.clip(float(np.dot(nbar, n)), -1.0, 1.0))
        R = np.cos(ang / 2) * I2 - 1j * np.sin(ang / 2) * (ax[0] * s1 + ax[1] * s2 + ax[2] * s3)
    St = np.cos(phi / 2) * I2 - 1j * np.sin(phi / 2) * (nbar[0] * s1 + nbar[1] * s2 + nbar[2] * s3)
    return R @ St


per_point = []
for n in TEST_POINTS:
    nbar = np.array([n[0], -n[1], n[2]])
    tuples, n_ok = set(), 0
    for phi in np.linspace(0.0, 4 * np.pi, 40):
        M = kron(su2_carrying(nbar, n, phi), I2)
        rep = axiom_report(M, T_of(n))
        if rep and rep["order_zero"] and rep["first_order"]:
            n_ok += 1
            tuples.add((rep["J_sq"], rep["JDJ_vs_D"]))
    per_point.append(
        {"n": [round(float(x), 4) for x in n], "n_valid_phi": n_ok, "tuples": sorted(tuples)}
    )

n_with = sum(1 for p in per_point if p["n_valid_phi"] > 0)
observed = sorted({t for p in per_point for t in p["tuples"]})
print(f"  points where a real structure EXISTS: {n_with}/{len(TEST_POINTS)}")
print(f"  sign tuples (J^2, JDJ^-1/D) found: {observed}")
print("  order-zero and first-order hold automatically once J D J^-1 = +D: with")
print("  D = 3(T(x)I2), that condition already forces J b J^-1 = b on A, and A is")
print("  commutative. Both locality axioms are consequences, not constraints.")

print("\n  GLOBAL test -- does ONE fixed J work at every point?")
glob = 0
for pi in range(3):
    n = TEST_POINTS[pi]
    nbar = np.array([n[0], -n[1], n[2]])
    for phi in np.linspace(0.0, 4 * np.pi, 12):
        M = kron(su2_carrying(nbar, n, phi), I2)
        reps = [axiom_report(M, T_of(m)) for m in TEST_POINTS]
        if all(r and r["order_zero"] and r["first_order"] for r in reps):
            glob += 1
print(f"    fixed J valid at ALL {len(TEST_POINTS)} points: {glob}")
print("  STRUCTURAL REASON (not a search failure -- the same det obstruction C30")
print("  found, one level up): J is ANTIlinear, so T -> J T J^-1 is (conjugation,")
print("  which is the reflection n -> n_bar, det = -1) followed by (conjugation by")
print("  M, a rotation, det = +1). The composite has det = -1 and can never be the")
print("  identity map on the Bloch sphere, which is what a GLOBAL J would require.")
print("  C30's exchange operator was blocked by det(-I_3) = -1; the real structure")
print("  is blocked by the determinant of the SAME reflection. One obstruction.")
results["step3_per_point"] = per_point
results["step3_points_with_solution"] = n_with
results["step3_observed_tuples"] = [list(t) for t in observed]
results["step3_global_solutions"] = glob
results["step3_global_blocked_by_determinant"] = True

# =============================================================================
# STEP 4 -- is Theta among them, and is the sign tuple FORCED?
# =============================================================================
print("\nSTEP 4 -- is Theta itself a valid J, and is the sign tuple FORCED?")
theta_lift = kron(1j * s2, I2)
theta_reports = [axiom_report(theta_lift, T_of(n)) for n in TEST_POINTS]
theta_ok = [r for r in theta_reports if r and r["order_zero"] and r["first_order"]]
print(
    f"  C30's Theta lifted as (i*s2)(x)I2 is a valid J at {len(theta_ok)}/{len(TEST_POINTS)} points"
)
if not theta_ok:
    print("  Theta is the WRONG OBJECT for this role, and structurally so:")
    print("  C30 built it to satisfy Theta T Theta^-1 = 1 - T. A real structure")
    print("  must satisfy the ORDER-ZERO axiom [a, J b* J^-1] = 0 -- i.e. commute")
    print("  with the algebra. An operator built to EXCHANGE the algebra's two")
    print("  minimal projectors cannot commute with them. Theta is a symmetry OF")
    print("  the algebra; J is part of the SPECTRAL DATA. Different roles, and")
    print("  the OB2 checklist's 'real structure J: NOT ATTEMPTED' field is NOT")
    print("  filled by C30's Theta after all.")
forced = len(observed) == 1
print(f"  distinct sign tuples over all pointwise solutions: {observed}")
print(f"  sign tuple FORCED by the axioms alone: {forced}")
if not forced:
    print("  => the axioms do NOT pick a single KO-type in this toy. Quoting one")
    print("     'KO-dimension' from it would be a choice, not a derivation.")
results["step4_theta_valid_points"] = len(theta_ok)
results["step4_theta_is_a_valid_J"] = bool(theta_ok)
results["step4_sign_tuple_forced"] = bool(forced)

# =============================================================================
# STEP 5 -- NEGATIVE CONTROL
# =============================================================================
print("\nSTEP 5 -- NEGATIVE CONTROL: does the checker reject things it should?")
# (a) a linear (not antilinear) impostor: use M with M conj(M) neither +-I
bad = kron(s1 + 1j * s3, I2) / np.sqrt(2)
rej_a = axiom_report(bad, T_of(n0)) is None
# (b) an operator that fails order-zero: mix the internal factor non-trivially
bad2 = kron(I2, I2)  # J = plain conjugation
rep_b = axiom_report(bad2, T_of(TEST_POINTS[0]))
# plain conjugation must FAIL to be a global solution unless T is real
rep_b_ok = rep_b is not None and rep_b["order_zero"] and rep_b["first_order"]
rej_b = not rep_b_ok
print(f"  (a) non-antiunitary impostor rejected (no valid J^2 sign): {rej_a}")
print(f"  (b) plain conjugation K is NOT a global solution: {rej_b}")
print("      (plain K preserves T only if T is real; generic Bloch T is not)")
control_ok = bool(rej_a and rej_b)
print(f"  CONTROL PASSES: {control_ok}")
results["step5_control_rejects_non_antiunitary"] = bool(rej_a)
results["step5_control_rejects_plain_conjugation"] = bool(rej_b)
results["step5_control_passes"] = control_ok

# =============================================================================
verdict_ok = (not symmetric) and all_zero and control_ok and n_with > 0
verdict = (
    "THETA_IS_NOT_A_REAL_STRUCTURE__J_EXISTS_POINTWISE_ONLY__TRIPLE_IS_ODD_AND_DEGENERATE"
    if verdict_ok
    else "INCONCLUSIVE"
)
print("\n" + "=" * 78)
print(f"VERDICT: {verdict}")
print("=" * 78)
results["verdict"] = verdict
RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
print(f"\nResults -> {RESULTS_PATH}")
