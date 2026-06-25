---
experiment_id: 20260625-l3-partial
date: 2026-06-25
tier: Full-Ladder
status: in_progress
---

# claim.md — E-L3-PARTIAL: ind=1 for all three SO(8) triality channels

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — G₂ representation theory + Atiyah–Singer index

## Falsifiable Claims

**C1 (Branching rule):** All three SO(8) triality representations 8_v, 8_s, 8_c
restrict to the SAME G₂-module: (1,0)_G₂ ⊕ (0,0)_G₂ = 7⊕1 (dim=8).

**C2 (SU(3) decomposition):** Under the maximal subgroup SU(3) ⊂ G₂:
7_G₂|_{SU(3)} = (1,0)⊕(0,1)⊕(0,0) = 3⊕3̄⊕1 (dim=7).
Hence each channel|_{SU(3)} = (1,0)⊕(0,1)⊕2×(0,0) (dim=8).

**C3 (Direct summand):** The S⁻-subbundle with fiber (1,0)⊕(0,0) is a direct
summand of the SU(3)-module of each channel.

**C4 (ind per channel):** By E-KP1 (KP spectral gap), ind(D⊗S⁻-component) = 1.
Since all three channels have IDENTICAL S⁻-subbundle at the SU(3)-level,
this computation applies identically: ind=1 for each of the three channels.

**C5 (Triality):** The ℤ₃ outer automorphism of SO(8) that cyclically permutes
8_v ↔ 8_s ↔ 8_c has G₂ = Fix(ℤ₃) as its fixed subgroup. The Atiyah–Singer
index, being a topological invariant, is preserved under this symmetry.
Hence ind(D⊗E_α) = 1 for α=0,1,2.

## What This Does NOT Mean (mandatory)

1. Does NOT prove channel independence (the open part of L3).
2. Does NOT prove that the three S⁻-subbundles are non-isomorphic as
   G₂-equivariant bundles — all three have the same SU(3)-module.
3. Does NOT by itself imply N_gen=3 (that requires independence, i.e., full L3).

## Kill Condition

C4 is FALSIFIED if:
- The KP gap fails for the S⁻-subbundle of some channel (impossible — same SU(3)-module)
- The branching rule C1 is wrong (standard rep theory, well-established)

## Remaining Open Question (full L3)

The three S⁻-subbundles are at the SU(3)-level identical. Distinguishing them
requires G₂-level or SO(8)-level structure, e.g.:
- Explicit bundle construction E_α = S⁻ ⊗ ρ_α where ρ_α are 1-dim ℤ₃-characters
- Or an SO(8) representation-theoretic argument

This requires Tom Lawrence's input on the explicit bundle construction (his
expertise in invariant spinors on homogeneous spaces).
