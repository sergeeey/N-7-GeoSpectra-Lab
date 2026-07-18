# Round106 — Decision

**Date:** 2026-07-17
**Verdict:** `PARTIAL__LINEARITY_POINT_CONFIRMED__SCALAR_ARGUMENT_WEAKENED_TO_NARROW_FORM__FULL_ITEM7_STILL_OPEN`
(skeptic verdict on Part 3, context-asymmetric review)
**Go/no-go:** does NOT complete Codex/round105's item 7 — genuinely
harder than "a finite symbolic calculation" turned out to be, on this
attempt. Two real, tool-verified, narrower results survive.

## Part 1 [VERIFIED-tool, uncontested]: `b(x) = Ad(g(x)⁻¹)` exactly

`Σ_j b_i^j(x)Z_j = g(x)⁻¹Z_i g(x)` confirmed for all `i=1,2,3`,
symbolically exact. Makes explicit what round80's construction implied
but never stated: `b(x)` is literally the adjoint-representation matrix
of the SAME group element `g(x)` this whole project already uses.

## Part 2 [VERIFIED, algebraic identity, uncontested]: round101's naive
computation IS correct, for what it computes

`Ω_i^R(t)(x):=Σ_jb_i^j(x)Ω_j(t)` is EXACTLY `ω^t(Z_i^R)` — a direct
consequence of `ω^t` being LINEAR in its vector argument (any 1-form is,
at each point), combined with round80's own `Z_i^R=Σ_jb_i^j(x)Z_j^L`.
Round101's finding that this is `x`-dependent is therefore not "missing a
term" at THIS step — it's the honest answer to "what is `ω^t` evaluated
at `Z_i^R`." **The genuine gap is a different, so-far-unaddressed step:
how `ι` acts on the SPINOR FIBER itself** (which spinors are "parallel"/
"constant" in which frame) — not `ω^t`'s own linearity.

## Part 3 — original claim, and the skeptic's correction

**Original claim:** since `H=(3c/2)·I₂` is scalar (E2's own established
fact, re-verified here), `D^t(ψ)=t·(3c/2)·ψ` on constant spinors is pure
scalar multiplication, and "no spin-lift conjugation of any kind" can
relate the `t` and `1-t` scalar eigenvalues except at `t=1/2`.

**Skeptic (Step 8a, context-asymmetric) verdict: WEAKENED**, three
concerns, all accepted here:

1. **The `D^t=`(derivative part)`+`(algebraic `H` part) split is itself
   frame-dependent** — conjugating `H` alone in isolation, while ignoring
   that the derivative piece `Σ_iZ_iZ_i(ψ)` transforms differently under
   the same conjugation, doesn't settle the FULL operator's behavior.
2. **["Constant spinor" is a frame-dependent notion — the real
   problem.]** If `ψ` is constant in the L-frame, `S(x)⁻¹ψ` is generically
   NOT constant in a DIFFERENT, `x`-dependent frame `S`. Since `ι`
   induces exactly such a point-dependent twist (`dι=-Ad(g⁻¹)`), **the
   "constant-spinor subspace" being tested is not even the same object
   across the L-frame and the `ι`-transformed frame** — meaning this
   whole approach may answer a narrower, frame-bound question, not the
   genuinely relevant one (which lives on the full `L²` spectrum, not
   the `x`-independent-coefficient subspace specifically).
3. **Overclaim in scope:** "no conjugation mechanism" was stated as "no
   mechanism of ANY kind" — a diffeomorphism-induced pullback (`ι*`) is a
   chain-rule/pushforward operation, not restricted to pure algebraic
   conjugation; kernels/spectra CAN match under a pullback without any
   conjugation-based argument existing to show it.

**What survives, in the skeptic's own words:** *"a globally CONSTANT
(`x`-independent) conjugation `S` cannot map scalar `t·(3c/2)` to
`(1-t)·(3c/2)` except at `t=1/2`"* — true, narrow, worth keeping, with
the "of any kind" language dropped and the frame-dependence caveat
(point 2) stated explicitly alongside it.

## Applying the pre-registered criteria (claim.md Section 3)

**PARTIAL** — Parts 1-2 are genuine, uncontested sharpenings (what the
naive computation actually establishes, and why it's not itself the
gap). Part 3 survives only in a narrowed form. **Codex's own
characterization of item 7 as "a finite symbolic calculation" was
optimistic** — the genuine remaining step (constructing `ι`'s actual
action on the spinor fiber, i.e. which spinors count as parallel in
which frame) is exactly the kind of subtlety this session has
repeatedly found requires real care, not a quick substitution.

## Kill Analysis

- **What this kills:** the overclaimed "no spin-lift of any kind" version
  of the scalar argument; Codex's implicit framing of item 7 as
  quick/finite (it is not, on this attempt).
- **What this does NOT kill:** round101's own `BLOCKED` verdict — Parts
  1-2 here EXPLAIN and sharpen why it's blocked (the linearity point),
  they don't overturn it.
- **What survives, sharper than before, across THREE rounds now (101,
  105, 106):** the precise location of the remaining gap is now stated
  three independent ways that all agree: round101 ("inhomogeneous term
  needed"), Codex/round105 ("construct the explicit spin lift"), and this
  round ("how `ι` acts on the spinor fiber — which spinors are constant
  in which frame"). This convergence across two different models and
  three separate attempts is itself informative: the gap is real and
  consistently located, not an artifact of any one approach.

## Session-level note (third self-correction after skeptic review this
session)

Rounds 102, 103, and now 106 have each required a skeptic-driven
correction to an initially-overreaching claim in this exact research
territory (spin lifts, connection pullbacks, category distinctions
between algebra/group/holonomy/frame). Worth stating plainly: this
specific corner of differential geometry (equivariance of spin
connections under isometries with a non-trivial fixed-point structure)
is genuinely subtle, and this session's mandatory pre-registered
escalation discipline has caught a real error each time it was invoked
here — a good argument for continuing to require it for any future round
touching this same territory.

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Construct `ι`'s actual spinor-fiber action | Determine the correct `Spin`-level lift of `ι` (an orientation-REVERSING isometry, `det(J)=-1`, round80 Section A — likely requires `Pin(3)`, not `Spin(3)`, adding a further subtlety not addressed in rounds 101/106 either) and how it acts on the L-frame's spinor trivialization specifically |
| Reformulate on the full `L²` spectrum, not the constant-spinor subspace | Per skeptic point 2 — a substantially larger computation than anything attempted in rounds 101/106 |

## What this does NOT mean

Does not resolve H1c, KT-8, or E12/E13's multiplicity gap. Does not
affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
`safe_for_runtime=False`. Does not modify `preprint.tex` or any prior
experiment folder.

## Check (reproduces this decision)

```
cd experiments/20260717-round106-codex-item7-spin-connection-followup
python e29_spin_pullback_scalar_check.py
```
