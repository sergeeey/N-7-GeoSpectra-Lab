# S3 Dirac Methods Note

Date: 2026-06-07

## Scope

[CODE] This note summarizes the exact direct Haar-unit smoke layer for the S3 Dirac operator scaffold:

```text
D(lambda) = D0 + lambda V
```

with:

```text
k_max = 3
```

This is a methods note only. It does not claim:

- a physical homogeneous `SU(2)` gauge-background spectrum;
- an instanton;
- an index theorem result;
- chirality;
- spectral flow;
- eta invariants;
- zero modes;
- validation of Tom Lawrence's theory.

## Working Convention

[CODE] The operator stack uses the exact direct Haar/unit-coframe convention:

```text
ANALYTIC_DIRECT_HAAR_CONVENTION
||e^i|| scale = 1
final_ben_achour_normalization = unresolved
```

## Proven Working Pieces

[VERIFIED-SYNTHETIC] The following layers are already green:

```text
clean exact Dirac baseline D0
spectral/Wigner label scaffold
Hermitian symbolic V scaffold
direct-Haar one-form diagnostic
pre-registered toy smoke test for D = D0 + alpha V
exact-scale spectrum visualization
```

## Quantitative Sweep Summary

[VERIFIED-SYNTHETIC] Exact-scale sweep at `lambda in linspace(0, 1, 11)`:

```text
max_abs_shift  = 0.06112145532459046
mean_abs_shift = 0.031405583903139744
l2_shift       = 0.3520593881833174
min_abs_final  = 1.5206906325745546
max_symmetry_violation = 0.0
```

[VERIFIED-SYNTHETIC] Endpoint structure:

```text
D0 lowest branch: -4.5 repeated
D(lambda=1) lowest branch: approximately -4.552435702402905 repeated
next branch: approximately -4.529054582609522 repeated
```

## Interpretation

[INFERRED] The direct Haar-unit smoke layer produces small, symmetric, smooth shifts relative to the exact baseline.

[INFERRED] No numerical artifact was detected by the current smoke criteria:

- Hermiticity held;
- the spectrum remained symmetric about zero;
- the smallest absolute eigenvalue stayed above `1.0`.

[UNCERTAIN] This remains an engineering result, not a physical gauge-background claim.

## Claim Discipline

[CODE] Allowed wording:

```text
preliminary spectrum sweep
direct Haar-unit coframe smoke layer
quantitative engineering metric
pending separate Ben Achour E/E' basis mapping
no physical claims
```

[CODE] Forbidden wording:

```text
physical spectrum
instanton
index
zero modes
Tom validation
final normalization
```

## Verdict

[VERIFIED-SYNTHETIC] The current operator pipeline is stable enough for methods-style reporting.

[UNCERTAIN] Any physical interpretation must wait for the separate Ben Achour `E/E'` basis mapping discussion.
