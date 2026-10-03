# C219 — Claim: does the COMPUTED Dirac Casimir energy of S³×S⁶ (not a parametric C/ρ₃⁴) create a local minimum of the 2D (ρ₃,ρ₆) potential in the EFT-valid region?

**Date:** 2026-10-03
**FL tier:** [x] Full (research claim; touches the G54/G91-G93 modulus-stabilization chain)
**Question type (L0):** [x] descriptive — properties of an explicitly defined function V(ρ₃,ρ₆); no causal or predictive content.
**Origin:** hypothesis H8 of an externally generated list (2026-10-03), screened against the repo the same day.

## Why this round exists (read first)
Screen found H8 *as worded* ("a₂ heat-kernel correction cannot create a minimum") is mostly already covered:
G54-D/E/F computed the real ζ_FP **only along the 1D path ρ₃=0.986ρ₆²** (runaway confirmed there, G54-F), and
G91/G93 showed V_main has no 2D minimum. G92 then found a 2D minimum off the path **using a parametric
ansatz V_Cas = C/(Vol₃Vol₆ρ₃⁴ρ₆⁶) with C tuned** (C_crit=0.012415), minimum at ρ₃=0.32 (EFT-invalid). Nobody put
the **computed** ζ_FP(ρ₃,ρ₆) into the 2D landscape. That is the one real gap, and it is what this round tests.
G54 also extracted the S⁶ heat-kernel coefficients B₈,B₁₀ by least-squares fit (6-param −0.0033, 7-param −0.0029:
unstable at the 14% level) although they are exactly computable (Mellin transform of a polynomial multiplicity).

## Prior Result Gate
1. Exact claim: with Casimir = κ·ζ_FP(ρ₃,ρ₆) (computed), V_tot = V_main(G91/G92) + κ ζ_FP/(Vol₃Vol₆ρ₃³ρ₆⁶) has no local minimum with ρ₃>1, ρ₆>1.5 for |κ|≤1.
2. grep `null_results/INDEX.md`, `parked/INDEX.md`: G34-D1, G93 (flux path, no valid minimum), G92/G54-F as above; 0 hits for "computed Casimir 2D landscape".
3. Status: [x] NEW as a *combination* (computed ζ_FP × 2D landscape); constituents are G54-D/E/F and G92. Not a duplicate.
4. External novelty: [UNKNOWN] — Casimir/Dine–Seiberg stabilization literature is large; not scanned.

## Estimand
**Population:** the function V_tot(ρ₃,ρ₆;κ,μ) on ρ₃,ρ₆∈[0.3,6].
**Definitions (all re-stated, none imported):** D² spectrum on round S³_{ρ₃}×S⁶_{ρ₆}: λ²=(n+3/2)²/ρ₃²+m²/ρ₆², weights
W₃=2(n+1)(n+2), W₆(m)=16·C(m+2,5)=(2/15)(m⁵−5m³+4m), m=k+3. ζ(s)=ΣW₃W₆λ^{−2s}; ζ_FP = constant term of the Laurent
expansion at s=−1/2 (exact, via Mellin split + Poisson-exact K₃ + exact asymptotic K₆; both with and without the
(1/Γ)′ cross-term c·ψ(−½) reported, since which one G54 used is unknown).
**Casimir→V:** V_Cas = κ·ζ_FP/(Vol₃Vol₆ρ₃³ρ₆⁶) (G54-F/G92 convention V_EH=E_vac/V_int). κ is NOT derived: its sign and
size depend on dof counting and boson/fermion content; scanned, natural range |κ|∈[0.25,1] **[assumption]**.
**EFT-valid region (assumption, from G91/G93):** ρ₃>1 and ρ₆>1.5.
**MCID:** a local minimum (Hessian positive definite) strictly inside the valid region for some |κ|≤1.

## Falsifiable claims (pre-registered before running)
- **P0 (instrument, Gate 3 positive control).** Exact S⁶ coefficients: B₀=2/15 exactly; B₈,B₁₀ from the closed form lie within 25% of
  G54's fits (B₈≈−0.0076, B₁₀≈−0.0033). If not, G54's ρ₆* shifts and that is itself a finding (recorded, not hidden).
- **P1 (calibration vs G54-E).** Along ρ₃=0.986ρ₆², my independent ζ_FP reproduces ρ₆_min≈0.953, ρ₆*≈1.090 (c_{1/2}=0), ρ₆**≈1.4469
  within 0.02 / 0.01 / 0.02. **Negative control:** a deliberately wrong weight (W₆ with one term dropped) must NOT reproduce them.
  If P1 fails for BOTH FP definitions → verdict INSTRUMENT_UNCALIBRATED; no H8 conclusion is drawn (not evidence either way).
