# Prior Result Gate — MANDATORY, before writing any new round's claim.md

**Why this exists:** Round 46 (2026-07-13) rediscovered a result Round
30 (2026-07-11) had already closed, two days earlier, in this same
directory — wasting a full round because Round 39 (2026-07-12) had
itself reopened the question without checking, and Round 46 trusted
Round 39's framing without independently verifying it was still open.
This is not a one-off mistake; it is a structural risk in any project
with 45+ rounds of accumulated state. This gate makes the check
mandatory and mechanical, not a thing to "remember to do."

**Rule:** no `roundNN_claim.md` may be written in this experiment
until this gate is filled in and its final status is NEW or OPEN. If
the status comes back CLOSED / SUPERSEDED / DUPLICATE / RETRACTED /
PARKED, STOP — do not write the round. Report the finding instead.

## The 7 steps (run in order, every one, every round)

### Step 1 — State the exact claim
Write the ONE-SENTENCE falsifiable claim the new round would test,
in the same precise terms you'd put in `round NN_claim.md`'s own
"Claim" line. Vague claims cannot be gate-checked — sharpen first.

> Claim: _______________________________________________

### Step 2 — Search `decision.md` for the formula and its synonyms
```bash
grep -in "<key term 1>\|<key term 2>\|<synonym>\|<the exact formula, ASCII-approximated>" decision.md
```
Read every hit's surrounding paragraph, not just the matched line —
Round 39's own miss happened because the *topic* was mentioned in
passing without triggering a "this is already closed" recognition.

### Step 3 — Search `round*_claim.md` files and their scripts directly
```bash
grep -rln "<key term>" round*_claim.md
ls g2su3_round*<key term>* 2>/dev/null
```
If a matching script exists, RUN IT — do not assume from the filename
alone what it established.

### Step 4 — Search `null_results/` and `parked/` (both INDEX.md and
individual files, project-level AND this experiment's own entries)
```bash
grep -in "<key term>" null_results/INDEX.md parked/INDEX.md
grep -rln "<key term>" null_results/ parked/
```

### Step 5 — `git log` pickaxe search (catches renamed/refactored code
and reverted-but-still-informative commits the file-based searches above
can miss)
```bash
git log -S "<key term or formula fragment>" --oneline -- "experiments/20260708-dolan-casimir-g2su3/"
git log -G "<regex for the formula>" --oneline -- "experiments/20260708-dolan-casimir-g2su3/"
```

### Step 6 — Search primary sources and attribution notes
Re-read (not recall from memory) the relevant pages of the primary
source PDF(s) already in this repo (Agricola 2002, AHL2023, etc.) for
the specific claim — does the SOURCE already define/settle this, making
the claim near-definitional rather than a discovery to make? (This is
exactly what both Round 30 and Round 46's own skeptic review had to
re-derive independently — checking it BEFORE building saves a full
round.)

### Step 7 — Declare the final status (pick exactly one)

| Status | Meaning | Action |
|---|---|---|
| **NEW** | No prior work touches this claim at all | Proceed to write the round |
| **OPEN** | Prior work touched it but explicitly left it unresolved, AND you independently re-confirmed it's still unresolved (not just citing the old "left open" text) | Proceed to write the round |
| **CLOSED** | A prior round already answered this, with a verdict that still stands | STOP — cite the prior round, do not re-derive |
| **SUPERSEDED** | A prior round answered a related-but-different version; the current claim needs to state precisely what's different | STOP — either sharpen the claim to the genuine delta, or don't proceed |
| **DUPLICATE** | Same claim, same scope, already fully answered — this is what Round 46 actually was | STOP — cite the prior round, do not re-derive |
| **RETRACTED** | A prior round claimed this then walked it back (skeptic-killed, or self-corrected) | STOP — read why it was retracted before considering any revival; needs a genuinely new condition, not a re-run |
| **PARKED** | Already explicitly parked with a revival condition | STOP unless the revival condition is concretely met — cite the park file |

## Retroactive validation (run once, to prove the gate actually works)

Applied to Round 46's own claim ("Casimir_su3 = Jac_h-induced operator,
on the full 8-dim Σ") as if this gate had existed on 2026-07-13 before
writing it:

- Step 1: Claim = "Casimir_su3 (su3_action) equals C~h (Agricola Prop
  3.3, built from curv_h/Jac_h), exactly, on the full 8-dim Σ."
- Step 2: `grep -in "casimir_su3\|jac_h\|c.h\|casimir.*su(3)" decision.md`
  → hits at Round 26 (open question raised), Round 30 (**"Ch_tilde ==
  Casimir_su(3) is a STRUCTURAL consequence"**), Round 39 (question
  reopened as "left open," no citation to Round 30).
- Step 3: `ls g2su3_round30*` → `g2su3_round30_ch_casimir_structural.py`
  exists. Running it: exit 0, `Ch_tilde == Casimir_su3` asserted True.
- Step 4: not in null_results or parked (never rejected — it was
  PROMOTEd).
- Step 5: `git log -S "Ch_tilde" --oneline` would show the Round 30
  commit (2026-07-11) predating any Round 46 work.
- Step 6: Agricola 2002 p.10 defines `C~h` as the Casimir-of-h lift —
  would have been read at Step 6 instead of discovered post-hoc by a
  skeptic.
- Step 7: **Status = DUPLICATE.** Gate would have stopped Round 46
  before any code was written, saving the full round.

**Conclusion: this gate, mechanically applied, would have caught
Round 46's mistake in Step 2 alone** (Round 30's own decision.md entry
literally contains the headline "Ch_tilde=Casimir_su(3) structural
derivation"). The failure was not a missing tool — it was skipping the
check. This document exists so skipping is no longer the default.
