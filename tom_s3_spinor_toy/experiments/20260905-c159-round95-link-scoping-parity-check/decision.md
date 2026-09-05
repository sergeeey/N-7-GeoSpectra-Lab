# C159 — Decision

**Date:** 2026-09-05
**Verdict:** `ESCAPE-FOUND (WEAKENED — corrected 2026-09-05 after an
independent context-blind skeptic pass; two overreaches fixed, top-line
unchanged)** — the claim's own necessary step, "if H1c is ever closed by an
exclusive channel↔sector pairing rule, then `n_L+n_R=3` necessarily," is not
forced as a GENERAL impossibility proof. **Corrected characterization**
(see skeptic finding, Section 6b below): E17/round85 Section 4 does NOT
treat non-exclusive ("both sectors") assignment as "a live, unexcluded
candidate" — E17 §4 explicitly reaches its own pre-registered `BLOCKED`
verdict there, with the specific missing ingredient NAMED ("either two
distinct fermion fields on the same S³... or a mechanism making `t` itself
a dynamical field with two coexisting vacua/sectors... or an explicit
orbifold-type construction... already tried and found to collapse to
`t=1/2`"), and two of its three examined readings point AWAY from
coexistence, the third is flagged as "an unadopted, tension-carrying
choice." What E17 actually supplies is: the possibility is BLOCKED, not
excluded outright — a "named hole," not a live candidate. **What removes
C159's own parity obstruction is a narrower, later fact**: C132/C133 §9
(2026-09-02/03) exhibits `all→both` as one of exactly 3 logically available
*support patterns* of a specific channel-uniform (ℤ₃-symmetric) coupling
ansatz — a concrete structure, not merely an unexcluded possibility — and
**the accounting bridge from that support pattern to `n_L+n_R=2·N_gen`
(rather than `N_gen`) is this round's own derived supplement, not a
quantity C133 §8a itself states** (C133 §8a states only the exclusive
formula and gestures at "the assumed Pati-Salam content" as the anomaly
condition's non-excluded survivor, without spelling out the doubled-count
arithmetic). **Corrected top-line**: a labeled hole (E17, BLOCKED,
unresolved) sits in the same logical space C159's exclusive-pairing
argument occupies, and a later, more concrete structure (C133's `all→both`
support pattern, with this round's own accounting bridge) demonstrates
that space is not empty — so C159's parity argument is not a general
impossibility proof. The parity arithmetic itself (`2n_L=3` has no
solution, under the EXCLUSIVE reading) remains correct (Section 2).

**Per the claim's own explicit escape route: this resolves cleanly within
one session. STOPPING here — no attempt was made to construct an actual
pairing rule.**

---

## 0. What was done (Prior Result Gate steps 3–5, per claim.md's own
instruction not to trust its "0 hits" paragraph without re-verification)

1. Re-ran the regex grep from claim.md item 2 (`n_L\s*=\s*n_R`, `n_L\s*\+\s*n_R`,
   `2n_L`, `parity`, "odd number of generation") against `null_results/
   INDEX.md`, `parked/INDEX.md`, `pearl_registry/INDEX.md`, `OPEN_BLOCKERS.md`
   myself. **Confirmed**: every "parity" hit in these four files is about a
   *different* parity (the `ι` orientation-reversing-isometry / Pin-structure
   parity of OB13/C37-C131, or a flag-manifold root-count parity in C156's
   own SU(3)/T² work) — none is about the `n_L`/`n_R` generation-count
   parity this claim concerns. The "0 hits in these 4 registry files"
   sub-claim is correct as far as it goes.
2. **claim.md's own step 3 ("round*_claim.md + scripts grep") was the
   actual gap, and running it changes the verdict.** `git log --all -S
   "n_L=n_R"` and a literal grep for `n_L`/`n_R` across the `experiments/`
   tree returns real, substantive hits in
   `experiments/20260902-c133-symmetry-ladder-pairing-space/decision.md`
   and `experiments/20260902-c132-13d-parent-action-survey/decision.md`
   (both dated 2026-09-02, committed 2026-09-03 in `aa55383`, "C123-C137 --
   15-round OB1 pipeline" — the immediate predecessor context this round's
   own prompt names via "C127-C131" but does not mention C132/C133, even
   though they are literally the same commit). `git log --all -S"2n_L"` and
   `-G"2.n_L\s*=\s*3"` return **zero** hits anywhere — the specific
   `2n_L=3` arithmetic form is genuinely new phrasing. `git log --all
   -S"n_L + n_R"` returns one additional, **unrelated** hit (`761236f`,
   round G24 "Blind Spectrum," June 2026) — checked directly: that file's
   `n_L`/`n_R` count SO(4)×G2 weight-multiplicities in a 32-state
   bookkeeping (`n_L==16, n_R==16`), a completely different object from
   round95's generation-sector counts. Coincidental variable-name reuse,
   not a prior instance of this claim.
3. Re-read round90, round95, E17/round85, round83 (E16), and round86 (E18)
   **in full**, via `Read`, not from claim.md's summary (Sections 1–4
   below cite exact lines).
4. Read C132's and C133's decision.md in the sections bearing on the
   anomaly step (`decision.md` §8a, §9 of C133; the "anomaly step,
   deflated" passage of C132), and `PARENT_ACTION_GATE.md` F4's summary of
   both.
5. Ran `c159_parity_check.py` (this directory) to replace hand arithmetic
   with a tool-run check — output below (Section 2).

---

## 1. Primary-source verification, cited at the file:line level

### 1a. Round90 (`experiments/20260717-round90-pati-salam-gauge-completeness/decision.md`)

Read in full. Confirmed exactly as claim.md cites:
- `decision.md:157`: `A(4,2,1) = +2` (`A(4)×dim(2)×dim(1) = 1×2×1`).
- `decision.md:159` (via the correction block, lines 12-19): `A(4̄,1,2) = -2`
  (`A(4̄)×dim(1)×dim(2) = (-1)×1×2`).
- These are fixed, generation-independent coefficients — confirmed, not an
  a priori assumption.

**New finding, not in claim.md's scope but worth recording (does not
change this round's verdict, flagged for a future round instead):**
round90's own **retroactive correction block** (top of the file, added
2026-07-17 "after user review") explicitly **refutes** the file's original
in-body claim that Witten's `SU(2)` global anomaly forces an even number of
`SU(2)`-doublets and thereby "forces the pair" — because "each Pati-Salam
multiplet ALONE already contains **4** `SU(2)`-doublets (the `4` of `SU(4)`
supplies the multiplicity), which is even." This means round95 Section 5's
own **separate**, "new observation… worth recording as a pearl candidate"
point 2 ("`n_L=3` is odd," therefore a Witten-anomaly violation,
`experiments/20260717-round95-l5-tension-check/decision.md:248-254`) treats
`n_L` as if it directly counted `SU(2)_L` doublets — but by round90's own
(same-file, same-day) correction, the actual doublet count for `n_L` copies
of `(4,2,1)` is `4·n_L`, which is **even for every integer `n_L`**, not just
even `n_L`. Round95's own Witten-anomaly pearl candidate therefore appears
to rest on the same doublet-counting confusion round90's correction already
retracted **in the very file round95 cites**. **This does not affect
C159's own argument** — C159 uses only the cubic `SU(4)^3` condition
(`n_L=n_R`), never the Witten-parity point — but it is a live, unflagged
inconsistency between round90's corrected text and round95's Section 5,
worth a future round's attention. Not pursued further here (out of scope,
per claim.md's own "do not proceed" instruction).

### 1b. E17/round85 (`experiments/20260717-round85-e17-sector-coexistence-gate/decision.md`)

Read in full. Confirmed: Section 1 (`decision.md:50-93`) establishes, under
**both** labeling conventions, `{ker D^{t=0}, ker D^{t=1}} = {(1,2),(2,1)}`
exactly — no third representation type, never two copies of the same piece.
This part of claim.md's premise is solid.

**Directly bears on the escape, corrected after skeptic review (see
Section 6b) — weaker than this file's own first draft claimed:** E17's own
**Section 4** (`decision.md:199-295`) is not about representation content
at all — it is a dedicated investigation of **whether both `t`-sectors are
ever simultaneously physically present** for a single generation/channel
(framed there as "coexistence"). E17 §4 examines three readings and finds
none of them supplies coexistence: Reading 1 ("same physics, different
labels," `decision.md:210-219`) argues for UNDER-counting, the opposite
direction; Reading 2 (gauging `iota` as an orbifold identification,
`decision.md:220-226`) collapses to `t=1/2` — KT-8's already-established
zero-zero-mode point — a decisive negative, not a live option; Reading 3
(Pati-Salam parity, `decision.md:227-234`) is "an unadopted,
tension-carrying choice," in "direct, unreconciled tension" with Lemma L5's
own asymmetric chirality result. E17's own summary is explicit: **"None of
the three readings closes the gap in [coexistence's] direction; Readings 1
and 2 point away from it, Reading 3 is an unadopted, tension-carrying
choice"** (`decision.md:236-237`), and E17 reaches its pre-registered
`BLOCKED` verdict with the missing ingredient NAMED, not left as an
open toss-up: "Genuinely realizing both `t=0` and `t=1` at once would
require something this project does not state anywhere: either two
distinct fermion fields on the same S³..., or a mechanism making `t` itself
a dynamical field with two coexisting vacua/sectors, or an explicit
orbifold-type construction... already tried and found to collapse to
`t=1/2`" (`decision.md:284-295`). **This is BLOCKED-with-a-named-hole, not
"a live, unexcluded candidate" — this file's first draft overstated E17's
own position, and the correction matters**: E17 alone does not license
"both sectors, non-exclusive" as an equally-live alternative to a single
sector; it names the missing ingredient and shows every considered concrete
reading of "how" fails or is disfavored. E16/round83
(`decision.md:242-244, 261, 291-294`) independently flags the identical
item as **open** (not "candidate"), consistent with this weaker reading.

**What actually does the work for C159's escape is narrower and later than
E17**: E17 supplies only that "both sectors, non-exclusive" is a
*conceivable structure this project has examined and not been able to
exclude outright* (a labeled hole in the argument space), not that it is a
live, positively-supported candidate. The concrete structure that
demonstrates the hole is non-empty is C132/C133 §9 (Section 1f below),
dated 2026-09-02/03 — two to three days LATER than E17 (2026-07-17) and
outside claim.md's own cited round list. Claim.md's parenthetical ("which
is what 'pairing rule' has meant in every round that has discussed H1c so
far, including round95, E17, E18/round86") is not accurate as a
description of E17's own content, but the escape does not actually depend
on E17 alone doing more than it does — it depends on C133's later, more
concrete support-pattern enumeration (Section 1f).

### 1c. Round83/E16 (`experiments/20260717-round83-joint-representation-decomposition/decision.md`)

Read in full. Two findings:
- Confirms 1b: `decision.md:242-244, 261, 291-294` name "whether BOTH `t=0`
  and `t=1` doublets are simultaneously required" as **open**, unchanged
  by round83's own PASS verdict (which concerns a narrower question — is
  the 2-fold multiplicity within *one* sector a doublet or a family copy —
  not the cross-sector question at all).
- **H1c's own defining round does not itself frame H1c as an exclusive
  3-channel→2-sector pairing function.** Every occurrence of "H1c" in this
  file (`decision.md:20, 240, 255, 285, 291`) glosses it as "physical
  selection between `t=0` and `t=1`" — i.e. which single value of the
  connection parameter `t` is realized — a statement about **one**
  connection parameter, not a claim about how 3 separate channels map onto
  2 sectors. The "3 channels → 2 sectors" framing claim.md's argument
  depends on appears to be a **later gloss** (introduced in round95
  Section 4-5's discussion, and used again in the C123-C137 pipeline), not
  H1c's own original content.

### 1d. Round86/E18 (`experiments/20260717-round86-parent-action-discriminator/decision.md`)

Skimmed for the relevant sections (H1c/KT-1 references, `decision.md:46-49,
387-390, 415-417, 462-465, 487-511`). Consistent with 1b/1c: round86
continues E17's same "coexistence" question (via a different candidate
mechanism, AHL2023's `ψ±`), reaches BLOCKED again, and never states or
relies on an exclusive-pairing framing either.

### 1e. Round95 (`experiments/20260717-round95-l5-tension-check/decision.md`)

Read in full (already largely quoted in claim.md). Section 3
(`decision.md:144-189`) derives `n_L=n_R` exactly as claim.md states — the
arithmetic is correct (Section 2 below re-verifies it by tool). Section 5
(`decision.md:229-260`) discusses only the single special case "all 3
channels to one sector" (`n_L=3, n_R=0`) as a **hypothetical future**
scenario ("if this project ever establishes a definite pairing rule... and
assigns ALL 3 generations to the SAME sector") — it does **not** state or
assume this is the only possible outcome, and does not consider intermediate
splits (`n_L=1,n_R=2` etc.) or the non-exclusive "both" pattern at all.
Round95 nowhere states "`n_L+n_R=3` necessarily" as a general fact independent
of which specific pairing scenario eventually obtains.

### 1f. C132/C133 (2026-09-02/03) — where the escape is actually on record

`experiments/20260902-c133-symmetry-ladder-pairing-space/decision.md`
§9 (lines 584-616) enumerates, under a **channel-uniform** (`ℤ₃`-symmetric)
coupling ansatz, exactly **three** possible nonzero support patterns for
the S6-channel↔S3-sector coupling: `all→t=0`, `all→t=1`, `all→both`
(line 599). §8a (lines 554-565) then applies round95's own `n_L=n_R`
condition to these three patterns and states explicitly: "with `n_L + n_R
= N_gen`, the one-sector options give `{0, N_gen}` and fail for **every**
`N_gen ≥ 1`. It is a **consistency filter**, not a differentiator, **and
its survivor is the assumed Pati-Salam content**" — i.e. `all→both`, under
which every channel supplies content to both sectors, giving `n_L=n_R=N_gen`
automatically (`n_L+n_R=2N_gen`, not `N_gen`), with no parity obstruction
of any kind. `C132`'s own decision.md (`decision.md:239-245, 847-853`)
states the identical point independently. **`all→both` is not claimed to
be a confirmed physical resolution of H1c** — C133's own header states OB1
"stays PARKED," H1c "stays OPEN," and explicitly disclaims that its
"anomaly step" analysis is a differentiator among candidates, only a
non-exclusionary filter. It is, however, already an on-the-record
counterexample to "a pairing rule must be exclusive."

---

## 2. Tool-run verification of the arithmetic (`c159_parity_check.py`)

```
Anomaly condition: Eq(2*n_L - 2*n_R, 0)
Solved for n_L: [n_R]
N_gen=3, exclusive-pairing solutions with n_L=n_R AND n_L+n_R=N_gen: []

