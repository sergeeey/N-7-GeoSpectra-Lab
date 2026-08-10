# Test (a) — Lemma B's degradation IS computable, and it goes the wrong way

**Date:** 2026-08-10
**Verdict:** `DEGRADATION_IS_DISCRETE_AND_COMPUTABLE__BUT_IT_LOOSENS_THE_BOUND`
**Runs:** test (a) from the consortium run — *"is there a quantitative Lemma B
with a margin under `G₂`-breaking?"*

## The hope, and the result

The hope was that Lemma B might survive `G₂`-breaking with a margin, dissolving
OB4's dependence on unpublished external input. **It does not. The opposite.**

Lemma B is a **singlet count** (`g74a_lichnerowicz.py:129-151`): `ker(D⊗S⁻)` is
the `G₂`-invariant subspace, so by Schur `dim ker` = multiplicity of the trivial
`G₂` rep = 1 per channel. Under breaking `G₂ → H` the bound becomes a count of
**`H`-singlets** — a joint-kernel dimension, computable from matrices this repo
already has.

## Result [VERIFIED-numpy], reusing G102's own generators

| module | `g₂`-singlets | `su(3)`-singlets | change |
|---|---|---|---|
| `𝕆 = ℝ⁸` | **1** | **2** | **+1** |
| the `7` (imaginary octonions) | **0** | **1** | **+1** |

Matches the standard branching `7 = 3 ⊕ 3̄ ⊕ 1` — obtained here as a computed
kernel dimension, not cited. `dim Der(𝕆) = 14`, `dim stab(e₁) = 8`, both
reproduced from G102's machinery.

**Negative control passes:** five random 8-element subsets of `so(8)` give
singlet counts `[0, 0, 2, 0, 0]` — not all matching `su(3)`'s 2, so the method
is measuring `su(3)`'s structure and not merely the size of the generating set.

## What this means, stated against the hope rather than for it

**G74A's wording is right and this sharpens it, unhelpfully.** "Lemma B does not
degrade *gradually*" — correct: the degradation is **discrete**. But discrete is
not the same as unknowable, and the number is now known: breaking `G₂ → SU(3)`
adds **one** singlet on the relevant modules.

**And an added singlet loosens the bound.** `dim ker ≤ 1` becomes `dim ker ≤ 2`.
That is the wrong direction for OB4: the `G₂`-breaking both rank-4 candidates
require does not merely make Lemma B's *argument* inapplicable — it
quantifiably **costs** the uniqueness Lemma B was supplying, and uniqueness is
what `N_gen = 3` per channel rests on.

**So OB4's dependence on Tom is NOT dissolved.** It is made precise: any
candidate requiring `G₂ → SU(3)` must independently exclude the extra singlet,
and "extra singlet" now has a number attached instead of being a vague worry.

## What this does NOT establish

1. **Does not show the extra singlet is occupied.** A singlet is a *slot*; whether
   a zero mode sits in it is Lemma A's (Lichnerowicz) question, which is separate
   and metric-dependent. This bounds how much the Schur argument can loosen, not
   what actually happens.
2. **Does not compute the count for the OB4 candidates' actual subgroups.** Both
   `SO(4)×SO(4)` and `su(3)⊕u(1)⊕u(1)` lie partly *outside* `g₂`; the relevant
   `H` is the intersection, which round125 showed is a non-generic 3-dim abelian
   `u(1)³`. That count is the natural next step and is **not** done here.
3. **Does not touch OB4's other half** — whether the structure acts globally on
   the compactification.
4. Does not revisit Lemma A, whose `8/45` safety factor already carries its own
   quantitative margin and is unaffected.

## Next

Compute the singlet count for `H = g₂ ∩ (candidate)`, i.e. for round125's
`u(1)³`. If that count is *also* 1, the candidates survive Lemma B after all and
OB4's blocker genuinely narrows. If it is larger, the cost is explicit and the
candidates need an independent exclusion argument. Either way the question is now
a finite computation rather than a wait.

## Check

```
python experiments/20260810-lemmab-quantitative/lemmab_margin.py
```
Expect `dim g₂ = 14`, `dim su(3) = 8`; singlets `1 → 2` on `𝕆` and `0 → 1` on the
`7`; control not uniformly matching.
