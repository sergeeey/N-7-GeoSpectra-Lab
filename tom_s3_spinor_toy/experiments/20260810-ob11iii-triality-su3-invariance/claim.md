# OB11(iii), cross-construction check: is the SU(3) matter action genuinely triality-fixed?

**Experiment id:** `20260810-ob11iii-triality-su3-invariance`
**Date:** 2026-08-10 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C61 (OB11(ii), necessary condition, mixing not excluded); G102 (Cl(0,8)
channel construction); `experiments/20260715-l3b-triality-so4xso4-invariance/triality_so4xso4_invariance.py`
(independent octonion-trilinear triality construction, Baez §2.4, `solve_triality_partners`)

---

## Continuing in order (per user instruction "го вс по очереди")

C61 closed the cheapest route to OB11(ii). This round is OB11(iii): does triality act
purely as `1⊗t` on `H_matter⊗H_generation`, with no admixture on the matter factor?

## Grounding this session found (why this round is scoped the way it is)

The literal question ("build an explicit state-level operator `t` cyclically mapping
`8_v→8_s→8_c→8_v`") is a **genuinely open problem in the pure mathematics literature**,
not merely unattempted here: pearl entry #29 (McRae 2025, arXiv:2502.14016, read in full)
states that in the **Euclidean signature** — exactly this project's signature — triality
"has no intertwining action upon the representation space (the fields)," left explicitly
unresolved even by that paper. `L3B_SPIN8_INTERFACE_SPEC.md`'s own skeptic-reviewed
condition table confirms: condition 1 (an order-3 automorphism `U` exists) holds; condition
2 (`[D,U]=0` for the physical Dirac operator) is "undetermined, not just unverified";
conditions 3-5 remain open, gated on unpublished external input (Tom Lawrence's Part 5).
Attempting the full construction from scratch this round would not be the cheapest
differentiating test — it would be re-attempting an open literature problem.

**What this round attempts instead, using already-built and partially-verified machinery:**
`triality_so4xso4_invariance.py` implements Baez's genuine trilinear covariance construction
(`solve_triality_partners`, `a(x)·y+x·b(y)=c(x·y)` for octonion multiplication) — a
mathematically real, different-from-Clifford-splitting realization of the same `V/S+/S-`
triple, with its own from-scratch octonion table and `g2` basis. It already contains one
sanity check (`g2_sanity_check_residual`): for ONE arbitrary `g2` basis element, the
triality partners `b,c` equal `a` exactly — because `g2 = Fix(triality)` is the classical
defining property of `g2` within `so(8)` triality theory. **That check was never extended
to the specific 8-dimensional `su(3)` subalgebra this project's whole OB11 chain is built
on** (only one generic `g2` element was checked, not `su(3)` specifically, and not
cross-checked against G102's independent Clifford-based construction).

## The claim under test

> **C62.** Within this independent octonion-trilinear-covariance realization of
> `V=S+=S-=O`, every one of the 8 `su(3)` generators (stabilizer of a point in this file's
> own from-scratch `g2`, same technique as G102's `stabilizer_basis`) is triality-fixed:
> `solve_triality_partners(a) = (a, a)` exactly, for all `a∈su(3)`. This would mean the
> `SU(3)` gauge/charge structure — the matter content OB11 is about — is represented by the
> **identical matrix** on `V`, `S+`, and `S-` simultaneously, independently confirming
> (via a structurally different construction: octonion trilinear covariance, not Clifford
> chirality-splitting) the same "channels look identical under `SU(3)`" conclusion G102's
> `Hom_su3` computation already established.

**Falsifier, fixed in advance:** any `su(3)` generator whose triality partners `b` or `c`
differ from `a` by more than numerical tolerance refutes the claim, and would mean `g2`'s
own `su(3)` subalgebra is NOT triality-fixed in this construction — a genuine surprise
that would need reconciling with the classical `g2=Fix(triality)` fact.

## Predictions, recorded before running

| # | Prediction |
|---|---|
| **P1 (setup)** | this file's own from-scratch `stabilizer_basis`-style extraction gives `dim(su3)=8`, matching G102's independently-built `su(3)` (cross-construction dimension check) |
| **P2 (the claim)** | for all 8 `su(3)` generators, `solve_triality_partners(a)` gives `b=a`, `c=a`, residual ~0 — extending the file's existing single-element `g2` sanity check to the full, physically relevant `su(3)` subalgebra specifically |
| **P3 (negative control, load-bearing)** | for a **generic** `so(8)` element NOT in `g2` (e.g. a random antisymmetric `8×8` matrix), `solve_triality_partners` gives `b≠a` and `c≠a` (nonzero residual against `a`) — confirming the machinery is not vacuously returning `b=c=a` for everything. If this control fails (gives `b=a` for a generic element too), the harness itself is broken and P2 cannot be trusted |

## What this cannot show (stated in advance, not after seeing results)

- Does **not** construct the actual state-level triality generator `t` (the map sending a
  *vector in* `8_v` to a *vector in* `8_s`) — that is the genuinely open, McRae-flagged
  construction. This round only establishes that the **gauge generators** commute correctly
  with the switch of representation, a necessary but not sufficient piece of condition (iii).
- Does **not** cross-align this file's own octonion basis convention with G102's — deliberately
  avoided by staying entirely within this file's self-contained construction (own `C8` table,
  own `G2_BASIS`), sidestepping the basis-alignment problem round127/128 solved for a
  different pair. The "independent confirmation" claimed above is at the level of the
  **abstract conclusion** (channels identical under `SU(3)`), not a literal shared basis.
- Does **not** touch OB1, `t`-selection (the S³ torsion parameter — unfortunate historical
  name collision with the "triality generator `t`" of condition (iii); the two `t`s are
  unrelated), or the S³ factor at all.
- Nothing about `N_gen=3`'s CONDITIONAL status changes.

## kill_criterion

C62 survives if P1, P2, P3 all pass as predicted. C62 fails (surprising, would require
reconciling with the classical `g2=Fix(triality)` fact) if any `su(3)` generator in P2 shows
nonzero residual. The round is uninformative/harness-broken if P3 fails.
