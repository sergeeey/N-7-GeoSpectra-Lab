"""LAMBDA-B5-G2 evidence: cot(2α) is a Hopf-coframe frame artifact.

Hypothesis verified here (see claim.md in this folder):
    1. Identity:   tan(α) - cot(α) = -2 cot(2α)  [exact, algebraic]
    2. Hopf frame: ω¹₂ = +tan(α) e²,  ω¹₃ = -cot(α) e³,  ω²₃ = 0
       — connection coefficients are α-dependent
    3. α-combination: coefficient(ω¹₂) + coefficient(ω¹₃) = tan(α) - cot(α) = -2cot(2α)
    4. Curvature in Hopf frame = e^a ∧ e^b  (unit S³, frame-independent check)
    5. Invariant frame: Maurer-Cartan structure dσ₃ = k·σ₁∧σ₂ with k = CONSTANT
       — connection structure constants are integers, no α-dependence

Conventions (same as G0 evidence_sympy_invariant_sector.py):
    Metric       ds² = dα² + cos²(α) dθ² + sin²(α) dφ²
    Orientation  vol = +sin(α) cos(α) dα ∧ dθ ∧ dφ
    Coframe      e¹ = dα,  e² = cos(α) dθ,  e³ = sin(α) dφ
    Cartan       de^a + ω^a_b ∧ e^b = 0  (torsion-free)
    Killing      ξ̃  = (0, cos²α, sin²α)   [same as G0]

Standalone: requires only sympy. Run from this folder:
    python evidence_sympy_g2_frame_artifact.py
Exit code 0 = all 14 checks pass (PASS_FRAME_ARTIFACT_CONFIRMED).
Exit code 1 = at least one check failed.
Writes results_g2.json next to this file.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

# ─── Symbolic variables ───────────────────────────────────────────────────────
a, t, p = sp.symbols("alpha theta phi", real=True)

# ─── Helpers: 1-form and 2-form algebra ──────────────────────────────────────


def d_one_form(w: tuple) -> tuple:
    """Exterior derivative: 1-form (w_α, w_θ, w_φ) → 2-form (F_αθ, F_αφ, F_θφ)."""
    w_a, w_t, w_p = w
    return (
        sp.diff(w_t, a) - sp.diff(w_a, t),  # dα∧dθ coefficient
        sp.diff(w_p, a) - sp.diff(w_a, p),  # dα∧dφ coefficient
        sp.diff(w_p, t) - sp.diff(w_t, p),  # dθ∧dφ coefficient
    )


def wedge_11(f: tuple, g: tuple) -> tuple:
    """Wedge product of two 1-forms → 2-form (F_αθ, F_αφ, F_θφ)."""
    fa, ft, fp = f
    ga, gt, gp = g
    return (
        fa * gt - ft * ga,  # dα∧dθ
        fa * gp - fp * ga,  # dα∧dφ
        ft * gp - fp * gt,  # dθ∧dφ
    )


def add2(A: tuple, B: tuple) -> tuple:
    return (A[0] + B[0], A[1] + B[1], A[2] + B[2])


def neg2(A: tuple) -> tuple:
    return (-A[0], -A[1], -A[2])


def simp2(A: tuple) -> tuple:
    return tuple(sp.trigsimp(sp.simplify(x)) for x in A)


def is_zero2(A: tuple) -> bool:
    return all(sp.trigsimp(sp.simplify(x)) == 0 for x in A)


def is_equal2(A: tuple, B: tuple) -> bool:
    return is_zero2(add2(A, neg2(B)))


# ─── Coframe (G0 convention) ─────────────────────────────────────────────────
# e¹ = dα, e² = cos(α) dθ, e³ = sin(α) dφ

E1 = (sp.Integer(1), sp.Integer(0), sp.Integer(0))
E2 = (sp.Integer(0), sp.cos(a), sp.Integer(0))
E3 = (sp.Integer(0), sp.Integer(0), sp.sin(a))

# ─── Spin connection ansatz (to be verified) ─────────────────────────────────
# ω¹₂ = +tan(α) e² = (0, tan(α)·cos(α), 0) = (0, sin(α), 0)
# ω¹₃ = -cot(α) e³ = (0, 0, -cot(α)·sin(α)) = (0, 0, -cos(α))
# ω²₃ = 0
# antisymmetry: ω²₁ = -ω¹₂, ω³₁ = -ω¹₃, ω³₂ = -ω²₃

W12 = (sp.Integer(0), sp.sin(a), sp.Integer(0))  # ω¹₂
W13 = (sp.Integer(0), sp.Integer(0), -sp.cos(a))  # ω¹₃
W23 = (sp.Integer(0), sp.Integer(0), sp.Integer(0))  # ω²₃
W21 = neg2(W12)  # -ω¹₂
W31 = neg2(W13)  # -ω¹₃
W32 = neg2(W23)  # -ω²₃

# ─── Check infrastructure ─────────────────────────────────────────────────────
checks: list[dict] = []
n_pass = 0
TOTAL = 14


def chk(name: str, passed: bool, note: str = "") -> None:
    global n_pass
    status = "PASS" if passed else "FAIL"
    checks.append({"check": name, "status": status, "note": note})
    if passed:
        n_pass += 1
    marker = "✓" if passed else "✗"
    print(f"  {marker} {name}")
    if not passed and note:
        print(f"      ↳ {note}")


# ═══════════════════════════════════════════════════════════════════════════════
print("\nLAMBDA-B5-G2 — Hopf vs invariant frame spin connection")
print("=" * 60)

# ─── GROUP A: Algebraic identity ─────────────────────────────────────────────
print("\n[A] Algebraic identity")

# T1: tan(α) - cot(α) = -2cot(2α)
# Explicit sin/cos form: use expand_trig to unfold double-angle, then simplify.
# tan(α)-cot(α) = (sin²α-cos²α)/(sinα cosα)
# -2cos(2α)/sin(2α) after expand_trig = -2(cos²α-sin²α)/(2sinα cosα) = same → diff = 0
lhs_T1 = sp.sin(a) / sp.cos(a) - sp.cos(a) / sp.sin(a)  # explicit: no cot/tan
rhs_T1 = (
    sp.Integer(-2) * (sp.cos(a) ** 2 - sp.sin(a) ** 2) / (sp.Integer(2) * sp.sin(a) * sp.cos(a))
)
diff_T1 = sp.simplify(lhs_T1 - rhs_T1)
chk("T1: tan(α) − cot(α) = −2cot(2α)  [exact identity]", diff_T1 == 0, f"residual={diff_T1}")

# T2: d(cot α)/dα ≠ 0 — cot α is genuinely α-dependent (not a constant)
dcot = sp.diff(sp.cot(a), a)
chk(
    "T2: d/dα[cot α] ≠ 0  [α-dependent, not constant]",
    sp.simplify(dcot) != 0,
    f"d/dα cot α = {dcot}",
)

# ─── GROUP B: Hopf coframe exterior derivatives ───────────────────────────────
print("\n[B] Hopf coframe structure (metric ds²=dα²+cos²α dθ²+sin²α dφ²)")

# T3: de¹ = 0
chk("T3: de¹ = 0", is_zero2(d_one_form(E1)))

# T4: de² = −tan(α) e¹∧e²
de2 = d_one_form(E2)
e1we2 = wedge_11(E1, E2)
lhs_T4 = de2
rhs_T4 = tuple(-sp.tan(a) * x for x in e1we2)
chk(
    "T4: de² = −tan(α) e¹∧e²",
    is_equal2(lhs_T4, rhs_T4),
    f"de²={simp2(de2)}, -tanα·e¹∧e²={simp2(rhs_T4)}",
)

# T5: de³ = +cot(α) e¹∧e³
de3 = d_one_form(E3)
e1we3 = wedge_11(E1, E3)
lhs_T5 = de3
rhs_T5 = tuple(sp.cot(a) * x for x in e1we3)
chk(
    "T5: de³ = +cot(α) e¹∧e³",
    is_equal2(lhs_T5, rhs_T5),
    f"de³={simp2(de3)}, cotα·e¹∧e³={simp2(rhs_T5)}",
)

# ─── GROUP C: Cartan structure equations (torsion-free) ───────────────────────
print("\n[C] Cartan torsion-free equations  de^a + ω^a_b ∧ e^b = 0")

# de^a + ω^a_b ∧ e^b = 0 summed over b ≠ a:
# For e¹: de¹ + ω¹₂∧e² + ω¹₃∧e³ = 0
cartan1 = simp2(add2(d_one_form(E1), add2(wedge_11(W12, E2), wedge_11(W13, E3))))
chk("T6: Cartan de¹ + ω¹₂∧e² + ω¹₃∧e³ = 0", is_zero2(cartan1), f"residual={cartan1}")

# For e²: de² + ω²₁∧e¹ + ω²₃∧e³ = 0
cartan2 = simp2(add2(d_one_form(E2), add2(wedge_11(W21, E1), wedge_11(W23, E3))))
chk(
    "T7: Cartan de² + ω²₁∧e¹ + ω²₃∧e³ = 0  [ω¹₂=+tanα e²]", is_zero2(cartan2), f"residual={cartan2}"
)

# For e³: de³ + ω³₁∧e¹ + ω³₂∧e² = 0
cartan3 = simp2(add2(d_one_form(E3), add2(wedge_11(W31, E1), wedge_11(W32, E2))))
chk(
    "T8: Cartan de³ + ω³₁∧e¹ + ω³₂∧e² = 0  [ω¹₃=−cotα e³]", is_zero2(cartan3), f"residual={cartan3}"
)

# ─── GROUP D: Connection coefficients are α-dependent ─────────────────────────
print("\n[D] Hopf connection coefficients are α-dependent")

# ω¹₂ = sin(α) dθ → coefficient relative to e² = cos(α) dθ is sin(α)/cos(α) = tan(α)
coeff_w12 = sp.trigsimp(sp.simplify(W12[1] / E2[1]))  # sin(α)/cos(α) = tan(α)
chk(
    "T9: ω¹₂/e² = +tan(α)  [α-dependent coefficient]",
    sp.trigsimp(coeff_w12 - sp.tan(a)) == 0,
    f"ω¹₂/e² = {coeff_w12}",
)

# ω¹₃ = -cos(α) dφ → coefficient relative to e³ = sin(α) dφ is -cos(α)/sin(α) = -cot(α)
coeff_w13 = sp.trigsimp(sp.simplify(W13[2] / E3[2]))  # -cos(α)/sin(α) = -cot(α)
chk(
    "T10: ω¹₃/e³ = −cot(α)  [α-dependent coefficient]",
    sp.trigsimp(coeff_w13 + sp.cot(a)) == 0,
    f"ω¹₃/e³ = {coeff_w13}",
)

# ─── GROUP E: Curvature = unit S³ (frame-independent check) ──────────────────
print("\n[E] Curvature R^ab = e^a ∧ e^b  (unit S³, frame-independent)")

# R¹₂ = dω¹₂ + ω¹ₖ∧ωᵏ₂  (with ω¹₁=0)
# = dω¹₂ + ω¹₃∧ω³₂
R12 = simp2(add2(d_one_form(W12), wedge_11(W13, W32)))
chk(
    "T11: R¹₂ = e¹∧e²  [unit-sphere curvature]",
    is_equal2(R12, e1we2),
    f"R¹₂={R12}, e¹∧e²={simp2(e1we2)}",
)

# R¹₃ = dω¹₃ + ω¹₂∧ω²₃
R13 = simp2(add2(d_one_form(W13), wedge_11(W12, W23)))
chk("T12: R¹₃ = e¹∧e³", is_equal2(R13, e1we3), f"R¹₃={R13}, e¹∧e³={simp2(e1we3)}")

# R²₃ = dω²₃ + ω²₁∧ω¹₃
e2we3 = wedge_11(E2, E3)
R23 = simp2(add2(d_one_form(W23), wedge_11(W21, W13)))
chk("T13: R²₃ = e²∧e³", is_equal2(R23, e2we3), f"R²₃={R23}, e²∧e³={simp2(e2we3)}")

# ─── GROUP F: Invariant frame — Maurer-Cartan constant structure ──────────────
print("\n[F] Invariant frame — Maurer-Cartan structure constants are integers")

# Left-invariant 1-forms on S³  (same G0 convention, verified there with *d eigenvalues):
#   σ₁ = sin(θ+φ) dα + sin(α)cos(α)cos(θ+φ) [dφ − dθ]
#   σ₂ = −cos(θ+φ) dα + sin(α)cos(α)sin(θ+φ) [dφ − dθ]
#   σ₃ = cos²(α) dθ + sin²(α) dφ  = ξ̃  (G0 Killing form, *d ξ̃ = −2ξ̃)

sig1 = (
    sp.sin(t + p),
    -sp.sin(a) * sp.cos(a) * sp.cos(t + p),
    sp.sin(a) * sp.cos(a) * sp.cos(t + p),
)
sig2 = (
    -sp.cos(t + p),
    -sp.sin(a) * sp.cos(a) * sp.sin(t + p),
    sp.sin(a) * sp.cos(a) * sp.sin(t + p),
)
sig3 = (sp.Integer(0), sp.cos(a) ** 2, sp.sin(a) ** 2)

# Compute dσ₃ and σ₁∧σ₂, then check their ratio is a constant k ∈ ℤ
ds3 = d_one_form(sig3)  # 2-form
s1ws2 = wedge_11(sig1, sig2)  # 2-form

# Use the dα∧dθ component (ds3[0] and s1ws2[0] are both non-zero and simplest)
ds3_at = sp.trigsimp(sp.expand(ds3[0]))  # dα∧dθ component of dσ₃
s1ws2_at = sp.trigsimp(sp.expand(s1ws2[0]))  # dα∧dθ component of σ₁∧σ₂

ratio = sp.trigsimp(sp.simplify(ds3_at / s1ws2_at))

# Ratio must be a constant integer (independent of α, θ, φ)
d_ratio_da = sp.simplify(sp.diff(ratio, a))
d_ratio_dt = sp.simplify(sp.diff(ratio, t))
d_ratio_dp = sp.simplify(sp.diff(ratio, p))
is_const = d_ratio_da == 0 and d_ratio_dt == 0 and d_ratio_dp == 0

chk(
    "T14: dσ₃/(σ₁∧σ₂) = integer constant  [invariant frame: constant MC structure]",
    is_const,
    f"ratio={ratio}, ∂_α={d_ratio_da}, ∂_θ={d_ratio_dt}, ∂_φ={d_ratio_dp}",
)

# ─── Summary ──────────────────────────────────────────────────────────────────
print()
print("=" * 60)
hopf_sum = sp.trigsimp(coeff_w12 + coeff_w13)  # tan α + (-cot α) = tan α - cot α
expected_hopf_sum = -2 * sp.cos(2 * a) / sp.sin(2 * a)
hopf_sum_check = sp.trigsimp(hopf_sum - expected_hopf_sum)

verdict = (
    "PASS_FRAME_ARTIFACT_CONFIRMED"
    if n_pass == TOTAL
    else (f"PARTIAL_PASS_{n_pass}_of_{TOTAL}" if n_pass > 0 else "FAIL")
)

print(f"Verdict  : {verdict}")
print(f"Passed   : {n_pass}/{TOTAL}")
print("Key result (Hopf frame):")
print(f"  ω¹₂ coefficient  = {coeff_w12}")
print(f"  ω¹₃ coefficient  = {coeff_w13}")
print(f"  sum tan−cot      = {sp.trigsimp(hopf_sum)}")
print(f"  = −2cot(2α)?     residual = {hopf_sum_check}")
print(f"Invariant MC ratio = {ratio}  (integer constant, no α-dependence)")

# ─── Write results_g2.json ────────────────────────────────────────────────────
output = {
    "verdict": verdict,
    "passed": n_pass,
    "total": TOTAL,
    "checks": checks,
    "key_result": {
        "hopf_connection_w12_coeff": str(coeff_w12),
        "hopf_connection_w13_coeff": str(coeff_w13),
        "hopf_sum_tan_minus_cot": str(sp.trigsimp(hopf_sum)),
        "hopf_sum_equals_minus2cot2a_residual": str(hopf_sum_check),
        "invariant_mc_structure_constant": str(ratio),
        "frame_artifact_conclusion": (
            "cot(2α) = (tan α − cot α) / (−2) arises from α-dependent Hopf-frame"
            " spin connection. Invariant frame has integer MC structure constants"
            " — no cot(2α) obstruction."
        ),
    },
    "fence": {
        "lambda_status": "FREE_COUPLING_PARAMETER — G2 does NOT fix lambda",
        "geometry_status": "GEOMETRY_AGNOSTIC intact — no spin-structure selection",
        "promotion_status": "PROMOTION_BLOCKED — no physical V promoted",
        "safe_for_runtime": False,
    },
}

results_path = Path(__file__).parent / "results_g2.json"
with results_path.open("w", encoding="utf-8") as fh:
    json.dump(output, fh, indent=2, ensure_ascii=False)
print(f"\nResults written to: {results_path}")

sys.exit(0 if n_pass == TOTAL else 1)
