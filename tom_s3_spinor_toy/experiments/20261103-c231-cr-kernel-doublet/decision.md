# C231 Decision -- CR kernel on S^3 and the doublet

**Date:** 2026-11-03

## Result

Exact sympy, all asserted checks passed and all self-controls caught, exit 0 (`run_output_cr_kernel_doublet.txt`).

- For charge n = 0..4 the kernel of Lbar (degree <= n+3, modulo the sphere relation) has dimension n+1 and equals the span of the holomorphic monomials x1^i x2^(n-i); for n = -1, -2 it is zero.
- The kernel is SU(2)-invariant (pull-back convention A) with Casimir (n/2)(n/2+1): spin n/2.
- D3 weights on (x1, x2, y1, y2) = (-1/2, +1/2, +1/2, -1/2); the anti-holomorphic doublet has the opposite weights, and eta = (y2, -y1) transforms exactly like (x1, x2). The conjugate operator has kernel dimension n+1 at charge -n.
- In the gauge xi = (cos(th/2), sin(th/2) e^{i ph}): Psi = xi^2 * J xi and Phi = -xi^1 * J xi, with J xi = (-conj xi^2, conj xi^1) the pointwise Gamma = -1 eigenvector. So H2 of C228 = {f(xi) J xi : f in span(xi^1, xi^2)}, the holomorphic doublet times a frame vector.

Reading: the doublet is the degree-1 kernel of a first-order equation (Lbar f = 0, holomorphy), not of D0. Together with C230 (H2 is preserved by (1 - Gamma) sigma.L, not by D0), this gives two concrete candidate selectors.

## What this does NOT imply

- that the correspondent's equation is Lbar f = 0; no text of his equation is available
- novelty; textbook status not checked

## Caveat

Kernel dimensions are computed on polynomials of bounded degree (n+3), not proved for all degrees; the Riemann-Roch pattern is the expected general answer.

Ledger: C231_CR_KERNEL_ON_S3_AT_CHARGE_N_HAS_DIMENSION_N_PLUS_1_SPIN_N_OVER_2_H2_IS_HOLOMORPHIC_DOUBLET_TIMES_FRAME_VECTOR
Follow-ups: none
