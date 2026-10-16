# C220 Claim — sphere normalisation of the l=1 harmonics, ladder operators on the normalised set, and "discovering" the harmonics from the ladder operators

**Date:** 2026-10-12
**FL tier:** [x] Standard (derivation/instrument round in support of external correspondence; no project physics claim)
**Question type:** [x] descriptive (exact calculation; no population, no intervention)
**Numbering note:** C219 was taken by a parallel session's commit (`0e61a14`) while this round was being set up; this round is therefore C220.

## Why this round exists

The correspondent's reply of 2026-10-10 (a PDF; its prose is not reproduced
here) asks for four things, all of them calculations that must be shown step
by step, not just summarised. Two earlier rounds were criticised for exactly
that (C201: headline `sqrt(2)` only; C205/C206: too few intermediate steps):

1. Decide whether the surface integral `∫_{S²} x* x dS` over the sphere of radius
   `r` is proportional to `r²` or to `r⁴`; if the correspondent's corrected
   value is wrong, correct it; give the normalised real harmonics.
2. Normalise the complex harmonics by the same method.
3. Apply the ladder operators to the sphere-normalised complex harmonics:
   do the coefficients equal McMurry's exactly? Are the matrices of `L±` equal
   to `Γ'(T_23) ± iΓ'(T_31)` (his complex-basis matrices, already encoded in
   C205 step 3) or must the normalisations change for that to hold?
4. "Discover" the complex harmonics from the ladder operators: eigenfunctions
   of `L_z` with eigenvalues `-1,0,1` (an unknown function of `θ` times an
   `e^{imφ}` factor), `L₊ Y_{1,1} = 0`, `L₋ Y_{1,-1} = 0`, then `Y_{1,0}` from
   `L₋ Y_{1,1}` or `L₊ Y_{1,-1}`.

## Prior Result Gate

