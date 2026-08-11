# decision — OB11(ii) necessary condition: mixing is NOT excluded by bare SU(3) equivariance

> **CORRECTION 2026-08-10 (same-day follow-up, `20260810-ob11ii-round59-su3-bridge`).**
> This file's own framing that `Hom_su3(m⊗channel_i,channel_j)≠0` is "necessary, not
> sufficient" for a genuine G2-invariant mixing term to exist is **imprecise**. Standard
> Frobenius-reciprocity theory for homogeneous vector bundles (sections of an invariant
> bundle over `G/H` correspond exactly to `H`-equivariant maps on the fiber) means a
> nonzero element of this Hom space **already suffices** to build a genuine G2-invariant
> first-order differential operator term — existence was never really in question once the
> Hom space is nonzero. The real remaining question, sharpened in the follow-up round, is
> whether such a term can be part of a **Hermitian, genuinely Clifford-compatible** combined
> operator (the physical requirement, not mere G-invariance) — a materially different, harder
> question than what this file's own "does_not_imply" section stated. Not retracted — the
> computed result (`Hom≠0` for all pairs) stands unchanged — only the interpretation of what
> that result leaves open is corrected here.

## Verdict

`MIXING_NOT_EXCLUDED_BY_NECESSARY_CONDITION` → **C61 (strong form) REFUTED; OB11(ii) stays
OPEN, genuinely narrowed.**
**Date:** 2026-08-10 · L0: descriptive · ruff clean · `results_ob11ii.json` persisted.

---

## What was checked and how

Extracted `m = g2/su3` (6-dim complement, Frobenius-orthogonal, from G102's own `der`/`su3`
bases) and built the tensor representation `m⊗channel_i` for each triality channel, using
G102's unmodified `restrict_to_subalgebra`/`hom_dim` machinery throughout. Computed
`dim Hom_su3(m⊗channel_i, channel_j)` for all 9 ordered pairs `(i,j) ∈ {v,s,c}²`.

## Results, all [VERIFIED-numpy]

| check | predicted | found |
|---|---|---|
| **P0** dim(m) | 6 | **6** ✓ |
| **reductivity** `[su3,m]⊆m` | ~0 leakage | **4.2e-16** ✓ (confirmed, not assumed) |
| **P1** `C₂(m)` spectrum | consistent with `3⊕3̄` | **all 6 eigenvalues = -4/3 exactly**, one cluster, not two — consistent with C29's own established fact that `C₂(3)=C₂(3̄)=4/3` identically, so a single cluster is the *correct* signature, not an anomaly |
| **P2** diagonal `Hom_su3(m⊗channel_i,channel_i)` | nonzero (harness sanity) | **10, all three** ✓ harness sound |
| **P3** off-diagonal `Hom_su3(m⊗channel_i,channel_j)`, i≠j | predicted nonzero | **10, all six pairs** — refutes the strong claim |

**The finding, stated precisely:** off-diagonal and diagonal Hom-dimensions are not just both
nonzero — they are **exactly equal** (10 = 10, all nine pairs, no exceptions). Bare SU(3)-
equivariance draws no distinction whatsoever between "channel talks to itself" and "channel
talks to a different channel."

## Interpretation — why this is the *expected* consequence of already-established facts, not a new surprise

This is not an isolated new fact — it is the direct, predictable consequence of two things this
project already established and cites in `claim.md`:

1. **OB11 condition (i) / C29**: all three channels have *identical* internal SU(3) block
   structure (`1⊕1⊕3⊕3̄`), verified by Hom-count, not just Casimir.
2. **G102 S6/S7**: `su(3)` alone gives `Hom(channel_a,channel_b)=6` for **all nine** pairs
   including off-diagonal — the algebra genuinely cannot tell the channels apart at the bare
   fiber level; that is what "identical SU(3)-module" *means*.

