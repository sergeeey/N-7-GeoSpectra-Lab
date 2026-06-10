# activeContext — N-7-GeoSpectra-Lab
**Updated:** 2026-06-10 (session 2)

## Current Focus
AV-2 G2 — DONE ✅. Next: E1 sparse reconstruction.
G0, G1, G2 all PASS. item40 = RADIAL+TWO_COMPONENT_BOUNDARY_MECHANISM_SUPPORTED.


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
- `item40`: `RADIAL + TWO_COMPONENT_BOUNDARY_MECHANISM_SUPPORTED`


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
5. ▶ AV-2 E1 sparse reconstruction — NEXT (greedy ≤5 terms, residual < 5%)
6. BG-H1 pre-registration — S³×S¹ bridge gate (λ²=(n+3/2)²+(m/R)²)
7. P14B — S3 normalization robustness test (AFTER Tom confirms replacement basis)


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
