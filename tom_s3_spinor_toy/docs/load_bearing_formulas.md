# Load-bearing formulas across tom_s3_spinor_toy

Compiled 2026-07-11 via 5 parallel agent surveys of `experiments/` + targeted
direct verification. NOT a padded "top 100" — an honest, deduplicated count of
formulas that were actually load-bearing for a gate's PASS/REJECT/PROMOTE
verdict, i.e. the one thing that, if wrong, would change the outcome. Generic
textbook formulas present-but-not-decisive are excluded.

**Total: 64 entries.** Organized by theme, most important first within each.
G53-G61 gap closed 2026-07-11 (direct read, bypassing a Glob-tool path-matching
bug — confirmed via `docs/exports/gates_tracker.json` that G55/G56/G58/G59/G61
simply do not exist as separate gates; only G53, G54A-F, G57, G60 are real).
Remaining known gaps (not yet surveyed): G76, G82, G83, G84a/b, G89b, G90, G92,
G93, Rounds 24-46 of the Dolan-Casimir thread. Do not treat this as exhaustive
coverage of every gate in the project.

---

## 1. Gauge structure & fermion content (G6-G29, Contour gates)

| Gate | Formula | Why load-bearing |
|---|---|---|
| BG-E1 | k₀_disc(N)→3/2 as N→∞, max_rel_err=2.93e-8 at N=4000 | Whole S³×S¹ product-Dirac bridge stands/falls on this extrapolation hitting the exact half-integer eigenvalue |
| BG-G1 | D₄²=−(k²+p²)·I₄, max_rel_error=0.0 | Machine-precision certifies D₄ is a genuine Dirac operator, not just formally similar |
| AV-E1 | φ₀₀·g₀₀=cosα·sinα=sin(2α)/2 | Exact identity promoting AV contour from "numerically close" to STRONG_PASS |
| LB-G4 | rank(J_phys)=2 | Formal justification behind the hard fence λ=FREE_COUPLING_PARAMETER |
| LB-VR | R=√2 exactly (Wigner-Eckart CG ratio, λ cancels) | First λ-independent structural prediction in the project |
| G66 | κ²=(n+1)/n=7/6, n=dim(S⁶)=6 | Converts fitted κ≈1.08 into an analytically derived number |
| G74A | \|F\|/(R/4)=8/45≪1 + G₂-Schur mult=1 | Forces dim ker(D)=1 exactly per channel, not just ≥0 |
| G73 | ind(D_S⁶⊗S⁻)=1, from Â(S⁶)=1, c₃(S⁻)=2 | Turns "3 triality channels exist" into "N_gen=3" |
| G33 | c₃(T^{1,0}S⁶)=χ(S⁶)=2 (not 6) | Falsifies the most natural bundle route, seeds the whole G33-G48 NULL chain |
| G50 | H²(S⁶)=H⁴(S⁶)=0 ⟹ c₁=c₂=0 | Unifies G33/G38/G39 into one root cause instead of three coincidences |
| G29 | g₂²/g₃²=15/(16π) | Zero-free-parameter number directly compared to SM value (4.3% error) |
| G22 | FO violation=(1/2)² for SU(2)_L/R | Specific value selects SU(3)×U(1)_B-L as first-order-compliant |
| G17 | Q=T₃L+Y on all 32 states, ΣQ=0 | Closure check with the actual T₃L/Y values from G11/G16 |
| G12 | 5 anomaly sums = 0 (exact rational arithmetic) | Certifies the specific 32-state fermion table, not a generic formula |
| G7 | M²_mn=(n+3/2)²/ρ₃²+m²/ρ₆² | The 3/2 half-integer offset (Lichnerowicz spectrum) is the load-bearing detail |
| G62 | ρ₆_min from dV/dρ₆=0 (Freund-Rubin+Casimir) → ρ₆_min=1.179 | First zero-fit falsifiable observable with no SM input |
| G54A | V_flux=g₂²/g₃²=15·C_SM³/(16π)=0.2861 | Seeds the entire G57-G66 stabilization chain |
| G13 | ind(D_T^{1,0})=1≠0 | The specific nonzero value supplies the chiral zero mode G73/G74B build on |
| G8 | Atiyah-Singer index=0 (untwisted bundle) | NULL result that forces the twisted-bundle approach (G13) |

