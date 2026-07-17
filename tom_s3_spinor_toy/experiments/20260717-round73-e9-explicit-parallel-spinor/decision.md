# E9 — Decision

**Date:** 2026-07-17
**Verdict:** `PASS_T0_ONLY__T1_NAIVE_ANSATZ_FAILS_PARTIAL` — core claim PASS at t=0
(clean, exact, no caveats); t=1 sub-claim is an honest, informative NULL for the
*specific* ansatz tested, not a falsification of E7's abstract argument.
**Go/no-go:** t=0 result is promotable as a direct, mechanical confirmation of
E7's H1b Recomposition; t=1 remains OPEN, flagged as a concrete follow-up
(candidate E10), not forced to a fake PASS.

## Result

### 1. Explicit spin connection, derived (not assumed)

Building `Γ^k_{ij}(t) = t·c·ε_{ijk}` directly from the task's own definition
`∇^t_X Y = t[X,Y]` (the same su(2) convention E7 used), this frame connection is
exhaustively [VERIFIED-tool] `so(3)`-valued (antisymmetric in `j,k`) for all
three `i` (`step2_so3_valued.so3_valued_all_i = true`) — confirming metric
compatibility directly, not by citation.

Applying the **standard** spin lift for an so(n)-valued connection ([DOCS],
Lawson–Michelsohn / Friedrich) — `Ω_i(t) = (1/4)Σ_{j,k}Γ^k_{ij}(t)·Z_j·Z_k` —
gives, exactly:

```
Ω_1(t) = -(tc/2)·Z_1,   Ω_2(t) = -(tc/2)·Z_2,   Ω_3(t) = -(tc/2)·Z_3   (up to reindexing)
```

(concretely, `Ω_1(t) = [[0, -ict/2],[-ict/2, 0]]`, matching `-(tc/2)·Z_1` exactly
since `Z_1 = iσ_1`).

### 2. Independent cross-check against Agricola's own eq.(5) — non-circular

`Σ_i Z_i·Ω_i(t)` was computed [VERIFIED-tool] and found to equal **exactly**
`t·H`, with `H = (3c/2)ω` — E2's own already-established Kostant cubic element,
`ω = Z1Z2Z3` confirmed (again) exactly the 2×2 identity
(`step3_omega_and_H`, `step4_crosscheck_against_agricola_H.crosscheck_matches_tH
= true`, sign convention `+tH`). This is a genuine, non-circular check: `Ω_i(t)`
was derived here purely from the connection's own definition and the standard
spin-lift formula — **not** from Agricola's eq.(5) — and it reproduces
Agricola's algebraic term exactly. This directly satisfies the task's "derive,
don't assert" requirement for the spin connection.

### 3. t=0: explicit parallel spinor, exact, no caveats

Since every `Ω_i(t)` is proportional to `t`, `Ω_i(0)=0` identically for all
`i=1,2,3` (`step5.t0_omega_all_zero = true`). Hence **any** constant
left-invariant spinor — tested explicitly for `e1=(1,0)`, `e2=(0,1)`, and a
generic symbolic combination `(a,b)` — satisfies `∇^0_{Z_i}ψ = Z_i(ψ) +
Ω_i(0)ψ = 0 + 0 = 0` for all three `i` simultaneously
(`parallel_checks` all `true`). Substituting into Agricola's own eq.(5),
`D^0ψ = Σ_i Z_i·Z_i(ψ) + 0·H·ψ`: the orbital term vanishes because `ψ` is
constant (`Z_i(ψ)=0` by definition of "constant" in this trivialization) and
the algebraic term vanishes because `t=0` kills it regardless of `H`
— **`D^0ψ = 0` exactly**, for the entire 2-dimensional constant-spinor space,
verified symbolically (`t0_D_psi_is_zero = true`).

This is a **direct, mechanical, non-abstract confirmation** of E7's H1b chain
(flatness → trivial holonomy → parallel spinor → zero mode) at t=0: the parallel
spinor was explicitly constructed (not merely asserted to exist by a general
theorem) and substituted into the actual Dirac-operator formula, giving exactly
zero.

### 4. t=1: the naive ansatz fails — reported honestly, not forced

