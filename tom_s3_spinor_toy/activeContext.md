# Active Context — Tom S3 Spinor Toy

Updated: 2026-06-08
Scope: local memory for future Codex/agent sessions started in `tom_s3_spinor_toy/`.

## Current Focus

[USER-PROVIDED] This project is not intended to refute or validate Tom Lawrence's full Covariant Compactification theory. It is a collaborative computational sanity-check layer for the S3 harmonic/spinor conventions in Tom's Part 3 work:

- coordinate choice;
- volume measure / Jacobian;
- weighted vs unweighted inner product;
- alpha-dependence;
- scalar/vector/spinor basis separation;
- representation covariance;
- reproducible lightweight Python diagnostics.

Internal working formula:

```text
Tom S3 toy = translation/debug layer between Tom's analytic construction
and reproducible computational checks.
```

## Project Separation

[CODE] `GeoSpectra main` is a falsification-first numerical harness. It is not a test of Tom Lawrence's theory.

[CODE] `tom_s3_spinor_toy` is separate from Gate4B/Gate4C/negative-controls work. Do not mix commits, reports, or claims between these tracks.

[USER-PROVIDED] Do not mix Tom Lawrence / Covariant Compactification with IDM/MULTING / multipole-force cosmology / Buckholtz. That was a separate author/theory track.

## Operational State

[CODE] Current phase map:

```text
Phase 0 — design spec done
Phase 1 — literature/PDF verification done
Phase 2 — small numerical sanity tester done
Phase 3 — cautious message to Tom sent
Phase 4 — blocked on exact alpha / measure / generator equations
```

[VERIFIED] Local check run on 2026-06-07:

```text
python -m pytest -q .\tests
11 passed, 12 warnings
```

Warnings are from deprecated `np.trapz`; they do not change the current scientific interpretation.

## Scientific Frame

[CODE] Current Phase 2 result is a sanity baseline only:

```text
In standard Hopf S3 geometry with alpha in [0, pi/2],
sqrt(sin(2 alpha)) behaves like sqrt(volume density),
not like a standard Camporesi-Higuchi Dirac eigenspinor radial function.
```

[USER-PROVIDED] This must not be phrased as:

```text
Tom is wrong.
We solved Tom's problem.
Phase 2 refutes or validates Covariant Compactification.
```

Allowed framing:

```text
This may clarify a convention.
This diagnostic shows what happens under this coordinate/measure choice.
If Tom's basis differs, test covariance rather than Dirac eigenspinor identity.
```

## Updated Tom Part 3 Context

[USER-PROVIDED] The current working understanding of Tom Lawrence's Part 3 video:

- Background programme: Covariant Compactification, with geometry of higher-dimensional spacetime, especially product geometry `S3 x S6`.
- One fermion generation, including right-handed neutrino, is treated as 32 states that can be organised into a spinor structure.
- For massless fermions before Higgs mass acquisition, a 16-component spinor is sufficient.
- The 16 states are intended to arise as harmonics on `S3 x S6`.
- `S3` has isometry related to `SO(4) ~= SU(2)_L x SU(2)_R`.
- Rotations/diffeomorphisms on `S3` act on harmonics and mix components like `SU(2)_L` and `SU(2)_R` representations.
- `S6` / `SO(6) ~= SU(4)` supplies the route toward colour `SU(3)`.
- Right-handed neutrino is postulated as a background/deep-space harmonic; its stabiliser is described as `SU(2)_L x U(1)_Y x SU(3)_C`.
- Higgs integration remains open; Forgacs-Manton type mechanisms may be relevant.

## Tom's Current S3 Convention Questions

[USER-PROVIDED] Tom's alpha is currently understood as:

```text
alpha in [0, pi]
theta, theta_tilde in [0, 2pi]
theta = 2 alpha is NOT used by Tom
alpha is the rotation angle between two independent planes
```

[CODE] Our current Phase 2 code uses standard Hopf coordinates:

```text
alpha in [0, pi/2]
sqrt(g) = sin(alpha) cos(alpha)
sqrt(sin(2 alpha)) is real on this domain
```

[INFERRED] This is the main convention mismatch. If alpha is extended to `[0, pi]`, then `sin(alpha) cos(alpha)` and `sin(2 alpha)` change sign after `pi/2`, so `sqrt(sin(2 alpha))` becomes imaginary unless Tom's convention uses a patch, absolute Jacobian, signed coordinate, phase convention, or different measure.

## Harmonic Basis Difference

[USER-PROVIDED] Tom uses a harmonic expansion of a one-component real scalar field, especially `sqrt(|g|)` / root mod G. The idea is that scalar geometric harmonics or their linear combinations transform as spinor fields under diffeomorphisms.

[CODE] Our Phase 2 comparison used Camporesi-Higuchi Dirac eigenspinors as a reference baseline.

[INFERRED] Therefore:

```text
Camporesi-Higuchi is a reference baseline, not the judge of Tom's construction.
If Tom's objects are scalar harmonic combinations transforming as spinors,
the correct test is representation covariance, not only eigenspinor identity.
```

## Coefficients and Real Combination Constraint

[USER-PROVIDED] There is no explicit closed formula yet for the coefficients `c_n`; this is still a system of mathematical constraints.

[USER-PROVIDED] Since `sqrt(|g|)` is real and Tom's spinor functions are complex, fundamental spinors can enter the expansion only in real combinations.

[INFERRED] This indicates the theory is currently at:

```text
conceptual representation programme + partial algebra,
not yet a closed constructive harmonic expansion.
```

This is exactly where lightweight computational diagnostics can help.

## cot(2 alpha) Issue

[USER-PROVIDED] `cot(2 alpha)` arises when Tom tries to analytically find the fundamental spinor dependence on alpha. Applying a differential generator such as `I_{1R}` to a right-handed doublet and equating it to matrix-generator action yields coupled differential equations. After choosing trigonometric alpha factors to cancel exponentials in `theta` and `theta_tilde`, the remaining equations become inconsistent and would require `cot(2 alpha)` to be imaginary.

[USER-PROVIDED] "Imaginary" here means mathematical inconsistency, not a physical signature or analytic continuation.

Current strongest hypothesis:

```text
[HYPOTHESIS]
The cot(2 alpha) / imaginary inconsistency may be caused by extending a half-domain
Hopf-like normalization or volume factor across alpha in [0, pi], where sin(2 alpha)
changes sign.
```

Do not present this as confirmed.

## Main Open Blockers

Need from Tom or raw slides/equations:

1. Exact embedding formula for `x1..x4(alpha, theta, theta_tilde)` and coordinate identifications, especially for `alpha > pi/2`.
2. Exact Jacobian / measure in the overlap integral over the whole `S3`.
3. Full differential operator form for `I_{1R}` or the relevant generator.
4. Matrix generator action being matched to the differential operator.
5. The two coupled differential equations where `cot(2 alpha)` appears.
6. Whether the desired condition is eigenfunction status or covariance under group action.
7. How the real-combination constraint is imposed on the complex spinor basis.

Without these, diagnostics are useful but cannot close Tom's problem.

## Safe Next Action

If work proceeds before Tom replies, do only a small Phase 4 diagnostic:

```text
1. Use alpha in [0, pi].
2. Compare:
   sin(alpha) cos(alpha)
   abs(sin(alpha) cos(alpha))
   sin(2 alpha)
   abs(sin(2 alpha))
   sqrt(sin(2 alpha))
   sqrt(abs(sin(2 alpha)))
3. Mark real vs imaginary domains.
4. Check whether alpha in [0, pi] behaves like a double-cover or signed-radius chart.
5. Formulate a focused question:
   "Is your alpha chart patch-wise, signed, or using an absolute Jacobian?"
```

No heavy compute is needed for this.

## Ben Achour Scalar-Mode Layer

[VERIFIED] `C:\Users\serge\Downloads\1505.03426v2 (1).pdf` was rechecked on 2026-06-07. It confirms:

```text
Ben Achour standard Hopf alpha: [0, pi/2]
metric: ds^2 = d alpha^2 + cos^2(alpha) d theta^2 + sin^2(alpha) d phi^2
volume density: sqrt(g) = sin(alpha) cos(alpha)
```

[CODE] `ben_achour_scalar_modes.py` implements the displayed scalar-mode convention for lightweight checks only. It is not a Dirac spinor-harmonic implementation.

[VERIFIED] `tests/test_ben_achour_scalar_modes.py` passed locally on 2026-06-07.

[VERIFIED] Important sign-convention caveat: the rendered PDF displays the scalar phase as:

```text
exp(i(S phi + D theta)), S = m_+ + m_-, D = m_+ - m_-
```

This displayed phase gives:

```text
(partial_phi + partial_theta) Phi = +2 i m_+ Phi
(partial_phi - partial_theta) Phi = +2 i m_- Phi
```

but the PDF-stated line below eqs. (4)-(5) says:

```text
xi'(Phi_i) = nu_i Phi_i, nu_i = -2 i m_-
```

[INFERRED] The displayed Ben Achour scalar phase and the printed `xi'` generator are now treated as a resolved typographical sign issue in the codebase. For Tom-facing work, keep the displayed-phase convention as default and treat the PDF-text minus as a legacy note only.

## Wigner-D Micro-Audit Layer

[CODE] `wigner_d_micro_audit.py` implements a tiny no-heavy-dependency bridge from the displayed Ben Achour scalar modes to Wigner-D matrix elements.

[VERIFIED-SYNTHETIC] Local checks run on 2026-06-07:

```text
python -m pytest -q .\tests\test_wigner_d_micro_audit.py
13 passed

python -m pytest -q .\tests
28 passed, 12 warnings
```

[VERIFIED-SYNTHETIC] The convention used by the audit is:

```text
D^j_{m',m}(a,b,c) = exp(-i m' a) d^j_{m',m}(b) exp(-i m c)

a = -(phi + theta)
b = 2 alpha
c = phi - theta

j = L/2
m' = m_plus
m = -m_minus
```

[VERIFIED-SYNTHETIC] For small modes `L=0,1,2`, the unnormalised Ben Achour scalar modes are proportional to the Hopf-mapped Wigner-D functions up to a constant sign/normalisation factor. The generated report is:

```text
reports/WIGNER_D_MICRO_AUDIT_2026-06-07.md
reports/WIGNER_D_MICRO_AUDIT_2026-06-07.json
```

[VERIFIED-SYNTHETIC] This Wigner-D alignment reproduces the displayed Ben Achour phase and therefore fixes the sign convention in favor of the displayed-phase mapping:

```text
xi  = partial_phi + partial_theta -> +2 i m_plus
xi' = partial_phi - partial_theta -> +2 i m_minus
```

while the rendered PDF text states:

```text
xi' -> -2 i m_minus
```

[VERIFIED-SYNTHETIC] A follow-up audit checked the proposed direct Euler-swap explanation:

```text
a = theta_H
b = 2 alpha
c = phi_H
```

Under the Wigner-D convention used here, this direct swap cannot match the displayed Ben Achour phase for the whole PDF-valid label range: for `L=2, m_+=1, m_-=1`, the required Wigner label leaves `[-j,j]`.

[VERIFIED-SYNTHETIC] The PDF-stated pair of eigenvalues would be consistent with the phase:

```text
exp(i(D phi + S theta))
```

