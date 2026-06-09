# Wigner-D Micro Audit - 2026-06-07

[VERIFIED-SYNTHETIC] Scope: representation-sanity only; not a Tom Lawrence theory verdict.

## Convention

`D^j_{m',m}(a,b,c) = exp(-i m' a) d^j_{m',m}(b) exp(-i m c)`

Hopf-aligned map for the displayed Ben Achour phase:

```text
a = -(phi + theta)
b = 2 alpha
c = phi - theta
j = L/2, m' = m_plus, m = -m_minus
```

## Small-L Checks

| L | m_plus | m_minus | j | m' | m | max residual | ratio |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.0 | 0.0 | 0.0 | 0.0 | -0.0 | 0.000e+00 | 1+0i |
| 1 | 0.5 | 0.5 | 0.5 | 0.5 | -0.5 | 2.652e-16 | -1.41421356237+-1.7376180584e-17i |
| 1 | 0.5 | -0.5 | 0.5 | 0.5 | 0.5 | 5.675e-16 | 1.41421356237+-1.0433812822e-16i |
| 2 | 1.0 | 0.0 | 1.0 | 1.0 | -0.0 | 4.718e-16 | -1.41421356237+-8.8457939226e-17i |
| 2 | 1.0 | 1.0 | 1.0 | 1.0 | -1.0 | 9.742e-16 | 2+8.61497800296e-17i |

## Sign Caveat

[VERIFIED-SYNTHETIC] The Wigner-D alignment reproduces the displayed Ben Achour phase.
Therefore `xi' = partial_phi - partial_theta` gives `+2 i m_minus`.
The rendered PDF text states `-2 i m_minus`; this remains an explicit convention gap.

Equivalently, the PDF-stated pair of eigenvalues would require:

```text
exp(i(D phi + S theta))
```

rather than the displayed:

```text
exp(i(S phi + D theta))
```

## Working Convention Decision

[CODE] Downstream code adopts the displayed Ben Achour phase as an explicit working convention:

```text
convention_id = ben_achour_displayed_phase
phase = exp(i(S phi + D theta))
xi' = partial_phi - partial_theta -> +2 i m_minus
gap_status = resolved_as_typo
```

[INFERRED] This is a resolved sign convention in the codebase.
Treat the displayed phase as the default and keep the paper-text minus only as a legacy note.

The recorded alternative remains:

```text
phase = exp(i(D phi + S theta))
xi' -> -2 i m_minus
```

## Direct Euler-Swap Candidate

[VERIFIED-SYNTHETIC] For `a=theta_H`, `b=2 alpha`, `c=phi_H`, the Wigner labels needed to match the displayed or sign-resolving phase leave the allowed `[-j,j]` range for the PDF-valid boundary case `L=2, m_+=1, m_-=1`.
