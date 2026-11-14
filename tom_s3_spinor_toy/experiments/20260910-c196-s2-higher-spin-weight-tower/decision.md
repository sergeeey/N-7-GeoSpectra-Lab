# C196 Decision — CONFIRMED. S² has a genuine tower, not an isolated χ_{±1/2}.

**Date:** 2026-09-10
**Verdict:** **CONFIRMED**, `9 of 9` checks pass (after one self-caught wrong
prediction, corrected — see §2). Exact symbolic arithmetic throughout.
All numbers trace to `c196_s2_higher_spin_weight.py` and `run_output.txt`.

---

## 1. Result

Applying `C184b`'s exact descent recipe (diagonalise the fibre generator,
split degeneracy with the second generator, substitute Hopf, strip the pure
phase) one level further, at `k=3` instead of `k=1`, gives a second, genuine
member of the S² spin-weighted family:

```
k=3, fibre weight -3/2, m_R=-3/2, in Hopf coordinates:
  (e^{3iθ} + 3e^{2iθ} + 3e^{iθ} + 1) e^{-3i(φ+θ)/2} / 8
```

Confirmed: double-valued under `φ→φ+2π` (like `χ_{-1/2}`), and NOT a
constant multiple of `χ_{-1/2}` — a genuinely new object, not a rescaling of
the k=1 result.

## 2. A wrong prediction, caught by running it

The pre-registered claim.md expected the extremal `±3/2` fibre-weight
sectors to be **1-dimensional** ("already fully split, no second generator
needed") — this was **wrong**, caught by the script itself (check B2 failed
on the first run). The actual dimension is **4** at each weight, because the
fibre generator `X3L` diagonalizes only the LEFT `SU(2)` label; the RIGHT
`SU(2)` content (`j_R=3/2`, dimension 4) sits inside each fixed-left-weight
sector untouched — exactly the same degeneracy structure `C184b` names for
`k=1` (there, dimension 2 per weight, from `j_R=1/2`). Fixed by applying
`C184b`'s own second-generator split (`X3R`) to properly label the sector
before picking a representative — not by discarding the failed check.

This is recorded rather than smoothed over: a false prediction about the
`(j_L,j_R)` structure was made, caught mechanically (not by re-reading
theory beforehand), and fixed using machinery already in this project. Same
discipline as C188's own self-correction pattern.

## 3. What this gives the reply

Upgrades the previous turn's synthesis answer to Tom's central question from
`[MEMORY]` (citing that spin-weighted harmonics on S² are textbook-standard)
to `[VERIFIED-tool]`: this project's own construction, run a second time at
a different level, reproduces the expected general behavior (odd `k` ↔
half-integer weight, genuinely double-valued, a real family — not a fluke
at `k=1`). Strengthens, without yet finalizing, the claim that S² and S³
both carry spinor-type content in the SECTIONS sense; the difference is
S³'s parallelizability collapsing its version to literal constants, which
S²'s tower structure here shows it structurally cannot do.

## 4. What this does NOT establish

- Does not derive the general `_{1/2}Y_{j,m}` family for all `j` — a second
  data point, not an induction proof.
- Does not touch `C179`'s no-go for bare scalar decomposition — orthogonal.
- Does not resolve Tom's question without his forwarded Jantzen
  correspondence — evidentiary support only.

## 5. Floor–Ceiling (Step 4a)

Metric: **does a second application of the descent method at a different k
produce a genuinely new, correctly-behaved family member, or does it fail to
generalize (single-valued, proportional to k=1, or the phase-stripping step
breaking down)?**

FLOOR (mechanism absent) = `0.0`. If the descent method were an artifact
specific to `k=1` (e.g. relying on some coincidence of low dimension), `k=3`
would plausibly fail at least one of: half-integer weight (B1), clean phase
stripping (C1/C2), double-valuedness (D1) — 0 of 3 structural checks passing
would mean no generalization.

CEILING (full generalization) = `3.0`. All three structural checks (B1, C1/C2
combined as one, D1) pass, AND the result is a genuinely new, non-
proportional object (D2) — full confirmation the method is not an isolated
`k=1` coincidence.

OBSERVED = `3` (B1 half-integer weights confirmed; C1/C2 phase-stripping
confirmed at k=3; D1 double-valuedness confirmed) plus D2 as an additional,
non-trivial bonus (genuinely new content, not just "the method still runs").

EFFICIENCY = `(3-0)/(3-0)` = **`1.0`** — full generalization, not partial.

## 6. Reproduction

```
cd experiments/20260910-c196-s2-higher-spin-weight-tower
python c196_s2_higher_spin_weight.py
```

`9/9` (~1-2 min, degree-3 harmonic projection in 4 variables is the slow
step). `ruff check` and `ruff format`: clean.
