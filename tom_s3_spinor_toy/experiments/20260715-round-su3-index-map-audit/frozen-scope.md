---
round_id: 20260715-round-su3-index-map-audit
date: 2026-07-15
tier: Standard-Ladder
status: open
depends_on: ../20260715-index-formula-s-tensor-t-candidate/ (PRIOR RESULT, not reopened)
---

# Frozen scope — SU(3) index map and exact-chirality audit

## Why a new round, not a rewrite

`20260715-index-formula-s-tensor-t-candidate/` already froze and closed one
falsified candidate (E=S^-⊗T^{1,0}S^6 has index 7, not 3). That experiment's
claim.md/decision.md are NOT reopened or edited here. This round consumes its
result as an external, cited fact:

```
PRIOR RESULT (cited, not re-derived):
ind(D ⊗ (S^-⊗T^{1,0}S^6)) = 7  [S-T-cand, null_results/INDEX.md]
```

Rewriting the old experiment in place would mix a candidate-specific null
result with a general index-map theorem, an irreducible gap theorem, and an
exact-chirality obstruction — three claims with different scope, different
proof status, and different failure modes. Keeping them separate preserves
change control and keeps each claim independently falsifiable.

## What this round covers

Three separately-frozen claims, each with its own claim.md, evidence, and
independent status:

- **Claim A** — general index-map identity ind(D⊗E_{p,q}) = I(p,q) for all
  SU(3) irreps (p,q), not just the 3 controls already checked.
- **Claim B** — irreducible gap theorem: I(p,q) > 0 ⟹ I(p,q) = 1 or I(p,q) ≥ 7.
- **Claim C** — exact-chirality obstruction, scoped PRECISELY to the standard
  block-diagonal homogeneous twisted Dirac operator (not "any equivariant
  operator" — see `claim-C-exact-chirality.md` for why that's a real,
  separate gap, not covered by Schur's lemma alone).

## What this round does NOT cover

- Does not reopen or re-verify the S⁻⊗T candidate itself.
- Does not attempt the general equivariant Dirac-type operator classification
  needed to close Claim C's open extension (invariant symbol / intertwiner
  classification on T*S⁶⊗V_i → V_j) — that is out of scope, flagged OPEN.
- Does not attempt the index-zero-sector vanishing proof (ker D_{E_0} = 0) —
  flagged OPEN, needed before any claim like E ≅ 3^⊕3 ⊕ E_0 can be asserted.
