# P5F Non-Cartan Commutator Convention Audit

Date: 2026-06-08

Scope: audit the exact commutator conventions for the explicit coordinate-space
non-Cartan generator layer in Lawrence coordinates `(alpha, theta, theta_tilde)`.

This audit is local to the `S3` spin-geometry layer only. It does not touch
`S6`, `SU4`, instantons, index, chirality, heavy spectra, or any production
runtime claim.

## Current State

```text
P5E_EXPLICIT_NONCARTAN_COORDINATE_GENERATORS = implemented / smoke-verified
P5F_NONCARTAN_COMMUTATOR_CONVENTION_AUDIT = passed
runtime = research_only
V-selection rules = smoke_only
```

## Convention Checked

The generator module now uses the standard Hermitian physics convention

```text
I = -i X
```

for the underlying real Killing vector field `X`.

This is the convention required to compare the coordinate-space generators with
the validated standard `S3` spinor-harmonic basis and with the lifted
`su(2)_L x su(2)_R` oracle.

## Verified Matching to the Standard Oracle

[VERIFIED] The following coordinate-space generators match the lifted standard
`su(2)` action on the validated lowest spinor frame:

```text
L1, L2, L3  <->  lifted left J1, J2, J3
R1, R2, R3  <->  lifted right J1, J2, J3
```

This was verified by fitting the action on the standard basis and comparing to
the oracle matrices from `standard_s3_spinor_harmonics.py`.

## Commutator Audit

[VERIFIED] The explicit matrix oracle now satisfies the standard Hermitian
`su(2)` commutators:

```text
[I1L, I2L] = i I3L
[I2L, I3L] = i I1L
[I3L, I1L] = i I2L

[I1R, I2R] = i I3R
[I2R, I3R] = i I1R
[I3R, I1R] = i I2R

[IaL, IbR] = 0
```

The commutator audit is now convention-consistent with the lifted standard
oracle and no longer convention-sensitive in the tested layer.

## Evidence

[VERIFIED] Targeted smoke bundle:

```text
python -m pytest -q tests/test_p5e_noncartan_coordinate_generators.py \
  tests/test_standard_s3_spinor_harmonics.py \
  tests/test_lawrence_i1r_failure_reproduction.py \
  tests/test_s3_spin_connection_lawrence_frame.py
15 passed
```

The extra two passes relative to the earlier P5E smoke bundle come from the new
oracle-matching and commutator-closure checks.

## Remaining Scope Boundary

[INFERRED] This closes the coordinate-space generator convention audit, but it
does **not** promote the project to runtime-safe.

[INFERRED] `V-selection rules` remain `smoke_only` because no full V-coupling
policy audit has been performed in this gate.

## Conclusion

```text
P5F = commutator conventions resolved
runtime = research_only
V-selection rules = smoke_only
next = P5G_V_SELECTION_RULE_REVIEW
```

