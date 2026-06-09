# P2 Sign Convention and Selection Rule Audit

Date: 2026-06-07

## 1. Executive Verdict

[VERIFIED-SYNTHETIC] The displayed Ben Achour phase convention is the runtime default in the current codebase, and for that convention the local sign calculation gives:

```text
xi'Y = +2 i m_- Y
```

[INFERRED] The code-level status `resolved_as_typo` is a **local convention decision**, not an external or bibliographic proof.

[UNKNOWN] The Lawrence Part 3 coordinate mapping remains unresolved, so Lawrence-specific runtime claims remain blocked.

[INFERRED] The sign-gap issue is locally closed for the displayed-phase runtime convention, but it is not externally validated and it does not resolve Lawrence-specific runtime interpretation.

## 2. Convention Ledger

| Convention | Phase | `xi'` definition | Eigenvalue | Meaning of `m_-` | Status | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `BEN_ACHOUR_DISPLAYED_PHASE` | `exp(i(S phi + D theta))`, `S=m_+ + m_-`, `D=m_+ - m_-` | `xi' = partial_phi - partial_theta` | `+2 i m_-` | Wigner-aligned right label with `m = -m_-` | passed | `ben_achour_scalar_modes.py:13-14, 81-114`; `wigner_d_micro_audit.py:22-33, 219-234, 437-465`; tests `tests/test_wigner_d_micro_audit.py::test_working_convention_is_resolved_as_typo` |
| `BEN_ACHOUR_TEXT_EIGENVALUE` | same displayed phase in docs, but PDF text states the minus | same operator | `-2 i m_-` | legacy PDF-text sign | partial / legacy | `ben_achour_scalar_modes.py:13-14, 118-123`; `wigner_d_micro_audit.py:26-33, 194-208, 239-244, 471-476` |
| `WIGNER_STANDARD` | `D^j_{m',m}(a,b,c)=exp(-i m' a)d^j_{m',m}(b)exp(-i m c)` | not a separate xi' convention; mapped via Hopf-aligned coordinates | reproduces displayed-phase local sign when `a=-(phi+theta), b=2 alpha, c=phi-theta` | `m = -m_-` under the current label map | passed | `wigner_d_micro_audit.py:1-33, 156-179, 397-461`; tests `tests/test_wigner_d_micro_audit.py::test_ben_achour_modes_are_proportional_to_hopf_mapped_wigner_D` |
| `WIGNER_CONJUGATE` | `D^{j*}`-style alternative convention | not used as runtime default | would require explicit alternative phase bookkeeping | same right label only after explicit remap | unknown / not runtime default | `wigner_d_micro_audit.py:239-244, 471-476` records an alternative phase only |
| `LAWRENCE_PART3_TRANSCRIPT` | Part 3 transcript notes `alpha in [0,pi]`, `theta, theta_tilde in [0,2pi]` and a rotation angle interpretation | not explicitly encoded as a generator table | unknown | unknown | unknown | `activeContext.md:82-113, 144-191, 301-303, 891-896` |
| Current runtime code default | `ben_achour_displayed_phase` | `xi' = partial_phi - partial_theta` in code convention | `+2 i m_-` | code treats `m_-` as the displayed-phase right weight, with PDF minus as legacy | passed / local convention only | `wigner_d_micro_audit.py:219-234, 458-465`; `tests/test_wigner_d_micro_audit.py:91-140` |

## 3. Local Sign Calculation

[FACT] With

```text
Y = f(psi) * exp(i(S phi + D theta))
S = m_+ + m_-
D = m_+ - m_-
```

we have:

```text
partial_phi Y = i S Y
partial_theta Y = i D Y
(partial_phi - partial_theta) Y = i(S - D) Y = 2 i m_- Y
(partial_phi + partial_theta) Y = i(S + D) Y = 2 i m_+ Y
```

[VERIFIED-SYNTHETIC] Therefore, for the displayed phase alone:

```text
xi'Y = +2 i m_- Y
```

## 4. Wigner Mapping Table

| Wigner form | Phase | Right generator eigenvalue | Left generator eigenvalue | Compatible with displayed Ben Achour phase? |
| --- | --- | --- | --- | --- |
| `D^j_{m',m}(a,b,c)=e^{-i m' a} d^j_{m',m}(b) e^{-i m c}` | standard | right label `m = -m_-` under the Hopf-aligned map | left label `m' = m_+` | yes, with `a=-(phi+theta), b=2 alpha, c=phi-theta` |
| `D^{j*}_{m',m}` | conjugate/alternative bookkeeping only | requires explicit convention remap | requires explicit convention remap | not the runtime default |
| `D^j_{m_+,m_-}` | naive same-label use | not compatible with current Hopf-aligned map | not compatible | no for the current displayed phase mapping |
| `D^j_{m_- ,m_+}` | swapped label use | not the current code map | not the current code map | no, unless labels are redefined |
| `D^j_{m_+,-m_-}` | explicit sign-resolving map | matches current code map | matches current code map | yes, this is the current runtime label convention |

