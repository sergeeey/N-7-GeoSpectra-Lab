---
# C191 — test P5's induced pairing rule, under an explicit, user-authorized POSTULATE

**Date:** 2026-09-09
**FL tier:** [x] Full (research claim touching OB1/H1c, per project CLAUDE.md)
**Question type:** [x] descriptive (does postulate P produce definite consequence X — not a causal or predictive claim)

---

## ⚠️ This round tests a POSTULATE, not a derivation

`P5` (C132, 2026-09-02 survey; `OPEN_BLOCKERS.md` OB1 section, C173
closure): identify **one** `so(4)` summand of the already-built,
already-verified `SO(4)×SO(4) ⊂ Spin(8)` block-chirality construction
(pearl_registry, 2026-07-15) with `S³`'s own isometry `SO(4)=SU(2)_L×SU(2)_R`.

This is explicitly flagged, in this project's own words, as **"high AOG-5
risk — no motivation beyond wanting to unblock OB1."** Nothing in this
project's own `G2/SU(3)+S³` geometric content forces this identification;
it is external, route-(c), by C132's own classification. This round does
**not** attempt to justify the postulate. **User explicitly authorized
running it as a stated postulate** ("ставить P5 как явно мотивированный
постулат (не вывод)... ставь если что потом откатим"), understanding the
AOG-5 risk and that it is fully reversible (a new experiment folder,
`git revert`-able).

**What this round DOES test:** granted the postulate, does it produce the
**definite pairing rule** C132's own text claims — *"'which block
chirality' — the datum separating `8_s` from `8_c` — becomes 'which `SU(2)`
factor', i.e. which `t`-sector... That is a pairing rule"* (`decision.md`
line 456-458)? Nobody had computed this before granting the postulate;
this round grants it and checks the consequence.

---

## Prior Result Gate

1. `SO(4)×SO(4) ⊂ Spin(8)` block chirality construction: built and fully
   verified 2026-07-15 (pearl_registry rows, `experiments/20260715-l3b-*`),
   reused here via import, **not rebuilt**.
2. `C38`: `ker D^{t=0}=(1,2)`, `ker D^{t=1}=(2,1)` as `S³`'s own
   `SU(2)_L×SU(2)_R` isometry representations, verified under "the `SO(4)`
   isometry action with the frame lift." Cited as the target to compare
   against, not re-derived.
3. `pearl_registry` row 58 (2026-07-15): `8_s=(2,1,2,1)+(1,2,1,2)`,
   `8_c=(2,1,1,2)+(1,2,2,1)` in `SU(2)^4` notation, independently confirmed
   against `hep-th/9804208`. Cited, then independently re-derived from
   scratch in Section F (`P13`) as a within-round cross-check, not merely
   quoted.
4. **Novelty check:** `grep -rl "C38"` finds `C38`'s own claim and many
   downstream uses, but no prior computation restricting the
   `SO(4)×SO(4)` branching to a single factor and comparing against `C38`.
   `P5`'s own Zero-Signal-Gate entry in `C132` ("PASS (H — V1)") is a
   well-posedness screen, not a computed result — `P5` was explicitly
   gated in `C132`'s own Relaxation Map behind "if a route-(c) postulate...
   is ever granted," which this session's user instruction supplies.
5. **Status:** [x] NEW (the specific computation; the underlying
   `SO(4)×SO(4)` machinery is reused, not new).

---

## Mechanism Claim Gate (Step 0a)

Triggering sentence: *"block chirality `Γ_A` vs `Γ_B` maps `8_s`/`8_c` onto
`t=1`/`t=0`"* (C132's own Zero-Signal-Gate table, P5 row). This is exactly
the kind of design-justifying behavioral claim this gate exists to check
before relying on it — checked directly in Sections C-D below (not assumed
true because it sounds plausible), **FAILS as stated** for the naive
reading (Section D, `P10`), **holds only in a weaker, self-referential form**
under a refined reading (Section F, `P14`/`P15`). Both outcomes reported.

---

## Falsifiable claim

**(a)** Granted the postulate (S³'s `SU(2)_L×SU(2)_R` = one `so(4)`
summand, "ignore" the other), `8_s` and `8_c` have **different** `(j_L,j_R)`
content under S³'s isometry alone.

**(b)** That difference reproduces `C38`'s specific pairing: `8_s` (or
`8_c`) contains `C38`'s `t=0` content `(1,2)` and not `t=1`'s `(2,1)`, or
vice versa, unambiguously.

---

## Kill criterion

**REJECTED** if `8_s` and `8_c` have identical `(j_L,j_R)` content under
S³'s postulated isometry alone (claim (a) fails), **regardless of** whether
a refined/strengthened version of the postulate might do better — that
refinement, if checked, is reported separately, not folded into a rescued
version of claim (a) itself.

## What was found

