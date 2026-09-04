# C142 decision -- DESIGN-ONLY round (no physics computation, per its own
# claim.md). Verdict: DESIGN NOT YET READY. The one candidate C141's own
# exhaustive search (F7) surfaced -- W_cand = 3(+)3bar(+)3bar, the only
# module type other than EVEN_IDX itself achieving round59's own (2,1)
# shape -- requires a genuinely SECOND, independently-sourced copy of the
# 3bar representation to be a real test (not a disguised repeat of the
# same single-scalar question every prior test has asked). Searched this
# project's own codebase for such a source. None exists without inventing
# new, unmotivated structure -- and the reason both candidates checked
# fail traces back to the SAME root cause (G44's su(3)/g2 branching
# collapse) that has recurred throughout this project's history.

**Date:** 2026-09-04
**Type:** DESIGN round, not an FL experiment execution. No Dirac operator
built, no kernel computed, no PROMOTE/REJECT/NULL physics verdict.

## 1. The structural argument, verified directly (not merely asserted)

**Claim (worked out in `claim.md`):** every `{connection}`-invariant summand
pairing tested in round59/C139/C141/T1 has equivariant `Hom`-space
dimension exactly `1`, which is why the graded floor always equals the
observed kernel -- a single complex scalar can only be "zero" (kernel
exceeds floor by exactly that channel's contribution) or "nonzero"
(kernel matches the floor exactly); there is no third option for a `1x1`
map.

`[VERIFIED-tool]`, re-checked directly against each of the four
constructions' own already-computed multiplicities (round59/T0's
`EVEN_IDX=1+3bar` paired against `ODD_IDX`'s `3`-piece: `Hom_su3(3,3bar)`
dim `1`, since `3` and `3bar` are dual irreps, standard fact; C139's `m`
paired internally, `3(x)3bar->1` dim `1`; C141's three summands, each
dim `1` or `0`; `T1`'s two summands, same as `T0` plus `ODD_IDX`'s own
`(1,2)` piece, dim `1`) -- **confirmed: zero multi-dimensional `Hom`
spaces have EVER been tested in this project's twisted-`D_S6` history.**

## 2. The candidate from C141's own F7 search

`W_cand = 3 (+) 3bar (+) 3bar` (module type `(mult_1,mult_3,mult_3bar) =
(0,1,2)`), the second of exactly two module types C141's brute-force
search found achieving shape `(2,1)` (the other being `EVEN_IDX` itself,
already fully tested via `T0`/`T1`).

**Why `mult_3bar=2` matters:** `Hom_su3(3, W_cand)`, the channel relevant
to `ODD_IDX`'s own `3`-constituent pairing with `W_cand`, is
2-DIMENSIONAL (one map per copy of `3bar`) -- `[VERIFIED-tool]`, standard
Frobenius-reciprocity counting, re-derived directly: `Hom_su3(3, 3bar) ⊕
Hom_su3(3, 3bar) `, each summand dimension `1`, total `2`. **This would
be the first genuinely multi-dimensional equivariant channel this
project's twisted-`D_S6` program has ever tested**, IF the two copies of
`3bar` carry independent connection data.

## 3. Search for an independent second source -- the actual design
   question this round exists to answer

Per `claim.md`'s own instruction, searched this project's codebase (not
memory) for any existing, independently-derived `su(3)`-equivariant map
into `3bar` (or `3`) beyond the one `m`/`Sigma`/`EVEN_IDX`/`ODD_IDX`
already share (all four are built from the SAME underlying nearly-Kähler
complex structure on `S6`, i.e. the SAME geometric `3bar`).

### 3a. Candidate A -- C70/C71's triality-channel intertwiners `U_v`/`U_s`/`U_c`

