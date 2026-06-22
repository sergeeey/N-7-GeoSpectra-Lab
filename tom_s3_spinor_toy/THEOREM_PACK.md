# Theorem Pack — S³×S⁶ Fermion Generation Mechanism

**Date:** 2026-06-22
**Status:** Five lemmas supporting N_gen = 3 and chirality from twisted Dirac index on S⁶.

**Scope:** One SM-like generation; full SM gauge group NOT claimed (see hard fences in
preprint_abstract.md). These lemmas are a candidate mathematical construction requiring
independent external review.

---

## Five Lemmas

### L1 — Geometry of S⁶

**Statement:**
S⁶ = G₂/SU(3) admits a G₂-equivariant almost-complex structure J. The negative-chirality
spinor bundle is S⁻ = T^{1,0}S⁶ ⊕ trivial, where T^{1,0}S⁶ is the holomorphic tangent
bundle of the almost-Kähler structure on S⁶.

**Supporting gates:** G67 (G₂=Fix(Z₃)), G17-G19 (SU(3) rep content), G21 (Schur dim)

**Formal failure condition:**
Lemma L1 fails if the almost-complex structure on S⁶ is not G₂-equivariant, or if S⁻
is not well-defined as a G₂-equivariant bundle. (Known risk: S⁶ does not admit a
*integrable* complex structure; the almost-complex structure is sufficient for the
Dirac operator, but a reviewer may dispute this.)

---

### L2 — Chern Class and Atiyah-Singer Index

**Statement:**
For the bundle E = S⁻ = T^{1,0}S⁶ ⊕ trivial on S⁶:

    c₃(S⁻) = χ(S⁶) = 2      (Chern–Gauss–Bonnet)
    Â(S⁶)  = 1               (since H²(S⁶;ℤ) = H⁴(S⁶;ℤ) = 0)

By the Atiyah-Singer index theorem:

    ind(D_{S⁶} ⊗ S⁻) = Â(S⁶) · c₃(S⁻) / 2 = 1 · 2 / 2 = 1

This holds *per triality channel* (see L3).

**Supporting gates:** G73 (index computation 29/29 tests), G33 (χ(S⁶)=2, χ-lemma)

**Formal failure condition:**
Lemma L2 fails if c₃(T^{1,0}S⁶) ≠ χ(S⁶), or if the Atiyah-Singer normalization
convention differs (factor of 2 risk). Verify: `experiments/20260621-g73-three-channel-dirac/`.

---

### L3 — Triality Channel Independence

**Statement:**
The Z₃ triality automorphism of SO(8) (= the automorphism of the octonion algebra 𝕆)
fixes the subgroup G₂ = Fix(Z₃) and cyclically permutes the three 8-dimensional
SO(8) representations:

    Z₃ : 8_v ↔ 8_s ↔ 8_c ↔ 8_v

Each channel carries a twisted Dirac operator D_{S⁶}⊗S⁻. The three zero-mode spaces
lie in distinct Z₃-eigenspaces with eigenvalues {1, ω, ω²} where ω = exp(2πi/3).
By orthogonality of Z₃ eigenspaces (Z₃ is unitary), the three zero modes are INDEPENDENT
and do not overlap. Total: N_gen = 3 × 1 = 3.

**Supporting gates:** G67 (G₂=Fix(Z₃), 25/25), G73 (ind=1 per channel), G75 (independence, PROMOTE)

**Formal failure condition:**
Lemma L3 fails if the three channels are equivalent as G₂-representations and their
zero modes coincide (i.e., one zero mode counted three times). The Z₃ eigenspace
argument is the key defense: distinct eigenvalues {1, ω, ω²} guarantee orthogonality.
See `experiments/20260622-g75-triality-independence/` for explicit verification.

---

### L4 — Exact Kernel: dim ker(D⁻) = 0

**Statement:**
The index theorem gives:

    dim ker(D⁺) − dim ker(D⁻) = ind = 1

Two independent lemmas together prove dim ker(D) = 1 EXACTLY per channel,
hence dim ker(D⁺) = 1 and **dim ker(D⁻) = 0**:

**Lemma 4A (Lichnerowicz–Weitzenböck spectral gap):**
The Weitzenböck formula gives (D⊗S⁻)² ≥ R/4 + F_{S⁻}. On round S⁶:
- Scalar curvature: R = 30/ρ₆²
- Bundle curvature: |F_{S⁻}|_op ≤ (4/3)/ρ₆²  (SU(3) Casimir for 3-rep)
- Ratio: |F_{S⁻}|/(R/4) = 8/45 ≈ 0.178 ≪ 1  (safety factor 5.625)

Since |F_{S⁻}| < R/4, the Weitzenböck inequality gives no zero modes other than
the one forced by the index → dim ker(D⊗S⁻) = 1.

**Lemma 4B (G₂-Schur cap):**
D_{S⁶}⊗S⁻ is G₂-equivariant. By Schur's lemma, ker(D⁺) is a G₂-submodule.
Since the zero-mode representation is irreducible (SU(3) singlet = trivial rep),
dim ker(D⁺) ≤ multiplicity of trivial rep in the zero mode space = 1.

**Corollary: dim ker(D⁻) = 0 exactly.**
Proof: index = 1 → dim ker(D⁺) - dim ker(D⁻) = 1.
Lemma 4A + 4B → dim ker(D) = dim ker(D⁺) + dim ker(D⁻) = 1.
Therefore dim ker(D⁺) = 1 and dim ker(D⁻) = 0.

**Supporting gates:** G74A (30/30), G74B (31/31)

