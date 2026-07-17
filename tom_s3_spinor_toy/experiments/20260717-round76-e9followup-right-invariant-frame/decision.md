# E10 (round76) — Decision

**Date:** 2026-07-17
**Verdict:** `PASS_MIRROR_NULL__PLUS_EXPLICIT_T1_SPINOR_UNDER_SIGN_CAVEAT` — the
task's literal ask (Parts 1–2) PASSES cleanly and reproduces E9's own t=1 NULL
in mirror image; going deeper (Parts 3–4, per the task's explicit honesty
requirement) finds a genuine, previously-latent frame-recipe subtlety and,
resolving it, an EXPLICIT right-invariant-trivialization parallel spinor at
t=1 — but only under a specific, now-explicit sign convention for the
structure constant, not under this project's own physics-calibrated one.
**Go/no-go:** Parts 1–2 promotable as a direct completion of E9's literal
follow-up request. Parts 3–4 promotable as a genuine, tool-verified finding,
but ONLY with the sign caveat stated explicitly every time it is cited — never
as an unqualified "E9's t=1 has an explicit parallel spinor."

## Result

### Part 1 — explicit L/R-invariant frames, sign flip [VERIFIED-tool]

Realizing SU(2) concretely as the unit-quaternion model
`g(x) = x0·I + x1·Z1 + x2·Z2 + x3·Z3` (E9's own `Z_i=i·σ_i`), verified exactly
`g(x)·ḡ(x) = |x|²·I` (`quaternion_norm_check.g_gbar_equals_norm2_I = true`).
Both `X_i^L(x):=coords(g(x)Z_i)` and `X_i^R(x):=coords(Z_i g(x))` are tangent
to SU(2) (`tangency_L_all = tangency_R_all = true`).

Computing `[X_i^L,X_j^L]` and `[X_i^R,X_j^R]` via the ORDINARY vector-field
bracket (direct `∂/∂x_μ` differentiation, no shortcut formulas assumed) gives,
exhaustively over all ordered pairs `(i,j)`, i,j∈{1,2,3}:

```
[X_i^L, X_j^L] = c0 · ε_{ijk} · X_k^L,   c0 = -2  (found, not assumed)
[X_i^R, X_j^R] = -c0 · ε_{ijk} · X_k^R = +2 · ε_{ijk} · X_k^R
```

(`left_bracket_check_all_pairs_ok = true`,
`right_bracket_matches_minus_c0L_all_pairs = true`,
`c0_right_equals_minus_c0_left = true`). This is a **direct, computational**
confirmation of the standard Lie-theory fact that right-invariant vector
fields realize the SAME abstract Lie algebra with the OPPOSITE-sign structure
constants — done here via an explicit matrix Lie-group construction, not
merely cited.

### Part 2 — literal mirror of E9's recipe [VERIFIED-tool]

Building `Γ^{right,k}_{ij}(t) := -t·c·ε_{ijk}` (E9's own abstract, symbolic
`c`, sign-flipped per the task's instruction) and lifting to spin via E9's own
formula gives, exactly:

```
Ω_i^right(t) = +(tc/2)·Z_i    (mirror of E9's Ω_i^left(t) = -(tc/2)·Z_i)
```

so(3)-valuedness holds (`so3_valued_right = true`); the cross-check
`Σ_i Z_i·Ω_i^right(t)` reproduces `-t·H` EXACTLY (`crosscheck_matches_minus_tH
= true`, `H=(3c/2)ω` unchanged from E2). At t=0, `Ω^right(0)=0` for all i
(`t0_omega_right_all_zero = true`), so any constant right-invariant spinor is
∇⁰-parallel — mirrors E9 exactly, unsurprising since `t=0` kills the algebraic
term regardless of frame or sign.

At t=1, `c=2` (E9's own calibration), solving `Ω_i^right(1)ψ=0` for i=1,2,3
simultaneously gives **only the trivial solution** (`t1_only_trivial_via_solve
= true`, `t1_only_trivial_via_nullspace = true`, nullspace dimension 0) —
independently cross-confirmed via the Agricola-style route
(`H_right_at_c2 = -3·I2`, invertible, so `D^{1,right}(const ψ)=-3ψ=0` only for
ψ=0: `theorem_style_crosscheck_confirms_trivial_only = true`). The
determinant-uniqueness argument (E9's own step 7) carries over unchanged:
`det(Ω_1^right(t)) = (tc/2)²`, unique root `t=0`
(`t0_is_unique_root_right_frame = true`).

**This is the literal, complete answer to the task's steps 1–4 as instructed:
switching to the right-invariant frame and mechanically reapplying E9's own
recipe does NOT rescue the t=1 constant-spinor ansatz — it fails in EXACTLY
the same way, mirror-imaged.** If this experiment stopped here, the honest
report would be: E9's hypothesis (that the right-invariant frame would fix
t=1) is NOT supported by the most direct reading of "build ∇^t in the
right-invariant frame."

### Part 3 — the subtlety the task's point 5 explicitly asked to watch for [VERIFIED-tool]

Part 2's `Ω^right(t)` treats "the right-invariant-frame connection" as a
FRESH connection, defined purely from `{f_i}`'s own self-bracket. But E9's
`∇^t` was already a fully-specified GLOBAL connection (pinned down via `{Z_i}`
and extended by Leibniz/C^∞-linearity to every vector field on G, including
`f_i` itself). These are, a priori, two DIFFERENT things that can both
reasonably be called "∇^t in the right-invariant frame."

Expressing `f_1 = X_1^R` in the `{Z_j}` basis with the honest, G-DEPENDENT
adjoint-action coefficient functions `b^j(x)` (verified, via reconstruction, to
exactly reproduce `X_1^R`: `reconstruction_of_fk_from_b_and_ZL_matches_part1_XR
= true`; the I₂-component of the conjugation vanishes identically as required
by su(2)-preservation: `I2_component_of_conjugation_is_zero = true`), and
applying E9's ORIGINAL Leibniz-extended connection —

```
∇^t_{Z_i} f_1 = Σ_j Z_i(b^j)·Z_j + t·Σ_{j,l} b^j·c0·ε_{ijl}·Z_l
```

(using the CONCRETE `c0=-2` from Part 1, since this question is about
applying E9's actual connection to a genuinely non-constant coefficient
function — the abstract, symbolic `c` cannot substitute here because
directional derivatives require an actual, concrete vector field) — evaluated
at t=1, this vanishes **identically, for all i=1,2,3, exactly**
(`nabla1_fk_vanishes_for_all_i = true`, all nine `coeff_l_at_t1` entries are
symbolically `0`, not merely numerically small).

**This means E9's ORIGINAL t=1 connection ALREADY makes the right-invariant
vector fields fully parallel — in EVERY direction, not just their own
self-bracket — directly contradicting what Part 2's mechanically-reapplied
recipe would suggest (`Ω^right(1)≠0`).** These two computations do not
disagree because either is wrong; they disagree because they answer two
different questions, both of which can be honestly labeled "∇¹ in the
right-invariant frame."

**Resolving an apparent contradiction with E7.** At first pass this looks
inconsistent with E7's own `R^t(X,Y)Z=t(t-1)S(X,Y,Z)`, which the reader might
expect to pin down a UNIQUE "t=1" independent of any sign convention for c —
and indeed it does: E7's flatness condition `t(t-1)=0` has roots {0,1}
regardless of the SIGN or magnitude of c (E7's own claim.md: "verified to hold
for GENERIC symbolic c"). So "t=1" is unambiguously the same, flat, non-t=0
connection whether built with `c=+2` (E9's calibration) or `c=c0=-2` (Part
1's concrete finding) — full vector-level parallelism of `f_i` at t=1 is
therefore a STRONGER statement than mere flatness, but it is NOT inconsistent
with E7: a flat connection (trivial holonomy) is exactly what permits a
globally parallel frame to exist in the first place. There is no
contradiction; Part 3's finding is a legitimate strengthening of E7's flatness
fact for this specific t=1 member of the family, using the internally
self-consistent concrete realization.

### Part 4 — the explicit spinor [VERIFIED-tool], with an honest sign caveat

Given Part 3's finding, the natural candidate parallel spinor is
`ψ(x) = ḡ(x)·ψ₀` (quaternion-conjugate of the group element times a constant
`ψ₀∈ℂ²` — equivalently `g(x)⁻¹·ψ₀` on the unit sphere, since `g·ḡ=|x|²I`).
Computing `Z_i(ψ)` by direct symbolic differentiation (no shortcuts) and
checking `∇¹_{Z_i}ψ = Z_i(ψ) + Ω_i^left(1)_{c0}·ψ = 0`, using E9's OWN
`Ω_i(t)=-(tc/2)Z_i` formula with `c=c0=-2` — this is EXACTLY zero for all
i=1,2,3 (`psi_is_nabla1_parallel_using_c0 = true`, all three residuals are the
literal zero matrix, not approximately zero). Substituting into Agricola's own
`D¹ψ = Σ_i Z_i·Z_i(ψ) + 1·H_{c0}·ψ` (with `H_{c0}=(3c0/2)ω=-3·I2`) gives
`D¹ψ = 0` EXACTLY (`D1_psi_is_zero_using_c0 = true`).

**This is a genuine, explicit, non-constant, right-invariant-trivialization
parallel spinor at t=1 — completing exactly what E9's decision.md
speculated.**

**The caveat, stated as prominently as the result itself:** re-running the
IDENTICAL check using E9's own abstractly-calibrated `c=2` (NOT the concrete
`c0=-2`) for `Ω_i(1)`, the SAME candidate `ψ=ḡ(x)ψ₀` FAILS —
(`psi_is_nabla1_parallel_using_E9_abstract_c2 = false`, residuals are nonzero,
generic functions of x0..x3, e.g. for i=1:
`-2a_x1 - 2i·a_x2 - 2i·b_x0 + 2b_x3` in the first spinor component). The
explicit spinor found here is a parallel section of the SAME t=1 CONNECTION
E9 studied, but built using the structure constant that is LITERALLY correct
for the concrete Pauli-matrix realization (`c0=-2`) rather than E9's own
abstractly-fixed sign (`c=+2`, calibrated via an unrelated physics fact,
`h_H=3`, and already flagged by E9's own claim.md as "a convention artifact,
not physical"). Since E9's own project explicitly accepts either sign of `c`
as equally valid (their own cross-check accepted both `+tH` and `-tH` as
PASS), this is NOT a contradiction of anything E9 claimed — but it means the
precise, honest statement of this result requires naming which sign
convention is in play, every time. **Do not cite this as "an explicit t=1
parallel spinor was found for E9's calibrated connection" without this
caveat** — the correct statement is: "an explicit parallel spinor exists for
the t=1 member of this connection family, in the sign convention where the
structure constant matches the concrete Pauli/quaternion realization
directly; it has not been shown to exist (and by this same computation,
demonstrably fails as literally attempted) in the sign convention this
project has used for its own physics calibration (`c=+2`)."

## Why Parts 3–4 do not simply overturn Part 2's clean NULL

Both are true simultaneously, and both matter for different purposes:
- **Part 2** (literal task instruction: "build ∇^t in the right-invariant
  frame using the same recipe pattern") is the correct answer to "does
  mechanically reapplying E9's OWN construction procedure to the new frame
  rescue the constant-spinor ansatz at t=1?" — **No.**
- **Part 3–4** is the correct answer to "does E9's ALREADY-EXISTING t=1
  connection (unchanged, not redefined) have a parallel spinor in SOME
  frame?" — **Yes, in the right-invariant frame, with an explicit,
  non-constant profile — but only under the sign convention matching the
  concrete realization, not E9's calibrated one.**

These are different questions the task's phrasing could reasonably be read to
ask; both are answered honestly and completely here, rather than picking the
one that produces a cleaner-looking headline.

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result rules out:** that mechanically reapplying E9's OWN recipe
  pattern to a new (right-invariant) frame is a valid way to compute how an
  ALREADY-DEFINED connection looks when re-expressed in that frame — Part 3
  is a concrete, verified counterexample to that implicit assumption. It also
  rules out "the naive right-invariant constant-spinor ansatz works at t=1"
  (Part 2's clean NULL stands).
- **What this result does NOT rule out:** E9's abstract holonomy argument (a
  parallel spinor exists at t=1 in SOME trivialization) — Part 3–4 in fact
  CONFIRMS this by direct construction, resolving what E9 left as an abstract
  guarantee into an explicit spinor. It also does not rule out that a
  DIFFERENT sign convention for `c` (E9's own `c=+2`) has ITS OWN, as-yet
  unconstructed, parallel spinor at t=1 — this remains open (see Recommended
  next action).
- **What survives, confirmed stronger than before:** E9's own speculative
  hypothesis ("the t=1 parallel spinor would need to be built in a
  right-invariant trivialization") is now DIRECTLY CONFIRMED by explicit
  construction — with the added, previously-invisible discovery that this
  project's abstract structure-constant bookkeeping (`c`) and its literal
  geometric realization (`c0`) disagree in sign, a fact that had never
  surfaced before because no prior experiment needed a concrete manifold
  model with nontrivial directional derivatives.

## Assumptions (status)

| Assumption | Status |
|---|---|
| Standard spin-lift formula for an so(n)-valued connection | [DOCS] — inherited from E9 |
| `∇^t_XY = t[X,Y]`, E9's Cl(3)/su(2) conventions | [VERIFIED-tool, inherited] |
| Right-invariant fields carry opposite-sign structure constants to left-invariant, same abstract algebra | [VERIFIED-tool, this experiment, Part 1] — no longer merely [DOCS] |
| E9's abstract `c=2` and Part 1's concrete `c0=-2` differ ONLY in sign, not otherwise | [VERIFIED-tool, this experiment, Part 1] |
| Cartan–Schouten "(+)-connection parallelizes right-invariant fields" | [VERIFIED-tool, this experiment, Part 3] — upgraded from E9's own [INFERRED, NOT verified] |
| An explicit parallel spinor exists at t=1 for E9's OWN `c=+2` convention (not just `c0=-2`) | **[OPEN, NOT verified here]** — the Part-4 candidate `ψ=ḡ(x)ψ₀` demonstrably fails under `c=+2`; no alternative candidate was found or tested for that sign |

## What this does NOT mean

1. Does **not** claim E9's own calibrated t=1 connection (`c=+2`) has been
   shown to possess an explicit parallel spinor — it demonstrably does NOT,
   for the one candidate tested here (`ψ=ḡ(x)ψ₀`). Whether SOME OTHER,
   untested candidate works under `c=+2` remains open.
2. Does **not** resolve H1c/H2/H3 (which of t=0/t=1 is physically selected,
   equations of motion, anomaly cancellation) — untouched, exactly as open.
3. Does **not** imply the abstract-`c`-vs-concrete-`c0` sign discrepancy is a
   "bug" in E2/E9's earlier work — E9's own claim.md already, correctly,
   flagged this exact sign as non-physical and convention-dependent; this
   experiment CONFIRMS that flag was well-founded, using, for the first time,
   an actual concrete realization to check it directly rather than accepting
   it as an unverified caveat.
4. Does **not** verify the generalized product-decoupling formula for the
   full S³×S⁶ operator — out of scope, same as E9/E2/E3.
5. Does **not** establish that Part 2's "mechanical recipe reapplication"
   failure mode generalizes beyond this specific left/right-invariant-frame
   case — flagged as a transferable methodological lesson (see pearl
   candidate below), not as a proven general theorem.

## Pearl-registry candidate

Two transferable insights, both concrete enough to state as falsifiable
lessons for future rounds in this line of work:

1. **Frame-recipe-reapplication trap** (impact_score ~5 — affects HOW future
   connection constructions in this project should be built when switching
   frames): mechanically reapplying a connection-defining recipe (built from
   one frame's self-bracket) to a DIFFERENT frame does not, in general,
   reproduce the restriction of the ALREADY-DEFINED connection to that frame —
   these can be genuinely different connections that happen to share the same
   defining formula PATTERN. Any future round that needs "the same connection,
   expressed in a new frame" should use the change-of-frame/gauge-transform
   route (as Part 3 did here, via the adjoint-action coefficient functions),
   not the mechanical-recipe route (Part 2), if the goal is re-expression
   rather than a genuinely new connection.
2. **Abstract-c vs concrete-c0 sign gap** (impact_score ~4 — narrow, but
   directly relevant to any future experiment in this project that builds an
   actual concrete matrix/manifold realization rather than staying purely
   symbolic): this project's `c` (fixed via `h_H=3` physics calibration) has
   the OPPOSITE sign from the literal geometric bracket constant of the
   concrete Pauli-based `Z_i=i·σ_i` realization (`c0=-2` vs `c=+2`). Already
   flagged by E9 as a non-physical convention artifact; now CONFIRMED
   concretely. Any future computation that mixes "abstract, physics-calibrated
   c" with "directional derivatives on a concrete realization" (as Part 3/4
   necessarily did) must pick ONE consistently and state which, or risk a
   silent sign error exactly like the one that made Part 2's naive `c=+2`
   spinor candidate fail while the `c0=-2` one succeeded.

## Recommended next action

If pursued further: search for a candidate parallel spinor under E9's OWN
`c=+2` convention specifically (the Part-4 candidate `ψ=ḡ(x)ψ₀` was tested
only against `c0=-2` successfully; a DIFFERENT candidate — e.g. `ψ=g(x)ψ₀`
without conjugation, or a candidate built from `ḡ(x)` raised to a different
power, or incorporating an explicit compensating sign/orientation flip in one
frame vector — might restore success under `c=+2` without needing to abandon
this project's own calibration). Until done, do not cite "an explicit
parallel spinor for E9's own calibrated t=1 connection was constructed"
anywhere — only the precise, dual statement given in Part 4 above.

## Check (reproduces this decision)
`python e10_right_invariant_frame.py` →
`verdict.core_part1_pass==true`, `verdict.core_part2_pass==true`,
`verdict.t1_naive_ansatz_fails_symmetrically_to_e9==true`,
`verdict.part3_reveals_frame_ambiguity_discrepancy==true`,
`verdict.explicit_t1_spinor_found_using_concrete_c0==true`,
`verdict.explicit_spinor_fails_under_e9_abstract_c2==true`,
`verdict.label=="PASS_MIRROR_NULL__PLUS_EXPLICIT_T1_SPINOR_UNDER_SIGN_CAVEAT"`.
