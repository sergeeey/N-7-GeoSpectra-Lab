# P1 Post-Normalization Migration Audit

Date: 2026-06-07

## 1. Executive Verdict

[VERIFIED-SYNTHETIC] The normalization migration to the exact direct Haar / unit-coframe scale is closed at **L2** for the current runtime smoke stack.

```text
canonical runtime convention = ||e^i|| = 1
```

[INFERRED] The migration is supported by code inspection, runtime metadata, and unit tests, but it is not externally/bibliographically validated as a physical theorem. The Ben Achour `E/E'` mapping remains separate and unresolved.

[UNKNOWN] The Lawrence coordinate mapping is still not established well enough for runtime use.

## 2. Atomic Claim Table

| ID | Claim | Status | Closure | Evidence | Risk |
| -- | -- | -- | -- | -- | -- |
| N1 | `||e^i|| = 1` is the canonical runtime convention | passed | L2 | `s3_reduced_matrix_elements.py: DIRECT_HAAR_ONE_FORM_SCALE = 1.0`; `s3_dirac_with_temp_coupling.py` metadata `one_form_scale = 1.0`; `s3_oneform_laplacian_numerical.py` target norm 1.0; `python -m pytest -q tests/` -> `72 passed` | external normalization still unresolved |
| N2 | Old `sqrt(2)` runtime scale is not used in operator code | passed | L1/L2 | `rg -n \"sqrt\\(2\\)|1\\.414|0\\.707\"` on runtime modules returned no matches; runtime scale constants resolve to `1.0` | temporary alias names still remain |
| N3 | Haar/coframe normalization is aligned with the current runtime path | passed | L2 | `s3_reduced_matrix_elements.py`, `s3_dirac_with_temp_coupling.py`, `s3_oneform_laplacian_numerical.py`; smoke tests green | one-form basis mapping unresolved |
| O1 | `D0` has correct scale | passed | L2 | `s3_dirac_spectral_operator.py::build_dirac_matrix`; `tests/test_s3_dirac_exact_baseline.py`; `python -m pytest -q tests/` | none within current scope |
| O2 | `V` has correct runtime scale | partial | L2 | `s3_coupling_v_option_b.py::build_v_symbolic` uses direct Haar scale 1.0 and hermitian symmetrization; tests pass | Ben Achour `E/E'` mapping unresolved; scale is engineering, not final analytic mapping |
| O3 | `D = D0 + V` is Hermitian | passed | L2 | `tests/test_s3_dirac_temp_coupling.py::test_temp_coupled_operator_is_hermitian`; `tests/test_s3_dirac_toy_test_alpha.py::test_d_is_hermitian` | hermiticity is internal-consistency only |
| S1 | Sign gap is unaffected by normalization migration | passed | L1/L2 | `ben_achour_scalar_modes.py` and `wigner_d_micro_audit.py` hard-code sign convention independently of normalization constants; no runtime sqrt2 leakage in sign modules | Lawrence mapping still open |
| S2 | Ben Achour `E/E'` mapping is quarantined from runtime scale | passed | L1/L2 | `reduced_element_metadata()["final_ben_achour_normalization"] == "unresolved"`; reports and metadata explicitly separate mapping from scale | representation-detail remains unresolved |
| L1 | Lawrence coordinate mapping is established | unknown | L0 | `activeContext.md` still records the mapping problem as unresolved; no explicit verified coordinate table in code | could affect sign-sensitive selection rules |

## 3. Scale Ledger