**Formal failure condition:**
Lemma L4 fails if:
(a) The Lichnerowicz gap ratio 8/45 has a sign or normalization error, OR
(b) The G₂-Schur argument does not apply because the zero mode carries a
    non-trivial G₂ representation (not the singlet), OR
(c) The Weitzenböck formula has curvature correction terms on S⁶ that were omitted.

---

### L5 — Chirality from Index Sign

**Statement:**
The sign of the Atiyah-Singer index determines which chirality carries zero modes:

    sign(ind) = sign(c₃(S⁻)) = sign(+2) = +1

A positive index means:

    dim ker(D⁺) > dim ker(D⁻)

Since dim ker(D⁻) = 0 (L4) and dim ker(D⁺) = 1, the zero mode is LEFT-HANDED.
This geometrically fixes SM chirality: parity violation arises from the sign of c₃,
controlled by the orientation of S⁶. The single discrete input is the orientation (Z₂);
standard orientation → left-handed weak interactions.

**Supporting gates:** G74B (sign(ind)=+1, 31/31), G23 (chirality from gauge sectors)

**Formal failure condition:**
Lemma L5 fails if:
(a) The orientation convention for S⁶ differs from the SM convention for chirality, OR
(b) "Left-handed" in the Dirac index sense does not map to "left-handed" in the SM
    weak-isospin sense (convention mismatch risk), OR
(c) The sign of c₃ is not uniquely determined by geometry without additional input.

---

## Summary Table

| Lemma | Statement | Gate | Failure mode | Status |
|-------|-----------|------|--------------|--------|
| L1 | S⁶ = G₂/SU(3), S⁻ bundle defined | G67, G17-G24 | Non-integrable J is insufficient | PROMOTE |
| L2 | ind = Â·c₃/2 = 1 per channel | G73, G33 | Normalization factor of 2 | PROMOTE |
| L3 | Three Z₃ eigenspaces independent | G67, G73, G75 | Channels equivalent → 1 mode × 3 labels | PROMOTE |
| L4 | dim ker(D⁻) = 0 exactly | G74A, G74B | Lichnerowicz normalization / G₂-Schur scope | PROMOTE |
| L5 | sign(ind)=+1 → left-handed | G74B, G23 | Convention mismatch L↔R | PROMOTE |
| C1 | λ_geom = c·ρ₆² → exp(−λ/ρ₆²) = const (Track B meta-result) | LAMBDA-DIM-GATE | New scale Λ_NP ≠ ρ₆ → not geometric | PROMOTE |

**Chain:** L1 ⊢ L2 ⊢ (L3 ∥ L4) ⊢ L5 → N_gen = 3 exactly with left-handed chirality.

**Track B structural result:** C1 → λ = FREE_COUPLING_PARAMETER (geometric derivation structurally impossible).

---

## What This Does NOT Mean

1. Does NOT prove the full Standard Model (one generation only; `sm_derivation_claimed = False`)
2. Does NOT fix the gauge coupling λ (`λ = FREE_COUPLING_PARAMETER`)
3. Does NOT imply G73/G74A/G74B have been externally verified by a mathematician
4. Does NOT exclude other mechanisms that could also give N_gen = 3
5. Does NOT replace a rigorous peer-reviewed proof

---

## Corollary C1 — λ-Dimensional Obstruction (Track B Meta-Result)

**Statement:**
Any coupling λ derivable from internal S³×S⁶ geometry satisfies λ = c·ρ₆² on the
compactification trajectory (where ρ₃ = κρ₆, κ = √(7/6) fixed by G66). Therefore:

    exp(−λ_geom/ρ₆²) = exp(−c·κᵃ) = constant (∀ a, c)

No geometric/spectral mechanism produces a non-trivial ρ₆-dependent exponential.

**Proof sketch (Buckingham Pi):**
[λ] = [length²]. Internal scales = {ρ₃, ρ₆}. Most general form: λ = c·ρ₃ᵃ·ρ₆^(2−a).
On trajectory ρ₃ = κρ₆: λ = c·κᵃ·ρ₆². Then exp(−λ/ρ₆²) = exp(−c·κᵃ) = const. □

**Hodge corollary (Künneth):**
H³(S³×S⁶) = H³(S³) = ℝ. The harmonic 3-form flux threads S³ (topologically quantized);
S⁶ has b₃ = 0 (no harmonic 3-forms). The flux potential scales as Vol(S³)/Vol(S⁶),
not as a flux quantum from S⁶ — consistent with C1.

**Supporting gate:** `experiments/20260622-lambda-dim-gate/`

**Formal failure condition:**
C1 fails if the compactification trajectory has ρ₃ ≠ κρ₆ (ratio is not fixed), OR
if a geometric mechanism introduces a new scale Λ_NP hidden inside {ρ₃, ρ₆} labeling.

---

## External Review Checklist

For a mathematical referee:
- [ ] L1: Is G₂-equivariant almost-complex structure sufficient for Atiyah-Singer?
- [ ] L2: Is c₃(T^{1,0}S⁶) = χ(S⁶) = 2 (not 6 or another value)?
- [ ] L3: Are the three Z₃ eigenspaces truly orthogonal zero-mode spaces, or do they collapse?
- [ ] L4A: Is the Lichnerowicz gap ratio 8/45 correctly computed with S⁶ curvature?
- [ ] L4B: Does G₂-equivariance + Schur → dim ker ≤ 1 (not just dim ker_irred ≤ 1)?
- [ ] L5: Does sign(c₃) correctly fix SM chirality (not just Dirac chirality)?

**Nearest prior work:** Dolan & Nash, JHEP10(2002)041 — SM fermions from CP spaces via
Dirac index. Different manifold (ℂP³, not S⁶), different index mechanism, result comparable.
