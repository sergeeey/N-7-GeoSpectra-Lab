# Round117 — Claim

**OB1 continued.** Attempts to resolve the one genuinely open thread
round80/E14 flagged (`CLAIM_LEDGER.yaml` `C18`): Reading 3 (S³'s discrete
`iota`-parity plausibly requires keeping BOTH `SU(2)_L`- and
`SU(2)_R`-doublet content, à la Left-Right-symmetric model building) sits
in unreconciled tension with Lemma L5 (`preprint.tex:884-912`, S⁶'s
chirality is fixed, unconditionally, left-handed only — no analogous
"keep both chiralities" demanded there).

## Candidate resolution tested

**Hypothesis:** the two cases are NOT actually parallel, because `SU(2)_L
×SU(2)_R` is a genuinely GAUGED symmetry (round90, established: real KK
gauge bosons, kinetic terms, Higgs bidoublet) — gauge theories generically
require complete multiplets under a gauged symmetry (anomaly-freedom,
unitarity) — **whereas** S⁶'s orientation choice (used by L5) is not
itself a gauged symmetry at all, merely a geometric/labeling convention.
If true, this would explain why "demand parity" is a meaningful physical
requirement for the S³-side gauged `SU(2)_L/R` but not for the S⁶-side
orientation, dissolving the tension — structurally similar to round95's
own prior dissolution of a different apparent tension in this project
(different invariants, not actually conflicting).

## L0 gate (EstimandOps)

**Question type: Descriptive/logical**, checking whether an established
project fact (`Iso(S³×S⁶)=SO(4)×SO(7)`, connected component only,
round80's own citation) applies symmetrically to BOTH factors or only one.

## Falsifiable claim

`Iso(S³×S⁶)=SO(4)×SO(7)` is the CONNECTED isometry group this project's
own gauge construction uses (round80's own citation,
`preprint.tex:274,279,422`). By the general fact `O(n)/SO(n)≅Z₂` for any
`n`, an orientation-reversing map of `S⁶` lies in the disconnected
component `O(7)\SO(7)`, **exactly the same structural status** as round80's
own `iota` on `S³` (shown there to lie in `O(4)\SO(4)`). If this holds,
S⁶'s own orientation-flip is **equally ungauged** as S³'s `iota` — meaning
the proposed "S³ is gauged, S⁶ is not" distinction is **false**, and the
candidate resolution above **fails**.

## Kill criterion (pre-registered)

- If S⁶'s orientation-reversal is confirmed to lie in the SAME
  disconnected, ungauged component as S³'s `iota` (expected, from the
  general `O(n)/SO(n)` fact) → the proposed "gauged vs ungauged"
  distinction **fails to resolve** round80's tension; report honestly that
  this specific resolution attempt does not work, sharpening (not closing)
  what remains open.
- If some OTHER, genuine asymmetry between the two factors is found
  instead (not attempted here unless the above check surprises) → would
  need its own separate justification, not assumed.

## What this does NOT mean (pre-registered)

1. Does NOT claim to resolve round80's tension either way if the kill
   criterion's expected branch holds — only closes off ONE specific
   candidate resolution, leaving the underlying question open.
2. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.
3. Does NOT re-derive round80's own `iota` result or Lemma L5 itself —
   both reused by citation.
