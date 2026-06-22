# Null Results Index

| ID | Date | Slug | Verdict | Why falsified |
|----|------|------|---------|---------------|
| G27-ℤ₃ | 2026-06-19 | z3-orbifold-s6 | REJECT | χ(S⁶)=2 not divisible by 3; Smith theory rules out free ℤ₃ action |
| G30-G₂ | 2026-06-20 | g2-instanton-3gen | REJECT | G₂ symmetry forces index=0; mult(3)=mult(3̄) in all G₂-irreps |
| G31-S³ | 2026-06-20 | s3-rarita-schwinger | REJECT | Lichnerowicz D²≥1/2ρ₃²>0 for j=1; parity: dim=3 needs j=1/2 but D²=1>0 |
| G33-A1 | 2026-06-20 | a1-euler-class | REJECT | c₃(T^{1,0}S⁶)=χ(S⁶)=2 (Chern-Gauss-Bonnet); A1 circular: c₃=6=N_gen×2 embeds N_gen=3 |
| G34-D1 | 2026-06-20 | d1-flux-quantization | WEAK | H⁶(S⁶;ℤ)=ℤ allows any c₃ ∈ ℤ; no topological invariant of S⁶ equals 3; D1 necessary not sufficient |
| G34-B3 | 2026-06-20 | b3-wzw-s3-level | REJECT | η(D_{S³})=0 → k_grav=0 → SU(2)₀ WZW → 1 primary, not 3; spin conn CS on S³ gives k=0 |
| G34-A2 | 2026-06-20 | a2-cobordism-s6 | REJECT | Ω^{Spin}_6=0 → no mod-k cobordism invariants on S⁶; η(S⁶)=0 via APS+trivial filling |
| G35-C1 | 2026-06-20 | c1-ncg-m3-generation | REJECT | rank(T^{1,0}S⁶)=3 ≠ ind=1; ONE M₃(ℂ) on S³×S⁶ → color SU(3), not generation count |
| G36-K1 | 2026-06-20 | k1-k-theory-s6 | REJECT | K̃(S⁶)=ℤ homogeneous; Adams ψ^k eigenvalue k³ same for all n; "3β"=N_gen=3 circular |
| G37-S1 | 2026-06-20 | s1-string-tadpole | REJECT | dim(S³×S⁶)=9≠6; χ(S³×S⁶)=0; min Type IIA tadpole → c₃=2=N_gen=1; brane count circular |
| G38-S2 | 2026-06-20 | s2-spectral-action-min | REJECT | S_spec(c₃) monotone increasing; min at c₃=2 (=G33); G38 is G33 restated in energy language |
| G39-B1 | 2026-06-20 | g32-b1-pati-salam-su4 | REJECT | Spin(6)≅SU(4) → Λ²(T^{0,1}) has c₃=2 not 6; factor 3 unaccounted by spin geometry |
| G40-B2 | 2026-06-20 | g32-b2-higgs-ssb-g2-su3 | WEAK | G₂→SU(3) SSB does not force c₃; "factor-2 from π₅" was error: π₅(S⁶)=0 (cellular approx k<n), not ℤ₂ (Freudenthal gives π₇(S⁶)=ℤ₂, not π₅) |
| G41-B3 | 2026-06-20 | g32-b3-brane-picture | WEAK | 3 D6-branes → rank-3 gauge, c₃ free; 2×N=6 arithmetic holds but no physical mechanism |
| G42-B4 | 2026-06-20 | g32-b4-anomaly-gs | REJECT | H⁴(S⁶)=0 makes GS trivial (p₁=c₂=0); also 9D≠10D → GS out of scope |
| G43-B5 | 2026-06-20 | g32-b5-stable-bundles | NULL | Harland-Nölle arXiv:1109.3552: T(S⁶) c₃=2 on base; new instantons on CONE ℝ⁷; no c₃=6 on S⁶ → closed by G48 |
| G44-B1 | 2026-06-20 | d4-triality-s3xs6 | REJECT | G₂ has no 8-dim irrep → 8_v≅8_s≅8_c as G₂-modules → triality orbit collapses to 1; S⁶ blind to τ |
| G45-B2 | 2026-06-20 | d4-triality-s3xs7 | WEAK | Triality orbit size=3 PASS (SO(8) visible); but 1 parallelization→N_gen=1; 3 sectors together = algebraic only |
| G46 | 2026-06-20 | triality-geometrization | NULL | Single metric → unique isotropy → 1 coset structure; 3-Sasakian within 8_s sector only; SO(8) dim=28 |
| G47 | 2026-06-20 | exhaustion-theorem | PASS+OPEN | Theorem T1: Cat 1-5 (14 null results) proved; Cat 6 (G43-B5 HYM-bundles on S⁶) remains OPEN |
| G48 | 2026-06-20 | harland-nolle-verification | NULL | Primary read: no c₃=6 on S⁶; cone≠base; N_gen absent → G43-B5 closed → T1 UNCONDITIONAL |
| G49 | 2026-06-20 | type-iia-kk-s3xs7 | NULL | dim=10 ✓ but min|λ_S⁷|=7/2≠0 → no zero modes; H⁴(S⁷)=0 → flux integers free → circular |
| G51 | 2026-06-20 | sspec-constraint-monotone | NULL | S_spec monotone along ρ₃=0.986ρ₆² (SM coupling constraint) → no interior min; coupling ratio alone cannot stabilize radii |
| G85B | 2026-06-22 | spectral-saddle-worldline | NULL | Saddle t*=ρ₆²/3 exists (K(t*)>0), but exp factor = exp(−3)=const, NOT exp(−λ/ρ₆²); ρ₆-dependence at saddle is ρ₆⁰ (λ_fit=0) |
| G86A | 2026-06-22 | dual-modulus-alpha-sweep | NULL | STRUCTURAL: I=Γ(d/2)/T^{d/2} ~ ρ₆^{−3α} for ALL α∈[−4,8]; Laplace integrals with power-law T are ALWAYS power-law; 0/25 alpha give exp(−λ/ρ₆²) |
| G86B | 2026-06-22 | warp-factor-omega-s6 | NULL | Uniform flux → trivial A=const (Hopf); localized source → power-law δM_Pl²~ρ₆² (R²_pow=1.000) + free Q; postulated exp(−λ/ρ₆²) is y-independent on S⁶ → same as trivial; ALL cases fail PASS; λ-map EXHAUSTED |
| META-C1 | 2026-06-22 | lambda-dimensional-obstruction | PROMOTE | STRUCTURAL THEOREM (Buckingham Pi): any geometric λ = c·ρ₃ᵃ·ρ₆^(2−a); on trajectory ρ₃=κρ₆ → λ=c·κᵃ·ρ₆² → exp(−λ/ρ₆²)=const. G83–G86B null results are structurally necessary. Hodge corollary: H³(S³×S⁶)=ℝ from S³ (not S⁶). See experiments/20260622-lambda-dim-gate/ and THEOREM_PACK.md §C1 |
