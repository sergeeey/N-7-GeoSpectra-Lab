# C141 claim -- with a twist bundle MATCHED to Sigma's own singlet count
# (W'' = m (+) 2*1, module type 3+3bar+1+1, dim 8, TWO su(3) singlets --
# same shape as Sigma's 1+1+3+3bar), does the S6 twisted Dirac operator's
# invariant-sector kernel still differ from 1? This is the decisive
# follow-up BOTH of C139's independent skeptic passes converged on,
# isolating whether D_S6 discriminates Sigma from a genuinely alternative
# construction of the SAME shape, not merely a different-shape one.

## Mode declaration

**Convergent-mode round.** Tests ONE specific, pre-registered claim to
completion. This is the direct, both-skeptic-recommended follow-up to
`experiments/20260904-c139-twisted-s6-alternate-representation-negative-control/`
(C139), which found `kernel=0` (not 1) for `W'=m` (dim 6, ZERO singlets)
but was qualified by both context-blind skeptic passes: the `(1,1)`-shaped
invariant sector (vs `Sigma`'s `(2,1)`) is itself a forced consequence of
`m`'s zero-singlet module type, so C139's discrimination, while real and
robust, is narrower in mechanism than a genuinely shape-matched comparison
would be.

## A mandatory pre-registered fact this round MUST cite and build on,
## not re-derive: the equivalence precheck

**Before this round exists at all**, a precheck was run
(`experiments/20260904-c139-.../decision.md` Section 17, and
`c139_precheck_m_plus_2singlets.py` in that same directory) to answer a
sharp objection: since `m(+)2*1` and `Sigma` have IDENTICAL `su(3)`-module
branching (`3+3bar+1+1` vs `1+1+3+3bar`), is `D'_{m+2*1}` theorem-forced
to equal `D'_Sigma` via a trivial change of basis, making this round a
redundant regression test?

**Answer, already established, READ IT before doing anything else:**
NO -- verified both by a dimension-counting argument (`Sigma`'s only
achievable `{NAB_i}`-invariant subspace dimensions are `{0,4,4,8}`; `6` is
not among them, so `Sigma` cannot contain an invariant `m`-shaped block)
and by a direct intertwiner-nullspace search (nullspace dimension exactly
`0` -- no intertwiner exists at all, not even a non-unitary one), FOR THE
NATURAL construction of `m(+)2*1`'s connection: the two extra singlets are
**decoupled** (`conn_i = rho_vector(NOMIZU[i]) (+) 0_2`, block-diagonal),
since no `NOMIZU`-derived connection data exists for them.

**This round MUST use that exact, already-cleared construction** (extra
singlets decoupled, zero connection) -- do not invent a different coupling
for the extra singlets without first re-running an equivalent precheck for
whatever new choice is made, per C139's own Section 17 scope note.

## Background, read in full before computation

- `experiments/20260904-c139-twisted-s6-alternate-representation-negative-control/decision.md`
  IN FULL, especially Sections 2 (why `m` was chosen), 8b (Term1=0 is
  FORCED by Schur's lemma for any zero-singlet twist -- does NOT apply
  here, `m(+)2*1` HAS two singlets, matching `Sigma`), 9 (the dimension-shape
  caveat this round directly resolves), 11-12 (both skeptic passes' exact
  wording recommending this test), and 17 (the equivalence precheck, see
  above).
- `experiments/20260714-round59-trivial-rank-certification/decision.md`
  -- the original `Sigma`-twisted construction, `(a,b,s)=(-1,-sqrt(3),4)`,
  `dim ker(D+|1)=1`, domain/target shape `(2,1)`.
- `experiments/20260811-c73-round59-real-twisted-dirac-battery/decision.md`
  and
  `experiments/20260811-c73b-torsion-family-genuine-deformation-and-twist-control/decision.md`
  -- four prior non-discriminating wrong-twist attempts, for context (this
  round is a DIFFERENT kind of test than any of the five prior attempts
  including C139 itself -- shape-matched, not merely differently-shaped).
- `pearl_registry/INDEX.md` row 89 (closed by C139, but read the closure
  text for the exact residual gap this round fills) and `OPEN_BLOCKERS.md`
  OB14 ("why Sigma, not m") -- this round is the concrete next step OB14
  itself names.
- `CLAIM_LEDGER.yaml` `C139_ALTERNATE_TWIST_M_KERNEL_ZERO` and
  `C2_ROUND59_KERNEL_DIM1` -- read `does_not_imply` fields on both.

## Construction, stated precisely before computing anything

`W'' = m_C (+) 2*1` -- the complexified tangent/isotropy representation
`m` (dim 6, module type `3+3bar`, reused UNMODIFIED from C139) direct-summed
with two trivial `su(3)`-singlets (dim 8 total, module type `3+3bar+1+1`,
matching `Sigma`'s own two-singlet count).

Connection: `conn_i = rho_vector(NOMIZU[i]) (+) 0_2` for `i=1..6` -- `m`'s
own connection (reused UNMODIFIED from C139) block-diagonal with an
explicit ZERO 2x2 block on the two extra singlet directions (per the
precheck's own construction, Section 17). This is a design choice with a
stated reason (no other connection data exists for these two extra
dimensions) -- name any alternative considered and why it was rejected,
per the Anti-Overfitting Gate, matching C139's own Section 2 discipline.

`D''(eta (x) w) = sum_i (e_i . nabla^Sigma_i eta)(x)w + (e_i.eta)(x)(nabla^{m+2*1}_i w)`
-- the identical Leibniz-rule twisted-Dirac structure round59/C139 use,
reusing `build_twisted_dirac_np` (generalized, dim-agnostic, already exists
in C139's script) unmodified, with `dim_w=8`.

## The Zero-Signal Gate check, required before proceeding

Per `falsification-ladder.md` Step -5: `(exists entity) AND (exists
falsifiable predicate) AND (exists measurable outcome)`, all three
required.

- **Entity:** a twisted S6 Dirac operator `D''_{S6,twist=m+2*1}`, built
  with the same Killing-spinor/homogeneous-space machinery round59/C139
  used, twisted by `m(+)2*1` (dim 8, TWO singlets, matching `Sigma`'s own
  shape) with the precheck-cleared decoupled-singlet connection.
- **Falsifiable predicate:** the invariant-sector kernel of `D''` is
  `=1` (matching `Sigma` -- meaning `D_S6` does NOT discriminate a
  shape-matched alternative, i.e. C139's own discrimination was
  specifically a shape/singlet-count effect, not evidence `D_S6` prefers
  `Sigma`'s particular geometric content) or `!=1` (a genuinely
  shape-controlled discrimination -- the first evidence that `D_S6`
  distinguishes `Sigma` from an alternative of the SAME formal shape, not
  merely a differently-shaped one).
- **Measurable outcome:** the explicit kernel dimension, domain/target
  invariant-sector shapes (predict `(2,1)` via Clebsch-Gordan BEFORE
  computing, matching `Sigma`'s own shape -- state this prediction
  explicitly, then verify), computed via the same two-independent-routes
  discipline (numeric SVD + exact sympy) C139 used.

**If the kernel shape itself is NOT `(2,1)` despite the singlet count
matching (e.g. the extra singlets' decoupling changes the invariant-sector
DIMENSION count in some unexpected way), report this explicitly and
investigate before interpreting the kernel value -- do not silently treat
a shape mismatch as if the comparison were clean, per C139's own Section 9
lesson.**

## Falsifiable claim

The invariant-sector kernel dimension of `D_S6` twisted by `m(+)2*1`
(shape-matched to `Sigma`: dim 8, two `su(3)` singlets, precheck-cleared
as genuinely non-equivalent to `Sigma` under the natural construction) is
NOT 1 -- a discrimination that, unlike C139's own `m`-only result, cannot
be attributed to a bare singlet-count/shape effect (per C139 Section 8b's
Schur's-lemma forcing argument, which required a ZERO-singlet twist
bundle and does not apply here).

## Kill criterion

FALSE if: (a) `kernel=1` for `m(+)2*1` -- report this as informative in
the OTHER direction: it would suggest `D_S6`'s discrimination in C139 was
specifically a shape/singlet-count effect (matching `H_singlet` from the
user's own pre-registered alternative hypotheses, per C139 Section 17's
citing discussion), not evidence that `Sigma`'s specific geometric content
(as opposed to any two-singlet twist bundle) is preferred -- this would
NARROW, not reverse, C139's own qualified conclusion, and should be
reported precisely as that, not as a failure of this round; (b) the
domain/target invariant-sector shape is not `(2,1)` as predicted -- report
the actual shape found and why the CG prediction failed, before
interpreting any kernel value; (c) the chosen decoupled-singlet
construction turns out, on closer inspection, to admit an undisclosed
equivalence to `Sigma` after all despite the precheck (extremely unlikely
given the precheck's own two-independent-method confirmation, but check
explicitly per this project's own repeated "verify from at least two
angles" discipline -- re-run the precheck's own intertwiner search as
part of this round's own Section 3-equivalent, do not merely cite it).

## What this round does NOT show

- Does NOT, regardless of outcome, change `N_gen=3`'s CONDITIONAL status,
  `lambda = FREE_COUPLING_PARAMETER`, `sm_derivation_claimed = False`, or
  `safe_for_runtime = False`.
- Does NOT reopen C123-C140's verdicts.
- Does NOT, if `kernel!=1`, prove `Sigma` is THE uniquely correct twist --
  it would show `D_S6` discriminates at least one shape-matched
  alternative, not that it discriminates ALL of them (an exhaustive
  survey of shape-matched alternatives is not attempted).
- Does NOT, if `kernel=1`, prove `Sigma` is NOT physically preferred --
  it would show this SPECIFIC shape-matched alternative is not
  distinguished by `D_S6`'s kernel structure alone; other criteria
  (explicit physical motivation from AHL2023, consistency with the rest
  of the fermion content) are untouched either way.
- Does NOT close `OPEN_BLOCKERS.md` OB14 in full even if it succeeds --
  it supplies one more data point toward "why Sigma, not m," not the
  complete physical justification itself.
- Does NOT solicit Tom Lawrence's Part 5.

## Verification plan

- Read all cited files in full before any computation, especially
  C139's own Section 17 precheck (reuse its exact construction, do not
  re-derive independently) and Sections 8b/9 (the exact caveat this round
  is designed to resolve).
- Pre-register the Clebsch-Gordan prediction for domain/target invariant
  sector shapes BEFORE computing (expect `(2,1)`, matching `Sigma`'s own
  shape, since the singlet count now matches) -- verify against numeric
  SVD and exact sympy, per C139's own three-way-agreement discipline.
- Re-verify (not merely cite) the precheck's own equivalence result as
  part of this round's own construction -- confirm the actual `D''`
  matrix built here is consistent with what the precheck assumed.
- Verify from at least two independent angles throughout, matching this
  project's repeated discipline this session.
- Cite `[VERIFIED]`/`[CITED]`/`[INFERRED]`/`[SPECULATIVE]` throughout.
- FL Step 8a skeptic pass (context-blind: only claim.md + decision.md +
  code, no session history). Given this round directly resolves the
  residual gap BOTH of C139's skeptic passes independently flagged as the
  decisive next step, and touches the same 6-ledger-dependent headline
  evidentiary chain, run TWO differently-worded passes regardless of the
  first pass's verdict, matching C139's own precedent -- unless the first
  pass returns a clean, unqualified confirmation with zero findings.
