# Negative-control pattern

**Added:** 2026-09-07, after the C179–C182 round sequence produced five
verification checks that could not fail by construction. **Status:** ACTIVE,
engineering convention (not a research claim — see
`experiments/_template/negative_control.py` for the importable helper and
`scripts/check_negative_control.py` for the checker).

Sibling of `vacuity_gate_pattern.md`, and the two are not the same check.
The vacuity gate asks *is this run's observable non-zero?* This one asks *can
this check report failure at all?* A check can pass the vacuity gate on a
perfectly non-zero observable and still be unable to fail.

## The incident this closes

Five checks in one round sequence could not fail. In **every one of the five
the underlying physics was correct** — what failed was the machinery built to
establish that it was correct.

| # | Check | Why it could not fail |
|---|---|---|
| 1 | C180 multiplicity check | the pattern `(k+1)(k+2)/k(k+1)` is forced by **any** su(2) generator set, so it could not tell right- from left-invariant fields |
| 2 | C182 no-go condition | required `abs(w)` near 0.5 **and** below 1e-9 at once — unsatisfiable |
| 3 | C181 discrimination test | ranked the **same matrix twice** and called the two ranks different objects |
| 4 | C181B Frobenius-norm test | the Frobenius norm is invariant under `M -> u M v†` for **any** matrix, so it separates no block from any other |
| 5 | C180 connection-constant solve | returns `c = 3/2` uniquely, but 3/2 sits in every candidate set as an algebraic identity (observed eigenvalues are exactly `-n` and `n+3`, so `val ± (n+3/2)` collapses to 3/2); a spectrum shifted by +1 returns a unique 2.5 instead |

The fifth is subtler than the rest and was the most consequential: the check
cannot fail to return **a** unique answer, and it had already reached a letter
intended for someone outside the project as that section's strongest point.

**Who caught them.** Three of the five: external context-blind skeptics, *after*
the round had declared itself done. One: a negative control deliberately placed
in the script. One: a corrupted-input replay, run only because a skeptic queried
the wording. **Self-review caught none of the five.** A sixth shape then turned
up in the very script written to audit the other five — a cannot-fail *conjunct*
(`Tr(uAu†) = Tr(A)`, true for any matrix) inside a compound `A AND B` check that
can fail via `A`. That one was found by an independent code review.

The asymmetry is the whole point of the convention: the skeptic-caught defects
surfaced **after** the round closed; the control-caught one **before**.

## The rule

```
for every check whose PASS you intend to quote as evidence --
    run the SAME check on an input for which it MUST report failure.
    control also passes?      -> the check discriminates NOTHING. Not evidence.
    control fails as it must  -> the check has falsifying power. Quote it.
```

The control's outcome goes into the results JSON as a **boolean**, not into
stdout to be eyeballed. `scripts/check_negative_control.py` reads that boolean.

## How to use it

```python
from negative_control import negative_control   # experiments/_template/

def check(spectrum):                    # your own check, returns bool
    return solve(spectrum) == expected

nc = negative_control(
    check,
    real=observed_spectrum,
    controls={
        "every eigenvalue shifted by +1": shift(observed_spectrum, 1.0),
        "one multiplicity broken":        break_multiplicity(observed_spectrum),
    },
    label="connection-constant solve",
)
print(nc.report())
res["negative_control"] = nc.as_dict()  # <- the boolean the checker reads
# ... and do not quote the check as evidence unless nc.discriminates ...
```

Then, before the round closes:

```bash
python scripts/check_negative_control.py experiments/<round>/
```

`OK` / `OK-LEGACY` → the file records a control. `CONTROL-FIRED` → the round's
own control says the check discriminates nothing; withdraw that check.
`MISSING` → no control recorded; exit code 1.

## Choosing the control input — the part that is easy to get wrong

The control must break the **specific property the check claims to be sensitive
to**, not merely be different data. Both failure shapes below are taken from the
five above, not invented:

- **Too weak.** C180's multiplicity check was fed only genuine su(2) data. The
  pattern is forced by *any* su(2) generator set, so no su(2)-derived control
  could ever have exposed it — the control had to come from outside that family.
- **The same object twice.** C181's discrimination test ranked one matrix twice.
  A control that is a relabelling of the real input is not a control.

A control the check passes is a **result, not a bug in the control**: it means
the check does not discriminate. Record `discriminates: false` and withdraw the
check. Do not tune the control until the check looks good — that is the
self-serving threshold `falsification-ladder.md` already forbids elsewhere.

## Compound checks — the sixth shape