Attempting the *same* ansatz at t=1 (with the project's own calibrated `c=2`):
solving `Ω_i(1)ψ=0` for `i=1,2,3` simultaneously (6 scalar equations, 2
unknowns, via both `sympy.solve` and an independent nullspace computation on the
stacked 6×2 matrix) gives **only the trivial solution `ψ=0`**
(`t1_only_trivial_solution_via_solve = true`,
`t1_only_trivial_solution_via_nullspace = true`, nullspace dimension 0).

This is independently cross-confirmed via Agricola's own Theorem-4.2 route,
using nothing beyond already-calibrated quantities: `H = 3·I₂` (invertible,
since `h_H=3≠0`), so `D^1(constant ψ) = 1·H·ψ = 3ψ`, which is zero **only** for
`ψ=0` (`theorem42_cross_check_confirms_trivial_only = true`). Two independent
routes — direct parallel-transport (`Ω_i(1)ψ=0`) and Agricola's own eq.(5) via
the already-established `H` — agree exactly
(`two_independent_routes_agree = true`).

**Bonus generalization (step 7, symbolic in `t`,`c`):** `Ω_1(t) = -(tc/2)Z_1`
alone already answers a sharper question than "does t=1 work" — `det(Z_1)=1`
(`Z_1` is invertible for any nonzero scalar), so `det(Ω_1(t)) = (tc/2)²`, whose
only root in `t` (treating `c` as the established nonzero structure constant) is
**`t=0`**. This shows `t=0` is not merely "the value we happened to check that
works" — it is the **unique** value of `t` for which the naive constant
left-invariant-spinor ansatz can possibly produce a nonzero parallel spinor.
Every `t≠0` (not just `t=1`) fails this specific ansatz.

## Why this is PARTIAL, not a clean two-sided PASS

The task explicitly anticipated this possibility ("maybe the constant
left-invariant spinor ansatz is too naive and the actual parallel section
requires a nontrivial group-element-dependent profile — check this explicitly
rather than assuming the simplest ansatz works"). That is exactly what happened,
and the direct construction reveals *why*, cleanly:

- `∇^t_{Z_i}Z_j = t[Z_i,Z_j]` means the left-invariant frame `{Z_i}` **itself**
  is `∇^t`-parallel if and only if `t=0` (`Γ^k_{ij}(t)=0` for all `i,j,k` exactly
  when `t=0`, given `c≠0`). At `t=0` the frame is literally flat in this
  trivialization, so a constant spinor trivially rides along parallel — a
  transparent, structural reason, not a coincidence.
- At `t=1`, the connection is still flat as an **operator** (`R^1=0`, E7's own
  result — trivial holonomy around closed loops), but the specific
  left-invariant frame is **not** itself `∇^1`-parallel (nonzero torsion
  `T^1=+[X,Y]≠0`, i.e. nonzero Christoffel symbols in this frame). E7's abstract
  holonomy argument (flat + simply-connected S³ ⟹ *some* global parallel
  spinor exists) is **not contradicted** by this — it only guarantees existence
  in *some* trivialization, and this experiment shows concretely that the
  left-invariant one used throughout E2/E7/this project is not that
  trivialization for `t=1`.
- The standard classical fact this points toward (not verified here, [INFERRED]
  only): the Cartan–Schouten `(−)`-connection (`t=0`) is parallelized by
  **left**-invariant vector fields, while the `(+)`-connection (`t=1`) is
  parallelized by **right**-invariant vector fields — dual constructions. If
  true, the `t=1` parallel spinor would need to be built in a right-invariant
  trivialization, which was **not** constructed in this experiment (would
  require introducing genuinely new machinery — explicit right-invariant vector
  fields / group coordinates — not previously used anywhere in E2/E7/this
  project, and was judged out of scope for this mechanical-verification task
  rather than risk a rushed, unverified new convention).

## Kill Analysis (per this project's Anti-Overfitting Gate — recorded because the
t=1 sub-claim came back negative for the specific ansatz tested)

- **What this result rules out:** that the *same*, simplest, left-invariant
  constant-spinor construction works symmetrically at both t=0 and t=1. It does
  not. It also rules out "t=0 happens to work, we didn't check whether other t
  also work" — step 7 shows t=0 is the *unique* such value for this ansatz.
- **What this result does NOT rule out:** E7's abstract holonomy argument for
  t=1 (a parallel spinor may still exist there, in a different trivialization);
  it also does not touch H1c/H2/H3 (physical selection among t=0,1) at all.
- **What survives, confirmed stronger than before:** the t=0 zero mode is now a
  *directly constructed, verified* fact, not merely an application of a general
  theorem — this strengthens E7's H1b for t=0 specifically from "proved via
  abstract chain of general theorems" to "proved via abstract chain of general
  theorems **and** independently reproduced by explicit symbolic construction."

## Assumptions (status)

| Assumption | Status |
|---|---|
| Standard spin-lift formula for an so(n)-valued connection | [DOCS] — standard spin-geometry textbook fact, applied (not re-derived from first principles of spin geometry) |
| `∇^t_XY = t[X,Y]`, E2/E7's Cl(3)/su(2) conventions | [VERIFIED-tool, inherited from E2/E7] |
| "Constant spinor" ⟺ `Z_i(ψ)=0` | [DOCS, same identification E2 already used via Theorem 4.2] |
| Cartan–Schouten left/right-invariant duality as the likely explanation of the t=1 failure | **[INFERRED, NOT verified here]** — plausible, standard classical fact, but this experiment did not build the right-invariant trivialization needed to check it directly |

## What this does NOT mean

1. Does **not** claim a parallel spinor fails to exist at t=1 in any absolute
   sense — only that the specific left-invariant-constant ansatz used
   throughout this project's own conventions does not realize it. E7's abstract
   holonomy argument for t=1 is untouched by this finding.
2. Does **not** resolve H1c (which of t=0/t=1 is physically selected), H2
   (equations of motion), or H3 (anomaly cancellation) — unaffected, exactly as
   open as before.
3. Does **not** verify the generalized product-decoupling formula for the full
   S³×S⁶ operator (E2/E3's own flagged scope gap) — this experiment concerns the
   S³ factor's `D^t` alone, same scope as E2/E7.
4. Does **not** claim the t=0 result promotes E2/E3's candidate mechanism to
   `preprint.tex` — the E2/E3 scope gaps remain exactly as open as before this
   experiment.

## Pearl-registry candidate

The clean structural fact `Ω_i(t) = -(tc/2)Z_i` (spin lift proportional to the
Clifford generator itself, for this specific `∇^t` family on S³) plus the
left/right-invariant-frame asymmetry it exposes between the two Cartan–Schouten
connections is a genuinely non-obvious, transferable structural insight
(impact_score ~4: narrow to naturally-reductive-space constructions elsewhere in
this line of work, e.g. if a similar torsion family is ever built on S⁶ or
another odd-dimensional factor) — worth a `pearl_registry/INDEX.md` line if this
project's global registry is updated in a future session (not done here, outside
this folder's scope).

## Recommended next action

If pursued further (candidate "E10"): construct the explicit right-invariant
vector fields / trivialization for S³=SU(2) (would require introducing genuine
group-coordinate machinery, e.g. Euler angles or the exponential map, not
previously used in E2/E7/this project) and check directly whether the
`∇^1`-parallel spinor lives there, completing the t=0/t=1 symmetric picture. This
is a well-defined, cheap-ish follow-up (the algebra is the same Cl(3)/su(2)
toolkit; only the frame convention changes) but was not attempted here to avoid
introducing an unverified new convention under this experiment's mechanical-
verification scope. Until done, do not cite "an explicit t=1 parallel spinor was
constructed" anywhere — only "t=0's parallel spinor was explicitly constructed
and verified; t=1's existence remains guaranteed only by the abstract argument,
not by direct construction in this project's established left-invariant frame."

## Check (reproduces this decision)
`python e9_explicit_parallel_spinor.py` →
`verdict.core_claim_t0_pass == true`, `verdict.crosscheck_matches_tH == true`,
`verdict.t1_nonzero_solution_exists == false`,
`verdict.t0_is_unique_root_symbolic == true`,
`verdict.label == "PASS_T0_ONLY__T1_NAIVE_ANSATZ_FAILS_PARTIAL"`.