## 5. Generator Audit

| File | Function | Symbol | Role | Sign-sensitive? | Evidence |
| --- | --- | --- | --- | --- | --- |
| `ben_achour_scalar_modes.py` | `scalar_mode_unnormalized`, `ben_achour_phase_eigenvalues`, `pdf_stated_killing_eigenvalues` | `m_minus`, `xi'` | scalar-mode phase and legacy PDF sign note | yes | `ben_achour_scalar_modes.py:13-14, 81-123` |
| `wigner_d_micro_audit.py` | `ben_achour_to_wigner_labels`, `hopf_to_wigner_euler`, `get_working_convention_decision` | `m_minus`, `xi'`, `resolved_as_typo` | local convention audit and runtime default | yes | `wigner_d_micro_audit.py:156-234, 437-465` |
| `s3_reduced_matrix_elements.py` | `compute_reduced_V_element`, `reduced_element_metadata` | scale-only | reduced coefficients; no sign logic | no | `s3_reduced_matrix_elements.py:21-23, 45-71, 103-109` |
| `s3_coupling_v_option_b.py` | `_left_invariant_cg_coefficient`, `build_v_symbolic` | `j_left`, `m_left`, `j_right`, `m_right` | SU(2) coupling scaffold | indirectly, via label mapping only | `s3_coupling_v_option_b.py:76-151` |
| `s3_dirac_with_temp_coupling.py` | `build_temp_coupled_dirac` | `alpha`, `ENGINEERING_ALPHA` | operator assembly and metadata | no direct sign use | `s3_dirac_with_temp_coupling.py:31-65` |
| `s3_spinor_spectral_labels.py` | `generate_spectral_spinor_records` | `convention`, `su2_L_label`, `su2_R_label` | representation scaffold | no direct sign use | `s3_spinor_spectral_labels.py:25-83` |

## 6. Ladder Consistency

| Convention | Raising action | Lowering action | Algebra consistent? | Runtime compatible? | Risk |
| --- | --- | --- | --- | --- | --- |
| `+2 i m_-` (displayed phase) | right-raising changes the current right weight in the positive direction under the current label map | right-lowering decreases the right weight | yes at the level of the current code convention | yes | Lawrence mapping still unknown |
| `-2 i m_-` (PDF-text minus) | would reverse the right-weight interpretation unless labels are explicitly redefined | would reverse the right-weight interpretation unless labels are explicitly redefined | only if the entire sign convention is reparameterized consistently | not runtime default | high: silent convention drift |

[UNKNOWN] The current runtime does not encode a separate Lawrence-compatible ladder table; it encodes only the displayed-phase convention and the local sign decision.

## 7. V Selection-Rule Audit

| Convention | Allowed `Δm_+` | Allowed `Δm_-` | Allowed component coupling | Forbidden coupling | Evidence |
| --- | ---: | ---: | --- | --- | --- |
| displayed-phase runtime convention | not directly controlled by sign; current code uses SU(2) CG on `m_left` | not directly controlled by sign; current code does not use `m_-` from Ben Achour scalar phase in the runtime V assembly | `q_left in {-1,0,1}`, `j_right` conserved, `m_right` conserved | same-side `j_left=0 -> 0` and mismatched right labels | `s3_coupling_v_option_b.py:76-151`; `tests/test_hermiticity_condition_skeleton.py:24-70` |
| PDF-text minus convention | would require explicit redefinition of the right-weight labeling to preserve semantics | would require explicit redefinition | not encoded explicitly | not encoded explicitly | `ben_achour_scalar_modes.py:118-123`; `wigner_d_micro_audit.py:193-208, 239-244` |

[INFERRED] In the current implementation, `V` selection rules are **runtime independent of normalization scale** and do not depend on the old `sqrt(2)` factor. They are also not presently derived from a separate Lawrence mapping.

## 8. SELF-ORACLE Analysis

| Test | What it checks | Oracle type | Max closure | Risk |
| --- | --- | --- | --- | --- |
| `tests/test_wigner_d_micro_audit.py::test_ben_achour_modes_are_proportional_to_hopf_mapped_wigner_D` | Ben Achour scalar mode proportionality to Wigner-D | SELF-ORACLE for sign/label alignment, not external proof | L2/L3 for phase identity only | not Lawrence proof |
| `tests/test_wigner_d_micro_audit.py::test_working_convention_is_resolved_as_typo` | local runtime decision `resolved_as_typo` | SELF-ORACLE / convention audit | L2 | not external bibliographic proof |
| `tests/test_s3_dirac_temp_coupling.py` | Hermiticity, zero-coupling limit, metadata | SELF-ORACLE runtime consistency | L2 | not selection-rule proof against Lawrence |
| `tests/test_s3_dirac_toy_test_alpha.py` | Hermiticity, symmetry, no forbidden-zone violation | SELF-ORACLE runtime consistency | L2 | same operator pipeline under test |
| `tests/test_s3_dirac_spectrum_viz.py` | trajectory shape, plotting, `lambda=0` consistency | SELF-ORACLE / runtime consistency | L1/L2 | plot existence is not external validation |

