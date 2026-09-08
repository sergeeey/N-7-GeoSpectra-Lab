---
# C183 — closing the Round59 and Round65 pearls: why the two-line argument
# holds on three Butruille spaces and fails on the fourth

**Date:** 2026-09-08
**FL tier:** [x] Full
**Question type:** [x] descriptive  (no intervention, no counterfactual — this
is a statement about the representation theory of four fixed cosets)

---

## Prior Result Gate (MANDATORY — filled BEFORE computing anything)

The user's request was "close Round59 and Round65 with one round on S^3xS^3."
This gate is why that round is NOT run here.

1. **Exact claim under test (as the two pearls state it):** on any nearly-
   Kahler coset admitting Killing spinors with nonzero Killing constant, the
   trivial-block rank is forced to 1 by the same two-line argument used on
   `S^6=G_2/SU(3)` (Term1 = Killing eigenvalue `!= 0`; Term2 = 0 because
   `Lambda^2(m^{1,0}) (x) Lambda^2(m^{1,0})` carries no isotropy-trivial
   component). Round65 recorded this as "2 of 4 confirmed, a genuine positive
   signal for the Universality open problem."

2. `null_results/INDEX.md` grep (`s3xs3`, `S^3 x S^3`, `butruille`): 0 hits.

3. `parked/INDEX.md` grep: 0 hits.

4. `pearl_registry/INDEX.md` grep: hits at rows for Round59 (2026-07-14),
   Round65 (2026-07-15), C140 (2026-09-04), C151, C152, C175.

5. **`experiments/` grep — THE FINDING OF THIS GATE.** The requested S^3xS^3
   round already exists, twice, and neither pearl was ever updated:

   - **Round70** (`20260717-round70-e5-universality-cp3-s3xs3/`, 2026-07-17)
     ran the crux check on BOTH remaining spaces. Its own summary table:

     | Space | Route-C (no trivial component in `L2 (x) L2`)? |
     |---|---|
     | `S^6` | PASS |
     | `SU(3)/T^2` | PASS |
     | `CP^3` | **PASS** (a third space, never reflected in either pearl) |
     | `S^3xS^3` | **FAIL — an isotropy-trivial slot IS available** |

     Verdict for `S^3xS^3`: `OPEN_STRUCTURALLY_DISTINCT` /
     `INCONCLUSIVE-BY-ROUTE-C`.

   - **Round71** (`20260717-round71-e6-s3xs3-nomizu-torsion-audit/`, same day)
     then attempted the explicit `Term2` value for `S^3xS^3` and returned
     **ILL-POSED**: CH2016's own page-18 data for this coset is not internally
     Hermitian-consistent (`B(X,X)=5/3 != B(Y,Y)=2`, and `B(X,Y)=2sqrt(3)/3
     != 0`), and two independent repair attempts disagree with each other.

6. `git log -S` pickaxe on `contains_trivial`: confirms Round70's script is
   the only place the four-space comparison is computed.

7. **Status:** [x] ALREADY ANSWERED — re-running the S^3xS^3 crux would be a
   blind retry of committed work, which the Adaptive Iteration Branch Rule
   forbids without a NEW reviving condition. Round71's obstruction is a
   substrate problem in the primary source, not something a fresh session
   fixes by trying harder; no new source has appeared since.

**Therefore this round does not recompute S^3xS^3. It does the thing that
was actually left undone: propagate Round70/71 into the two pearls, and ask
the question Round70's own table raises but does not answer — WHY does
exactly one of the four fail?**

---

## Counterfactual Frame

In what world is the pearls' prediction true? One where the Term2-vanishing
step follows from "nearly-Kahler + Killing spinor" alone. Round70 already
shows that world is not ours: all four spaces are nearly-Kahler with Killing
spinors, and the step fails on one of them. So the prediction is false as
stated, and the live question is what the step actually depends on.

How many independent changes would be needed to save it as stated? One: a
demonstration that the trivial slot available on `S^3xS^3` carries
coefficient zero anyway. That is exactly what Round71 tried and could not
certify.

---

## Mechanism Claim Gate (Step 0a) — the sentence this round's design rests on

**The sentence:** `(V (x) W)^H = 0` iff `W` contains no constituent isomorphic
to the dual of a constituent of `V`; hence `(Lambda^2 (x) Lambda^2)^H = 0` iff
`Lambda^2(m^{1,0})` shares no constituent with its own dual.

**Status: DERIVED, not asserted** — `dim (V (x) W)^H = dim Hom_H(V^*, W)`,
and Schur makes that the number of shared irreducible constituents between
`V^*` and `W`. This is textbook, and is checked below against three
independently-computed cases rather than taken on faith.

**Terminology collision, flagged explicitly (per this project's own symbol-
registry discipline):** "self-dual" ALREADY means Hodge self-dual 2-forms
throughout this repo (C79/C80/C82/C89, the `so(4)` splitting). It is NOT used
in that sense here. Where this round needs `V ~= V^*` as an `H`-representation,
it writes **"isomorphic to its own dual"** in full, never "self-dual".

---

## Estimand

**Population:** the four homogeneous nearly-Kahler 6-manifolds (Butruille's
classification): `S^6=G_2/SU(3)`, `SU(3)/T^2`, `CP^3=Sp(2)/(Sp(1)xU(1))`,
`S^3xS^3=SU(2)^3/SU(2)_diag`.

**Intervention:** apply ONE uniformly-stated criterion — "does
`Lambda^2(m^{1,0})` share a constituent with its own dual?" — to the four
isotropy decompositions already committed in Round70's script, with no
per-space branching in the decision logic.

