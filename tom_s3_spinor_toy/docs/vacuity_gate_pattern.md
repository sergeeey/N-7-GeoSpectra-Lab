# Vacuity-gate-first pattern

**Added:** 2026-09-04, after C151 Stage 2b printed `PREDICTION CONFIRMED`
over a quantity that was identically zero. **Status:** ACTIVE, engineering
convention (not a research claim — see `experiments/_template/vacuity_gate.py`
for the importable helper).

## The incident this closes

C151's blind test of `c(J∇) = ±i·c(∇)` computed `c` and found it
**identically zero** across the whole admissible family. Reduced to
`0 = i·0`, which is satisfied *exactly* — the script's own deviation metric
scored it as `4.9e-16`, i.e. it looked **better** the more vacuous the
result was. The script had already computed a non-vacuity check, but the
check was never wired into the verdict branch, so the first run printed a
confirmation over a vacuum. Caught only by a human re-reading the raw
output, not by any gate.

Two rounds later (C152/C153, same day) this pattern repeated in a different
shape: a sector built from a non-equivariant generator gave `c ≡ 0`, and no
existing gate was sign-sensitive enough to catch it before a test ran on it.

## The rule

```
observable non-zero / non-degenerate?
    NO  -> STOP. Report VACUOUS. Do not evaluate the prediction at all.
    YES -> proceed to test the prediction, and only THEN report a verdict.
```

**Never the other order.** A prediction test evaluated before this gate can
pass "perfectly" on a vacuum — this is the exact shape of validation theater
`~/.claude/rules/skeptic-triggers.md` already names generically (Trigger 3,
"zero failures"); this pattern gives it a concrete, reusable implementation
for numerical prediction tests specifically.

## How to use it

```python
from vacuity_gate import vacuity_gate   # experiments/_template/vacuity_gate.py

values = [max(abs(x)) for x in observable_samples]   # your own metric,
                                                        # NOT the prediction's
                                                        # own deviation stat
gate = vacuity_gate(values, floor=1e-8, label="c on the 6 family basis vectors")
if not gate.nonvacuous:
    print(gate.report())
    raise SystemExit(0)   # or return/continue — STOP before the verdict
# ... only now compute and print the actual prediction verdict ...
```

`floor` must be chosen relative to the numerical process's *own* noise floor
(e.g. `1e-8` for a moderate-depth float64 chain), fixed **before** seeing
whether the current run's data passes it — a threshold tuned after the fact
to let data through is exactly the self-serving bound
`falsification-ladder.md` already forbids elsewhere in this project.

## What "the observable" means here — the part that is easy to get wrong

The gate must check the **same object the prediction is a statement about**,
not a summary of how well the prediction fits. On C151, the vacuity gate
needed to check `max|c(v)|` over the family — **not** `|c(J∇) − i·c(∇)|`,
which is the prediction's *own* deviation metric and is satisfied trivially
(`= 0`) by a vacuum for the same reason the vacuum is a problem in the first
place. Checking the wrong quantity here reproduces the original bug in a new
form.

## Scope

This is a coding pattern, not a Falsification-Ladder step of its own — it
sits inside FL Step 6 ("run test"), as a mandatory sub-step before the
verdict is written, alongside the already-existing Floor–Ceiling Interval
(Step 4a) and Oracle Adequacy Gate (Step 2b), which check related but
distinct failure modes (Step 4a: does the metric have room to move at all,
checked *before* running; this gate: is *this specific run's* observable
non-zero, checked *after* computing it, before trusting the verdict).
