# Claim (round95 / E22) — L5 vs Pati-Salam "both sectors" tension

## L0 gate (EstimandOps)

**Question type:** Descriptive (classification of two already-established results
against each other) — NOT causal, NOT predictive. This experiment does not run a
new numerical computation; it re-reads two already-tool-verified derivations
(Lemma L5 / G74B, and round90/E21's Pati-Salam anomaly argument) at the level of
"what mathematical object does each one quantify" and asks whether those two
objects are the same invariant or different invariants.

## Zero-Signal Gate

- **Entity:** (1) Lemma L5 (`preprint.tex:886-912`), the S6-factor Atiyah-Singer
  index `sign(ind)=+1`; (2) round90/E21's corrected Pati-Salam cubic-`SU(4)^3`
  anomaly argument (`experiments/20260717-round90-pati-salam-gauge-completeness/
  decision.md` Sections 3-4), requiring `SU(2)_R`-doublet matter to coexist with
  `SU(2)_L`-doublet matter.
- **Falsifiable predicate:** either (a) L5's index and round90's anomaly
  requirement are statements about the SAME invariant (in which case L5's
  asymmetric result and round90's symmetric-coexistence requirement are in
  logical conflict), or (b) they are statements about logically independent
  invariants (in which case there is no conflict, only surface-level
  terminological overlap).
- **Measurable outcome:** trace exactly which mathematical object each
  computation is defined on (S6-factor-only vs S3-factor-only, per this
  project's own decoupled-operator ansatz `preprint.tex:135-140`), using only
  already-tool-verified project artifacts (G74B, E17 Section 1, round90 Section
  4) — a citation-level classification, not a new derivation.

Gate passes: entity, predicate, and outcome are all concrete and already named
in the task. Proceeding (no REFUSE).

## The precise frozen question

**Are Lemma L5's `S^6`-side chirality asymmetry (`sign(ind)=+1`) and the
`S^3`-side Pati-Salam "both sectors needed" argument (round90's corrected
version, resting on the cubic `SU(4)^3` anomaly) claims about the SAME
invariant, or about DIFFERENT, logically independent invariants?**

## Estimand (L1)

- **Population:** this project's own established derivation chain (G73, G74A,
  G74B/L5 on the S6 factor; E9, E12, E16, E17 on the S3 factor; round90/E21 on
  the Pati-Salam anomaly argument) — not the general Pati-Salam literature.
- **Intervention/comparator:** none (descriptive comparison of two existing
  results, not an experimental manipulation).
- **Endpoint:** classification of L5's `sign(ind)=+1` as counting either
  (a) a net topological index/generation-count on the S6 factor alone, or
  (b) a claim about per-generation `SU(2)_L`/`SU(2)_R` representation content
  on the S3 factor — with exact citations for whichever is found.
- **Summary measure:** a three-way verdict (see below), not a numeric estimate.
- **ICE:** none — this is a single-shot classification of pre-existing,
  already-frozen artifacts; there is no post-baseline event to strategize
  around.
- **MCID:** not applicable (categorical verdict, not an effect size).

## Natural-language statement

"We classify, using only this project's own already-tool-verified derivations
(G74B for L5, E17 Section 1 for S3 representation content, round90 Section 4 for
the corrected Pati-Salam anomaly argument), whether L5's `S^6`-index asymmetry
and round90's `S^3`-side anomaly-driven symmetry requirement are statements
about the same mathematical invariant or about different ones — and report
which, with exact citations."

## What this does NOT mean (pre-registered)

1. Does NOT re-derive or challenge G73/G74A/G74B/L5's own tool-verified result
   (`sign(ind)=+1`, `dim ker(D^+_{S6})=1`, `dim ker(D^-_{S6})=0` per channel) —
   reused by citation only.
2. Does NOT re-derive or challenge round90/E21's own tool-verified anomaly
   argument or its `BLOCKED` verdict on the coexistence question — reused by
   citation only.
3. Does NOT resolve H1c (which S3 `t`-sector, if any, is physically selected)
   or KT-8 (whether a stated 13D parent action exists) — these remain exactly
   as open as E7-E18 left them, regardless of this experiment's verdict.
4. Does NOT affect the `N_gen=3` headline claim (G73/G74A/G74B, S6-only),
   which round90 itself already noted is independent of the S3-side torsion-
   escape-route program this tension concerns.
5. A `TENSION_DISSOLVES` verdict, if reached, does NOT claim the two results
   can NEVER come into conflict in the future — only that, AS THIS PROJECT'S
   TEXT CURRENTLY STANDS, no established derivation links them into the same
   invariant. See Relaxation Map in decision.md for the contingency.

## Possible verdicts

- **`TENSION_DISSOLVES`** — L5's index and round90's anomaly requirement are
  claims about different, currently-unlinked invariants (S6-only net count vs.
  S3-only representation content); the apparent conflict rests on treating an
  informal naming convention as if it were an established cross-factor link.
- **`TENSION_CONFIRMED`** — a precise, tool-groundable derivation shows both
  claims are in fact statements about the same invariant, and the asymmetric
  vs. symmetric requirements genuinely contradict each other.
- **`BLOCKED`** — this project's own artifacts do not cleanly separate "index"
  from "representation content" enough to answer the question either way.

## Kill criterion

This experiment is FALSIFIED (i.e., the eventual verdict must be
`TENSION_CONFIRMED` or `BLOCKED`, not `TENSION_DISSOLVES`) if either of the
following is found on inspection:
- L5's own derivation (G74B) is shown to depend on, or fix, the S3-factor's
  `t`-parameter or `SU(2)_L`/`SU(2)_R` representation assignment anywhere
  (i.e., the decoupled-operator ansatz is violated or L5 secretly uses S3-side
  information) — this would make L5 NOT S6-only, undermining the "different
  invariants" reading.
- round90's Section 4 argument is shown to require only a WEAKER condition
  than S3-side representation-content symmetry (e.g., if other SU(4)-charged
  matter in this project's own content could absorb an anomaly imbalance) —
  this would not by itself confirm the tension, but would require re-deriving
  Question 3's count-vs-content equivalence from scratch rather than reusing
  the derivation below.

## Assumptions carried in (not re-litigated here)

- `D_full^2 = D_{S3,t}^2 ⊗ I + I ⊗ D_{S6,twisted}^2` (E2/E12's decoupling
  ansatz, `preprint.tex:135-140`) — presupposed exactly as E9-E21 presuppose it.
- E17 Section 1's representation-content table (`{ker D^{t=0}, ker D^{t=1}} =
  {(1,2),(2,1)}` exactly, under either labeling convention) — reused, not
  re-derived.
- round90 Section 3a's corrected cubic-`SU(4)^3` anomaly formula
  (`A(4,2,1)=+2`, `A(4̄,1,2)=-2`) — reused, not re-derived.