**Comparator:** Round70's own already-computed four verdicts (PASS, PASS,
PASS, FAIL), treated as ground truth this round must reproduce.

**Endpoint:** agreement of the criterion's four verdicts with Round70's four.

**Summary measure:** number of the four spaces on which criterion and Round70
agree, out of 4.

**MCID:** not applicable — the endpoint is exact agreement, not a magnitude.

---

## Claim

**Falsifiable statement:** the Term2-vanishing step of Round59/65 holds on a
homogeneous nearly-Kahler 6-manifold exactly when `Lambda^2(m^{1,0})` shares
no irreducible constituent with its own dual as a representation of the
isotropy group `H`; and among the four Butruille spaces this fails for
`S^3xS^3` and only `S^3xS^3`, because its isotropy `SU(2)_diag` is the only
one of the four whose every complex representation is isomorphic to its own
dual.

**Narrowed after adversarial review (2026-09-08) — what is proved and by
what.** The sentence above is a statement about `H`-representations, and it is
true as stated (it is Schur). What the script computes is a **maximal-torus
proxy**: whether `Lambda^2`'s weight multiset contains a pair summing to zero.
The two are not the same condition, and the review supplied the separating
example: for `H = SU(3)` and `Lambda^2 = 3 (+) 6` the torus check finds
zero-sum pairs while the `H`-level singlet count is `0`. So

- `T`-count `= 0` **proves** the `H`-trivial component is absent (a real PASS);
- `T`-count `> 0` on its own proves nothing about `H` (not a FAIL).

The three PASSes therefore stand on the proxy alone. The one FAIL does not,
and is completed at `H`-level in the script — `mult(V0) = m(0) - m(2) = 1` for
`S^3xS^3` — rather than imported from Round70's Clebsch-Gordan as the first
draft did. The revised negative controls, and the enumeration replacing a
tautological assertion about `J`-independence, come from the same review.

---

## Floor and ceiling (Step 4a) — resolved BEFORE running

| | construction | value |
|---|---|---|
| **FLOOR** | a criterion with the mechanism removed: return PASS unconditionally | **3 of 4** — because 3 of the 4 spaces really do pass |
| **CEILING** | a lookup table keyed on the space's name | 4 of 4 |

`efficiency = (observed - 3) / (4 - 3)`. So **"agrees with 3 of 4" is the
floor, not a result** — it is exactly what a criterion containing no
mechanism scores, and the success threshold must therefore be 4 of 4.

The ceiling being reachable by a lookup table means the count alone cannot
separate a real criterion from a memorised one. Second, non-numeric
requirement, pre-registered here: the decision logic must be a single
function of the isotropy data with **no per-space branch**, and must flip its
verdict under an injected error (below). A criterion that scores 4 of 4 while
branching on the space's name is recorded as `CRITERION_INVALID`, not PASS.

---

## Kill criterion (MANDATORY — filled BEFORE running)

| Outcome | Verdict |
|---|---|
| 4 of 4 agreement, no per-space branch, injected-error control flips | **PROMOTE** — the criterion is the mechanism; the two pearls close as REFUTED-AS-STATED with a named structural reason |
| 4 of 4 but only with a per-space branch, or the injected-error control does not flip | `CRITERION_INVALID` — a lookup table, not a mechanism; report as such, pearls stay pending |
| 3 of 4 | **FLOOR** — indistinguishable from the no-mechanism null; the criterion is wrong or vacuous |
| <= 2 of 4 | the criterion is falsified outright; Round70's four cases have some other explanation |
| the four isotropy decompositions cannot be read off Round70's committed script without re-deriving them | `BLOCKED-SUBSTRATE` — stop; do NOT re-derive the coset data, that is Round70's work and re-doing it silently would destroy the independence of the comparison |

---

## Negative control (the injected-error catch)

Corrupt one input and require the verdict to flip:
- `S^6`: replace `Lambda^2(m^{1,0}) = 3bar` with `3bar (+) 3` (a
  deliberately dual-closed input). The criterion MUST turn `S^6` from PASS to
  FAIL. If it does not, it is not reading its input.
- `S^3xS^3`: replace `Lambda^2 = V2` with a `U(1)`-charged piece carrying no
  opposite charge. The criterion MUST turn `S^3xS^3` from FAIL to PASS.

Both corruptions are of the INPUT, never of the decision logic.

---

## What this result does NOT mean

- Does **NOT** establish `Term2 != 0` on `S^3xS^3`. Round70 already said the
  shortcut fails to force vanishing; it did not force non-vanishing either,
  and Round71 could not certify a substrate to decide it. That question stays
  open, and this round does not touch it.
- Does **NOT** establish that `rank = 1` fails on `S^3xS^3`. The isotropy-Schur
  bound `dim ker <= 1` holds on all four spaces independently of Route C
  (Round70 Step 4, robust) — so `S^3xS^3`'s trivial-block rank is still at
  most 1; what is missing is the argument forcing it to be exactly 1.
- Does **NOT** close the Universality open problem. It replaces an unqualified
  "2 of 4 and rising" with "3 of 4, with the exception identified and
  explained" — which is a weaker claim about universality than the pearls
  currently make, not a stronger one.
- Does **NOT** contradict C175. C175 says the four spaces differ in the
  isotropy's rigidity (`H = SU(3)` only for `S^6`); this round says they
  differ in whether `Lambda^2(m^{1,0})` meets its own dual. Two different
  asymmetries; both point the same way, that the four are not interchangeable.
- Does **NOT** apply beyond homogeneous nearly-Kahler 6-manifolds. Butruille's
  classification says there are exactly four; there is no fifth case to
  predict, so the criterion is retrodictive over a closed population and
  cannot be validated out of sample.
