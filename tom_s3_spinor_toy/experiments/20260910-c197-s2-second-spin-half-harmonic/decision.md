# C197 Decision — CONFIRMED. A genuine second spin-1/2 S² harmonic, found where round-3 skeptic pointed.

**Date:** 2026-09-10
**Verdict:** **CONFIRMED**, `9 of 9` checks pass. Exact symbolic arithmetic
+ 30-digit numeric cross-check for the one closed form sympy would not
auto-collapse. All numbers trace to `c197_second_spin_half.py` and
`run_output.txt`.

---

## 1. Result

```
k=3, fibre weight -1/2, m_R=-1/2, stripped of psi:
  e^{-iφ/2} · cos(θ/2) · (3cos²(θ/2) − 2)
```

Same ψ-weight as `χ_{±1/2}` itself (`-1/2`, not `-3/2`) — genuinely
spin-weight 1/2, unlike `C196`'s own object (spin-weight 3/2). Confirmed
double-valued (`D1`) and NOT a constant multiple of either `χ_{+1/2}` or
`χ_{-1/2}` (`D2`, both directions) — and unlike `C196`'s own D2 check
(which could not fail, since that object had different φ-periodicity by
construction), this D2 is a genuine, failable comparison: both objects
share the same `-1/2` periodicity, so agreement was not guaranteed.

## 2. Why this experiment exists

A round-3 context-blind skeptic review of the letter drafted using `C196`
found that `C196`'s object, described in that letter as "genuine spinor-
type content," is actually spin-weight 3/2 (confirmed by hand-folding its
formula to `cos³(θ/2)e^{-3iφ/2}`) — a different associated bundle from the
spin-1/2 one `χ_{±1/2}` lives in. The same review pointed out that `C196`'s
own `run_output.txt` already lists the fibre weights present at `k=3`
(`[-3/2,-1/2,1/2,3/2]`), and that the weight `-1/2` sector — the genuine
second spin-1/2 example — was one script iteration away, never computed.
This experiment computes it.

## 3. Floor–Ceiling (Step 4a)

Metric: **is the k=3, weight-(-1/2) object a genuine, non-trivial second
member of the spin-1/2 tower, or degenerate/proportional to what's already
known.**

FLOOR (mechanism absent) = `0.0`. If the descent method failed to
generalize to a second spin-1/2 example, the object would either fail to
be double-valued, or collapse to a constant multiple of `χ_{+1/2}` or
`χ_{-1/2}`.

CEILING (full confirmation) = `3.0`. Three independent properties hold:
double-valued (D1), not proportional to `χ_{+1/2}` (D2a), not proportional
to `χ_{-1/2}` (D2b).

OBSERVED = `3.0` (all three pass).

EFFICIENCY = `(3-0)/(3-0)` = **`1.0`**.

## 4. What this does NOT establish

- Does not derive the general family for all `j` — this is `j=3/2`
  specifically, a second data point alongside `χ`'s `j=1/2`.
- Does not re-derive or connect to `C185`'s S² Dirac operator spectrum —
  orthogonal result, both about S² but via different constructions.
- Does not affect `C196`'s own verdict (still correctly CONFIRMED for what
  it actually established — a spin-weight-3/2 tower member) — this
  experiment adds a sibling result, not a correction to `C196` itself
  (the correction to how `C196` was *described* was made separately, in
  `C196/claim.md` and the letter draft).

## 5. Reproduction

```
cd experiments/20260910-c197-s2-second-spin-half-harmonic
python c197_second_spin_half.py
```

`9/9` (~1-2 min). `ruff check` and `ruff format`: clean.