1. `C201` (polar `L±` on McMurry's `l=1` harmonics, `sqrt(2)` throughout),
   `C205` (rotation generators and the real-to-complex change `z`, which
   reproduces the correspondent's matrices for `Γ'(T_12)`, `Γ'(T_23)`,
   `Γ'(T_31)`), `C206` (polar and Cartesian `L±`, matrices in two bases)
   are all reused as inputs, not re-derived by assumption: this round
   recomputes what it needs from scratch and compares to their saved results.
2. `grep` of `experiments/`, `null_results/`, `parked/` for sphere
   normalisation of the `l=1` harmonics or for a ladder-operator "discovery"
   route: no hits.
3. **Source gap, stated up front.** C201's `Y_{1,-1}` came from the standard
   relation `Y_{l,-m} = (-1)^m conj(Y_{l,m})`, not from McMurry's definition on
   p. 92, which this project has not seen (C201's `decision.md` wording
   "ONLY McMurry's own stated definitions" overstates this for `m<0`). This
   round does not repair the source gap; it shows what the `m<0` definition
   must be for the ladder coefficients to be `+sqrt(2)` (P5).
4. **Status:** [x] NEW.

## Estimand

One sentence, written before any result: *we compute, exactly, the sphere
integrals, ladder-operator actions and matrices of the `l=1` harmonics of
`S²` of radius `r`, in polar and Cartesian form, handling the unknown
convention for `Y_{1,-1}` and the Condon–Shortley phase by stating it as an
explicit parameter rather than assuming it.*

**Population:** the three `l=1` harmonics on `S²_r`, real (`x,y,z`) and
complex (`x±iy, z`) forms. **Method:** exact symbolic computation (sympy),
independently cross-checked by numerical quadrature and finite differences
(scipy/numpy), which share no code path with the symbolic route.
**Conventions fixed before the run:** `L_z = -i ∂_φ`;
`L₊ = e^{iφ}(∂_θ + i cotθ ∂_φ)`, `L₋ = e^{-iφ}(−∂_θ + i cotθ ∂_φ)` (McMurry
p. 144 as used in C201/C206); Cartesian `L_x = i(z∂_y − y∂_z)`,
`L_y = i(x∂_z − z∂_x)`, `L_z = i(y∂_x − x∂_y)`, `L± = L_x ± iL_y` (C205/C206);
matrices in the **row = input** convention, `operator(b_a) = Σ_b M[a][b] b_b`.

## Pre-registered predictions (written before the script was run)

| # | Prediction | If false |
|---|---|---|
| P1 | `∫ x²dS = ∫ y²dS = ∫ z²dS = 4πr⁴/3`; mixed integrals vanish. The `r²` version, `4πr²/3`, is the integral of `(x/r)²`, not of `x²`; it also fails a dimension check for `x` | report the actual values |
| P2 | Normalised real harmonics `x'_i = √(3/(4π)) x_i / r²`, which equals `½√(3/π) x_i/r²`; Gram matrix = identity | report |
| P3 | Raw complex functions `x+iy, z, x−iy` have squared norms `8πr⁴/3, 4πr⁴/3, 8πr⁴/3` (ratio 2:1:2) and are mutually orthogonal. Normalised with Condon–Shortley phase: `Y'_{1,1} = −√(3/(8π))(x+iy)/r²`, `Y'_{1,0} = √(3/(4π)) z/r²`, `Y'_{1,-1} = +√(3/(8π))(x−iy)/r²`; Gram = identity; polar form = `Y_{1,m}(θ,φ)/r`; equals sympy's `Ynm` at `r=1` | report |
| P4 | `L± Y'_{1,m} = √2 Y'_{1,m±1}` (0 at the ends), in polar **and** Cartesian form, for every `r>0` (the `1/r` factor passes through, `L` is tangent to spheres). The magnitude `√2` is forced by the norm: `∫|L₋Y'_{1,1}|²dS = 2` | report the coefficients actually obtained |
| P5 | If `Y_{1,-1}` is replaced by `κ Y_{1,-1}`, the coefficients become `L₋Y_{1,0} = (√2/κ)(κY_{1,-1})` and `L₊(κY_{1,-1}) = κ√2 Y_{1,0}`. Dropping the Condon–Shortley sign of `Y_{1,1}` flips the sign of `L₊Y_{1,0}`. So "all coefficients `+√2`" selects unit sphere normalisation **and** the phase `Y_{1,-1} = −Y*_{1,1}` | report |
| P6 | In the basis `e = ((x+iy)/r, z/r, (x−iy)/r)`: `M(L₊) = [[0,0,0],[−1,0,0],[0,2,0]]`, `M(L₋) = [[0,−2,0],[0,0,1],[0,0,0]]`, and `M(L±) = Γ'(T_23) ± iΓ'(T_31)` with the matrices encoded in C205 step 3. In the basis `Y'` the entries of `M(L±)` are `√2, √2`; the generator matrices there are `D Γ' D⁻¹` with `D = diag(−1/√2, 1, 1/√2)`, i.e. Hermitian-symmetric forms; the identity `L± = Γ(T_23) ± iΓ(T_31)` holds in **both** bases (it is an operator identity), so no change of harmonic normalisation is *required* — what changes is the numerical form of the `Γ` matrices | report |
| P7 | Discovery route: `L₊(χe^{iφ}) = 0 ⇒ χ = C sinθ`; `L₋(χe^{-iφ}) = 0 ⇒ χ = C' sinθ`; `L₋ Y_{1,1}` and `L₊ Y_{1,-1}` agree for `Y_{1,0}` **only if** `C' = −C`; normalisation fixes `|C| = √(3/(8π))`; positivity of `Y_{1,0}` at the north pole fixes `C = −√(3/(8π))`. **Negative control:** the wrong annihilation conditions (`L₋` on `e^{iφ}` or `L₊` on `e^{-iφ}`) give `χ = C/sinθ`, which is not normalisable | report |

**Negative controls (must be able to fail):** (a) the `r²`-version of the
integral is evaluated and shown to fail the dimension test; (b) the
`κ`-rescaled `Y_{1,-1}` and the CS-phase-dropped `Y_{1,1}` must change the
coefficients as predicted in P5; (c) a basis with `e₁` and `e₃` swapped must
*fail* the comparison with `Γ'`; (d) the wrong-sign annihilation conditions in
P7.

**Positive control:** sympy's own `Ynm(1,m,θ,φ)` (an implementation that does
not use this script's definitions) must reproduce the `Y_{1,m}` used here.

## Kill criterion

| Condition | Consequence |
|---|---|
| Any of P1–P7 fails | report the exact discrepancy; the corresponding statement is FALSIFIED as predicted, nothing is quietly adjusted |
| A negative control passes where it should fail | the check is vacuous; withdraw the dependent claim |
| Symbolic and numerical routes disagree | investigate before anything is reported |

## What this does NOT mean

1. Does NOT establish what McMurry p. 92 says for `m<0`; it shows what that
   definition must give for the coefficients to be `+√2`.
2. Does NOT cover the spinor (`j=1/2`) representation; that is the
   correspondent's announced next step.
3. Does NOT say which phase convention is "correct": the Condon–Shortley phase
   is a choice that the positive-`√2` form of the ladder equations encodes.
4. Does NOT touch the project's `G2/SU(3)/Spin(8)` or `N_gen=3` claims
   (unrelated substrate), and is not a reply to the correspondent: the
   workings are an input to a letter that is a separate, user-owned step.

## Fence

- `safe_for_runtime = False`. No bare `lambda` symbol is introduced.

## Amendments after the independent pass (2026-10-12)

The pre-registered rows above are left as written. A context-blind skeptic pass (FL step 8a: this file and
the code only) found that three of the predictions were stated more strongly than the evidence supports.
Corrected statements, which are the ones the decision relies on:

| # | As pre-registered | Corrected |
|---|---|---|
| P5 | "all coefficients `+√2` selects unit sphere normalisation **and** the phase `Y_{1,-1} = −Y*_{1,1}`" | `L±` is linear, so a **common** rescaling of all three functions leaves every coefficient at `+√2`. The condition selects **equal norms (any common scale)** and the phase. Check P5d added |
| P6 | "the identity `L± = Γ(T_23) ± iΓ(T_31)` holds in **both** bases ... no change of harmonic normalisation is *required*" | The **printed** `Γ'` give `M(L±)` only in basis `e` (and in any common rescaling of it, check P6l). In the sphere-normalised basis `Y'` they do **not** (negative control P6k); there they must be replaced by `DΓ'D⁻¹`. The identity for the conjugated matrices is just linearity (relabelled a restatement) |
| P7 | "`C' = −C`" | conditional on taking **both** ladder coefficients `+√2`; with `L₊Y_{1,-1} = √2 e^{iα} Y_{1,0}` the relation is `C' = −C e^{iα}` (check E6c) |

Other corrections: (i) the `r²` value arises from two different integrals (`∫(x/r)² dS` and `∫x² dΩ`),
so the script does not say which one anyone used (A6, A6b); (ii) Part F is independent of sympy's
differentiation and integration, **not** of the definitions and conventions, and the numerical cross-check
was extended from P1–P4 to the matrices of P6 (F4); (iii) the matrices of C205/C206 are now loaded from
their saved results and compared (G1–G3) instead of being only retyped; (iv) E7 now uses the relation from
E6 and derives the sign of `C` from positivity of `Y_{1,0}` at the pole; (v) checks that cannot fail on their
own (dimension arithmetic on typed monomials, two typings of one formula, the `r`-independence of operators
that contain no `∂_r`, linearity) are labelled `restatement` and not counted as evidence; (vi) "McMurry" is
used only for the operator definitions as reported in C201/C206 and is not claimed to have been re-checked
against the book.
