# S3 Dirac Spectrum Visualization P1

Date: 2026-06-07

## Scope

[CODE] This report records a preliminary visualization of the direct Haar-unit coframe spectrum for:

```text
D(lambda) = D0 + lambda V
```

with:

```text
k_max = 3
```

This is a debug / preliminary artifact only. It does not claim:

- a physical homogeneous `SU(2)` gauge-background spectrum;
- an instanton;
- an index theorem result;
- chirality;
- spectral flow;
- eta invariants;
- zero modes;
- validation of Tom Lawrence's theory.

## Temporary Convention

[CODE] The visualization uses the exact direct Haar/unit-coframe convention:

```text
ANALYTIC_DIRECT_HAAR_CONVENTION
||e^i|| scale = 1
final_ben_achour_normalization = unresolved
```

## Artifact

[CODE] The visualization code is implemented in:

```text
s3_dirac_spectrum_viz.py
tests/test_s3_dirac_spectrum_viz.py
reports/s3_dirac_spectrum_viz_prelim.png
```

## Verification

[VERIFIED-SYNTHETIC] Targeted checks:

```text
python -m pytest -q .\tests\test_s3_dirac_spectrum_viz.py
3 passed
```

[VERIFIED-SYNTHETIC] The rendered PNG is non-empty and was generated successfully.

## Observed Preliminary Behavior

[VERIFIED-SYNTHETIC] A sweep over:

```text
lambda in [0.0, 1.0]
```

shows:

- smooth symmetric shifts relative to `D0`;
- no loss of Hermiticity in the smoke operator;
- no visible violation of the `|lambda| < 1.0` forbidden zone used by the smoke tests.

[VERIFIED-SYNTHETIC] Endpoint summary for the first ordered levels:

```text
D0 first levels: -4.5 repeated
D(lambda=1) first levels: shifted to approximately -4.55244, -4.52905, ...
```

[INFERRED] The shifts are systematic and small under the exact direct Haar-unit coframe convention.

## Claim Discipline

[CODE] Allowed wording:

```text
preliminary spectrum visualization
direct Haar-unit coframe smoke layer
pending exact direct Haar scale and separate Ben Achour E/E' basis mapping
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

[VERIFIED-SYNTHETIC] The visualization layer is working and produces a non-blank plot.

[UNCERTAIN] It remains a smoke-layer diagnostic, not evidence for a physical gauge-background spectrum.

