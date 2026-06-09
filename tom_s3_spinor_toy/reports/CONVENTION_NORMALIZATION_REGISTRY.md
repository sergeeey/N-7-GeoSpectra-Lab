# Convention / Normalization Registry

Date: 2026-06-08

## Objective

Record the frozen conventions and normalizations used by the validated S3,
S6, SU4, tensor-bridge, and matrix-element oracle layers.

This is a registry and fence document, not a research gate.

## Registry Entry

[CODE] The current registry records the conventions already frozen by the
project:

- P7 SU(4) / hypercharge gauge audit
- P13A1 Ben Achour one-form mode implementation
- P13A V-operator ansatz and convention registry
- P8 tensor-product basis/order bridge
- P9 matrix-element selection-rule audit
- P11 external-oracle matrix-element derivation
- P12 matrix-element derivation robustness audit
- P13H exact low-mode normalization integral audit
- P13C_NORM reduced matrix-element normalization audit
- P6K S6 spectrum computation

## Drift Check

[CODE] No silent basis reorder, phase flip, normalization rescale, tensor-factor
swap, or hypercharge rescale is allowed without a separate repair gate.

[CODE] Convention drift must be classified explicitly as one of:

```text
CONVENTION_FIXED
BASIS_ORDERING_DEPENDENT
FACTOR_ORDER_DEPENDENT
PHASE_CONVENTION_DEPENDENT
NORMALIZATION_DEPENDENT
RADIUS_DEPENDENT
SIGNATURE_DEPENDENT
SOURCE_CONVENTION_MISMATCH
MULTIPLICITY_CONVENTION_AMBIGUOUS
CONVENTION_DRIFT_DETECTED
PROMOTION_BLOCKED
```

## Dependency Classification

[VERIFIED-SYNTHETIC] The registry is consistent with the frozen project
contracts:

- P7: SU(4) generator normalization and Y_W candidate remain normalization-dependent.
- P13A1: low-mode Ben Achour one-form geometry is executable, while exact
  normalization remains dependent.
- P13A: candidate V ansatz is source-supported geometrically but not physically promoted.
- P8: S3 × S6 × SU4 tensor bridge remains basis-ordering-sensitive.
- P9: working reduced matrix elements remain normalization-dependent.
- P11/P12: external oracle match is robust on tested axes but exact coefficients remain normalization-dependent.
- P6K: S6 Dirac spectrum uses the round-sphere radius convention `R = 1 unless explicitly parameterized`.

## Matrix / Generator Conventions

| Field | Current Convention | Source | Status | Blocks Promotion |
| --- | --- | --- | --- | --- |
| basis_ordering | generalized Gell-Mann order / frozen bridge order / frozen scaffold ordering | P7/P8/P9/P11/P12 contracts | mixed | yes |
| factor_order | S3 basis × S6 labels × SU4 labels when tensor bridge is used | P8 contract | factor-order dependent | yes |
| trace_convention | Tr(T_a T_b) = 1/2 delta_ab for SU(4) generators | P7 contract | fixed | yes |
| lambda_15 | diag(1,1,1,-3)/sqrt(6) | P7 contract | normalization dependent | yes |
| Y_W | T_15 candidate; physical scaling not promoted | P7 contract | normalization dependent | yes |
| radius | R = 1 unless explicitly parameterized | P6K contract | fixed for current baseline | yes |
| multiplicity | per-sign multiplicity unless marked total | P6K/P9/P8 contracts | explicit | yes |
| phase | fixed by local basis/oracle contract; no silent phase flips | P11/P12 contracts | phase dependent | yes |

## P13A V-Operator Ansatz Registry

[VERIFIED-SYNTHETIC] The candidate V-like ansatz is now frozen as a source-
supported geometry registry entry:

- ansatz: `V_S3(x) = lambda * sum_{a,I} gamma^a A_a^I(x) T_I`
- A-field mapping: built from Ben Achour one-form basis `E_i` and `E'_i`
- gamma convention: Euclidean Pauli/Clifford scaffold
- SU4 generator convention: `T_I = lambda_I / 2`
- readiness: `P13_READY_FOR_SYMBOLIC_DERIVATION`
- Ben Achour executable one-form layer: `BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE`
- promotion status: physical promotion still blocked
- scope: registry only, not derivation

[VERIFIED-SYNTHETIC] The repo now exposes executable low-mode Ben Achour
`E_i` / `E'_i` mode functions. Exact normalization remains dependent, so later
symbolic build steps stay non-promotional until a separate derivation or repair
gate fixes coefficients explicitly.

## Spectrum Conventions

[CODE] The S6 spectrum contract is:

```text
lambda_{k,+/-} = +/- (k + 3) / R
mu_k = 8 * binomial(k + 5, k)
```