`[VERIFIED, direct read]`
`experiments/20260811-c70-independent-bridge-fingerprint-and-direct-solve/decision.md`
Section "What this means, stated carefully", items 1 and 3, quoted
exactly: *"The round59<->G102 su(3) bridge is closed... `U` (the
representation-space intertwiner)... **Non-uniqueness of `U` is
expected, not a defect.** `Inn(su(3))` acts transitively on the solution
set (composing the found `Phi`/`U` with any inner automorphism of the
source algebra gives another valid solution)... 15 random restarts...
land on 15 *different* `Phi` matrices."*

**Assessment:** `U_v`/`U_s`/`U_c` are BASIS-MATCHING intertwiners
establishing that round59's own `su(3)` presentation and G102's `su(3)`
presentation are the SAME abstract algebra action in different
coordinates -- an `8`-real-dimensional GAUGE freedom (`Inn(su(3))`), not
new geometric data. Using one of these to build a "second" `3bar` would
just relabel the SAME `3bar` in a different basis -- proportional, not
independent, connection data. **Rejected as a source: this is gauge
freedom, not physics.**

### 3b. Candidate B -- G102's three triality channels `8_v`/`8_s`/`8_c`
    themselves

`[VERIFIED, reused fact, already extensively certified this session]`
G102's own central, repeatedly-confirmed finding (`decision.md:14`,
re-cited throughout C123-C141): `dim c_{so(8)}(g2) = 0`, and, more
directly relevant here, `8_v|_{G2} = 8_s|_{G2} = 8_c|_{G2} = 7+1`
IDENTICALLY (G44, 2026-06-20, the oldest and most load-bearing negative
result in this project's history) -- the three channels are FORCED to
restrict to `su(3)` (a subalgebra of `g2`) the SAME way. **Assessment:**
this is not merely unhelpful, it is the DIRECT, general-purpose reason no
independent second `3bar` (or `3`) source can come from the triality
channels specifically -- the same branching-collapse mechanism that has
closed roughly a dozen other candidate mechanisms across this project's
history (G44 itself; the entire triality-bridge program's own novelty-
check, `OPEN_BLOCKERS.md` "Bridge F'" entry; G102 itself). **Rejected as
a source, for a reason that is not specific to this round -- it is the
project's own oldest structural obstruction, recurring here in a new
guise.**

### 3c. No other candidate identified

No other independently-sourced `su(3)`-equivariant map into `3` or
`3bar` was found in this project's `experiments/`, `docs/`, or root-level
registry files. The `su(3)`-adjoint alternative (C139 Section 2's
rejected runner-up) fails for the analogous reason: it would require
inventing a NEW projection/normalization not already present in this
project's own certified constructions -- exactly the kind of ad hoc
addition this project's own Anti-Overfitting Gate (AOG-5, independent
motivation) exists to block.

## 4. Verdict

**DESIGN NOT YET READY.** `W_cand = 3(+)3bar(+)3bar` is a real,
well-identified candidate (via C141's own F7 search) for the first
genuinely multi-dimensional equivariant test in this research line -- but
this project's own existing geometric content offers no independently-
sourced SECOND copy of `3bar` to populate it with. Both candidates
checked (C70/C71's basis-matching intertwiners; G102's triality channels)
fail for identifiable, non-arbitrary reasons -- one is gauge freedom, the
other is the SAME `su(3)`/`g2` branching-collapse mechanism (G44) that has
recurred throughout this entire project's history.

**This is itself an informative finding, not a null result to hide:**
C141's own falsifiable escape route ("the first twist bundle whose kernel
exceeds its own graded floor would be the first genuinely dynamical
result") is **currently unreachable within this project's existing
geometric content**, not merely unattempted. Closing this gap would
require either (a) an independently-motivated NEW geometric construction
this project does not currently have (high AOG-5 risk, per Section 3c),
or (b) external input (a genuinely different presentation of the compact-
ification geometry, plausibly something only Tom Lawrence's own fuller
framework could supply).

## 5. What this round does NOT show

- Does NOT prove no such second source could ever exist in principle --
  only that none was found in this project's CURRENT content.
- Does NOT close C141's own escape route as permanently unreachable --
  flags it as `BLOCKED-INTERNAL` (this project's own content is
  insufficient), not `IMPOSSIBLE`.
- Does NOT change `N_gen=3`'s CONDITIONAL status.
- Does NOT reopen C123-C141's verdicts.
- Does NOT solicit Tom Lawrence's Part 5.

## 6. Self-check (per claim.md, in place of a full skeptic pass for a
   design-only round)

