# OB11(ii), hard half — first step: does round59's real Σ carry the same abstract SU(3)-module as the triality channels?

**Experiment id:** `20260810-ob11ii-round59-su3-bridge`
**Date:** 2026-08-10 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C61 (necessary condition, corrected same-day above), C29 (OB11 condition i,
Casimir technique), round59 (`20260714-round59-trivial-rank-certification`, the real
curvature-twisted Clifford/Dirac construction)

---

## Continuing in order (per user instruction, all remaining items)

The user asked to continue through everything, including OB11(ii)'s hard half: building the
real G2-invariant differential Dirac operator with channel-mixing terms, not just the bare
representation-theoretic necessary condition C61 already closed.

## Why this is scoped as a first step, not a full resolution

Building the actual mixing-term operator requires a genuine Clifford-algebra-compatible
construction (Hermitian, satisfying an anticommutation-type relation), not just membership in
an abstract Hom space (see the correction added to C61's own decision.md today). The one place
in this project with a REAL, curvature-twisted, already-verified Clifford/Dirac construction on
S⁶ is round59 (`Σ = Λ•L'`, Nomizu-connection Clifford multiplication, dim ker = 1, PROVED) — but
it was built independently, in its own basis (`ADNU` su(3) generators, distinct from G102's own
`stabilizer_basis` construction used throughout C61-C64), with no established bridge between the
two. round59 predates the triality-channel apparatus in spirit but postdates G102 in the repo
timeline (2026-07-14 vs 2026-07-05) without ever being cross-referenced to it.

**Before attempting the full mixing-term construction** (which needs round59's actual
Clifford matrices identified as *one* of the triality channels), the cheapest, well-defined
first check is whether round59's `Σ`, as an abstract `su(3)`-representation under its own
`ADNU` generators, carries the **same module type** (`1⊕1⊕3⊕3̄`) that C29 already established
for all three triality channels — using the exact same Casimir technique, self-contained,
no cross-construction basis alignment attempted yet.

## The claim under test

> **C65 (working).** round59's `Σ` (8-dim, `Λ•L'` Clifford module), under its own `ADNU`
> `su(3)` isotropy generators (Remark 5.2, Agricola-Hofmann-Lawn 2023, already used
> unmodified by round59 itself), has quadratic Casimir spectrum matching `1⊕1⊕3⊕3̄`
> (2 zero eigenvalues + 6 equal nonzero eigenvalues) — the same pattern C29 found for all
> three of G102's triality channels via an independent construction.

**Falsifier, fixed in advance:** any other eigenvalue pattern (e.g. not 2+6, or the 6 nonzero
values not equal) refutes the claim and would mean round59's `Σ` is a structurally different
`su(3)`-module from the triality channels — closing off the planned bridge entirely, a genuine
and informative kill.

## Predictions, recorded before running

| # | Prediction |
|---|---|
| **P1** | round59's `ADNU` generators (8 of them, given as explicit bivector combinations acting on the 6 tangent directions, lifted to `Σ` via `spin_lift`) reproduce, unmodified, a valid `su(3)` Lie algebra (closure under commutator, 8-dimensional) — sanity check before trusting the Casimir computation |
| **P2 (the claim)** | quadratic Casimir `C₂=Σ_a T_a²` gives exactly 2 zero eigenvalues and 6 equal nonzero eigenvalues, matching C29's own found pattern for G102's channels (same qualitative signature, not necessarily the identical numeric value, since normalization conventions differ between round59's and G102's constructions) |

## What this cannot show

- Does **not** build the mixing-term operator itself — this is explicitly the first of several
  steps toward that (module-type match → basis alignment → Clifford-relation test), not the
  destination.
- Does **not** establish an explicit isomorphism between round59's `su(3)` presentation and
  G102's — only that they are the *same abstract module type*, a necessary precondition for
  such an isomorphism to exist, checked before investing in finding it explicitly.
- Does **not** resolve OB11(ii) — the harder question (Hermiticity/Clifford-compatibility of a
  cross-channel term) remains untouched regardless of this round's outcome.
- Nothing about `N_gen=3`'s CONDITIONAL status changes.

## kill_criterion

Survives if P1 and P2 both pass. If P2 fails (wrong Casimir pattern), the planned bridge to
round59's real construction is dead — a different route to OB11(ii)'s hard half would be
needed, and this should be recorded as a genuine null, not silently abandoned.
