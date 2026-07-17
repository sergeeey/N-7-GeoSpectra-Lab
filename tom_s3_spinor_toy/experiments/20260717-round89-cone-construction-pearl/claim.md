# E19 (round89) — Claim: does this project's own ∇^t/∇^{LC} connection-difference
# formula turn "∇^t-parallel" into an exact AHL2023 Killing-spinor equation?

**Date:** 2026-07-17
**FL tier:** [x] Full (research claim; methodology per project CLAUDE.md)
**Question type:** [x] descriptive [ ] predictive [ ] causal

Descriptive: for the naturally-reductive one-parameter connection family `∇^t` on
`S³=SU(2)` (Agricola, arXiv:math/0202094 — the family this project's own
`t`-parameter already IS, per `preprint.tex:1470`), does substituting this
project's own ALREADY-ESTABLISHED `∇^t`-parallel spinors (at `t=0` and `t=1`)
into the ALREADY-ESTABLISHED connection-difference formula between `∇^t` and
the Levi-Civita connection `∇^{LC}=∇^{t=1/2}` force each of them to satisfy the
Riemannian Killing-spinor equation `∇^{LC}_X ψ = λ·X·ψ` for a computable scalar
`λ`, and if so, does the resulting pair `(λ(0), λ(1))` match AHL2023's own
stated Killing constants for round `S³=SU(2)` (`λ=±1/2`, Corollary 3.14 /
p.48, reused via `experiments/20260717-round86-parent-action-discriminator/
decision.md:129-141`)?

This is NOT the cone-construction check round86 flagged as unattempted
(`decision.md:529-531`) — it is a more direct candidate bridge, using only
formulas this project has ALREADY derived and tool-verified (E9/E10's own
`Ω_i(t)=-(tc/2)Z_i` spin-lift formula), evaluated at the ALREADY-established
Levi-Civita point `t=1/2` (E7, `decision.md:21,74,119,155,159,191-192`;
`claim.md:24-25,101,104,126`), rather than importing new cone-manifold
machinery.

## Stakes
Internal-only (mechanical cross-check of a pearl candidate flagged, not
attempted, in E18/round86 `decision.md:517-544`). Not promoted to
`preprint.tex` here. Does not touch `N_gen=3`, `KT-8`, H1c, or any of this
project's headline results.

## Background (established, not re-derived here except where explicitly marked "fresh")

