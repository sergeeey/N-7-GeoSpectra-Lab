# G106 Decision — Third-point (N=7) confirmation of G105

**Verdict: PROMOTE (3/3 checks)** — the (a,N)=(2,7) point, never touched by any prior gate,
confirms both of G105's closed-form predictions to well within tolerance: kappa^2 within
0.22%, the local mass exponent within 0.1%. This directly closes the "physical genericity"
gap the G105 skeptic review flagged (G104/G105's own two tested points, (2,6) and (3,6),
both share N=6 — this is the first N≠6 point run in this project).

## Pre-registration order [VERIFIED — literal transcript order, this session]

1. Predictions computed FIRST, from G105's own closed-form functions alone (`leading_order_minimum(14)`,
   `exponent_coefficients(14)`, `predicted_local_exponent(14, 1/3)`) — no reference to G104's
   numerical machinery at this step:
   - kappa^2 predicted = 1.142857 (= 8/7 exactly)
   - mass exponent predicted = 0.4922
2. ONLY THEN was `G104.run_for_lambda(2, 7, 1/3)` called, producing the actual numbers.
3. `g106_third_point_n7.py` encodes both steps as separate functions (`predicted()` and
   `actual()`) so the same order is reproducible by re-running the file — the pre-registration
   is not resting on a one-off transcript claim.

## G106 results [VERIFIED-python — results_g106.json, `python g106_third_point_n7.py`]

| Check | Predicted | Actual | Diff | Threshold | Status |
|---|---|---|---|---|---|
| Minimum exists | yes | yes (V_min=-2.94e-6, rho_min=1.1666) | — | must exist | ✅ |
| kappa^2 | 1.142857 | 1.145416 | 0.002559 (0.22%) | < 1e-2 | ✅ |
| mass exponent (local) | 0.4922 | 0.4932 | 0.0010 | < 0.02 | ✅ |

Both diffs are SMALLER than the corresponding worst-case diffs G105 itself found across its
own tested range (kappa: G104's own C1 control was 0.29% off at (3,6); mass exponent: G105's
D5 check found 0.0005 diff at the far edge of G103's range, same order as here at a totally
different N). Nothing degrades at the new point — if anything, N=7 tracks the closed-form
prediction slightly better than N=6 did in places.

## Why this test is stronger than a blind "does it match" fishing expedition

Per the Anti-Overfitting Gate (AOG-1, pre-registration) and this project's own Cheapest
Differentiating Test Protocol: a test only counts as a genuine confirmation if the prediction
existed BEFORE the data. Unlike G104's original post-hoc power-law cross-check (which noticed
a match AFTER already having both numbers), this gate computed the prediction from a function
that has never seen (a,N)=(2,7)'s actual output, then ran the actual computation second. A
skeptic re-reading this decision.md cannot dismiss the match as "the formula was tuned to
hit this number" — the formula (G105's A,B coefficients) was fixed before this gate existed.

## Caveats

- One additional point narrows, but does not close, the "genericity across N" question — it
  moves the untested boundary from "everything beyond N=6" to "everything beyond N∈{6,7}".
  A skeptic could still reasonably ask for a much larger N, or a non-adjacent N, as a sharper
  test of whether some hidden N-dependence only appears far from the tested cluster.
- Does not touch lambda's value or G104's own H1-vs-H2 question — lambda=1/3 was used purely
  as this project's standard reference point.
- Reuses G104's `run_for_lambda` and G105's closed-form functions verbatim (both already
  reviewed and tested in their own gates) — this gate's own new-code surface is small (the
  `predicted()`/`actual()` wrapper and the comparison), correspondingly lower audit risk than
  G105's original derivation.

## Relation to prior results

- G105 (2026-07-06, PROMOTE): source of the closed-form formulas tested here.
- G104 (2026-07-05, NULL on H1-vs-H2): source of the (a,N)-generalized `run_for_lambda`
  machinery reused here, unmodified.
- Skeptic review of G105 (FL Step 8a): source of the specific gap ("physical genericity...
  NOT verified... only checked at (2,6) and (3,6)") this gate was designed to close.

## Pearl Gate

→ pearl_registry/INDEX.md G105 row's next_check condition ("test a third (a,N) pair with
the exponent pre-registered before running") is now satisfied — marked CONFIRMED, not just
pending. No new pearl candidate surfaced beyond the confirmation itself.
