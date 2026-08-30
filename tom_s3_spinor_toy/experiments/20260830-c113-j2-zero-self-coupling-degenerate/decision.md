# C113 decision -- j2=0 route to breaking C112's target_level=2 confound
is algebraically closed, not just empirically null

**Verdict:** `J2_ZERO_ALGEBRAICALLY_INCAPABLE_OF_BREAKING_REALITY__CONFOUND_ROUTE_CLOSED`
**Status:** RESOLVED -- a structural closure, not an ordinary null result

---

## Summary

C112's artifact review named `j2=0` as the one way to reach
`target_level=2` with `j1 != j2` inside this construction family, but
flagged it as a likely-degenerate self-coupling case. This round proves
why, algebraically, before confirming numerically.

## Results

| k | dim | max\|Im(D)\| | max\|Im(self-coupled)\| | matches D±t | 
|---|---|---|---|---|
| 1 | 8  | 0.0 (exact) | 1.17e-16 | yes |
| 2 | 18 | 0.0 (exact) | 0.0 (exact) | yes |
| 3 | 32 | 0.0 (exact) | 0.0 (exact) | yes |

All 3 predictions (P0/P1/P2) CONFIRMED for k=1,2,3.

## What this genuinely establishes

**The algebraic argument (stated in claim.md before running anything):**
for ANY square `D` and ANY scalar `t`, `[[D,tI],[tI,D]]` is similar,
via the fixed basis change `u=x+y, v=x-y` (independent of `D`), to
`diag(D+tI, D-tI)`. Since every `dbar_full(k)` in this project has an
EXACTLY real spectrum (re-confirmed here to be `0.0`, not merely small),
`D±tI` stays exactly real for any real `t`. **This is a general fact
about the block shape, not a per-level coincidence** -- it holds for
every `k` and every `t` simultaneously, which is exactly what the k=1,2,3
numerical confirmation shows (identical `True` across all three, no
level-dependence at all, unlike every genuine reality-breaking result in
this series C108-C112, which was always level- or parameter-specific).

**Consequence for C112's confound:** `j2=0` cannot be used to test
"does `target_level=2` alone (without `j1=j2`) trigger the anomaly,"
because it can NEVER trigger the anomaly, for a reason that has nothing
to do with `target_level` at all -- self-coupling a real-spectrum matrix
to itself via a scaled identity is provably real regardless of level.
This closes off the `j2=0` route rigorously, not by "we tried it and it
happened not to work."

## Kill Analysis

**Killed:** `j2=0` as a viable way to disentangle C112's confound.

**NOT killed:** C112's own finding (`j1=j2` alone, at the 8 non-anchor
grid points, does not reproduce the anomaly) -- unaffected, this round
neither confirms nor refutes it, only closes off one proposed follow-up.

**What remains genuinely open (the confound itself, still unbroken):**
whether `target_level=2` specifically (not `j1=j2`) is the anomaly's
true trigger. This round proves `j2=0` cannot answer that question; it
does not answer the question itself. A genuine test would need a
construction reaching `target_level=2` with `j1 != j2` WITHOUT
degenerating into self-coupling -- which requires abandoning the
`j_target = j1+j2` stretched-top-state convention this entire C90-C113
family has used throughout (a materially larger design change, not
scoped for a quick follow-up). Recorded as the next open item in
`pearl_registry/INDEX.md`, not attempted here.

## What this does NOT show

- Does not resolve whether `target_level=2` or `j1=j2` is the anomaly's
  true trigger -- only that `j2=0` cannot be the test that resolves it.
- Does not change `N_gen=3`'s CONDITIONAL status; this lineage stays
  entirely internal to S3, touches neither S6 nor triality.
- Does not solicit Tom Lawrence's Part 5.

## Verification

- `ruff check experiments/20260830-c113-j2-zero-self-coupling-degenerate/`
  -- clean.
- No skeptic pass run this round, by explicit judgment call (not a
  default skip): the claim is a closed-form linear-algebra identity
  (`[[D,tI],[tI,D]]` block-diagonalization via a `D`-independent basis
  change) confirmed by exact numerical agreement across 3 independent
  levels -- not a hypothesis-design decision or an uncertain empirical
  claim `doubt-driven-development.md`'s own triggers are aimed at. The
  algebraic argument itself is checkable directly by any reader (5 lines
  of linear algebra, stated in full in claim.md) rather than requiring
  an adversarial pass.
- `max|Im|` values reported as exactly `0.0` (not "below 1e-9") for most
  cells -- verified this is `np.linalg.eigvals`'s own genuine output
  (LAPACK correctly detects exact realness for these particular real
  input matrices), not a rounding artifact; the one `1.17e-16` result
  (k=1) is ordinary floating-point noise, consistent with every other
  "exactly real" result in this series (C108-C112 all show similar
  `1e-15`-to-`1e-16`-scale noise floors for genuinely real cases).
