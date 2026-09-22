# C203 Decision — Tom's SU(3) subset SU(4)~SO(6) embedding is the SAME representation type as this project's G2/SU(3)-on-S6 embedding

**Date:** 2026-09-23
**Verdict:** PROMOTE, with an explicit named scope caveat (see claim.md Verdict section)

## What was checked (all `[VERIFIED-tool]`, `c203_su3_embedding_comparison.py`)

| Side | Construction | Result |
|---|---|---|
| A (ours) | Reuse `g96_g2_su3.py` unmodified: G2 as octonion derivations, SU(3)=Stab(e6), restricted to the 6-dim tangent space at e6 | dim(G2)=14, dim(su3)=8, stabilizer/closure errors ~1e-16 |
| B (Tom's) | Cl(6) gamma-matrix construction (8x8, Pauli tensor products, anticommutation verified numerically), chirality projector to a 4-dim chiral su(4), invert the standard so(6)<->su(4) dictionary M_ab <-> (1/4)[Gamma_a,Gamma_b]\|_chiral, apply to the su(3) block-embedded in su(4) via Gell-Mann matrices | Clifford/chirality/reconstruction errors all ~0, closure ~1e-16 |
| C (control) | G10-B's own `su3_generators()`, reused directly, not reimplemented | dim=8, closure ~1e-16 |

## The two bugs caught and fixed during construction (both mine, not Tom's or G96's/G10-B's)

1. **Hermitian/anti-Hermitian convention mismatch.** First draft mapped
   `so(6) -> su(4)` via `(i/4)[Gamma_a,Gamma_b]`, which is HERMITIAN (since
   `[Gamma_a,Gamma_b]` is anti-Hermitian for Hermitian Gammas, and `i` flips
   that to Hermitian) -- an assertion (`elem` must be anti-Hermitian to land
   in `su(4)`) caught this immediately on the first run, before it could
   silently propagate. Fixed by dropping the factor of `i`: `(1/4)[.,.]` is
   itself anti-Hermitian, landing correctly in `su(4)`.
2. **Naive intertwiner search was the wrong test, caught by its own honest
   null result.** The straightforward `A_i U = U B_i` linear solve (same
   method as C201/C202) returned `n_free=0` -- literally no solution, not
   even a non-orthogonal one. This LOOKS like a clean negative but is not:
   C201/C202 had an explicit, STATED generator correspondence (Tom's own
   eq 67-69 naming which T_ij is which L). Here, no such correspondence
   exists between G96's SVD-derived su(3) basis and the Gell-Mann-derived
   one -- the index pairing was arbitrary, and su(3) has real automorphisms
   (inner + outer 3<->3bar conjugation) that could relabel generators many
   ways. Recognized mid-round rather than reported as a real mismatch;
   replaced with the Casimir-ratio invariant below, which needs no generator
   correspondence at all.

## The actual verdict test: Casimir(rep)/Casimir(adjoint) ratio

Built from each side's OWN structure constants (solved via least-squares
against the already-verified-closed generator set) and OWN Killing form
(`g_ij = Tr(ad(T_i) ad(T_j))`), so the arbitrary normalization of each side's
generators cancels exactly in the ratio -- this is what makes the number
comparable across three completely unrelated bases without needing to match
generator labels first.

```
A (ours, G96):        ratio = 0.444444444444...  (rep/adj scalar defect ~1e-16)
B (Tom's, SU(4)):      ratio = 0.444444444444...  (rep/adj scalar defect ~1e-16)
C (G10-B, control):    ratio = 0.444444444444...  (rep/adj scalar defect ~1e-16)
Theoretical su(3) "3": 4/9 = 0.444444444444...
```

All three agree to machine precision. The Casimir being confirmed EXACTLY
scalar on each 6-dim representation (not merely averaging to the same value)
rules out a coincidental match between structurally different reducible
combinations of irreps.

## Interpretation, honestly scoped

**Established:** all three constructions -- Tom's own GUT-derivation
embedding, this project's own G2/SU(3)-on-S6 Dirac-operator substrate, and
even the independently-built G10-B control -- realize the identical
representation TYPE of su(3): the fundamental "3" (and its conjugate
"3bar"), realified as the standard 3+3bar real 6-dimensional orthogonal
representation.

**Not established here:** the explicit O(6) matrix conjugating one embedding
into another. That step additionally relies on citing a standard
representation-theory fact (this specific representation type has a unique
O(6)-conjugacy class) rather than an independently-constructed intertwiner.
If a fully constructive proof is ever wanted, the next step would be finding
the Lie-algebra automorphism between the two generator bases first (e.g. by
matching Cartan subalgebras / root structure), then re-running the
intertwiner search with the corrected correspondence -- not attempted this
round, and not required to answer the correspondence-relevant question.

## What this means for the Tom Lawrence correspondence

There IS a genuine, verified structural link between Tom's SO(10)-GUT
derivation (his GPIC 2026 talk) and this project's own G2/SU(3)/N_gen=3
physics substrate: both use the identical su(3) representation type inside
so(6), not merely superficially similar terminology. This is a real,
interesting cross-connection worth surfacing eventually -- NOT sent to Tom
this round; per the standing DO NOT INITIATE CONTACT rule, any correspondence
requires the user's own explicit, per-instance send decision.

## Reproduce

```
cd experiments/20260923-c203-tom-su4-su3-vs-g2-su3-embedding
python c203_su3_embedding_comparison.py
```