[CODE] Multiplicity is tracked as per-sign multiplicity in the spectrum contract.

## Tensor Factor Order

[CODE] The tensor bridge order is fixed as:

```text
S3 basis × S6 labels × SU4 labels, lexicographic tensor order
```

[CODE] Any swap requires an explicit permutation map and a separate repair gate.

## External Oracle Convention

[CODE] The P11/P12 oracle convention is:

- oriented Wigner/CG coefficients
- Hermitianized selection pattern
- exact coefficients normalization-dependent
- pattern stable through tested robustness axes

## Ben Achour S3 Geometry Extraction

[VERIFIED-SYNTHETIC] The Ben Achour source-supported geometry block is now
registered for future operator-ansatz work:

- coordinate chart: Hopf `S3` chart with `alpha`, `phi`, `theta`
- metric: `dalpha^2 + cos^2(alpha) dtheta^2 + sin^2(alpha) dphi^2`
- coframe: `dalpha`, `cos(alpha) dtheta`, `sin(alpha) dphi`
- scalar modes: `T_{L,m_plus,m_minus}`
- Killing vectors: `xi = partial_phi + partial_theta`, `xi' = partial_phi - partial_theta`
- one-form modes: exact / coexact `E_i`, `E'_i` basis extracted from the source
- normalization: source-supported geometry only; no physical `V` promotion
- status: `SOURCE_SUPPORTED_GEOMETRY`

## P13A1 Ben Achour One-Form Mode Implementation

[VERIFIED-SYNTHETIC] The repo now contains an executable low-mode Ben Achour
one-form layer:

- executable module: `ben_achour_one_form_modes.py`
- low-mode scalar and Killing-vector source identities: implemented
- low-mode `B, B', C, C', E, E'` chain: implemented
- exact normalization of `E_i` / `E'_i`: normalization-dependent
- status: `BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE`
- scope: source-supported geometry only, no physical promotion

## P13B Symbolic V Matrix-Element Pattern Build

[VERIFIED-SYNTHETIC] The repo now contains a symbolic zero/nonzero matrix-
element pattern build for the candidate S3 V-like ansatz:

- symbolic pattern built from the frozen P11/P12 bridge and the executable
  P13A1 low-mode Ben Achour geometry
- exact coefficients remain normalization-dependent
- status: `NORMALIZATION_DEPENDENT`
- scope: symbolic pattern build only, no physical promotion

## P13B0 State Measure and Selection Rule Audit

[VERIFIED-SYNTHETIC] The repo now contains a repair-audit layer for the
candidate S3 V-like validation setup:

- state labels through `k_max = 2`: enumerated
- raw tuple `(0,0,0,0)` in the spinor context: `INVALID_SPINOR_STATE`
- S3 measure `sqrt(g) = sin(alpha) cos(alpha)`: applied once
- complex-valued matrix-element probe: preserved without `.real` truncation
- gamma^a A_a selection-rule audit: `INCONCLUSIVE`
- status: `BLOCKED_BY_INVALID_SPINOR_STATE`
- scope: repair audit only, no physical promotion

## P13B1 Spinor State and Selection Rule Repair

[VERIFIED-SYNTHETIC] The repo now contains a repaired spinor-basis audit for
the candidate S3 V-like validation setup:

- spinor state records through `k_max = 2` and `k_max = 3`: inspected
- raw scalar tuple `(0,0,0,0)`: excluded from spinor tests
- lowest valid spinor state: preserved in the frozen ordering
- allowed final states for the lowest `k_max = 2` state: pattern-supported
- P11/P12 symbolic pattern: still valid on the repaired basis
- `P13B` rerun: not required
- status: `P13B_PATTERN_STILL_VALID`
- scope: repair audit only, no coefficient normalization

## P13C0 Toy Gradient Formula Audit

[VERIFIED-SYNTHETIC] The repo now contains a toy-gradient reduced-element
audit for the repaired basis:

- toy gradient reduced-element formula: derived as a toy model only
- exact Ben Achour `E_i / E'_i` formula: pending
- low-mode table bug: repaired with exact rational arithmetic
- `j_R' = j_R`: treated as `ASSUMED_BY_MODEL`
- status: `NORMALIZATION_DEPENDENT`
- scope: toy-gradient audit only, no physical promotion

## P13C Ben Achour E-Mode Formula Derivation

[VERIFIED-SYNTHETIC] The repo now contains an exact Ben Achour E-mode formula
derivation on the repaired basis:

- exact source-supported low-mode identities:
  `E_i = (L + 2) B_i + C_i` and `E'_i = (L + 2) B'_i - C'_i`