- **Ω_i(t) formula.** `Ω_i(t) = -(tc/2)·Z_i`, the spin lift of `Γ^k_{ij}(t) =
  t·c·ε_{ijk}` (`∇^t_{Z_i}Z_j = t[Z_i,Z_j]`), derived and cross-checked against
  Agricola's `H=(3c/2)ω` in `experiments/20260717-round73-e9-explicit-parallel-
  spinor/e9_explicit_parallel_spinor.py:171-178` (`spin_connection_Omega`),
  `decision.md:13-30`. `Z_i=i·σ_i`, `{Z_i,Z_j}=-2δ_ij`
  (`e9_explicit_parallel_spinor.py:90-99`).
- **`t=0`/`t=1` = canonical/anticanonical, `t=1/2` = Levi-Civita.**
  `experiments/20260717-round72-e7-t-selection-principle/decision.md:155-161`
  ("t=0 is the 'canonical connection' ∇⁰ — by the Ambrose-Singer theorem... t=1
  is what Agricola names the 'anticanonical connection'... PDF p.5"),
  `decision.md:191-192` (`R_at_t=1/2_LeviCivita_nonzero_as_expected = true` —
  a genuine sanity check that `t=1/2` is curved, i.e. the actual round-sphere
  Levi-Civita connection, not a degenerate presentation), `claim.md:24-25,101,
  104,126` (repeats the same identification, citing Agricola's own naming).
- **Two `c` conventions, both legitimate, not interchangeable.**
  `CONVENTION_TABLE.md` §2/§4: abstract `c=+2` (physics-calibrated via
  `h_H=3`, E2/E9) vs concrete `c0=-2` (literal Pauli/quaternion bracket
  constant, found in `experiments/20260717-round76-e9followup-right-invariant-
  frame/e10_right_invariant_frame.py`, `find_structure_constant`).
- **`t=0` parallel spinor.** ANY constant left-invariant `ψ=(a,b)∈ℂ²`
  satisfies `∇^0_{Z_i}ψ=0` for all `i`, unconditionally (any `c`) — E9
  `decision.md:44-62`.
- **`t=1` parallel spinor.** `ψ(x)=ḡ(x)·ψ₀` (quaternion-conjugate profile)
  satisfies `∇^1_{Z_i}ψ=0` for all `i`, **established ONLY under `c0=-2`**
  (fails under the abstract `c=+2`) — `e10_right_invariant_frame.py:548-614`
  (`run_part4`), `decision.md:129-168`. `CONVENTION_TABLE.md` §5: "`t=1`↔
  right-invariant frame (established only under `c0=-2`)".
- **AHL2023's own stated Killing constants.** `experiments/20260717-round86-
  parent-action-discriminator/decision.md:129-141`: Corollary 3.14 (general,
  parametrized family `g_{a,b}`, `a=2b/n`): "we recover the usual Sasakian
  Killing spinors for the constants `1/2,-1/2` (or `1/2,1/2`, depending on
  `n`)"; p.48 (§6, case II, `G=SU(2)=Sp(1)`, i.e. exactly `n=1`, the
  project's own `S³` case): "the round metric `g_{a,b}|_{a=b=1/2}` admits **a
  PAIR of invariant Killing spinors for THE constant 1/2**" (singular
  constant — both basis spinors share the SAME sign, for this specific
  `n=1` case, per the "or 1/2,1/2, depending on n" clause of Corollary 3.14).
  This is reused directly, by citation, from round86's own
  `[VERIFIED-tool: pdftotext extraction]` reading — not re-extracted from the
  PDF in this experiment.

## Claim (falsifiable)

**Part A (the bridge, fresh derivation + fresh symbolic verification this round).**
Define `Ω_i^{LC} := Ω_i(t)|_{t=1/2}` (this project's own spin-lift formula,
evaluated at the already-established Levi-Civita point). Then:

1. The torsion of `∇^t` in this frame, `T^k_{ij}(t) = Γ^k_{ij}(t)-Γ^k_{ji}(t)-
   c·ε_{ijk}`, equals `c·(2t-1)·ε_{ijk}` exactly, vanishing **iff** `t=1/2` —
   a fresh, direct confirmation (not merely citing E7's curvature-based
   argument) that `t=1/2` is the torsion-free member of the family, i.e.
   genuinely `∇^{LC}` in the technical sense (torsion-free + metric-compatible
   ⟹ unique ⟹ Levi-Civita), not merely "the value E7 happened to call LC."
2. `Ω_i(t) - Ω_i^{LC} = (c/2)(t-1/2)·Z_i` **exactly**, symbolic in `t,c` (a
   trivial-looking but load-bearing algebraic identity, to be verified by
   sympy, not asserted).
3. **If** a spinor field `ψ` satisfies `∇^t_{Z_i}ψ=0` for all `i` (i.e. is
   `∇^t`-parallel, in whichever trivialization this project has already
   established that parallelism), **then** `∇^{LC}_{Z_i}ψ = λ(t)·Z_i·ψ` for
   all `i`, with `λ(t) = (c/2)(t-1/2)` — i.e. it is an EXACT Riemannian
   Killing spinor for `∇^{LC}` with Killing constant `λ(t)`. This is claimed
   to hold for BOTH this project's own `t=0` constant spinor (any `c`) and its
   own `t=1` `ψ=ḡ(x)ψ₀` spinor (under `c=c0=-2`, the only convention in which
   it is established parallel).

**Part B (comparison to AHL2023 — the actual question this experiment exists to answer).**

4. Using a single, self-consistent `c=c0=-2` throughout (forced by the fact
   that the `t=1` parallel spinor is established ONLY under this value): does
   `(λ(0),λ(1))` equal `(+1/2,-1/2)` in magnitude (`|λ(0)|=|λ(1)|=1/2`
   exactly, no extra normalization factor needed)?
5. **Sign structure — the sharper, previously-unasked question.** Since
   `λ(t)=(c/2)(t-1/2)` is LINEAR and HOMOGENEOUS in `t-1/2`, it is a
   structural, convention-independent fact of this project's OWN formula that
   `λ(1) = -λ(0)` **for every value of `c`** (not merely at `c=±2`) — i.e.
   this project's `t=0`/`t=1` pair is FORCED to be an OPPOSITE-sign Killing
   pair. Does this match AHL2023's own `n=1`-SPECIFIC statement (p.48: "a PAIR
   ... for THE constant 1/2" — a SAME-sign pair), or only the general,
   other-`n` Corollary 3.14 wording ("constants 1/2,-1/2")?

## Kill criterion (MANDATORY — filled BEFORE running)

| Kill condition | Threshold |
|---|---|
| Torsion does NOT vanish uniquely at `t=1/2` | `torsion_zero_iff_t_half == False` — would contradict E7's own established fact and this experiment's own "fresh derivation" claim; the whole `t=1/2=LC` premise would need re-examination |
| `Ω_i(t)-Ω_i^{LC}` is NOT exactly `(c/2)(t-1/2)Z_i` | `diff_formula_matches == False` — the bridge formula itself is wrong; stop, do not proceed to λ computation |
| `t=0` spinor does NOT satisfy the derived Killing equation with a SINGLE consistent `λ` across `i=1,2,3` and across generic `(a,b)` | `t0_killing_check == False` — Part A's core claim fails at `t=0` |
| `t=1` spinor (under `c0=-2`) does NOT satisfy the derived Killing equation with a SINGLE consistent `λ` across `i=1,2,3` and across generic `x0..x3,a_,b_` | `t1_killing_check == False` — Part A's core claim fails at `t=1` |
| `|λ(0)|≠1/2` or `|λ(1)|≠1/2` (using `c=c0=-2`) | `magnitudes_match_half == False` — no clean match to AHL2023 at all; report PASS-bridge/FAIL-comparison |
| `λ(1)≠-λ(0)` for generic symbolic `c` | would contradict the linear-homogeneous structure of `Ω_i(t)`, i.e. an arithmetic error somewhere upstream — re-check | 

**Pre-registered verdict logic:**
- If Part A's bridge checks (torsion, diff-formula, both Killing checks) all
  FAIL → **FAIL** overall (round86's "wrong parameter axis" dismissal stands,
  now for a checked reason instead of an unattempted flag).
- If Part A's bridge checks all PASS, magnitudes match `1/2` exactly, AND the
  sign structure matches AHL2023's `n=1`-specific same-sign p.48 statement →
  **PASS** (round86's dismissal was wrong; a genuine, structural coexistence
  fact transfers).
- If Part A's bridge checks all PASS and magnitudes match `1/2` exactly, BUT
  the sign structure is the STRUCTURALLY-FORCED opposite-sign pair (not
  matching AHL2023's n=1-specific same-sign statement, though consistent with
  the general Corollary 3.14 "other n" wording) → **PARTIAL**, with the
  specific named gap being: "this project's `t=0`/`t=1` pair is an
  opposite-sign Killing pair; AHL2023's own `S³`-specific coexistence fact
  (p.48) is a same-sign pair — these are different mathematical objects, and
  the bridge constructed here does not transfer AHL2023's specific
  `n=1` coexistence argument, even though it does transfer the bare `±1/2`
  magnitude."

## What this does NOT mean (pre-registered)

1. Does **not** re-derive or challenge E7's `t=1/2=LC` identification, E9's
   `Ω_i(t)` formula, or round76's `t=1` explicit spinor — all reused exactly
   as established.
2. A PARTIAL or FAIL verdict here does **not** reopen or re-litigate E15's
   `NULL_OMEGA_PROPORTIONAL_TO_IDENTITY` result (Clifford-volume-element
   grading) — a completely different candidate mechanism, untouched by this
   experiment.
3. Does **not** resolve E18/round86's parent-action gap regardless of
   outcome — even a full PASS here would only supply a *mathematical*
   coexistence fact (both `t=0,1` correspond to Killing spinors that
   AHL2023 shows must coexist on the round metric), not a *physical* action
   with independent fields and equations of motion requiring both `t=0` and
   `t=1` sectors to appear in a 13D compactification. Section on this is
   mandatory in `decision.md` regardless of which verdict is reached.
4. Does **not** independently re-verify AHL2023's own normalization
   convention against this project's Clifford normalization from the PDF
   itself beyond what round86 already extracted — the magnitude match is
   corroborated (not independently reproven) by this project's own
   pre-existing `n=0` Dirac eigenvalue calibration (`h_H=3`, matching the
   standard literature value `3/2` for the unit round `S³` Dirac spectrum,
   [DOCS]-level, Hitchin/Friedrich), which is flagged as [INFERRED] support,
   not a fresh independent verification.

## Assumptions (status)

| Assumption | Status |
|---|---|
| `∇^t_{Z_i}ψ = Z_i(ψ) + Ω_i(t)ψ` holds for ANY spinor field `ψ` (not just constant ones), in the fixed left-invariant trivialization | [DOCS/standard] — this is what "connection 1-form in a trivialization" means; used without further re-derivation, same as E9/E10's own usage |
| `t=1/2` genuinely IS `∇^{LC}` (torsion-free + metric-compatible ⟹ unique) | [VERIFIED-tool, E7, reused] + fresh torsion re-derivation this round |
| This project's `Z_i`-normalization corresponds to the SAME "unit round `S³`" convention AHL2023 uses (needed for the numeric value `1/2`, not just the functional FORM of the Killing equation, to match) | [INFERRED] — supported by this project's own `n=0` Dirac eigenvalue `=3/2` calibration matching the standard literature value for unit round `S³` (Hitchin), NOT independently re-derived from AHL2023's PDF text in this experiment |
| Round86's own quoted AHL2023 text (Corollary 3.14, p.48) is transcribed correctly | [VERIFIED-tool, reused from round86's own `pdftotext` extraction] — not re-extracted here |

## Check
`python e19_killing_bridge_check.py` →
`verdict.torsion_zero_iff_t_half == true`,
`verdict.diff_formula_matches == true`,
`verdict.t0_killing_check == true`,
`verdict.t1_killing_check == true`,
`verdict.lambda0_magnitude_is_half == true`,
`verdict.lambda1_magnitude_is_half == true`,
`verdict.lambda1_equals_minus_lambda0_symbolic == true`,
`verdict.label` reports one of
`PASS_SAME_SIGN_MATCH` / `PARTIAL_OPPOSITE_SIGN_STRUCTURAL` / `FAIL_BRIDGE_BROKEN`.
