---
claim_id: A-index-map
round: 20260715-round-su3-index-map-audit
status: OPEN — supported on controls, general proof not done
---

# Claim A — General SU(3) index-map identity

## Question Type (EstimandOps L0 / sci-evidence Domain Gate)
Mathematical / Formal. Not causal, not empirical — a proof-or-disproof question.

## Claim under test

For every SU(3) irrep with Dynkin labels (p,q), twisted with the standard
homogeneous connection on S^6=G₂/SU(3):

    ind(D ⊗ E_{p,q}) = I(p,q)
      = (p-q)(p+1)(q+1)(p+q+2)(p+2q+3)(2p+q+3) / 120

## Evidence so far (what IS verified)

1. Direct Chern-root computation for E_{1,0}=T^{1,0}S^6 (rank 3) and
   E=T⊕(T⊗T) (rank 12, ≅ S⁻⊗T): ind = 7, matching I(2,0)=7 exactly
   [see 20260715-index-formula-s-tensor-t-candidate/, cited not re-derived].
2. I(p,q) evaluated symbolically at (1,0),(0,1),(2,0) matches claimed values
   1, -1, 7 exactly [same prior experiment].
3. This round: sign-structure sweep over (p,q)∈[0,15]² confirms
   I(p,q)>0 ⟺ p>q with zero exceptions (see `certificates/`).

**Correction on independence (flagged by user):** items 1 and 2 above are
NOT two independent verification paths. The hand derivation and its sympy
implementation are two REALIZATIONS of the same method (Chern-root expansion
of ch₃), not independent lines of evidence — per the Independent Verification
Strength Ladder (`falsification-ladder.md`), this is "same model, isolated
context" at best, not "different method". The genuine independent Path B for
Claim A, not yet attempted, is the representation-ring route:

    R(SU(3)) → K^0(S^6) → ℤ

via representation-ring recursion (3⊗(p,q)=(p+1,q)⊕(p−1,q+1)⊕(p,q−1)) or an
explicit direct-sum-of-weight-cubes construction — genuinely different from
Chern-root expansion, since it works entirely in the representation ring
without reference to the tangent bundle's Chern classes.

So the honest evidence inventory is: 1 direct geometric method (2 write-ups
of it), checked at 3 points, plus 1 finite sign-consistency sweep. This is
NOT two independent confirmations — it is one method, well-checked at few
points. This does not weaken H1/H2 as already-established facts about the
specific S⁻⊗T candidate (those stand on their own), but it does mean Claim A
should not be described as having "two independent derivations converging" —
it has one geometric derivation, consistently re-verified.

## What remains to prove (the actual open gap)

A general argument along these lines, per the four steps:

1. H^6(S^6;ℤ) ≅ ℤ — top cohomology rank 1 (established, standard).
2. ch₃(V_{p,q}) is proportional to the SINGLE cubic SU(3) invariant
   (there is only one degree-3 Casimir-type invariant for SU(3) reps once
   restricted to this coset's characteristic classes) — this proportionality
   claim is the crux and is NOT yet shown in general, only checked at 3 points.
3. The proportionality constant is the normalized cubic index.
4. Orientation/normalization fixed by ind(E_{1,0})=1.

Step 2 is where the real content lives: it requires either (a) an explicit
general Chern-root computation for the (p,q) representation bundle analogous
to what was done for (1,0) and (2,0), or (b) an appeal to a known
representation-theoretic formula (e.g. via the Weyl dimension/index formula
machinery) that has NOT been cross-checked against this project's own
Chern-root method beyond the 3 existing points.

## Falsification test (if attempted)

Pick at least 2 more (p,q) pairs NOT yet checked by direct Chern-root
expansion (e.g. (1,1) and (3,0), both already numerically evaluated via I(p,q)
in the certificate sweep) and verify via an INDEPENDENT direct geometric
construction (not just formula substitution) that the index matches. This
would raise confidence but still not constitute a proof for all (p,q) — only
a full general argument (steps 1-4 above) closes this claim.

## What this does NOT mean if the 3-point + sign-sweep evidence is used to proceed

1. Does NOT mean the general formula is proved — "supported on controls" is
   the honest status, not "verified".
2. Does NOT invalidate Claim B or C's use of I(p,q) as a working formula —
   both are explicitly conditioned on Claim A (see their own status lines).
3. Does NOT mean every possible SU(3) irrep bundle can be built as an
   explicit homogeneous vector bundle on S^6 — existence of E_{p,q} as a
   genuine homogeneous bundle for arbitrary (p,q) is assumed, not verified here.

## Status

`SUPPORTED ON CONTROLS — GENERAL PROOF OPEN`
