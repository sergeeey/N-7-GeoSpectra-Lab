# C187 Decision — PARTIAL. The mechanism works; the eigenvalue match is unresolved, not forced.

**Date:** 2026-09-09
**Verdict:** **PARTIAL** (neither PROMOTE nor REJECT — this project's Falsification
Ladder anticipates exactly this outcome for a claim with two independently
checkable halves). Claim (a) **CONFIRMED**, 10/10. Claim (b) **OPEN**, not
falsified, not verified.

All numbers trace to `c187_s3_euler_reduction.py` and `run_output.txt`.

---

## 1. What this round was

`C186`'s decision.md §4 corrected the half-angle pearl's own falsification
test — it had named a task (`k≥2` exact `S³` eigenspinors) that exercises a
different method entirely and cannot test the pearl. The corrected test:
build the `S³` Dirac operator in **Euler angles**, where it genuinely is an
ODE, apply the half-angle substitution, and check (a) it stays fast/polynomial
and (b) it reproduces the already-known spectrum.

## 2. Claim (a) — CONFIRMED

Metric, frame, and spin connection were all **derived**, not quoted:

- the metric came from pulling back the flat `ℝ⁴` metric through the *same*
  `x0..x3` embedding this project uses everywhere else — not a textbook
  formula, `P1`–`P2`;
- the spin connection came from solving Cartan's structure equation exactly,
  `P4`–`P5`, mirroring `C185`'s discipline.

Applying `D` to a plane-wave ansatz `(F,G)e^{i(mφ+nψ)}` took **0.1 seconds**
(`P6`) — against `C185`'s abandoned first attempt on the analogous `S²`
problem, which ran **25 minutes** before being killed. Both components kept
the *same* `(m,n)` with no mismatch (`P7`) — the exact defect class that
`C185` hit once and this round checked for explicitly. Clearing denominators
and substituting `s=sin(θ/2)`, `c=cos(θ/2)` needed no `simplify()` call on a
transcendental expression anywhere (`P8`); the bare `m`-term needed the same
`hom=(s²+c²)` multiplier trick `C185` used for its own bare-`m` term (`P9`),
confirming the reduction generalises structurally, not by coincidence. A
blind scan of `176` `(m,n,N,λ)` combinations — a considerably broader sweep
than a single case — completed in `5.2` seconds (`P10`).

**This is the pearl's own registered claim, and it holds without
qualification.**

## 3. Claim (b) — genuinely open, and why it was not forced

The blind scan (four natural `(m,n)=(±1/2,±1/2)` guesses, degrees `N=0..3`,
every integer `λ∈[-5,5]`) found **zero** nonzero-kernel hits. Not a near miss
on one case — a clean null across all `176` combinations tried.

**What this is not:** it is not evidence against `C184`/`C186`'s spectrum,
which was independently verified there by a completely different method
(finite matrices over `ℚ(i)`, no angles). It is not evidence against claim
(a), which is about speed/polynomial-ness and was directly measured. Both
stand untouched.

**What it likely is:** a mismatch between the naive `(m,n)` plane-wave labels
used here and the actual periodicity of spin-weighted functions on `S³`'s
double cover. The half-integer values `-3/2` and `1/2` that appeared in an
early, later-discarded diagnostic (a buggy square-submatrix determinant check,
not a valid computation — flagged and replaced with the correct full-rank
`kernel_dim`, same technique `C185` used) are *suggestive* of a half-integer
shift somewhere between `(m,n)` and the true weight, but that is a hypothesis,
not a finding — it is not asserted as fact here.

**Why this was not chased further this round.** Getting the exact periodicity
right is its own derivation — comparable in care to the work `C186` did to
determine which relative sign of `J₃ᴿ` actually commutes with `D₀`, not
something to guess at by widening a blind numeric scan. This project's own
recorded practice (`patterns.md` and this session's own memory:
"3 consecutive skeptic-caught bugs = stop patching, park or redesign";
"needs spectral-flow machinery" turned out to be a 15-line fix once actually
tried, the opposite failure mode) argues against both premature declarations
of "blocked" *and* against unaudited persistence chasing a fit. Reporting an
honest partial result is the disciplined middle path this round takes.

## 3b. Floor–Ceiling for claim (a)'s speed metric (Step 4a)

The metric with room to move is **wall-clock time to reduce the eigenvalue
problem**, not a pass/fail threshold, so floor and ceiling are stated as
reference points rather than a formula:

| | construction | time |
|---|---|---|
| **floor** (mechanism removed — attack the problem in raw `θ` coordinates, no half-angle substitution, letting `simplify()` chew on `sin`/`cos`/`exp` mixed together) | this is exactly `C185`'s abandoned first attempt on the analogous `S²` problem | **~1500s, killed before completion** |
| **observed** | half-angle substitution, pure polynomial algebra | **0.1s** (single case, `P6`), **5.2s** (176-case blind scan, `P10`) |
| **ceiling** | the substitution step itself is pure algebraic rewriting with no search — there is no faster correct method than doing the rewrite once | effectively **instant**; observed is already within a small constant factor of it |

`efficiency` in the Step 4a sense is not a single number here because the
*floor* comparison is against a different problem instance (`S²`, not `S³`)
run by a different script — the two are not directly divisible. The
qualitative reading is unambiguous regardless: four orders of magnitude
between "mechanism absent" and "mechanism present," which is the entire
content of the pearl's speed claim.

Claim (b) does not get a Floor–Ceiling interval: it is not a threshold on a
continuous metric, it is a yes/no question (does *some* `(m,n)` reproduce the
known spectrum) that came back a clean null on every case tried, not a value
sitting somewhere on a scale between a floor and a ceiling.

## 4. Kill criterion for claim (b) — unresolved, carried forward

Claim (b) is rejected only once the correct `(m,n)`-periodicity is derived
**and** still fails to reproduce `-k` mult `(k+1)(k+2)`, `+(k+2)` mult
`k(k+1)`. Until then it is open, not falsified — recorded explicitly so a
future round does not have to rediscover that this is unresolved rather than
disproven.

## 5. What this does NOT establish

- **Does not touch any physics claim.** `C184`/`C186`'s spectrum stands,
  verified by a different method there.
- **Does not settle the periodicity hypothesis** in §3 — it is named as a
  plausible direction, not derived or verified.
- **The half-angle pearl's core mechanism claim is confirmed on a second,
  genuinely independent geometry** (`S³` in Euler angles, not `S²`) — this is
  real transfer, not a restatement of `C185`.

## 6. Consequence for the pearl registry

The corrected test (filed in `C186`'s pass over the registry) is now **partly
run**: its speed/polynomial half is answered (yes); its eigenvalue-match half
is not yet answerable and is recorded as such, not silently dropped. The
pearl's own `next_check` (`2026-10-15`) is unaffected — this round ran early,
ahead of schedule, and found a real complication worth recording now rather
than waiting.

## 7. Reproduction

```
cd experiments/20260909-c187-s3-euler-angle-reduction
python c187_s3_euler_reduction.py
```

`10/10` (claim (a) checks). `ruff check` and `ruff format`: clean.
