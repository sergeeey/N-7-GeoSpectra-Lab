# C219 audit A3 — S⁶ heat-kernel fits and the ρ₆\* = 1.090 constant: what depends on them

**Date:** 2026-10-03. Scripts: `c219_rho6star_sensitivity.py` (output: `run_output_sensitivity.txt`). Nothing in the repo outside this folder was modified by the scripts; addenda to G91/G92/G94 `decision.md` are append-only.

## 1. Where the fit lives
Ten test files each carry their own copy of the same least-squares fit of K_{S⁶}(τ) (`_sw()` / `_sw_s6_full()` / `_sw_s6_coefficients()`), run on a fixed τ-grid with a basis truncated at τ². Output of the fit vs the exact Mellin coefficients (`run_output_sensitivity.txt`, part A):

| file(s) | B₈ (exact −0.0076455) | B₁₀ (exact −0.0029521) |
|---|---|---|
| g54b (5-param, no B₁₀) | −0.010734 (+40%) | — (already superseded by G54-C's own text) |
| g54c, g54d, g54e, g54f, g55, g56, g57, g58, g60 (identical copy-pasted fit) | −0.007621 (−0.3%) | **−0.003302 (+11.8%)** |

All downstream fit users therefore inherit ONE error, not ten independent ones. Their test expectations (ρ₆\*=1.090, ρ₆_min=0.953, ρ₆\*\*=1.4469, C_UV=1.0743) were produced by the same fit, so those tests cannot detect it. Dense re-sampling does not cure it (replicated: 25 points → B₁₀ −0.00328, 11.2%); adding a single τ³ term to the basis does (−0.002932, 0.7%), so the cause is basis truncation.

## 2. How much do downstream results move? (ρ₆\* 1.090 → 1.1541)
`1.090` is hard-coded in 21 experiment scripts (G70, G77, G82, G84c, G85b, G88a/b/d/e/f, G91, G92, G93, G94, GA1, G103, G104, G105, round63 ×3). It enters V_main through A_NP = V_FLUX·exp(λ/ρ₆\*²). A_NP changes by only −3.0%, **but V_main = V_FLUX·(1 − exp(λ(1/ρ₆\*² − 1/ρ₆²))) vanishes at ρ₆\* and the minimum sits next to that zero, so the small change in A_NP is a large change in the potential near the minimum.** Measured by running copies of the scripts with the constant replaced (crude diff of printed numbers):

| quantity (script) | ρ₆\*=1.090 | ρ₆\*=1.1541 |
|---|---|---|
| AdS-minimum radius ρ₆_min (G70, G82, round63) | 1.179 | 1.248 |
| V_min (round63) | −2.53e-6 | −1.13e-6 (−55%) |
| m_mod/m_KK, G91 headline | 0.198% | 0.149% (−25%) |
| canonical mass ratio (G82, G88a) | 0.2517% | 0.1787% (−29%) |
| m²_KK (G91) | 0.161 | 0.065 (−60%) |
| G94 PATH+EFT window, K at ρ₃=1.9281 | present | window shifts (ρ₃≈2.02 at the same row); rows previously "saddle" become valid |
| G88d/e/f max change of any number | — | 33% |
| G84c | — | 0 |

What did **not** move: existence of the AdS minimum, signs, the G66 positive control κ²=7/6 (1.1701 → 1.1697), the qualitative picture. What moved: every absolute number that depends on the minimum's location and depth, by 25–60%.

**Caveats of this measurement.** (a) The diff compares any number on a changed output line, so single large "max relative change" values (G92: 1e5, round63_corrected_v2: 3.4) are near-zero quantities, not headline effects. (b) **G92's patched run is invalid**: it hard-codes the old G91 minimum (RHO6_MIN_G91, V_MIN_G91), so its output mixes new A_NP with stale reference values; only its qualitative status is untouched. (c) G77 and round63_route_a failed to run cleanly when patched, G105 failed in both copies (missing sibling file); not assessed. (d) Other constants (C_SM=0.986, λ) were not varied; C_UV=1.138 with C_SM=0.986 is consistent with ρ₆\*=1.154.

## 3. Statements elsewhere that carry the old numbers (NOT edited)
`README.md:226` and `:238` (ρ₆_min = 1.179), `docs/load_bearing_formulas.md`, `docs/gates_tracker.md`, G91/G92/G94/GA1/G103/G104/round63 decisions, `pearl_registry/INDEX.md`. The repo is public. Whether the "zero-fit" wording of the ρ₆_min headline survives is a question for the owner: the value inherits a *fitted* B₁₀ (the final potential has no free parameter, but one of its inputs was a numerical fit).

## 4. Separate finding: G92's "literature" Dirac Casimir constant
`g92_s3_casimir.py:193`: `c_dirac_theoretical = -11.0/240.0` (comment: Camporesi–Higuchi). Hurwitz-ζ computation (this round): Σ(n+1)(n+2)(n+3/2) = −17/960 exactly (the standard Weyl-fermion Casimir energy); the Dirac value is 17/480 or 17/960 in magnitude, not 11/240. G92's plausibility ratio C_required/|C_Dirac| = 0.27 becomes 0.35 or 0.70. Qualitative conclusion unchanged; the number was cited, not computed.

## 5. Not done
Re-derivation of G91–G94 with ρ₆\*=1.154 as a proper round (the numbers in § 2 are patched-constant reruns, not re-derivations; G92's needs the new G91 minimum), edits to README/docs/ledger values, and an audit of fits outside the heat-kernel family (91 files call `lstsq/polyfit/curve_fit`; only the ten above fit S⁶ heat-kernel coefficients).
