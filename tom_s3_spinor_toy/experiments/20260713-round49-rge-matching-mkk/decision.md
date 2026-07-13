# Round49-RGE Decision — Forward RGE running to the geometric string scale

**Date:** 2026-07-13
**Verdict: PROMOTE** (as a quantitative, tool-verified descriptive result;
does not resolve the underlying physical question of which scale/mechanism
reconciles the gap)

## Summary

Ran the forward-direction calculation that `preprint.tex`'s own existing
"RGE matching constraint" paragraph (backward-solve for M_KK) and G87's
own "Relaxation Map" (option A) both anticipated but never executed:
given PDG-known SM values at M_Z, run 1-loop RGE (same beta coefficients
already cited in the paper) up to the geometrically-predicted string
scale M_s = 1.7772×10^17 GeV (GA2), and read off the predicted coupling
ratio there.

**Result [VERIFIED-tool]:** pure 1-loop SM running predicts
g2²/g3²(M_s) ≈ 1.008, a **factor of 3.38x** away from G29's tree-level
geometric prediction of 15/(16π) ≈ 0.298. Stable to 0.2% across the PDG
1-sigma uncertainty on α_s(M_Z) (controls.md).

## Prior Result Gate corrections (found before running anything)

1. **Factual error caught and corrected**, in my own Round 48 recommendation:
   "GA2's M_KK≈1.78×10^17 GeV" conflated GA2's M_s (1.78×10^17 GeV, correct
   for M_s) with GA2's actual M_KK (1.9176×10^17 GeV, a different number).
   This round uses M_s throughout (see "Scale choice" below for why M_s,
   not M_KK, is the right scale here regardless).
2. GA1 (ROBUST verdict) confirms this scale is essentially λ-independent
   for RGE purposes (<0.3% shift across λ∈[0.15,0.60]) — GA2's own caveat
   3 ("does not map without λ fixed") does not block this calculation at
   the precision that matters (a 3.4x factor swamps a <0.3% uncertainty).

## Scale choice: M_s, not M_KK

G87 (2026-06-22, decision.md) already identified that G29's tree-level
ratio (computed at the equal-radii ρ3=ρ6=1 point) is naturally associated
with the string scale (ρ6≈1), calling it "the coupling scale," and
distinguished it from "the moduli minimum" (ρ6_min=1.179, where G87's own
formula gives a different ratio, 0.230). This round uses M_s — the
natural "ρ6≈1" scale — sidestepping G87's moduli-minimum number entirely.

**Correction — this is NOT a new pearl, checked `pearl_registry/INDEX.md`
before writing one (Prior Result Gate discipline, avoiding the exact
Round-46 duplicate-rediscovery mistake this project built the gate to
prevent).** G87's moduli-minimum calculation uses a trajectory formula
ρ3=κρ6 (κ=√(7/6) treated as a *slope*) — the same interpretation the
λ-nogo fix (Round 48B, commit `8c861ee`) found to be a mislabeling (κ is
actually a ratio of two ρ6 *values* on the potential, not a slope; the
physical trajectory is ρ3∝ρ6², not ρ3=κρ6). This was **already recorded**
in `pearl_registry/INDEX.md` on 2026-06-23 (row: "CANDIDATE Pearl
'ρ*≈ρ_coupling'... REFUTED. Analysis used G87 kappa-trajectory (ρ3=κρ6)
which was already marked STRUCTURALLY FLAWED... G29 equal-radii 4.2% IS
the structural prediction. Pearl does NOT exist."), status **CLOSED**.
My own suspicion on first reading G87 was directionally correct but
redundant — the project already knew this on the same day (2026-06-23)
G103's trajectory audit happened. What the pearl_registry entry does NOT
resolve: G87's own `decision.md` file itself was never annotated with
this closure, so a future reader of G87 alone (without cross-checking
pearl_registry) would not see it — the same "fix landed in one place,
never propagated to an adjacent record" shape as the Round 48B gaps, just
in `decision.md`↔`pearl_registry` rather than
`preprint.tex` body↔abstract. Not fixed here (out of this round's scope;
flagged in the final report as a small, optional Round 50-adjacent
cleanup, not a new pearl).

## Controls

All 3 positive controls (M_Z ratio, 1 TeV, 10 TeV forward-checks,
backward-solved M_KK) reproduced preprint.tex's own already-published
numbers within tolerance — see `controls.md`. One implementation bug
(inverted bisection direction) was caught by the M_KK positive control
failing on the first run, fixed, re-verified. Negative control confirms
discriminating power. No-collapse check confirms stability to PDG input
uncertainty.

## Kill Analysis

**What was tested:** whether pure 1-loop SM running "nearly closes" the
gap between G29's tree-level prediction and the SM value, when evaluated
at the geometrically-predicted scale (as opposed to the +4.3% gap at M_Z,
which is a different, smaller-looking number precisely because it's
comparing values at the SAME scale rather than running the geometric
prediction's own natural scale down through 35 e-folds of running).

**What was killed:** the optimistic framing in the Round 48 recommendation
("if pure-SM running nearly closes the 4.3% gap") — it does not; the
mismatch at the geometric scale is a factor of ~3.4x, not a small
percentage.

**What was NOT killed:** G29's own tree-level result (untouched, still
PROMOTE); the qualitative framing already in preprint.tex ("near-
electroweak-scale coincidence... not a precision GUT-scale prediction")
— this round's result is consistent with and sharpens that existing
honest framing, it does not contradict it.

**Relaxation Map (if this needs to be reconciled further):**
A. Identify a specific threshold-correction mechanism / new intermediate-
   scale particle content between M_Z and M_s that accounts for the 3.4x
   — not attempted here, would be a new, larger round.
B. Resolve the G87 pearl (correct trajectory for the moduli-minimum
   ratio) and check whether that scale/ratio pairing fares better —
   flagged, not attempted here.
C. Accept the mismatch as expected given the paper's own existing
   framing (already-caveated "near-electroweak-scale coincidence, not a
   precision GUT-scale prediction") and simply report the number.

## Recommended preprint action

Add the quantitative number to `preprint.tex`'s existing "RGE matching
constraint" paragraph (`sec:coupling`) as a citation-only addition (same
discipline as Round 48A/48B — no new claims beyond what this round
verified): state that forward-running from M_Z to the geometrically-
predicted M_s≈1.78×10^17 GeV gives ratio≈1.01, a factor of ~3.4x from
the tree-level prediction, replacing the implicit "not computed" gap
with an explicit number. This is a Round 50 candidate (small, citation-
only preprint edit) — not done in this round, per this project's own
"one round, one clearly-scoped deliverable" discipline; flagged for the
user to confirm before editing `preprint.tex` again.

**Round 50 (2026-07-13, applied, `main @ ` commit `742cb54`):** user
confirmed. Added the recommended paragraph to `preprint.tex`'s
`sec:coupling` (RGE matching constraint), citation-only, wording exactly
matching this round's tool-verified result (factor ≈3.4x, ratio(M_s)
≈1.01, stable to 0.2% across PDG uncertainty). Compiled clean, exit 0,
24 pages (unchanged). Feature branch
`docs/round50-rge-quantification-20260713` → `merge --no-ff` → branch
deleted, per standing workflow.

## Files

- `round49_rge_matching.py` — script, positive+negative controls inline
- `results_round49.json` — full numeric output
- `claim.md`, `controls.md` — this round's FL Standard-tier artifacts
