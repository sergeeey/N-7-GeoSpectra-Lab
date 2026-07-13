# Round49-RGE Claim — Forward 1-loop SM RGE running to the geometric string scale

**Date:** 2026-07-13
**FL tier:** [x] Standard
**Question type:** [x] descriptive

---

## Prior Result Gate (MANDATORY — fill BEFORE writing anything below)

1. Exact claim: what does pure 1-loop SM RGE running (from known M_Z values,
   using the beta coefficients already cited in preprint.tex) predict for
   g2^2/g3^2 at the geometrically-predicted string scale M_s (GA2), and how
   does that compare to G29's tree-level geometric prediction (15/16pi)?
2. `decision.md` grep: done. `experiments/20260708-dolan-casimir-g2su3/
   decision.md` lines 6441-6442, 6472-6496 — Round 48's own audit named this
   exact round as priority #1 (score 2.11), recommending "RGE-matching /
   M_KK threshold corrections", but had NOT verified the M_KK number it
   cited (see item 6 below).
3. `round*_claim.md` + scripts grep: done, 0 hits for an existing forward-
   direction RGE script anywhere in the repo (`git log -S"RGE matching"
   --all`, `Glob("experiments/*rge*")`).
4. `null_results/` + `parked/` grep: done, 0 hits for "RGE", "M_KK
   threshold", "RGE running", "one-loop running" in either INDEX.md.
5. `git log -S`/`-G` pickaxe: done. `git log -S"RGE matching" --all`
   finds only the existing backward-solve paragraph (commit `683a1e8`,
   "H3 RGE inversion") already in preprint.tex — no experiment folder,
   claim.md, or script backs it; it was written directly into prose.
6. Primary source re-read: done, direct Read (not paraphrase) of
   `experiments/20260626-ga2-m4-ms-units/decision.md` +
   `ga2_m4_ms_units.py` + `results_ga2.json`, and
   `experiments/20260626-ga1-lambda-sensitivity/decision.md`. **Found and
   corrected a factual error in the Round 48 recommendation itself**: the
   cited "GA2's own M_KK≈1.78×10^17 GeV" conflates two different GA2
   numbers — 1.78×10^17 GeV is GA2's **M_s** (string scale); GA2's own
   **M_KK** is 1.9176×10^17 GeV. GA1 (verdict ROBUST) independently shows
   this scale shifts by <0.3% across λ∈[0.15,0.60] — GA2's own caveat 3
   ("does not map to the SM coupling scale without λ fixed") is real in
   principle but quantified as negligible in practice by GA1.
7. **Status:** [x] OPEN (topic touched by G29's own caveat, G87's
   Relaxation Map "option A", and the preprint's existing backward-solve
   paragraph — all of which explicitly left this exact forward-direction
   calculation undone; independently re-confirmed still undone).

Also found during the gate: `experiments/20260622-g87-coupling-physical-
vacuum/decision.md` computes a "physical vacuum" coupling ratio (0.230)
using a trajectory formula ρ3=κρ6 that treats κ=√(7/6) as a slope — the
same interpretation the later λ-nogo fix (Round 48B, commit 8c861ee)
found to be a mislabeling. **Checked pearl_registry/INDEX.md before
treating this as new** (Prior Result Gate discipline): already recorded
2026-06-23, status CLOSED — "G87 kappa-trajectory... already marked
STRUCTURALLY FLAWED... Pearl does NOT exist." Not a new finding; see
decision.md for the one residual gap this surfaced (G87's own decision.md
was never annotated with this closure). This round does NOT use G87's
number and is not affected either way.

---

## Estimand

**Population:** the SM gauge coupling ratio g2^2/g3^2 as a function of
renormalization scale μ, under 1-loop running.
**Intervention:** evaluate the ratio at μ = M_s (GA2's geometrically-
predicted string scale, 1.7772×10^17 GeV) via pure 1-loop SM RGE running
from known M_Z boundary values, using the same beta coefficients
(b3=-7, b2=-19/6, MS-bar) already cited in preprint.tex.
**Comparator:** G29's tree-level geometric prediction, 15/(16π)=0.2984.
**Endpoint:** the ratio g2^2/g3^2(M_s), dimensionless.
**Summary measure:** factor mismatch = ratio_predicted(M_s) / ratio_geometric.
**MCID:** a factor of ≥1.5x is a qualitatively different finding from the
paper's current framing ("near-electroweak-scale coincidence... not a
precision GUT-scale prediction," i.e. already anticipating some mismatch);
below 1.1x would be a genuine near-closure of the gap.

---

## Claim

Pure 1-loop SM RGE running from M_Z to the geometrically-predicted string
scale M_s does NOT reproduce G29's tree-level ratio 15/(16π) — the mismatch
factor exceeds the MCID (1.5x) by a wide margin.

Supporting sub-claims:
1. The script's forward-RGE function, run at 1 TeV and 10 TeV, reproduces
   preprint.tex's own already-published values (0.362, 0.430) within 0.01
   — validating the method before trusting the new M_s-scale result.
2. The same function, backward-solved for μ, reproduces preprint.tex's
   own already-published M_KK≈130 GeV within 5 GeV.

---

## Kill criterion (MANDATORY — fill BEFORE running)

| Kill condition | Threshold |
|---|---|
| Positive controls (1 TeV, 10 TeV, backward-M_KK) fail to reproduce preprint.tex's own published numbers | any control off by >0.01 (ratios) or >5 GeV (M_KK) |
| PDG-derived M_Z ratio does not match preprint.tex's own stated 0.2865/0.287 | off by >0.01 |
| Negative control (deliberately wrong α_s input) fails to be flagged as wrong | discriminating power lost |

If FAIL → kills: the calculation method itself (wrong beta-function sign
convention, wrong PDG inputs, or an implementation bug) — STOP, do not
report the M_s-scale result.
If PASS → survives: the M_s-scale factor-mismatch number becomes a
tool-verified, reportable quantitative result.

---

## Checks planned

- T1: cross-check PDG-derived α2⁻¹(M_Z), α3⁻¹(M_Z) reproduce preprint.tex's
  stated M_Z ratio (0.287).
- T2 (positive control): reproduce preprint.tex's own published 1 TeV
  (0.362) and 10 TeV (0.430) forward-check values, and its own backward-
  solved M_KK≈130 GeV.
- T3 (negative control, adversarial): deliberately corrupt α_s(M_Z) input
  by ~10% and confirm the resulting M_Z-ratio cross-check correctly flags
  it as wrong (discriminating power).

---

## What this does NOT mean

1. Does NOT claim M_s is definitively "the" correct coupling-matching
   scale — G87 separately found the moduli-minimum scale gives a
   different ratio (0.230) on its own (since-questioned) trajectory
   formula; this round does not resolve which scale is "correct," only
   quantifies the mismatch under the M_s identification G87 itself
   suggested as most natural.
2. Does NOT identify a specific threshold-correction mechanism or new
   particle content that would close the gap — only quantifies its size.
3. Does NOT depend on λ being fixed in any way that matters at this
   precision (GA1's <0.3% scale-shift is far below the ~3x mismatch
   found here).
4. Does NOT re-derive or challenge G29's tree-level result itself.

---

## Fence (do not change without postmortem)

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

See `decision.md`.
