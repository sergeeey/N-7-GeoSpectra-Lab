# C84 -- first step into the full Peter-Weyl tower: sigma=-1 branch (real extension) + n=1 naive ansatz (honest NULL)

**Experiment id:** `20260812-c84-sigma-minus-branch-and-n1-ansatz-null`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C80 and C83 both independently named "the full Peter-Weyl
tower (S3's n=0, +-branch alone across every round in this arc)" as the
genuinely untested direction. This round is directed by the user: "Continue
with C84 -- try the full Peter-Weyl tower."

---

## Scoping done before writing the permanent script (not assumed, computed)

Before designing any test, this round re-read the primary source (Agricola
2002, `Agricola_2002_Dirac_naturally_reductive.pdf`, already in this repo)
directly and traced C74's and C79-C83's own WORKING CODE (not just
docstrings) for exactly how "D_S3 at n=0" is realized. Finding, confirmed by
reading the actual matrix construction in `c79_nonproduct_coupling.py` line
149 (`d_joint_base = d_s3_scalar * np.kron(I2, I64) + ...`): **every round in
this arc represents "D_S3 restricted to the n=0, sigma=+1 branch" as a bare
scalar `d_s3_scalar * I2`** -- NOT the actual `H=(3c/2)*omega` matrix (which
has two distinct eigenvalues +-1, `omega_squared_is_identity=True`, verified
in round67's own script). "sigma" in this arc's own established convention
labels which of TWO SEPARATE scalar constructions is used (mirror t<->1-t,
per round67's own docstring), not two subspaces of one physical `Delta_m`.
This is internally consistent with round67's own claim ("dim of
constant-spinor space = dim(V_0)*dim(Delta_m) = 1*2 = 2 ... for ONE sign")
and C74's own "n=0 total dim 4" (2+2, two separate copies).

Two independent hand-derivation attempts at the n=1 representation structure
(a naive `V_1 (x) Delta_m` tensor-product guess, and a full Peter-Weyl-block
guess `V_1 (x) V_1 (x) Delta_m`) gave inconsistent dimension counts (4 and 8
respectively), neither confidently matching round67's own closed-form target
multiplicity `(n+1)(n+2)=6` at n=1 by hand-reasoning alone. Per this
project's own OB10 lesson (never trust a hand-derived convention, verify
numerically) and the Oracle/Substrate Adequacy Gate discipline, this claim
does not trust either guess -- it builds the concrete 4-dim ansatz and
diagonalizes it numerically in the permanent script.

## The claims under test

> **C84-A (sigma=-1 branch, real extension).** Reusing C81's own
> `run_for_triple` methodology exactly, parametrized by `d_s3_scalar=-3/2`
> (the mirror of the already-tested `+3/2`), test round119's `so(4)_1`
> self-dual and anti-self-dual triples (the same candidates tested at
> sigma=+1 throughout C79-C82) against this second n=0 branch. **Prediction:
> clean NULL (no crossing)**, matching every other candidate's sigma=+1
> result in this arc under the corrected (raw-kernel-excluded) methodology.

> **C84-B (naive n=1 ansatz, honest attempt).** Build
> `D_orbit = sum_i Z_i (x) L_i` on `Delta_m (x) V_1` (4-dim, `L_i =
> sigma_i/2` the standard spin-1/2 angular momentum matrices -- the
> cheapest, most natural first guess for "the n=1 Peter-Weyl carrier").
> Diagonalize `i*D_orbit` (Hermitian) and compare against round67's own
> cited target at n=1 (eigenvalues +-5/2, multiplicity 6 each, total dim 12).
> **Prediction: this specific 4-dim naive ansatz will NOT match** (the
> dimension alone, 4, is already less than the target's 12), giving an
> explicit, numerically-verified NULL for this construction attempt --
> informative, not a failure, per this project's own Falsification Ladder
> discipline (NULL = progress, narrows the search space).

## Predictions, recorded before running the permanent script

| # | Prediction | Outcome |
|---|---|---|
| **P1 (Z_i bracket relations)** | `[Z_i,Z_j] = -2*epsilon_ijk*Z_k` exactly, all cyclic triples | pending |
| **P2 (sigma=-1, self-dual)** | no crossing, compressed test | pending |
| **P3 (sigma=-1, anti-self-dual)** | no crossing, compressed test | pending |
| **P4 (n=1 naive ansatz)** | does NOT match round67's target (mult 3,1 vs required 6,6; dim 4 vs required 12) | pending |

## kill_criterion

P1 fails if the bracket relations don't reproduce -- would mean a bug in
this round's own Clifford-algebra reuse, must stop and fix before trusting
anything downstream (the script asserts this and halts if it fails).
**P2/P3 are the actual sigma=-1 test** -- a "no crossing" result extends
n=0's full 4-dim level (both branches) to coverage for these candidates,
consistent with the whole arc's own pattern; a crossing would be the first
positive anywhere in this arc's `so(4)_1` testing and would require the
same extra scrutiny every unexpectedly positive result here has received.
**P4 is a genuine falsification test of THIS SPECIFIC construction
attempt**, not of the underlying physics -- if it matches, unexpectedly, that
would itself be a notable finding (an accessible n=1 basis); if it does not
match (the predicted, expected outcome, since its dimension is too small),
that specific ansatz is killed and the correct n>=1 representation
structure remains open for a future round.

## What this cannot show

- Does **not** complete the full Peter-Weyl tower -- only extends n=0 to
  both branches, and produces (at best) a documented NULL for one specific
  n=1 construction attempt, not a working n=1 (or higher) construction.
- Does **not** claim the naive `Delta_m (x) V_1` ansatz is the only possible
  n=1 construction -- only that this specific, cheapest first guess fails;
  a correctly-scoped outer(x)inner Clebsch-Gordan construction, or the
  explicit formula in this project's own cited external source (Sire & Xu,
  arXiv:2005.01448), remain unexplored paths for a future round.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
