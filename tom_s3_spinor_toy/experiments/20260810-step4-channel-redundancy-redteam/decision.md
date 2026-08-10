# decision — step 4 red-team: the three channels are provably not redundant

## Verdict

`THREE_CHANNELS_PROVABLY_NOT_REDUNDANT` → **C63 SUPPORTED.**
**Date:** 2026-08-10 · L0: descriptive · ruff clean · `results_step4.json` persisted.

---

## What was checked and how

Re-verified G102's own S5 computation directly (`Hom_so8(vec,sp)`, `Hom_so8(vec,sm)`,
`Hom_so8(sp,sm)`), then went further: built the "coincidental" `su(3)`-level
identification `Φ` between two channels explicitly (an actual 8×8 matrix, not just an
abstract Hom-space dimension), and tested it against both `su(3)` itself and a generic
`so(8)` element.

## Results, all [VERIFIED-numpy]

| check | predicted | found |
|---|---|---|
| **P1** `Hom_so8` off-diagonal (`vec-sp`, `vec-sm`, `sp-sm`) | `(0,0,0)` | **`(0,0,0)`** ✓ — reproduces G102's own S5 independently |
| positive control `Hom_so8(vec,vec)` | 1 (Schur, self-map is scalar) | **1** ✓ |
| **P3** does the constructed `Φ` intertwine `su(3)` itself? | residual ~0 | **5.13e-16** ✓ — `Φ` is genuinely `su(3)`-equivariant, as it must be by construction |
| **P2** does `Φ` intertwine a **generic** `so(8)` element? | large residual (fails) | **3.22** (element norm 2.71) ✓ — fails decisively, not marginally |

## Interpretation

The three triality channels are **provably inequivalent as `Spin(8)` representations**
(`Hom_so8` off-diagonal `=0`, Schur's lemma, re-confirmed directly). A change of basis
making them "look identical" **does exist** — it is possible precisely because the
channels share identical `su(3)` content — but this round makes explicit, with an actual
constructed matrix rather than an abstract dimension count, exactly why that identification
is not a genuine symmetry: it intertwines `su(3)` (or more generally `g2`, the subalgebra
where the channels are indistinguishable) essentially exactly, but fails badly — by a
factor of order 1, not a small perturbation — for a generic element of the ambient
`so(8)`. The "redundancy" is confined entirely to the restricted `su(3)`/`g2` view; it does
not survive contact with the full `Spin(8)` structure the compactification's fiber content
is built from.

**Answer to the user's red-team question:** no — "3" is not a hidden "1" counted three
times. Any basis change that collapses the three channels together necessarily discards
the `Spin(8)`-representation-theoretic distinction between them, which is real and rigid
(Schur's lemma forces it), not a bookkeeping artifact removable by a clever relabeling.

## Kill Analysis

**Killed:** the specific worry that `N_gen=3` might be triple-counting one physical
degree of freedom, made concrete rather than left as an informal aside.

**Not newly established, credited to prior work:** the crux fact (`Hom_so8` off-diagonal
`=0`) was already computed and PASSING in G102 (2026-07-05) and already reasoned through
qualitatively in a pearl_registry entry (2026-07-15, in the course of a different
investigation). This round's contribution is (a) an independent direct re-verification,
per this project's spot-check discipline, since the fact is now load-bearing for a new
claim, and (b) the first **concrete, explicit construction** of the "coincidental" `Φ`
and demonstration of its failure mode, rather than leaving the argument at the level of
"if `Φ` were `Spin(8)`-equivariant it would have to vanish by Schur."

## What this does NOT show

1. Does **not** newly discover the `Spin(8)`-inequivalence fact — reused from G102 (S5),
   re-verified not re-derived.
2. Does **not** establish that the compactification's actual physical fiber structure
   realizes the full `Spin(8)` action — that is `OB11(iii)`'s harder, still-open half
   (gates 2-6 of `C_G67C3_THIRD_CHANNEL`). This round shows the distinction, *if* present,
   cannot be undone by relabeling — not that the distinction is physically realized.
3. Nothing about `N_gen=3`'s CONDITIONAL status changes — this defends against one
   specific way it could have been undermined; it does not newly establish the headline
   result.

## Check (reproduces this derivation)

```
cd experiments/20260810-step4-channel-redundancy-redteam
python step4_channel_redundancy.py
```
Expect: `Hom_so8` off-diagonal `(0,0,0)`, diagonal control `1`, `su(3)` residual `~1e-15`,
generic residual `~3.2`, `VERDICT: THREE_CHANNELS_PROVABLY_NOT_REDUNDANT`.
