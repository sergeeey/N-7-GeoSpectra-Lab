# G98 — B-L as isometry vs. holonomy charge

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:**
G97's B-L generator (from G15, on the 8-dim S6 spinor) commutes with the
so(6) isotropy subalgebra of so(7) (15 generators) but does NOT commute with
at least one generator of the so(7)/so(6) coset (6 generators). This would
show that G97's "B-L not in Iso(S6)=SO(7)" finding is expected structure
(B-L is a holonomy/R-symmetry charge, not an isometry generator), not an
unresolved contradiction with G15's earlier B-L construction.

**Kill target (MANDATORY — Strong Inference):**
Case in TOM_RECONSTRUCTION_ACH_MATRIX.md / RESEARCH_STATUS_REPORT.md
U(1)_Y coverage table (G97 row: "B-L generator: not covered by
Iso(S3xS6)").

- FAIL (all 6 coset commutators are also zero) -> kills this reconciliation
  hypothesis; G97's finding becomes a genuine unexplained tension between
  the NCG route (G15/G18-22) and the isometry route (G95-97) that DOES
  require external input (Tom) to resolve, exactly as G97 currently states.
- PASS (at least one coset commutator is non-zero, so(6) commutators all
  zero) -> the apparent G15-vs-G97 contradiction is resolved: B-L is
  correctly absent from the FULL isometry algebra (confirming G97) while
  still being a valid geometric charge (confirming G15), because it lives
  in the isotropy/holonomy subalgebra, not the isometry Cartan. G97's status
  should be updated from "OPEN, needs Tom" to "RESOLVED: B-L is a holonomy
  charge, expected to be absent from Iso(S6) Cartan; U(1)_Y combination rule
  (Y=T3_R+(B-L)/2) itself is not yet derived from a single unified group,
  but each piece's origin is now understood."

If no hypothesis is killed by FAIL -> gate is not scientifically motivated.
(Not applicable here: FAIL is a real, informative outcome -- it would mean
the NCG and isometry routes are in genuine tension, itself a valuable
finding to escalate.)

**Checks planned:**
- T1: Gamma_7 = kron(s3,s3,s3) anticommutes with all 6 Gamma_a (a=1..6),
  is Hermitian, squares to +I [pre-check, already verified inline before
  committing to this design]
- T2: build 6 coset generators K_a = [Gamma_a, Gamma_7]/4 for a=1..6
- T3: build all 15 so(6) generators J_ab = [Gamma_a,Gamma_b]/4, a<b in 1..6
- T4: verify the 21 generators (15+6) close under commutation into the
  so(7) algebra with the correct structure constants (sanity check that
  this really is so(7), not some other algebra)
- T5: [BmL, J_ab] = 0 for all 15 so(6) generators (extends G15's T4, which
  only checked the 8 su(3) generators, a proper subset of so(6))
- T6: [BmL, K_a] for all 6 coset generators -- report each value, count
  non-zero
- T7 (adversarial/edge case): repeat T5-T6 with an independently
  constructed BmL (via the Hamming-weight formula from G15's own T2, not
  the sigma3-sum formula) to rule out a construction-specific artifact

**Verdict:** WEAK_UNINFORMATIVE_DIAGONAL_ARTIFACT — see decision.md.
Skeptic-required control (generic so(6) Cartan generators J_01/J_23/J_45)
also fails to commute with the coset, so BmL's failure is not B-L-specific.
G97's gap remains OPEN.

**Evidence:** [VERIFIED-sympy 10/11] — 1 fail is a design mis-scope (T5
tested full so(6) instead of su(3)+u(1) subalgebra), not a computation bug.

**Caveat / What this does NOT mean:**
- Does NOT derive U(1)_Y from a single group (see estimand.md, "what this
  does NOT mean" #1-2)
- Does NOT change sm_derivation_claimed=False
- Does NOT bear on N_gen=3, moduli stabilization, or lambda -- fully
  independent of those threads

**Fence (do not change):**
- lambda_v_operator = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

**Status:** CLOSED WEAK
