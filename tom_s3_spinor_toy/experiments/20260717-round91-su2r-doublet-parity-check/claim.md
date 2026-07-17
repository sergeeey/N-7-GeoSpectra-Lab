# E21-followup (round91) — Claim

## Zero-Signal Gate

- **Entity:** the specific `t=0` sector of this project's own S³ torsion-
  connection family `∇^t` (E2/E7/E9-E17), combined with `G73`'s 3 triality
  channels and `G74A`'s (now `dolan-casimir-g2su3`/`round59`-attributed,
  provenance-corrected) `S⁶`-side twisted-Dirac kernel.
- **Falsifiable predicate:** the number of `SU(2)_R` doublets this specific
  content supplies is either EVEN or ODD — a definite integer parity, not a
  vague "some" or "enough."
- **Measurable outcome:** count the joint-kernel dimension per channel from
  this project's own already tool-verified numbers, divide by 2 (doublet
  size), sum/compare across channels, and read off the parity. PASS/FAIL/
  BLOCKED criteria below.

Gate passes — proceed.

## L0 classification (EstimandOps)

**Descriptive.** This is a bookkeeping/arithmetic exercise over already-
established numbers (`dim ker(D_{S3,t})`, `dim ker(D_{S6,twisted})`, channel
count) — no new measurement, no causal claim, no prediction about
unobserved data. The question is: "does this project's own text, taken on
its own terms, currently specify enough to determine a parity, and if so
what is it?"

## Background (reused, not re-derived)

- Round90 (E21, `experiments/20260717-round90-pati-salam-gauge-completeness/
  decision.md`) found `SU(2)_R` is genuinely gauged in `preprint.tex` (a real
  4D gauge boson from the KK spin-connection mechanism), triggering Witten's
  `SU(2)` global anomaly (`Phys. Lett.` B117, 324, 1982): a gauged `SU(2)`
  with charged matter requires an EVEN number of doublets. Verdict: `BLOCKED`
  (full `SU(4)` unification not geometrically realized, gate G97). Relaxation
  Map's cheapest next step (not attempted there): "Check whether the
  NARROWER `SU(2)_R`-only Witten-anomaly argument suffices WITHOUT full
  `SU(4)` — would require explicitly verifying the `SU(2)_R` global-anomaly
  (even-doublet) condition using ONLY this project's own already-established
  fermion content."
- E16 (round83) tool-verified (`PASS__ONE_WEAK_ISOSPIN_DOUBLET__NARROW_SCOPE`):
  the 2-dim joint kernel `ker(D_{S3,t})⊗ker(D_{S6,twisted})`, for one fixed
  channel, is one irreducible `SU(2)` doublet (different `T3`, same
  S6-side/color/B-L-type content), not two independent copies.
- E17 (round85) tool-verified (`BLOCKED`): under either `SU(2)_L`/`SU(2)_R`
  labeling convention, `{ker D^{t=0}, ker D^{t=1}} = {(1,2),(2,1)}` — never
  two copies of the same piece — but whether `t=0` and `t=1` are ever
  simultaneously physically realized is undecidable without a parent action.
- `G73`/`G67`: 3 independent `Z3`-triality channels, each contributing
  `ind(D_{S6}⊗S⁻)=1`.
- `G74A` (provenance-corrected): `dim ker(D_{S6,twisted}) = 1` EXACTLY per
  channel, established via a `G2`-singlet multiplicity argument (Lemma B) —
  i.e. the kernel is a `G2`-invariant vector, hence (since `SU(3)⊂G2`,
  `S⁶=G2/SU(3)`, `G9`) also an `SU(3)_c`-SINGLET.

## The precise pre-registered question

Using ONLY this project's own already-established, already-cited
constructions: does `t=0`'s content, combined with `G73`'s 3 triality
channels and `G74A`'s 1-dim `S⁶`-side kernel, supply an EVEN or ODD number of
`SU(2)_R` doublets — and is that count determined precisely enough by this
project's own text to answer the question at all?

## PASS / FAIL / BLOCKED criteria (pre-registered)

- **PASS** — `t=0`'s content, per this project's own established, directly
  `t`-indexed bookkeeping (the E9-E17 zero-mode-kernel chain, the ONLY
  bookkeeping in this project that is actually indexed by `t`), supplies a
  count of `SU(2)_R` doublets whose PARITY is unambiguously determinable from
  established numbers, is ODD without `t=0` and EVEN with it (i.e. `t=0`
  uniquely and necessarily completes the doublet-parity requirement), AND
  the SAME counting methodology, applied to the analogous `SU(2)_L`/`t=1`
  case as a consistency cross-check, reproduces the independently-known-true
  answer (an EVEN count, since the real Standard Model's `SU(2)_L` is
  independently known to be anomaly-consistent).
- **FAIL** — the count (with or without `t=0`) is already EVEN without
  needing `t=0` specifically, OR `SU(2)_R` is shown to carry no doublet
  content requiring parity at all (e.g. if it turns out to be exclusively
  singlet-valued matter).
- **BLOCKED** — this project's own established bookkeeping is insufficient
  to determine the count precisely (e.g. because the only bookkeeping that
  is actually `t`-indexed gives a count whose reliability cannot be checked,
  or the count depends on an unresolved choice between two non-reconciled
  bookkeeping systems this project has not itself reconciled) — a well-
  argued `BLOCKED` is a legitimate, valuable outcome, not a failure to
  complete the task.

## Kill criterion

If the ONLY established, `t`-indexed counting methodology (E9-E17's
zero-mode-kernel chain) FAILS its own internal consistency check when
applied identically to the independently-known-correct `SU(2)_L` case (i.e.
produces an odd/inconsistent count where the true answer is known to be
even), this KILLS the possibility of trusting that same methodology's
`SU(2)_R` output as a genuine anomaly-parity count — the verdict must then be
`BLOCKED`, not a forced `PASS` on the `SU(2)_R` number alone.

## Assumptions carried in (not re-derived here)

- `D_full² = D_{S3,t}²⊗I + I⊗D_{S6,twisted}²` (E2/E12's decoupling
  assumption) — presupposed, as it is by every experiment this round reuses.
- `SU(2)_L`=left-translation (Convention A, `CONVENTION_TABLE.md` row 6) —
  adopted as the working convention (matching round90/E17's own citations),
  with the qualitative structural fact (`{t=0,t=1}={(1,2),(2,1)}`, never two
  copies) noted as convention-independent, per E17 Section 1.
- `t=1`'s kernel exists only under `c0=-2` (`CONVENTION_TABLE.md` row 5) —
  carried forward, not re-litigated.

## What this does NOT mean (pre-registered)

1. Will NOT re-derive or challenge Witten's anomaly theorem itself, or
   round90's finding that `SU(2)_R` is genuinely gauged — both reused by
   citation.
2. Will NOT resolve E17's `BLOCKED` coexistence question (whether `t=0` and
   `t=1` are ever simultaneously physically realized) — a PASS here on
   doublet-parity grounds would supply a NEW argument for why both are
   needed, but does not itself supply a parent action.
3. Will NOT affect this project's `N_gen=3` headline claim (S⁶-only
   triality/index/chirality chain) — this round concerns only the separate,
   already-non-load-bearing S³-side torsion-escape-route program.
