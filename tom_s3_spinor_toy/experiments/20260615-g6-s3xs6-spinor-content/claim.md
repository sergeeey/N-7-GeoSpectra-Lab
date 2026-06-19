# G6 — Claim: 32-component S³×S⁶ spinor = one SM generation

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:** The Dirac spinor on S³×S⁶, decomposed under the Pati-Salam identification
`SO(4)≅SU(2)_L×SU(2)_R` (from S³) and `SO(6)≅SU(4)→SU(3)_c×U(1)_{B-L}` (from S⁶),
with hypercharge `Y = T3R + (B-L)/2`, yields EXACTLY 32 states that match one full Dirac
generation of SM fermions (particle + antiparticle): all 16 labels present, correct
multiplicities (quarks×3 colors, leptons×1).

**Check:** `python g6_spinor_decomposition.py` → `PASS_G6_SM_CONTENT_CONFIRMED`, `32/32 matched`

**Caveat / What this does NOT mean:**
1. Does NOT prove these are zero modes — only that the representation theory is consistent
2. Does NOT explain why THREE generations appear (not one)
3. Does NOT fix λ or any coupling constant
4. Does NOT use the actual metric on S³×S⁶ — this is a weight-space / algebra-level check
5. Does NOT prove the Pati-Salam identification is the correct one (assumed from S6-BRANCH-G0)

**Key formula:** `Y = T3R + (B-L)/2`  (standard Pati-Salam hypercharge)

**Inputs from prior gates:**
- S³: SO(4)≅SU(2)_L×SU(2)_R splitting — from P5/P6 (Tom rows 5-6)
- S⁶ G0: 8 spinor weights (±½,±½,±½) — VERIFIED-sympy 7/7
- S⁶ S6-BRANCH-G0: SU(4)→SU(3)×U(1), rational charges — VERIFIED-sympy 7/7
- Pati-Salam formula — standard (Pati-Salam 1974)

**Result table (summary):**
```
Sector          | States | Content
────────────────|--------|────────────────────────────────
S³+ × S⁶ S+    |  8     | (2_L, 3)_{1/6} + (2_L, 1)_{-1/2}  = Q_L + L
S³+ × S⁶ S-    |  8     | (2_L, 3̄)_{-1/6} + (2_L, 1)_{1/2} = Q̄_L + L̄
S³- × S⁶ S+    |  8     | (1_L, 3)_{2/3,−1/3} + (1_L, 1)_{0,−1} = u_R,d_R + ν_R,e_R
S³- × S⁶ S-    |  8     | (1_L, 3̄)_{−2/3,1/3} + (1_L, 1)_{0,+1} = ū_R,d̄_R + ν̄_R,ē_R
────────────────|--------|────────────────────────────────
Total           | 32     | 1 full Dirac generation (particle+antiparticle)
```

**Status:** PASS [VERIFIED-sympy, 2026-06-15]
