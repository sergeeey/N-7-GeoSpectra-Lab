# Research audit report — 2026-10-21

Scope: items A (C78), B (Track A statistic), G102 dimensions, C (Structural Twin, one protocol plus a worked pair check), and D (one null/verdict audit). Evidence tags follow `EVIDENCE_LEDGER.md`. Nothing here re-certifies a repo verdict unless marked PASS by a script run in this pass.

## 1. Track A — "48 sigma"  (B)

**Reproduced:** the published means and errors give z ≈ 8.07 under independence (difference −0.4950, SE 0.06136). [VERIFIED-tool, awk]

**New finding — the slope SE is not what the report says.** The FSS slope for spectral_circle (`reports/SPECTRAL_CIRCLE_EXTENDED_ANALYSIS_v0.1.24.md`, appendix) is fitted on **three points** (N = 16, 64, 128; mean log IPR per size). With the per-size IPR values printed in that appendix (0.267, 0.172, 0.129), an OLS fit gives:

- slope = −0.345, SE = 0.024, df = 1 [VERIFIED-tool, awk]
- the report states −0.4844 ± 0.0546, R² = 0.99

So the printed slope is **not reproduced** by the printed per-size values. The sign (negative) and the qualitative drop of IPR with N survive. The magnitude and the ±0.0546 error do not. A 3-point fit with df = 1 gives an SE that is not a credible basis for a "HIGH confidence" classification.

**Origin of 48:** not found. No repo file contains a computation that yields 48; the only occurrence is the sentence in `GATE4B_SPECIFICITY_VERDICT_v0.1.24.md:68`. Arithmetic check: 48 needs a denominator of about 0.0103 for a 0.495 difference, and no reported SE equals that. [UNKNOWN] origin.

**Also weakens the verdict:** the "reproduced on 2 independent grids" claim (`GATE4B_...:70`) compares a 54-case and an 18-case run of the same spectral_circle code, not independent data; the two slopes differ by 2.1% but both rest on the same 3-point fit form. Not established as independent.

**Status:** direction (spectral_circle IPR decreases with N, ring flat) is plausible from the appendix; the "48 σ" number, the ±0.0546 SE, and "HIGH confidence" are not supported by the printed numbers. Needed: per-case raw data for the 54-case and 18-case runs and a fit with ≥5 sizes and per-seed errors.

## 2. C78 — so(8) commutant of the physical D  (A)

Reproduced at HEAD and at its own commit `c4f8d40` (scratch worktree):

- commutator-map rank = 20, nullity = 8 on the 28-dim so(8) basis; su(3) residual ≈ 3.5e-15 [VERIFIED-tool]
- leading singular value 26.3698 at both HEAD and c4f8d40

**Spectrum mismatch — diagnosed.** The committed `results_c78.json` lists leading singular value 28.2598 and other values that are not a uniform rescaling of the rerun (ratios 1.07, 1.006, 0.979 for successive entries). So the stored file was **not** produced by the committed script at its commit. Rank and nullity agree; the stored spectrum is not reproducible from `c78_so8_commutant_exhaustive.py`. [VERIFIED-tool]. Cause of the stored file's origin: not established (it may come from an earlier uncommitted variant). Action: cite rank/nullity only; regenerate the JSON from the committed script.

**Scope limit (unchanged):** this is a fiber-level statement about a fixed operator D acting through U_v. It does not decide global symmetries of the full geometric operator (base action, sections, connection). No exact-arithmetic certificate exists. Status: NUMERICALLY SUPPORTED.

## 3. G102 dimensions  (G102)

Rerun of `experiments/20260705-g102-spin8-fiber-obstruction/g102_spin8_fiber.py` at HEAD: PASS. Der(O) dim 14, stabiliser dim 8 (su(3)), centraliser of g₂ in so(8) = 0, centraliser of su(3) in so(8) = 2 (abelian). [VERIFIED-tool]

Representation-theory cross-check (independent of the code): so(8) = 14 ⊕ 7 ⊕ 7 as g₂-modules, with no trivial summand, so the g₂-centraliser is 0. Under su(3) ⊂ g₂, 14 → 8 ⊕ 3 ⊕ 3̄ and 7 → 3 ⊕ 3̄ ⊕ 1, so the su(3)-centraliser in so(8) is 2-dim. [DOCS-level derivation, consistent with the tool output]

Note from the script's own text: the fiber-level symmetry analysis gives "no fiber symmetry beyond g₂" and the Spin(8) channel structure is not derivable from the fiber alone. That is a stated limitation, not a new result.

## 4. C — Structural Twin (protocol and one check)

No constructed twin pair in the relevant class was produced. What is in hand:

- The pair spectral_circle vs ring in Track A has **matched** invariants (same N grid, same disorder W, same seeds in the design) but a claimed different slope. Whether the invariants are exactly matched and whether the slope difference survives a proper fit is exactly the open question in §1. Until §1 is resolved, this pair cannot be used as a twin.
- The C78 vs G102 pair: they share the so(8) commutant dimension 2 vs 8 on different objects (the 2-dim centraliser of su(3) in G102 vs the 8-dim commutant of D in C78). These are different objects, not a twin.

**Protocol for the next twin search (one row per pair):** (a) fixed invariants stated before data (N, W, seed set, basis, normalisation); (b) the property tested stated as a number with its SE; (c) cause recorded only if a control shows it; (d) "physical admissibility" marked separately. Matrices built only to be diagnostic are labelled DIAGNOSTIC, not geometric models.

## 5. D — null/verdict audit (one item)

Chosen: the Gate 4B Level-3 "discretisation dependence" verdict. Checked: the statistic (§1), the 3-point fit (§1), the independence claim (§1). Result: the verdict's sign survives; its confidence level and σ-count do not survive as written. Reclassified as **INCONCLUSIVE at stated confidence** until a fit with ≥5 sizes and per-case errors is run. The other null results in `null_results/INDEX.md` were not audited in this pass.

## 6. Not done

- Global-symmetry bound for the full operator (A).
- Exact certificate for the 64-dim construction (A).
- Audit of the remaining null results (D), and the discovery list beyond §7.
- Regenerating `results_c78.json` from the committed script (left as-is; reference file restored).

## 7. Next experiment with highest expected value

Re-fit the spectral_circle FSS with sizes 16, 32, 64, 128, 256 (ideally 512) and per-seed errors, with the 3-point fit and the 48σ claim both replaced by that fit. Cost: one run of the existing Gate-5 pipeline class (`scripts/run_gate5_fss_v0.1.25.py`, pre-registered). It decides whether the only discretisation contrast in Track A survives.

## Files changed in this pass

- `audit_2026-10-21/RESEARCH_AUDIT_REPORT.md` (this file), `EVIDENCE_LEDGER.md`, `DISCOVERY_OPPORTUNITIES.md` (new).
- No experiment reference file is modified (C78 JSON and G102 JSON were restored by `git checkout`).
