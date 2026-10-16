# C165 Claim -- canonical (NOMIZU/ADNU) connection's own curvature 2-form R^c,
# restricted to the 3bar-summand of Lambda^2(m), independent source or not?

**Date:** 2026-09-06
**FL tier:** [x] Full
**Question type:** [x] descriptive (algebraic/representation-theoretic; NOT
empirical, NOT causal -- a structural computation about a fixed Lie-algebraic
object, per EstimandOps L0)

---

## Prior Result Gate

1. **Exact claim under test:** does `R^c`, the curvature 2-form of the
   canonical (Ambrose-Singer/Nomizu) connection on `m` (the tangent
   representation of `S^6=G2/SU(3)`), restricted to the `3bar`-isotypic
   summand of `Lambda^2(m)`, supply an `su(3)`-equivariant map `3bar ->
   su(3)_C` that is genuinely INDEPENDENT of `m`'s already-used connection/
   representation data (as opposed to zero, or proportional to already-used
   data)?
2. `decision.md` grep for "R^c", "canonical connection curvature",
   "Nomizu curvature": [x] done, 0 hits outside C164's own Section 9 (the
   round that raised this question) -- reviewed at
   `experiments/20260906-c164-ob14-path-i-vs-ii-scoping/decision.md` Sec 9,
   Concern 3.
3. `round*_claim.md` + scripts grep for "canonical connection" /
   "R^c(X,Y)" / "ad([X,Y]_h)": [x] done -- no prior round computes this
   specific object (the canonical connection's curvature as distinct from
   the Levi-Civita Riemann tensor) as a separate su(3)-valued 2-form on `m`.
   Round 22-25 of `20260708-dolan-casimir-g2su3` compute a "canonical-
   connection torsion `T^c`" on a DIFFERENT coset presentation (`V_7`, the
   7-dim vector rep of `G2/SU(3)` used in the Dolan-Casimir Weitzenbock
   program, not `S^6`'s 6-dim `m`) -- a related but distinct object on a
   different representation, not re-used here, not superseding this claim.
4. `null_results/` + `parked/` grep for "curvature 2-form" / "R^c":
   [x] done, 0 hits.
5. `git log -S"R^c"` / `-G"ad\(\[X,Y\]"`: not run (no prior code references
   this exact construction under any name found in steps 2-4 above).
