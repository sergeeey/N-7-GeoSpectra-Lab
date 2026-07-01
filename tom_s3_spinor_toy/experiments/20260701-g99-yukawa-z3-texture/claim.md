# G99 — Z3-triality texture of inter-generation Yukawa couplings

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:**
Extending the verified Z3 triality action (G75: eigenvalues 1, omega, omega^2
on channels v,s,c) to the 3 generation-copies of G25's single-generation
Yukawa object, the Z3-invariance condition on a standard mass-like Yukawa
term (total Z3 charge = 0 mod 3) forces the inter-generation coupling
matrix M_species[i,j] to vanish unless (i+j) = 0 (mod 3) -- i.e. the texture
is NOT purely diagonal: entries (0,0), (1,2), (2,1) are allowed; entries
(0,1),(0,2),(1,0),(2,0),(1,1),(2,2) -- wait, (1,1) and (2,2) also satisfy
i+j=2,4=1 mod 3 respectively, need explicit check, not assumed here.

**Kill target (MANDATORY — Strong Inference):**
No existing ACH case covers this (new question). Kill target is the
estimand's own MCID: does Z3-invariance permit anything beyond PURE_DIAGONAL?

- FAIL (texture = PURE_DIAGONAL, i.e. Z3-invariance forces M_species to be
  proportional to a diagonal matrix with no further off-diagonal freedom,
  OR the diagonal entries are additionally forced equal by some other
  argument) -> this specific triality construction structurally EXCLUDES
  generation hierarchy without extra input; document as a real limitation
  of the current framework, not a bug.
- FAIL (texture = FULLY_UNCONSTRAINED, i.e. the Z3 charge assignment on the
  Yukawa bilinear is trivial/undefined given current constructions) ->
  the triality label has not actually been connected to the Yukawa sector
  at all; this experiment could not even ask a meaningful question yet,
  and a prerequisite construction (a genuine Z3-covariant Yukawa operator)
  is needed before this claim can be tested.
- PASS (texture is neither pure-diagonal nor fully unconstrained --
  specific nonzero off-diagonal entries survive per a computable rule) ->
  new structural result: Z3 triality is compatible with (does not exclude)
  non-degenerate generation masses, and predicts WHICH inter-generation
  couplings are allowed vs forbidden.

**Checks planned:**
- T1: construct the 3 Z3-covariant "generation blocks" explicitly (each a
  copy of the 32-state object with an assigned Z3 phase omega^k)
- T2: define the Z3 action on the tensor-product Yukawa-term space
  (channel_i (x) channel_j, i.e. what phase a term connecting generation i
  to generation j picks up)
- T3: solve the invariance condition (total phase = 1) for all 9 (i,j)
  pairs, report exactly which survive
- T4 (adversarial control, required per G98 lesson): verify the SAME
  computation using an independently-labeled Z3 action (e.g. relabel
  channels 0<->1) gives the SAME texture PATTERN (not the same matrix, but
  an equivalent one under relabeling) -- rules out an artifact of an
  arbitrary channel-labeling choice
- T5: cross-check against G25's existing |Q|-based structure -- does the
  allowed texture respect Q-conservation already established within one
  generation (sanity, not a new physics claim)

**Verdict:** [Run result — filled after running]

**Evidence:** [VERIFIED-sympy N/N] — filled after running

**Caveat / What this does NOT mean:**
- Does NOT derive the observed Yukawa hierarchy values
- Does NOT touch N_gen=3, moduli stabilization, or lambda
- Does NOT change sm_derivation_claimed=False

**Fence (do not change):**
- lambda_v_operator = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

**Status:** CLOSED BLOCKED_PRE_IMPLEMENTATION — see decision.md. Two
independent pre-implementation reviews found the Z3-to-Yukawa phase
assignment unfounded (S3 sector's triality behavior never established in
repo); no script was written, no result was forced.
