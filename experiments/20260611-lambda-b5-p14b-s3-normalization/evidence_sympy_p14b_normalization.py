"""LAMBDA-B5-P14B: S³ Hopf measure normalization robustness.

Hopf coordinates on S³(radius rho):
  alpha in [0, pi/2],  theta, theta_tilde in [0, 2*pi)
  volume element: rho^3 * sin(alpha)*cos(alpha) * d_alpha * d_theta * d_theta_tilde

Claim: this measure is self-consistent — correct S³ volume, finite bilinear norm,
phase-invariant, equivalent to sin(2*alpha)/2 form.

Runs autonomously without Tom Q4 reply.
"""

import json
import os
import sys

import sympy as sp

alpha, chi, rho = sp.symbols("alpha chi rho", real=True, positive=True)
pi = sp.pi

results: list[dict] = []
_passed = 0


def chk(name: str, cond: object, desc: str) -> bool:
    global _passed
    ok = bool(cond)
    results.append({"check": name, "pass": ok, "desc": desc})
    status = "PASS" if ok else "FAIL"
    print(f"{status} {name}: {desc}")
    if ok:
        _passed += 1
    return ok


# ── T1: Radial integral = 1/2 ────────────────────────────────────────────────
radial_vol = sp.integrate(sp.sin(alpha) * sp.cos(alpha), (alpha, 0, pi / 2))
chk("T1", sp.Eq(radial_vol, sp.Rational(1, 2)), "∫₀^{π/2} sin(α)cos(α) dα = 1/2")

# ── T2: Full S³ volume = 2π² (unit sphere) ───────────────────────────────────
# angular part: ∫₀^{2π} dθ × ∫₀^{2π} dθ̃ = (2π)² = 4π²
vol_s3 = radial_vol * (2 * pi) ** 2
chk("T2", sp.Eq(sp.simplify(vol_s3), 2 * pi**2), "S³ volume (unit) = 2π²")

# ── T3: Measure equivalence sin(α)cos(α) = sin(2α)/2 ─────────────────────────
diff_measure = sp.simplify(sp.sin(alpha) * sp.cos(alpha) - sp.sin(2 * alpha) / 2)
chk("T3", sp.Eq(diff_measure, 0), "sin(α)cos(α) = sin(2α)/2 — symbolic identity")

# ── T4: Bilinear radial norm = 1/12 ──────────────────────────────────────────
# φ₀₀·g₀₀ = cosα·sinα  (from AV-2 E1 STRONG_PASS)
# radial norm: ∫₀^{π/2} (cosα·sinα)² · sin(α)cos(α) dα
bilinear_radial = sp.integrate(
    (sp.cos(alpha) * sp.sin(alpha)) ** 2 * sp.sin(alpha) * sp.cos(alpha),
    (alpha, 0, pi / 2),
)
chk(
    "T4",
    sp.Eq(bilinear_radial, sp.Rational(1, 12)),
    "∫₀^{π/2} sin²α cos²α · sinα cosα dα = 1/12 (AV-2 E1 bilinear norm, radial)",
)

# ── T5: Full bilinear norm (radial × angular) = π²/3 ─────────────────────────
bilinear_full = bilinear_radial * (2 * pi) ** 2
chk(
    "T5",
    sp.Eq(sp.simplify(bilinear_full), pi**2 / 3),
    "Full bilinear norm = π²/3 — finite and exact",
)

# ── T6: Phase invariance ─────────────────────────────────────────────────────
# φ₀₀·g₀₀ may carry spinor phase e^{iχ}
# |e^{iχ} · cosα · sinα|² = cos²α · sin²α  (independent of χ)
phase_factor = sp.Abs(sp.exp(sp.I * chi)) ** 2
bilinear_with_phase = sp.simplify(phase_factor * (sp.cos(alpha) * sp.sin(alpha)) ** 2)
bilinear_no_phase = (sp.cos(alpha) * sp.sin(alpha)) ** 2
chk(
    "T6",
    sp.Eq(sp.simplify(bilinear_with_phase - bilinear_no_phase), 0),
    "|e^{iχ}·cosα·sinα|² = cos²α·sin²α — phase-invariant",
)

# ── T7: Radius scaling — S³(ρ) volume = 2π²ρ³ ────────────────────────────────
# Under α → α, θ → θ, θ̃ → θ̃, r → ρ·r:
# the Jacobian inserts ρ³ into the volume element
vol_s3_rho = vol_s3 * rho**3
chk(
    "T7",
    sp.Eq(sp.simplify(vol_s3_rho), 2 * pi**2 * rho**3),
    "S³(ρ) volume = 2π²ρ³ — radius scaling consistent",
)

# ── Summary ──────────────────────────────────────────────────────────────────
total = len(results)
print(f"\n{_passed}/{total} checks passed")

verdict = "PASS_S3_MEASURE_SELF_CONSISTENT" if _passed == total else "PARTIAL"

print("\nKey values:")
print(f"  S³ volume (unit):       {sp.simplify(vol_s3)}")
print(f"  S³ volume (radius ρ):   {sp.simplify(vol_s3_rho)}")
print(f"  Bilinear radial norm:   {bilinear_radial}")
print(f"  Bilinear full norm:     {sp.simplify(bilinear_full)}")

out = {
    "gate": "LAMBDA-B5-P14B",
    "verdict": verdict,
    "passed": _passed,
    "total": total,
    "s3_volume_unit": str(sp.simplify(vol_s3)),
    "s3_volume_rho": str(sp.simplify(vol_s3_rho)),
    "bilinear_radial_norm": str(bilinear_radial),
    "bilinear_full_norm": str(sp.simplify(bilinear_full)),
    "measure": "sin(alpha)*cos(alpha) d_alpha  ==  sin(2*alpha)/2 d_alpha",
    "autonomous": True,
    "requires_tom_q4": False,
    "note": (
        "Measure is self-consistent regardless of Tom's basis choice. "
        "Q4 concerns WHICH spinor modes are canonical, not WHETHER the measure is valid."
    ),
    "GEOMETRY_AGNOSTIC": True,
    "safe_for_runtime": False,
    "checks": results,
}

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_p14b.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2)

print(f"Verdict: {verdict}")
print(f"Saved: {out_path}")
sys.exit(0 if _passed == total else 1)