Since `channel_v ≅ channel_s ≅ channel_c` as `su(3)`-modules via the identity map (not merely
abstractly isomorphic — G102's own construction gives them as *literally the same* action, per
pearl-registry entry #34: "the twisted Dirac operators... are THE SAME OPERATOR"), tensoring
each with the same `m` produces the same module again, and `Hom_su3` of a fixed module against
itself is necessarily independent of which channel-label you started from. Finding `10=10=...`
is exactly what this predicts. The genuine content of this round is **extending the
already-known "SU(3) alone cannot distinguish channels" result from the bare fiber (G102 S7,
Hom=6) to the tangent-twisted, Dirac-operator-relevant Hom-space (Hom=10)** — closing off the
possibility that folding in the tangent representation (the object the actual Dirac operator is
built from) might have broken the degeneracy where the bare fiber didn't. It doesn't.

## Kill Analysis

**Killed:** the specific, narrow hypothesis that bare `SU(3)`-representation theory alone
forces `X_ij=0` (the strong form of C61, and the cheapest possible route to proving OB11(ii)).
This route is now closed — not "not yet tried," genuinely closed, the same way pearl #26 closed
a structurally analogous route for a different rep pair.

**Not killed:** OB11(ii) itself. A first-order mixing term could still be forbidden by finer
structure this round did not test — specifically, whether the actual **G2-invariant differential
operator** (not just the pointwise `su(3)`-equivariant algebraic room) picks out a nonzero
element in this 10-dimensional Hom-space, which is a question about the specific octonion/
Clifford/connection data, not about representation content. This is exactly the harder,
not-yet-attempted question the project's own 2026-08-03 note anticipated when it said condition
(ii) "requires assembling a genuinely new channel-decomposed differential Dirac operator" — this
round narrows *why* that's true (SU(3) content alone provides no shortcut around it) without
removing the need for it.

**Relaxation map for the surviving question:** the honest next step, if OB11(ii) is picked up
again, is not "redo this computation" (closed) but one of:
1. Build the actual G2-invariant differential operator using round59's real Clifford/connection
   apparatus (expensive, and per the 2026-08-03 note, entangled with the S³-side OB1/`t`
   selection once the full 4D operator is needed — though this round's S⁶-only scope suggests
   the *S⁶-side* piece specifically may not need `t` at all; that separability is *asserted* in
   `claim.md`'s scope note but not independently re-verified here and should not be assumed
   settled without checking).
2. Determine whether triality itself (an outer, not inner, symmetry — G102 S3/S4 already showed
   no inner symmetry can permute the labels) imposes a *further* selection rule on which element
   of the 10-dim Hom-space, if any, is picked out by requiring the resulting operator to be
   triality-covariant as a whole — a genuinely different, not-yet-explored angle.

## What this does NOT show

1. Does **not** prove `X_ij≠0`. Absence of a necessary-condition obstruction is not existence of
   a term — only the removal of the cheapest reason it couldn't exist.
2. Does **not** attempt condition (iii) (`τ=1⊗t`) — untouched, as scoped.
3. Does **not** touch OB1, `t`-selection, or the S³ factor.
4. Does **not** build the actual differential Dirac operator — the algebraic room (`Hom`-space)
   found here is a necessary precondition for a term to exist, not the term itself.
5. Nothing about `N_gen=3`'s status changes — it was CONDITIONAL before this round and remains
   CONDITIONAL after it; this round neither strengthens nor further weakens it, it narrows what
   the open question actually is.

## Check (reproduces this derivation)

```
cd experiments/20260810-ob11ii-channel-mixing-necessary-condition
python ob11ii_channel_mixing.py
```
Expect: `dim(m)=6`, reductivity leak ~1e-16, `C2(m)` all six eigenvalues at `-1.333333`, all
nine `Hom_su3(m⊗channel_i,channel_j)=10`, `VERDICT: MIXING_NOT_EXCLUDED_BY_NECESSARY_CONDITION`.
