# Step 7 — does the C11 chain (C41–C57) reopen OB1 (KT-8 / `N_gen=3` zero-mode blocker)?

**Experiment id:** `20260810-c11-vs-ob1-kt8-crossreference`
**Date:** 2026-08-10 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessor:** the whole day's C11 chain (C41–C57); OB1 (`OPEN_BLOCKERS.md`, PARKED 2026-07-17)

---

## Zero-Signal Gate

- **Entity:** the C11 spectral-triple chain run today (C41–C57) and OB1, the parked
  KT-8/`N_gen=3` zero-mode blocker.
- **Falsifiable predicate:** either C41–C57 meets ≥1 of OB1's four explicit reopen
  conditions, or it does not.
- **Measurable outcome:** direct inspection of C41–C57's actual statements against OB1's
  four conditions, verbatim from `OPEN_BLOCKERS.md`.

Gate passes.

## Mandatory pre-work check, per the Adaptive Iteration Branch Rule

Before treating "`N_gen=3`" as a fresh question, `grep`:

```
$ grep -in "kt-8\|kt8\|zero.mode\|torsion.select\|n_gen" null_results/INDEX.md
$ grep -in "kt-8\|kt8\|zero.mode\|torsion.select\|ob1\b" parked/INDEX.md
```

**Result: `OB1` is PARKED, not open.** `OPEN_BLOCKERS.md`'s OB1 section and
`parked/INDEX.md`'s `OB1-PARENT-ACTION` entry record **four independent mechanism
attempts (rounds 114–117)**, all null/falsified/equivalent-restatement, reaching
"diminishing returns" and an explicit `STATUS: PARKED — REOPEN ONLY ON NEW EXTERNAL
INPUT`.

**This changes what "step 7" honestly means.** It is not "solve `N_gen=3`" — that headline
is `C4_NGEN3_HEADLINE`, `truth_status: CONDITIONAL`, `test_outcome: CONFLICTING`, resting on
four dependencies (`C1`, `C2`, `C3`, `C_G67C3_THIRD_CHANNEL`), of which `C3` (no zero mode
for the untwisted/Levi-Civita full operator) is what OB1 tracks. **Re-running a null-result
search without a revival condition is exactly what the Adaptive Iteration Branch Rule
forbids.** Step 7, correctly scoped, is: *check whether today's C11 work constitutes a
revival condition* — nothing more, nothing less.

## OB1's four reopen conditions, quoted verbatim

1. A concrete candidate action is found (external literature or new internal insight).
2. A directly relevant parent mechanism is published somewhere new.
3. A new derivation map linking geometry → Dirac operator → torsion emerges from OTHER
   work in this project.
4. Any candidate must pass `PARENT_ACTION_GATE.md`'s checklist before being attempted.

## The claim under test

> **C58 (proposed).** C41–C57 does **not** meet any of OB1's four reopen conditions, and OB1
> should remain PARKED. The C11 chain is orthogonal to OB1's actual question.

**Falsifier, fixed in advance:** if any single claim in C41–C57 supplies an
action/symmetry/topology argument that forces a **single** value of `t` (0 or 1, not both)
over Levi-Civita `t=1/2` — the thing OB1 has searched for since round62 — C58 is refuted and
OB1 should be reopened under condition 3.

## The scope distinction this hinges on, stated precisely

| | OB1's question (KT-8, `C3`) | C11's question (this session) |
|---|---|---|
| Object | **one copy** of `D_{S³}(t)` for **one** `t`, tensored with `D_{S⁶}` | **both** `t=0` and `t=1` combined as **two sectors** of one Hilbert space |
| Asks | is a **single** `t≠1/2` physically selected? | does the **combination** of both `t` form a valid NCG spectral triple? |
| This session's answer | not addressed | **no** — not earned (C45/C48/C50/C51), and even if taken, fails orientability/PD (C49/C52–C54) |

**These are different objects.** A verdict about the doubled two-sector construction does not
transfer to the single-copy question — the same non-transfer discipline this project's own
`artifact-provenance-gates.md` Gate 1 requires for any two related-but-distinct artifacts.

## Predictions, recorded before the check

| # | Prediction |
|---|---|
| **S1** | condition 1 (concrete candidate action): **not met** — no claim in C41–C57 proposes an action, symmetry, or anomaly principle |
| **S2** | condition 2 (external publication): **not met** — the entire chain is internal computation |
| **S3** | condition 3 (new derivation map from other project work): **the closest candidate**, and the one requiring real scrutiny — does "NCG spectral-triple axioms don't force the doubling" constitute a new geometry→Dirac→torsion derivation map? |
| **S4** | C46 ("if taken, the doubling is a parity doubling") is the single most KT-8-adjacent finding in the chain — does it, specifically, meet condition 3? |
| **S5** | round116 (2026-07-17) already proved the minimality fact this session's C44 cites (`t=0,1` innermost crossing pair) — **C44 correctly cites and extends it** (closing round116's own flagged multiplicity gap via `dim ker`), rather than duplicating it as new |

## What this cannot show

- It does not determine whether `N_gen=3` is true. That headline stays exactly where it was:
  `CONDITIONAL`/`CONFLICTING`.
- It does not attempt E3's own recommended next actions (plugging the real
  `G73`/`G74A`-verified `D_{S⁶,twisted}` operator into the Cl(9) framework; finding a physical
  selection principle) — those remain genuinely open and are **not** what this round attempts.
- It is not a new physics result. It is a scope/status assessment, and its value is entirely
  in correctly **not** reopening a properly-parked item, and in explicitly recording that this
  session's chain was checked against it.

## kill_criterion

C58 is refuted if any of S1–S4 comes back "met" on honest re-reading of C41–C57's actual
statements.
