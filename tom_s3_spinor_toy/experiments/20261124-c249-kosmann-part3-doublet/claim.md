# Claim C249: the Kosmann (spinorial) Lie derivative in the Hopf frame and the (0, 1/2) doublet of Part 3

**Date:** 2026-11-24 (written before the script was run)
**FL tier:** Standard
**Question type:** [x] descriptive (mathematical identity on the round unit S^3; no physical claim)

## Background

In Part 3 the correspondent applies the SU(2)_R generators, written as vector fields in Hopf coordinates
(alpha, theta, theta~), to a scalar ansatz A(alpha) exp(+-i(theta - theta~)/2) and reaches cot^2(2 alpha) = -1.
This step is known to us only through an external summary (2026-11-24); the slides were not opened.
Peter-Weyl (TOM-CERT-01, C222) says scalar functions carry only (j, j), so a scalar (0, 1/2) doublet cannot exist.
An external text proposed that the missing piece is the frame-rotation term of the Kosmann derivative.

## Predictions (fixed before running)

P1. In the orthonormal Hopf frame E = (d_alpha, d_theta / sin alpha, d_theta~ / cos alpha) the Kosmann derivative
    L_v psi = nabla_v psi - (1/4) sum_{bc} g(nabla_{E_b} v, E_c) sigma_b sigma_c psi (one sign) commutes with the Dirac
    operator for all six Killing fields; the opposite sign and the plain component-wise action do not.
P2. For d_theta and d_theta~ the correction vanishes (the frame is torus-invariant), so the Cartan generators act by
    plain derivatives and half-integer charges force half-integer phases in the Hopf-frame components.
P3. The Hopf frame, transported once around a theta-loop, is a non-contractible loop in SO(3) relative to a global
    (left-invariant) frame, so Hopf-frame components of a smooth spinor are antiperiodic in theta and theta~.
    (This would correct my 2026-11-24 remark that half-angle phases are "not on S^3": that holds for scalars only.)
P4. A spinor field with i_L = 0 and i_R = +1/2 (highest weight) exists; with its partner it closes under the full
    corrected SU(2)_L x SU(2)_R as (0, 1/2), with no imaginary cotangent.
P5. The scalar version of the same system (no correction) has only the zero solution, reproducing the obstruction.

## Amendment after the run (2026-11-24; the predictions above are left as written)

- P1 formula: with the index order g(nabla_{E_b} v, E_c), the sign that passes is **+** (1/4) sum ..., not -. The prereg said "one sign"; the discriminating test chose +. Use the + form to reproduce.
- Conventions fixed: N^+ = (K23 + K14)/2, ... is called SU(2)_R (its N3 = (d_theta - d_thetat)/2); frame orientation det[x, E1, E2, E3] = -1 in R^4; D = sum_k sigma_k nabla_{E_k} with Hermitian sigma (eigenvalues imaginary). The value -3i/2 and the pairing with "R" flip with orientation or with D = i sigma.nabla.
- The (1/2, 0) highest weight e^{i(theta + thetat)/2} (cos(alpha/2), i sin(alpha/2)) also exists, with D = +3i/2 (found by the skeptic, re-checked numerically).
- P5 is shown through a pointwise algebraic system, not by reproducing cot^2(2 alpha) = -1.

## Kill criterion

P1 fails for the chosen sign (then the construction is wrong), or P4 has no non-zero solution, or the scalar
system of P5 has a non-zero smooth solution (that would contradict Peter-Weyl and signal a bug).

## What this does NOT mean

- It does not reconstruct the correspondent's own operator or field equation; generators are derived here from the embedding.
- It does not say which SU(2) is physical spin, nor which multiplet is physically selected.
- It does not show the correspondent made an error; a spinor reading of his ansatz is one consistent reading.
- No novelty is claimed: the Kosmann derivative and Killing spinors on S^3 are textbook material.
