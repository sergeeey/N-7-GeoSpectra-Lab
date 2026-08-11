# C81 -- redesigned non-product test with D_S6's raw kernel excluded, both so(4)_1 halves

**Experiment id:** `20260811-c81-raw-kernel-excluded-retest`
**Date:** 2026-08-11 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C79 (built the coupling term, found a crossing later
traced to a raw-kernel artifact); C80 (completed the pair, generalized
the artifact finding, named "fix the test design by excluding the raw
kernel" as the correct next step -- this round)

---

## Why the fix is well-posed (checked before writing the redesigned test)

`D_S6`'s full spectrum was read directly this round, not assumed: exactly
36 eigenvalues at `0` (the raw kernel), then a CLEAN GAP to the next
eigenvalue at `|0.8165|` (`=sqrt(2/3)`, exact). This gap is what makes the
fix well-defined: within `Delta_m (x) ker(D_S6)` (the 36-dim raw kernel,
tensored with `S3`'s 2-dim spinor factor), `D_joint_base` reduces to the
CONSTANT `1.5 * I` (since `D_S6` contributes exactly zero there) --
meaning `D_joint(eps) = 1.5*I + eps*T` restricted to this subspace is a
straight-line function of `eps` in every direction, and for ANY nonzero
eigenvalue of `T` restricted there (which a generic `T` will have), a
crossing at `eps = -1.5/lambda` is **mathematically guaranteed**, not a
finding about physics. Outside the raw kernel, `D_S6` contributes a
genuinely nonzero, gapped value that the coupling has to actually
overcome -- a real dynamical question, not an algebraic certainty.

## The fix

1. **Primary, clean test:** compress `D_joint(eps)` onto `Delta_m (x)
   (D_S6's 28-dim non-kernel eigenspace)` -- a 56-dim subspace on which
   `D_S6` is, by construction, bounded away from zero (`|eigenvalue| >=
   0.8165` everywhere). Sweep `eps`, look for crossings in this
   COMPRESSED operator. Since this subspace has no free zero from `D_S6`
   alone, any crossing found here reflects a genuine competition between
   `D_S6`'s own nonzero spectrum and the coupling -- not an artifact.
2. **Cross-check, so the compression itself is not silently hiding
   something:** on the FULL, uncompressed 128-dim spectrum (exactly as
   C79/C80 built it), classify every near-zero eigenvalue found across the
   sweep by its raw-kernel overlap. The known deterministic crossings
   (`eps=+-1.5`) should reappear with high overlap (a sanity check that
   this round's own machinery reproduces C79/C80 correctly); any
   ADDITIONAL crossing with LOW raw-kernel overlap would be a genuinely
   new signal the compression might have missed (since compression ignores
   `T`'s mixing into/out of the kernel).

Both self-dual and anti-self-dual `so(4)_1` triples (C79/C80's own,
reused unmodified) are tested.

## The claim under test

> **C81 (working).** With the raw-kernel artifact mechanism excluded by
> construction, does either half of `so(4)_1` produce a genuine crossing
> in the physically meaningful (non-kernel) part of the spectrum?
> **Prediction:** no -- the raw kernel's deterministic mechanism was the
> ENTIRE explanation for C79/C80's crossings (both were traced to
> ~100% raw-kernel eigenvectors), so removing it should leave nothing.
> This prediction is recorded honestly and must not be protected if the
> result differs.

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1 (spectral gap)** | `D_S6` has exactly 36 zero eigenvalues and a clean gap to the next value (`>=0.8`) -- confirms the fix is well-posed | pending |
| **P2 (eps=0 sanity, restricted)** | the compressed 56-dim `D_joint` at `eps=0` has no zero eigenvalue (matches the full-space eps=0 result, `min|eigval|=0.3257`, since the raw kernel contributed nothing to that number either) | pending |
| **P3 (self-dual, restricted)** | sweeping `eps in [-2,2]` for the compressed operator, self-dual triple: no crossing | pending |
| **P4 (anti-self-dual, restricted)** | same, anti-self-dual triple: no crossing | pending |
| **P5 (full-spectrum cross-check)** | the full 128-dim spectrum reproduces the known `eps=+-1.5` crossings (high raw-kernel overlap, sanity) and finds no ADDITIONAL crossing with low raw-kernel overlap | pending |

## kill_criterion

P1 fails if `D_S6`'s spectrum does not show a clean gap -- would mean the
fix is not well-posed as designed and needs rethinking before trusting
anything downstream. P2 fails if the restricted eps=0 result disagrees
with the already-established full-space value -- would indicate a bug in
the compression. **P3/P4/P5 are the actual test.** A "no crossing" result
(matching the prediction) is a genuine, informative negative -- it means
the raw-kernel exclusion removed the ONLY signal these two candidates ever
produced, closing them properly rather than leaving the artifact
unresolved. A crossing found here, in EITHER the compressed test or as a
low-overlap signal in the cross-check, would be a genuinely new and
significant finding requiring the same extra scrutiny this project applies
to any unexpectedly positive result after a long run of negatives --
verified against its OWN mechanism (not just accepted) before being
trusted, exactly as C79's own crossing was investigated rather than
believed at face value.

## What this cannot show

- Does **not** test any candidate beyond `so(4)_1`'s two halves -- the
  SAME two candidates as C79/C80, now properly re-examined.
- Does **not** test the full Peter-Weyl tower -- `S3`'s `n=0` sector only,
  same scope limit as C79/C80.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