- low-mode boundary case `L = 1`: `VANISHING_OR_EXCLUDED`
- exact source formula: `SOURCE_FIXED`
- reduced matrix element normalization: still `NORMALIZATION_DEPENDENT`
- pattern comparison: matches the frozen P11/P12 scaffold
- scope: exact source identities only, no physical promotion

## P13D Coefficient Normalization And Hermiticity Audit

[VERIFIED-SYNTHETIC] The repo now contains a coefficient-normalization and
Hermiticity audit for the repaired candidate stack:

- exact Ben Achour source identities: source-fixed
- Haar/unit-coframe, Clifford gamma, and P7 SU4 trace conventions: fixed at
  the current audit level
- exact reduced coefficient normalization: still `NORMALIZATION_DEPENDENT`
- Hermiticity: preserved under the audited convention stack
- compatibility with frozen P11/P12 pattern: preserved
- scope: coefficient audit only, no physical promotion

## P13E Reduced Coefficient Scale Fixing Or No-Go

[VERIFIED-SYNTHETIC] The repo now contains a reduced-scale fixing / no-go
audit for the repaired candidate stack:

- exact source identities: fixed
- Haar/unit-coframe, Ben Achour one-form, Clifford, and P7 SU4 conventions:
  fixed at the current audit level
- Hermiticity: preserved under the audited convention stack
- compatibility with frozen P11/P12 pattern: preserved
- exact reduced coefficient scale: still a no-go / normalization-dependent
- coupling lambda: free physical input
- scope: scale-fixing or no-go audit only, no physical promotion

## P13F V-Operator Derivation Status And No-Go Record

[VERIFIED-SYNTHETIC] The repo now contains a final status record for the
candidate V-like S3 operator stack:

- source identities: fixed
- convention stack: fixed
- Hermiticity: preserved
- compatibility with frozen P11/P12: preserved
- reduced coefficient scale: `NORMALIZATION_DEPENDENT_NO_GO`
- coupling lambda: free physical input
- operator derivation: blocked / no-go record only
- scope: status record only, no physical promotion

## P13G Handoff Limitations And Next Evidence Package

[VERIFIED-SYNTHETIC] The repo now contains a handoff package for the frozen
candidate V-like S3 operator stack:

- verified claims: source identities, convention stack, Hermiticity, P11/P12
  compatibility, no-go on reduced scale, free coupling lambda
- not verified: physical V-operator derivation, physical V-selection rules,
  Standard Model reproduction, fermion generation claim, runtime safety
- next evidence requirement: an external physical principle or source-fixed
  coupling derivation that actually fixes lambda
- scope: handoff/limitations package only, no physical promotion

## P13C_NORM Reduced Matrix Element Normalization Audit

[VERIFIED-SYNTHETIC] The repo now contains a coefficient-normalization audit
for the candidate S3 V-like operator stack:

- coefficient provenance is split into Wigner/CG, reduced matrix element,
  Ben Achour E/E' normalization, gamma/Clifford normalization, SU4 generator
  normalization, and coupling lambda
- relative coefficients are available from the working scaffold
- exact Ben Achour / physical normalization remains unresolved
- lambda remains a physical-input requirement
- wrong normalization and wrong phase are both flagged as non-promotional
- status: `NORMALIZATION_DEPENDENT`
- scope: normalization audit only, no physical promotion

[CODE] Legacy filename retained for compatibility:

```text
reports/P13C_REDUCED_MATRIX_ELEMENT_NORMALIZATION_AUDIT.md
(display label: P13C_NORM)
```

## P13H S3 Absolute Normalization Integral Test

[VERIFIED-SYNTHETIC] The repo now contains a single explicit low-mode S3
integral audit for the candidate V-like operator stack:

- selected low-mode representative: lowest repaired spinor pair from P13B1
- measure: Lawrence/Hopf `rho^3 sin(alpha) cos(alpha)` volume factor applied
  exactly once
- exact matrix element: derived as `coefficient × lambda`
- coefficient: `16*pi**2*rho**3/15`
- phase control: invariant under a global unit phase twist
- coupling lambda: remains free
- status: `NORMALIZATION_DEPENDENT_NO_GO`
- scope: one explicit integral only, no physical promotion

## Verdict

```text
registry_status = CONVENTION_REGISTRY_FIXED
physics_status = PROMOTION_BLOCKED
lambda_status = FREE_COUPLING_PARAMETER
blocking_fields = basis_ordering, factor_order, trace_convention, lambda_15,
Y_W, radius, multiplicity, phase
promotion_allowed = false
required_repair_gate = explicit convention-repair gate, if any field drifts
next_safe_gate = none; this is a registry, not a research gate
```

## Scope Fence

This registry verifies only convention bookkeeping and drift prevention.

It does not verify:

```text
- physical interpretation
- runtime safety
- Standard Model reproduction
- full selection-rule promotion
- claims outside current scaffold
```

Current status:

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```
