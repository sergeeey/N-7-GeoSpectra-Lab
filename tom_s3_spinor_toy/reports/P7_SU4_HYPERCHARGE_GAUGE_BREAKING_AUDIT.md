# P7 SU4 Hypercharge Gauge Breaking Audit

Date: 2026-06-08

## Executive Verdict

```text
SU4_ALGEBRA_AUDIT_PASSED_WITH_NORMALIZATION_DEPENDENT_YW
```

## Scope

Only the gauge algebra layer in strict isolation from S3/S6 dynamics.

No full fermion generation claim.

No Standard Model reproduced claim.

No V-selection promotion.

## Algebra Layer

[CODE] The audit works at the intended level:

```text
Spin(6) ≅ SU(4)
so(6) ≅ su(4)
```

[CODE] The canonical 4x4 generalized Gell-Mann basis is used with the standard
HEP normalization:

```text
Tr(T_a T_b) = 1/2 delta_ab
```

[CODE] The basis ordering is fixed as:

```text
6 symmetric off-diagonal
6 antisymmetric off-diagonal
3 diagonal
```

[VERIFIED] The generated basis is Hermitian, traceless, and closed under the
commutator in the tested normalization.

## λ15 / SU(3)c / Y_W

[CODE] The canonical diagonal generator is fixed as:

```text
lambda_15 = diag(1,1,1,-3) / sqrt(6)
```

[CODE] The candidate hypercharge operator is audited as:

```text
Y_W = T_15
```

[CODE] The standard SU(3)c embedding is the upper-left 3x3 block.

[CODE] The right-neutrino direction is the 4th basis vector and is SU(3)c-singlet
under the audited embedding.

[INFERRED] The candidate Y_W remains normalization-dependent. This audit does
not promote it to a physical hypercharge claim.

## Claim Classification

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

## Tests

[VERIFIED] Targeted smoke test passed locally:

```text
python -m pytest -q tests/test_p7_su4_hypercharge_gauge_breaking_audit.py
3 passed
```

## Status

```text
P7_SU4_HYPERCHARGE_GAUGE_BREAKING_AUDIT = passed
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

## Next Gate

```text
P8_S3xS6_TENSOR_PRODUCT_BASIS_AND_SELECTION_RULES
```
