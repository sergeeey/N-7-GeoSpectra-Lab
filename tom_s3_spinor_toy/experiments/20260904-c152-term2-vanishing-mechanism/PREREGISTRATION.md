# PRE-REGISTRATION — C152: what mechanism annihilates `Term2` on `SU(3)/T²`?

**Registered:** 2026-09-04, before the discriminating computation.

## L0 gate (EstimandOps, mandatory first step)

**Question type: DESCRIPTIVE.** We characterise a structural property of an
object that already exists and is already built (`Term2` on `SU(3)/T²`, the
geometry certified by C151 Stage 2a's calibration gate). We do not predict a
new observation, and we make no counterfactual claim, so no DAG and no
identifiability check are required. What IS required, and is supplied below:
a pre-committed prediction per hypothesis, a negative control, and a stated
non-interpretation.

## The narrow question — deliberately not "why is the Dirac operator zero"

C151 established, numerically, that the whole invariant-sector block of the
twisted Dirac operator vanishes on `SU(3)/T²`, and that `Term1` and `Term2`
vanish **separately**. The follow-up diagnostic (2026-09-04, same session)
then explained `Term1` completely:

```
domain sits at Σ_odd weights : (−2,1), (1,1), (1,−2)
Σ_even available weights     : (0,0), (−1,2), (−1,−1), (2,−1)
overlap                      : EMPTY
```

`Term1 = (e·∇^Σ)⊗Id_W` leaves `W` untouched, so it must send
`Σ_odd(w)⊗W(−w) → Σ_even(w)⊗W(−w)`; with no shared weight it is forced to
zero. Verified at exactly `0.000e+00`. This is C146's mechanism transplanted
to the flag manifold.

`Term2` is a different matter. It shifts BOTH factors, so that argument does
not apply — and `Term2` is precisely the term that carried the entire nonzero
signal on `S⁶` (C145: Kostant's candidate contributes nothing on the
invariant sector, the whole value comes from the twist connection; C147: that
coefficient is nonzero everywhere in the admissible family except the zero
connection). So:

> **Why does the twist-connection term annihilate `(Σ_odd ⊗ m)^{T²}` on
> `SU(3)/T²`?**

## Three competing hypotheses, fixed before the computation

| | mechanism | what it would mean |
|---|---|---|
| **H1** refined weight selection | after decomposing `Term2` into elementary root shifts, NO admissible path `(σ,w) → (σ',w')` connects the invariant domain to a nonzero target state | the zero is still entirely representation-theoretic |
| **H2** cancellation by NK geometry | admissible paths exist individually, but the coefficients fixed by the structure constants / Nomizu connection / NK `J` cancel exactly | genuine geometric information |
| **H3** stronger annihilator identity | `Term2` admits an algebraic factorisation / Casimir / intertwiner identity giving `Term2·P_inv = 0` without term-by-term cancellation | theorem-level structural zero — the most interesting outcome |

## Pre-committed predictions

- **P1** — if the zero is representation-forced, it SURVIVES a generic
  perturbation of the connection coefficients.
- **P2** — if the zero is geometric, a generic perturbation DESTROYS it.
- **P3** — if a stronger annihilator identity holds, symbolic simplification
  returns `Term2·P_inv ≡ 0` as a matrix identity in free symbols, not merely
  a numerical zero.

P1 and P2 are jointly exhaustive and mutually exclusive for the perturbation
test, so that test cannot come back uninformative. P3 is a strictly stronger
condition than P1 and is checked separately.

## The negative control (this is the load-bearing part)

Build an operator of the SAME tensorial shape `Σ_a A_a^{(Σ)} ⊗ B_a^{(W)}`
but with the geometric coefficient destroyed — replace the connection
coefficients by independent free symbols, or break the nearly-Kähler
relation. Then:

- `Term2|_inv ≠ 0` after perturbation → the zero genuinely uses the special
  geometry (**H2/H3**);
- `Term2|_inv = 0` for arbitrary coefficients → almost certainly a pure
  representation-theoretic selection rule (**H1**).

This is what makes C152 more informative than re-deriving `5×10⁻¹⁷`.

## The cross-space control

Run the SAME elementary-transition analysis on `S⁶ = G₂/SU(3)` under the
same `T²` (the maximal torus of `SU(3)`, common to both spaces — `t² ⊂ su(3)`
and `su(3) ⊂ g₂`, so the language is genuinely uniform, not a re-labelling).
Not "there it is nonzero", but: **which specific root/weight path exists on
`S⁶` and is absent or cancelled on `SU(3)/T²`.**

## ⚠️ HONEST DISCLOSURE — partial loss of blindness on the H1 test

While designing this file I carried out the weight-path enumeration **by
hand, in reasoning, before writing any code**, and reached a preliminary
conclusion about whether admissible paths exist. I am recording that rather
than presenting the scripted enumeration as blind.

What this does and does not compromise:

- The **H1/H2/H3 discrimination via path enumeration** is NOT blind. It is,
  however, a deterministic finite integer computation with no free choices —
  there is nothing in it to fit. The script must reproduce the hand result;
  if it does not, the hand result was wrong and the script wins.
- The **perturbation test (P1/P2)** IS blind. I have not computed it in any
  form, by hand or otherwise.
- The **S⁶ contrast** IS blind. Not computed in any form.
- **P3** IS blind.

## What this round will NOT claim

1. Will NOT reopen C151's pre-registered question. Whether `c`'s holomorphy
   is a nearly-Kähler universality stays OPEN; a vacuum explained is still a
   vacuum.
2. Will NOT treat any outcome as evidence for or against `N_gen = 3`. The
   `3` in the invariant sector's dimension is a `T²`-weight count, nothing
   more (C151's own `does_not_imply`).
3. Will NOT claim a general nearly-Kähler theorem from two spaces.
4. If the mechanism turns out to be H2, that does NOT make the SU(3)/T² zero
   "fine-tuned" — an exact cancellation forced by structure constants is
   still exact.
