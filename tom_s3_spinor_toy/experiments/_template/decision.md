# <ID> — Decision

**Date:** YYYY-MM-DD
**Verdict:** `PROMOTE` | `REPEAT` | `REJECT` | `ARCHIVE`
**Evidence marker:** `[VERIFIED-tool]` | `[VERIFIED-REAL]` | `[HYPOTHESIS]` | `[WEAK]`

---

## 0. Summary

One table. What was asked, what came out. No narrative.

| | result |
|---|---|
| | |

---

## 1. Floor–Ceiling (FL Step 4a) — resolved BEFORE the run, not after

| | value | how constructed |
|---|---|---|
| FLOOR | | the same pipeline with the tested mechanism REMOVED |
| OBSERVED | | |
| CEILING | | a performer with privileged access to the answer |

`efficiency = (observed − floor) / (ceiling − floor) = `

Threshold ≤ floor → `CRITERION_INVALID`. Ceiling < threshold → `TASK_INFEASIBLE`.
Ceiling ≈ floor → `NO_HEADROOM`. **None of the three is evidence against the claim.**

---

## 2. Kill Analysis — REQUIRED for every REJECT

**Killed:** H under conditions {A₁ ∩ A₂ ∩ A₃} — state the conjunction explicitly.

**NOT killed:** the core mechanism X (independent basis: …), A₁, A₂ — state what
still stands, or a later reader will assume the whole direction died.

**Relaxation Map** — one assumption per row, never bundled:

| assumption | Remove | Weaken | Replace |
|---|---|---|---|
| A₁ | | | |

---

## 3. Revival Condition — MANDATORY for every REJECT

> Added 2026-09-07 to `~/.claude/rules/falsification-ladder.md` § On REJECT.
> Motivation, measured across 7 repos: `123` REJECT vs `20` PARKED (`6.2×`), with a
> revival condition recorded in **at most 9%** of rejection-bearing `decision.md`
> files. The cause was structural — the ARCHIVE branch had always asked "what would
> trigger revival", the REJECT branch never did.

**What specific, measurable event would bring this direction back?**

Same standard the Pearl Registry enforces for `next_check`: a real event, threshold
or milestone. Not "someday", not "when tooling improves", not "with fresh eyes".

```
Revival condition: <event / threshold / artifact that must appear>
Who or what would produce it: <so it is checkable, not aspirational>
```

**OR — and this is a complete answer, not a lesser one:**

```
hard_killed — <the closing mechanism>, see <ref>
```

`hard_killed` is a status that already exists in FL, outside Rescue scope. Use it
honestly rather than decorating the field.

⚠️ **The two failure modes are symmetric, and the second is the sneakier:**
an empty field hides a direction that could have been revived; a *manufactured*
condition ("if we look again with better tools") is unfalsifiable widening and is
worse than an honest `hard_killed`, because it looks like the field was satisfied.

### How to tell which answer you owe — ask what the kill rests on

| the kill rests on | verdict |
|---|---|
| a **contingent assumption** — an ansatz, a restricted domain, a chosen family, a missing mechanism | a **real** revival condition exists: relax exactly that assumption |
| a **theorem** | `hard_killed`, and that is the honest answer — "revive it by making the theorem false" is a wish, not a condition |

Without this split the field is satisfiable by reflex — *"revival = if what killed
us were not true"* — which passes every time and so certifies nothing. **That
reflex is itself a cannot-fail check, one level up.**

**Practical note from the 8-case test that produced this table** (random sample of
this project's own `null_results`, 2026-09-07): in 6 of 8 the kill was contingent,
and in **all six the entry had already named its own conditioning assumption in the
kill text** — *"STRUCTURAL: … with power-law T"*, *"factor 3 unaccounted by spin
geometry"*, *"forces T=0 in vacuum"*. So filling this field is usually not new
work; it is promoting a qualifier you already wrote into a place a later reader
will find. The other 2 rested on theorems (`π₅(S⁶)=0`; `η mod 2` identical on every
interval) and are honest `hard_killed`.

---

## 4. Skeptic Response Matrix (FL Step 8a) — skeptic is NOT a veto

| Verdict | Concern | Response: Fix / Accept-with-doc / Dismiss-with-reason / Mitigate |
|---|---|---|
| | | |

`FALSIFIED` ≠ killed. A true kill means the CORE predicate is false **and** none of
the four responses is viable. This is rare — most concerns resolve as Dismissed or
Accepted-limitation.

---

## 5. Pearl Gate / Caveat Gate

- Did this surface an unexpected but testable side-finding? → `pearl_registry/INDEX.md`
- Did I write a caveat naming a SPECIFIC untested alternative? → same registry, same row shape

---

## 6. Status

Where the artifacts live, what was committed, what was not.