**Does this design actually test what C141's escape route asks?** Yes,
directly: it asked "is there a candidate that could show kernel > floor,"
found the one candidate C141's own search already surfaced, and checked
whether it is actually buildable with existing project content -- found
it is not, for two independently-verified, non-arbitrary reasons. This
is not a disguised restatement of an easier question; it is the honest,
negative answer to the question actually asked.

## 7. Registry actions -- NOT performed by this round, proposed only

**`pearl_registry/INDEX.md`** -- new row (append to the same escape-route
thread C141 opened, 2026-09-04):

```
| 2026-09-04 | C142 (design-only, scoping C141's own escape route) | The one candidate for a genuinely multi-dimensional equivariant channel in this project's twisted-D_S6 test family (W_cand=3+3bar+3bar, from C141's own F7 exhaustive search) requires a SECOND, independently-sourced copy of 3bar -- searched, none exists in this project's current content. Two candidates checked and rejected for identifiable reasons: C70/C71's U_v/U_s/U_c triality intertwiners are basis-matching gauge freedom (Inn(su(3)) orbit, non-unique by construction), not independent data; G102's own three triality channels are forced identical under su(3) (G44's branching-collapse, this project's oldest and most-recurring negative result). This means C141's own falsifiable escape route ("first kernel exceeding its floor") is currently UNREACHABLE with existing project content, not merely untried -- and the reason is the SAME root mechanism (G44) that has closed roughly a dozen other candidate mechanisms across this project's history | If this project's geometric content is ever extended (new construction, or external input from Tom Lawrence's fuller framework) to include a genuinely independent second su(3)-equivariant map into 3 or 3bar, building W_cand=3+3bar+3bar and computing its kernel becomes the single most informative test remaining in the "why Sigma, not m" research line | any future round proposing new geometric content for this project (a new twist bundle, a new triality-channel construction, an externally-motivated extension); OR if Tom Lawrence's own framework is ever consulted and supplies a genuinely independent su(3)-equivariant structure | whenever new geometric content is proposed for this project, check FIRST whether it supplies an independent second copy of an already-used su(3) irrep, before building anything else | pending -- impact 6 -- see experiments/20260904-c142-graded-floor-candidate-scan/decision.md |
```

**`OPEN_BLOCKERS.md` OB14** -- one-line append: *"C142 (2026-09-04,
design-only) checked whether C141's own falsifiable escape route (a
twist bundle whose kernel exceeds its graded floor) is currently
buildable -- NOT with this project's existing content; the one candidate
(`W_cand=3+3bar+3bar`) needs an independently-sourced second `3bar` that
does not exist here, for the same G44 branching-collapse reason that
recurs throughout this project. `BLOCKED-INTERNAL`, not `IMPOSSIBLE`."*

**No `CLAIM_LEDGER.yaml`, `null_results/INDEX.md`, or
`PARENT_ACTION_GATE.md` edit proposed** -- this round produced no
physics claim and no gate-field-relevant construction; it is a negative
feasibility finding about future work, appropriately homed in
`pearl_registry` (a flagged, falsifiable, dated future-check item) and as
a one-line `OPEN_BLOCKERS.md` amendment.

## Evidence tier

**Tier: `[VERIFIED]`** for the `Hom`-space dimension-counting argument
(Section 1, standard representation theory, re-derived directly) and for
both source-rejection findings (Section 3a/3b, direct citation of
already-certified project files, not from memory). **`[INFERRED]`,
confidence MEDIUM** for the connection between "no independent source
found" and "this traces to the same G44 mechanism" -- a structural
observation, not a formally proven necessity (a genuinely different,
not-yet-conceived construction might still exist). No physics claim is
made or implied by this round.
