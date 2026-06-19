# Null Result: G30 — G₂-Instanton Bundle → 3 Generations on S⁶

**Date:** 2026-06-20  
**Verdict:** REJECT  
**Claim:** G₂-equivariant bundle V over S⁶ with index(D⊗V) = 3

---

## Why Falsified

**G₂ symmetry theorem (proven):**

For any G₂-irreducible representation restricted to SU(3) ⊂ G₂:
```
mult(3) = mult(3̄)  always
```
This follows because the ℤ₂ automorphism of SU(3) that exchanges 3 ↔ 3̄
is INNER for G₂ (realized by an element of G₂ \ SU(3)).

From the Frobenius reciprocity formula on S⁶ = G₂/SU(3):
```
index(D⊗V_ρ) = mult(3 in ρ|SU(3)) − mult(3̄ in ρ|SU(3)) = 0
```
for every G₂-equivariant bundle V_ρ.

**Verified for: G₂(7), G₂(14), G₂(27), G₂(64), G₂(77), G₂(77')**  
Source: Slansky (1981), Physics Reports 79.

---

## Why This is Fundamental (not a loophole)

The result is not a limitation of the irreps checked — it follows from the abstract structure of G₂:
- G₂ is a simple compact Lie group with trivial center and no outer automorphisms
- All G₂-representations are "real" (have a G₂-invariant real structure)
- The complex conjugation of SU(3)-reps is inner in G₂

Any G₂-equivariant construction on S⁶ = G₂/SU(3) will have index = 0.

---

## Prior Constraint

G27 (2026-06-19): ℤ₃-orbifold approach also killed (Smith theory, χ(S⁶)=2).

Both routes to 3 generations on S⁶ are now blocked.

---

## What This Does NOT Rule Out

1. Non-equivariant bundles over S⁶ (break G₂ symmetry explicitly)
2. Three generations from S³ geometry (SU(2) adjoint = 3-dim, unexamined)
3. Three generations from GLOBAL topology of S³×S⁶ (not Dirac index on S⁶ alone)

---

## Do NOT Retry Unless

- Different compactification geometry (not S⁶ or S⁶/G₂)
- Mechanism that explicitly breaks G₂ (must be physically motivated)
- G31 approach: S³ factor provides 3 copies (requires new gate)
