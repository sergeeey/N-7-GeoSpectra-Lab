# G106 Claim — Pre-registered third-point confirmation of G105 at N=7

**Question type:** descriptive (numeric confirmation of an already-derived closed-form formula
at a new input point; no new physical input, no claim about lambda's value)

**Background:** G105 (2026-07-06) derived analytically that kappa^2=(N+1)/N and the modulus
mass exponent (leading order 0.5 + computable O(lambda) correction) follow algebraically from
the potential's functional form, for ANY N. Skeptic review of G105 (FL Step 8a) explicitly
flagged that "physical genericity" — whether G104's actual (a,N)-generalized numerical
construction reduces to this exact potential shape for N outside the two already-tested
points, (2,6) and (3,6) — was NOT independently verified, since both prior points share N=6.

**This gate's point:** (a,N)=(2,7), lambda=1/3 (the project's standard reference value) — the
first N≠6 point ever run in this project.

**Pre-registration (AOG-1 — computed and stated BEFORE the (2,7) numerical run):**
- kappa^2 predicted = (N+1)/N = 8/7 = 1.142857 (from G105's `leading_order_minimum`)
- mass exponent predicted (local, at lambda=1/3) = 0.4922 (from G105's `predicted_local_exponent`,
  using A(n=14), B(n=14) freshly computed for n=14 — NOT reusing G105's own n=12 coefficients)

These two numbers were computed and written down in the session transcript BEFORE
`G104.run_for_lambda(2, 7, ...)` was ever called. `g106_third_point_n7.py` re-derives the same
predictions programmatically (via `predicted()`) so the pre-registration is reproducible by
re-running the file, not resting on a one-off transcript claim.

**Falsifiable predicate:**

| Check | Predicted | Kill if |
|---|---|---|
| Actual (2,7) minimum exists (V_min<0, V''>0) | yes | run_for_lambda returns exists=False |
| kappa^2 matches predicted 1.142857 | within 1e-2 (same bar G104 used for its own (a,N) checks) | diff > 1e-2 |
| Local mass exponent matches predicted 0.4922 | within 0.02 (same bar as G105's own D5 check) | diff > 0.02 |

**Actual result:** kappa^2 = 1.145416 (diff 0.0026), mass exponent = 0.4932 (diff 0.0010) —
both well inside tolerance. See decision.md.

**What this does NOT mean:**
1. Does NOT derive lambda's value — unchanged, as in every prior gate in this chain.
2. Does NOT prove genericity for ALL N — one additional point (N=7) narrows the untested gap
   from "everything beyond N=6" to "everything beyond N∈{6,7}"; it does not close it entirely.
   A skeptic could reasonably ask for a 4th point at a much larger or non-integer-adjacent N.
3. Does NOT re-open or re-litigate G104's own H1-vs-H2 question — lambda=1/3 was chosen here
   purely as the project's standard reference value, not to test either H1 or H2.
