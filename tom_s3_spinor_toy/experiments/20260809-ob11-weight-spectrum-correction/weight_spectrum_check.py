"""OB11 condition (i) -- C29 reached the right answer with the wrong evidence.

An external red-team audit (2026-08-09) pointed out that C29's conclusion
("each channel decomposes as 1+1+3+3bar under su(3)") does NOT follow from
what C29 actually computed. C29 diagonalised the QUADRATIC Casimir, finding
per channel 2 zero eigenvalues + 6 at one shared nonzero value.

The audit is right: C2(3) = C2(3bar) exactly, so that spectrum is equally
consistent with 1+1+3+3bar, 1+1+3+3, or 1+1+3bar+3bar.

THIS FILE'S FINDING: the audit's criticism of the EVIDENCE stands, but its
implied remedy (add a cubic Casimir) is unnecessary -- the discriminating
number has been sitting in this repo since G102 (2026-07-05), and round127
already used exactly this argument. C29 simply reached for the wrong tool
when the right one was already computed.

    Hom(V,V) = sum over irreps of (multiplicity)^2
        1+1+3+3bar  ->  2^2 + 1^2 + 1^2 = 6
        1+1+3+3     ->  2^2 + 2^2       = 8
        1+1+3bar+3bar -> 2^2 + 2^2      = 8

G102 S7 measured Hom_su3 = 6 for all pairs, diagonal included. That number
alone excludes 1+1+3+3 and 1+1+3bar+3bar. C29's conclusion is CORRECT; its
stated justification was not the one that carries it.

TWO OF MY OWN FAILED ATTEMPTS ARE RECORDED IN THE HEADER OF THIS FILE'S
HISTORY rather than silently dropped, because they are instructive:
  (1) First attempt built a "weight negation-symmetry" test. It failed its
      own negative control. Diagnosis: G102's channel reps are REAL
      antisymmetric matrices, whose spectra are purely imaginary and hence
      AUTOMATICALLY symmetric under negation -- the test was vacuous on this
      data and would have passed anything.
  (2) The same attempt compared those against hermitian control matrices
      (real eigenvalues), so np.imag() zeroed the controls -- an
      apples-to-oranges comparison on top of the vacuity.
Both were caught by the negative control, which is the entire reason it was
written before trusting the result.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_weight_spectrum.json"
G102_PATH = HERE.parent / "20260705-g102-spin8-fiber-obstruction" / "g102_spin8_fiber.py"
_spec = importlib.util.spec_from_file_location("g102_spin8_fiber", G102_PATH)
assert _spec and _spec.loader
G102 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G102)

results: dict = {}
print("=" * 74)
print("OB11 (i): C29's conclusion is right; its evidence was not sufficient")
print("=" * 74)

# --- STEP 1: confirm the audit's premise ------------------------------------
print("\nSTEP 1 (CONTROL): can the quadratic Casimir separate 3 from 3bar?")
gm = [
    np.array(m, dtype=complex)
    for m in [
        [[0, 1, 0], [1, 0, 0], [0, 0, 0]],
        [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]],
        [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
        [[0, 0, 1], [0, 0, 0], [1, 0, 0]],
        [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]],
        [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
        [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]],
        (np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3)),
    ]
]
T_f = [g / 2 for g in gm]
T_fbar = [-np.conj(g) / 2 for g in gm]
C2_f = sum(t @ t for t in T_f)
C2_fbar = sum(t @ t for t in T_fbar)
c2_same = bool(np.allclose(C2_f, C2_fbar))
print(f"  C2 on 3    = {np.round(np.real(C2_f[0, 0]), 6)} * I")
print(f"  C2 on 3bar = {np.round(np.real(C2_fbar[0, 0]), 6)} * I")
print(f"  identical -> C2 CANNOT separate them: {c2_same}")
print("  => the audit's criticism of C29's evidence is CORRECT.")
results["step1_C2_cannot_separate_3_from_3bar"] = c2_same

# --- STEP 2: the number that DOES discriminate, already in the repo ---------
print("\nSTEP 2: which decomposition is consistent with Hom(V,V) = 6?")
print("  Hom(V,V) = sum of squared multiplicities:")
candidates = {
    "1+1+3+3bar": (2, 1, 1),
    "1+1+3+3": (2, 2, 0),
    "1+1+3bar+3bar": (2, 0, 2),
}
hom_pred = {}
for name, (m1, m3, m3b) in candidates.items():
    hom_pred[name] = m1**2 + m3**2 + m3b**2
    print(f"    {name:16s} -> Hom(V,V) = {hom_pred[name]}")
consistent = [k for k, v in hom_pred.items() if v == 6]
print(f"\n  consistent with Hom=6: {consistent}")
results["step2_hom_predictions"] = hom_pred
results["step2_only_candidate_at_hom6"] = consistent

# --- STEP 3: measure Hom directly, using G102's own verified machinery ------
print("\nSTEP 3: measure Hom_su3 on this project's actual channels")
der = G102.derivation_basis()
su3 = G102.stabilizer_basis(der)
assert len(su3) == 8, f"expected su(3) dim 8, got {len(su3)}"
reps = G102.restrict_to_subalgebra(su3)
labels = ("v", "s", "c")
hom_measured = {}
for i, la in enumerate(labels):
    for j, lb in enumerate(labels):
        hom_measured[f"{la}-{lb}"] = G102.hom_dim(reps[i], reps[j])
print(f"  Hom_su3 pairs: {hom_measured}")
all_six = all(v == 6 for v in hom_measured.values())
print(f"  all pairs equal 6 (reproduces G102 S7): {all_six}")
results["step3_hom_measured"] = hom_measured
results["step3_all_pairs_are_6"] = bool(all_six)

diag_six = all(hom_measured[f"{la}-{la}"] == 6 for la in labels)
print(f"\n  DIAGONAL Hom(V,V) = 6 for every channel: {diag_six}")
print("  => 1+1+3+3 and 1+1+3bar+3bar (both predicting 8) are EXCLUDED.")
print("  => each channel is 1+1+3+3bar. C29's conclusion holds.")
results["step3_diagonal_hom_is_6"] = bool(diag_six)

# --- STEP 4: NEGATIVE CONTROL -- does the Hom criterion actually reject 3+3? -
print("\nSTEP 4: NEGATIVE CONTROL -- build 1+1+3+3 explicitly, measure its Hom")
print("  (if the criterion returned 6 for this too, it would prove nothing)")
zero3 = np.zeros((3, 3), dtype=complex)


def block_rep(a_list, b_list):
    """1 + 1 + a + b as 8x8 complex matrices (two trivial 1-dim summands)."""
    out = []
    for a, b in zip(a_list, b_list):
        M = np.zeros((8, 8), dtype=complex)
        M[2:5, 2:5] = a
        M[5:8, 5:8] = b
        out.append(M)
    return out


rep_33bar = block_rep(T_f, T_fbar)  # 1+1+3+3bar  -> expect Hom 6
rep_33 = block_rep(T_f, T_f)  # 1+1+3+3     -> expect Hom 8
hom_33bar = G102.hom_dim(rep_33bar, rep_33bar)
hom_33 = G102.hom_dim(rep_33, rep_33)
print(f"  explicit 1+1+3+3bar : Hom(V,V) = {hom_33bar}  (predicted 6)")
print(f"  explicit 1+1+3+3    : Hom(V,V) = {hom_33}  (predicted 8)")
control_ok = (hom_33bar == 6) and (hom_33 == 8)
print(f"  NEGATIVE CONTROL PASSES (criterion separates the two): {control_ok}")
results["step4_hom_explicit_33bar"] = int(hom_33bar)
results["step4_hom_explicit_33"] = int(hom_33)
results["step4_negative_control_passes"] = bool(control_ok)

verdict = c2_same and diag_six and control_ok
print("\n" + "=" * 74)
print(f"VERDICT: {'C29_CONCLUSION_STANDS__EVIDENCE_CORRECTED' if verdict else 'INCONCLUSIVE'}")
print("=" * 74)
if verdict:
    print("C29's CONCLUSION (1+1+3+3bar per channel) is CORRECT and survives.")
    print("C29's EVIDENCE (quadratic Casimir) never established it -- the audit is")
    print("right about that. The sufficient evidence (Hom_su3 = 6, excluding the")
    print("Hom=8 alternatives) has been in this repo since G102 and was already")
    print("used by round127. C29 reached for the wrong tool; nothing needs to be")
    print("recomputed, only re-cited.")
results["verdict"] = "C29_CONCLUSION_STANDS__EVIDENCE_CORRECTED" if verdict else "INCONCLUSIVE"

RESULTS_PATH.write_text(json.dumps(results, indent=2))
print(f"\nResults -> {RESULTS_PATH}")
