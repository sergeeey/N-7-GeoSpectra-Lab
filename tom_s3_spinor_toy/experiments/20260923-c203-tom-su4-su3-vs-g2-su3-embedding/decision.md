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

## Interpretation, sharpened per user review (2026-09-23)

The Casimir ratio alone is NOT a complete representation fingerprint --
distinct irreps can share a Casimir eigenvalue. The classification claim
below is licensed by the COMBINATION of computed invariants
(dimension + reality + Casimir ratio) checked against su(3)'s known
small-representation catalogue, not by the ratio number in isolation. Split
explicitly into four tiers so this cannot later be misread as "one Casimir
number proved equivalence":

**Computed [VERIFIED-tool, exact]:** dimension (6, real, orthogonal) and
Casimir(rep)/Casimir(adjoint) = exactly 4/9 (scalar to ~1e-16), identically
for all three constructions.

**Classification inference [INFERRED, standard su(3) rep theory, not
re-derived]:** dimension 6 + reality + Casimir ratio 4/9 together identify
the representation TYPE as the realification of `3 (+) 3bar` -- this
inference step, not the bare ratio, licenses "same representation type."

**Not established:** (a) the explicit O(6) matrix conjugating one embedding
into another; (b) which `phi in Aut(su(3))` -- possibly including the OUTER
3<->3bar swap -- relates the two generator bases (exactly the unknown that
made the naive `n_free=0` search uninformative rather than a real negative);
(c) whether Tom's complex structure `J_Tom` matches this project's
nearly-Kahler `J_NK` under the same (still unfound) `O`, or whether the
associated 2-form/3-form (`omega`, `Omega`) or Nomizu-connection/torsion data
correspond at all. None of (a)-(c) were tested.

**Does NOT imply:** theory-level equivalence between Tom's Covariant
Compactification and this project's own G2/SU(3)/N_gen=3 construction, or
that any additional SU(3)-structure/connection data matches.

## Coarse-graining caution (user-raised, 2026-09-23, directly tied to this project's own G44/C72 result)

This project's own G44/C72 chain already established that restricting to
G2 -- let alone further down to SU(3) -- CAN ERASE the triality information
this project's N_gen=3 program actually depends on. A match at the bare
su(3)-representation level between Tom's construction and ours can therefore
mean EITHER of two very different things, and C203 as run cannot yet
distinguish them:

- a genuine shared geometric platform worth building on, OR
- confirmation that both constructions have been coarse-grained down to
  PRECISELY the level where the generation-counting information no longer
  lives -- i.e. the match is real but uninformative for N_gen=3 specifically.

**Explicit hierarchy for any follow-up (do not skip levels):**

| Level | Claim | Status after C203 |
|---|---|---|
| H0 | Only the standard `SU(3) acting on R^6` matches | **Established this round** |
| H1 | The same ADDITIONAL SU(3)-structure matches (`J`, `omega`, `Omega`) | Untested |
| H2 | The match extends to operator/connection/torsion structure | Untested |

C203 supports H0 only. It does not resolve whether the Tom/NK correspondence
is a real bridge or precisely the point past which this project's own
generation-relevant structure has already been coarse-graining away --
possibly the more informative reading of a positive H0 result, not the less
informative one.

## Next step (explicitly NOT run this round, per user instruction)

A candidate C204 would need to solve for `O in O(6)` and `phi in Aut(su(3))`
JOINTLY (`O rho_A(X) O^-1 = rho_B(phi(X))`), including the outer 3<->3bar
automorphism as a real branch to check, not an edge case to ignore -- then,
if found, test H1 (`J_Tom` vs `O J_NK O^-1`) before touching H2. Parked
rather than launched now; see `parked/INDEX.md`.

## What this means for the Tom Lawrence correspondence

A real, verified representation-TYPE match exists between Tom's SO(10)-GUT
derivation and this project's own G2/SU(3) substrate (H0 only) -- best
described as **the first explicitly computed shared local
representation-theoretic structure between Tom's six-dimensional sector and
this project's own S6 construction**, not yet a claim of a physical bridge
between the two theories. NOT sent to Tom this round; per the standing DO NOT
INITIATE CONTACT rule, any correspondence requires the user's own explicit,
per-instance send decision. Per the user's own stated priority, the more
pressing next correspondence action is the already-completed C202 (ladder-
operator matrix comparison), not this round.

## Reproduce

```
cd experiments/20260923-c203-tom-su4-su3-vs-g2-su3-embedding
python c203_su3_embedding_comparison.py
```