rather than the displayed:

```text
exp(i(S phi + D theta))
```

[INFERRED] Therefore the `xi'` issue is recorded in the codebase as `resolved_as_typo` for the displayed-phase convention. The legacy PDF-text minus remains documented as an alternative text convention only, not the default downstream choice.

[VERIFIED-SYNTHETIC] PDF archaeology on 2026-06-07 checked the available Tom/Lawrence PDFs, including `Covariant Compactification Toy Lab`, `Mathematics of Kaluza-Klein unification - correctedv2`, and `preprints202303.0314.v1`. These did not contain an explicit S3 Hopf/Wigner phase, `xi'` generator convention, or angle-map formula sufficient to override the displayed-phase convention.

[CODE] Working convention decision adopted on 2026-06-07:

```text
convention_id = ben_achour_displayed_phase
phase = exp(i(S phi + D theta))
S = m_+ + m_-
D = m_+ - m_-
xi' = partial_phi - partial_theta -> +2 i m_-
gap_status = resolved_as_typo
```

[INFERRED] This is now the operational default for downstream code. The alternative convention remains recorded as a legacy paper-text note:

```text
phase = exp(i(D phi + S theta))
xi' -> -2 i m_-
```

[INFERRED] The next useful representation-sanity step is to keep downstream spinor/Dirac checks under the explicit `ben_achour_displayed_phase` convention while preserving the legacy PDF-text sign as a parameterised compatibility note.

## Exact Clean S3 Dirac Baseline

[CODE] P0 exact clean `S3` Dirac baseline added on 2026-06-07:

```text
s3_dirac_exact_baseline.py
tests/test_s3_dirac_exact_baseline.py
```

[CODE] The analytic baseline implements:

```text
lambda_{k,+/-} = +/- (k + 3/2) / R
degeneracy per sign = (k + 1)(k + 2)
k = 0, 1, 2, ...
```

[VERIFIED-SYNTHETIC] Local P0 check:

```text
python -m pytest -q .\tests\test_s3_dirac_exact_baseline.py
6 passed
```

[VERIFIED-SYNTHETIC] This verifies only the analytic/unit-test negative-control mechanics:

```text
positive/negative spectral symmetry
no zero eigenvalues on clean round S3 for R > 0
first R=1 levels +/-1.5, +/-2.5, +/-3.5
degeneracies 2, 6, 12 per sign for k=0,1,2
radius scaling as 1/R
```

[NEEDS-REAL-DATA] No numerical kNN Dirac validation exists yet for this baseline.

[INFERRED] `SU(2)` instanton, index, spectral flow, eta invariant, and zero-mode claims remain backlog. Do not use this P0 baseline to claim a gauge-field result.

## P1 Design Gate

[CODE] P1 design gate recorded on 2026-06-07:

```text
reports/S3_DIRAC_P1_DESIGN_GATE.md
```

[INFERRED] Preferred P1 route is `Spectral/Wigner-D`, but the current status is `DESIGN_ONLY`, not implementation.

[INFERRED] Point-cloud `kNN` graph Dirac and Hopf finite-difference Dirac are explicitly `NO_GO_NOW` because they require unresolved frame, spin connection, transport, Hermiticity, and convergence machinery.

[INFERRED] The next safe coding slice is:

```text
P1a_SPECTRAL_LABEL_SCAFFOLD
```

Allowed in P1a:

```text
generate spectral spinor-branch records
attach explicit ben_achour_displayed_phase convention metadata
compare labels/eigenvalues/degeneracies against P0 exact baseline
assert no zero modes in clean round S3
```

Not allowed in P1a:

```text
kNN graph Dirac
graph spin connection
Hopf finite-difference Dirac
SU(2) instanton
index/chirality/spectral-flow/eta-invariant claims
zero-mode claims
heavy diagonalisation
```

## P1a Spectral Label Scaffold

[CODE] P1a spectral spinor label scaffold implemented on 2026-06-07:

```text
s3_spinor_spectral_labels.py
tests/test_s3_spinor_spectral_labels.py
```

[CODE] `generate_spectral_spinor_records(k_max, radius=1.0, convention="ben_achour_displayed_phase")` emits records with:

```text
k
branch
eigenvalue
degeneracy_per_branch
su2_L_label
su2_R_label
convention
note
```

[INFERRED] The current representation scaffold uses:

```text
positive branch: (j_L, j_R) = ((k + 1)/2, k/2)
negative branch: (j_L, j_R) = (k/2, (k + 1)/2)
```

so each branch has:

```text
(2 j_L + 1)(2 j_R + 1) = (k + 2)(k + 1)
```

[VERIFIED-SYNTHETIC] Local P1a check:

```text
python -m pytest -q .\tests\test_s3_spinor_spectral_labels.py
5 passed
```

[VERIFIED-SYNTHETIC] P1a tests compare eigenvalues and degeneracies against `s3_dirac_exact_baseline.py` for `k=0..3`, require explicit convention metadata, assert no zero eigenvalues, and assert branch symmetry.

[INFERRED] Spectral/Wigner basis scaffolding is now ready as metadata/label infrastructure only.

[CODE] Implementation of the actual spectral Dirac operator is still not started.

[INFERRED] `SU(2)` instanton, index, chirality, spectral flow, eta invariant, and zero-mode claims remain backlog.

## P1b Diagonal Spectral Dirac Operator Prototype

[CODE] P1b diagonal spectral operator prototype implemented on 2026-06-07:

```text
s3_dirac_spectral_operator.py
tests/test_s3_dirac_spectral_operator.py
```

[CODE] `build_dirac_matrix(k_max, radius=1.0, convention="ben_achour_displayed_phase")` builds a `scipy.sparse.csr_matrix` in the exact spectral branch basis. The matrix is diagonal because the basis is already the clean Dirac eigenbasis.

[CODE] Diagonal entries are generated from `generate_spectral_spinor_records(...)`; each branch eigenvalue is repeated according to `degeneracy_per_branch`.

[VERIFIED-SYNTHETIC] Local P1b check:

```text
python -m pytest -q .\tests\test_s3_dirac_spectral_operator.py
5 passed
```

[VERIFIED-SYNTHETIC] P1b tests check:

```text
matrix shape equals total P0 mode count
dense eigvalsh for small k_max matches P0 exact baseline
Hermiticity
no zero modes in clean round S3
diagonal entries follow P1a records
```

[INFERRED] This is a spectral diagonal prototype, not a full wavefunction-level Dirac construction.

[CODE] Off-diagonal matrix elements, gauge-field couplings, 3j-symbol interactions, instanton backgrounds, index/chirality/spectral-flow/eta-invariant claims, and zero-mode claims are still not started.

## P1c Gauge Background Design Gate

[CODE] P1c gauge-background design gate recorded on 2026-06-07:

```text
reports/S3_DIRAC_P1C_GAUGE_BACKGROUND_DESIGN_GATE.md
```

[INFERRED] The design gate separates four options:

```text
A. Pure spectral toy Hermitian SU(2) perturbation
B. Homogeneous SU(2) connection on S3 ~= SU(2)
C. Boundary/spectral-flow picture of 4D BPST instanton
D. Full 4D instanton Dirac problem
```

[INFERRED] Current recommendation:

```text
P1c_NEXT = Option B formula specification
```

Meaning: before code, define the `S3` coframe, gamma/Pauli conventions, gauge representation, candidate homogeneous connection, spectral/Wigner matrix-element selection rules, inner product, and Hermiticity checks.

[INFERRED] Option A is allowed only as a toy Hermitian matrix-infrastructure test if clearly labelled synthetic.

[INFERRED] Options C and D require separate 4D/boundary formulations and are not current implementation tasks.

[CODE] No gauge-background operator code has been written. No instanton, index, chirality, spectral-flow, eta-invariant, or zero-mode claims are allowed from the current code.

## P1c Hermiticity Unit-Test Skeleton

[CODE] Hermiticity unit-test skeleton created on 2026-06-07:

```text
tests/test_hermiticity_condition_skeleton.py
```

[CODE] The file defines `generate_hermitian_test_matrix(k_max)` as a zero-matrix placeholder with dimension:

```text
total_number_of_modes(k_max)
```

[FAIL] Current targeted check intentionally fails:

```text
python -m pytest -q .\tests\test_hermiticity_condition_skeleton.py
1 failed, 1 passed
```

Failure message:

```text
Stub matrix is zero: implement real V
```

[INFERRED] This is the correct red gate for Option B: Hermiticity alone is not enough; the future coupling matrix must also contain real nonzero analytic/symbolic coefficients.

[CODE] Next step:

```text
implement minimal symbolic coefficients for k_max=1
```

[INFERRED] Do not proceed to spectrum, instanton, index, chirality, spectral-flow, eta-invariant, or zero-mode claims while this skeleton test remains red.

## P1c Minimal Symbolic V Scaffold

[CODE] Minimal symbolic Option B coupling scaffold implemented on 2026-06-07:

```text
s3_coupling_v_option_b.py
tests/test_hermiticity_condition_skeleton.py
```

[CODE] `build_v_symbolic(k_max=1, lambda_val=1.0, radius=1.0)` builds a dense `numpy` matrix using:

```text
P1a spectral spinor records
working left-invariant representation (J_L, J_R) = (1, 0)
Clebsch-Gordan selection rules
unit reduced matrix elements
Hermitian symmetrisation
T_i = tau_i / 2 represented as a global scaffold factor
```

[CODE] Current scaffold dimension is:

```text
total_number_of_modes(1) = 16
```

not `20`. A full internal gauge-doublet expansion would require a separate basis contract and would double this clean spectral dimension.

[VERIFIED-SYNTHETIC] Local targeted check:

```text
python -m pytest -q .\tests\test_hermiticity_condition_skeleton.py
5 passed
```

[VERIFIED-SYNTHETIC] The targeted tests verify:

```text
V is nonzero
V is Hermitian
V shape matches total_number_of_modes(1)
nonzero entries satisfy working (J_L,J_R)=(1,0) selection rules
```

[INFERRED] This closes the previous red gate:

```text
Stub matrix is zero: implement real V
```

[UNCERTAIN] This is still a symbolic coefficient scaffold, not a physically normalised homogeneous `SU(2)` gauge-background operator. Exact reduced matrix elements, Ben Achour one-form normalisation, and full internal gauge-index expansion remain unresolved.

[NEXT] Extend to `k_max=2,3` only after adding an explicit basis contract for magnetic labels and, if needed, gauge-doublet indices. Then verify Hermiticity and cutoff stability before any spectrum interpretation.

## P1c Working Reduced Matrix Elements

[CODE] Working analytic reduced matrix-element helper added on 2026-06-07:

```text
s3_reduced_matrix_elements.py
```

[CODE] `compute_reduced_V_element(...)` now supplies the `k_max=1` scaffold with real SU(2) triple-harmonic normalization factors for the working left-invariant case:

```text
(J_L, J_R) = (1, 0)
```

[CODE] `s3_coupling_v_option_b.py` now uses these reduced elements instead of unit reduced matrix elements.

[VERIFIED-SYNTHETIC] Local targeted check:

```text
python -m pytest -q .\tests\test_hermiticity_condition_skeleton.py
7 passed
```

