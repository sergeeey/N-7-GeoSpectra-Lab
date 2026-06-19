# G8 — Claim: chirality obstruction on round S³×S⁶ (Witten problem)

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:** The round product S³×S⁶, with no gauge background, cannot produce a net
chirality of 4D fermions. Three independent facts establish this:
- (A) Künneth cohomology: b₁(S³×S⁶) = b₂(S³×S⁶) = 0 → no Wilson lines, no abelian flux.
- (B) The Dirac spectrum on each factor is ±-symmetric → index = 0 → zero net chirality.
- (C) S³×S⁶ is simply connected → confirms Hosotani is impossible (unlike S³×S¹).

**Check:** `python g8_chirality_obstruction.py` → `PASS_G8_CHIRALITY_OBSTRUCTION_QUANTIFIED`

**Key results (VERIFIED-sympy):**
- P(S³×S⁶) = (1+t³)(1+t⁶) = 1 + t³ + t⁶ + t⁹ → b₀=b₃=b₆=b₉=1, **b₁=b₂=0**
- Contrast P(S³×S¹) = (1+t³)(1+t) → **b₁=1** (this is why BG-H1 could use Hosotani)
- S⁶ spectrum ±(n+3)/ρ : index = 0, zero modes = 0
- S³ spectrum ±(m+3/2)/ρ : index = 0, zero modes = 0
- dim(G₂/SU(3)) = 14 − 8 = 6 = dim S⁶ (coset structure dimensionally consistent)

**Escape route (NOT computed — structural insight):**
- [DOCS] S⁶ = G₂/SU(3) is a coset (nearly-Kähler); KK on a coset G/H carries a
  canonical H-connection = a non-trivial gauge background.
- [INFERRED] This SU(3) coset connection is the extra structure that can evade the
  obstruction (give index ≠ 0), and is naturally identified with SU(3)_color (G6).
- [UNKNOWN] Whether it yields exactly three generations.

**Caveat / What this does NOT mean:**
1. Does NOT prove Tom's theory fails — it identifies the central mechanism still needed.
2. The coset SU(3) escape is INFERRED, not computed. Other routes exist (warping,
   SUGRA form-flux, torsion). G8 does not select among them.
3. "Index = 0" here is for the round metric WITHOUT gauge background. With the coset
   connection the relevant (twisted) index can differ — that computation is future work.
4. The 4D-chirality interpretation has dimension subtleties (S³×S⁶ internal = 9D);
   G8 establishes the obstruction at the level of spectrum symmetry + cohomology, which
   is robust regardless of those subtleties.

**Why this is valuable (even though negative):**
This is the Witten-1981 chirality problem made concrete for Tom's specific geometry.
It sharpens the single most important open question: what provides the chiral
asymmetry? G6 (rep content) + G7 (mass tower) + G8 (chirality obstruction) together
map exactly where the theory stands and what the next mechanism must do.

**Inputs from prior gates:**
- S⁶ spectrum ±(n+3)/ρ — G4 PASS [VERIFIED-sympy]
- S³ spectrum, SM content — P5/G2, G6 PASS [VERIFIED-sympy]
- S³×S¹ Hosotani zero mode (b₁=1 enables it) — BG-H1 COMPLETE

**Status:** PASS_G8_CHIRALITY_OBSTRUCTION_QUANTIFIED [VERIFIED-sympy, 2026-06-15, 12/12 pytest]
