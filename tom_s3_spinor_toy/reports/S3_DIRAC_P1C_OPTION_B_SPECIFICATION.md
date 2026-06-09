# S3 Dirac P1c Option B Specification

Date: 2026-06-07

Subject: Homogeneous `SU(2)` connection on `S3` for a future spectral/Wigner-basis Dirac extension.

## Scope

[CODE] This is a mathematical/design specification only.

It does not implement code, does not build a gauge-background matrix, does not run a spectrum calculation, and does not claim:

- `SU(2)` instanton;
- index theorem result;
- chirality result on odd-dimensional `S3`;
- spectral flow;
- eta invariant;
- zero modes;
- validation of Tom Lawrence's theory.

The intended future task is `P1d`: implement a controlled homogeneous `SU(2)` connection only after this specification is accepted or tightened.

## 1. Coframe On S3

### Coordinates

[CODE] We keep the current Ben Achour / Hopf baseline convention:

```text
x1 = sin(alpha) cos(phi)
x2 = sin(alpha) sin(phi)
x3 = cos(alpha) cos(theta)
x4 = cos(alpha) sin(theta)

alpha in [0, pi/2]
theta, phi in [0, 2pi)
```

The metric and volume form are:

```text
ds^2 = d alpha^2 + cos^2(alpha) d theta^2 + sin^2(alpha) d phi^2
dmu = sin(alpha) cos(alpha) d alpha d theta d phi
    = (1/2) sin(2 alpha) d alpha d theta d phi
```

### Coordinate Orthonormal Coframe

[CODE] The direct Hopf orthonormal coframe used in the current Ben Achour layer is:

```text
e^alpha = d alpha
e^theta = cos(alpha) d theta
e^phi   = sin(alpha) d phi
```

[INFERRED] This coframe is convenient for integration and local Clifford algebra checks, but it is not the preferred homogeneous group-manifold coframe for an `S3 ~= SU(2)` gauge-background design.

### Homogeneous Coframe Choice

[INFERRED] For Option B, the preferred coframe should be a left-invariant or right-invariant coframe on `S3 ~= SU(2)`. We choose a **left-invariant coframe** as the working design convention:

```text
sigma_1, sigma_2, sigma_3
```

with structure equations, up to radius/sign convention:

```text
d sigma_i = - epsilon_ijk sigma_j wedge sigma_k
```

For a sphere of radius `R`, the orthonormal coframe is:

```text
e^i = R sigma_i
```

so the structure equations become:

```text
d e^i = -(1/R) epsilon_ijk e^j wedge e^k
```

[UNCERTAIN] Some references use a factor of `1/2` in the Maurer-Cartan equations depending on whether `sigma_i` or `sigma_i/2` is called the invariant form. Before implementation, this normalization must be matched to the P0 Dirac spectrum `lambda = +/-(k+3/2)/R`.

### Relation To Euler Angles

[INFERRED] If Euler angles are needed, use a standard `SU(2)` parameterisation:

```text
g = exp(i phi_E sigma_3 / 2) exp(i beta sigma_2 / 2) exp(i psi sigma_3 / 2)
```

with a convention bridge to Hopf coordinates fixed by the Wigner-D audit. The current displayed-phase Wigner map is:

```text
a = -(phi_H + theta_H)
b = 2 alpha
c = phi_H - theta_H
```

[CODE] This is the `ben_achour_displayed_phase` convention. The Ben Achour `xi'` sign gap remains open but operationally unblocked.

## 2. Gamma Matrices And Spinor Representation

### Clifford Algebra

[INFERRED] Use the Hermitian Pauli matrices as Euclidean 3D gamma matrices:

```text
gamma^1 = sigma_x
gamma^2 = sigma_y
gamma^3 = sigma_z

{gamma^i, gamma^j} = 2 delta^ij
```

where:

```text
sigma_x = [[0, 1], [1, 0]]
sigma_y = [[0, -i], [i, 0]]
sigma_z = [[1, 0], [0, -1]]
```