[VERIFIED-SYNTHETIC] V remains nonzero and Hermitian with the working reduced coefficients, and all `k_max=1` reduced coefficients returned by `reduced_elements_for_kmax1()` are real finite floats.

[UNCERTAIN] These are not final exact Ben Achour `E/E'` one-form reduced matrix elements. The current metadata explicitly marks:

```text
Ben_Achour_E_Eprime_one_form_normalization_unresolved
```

[NEXT] Before extending to `k_max=2,3` or interpreting spectra, derive or externally verify the final Ben Achour one-form normalization and the full gauge-doublet basis contract.

## P1c Ben Achour One-Form Normalization Audit

[CODE] P1c-NORM report added on 2026-06-07:

```text
reports/S3_BEN_ACHOUR_ONE_FORM_NORMALIZATION_P1C.md
```

[UNCERTAIN] The Ben Achour `E/E'` basis mapping is still unresolved as a separate representation detail. A single `E` or `E'` family does not provide an unambiguous one-coefficient mapping for the homogeneous left-invariant coframe under the naive candidate identification, because the boundary spin-1 components hit the zero-norm exclusions in the Ben Achour norm formula.

[CODE] Current `V` scale remains:

```text
ANALYTIC_DIRECT_HAAR_CONVENTION
Ben_Achour_E_Eprime_one_form_normalization_unresolved
```

[INFERRED] Do not treat the exact unit coframe scale as evidence that the Ben Achour `E/E'` basis mapping is derived.

[INFERRED] Do not build or interpret `D = D0 + V` spectra as physical claims while the Ben Achour basis mapping remains unresolved.

## P1d Direct Haar Coupled Operator Smoke

[CODE] Exact direct Haar/unit-coframe convention accepted on 2026-06-07:

```text
ANALYTIC_DIRECT_HAAR_CONVENTION
||e^i|| scale = 1
final_ben_achour_normalization = unresolved
```

[CODE] Files added/updated:

```text
s3_dirac_with_temp_coupling.py
tests/test_s3_dirac_temp_coupling.py
reports/S3_DIRAC_TEMP_COUPLING_SMOKE_P1D.md
s3_reduced_matrix_elements.py
tests/test_hermiticity_condition_skeleton.py
```

[CODE] `build_temp_coupled_dirac(k_max<=3, lambda_val=1.0, radius=1.0, alpha=None)` returns:

```text
D
D0
V
metadata
```

[VERIFIED-SYNTHETIC] Targeted temporary-coupling checks:

```text
python -m pytest -q .\tests\test_s3_dirac_temp_coupling.py .\tests\test_hermiticity_condition_skeleton.py
13 passed
```

[VERIFIED-SYNTHETIC] Verified only:

```text
lambda=0 returns D0
D is Hermitian
V is nonzero for lambda=1
matrix size matches total_number_of_modes(k_max) for the supported smoke range
metadata marks ANALYTIC_DIRECT_HAAR_CONVENTION
```

[UNCERTAIN] This remains an engineering smoke layer, not a physical gauge-background result.

[CODE] Supported smoke range:

```text
0 <= k_max <= 3
```

[INFERRED] Spectrum visualization is allowed only as a preliminary/debug artifact after explicit request and must be labelled exact direct Haar-unit coframe scale with separate Ben Achour `E/E'` basis mapping unresolved.

## P1 Spectrum Visualization

[CODE] Preliminary spectrum visualization layer added on 2026-06-07:

```text
s3_dirac_spectrum_viz.py
tests/test_s3_dirac_spectrum_viz.py
reports/S3_DIRAC_SPECTRUM_VISUALIZATION_P1.md
reports/s3_dirac_spectrum_viz_prelim.png
```

[VERIFIED-SYNTHETIC] Targeted visualization check:

```text
python -m pytest -q .\tests\test_s3_dirac_spectrum_viz.py
3 passed
```

[VERIFIED-SYNTHETIC] The preliminary plot is non-blank and shows smooth symmetric spectral shifts for `D(lambda) = D0 + lambda V` on the smoke layer.

[INFERRED] This remains a debug artifact only. Use only the labels:

```text
preliminary
exact direct Haar-unit coframe scale
separate Ben Achour E/E' basis mapping unresolved
no physical claims
```

## P1d Spectrum Sweep Analysis

[CODE] Quantitative exact-scale sweep analysis added on 2026-06-07:

```text
reports/S3_DIRAC_SPECTRUM_SWEEP_ANALYSIS_P1D.md
```

[VERIFIED-SYNTHETIC] Summary metrics for `k_max=3`, `lambda in [0,1]`:

```text
max_abs_shift  = 0.06112145532459046
mean_abs_shift = 0.031405583903139744
l2_shift       = 0.3520593881833174
min_abs_final  = 1.5206906325745546
max_symmetry_violation = 0.0
```

[INFERRED] The exact-scale P1d sweep is numerically stable and preserves the symmetric branch structure.

[UNCERTAIN] This is a smoke-layer spectrum study only; no physical gauge-background claim is attached.

## P1-NORM Numerical Coframe Norm Diagnostic

[CODE] Safe numerical norm diagnostic added on 2026-06-07:

```text
s3_oneform_laplacian_numerical.py
tests/test_s3_oneform_laplacian_numerical.py
reports/S3_ONEFORM_NORM_NUMERICAL_P1.md
```

[CODE] Despite the filename, this is not a kNN connection-Laplacian implementation. It uses Muller sampling on unit `S3` and checks the ambient-metric Gram matrix of the left-invariant frame generated by quaternion left multiplication.

[VERIFIED-SYNTHETIC] Targeted check:

```text
python -m pytest -q .\tests\test_s3_oneform_laplacian_numerical.py
3 passed
```

[VERIFIED-SYNTHETIC] Deterministic diagnostic values:

```text
n_points = 200:  raw_component_norm_mean = 1.0, scale_to_direct_haar_norm = 1.0
n_points = 2000: raw_component_norm_mean = 1.0, scale_to_direct_haar_norm = 1.0
diagnostic Gram spectrum = [1, 1, 1]
```

[UNCERTAIN] This does not close the Ben Achour `E/E'` basis mapping. It only supports the exact direct Haar unit scale as a coframe-norm convention.

[CODE] For downstream engineering work, the direct Haar unit scale `1` is the working convention. The Ben Achour `E/E'` basis mapping remains a separate unresolved representation detail. This is a continuation contract, not a physical claim.

[INFERRED] Do not use this diagnostic as evidence for graph one-form Laplacian convergence or physical gauge-background spectra.

## P1_TOY_TEST_ENGINEERING_ALPHA Smoke Test

[CODE] Pre-registered engineering smoke test added on 2026-06-07:

```text
tests/test_s3_dirac_toy_test_alpha.py
reports/S3_DIRAC_TOY_TEST_ALPHA_P1.md
```

[CODE] The smoke test covers:

```text
D is Hermitian
V is nonzero
alpha=0 returns D0
spectrum avoids |lambda| < 1.0
spectrum is symmetric about zero
metadata includes ENGINEERING_ALPHA and a direct-Haar normalization warning
```

[VERIFIED-SYNTHETIC] Targeted check:

```text
python -m pytest -q .\tests\test_s3_dirac_toy_test_alpha.py .\tests\test_s3_dirac_temp_coupling.py
12 passed
```

[UNCERTAIN] This is an engineering smoke result only. It does not establish any physical gauge-background, instanton, or index claim.

## Guardrails

Do not:

- send Tom a second long report without his answer or explicit approval;
- claim Tom made an error;
- claim `sqrt(sin(2 alpha))` is definitely the source of his problem;
- promote Phase 2 to a theory verdict;
- touch Gate4B/Gate4C/negative-controls work for this task;
- start S3 x S6, Wigner/Haar, instanton, index, zero-mode, or heavy diagonalisation work as a response to this blocker;
- mix with IDM/MULTING / Buckholtz.

Do:

- phrase findings as convention clarification;
- keep evidence markers;
- separate `[CODE]`, `[VERIFIED]`, `[USER-PROVIDED]`, `[INFERRED]`, `[HYPOTHESIS]`;
- prefer small reproducible Python checks;
- keep Tom's construction central;
- treat Camporesi-Higuchi and Ben Achour as reference baselines, not as proof that Tom's approach is wrong.

## P1 Methods Note

[CODE] Added a short methods-style summary for the exact direct Haar-unit sweep:

```text
reports/S3_DIRAC_METHODS_NOTE_P1.md
```

[CODE] Added a methods-paper draft artifact:

```text
reports/S3_DIRAC_METHODS_PAPER_DRAFT.md
```

[CODE] Added a paper outline artifact:

```text
reports/S3_DIRAC_METHODS_PAPER_OUTLINE.md
```

[VERIFIED-SYNTHETIC] The note records the exact-scale sweep metrics already established by the green smoke tests:

```text
max_abs_shift  = 0.06112145532459046
mean_abs_shift = 0.031405583903139744
l2_shift       = 0.3520593881833174
max_symmetry_violation = 0.0
min_abs_final  = 1.5206906325745546
```

[INFERRED] This is a methods artifact only. It is not a physical gauge-background claim and does not close the Ben Achour `E/E'` basis mapping.

## P1 Post-Normalization Audit

[CODE] Added the post-normalization migration audit:

```text
reports/P1_POST_NORMALIZATION_MIGRATION_AUDIT.md
```

[VERIFIED-SYNTHETIC] Current audit verdict:

```text
canonical runtime normalization = exact direct Haar / unit-coframe scale, ||e^i|| = 1
normalization migration closed at L2 for the current runtime smoke stack
sign gap remains separate from normalization migration
Lawrence coordinate mapping remains unknown
```

[INFERRED] Next hard gate:

```text
P2_SIGN_CONVENTION_AND_SELECTION_RULE_AUDIT
```

## P2 Sign / Selection-Rule Audit

[CODE] Added the P2 convention and selection-rule audit:

```text
reports/P2_SIGN_CONVENTION_AND_SELECTION_RULE_AUDIT.md
```

[VERIFIED-SYNTHETIC] Current P2 audit verdict:

```text
displayed Ben Achour phase -> xi' = +2 i m_-
resolved_as_typo = local code convention only
Wigner standard mapping matches the displayed phase
normalization scale does not alter the current runtime sign/selection-rule path
Lawrence mapping remains unknown
final runtime verdict = blocked_by_mapping
```

## P3 Lawrence Coordinate / Sign Translation Table

[CODE] Added the P3 mapping audit:

```text
reports/P3_LAWRENCE_COORDINATE_SIGN_TRANSLATION_TABLE.md
```

[VERIFIED-SYNTHETIC] Current P3 verdict:

```text
Lawrence coordinate/sign mapping is unknown
Ben Achour displayed phase locally implies xi'Y = +2 i m_- Y
Lawrence-specific runtime interpretation remains blocked_by_mapping
next gate = P4_SOURCE_ACQUISITION_FOR_LAWRENCE_MAPPING
```

## P4 Source Acquisition for Lawrence Mapping

[UNKNOWN] Exact Lawrence coordinate/sign mapping is still not established from
the recovered local/public sources.

[FACT] The inspected Lawrence essay and related preprints discuss unitary groups,
spinors, and curved complex spaces, but do not provide an explicit verified S3
embedding table of the form `x_i(alpha, theta, theta_tilde)`.