6. Primary source re-read: Agricola, Hofmann, Lawn 2023 ("Invariant spinors
   on homogeneous spheres", arXiv:2203.02961v3), Remark 5.2 (page 42) --
   already the source for `round59_route_a_independent.py`'s `NOMIZU`
   (labelled in-code as "Nomizu / Levi-Civita map Lambda^g(e_i)") and
   `ADNU` ("su(3) isotropy generators ad(nu_i)|m") tables. Standard general
   theory for the canonical connection's curvature on a reductive
   homogeneous space (Nomizu 1954; Kobayashi-Nomizu Vol.II Ch.X): for
   `g = h (+) m` reductive, `R^c(X,Y)Z = -[[X,Y]_h, Z]` for `X,Y,Z in m` --
   a standard closed-form result, used directly below (Section "Method"),
   not re-derived from a Leibniz-rule sweep, per the task's own instruction.
7. **Status:** [x] NEW (a genuinely new object for this project, per steps
   2-4's grep results) -- proceed.

---

## Estimand

**Population:** the single fixed geometric object `S^6 = G2/SU(3)`, its
tangent representation `m` (real 6-dim, `su(3)`-module `3 (+) 3bar` after
complexification), and its canonical connection's curvature 2-form.
**Intervention:** none (descriptive/structural computation, not an
intervention on a population).
**Comparator:** `m`'s own already-certified connection/representation data
(`NOMIZU`, `ADNU` from `round59_route_a_independent.py`), used as the
baseline against which "independent" is judged -- same standard C142 used
to reject the C70/C71 triality intertwiners as gauge-orbit relabelings, not
independent data.
**Endpoint:** whether the linear map `R^c|_{3bar}: 3bar -> su(3)_C` is (a)
identically zero, (b) nonzero but proportional to / derivable from `m`'s own
already-used data, or (c) genuinely new/independent data.
**Summary measure:** categorical verdict (one of the 4 kill-criterion rows
below), not a continuous statistic -- MCID is not applicable to a structural
existence question of this kind.
**MCID:** N/A (categorical, not a magnitude comparison).

---

## Claim

`R^c`, restricted to the `3bar`-summand of `Lambda^2(m)`, supplies data that
is either zero, proportional to already-used data, or independent -- exactly
one of these three holds, and this round determines which by direct
computation of the actual curvature tensor, cross-checked against the
representation-theoretic constraint that `R^c` (as a curvature 2-form of a
reductive homogeneous space) is automatically `Ad(SU(3))`-equivariant.

Supporting sub-claims:
1. `R^c(e_i,e_j) = -[e_i,e_j]_h` (the `su(3)`-part of the full `g2` bracket
   of two `m`-basis vectors), computed via an independent, from-octonions
   construction of the full 14-dim `g2` Lie algebra (not reusing `NOMIZU`/
   `ADNU`'s own bivector tables directly for the bracket itself, only for
   cross-checking normalization/basis-matching afterward).
2. `Lambda^2(m)` (real 15-dim, complexifying to `3bar (+) 1 (+) 8 (+) 3`)
   decomposes into `su(3)`-isotypic blocks distinguishable, at minimum, by
   the quadratic Casimir eigenvalue of the `su(3)` vector-representation
   (`ad(nu_a)|_m`, 6x6 real antisymmetric matrices) acting on `Lambda^2(m)`.
3. `R^c` restricted to the isotypic block(s) matching the fundamental
   representation's Casimir eigenvalue (i.e. the combined `3 (+) 3bar`
   6-dim piece, since `3` and `3bar` share the same quadratic Casimir and
   cannot be separated by it alone) is checked directly for vanishing.

---

## Kill criterion (filled BEFORE running the computation)

| Outcome | Condition |
|---|---|
| `ZERO-ON-3BAR-SUMMAND` | `R^c` restricted to the `3 (+) 3bar` Casimir-eigenspace of `Lambda^2(m)` is the zero map, to machine/exact precision. Consistent with, and independently predicted by, Schur's Lemma: `su(3)_C` (the adjoint, `dim=8`) and `3bar` (`dim=3`) are non-isomorphic irreducible `su(3)`-representations, so ANY `su(3)`-equivariant linear map between them is forced to be zero, regardless of the specific curvature values -- this is a representation-theoretic prediction stated here BEFORE running the numeric check, not a post-hoc rationalization. |
| `PROPORTIONAL-NOT-INDEPENDENT` | `R^c` restricted there is nonzero, but its nonzero values are a scalar multiple of (or linearly reconstructible from) `m`'s own `NOMIZU`/`ADNU` bivector data under a change of basis -- same standard C142 applied to C70/C71. |
| `INDEPENDENT-SOURCE-FOUND` | `R^c` restricted there is nonzero AND not reconstructible from `NOMIZU`/`ADNU` data alone (requires genuinely new structure-constant information, i.e. the `m`-`m` bracket's `h`-component, which is absent from `round59`'s own tables). |
| `COMPUTATION-INFEASIBLE` | The full 14-dim `g2` bracket cannot be reconstructed to sufficient precision/certainty from available machinery (e.g. numeric octonion-derivation construction fails Jacobi/closure checks) within this round's scope. |

**Pre-registered expectation:** `ZERO-ON-3BAR-SUMMAND`, via the Schur's-Lemma
argument above -- stated explicitly BEFORE running the computation, per this
project's Anti-Overfitting Gate discipline (AOG-1: pre-registration). If the
numeric result contradicts this prediction, that is itself the more
important finding (it would mean either the representation-theoretic
identification of the target space is wrong, or `R^c` does not actually
land purely in `su(3)_C` as claimed -- both would be significant errors to
catch, not explained away).

If FAIL (i.e. `INDEPENDENT-SOURCE-FOUND`): kills the operative premise of
C164 Section 9 Concern 3's own uncertainty ("whether it is INDEPENDENT... is
not yet known") in the surviving direction -- OB14 sub-paths (i')/(ii')
gain a genuine candidate construction, a significant unblock.
If PASS (`ZERO-ON-3BAR-SUMMAND` or `PROPORTIONAL-NOT-INDEPENDENT`): confirms
C164's corrected verdict should revert toward `BOTH-HIGH-RISK-NO-CHEAP-
DIFFERENTIATOR` (the third candidate, once checked, joins C70/C71 and G102
as rejected), closing the specific gap the skeptic pass opened.

If no hypothesis is killed/confirmed by either outcome -> gate is not
scientifically motivated. Both possible outcomes here directly resolve
C164's explicitly-left-open question, so this condition does not apply.

---

## Checks planned

- T1: Independently reconstruct the full 14-dim `g2` Lie algebra as 7x7
  matrices via the octonion-derivation condition (reusing `g96_g2_su3.py`'s
  already-certified `find_g2_generators`/`g2_condition_matrix` construction,
  `experiments/20260626-g96-s6-g2-su3/`, `status: VERIFIED` per its own
  `results_g96.json`), confirm closure + Jacobi + the `su(3) (+) m` (8+6)
  split reproduces `G96`'s own certified dimension counts before using it
  for anything new.
- T2: Compute `[e_i,e_j]` for the 6 `m`-basis generators (`comp_gens` in
  `G96`'s own naming), project onto the `su3_gens` subspace via
  least-squares (same projection method `G96` already uses for its own
  closure/adjoint-rep checks) -- this projection coefficient vector IS
  `R^c(e_i,e_j)` (up to sign convention), a genuinely new 6x6x8 tensor this
  project has not computed before.
- T3 (adversarial): verify the `su(3)`-equivariance of the resulting `R^c`
  tensor directly (not merely assumed from general theory) -- check that
  `R^c(Ad(g)e_i, Ad(g)e_j) = Ad(g)R^c(e_i,e_j)` for at least one nontrivial
  `su(3)` group element numerically, as an internal consistency check that
  the construction was not corrupted by a basis-matching error between
  `G96`'s octonion-derived frame and `round59`'s `NOMIZU`/`ADNU` frame
  (these two frames were built independently and are NOT guaranteed to
  share a common normalization/orientation without an explicit check).
- T4 (adversarial): confirm the Schur's-Lemma prediction is not a red
  herring by explicitly checking that `su(3)_C` (`ADNU`'s own 8
  generators, or `G96`'s `su3_gens`) really is irreducible under its own
  adjoint action (standard for a simple Lie algebra, but checked directly
  via the Casimir/no-invariant-subspace test rather than cited from memory)
  and that `3bar` really is non-isomorphic to it (trivial dimension check,
  3 != 8, but stated explicitly).

---

## What this does NOT mean

1. Does NOT prove no OTHER, not-yet-conceived `su(3)`-equivariant object
   could supply independent data for OB14's sub-paths -- only resolves this
   ONE specific candidate (`R^c`'s `3bar`-restriction), exactly as C164
   itself scoped this as "one previously-uncomputed candidate," not "the
   last possible one."
2. Does NOT reopen or re-derive C142's rejections of C70/C71 or G102 --
   those stand independently, cited not re-verified here.
3. Does NOT change `N_gen=3`'s `CONDITIONAL` status, `lambda =
   FREE_COUPLING_PARAMETER`, `sm_derivation_claimed = False`, or
   `safe_for_runtime = False`.
4. Does NOT edit `OPEN_BLOCKERS.md`, `pearl_registry/INDEX.md`,
   `null_results/INDEX.md`, or `CLAIM_LEDGER.yaml` -- per this round's
   explicit instructions, registry updates are the orchestrating session's.
5. Does NOT run any git operations.
6. If `ZERO-ON-3BAR-SUMMAND` is confirmed, does NOT by itself prove the
   Levi-Civita-vs-canonical distinction C164 raised was worthless to check
   -- the check was cheap, well-motivated by the skeptic pass, and a
   negative result here is exactly the kind of informative NULL this
   project's methodology treats as progress (closes a candidate cleanly),
   not a wasted round.
