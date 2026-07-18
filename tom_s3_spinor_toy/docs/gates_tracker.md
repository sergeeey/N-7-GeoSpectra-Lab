# Gates Tracker — S³×S⁶ Research Results

**Source of truth** — edit here, then run `python scripts/export_results.py` to regenerate Excel/PDF.

```
python scripts/export_results.py --excel   → docs/exports/gates_tracker.xlsx
python scripts/export_results.py --pdf     → docs/exports/gates_tracker.pdf
python scripts/export_results.py --all     → both
```

**Hard constraints (never remove):**
- `lambda = FREE_COUPLING_PARAMETER`
- `sm_derivation_claimed = False`
- `safe_for_runtime = False`

**Last updated:** 2026-07-07 | **Tests:** 2484 passed, 4 skipped

---

## Table

<!-- Parser anchor — do not remove this line -->
| Gate | Section | Claim (one line) | Status | Key Result / Formula | Tests | Date |
|------|---------|-----------------|--------|----------------------|-------|------|
| G6 | Fermion Chain | 32-component spinor = 1 SM generation under SO(4)×G₂ | PASS | 32/32 states matched; all quantum numbers correct | 6/6 | 2026-06-15 |
| G7 | Fermion Chain | KK mass spectrum on S³×S⁶ from Lichnerowicz | PASS | M²_{mn} = (n+3/2)²/ρ₃² + m²/ρ₆²; gap confirmed | 8/8 | 2026-06-15 |
| G8 | Fermion Chain | Chirality obstruction on round S³×S⁶ | PASS | b₁=b₂=0; Atiyah-Singer index=0 on untwisted bundle | 6/6 | 2026-06-15 |
| G9 | Fermion Chain | Coset chirality: G₂/SU(3) gives SU(3) action on S⁶ | PASS | G₂/SU(3) = S⁶; SU(3) acts isometrically | 4/4 | 2026-06-15 |
| G10 | Gauge Structure | S⁶ spin connection → SO(6) gauge field | PASS | so(6)≅su(4); 15 generators; cross-spectator effect. **Caveat (added 2026-07-17, round120, per gate G97):** this is the spin-connection's structure algebra, not a claim that all 15 generators are realized as an isometry-derived gauge symmetry — only SU(3)_c×SU(2)_L×SU(2)_R (9 generators) is; full SU(4)/SO(6) as a gauge group is BLOCKED (G97, `CLAIM_LEDGER.yaml` C7_GATE_G97_CLOSED). | 6/6 | 2026-06-17 |
| G10b | Gauge Structure | SU(3) embedded in SO(6) explicitly | PASS | J-preserving traceless subalgebra; dim=8 | 5/5 | 2026-06-18 |
| G11 | Gauge Structure | 32×32 block generators SU(2)_L, SU(2)_R, SU(3) | PASS | Algebras close with correct structure constants | 12/12 | 2026-06-18 |
| G12 | Gauge Structure | All 5 SM anomaly cancellations | PASS | ΣY³=0, ΣY=0, all mixed anomalies=0 | 5/5 | 2026-06-18 |
| G13 | Gauge Structure | Twisted Dirac index on S⁶ ≠ 0 | PASS | ind(D_{T^{1,0}})=1 ≠ 0 | 4/4 | 2026-06-19 |
| G14 | Gauge Structure | Quark color triplet from S⁶ spinor basis | PASS | 3 colors = {|011⟩,|101⟩,|110⟩} Kronecker | 6/6 | 2026-06-19 |
| G15 | Quantum Numbers | Hypercharge Y from S⁶ geometry | PASS | Y = T₃R + (B−L)/2 for all 8 S⁶ states | 8/8 | 2026-06-19 |
| G16 | Quantum Numbers | Y = K₃ + (B−L)/2 fully geometric | PASS | Right-handed generation + CPT conjugates correct | 8/8 | 2026-06-19 |
| G17 | Quantum Numbers | Q = T₃L + Y; ΣQ=0 for all 32 states | PASS | Electric charge geometric; ΣQ=0 exact | 10/10 | 2026-06-19 |
| G18 | NCG Structure | Spectral triple KO-dim=6; 4 free Yukawa | PASS | J_F²=−1, {J_F,γ_F}=0, [D_F,J_F]=0 | 8/8 | 2026-06-19 |
| G19 | NCG Structure | (2,2)₀ Higgs bidoublet from D_F | PASS | dBL=0 geometric; Pati-Salam structure | 6/6 | 2026-06-19 |
| G20 | NCG Structure | Yukawa intertwiner dim=4 (8→4 via CPT) | PASS | 4 = dim(SU(3)-orbits on S⁶) via CPT folding | 6/6 | 2026-06-19 |
| G21 | NCG Structure | S⁶ necessary: Extended Schur dim check | PASS | dim=12 without B-L, dim=8 with B-L | 5/5 | 2026-06-19 |
| G22 | NCG Structure | NCG first-order condition selects SU(3)×U(1)_{B-L} | PASS | Violation=(1/2)² for SU(2) sectors | 6/6 | 2026-06-19 |
| G23 | Closing Gates | Chirality from gauge sectors; Witten index=0 | PASS | {D_F,γ_F}=0; SM chirality from SU(2)_L vs SU(2)_R | 8/8 | 2026-06-19 |
| G24 | Closing Gates | Blind Spectrum: SO(4)×G₂ rep → SM content | PASS | SM fermion content predicted from group theory alone | 6/6 | 2026-06-19 |
| G25 | Closing Gates | Yukawa Texture: 256→16→4 geometric cascade | PASS | Exactly 4 Yukawa params from geometry | 6/6 | 2026-06-19 |
| G26 | Closing Gates | CCM 2006 comparison: 3 postulates become derived | PASS | 5/5 correspondences; Dolan-Nash 2002 cited | 5/5 | 2026-06-19 |
| G28 | Spectral Action | Spectral action → SM gauge kinetic terms | PASS | g₂²∝Vol(S⁶)/N_{s6}, g₃²∝Vol(S³)/N_{s3} | 8/8 | 2026-06-19 |
| G29 | Spectral Action | Coupling ratio g₂²/g₃² = 15/(16π) | PASS | 4.3% error vs SM at equal radii; zero free params | 6/6 | 2026-06-20 |
| G27 | N_gen NULL | Z₃ orbifold on S⁶ gives N_gen=3? | NULL | χ(S⁶)=2; Z₃ has no free action on S⁶ | 8/8 | 2026-06-20 |
| G30 | N_gen NULL | G₂-instanton index on S⁶ gives ind=3? | NULL | G₂ acts identically on S⁺ and S⁻ → ind=0 for all G₂-irreps | 34/34 | 2026-06-20 |
| G31 | N_gen NULL | S³ adjoint bundle j=1 gives ind=3? | NULL | Lichnerowicz D²≥0 + parity → ind=0; j_crit=3/2 (Rarita-Schwinger) | 12/12 | 2026-06-20 |
| G33 | N_gen NULL | Euler class c₃(T^{1,0}S⁶)=χ(S⁶) gives N_gen=3? | NULL | c₃=χ(S⁶)=2 (not 6); A1 circular (embeds N_gen=3 as input) | 10/10 | 2026-06-20 |
| G34-D1 | N_gen NULL | Flux H⁶(S⁶;ℤ)=ℤ selects c₃=6? | WEAK | H⁶=ℤ allows any c₃∈ℤ; necessary not sufficient | 4/4 | 2026-06-20 |
| G34-B3 | N_gen NULL | WZW SU(2)_k level k=2 gives 3 primaries → N_gen=3? | NULL | η(D_{S³})=0 → k_grav=0 → SU(2)₀ → 1 primary | 6/6 | 2026-06-20 |
| G34-A2 | N_gen NULL | Cobordism Ω^Spin_6=0 selects N_gen=3? | NULL | No mod-k cobordism invariants on S⁶; η(S⁶)=0 | 4/4 | 2026-06-20 |
| G35 | N_gen NULL | NCG M₃(ℂ) dimension = generation counter? | NULL | rank(T^{1,0}S⁶)=3 ≠ ind=1; M₃(ℂ)=color SU(3) | 6/6 | 2026-06-20 |
| G36 | N_gen NULL | K-theory Adams ops select n=3? | NULL | K̃(S⁶)=ℤ homogeneous; Adams k³ eigenvalue same ∀n | 8/8 | 2026-06-20 |
| G37 | N_gen NULL | String tadpole on S³×S⁶ selects N_gen=3? | NULL | dim=9≠10D; compact bulk not specified; vacuous | 4/4 | 2026-06-20 |
| G38 | N_gen NULL | Spectral action minimum at c₃=6? | NULL | S_spec(c₃) monotone → min at c₃=2 (=G33 restated) | 8/8 | 2026-06-20 |
| G39-B1 | N_gen NULL | Pati-Salam SU(4) bundle: Λ²(T^{0,1}) gives c₃=6? | NULL | Λ²(T^{0,1}) has c₃=2 not 6 | 6/6 | 2026-06-24 |
| G40-B2 | N_gen NULL | G₂→SU(3) SSB via π₅(S⁶) gives c₃=6? | WEAK | π₅(S⁶)=0 (not ℤ₂); cellular approx; G₂-SSB doesn't force c₃ | 4/4 | 2026-06-24 |
| G41-B3 | N_gen NULL | 3 D6-branes: rank-3 gauge bundle selects c₃=6? | WEAK | c₃ free; no physical selection principle | 3/3 | 2026-06-24 |
| G42-B4 | N_gen NULL | Green-Schwarz anomaly cancellation selects c₃=6? | NULL | H⁴(S⁶)=0 → GS trivial; dim=9≠10 | 4/4 | 2026-06-24 |
| G43+G48 | N_gen NULL | Stable HYM bundles (Harland-Nölle): c₃=6 on S⁶? | NULL | Harland-Nölle: instantons on ℝ⁷ cone not S⁶; all known S⁶: c₃=2 | 8/8 | 2026-06-24 |
| G44 | N_gen NULL | D₄ triality on S³×S⁶ (G₂ holonomy) gives N_gen=3? | NULL | G₂ has no 8-dim irrep; triality orbit collapses to 1 on S⁶ | 6/6 | 2026-06-20 |
| G45 | N_gen NULL | D₄ triality on S³×S⁷ (SO(8)) gives N_gen=3? | WEAK | Orbit size=3 visible; single parallelization → N_gen=1 | 4/4 | 2026-06-20 |
| G46 | N_gen NULL | Geometric ℂ⊗ℍ⊗𝕆 realization gives N_gen=3? | NULL | Single metric → unique isotropy; SO(8) dim=28 not compactifiable | 6/6 | 2026-06-20 |
| T1 | N_gen THEOREM | No single-bundle mechanism selects N_gen=3 on S³×S⁶ | THEOREM | 14 NULL + 4 WEAK; all 5 categories exhausted; N_gen=3 is dynamical | 29/29 | 2026-06-24 |
| G50 | χ-Lemma | χ-lemma: H²=H⁴=0 → c₁=c₂=0 → single algebraic cause | PROMOTE | All G33/G38/G39 = one algebraic cause; T1 from 2 lemmas | 10/10 | 2026-06-20 |
| G53 | Casimir | Casimir energy on S³×S⁶; A₀=√π/2 | PARTIAL | C1-C3 PASS; ζ(−1/2) not computed analytically | 12/12 | 2026-06-21 |
| G54A | Stabilization | Freund-Rubin flux: V_flux = g₂²/g₃² | PASS | V_flux=15·C_SM³/(16π)=0.2861; SU(2)_L←Vol(S⁶) cross-spectator | 8/8 | 2026-06-21 |
| G57 | Stabilization | UV-selection: Casimir half-integer pole c_{1/2}=0 at ρ₆* | PASS | ρ₆*=1.090 (C_UV/C_SM); UV divergence cancelled | 6/6 | 2026-06-21 |
| G60 | Stabilization | Minkowski uplift: can NP term alone reach V=0? | NULL | λ_geom=−0.002<0; zeta_FP monotone; external uplift required | 6/6 | 2026-06-21 |
| G62 | Stabilization | Zero-fit observables from potential chain | PROMOTE | ρ₆_min=1.179, V_min=−2.53×10⁻⁶, m_mod/m_KK=2.02% (proxy); zero SM input | 19/19 | 2026-06-21 |
| G63 | Stabilization | Casimir correction to ρ_min | PROMOTE | Casimir=0.24% of V_flux; δρ_min<0.005%; G62 stable | 13/13 | 2026-06-21 |
| G64 | Stabilization | ρ_min=1.179 independent of C (g₂/g₃ ratio) | PROMOTE | ρ_min C-invariant; m_ratio∝C^{3/2} | 23/23 | 2026-06-21 |
| G65 | Stabilization | κ=ρ_min/ρ* is C-invariant | PROMOTE | κ=1.082 C-invariant; ρ_min∝1/C, ρ*∝1/C simultaneously | 24/24 | 2026-06-21 |
| G66 | Stabilization | Analytic κ² = (n+1)/n = 7/6 | PROMOTE | κ=√(7/6)=1.0801 ANALYTIC; n=dim(S⁶)=6; error 0.004% | 25/25 | 2026-06-21 |
| G67 | Three Channels | SO(8) triality Z₃ → 3 independent channels | PROMOTE | G₂=Fix(Z₃⊂Aut(𝕆)); |Z₃-orbit|=3; G68: L≠R (2/3 closed) | 25/25 | 2026-06-21 |
| G69 | Three Channels | CSDR G₂/SU(3): Spin(6)→SU(3) branching = SM content | PROMOTE | 4→3+1, 4̄→3̄+1; 3+3̄+1+1 per channel | 26/26 | 2026-06-21 |
| G73 | Three Channels | ind(D_{S⁶}⊗S⁻)=1/channel × 3 channels = N_gen=3 | PROMOTE | Â(S⁶)=1 exact; c₃(S⁻)=2; N_gen=3 EXACT | 29/29 | 2026-06-21 |
| G74A | Three Channels | Lichnerowicz+G₂-Schur: dim ker=1 EXACTLY per channel | PROMOTE | |F|/(R/4)=8/45≪1; safety=5.625×; G₂-singlet mult=1 | 30/30 | 2026-06-21 |
| G74B | Three Channels | sign(ind)=+1 → LEFT_HANDED_EXCESS | PROMOTE | L=1, R=0 per channel; 3 left-handed zero modes total | 31/31 | 2026-06-21 |
| G76 | Parameter Audit | Parameter registry: classify all constants by provenance | PASS | FIXED: n₃,n₆,K_vol / CONDITIONAL: C_SM,ρ₆*,V_flux / FREE: λ_np,λ_V,A_np | — | 2026-06-22 |
| G82 | Parameter Audit | Canonical mass ratio m_mod/m_KK in Einstein frame | CONDITIONAL | 2.02% (coordinate proxy) → 0.25% (canonical, M4=Ms=1); physical needs string units | 5/5 | 2026-06-22 |
| AV-G0 | Contour AV-2 | Source trace: C-H eqs 3.27-3.41 VERIFIED_FROM_PDF | PASS | Equations matched to source PDF | verified | 2026-06-10 |
| AV-G1 | Contour AV-2 | Two-component first-order system | PASS | 24 tests; FD error ≤5×10⁻⁷ | 24/24 | 2026-06-10 |
| AV-G2 | Contour AV-2 | Boundary exponent g_l0≈0; mixed_l0≈cosα | PASS | g_l0≈−0.096≈0; mixed_l0=0.928 | 45/45 | 2026-06-10 |
| AV-E1 | Contour AV-2 | φ₀₀·g₀₀ = cosα·sinα = sin(2α)/2 EXACT | STRONG_PASS | Spinor bilinear origin of sin(2α); analytic identity | 26/26 | 2026-06-10 |
| AV-E2 | Contour AV-2 | Angular CG singlet C²=0.5 | PASS | SU(2) state (m=±1/2) has nonzero singlet projection | 21/21 | 2026-06-10 |
| BG-G0 | Contour BG-H1 | Product Dirac on S³×S¹: source trace | PASS | C-H eqs (2.1),(2.4),(2.10),(3.46)-(3.48) verified | verified | 2026-06-10 |
| BG-G1 | Contour BG-H1 | D₄²=−(k²+p²)·I₄ at machine precision | PASS | max_rel_error=0.0 | 58/58 | 2026-06-10 |
| BG-E1 | Contour BG-H1 | Discrete KK eigenvalue k₀ → 3/2 (N→∞) | PASS | k₀_disc(N=4000)=1.4999999561; max_rel_err=2.93×10⁻⁸ | 72/72 | 2026-06-10 |
| BG-E2 | Contour BG-H1 | S³×S¹ bridge: disorder W=0.5 stress test | PASS | max_frag_ratio=0.998; max_mean_err=2.54×10⁻⁴ | 67/67 | 2026-06-15 |
| LB-G0 | Contour Lambda-B5 | Invariant 1-forms ∉ span(E_i,E′_i) | STRUCTURAL_SPLIT | λ_geom conditionally canonical; Dereli route separated | 12/12 | 2026-06-11 |
| LB-G2 | Contour Lambda-B5 | cot(2α) is Hopf-frame artifact, not physical | PASS | Left-invariant frame: ω_ij=ε_ijk·σ_k/ρ (constant); no α-dependence | 14/14 | 2026-06-11 |
| LB-G4 | Contour Lambda-B5 | λ non-identifiable from S³ geometry alone | PASS | rank(J_phys)=2; Fisher rank theorem; λ=FREE | 18/18 | 2026-06-11 |
| LB-VR | Contour Lambda-B5 | R=√2 EXACT λ-free ratio from S³ CG coefficients | PASS | Wigner-Eckart: CG ratios cancel λ; first λ-free prediction | 7/7 | 2026-06-11 |
| S6H-G0 | Contour S6-HARM | SO(6) Clifford: {Γa,Γb}=2δI; 8 weight vectors | PASS | G₇ chirality; Killing count=8=2^{n/2} | 4/4 | 2026-06-15 |
| S6H-G5 | Contour S6-HARM | cotβ_k universality: same coeff at 4 levels | PASS | Algebra, ODE, Dirac spectrum, spin connection; G2→G5 chain | 17/17 | 2026-06-15 |
| G85A | Lambda-Map | Poisson resummation: exp(−λ/ρ₆²) from spectral? | NULL | Poisson theta form found; Bessel bridge absent; NP ansatz manual | 10/10 | 2026-06-22 |
| G86A | Lambda-Map | Any geometric T with power-law gives exp(−λ/ρ₆²)? | NULL | Structural theorem: I=Γ(d/2)/T^{d/2}∝ρ₆^{-3α} always (power-law) | 25/25 | 2026-06-22 |
| G86B | Lambda-Map | Warp factor Ω(y) on S⁶ gives exp(−λ/ρ₆²)? | NULL | Trivial (Hopf lemma) / polynomial+free Q / circular | 8/8 | 2026-06-22 |
| G90 | Lambda-Map | Which NP form V∝exp(−a_p/ρ^p) supports minimum? | PASS | p>0 has minimum; p=2 special: κ²=(N+1)/N=7/6 | 12/12 | 2026-06-22 |
| G91 | Lambda Origin | H1 (λ=1/a) vs H2 (λ=a/(a+N)): which gives λ=1/3? | NULL | Both give λ=1/3 on S³×S⁶; κ blind to both off (3,6) coincidence | 8/8 | 2026-07-05 |
| G100 | Audit | G73 "×3 channels" dependency map: what does it rely on? | PASS | G67-C3: 2/3 closed (G68 L≠R); 1/3 open (8_v vector channel) | 6/6 | 2026-07-01 |
| G102 | Triality | Can Spin(8) fiber give third triality channel derivably? | NULL | c_{so(8)}(g₂)=0; no fiber symmetry coexists with S⁶ geometry; 8_v = MODEL POSTULATE | 14/14 | 2026-07-05 |
| G103 | Lambda Origin | KK tower lambda-blindness + UV mechanism proposals | PASS | m_mod∝λ⁰·⁴⁹³; 5 external proposals killed; KK sector λ-blind | 12/12 | 2026-07-05 |
| G104 | Lambda Origin | H1 vs H2 forward test on S²×S⁶ (different geometry) | NULL | κ/ρ_min stays blind off (3,6) coincidence; H1≠H2 not distinguishable | 8/8 | 2026-07-05 |
| G105 | Modulus Mass | Analytic derivation of m_mod∝ρ₆^α power law | PROMOTE | Leading order α=1/2 EXACTLY from asymptotic expansion; unifies G66+G103 | 18/18 | 2026-07-06 |
| G106 | Modulus Mass | Pre-registered prediction at genuinely new N=7 point | PROMOTE | κ² within 0.22%; exponent within 0.001; pre-registration confirmed | 6/6 | 2026-07-06 |

