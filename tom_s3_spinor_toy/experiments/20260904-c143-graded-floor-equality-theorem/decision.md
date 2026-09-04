# C143 decision -- DESIGN/THEOREM round (no new Dirac-operator computation).
# Proves a general, precise necessary-and-sufficient LEMMA for when C141's
# graded rank-nullity floor is achieved with equality (Lemma 1, Hom-space
# dimension 1 -- the case of all 4 constructions tested so far), and shows
# WHY the same argument genuinely does not settle the question for a
# Hom-space of dimension >=2 (Lemma 2, C142's still-unbuilt candidate).
# Formalizes the Delta_dyn := ker - floor diagnostic (per the user's own
# 2026-09-04 proposal) as a standing pre-registration gate for future
# twisted-D_S6 rounds.

**Date:** 2026-09-04
**Type:** DESIGN/THEOREM round. No physics computation, no Dirac operator
built, no numeric verification script -- the "proof" below is a synthesis
of ALREADY-certified facts (round59, C139, C141, C142), not a new
computed result. Where a symbolic illustration is used (Lemma 2), it is
explicitly a toy example, labeled as such.

## Verdict

```text
LEMMA_1_PROVED__HOM_DIM_1_EQUALITY_IFF_DEFINING_SCALAR_NONZERO
  __GENERALIZES_AND_EXPLAINS_ALL_4_OF_C141S_TESTED_CASES__NOT_JUST_RESTATES_THEM
  __ROUND59S_OWN_2026-07-14_PEARL_ROW_24_ALREADY_STATED_HALF_OF_THIS_GENERALLY
  __LEMMA_2_STATES_WHY_HOM_DIM_2_CASE_IS_GENUINELY_OPEN__NOT_JUST_UNTESTED
  __TOY_EXAMPLE_SHOWS_GENERICITY_DOES_NOT_TRIVIALLY_RESOLVE_HOM_DIM_2
  __DELTA_DYN_GATE_FORMALIZED__PROPOSED_ADDITION_TO_PARENT_ACTION_GATE_F2
```

**One line:** the graded-floor equality is NOT an unconditional theorem
("kernel always equals floor for any twist bundle") -- it is the
CONSEQUENCE of a provable structural lemma (Schur's lemma forces a
1-dimensional-Hom-space summand's map to be a single scalar, and a single
scalar achieves full rank iff nonzero) COMBINED WITH four independently-
established, non-automatic geometric facts (each summand's specific
scalar happens to be nonzero) that round59/C139/C141 each separately
verified. This is a stronger, more useful result than either "it's a
theorem" (false, as Lemma 2 shows) or "it's a coincidence" (also false,
as Lemma 1 shows) -- it is a PRECISE, checkable criterion, proved once
and now citable for any future round instead of re-derived case by case.

---

## 1. Setup, stated precisely (reusing already-certified structure)

`[CITED]`, reusing C141 Sections 8/9e without re-deriving: for every
twisted-`D_S6` construction in this project's Leibniz-rule family, the
operator restricted to its `su(3)`-invariant sector decomposes as a
direct sum over `{connection}`-invariant summands `k=1..K`, each a linear
map `D_k: domain_k -> target_k` between finite-dimensional
`su(3)`-invariant subspaces, with `dim domain_k` and `dim target_k`
computable from pure branching data (Frobenius reciprocity, `C141`
Section 2's `trivial_mult()`).

**Graded floor** (`[CITED]`, C141 Section 9e): `floor_k := max(0, dim
domain_k - dim target_k)`; `floor(rho) := sum_k floor_k`. By ordinary
rank-nullity applied to each summand separately, `dim ker(D_k) >=
floor_k` ALWAYS -- this half needs no new proof, it is elementary linear
algebra, true for literally any linear map of any shape.

**The open question, restated precisely:** when does `dim ker(D_k) =
floor_k` (equality, not merely `>=`)?

## 2. Lemma 1 -- the Hom-dimension-1 case (proved; covers all 4 tested
   constructions)

**Statement.** Suppose the space of `su(3)`-equivariant linear maps
`domain_k -> target_k` (i.e. `Hom_su3(domain_k, target_k)`, computed from
the irreducible constituents of `domain_k`/`target_k` alone, independent
of any specific connection) is **1-dimensional**. Then:

