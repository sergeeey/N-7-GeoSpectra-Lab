# C197 Decision — CONFIRMED. A genuine second spin-1/2 S² harmonic, found where round-3 skeptic pointed.

**Date:** 2026-09-10 (§6 hardening addendum added 2026-09-16)
**Verdict:** **CONFIRMED**, `9 of 9` checks pass. Exact symbolic arithmetic
+ 30-digit numeric cross-check (now at 5 points, see §6) for the one
closed form sympy would not auto-collapse. All numbers trace to
`c197_second_spin_half.py` and `run_output.txt`.

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

## 6. Post-hoc hardening (2026-09-16) — code-review findings addressed, one left honestly open

A `skeptic` code review of this script (run as part of an unrelated harness
test — the `doubt-driven-development.md` Independent Review Fallback
Policy dogfood, 2026-09-12) surfaced four findings. Three fixed at the
source, one is NOT a quick fix and is recorded as still open rather than
forced:

- **Fixed — C3 was a one-point numeric check** for a closed form quoted
  verbatim in the letter to Tom. Now checks 5 points spanning both halves
  of θ and multiple φ quadrants, none a special value where a sign error
  could cancel by symmetry. All 5 residuals `0.0` to 30 digits.
- **Fixed — D2's `sp.diff(ratio) != 0` was symbolic-only**, trustworthy
  only as far as sympy's own simplification of that derivative. Added a
  concrete, tool-independent numeric check: the ratio evaluated at two
  different θ values must differ (a fact no simplification bug can hide).
  Both checks agree for both `χ_{±1/2}` comparisons.
- **Fixed — C2's label overreached**, describing an algebraic
  sanity-check (did the ψ-phase genuinely cancel after stripping) as if it
  carried physics content on its own. Reworded to say what it actually is.
- **NOT fixed, honestly left open — no direct spectral verification that
  `q` is an eigenfunction of `C185`'s actual S² Dirac operator at the
  matching eigenvalue.** This is not a quick addition: `C185`'s operator
  acts on 2-component spinors `(f,g)·e^{imφ}` with the SAME `m` on both
  components (forced by `D`'s own structure — see `c185_s2_dirac.py`
  lines 138-143), while `q` here — like `χ` itself — is a single-component
  object descended from the Hopf/quaternion construction. Testing `q`
  against `C185`'s operator would first require exactly the frame
  transport `C185/decision.md` §4 already flags as pre-registered and
  still unresolved for `χ` itself (its two components carry opposite
  φ-phases; `C185`'s own eigenspinor ansatz needs a shared phase). Closing
  this for `q` without first closing it for `χ` would mean solving a
  harder, unaddressed instance of the same open problem — not a
  proportionate fix for a code-review finding. Left as a real, named gap;
  §4 of this file's "does NOT establish" list already scoped this
  correctly ("does not re-derive or connect to C185's spectrum").

All numbers re-verified after hardening: `run_output.txt` regenerated,
`9/9` unchanged, no check's pass/fail status changed — the hardening
strengthened HOW C3/D2 are checked, not WHAT they concluded.
