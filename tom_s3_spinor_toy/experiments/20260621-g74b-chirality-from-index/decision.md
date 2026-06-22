# G74B decision — PROMOTE (SM chirality from index sign)

**Date:** 2026-06-21
**Verdict:** PROMOTE — SM left-handed chirality is geometric

## Summary (31/31 tests pass)

**Claim:** sign(ind(D^+_{S⁶}⊗S⁻)) = sign(c₃(S⁻)) = +1 → LEFT_HANDED_EXCESS.
Combined with G74A (dim ker = 1 per channel): unique solution L=1, R=0 per channel.

## Index sign argument

The twisted Dirac has two chirality sectors:
```
D^+: S⁺⊗E → S⁻⊗E     (positive → negative chirality)
D^-: S⁻⊗E → S⁺⊗E     (negative → positive chirality, = (D^+)†)
```

Atiyah-Singer: ind(D^+⊗E) = dim ker(D^+) - dim ker(D^-)

From G74A: dim ker(total) = dim ker(D^+) + dim ker(D^-) = 1 (per channel).
From G73: ind = dim ker(D^+) - dim ker(D^-) = +1 (per channel).

System of two equations, two unknowns:
```
dim ker(D^+) + dim ker(D^-)  = 1   (from G74A)
dim ker(D^+) - dim ker(D^-)  = +1  (from G73, ind=+1)
```
Unique solution: **dim ker(D^+) = 1, dim ker(D^-) = 0** → **L=1, R=0** per channel.

Three channels: 3×(L=1, R=0) → **3 left-handed zero modes, 0 right-handed**.

## Sign from Chern class

ind = Â(S⁶)·c₃(S⁻)/2 = 1·(+2)/2 = **+1**

c₃(S⁻) = +2 > 0 (positive, from G33: χ(S⁶)=+2 with standard orientation).
**The orientation of S⁶ is the single discrete input.** Standard (positive) orientation
gives c₃ > 0 → ind > 0 → left-handed excess = observed SM chirality.
Reversed orientation: ind → -1 → right-handed excess (unphysical).

## Relationship to G23

**G23 (NCG result):** {D_F, γ_F} = 0 → SU(2)_L gauge symmetry acts on the left sector;
SU(2)_R would act on the right sector. SM only has SU(2)_L → chirality from gauge structure.

**G74B (Atiyah-Singer result):** ind > 0 → more L zero modes than R. Pure spinor counting.

These two results are CONSISTENT but INDEPENDENT:
- G23 derives chirality from gauge-sector representation theory (NCG framework)
- G74B derives chirality from the index of the Dirac operator (Atiyah-Singer)
- Together they provide independent cross-validation of SM chirality from S³×S⁶

## Skeptic concerns addressed

- **Concern:** Isn't the orientation choice just choosing the answer by hand?
  → **Dismissed:** The orientation is a discrete geometric input (Z₂) analogous to choosing
  an orientation for any spin manifold. It is not a continuous parameter or a fit.
  The claim is: "given the geometric orientation of S⁶ compatible with the coset G₂/SU(3),
  the chirality is left-handed." This is one binary choice, not tuning.

- **Concern:** Could there be additional right-handed zero modes from other bundles?
  → **Dismissed:** G74A and the G₂-Schur bound are exhaustive for D_{S⁶}⊗S⁻. Additional
  bundles would require additional physical input beyond the S³×S⁶ geometry.

## What this does NOT mean

1. Does NOT prove parity violation from first principles — the orientation choice (Z₂) is an
   input. The claim is that parity violation is encoded in the orientation, not derived from it.
2. Does NOT explain WHY nature chose left-handed over right-handed — only that S³×S⁶ with
   standard orientation gives left-handed.
3. Does NOT establish the DYNAMICS of chirality breaking — this is geometric/topological.

## Chain

- Depends on: G73 (ind=+1), G74A (dim ker=1), G23 (independent chirality check)
- Closes: N_gen=3 question completely (G73: lower bound → G74A: exact → G74B: chirality)
- Used by: preprint_abstract.md

## Test summary

31 tests pass. Tests cover: chirality sector equations, unique solution (L=1, R=0),
sign of c₃ and its effect on ind, orientation reversal (anti-chirality), consistency
with G23 (different mechanism, same conclusion), three-channel multiplication.
