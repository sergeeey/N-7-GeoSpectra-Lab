# Step 5 (scoped): does the S³ factor's own candidate zero-mode mechanism ever stay multiplicity-safe?

**Experiment id:** `20260810-step5-s3-torsion-multiplicity-safety`
**Date:** 2026-08-10 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** E2 (`20260717-round67-e2-s3-torsion-deformation`), E3
(`20260717-round68-e3-full-operator-torsion-deformed`), OB1 (PARKED)

---

## Scope, agreed with the user before starting

The user's original step 5 asked to check `ker D_{S³×S⁶}` and the full 4D fermion content,
with S³ constrained to supply geometry/spinor structure only, never multiplicity. Taken
literally this collides directly with **OB1** ("no zero mode for the full S³×S⁶ Dirac
operator"), which this project already investigated exhaustively (rounds 62–117) and marked
`PARKED — REOPEN ONLY ON NEW EXTERNAL INPUT`; C58 (this session) already confirmed the C11
arc doesn't meet any of OB1's four reopen conditions. Resolving *which* torsion value `t` is
physically correct is exactly OB1's own open problem and is explicitly out of scope here.

**Agreed narrower question (does not touch OB1's gate):** for the one candidate mechanism
this project already has on record for giving the S³ factor a nonzero kernel at all (E2's
torsion-deformed family `D^t`, Agricola/Kostant construction) — at every `t` where a zero
mode appears, is the kernel dimension exactly 1 (safe), or could it exceed 1 (multiplying
generations regardless of which crossing nature might select)? This is a closed, bounded
question about an already-fully-determined mathematical object, not a selection of `t`.

## Pre-work check — the multiplicity gap is already on record; this round's new content is narrower

E2 computed the *crossing values* `t*` where some eigenvalue of `D^t` passes through zero
(`{-2/3,-1/3,0,1,4/3,5/3}` for levels `n=0,1,2`) but did not itself report the **dimension** of
the resulting kernel. **round116 (`20260717-round116-minimal-crossing-pair-structure`) already
caught exactly this**, via skeptic review: its own Finding 2 states the `(n,σ)` parametrization
"silently drops the `(n+1)(n+2)` eigenspace multiplicity," gives the same numbers this round
would otherwise re-derive (`t=0,1`: multiplicity 2 each; `t=-1/3,4/3`: multiplicity 6 each), and
is logged as a pearl (`pearl_registry/INDEX.md`, 2026-07-17) whose trigger is "any future round
that invokes a spectral-flow-type integer for this project's `D^t` family." Round116 itself
states, without justification, that this "does NOT affect `N_gen=3`" (its own item 3).

**What is genuinely new here, not already covered:** (a) an explicit, direct verification — not
a citation of the abstract multiplicity formula, but an actual constructed 2×2 matrix, shown to
be exactly scalar and exactly zero at the crossing — and (b) the actual consequence round116
asserted but never worked out: connecting the multiplicity fact to OB1-resolution safety via
E3's product-decoupling identity (`ker(D_full)=ker(D_S6)⊗ker(D_S3)`), which neither E2/E3 nor
round116 addressed. Round116's own trigger (a formal spectral-flow computation) has not fired;
this round approaches the same underlying fact from a different angle its trigger didn't
anticipate.

## The claim under test

> **C64.** `H` (Kostant's cubic element) acts as `h_H · Identity` on S³'s ENTIRE spinor
> bundle (E2's own step 2, `omega_ok`, is a scalar times the identity — proven for the algebra
> element itself, not level-specific). Since `D^{1/2}` (Levi-Civita) is, by construction, exactly
> `σ(n+3/2)·Identity` restricted to each `(n+1)(n+2)`-dimensional eigenspace, and `D^t = D^{1/2} +
> (t−1/2)·H`, the shifted operator `D^t` restricted to that SAME eigenspace is
> `[σ(n+3/2)+(t−1/2)h_H]·Identity` — still exactly scalar. **Consequently, at every crossing
> `t*_n`, the ENTIRE `(n+1)(n+2)`-dimensional eigenspace hits zero simultaneously — dim
> ker(D_S3(t*)) = (n+1)(n+2) ≥ 2 for every crossing found by E2, never 1.** Via the
> product-decoupling identity (E3, `ker(D_full)=ker(D_S6)⊗ker(D_S3)`), this means E2/E3's own
> candidate mechanism for giving the full operator a nonzero kernel would multiply the
> generation count by at least 2 at its cheapest crossing (n=0) — the S³ factor is NOT
> multiplicity-safe under this specific, already-on-record mechanism.

**Falsifier, fixed in advance:** if an explicit construction of the n=0 level's `D^t` operator
(2-dimensional, directly reusing E2's own Clifford/`H` machinery) does NOT become the exact
zero matrix at `t=0`, but instead has only one zero eigenvalue (rank 1, not rank 0), the claim
is refuted and the "uniform scalar shift ⟹ full-eigenspace crossing" argument has a hole.

## Predictions, recorded before running

| # | Prediction |
|---|---|
| **P1 (re-verify E2's own crux fact)** | `H`'s image on the n=0 (2-dim) spinor space is exactly `h_H·I₂`, reproducing E2's own `step2_omega_ok=True` directly (own re-run of the same construction, spot-check discipline) |
| **P2 (the new question)** | the explicit n=0-level `D^t` matrix, built directly from E2's own Clifford generators and calibrated `h_H`, is exactly `[3/2+(t−1/2)·3]·I₂` — a genuinely scalar 2×2 matrix for all `t`, not merely diagonal with two different entries |
| **P3 (the consequence)** | at `t=0` (the cheapest known crossing), this 2×2 matrix is the exact **zero matrix** (both eigenvalues 0, not one) — `rank=0`, `dim ker=2` |
| **P4 (re-cites round116, not new)** | the same scalar-shift structure applies to every `n` (E2's own construction: `H` is level-independent), so the n=1 crossings give multiplicity 6 and n=2 crossings give multiplicity 12 — this is round116's own already-established fact (its Finding 2), reported here by direct formula `(n+1)(n+2)` for completeness, not re-derived independently |

## What this cannot show

- Does **not** resolve OB1 — does not select a physical `t`, does not claim the torsion
  mechanism is the one nature uses. It only characterizes a property of an already-published
  candidate mechanism.
- Does **not** show `N_gen=3` is threatened. The currently-relevant construction is the
  Levi-Civita case (`t=1/2`), which E2/E3 already establish gives `dim ker(D_S3)=0` (not 2) —
  i.e. `N_gen=3`'s own derivation does not currently rely on any torsion-deformed crossing at
  all. This round's finding is a caveat for OB1's *future* record (if the torsion escape route
  is ever pursued further), not a new problem for the headline result as it currently stands.
- Does **not** rule out that some ADDITIONAL structure (chirality projection, gauge selection,
  a different combination of `n`-levels) could cut the `(n+1)(n+2)` multiplicity back down to 1
  in a fuller construction — only that the bare S³-factor-alone mechanism, as E2/E3 left it,
  does not do so by itself.
- Does **not** build the full `D_{S3×S6}` product operator — stays at the S³-factor level, per
  E2/E3's own explicit scope limit, extended only by the multiplicity question.

## kill_criterion

C64 stands if P1–P3 all pass as predicted (explicit n=0 verification). Refuted if the explicit
n=0 matrix construction shows the crossing has rank 1 (not 0) at `t=0`.