General sweep, N_gen=0..6, EXCLUSIVE pairing (n_L+n_R=N_gen):
  N_gen=0: n_L=n_R solutions = [(0, 0)]
  N_gen=1: n_L=n_R solutions = NONE (impossible)
  N_gen=2: n_L=n_R solutions = [(1, 1)]
  N_gen=3: n_L=n_R solutions = NONE (impossible)
  N_gen=4: n_L=n_R solutions = [(2, 2)]
  N_gen=5: n_L=n_R solutions = NONE (impossible)
  N_gen=6: n_L=n_R solutions = [(3, 3)]

'all->both' pattern for N_gen=3: n_L=3, n_R=3 (n_L=n_R holds trivially: True); n_L+n_R=6 != N_gen=3
```

This confirms: (a) round95's `n_L=n_R` derivation is correct; (b) **if** a
pairing rule is required to be an exclusive, sum-preserving function
(`n_L+n_R=N_gen`), then for `N_gen` odd (including `N_gen=3`) no solution
exists — the claim's arithmetic is right; (c) the `all→both` pattern
already on record in C133 evades this entirely, because it does not
satisfy `n_L+n_R=N_gen` in the first place.

---

## 3. Verdict, applying claim.md's Kill Criterion table

**ESCAPE-FOUND** — row 3 of claim.md's table: "`n_L+n_R=3` does NOT
actually have to hold (e.g. 'pairing rule' could mean something looser
than a total function on the 3 channels...)."

**The specific escape, named precisely, corrected after skeptic review:**
the premise "if H1c is ever closed by a rule assigning EACH of the 3
channels to exactly one of the 2 t-sectors, then `n_L+n_R=3` necessarily"
is a true conditional, but its antecedent ("exclusive assignment") is not
the only structure this project's own text has considered. **E17/round85
Section 4 (2026-07-17) does not itself supply a live non-exclusive
candidate — it reaches its own `BLOCKED` verdict, with the specific missing
ingredient named, after finding two of its three examined readings point
AWAY from coexistence and the third an unadopted, tension-carrying choice
(Section 1b above).** What E17 supplies is only that this structure is a
labeled hole in the argument space, not excluded outright — not a positive
candidate. **The concrete structure that fills that hole is later and
narrower**: C132/C133 §9 (2026-09-02/03) exhibits `all→both` as one of
exactly 3 logically available support patterns of a specific
channel-uniform (ℤ₃-symmetric) coupling ansatz. **The step from that
support pattern to `n_L+n_R=2·N_gen` (rather than `N_gen`) is this round's
own derived accounting bridge, not a quantity C133 §8a itself states** —
C133 §8a states only the exclusive formula and names "the assumed
Pati-Salam content" as the anomaly condition's non-excluded survivor,
without spelling out the doubled-count arithmetic. Combining C133's
support-pattern structure with this round's own accounting gives
`n_L+n_R=2·N_gen`, under which the `2n_L=3`-has-no-solution argument does
not apply.

**This is NOT a claim that H1c is closed, or that "all→both" is
established physics.** OB1 stays PARKED and H1c stays OPEN in this
project's own registries, exactly as C133 itself states — "all→both" is
merely the demonstration that an exclusive pairing is not the only
logically available structure, which is all that is needed to block
C159's specific parity argument from going through as a general
impossibility result.

---

## 4. 5-gate discovery-mandate assessment (per C157/C158's own precedent)

This round does **not** reach a PROMOTE or FORCED-NOT-DISCOVERED verdict,
so the 5-gate "is this forced, not discovered" mandate applies in a
slightly different shape here: the question is whether the **escape**
itself is a new discovery of this round, or already on record.

**Answer: mostly already on record, with one small genuinely-new piece —
corrected after skeptic review to credit each piece precisely.** C132/C133
(2026-09-02, committed 2026-09-03) already state that the anomaly condition
"does NOT discriminate" and names "the assumed Pati-Salam content"
(`all→both`) as its non-excluded survivor — this round's contribution,
stated precisely:
(a) shows this refutes C159's own specific "`n_L+n_R=3` necessarily"
    premise — a scoping/consolidation step, forced by C132/C133's own
    already-stated content, not a discovery;
(b) traces the labeled HOLE (not a positive candidate) back to E17/round85
    Section 4 (2026-07-17) — E17 itself is BLOCKED-with-a-named-ingredient,
    it does not license "both sectors" as live; correctly stated, this
    trace shows only that the hole predates C132/C133, not that E17 solves
    anything — also forced/consolidation, not a discovery;
(c) supplies the tool-run `2n_L=3`-has-no-solution arithmetic under the
    EXCLUSIVE reading, which neither C132/C133 nor round95 wrote out this
    explicitly — genuinely new phrasing (confirmed by git pickaxe, Section
    0 item 2), though it only restates what C133 §8a's own stated formula
    already implies for `N_gen=3`, so it is new PHRASING, not new content;
(d) **supplies the `n_L+n_R=2·N_gen` accounting bridge connecting C133's
    `all→both` SUPPORT PATTERN to the actual zero-mode-COUNT quantity
    C159's own argument needs** — this specific step is this round's own
    derivation, not stated by C133 §8a or §9, and is the one place this
    round adds actual reasoning beyond consolidation, though it is a small,
    mechanical accounting step (doubling a count once a support pattern is
    fixed), not a new physical mechanism.
Per this project's own 5-gate standard: **items (a), (b), (c) are
FORCED-NOT-DISCOVERED** (consolidation of, or new phrasing for, already-
available material); **item (d) is a minor genuine addition**, small enough
that labeling the round's overall character as "scoping/consolidation,
plus one small accounting bridge" is more accurate than either "pure
discovery" or "pure restatement."

---

## 5. What this does NOT mean (per claim.md's own required section)

- Does **not** mean H1c/KT-8 is closed, in either direction — H1c stays
  OPEN, OB1 stays PARKED, exactly as C133 (the most recent primary source
  touching this question) states.
- Does **not** mean `all→both` is a confirmed, physically realized
  structure — it is an unexcluded candidate, explicitly flagged by both
  E17 (BLOCKED, "not established or derivable") and C133 ("the assumed
  Pati-Salam content," not a derived result). Establishing it would still
  require the missing 13D parent action (KT-1), exactly as before.
- Does **not** mean round95's `n_L=n_R` derivation is wrong — it is
  confirmed correct (Section 2). Only its combination with an *assumed*
  `n_L+n_R=3` is blocked, and only because that second premise is not
  forced.
- Does **not** touch OB4, OB11, OB12, OB14, or the C144-158 methodology
  thread — scoped strictly to OB1's H1c/round95/round90/C132/C133
  quadrangle, per claim.md's own scope statement.
- Does **not** commit to any further round on H1c. Per claim.md's own
  explicit escape route, this round stops here.
- **Does not mean claim.md's Prior Result Gate was performed in bad
  faith** — its own text explicitly marked steps 3-5 "to be done by the
  executing agent" and warned "do not skip 3-5 just because this file says
  '0 hits.'" The gap this round found is exactly the gap claim.md itself
  flagged as open and told the executing agent to check.

---

## 6. Self-run adversarial pass (documented per FL Step 8a's "pre-answered
skeptic concerns" allowance — no separate agent invoked this session,
flagged explicitly for the orchestrator below)

Before finalizing, I re-attacked my own ESCAPE-FOUND verdict from a
skeptical angle, actively looking for a reason it might not hold:

1. **"Is `all→both` actually a coherent answer to H1c, or just a label for
   'unselected'?"** Checked: C133 itself calls `all→both` "the assumed
   Pati-Salam content" and explicitly disclaims it as a differentiator.
   This does weaken `all→both` as a *positive* physical prediction — but
   it does not weaken it as a *counterexample to exclusivity*, which is
   all C159's own escape-route criterion requires ("does 'pairing rule'
   have to mean a total function"). The verdict stands: C159 asked whether
   `n_L+n_R=3` is FORCED, and one already-considered candidate in this
   project's own text is sufficient to show it is not, regardless of
   whether that candidate is itself established.
2. **"Does E17 Section 4 actually license 'both sectors, non-exclusive'
   for MULTIPLE channels simultaneously, or only for one channel in
   isolation?"** E17's own text is scoped to "a single generation's
   content" and does not explicitly generalize to all 3 channels at once.
   This is a genuine, narrower reading than I first stated — E17 alone
   would only license a non-exclusive assignment for the *specific*
   channel(s) actually realized, not necessarily all 3 simultaneously.
   **This is why C133's `all→both` (which explicitly IS the all-3-channels
   case, forced by its own `ℤ₃`-channel-uniformity ansatz) is the load-
   bearing citation for the escape, not E17 alone** — E17 supplies only
   that the general *concept* (non-exclusive, both-sector content) was
   already an open, non-excluded question before C133, not that it
   applies to all 3 channels. Decision.md Section 1b/3 above has been
   worded to reflect this distinction (E17 = concept was open; C133 =
   concept applied to all 3 channels, under a stated symmetry ansatz).
3. **"Could `n_L=n_R` itself have a compensating-matter escape instead
   (Kill Criterion row 4)?"** Checked round95's own assumptions section
   (`decision.md:361-367`): "whether any OTHER `SU(4)`-charged
   representation could ever enter this project's construction... not
   checked here; assumed absent based on E17's own stated exhaustive
   `{(1,2),(2,1)}` finding." E17 Section 1 is genuinely exhaustive for
   this project's *specific* connection family (confirmed 1b above) — no
   compensating-matter escape was found. This row of the Kill Criterion
   does not apply; the escape found is specifically the `n_L+n_R=3` row,
   not this one.
4. **"Is this whole finding itself vacuous — does C132/C133 already fully
   supersede round95's tension, making this round a restatement of
   C133?"** No: C133 states the anomaly step "does not discriminate" as a
   narrow methodological aside inside a much larger, differently-scoped
   experiment (the symmetry-ladder coupling-dimension survey) and does not
   frame it as answering "does the n_L=n_R / n_L+n_R=3 conjunction
   constitute a general impossibility proof," which is the specific
   question this round's claim.md was designed to test. This round's
   value is narrowly that consolidation + the explicit tool-run arithmetic
   + tracing the escape back to E17 (2026-07-17), not a mathematical
   discovery.

**Update — independent context-blind skeptic pass WAS run, 2026-09-05,
after this section was first drafted** (claim.md + this decision.md only,
no reasoning chain, per the orchestrator's own follow-through on the
recommendation immediately below). **Verdict: `WEAKENED`.** The skeptic
independently re-read E17/round85 §4 and C132/C133 §8a/§9 directly and
found the same gap this round's own self-review (point 2 above) had
already partially caught but not fully corrected in the front-matter
verdict language: (i) E17 §4 was characterized in an earlier draft's
top-line as "a live, unexcluded candidate" when it is properly
BLOCKED-with-a-named-missing-ingredient — corrected in Section 1b and the
top verdict box above; (ii) the `n_L+n_R=N_gen` → `n_L+n_R=2·N_gen`
accounting bridge was implied to come from C133 §8a itself, when it is
this round's own derived supplement — corrected in Section 3 and Section 4
above. The skeptic found **no defect that overturns the top-line**
(ESCAPE-FOUND survives; C133's `all→both` support pattern, combined with
this round's own accounting, remains a valid counterexample to the
"exclusive pairing is forced" premise) — both corrections are precision
fixes to how the escape is characterized, not to whether it holds. All
edits above (top verdict box, Section 1b, Section 3, Section 4) were made
in direct response to this skeptic pass. This paragraph is left in place,
historically, to show the self-review correctly anticipated the skeptic's
finding (point 2 above) before the skeptic ran, even though the
front-matter text had not yet been brought into line with it.

**Recommendation to the orchestrator (original, now acted on):** given this round
touches OB1's central blocker and effectively redirects part of the
C127-C137 bordism/Pin-structure narrative's framing of "the missing
pairing rule," an independent context-blind skeptic pass (claim.md + this
decision.md only, no reasoning chain) before this is registered in
`OPEN_BLOCKERS.md`/`pearl_registry/INDEX.md` would be worthwhile — primarily
to stress-test point 2 above (the E17-vs-C133 scope distinction), which is
the one place this self-review found and corrected a real overreach in an
earlier draft of this file.

---

## FL Step 4a (Floor-Ceiling Interval) — not applicable, stated explicitly

This round has no continuous metric compared against a numeric threshold —
its Kill Criterion (claim.md) is a discrete classification (PROMOTE /
FORCED-NOT-DISCOVERED / ESCAPE-FOUND / ALREADY-KNOWN), decided by a logical
argument (does a specific conditional hold, given already-established
facts), not a measured statistic. Round95 and round90 — the two primary
sources this round most directly extends — are the same kind of
citation-and-classification round and record the identical thing ("there is
no new numerical script... per this project's own precedent"). Floor
(mechanism-removed baseline) and ceiling (privileged-access bound) do not
have a meaningful construction here: there is no null model whose "success"
would need bounding, and no oracle-with-answer-access analogue for a
yes/no logical-consistency check. This is not a workaround — it is the same
disposition round90/round95 themselves use, extended honestly rather than
manufacturing a floor/ceiling pair to satisfy the hook mechanically.

---

## Check (reproduces this decision)

`python c159_parity_check.py` → reproduces Section 2's output exactly.
All file:line citations in Sections 1a-1f were verified by direct `Read`
this session (not from claim.md's paraphrase). Git pickaxe searches
(`git log --all -S"n_L=n_R"`, `-S"2n_L"`, `-S"n_L + n_R"`,
`-G"2.n_L\s*=\s*3"`) were run directly this session, output quoted in
Section 0.
