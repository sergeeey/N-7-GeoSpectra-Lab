# G54-F: Casimir potential in 4D Einstein-Hilbert frame — Weyl rescaling of G54-A through G54-E

**Date:** 2026-06-21
**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Closes:** G54-A gate F4 (open since G54-A commit feafaae).

---

## Estimand

**Population:** S³×S⁶ compactification along the SM constraint ρ₃ = 0.986 ρ₆²
**Endpoint:** Casimir potential V^EH_Cas(ρ₆) in the 4D Einstein-Hilbert frame (Weyl-rescaled)
**Summary measure:** Monotonicity, sign, and zero structure of V^EH_Cas on ρ₆ ∈ [0.7, 1.5]
**MCID:** Existence or absence of a local minimum (i.e., the three-radius structure from G54-E either survives or does not)

**Weyl rescaling:**
  g_μν^(4D EH) = V_int^{−1} g_μν^(10D string)
  V^EH_Cas(ρ₆) = ζ_FP(ρ₆) / V_int(ρ₆)

where V_int = vol(S³, ρ₃) × vol(S⁶, ρ₆) = (32π⁵C³/15) × ρ₆¹²

---

## Gates

### F4.1: V_int ∝ ρ₆¹² (exact power law along SM constraint)

**Claim:** Along ρ₃ = Cρ₆², the internal volume scales as V_int ∝ ρ₆¹².
Derivation: vol(S³, Cρ₆²)³ × vol(S⁶, ρ₆)⁶ = (2π²C³ρ₆⁶) × (16π³ρ₆⁶/15) = (32π⁵C³/15)ρ₆¹².
Exponent 12 = 3+3 (S³ fiber doubling from ρ₃=Cρ₆²) + 6 (S⁶ power).

**Evidence:** [VERIFIED] V_int(2)/V_int(1) = 4096 = 2^12; V_int(1.5)/V_int(1) = 1.5^12 = 129.75 (errors < 1e-6).
**Tests:** F4.1.1 (ratio 2^12), F4.1.2 (ratio 1.5^12), F4.1.3 (monotone)

---

### F4.2: V^EH_Cas monotone on [0.7, 1.5] — no local minimum in EH frame

**Claim:** The local minimum of ζ_FP at ρ₆_min ≈ 0.953 (G54-E) does NOT survive Weyl rescaling.
In the 4D EH frame, V^EH_Cas = ζ_FP/V_int is monotone increasing on [0.7, 1.5].

Physical reason: V_int ∝ ρ₆¹² grows rapidly; when ζ_FP is divided by this growing factor,
the minimum is suppressed — the ρ₆¹² denominator overwhelms the ζ_FP structure.

At ρ₆ = 0.953 (the 10D local minimum):
  In 10D: ζ_FP(0.95) < ζ_FP(0.8)   [minimum, ζ_FP is more negative here]
  In 4D: V^EH_Cas(0.95) > V^EH_Cas(0.8)   [NOT a minimum — monotone]

**Evidence:** [VERIFIED] d(V^EH_Cas)/dρ₆ at ρ₆=0.953 > 0 (positive, not a minimum).
V^EH_Cas(0.7) < V^EH_Cas(1.0) < V^EH_Cas(1.3) confirmed numerically.
V^EH_Cas < 0 throughout [0.7, ρ₆**) — Casimir is attractive in this range.
**Tests:** F4.2.1 (monotone at three points), F4.2.2 (no extremum at ρ₆_min), F4.2.3 (negative on range)

---

### F4.3: V^EH_Cas(ρ₆**) = 0 — zero of ζ_FP preserved under Weyl rescaling

**Claim:** ρ₆** ≈ 1.4469 is a zero of V^EH_Cas (as well as ζ_FP), because V_int ≠ 0 everywhere.

Algebraic reason: V_int = (32π⁵C³/15)ρ₆¹² > 0 for all ρ₆ > 0.
Therefore: V^EH_Cas = ζ_FP/V_int = 0 ⟺ ζ_FP = 0 ⟺ ρ₆ = ρ₆**.