## 2. N_gen NULL chain & Theorem by Exhaustion (G27-G50, T1)

| Gate | Formula | Why load-bearing |
|---|---|---|
| G33/G50 (χ-lemma) | H²(S⁶)=H⁴(S⁶)=0 ⟹ c₁=c₂=0 ⟹ c₃=−χ(S⁶)=−2 for ANY bundle | Single most important formula in the chain — vanishing cohomology is the actual reason no Chern-class mechanism can produce 6 |
| T1/G47 | Categories 1-5 all reduce to ind(D⊗T^{1,0}S⁶)=c₃/2=1 | Proof structure is reduction to one invariant, not enumeration |
| G27 | χ(S⁶)=2, Smith theory: 3∤(n+1)=7 | Single number kills the ℤ₃-orbifold route |
| G30 | mult(3)=mult(3̄) for every G₂-irrep restricted to SU(3) | Forces index=0 for ANY G₂-equivariant bundle |
| G31 | D²≥1/(2ρ₃²)>0 for j=1, zero-mode count=2j+2 | Two independent constraints jointly needed, either alone leaves a loophole |
| G34-B3 | k_grav(S³)=η(D_S³)/2=0 | Specific vanishing eta-invariant falsifies the WZW k=2 candidate |
| G34-A2 | Ω^Spin_6=0 | Forbids any mod-k topological invariant via cobordism |
| G36 | K̃(S⁶)=ℤ, single generator via Bott periodicity | Shows no intrinsic K-theory invariant distinguishes c₃=6 from any other multiple |
| G37 | Minimal integer tadpole → c₃=2 (same as G33) | Makes the string route redundant with G33, not independent |
| G38 | S_zero=ch₃(V)×f(0)=c₃/2, monotone in c₃ | Monotonicity forces the spectral-action minimum to c₃=2 |

## 3. Triality, three channels, lambda-origin (G67-G106)

| Gate | Formula | Why load-bearing |
|---|---|---|
| G73 | ind(D_S⁶⊗S⁻)=Â(S⁶)·c₃(S⁻)/2=1 per channel | Upgraded headline number from N_gen=1 to N_gen=3 |
| G74A | \|F_S⁻\|/(R/4)=8/45≪1, Weitzenböck | If ratio≥1, exact-count claim collapses to a bound |
| G74B | dim ker(D+)+dim ker(D-)=1 (G74A), dim ker(D+)−dim ker(D-)=+1 (G73) | 2×2 linear system is the whole chirality derivation |
| G67 | G₂=Fix(ℤ₃⊂Aut(𝕆)), triality permutes 8_v/8_s/8_c | Z₃-invariance is the only reason all 3 channels share topological charge |
| G102 | dim c_so(8)(g₂)=0 | Converts "open 8_v channel" from unsolved to provably unsolvable internally |
| G105 | x₀²=(N+1)/N as leading order of the SAME expansion giving the 0.4928 exponent | Unifies G66 and G103 into one expansion, not two coincidences |
| G106 | κ² pre-registered=(N+1)/N at N=7=8/7, matched to 0.22% BEFORE computing | Pre-registration-before-computation is what makes it a real confirmation |
| G69 | Spin(6)=SU(4) spinor 4+4̄ under SU(3) → 3+3̄+1+1 | Independent (non-triality) route agreeing with G67 = structural cross-check |
| G94 | A_S3·exp(−c·ρ₃³), 0.248<c<0.372 for true minimum | Cubic (not quadratic) exponent is what fixed the earlier non-stabilizing ansatz |
| G91 | m_mod/m_KK=0.198%, using λ₀=3/(2ρ₃) (S³ spectrum, not S⁶ proxy) | Correct eigenvalue formula changed the physical ratio from G88A's proxy |
| G103 | dln(m_mod)/dln(λ)=0.4928 over λ∈[0.15,0.60], KK-sensitivity≤0.41% | Jointly separates "λ measurable" from "λ measurable ONLY in modulus sector" |
| GAP-4 | S3_SPINOR_DIM=4 fixed block (g67_triality.py) | REJECT by structural absence — no cross-term exists to check |
| ModFlav | f_inv(ρ)=exp(−b(1/ρ²−1/ρ₆*²)), no ρ→c/ρ symmetry | REJECT by direct functional-form inspection, not assumption |