`A and B` looks like two independent tests and may not be. If `B` is an identity
(true for any input), the conjunction still fails via `A`, so it is not a
cannot-fail *check* — but quoting it as two corroborating tests is an overclaim.
Control each conjunct separately, or say in the results which conjunct carries
the falsifying power, as `c181b` now does
(`"falsifying_power_is_entirely_in": "offdiag_x0_drift > 1e-3"`).

## Defects found in this machinery itself

The pearl notes that a sixth cannot-fail shape turned up in the very script
written to audit the other five. The same thing happened again here: a
context-blind review of the helper and checker, run before either was committed,
found four defects. All four were reproduced by running them, then fixed, and
each now has a regression test in `tests/test_negative_control.py`. **Self-review
had not caught any of them** — the seventh instance of that asymmetry in this
sequence, and directly on-point for what the pearl is predicting.

| Defect | What it did | Fix |
|---|---|---|
| Stateful check certified as discriminating | a check answering from call order (`return self.n == 1`), never inspecting its argument, produced the exact success signature — pass on real, fail on every control | the helper now calls the check on the real input **twice**, before and after the controls, and requires agreement (`deterministic_on_rerun`) |
| Genuine control discarded | `_canonical` returned `MISSING` on the first malformed entry, throwing away a co-located block that *was* a valid discriminating control — contradicting the module's own "at least one" contract | entries are sorted into good / fired / malformed; a fired control outranks a good one, malformed entries are named in the reason but do not erase a good one |
| Zero files scanned printed `RESULT: PASS` | a mistyped path read as a clean bill of health to anything gating on the exit code — a cannot-fail check inside the script built to forbid them | zero files is never a pass: explicit paths matching nothing exit 1; `--since` with no rounds yet in scope prints `NOTHING IN SCOPE` |
| Legacy shapes usable as an enforcement bypass | a lone `discriminates: true`, or any corruption-named boolean plus an *unrelated* mixed-polarity table anywhere in the file, cleared the gate | legacy shapes no longer satisfy enforcement for rounds dated ≥ `CONVENTION_START`; they stay readable for the pre-convention files that have them |

The last one was fixed by narrowing what legacy recognition is *for*, not by
making the heuristics cleverer — an arms race over shapes nobody should be
writing any more.

Measured, since the bypass is a construction and the question is whether it
fires in practice. Over all 203 real `results*.json` files: 21 carry a
corruption-named boolean but no mixed-polarity table (rejected), 13 carry a
table but no corruption name (rejected), and **3 carry both — all three genuine
controls** (`round72-e7`'s Jacobi-identity control, `c126`'s explicit
positive/negative pair, `c180b`'s corruption replay). Plus `c181b` via the
`discriminates` form: 4 legacy recognitions, 0 false positives. So the pairing
holds on this corpus; it is defeatable by construction, which is why it no
longer counts inside the enforced window rather than why it was rewritten.

## What the checker still cannot do — stated because a checker that appears to verify more than it does is the same defect

1. It **cannot tell whether the control input was adversarial enough.** C180's
   su(2) control would pass this checker and still be worthless. That judgement
   stays with a human or a context-blind skeptic.
2. It asks for **at least one** negative control per results file. It cannot map
   controls onto individual checks — that would require every round to report in
   a uniform schema, a far larger change than the observation justifies.
3. On the two legacy forms it validates the **shape** of a control record, not
   the control. Only the canonical helper block is fully validated — which is
   why legacy shapes stop counting inside the enforced window.
4. The determinism re-run catches a check that ignores its input. It does **not**
   catch a check that inspects its input and is simply wrong about it.

## Scope and enforcement

Like the vacuity gate, this is a coding pattern, not a Falsification-Ladder step
of its own — it sits inside FL Step 6 ("run test"), before the verdict is
written. It is the run-time counterpart to Step 4a (Floor–Ceiling Interval),
which asks the same question about the *threshold* before the run; this asks it
about the *check* during the run.

Enforcement is **forward-only**. `check_negative_control.py` enforces on rounds
dated on or after `CONVENTION_START = 20260908`; `--all` reports coverage over
every round and always exits 0. Nothing about how an existing round reports its
results has to change. Baseline at the time of writing: 4 of 203 historical
results files carry a recognisable control
(`round72-e7`, `c126`, `c180b`, `c181b`).

## Scoring the prediction this came from

`pearl_registry/INDEX.md` (2026-09-07) predicts that with this convention in
place, over the next five rounds the count of cannot-fail checks found by an
**external skeptic** drops to at most 1, while the count found by **the script's
own control** rises. To score it:

```bash
python scripts/check_negative_control.py --since   # control-caught + coverage
```

The scoreboard block it prints gives the control-caught count directly. The
skeptic-caught count is **not** machine-readable and must be counted by hand
from each round's `decision.md` Step 8a section. Record both in the tally line
appended to that pearl row.
