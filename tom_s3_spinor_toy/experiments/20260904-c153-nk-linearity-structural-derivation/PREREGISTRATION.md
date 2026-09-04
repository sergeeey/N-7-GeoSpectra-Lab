# PRE-REGISTRATION — C153: does non-integrability (Nijenhuis != 0) predict WHICH
# 2 of the 8 invariant almost-complex structures satisfy c(J.grad) = i c(grad)?

**Registered:** 2026-09-04, before running the correlation test below.

## L0 gate (EstimandOps): DESCRIPTIVE

Characterising an already-computed structural pattern (C152 Step 8's own
finding: the identity holds for exactly 2 of 8 invariant a.c.s.). No
counterfactual, no DAG.

## Background (what is already established, not re-derived here)

- C152 Step 8 (`is_c_linear`, `acs_from_eps`) found, ON THE CORRECTED
  SU(3)/T^2 sector: `c(J_eps.grad) = +-i c(grad)` holds for EXACTLY 2 of the
  8 invariant almost-complex structures `eps in {+-1}^3`, at machine-exact
  deviation (1.8e-31), and fails for the other 6 at deviation of order unity
  (1.6-2.0). The `acs_from_eps` construction is a SIMPLE fixed 6x6
  block-diagonal sign matrix (+-90 deg rotation per root plane) that
  commutes with T^2 (rotations in a common 2-plane always commute), so it is
  T^2-equivariant for ALL 8 eps -- this was already established (C151's
  "J preserves the family" check, later shown tautological for this reason).
- C151 Stage 1a computed the Nijenhuis tensor for the SAME 8 sign tuples in
  the RAW (pre-alignment) basis and classified them 6 integrable
  (Kahler, N=0) + 2 non-integrable (nearly-Kahler, max|N|=4.000).
- Stage 2a THEN reordered the basis by eps_NK = (-1,1,-1) so that J_NK
  becomes the standard J_0 in the aligned coordinates C152 Step 8 works in.
  So the RAW eps used by Stage 1a and the ALIGNED eps used by Step 8 are
  related by a fixed, known relabelling: aligned_k = raw_k * eps_NK[k].

## The question

Is "non-integrable" (Nijenhuis != 0) the SAME 2-element subset of {+-1}^3 as
"C-linear" (Step 8's 2-of-8), once the raw/aligned relabelling is undone --
i.e. is nearly-Kahler-ness (a purely GEOMETRIC/torsion property) exactly
equivalent, on this finite population of 8 invariant structures, to
C-linearity of the twist-connection coefficient (an ALGEBRAIC property of
the operator)?

## Prediction, frozen before computing

Under the relabelling `aligned = raw * eps_NK`, the two sets should coincide
exactly:

    {aligned eps : C-linear}  ==  {raw eps : non-integrable} * eps_NK

Reasoning given in advance (not yet verified): Stage 2a's alignment was
BUILT so that J_NK (the unique-up-to-conjugation non-integrable structure)
becomes eps=(1,1,1) in aligned coordinates -- and Step 8 already found
(1,1,1) and (-1,-1,-1) (its conjugate) are exactly the 2 that hold. If the
raw-to-aligned bookkeeping is consistent, this is not a new geometric fact,
but confirming it computationally (not just narratively) is the whole point
of a descriptive claim: the ⟺ must be SHOWN, not asserted from the
construction's intent.

## Kill criterion

If the non-integrable RAW set, relabelled by eps_NK, is NOT identical to the
C-linear ALIGNED set found in C152 Step 8, this predicts nothing and the
claim that "the 2-of-8 selection is the nearly-Kahler condition" is
FALSIFIED -- the true selector would then be some OTHER, unidentified
property that happens to coincide with (1,1,1)/(-1,-1,-1) for a different
reason.

## Second, independent question (not contingent on the first)

Does the obstruction `O(eps) := c(J_eps.grad) - i c(grad)`, computed as an
EXACT linear map on the 6-dim family (not merely tested on random draws),
vanish IDENTICALLY (all 6 basis coefficients, not just a few random probes)
for the 2 C-linear eps, and is it EXACTLY, algebraically nonzero for the
other 6 -- verified with exact rational arithmetic (sympy), not floats?

Prediction: yes to both, since SU(3)/T^2's construction (unlike S^6's, which
needs sqrt(3) from the CH2016 radius normalisation) uses only integer/half-
integer structure constants (Stage 2a's basis is EXACTLY B-orthonormal with
zero residual), so no irrational surds should appear anywhere in this
computation -- a genuinely stronger (P3-flavoured) form than C152's floating
verification.

## What this would NOT establish, even if confirmed

1. Does NOT prove a general theorem for ARBITRARY almost-complex structures
   -- only for the 8 INVARIANT ones on THIS coset.
2. Does NOT explain WHY nearly-Kahler-ness (rather than some other
   invariant) is the discriminator at the level of a general Lie-theoretic
   argument -- it would establish the correlation on this coset, not derive
   it from first principles applicable to any homogeneous NK 6-manifold.
3. Does NOT bear on S^6, where there is no analogous "8 choices" question
   (the isotropy SU(3) rigidifies J to a single one up to sign, per C147).