| Object | Expected convention | Code convention | Evidence | Risk |
| -- | -- | -- | -- | -- |
| `e^i` | unit coframe | `1.0` | `s3_reduced_matrix_elements.py`, `s3_dirac_with_temp_coupling.py`, `s3_oneform_laplacian_numerical.py` | direct coframe norm is not the final Ben Achour basis map |
| Haar measure | direct Haar / unit-coframe compatible | used in reports and diagnostics | `geometry_s3_hopf.py`, `reports/S3_ONEFORM_NORM_NUMERICAL_P1.md` | current diagnostic is not a graph-Laplacian proof |
| scalar inner product | displayed-phase scalar-mode convention | isolated in `ben_achour_scalar_modes.py` | phase test modules and `wigner_d_micro_audit.py` | sign convention still matters for `xi'` |
| one-form inner product | direct Haar unit scale | `1.0` | `s3_oneform_laplacian_numerical.py` | Ben Achour basis mapping unresolved |
| `D0` | clean exact baseline | exact spectral baseline | `s3_dirac_spectral_operator.py` and `tests/test_s3_dirac_exact_baseline.py` | none in current scope |
| `V` | working Option B smoke scale | direct Haar scale 1.0 with hermitian symmetrization | `s3_coupling_v_option_b.py`, `tests/test_s3_dirac_temp_coupling.py` | not the final physical matrix element |
| plotted eigenvalues | direct Haar exact-scale sweep | `D(lambda) = D0 + lambda V` | `s3_dirac_spectrum_viz.py`, `reports/S3_DIRAC_SPECTRUM_SWEEP_ANALYSIS_P1D.md` | preliminary only |

## 4. Hidden Convention Leakage

| File | Function / Context | Constant / Phrase | Meaning | Safe? | Covered by test? |
| -- | -- | -- | -- | -- | -- |
| `s3_reduced_matrix_elements.py` | module constants | `TEMPORARY_ENGINEERING_ONE_FORM_SCALE = 1.0` | historical alias only; numerical value is direct Haar scale | mostly safe, but name is legacy | yes, metadata test covers value |
| `s3_reduced_matrix_elements.py` | module constants | `TEMPORARY_ENGINEERING_ALPHA = 1.0` | engineering alias for alpha default | safe numerically; semantically legacy | yes, metadata test covers value |
| `s3_dirac_with_temp_coupling.py` | metadata | `warning = direct Haar/unit-coframe normalization; final Ben_Achour basis mapping unresolved` | explicit quarantine of final mapping | safe | yes |
| `s3_oneform_laplacian_numerical.py` | diagnostic metadata | `temporary_engineering_target_norm = 1.0` | alias to direct Haar target norm | safe numerically; legacy name remains | yes |
| `ben_achour_scalar_modes.py` | scalar phase docs | `xi'(Phi_i)=nu_i Phi_i with nu_i=-2 i m_-` in docstring caveat | legacy PDF-text minus preserved as note | safe if treated as legacy only | yes, sign tests cover the displayed-phase convention |
| `wigner_d_micro_audit.py` | working convention | `gap_status = resolved_as_typo` | downstream sign decision | safe as code convention | yes |

## 5. SELF-ORACLE Analysis

| Test | What it checks | Oracle type | Max closure level | Risk |
| -- | -- | -- | -- | -- |
| `tests/test_s3_dirac_temp_coupling.py` | Hermiticity, alpha=0 -> D0, nonzero V, metadata | SELF-ORACLE / runtime consistency | L2 | hermiticity is enforced by construction; spectral claim is smoke-only |
| `tests/test_s3_dirac_toy_test_alpha.py` | Hermiticity, symmetry, no forbidden zone, metadata | SELF-ORACLE / runtime consistency | L2 | uses same coupled operator pipeline as object under test |
| `tests/test_s3_oneform_laplacian_numerical.py` | raw coframe norm and Gram symmetry | independent math diagnostic, but still implementation-linked | L2 | not a graph-Laplacian convergence proof |
| `tests/test_s3_dirac_spectrum_viz.py` | trajectory shape, file creation, lambda=0 consistency | SELF-ORACLE / runtime consistency | L1/L2 | plot existence does not validate external physics |
| `tests/test_wigner_d_micro_audit.py` | displayed phase vs sign convention and label mapping | mixed: direct symbolic check + convention audit | L2/L3 for the phase identity, not for Tom's theory | does not establish Lawrence mapping |