[INFERRED] Lawrence-specific runtime claims remain blocked_by_mapping until an
explicit coordinate/sign translation table is available.

Current final verdict:
blocked_by_mapping

## P4B Recovered Lawrence Frames

[USER-PROVIDED] New recovered frame text provides explicit S3 embedding and
Cartan-generator formulas for Lawrence Part 3:

```text
x1 = rho sin(alpha) cos(theta)
x2 = rho sin(alpha) sin(theta)
x3 = rho cos(alpha) sin(theta_tilde)
x4 = rho cos(alpha) cos(theta_tilde)

i I_3L = 1/2 (partial_theta + partial_theta_tilde)
i I_3R = 1/2 (partial_theta - partial_theta_tilde)

chi(theta, theta_tilde)
  = exp(i[(i_L + i_R) theta + (i_L - i_R) theta_tilde])
```

[INFERRED] This is sufficient for the Lawrence Cartan mapping only:

```text
phi_BA <-> theta_L
theta_BA <-> theta_tilde_L
m_+ <-> i_L
m_- <-> i_R
```

[INFERRED] Updated status:

```text
source_sufficient_for_cartan_mapping
runtime verdict = research_only
```

[INFERRED] This does not yet close Lawrence-specific runtime safety. Remaining
blockers:

- non-Cartan generators;
- alpha-dependence;
- cot(2 alpha);
- V-selection rules;
- full Dirac / spinor interpretation.

[INFERRED] Next gate for the S3 block:

```text
P5_LAWRENCE_NONCARTAN_AND_SELECTION_RULE_VALIDATION
```

## P6 S6 / SU(4) Track

[USER-PROVIDED] A separate recovered-frame package opens a distinct track for:

- `S3 x S6` embedding;
- `SO(7)/SO(6)` local translation-like action;
- `SO(6) -> SU(4)` generator closure;
- hypercharge `Y_W`;
- right-handed neutrino background.

[INFERRED] This is not yet runtime-safe and should not be mixed with the S3
Cartan-sign audit. The next gate for that separate track is:

```text
P6_S6_SU4_GAUGE_BREAKING_AUDIT
```

## P5 Lawrence Non-Cartan / Selection-Rule Validation

[USER-PROVIDED] The S3 Cartan layer is now at research-only status, but the
Lawrence fundamental spinor ansatz is still not validated under the non-Cartan
generators.

[INFERRED] P5 must test:

- `I_{1L}`, `I_{2L}`, `I_{1R}`, `I_{2R}`;
- full `SU(2)_L x SU(2)_R` commutators;
- action on the four fundamental spinor states;
- `cot(2 alpha)` dependence;
- implications for `V` selection rules.

[INFERRED] P5 runtime verdict target:

```text
research_only
```

[INFERRED] Hard blockers still include:

- unresolved `cot(2 alpha)` behavior;
- non-Cartan closure;
- spinor-harmonic ansatz validity;
- selection-rule derivation for `V`.

[INFERRED] Next gate:

```text
P5B_CORRECT_SPINOR_HARMONIC_ANSATZ_SEARCH
```

## P5B Correct Spinor Harmonic Ansatz Search

[USER-PROVIDED] The next step is to determine whether the recovered Lawrence
fundamental spinor ansatz is actually a valid spinor harmonic on `S3`, or
whether it must be replaced by a standard spinorial basis / Kosmann derivative
construction.

[INFERRED] Current P5B finding:

```text
spinorial Lie derivative required
```

[INFERRED] The recovered scalar-dragging ansatz is incomplete under the
non-Cartan generator action: the `cot(2 alpha)` constraint fixes a radial
profile but leaves an `alpha`-dependent ladder coefficient, so the full
`SU(2)_L x SU(2)_R` closure is not yet achieved.

[INFERRED] P5B must test:

- reproduction of the `cot(2 alpha)` failure;
- ODE system for `A(alpha)`;
- ordinary scalar dragging vs spinorial Lie derivative;
- compatibility with standard `S3` spinor harmonics;
- impact on `V` selection rules.

[INFERRED] P5B runtime verdict target:

```text
research_only
```

[INFERRED] Possible next gates after P5B:

- `P5C_KOSMANN_LIE_DERIVATIVE_TEST`
- `P5C_STANDARD_S3_SPINOR_HARMONICS_IMPLEMENTATION`
- `P5C_CORRECTED_SPINOR_ANSATZ_VALIDATION`

[VERIFIED] Targeted regression check for the recovered scalar-dragging failure
passed locally:

```text
python -m pytest -q tests/test_lawrence_i1r_failure_reproduction.py
2 passed
```

[VERIFIED] This preserves the current P5B conclusion:

```text
spinorial Lie derivative required
research_only
V-selection rules = smoke_only
```

## P5C Kosmann Lie Derivative Test

[INFERRED] The Kosmann/spinorial-Lie-derivative path does not rescue the current
Lawrence scalar-dragging ansatz into a closed full `SU(2)_L x SU(2)_R`
representation.

[INFERRED] Current P5C verdict:

```text
standard_spinor_harmonics_required
```

[INFERRED] Reason:

- the recovered scalar ansatz still does not provide a validated full non-Cartan
  spinor representation;
- standard `S3` spinor harmonics / Killing spinors are the natural replacement
  basis;
- `V` selection rules must remain `smoke_only` until that basis is implemented.

[INFERRED] Next gate:

```text
P5C_STANDARD_S3_SPINOR_HARMONICS_IMPLEMENTATION
```

[VERIFIED] Targeted P5C regression checks passed locally:

```text
python -m pytest -q tests/test_lawrence_i1r_failure_reproduction.py tests/test_s3_spin_connection_lawrence_frame.py
4 passed
```

[VERIFIED] This preserves the current P5C conclusion:

```text
standard_spinor_harmonics_required
research_only
V-selection rules = smoke_only
```

## P5C Standard S3 Spinor Harmonics Implementation

[CODE] Added a standard lowest `S3` spinor-frame basis in Lawrence/Hopf
coordinates:

```text
standard_s3_spinor_harmonics.py
tests/test_standard_s3_spinor_harmonics.py
```

[CODE] The implemented basis is the pointwise unitary `2 x 2` frame

```text
U(alpha, theta, theta_tilde)
```

with entries

```text
cos(alpha) * exp(+i(theta + theta_tilde)/2)
sin(alpha) * exp(+i(theta - theta_tilde)/2)
-sin(alpha) * exp(-i(theta - theta_tilde)/2)
cos(alpha) * exp(-i(theta + theta_tilde)/2)
```

[VERIFIED] Targeted local tests passed:

```text
python -m pytest -q tests/test_standard_s3_spinor_harmonics.py \
  tests/test_lawrence_i1r_failure_reproduction.py \
  tests/test_s3_spin_connection_lawrence_frame.py
8 passed
```

[INFERRED] This is the standard `S3` replacement basis layer, not a rescue of
the recovered Lawrence scalar ansatz.

[INFERRED] Current project status remains:

```text
P5C verdict = standard_spinor_harmonics_required
runtime = research_only
V-selection rules = smoke_only
```

## P5D Standard Spinor Harmonics Representation Tests

[CODE] Added representation-level tests for the standard `S3` spinor frame:

```text
tests/test_standard_s3_spinor_harmonics.py
```

[CODE] The test layer checks:

- Cartan weights for the four entries;
- `su(2)_L` and `su(2)_R` closure on lifted generators;
- pointwise unitarity and orthonormality;
- regularity at `alpha = 0` and `alpha = pi/2`;
- Haar-weighted norms;
- comparison against the existing `Wigner-D` oracle.

[VERIFIED] Targeted local test bundle passed:

```text
python -m pytest -q tests/test_standard_s3_spinor_harmonics.py \
  tests/test_lawrence_i1r_failure_reproduction.py \
  tests/test_s3_spin_connection_lawrence_frame.py
11 passed
```

[INFERRED] This validates the standard `S3` basis layer as a local
representation test layer. It does not promote the project to runtime-safe and
does not by itself change `V`-selection policy.

[INFERRED] Current status remains:

```text
runtime = research_only
V-selection rules = smoke_only
```

## P5D Non-Cartan Formulas Required

[INFERRED] The standard `S3` basis layer is now in place, but the exact
coordinate-space formulas for the non-Cartan generators
`I_{1L}, I_{2L}, I_{1R}, I_{2R}` are still required to complete a full
representation-layer audit in Lawrence coordinates.

[INFERRED] Current blocker:

```text
FORMULAS_REQUIRED
```

## P5E Explicit Non-Cartan Coordinate Generators

[CODE] Added the explicit coordinate-space non-Cartan generator layer for the
Lawrence/Hopf chart:

```text
s3_lawrence_noncartan_generators.py
tests/test_p5e_noncartan_coordinate_generators.py
reports/P5E_EXPLICIT_NONCARTAN_COORDINATE_GENERATORS.md
```

[CODE] The layer records the raw Euler-angle chart used by the repository
Wigner-D oracle:

```text
a = -theta
b = 2 * alpha
c = -theta_tilde
```

[CODE] It exposes the alias map:

```text
I1L -> L1
I2L -> L2
I3L -> L3
I1R -> R1
I2R -> R2
I3R -> R3
```

[VERIFIED-SYNTHETIC] The targeted smoke bundle passed locally:

```text
python -m pytest -q tests/test_p5e_noncartan_coordinate_generators.py \
  tests/test_standard_s3_spinor_harmonics.py \
  tests/test_lawrence_i1r_failure_reproduction.py \
  tests/test_s3_spin_connection_lawrence_frame.py
13 passed
```

[INFERRED] Current P5E status:

```text
explicit non-Cartan coordinate generators implemented / smoke-verified
runtime = research_only
V-selection rules = smoke_only
```

[INFERRED] Remaining caveat:

- exact commutator normalization is still convention-sensitive;
- do not promote to runtime-safe;
- do not raise `V-selection rules` above `smoke_only`.

[INFERRED] Next gate:

```text
P5F_NONCARTAN_COMMUTATOR_CONVENTION_AUDIT
```

## P5F Non-Cartan Commutator Convention Audit

[CODE] The explicit coordinate-space non-Cartan generator layer has now been
audited against the lifted standard `su(2)` oracle using the Hermitian
convention:

```text
I = -i X
```

[VERIFIED-SYNTHETIC] Targeted smoke bundle after the convention fix:

```text
python -m pytest -q tests/test_p5e_noncartan_coordinate_generators.py \
  tests/test_standard_s3_spinor_harmonics.py \
  tests/test_lawrence_i1r_failure_reproduction.py \
  tests/test_s3_spin_connection_lawrence_frame.py
15 passed
```

[INFERRED] Audit result:

```text
P5F_NONCARTAN_COMMUTATOR_CONVENTION_AUDIT = passed
```

[INFERRED] What is now fixed:

- `L1/L2/L3` match the lifted standard left `su(2)` generator oracle;
- `R1/R2/R3` match the lifted standard right `su(2)` generator oracle;
- `[IaL, IbR] = 0` in the tested layer;
- the coordinate-space non-Cartan convention is no longer ambiguous in the
  current smoke-verified basis layer.

[INFERRED] Remaining boundary:

