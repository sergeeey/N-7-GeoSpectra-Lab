# G67 decision — PROMOTE (SO(8) triality → 3 independent channels)

**Date:** 2026-06-21
**Verdict:** PROMOTE — three independent triality channels established

## Summary (25/25 tests pass)

**Claim:** G₂ = Fix(Z₃ ⊂ Aut(𝕆)) acting on SO(8) triality defines three independent
Dirac channels (8_v, 8_s, 8_c) each carrying identical topological content c₃=2.

| Channel | SO(8) rep | c₃ | G₂ content |
|---------|-----------|-----|------------|
| 8_v | vector | 2 | 7 + 1 (adjoint + singlet) |
| 8_s | spinor | 2 | 8 (fundamental) |
| 8_c | co-spinor | 2 | 8 (co-fundamental) |

**Z₃ triality:** The outer automorphism Z₃ ⊂ Aut(𝕆) permutes 8_v, 8_s, 8_c cyclically.
Since topological invariants (c₃) are preserved by automorphisms, c₃ is the same for all three.
G₂ = Fix(Z₃): the symmetry preserved by all three channels simultaneously.

## Key findings

1. **Three independent channels:** Not three copies of one channel — three inequivalent SO(8) reps
   related by Z₃ outer automorphism. All have the same G₂-content because G₂ = Fix(Z₃).

2. **c₃ equality:** c₃(8_v) = c₃(8_s) = c₃(8_c) = 2. Established by Z₃ triality preserving
   all Chern classes plus the identification c₃=χ(S⁶)=2 from G33.

3. **SU(3) roots verified:** A₂ root system axioms confirmed for generators embedded in G₂.

## Skeptic concerns addressed

- **Concern:** Are 8_v, 8_s, 8_c genuinely independent, not just copies?
  → **Dismissed:** they are inequivalent as SO(8) representations. 8_v has trace=8 for identity
    but different eigenvalue structure from 8_s and 8_c under the Cartan subalgebra.
- **Concern:** Does triality really preserve c₃?
  → **Accepted:** Z₃ acts as an outer automorphism of Lie(SO(8)). As a bundle automorphism,
    it preserves all Pontryagin/Chern classes. This is the standard result.

## What this does NOT mean

1. Does NOT mean all three channels are physically distinct in 4D — their physical
   realization in the 4D effective theory is subject to G72 (geometric realization of E_v).
2. Does NOT select N_gen=3 by itself — that requires G73 (each channel has ind=1).
3. Does NOT work on manifolds without G₂ holonomy structure.

## Chain

- Depends on: G33 (c₃=χ(S⁶)=2), G50 (χ-lemma)
- Used by: G73 (ind=1 per channel × 3 channels), G74A (G₂-Schur), G74B (chirality)

## Test summary

25 tests pass. Tests cover: Z₃ permutation algebra, c₃ equality under triality,
G₂ root system axioms (A₂), SO(8) rep dimensions, Fix(Z₃)=G₂ rank check.
