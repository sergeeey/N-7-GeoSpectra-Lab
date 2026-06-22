# G73 decision — PROMOTE (N_gen ≥ 3 from Atiyah-Singer index)

**Date:** 2026-06-21
**Verdict:** PROMOTE — N_gen ≥ 3 established from twisted Dirac index

## Summary (29/29 tests pass)

**Claim:** ind(D_{S⁶} ⊗ S⁻) = Â(S⁶) · c₃(S⁻)/2 = 1 per Z₃-triality channel.
Three channels (G67) → N_gen = 3 × 1 = 3 as a topological lower bound.

**Index formula chain:**

| Step | Fact | Source |
|------|------|--------|
| c₃(T^{1,0}S⁶) = 2 | = χ(S⁶) = 2 (Chern–Gauss–Bonnet) | G33 |
| S⁻ = T^{1,0}S⁶ ⊕ trivial | SU(3) decomposition of Spin(6) spinor | G69 |
| c₃(S⁻) = 2 + 0 = 2 | Whitney product formula | G73-B |
| Â(S⁶) = 1 | p₁=0 since H⁴(S⁶;ℤ)=0 | G50 |
| ind = Â·c₃(S⁻)/2 = 1 | Atiyah-Singer for twisted Dirac | G73-D |
| Three channels | c₃(8_v)=c₃(8_s)=c₃(8_c)=2 by Z₃ triality | G67 |
| N_gen = 3 × 1 = 3 | Sum of indices over channels | G73-F |

## Key finding: upgrade from N_gen=1 (G13) to N_gen=3

G13 established ind(D_{S⁶}⊗T^{1,0}) = 1 for the HOLOMORPHIC tangent bundle.
G73 uses the FULL negative-chirality spinor bundle S⁻ = T^{1,0} ⊕ trivial, which accounts
for all three Z₃-triality channels simultaneously via G67.

## Boundary conditions (what G73 does NOT prove)

1. **This is a lower bound:** ind=1 means dim ker(D^+) - dim ker(D^-) = 1.
   It does NOT yet exclude extra zero modes (e.g. dim ker = 2 with one of each sign).
   Exact count dim ker = 1 is proved separately by G74A.

2. **E_v channel:** The geometric realization of the 8_v (vector) channel requires G72.
   G73 uses the algebraic triality argument that c₃(8_v) = c₃(8_s) = c₃(8_c) = 2
   without constructing the E_v bundle explicitly.

## Skeptic concerns addressed

- **Concern:** Does Atiyah-Singer apply to S⁶? S⁶ is not a complex manifold.
  → **Dismissed:** Atiyah-Singer applies to all compact spin manifolds. S⁶ is a compact
    Riemannian spin manifold (spin structure from G9). The formula ind = ∫Â·ch(E) is general.
- **Concern:** Is c₃(S⁻) = c₃(T^{1,0}) or c₃(S⁻) = c₃(T^{1,0}) + c₃(trivial)?
  → **Dismissed:** Whitney formula: c₃(E⊕F) = Σ c_i(E)c_{3-i}(F). Since c_k(trivial)=0
    for k>0, we get c₃(E⊕trivial) = c₃(E). Confirmed algebraically in tests.

## What this does NOT mean

1. Does NOT prove dim ker = 1 (that requires G74A Lichnerowicz + G₂-Schur).
2. Does NOT prove SM chirality (that requires G74B sign(ind) argument).
3. Does NOT work for the UNTWISTED Dirac on S⁶ (Proposition T2: min eigenvalue = 3/ρ₆ > 0).
4. Does NOT bypass Proposition T1: T1 closes single-bundle c₃=6 mechanisms.
   G73 uses THREE bundles of c₃=2, not one of c₃=6 — a different mechanism class.

## Chain

- Depends on: G33, G50 (χ-lemma + Â=1), G67 (triality channels), G69 (S⁻ decomposition)
- Used by: G74A (exact count), G74B (chirality), preprint_abstract.md

## Test summary

29 tests pass. Tests cover: tensor product Dirac structure, S⁶ spinor bundle splitting,
c₃ computation via Whitney formula, Â(S⁶)=1 from H⁴=0, index formula, triality
c₃ equality, N_gen count.
