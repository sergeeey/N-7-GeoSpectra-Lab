# E10 (round76) — Claim: explicit right-invariant frame on S³=SU(2), completing
# E9's own flagged follow-up

**Date:** 2026-07-17
**FL tier:** [x] Full (research claim; methodology per project CLAUDE.md)
**Question type:** [x] descriptive [ ] predictive [ ] causal

Descriptive: for the naturally-reductive connection family ∇^t on S³=SU(2)/{e}
(Agricola, arXiv:math/0202094 — same presentation used throughout E2/E7/E9),
does the RIGHT-invariant frame {f_i} (as opposed to E9's left-invariant {Z_i})
carry a ∇^t-parallel spinor at t=1, completing the t=0/t=1 symmetric picture
E9 explicitly left open ("candidate E10", E9's `decision.md` § Recommended next
action)?

## Stakes
Internal-only (mechanical follow-up verification of E9's own flagged, explicitly
unattempted, next step). Not promoted to `preprint.tex` here.

## Background (established, not re-derived here)
- E9 (`experiments/20260717-round73-e9-explicit-parallel-spinor/`): built the
  LEFT-invariant frame {Z_i} (Pauli-based Cl(3), Z_i=i·σ_i), spin connection
  `Ω_i(t) = -(tc/2)·Z_i` (E9's own abstract, physics-calibrated structure
  constant, `c=2`), showed `Ω_i(0)=0` (any constant left-invariant spinor is
  ∇⁰-parallel, D⁰ψ=0 exactly), and showed the SAME constant-spinor ansatz FAILS
  at t=1 (only ψ=0 solves `Ω_i(1)ψ=0` for all i). E9's `decision.md` explicitly
  hypothesized, but did NOT verify, that "the classical fact... the
  Cartan–Schouten (−)-connection (t=0) is parallelized by LEFT-invariant vector
  fields, while the (+)-connection (t=1) is parallelized by RIGHT-invariant
  vector fields" would resolve the t=1 case, and flagged this as future work
  ("candidate E10") specifically because building the right-invariant frame was
  "judged out of scope" for E9's own mechanical-verification task.
- E7 (`experiments/20260717-round72-e7-t-selection-principle/`): full curvature
  `R^t(X,Y)Z = t(t−1)·S(X,Y,Z)` vanishes EXACTLY at t=0,1, symbolic in c, for
  ANY value (sign or magnitude) of c — this fact is used below to resolve an
  apparent contradiction in Part 3/4 (see decision.md).

## Claim (falsifiable, four parts)

**Part 1 — sign-flip verification (task's explicit ask, step 1).** There exist
explicit LEFT- and RIGHT-invariant vector fields on SU(2), realized concretely
via the unit-quaternion model `g(x) = x0·I + x1·Z1 + x2·Z2 + x3·Z3` (E9's own
Z_i), such that:
  (a) both families are tangent to SU(2) (`x · X(x) = 0` identically),
  (b) `[Z_i^L, Z_j^L] = c0·ε_{ijk}·Z_k^L` for a concrete c0 found (not assumed)
      by direct symbolic differentiation of the ordinary vector-field bracket,
  (c) `[Z_i^R, Z_j^R] = −c0·ε_{ijk}·Z_k^R` EXACTLY — the opposite-sign relation
      the task asks to verify explicitly, not merely cite.

**Part 2 — literal repeat of E9's own recipe (task's explicit ask, steps 2–4).**
Mechanically reapplying E9's construction procedure — same symbolic structure
constant `c` (E9's own abstract, physics-calibrated parameter, kept separate
from Part 1's concretely-found `c0` — see "Two notions of c" below), same
spin-lift formula `Ω_i(t) = (1/4)Σ Γ^k_{ij}(t)·Z_j·Z_k` — but built from the
RIGHT-invariant bracket `[f_i,f_j] = −c·ε_{ijk}·f_k`, gives a well-defined
`Ω_i^right(t)`. The claim is agnostic in advance about whether this makes the
t=1 constant-spinor ansatz work in this frame (mirroring E9's own agnosticism
about the t=1 case) — see kill criteria.

**Part 3 — the deeper subtlety (task's honesty requirement, step 5).** Part 2's
`Ω^right(t)` is built by treating "∇^t in the right-invariant frame" as a
FRESH connection defined purely from {f_i}'s own self-bracket. But E9's ∇^t was
ALREADY a fully-specified global connection (pinned down via {Z_i} and extended
by Leibniz/C^∞-linearity to ALL vector fields, including f_i). The claim under
test: does E9's ORIGINAL, unmodified ∇^t at t=1 ALREADY make f_i fully parallel
(`∇¹_X f_i = 0` for every X, not just `∇¹_{f_i}f_j`) — a genuinely different
question from Part 2's mechanically-reapplied recipe?

**Part 4 — explicit spinor, if Part 3 finds full parallelism.** If Part 3
confirms f_i is fully ∇¹-parallel (as vector fields), does the natural
candidate spinor `ψ(x) = ḡ(x)·ψ₀` (quaternion-conjugate of the group element
times a constant `ψ₀ ∈ ℂ²` — i.e. "g⁻¹·ψ₀" on the unit sphere, since
`g·ḡ = |x|²·I`) satisfy `∇¹_{Z_i}ψ = 0` for all i, and does substituting it
into Agricola's own `D¹ψ = Σ_i Z_i·Z_i(ψ) + 1·H·ψ` give exactly zero?

## Two notions of "c" (pre-registered, not glossed over)

E7/E9 always treat the structure constant `c` in `[Z_i,Z_j]=c·ε_{ijk}·Z_k` as a
FREE, ABSTRACT bookkeeping parameter, later fixed to `c=2` via an INDEPENDENT
physics fact (Kostant cubic element calibration `h_H=3`), never by literally
computing the matrix commutator of the concrete Pauli-based `Z_i=i·σ_i`. E9's
own claim.md already flags the SIGN of this parameter as "a convention
artifact, not physical" (accepting either `+tH` or `−tH` as PASS). This
experiment is the FIRST in this project to build an actual concrete manifold
realization (the quaternion-sphere model) and compute NONTRIVIAL directional
derivatives — which is exactly where the abstract `c` and the LITERAL
geometric bracket constant of the concrete realization (`c0`, found in Part 1)
can, in principle, disagree. Both are used explicitly below, kept clearly
labeled, and Part 4 reports what happens under EACH.

## Kill criteria (MANDATORY — filled BEFORE running)

| Part | Kill condition | Threshold |
|---|---|---|
| 1 | Left or right vector fields fail tangency | `tangency_L_all==False` or `tangency_R_all==False` — would mean the quaternion-sphere realization itself is wrong |
| 1 | Right bracket does NOT carry the opposite sign of the left bracket | `c0_right_equals_minus_c0_left==False` — would directly falsify the task's central premise (would need to report this as a genuine surprise, not force a match) |
| 2 | Right-frame Γ is not so(3)-valued | `so3_valued_right==False` — would mean the right-invariant "same recipe" connection is not even metric-compatible |
| 2 | Cross-check `ΣZ_iΩ_i^right(t)` does not match `±tH` | `crosscheck_matches_tH_either_sign==False` — would mean the spin-lift formula was mis-applied in this frame |
| 2 | t=0 in the right frame does NOT give Ω=0 | `t0_omega_right_all_zero==False` — would break the expected mirror symmetry with E9's own t=0 result |
| 3 | E9's ORIGINAL ∇¹ does NOT make f_i fully parallel (using the concrete, internally-consistent c0) | `nabla1_fk_vanishes_for_all_i==False` — this is a genuine, informative, reportable finding either way (see decision.md for how it resolves an apparent tension with E7's own R^t=t(t−1)S fact) |
| 4 | Candidate `ψ=ḡ(x)ψ₀` does NOT satisfy `∇¹ψ=0` (using c0) even though Part 3 found f_i parallel | `psi_is_nabla1_parallel_using_c0==False` — would mean the vector-level parallelism of Part 3 does not lift cleanly to the spinor level; report as OPEN, not forced |
| 4 | `D¹ψ ≠ 0` for the Part-4 candidate (using c0), even though it is ∇¹-parallel | `D1_psi_is_zero_using_c0==False` — would mean Agricola's own formula and the parallel-transport check disagree, a serious internal inconsistency requiring escalation, not glossing |

If Parts 1–2 fail their kill conditions, the CORE task (as literally asked) is
FALSIFIED. If Part 3/4 diverge from the "clean mirror" expectation (either
direction), this is NOT a kill of Parts 1–2 — it is the honest "subtlety"
outcome the task's point 5 explicitly anticipates and asks to be reported, not
glossed over.

## Method

1. Reuse E9's own Cl(3) construction (Pauli matrices, `Z_i=i·σ_i`) unchanged;
   re-verify Clifford relations (not assumed).
2. Realize SU(2) concretely as the unit-quaternion model
   `g(x)=x0·I+x1·Z1+x2·Z2+x3·Z3`; verify `g(x)·ḡ(x)=|x|²·I` explicitly.
3. Build `X_i^L(x) := coords(g(x)·Z_i)` and `X_i^R(x) := coords(Z_i·g(x))` in
   the `{I,Z1,Z2,Z3}` basis; verify tangency to SU(2).
4. Compute `[X_i^L,X_j^L]` and `[X_i^R,X_j^R]` via the ORDINARY vector-field
   bracket formula (direct symbolic differentiation, `∂/∂x_μ`, no shortcuts);
   read off the concrete structure constant `c0`; verify the opposite-sign
   relation for ALL ordered pairs `(i,j)`, exhaustively.
5. Literal repeat of E9's recipe with `Γ^{right,k}_{ij}(t) := −t·c·ε_{ijk}`
   (E9's OWN abstract, symbolic `c`); build `Ω_i^{right}(t)`; cross-check
   against `±t·H`; repeat E9's t=0/t=1 checks (`sympy.solve` + independent
   nullspace) in this new frame.
6. Express `f_1 = X_1^R` in the `{Z_j}` basis with G-DEPENDENT coefficient
   functions `b^j(x) := ` coefficient of `Z_j` in `ḡ(x)·Z_1·g(x) / |x|²` (the
   adjoint-action conjugation, scaled to avoid symbolically inverting `|x|²`
   inside the conjugation itself); verify this reconstructs `X_1^R` exactly
   (consistency control).
7. Apply E9's ORIGINAL Leibniz-extended `∇^t_{Z_i}f_1 = Σ_j Z_i(b^j)·Z_j +
   t·Σ_{j,l} b^j·c0·ε_{ijl}·Z_l` (using the CONCRETE `c0`, since this question
   is about E9's own already-specified connection applied to a genuinely
   non-constant coefficient function, not about the abstract-c recipe of step
   5); evaluate at t=1; check whether it vanishes for all i=1,2,3.
8. If step 7 passes: construct `ψ(x)=ḡ(x)ψ₀`; compute `Z_i(ψ)` by direct
   differentiation (no shortcuts); check `∇¹_{Z_i}ψ=0` for all i using E9's
   `Ω_i(1)` formula with `c=c0`; substitute into Agricola's `D¹ψ` (built with
   `H_{c0}:=(3c0/2)ω`); check exactly zero. Cross-reference: repeat the SAME
   check using E9's own abstract `c=2` instead of `c0`, report whether it also
   works (pre-registered expectation: it should NOT, given the sign
   difference — report honestly either way).

## What this does NOT mean

1. Does **not** re-derive or challenge E7's abstract holonomy theorem, or E9's
   own t=0 result — both untouched, taken as given.
2. Does **not** resolve which of t=0/t=1 is physically selected (H1c/H2/H3 in
   E7's own open-questions list) — unaffected, exactly as open as before.
3. A Part-4 success does **not** mean "E9's own t=1 (using their abstractly
   calibrated c=2) has an explicit parallel spinor in the right-invariant
   frame" — if Part 4's crossref check shows the candidate FAILS under E9's
   own c=2, the correct, precise statement is narrower: a parallel spinor
   exists for THIS project's t=1 connection ONLY when the structure constant
   is matched to the concrete Pauli realization's own geometric bracket (c0),
   which differs from E9's abstract calibration by exactly the SIGN E9's own
   claim.md already flagged as a non-physical convention artifact. This
   distinction must be stated explicitly wherever this result is cited.
4. Does **not** verify the generalized product-decoupling formula for the full
   S³×S⁶ operator — out of scope, same as E9.
5. Does **not** imply E9's own Part-2-style construction (mechanically
   reapplying the recipe pattern to a new frame) is a reliable way to
   re-express an already-specified connection in a different frame in
   general — Part 3 shows a concrete counterexample to that implicit
   assumption, which is itself the main transferable finding here.

## Assumptions (status)

| Assumption | Status |
|---|---|
| Standard spin-lift formula for an so(n)-valued connection | [DOCS] — same citation as E9, applied not re-derived |
| Right-invariant vector fields are structure-constant-negated relative to left-invariant ones, for the SAME abstract Lie algebra | [DOCS] — standard Lie theory fact; VERIFIED here concretely via direct symbolic differentiation (Part 1), not merely cited |
| `∇^t_XY = t[X,Y]`, E9's own Cl(3)/su(2) conventions | [VERIFIED-tool, inherited from E2/E7/E9] |
| "Constant spinor" ⟺ `Z_i(ψ)=0` (E9's identification) | [DOCS, inherited] |
| E9's abstract `c` and Part 1's concrete `c0` are related only by the SIGN E9 already flags as non-physical, not by any other discrepancy | [VERIFIED-tool, this experiment, Part 1] — `|c0|=|c_E9|=2` confirmed; only the sign differs |
| The classical Cartan–Schouten "(+)-connection parallelizes right-invariant fields" fact | [DOCS] — motivated Part 3/4's design; independently VERIFIED here for THIS project's specific ∇^t family, not merely cited |

## Check
`python e10_right_invariant_frame.py` →
`verdict.core_part1_pass==true`, `verdict.core_part2_pass==true`,
`verdict.t1_naive_ansatz_fails_symmetrically_to_e9==true`,
`verdict.part3_reveals_frame_ambiguity_discrepancy==true`,
`verdict.explicit_t1_spinor_found_using_concrete_c0==true`,
`verdict.explicit_spinor_fails_under_e9_abstract_c2==true`,
`verdict.label=="PASS_MIRROR_NULL__PLUS_EXPLICIT_T1_SPINOR_UNDER_SIGN_CAVEAT"`.
