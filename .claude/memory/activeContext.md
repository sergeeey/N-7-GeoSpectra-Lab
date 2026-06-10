# activeContext — N-7-GeoSpectra-Lab
**Updated:** 2026-06-10 (session 2)

## Current Focus
AV-2 COMPLETE ✅ — G0, G1, G2, E1, E2 all PASS. item40 = RADIAL+ANGULAR_BILINEAR_SUPPORTED.
BG-H1 pre-registered ✅ (design only): λ²=(n+3/2)²+(m/R)², δ₁(R)=√(9/4+(m₁/R)²)−3/2
(first excited KK; periodic ground state δ₀=0 — m=0 in spectrum!),
both spin structures forked (m∈ℤ vs m∈ℤ+1/2), no choice made.
BG-H1-G0 ✅ PASS v1.1 (после adversarial re-audit, 4 verifiers) — source_register_bg_h1_g0.md:
cross terms vanish by JOINT mechanism: {Γʲ,Γ⁴}=0 (eq 2.1) ∧ [∇ⱼ,∂_y]=0 + lemma
[Σ^{bc},Γ⁴]=0 (eq 2.10) — НЕ независимо (falsified: |X|≈13.9/22.1 поодиночке).
In-source precedent: C-H eqs 3.46-3.48 (warped cross ∝ f′, product → 0).
Spinor doubling 2→4 [VERIFIED_FROM_PDF]. Spin structures: [WEAK]+[INFERRED] — partial-evidence pass.
BG-H1-G1 ✅ PASS [VERIFIED-pytest 2026-06-10, 58/60 tests] — bg_h1_product_dirac_check.py:
D4²=-(k²+p²)·I₄ (max_rel_error=0.0, machine precision); convention-pin: correct(±i√(k²+p²)) ≠ wrong(±i|p-k|, ±i(p+k)); {Γ^j,Γ^4}=0 for j=1,2,3; δ₁(R) ✓ both spin structures; fork reported, no selection.
Next: BG-H1-E1 — discrete S³×S¹ proxy, δ(R) vs closed form, kill: rel error > 1e-2.






## Branch State
| Branch | Status | Contains |
|--------|--------|---------|
| `main` | up to date with origin | v0.2.0: E0, KT-3, NC-2, AV-1, AV-1c′, AV-2 (126 tests) |
| `preserve/tom-s3-p5-p14-scaffold` | up to date with origin | P5–P14 / P13H / V-operator / lambda no-go (191 tests) |

Currently on: `main`






## Key Scientific Results (VERIFIED from git 2026-06-10)

### P13H (preserve branch)
- Coefficient: `(16π²ρ³/15) × λ` — exact, geometric prefactor fixed
- `λ = FREE_COUPLING_PARAMETER` — S3-only does NOT fix physical coupling
- `PROMOTION_BLOCKED` — no physical V-operator promoted
- `safe_for_runtime = False`

### v0.2.0 (main branch)
- Spectral fingerprint: `E0 ~ 3/2 + ε` (discrete Dirac on S3)
- `KT-3`: fingerprint survives disorder W=0.5 (robust)
- `NC-2`: fingerprint is geometric (permuted grid PASS)
- `AV-1`: angular dictionary verified — φ11/boundary-family dominated
- `AV-1c′`: sparse H-T1 bilinear killed (`null_results/20260610-ht1-sparse-bilinear.md`)
- `AV-2 G0`: PASS — `source_register_av2.md` — C-H eq. 3.27-3.30, 3.32-3.33, 3.37-3.38, 3.41 VERIFIED_FROM_PDF + numerical cross-checks
- `AV-2 G1`: PASS — `test_ch_first_order_system.py` 24/24 — eq 3.28 (≤2.3e-15), eq 3.29/3.30 (FD ≤5e-7), eq 3.38 (≤6e-16), g_nl l=0 nonzero at south pole VERIFIED
- `AV-2 G2`: PASS — `g2_boundary_exponent_report.md` — g_l0=−0.0958 (≈0, nonzero at boundary), mixed_l0=0.9281 (≈cos¹); item40 → RADIAL+TWO_COMPONENT_BOUNDARY_MECHANISM_SUPPORTED; 45 tests [VERIFIED-pytest 2026-06-10]
- `AV-2 E1`: STRONG_PASS — `e1_sparse_reconstruction_report.md` — 1 term: φ_{0,0}·g_{0,0} = cosα·sinα = sin(2α)/2 (exact); item40 → RADIAL+TWO_COMPONENT_RECONSTRUCTION_SUPPORTED; 26 tests [VERIFIED-pytest 2026-06-10]
- `AV-2 E2`: PASS — `e2_angular_singlet_report.md` — CG singlet=√2/2, C²=0.5>0; SU(2) m=(+1/2,−1/2) state has nonzero singlet projection; item40 → RADIAL+ANGULAR_BILINEAR_SUPPORTED; 21 tests [VERIFIED-pytest 2026-06-10]
- `item40`: `RADIAL + ANGULAR_BILINEAR_SUPPORTED`