```text
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

[INFERRED] Next gate:

```text
P5G_V_SELECTION_RULE_REVIEW
```

## P5G V-Selection Rule Review

[CODE] Added the V-selection review layer and a tight regression check:

```text
reports/P5G_V_SELECTION_RULE_REVIEW.md
tests/test_p5g_v_selection_rule_review.py
```

[VERIFIED-SYNTHETIC] Targeted review bundle passed locally:

```text
python -m pytest -q tests/test_p5g_v_selection_rule_review.py \
  tests/test_p5e_noncartan_coordinate_generators.py \
  tests/test_standard_s3_spinor_harmonics.py \
  tests/test_lawrence_i1r_failure_reproduction.py \
  tests/test_s3_spin_connection_lawrence_frame.py
17 passed
```

[INFERRED] Review result:

```text
V-selection rules remain smoke_only
runtime remains research_only
safe_for_runtime remains no
```

[INFERRED] Why:

- the current `V` scaffold is a Hermitian engineering layer, not a final
  physical operator;
- its nonzero structure is still tied to the working `(J_L,J_R)=(1,0)` reduced
  matrix-element scaffold;
- no separate Lawrence-compatible physical selection-rule table has been
  promoted.

[INFERRED] Next gate:

```text
P5G complete; next work should only expand V if a new validated basis contract
or a new physical selection-rule derivation is supplied.
```

## P5H Technical Task Addendum

[INFERRED] Useful external information has been folded into the roadmap as a
conservative addendum:

- Kosmann lift remains a reference, not a rescue proof;
- `S6` should be treated as a separate first-class track beginning with a
  `G2/SU(3)` formula spec and a Casimir baseline;
- the homogeneous-space Dirac relation `D = C_G + (1/8) s` is a useful
  cross-check for later `S6` work;
- `V-selection rules` remain `smoke_only`;
- `runtime` remains `research_only`.

[INFERRED] Suggested next technical gates:

```text
P5H_S3_CAS_ORACLE_REVIEW
P6_S6_G2_SU3_FORMULA_SPEC
```

## P6 S6 / G2 / SU(3) Formula Spec

[CODE] Added the separate first-class `S6` track specification:

```text
reports/P6_S6_G2_SU3_FORMULA_SPEC.md
```

[INFERRED] The `S6` track is now formally separated from the validated `S3`
basis work and begins from the homogeneous-space identity:

```text
S6 ≅ G2 / SU(3)
```

[INFERRED] The spec locks the next questions to:

- reductive decomposition `g2 = su(3) ⊕ m`;
- metric normalization;
- spinor-bundle convention;
- Dirac operator under the chosen connection;
- Casimir cross-check.

[INFERRED] This is a formula spec only, not an implementation or spectrum claim.

[INFERRED] Current boundary:

```text
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

[INFERRED] Next gate:

```text
P6_S6_G2_SU3_IMPLEMENTATION
```

## P6 S6 / G2 / SU(3) Implementation

[CODE] Added the first executable S6 contract layer:

```text
s6_g2_su3_formula_spec.py
tests/test_p6_s6_g2_su3_formula_spec.py
reports/P6_S6_G2_SU3_IMPLEMENTATION.md
```

[VERIFIED-SYNTHETIC] Targeted S6 smoke bundle passed locally:

```text
python -m pytest -q tests/test_p6_s6_g2_su3_formula_spec.py
2 passed
```

[INFERRED] The S6 track is now started as a formula-spec implementation with
the following fixed contract:

```text
S6 ≅ G2 / SU(3)
g2 = su(3) ⊕ m
D ~ C_G + (1/8) s
```

[INFERRED] The implementation layer now fixes the geometric convention:

```text
metric normalization = unit round S6 normalization
connection choice = Levi-Civita connection on the canonical homogeneous metric
spinor-bundle convention = canonical spin structure induced by the G2/SU(3) reductive frame
Dirac convention = homogeneous Dirac operator with Casimir cross-check target
```

[INFERRED] The following remain deferred by design:

- selection rules;
- spectrum computation;
- SU(4) / hypercharge interpretation.

[INFERRED] Current boundary:

```text
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

[INFERRED] Next gate:

```text
P6_S6_G2_SU3_FORMULA_SPEC = drafted
P6_S6_G2_SU3_IMPLEMENTATION = geometry convention fixed / started
P6B_S6_METRIC_CONNECTION_SPINOR_CONVENTION = passed
P6C_S6_DIRAC_CASIMIR_BASELINE = passed
P6D_S6_SPECTRUM_BASELINE = passed
P6E_S6_SPECTRUM_IMPLEMENTATION = passed
```

## P6C S6 Dirac / Casimir Baseline

[CODE] The S6 baseline layer now fixes the operator fence:

```text
S6 ≅ G2 / SU(3)
g2 = su(3) ⊕ m
metric normalization = unit round S6 normalization
connection choice = Levi-Civita connection on the canonical homogeneous metric
spinor-bundle convention = canonical spin structure induced by the G2/SU(3) reductive frame
dirac operator = homogeneous Dirac operator with Casimir cross-check target
Casimir cross-check = D ~ C_G + (1/8) s
```

[INFERRED] The following remain deferred:

- selection rules;
- spectrum computation;
- SU(4) / hypercharge interpretation.

[VERIFIED-SYNTHETIC] The targeted baseline smoke test is the next check:

```text
python -m pytest -q tests/test_p6c_s6_dirac_casimir_baseline.py
```

[VERIFIED-SYNTHETIC] The baseline smoke bundle passed locally:

```text
python -m pytest -q tests/test_p6_s6_g2_su3_formula_spec.py tests/test_p6_s6_g2_su3_implementation.py tests/test_p6c_s6_dirac_casimir_baseline.py
6 passed
```

## P6D S6 Spectrum Baseline

[CODE] The spectrum baseline contract now fences the next S6 layer:

```text
spectrum target = homogeneous Dirac spectrum on S6, to be derived later
```

[CODE] The baseline deliberately defers:

- selection rules;
- spectrum computation;
- SU(4) / hypercharge interpretation.

[VERIFIED-SYNTHETIC] The spectrum baseline smoke test is the next check:

```text
python -m pytest -q tests/test_p6d_s6_spectrum_baseline.py
```

[VERIFIED-SYNTHETIC] The spectrum baseline smoke bundle passed locally:

```text
python -m pytest -q tests/test_p6_s6_g2_su3_formula_spec.py tests/test_p6_s6_g2_su3_implementation.py tests/test_p6c_s6_dirac_casimir_baseline.py tests/test_p6d_s6_spectrum_baseline.py
8 passed
```

## P6E S6 Spectrum Implementation

[CODE] The spectrum implementation layer now fences the next S6 step:

```text
spectrum target = homogeneous Dirac spectrum on S6, to be derived later
```

[CODE] The implementation layer deliberately defers:

- selection rules;
- spectrum computation;
- SU(4) / hypercharge interpretation.

[VERIFIED-SYNTHETIC] The spectrum implementation smoke test is the next check:

```text
python -m pytest -q tests/test_p6e_s6_spectrum_implementation.py
```

[VERIFIED-SYNTHETIC] The spectrum implementation smoke bundle passed locally:

```text
python -m pytest -q tests/test_p6_s6_g2_su3_formula_spec.py tests/test_p6_s6_g2_su3_implementation.py tests/test_p6c_s6_dirac_casimir_baseline.py tests/test_p6d_s6_spectrum_baseline.py tests/test_p6e_s6_spectrum_implementation.py
10 passed
```

[INFERRED] Next gate:

```text
P6F_S6_SPECTRUM_OPERATOR_REVIEW
```

## P6F S6 Spectrum Operator Review

[CODE] The spectrum operator review layer now fences the next S6 step:

```text
review result = contract_fence_preserved
```

[CODE] The review layer deliberately defers:

- selection rules;
- spectrum computation;
- SU(4) / hypercharge interpretation.

[VERIFIED-SYNTHETIC] The spectrum operator review smoke test is the next check:

```text
python -m pytest -q tests/test_p6f_s6_spectrum_operator_review.py
```

[VERIFIED-SYNTHETIC] The spectrum operator review smoke bundle passed locally:

```text
python -m pytest -q tests/test_p6_s6_g2_su3_formula_spec.py tests/test_p6_s6_g2_su3_implementation.py tests/test_p6c_s6_dirac_casimir_baseline.py tests/test_p6d_s6_spectrum_baseline.py tests/test_p6e_s6_spectrum_implementation.py tests/test_p6f_s6_spectrum_operator_review.py
12 passed
```

[INFERRED] Next gate:

```text
P6G_S6_SPECTRUM_OPERATOR_STABILIZATION
```

## P6G S6 Spectrum Operator Stabilization

[CODE] The spectrum operator stabilization layer now fences the next S6 step:

```text
stabilization result = contract_fence_preserved
```

[CODE] The stabilization layer deliberately defers:

- selection rules;
- spectrum computation;
- SU(4) / hypercharge interpretation.

[VERIFIED-SYNTHETIC] The spectrum operator stabilization smoke test is the next check:

```text
python -m pytest -q tests/test_p6g_s6_spectrum_operator_stabilization.py
```

[VERIFIED-SYNTHETIC] The spectrum operator stabilization smoke bundle passed locally:

```text
python -m pytest -q tests/test_p6g_s6_spectrum_operator_stabilization.py
2 passed
```

[INFERRED] Next gate:

```text
P6H_S6_SPECTRUM_OPERATOR_LOCKDOWN
```

## P6H S6 Spectrum Operator Lockdown

[CODE] The spectrum operator lockdown layer now fences the next S6 step:

```text
lockdown result = contract_fence_preserved
```

[CODE] The lockdown layer deliberately defers:

- selection rules;
- spectrum computation;
- SU(4) / hypercharge interpretation.

[VERIFIED-SYNTHETIC] The spectrum operator lockdown smoke test is the next check:

```text
python -m pytest -q tests/test_p6h_s6_spectrum_operator_lockdown.py
```

[VERIFIED-SYNTHETIC] The spectrum operator lockdown smoke bundle passed locally:

```text
python -m pytest -q tests/test_p6h_s6_spectrum_operator_lockdown.py
2 passed
```

[INFERRED] Next gate:

```text
P6I_S6_SPECTRUM_OPERATOR_FREEZE
```

[INFERRED] Do not promote the status of the `S3` representation layer until the
non-Cartan differential action is explicitly verified in coordinate space.

## P6I S6 Spectrum Operator Freeze

[CODE] The spectrum operator freeze layer now fences the next S6 step:

```text
freeze result = contract_fence_preserved
```

[CODE] The freeze layer deliberately defers:

- selection rules;
- spectrum computation;
- SU(4) / hypercharge interpretation.

[VERIFIED-SYNTHETIC] The spectrum operator freeze smoke test is the next check:

```text
python -m pytest -q tests/test_p6i_s6_spectrum_operator_freeze.py
```

[VERIFIED-SYNTHETIC] The spectrum operator freeze smoke bundle passed locally:

```text
python -m pytest -q tests/test_p6_s6_g2_su3_formula_spec.py tests/test_p6_s6_g2_su3_implementation.py tests/test_p6c_s6_dirac_casimir_baseline.py tests/test_p6d_s6_spectrum_baseline.py tests/test_p6e_s6_spectrum_implementation.py tests/test_p6f_s6_spectrum_operator_review.py tests/test_p6g_s6_spectrum_operator_stabilization.py tests/test_p6h_s6_spectrum_operator_lockdown.py tests/test_p6i_s6_spectrum_operator_freeze.py
18 passed
```

[INFERRED] Next gate:

```text
P6J_S6_SPECTRUM_OPERATOR_FINAL_REVIEW
```

## P6J S6 Spectrum Operator Final Review

[CODE] The terminal review layer now closes the S6 operator chain:

```text
P6J_S6_SPECTRUM_OPERATOR_FINAL_REVIEW = passed
final review result = contract_fence_final_review_complete
```

[CODE] The final review layer deliberately defers:

- selection rules;
- spectrum computation;
- SU(4) / hypercharge interpretation;
- runtime safe promotion.

[VERIFIED-SYNTHETIC] The final review smoke test is the next check:

```text
python -m pytest -q tests/test_p6j_s6_spectrum_operator_final_review.py
```

[VERIFIED-SYNTHETIC] The final review smoke bundle passed locally:

```text
python -m pytest -q tests/test_p6_s6_g2_su3_formula_spec.py tests/test_p6_s6_g2_su3_implementation.py tests/test_p6c_s6_dirac_casimir_baseline.py tests/test_p6d_s6_spectrum_baseline.py tests/test_p6e_s6_spectrum_implementation.py tests/test_p6f_s6_spectrum_operator_review.py tests/test_p6g_s6_spectrum_operator_stabilization.py tests/test_p6h_s6_spectrum_operator_lockdown.py tests/test_p6i_s6_spectrum_operator_freeze.py tests/test_p6j_s6_spectrum_operator_final_review.py
20 passed
```

[INFERRED] Next gate:

```text
P6K_S6_SPECTRUM_COMPUTATION
```

## P6K S6 Spectrum Computation

[CODE] The S6 track now has an explicit analytic spectrum computation layer:

```text
lambda_{k,+/-} = +/- (k + 3) / R
mu_k = 8 * binomial(k + 5, k)
```

[CODE] The computation layer keeps the frozen S6 convention fixed and
deliberately defers:

- selection rules;
- SU(4) / hypercharge interpretation;
- instanton / index / chirality;
- runtime safe promotion.

[VERIFIED-SYNTHETIC] The new computation smoke test is the next check:

```text
python -m pytest -q tests/test_p6k_s6_spectrum_computation.py
```

[VERIFIED-SYNTHETIC] The computation smoke bundle passed locally:

```text
python -m pytest -q tests/test_p6_s6_g2_su3_formula_spec.py tests/test_p6_s6_g2_su3_implementation.py tests/test_p6c_s6_dirac_casimir_baseline.py tests/test_p6d_s6_spectrum_baseline.py tests/test_p6e_s6_spectrum_implementation.py tests/test_p6f_s6_spectrum_operator_review.py tests/test_p6g_s6_spectrum_operator_stabilization.py tests/test_p6h_s6_spectrum_operator_lockdown.py tests/test_p6i_s6_spectrum_operator_freeze.py tests/test_p6j_s6_spectrum_operator_final_review.py tests/test_p6k_s6_spectrum_computation.py
26 passed
```

[INFERRED] Next gate:

```text
P6L_S6_SPECTRUM_RESULT_REVIEW
```

## P6L S6 Spectrum Result Review

[CODE] The spectrum result review layer is now closed:

```text
P6L_S6_SPECTRUM_RESULT_REVIEW = passed
```

[CODE] The analytic S6 spectrum result review layer now records the computed
round-sphere baseline:

```text
lambda_{k,+/-} = +/- (k + 3) / R
mu_k = 8 * binomial(k + 5, k)
```

[CODE] The review layer deliberately defers:

- selection rules;
- SU(4) / hypercharge interpretation;
- instanton / index / chirality;
- runtime safe promotion.

[VERIFIED-SYNTHETIC] The review smoke test is the next check:

```text
python -m pytest -q tests/test_p6l_s6_spectrum_result_review.py
```

[VERIFIED-SYNTHETIC] The review smoke bundle passed locally:

```text
python -m pytest -q tests/test_p6_s6_g2_su3_formula_spec.py tests/test_p6_s6_g2_su3_implementation.py tests/test_p6c_s6_dirac_casimir_baseline.py tests/test_p6d_s6_spectrum_baseline.py tests/test_p6e_s6_spectrum_implementation.py tests/test_p6f_s6_spectrum_operator_review.py tests/test_p6g_s6_spectrum_operator_stabilization.py tests/test_p6h_s6_spectrum_operator_lockdown.py tests/test_p6i_s6_spectrum_operator_freeze.py tests/test_p6j_s6_spectrum_operator_final_review.py tests/test_p6k_s6_spectrum_computation.py tests/test_p6l_s6_spectrum_result_review.py
29 passed
```

[INFERRED] Next gate:

```text
P6M_S6_SELECTION_RULE_REVIEW
```

## P6M S6 Selection Rule Review

[CODE] The S6 selection-rule review layer is now closed:

```text
P6M_S6_SELECTION_RULE_REVIEW = passed
```

[CODE] The review classifies the current S6 rule families as:

```text
round_s6_dirac_spacing_rule -> S6_SPECTRUM_DERIVED
round_s6_multiplicity_rule -> S6_SPECTRUM_DERIVED
casimir_cross_check_rule -> CASIMIR_DERIVED
g2_su3_representation_labels -> REPRESENTATION_CANDIDATE
su4_hypercharge_mapping -> REQUIRES_SU4_HYPERCHARGE
s3xs6_tensor_product_coupling -> REQUIRES_TENSOR_PRODUCT_S3xS6
physical_v_selection_rule -> SMOKE_ONLY
```

[CODE] The review preserves the frozen fence:

```text
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

