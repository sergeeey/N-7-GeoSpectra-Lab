# decision — OB11(ii) hard half, step 2: BLOCKED by a real/complex reality-type mismatch, not a bug

## Verdict

`HARNESS_SETUP_FAILED` (properly diagnosed, not patched around) → **C66 BLOCKED-SUBSTRATE, not
REFUTED.** C65's underlying mathematical fact (an isomorphism exists) is untouched.
**Date:** 2026-08-10 · L0: descriptive · `results_explicit_isomorphism.json` not produced
(script raised before completion — the diagnostic run below is what's persisted instead).

---

## What happened

round128's `extract_csa_and_roots` (reused unmodified) asserts the Cartan-subalgebra
coefficients, expressed in the *original* generator basis, come out real — true for round128's
own pair (`su3_v`/`su3_σ`, both real-antisymmetric-type constructions) but **not** for this
pair. Diagnosed directly rather than patched around:

| generator set | reality type |
|---|---|
| round59's `su(3)` (via `spin_lift` on complex Clifford matrices) | **complex, anti-Hermitian** (`A+A†=0` exactly; imaginary part up to 0.5) — standard physics `su(n)` convention |
| G102's `su(3)` (via `stabilizer_basis`, embedded in `so(8)`) | **real, antisymmetric** (`A+Aᵀ=0` exactly, zero imaginary part) |

Both represent the same abstract `su(3)` and the same module type (C65: Casimir exactly `-4/3`
for both), but in genuinely different **reality forms** — round59's is a complex representation;
G102's is a real representation whose complexification splits as `1⊕1⊕3⊕3̄`. round128's specific
algorithm assumes a shared reality type going in; it does not transfer as-is.

## Why this is not treated as a refutation

C65 already established, via general representation theory (matching module type + matching
Casimir), that an intertwiner between the two constructions exists. This round's failure is
about *this specific algorithm's applicability*, not about whether the underlying mathematical
object exists — exactly the Falsification Ladder's Substrate Gate distinction (a tool that can't
run the test yet is not evidence against the claim). Recorded honestly as `BLOCKED-SUBSTRATE`.

## What would actually be needed (not attempted here)

Either (a) realify round59's complex anti-Hermitian representation into a real form directly
comparable to G102's (a real representation theory construction, not just relabeling — the
complex-to-real correspondence needs to preserve the specific `1⊕1⊕3⊕3̄` splitting, not just
match dimensions), or (b) adapt the Cartan-Weyl matching algorithm itself to work correctly
across a real/complex reality-type boundary (dropping or reworking round128's real-coefficient
assumption specifically, understanding what it was protecting against before removing it). Either
is a genuine, non-trivial extension of round128's technique, not a quick fix.

## Kill Analysis

**Not killed:** C65's finding (module-type match) and the general-theory guarantee that an
isomorphism exists.

**What this narrows:** the specific plan of directly reusing round128's algorithm unmodified —
that plan required an assumption (shared reality type) this pair doesn't satisfy. The bridge
project (OB11(ii) hard half) needs one more genuine construction step than anticipated when C65
was scoped.

**Given the scope of what remains (OB11(iii) hard half, OB2/OB12/OB13, OB6, all still queued
per explicit user instruction), this specific sub-step is parked here rather than pursued
further this round** — a real/complex representation-theory bridge is itself a substantial,
well-defined task for a future round, not a quick continuation.

## What this does NOT show

1. Does **not** refute C65 or the existence of an isomorphism.
2. Does **not** mean the bridge project is dead — see "what would actually be needed" above for
   the concrete, identified next step.
3. Does **not** resolve OB11(ii).
4. Nothing about `N_gen=3`'s CONDITIONAL status changes.

## Check (reproduces the diagnostic, not a passing run)

```
cd experiments/20260810-ob11ii-round59-g102-explicit-isomorphism
python ob11ii_explicit_isomorphism.py
```
Expect: `AssertionError: CSA coefficients unexpectedly complex`, raised inside round128's
`extract_csa_and_roots` when called on round59's complex anti-Hermitian generators — confirms
the reality-type mismatch is reproducible, not a one-off.
