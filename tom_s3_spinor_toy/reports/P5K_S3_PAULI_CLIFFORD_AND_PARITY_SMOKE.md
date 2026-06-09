# P5K S3 Pauli/Clifford and Parity Smoke

Date: 2026-06-08

## Executive Verdict

PAULI_CLIFFORD_PASSED_PARITY_PASSED

## Scope

Only S3 algebra scaffold and parity smoke.
No S6.
No SU4.
No V promotion.

## Pauli Scaffold

- coordinate convention: Lawrence/Hopf embedding with
  `x1 = rho sin(alpha) cos(theta)`, `x2 = rho sin(alpha) sin(theta)`,
  `x3 = rho cos(alpha) sin(theta_tilde)`, `x4 = rho cos(alpha) cos(theta_tilde)`
- Pauli map convention: `U = x4 I + i(x1 sigma1 + x2 sigma2 + x3 sigma3)`
- unitarity result: passes pointwise on the tested grid

## Clifford Scaffold

- gamma matrix convention: Euclidean
- factor ordering: `spinor / chirality / internal / placeholder`
- Clifford algebra result: passes the 4D anticommutator smoke test

## Parity Smoke

- tested parity candidates:
  - P1 embedded inversion-like action
  - P2 coordinate-swap smoke candidate
- radius preserved: yes for both candidates
- standard spinor basis closure:
  - P1: coefficient matrix varies with coordinates, inconclusive
  - P2: constant coefficients, passed
- limitations: this is a smoke test only; it does not claim a physical parity
  operator or a 32-component model.

## Tests

Command:

```text
python -m pytest -q tests/test_p5k_s3_pauli_clifford_explicit.py tests/test_p5k_s3_parity_smoke.py
```

Result:

```text
7 passed
```

## Status

```text
runtime = research_only
V-selection rules = smoke_only
safe_for_runtime = no
```

## Next Gate

```text
P5L_32D_KRONECKER_SKELETON_OR_S3_PARITY_FORMALIZATION
```
