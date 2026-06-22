# Three Generations from the Geometry of S³×S⁶

**Draft:** 2026-06-22 — NOT FOR DISTRIBUTION  
**Status:** Introduction complete; remaining sections placeholder

---

## Authors

Sergey Boyko  
Independent Researcher  

*In collaboration with Tom Lawrence (S³ framework, Lawrence [2022])*

---

## Abstract

*(see preprint_abstract.md — paste here before submission)*

---

## 1. Introduction

The Standard Model of particle physics contains three generations of fermions
— quarks and leptons — with identical gauge quantum numbers but widely
differing masses. Despite decades of effort, no compelling geometric or
algebraic explanation for this threefold repetition has emerged from four-dimensional
quantum field theory alone. Extra-dimensional compactifications typically leave the
generation count as a free parameter determined by the topology of the compact space;
string constructions require specific brane configurations or flux choices; and the
noncommutative geometry approach of Connes, Chamseddine, and Marcolli [CCM 2006]
takes the algebra A_F = ℂ⊕ℍ⊕M₃(ℂ) — which encodes three generations — as an
axiom rather than deriving it from first principles.

In this paper we present a candidate mathematical construction in which the
three-generation count N_gen = 3 emerges as an exact integer from the
Atiyah-Singer index theorem on the internal space S⁶ = G₂/SU(3), without
postulating it, without tuning parameters, and without any input from the
Standard Model. We work within the framework of Lawrence [2022], who showed
that identifying the spin connection of S³ with gauge fields reproduces the
Standard Model gauge group SU(3)×SU(2)×U(1) and the correct fermion quantum
numbers for one generation. Extending this construction to the product space
S³×S⁶, we find that the six-dimensional factor provides the geometric mechanism
for generation counting.

The key observation is that S⁶ = G₂/SU(3) admits a G₂-equivariant
almost-complex structure J, and the negative-chirality spinor bundle
S⁻ = T^{1,0}S⁶ ⊕ trivial carries a twisted Dirac operator D_{S⁶}⊗S⁻ whose
Atiyah-Singer index equals one per triality channel:

    ind(D_{S⁶} ⊗ S⁻) = Â(S⁶) · c₃(S⁻) / 2 = 1 · 2 / 2 = 1

The three channels arise from the automorphism G₂ = Fix(Z₃ ⊂ Aut(𝕆)) of the
octonion algebra 𝕆, which cyclically permutes the three eight-dimensional
SO(8) representations 8_v, 8_s, 8_c. Because the Z₃ eigenspaces
{1, ω, ω²} (ω = exp(2πi/3)) are mutually orthogonal, the three zero modes are
independent. The total count N_gen = 3 × 1 = 3 is exact, not a lower bound:
the Lichnerowicz–Weitzenböck formula gives a spectral gap with safety factor
5.625, eliminating accidental zero modes; G₂-equivariance of the Dirac operator
and Schur's lemma independently cap the kernel dimension at one per channel.
The sign of the index, sign(ind) = sign(c₃) = +1, places the zero mode in
D⁺ (left-handed), geometrically fixing the chirality of the weak interaction
with the single discrete input of S⁶ orientation.

Alongside the generation-counting result (Track A), we map the space of possible
geometric origins for the gauge coupling λ that appears in the non-perturbative
stabilization potential V_np ∼ exp(−λ/ρ₆²) (Track B). By a dimensional analysis
argument (Buckingham Pi theorem) combined with the analytic relation ρ₃ = κρ₆
(κ = √(7/6), derived from the modulus potential), we prove that any coupling λ
derivable from internal S³×S⁶ geometry satisfies λ = c·ρ₆² with c a pure number,
giving exp(−λ/ρ₆²) = constant — a constant provides no ρ₆-dependent force.
An exhaustive case-by-case verification (G83–G86B) confirms that the entire
geometric and spectral class of mechanisms is closed. The coupling λ is therefore
a free phenomenological parameter with non-perturbative origin (brane instantons
or gaugino condensation) outside the geometric framework of this paper.

The paper is organized as follows. Section 2 reviews the Lawrence [2022] framework
for S³ and extends it to S³×S⁶, deriving the gauge structure and electric charge
formula. Section 3 proves N_gen = 3 via the twisted Dirac index. Section 4
establishes the exact kernel count (Lichnerowicz gap + G₂-Schur) and chirality.
Section 5 presents the modulus stabilization and zero-parameter radius prediction
ρ_min ≈ 1.179. Section 6 proves the λ-dimensional obstruction. Section 7 compares
to prior work and discusses open problems.

---

## 2. The S³×S⁶ Framework

*(placeholder — derive gauge group, Q formula, SM fermion content)*