- **P2 (H8 narrowed).** For every κ∈[−1,1] (and μ∈{0.5,1,2}), V_tot has no local minimum in the valid region.
- **P3 (descriptive).** Report the minimal |κ| (either sign) at which any local minimum exists at all, and where it sits (ρ₃,ρ₆),
  to show how far the G92 minimum is from the valid region.

## Kill criterion
**REJECTED (H8 falsified)** if P2 fails: any local minimum in the valid region for |κ|≤1. **INSTRUMENT_UNCALIBRATED** if P1 fails.
P0 failure does not reject anything; it forces the discrepancy to be stated.

## What this would NOT mean
1. κ is a free assumption: P2 passing is "no minimum for |κ|≤1", NOT "no stabilization is possible".
2. Only the Dirac (fermionic) Casimir is computed; graviton/form-field/gauge-sector Casimir terms are absent (G92's bosonic C_crit would have to come from there).
3. Nothing about N_gen=3, OB1, torsion t (S³ is round: C134's torsion EOM puts t=1/2), or any ledger value changes.
4. V_main inputs (V_FLUX, A_NP, λ=1/3, ρ₆*=1.090) are imported from G91/G92 unverified here.

---

## Amendment A1 (2026-10-03, written BEFORE any run; original text above unedited)
While writing the script I computed the exact S⁶ coefficients by hand (Mellin: Σ m^{2k+1}e^{-ym²} ~ ½k!y^{-k-1}+Σ_j(−y)^j/j!·ζ(−2k−1−2j),
W₆=(2/15)(m⁵−5m³+4m)): B₈=−0.007646 (matches G54's fit), B₁₀≈−0.002952 (matches G54's 7-param fit −0.0029, NOT the 6-param −0.0033 that
G54-C used). With the exact B₁₀, G54's formula ρ₆*²=−A₂B₈/(A₀B₁₀C²) predicts ρ₆*≈1.15, not 1.09. [hand arithmetic, to be tool-verified]
Consequence for P1: pinning "reproduce ρ₆*=1.090±0.01" with exact coefficients would be a test that is **expected to fail by arithmetic**, not a test of the
instrument. P1 is therefore replaced by instrument checks that do not depend on G54's fit: (a) ζ_FP independent of the Mellin split point T (<1e-8 rel);
(b) the split-Mellin formula equals the brute-force double sum at a convergent s (s=3) to <1e-8; (c) feeding G54's own fitted B₈,B₁₀ into c_{1/2} reproduces ρ₆*=1.090±0.01
(tests my c_{1/2} formula); (d) negative control: dropping one term of W₆ breaks (a) or (b). P1': report ρ₆_min, ρ₆*, ρ₆** from the exact computation next to
G54-E's values with the discrepancy and its explanation (fit error in B₁₀) — a **reported difference, not a pass/fail**. Everything else in the claim is unchanged.

---

## Amendment A2 (2026-10-03, after the first run and the context-blind skeptic; originals unedited)
First run (pre-registered thresholds, results in `run_output.txt`): **P1a FAIL** (T-spread 9e-7 rel vs 1e-8), **P1b FAIL at s=6.3** (passes at s=8.1; diagnostics D2 show brute-sum
truncation, rel diff 2.9e-7 → 3.4e-8 → 2.8e-9 for N=220/400/800). Neither is relabelled as a pass. Skeptic (Step 8a) verdict **WEAKENED**; accepted points:
(1) μ∈{0.5,1,2} was pre-registered in P2 but never run → run in `c219_followup.py`; the μ branch had a wrong extra 1/μ (unused), fixed to the E=μ^{2s+1}ζ/2 convention;
(2) P2's PASS depends on the imported validity cut (ρ₃>1, ρ₆>1.5): for κ<0 a positive-definite minimum always exists at ρ₃≈0.44–0.62, ρ₆≈1.25 → reported as such, plus cut sensitivity;
(3) V_main is built on ρ₆*=1.090 (G54-C's fitted B₁₀); re-run with the exact ρ₆*=1.154;
(4) P1′: "min at 0.600" was the scan edge, replaced by an interior-extrema search; (5) the B₁₀ fit error explains ρ₆* only, not ρ₆** or the ζ values;
(6) convention caveat: κζ(−½)/V_int is the static Casimir energy; the Coleman–Weinberg 4D one-loop potential would involve ζ′(−2) of the internal operator (not computed, not claimed).
Skeptic's independent method (Poisson over S³ + Riemann-zeta/functional-equation for S⁶, no split point) gave ζ_FP(1.3,1.1)=−4.70868915e-4, identical to my code to all printed digits (tool-run by me).