[INFERRED] Next gate:

```text
none; expand only if a new validated basis contract or a new physical
selection-rule derivation is supplied
```

## P7 SU4 Hypercharge Gauge Breaking Audit

[CODE] The P7 gauge-audit layer is now closed:

```text
P7_SU4_HYPERCHARGE_GAUGE_BREAKING_AUDIT = passed
```

[CODE] The audit works at the gauge-algebra level:

```text
Spin(6) ≅ SU(4)
so(6) ≅ su(4)
```

[CODE] The classification stays explicit:

```text
algebraically_verified:
  - Spin(6) ≅ SU(4) / so(6) ≅ su(4) algebra layer
  - SU(4) generator closure
  - trace convention
  - Hermiticity
  - tracelessness

basis_ordering_dependent:
  - SU(3)c embedding
  - right-neutrino invariance

normalization_dependent:
  - lambda_15 normalization
  - candidate Y_W

requires_tensor_product_S3xS6:
  - S3xS6 tensor-product coupling claim

requires_physical_input:
  - full fermion generation claim
  - Standard Model reproduced claim

smoke_only:
  - V-selection promotion
```

[CODE] The fence remains unchanged:

```text
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

[INFERRED] Next gate:

```text
P8_S3xS6_TENSOR_PRODUCT_BASIS_AND_SELECTION_RULES
```

## P8 S3xS6 Tensor Product Basis and Selection Rules

[CODE] The P8 tensor-product bridge layer is now closed:

```text
P8_S3xS6_TENSOR_PRODUCT_BASIS_AND_SELECTION_RULES = passed
```

[CODE] The bridge order is fixed as:

```text
S3 basis × S6 labels × SU4 labels, lexicographic tensor order
```

[CODE] The selection-rule classes are explicit:

```text
tensor_product_derived:
  - s3_spinor_basis_order
  - s6_spectrum_level_order
  - tensor_product_label_order

basis_ordering_dependent:
  - su4_generator_order
  - su3c_embedding_labels

normalization_dependent:
  - lambda_15_normalization
  - candidate_Y_W

requires_physical_input:
  - full fermion generation claim
  - Standard Model reproduced claim

smoke_only:
  - physical V-selection rule
```

[CODE] The fence remains unchanged:

```text
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

[INFERRED] Next gate:

```text
P9_MATRIX_ELEMENT_SELECTION_RULES
```

## P9 Matrix Element Selection Rules

[CODE] The P9 matrix-element audit layer is now closed:

```text
P9_MATRIX_ELEMENT_SELECTION_RULES = passed
```

[CODE] The audit treats the current working scaffold as a 16x16 Hermitian
matrix-element scaffold at `k_max=1` and preserves the direct Haar/unit-coframe
reduced matrix-element convention:

```text
normalization status = ANALYTIC_DIRECT_HAAR_CONVENTION
claim scope = engineering smoke tests only; no quantitative physics claims
```

[CODE] The selection-rule classes remain explicit:

```text
tensor_product_derived:
  - v_scaffold_shape
  - v_scaffold_hermiticity
  - S3 Cartan weights
  - P8 tensor-product bridge
  - S6 selection review
  - SU4 audit

basis_ordering_dependent:
  - basis ordering of S3/SU4 labels
  - current working selection-rule scaffold labels

normalization_dependent:
  - working reduced matrix elements
  - final Ben Achour E/E' basis mapping

requires_physical_input:
  - full fermion generation claim
  - Standard Model reproduced claim

smoke_only:
  - physical V-selection rule
```

[CODE] The fence remains unchanged:

```text
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

[INFERRED] Next gate:

```text
P10_SELECTION_RULE_MATRIX_ELEMENT_REVIEW
```

## P10 Selection Rule Matrix Element Review

[CODE] The terminal matrix-element review layer is now closed:

```text
P10_SELECTION_RULE_MATRIX_ELEMENT_REVIEW = passed
```

[CODE] The review keeps the frozen scaffold explicit:

```text
v_scaffold_shape = (16, 16)
v_scaffold_hermitian = True
v_scaffold_nonzero = True
selection_rule_status = smoke_only
```

[CODE] The review classification stays explicit:

```text
tensor_product_derived:
  - v_scaffold_shape
  - v_scaffold_hermiticity

normalization_dependent:
  - working reduced matrix elements
  - final Ben Achour E/E' basis mapping

smoke_only:
  - physical V-selection rule

requires_physical_input:
  - full fermion generation claim
  - Standard Model reproduced claim
```

[CODE] The fence remains unchanged:

```text
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

[INFERRED] Next gate:

```text
P11_EXTERNAL_ORACLE_MATRIX_ELEMENT_DERIVATION
```

## P11 External-Oracle Matrix-Element Derivation

[CODE] The external-oracle derivation is now closed:

```text
P11_EXTERNAL_ORACLE_MATRIX_ELEMENT_DERIVATION = passed
```

[CODE] The oracle comparison is explicit:

```text
external_oracle_status = EXTERNAL_ORACLE_DERIVED
comparison_status = MATCHES_FROZEN_SCAFFOLD
selection_rule_status = smoke_only
```

[CODE] The comparison stays scoped to the frozen matrix-element scaffold:

```text
k_max = 1, 2
pattern comparison = matches
hermiticity compatibility = true
exact coefficients = normalization_dependent
```

[CODE] The fence remains unchanged:

