# Evidence ledger — audit 2026-10-21

| # | Claim | Source | Method | Result | Limits | Independence |
|---|---|---|---|---|---|---|
| E1 | Track A z ≈ 8.07 from published means and SEs | `reports/GATE4B_SPECIFICITY_VERDICT_v0.1.24.md:66-68` | awk: (−0.4844 − 0.0106)/√(0.0546²+0.0280²) | z = −8.067 | assumes independence; no per-case data | recomputed here, VERIFIED-tool |
| E2 | "48 σ" | same, line 68 | repo-wide search | no computation found; denominator would need ≈0.0103 | origin unknown | [UNKNOWN] |
| E3 | spectral_circle slope −0.4844 ± 0.0546 | `reports/SPECTRAL_CIRCLE_EXTENDED_ANALYSIS_v0.1.24.md` | OLS on printed per-size IPR (N=16,64,128) | slope −0.345, SE 0.024, df=1 | 3 points; printed values rounded to 3 dp (rounding does not explain the gap) | VERIFIED-tool, does NOT reproduce printed value |
| E4 | C78: commutator rank 20, commutant dim 8 | `experiments/20260811-c78-.../c78_so8_commutant_exhaustive.py` | rerun at HEAD and at c4f8d40 | rank 20, nullity 8, su(3) residual 3.5e-15 | numerical; fiber-level only | VERIFIED-tool, reproduced at its own commit |
| E5 | C78 stored singular values | `results_c78.json` | compare with rerun | leading 28.2598 vs 26.3698; non-uniform ratios | stored file not produced by committed script | VERIFIED-tool, mismatch |
| E6 | G102 dims: Der(O)=14, stab=8, c_so8(g2)=0, c_so8(su3)=2 | `experiments/20260705-g102-spin8-fiber-obstruction/g102_spin8_fiber.py` | rerun, verdict PASS | all predicted values | fiber-level; Spin(8) channel not derivable from fiber (script's own statement) | VERIFIED-tool; rep-theory check [DOCS-level] agrees |
| E7 | G102 c_S3 = 1/(2 g_s) | `experiments/20260701-g102-cs3-dbrane-normalization/results_g102.json` | read file | STRUCTURAL_RELATION_CONFIRMED | prefactor 1/2 marked [WEAK-MEDIUM] by file | not rerun in this pass |
| E8 | Gate 4B "reproduced on 2 independent grids" | `GATE4B...:70` | read | same code, 54- and 18-case runs | independence not shown | [WEAK] |

Not in this ledger yet: the full null-result audit (D), the Structural Twin pairs (C), and any exact certificate (A).
