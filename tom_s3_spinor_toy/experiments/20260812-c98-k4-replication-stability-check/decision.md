# C98 decision — k=4 confirms k=2/k=3: three independent points now support the k>=2 rule

**Verdict:** `K4_MATCHES_K2_K3__STABILITY_HYPOTHESIS_SUPPORTED_3_POINTS`
**Status:** RESOLVED — meaningful support gained, not a proof

---

## Summary

```
k=1 (C95):  L_i = +l_{e_i}(1)         R_i = -l_{e_i}(1)^T
k=2 (C96):  L_i = -l_{e_i}(2)^T       R_i = +l_{e_i}(2)
k=3 (C97):  L_i = -l_{e_i}(3)^T       R_i = +l_{e_i}(3)
k=4 (C98):  L_i = -l_{e_i}(4)^T       R_i = +l_{e_i}(4)
```

k=4 matches k=2 and k=3 exactly. Both brackets (`[L1,L2]=2L3`,
`[R1,R2]=2R3`) hold exactly (symbolic zero residual, 5x5 matrices).
Calibration (P0) passes cleanly, `R` matching `+l` uniformly across
all three quaternion units, the same candidate as k=2 and k=3.

**Three independent, consistent data points now support the tentative
"k=1 is a distinct base case, k>=2 follows one fixed rule" picture**
first proposed in C97's decision.md after the parity hypothesis was
falsified. This is meaningfully stronger than the 2-point support C97
itself explicitly flagged as "encouraging, not conclusive."

## Predictions vs outcome

| # | Prediction (claim.md) | Outcome |
|---|---|---|
| P0 (calibration) | R matches one of 4 candidates uniformly, bracket holds | **PASSES** — matches `+l` uniformly, `[R1,R2]=2R3` exact. |
| P1 (k>=2 stability) | `L_i(k=4)` matches `-l_{e_i}(4)^T` (k=2/k=3 pattern), not `+l_{e_i}(4)` (k=1's pattern) | **HOLDS** — matches `-l_{e_i}(4)^T` exactly, k=1's pattern does not appear. |
| P2 (bracket) | both brackets hold exactly at k=4 | **HOLDS** — verified symbolically, exact zero residual. |

## What this does and does not establish

**Established (empirically, to a reasonable standard for a working
rule):** for `k=2,3,4` — three separate, independently-constructed,
bracket-verified representations, using a construction that has now
been exercised four separate times (k=1 trivially via C95, then k=2,3,4
via the shared, twice-debugged `build_dk_matrix`/`coefficient_space_
generator_general` code) — the q-side and p-side generators follow:

```
L_i = -l_{e_i}(k)^T
R_i = +l_{e_i}(k)          for k = 2, 3, 4 (verified)
```

with `k=1` (C95) as a distinct base case using `L_i=+l_{e_i}(1)`,
`R_i=-l_{e_i}(1)^T` directly, structurally different because `D^{(1)}
(g):=g` is the trivial identity map (no monomial-substitution
construction, no possibility of the anti-homomorphism bug C96 found
and fixed).

**NOT established:** a formal proof that this holds for ALL `k>=2`.
Three consistent points is strong empirical support for a working
hypothesis, not an inductive or structural proof. If the
multiplication-operator build (task #59) needs a specific `k>5` value,
that specific `k` should still get its own cheap confirmation run
(the construction is fully general and reusable — changing `K` in the
now-three-times-reused script is a few minutes of work) before being
trusted without question, though the bar for skepticism at that point
is reasonably lower given the consistent 3-point track record.

## Practical consequence for task #59 (multiplication-operator build)

The working rule is now reasonably well-supported:

```
k=1:        L_i = +l_{e_i}(1),   R_i = -l_{e_i}(1)^T   (C95)
k=2,3,4:    L_i = -l_{e_i}(k)^T, R_i = +l_{e_i}(k)      (C96,C97,C98)
k>=5:       not independently checked -- treat the k>=2 rule as a
            reasonable working hypothesis, not a certainty, until
            checked at the specific level(s) actually needed
```

This is sufficient to unblock task #59 for any low Peter-Weyl level
(`k<=4`) without further replication rounds. A genuinely general-`k`
proof (rather than case-by-case verification) would require an
inductive/structural argument this round does not attempt.

## What this cannot show

- Does not prove the k>=2 rule for arbitrary k — 3 consistent points,
  not an inductive proof.
- Does not build the multiplication operator itself.
- Does not change `N_gen=3`'s CONDITIONAL status.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## Verification

- `ruff check experiments/20260812-c98-k4-replication-stability-check/`
  — clean, 0 errors.
- All candidate matches are exact symbolic equalities
  (`sp.simplify(...) == sp.zeros(5,5)`), not numerical near-matches.
- Construction reused verbatim from C96/C97 (only the `K` parameter
  changed, 3->4) — no new logic introduced that could hide a fresh bug.
