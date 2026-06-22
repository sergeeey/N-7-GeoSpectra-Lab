# Decision: G86A — Dual-Modulus / Inverse-Modulus Route

**Date:** 2026-06-22
**Verdict:** NULL — structural: Laplace integral with ANY power-law T(ρ₆) gives power-law, never exp(−λ/ρ₆²)

---

## Claim

T(ρ₆)=B·ρ₆^α with α≠6 in the proper-time integral gives exp(−λ/ρ₆²).

**Falsifier:** PASS if result ∝ exp(−const/ρ₆²) with const>0.
FAIL if exponent is positive or T→ρ₆^6 again.

---

## Gate Results (4/4 gates)

| Gate | Test | Result |
|------|------|--------|
| G1 | Numeric vs analytic | ratio=1.0000 for all 4 test α values ✓ |
| G2 | 25 alpha values in [−4,8] | ALL POWER-LAW, R²_pow=1.0000 |
| G3 | Search for exp(−λ/ρ₆²) | **0 / 25 alpha values** — none found |
| G4 | Special case α=−2 (T~1/ρ₆²) | POWER-LAW ρ₆^+6, not exponential |

**Result: NULL** — 0 out of 25 alpha values give exp(−λ/ρ₆²).

---

## Structural Proof (analytic, verified numerically)

The proper-time integral for T(ρ₆)=B·ρ₆^α evaluates **exactly**:

```
I(ρ₆) = ∫₀^∞ dt t^{−d/2−1} exp(−T/t)
       = Γ(d/2) / T(ρ₆)^{d/2}
       = Γ(d/2) / (B·ρ₆^α)^{d/2}
       ~ ρ₆^{−α·d/2}  [POWER LAW]
```

For S⁶ (d=6): I(ρ₆) ~ ρ₆^{−3α}

For exp(−λ/ρ₆²) we'd need log I ~ −λ/ρ₆², but log(ρ₆^{−3α}) = −3α·log(ρ₆) — logarithmic, not 1/ρ₆².

**This is incompatible for any finite α.** The mechanism is structurally wrong — Laplace integrals with power-law kernels always give power-law results.

---

## Kill Analysis

**Killed:** "Dual-modulus T(ρ₆)=B·ρ₆^α proper-time integral → exp(−λ/ρ₆²)" for ALL α ∈ ℝ.

**Stronger kill:** G83+G84+G85A+G85B+G86A together close the ENTIRE CLASS of spectral/worldline/proper-time mechanisms as a source of exp(−λ/ρ₆²). The Laplace integral I=Γ(d/2)/T^{d/2} is exact — no power-law T(ρ₆) can produce the required exponential.

**What was NOT killed:**
1. **G86B route** — warp factor Ω(y) modifies the 4D volume factor, not the spectral determinant. Different class, untested.
2. **Brane-instanton mechanism** — S_inst = Vol(brane)/g_s; for a D4 wrapping a 2-cycle in S⁶ with Vol~1/ρ₆², gives exp(−1/ρ₆²). Not a Laplace integral — genuinely different physics.
3. **Gaugino condensation** — W~exp(−const/g²) where g~ρ₆ could give the form. Also not a spectral mechanism.
4. **exp(−λ/ρ₆²) itself** — the form exists, but its origin must be non-perturbative/non-spectral.

---

## Updated λ-map

```
CLOSED (spectral/worldline class — ALL killed by structural theorem):
  G83-G84B: standard reduction → +12/+6, not 1/ρ₆²
  G85A: Poisson/theta resummation → form exists, bridge missing
  G85B: Spectral saddle → t*=ρ₆²/3, exp(-3)=const, not 1/ρ₆²
  G86A: Dual-modulus T∝ρ₆^α (ALL α) → POWER-LAW, never exp

OPEN (non-spectral class):
  G86B: Warp factor Ω(y) ← last remaining candidate
```