## 6. Sign-Gap Interaction

[VERIFIED-SYNTHETIC] The normalization migration does **not** change the sign-gap conclusion in the current runtime stack.

Reason:

- sign handling is isolated in `ben_achour_scalar_modes.py` and `wigner_d_micro_audit.py`;
- direct Haar normalization lives in `s3_reduced_matrix_elements.py`, `s3_dirac_with_temp_coupling.py`, and `s3_oneform_laplacian_numerical.py`;
- no runtime `sqrt(2)` literal appears in the targeted runtime modules;
- the sign decision is still recorded as `resolved_as_typo` in code.

[UNCERTAIN] The only remaining way scale could matter would be through a future explicit Lawrence coordinate mapping that couples sign-sensitive basis labels to representation normalization. That mapping is not established yet.

## 7. Recomposition Verdict

[VERIFIED-SYNTHETIC] Closed now:

- direct Haar / unit-coframe runtime normalization;
- clean exact baseline `D0`;
- Hermitian smoke operator `D = D0 + V`;
- preliminary exact-scale spectrum sweep;
- documentation consistently labels Ben Achour `E/E'` mapping as unresolved.

[UNKNOWN] Still open:

- Lawrence coordinate mapping;
- final Ben Achour `E/E'` basis normalization;
- physical interpretation of `V`;
- any selection-rule statement that depends on unresolved mapping.

[INFERRED] Main residual risk is not scale leakage; it is sign-sensitive representation mapping.

## 8. New Tests to Add

| Test file | Test name | Purpose | Expected failure caught |
| -- | -- | -- | -- |
| `tests/test_no_hidden_sqrt2_runtime.py` | `test_no_sqrt2_literal_in_runtime_modules` | guard against future hidden scale reintroduction | accidental reappearance of `sqrt(2)` / `0.707` / `1.414` in runtime code |
| `tests/test_s3_convention_metadata.py` | `test_generated_objects_include_convention_metadata` | require explicit scale/sign metadata | missing or ambiguous normalization metadata |
| `tests/test_s3_dirac_randomized_hermiticity.py` | `test_randomized_hermiticity_small_matrices` | smoke-check Hermiticity under randomized small perturbations | wrong conjugation / asymmetry in coupling assembly |
| `tests/test_s3_oneform_laplacian_lowmode_oracle.py` | `test_lowmode_oracle_against_independent_formula` | compare against hard-coded independent low-mode oracle | self-oracle leakage in one-form diagnostic |
| `tests/test_normalization_sign_gap_independence.py` | `test_scale_metadata_does_not_change_sign_convention` | ensure normalization migration leaves sign convention unchanged | accidental coupling between scale and sign |
| `tests/test_lawrence_mapping_quarantine.py` | `test_lawrence_mapping_required_for_runtime_use` | block runtime use without explicit coordinate mapping | silent assumption that Tom/Lawrence mapping is known |

## 9. Documentation Patches

[CODE] Suggested wording for `activeContext.md` and reports:

```text
Canonical runtime normalization:
exact direct Haar / unit-coframe scale, ||e^i|| = 1.

Deprecated:
sqrt(2)-scaled convention is no longer used as runtime operator scale.

Quarantined:
Ben Achour E/E' basis mapping is representation-detail only.

Open:
sign gap remains unresolved and is independent from normalization migration unless explicitly shown otherwise.

Blocked:
Lawrence Dirac/spinor validation requires coordinate/sign convention translation table.
```

## 10. Next Hard Gate

```text
P2_SIGN_CONVENTION_AND_SELECTION_RULE_AUDIT
```

[CODE] The next gate must prove or refute that the Ben Achour / Wigner / Lawrence sign convention implies the correct SU(2)_L / SU(2)_R weights and V-coupling selection rules independently of normalization scale.