---

## Status legend

| Status | Meaning |
|--------|---------|
| PROMOTE | Claim promoted — strong evidence, skeptic passed |
| PASS | Gate passed — claim confirmed |
| STRONG_PASS | Analytic identity, not numerical coincidence |
| THEOREM | Proved by exhaustion (multiple NULL results) |
| PARTIAL | Partially confirmed — some sub-gates open |
| CONDITIONAL | Confirmed under stated assumptions |
| STRUCTURAL_SPLIT | Architectural finding — not pass/fail |
| NULL | Gate falsified — mechanism does not work |
| WEAK | Allowed but not forced — not a proof |
| OPEN | Active investigation — no verdict yet |

## Open channels

| Gate | What's needed |
|------|--------------|
| G72 | Triality bundles: Tom Lawrence input on 8_v channel |
| G102 | Third triality channel: explicit fiber-Spin(8) framework or new physics |
| G82 | Full 4D reduced action for canonical m_mod/m_KK |
| G61 | λ physical origin: non-perturbative mechanism (outside geometric scope) |
| Preprint | Insert §1 paragraph on "Testable predictions" + G105/G106 in §moduli |

## Tom Q&A status

| Q# | Question | Our answer | Tom's response |
|----|---------|-----------|---------------|
| Q1 | S³ spinor frame basis correct? | YES (G2, G11, G15-G17) | Awaiting |
| Q2 | cot(2α) disappears in correct frame? | YES (G2, PASS_FRAME_ARTIFACT) [VERIFIED-sympy 14/14] | Awaiting |
| Q3 | λ fixed at S³×S⁶ stage? | NO — λ=FREE (G83-G86B, G103 exhaustion) | Awaiting |
| Q4 | Alpha coordinate convention? | RESOLVED: Ben Achour θ = π/2 − Tom_θ | ✅ Confirmed 2026-06-15 |

*Edit this file → run `python scripts/export_results.py --all` → commit both MD and exports.*
