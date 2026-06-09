# Ben Achour et al. 2016 PDF Recheck — 2026-06-07

Source file:

```text
C:\Users\serge\Downloads\1505.03426v2 (1).pdf
```

Scope: compare the local PDF against the current `tom_s3_spinor_toy` assumptions and the pasted text excerpt.

## Verdict

[VERIFIED] The pasted excerpt is broadly consistent with the PDF, but text extraction/OCR mangles some formulas. Use rendered PDF pages for equation-level work.

[VERIFIED] This paper is about scalar modes and vector/one-form harmonics on `S3`, not Dirac spinor eigenspinors.

## What the PDF Confirms

[VERIFIED] Title / scope:

```text
Explicit vector spherical harmonics on the 3-sphere
```

The abstract says the authors build explicit one-forms on `S3` forming a complete set of eigenmodes for the Laplace-de Rahm operator.

[VERIFIED] Hopf coordinates, eq. (1):

```text
x1 = sin(alpha) cos(phi)
x2 = sin(alpha) sin(phi)
x3 = cos(alpha) cos(theta)
x4 = cos(alpha) sin(theta)

alpha in [0, pi/2]
theta, phi in [0, 2pi)
```

[VERIFIED] Metric:

```text
ds^2 = d alpha^2 + cos^2(alpha) d theta^2 + sin^2(alpha) d phi^2
```

with orthonormal co-frame:

```text
e_alpha = d alpha
e_theta = cos(alpha) d theta
e_phi = sin(alpha) d phi
```

[VERIFIED] Consequence for volume density:

```text
sqrt(g) = sin(alpha) cos(alpha) = 1/2 sin(2 alpha)
```

This is positive on the paper's Hopf domain `[0, pi/2]`.

[VERIFIED] Scalar modes, eq. (3), use:

```text
x = cos(2 alpha)
S = m_+ + m_-
D = m_+ - m_-
Jacobi polynomial P_{L/2 - m_+}^{(S,D)}(x)
phase exp(i(S phi + D theta))
```

Guardrail: quote the full normalization constant only from rendered PDF or original TeX, not from OCR extraction.

[VERIFIED] Killing vectors, eqs. (4)-(5):

```text
xi  = X12 + X34 = partial_phi + partial_theta
xi' = X12 - X34 = partial_phi - partial_theta
```

The PDF states `||xi|| = ||xi'|| = 1`.

[VERIFIED] Their associated one-forms satisfy, eq. (6):

```text
* d xi  = -2 xi
* d xi' = +2 xi'
```

[VERIFIED] Scalar modes are eigenmodes of these differential operators:

```text
xi(Phi_i)  = mu_i Phi_i,     mu_i = +2 i m_+
xi'(Phi_i) = nu_i Phi_i,     nu_i = -2 i m_-
```

[VERIFIED] One-form construction, eq. (7):

```text
A_i  = d Phi_i
B_i  = * d(Phi_i xi)
C_i  = * d B_i
B'_i = * d(Phi_i xi')
C'_i = * d B'_i

E_i  = (L + 2) B_i  + C_i
E'_i = (L + 2) B'_i - C'_i
```

The resulting co-exact modes satisfy:

```text
Delta E_i  = -L^2 E_i
Delta E'_i = -L^2 E'_i
```

for `L >= 2`, with the stated boundary exclusions.

## Comparison Against Current Project

[CODE] Current `geometry_s3_hopf.py` matches Ben Achour eq. (1) for the standard Hopf domain:

```text
alpha in [0, pi/2]
sqrt(g) = sin(alpha) cos(alpha)
volume = 2 pi^2
```

[CODE] Current `phase4_alpha_domain_diagnostic.py` correctly treats extending `alpha` to `(0, pi)` as a diagnostic, not as Ben Achour's coordinate domain.

[INFERRED] Ben Achour strengthens the convention mismatch:

```text
Ben Achour standard Hopf alpha: [0, pi/2]
Tom's currently reported alpha: [0, pi]
```

Therefore Tom's alpha is not directly the same object as Ben Achour's Hopf alpha unless there is a patch, signed chart, double cover, or another coordinate convention.

## Usefulness for Tom S3 Work

[INFERRED] This paper is useful as the scalar/vector harmonic bridge closest to Tom's stated construction:

```text
scalar harmonics on S3
Killing-vector action
SU(2)_L x SU(2)_R-related quantum labels m_+, m_-
one-form/vector harmonic construction from scalar modes
```

[INFERRED] It is not sufficient to judge Tom's spinor-transforming scalar combinations. For that, we still need Tom's exact generator equations and covariance condition.

## Next Useful Test

Implement a small `ben_achour_scalar_modes.py` layer and tests:

```text
1. T_{L,m_+,m_-}(alpha, phi, theta) from eq. (3)
2. xi T = 2 i m_+ T
3. xi' T = -2 i m_- T
4. weighted orthogonality under sin(alpha) cos(alpha)
5. explicit caveat: scalar/vector harmonic baseline, not Dirac spinor eigenspinor
```

Do not implement from OCR. Use rendered PDF formula or original source.