## 9. Lawrence Quarantine Verdict

```text
unknown
```

[UNKNOWN] The Part 3 transcript notes and `activeContext.md` still do not provide an explicit verified coordinate/sign translation table sufficient to make Lawrence-specific runtime claims safe.

## 10. Normalization Interaction Verdict

```text
no
```

[INFERRED] The current direct Haar/unit-coframe normalization does not affect the P2 sign/selection-rule layer in the runtime code path. The sign convention is encoded separately from scale.

## 11. Atomic Claim Table

| ID | Claim | Status | Closure | Evidence | Risk |
| -- | -- | -- | -- | -- | -- |
| P2-1 | Displayed phase implies `xi'Y = +2 i m_- Y` | passed | L2/L3 | `ben_achour_scalar_modes.py:81-123`; `wigner_d_micro_audit.py:182-234`; tests `tests/test_wigner_d_micro_audit.py::test_xi_prime_sign_is_resolved_as_typo_after_wigner_mapping` | external proof absent |
| P2-2 | `resolved_as_typo` is a local code convention only | passed | L1/L2 | `wigner_d_micro_audit.py:219-234, 458-465`; `tests/test_wigner_d_micro_audit.py::test_working_convention_is_resolved_as_typo` | not bibliographic proof |
| P2-3 | `Wigner standard` mapping matches displayed phase | passed | L2/L3 | `wigner_d_micro_audit.py:1-33, 156-179`; `tests/test_wigner_d_micro_audit.py::test_ben_achour_modes_are_proportional_to_hopf_mapped_wigner_D` | Lawrence mapping missing |
| P2-4 | `V` selection rules in runtime are sign-neutral w.r.t. `sqrt(2)` migration | passed | L2 | `s3_coupling_v_option_b.py:76-151`; no runtime `sqrt(2)` in runtime modules | future label reinterpretation remains possible |
| P2-5 | Lawrence mapping is runtime-safe | unknown | L0 | no explicit mapping table in code/docs | blocks Lawrence-specific claims |
| P2-6 | Normalization migration affects selection rules | failed / no | L2 | sign logic and scale logic are separated in code; runtime scale no longer contains `sqrt(2)` | selection rules still blocked by missing Lawrence mapping |

## 12. Tests to Add

| Test file | Test name | Purpose | Expected failure caught |
| --- | --- | --- | --- |
| `tests/test_sign_convention_selection_rules.py` | `test_displayed_vs_pdf_text_convention` | compare displayed phase and PDF-text sign behavior | silent flip between `+2im_-` and `-2im_-` |
| `tests/test_sign_convention_selection_rules.py` | `test_wigner_label_map_stays_fixed_under_scale_change` | ensure normalization changes do not change sign map | accidental coupling of scale and sign |
| `tests/test_lawrence_mapping_quarantine.py` | `test_runtime_requires_explicit_lawrence_mapping` | block Lawrence-specific use without translation table | silent assumption that mapping is known |
| `tests/test_v_selection_rules.py` | `test_v_coupling_respects_current_cg_rules` | assert current `V` selection rules on `m_left/m_right` | hidden drift in selection rules |
| `tests/test_convention_metadata.py` | `test_generated_objects_expose_sign_and_scale_metadata` | require explicit convention metadata in runtime objects | ambiguous sign/scale metadata |

## 13. Documentation Patch

[CODE] Suggested `activeContext.md` wording:

```text
P2 sign audit verdict:
The displayed Ben Achour phase is the runtime default and locally implies
xi' = partial_phi - partial_theta -> +2 i m_-.

Status label `resolved_as_typo` is a local code convention only, not an
external bibliographic proof.

The current V-selection rules are runtime-independent of the direct Haar
normalization scale, but Lawrence-specific runtime claims remain blocked until
a verified coordinate/sign translation table is available.

Next gate:
P2_SIGN_CONVENTION_AND_SELECTION_RULE_AUDIT
```

## 14. Final Runtime Verdict

```text
blocked_by_mapping
```

[INFERRED] The current code is safe for the displayed-phase local convention and the exact direct Haar runtime normalization, but Lawrence-specific runtime interpretation remains blocked until the coordinate/sign mapping is explicit.
