---
experiment_id: 20260708-dolan-casimir-g2su3
date: 2026-07-08
tier: Full-Ladder
status: in_progress
parent_experiment: 20260625-kp-zero-mode (E-KP1), 20260625-e-coker (E-COKER)
---

# claim.md — Resolving the rank(D+|_trivial) ambiguity in E-KP1/L4B

## Background (why this experiment exists)

preprint.tex's Corollary "Exact kernel" (cited as L4B, "proved") claims
dim ker(D+_{S-}) = 1, dim ker(D-) = 0 on the G2-trivial isotypic component of
S+⊗S- → S-⊗S- (a 2-dim → 1-dim map). This rests on `kp_zero_mode.py` lines
421-433, which ASSUMES rank(D+|_trivial) = 1 ("surjective") with a justifying
comment that a skeptic agent (2026-07-08, Falsification-Ladder Step 8a,
mode=artifact, HIGH confidence) confirmed is a non-sequitur: for a map
C^2 -> C^1, index = dim(domain) - dim(codomain) = 1 identically, for EITHER
rank 0 (ker=2, coker=1) or rank 1 (ker=1, coker=0). The existing code and
preprint text do not actually distinguish these two cases.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — representation-theoretic derivation check.
NOT empirical, NOT causal.

## Falsifiable Claim

**C1 (original ambiguity, CONFIRMED by skeptic 2026-07-08):**
rank(D+|_trivial) is NOT determined by (a) the KP spectral gap on non-trivial
G2-components, plus (b) the global Atiyah-Singer index=1, plus (c) the naive
"surjectivity" assumption in kp_zero_mode.py:426. Both rank=0 and rank=1 are
consistent with (a)+(b).

**C2 (NEW, escalated hypothesis — NOT yet verified, flagged for skeptic review
before being used in any further computation or claim):**
The G2-trivial isotypic component of the domain S+⊗S- has multiplicity 2,
arising from TWO DIFFERENT tensor sub-pieces: (i) the singlet inside
(0,1)⊗(1,0) = (1,1)⊕(0,0) [i.e. the 3bar⊗3 = 8⊕1 branching], and (ii) the
"singlet x singlet" piece (0,0)⊗(0,0) coming from S+'s own trivial SU(3)-part
tensored with S-'s own trivial SU(3)-part. If the Kostant-Parthasarathy /
Frobenius-reciprocity eigenvalue formula lambda^2(rho,sigma) =
C2(G2;rho) - C2(SU(3);sigma) applies SEPARATELY and identically to each of
these two origin-pieces (both giving lambda^2=0 since both are the (0,0)_G2,
(0,0)_SU(3) pair), then D^2 = D-D+ acts as the ZERO operator on the FULL
2-dimensional multiplicity space (not just "has a zero eigenvalue somewhere
in it") -- because both basis vectors spanning that space would independently
be eigenvalue-0 eigenvectors of the same G2-equivariant operator D^2, hence so
is their span. If that reasoning is correct, then D+|_trivial is IDENTICALLY
ZERO (not partially so), forcing rank(D+|_trivial)=0, NOT 1 -- the OPPOSITE
of the paper's claim, giving dim ker(D+_{S-})=2, dim ker(D-)... (needs
adjoint recomputation) instead of dim ker(D+)=1.

**This C2 hypothesis is NOT confirmed.** It rests on an assumption I am not
certain of: that the KP/Frobenius eigenvalue formula, derived for a single
H-irreducible fiber type, applies additively/independently when the SAME
(G2-rep, SU(3)-type) pair (0,0)/(0,0) arises from two structurally different
positions in a REDUCIBLE fiber decomposition, without any additional coupling
term between them. This may be wrong — there could be an off-diagonal
"mixing" contribution between the two origin-pieces that the naive
per-piece Casimir formula does not capture, in which case D^2 on the
2-dim space could be a genuinely non-diagonal or non-zero-eigenvalue-only
2x2 matrix, and rank(D+|_trivial) could still be 1 as claimed.

## Kill Condition

- If skeptic/independent check FALSIFIES C2 (finds a concrete reason the
  per-piece additivity assumption fails, e.g. an explicit off-diagonal
  coupling term in the true KP formula for reducible fibers, or a citation
  to Kostant/Parthasarathy's original papers establishing the formula only
  applies to irreducible H-types and says nothing about cross-terms) —
  C2 is REJECTED, and the experiment reduces to resolving the original C1
  ambiguity (rank 0 vs 1, genuinely undetermined by present arguments) via
  an explicit computation (Dolan 2003 Casimir method, or direct matrix
  element of a specific spinor harmonic pairing).
- If skeptic CONFIRMS or WEAKENS-toward C2 — this is a more serious finding
  than C1 alone: it would mean the paper's central "one zero mode per
  triality channel" claim is not just under-justified but actually
  contradicted by the paper's own KP machinery, pending independent
  confirmation via explicit computation.

## Claim Entropy (Perelman)
- N_unsupported_HIGH = 1 (C2 itself, explicitly flagged as unverified)
- N_hidden_assumptions = 2 (per-piece KP additivity for reducible fibers;
  pre-existing torsion correction D^g vs D^c from E-KP1 claim.md, still open)
- N_missing_negative_controls = 0
- N_unresolved_blockers = 2

claim_entropy = 5 (higher than E-KP1's original 2 — this experiment currently
ADDS uncertainty pending verification, which is expected and honest at this
stage: a new hypothesis was generated, not yet tested)

## Next Step
Send C2 to skeptic (context-asymmetric, mode=artifact) BEFORE attempting any
further computation that assumes it. Do not build downstream conclusions on
C2 until independently checked.