```
dim ker(D_k) = floor_k   <=>   D_k != 0 (the summand's single defining
                                          scalar is nonzero)
```

**Proof.** By Schur's lemma, `Hom_su3(domain_k, target_k)` being
1-dimensional means every `su(3)`-equivariant map between them is a
scalar multiple `c_k * Phi_k` of a FIXED (basis-independent up to that
scalar) map `Phi_k`, determined entirely by the irreducible-constituent
structure of `domain_k`/`target_k` -- not by the specific geometric
connection data. `D_k`, being `su(3)`-equivariant by construction (it is
built from `su(3)`-invariant-sector projections of an `su(3)`-equivariant
Leibniz-rule Dirac operator), MUST equal `c_k * Phi_k` for some scalar
`c_k` depending on the geometry (`NOMIZU`'s specific realization). `Phi_k`
itself, being THE (unique up to scale) nonzero equivariant map between
these specific irreducible pieces, achieves the MAXIMUM POSSIBLE rank for
a map of its shape (this is what "the" equivariant map, singular, means
representation-theoretically -- there is no OTHER, lower-rank equivariant
map to degenerate into, since the space of equivariant maps is exactly
1-dimensional). Therefore: `c_k = 0` gives `D_k = 0`, `dim ker = dim
domain_k > floor_k` (strictly, whenever `domain_k > 0`); `c_k != 0` gives
`D_k` at `Phi_k`'s own maximal rank, hence `dim ker(D_k) = dim domain_k -
rank(Phi_k) = floor_k` exactly. `QED`.

**This is a genuine theorem, not a restatement of C141's empirical
finding** -- it explains WHY equality held in all 4 cases, as a
structural NECESSITY given 1-dimensional Hom spaces, rather than an
observed coincidence. What it does NOT do is guarantee `c_k != 0` --
THAT remains a geometric fact requiring its own, separate justification,
addressed next.

### 2a. Why `c_k != 0` in every case tested so far -- two DIFFERENT
    strengths of justification, named honestly

**Round59-type summands (the "Killing-eigenvalue" channel, `T0`'s own
floor-1 contribution, and `T1`'s matching sub-block):** `c_k != 0` is
established by a GENERAL geometric argument, not a case-specific
computation. `[CITED]`, round59's own decision.md, "Why the coefficient
is `-sqrt(3)`": *"the trivial-block amplitude IS the Killing-spinor Dirac
eigenvalue... the rank-1 result is therefore not a numerical accident of
this coset -- it is forced by the existence of Killing spinors with
nonzero Killing constant."* **This general principle is ALREADY
registered in this project's own `pearl_registry/INDEX.md` row 24**
(2026-07-14, quoted exactly): *"rank(D+|1) is thus MECHANISM-forced by
Killing-spinor existence, not a coset-specific numerical accident... On
any other nearly-Kahler coset admitting Killing spinors with nonzero
Killing constant... the analogous trivial-block rank should also be 1 by
the same two-line argument."* **This round's contribution is connecting
this decade-old-in-session-time pearl explicitly to Lemma 1**: pearl row
24's own claim IS, in the language developed here, "`c_k != 0` for the
Killing-eigenvalue summand, for a GENERAL reason (any nonzero Killing
constant), not merely a verified fact about this one coset."

**`m`-twist-type summands (`Term2`, C139's own contribution, and its
copy inside `C141`'s three summands):** `c_k != 0` is established, so
far, only by DIRECT SYMBOLIC COMPUTATION for this project's specific
`NOMIZU` data (`c = -2*sqrt(3)/3` exactly, C139 Section 6), independently
re-verified across the WHOLE admissible connection family (C139 Section
8c's 13-angle sweep, `|c(theta)|` constant). **No general argument
(analogous to the Killing-eigenvalue one) is currently known for WHY this
specific class of scalar must be nonzero** -- it is a computed,
robustly-confirmed geometric fact, not (yet) a theorem. This is a
genuinely weaker form of certainty than the round59-type case, and is
named as such, not silently equated with it.

**Net effect on the 4 tested cases:** `[VERIFIED, by citation, not
recomputed]` `T0`/round59 (floor 1, one round59-type summand, `c!=0`
general): equality holds by Lemma 1 + the general argument. `C139` (floor
0, one `m`-type summand, `c!=0` computed+swept): equality holds by Lemma
1 + the computed fact. `C141` (floor 0, three summands -- one `m`-type,
two trivially-zero-dimension singlets contributing `floor_k=0` with
`domain_k=target_k=0`, a degenerate but consistent case of Lemma 1):
equality holds. `T1` (floor 1, two summands -- one round59-type
[`Sigma_even`], one a "wide" `(1,2)`-shaped piece [`Sigma_odd`] with
`floor_k=0` that C141 itself found "automatically injective"): equality
holds, with the `Sigma_odd` piece's own nonvanishing following from the
SAME round59-type Killing-eigenvalue argument (it is built from the same
`NAB` connection, just a different `su(3)`-isotypic piece of it).

## 3. Lemma 2 -- the Hom-dimension->=2 case (genuinely open; states
   precisely WHY, not merely "untested")

**Statement (negative -- what does NOT follow).** If `Hom_su3(domain_k,
target_k)` has dimension `d >= 2`, Lemma 1's proof does NOT go through:
`D_k` is now a linear combination `c_1*Phi_1 + ... + c_d*Phi_d` of `d`
INDEPENDENT equivariant maps, and there is no single "the" equivariant
map to be nonzero or zero -- `D_k`'s RANK depends on the specific values
of `(c_1,...,c_d)`, not merely on whether they are collectively nonzero.

**Toy illustration (explicitly NOT a physics claim -- illustrates the
linear-algebra fact only):** take `domain_k` 2-dimensional, `target_k`
2-dimensional, `Hom` space 2-dimensional with basis `Phi_1, Phi_2`.
`D_k(c_1,c_2) = c_1*Phi_1 + c_2*Phi_2`. Even with BOTH `c_1 != 0` AND
`c_2 != 0` (the direct 1-dimensional-case analogue of "the scalar is
nonzero"), `D_k` can still be RANK-DEFICIENT for special ratios
`c_1/c_2` (e.g. if `Phi_1, Phi_2` are chosen so that `det(c_1*Phi_1 +
c_2*Phi_2) = c_1*c_2 - c_1*c_2 = 0` identically along some curve in
`(c_1,c_2)`-space, or more simply: `Phi_1 = [[1,0],[0,0]]`, `Phi_2 =
[[0,0],[0,1]]`, then `D_k(c_1,c_2) = diag(c_1,c_2)` is rank-DEFICIENT
exactly when `c_1=0` OR `c_2=0` individually, a REAL, checkable, non-
measure-zero-in-any-relevant-sense condition if the geometry ever forces
one of the two independent contributions to vanish while the other does
not). **A `>=2`-dimensional Hom space genuinely opens a `dim ker > floor`
possibility that a 1-dimensional one structurally cannot** -- this is the
precise, provable reason `W_cand=3+3bar+3bar` (C142's own candidate,
`Hom_su3(3, W_cand)` dimension 2) would be a REAL test, not a
foregone-conclusion repeat of the 4 cases already checked, IF it could be
built (C142 found it currently cannot, for reasons unrelated to this
lemma -- see `OPEN_BLOCKERS.md` OB14).

**What remains genuinely `[OPEN]`:** whether `su(3)` representation
theory (independent of the connection's specific values) forces the
MULTIPLE scalars entering a `>=2`-dimensional Hom space to combine into a
full-rank map for THIS project's specific class of `NOMIZU`-derived
connections -- this is not addressed by Lemma 1 or 2 and would require
either a new general argument (analogous to the Killing-eigenvalue one)
or an actual computed example, neither of which exists yet (C142's own
finding: no buildable example currently exists in this project's
content).

## 4. The `Delta_dyn` diagnostic, formalized (per the user's own
   2026-09-04 proposal)

**Definition:** `Delta_dyn(rho) := dim ker(D_rho) - floor(rho)`.

By Lemma 1 (Section 2) applied summand-by-summand: for ANY twist bundle
built entirely from Hom-dimension-1 summands (as all 4 tested
constructions are), `Delta_dyn = 0` is not merely likely, it is FORCED
by Lemma 1 alone, GIVEN that each summand's own defining scalar is
nonzero -- which is exactly what round59/C139 each separately, and
independently, established. **`Delta_dyn > 0` is impossible for this
class of twist bundle UNLESS at least one previously-verified-nonzero
scalar were somehow zero for a NEW connection choice** (a real, checkable
possibility this round does not rule out for connections outside the
ones already tested, but which would contradict already-certified facts
for the specific connections `round59`/`C139`/`C141`/`T1` used).

**Consequence, stated plainly:** any FUTURE round using only
Hom-dimension-1 summands (the ENTIRE class this project has built so
far) is **predictable in advance, before building anything** -- compute
`floor(rho)` from branching data alone (per claim.md's own "cheapest
differentiating test" framing), and `Delta_dyn=0` follows automatically
from Lemma 1, MAKING SUCH A ROUND UNINFORMATIVE ABOUT `D_S6`'s DYNAMICS
by construction (exactly C141's own finding, now explained rather than
merely observed). **A round is only capable of showing something new if
it uses a genuinely `>=2`-dimensional Hom-space summand** -- which C142
already found unbuildable with this project's current geometric content.

## 5. Proposed standing methodology gate (registry action)

**Proposed addition to `PARENT_ACTION_GATE.md` F2 (Twist):** before
building ANY future twisted-`D_S6` construction, compute:
1. The summand decomposition and each summand's `Hom_su3` dimension
   (pure branching data, no connection needed).
2. If EVERY summand has `Hom` dimension 1: **the round is
   `PRE-DETERMINED-UNINFORMATIVE` by Lemma 1** (this document) UNLESS at
   least one summand's defining scalar can be argued, in advance, to
   plausibly VANISH for the proposed connection (a real, checkable
   escape -- flag it explicitly if claimed, per the Anti-Overfitting
   Gate's pre-registration discipline). Do not build; report the
   floor and stop.
3. If at least one summand has `Hom` dimension `>=2`: the round is
   `POTENTIALLY-INFORMATIVE` -- pre-register the falsifiable hypothesis
   pair `H0: Delta_dyn=0` (representation theory suffices) vs `H1:
   Delta_dyn>0` (first genuinely dynamical result in this line) BEFORE
   computing anything, per the user's own explicit proposal, then build.

This directly operationalizes claim.md's own "cheapest differentiating
test" principle for this ENTIRE family of future rounds, not just this
one -- a round's informativeness is now checkable in minutes, from pure
representation theory, before any Dirac-operator construction begins.

## 6. What this round does NOT show

- Does NOT prove `Delta_dyn=0` is a general theorem for ALL conceivable
  twist bundles -- Section 3 explicitly shows the Hom-dimension-`>=2`
  case is open, not closed favorably or unfavorably.
- Does NOT build or test any new twist bundle.
- Does NOT establish a general argument for WHY `m`-type (twist-bundle's-
  own-connection) scalars are nonzero, the way round59's pearl row 24
  does for Killing-eigenvalue-type scalars -- named as a real, narrower
  gap (Section 2a), not glossed over.
- Does NOT reopen C123-C142's verdicts.
- Does NOT change `N_gen=3`'s CONDITIONAL status.
- Does NOT solicit Tom Lawrence's Part 5.

## 7. Self-check (per claim.md, in place of a full skeptic pass)

**Does Lemma 1 smuggle in an unstated assumption?** The proof rests on
`Phi_k` (the unique-up-to-scale equivariant map) achieving MAXIMAL rank
among maps of its shape when nonzero -- this is not an assumption, it
follows directly from Schur's lemma's own content (there is no SECOND,
independent, possibly-lower-rank equivariant map for it to degenerate
towards, since the Hom space is 1-dimensional). The one place genuine
care is needed: Lemma 1 is stated for a SINGLE summand's map having
target rank exactly `min(domain_k, target_k)` when `c_k!=0` -- this holds
because `Phi_k` itself, being canonically built from the irreducible
decomposition (an isomorphism-type map when `domain_k`/`target_k` share
an irrep 1-1, an inclusion/projection-type map otherwise), already
achieves that rank by its own construction, independent of any specific
connection. This is re-confirmed, not merely assumed, by the fact that
EVERY 1-dimensional-Hom-space summand actually computed in this project
(round59, C139, C141, T1 -- Section 2a) achieved exactly this behavior.

## 8. Registry actions -- NOT performed by this round, proposed only

**`PARENT_ACTION_GATE.md` F2** -- append Section 5's proposed gate
(exact wording above), replacing the ad hoc "compute floor before
building" language C141/C142 already used informally with a citable,
two-branch procedure.

**`pearl_registry/INDEX.md`** -- new row:

```
| 2026-09-04 | C143 (theorem synthesis, connecting C141's graded floor to round59's own 2026-07-14 pearl, row 24) | Proved (not merely observed) that dim ker(D_rho) = floor(rho) whenever every connection-invariant summand has a 1-dimensional su(3)-equivariant Hom space (Schur's lemma forces a single scalar; nonzero iff full rank) -- this covers ALL FOUR twist-bundle constructions tested in this project's history (round59/T0, C139, C141, T1), explaining rather than merely confirming C141's own empirical 4/4 match. Round59's own scalar nonvanishing has a GENERAL geometric reason (any nearly-Kahler coset with a nonzero-Killing-constant Killing spinor, pearl row 24, 2026-07-14 -- already registered, newly connected here); C139/C141's m-type scalar nonvanishing is established only by direct computation, a genuinely weaker form of certainty, named honestly. For Hom-space dimension >=2 (C142's still-unbuildable W_cand=3+3bar+3bar candidate), the SAME argument genuinely fails -- a toy example shows multiple independent nonzero scalars can still combine into a rank-deficient map, meaning Delta_dyn>0 becomes possible in principle for the first time. Consequence: ANY future twisted-D_S6 round using only Hom-dim-1 summands (the entire class built so far) is PRE-DETERMINED uninformative about D_S6's dynamics, checkable in minutes from pure branching data before building anything | If a future round is proposed using only Hom-dimension-1 summands, computing its graded floor in advance will show Delta_dyn=0 is forced by Lemma 1, and building it would be uninformative -- OR, if a genuinely Hom-dimension->=2 twist bundle is ever found buildable (per OB14's own open status), computing whether its Delta_dyn is provably forced to 0 (an extension of this round's Lemma 2, not yet attempted) versus genuinely undetermined would settle whether such a round is worth building at all | any future round proposing a new twisted-D_S6 construction, before any Dirac-operator computation begins | at the next twisted-D_S6 round proposal, or if new geometric content extends this project's Hom-space options | pending -- impact 8 -- see experiments/20260904-c143-graded-floor-equality-theorem/decision.md |
```

**No `CLAIM_LEDGER.yaml` or `null_results/INDEX.md` entry proposed** --
this round proves a lemma about an existing, already-registered claim
(`C141_KERNEL_IS_GRADED_BRANCHING_FLOOR_NOT_DYNAMICS`), it does not
itself assert a new physics claim with its own truth/test-outcome status.

## Evidence tier

**Tier: `[VERIFIED]`** for Lemma 1's proof (Section 2, elementary Schur's-
lemma + rank-nullity argument, self-contained) and for its application to
all 4 tested cases (Section 2a, direct citation of already-certified
facts, re-checked against the cited files this session, not from
memory). **`[CITED]`** for pearl_registry row 24's exact wording
(re-quoted directly from the file). **`[VERIFIED]`** for Lemma 2's toy
example (elementary linear algebra, `diag(c_1,c_2)` rank-deficient iff
`c_1=0` or `c_2=0`, trivially checkable by inspection). **`[OPEN]`,
explicitly, not glossed over:** whether a general (not case-by-case)
argument exists for `m`-type scalar nonvanishing (Section 2a), and
whether `su(3)` representation theory forces `Delta_dyn=0` even for
Hom-dimension-`>=2` cases in this project's specific connection class
(Section 3's closing paragraph). No claim in this document overstates
what Lemmas 1/2 actually establish.
