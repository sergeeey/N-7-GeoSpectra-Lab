# S3 Dirac Spectrum Sweep Analysis P1D

Date: 2026-06-07

## Scope

[CODE] This note records a quantitative analysis of the exact direct Haar-unit smoke-layer sweep for:

```text
D(lambda) = D0 + lambda V
```

with:

```text
k_max = 3
lambda grid = linspace(0, 1, 11)
```

This is a preliminary engineering analysis only. It does not claim:

- a physical homogeneous `SU(2)` gauge-background spectrum;
- an instanton;
- an index theorem result;
- chirality;
- spectral flow;
- eta invariants;
- zero modes;
- validation of Tom Lawrence's theory.

## Convention

[CODE] The spectrum is evaluated under:

```text
ANALYTIC_DIRECT_HAAR_CONVENTION
||e^i|| scale = 1
final_ben_achour_normalization = unresolved
```

## Computed Metrics

[VERIFIED-SYNTHETIC] Endpoint comparison between `D0` and `D(lambda=1)`:

```text
max_abs_shift  = 0.06112145532459046
mean_abs_shift = 0.031405583903139744
l2_shift       = 0.3520593881833174
```

[VERIFIED-SYNTHETIC] Spectral safety checks at `lambda=1`:

```text
min_abs_final = 1.5206906325745546
max_symmetry_violation = 0.0
```

[VERIFIED-SYNTHETIC] First 10 ordered eigenvalues at the endpoints:

```text
D0:
-4.5 repeated

D(lambda=1):
-4.552435702402905 repeated for the lowest branch,
then -4.529054582609522 for the next repeated pair.
```

## Interpretation

[VERIFIED-SYNTHETIC] The branch trajectories remain smooth and symmetric on the sampled lambda grid.

[VERIFIED-SYNTHETIC] The coupled operator stays outside the `|lambda| < 1.0` smoke-test zone and remains Hermitian.

[INFERRED] The observed shifts are small and systematic under the exact direct Haar-unit coframe convention.

[UNCERTAIN] This remains a smoke-layer spectrum study, not evidence for a physical gauge-background spectrum.

## Claim Discipline

[CODE] Allowed wording:

```text
preliminary spectrum sweep
direct Haar-unit coframe smoke layer
quantitative engineering metric
pending separate Ben Achour E/E' basis mapping
no physical claims
```

Forbidden wording:

```text
physical spectrum
instanton
index
zero modes
Tom validation
final normalization
```

## Verdict

[VERIFIED-SYNTHETIC] The exact-scale P1d sweep is numerically stable and produces a coherent symmetric branch structure.

[UNCERTAIN] The next interpretive step is a methods-style summary, not a physical claim.