```text
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

[INFERRED] Next gate:

```text
P12_MATRIX_ELEMENT_DERIVATION_ROBUSTNESS_AUDIT
```

## P12 Matrix-Element Derivation Robustness Audit

[CODE] The robustness audit is now closed:

```text
P12_MATRIX_ELEMENT_DERIVATION_ROBUSTNESS_AUDIT = passed
```

[CODE] The axis classifications are explicit:

```text
basis_ordering_status = PERMUTED_EQUIVALENT
phase_status = PHASE_DEPENDENT
normalization_status = NORMALIZATION_DEPENDENT
k_max_status = ROBUST
hermiticity_status = ROBUST
overall_status = ROBUST
```

[CODE] The comparison stays within the frozen matrix-element contract:

```text
k_max = 1, 2, 3
pattern comparison = stable
Hermiticity = preserved
exact coefficients = normalization_dependent
```

[CODE] The fence remains unchanged:

```text
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

[INFERRED] Next gate:

```text
none; expand only if a new physical operator formula or a new validated operator scaffold is supplied
```

## PX Known Limitations and Next Evidence Requirements

[CODE] This is a limitation record, not a research gate.

```yaml
verified_claims:
  - gate: P11_EXTERNAL_ORACLE_MATRIX_ELEMENT_DERIVATION
    checked: external Wigner/CG oracle matches the frozen P9/P10 scaffold pattern for k_max = 1, 2
    evidence: pytest bundle passed
    status: passed
  - gate: P12_MATRIX_ELEMENT_DERIVATION_ROBUSTNESS_AUDIT
    checked: the P11 pattern is robust on tested axes
    evidence: pytest bundle passed
    status: passed

not_verified:
  - physical V-operator formula
  - exact physical coefficient normalization
  - physical V-selection rules
  - Standard Model reproduction
  - fermion generation claim
  - runtime safety
  - universality beyond tested conventions and k_max values
```

[CODE] Current fence:

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

[INFERRED] Next evidence requirement:

```text
explicit V operator formula candidate with its own dedicated promotion review
```

## P5K S3 Pauli / Clifford and Parity Smoke

[CODE] The S3 algebra scaffold now fixes an explicit Pauli map convention:

```text
U = x4 I + i(x1 sigma1 + x2 sigma2 + x3 sigma3)
```

[CODE] The coordinate and Clifford smoke layer records:

```text
factor_order = spinor / chirality / internal / placeholder
signature = euclidean
dimension = 4
```

[CODE] The parity smoke layer tests two S3-only candidates:

- P1 embedded inversion-like action
- P2 coordinate-swap smoke candidate

[VERIFIED-SYNTHETIC] The local smoke bundle passed:

```text
python -m pytest -q tests/test_p5k_s3_pauli_clifford_explicit.py tests/test_p5k_s3_parity_smoke.py
```

[VERIFIED-SYNTHETIC] Result:

```text
7 passed
```

[CODE] The parity smoke layer closes as:

```text
P5K_S3_PAULI_CLIFFORD_AND_PARITY_SMOKE = passed
```

[INFERRED] Current boundary:

```text
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

[INFERRED] Next gate:

```text
P5L_32D_KRONECKER_SKELETON_OR_S3_PARITY_FORMALIZATION
```

## P5L 32D Kronecker Skeleton or S3 Parity Formalization

[CODE] The combined S3 formalization layer is now closed:

```text
P5L_32D_KRONECKER_SKELETON_OR_S3_PARITY_FORMALIZATION = passed
```

[CODE] The S3 scaffold now includes an explicit 32D Kronecker skeleton:

```text
dimension = 32
factor_order = spinor / chirality / internal / flavor / placeholder
basis_order = lexicographic binary order on five tensor factors
```

[CODE] The parity smoke is now formalized with the already-validated P2
coordinate-swap smoke candidate.

[VERIFIED-SYNTHETIC] The P5L smoke tests are the next check:

```text
python -m pytest -q tests/test_p5l_s3_kronecker_skeleton.py tests/test_p5l_s3_parity_formalization.py
```

[INFERRED] Current boundary:

```text
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

[INFERRED] Next gate:

```text
P5M_S3_SELECTION_RULE_REVIEW_AFTER_PARITY_FORMALIZATION
```

## P5M S3 Selection Rule Review After Parity

[CODE] The selection-rule review layer is now closed:

```text
P5M_S3_SELECTION_RULE_REVIEW_AFTER_PARITY = passed
```

[CODE] The parity formalization did not justify promotion of the current `V`
scaffold:

```text
V-selection rules = smoke_only
```

[CODE] The selection-rule review remains tied to the engineering smoke scaffold
and the reduced matrix-element convention:

```text
reduced matrix-element status = ANALYTIC_DIRECT_HAAR_CONVENTION
parity candidate P1 = inconclusive
parity candidate P2 = passed
```

[VERIFIED-SYNTHETIC] The P5M smoke tests are the next check:

```text
python -m pytest -q tests/test_p5m_s3_selection_rule_review_after_parity.py
```

[INFERRED] Current boundary:

```text
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

[INFERRED] Next gate:

```text
none; expand V only if a new validated basis contract or a new physical
selection-rule derivation is supplied
```

## P6B S6 Metric / Connection / Spinor Convention

[CODE] The S6 implementation contract now fixes the geometric convention:

```text
metric normalization = unit round S6 normalization
connection choice = Levi-Civita connection on the canonical homogeneous metric
spinor-bundle convention = canonical spin structure induced by the G2/SU(3) reductive frame
Dirac convention = homogeneous Dirac operator with Casimir cross-check target
```

[VERIFIED-SYNTHETIC] The S6 contract bundle passed locally:

```text
python -m pytest -q tests/test_p6_s6_g2_su3_formula_spec.py tests/test_p6_s6_g2_su3_implementation.py
4 passed
```

[INFERRED] Remaining deferred items:

- selection rules;
- spectrum computation;
- SU(4) / hypercharge interpretation.

[INFERRED] Next gate:

```text
P6I_S6_SPECTRUM_OPERATOR_FREEZE
```

## Fast Resume Summary

```text
Context recovery: about 8.8/10.
Operational state: stable.
Scientific frame: collaborative support, not adjudication.
Main risk: tone and claim discipline.
Main unresolved blocker: exact alpha-domain / measure / generator equations.
Best next step: wait for Tom/raw equations; otherwise run only the tiny alpha-domain diagnostic.
```

## Protocol Layer: Scope Fence / Non-Promotion Discipline + HD-MAVP

[CODE] The protocol layer is active as an always-on guardrail and does not
change any frozen gate status.

```yaml
verified_claims:
  - gate: P11_EXTERNAL_ORACLE_MATRIX_ELEMENT_DERIVATION
    checked: external Wigner/CG oracle matches the frozen P9/P10 scaffold pattern
    evidence: pytest passed for k_max = 1, 2
    status: passed
  - gate: P12_MATRIX_ELEMENT_DERIVATION_ROBUSTNESS_AUDIT
    checked: the P11 pattern is stable under tested basis-ordering, phase,
      normalization, and k_max extension stress tests
    evidence: pytest passed for k_max = 1, 2, 3
    status: passed

not_verified:
  - physical V-operator formula
  - physical V-selection-rule promotion
  - Standard Model reproduction
  - fermion generation claim
  - runtime safety
  - exact coefficient universality across all conventions
```

[CODE] Current fence:

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

[CODE] Classification levels in use:

```text
LEVEL 0: code exists
LEVEL 1: smoke test passed
LEVEL 2: scaffold invariant passed
LEVEL 3: external oracle matched
LEVEL 4: robustness audit passed
LEVEL 4.5: external oracle + robustness audit passed, but no explicit physical operator
LEVEL 5: physical interpretation supported by explicit derivation
LEVEL 6: runtime-safe promotion after separate promotion gate
```

[INFERRED] Forbidden promotion language is replaced by scoped language unless a
separate promotion gate passes.

## Project Protocol Stack

[CODE] The project now has an always-on operational stack for gate handling,
scope discipline, source checking, red teaming, CI bundling, and context
capture.

```text
1. Scope Fence / Non-Promotion Discipline
2. HD-MAVP
3. LLM-MCM Gate Selection
4. Algebra Scaffold Verification
5. Selection-Rule Audit
6. Mathematical Source Verification
7. Red Team / No Fake-Pass
8. CI / Regression Bundle
9. ReportOps / ActiveContext Discipline
10. Gate-Based TDD
```

[CODE] The stack does not change any frozen gate status and does not promote
physical claims by itself.

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

[INFERRED] Reference report:

```text
reports/PROJECT_PROTOCOL_STACK.md
```

## Convention / Normalization Registry

[CODE] The project now keeps a frozen convention registry for basis ordering,
factor order, matrix conventions, trace conventions, generator normalization,
hypercharge normalization, radius convention, multiplicity convention, and
oracle convention matching.

```text
registry report = reports/CONVENTION_NORMALIZATION_REGISTRY.md
```

[CODE] The registry is a drift-prevention layer, not a research gate.

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

[INFERRED] Drift is only allowed through an explicit repair gate with a frozen
old convention, a new convention, and an explicit map between them.

## Ben Achour S3 Geometry Extraction

[CODE] The Ben Achour S3 source-supported geometry block is now frozen in the
registry for future operator-ansatz work:

- Hopf chart conventions for `alpha`, `phi`, `theta`
- source-supported scalar modes `T_{L,m_plus,m_minus}`
- Killing vectors `xi` and `xi'`
- exact / coexact one-form mode basis `E_i`, `E'_i`
- normalization and phase caveat tracking from the displayed PDF convention

[CODE] This is not a V-promotion gate.

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

[INFERRED] The repository now has source-supported Ben Achour geometry and an
executable low-mode `E_i` / `E'_i` implementation. Exact normalization remains
dependent, so later symbolic build steps stay non-promotional until a separate
derivation or repair gate fixes coefficients explicitly.

## P13A V-Operator Ansatz and Convention Registry

[CODE] The project now freezes a concrete candidate V-like ansatz and its
conventions for later symbolic derivation:

- ansatz: `V_S3(x) = lambda * sum_{a,I} gamma^a A_a^I(x) T_I`
- A-field mapping: source-supported Ben Achour one-form basis `E_i`, `E'_i`
- gamma convention: Euclidean Pauli/Clifford scaffold
- SU4 generator convention: `T_I = lambda_I / 2`
- readiness verdict: `P13_READY_FOR_SYMBOLIC_DERIVATION`
- Ben Achour executable one-form status: `BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE`
- exact normalization status: `NORMALIZATION_DEPENDENT`

[CODE] This is a registry and readiness gate, not a physical promotion gate.

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

## P13A1 Ben Achour One-Form Mode Implementation

[CODE] The repo now contains an executable low-mode Ben Achour one-form layer:

- scalar metadata / symbolic low-mode Phi
- Killing one-forms `xi_tilde` and `xi_prime_tilde`
- source-supported `B, B', C, C', E, E'` construction
- exact normalization remains dependent

[CODE] This is still source-supported geometry, not a physical V-promotion gate.

## P13B Symbolic V Matrix-Element Pattern Build

[CODE] The repo now contains a symbolic zero/nonzero matrix-element pattern
build for the candidate S3 V-like ansatz:

- symbolic pattern built from the frozen P11/P12 bridge
- executable P13A1 low-mode Ben Achour geometry used as input support
- real-valued shared reduced-symbol convention preserves Hermitian cancellation
- exact coefficients remain normalization-dependent

