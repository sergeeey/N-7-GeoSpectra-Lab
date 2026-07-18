# Round117 — Decision

**Date:** 2026-07-17
**Verdict:** `NARROW_SUBARGUMENT_KILLED__ACTUAL_TENSION_NOT_PROPERLY_TESTED__REMAINS_FULLY_OPEN`
(skeptic: `FALSIFIED` — the round's own "resolution attempt fails" label was
not an earned conclusion; it tested the wrong question)

**Go/no-go:** the computation is correct, but per mandatory skeptic
review, it does **not** actually test round80's flagged tension (Reading 3
vs Lemma L5). It kills only a narrow strawman version of the argument.
The genuine tension is **untouched**, not resolved and not disproven.

## What was computed [VERIFIED-tool: sympy, this round]

Confirmed `S⁶`'s orientation-reversal (`diag(1,1,1,1,1,1,-1)`, `det=-1`)
is an isometry lying in the disconnected component `O(7)\SO(7)`, exactly
the same group-theoretic status round80 established for `S³`'s `iota`
(`det=-1`, `O(4)\SO(4)`). Both confirmed correctly, both true facts.

## Skeptic review [context-asymmetric: claim.md + code only] — FALSIFIED

**The core problem:** "lies in the disconnected component of the
isometry group" (a narrow group-theoretic classification) is **not the
same question** as "is this a symmetry of the physical action" or "is
this the kind of discrete symmetry Reading 3's parity argument is
actually about." The round's proposed resolution ("`SU(2)_L/R` gauged, so
demand completeness; `S⁶` orientation not gauged, so don't") was itself
too crude — but disproving THAT crude version by showing both `iota` and
the `S⁶` flip are equally "ungauged" (in the narrow sense of "not in the
connected component") **does not settle whether either is a genuine
symmetry of the theory's action**, which is the actual criterion relevant
to Reading 3's Left-Right-symmetric-model-building logic (real parity `P`
in physics is exactly this: not part of a continuous gauge group, but
still a genuine symmetry of the action that DOES impose real multiplet
constraints when present).

**Second, independent problem the skeptic identified:** `S⁶`'s
orientation-flip and `S³`'s `iota` act on **structurally different kinds
of data** — `iota` (round80) acts on the tangent bundle / connection
family directly (exchanging left/right-invariant frames, and by extension
the `SU(2)_L`/`SU(2)_R` gauge-multiplet LABELS carried on those frames);
`S⁶`'s orientation choice, as used by Lemma L5, fixes the sign of the
**chirality operator** on the spinor bundle (`D^+` vs `D^-`), a
categorically different structure. Same abstract group-theoretic status
(`O(n)\SO(n)`) does not imply the two Z2's play analogous physical roles.

**Third:** round80's own Section D found `iota` is **never invoked** by any
established mechanism in this project, while `S⁶`'s orientation IS
directly invoked (Lemma L5 cites it as THE mechanism fixing chirality).
"Is this symmetry actually used as a physical selection mechanism
somewhere" may be the real, relevant asymmetry — untested by this round's
comparison, which only checked isometry-group component membership.

## Applying the corrected verdict

The kill criterion's expected branch (same group-theoretic status) was
confirmed — but the INTERPRETIVE conclusion drawn from it
("proves the resolution fails, tension remains open" as if this were a
positive finding) overclaimed. **Corrected: this round tested a narrow,
insufficient proxy for the real question and its result is largely
uninformative about the actual tension**, not a genuine advance toward
resolving OR properly refuting it.

## Kill Analysis

- **What this kills:** only the specific strawman "iota is literally
  inside the gauged continuous `SO(4)` subgroup, while `S⁶`'s orientation
  flip is inside the gauged continuous `SO(7)` — therefore asymmetric
  treatment is justified." Nobody serious was defending exactly that
  narrow claim; killing it adds little.
- **What this does NOT kill:** round80's own flagged tension (Reading 3
  vs Lemma L5) remains **exactly as open as round80 left it** — this
  round neither advances nor closes it, contrary to its own first-draft
  framing.
- **What survives, as a genuinely sharpened NEXT step (per skeptic):** the
  real test would need to check (a) whether `iota` is a symmetry of the
  full theory's ACTION (not just an isometry of the metric — a stronger,
  different condition), and (b) whether `iota`'s role (frame/gauge-label
  exchange) and `S⁶`'s orientation role (chirality-operator sign) can be
  meaningfully compared at all, given they act on different structures.
  Neither check was attempted here.

## Relaxation Map (future work, not attempted here)

| Option | What it would require |
|---|---|
| Check whether `iota` is a symmetry of the FULL theory's action (not just an isometry) | Requires specifying the actual action (spectral action, or an Einstein-Cartan-type action) this project has not yet derived (`PARENT_ACTION_GATE.md` F6) — this check is itself blocked on the SAME central gap OB1 as a whole is trying to close |
| Directly compare "chirality-operator sign" (S⁶) and "frame/gauge-label exchange" (S³) as mathematical objects | Would require an explicit map between the two structures — not obviously possible, may be a category error to even attempt |

## What this does NOT mean

1. Does NOT resolve round80's Reading-3-vs-L5 tension — it remains fully
   open, more clearly scoped than before but not advanced.
2. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.
3. Does NOT re-derive round80's own `iota` result or Lemma L5 — reused by
   citation.

## Check (reproduces the arithmetic, not the withdrawn interpretive claim)

```
cd experiments/20260717-round117-l5-reading3-tension-reconciliation-attempt
python e39_l5_reading3_reconciliation.py
```
Expect: both `det=-1` isometries confirmed. The script's own printed final
label (`RESOLUTION_ATTEMPT_FAILS...`) is SUPERSEDED by this decision.md —
the arithmetic is correct, but the label overreaches per skeptic review.
