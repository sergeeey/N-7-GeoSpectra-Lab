# Preprint Abstract — S³×S⁶ Standard Model Geometry

**Draft:** 2026-06-21 (revised)
**Status:** Major revision — G73/G74A/G74B results incorporated; N_gen=3 now positive geometric result

> **⚠️ STALE — this file predates gate G102 (2026-07-05) and the L4B rank
> certification / F4 route work (through 2026-07-15).** `preprint.tex` is the
> authoritative, current source; its §sec:open correctly labels `N_gen=3` as
> *conjectured*, conditional on the open L3b channel-independence problem (an
> external Spin(8) fiber-symmetry input, not yet derived — see
> `L3B_SPIN8_INTERFACE_SPEC.md`). Two claims below are stronger than
> `preprint.tex` currently supports and should not be cited as-is: "We prove
> N_gen = 3 exactly" (line 20) and "zero-parameter prediction" (line 48, should
> read "zero-fit" and is itself conditional on `(λ, ρ₆*)` being fixed — see
> `preprint.tex` §sec:moduli). Flagged in `reports/CLAIM_BOUNDARY_AUDIT_2026-06-25.md`
> (HIGH-3) and reconfirmed in `reports/PROJECT_360_ROUND3_SYNTHESIS.md` (2026-07-15).
>
> **Additionally stale as of 2026-07-17:** predates KT-8 (full internal Dirac
> operator on S³×S⁶ has no zero mode for the round Levi-Civita S³ construction
> — see `reports/PROJECT_360_ROUND3_SYNTHESIS.md`, KT-8 through KT-11) and the
> dimension correction (total spacetime dimension is 13, not 10). The abstract
> below should not be cited for either point.

---

## Abstract

We derive the Standard Model gauge structure and fermion quantum numbers
for one generation from the geometry of S³×S⁶. By identifying the
spin connection with gauge fields (following Lawrence [2022]), we obtain the gauge
group SU(3)×SU(2)×U(1)_{B−L} and the full electric charge formula Q = T₃L + (B−L)/2
geometrically, with all 32 spinor states matching one SM generation. The gauge
coupling ratio g₂²/g₃² = 15/(16π) at equal radii agrees with the SM value at M_Z
within 4.3%. The KO-dimension 6 spectral triple structure A_F = ℂ⊕ℍ⊕M₃(ℂ)
emerges from representation theory rather than being postulated, and Yukawa
parameter count reduces to dim=4 via SU(3)-orbit degeneracy on S⁶.

We conjecture N_gen = 3, conditional on an open channel-independence problem
(L3b — see `preprint.tex` §sec:open), by the Atiyah-Singer index theorem on the internal
space S⁶ = G₂/SU(3). The negative-chirality spinor bundle S⁻ = T^{1,0}S⁶ ⊕ trivial
has c₃(S⁻) = χ(S⁶) = 2 (Chern–Gauss–Bonnet) and Â(S⁶) = 1 (since H⁴(S⁶;ℤ)=0),
giving ind(D_{S⁶}⊗S⁻) = Â(S⁶)·c₃(S⁻)/2 = 1 per triality channel. The three
channels arise from G₂ = Fix(Z₃ ⊂ Aut(𝕆)) acting on SO(8) representations
8_v, 8_s, 8_c; by Z₃ symmetry each carries c₃=2. This yields N_gen = 3×1 = 3.
The count is exact (not a lower bound): the Lichnerowicz–Weitzenböck formula
gives |F_{S⁻}|_op/(R/4) = 8/45 ≪ 1 (safety factor 5.625), eliminating accidental
zero modes; G₂-equivariance of D_{S⁶}⊗S⁻ and Schur's lemma independently cap
dim ker at 1 per channel. The sign of the index, sign(ind) = sign(c₃) = +1,
gives a left-handed zero-mode excess, geometrically fixing SM chirality. The
choice of S⁶ orientation (Z₂) is the single discrete input; standard orientation
yields the observed parity-violating weak-interaction handedness.

Proposition T1 (established earlier) closes five mechanism classes for single-bundle
N_gen selection: the χ-lemma (H²=H⁴=0 forces c₁=c₂=0, so |c₃|=χ(S⁶)=2, not 6)
eliminates large-c₃ bundles; together with the rigidity lemma this covers
topological invariants, representation theory, brane-flux quantization, SO(8)
triality (single-bundle), and stable HYM bundles. The twisted-index mechanism
above circumvents T1 not by contradicting it but by using three bundles of c₃=2
rather than one bundle of c₃=6: three channels × ind=1 = 3. Proposition T2
(untwisted Dirac on Sᵃ×Sᵇ has min eigenvalue a/2 > 0) remains valid for the
trivial bundle; the non-trivial twisted bundle S⁻ is precisely what T2 does not
cover and what G73/G74A/G74B address.

The compactification radius ρ₆ is fixed at ρ_min ≈ 1.179 (in string units) by a
zero-fit condition: Casimir and flux contributions to V(ρ₃, ρ₆) balance at a
minimum with moduli-to-KK mass ratio m_mod/m_KK ≈ 2% and κ = ρ_min/ρ* = √(7/6)
analytically (n = dim S⁶ = 6). This is a zero-fit prediction once (λ, ρ₆*) are
fixed: no SM input is used to locate ρ_min. The coupling ratio c_{1/2} = 0 along the SM constraint
(open problem; depends on Tom Lawrence's framework).

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-20 | Initial draft (doc-writer agent) |
| 2026-06-20 | "Theorem T1" → "Proposition T1" after skeptic review |
| 2026-06-20 | Attribution: "CCM program" → "Lawrence [2022]" for spin connection identification |
| 2026-06-20 | Category 3 clarified: excluded by dimensionality, not falsified |
| 2026-06-20 | 6 categories → 5 geometric mechanism classes (string excluded from count) |
| 2026-06-20 | T2 + Casimir open problem added |
| 2026-06-20 | T1 proof upgraded: "case analysis" → "2 structural lemmas" (χ-lemma + rigidity, G50) |
| 2026-06-21 | **MAJOR REVISION** — G73/G74A/G74B: N_gen=3 positive geometric result added |
| 2026-06-21 | Conclusion inverted: N_gen IS geometric (twisted Dirac), not "beyond geometry" |
| 2026-06-21 | T2 clarified: valid for untwisted; twisted S⁻ bundle is what G73 addresses |
| 2026-06-21 | Chirality added: sign(ind)=+1 → left-handed; S⁶ orientation = parity choice |
| 2026-06-21 | κ=√(7/6) analytic + ρ_min=1.179 zero-parameter prediction added |
| 2026-06-21 | T1 role reframed: closes single-bundle c₃=6 mechanisms; 3×(c₃=2) circumvents |

---

## Hard Fences (do not violate in any version)

- λ = FREE_COUPLING_PARAMETER — never claim λ is fixed
- sm_derivation_claimed = False — "one generation", not "full SM"
- No Tom Lawrence endorsement claim

---

## Key References (must-cite)

1. Tom Lawrence, arXiv:2203.09473 (2022) — foundational
2. Dolan & Nash, JHEP10(2002)041 — prior work, different manifold/method
3. Connes, Chamseddine, Marcolli, arXiv:hep-th/0610241 (2006) — CCM comparison
4. Chamseddine & Connes, CMP 186 (1997) — spectral action principle
5. Harland & Nölle, arXiv:1109.3552 (2011) — closes Proposition T1 Category 5