### SU(2)_L x SU(2)_R Labels

[CODE] P1a currently labels clean Dirac branches as:

```text
positive branch: (j_L, j_R) = ((k + 1)/2, k/2)
negative branch: (j_L, j_R) = (k/2, (k + 1)/2)
```

with branch degeneracy:

```text
(2 j_L + 1)(2 j_R + 1) = (k + 1)(k + 2)
```

[INFERRED] In the chosen left-invariant coframe, the homogeneous connection should have a clear declaration of whether it couples through left or right group action. The first implementation should pick one action and make the other a testable alternative, not silently mix them.

### Current Convention

[CODE] All P1c records and future matrix metadata must carry:

```text
convention = ben_achour_displayed_phase
```

This means the displayed Ben Achour phase is used:

```text
exp(i(S phi + D theta))
S = m_+ + m_-
D = m_+ - m_-
```

and the operational `xi'` action is:

```text
xi' = partial_phi - partial_theta -> +2 i m_-
```

[INFERRED] Do not state that the Ben Achour sign gap is closed.

## 3. Homogeneous SU(2) Gauge Field

### Ansatz

[INFERRED] Use a homogeneous `SU(2)` connection aligned with the invariant coframe:

```text
A = lambda e^i T_i
```

where:

```text
lambda = real coupling parameter
T_i = SU(2) gauge generators
```

For a Hermitian physics convention, choose:

```text
T_i = (1/2) tau_i
```

where `tau_i` are Pauli matrices acting on the gauge/internal doublet.

[UNCERTAIN] If the implementation uses anti-Hermitian Lie algebra generators, then `T_i = -i tau_i/2` and the Dirac coupling must be adjusted so the full Dirac operator remains Hermitian. This must be fixed before code.

### Curvature

[INFERRED] The curvature is:

```text
F = dA + A wedge A
```

Using:

```text
d e^i = -c epsilon_ijk e^j wedge e^k
```

with `c = 1/R` or `1/(2R)` depending on normalization, one obtains:

```text
F = lambda d e^i T_i + lambda^2 e^i wedge e^j T_i T_j
```

Equivalently, using `[T_i, T_j] = i epsilon_ijk T_k` in a Hermitian convention, the Lie-algebra-valued part has the schematic homogeneous form:

```text
F^k proportional to (-c lambda + C lambda^2) epsilon_kij e^i wedge e^j T_k
```

where `C` depends on generator normalization.

[INFERRED] This is homogeneous because all components are constant in the invariant coframe.

[UNCERTAIN] The precise coefficient is not to be coded until the Maurer-Cartan and generator normalizations are fixed.

### Dirac Coupling

[INFERRED] The coupled Dirac operator has schematic form:

```text
D_A = D_0 + gamma^i A_i
```

With the ansatz above:

```text
gamma^i A_i = lambda gamma^i tensor T_i
```

if the spinor also carries an internal `SU(2)` gauge doublet.

[INFERRED] If no internal doublet is included, the object is not a genuine non-Abelian gauge coupling; it becomes a spin-space toy perturbation and must be labelled Option A, not Option B.

## 4. Matrix Elements In The Spectral/Wigner Basis

### Basis States

[CODE] The P1a scaffold uses spectral branch records:

```text
|k, branch, j_L, m_L, j_R, m_R>
```

with:

```text
branch = positive or negative
positive: (j_L, j_R) = ((k + 1)/2, k/2)
negative: (j_L, j_R) = (k/2, (k + 1)/2)
```

[INFERRED] A real implementation must expand P1a branch records into individual magnetic labels:

```text
m_L = -j_L, -j_L + 1, ..., j_L
m_R = -j_R, -j_R + 1, ..., j_R
```

### Gauge Matrix Element

[INFERRED] The future matrix element has the schematic form:

```text
<k', b', j_L', m_L', j_R', m_R'; a' |
  gamma^i A_i
| k, b, j_L, m_L, j_R, m_R; a>
```

where `a,a'` are internal gauge-doublet indices.

