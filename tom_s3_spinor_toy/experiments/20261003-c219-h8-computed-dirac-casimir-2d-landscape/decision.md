# C219 Decision — computed Dirac Casimir of S³×S⁶ in the 2D landscape (hypothesis H8, narrowed)

**Date:** 2026-10-03
**Verdict:** **PROMOTE (WEAKENED)**, split by finding (skeptic Step 8a: WEAKENED; all points accepted, see § 3):
- **F1 (strongest, [VERIFIED-tool], independent method):** G54-C's fitted S⁶ heat-kernel coefficient B₁₀=−0.0033 is 12% off the exact −0.0029521; hence the UV-finite point is **ρ₆\*=1.154, not 1.090** (UV ray ρ₃/ρ₆=1.138, not 1.0743).
- **F2:** G54-E's three-radius map is **not numerically reproduced** (qualitatively it is).
- **F3 (H8 narrowed, weak):** with the computed ζ_FP and |κ|≤1 there is no local minimum in the imported valid region; this rests on the imported cut and on the unknown κ.
**Not established:** that the potential cannot be stabilized in the valid region (κ is free; only the Dirac Casimir is in); anything about N_gen=3, OB1, torsion, or any ledger value.
N=1 independent re-implementation + 1 independent-method point check (skeptic's, tool-run by me).

Numbers trace to `c219_computed_casimir_landscape.py` (`run_output.txt`, `results_c219.json`), `c219_diagnostics.py` (`run_output_diagnostics.txt`), `c219_followup.py` (`run_output_followup.txt`, `results_c219_followup.json`).

## 1. Results against the pre-registered claims

| Claim | Result |
|---|---|
| P0 exact B₀=2/15; B₈,B₁₀ within 25% of G54 fits | **PASS**: B₈=−0.0076455 (0.6% from fit), **B₁₀=−0.0029521** (11.8% from the 6-param fit −0.0033; agrees with G54's own 7-param −0.0029) |
| P1a ζ_FP independent of split T, <1e-8 rel | **FAIL as registered**: spread 9.2e-7 rel (≈4e-10 abs) over T∈{0.03,…,0.2}·min(ρ)². Diagnostics D1: 4e-10 abs at the smallest T (floating cancellation), 2–7e-11 abs at moderate T. Not relabelled; the practical precision (≈1e-10) is ≪ the 1e-4…1e-3 scale of every conclusion, and an independent method (skeptic's, no split point) gives ζ_FP(1.3,1.1)=−4.70868915e-4, identical to my code to all printed digits |
| P1b Mellin = brute double sum | s=6.3 **FAIL as registered**, s=8.1 **PASS** (1e-9). D2: the brute sum is truncated, rel diff 2.9e-7→3.4e-8→2.8e-9 for N=220/400/800 (∝N^−3.6, as the tail exponent predicts). Skeptic: P1b is a weak check of B₁₀ (its error shifts ζ at s=6.3 by ~3e-9); the real coefficient validation is P1a (a B₁₀ error of 12% would give ~2.5e-4 T-spread, observed ~1e-11) |
| P1c G54's fitted B₈,B₁₀ in my c_{1/2} give ρ₆\*=1.090±0.01 | PASS (1.0883) — close to an algebraic identity (two-term formula), not an instrument test |
| P1d negative control (drop a W₆ term) breaks the match | PASS (rel diff 1.9e-3) |
| P1′ radii along ρ₃=0.986ρ₆² (reported, not pass/fail) | interior local **max at ρ₆=0.765**, local **min at ρ₆=0.92** (ζ_FP=−6.78e-4), zero at **ρ₆≈1.367** (with ψ term; 1.3625 without). G54-E: min at 0.953 (−8.63e-4), zero at 1.4469. ρ₆\* (c_{1/2}=0): 1.154 vs G54's 1.090 |
| P2 no local minimum in valid region (ρ₃>1, ρ₆>1.5) for \|κ\|≤1, μ∈{0.5,1,2}, both FP definitions | **PASS** (36 of 36 combinations, `run_output_followup.txt` B), **narrowed**: see § 2 |
| P3 descriptive thresholds | see § 2 |

## 2. What P2 does and does not say

- For **κ>0** there is no local minimum anywhere in [0.35,8]² (all μ, both FP definitions).
- For **κ<0** (the sign a net fermionic Casimir would give; κ itself is NOT derived) a positive-definite-Hessian minimum **always exists**, e.g. κ=−1 at (ρ₃,ρ₆)=(0.625,1.252), V=−2.4e-5; κ=−0.05 at (0.441,1.255). Its ρ₆≈1.25–1.34 is just where V_main is lowest at fixed ρ₃; the Casimir term only adds a wall against small ρ₃. **P2 passes only because of the imported cut ρ₃>1** (from G91/G93, not re-derived here). With a cut of ρ₃>0.6 it would fail.
- Valid-region minima appear for the attractive sign only in a window: |κ|≈43–70 (V_main with ρ₆\*=1.090) or ≈29–70 (with the exact ρ₆\*=1.154); none for the repulsive sign up to 400. Existence is **not monotone in κ** (my first bisection assumed it and was wrong; replaced by a scan). Thresholds are grid-limited (70-point log grid; positions snapped to the grid, refined e.g. (1.085,1.524) at κ=−42.6, V=−1.08e-6, Hessian PD).
- μ axis is live (ζ_FP at (2.22,1.5) is +4.7e-4/−4.3e-4/+1.4e-3 for μ=1/0.5/2), but it does not change the position of any minimum at 2 decimals.
- Compare G92: its parametric Casimir gave a minimum at ρ₃=0.32; the computed Casimir gives 0.44–0.64 (still invalid).

## 3. Skeptic Response Matrix (verdict WEAKENED)
- μ axis never run → **Accepted**, run in `c219_followup.py`; the μ branch had a wrong extra 1/μ (unused) → fixed.
- PASS depends on the validity cut → **Accepted**, stated in § 2; cut sensitivity reported.
- V_main uses the fitted ρ₆\*=1.090 → **Accepted**, re-run with 1.154 (§ 2).
- "min at 0.600" was the scan edge → **Accepted**, replaced by interior extrema (max 0.765, min 0.92).
- B₁₀ fit error explains ρ₆\* only → **Accepted**: feeding G54's fitted B₈,B₁₀ into my ζ_FP moves the zero from 1.367 to only 1.392 (30% of the gap to 1.447) and the ζ values stay offset by ~2e-4 (D4; D4 itself is ill-posed — fitted coefficients plus an exact tail break T-independence). The remainder is **[UNKNOWN]**; candidate cause not tested: G92's docstring writes the S³ degeneracy as 2(n+1)², which is not a valid Laplace-type spectrum on S³ — if G54 used it, that would be G54's error.
- P1a/P1b thresholds → **Accepted**, reported as FAIL, not loosened; D1/D2 are post-hoc diagnoses (Amendment A2).
- Convention caveat (κζ(−½)/V_int is the static Casimir energy; the 4D Coleman–Weinberg potential would involve ζ′(−2) of the internal operator, no pole, no μ) → **Accepted**, not computed here.
- "Amendment A2" cited by the diagnostics before it existed → **fixed** (A2 now in claim.md).
- Box coverage ([0.37,5.7]² in the first run) → widened to [0.35,8]²; ρ₆>8 unchecked; skeptic's analytic argument covers ρ₃≫ρ₆ (any stationary point in ρ₃ there is a maximum for ρ₆>ρ₆\*).
- Cosmetic: D5 header says L-BFGS but uses Nelder–Mead; dead `worst` placeholder.

## 4. Kill Analysis
H8 as originally worded ("no minimum for any admissible sign") was **not falsified but is not what was tested**: a minimum exists for the attractive sign wherever the cut allows it. What survives: P2 for |κ|≤1 inside the imported cut. What does **not** survive as a claim: "the runaway is robust to Casimir corrections" in general.

## 5. Consequences / audit items (NOT executed here)
1. **ρ₆\*=1.090 is a fit artifact of G54-C's B₁₀** (exact → 1.154; G57's ray 1.0743 → 1.138). The constant `1.090` is hard-coded in G70, G77, G82, G84c, G85b, G88a, G88b, G91, G92 (grep, `.py` under experiments/). Whether their conclusions move was **not assessed** (e.g. A_NP=V_FLUX·exp(λ/ρ₆\*²) changes by ~3%).
2. G54-E's three-radius numbers (0.953/1.090/1.4469) should be read with this round's discrepancy; pointer lines appended to G54-C, G54-E, G57 (original text untouched).
3. `CLAIM_LEDGER.yaml` was NOT touched (peer session owns it); an entry for C219 is pending.

## 6. What this does NOT mean
κ unknown; bosonic/graviton/form-field Casimir terms absent; S³ round (C134 puts t=½); EFT-valid cut imported; G54-E not "refuted", only not reproduced with exactly computed coefficients and an independently verified machinery.

## 7. Reviewer note
Independent review: context-blind `skeptic` (WEAKENED). The skeptic could not execute code; its numbers are hand arithmetic except its independent-method script, which I ran (ζ_FP(1.3,1.1) match above). `reviewer` cap closed this session → skeptic fallback per policy, substitution stated.

## 8. Reproduction
```
cd experiments/20261003-c219-h8-computed-dirac-casimir-2d-landscape
python c219_computed_casimir_landscape.py   # 6 pass, 2 FAIL (P1a, P1b@6.3), as registered
python c219_diagnostics.py
python c219_followup.py
```
Full pytest (before the last edits to c219 scripts, which are not collected by tests): 2583 passed, 4 skipped. `ruff` clean on the folder.
