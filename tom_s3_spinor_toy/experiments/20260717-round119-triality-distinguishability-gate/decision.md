# Round119 — Decision

**Date:** 2026-07-17
**Verdict:** `GATE 1 OF 7 DONE / GATES 2-6 OPEN` (narrower than a flat
`PARTIAL` — corrected after skeptic review)

**Go/no-go:** Applying `L3B_SPIN8_INTERFACE_SPEC.md`'s own gate to its own
most-advanced candidate (`SO(4)×SO(4)` block-chirality construction) does
**not** yield a clean `PARTIAL` per that document's §4 rubric, once checked
against the source's own sharper §7 gate table. The algebraic-
distinguishability half is genuinely done; the physical-realization half is
exactly what the source itself calls "the blocker."

## Single skeptic pass — three real findings, all fixed

Ran the mandatory context-asymmetric skeptic review (claim.md + the gate
document only, no reasoning chain) per this project's `falsification-
ladder.md` Step 8a. Verdict: `WEAKENED`. Three concrete issues, all
addressed directly in `TRIALITY_DISTINGUISHABILITY_GATE.md` (inline,
marked `[skeptic correction]`, original claim kept visible, not silently
rewritten):

1. **Condition 2 downgrade was understated.** First draft said `[D,U]=0`
   "holds at the bare-geometry level... not independently re-verified" for
   the physical `D`. Skeptic found this understates the actual situation:
   the source's own G74A discussion shows Lemma B's proof "does not degrade
   gradually with perturbation size; it simply no longer applies, at any
   nonzero perturbation" once `G₂` breaks — and `G₂`-breaking is mandatory
   for the `SO(4)×SO(4)` route. So the physical-`D` case is not merely
   unchecked, the source's own tooling says it cannot be checked this way.
2. **Condition 3 was overclaimed as fully "Holds, verified."** Skeptic found
   this conflates the algebraic-distinguishability half (source's own §7
   gate 1, genuinely "done today, verified") with the global/physical half
   (§7 gate 2, explicitly "the blocker, needs Part 5"). Only the former is
   established.
3. **§5's cross-connection to Round118 contained a hard arithmetic/category
   error.** First draft claimed `SU(3)×SU(2)×SU(2)` (actual rank 4, not 3 —
   miscounted) "embeds inside `SO(6)`" — false on rank grounds alone, and
   more fundamentally wrong because `SU(2)_L×SU(2)_R` lives on the `S³`
   factor, not as an `SO(6)`/`S⁶`-side subgroup at all. The "same rank
   ceiling" analogy conflated an `S³`-side gauge factor with an `S⁶`-side
   one. Corrected to a much more modest, unresolved connection.

Skeptic also correctly flagged that the first draft's stated reason for the
§3.5 anti-circularity screen passing ("falls out of `T`'s eigenvalues") cited
the wrong fact (the `SO(4)×SO(4)` subalgebra's own triality-decomposition,
not the `Γ_A/Γ_B` structure that actually distinguishes the channels) —
right conclusion (the screen does pass), wrong citation. Fixed.

## What was actually verified this round

- Re-read `L3B_SPIN8_INTERFACE_SPEC.md` §1 (SO(4)×SO(4) candidate, full,
  lines ~390-686), §2-§4 (gate definition), §3.5 (anti-circularity), §7
  (gate table) in their entirety before drafting, and again during the
  skeptic-correction pass to confirm each correction against the exact
  source text (not from memory).
- No new physics computation — this round is a rubric-application and
  registry-accuracy audit, consistent with its own L0 gate (Descriptive).

## Kill Analysis

- **What this kills:** the flat `PARTIAL` label as an accurate summary of
  the `SO(4)×SO(4)` candidate's status — it overstates what the source's
  own §7 framing establishes.
- **What this does NOT kill:** the `SO(4)×SO(4)` candidate itself (a
  genuine, verified advance — the first candidate to algebraically
  distinguish all three channels, not just `v` from `{s,c}`), or L3b's
  overall open status (unchanged either way — both `PARTIAL` and the
  corrected `GATE 1 OF 7` label agree L3b is not closed).
- **What survives as a scoped next step:** checking whether an explicit
  `SO(4)×SO(4)`-breaking term introduces channel-mixing in the full Dirac
  operator (the flagged, unresolved OB4/OB11 connection) — requires either
  Part 5's content or a new internal construction, neither attempted here.

## Relaxation Map

| Option | What it would require |
|---|---|
| Resolve condition 2/3's physical half | Part 5's actual content (unpublished, not solicited), or a new `G₂`-breaking-compatible spectral-gap argument (no such tool currently exists per this round's re-read of G74A) |
| Check the OB4/OB11 channel-mixing connection | An explicit construction of the `SO(4)×SO(4)`-breaking Dirac operator and a check for off-diagonal terms between `S⁶` channels — a genuinely new computation, not attempted this round |

## What this does NOT mean

1. Does NOT close L3b — conditions 4-5 (in `L3B_SPIN8_INTERFACE_SPEC.md`'s
   own §3 language) remain open regardless of which label is used.
2. Does NOT change `N_gen=3`'s conditional status, `lambda=FREE_COUPLING_
   PARAMETER`, or `safe_for_runtime=False`.
3. Does NOT redo any verified computation from `L3B_SPIN8_INTERFACE_SPEC.md`.
4. Does NOT establish or refute the OB4/OB11 connection — flagged only.

## Standing lesson (reinforces round118's, from a different angle)

**A generous rubric-label choice made in narrative ("Spin(8)-adjacent",
"bare-geometry level") does not protect against an overclaiming *label*
sitting next to that narrative.** Round118's lesson was about an unverified
assertion in a code comment; this round's is about a formally-correct-
sounding rubric label (`PARTIAL`) that the surrounding hedged prose already
half-contradicted. When a document's own finer internal framing (here, §7)
exists alongside a coarser one (§3/§4), always check the two against each
other explicitly before picking a label — "no discrepancy found" is itself
a claim that needs checking, not a default.

## Check (reproduces the source citations)

```
Read tom_s3_spinor_toy/L3B_SPIN8_INTERFACE_SPEC.md, lines 390-686 (§1 SO(4)xSO(4)),
lines 689-886 (§2-§7)
```
Expect: §7's gate table (lines ~872-879) shows gate 1 marked done, gates
2/5/6 marked blocked on Part 5 — confirming the `GATE 1 OF 7 DONE / GATES
2-6 OPEN` verdict is a direct reading of the source, not an inference.