For the homogeneous ansatz:

```text
gamma^i A_i = lambda gamma^i tensor T_i
```

the matrix element factors into:

```text
spinor/spectral overlap
times internal SU(2) generator matrix element
times invariant one-form / vector-harmonic coupling
```

### Relation To Ben Achour One-Forms

[CODE] Ben Achour et al. build exact and co-exact one-form harmonics on `S3`:

```text
A_i = d Phi_i
E_i, E'_i = co-exact one-form modes
```

[INFERRED] The invariant coframe components `e^i` should be expressible as the lowest non-trivial co-exact one-form sector, equivalently as Killing one-forms related to the `L=1` vector modes or to the special Killing forms `xi`, `xi'`.

[UNCERTAIN] The exact mapping from the chosen invariant coframe `e^i` to Ben Achour `E_i/E'_i` normalization must be derived before implementation.

### 3j / Clebsch-Gordan Structure

[INFERRED] Since `S3 ~= SU(2)`, the product of spectral/Wigner states with a vector/invariant one-form reduces to `SU(2)` Clebsch-Gordan couplings.

The schematic selection rule is:

```text
j_L' in j_L tensor J_L(A)
j_R' in j_R tensor J_R(A)
```

where `(J_L(A), J_R(A))` is the representation content of the connection component.

For a left-invariant one-form, the dominant action is expected to be on one of the two `SU(2)` factors; for a right-invariant one-form, on the other.

[UNCERTAIN] Which factor is affected depends on the left/right convention for invariant forms and vector fields. This must be checked against the Wigner-D audit before implementation.

Expected small-step coupling candidates:

```text
Delta j_L = 0, +/-1
Delta j_R = 0
```

or the mirrored rule:

```text
Delta j_L = 0
Delta j_R = 0, +/-1
```

depending on whether the connection is left- or right-invariant.

[UNCERTAIN] Translated into `k`, this may allow `Delta k = 0, +/-1` for adjacent branch sectors, but this is a design hypothesis until the exact representation content is fixed.

## 5. Inner Product And Hermiticity

### Inner Product

[INFERRED] Use the spinor inner product:

```text
<psi | chi> = integral_S3 psi^\dagger chi dmu
```

with:

```text
dmu = (1/2) sin(2 alpha) d alpha d theta d phi
```

in Hopf coordinates, or equivalently the Haar measure in Euler/group coordinates.

If gauge-doublet indices are present:

```text
psi^\dagger chi = sum_spin sum_gauge psi^*_{spin,gauge} chi_{spin,gauge}
```

### Hermiticity Condition

[INFERRED] The gauge term must satisfy:

```text
<psi | gamma^i A_i chi> = <gamma^i A_i psi | chi>
```

equivalently:

```text
<psi | Aterm | chi> = <chi | Aterm | psi>*
```

Sufficient design conditions:

- `gamma^i` Hermitian;
- gauge generators `T_i` Hermitian if the coupling is written without an extra `i`;
- real `lambda`;
- orthonormal spectral basis under Haar measure;
- matrix elements constructed with complex conjugation conventions consistent with Wigner-D.

[UNCERTAIN] If anti-Hermitian gauge generators are used, the coupling must include the appropriate factor of `i` for the operator to remain Hermitian.

## 6. Expected Matrix Structure

### Clean Operator

[CODE] Current P1b operator:

```text
D_0 = diagonal(lambda_{k,branch})
```

in the exact spectral branch basis.

### Coupled Operator

[INFERRED] Future Option B operator:

```text
D_A = D_0 + A_spectral
```

where `A_spectral` is sparse and structured by `SU(2)` selection rules.

Expected structure:

- diagonal clean part from P1b;
- sparse off-diagonal or block-sparse gauge part;
- block organization by `(j_L, j_R, branch, gauge_index)`;
- no graph-neighbor structure;
- no coordinate-grid finite differences.

### Level Coupling

[HYPOTHESIS] If the homogeneous connection transforms as a low representation, it should couple only a small number of nearby representation sectors. A plausible first expectation is:

```text
Delta k = 0, +/-1
```

but this is not accepted as an implementation rule until derived from the chosen invariant coframe and Wigner-D convention.

## 7. Future Verification Plan

No checks are executed in this specification step.

After implementation, the minimum verification plan is:

```text
1. Build D_A for k_max = 3, 4, 5.
2. Verify lambda = 0 exactly reproduces D_0 from P1b.
3. Verify Hermiticity: ||D_A - D_A^\dagger|| within tolerance.
4. Verify matrix dimensions and degeneracy bookkeeping.
5. For small lambda, inspect spectral motion without claiming index.
6. Check cutoff stability as k_max increases.
7. Confirm no phantom low modes caused by broken Hermiticity or selection rules.
```

Allowed future statement:

```text
We observe spectral motion under a specified homogeneous SU(2) connection.
```

Forbidden future statement without additional theory:

```text
We found instanton zero modes.
We verified an index.
We proved Tom's theory.
```

## 8. Stop Conditions Before P1d Code

Do not implement Option B until these are fixed:

```text
1. Maurer-Cartan normalization for e^i.
2. Left-invariant vs right-invariant coframe choice.
3. Gamma/Pauli convention.
4. Hermitian vs anti-Hermitian SU(2) generator convention.
5. Internal gauge representation dimension.
6. Exact representation content of the connection component.
7. Matrix-element formula and selection rules.
8. Inner-product convention and Hermiticity proof/check.
```

## Current Verdict

[INFERRED] Option B remains the best physically/geometrically meaningful next candidate for `S3`.

[UNCERTAIN] The exact coefficients and selection rules are not yet implementation-ready.

[CODE] Next valid step is to tighten this specification, especially the invariant coframe normalization and Wigner-D selection rules, before writing `P1d` code.

## 9. Formula Tightening Before P1d

This section narrows the working formula set for a future `P1d` implementation. It is still a specification layer, not code.

### 9.1 Working Maurer-Cartan Normalization

[INFERRED] For the next design slice, use the working orthonormal left-invariant coframe convention:

```text
d e^i = -(1/R) epsilon_ijk e^j wedge e^k
```

where:

```text
R = S3 radius
epsilon_123 = +1
```

[UNCERTAIN] This is a working convention, not yet a physical-claim convention. Before any physics claim, it must be checked against:

- the P0 spectrum normalization `lambda = +/-(k + 3/2)/R`;
- the Wigner-D phase convention;
- the chosen normalisation of invariant one-forms;
- the Ben Achour one-form normalization.

### 9.2 Hermitian Gauge Generators And Coupling

[INFERRED] Use Hermitian `SU(2)` gauge generators:

```text
T_i = tau_i / 2
```

where `tau_i` are Pauli matrices acting on an internal gauge-doublet index.

The homogeneous connection ansatz is:

```text
A = lambda e^i T_i
lambda in R
```

The candidate Dirac coupling term is:

```text
V = lambda gamma^i tensor T_i
```

with Hermitian Euclidean gamma matrices:

```text
gamma^i = sigma_i
```

[INFERRED] With real `lambda`, Hermitian `gamma^i`, and Hermitian `T_i`, this local algebraic term is Hermitian before spectral projection, provided the spatial matrix elements use a consistent orthonormal basis and Wigner-D conjugation convention.

### 9.3 Branch / Representation Action Hypothesis

[HYPOTHESIS] Working hypothesis:

```text
left-invariant connection acts on one SU(2) factor only
right-invariant mirrored connection acts on the other SU(2) factor
```

For the first Option B formula path, use:

```text
left-invariant one-form representation: (J_L, J_R) = (1, 0)
right-invariant mirror alternative:     (J_L, J_R) = (0, 1)
```

[UNCERTAIN] This must be verified against the Ben Achour `E/E'` co-exact one-form conventions and the Wigner-D sign convention before implementation.

### 9.4 Schematic Matrix Element

Let:

```text
n = (k, branch, j_L, m_L, j_R, m_R)
a = internal SU(2) gauge index
```

The future matrix element is specified schematically as:

```text
V_{n'a',na}
  = lambda sum_i <n' | gamma^i e^i | n> <a' | T_i | a>
```

where:

```text
<a' | T_i | a>
```

is the internal gauge-doublet matrix element, and:

```text
<n' | gamma^i e^i | n>
```

is the spatial/spinor spectral overlap.

[INFERRED] This decomposition is the target structure for `P1d`; it should be tested first at the coefficient/Hermiticity level before any spectrum claim.

### 9.5 Wigner / Clebsch-Gordan Decomposition

[INFERRED] The spatial overlap is proportional to products of `SU(2)` Clebsch-Gordan coefficients, equivalently Wigner `3j` symbols:

```text
C(j_L, J_L, j_L'; m_L, q_L, m_L')
C(j_R, J_R, j_R'; m_R, q_R, m_R')
```

with selection rules:

```text
|j_L - J_L| <= j_L' <= j_L + J_L
|j_R - J_R| <= j_R' <= j_R + J_R

m_L' = m_L + q_L
m_R' = m_R + q_R
```

Equivalent `3j` notation may be used:

```text
( j_L  J_L  j_L' ; m_L  q_L  -m_L' )
( j_R  J_R  j_R' ; m_R  q_R  -m_R' )
```

with the usual phase convention to be fixed before implementation.

[UNCERTAIN] The exact reduced matrix element and phase factor are not yet specified. P1d is forbidden until these are fixed or explicitly parameterised in tests.

### 9.6 Working Representation Of The Homogeneous One-Form

[HYPOTHESIS] Working left-invariant choice:

```text
(J_L, J_R) = (1, 0)
```

Then:

```text
j_L' in {j_L - 1, j_L, j_L + 1}
j_R' = j_R
m_L' = m_L + q_L
m_R' = m_R
```

[HYPOTHESIS] Mirrored right-invariant alternative:

```text
(J_L, J_R) = (0, 1)
```

Then:

```text
j_L' = j_L
j_R' in {j_R - 1, j_R, j_R + 1}
m_L' = m_L
m_R' = m_R + q_R
```

[UNCERTAIN] The left/right assignment must be checked against Ben Achour `xi`, `xi'`, `E`, and `E'` conventions before code is allowed to make a physical interpretation.

### 9.7 Hermiticity Condition On Coefficients

The required coefficient-level Hermiticity condition is:

```text
V_{n'a',na} = conjugate(V_{na,n'a'})
```

Sufficient working assumptions:

```text
lambda is real
gamma^i are Hermitian
T_i are Hermitian
the spectral basis is orthonormal under Haar measure
CG / 3j phase conventions are used consistently
reduced matrix elements satisfy the corresponding conjugation rule
```

[INFERRED] The first P1d unit test must check Hermiticity directly from generated analytic/symbolic coefficients before any eigenvalue analysis.

### 9.8 Cautious Translation To k Couplings

[HYPOTHESIS] Combining P1a branch labels:

```text
positive branch: (j_L, j_R) = ((k + 1)/2, k/2)
negative branch: (j_L, j_R) = (k/2, (k + 1)/2)
```

with a low representation connection suggests nearby-level couplings, plausibly:

```text
Delta k = 0, +/-1
```

[UNCERTAIN] This is not yet an implementation rule. The allowed `k` couplings must be derived from the actual `(j_L, j_R)` selection rules and branch mapping.

### 9.9 Stop Condition For P1d

[CODE] P1d implementation is forbidden until a unit test can verify:

```text
V_{n'a',na} = conjugate(V_{na,n'a'})
```

from the generated symbolic/analytic coefficients under the chosen:

```text
Maurer-Cartan normalization
left/right invariant choice
gamma convention
SU(2) generator convention
CG / 3j phase convention
branch representation labels
```

[INFERRED] If this Hermiticity test cannot be written cleanly, the formula specification is still incomplete.
