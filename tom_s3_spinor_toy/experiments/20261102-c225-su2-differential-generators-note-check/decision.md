# C225 Decision -- Differential generators of SU(2) on functions of xi and conj xi

**Date:** 2026-11-02

## Result

Exact sympy, 11 checks, xi and conj(xi) treated as independent symbols (Wirtinger calculus). With the action (U(g) f)(xi, conj xi) = f(g^-1 xi, conj(g^-1 xi)) and generators D_a = (1/i) d/dt U(exp(i t sigma_a / 2)) at t = 0: D_a = -(1/2)(sigma_a xi)^alpha d_alpha + (1/2)(sigma_a^* conj xi)^alpha conj(d)_alpha, computed from the definition for a generic function F; [D_1, D_2] = i D_3 and its cyclic images hold identically for generic F (not only for polynomials); the D_3 eigenvalues on (xi^1, xi^2, conj xi^1, conj xi^2) are (-1/2, +1/2, +1/2, -1/2); D_3[(xi^1)^p (xi^2)^q (conj xi^1)^r (conj xi^2)^s] = ((-p+q+r-s)/2) times the monomial, checked for p, q, r, s <= 3.

## Scripts and outputs (re-run in this folder)

| script | output | outcome |
|---|---|---|
| `note_final_check.py` | `run_output_note_final_check.txt` | 11 PASS, 0 FAIL |

## Conventions

U(g) f = f(g^-1 xi); g_a(t) = exp(i t sigma_a/2); (1/i) d/dt at t = 0; t real. The opposite (active, xi -> g xi) reading is treated in C226.

## What this does NOT imply

- that this action is the one the correspondent means; with xi -> g xi the weights and the commutator sign both flip (C226)
- that the monomial formula holds for all exponents: checked for exponents <= 3 only, it follows from the first-order form

## Caveat

The first symbolic run failed on an artefact (a complex t gave a conjugate(t) residual); declaring t real removes it. The check count includes several restatements of the definition.

## Notes

Result row R09 of the private correspondence layer; the generators were sent in a note on 2026-10-31. Status vocabulary follows the ledger; no result here is externally reviewed.