[CODE] This is still symbolic pattern work, not a physical V-promotion gate.

[VERIFIED-SYNTHETIC] The symbolic pattern matches the frozen P11/P12 pattern
for the tested `k_max = 1, 2, 3` bundle.

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

Current status:
P13B = SYMBOLIC_PATTERN_MATCHES_P11_P12
normalization = NORMALIZATION_DEPENDENT
next = none; expand only if coefficient-normalization repair or physical input is supplied

## P13B0 State Measure and Selection Rule Audit

[CODE] The repo now contains a repair-audit layer that checks:

- state labels through `k_max = 2`
- exact S3 Hopf measure application
- complex-valued toy matrix elements without `.real` truncation
- low-mode Ben Achour / spinor dependency classification
- selection-rule assumptions for the candidate `gamma^a A_a`

[VERIFIED-SYNTHETIC] The audit classifies the raw tuple `(0,0,0,0)` as
`INVALID_SPINOR_STATE` in the spinor context and keeps the selection-rule
derivation status at `INCONCLUSIVE`.

[CODE] The audit verdict is blocked before any new pattern claim.

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

Current status:
P13B0 = BLOCKED_BY_INVALID_SPINOR_STATE
next = none; repair the invalid spinor-state assumption before any further pattern claim

## P13B1 Spinor State and Selection Rule Repair

[CODE] The repo now contains a repaired spinor-basis audit for the candidate
S3 V-like validation setup:

- state records through `k_max = 2` and `k_max = 3`: inspected
- scalar tuple `(0,0,0,0)` is excluded from spinor tests
- lowest valid spinor state is preserved by the frozen ordering
- allowed final states from the lowest `k_max = 2` state are pattern-supported
- P11/P12 symbolic pattern remains valid on the repaired basis
- `P13B` rerun is not required

[VERIFIED-SYNTHETIC] The repaired basis does not promote any coefficient or
physical claim.

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

Current status:
P13B1 = P13B_PATTERN_STILL_VALID
next = none; coefficient normalization remains deferred until the repaired basis is accepted

## P13C0 Toy Gradient Formula Audit

[CODE] The repo now contains a toy-gradient reduced-element audit on the
repaired spinor basis:

- toy gradient reduced-element formula: derived as a toy model only
- exact Ben Achour `E_i / E'_i` formula: pending
- low-mode table bug: repaired with exact rational arithmetic
- `j_R' = j_R`: treated as `ASSUMED_BY_MODEL`
- upstream `P13B1` status: `passed`
- upstream `P13B1` verdict: `P13B_PATTERN_STILL_VALID`

[VERIFIED-SYNTHETIC] The low-mode table matches `full_matrix_element()` and
the audit remains normalization-dependent.

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

Current status:
P13C0 = NORMALIZATION_DEPENDENT
next = P13C_NORM_REDUCED_MATRIX_ELEMENT_NORMALIZATION_AUDIT

## P13C_NORM Reduced Matrix Element Normalization Audit

[CODE] The repo now contains a coefficient-normalization audit for the
candidate S3 V-like operator stack:

- coefficient provenance split into Wigner/CG, reduced matrix element,
  Ben Achour E/E' normalization, gamma/Clifford normalization, SU4 generator
  normalization, and coupling lambda
- relative coefficients are derived from the working scaffold
- exact Ben Achour / physical normalization remains unresolved
- coupling lambda remains a physical-input requirement
- wrong normalization and wrong phase are both classified as non-promotional

[VERIFIED-SYNTHETIC] The audit verdict remains `NORMALIZATION_DEPENDENT` and
does not promote physical V-selection rules.

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

Current status:
P13C_NORM = NORMALIZATION_DEPENDENT
next = none; exact coefficients remain normalization-dependent unless a separate normalization or physical-coupling repair gate is supplied

## P13C Ben Achour E-Mode Formula Derivation

[CODE] The repo now contains an exact Ben Achour E-mode formula derivation on
the repaired basis:

- exact source-supported low-mode identities:
  `E_i = (L + 2) B_i + C_i` and `E'_i = (L + 2) B'_i - C'_i`
- low-mode boundary case `L = 1`: `VANISHING_OR_EXCLUDED`
- exact source formula: `SOURCE_FIXED`
- reduced matrix element normalization: still `NORMALIZATION_DEPENDENT`
- pattern comparison: matches the frozen P11/P12 scaffold
- scope: exact source identities only, no physical promotion

[VERIFIED-SYNTHETIC] The exact-formula gate separates source-fixed identities
from normalization-dependent reduced coefficients and keeps the physical
operator unpromoted.

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

Current status:
P13C = SOURCE_FIXED
next = none; exact source identities are fixed, while reduced coefficients remain normalization-dependent unless a separate normalization or physical-coupling repair gate is supplied

## P13D Coefficient Normalization And Hermiticity Audit

[CODE] The repo now contains a coefficient-normalization and Hermiticity audit
for the repaired Ben Achour stack:

- exact Ben Achour source identities: source-fixed
- Haar/unit-coframe normalization, Clifford gamma convention, and P7 SU4 trace
  convention: fixed at the current audit level
- exact reduced coefficient normalization: still normalization-dependent
- Hermiticity: preserved under the audited convention stack
- compatibility with frozen P11/P12 pattern: preserved
- scope: coefficient audit only, no physical promotion

[VERIFIED-SYNTHETIC] The audit keeps the physical operator unpromoted while
distinguishing source-fixed identities from normalization-dependent reduced
coefficients.

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

Current status:
P13D = NORMALIZATION_DEPENDENT
next = none; exact coefficient scale remains normalization-dependent unless a separate normalization or physical-coupling repair gate is supplied

## P13E Reduced Coefficient Scale Fixing Or No-Go

[CODE] The repo now contains a reduced coefficient scale fixing / no-go audit
for the repaired Ben Achour stack:

- exact source identities: fixed
- Haar/unit-coframe, Ben Achour one-form, Clifford, and P7 SU4 conventions:
  fixed at the current audit level
- Hermiticity: preserved under the audited convention stack
- compatibility with frozen P11/P12 pattern: preserved
- exact reduced coefficient scale: still a no-go / normalization-dependent
- coupling lambda: free physical input
- scope: scale-fixing or no-go audit only, no physical promotion

[VERIFIED-SYNTHETIC] The audit preserves the pattern and Hermiticity while
classifying the reduced coefficient scale as unresolved under the current
source stack.

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

Current status:
P13E = NORMALIZATION_DEPENDENT_NO_GO
next = none; the unresolved reduced coefficient scale remains a no-go unless a separate physical-coupling or normalization repair gate is supplied

## P13F V-Operator Derivation Status And No-Go Record

[CODE] The repo now contains a final status record for the candidate V-like S3
operator stack:

- source identities: fixed
- convention stack: fixed
- Hermiticity: preserved
- compatibility with frozen P11/P12: preserved
- reduced coefficient scale: `NORMALIZATION_DEPENDENT_NO_GO`
- coupling lambda: free physical input
- operator derivation: blocked / no-go record only
- scope: status record only, no physical promotion

[VERIFIED-SYNTHETIC] The final record is conservative: it preserves the
frozen scaffold and records the derivation block without promoting physics.

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

Current status:
P13F = NO_GO_RECORD
next = none; a physical V-operator derivation remains blocked unless a new source-fixed coupling or normalization repair gate is supplied

## P13G Handoff Limitations And Next Evidence Package

[CODE] The repo now contains a handoff package for the frozen candidate
V-like S3 operator stack:

- verified claims: source identities, convention stack, Hermiticity, P11/P12
  compatibility, no-go on reduced scale, free coupling lambda
- not verified: physical V-operator derivation, physical V-selection rules,
  Standard Model reproduction, fermion generation claim, runtime safety
- next evidence requirement: an external physical principle or source-fixed
  coupling derivation that actually fixes lambda
- scope: handoff/limitations package only, no physical promotion

[VERIFIED-SYNTHETIC] This package is a clean stop point, not a new derivation.

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

Current status:
P13G = HANDOFF_RECORDED
next = none; a new physical principle or source-fixed coupling derivation is required to continue the V-branch

## P13H S3 Absolute Normalization Integral Test

[CODE] The repo now contains a single explicit low-mode S3 integral audit for
the candidate V-like operator stack:

- selected state: lowest repaired spinor representative from P13B1
- measure: Lawrence/Hopf `rho^3 sin(alpha) cos(alpha)` applied exactly once
- matrix element: reduced to `coefficient × lambda`
- coefficient: `16*pi**2*rho**3/15`
- phase control: invariant under a global unit phase twist
- coupling lambda: still free
- status: `NORMALIZATION_DEPENDENT_NO_GO`
- scope: one explicit integral only, no physical promotion

[VERIFIED-SYNTHETIC] The test is intentionally narrow and symbolic; it avoids a
grid sweep and keeps the previous no-go fence intact.

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

Current status:
P13H = NORMALIZATION_DEPENDENT_NO_GO
next = none; the branch remains blocked unless a new source-fixed coupling principle or repair gate fixes lambda

## P13 V Branch Simple Status And Handoff

[CODE] The V-branch is now frozen as a strong research scaffold, not a
physical proof:

- pattern of allowed matrix elements: verified with external oracle support
- Hermiticity: preserved
- Ben Achour `E_i / E'_i`: source-fixed at low mode
- explicit low-mode integral: computed
- exact result: `(<psi_i|V|psi_j> = 16*pi**2*rho**3/15 * lambda)`
- blocker: `lambda` remains free
- physical `V` operator: not promoted

[VERIFIED-SYNTHETIC] This is the plain-language handoff summary for the
current branch state. It records the exact blocker without reopening the
derivation.

[CODE] The short handoff has been expanded into a full chronology report:
`reports/P13_V_BRANCH_SIMPLE_STATUS_AND_HANDOFF.md`. The document now covers
the Part 3 context, the `cot(2 alpha)` dead end, the replacement scaffold, the
P11/P12 oracle path, the P13A-H gate chain, and the 32 project directions in a
single long-form handoff.

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

Current status:
V branch = scaffold complete, physical promotion blocked
next = none; continuation requires a new external physical principle that fixes lambda or a different branch

## P14 Lambda Fixing Options Feasibility Note

[CODE] The repo now contains a structured decision note for possible ways to
fix or reinterpret the free coupling `lambda` after the S3-only no-go result.

[VERIFIED-SYNTHETIC] The note ranks six routes:

- S3×S6 scale / radius relation
- action-principle requirement
- topological / Chern-Simons / winding quantization feasibility
- FRGE / UV fixed-point feasibility
- phenomenological calibration
- ML-assisted pattern search

[VERIFIED-SYNTHETIC] Current conclusion:

```text
lambda is still free under the current S3-only evidence.
```

[INFERRED] The best-priority scientific route is the S3×S6 scale / radius
relation, followed by an action-principle check. Phenomenological calibration
can only reinterpret lambda, and ML is hypothesis generation only.

Current status:
P14 = FEASIBILITY_NOTE_COMPLETE
lambda = FREE_COUPLING_PARAMETER

Next:
none; continue only if a new physical principle, a new S3×S6 derivation, or a
source-fixed coupling relation is supplied