Sign change: V^EH_Cas(1.44) < 0, V^EH_Cas(1.46) > 0. Same bracket as ζ_FP.

**Evidence:** [VERIFIED] |V^EH_Cas(ρ₆**)| < 1e-10 at brentq zero of ζ_FP.
Sign change verified numerically at bracket [1.44, 1.46].
**Tests:** F4.3.1 (zero at ρ₆**), F4.3.2 (sign change)

---

### F4.4: V_flux >> |ζ_FP| — flux dominates in EH frame (Dine-Seiberg regime)

**Claim:** The Freund-Rubin flux V_flux = const ≈ 0.286 (G54-A F3) is ~300× larger
than max|ζ_FP| ≈ 0.00085 on [0.7, 1.5]. Both terms scale as 1/V_int ∝ 1/ρ₆¹² in EH frame,
but the flux numerator dominates by a factor ~330.

Consequence: V_total_EH = V^EH_Cas + V^EH_flux > 0 on all of [0.7, 1.5].
The Casimir energy is a small negative perturbation on the positive flux background.

**Evidence:** [VERIFIED] V_flux_const/max|ζ_FP| ≈ 330 >> 100. V_total_EH > 0 at all 8 test points.
**Tests:** F4.4.1 (ratio > 100), F4.4.2 (V_total > 0 on range)

---

### F4.5: Dine-Seiberg runaway — no minimum from Casimir+flux in EH frame on [0.7, 1.5]

**Claim:** V_total_EH is monotone decreasing on [0.7, 1.5]. No local minimum exists
in this range. The compactification is not stabilized by Casimir + Freund-Rubin flux alone.

Physical consequence: ρ₆** is preserved as a zero of V^EH_Cas but is NOT a minimum
of V_total_EH (because V_flux contribution remains positive at ρ₆**).
The three-radius structure (ρ₆_min, ρ₆*, ρ₆**) is a property of ζ_FP in the 10D string
frame, not of the 4D EH potential.

**Evidence:** [VERIFIED] V_total_EH(0.7) > V_total_EH(1.0) > V_total_EH(1.3) numerically.
V^EH_Cas(0.95) > V^EH_Cas(0.8) — confirms 10D minimum does NOT transfer to 4D.
**Tests:** F4.5.1 (V_total decreasing), F4.5.2 (ρ₆_min not extremum in EH), F4.5.3 (ρ₆** not minimum of V_total)

---

## Numerical summary

| Quantity | Value | Frame |
|----------|-------|-------|
| V_int ∝ ρ₆¹² | exact | geometric |
| V_flux_const | ≈ 0.286 | 10D string |
| max |ζ_FP| on [0.7,1.5] | ≈ 0.00085 | 10D string |
| V_flux/|ζ_FP|_max | ≈ 330 | ratio |
| V^EH_Cas sign on [0.7, ρ₆**) | negative | 4D EH |
| V^EH_Cas sign at ρ₆** | zero | 4D EH |
| V_total_EH on [0.7, 1.5] | > 0, decreasing | 4D EH |
| Local minimum of ζ_FP at ρ₆_min | survives | 10D only |
| Local minimum of V^EH_Cas | NONE | 4D EH |

---

## What this does NOT mean

1. Does NOT close the compactification stabilization problem — additional physics required
   (gaugino condensation, D-branes, orientifolds, NS5-branes, or non-perturbative effects).
2. Does NOT imply ρ₆** is the physical compactification radius — it is a zero of V^EH_Cas
   but also a region where V_total_EH remains positive (flux contribution).
3. Does NOT change the status of λ = FREE_COUPLING_PARAMETER (G4 Fisher rank theorem).
4. Does NOT constitute SM derivation (sm_derivation_claimed = False).
5. Does NOT imply Tom Lawrence endorsement of any result.

---

## Claim entropy (Perelman)

| Source of uncertainty | Count |
|-----------------------|-------|
| Unsupported HIGH claims | 0 |
| Hidden assumptions | 1 (SW fit accuracy propagated from G54-D) |
| Missing negative controls | 0 |
| Ambiguous definitions | 0 |
| Unresolved blockers | 0 |
| **Total** | **1** |
