# Round52-GrowingGap Claim — premise audit for the L4B "growing-gap" argument

**Date:** 2026-07-13
**FL tier:** [x] Standard (premise audit — no new Dirac-operator matrices, per explicit user scope constraint)
**Question type:** [x] descriptive

---

## Prior Result Gate (MANDATORY — fill BEFORE writing anything below)

1. Exact claim: does the "Casimir gap grows unboundedly while the torsion
   correction is a fixed, bounded fibre operator" premise (colloquially
   "Round 6", `decision.md:393-397`) hold for G₂ representations beyond
   ρ=7,14 — tested WITHOUT building the full Dirac-operator matrices for
   ρ=27,64,77 (explicit user constraint for this round).
2. `decision.md` grep: done. Growing-gap text at `decision.md:393-397`
   (original), restated `:2017-2020` (Round 16). Self-flagged as
   "inherited, not re-derived" at `:2998-3000` (Round 19 skeptic) and
   `:3024-3027` (Round 20). Round 48's own shortlist flags it
   "unverified" at `:6479`.
3. `round*_claim.md` + scripts grep: done. No prior round attempted a
   rho-scaling audit. Existing calibrated tools found and reused:
   `experiments/20260625-kp-zero-mode/kp_zero_mode.py` (g2_casimir,
   su3_casimir, g2_dim, su3_dim, S⁺⊗S⁻ fibre decomposition — 2296-tests
   calibrated per its own docstring).
4. `null_results/` + `parked/` grep: done, 0 hits for growing-gap/
   monotonic/rho-scaling anywhere.
5. `git log -S`/`-G` pickaxe: done, confirms no prior attempt exists.
6. Primary source re-read: done — preprint.tex §sec:schur (L4B, lines
   668-736), Round 22's torsion cross-term derivation (decision.md
   :3317+), all read directly (not paraphrased) before writing this claim.
7. **Status:** [x] OPEN → this round.

**Critical finding from the gate itself**: ρ=27, 64, 77 were never
defined anywhere in this project — Round 48's shortlist listed bare
dimension numbers with no Dynkin labels. Resolved in this round (Step 1
of the script): 27=(2,0) unique, 64=(1,1) unique, but **77 is
genuinely ambiguous** — both (0,2) [C₂=20] and (3,0) [C₂=16] are
inequivalent G₂ irreps of dimension 77.

---

## Estimand

**Population:** the "growing-gap" premise underlying the L4B mechanism
(Kostant-Parthasarathy formula on G₂/SU(3)), specifically its
applicability to G₂ representations ρ beyond the two already-checked
cases (ρ=7,14).
**Intervention:** decompose the premise into its two logically separate
sub-claims (A: Casimir gap growth; B: torsion-correction boundedness)
and test each using only already-calibrated, existing project tools —
no new per-representation matrix construction.
**Comparator:** the two already-established base cases, ρ=7 (established)
and ρ=14 (strongly supported).
**Endpoint:** whether sub-claims A and B are provable, disprovable, or
neither, at this audit's cheap tier.
**Summary measure:** PASS/FAIL/UNRESOLVED per sub-claim.
**MCID:** N/A — descriptive premise audit.

---

## Claim

Sub-claim (A) — "C₂(G₂;ρ) grows unboundedly, and in particular never
returns below the fixed fibre's max Casimir (3)" — is TRUE and provable
unconditionally, for ALL nontrivial G₂ representations, via elementary
algebra on the already-calibrated Casimir formula (no scan needed,
though a wide scan is included as a sanity check).

Sub-claim (B) — "the torsion correction stays a fixed, bounded fibre
operator as ρ grows" — is NEITHER provable NOR disprovable at this
audit's cheap tier: zero data exists anywhere in this project beyond
the two closed, ρ-specific constructions at ρ=7 and ρ=14, and no
scaling law is derivable from existing tools without exactly the kind
of per-representation construction this audit was designed to avoid.

---

## Kill criterion (MANDATORY — fill BEFORE running)

| Kill condition | Threshold |
|---|---|
| Positive control (reproduce kp_zero_mode.py's own ρ=7 numbers: C₂=4, gap=1) fails | any mismatch |
| Hand-proof of min C₂(G₂;ρ)=4 contradicted by a wide computational scan | any (m,n)≠(0,0) found with C₂<4 |
| dim=77 ambiguity assertion fails (expected exactly this ambiguity per the gate-check) | ambiguity not confirmed |

If FAIL → kills: the elementary algebraic argument itself (an error in
the case analysis) — STOP, do not report Step 2/3 results.
If PASS → survives: sub-claim (A) becomes an established, general,
unconditional result; sub-claim (B) remains explicitly unresolved (not
addressed by this audit's kill criterion, since no cheap test for it
exists — see "What this does NOT mean").

---

## Checks planned

- T1 (positive control): reproduce `kp_zero_mode.py`'s own published
  ρ=7 Casimir/gap values exactly.
- T2 (the core result): elementary case-analysis proof that
  min C₂(G₂;m,n)=4 over all nontrivial (m,n), stated in closed form
  (not a finite scan).
- T3 (sanity check on T2, not a substitute for it): computational scan
  over (m,n)∈[0,60)² confirming no counterexample to the T2 bound.
- T4 (adversarial/negative): explicitly search for whether ρ=27/64/77's
  dimension labels are unambiguous — found they are NOT (77 collides).

---

## What this does NOT mean

1. Does NOT establish or refute the full growing-gap premise as
   originally stated — only its Casimir-growth half (A). The torsion-
   boundedness half (B) is explicitly left open, not resolved.
2. Does NOT license computing the full Dirac-operator spectrum for
   ρ=27, 64, or either 77-label — per the user's explicit scope
   constraint for this round.
3. Does NOT mean sub-claim (B) is false — only that no evidence exists
   either way at this project's current state of tooling.
4. General Weitzenböck-formula caution (not project-specific, a field
   observation, not asserted as fact about THIS torsion term): torsion/
   curvature-correction terms in Weitzenböck-type formulas typically DO
   scale with representation-theoretic data of the bundle they act on
   in the general theory — this is a reason for caution about assuming
   "fixed, bounded" as a safe default, not a proof that this project's
   specific torsion term behaves that way.

---

## Fence (do not change without postmortem)

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

See `decision.md`.
