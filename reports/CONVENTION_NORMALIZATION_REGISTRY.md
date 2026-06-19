# Convention / Normalization Registry

**Runtime:** research_only | **safe_for_runtime:** no

## Frozen gates (P13A–P13G)

| Gate | Status | Key field | Path |
|------|--------|-----------|------|
| P11 | fixed | Wigner/CG zero pattern | `docs/compactification/registry/P11_robust_wigner_cg_pattern.yaml` |
| P12 | fixed | normalization_dependent scale | `docs/compactification/registry/P12_matrix_element_pattern.yaml` |
| P13A | fixed | V-operator ansatz | `docs/compactification/registry/P13A_v_operator_ansatz.yaml` |
| P13B1 | fixed | spinor basis | `docs/compactification/registry/P13B1_spinor_basis.yaml` |
| P13C | fixed | Ben Achour E_i / E'_i | `docs/compactification/registry/P13C_ben_achour_sources.yaml` |
| P13D | fixed | convention stack | `docs/compactification/registry/P13D_convention_stack.yaml` |
| P13E | fixed | **NORMALIZATION_DEPENDENT_NO_GO** | `docs/compactification/registry/P13E_no_go.yaml` |
| P13F | fixed | NO_GO + FREE_COUPLING_PARAMETER | `docs/compactification/registry/P13F_no_go.yaml` |
| P13G | fixed | handoff / limitations | `docs/compactification/registry/P13G_handoff.yaml` |

**P13E/P13F statuses are immutable from P13H** unless a separate gate with evidence overwrites.

## P13H result (2026-05-25)

| Field | Value |
|-------|-------|
| Classification | `NORMALIZATION_DEPENDENT_NO_GO` |
| lambda | `FREE_COUPLING_PARAMETER` |
| P11 pattern (0,1) | zero — compatible |
| Diagonal (1,1) convention | **not** invariant under P13G conventions |
| Hermiticity | preserved |
| Report | `reports/P13H_S3_ABSOLUTE_NORMALIZATION_INTEGRAL_TEST.md` |

## Classifications enum

`CONVENTION_FIXED_CANDIDATE` | `NORMALIZATION_DEPENDENT_NO_GO` | `FREE_COUPLING_PARAMETER_CONFIRMED` | `BASIS_ORDERING_DEPENDENT` | `PHASE_DEPENDENT` | `FAILED` | `INCONCLUSIVE`

Code: `cc_toy_lab/compactification/convention_registry.py`