Key results to include:
- Spin connection on S³ = gauge fields (Lawrence [2022])
- SU(3)×SU(2)_L×SU(2)_R×U(1)_{B-L} from S³×S⁶ spinor decomposition
- Q = T₃L + (B-L)/2 fully geometric (G17)
- Y = K₃ + (B-L)/2 from K₃ quantum number (G16)
- Higgs bidoublet (2,2)_0 from D_F Yukawa intertwiner (G19)
- 32 spinor states = one SM generation (G17)
- g₂²/g₃² = 15/(16π) ≈ 0.298 vs SM value at M_Z ≈ 0.285 (4.3% gap)
- NCG spectral triple KO-dim 6: A_F = ℂ⊕ℍ⊕M₃(ℂ) derived (G18-G22)

---

## 3. N_gen = 3 from Twisted Dirac Index

*(placeholder — Lemmas L1-L3 from THEOREM_PACK.md)*

Key results:
- L1: S⁻ = T^{1,0}S⁶ ⊕ trivial, G₂-equivariant
- L2: c₃(S⁻) = χ(S⁶) = 2, Â(S⁶) = 1, ind = 1
- L3: Three Z₃ eigenspaces, orthogonal zero modes, N_gen = 3

---

## 4. Exact Kernel and Chirality

*(placeholder — Lemmas L4, L5 from THEOREM_PACK.md)*

Key results:
- L4A: Lichnerowicz gap |F_{S⁻}|/(R/4) = 8/45 ≪ 1
- L4B: G₂-Schur → dim ker ≤ 1 per channel
- L4 corollary: dim ker(D⁻) = 0 exactly
- L5: sign(ind) = +1 → left-handed zero mode

---

## 5. Modulus Stabilization

*(placeholder — G62-G66 results)*

Key results:
- V_flux = g₂²/g₃² × ρ₃³/ρ₆⁶
- Casimir correction: 0.24% of V_flux
- ρ₆_min = 1.179, κ = √(7/6) analytic (G66)
- Zero-parameter prediction: no SM input used

---

## 6. The λ-Dimensional Obstruction

*(placeholder — Track B summary + Corollary C1)*

Key results:
- C1: λ_geom = c·ρ₆² on trajectory → exp(−λ/ρ₆²) = const
- G83-G84B: gauge reduction → power-law, not 1/ρ₆²
- G85B: spectral saddle → exp(−3) = const
- G86A: structural theorem — Laplace integrals always power-law
- G86B: warp factor → trivial or power-law + free Q
- Hodge corollary: H³(S³×S⁶) = ℝ from S³; b₃(S⁶) = 0
- Conclusion: λ = FREE_COUPLING_PARAMETER

---

## 7. Comparison and Open Problems

*(placeholder)*

**Comparison to CCM [2006]:**
| Feature | CCM approach | This work |
|---------|-------------|-----------|
| N_gen = 3 | Postulated (A_F axiom) | Derived (Dirac index) |
| SM gauge group | Derived from A_F | Derived from S³ spin connection |
| Chirality | Postulated (J_F) | Derived from sign(ind) = sign(c₃) |
| Yukawa count | 4 free parameters | 4 parameters (SU(3)-orbit, G20) |
| Coupling λ | Not addressed | Free parameter, origin non-perturbative |

**Comparison to Dolan & Nash [2002]:**
Different internal space (ℂP³ vs S⁶), different index mechanism. Generation count
not derived in Dolan-Nash; they derive SM representations from ℂP³ geometry.

**Open problems:**
1. G72: Triality bundle 8_v construction (requires independent input)
2. Three-generation mass hierarchy: beyond geometric framework
3. Full gauge coupling λ: non-perturbative mechanism (brane instantons or gaugino)
4. Universality: does L4 (Lichnerowicz + G₂-Schur) extend to nearly Kähler 6-manifolds?
5. External mathematical review of L1–L5 (especially L4B G₂-Schur scope)

---

## References

[Lawrence 2022] T. Lawrence, arXiv:2203.09473 (2022)  
[Dolan-Nash 2002] B.P. Dolan, C. Nash, JHEP 10 (2002) 041  
[CCM 2006] A. Chamseddine, A. Connes, M. Marcolli, arXiv:hep-th/0610241  
[Chamseddine-Connes 1997] A. Chamseddine, A. Connes, CMP 186 (1997) 731  
[Harland-Nölle 2011] D. Harland, C. Nölle, arXiv:1109.3552  
[Atiyah-Singer 1963] M.F. Atiyah, I.M. Singer, Bull. AMS 69 (1963) 422  
[Milnor 1963] J. Milnor, Morse Theory, Princeton University Press  
[Buckingham 1914] E. Buckingham, Phys. Rev. 4 (1914) 345  

---

## Hard Fences (enforced by test_markdown_claim_audit.py)

- λ = FREE_COUPLING_PARAMETER — not fixed by geometry
- sm_derivation_claimed = False — one generation only
- N_gen=3 is a candidate mathematical construction; external review pending
- No Tom Lawrence endorsement claimed
