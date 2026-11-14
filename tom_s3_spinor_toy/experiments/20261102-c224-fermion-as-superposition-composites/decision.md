# C224 Decision -- Can a half-integer amplitude be a superposition of the bosons built from it?

**Date:** 2026-11-02

## Result

Exact sympy plus numeric checks, 34 checks in five scripts, two defined models. (1) Cut sphere, phi in (0, 2 pi): e^{i phi/2} equals an L^2 sum of e^{i k phi} with coefficients c_k = i/(pi (1/2 - k)) (Parseval sum 1); the periodic sum takes the value 0 at the seam; psi(phi + 2 pi) = -psi(phi), so the result is not a function on S^2 and does not commute with rotations. (2) The two-spinor composite space has total spin 0 and 1 only, and there is no intertwiner from an integer-spin to a half-integer representation (null space dimension 0, control 1). (3) On S^3 with the central element z = -I acting by xi -> -xi: odd functions (fermions, by definition) and even functions are L^2-orthogonal; products of two odd functions are even, so a constant-coefficient superposition of two-fermion composites cannot be a fermion; eps_ab xi^a xi^b = 0 for one doublet and eps_ab xi^a (eps conj xi)^b = -|xi|^2 = -1 for two different doublets. (4) On S^3 the identity xi^a = sum_b xi^a xi^b conj(xi^b) holds (|xi| = 1) but equals xi^a times 1, so it is not evidence that a fermion is composed of three fermions.

## Scripts and outputs (re-run in this folder)

| script | output | outcome |
|---|---|---|
| `q6_fourier_superposition.py` | `run_output_q6_fourier_superposition.txt` | 8 PASS, 0 FAIL |
| `q6_composites_reps.py` | `run_output_q6_composites_reps.txt` | 6 PASS, 0 FAIL |
| `q6_parity_statistics.py` | `run_output_q6_parity_statistics.txt` | 7 PASS, 0 FAIL |
| `q6_superposition_models.py` | `run_output_q6_superposition_models.txt` | 9 PASS, 0 FAIL |
| `q6_constructive.py` | `run_output_q6_constructive.txt` | 4 PASS, 0 FAIL |

## Conventions

Fermion = odd under xi -> -xi (definition used here); composite = pointwise product; superposition = constant-coefficient linear combination, finite or L^2-closed.

## What this does NOT imply

- anything about exchange statistics or a quantum field algebra: that needs a field model, none is built here
- that the correspondent's 'superposition' means constant coefficients; with point-dependent coefficients the statement changes
- that a physical fermion is composed of three fermions: the three-factor identity is trivial

## Caveat

The result is model-dependent: it holds for the two defined models. Checks M2 and M3b of q6_superposition_models.py are definitional; the Fourier overshoot mask in F4b was widened to 0.3 rad after a Gibbs overshoot (a calibration of a numeric check, the formula is unchanged).

## Notes

Result rows R07 and R08 of the private correspondence layer. Motivating hypothesis (a fermion is a superposition of the bosons composed of fermions) fails in the defined models, hence test_outcome FAIL with a supported negative finding. Status vocabulary follows the ledger; no result here is externally reviewed.
