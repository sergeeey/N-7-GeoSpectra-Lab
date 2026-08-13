# C97 decision — k=3 matches k=2, NOT k=1: parity hypothesis falsified, cleaner "k=1-is-special" picture emerges

**Verdict:** `K3_MATCHES_K2_PARITY__PARITY_HYPOTHESIS_FALSIFIED`
**Status:** RESOLVED — informative, narrows the picture usefully

---

## Summary

```
k=1 (C95):  L_i = +l_{e_i}(1)         R_i = -l_{e_i}(1)^T
k=2 (C96):  L_i = -l_{e_i}(2)^T       R_i = +l_{e_i}(2)
k=3 (C97):  L_i = -l_{e_i}(3)^T       R_i = +l_{e_i}(3)
```

k=3 matches k=2's pattern exactly, not k=1's. The parity/alternating
hypothesis pre-registered in this round's own `claim.md` (P1: does
k=3 match k=1's odd-k pattern?) is **falsified by direct
counterexample** — a clean, single-test falsification, not an
ambiguous or partial result. Both brackets (`[L1,L2]=2L3`,
`[R1,R2]=2R3`) hold exactly at k=3, and the calibration (P0: does R
match one of the four candidates uniformly?) passes cleanly, matching
`+l` — same candidate as k=2, again not the literal guess carried over
naively from k=1.

## What this replaces the parity hypothesis with

Three data points now available (k=1, k=2, k=3), with k=2 and k=3
agreeing and k=1 alone differing. The natural reading: **k=1 is a
genuinely special/degenerate case** (the self-conjugate defining
representation, where `D^{(1)}(g):=g` is used directly with no
monomial-substitution construction at all — structurally different
from every `k>=2` case, which all go through the raw-monomial +
`g^{-1}`-correction construction). For `k>=2`, the tentative emerging
rule (two consistent data points, not yet a proof) is:

```
L_i = -l_{e_i}(k)^T
R_i = +l_{e_i}(k)          (for k>=2, verified at k=2,3)
```

**This is explicitly NOT proven** — two consistent points after one
falsified hypothesis is encouraging, not conclusive. A genuine
confirmation would need at least one more independent check (k=4)
before this pattern is trusted as a general `k>=2` rule for the
multiplication-operator build. This round does not run k=4 — kept as
a separate, properly pre-registered round (see Kill Analysis below)
rather than folded in post-hoc, to avoid fitting a new hypothesis to
data already in hand without a fresh, falsifiable prediction.

## Predictions vs outcome

| # | Prediction (claim.md) | Outcome |
|---|---|---|
| P0 (calibration) | R matches one of the 4 candidates uniformly, bracket holds | **PASSES** — matches `+l` uniformly, `[R1,R2]=2R3` exact. |
| P1 (parity hypothesis) | `L_i(k=3)` matches `+l_{e_i}(3)` (k=1's pattern) | **FAILS** — matches `-l_{e_i}(3)^T` instead (k=2's pattern). |
| P2 (bracket) | both brackets hold exactly at k=3 | **HOLDS** — verified symbolically, exact zero residual. |

## Kill Analysis (per Anti-Overfitting Gate discipline)

**What was killed:** the specific "parity/2-cycle alternation" hypothesis
for how the L/R role assignment varies with `k`. A single counterexample
(k=3 matching k=2, not k=1) is sufficient to kill a strict alternation
claim — no ambiguity in this verdict.

**What was NOT killed:** (a) the underlying construction itself — both
brackets hold exactly, calibration passes cleanly, this is a real
bracket-consistent result, not a broken test; (b) the possibility that
`k=1` is simply a structurally distinct base case and `k>=2` follows a
single fixed rule — this is *consistent* with the k=2,k=3 data, not yet
independently tested by a fresh prediction.

**Relaxation map (one assumption changed, per Minimal Relaxation Rule):**
the killed hypothesis assumed "the pattern alternates with period 2 in
k." The next candidate hypothesis — "k=1 is a distinct base case; k>=2
follows one fixed rule" — changes exactly that one assumption (period-2
alternation → k=1-anomaly-then-stable), not multiple assumptions at
once. Testing it requires a genuinely new pre-registered prediction at
k=4 (does k=4 ALSO match k=2/k=3's pattern?), not a re-labeling of the
k=2/k=3 data already collected.

## Practical consequence for task #59 (multiplication-operator build)

- Do **not** use a single fixed formula across all Peter-Weyl levels.
- For `k=1` specifically: `L_i=+l_{e_i}(1)`, `R_i=-l_{e_i}(1)^T`
  (C95, fully certified).
- For `k=2,3` (verified): `L_i=-l_{e_i}(k)^T`, `R_i=+l_{e_i}(k)`.
- For `k>=4`: **not yet verified** — treat as unconfirmed until an
  independent k=4 (or higher) check is run. Do not silently assume the
  k=2/k=3 pattern extends without that check, per this project's own
  Anti-Overfitting Gate discipline (AOG-1: pre-registration required
  before promoting a relaxed hypothesis).

## What this cannot show

- Does not prove the "k=1 special, k>=2 stable" hypothesis — 2
  consistent points, not a proof; k=4 is the next-cheapest
  discriminating test, deliberately not run in this same round.
- Does not build the multiplication operator itself.
- Does not change `N_gen=3`'s CONDITIONAL status.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## Verification

- `ruff check experiments/20260812-c97-k3-replication-parity-check/` —
  clean, 0 errors.
- All candidate matches are exact symbolic equalities
  (`sp.simplify(...) == sp.zeros(4,4)`), not numerical near-matches.
- Construction reused verbatim from C96 (already debugged and verified
  there: `build_dk_matrix`'s homomorphism property and the abstract-
  symbol `D_sym` extraction fix), generalized only in the dimension
  parameter `k` — no new logic introduced that could hide a fresh bug.
