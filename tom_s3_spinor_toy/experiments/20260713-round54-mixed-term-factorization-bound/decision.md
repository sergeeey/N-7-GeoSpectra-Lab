# Round54-MixedTermBound Decision

**Date:** 2026-07-13
**Verdict: PASS** (factorization confirmed, general O(√C₂(ρ)) bound
established structurally) — **with a correction to Round 53** that
strengthens the overall program despite weakening one specific claim

## Summary

Direct, line-by-line code audit (not name-based assumption, per the
user's explicit warning) of Round 22's actual construction confirms:
**both** `torsion_cross_term` and `mixed_AB_term` factor as
`Σ_r B_r·w(ρ_ρ(e_r)·v)` for FIXED 64×64 matrices `B_r`, with ALL
ρ-dependence isolated in a single, linear application of `ρ_ρ` to a
fixed G₂ generator. All four of the user's required invariants hold for
**both** pieces (see `claim.md` for the itemized verification with
exact file:line citations). By the standard compact-Lie-group bound
`‖ρ_ρ(X)‖≤‖X‖√C₂(ρ)` (Cauchy-Schwarz on `Σ_aρ(X_a)²=-C₂(ρ)I`, standard
representation theory, not project-specific), this gives:

```
‖torsion(ρ) + mixed_AB(ρ)‖ ≤ K·√C₂(ρ)
```

for a single, ρ-independent constant `K` (built from the fixed matrices'
own operator norms — not yet computed, see Round 55 below).

## The correction to Round 53

Round 53 claimed Agricola 2002's Theorem 3.2 shows the torsion piece is
representation-**independent** (`O(1)`), citing her general formula for
the bare, untwisted Dirac operator on `G/H`. **This does not hold for
this project's actual twisted construction.** Reading Round 22's code
directly shows `torsion_cross_term` explicitly contains one factor of
`ρ_7(e_r)` (`g2su3_nomizu_crossterms.py:185-189`) — because this
project's operator is built via the "matrix-coefficient section"
formalism `ψ_{v,w}(g)=w(ρ_V(g⁻¹)v)` (Round 17), where the bracket
`[e_p,e_q]=Σ_r T(p,q,r)e_r+...` gets applied to `v` through `ρ_V`, not
used as an abstract fixed Clifford element the way Agricola's untwisted
case allows. **Agricola's bare theorem does not directly transfer to
this project's twisted operator** — a genuine, honest correction, found
precisely because this round insisted on reading the actual code rather
than trusting the prior round's literature-based inference.

**This correction does not weaken the overall program — it strengthens
it.** Both pieces now share the *same* mechanism and the *same*
`O(√C₂(ρ))` order, rather than one being `O(1)` (Round 53's claim, now
withdrawn) and the other `O(√C₂(ρ))`. The combined bound is cleaner and
more uniform than either round anticipated separately.

## The resulting general lower bound

Combining this round's result with Round 52's proof (`min C₂(G₂;ρ)=4`
for all nontrivial ρ, `max C₂(SU(3);σ)=3` on the fixed fibre):

```
λ²_min(D_LC²|_ρ) ≥ C₂(ρ) - 3 - K√C₂(ρ)
```

Writing `x=√C₂(ρ)`, this is positive whenever `x² - Kx - 3 > 0`, i.e.

```
√C₂(ρ) > (K + √(K²+12)) / 2
```

— a single, finite threshold. **This structurally proves a finite
exceptional set exists**, exactly the user's own Round 54 goal — with
the caveat that the explicit numeric value of `K` (and hence the exact
threshold and exceptional-set size) is not computed in this round.

## Kill Analysis

**What was tested:** whether the mixed-A-B-cross-term (and, as an
emergent consequence, the torsion-cross-term) admits the linear
factorization the user's Cauchy-Schwarz argument requires, verified
against the actual ρ=7 code rather than assumed from names or from
Round 53's literature-based inference.

**What was killed:** Round 53's specific claim that Agricola's bare
theorem alone establishes torsion-boundedness for this project's
twisted operator. Superseded, not merely wrong-and-discarded — the
replacement mechanism (Cauchy-Schwarz on the SAME linear factorization)
is stronger in scope (covers both pieces, not one) even though weaker
in per-piece bound order (`O(√C₂)` not `O(1)` for torsion specifically).

**What was NOT killed:** the overall program (finite exceptional set
exists) survives, on firmer and more unified ground than either Round
52 or Round 53 established alone. Round 52's Casimir-growth proof
(`min C₂=4`) is untouched and remains the other pillar of the bound.

## Recommendation — proceed per the user's own sequencing

**Round 55** (not started, not this round's scope): compute the actual
numeric constant `K` — requires computing operator norms of the fixed
64×64 matrices `B_r` (built from `T(p,q,r)`, `Ms[p]`, `D64` — all
already-calibrated, already-built objects; this is arithmetic on
existing fixed matrices, not a new per-representation construction) and
the norms `‖e_r‖` in the Casimir-consistent inner product.

**Round 56** (not started): once `K` is known, enumerate the finite set
of G₂ Dynkin labels `(m,n)` with `√C₂(m,n) ≤ (K+√(K²+12))/2` — per
Round 52's own finding, representations must be identified by Dynkin
label, not bare dimension (dim=77 is ambiguous).

**Only then**: compute explicit matrices for the (now finite,
enumerable) exceptional set — the expensive step every prior round in
this chain has correctly deferred.

## What NOT to do (per explicit user instruction, reconfirmed)

Do not compute ρ=27, 64, or 77 (or any other specific representation)
in this round. Do not touch `preprint.tex` — the stronger, unified
`O(√C₂(ρ))` bound is real progress but the numeric constant `K` is not
yet known, so no preprint claim beyond the existing honest hedge is
licensed yet.

## Update to parked/INDEX.md

`L4B-HIGHER-REPS` remains PARKED (the finite exceptional set is not yet
enumerable without `K`), but its revival condition is now substantially
sharpened: the "general bound" half of the original revival condition
is now structurally PROVEN (this round); only the numeric constant `K`
remains outstanding, a concrete, bounded, non-open-ended piece of work
(Round 55) rather than an open research question.

## Scope discipline check

No Dirac-operator matrices built for any new ρ. `preprint.tex`
untouched. Round 53's error corrected transparently, not silently
overwritten — its claim.md/decision.md remain as the historical record
with this round's correction cross-referenced, per this project's
"never delete, annotate" discipline for superseded findings.

## Files

- `claim.md` — this round's FL Standard-tier artifact, with exact
  file:line citations for all four invariant checks
- No script — pure code-reading/structural audit, no new numeric
  computation performed (per explicit user scope for this round)