**Claim (a) is REJECTED, exactly and cleanly (`P8`–`P10`, 15/15 checks
overall pass — the checks themselves confirm the negative, not fail to
run).** Restricting the already-verified `SO(4)×SO(4)` branching
(`8_s=(2,1,2,1)+(1,2,1,2)`, `8_c=(2,1,1,2)+(1,2,2,1)` in `SU(2)^4`
notation) to just the first `so(4)` factor (S³'s postulated isometry,
summing over the second factor's own quantum numbers) gives:

```
8_s restricted to (L1,R1): 4-dim (j_L=1/2,j_R=0) + 4-dim (j_L=0,j_R=1/2)
8_c restricted to (L1,R1): 4-dim (j_L=1/2,j_R=0) + 4-dim (j_L=0,j_R=1/2)
```

**Identical.** `S³`'s own isometry, taken alone, cannot tell `8_s` from
`8_c` — the postulate as C132's sentence states it does **not** produce a
pairing rule. This is a genuine finding, not a re-statement of something
already known: nobody had run this specific restriction before.

**Role-swap, checked rather than assumed by symmetry (Section G,
`P16`-`P17`, added same session after an initial draft of this claim had
flagged the swap as untested):** does it matter *which* of the two
`so(4)` factors is postulated to be `S³`'s isometry? Restricting to the
*second* factor instead gives the identical `4×(1/2,0)+4×(0,1/2)`
structure for `8_s` (`P16`, exact match to the first-factor case) and the
same `8_s`=`8_c` collapse (`P17`) — the naive rejection (claim a) does
**not** depend on the arbitrary choice of which factor plays "S³'s role";
the construction's own `H↔Hl` block symmetry makes the two choices
equivalent, now confirmed by computation rather than left as a plausible-
but-unchecked symmetry argument.

**Steelman, checked before writing this verdict (Section F, `P12`-`P15`):**
does fixing the *second* `so(4)` factor's own quantum number `(L2,R2)`
(treating it as an independent "internal" label the postulate left
unaddressed) rescue the pairing? **Partially, and revealingly.** At each
*fixed* `(L2,R2)` value, `8_s` and `8_c` **do** separate cleanly (`P14`):

```
at (L2,R2)=(1/2,0):  8_s -> (L1,R1)=(1/2,0)   8_c -> (L1,R1)=(0,1/2)
at (L2,R2)=(0,1/2):  8_s -> (L1,R1)=(0,1/2)   8_c -> (L1,R1)=(1/2,0)
```

But the pairing **flips** between the two `(L2,R2)` choices (`P15`): `8_s`
always tracks whichever `(L1,R1)` **matches** `(L2,R2)`, and `8_c` always
tracks the **mismatch**. This is not "which SU(2) factor is which
t-sector" (C132's sentence) — it is "does the S³-side label match the
S⁶-side label," a strictly more complex, self-referential structure that
needs an **independent** physical meaning for `(L2,R2)` (presumably an
S⁶-side triality label) before it says anything about `t=0` vs `t=1` at
all — and supplying that independent meaning is exactly the missing
ingredient `C173` already named (Part 5, or a genuinely new non-`G2`
construction), not something this round's postulate alone provides.

## Negative control

None needed beyond the reused construction's own 2026-07-15 controls
(triality-invariance, Cl(8) relations, cross-literature check against
`hep-th/9804208`) — this round adds no new machinery to the Clifford
algebra itself, only a restriction/decomposition on top of it, verified
directly against the known branching (`P13`, exact match).

## Kill Analysis

**What this round killed:** the specific reading "one `so(4)` factor = S³'s
isometry, ignore the other factor" as a source of a `t=0`/`t=1` pairing
rule (claim (a), `P10`). **What survives:** the underlying `SO(4)×SO(4)`
construction itself (untouched, re-verified); the refined
match/mismatch structure (`P14`/`P15`), which is real and could in
principle carry information **if** an independent physical meaning for the
second `so(4)` factor's quantum number were ever supplied — but that is a
**separate, larger, still-unaddressed postulate**, not a free consequence
of `P5` as C132 stated it.

**Revival condition:** if `Part 5` (or any future source) supplies an
independent physical interpretation of the second `so(4)` factor's
quantum number as an actual S⁶-side triality/gauge label (not just "the
other half of the Clifford algebra"), the match/mismatch structure found
here (`P14`/`P15`) becomes directly testable against `C38`'s specific
`t=0↔(1,2)`/`t=1↔(2,1)` assignment. Until then: **no revival — the
postulate as stated in C132 does not, by itself, produce the claimed
pairing; this is not a contingent gap fillable by more computation on
this project's own existing content**, since the missing ingredient (an
independent meaning for the second SO(4) factor) is definitionally
external, matching `C173`'s already-established closure reasoning.

## What this does NOT establish

- **Does not touch whether the postulate itself (identifying S³'s isometry
  with a `Spin(8)`-fiber `so(4)` factor at all) is physically true** — this
  round only tested one specific consequence of granting it.
- **Does not rebuild or re-verify the `SO(4)×SO(4)` construction from
  scratch beyond the reused import** — `P1`/`P2` confirm the import is
  well-formed; the deeper triality-invariance/uniqueness claims are
  `C173`'s and the 2026-07-15 pearls', not re-derived here.
- **Does not exhaust every possible reading of P5** — three readings are
  now checked (naive: ignore the second factor, `P10`; refined: fix its
  quantum number, `P14`/`P15`; role-swap: which factor plays "S³'s role",
  `P16`/`P17`, checked not assumed). **Still not attempted:** a *split*
  identification (`S³`'s `SU(2)_L` from the first factor, `S³`'s
  `SU(2)_R` from the second, rather than one factor wholesale), and a
  *dynamical* (not fixed-value) treatment of the second factor's quantum
  number. Neither is excluded by this round.
- **Does not change `OB1/H1c`'s status** from `PARKED` — this round
  sharpens (does not resolve) what a working `P5`-style construction would
  actually need to supply.

## Floor–Ceiling (Step 4a)

The metric here is discrete (does a clean pairing exist: yes/no), not a
continuous statistic — Floor-Ceiling in the numeric-interval sense does
not apply to this shape of check. Substituted with the equivalent
discrete safeguard already built into the round: `P8`/`P9` independently
re-derive the known `SU(2)^4` branching (`P13`) as a positive control
before `P10`'s negative conclusion is drawn — the machinery is shown
capable of reproducing an already-known-correct result before it is
trusted to report a new negative one.

## Reproduction

```
cd experiments/20260909-c191-p5-so4-postulate-pairing-test
python c191_p5_postulate_pairing.py
```

`15/15`. `ruff check` and `ruff format`: to be run before commit.