## 4. Casimir & moduli stabilization (G53-G92)

| Gate | Formula | Why load-bearing |
|---|---|---|
| G57 | ρ₃/ρ₆=C_UV≈1.0743 (ray, from homogeneity degree −1 of c_{1/2}) meets SM parabola ρ₃=C_SM·ρ₆² at exactly one point | Turns ρ₆*≈1.090 from a numerically-found coincidence (G54-C) into a GEOMETRIC necessity — a ray and a parabola in 2D moduli space intersect at one point, this is why ρ₆* is special, not just where it happens to be |
| G54-A | V_flux=15q²ρ₃³/(16πρ₆⁶); at q=1, V_flux ≡ g₂²/g₃² EXACTLY | The Freund-Rubin flux energy and the gauge coupling ratio (G29) are the SAME function of (ρ₃,ρ₆) — stabilizing the flux literally IS stabilizing the gauge coupling, not two separate things that happen to agree |
| G54-B | K_{S³}(τ)=(√π/2)τ^{-3/2}−(√π/4)τ^{-1/2}+O(e^{-π²/τ}) — proven EXACT via Poisson summation, no polynomial τ^{1/2} term | Proves ALL higher Seeley-DeWitt coefficients (A4, A6, ...) are exactly zero for S³ — this exactness is what produces the simple (not higher-order) pole at s=−1/2 that the whole Casimir chain depends on |
| G54-E | Three ordered radii: ρ₆_min≈0.953 (ζ_FP most negative), ρ₆*≈1.090 (UV pole=0), ρ₆**≈1.447 (ζ_FP=0) | Each radius is defined by a DIFFERENT, independent condition; the ordering ρ₆_min<ρ₆*<ρ₆** being non-degenerate is what makes them three physically distinct special points, not one point under different names |
| G54-F | V_int∝ρ₆¹² exactly (F4.1); V_total_EH monotone decreasing on [0.7,1.5], ρ₆** is NOT its minimum (F4.5, Dine-Seiberg runaway) | Kills the naive hope that switching to Einstein-frame variables turns any of the three special radii into a genuine potential minimum — the runaway is a real obstruction, not a coordinate artifact |
| G54-D | Σ'=Σ_{αₙ≠1/2} cₙ/(αₙ−1/2) changes sign between ρ₆=1.09 and 1.20 along the SM constraint | This sign flip in an analytic (not numerically-fitted) sum is THE geometric source of ζ_FP's own sign change — traces the Casimir-energy sign flip to a specific term, not just observes it |
| G53 | Product spectrum λ²_{j,k}=λ²_j+λ²_k (ADDS across S³×S⁶, does not multiply) ⟹ ζ_product≠ζ_S³×ζ_S⁶ (>10% difference at unit radii) | Proves the two-radius Casimir computation is genuinely non-trivial — the whole G54 chain would collapse to "just multiply two known single-sphere results" if this additive structure weren't the case |
| G54-C | B₁₀≈−0.0033, distinct from B₈≈−0.0076 (6-parameter fit corrects G54-B's earlier 5-parameter B₈_eff≈−0.0108) | Self-caught fitting error: an incomplete parameterization had silently absorbed B₁₀ into B₈, which would have propagated a wrong coefficient through every downstream ρ₆* /ρ₆** computation |
| G60 | λ_geom=−0.0022<0 (from Minkowski+minimum conditions on V_total with V_np=−A·exp(−λ/ρ₆²)) | NULL result: falsifies the hope that λ≈0.30 can be algebraically derived from pure S³×S⁶ geometry — the sign itself (negative, not just "wrong magnitude") is what rules out this entire derivation route |
| G64 | V_total(ρ,C)=C³×[15/(16π)]×f(ρ,ρ*,λ)/(K_VOL·ρ¹²), f independent of C | Proves ρ_min is a genuine zero-fit — no SM coupling input needed for the minimum's location |
| G65 | κ=ρ_min(C)/ρ*(C)≈1.0817, C-invariant (spread<0.1%) | KKLT gap ratio depends only on λ=1/3, not on C or ρ* individually |
| G63 | V_Cas=α·ζ_FP(ρ₆)/(K_VOL·ρ₆¹²), \|ζ_FP(ρ_min)\|/V_FLUX=0.24% | Shows the Casimir correction is sub-percent — G62's prediction is robust, not fragile |
| G88A | coordinate proxy m_mod/m_KK=0.020248 vs canonical 0.0025165 (factor 0.124) | Honesty check: the "raw" G62 ratio is NOT the physically canonical radion mass — must be stated as a proxy |
| G85B | Saddle t*=ρ₆²/3 exists, but exp factor=exp(−3)=const, NOT exp(−λ/ρ₆²) | NULL: kills this specific saddle-point route to the non-perturbative λ-term |
| G86A | I=Γ(d/2)/T^{d/2}~ρ₆^{−3α} for ALL α∈[−4,8] | Structural NULL: Laplace integrals with power-law T are ALWAYS power-law, 0/25 give exp(−λ/ρ₆²) |
| G86B | Uniform flux→trivial A=const; localized source→power-law δM_Pl²~ρ₆² | NULL closes the λ-map search: both cases fail to reproduce exp(−λ/ρ₆²) |

## 5. Dolan-Casimir G2/SU(3), Rounds 14-34 (Kostant-Parthasarathy generalization)

| Round | Formula | Why load-bearing |
|---|---|---|
| Round 21 | D²\|_M has nonzero off-(SU(3)-type)-blocks; Scal/4, any invariant fiber endomorphism, ∇*∇_can are ALL block-diagonal | Single structural fact killing Round 16's whole construction — a theorem, not a sign bug |
| Round 22 | D_7²=[Scal/4+∇*∇_can]+[SU(3)-curvature]+[torsion]+[mixed A-B] | Closed-form fix for Round 21's impossibility result, verified on 2 independent test vectors |
| Round 23 STEP B v2 | F_S⁻:=Σ_{p<q}(E_pE_q)⊗R(e_p,e_q), spectrum {1/6:15,−5/2:1} | Required discovering Clifford mult and spin connection do NOT commute on one Sigma factor |
| Round 19 | D²_7 eigenvalues {4,2,20/3,10/3} via exact-in-span coefficient extraction | Closure step turning "no zero mode found yet" into "provably none exists" |
| Round 14 | V_7:=φ₁^⊥ (7-dim), Casimir C₂=−Σ(ν_k\|_V7)²=2·Id₇ | Converts G₂'s abstract 14 generators into an explicit 7-dim rep the whole Rounds 14-20 program depends on |
| Round 14 (convention) | C₂(G2;7)=2 (physics) vs Agricola's 4 (long-root²=2) | Silent factor-of-2 mismatch would corrupt every downstream Casimir-gap argument |
| Round 16→17 | {2,6}={0,4}+2·[1,1] (three independent derivations agree) | Convergence of 3 routes on the same relation is the strongest evidence for rho=7's result |
| Round 20 | D²_14 eigenvalues {6,20/3,10/3} rational under one sign convention vs irrational under the flip | Rationality (matching every other Casimir quantity in the project) selects the physical sign |
| Round 15 | D²_S⊗E=∇*∇+(1/4)Scal_g+R^E, valid because t=1/2 is exactly torsion-free | Pivot formula enabling Rounds 16-20, later superseded but the hinge decision |

---

## Coverage note

Agent-surveyed (2026-07-11): sections 1-3 fully, section 4 partially (5 of ~15
gates in that range, gap-filled by direct read), section 5 partially (9 of
30+ rounds, explicitly flagged as scope-limited by the surveying agent).
Sections 4-5 have real, acknowledged gaps — see "Known gaps" above. This file
should be extended, not re-generated from scratch, if those gaps are closed later.