## Open Questions (awaiting Tom Lawrence)
1. Is replacement basis U(α,θ,θ̃) the correct spinor frame for S3?
2. cot(2α) — expected to vanish with correct SO(4) spinor basis?
3. λ — expected free at S3 stage, or fixed by S3×S6/action/gauge?
4. α convention and S3 measure `sin(α)cos(α)dα` correct?

Tom last contacted: 2026-06-09 (LinkedIn, 4 questions sent). Status: hang fire / no reply yet.






## Next Steps (ordered)
1. ✅ Re-audit preserve/P5-P14 — DONE (`reports/P5_P14_REAUDIT_REPORT.md`)
2. ✅ AV-2 G0 source trace — DONE (`source_register_av2.md`, VERIFIED_FROM_PDF)
3. ✅ AV-2 G1 two-component system — DONE (`test_ch_first_order_system.py` 24/24)
4. ✅ AV-2 G2 boundary exponent — DONE (`g2_boundary_exponent_report.md`, 45 tests)
5. ✅ AV-2 E1 sparse reconstruction — DONE (STRONG_PASS, 1 term, 0%, analytically exact)
6. ✅ AV-2 E2 angular singlet check — DONE (PASS, CG=√2/2, C²=0.5, item40→ANGULAR_BILINEAR_SUPPORTED)
7. ✅ BG-H1 pre-registration — DONE (`experiments/20260610-bg-h1-s3xs1-bridge/claim_bg_h1.md`, design only, no code)
8. ✅ BG-H1-G0 source trace — PASS v1.1 (`source_register_bg_h1_g0.md`): C-H eqs (2.1),(2.4),(2.10),(2.12),(2.13),(3.16),(3.26),(3.34),(3.46)-(3.48); cross-term cancellation = JOINT {Γʲ,Γ⁴}=0 ∧ [∇ⱼ,∂_y]=0 + lemma eq 2.10; corrected after adversarial re-audit (phantom file, overclaims, sign convention)
9. ✅ BG-H1-G1 — analytic cross-check PASS [VERIFIED-pytest 2026-06-10]: D4²=-(k²+p²)·I₄, max_rel_error=0.0; convention-pin: correct vs wrong ✓; {Γ^j,Γ^4}=0 ✓; δ₁(R) both spin structures ✓; 58 tests; g1_product_dirac_cross_check_report.md
10. ▶ BG-H1-E1 — discrete S³×S¹ proxy: extend v0.2.0 discrete Dirac to product grid, measure δ(R) for R∈[0.5,8], fit against closed form for both spin structures; kill condition: rel error > 1e-2
11. P14B — S3 normalization robustness test (AFTER Tom confirms replacement basis)






## Hard Constraints (do not change)
- DO NOT mix Tom Lawrence / Covariant Compactification with IDM/MULTING/Buckholtz
- DO NOT claim "lambda fixed" or "physical V promoted"
- DO NOT merge preserve → main without explicit audit/cherry-pick decision
- DO NOT write to Tom until he responds to 4-question message
- runtime=research_only, selection_rules=smoke_only






## Test Suite Status
| Suite | Tests | Status | Verified |
|-------|-------|--------|----------|
| preserve/P5-P14 | 191 | passed | [VERIFIED-SYNTHETIC] prior session |
| P13H only | 3 | passed | [VERIFIED-pytest 2026-06-10] |
| P14 only | 2 | passed | [VERIFIED-pytest 2026-06-10] |
| main/v0.2.0 | 126 | passed | [VERIFIED-pytest 2026-06-10, home PC] |
| C-H first-order | 24 | passed | [VERIFIED-pytest 2026-06-10, home PC] |
| AV-2 G2 | 45 | passed | [VERIFIED-pytest 2026-06-10, home PC] |
| AV-2 E1 | 26 | passed | [VERIFIED-pytest 2026-06-10, home PC] |
| AV-2 E2 | 21 | passed | [VERIFIED-pytest 2026-06-10, home PC] |





## Auto-commit log
- [2026-06-10 23:10] `56d8c38`: feat(bg-h1): BG-H1-G1 product Dirac cross-check — PASS (λ²=(n+3/2)²+(m/R)², max_err=0.0)
- [2026-06-10 22:49] `9f022a0`: fix(bg-h1): G0 source register v1.1 — corrections after adversarial re-audit
- [2026-06-10 22:32] `5681377`: feat(bg-h1): BG-H1-G0 source trace — PASS (product Dirac additivity confirmed from C-H)
- [2026-06-10 20:27] `4025e79`: feat(av2): AV-2 E1 sparse reconstruction — STRONG_PASS (1 term, 0% residual)
- [2026-06-10 19:37] `993981a`: feat(av2): AV-2 G2 boundary exponent — PASS (g_l0≈0, mixed_l0≈0.928)
