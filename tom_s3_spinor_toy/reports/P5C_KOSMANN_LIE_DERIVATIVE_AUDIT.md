# P5C Kosmann Lie Derivative Audit

Date: 2026-06-08

Scope: local spin-geometry audit for the recovered Lawrence `S3` ansatz only.
No `kNN`, no `S6`, no `SU4`, no instanton/index/chirality claims, no heavy
compute, no external message to Tom.

## Executive Verdict

```text
KOSMANN_DOES_NOT_REMOVE_OBSTRUCTION
```

<fact> The recovered `S3` geometry and spin connection can be written down
cleanly from the Lawrence coordinates, but the current local evidence does not
show that the Kosmann/spinorial Lie derivative promotes the scalar-separable
Lawrence ansatz to a closed non-Cartan spinor representation.

<fact> The local repository conclusion remains the same as the current P5C
state: the safer implementation path is still standard `S3` spinor harmonics /
Killing spinors.

## 1. Geometry Setup

Recovered Lawrence coordinates:

```text
x1 = rho sin(alpha) cos(theta)
x2 = rho sin(alpha) sin(theta)
x3 = rho cos(alpha) sin(theta_tilde)
x4 = rho cos(alpha) cos(theta_tilde)
```

Metric:

```text
ds^2 = rho^2 d alpha^2 + rho^2 sin^2(alpha) d theta^2 + rho^2 cos^2(alpha) d theta_tilde^2
```

Orthonormal coframe:

```text
e^1 = rho d alpha
e^2 = rho sin(alpha) d theta
e^3 = rho cos(alpha) d theta_tilde
```

Cartan structure equations:

```text
de^1 = 0
de^2 = (cot(alpha) / rho) e^1 ^ e^2
de^3 = -(tan(alpha) / rho) e^1 ^ e^3
```

Nonzero spin connection 1-forms:

```text
omega_12 = - cos(alpha) d theta
omega_13 = + sin(alpha) d theta_tilde
```

Equivalently in the orthonormal frame:

```text
omega^1_2 = - (cot(alpha) / rho) e^2
omega^1_3 = + (tan(alpha) / rho) e^3
omega^2_1 = + (cot(alpha) / rho) e^2
omega^3_1 = - (tan(alpha) / rho) e^3
```

## 2. Gamma / Pauli Convention

Use the local Euclidean 3D Clifford basis:

```text
gamma^1 = sigma_1
gamma^2 = sigma_2
gamma^3 = sigma_3
```

with

```text
{gamma^a, gamma^b} = 2 delta^{ab} I
```

This is sufficient for the local `S3` spin-geometry audit.

## 3. Spin Covariant Derivative

Definition:

```text
nabla_mu psi = partial_mu psi + 1/4 omega_{mu ab} gamma^a gamma^b psi
```

With the above coframe, the nonzero directional derivatives are:

```text
nabla_alpha psi = partial_alpha psi
nabla_theta psi = partial_theta psi - (cos(alpha)/2) gamma^1 gamma^2 psi
nabla_theta_tilde psi = partial_theta_tilde psi + (sin(alpha)/2) gamma^1 gamma^3 psi
```

This is the exact local spin-connection correction missing from scalar dragging.

## 4. Kosmann Audit for `I_{1R}`

Recovered scalar vector field from the P5B frame:

```text
X_{1R} = 1/2 * (
  cos(theta - theta_tilde) partial_alpha
  - sin(theta - theta_tilde) * (cot(alpha) partial_theta + tan(alpha) partial_theta_tilde)
)
```

Kosmann / spinorial Lie derivative:

```text
L_X^spin psi = X^mu nabla_mu psi + 1/4 (nabla_mu X_nu - nabla_nu X_mu) gamma^mu gamma^nu psi
```

Local comparison:

- scalar dragging on `psi_{0,1/2} = A(alpha) exp(i(theta-theta_tilde)/2)` is the
  P5B failure mode;
- it produces an unwanted harmonic sector and forces
  `A'(alpha) / A(alpha) = cot(2 alpha)`;
- that relation integrates to `A(alpha) ~ sqrt(sin(2 alpha))`, but the ladder
  coefficient remains `alpha`-dependent in the scalar-dragging audit.

<inference> The Kosmann correction is the right formal ingredient, but the
current local repository evidence does not demonstrate that it removes the
`cot(2 alpha)` obstruction for the recovered scalar-separable Lawrence ansatz.

## 5. Scalar Dragging vs Kosmann

| Aspect | Scalar dragging | Kosmann path |
| --- | --- | --- |
| Spin connection included | No | Yes, in principle |
| Extra harmonic sector | Present | Not shown removed in local audit |
| `cot(2 alpha)` obstruction | Present | Not shown resolved |
| Constant ladder coefficient | No | Not established in current local evidence |
| Non-Cartan closure on current ansatz | Fails | Not promoted to a validated closure |

## 6. Obstruction Status

<fact> The local tests preserve the non-rescue conclusion:

```text
python -m pytest -q tests/test_lawrence_i1r_failure_reproduction.py tests/test_s3_spin_connection_lawrence_frame.py
4 passed
```

<inference> That is enough to keep the current project status at `research_only`
with `V-selection rules = smoke_only`.

<inference> The audit does not establish a rescue of the Lawrence ansatz by the
Kosmann derivative. The obstruction remains unresolved for the current scalar-
separable basis.

## 7. Caveats

- local spin-geometry test only;
- not full Lawrence theory validation;
- not `S6` / `SU4`;
- not hypercharge;
- not instanton / index / chirality;
- no heavy compute.

## 8. Evidence Trail

- P5B report: scalar-dragging failure and `cot(2 alpha)` obstruction.
- P5C report: current repository conclusion is
  `standard_spinor_harmonics_required`.
- Targeted regression checks passed locally and preserve that conclusion.

## 9. Next Step

```text
P5C_STANDARD_S3_SPINOR_HARMONICS_IMPLEMENTATION
```

