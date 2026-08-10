# decision — OB11(iii): SU(3) matter action is triality-fixed, confirmed by an independent construction

## Verdict

`SU3_TRIALITY_FIXED_CONFIRMED_INDEPENDENT_CONSTRUCTION` → **C62 (as scoped) SUPPORTED.**
**Date:** 2026-08-10 · L0: descriptive · ruff clean · `results_ob11iii.json` persisted.

---

## What was checked and how

Reused `triality_so4xso4_invariance.py`'s own self-contained octonion table, `g2` basis, and
`solve_triality_partners` (Baez's genuine trilinear covariance construction) unmodified.
Extracted `su(3)` from THIS file's own `g2` (stabilizer of an imaginary octonion unit) and ran
every one of its 8 generators through `solve_triality_partners`, checking whether the returned
partner actions `b` (on `S+`) and `c` (on `S-`) equal the same matrix `a` used on `V`.

## A real bug, caught and fixed before accepting the verdict

The first run used `point_index=0` (stabilizer of the octonion **real unit**) and returned
`dim(su3)=7`, not the predicted 8 — refuting P1. Before treating this as a genuine surprise
(P3-style, forcing reconciliation with the classical `g2=Fix(triality)` fact), the discrepancy
was traced to its actual cause: **every derivation kills the algebra's unit automatically**
(`D(1)=D(1·1)=D(1)·1+1·D(1)=2D(1) ⟹ D(1)=0`), so "stabilizing the real unit" does not select
`su(3)` at all — it's not the mathematically meaningful point to stabilize. G102's own
`stabilizer_basis` already encodes this correctly (`point_index: int = 1`, an imaginary unit,
its own default) — the bug was using a different, wrong default in this file's own re-derivation
instead of copying that convention. Fixed by setting `point_index=1`; rerun gave `dim(su3)=8`
exactly, matching prediction, and the finding below.

## Results, all [VERIFIED-numpy]

| check | predicted | found |
|---|---|---|
| **P1** dim(su3) | 8 | **8** ✓ (after the fix above) |
| **P2** `solve_triality_partners(a)=(a,a)` for all 8 `su(3)` generators | residual ~0 | **max `\|b-a\|`=1.58e-15, max `\|c-a\|`=1.33e-15** ✓ |
| **P3** negative control, generic non-`g2` `so(8)` element | large deviation | **`\|b-a\|`=4.53, `\|c-a\|`=2.91** ✓ — harness genuinely discriminates, not vacuous |

## Interpretation

Within an **independent** mathematical construction — Baez's octonion-multiplication
trilinear-covariance realization of `V/S+/S-`, built entirely from scratch (own octonion
table, own `g2` derivation basis), sharing no code or basis convention with G102's Cl(0,8)
chirality-splitting realization — every `su(3)` generator is represented by the **identical
matrix** on all three triality channels. This is not a new mathematical fact (`g2=Fix(triality)`
is the classical defining property of `g2` within `so(8)` triality theory) but it **was not
previously verified concretely for this project's specific `su(3)`, nor cross-checked against
G102's construction** — only one arbitrary `g2` element had been spot-checked
(`g2_sanity_check_residual`), and never against the physically relevant `su(3)` subalgebra
specifically. This round closes that gap and gives a genuine **independent confirmation**
(different construction, same conclusion) of the "channels look identical under `SU(3)`"
finding G102's `Hom_su3` computation already established via a structurally different route —
exactly the kind of no-collapse/alternative-tool cross-check this project's own audit
discipline calls for.

## Kill Analysis

**Confirmed, not killed:** the `SU(3)` gauge/charge structure genuinely commutes correctly with
triality — a necessary piece of condition (iii)'s "no admixture on the matter factor," now
established by two independent constructions rather than one.

**NOT resolved — the genuinely hard remainder, named explicitly:** this establishes that
triality fixes the **generators** (algebra elements), not that an explicit **state-level**
operator `t` (mapping an actual vector in `8_v` to a vector in `8_s`) exists with the right
properties. That is precisely the construction pearl entry #29 (McRae 2025) found genuinely
unresolved in the Euclidean signature even at the level of pure mathematics — this round did
not attempt it and should not be read as narrowing that gap. Condition (iii), taken as the
user originally posed it ("triality acting purely as `1⊗t`"), **remains open** on its harder,
state-level half.

## What this does NOT show

1. Does **not** construct the state-level triality generator `t` — the hard, open part.
2. Does **not** establish a shared basis between this construction and G102's — the
   "independent confirmation" is at the level of the abstract conclusion only, deliberately
   avoiding the basis-alignment problem (see claim.md).
3. Does **not** touch OB1, the S³-side `t`-selection parameter (unrelated name collision with
   condition (iii)'s triality generator, also called `t`), or the S³ factor at all.
4. Nothing about `N_gen=3`'s CONDITIONAL status changes.

## Check (reproduces this derivation)

```
cd experiments/20260810-ob11iii-triality-su3-invariance
python ob11iii_triality_su3_invariance.py
```
Expect: `n_su3_generators=8`, `max|b-a|~1e-15`, `max|c-a|~1e-15`, negative control gives
`|b-a|~4.5`, `|c-a|~2.9`, `VERDICT: SU3_TRIALITY_FIXED_CONFIRMED_INDEPENDENT_CONSTRUCTION`.
