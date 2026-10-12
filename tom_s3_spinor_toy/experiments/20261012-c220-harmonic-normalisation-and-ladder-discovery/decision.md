# C220 Decision — the surface integral is 4πr⁴/3; the coefficient √2 is forced by the norm; the matrices are basis-dependent forms of one operator identity

**Date:** 2026-10-12
**Verdict:** **PROMOTE** (the seven pre-registered predictions P1–P7 hold; three of them had to be
restated more carefully after the independent pass, see the last section and `claim.md` "Amendments").
In `c220_harmonic_normalisation_and_ladder_discovery.py` (`run_output.txt`, `results_c220.json`):
`44/44` independent main checks pass, `5/5` negative controls behave as required, and `9` further
checks that follow from others (or compare two typings of one formula) hold but are **not counted** as
evidence. A numerical route that does not use sympy's differentiation or integration (scipy quadrature,
numpy finite differences) agrees; it is independent of the calculus, **not** of the definitions and
conventions. The matrices of C205/C206 are loaded from their saved results and compared.

Every number below is copied from `run_output.txt`. `[VERIFIED-sympy]` = exact symbolic;
`[VERIFIED-numeric]` = independent quadrature / finite differences.

## 0. Conventions used (fixed in `claim.md` before the run)

| Item | Definition |
|---|---|
| Sphere | `S²` of radius `r`; `x = r sinθ cosφ`, `y = r sinθ sinφ`, `z = r cosθ`; `dS = r² sinθ dθ dφ` |
| `L_z`, `L_±` (polar, McMurry p.144 as in C201/C206) | `L_z = −i ∂_φ`; `L₊ = e^{iφ}(∂_θ + i cotθ ∂_φ)`; `L₋ = e^{−iφ}(−∂_θ + i cotθ ∂_φ)` |
| Cartesian (C205/C206) | `L_x = i(z∂_y − y∂_z)`, `L_y = i(x∂_z − z∂_x)`, `L_z = i(y∂_x − x∂_y)`; `L_± = L_x ± iL_y` |
| Matrices | row = input: `operator(b_a) = Σ_b M[a][b] b_b` |
| Inner product | `⟨f,g⟩ = ∫ f* g dS` |

## 1. Real harmonics: `∫x*x dS` is proportional to `r⁴`, not `r²`

**Steps** [VERIFIED-sympy]. With `x² dS = r⁴ sin³θ cos²φ dθ dφ` (one `r²` from `x²`, one from `dS`):

```
identity (2):  d/dφ [ φ/2 + sinφ cosφ/2 ] = cos²φ            =>  ∫₀^{2π} cos²φ dφ = π ,  ∫₀^{2π} sin²φ dφ = 2π − π = π
identity (3):  d/dθ [ cos3θ/12 − 3cosθ/4 ] = sin³θ             =>  ∫₀^{π}  sin³θ dθ  = 4/3
               d/dθ [ −cos³θ/3 ]           = cos²θ sinθ        =>  ∫₀^{π}  cos²θ sinθ dθ = 2/3

∫ x² dS = r⁴ · (4/3) · π         = 4π r⁴/3
∫ y² dS = r⁴ · (4/3) · π         = 4π r⁴/3
∫ z² dS = r⁴ · (2/3) · 2π        = 4π r⁴/3
∫ xy dS ∝ ∫ sinφ cosφ dφ = 0 ,  ∫ xz dS ∝ ∫ cosφ dφ = 0 ,  ∫ yz dS ∝ ∫ sinφ dφ = 0
```

(Identity (3) was garbled in the PDF text extraction; it was read as `cos3θ/12 − 3cosθ/4`, and at that
reading it is correct.) A separate full double integration of all nine products gives the Gram matrix
`(4πr⁴/3)·I`. [VERIFIED-numeric] at `r = 2`: `∫x² dS = 67.0206432766 = 4π·2⁴/3`, `∫xy dS = −9e−16`.

**Where the `r²` value can come from.** Two different integrals both give `4πr²/3`:
route 1, `∫(x/r)² dS` (the integral of `x/r`, not of `x`); route 2, `∫x² dΩ` (the area element with the
`r²` of `dS` left out). This script shows that both give `r²`; it does **not** decide which of them any
particular calculation used.
**Dimension test** (an illustration, not independent evidence; the integral itself is established by the
step route, the full double integral and the quadrature): `x²` carries degree 2 in `r`, `dS` degree 2, so
`∫x² dS` must have degree 4. `4πr⁴/3` passes; `4πr²/3` does not.

**Normalised real harmonics** (P2): `x'ᵢ = √(3/(4π)) xᵢ/r² = ½√(3/π) xᵢ/r²`, and the Gram matrix of
`(x', y', z')` is exactly the identity. The same three functions need different constants depending on
what is being normalised:

| function | `∫f² dS` | normalising constant |
|---|---|---|
| `xᵢ` | `4πr⁴/3` | `√3/(2√π r²)` |
| `xᵢ/r` | `4πr²/3` | `√3/(2√π r)` |
| `xᵢ/r²` | `4π/3` | `√3/(2√π)` (independent of `r`) |

So `x'ᵢ = N xᵢ/r²` with `N = √(3/4π)` is the one for which the normalised function has no `r` left in its
norm, which is why it matches the "Y(θ,φ)/r" form of Section 2.

## 2. Complex harmonics, by the same method

**Raw functions** `p = x+iy`, `z`, `m = x−iy`; Gram matrix `⟨fₐ,f_b⟩` [VERIFIED-sympy]:

```
diag( 8πr⁴/3 ,  4πr⁴/3 ,  8πr⁴/3 ),   all off-diagonal entries 0
```

(`|x+iy|² = x²+y²`, hence the factor 2.) Squared norms are in the ratio **2 : 1 : 2**; confirmed
numerically at `r = 2` (33.5103, 16.7552, 33.5103). **This 2:1:2 is the whole difference between the
"raw" basis and a normalised one.**

**Normalised, with the Condon–Shortley phase** (P3):

```
Y'(1, 1) = −√(3/8π) (x+iy)/r²     = Y(1, 1)(θ,φ)/r ,  Y(1, 1) = −√(3/8π) sinθ e^{ iφ}
Y'(1, 0) = +√(3/4π)  z   /r²      = Y(1, 0)(θ,φ)/r ,  Y(1, 0) = +√(3/4π) cosθ
Y'(1,−1) = +√(3/8π) (x−iy)/r²     = Y(1,−1)(θ,φ)/r ,  Y(1,−1) = +√(3/8π) sinθ e^{−iφ}
```

Gram matrix of these three on `S²_r` is exactly the identity. **Positive control:** sympy's own
`Ynm(1,m,θ,φ)` reproduces all three `Y(1,m)` (an implementation that does not use this script's
definitions). Numerical Gram matrix at `r = 2` equals the identity to better than `1e-8`.

## 3. The ladder operators on the sphere-normalised harmonics

**Answer to the question "do we get exactly McMurry's equations?":** yes, the coefficient is `√2` in
all four non-trivial cases and `0` at the two ends, in polar **and** in Cartesian form, for every `r`.

### 3.1 Polar form, every step (`c = √(3/4π)`; `Y10 = c cosθ`, `Y11 = −(c/√2) sinθ e^{iφ}`, `Y1,−1 = (c/√2) sinθ e^{−iφ}`)

| action | `±∂_θ f` | `i cotθ ∂_φ f` | sum | × `e^{±iφ}` | result |
|---|---|---|---|---|---|
| `L₊Y(1,−1)` | `(c/√2) cosθ e^{−iφ}` | `(c/√2) cosθ e^{−iφ}` | `√2 c cosθ e^{−iφ}` | `√2 c cosθ` | `√2 Y(1,0)` |
| `L₊Y(1,0)` | `−c sinθ` | `0` | `−c sinθ` | `−c sinθ e^{iφ}` | `√2 Y(1,1)` |
| `L₊Y(1,1)` | `−(c/√2) cosθ e^{iφ}` | `+(c/√2) cosθ e^{iφ}` | `0` | `0` | `0` |
| `L₋Y(1,1)` | `+(c/√2) cosθ e^{iφ}` | `+(c/√2) cosθ e^{iφ}` | `√2 c cosθ e^{iφ}` | `√2 c cosθ` | `√2 Y(1,0)` |
| `L₋Y(1,0)` | `+c sinθ` | `0` | `c sinθ` | `c sinθ e^{−iφ}` | `√2 Y(1,−1)` |
| `L₋Y(1,−1)` | `−(c/√2) cosθ e^{−iφ}` | `+(c/√2) cosθ e^{−iφ}` | `0` | `0` | `0` |

(`±∂_θ` is `+∂_θ` for `L₊`, `−∂_θ` for `L₋`.) All six differences from the target are `0` exactly.

### 3.2 Cartesian form (functions written with `1/(x²+y²+z²)`, so no square roots)

`L_x f = i(z f_y − y f_z)`, `L_y f = i(x f_z − z f_x)`, `L_± = L_x ± iL_y`; write `ρ = x²+y²+z²`.

| action | `L_x f` | `L_y f` | `L_± f` | target |
|---|---|---|---|---|
| `L₊Y'(1,−1)` | `√6 z/(4√π ρ)` | `−i√6 z/(4√π ρ)` | `√6 z/(2√π ρ)` | `√2 Y'(1,0)` ✓ |
| `L₊Y'(1,0)` | `−i√3 y/(2√π ρ)` | `i√3 x/(2√π ρ)` | `−√3 (x+iy)/(2√π ρ)` | `√2 Y'(1,1)` ✓ |
| `L₊Y'(1,1)` | `√6 z/(4√π ρ)` | `i√6 z/(4√π ρ)` | `0` | `0` ✓ |
| `L₋Y'(1,1)` | `√6 z/(4√π ρ)` | `i√6 z/(4√π ρ)` | `√6 z/(2√π ρ)` | `√2 Y'(1,0)` ✓ |
| `L₋Y'(1,0)` | `−i√3 y/(2√π ρ)` | `i√3 x/(2√π ρ)` | `√3 (x−iy)/(2√π ρ)` | `√2 Y'(1,−1)` ✓ |
| `L₋Y'(1,−1)` | `√6 z/(4√π ρ)` | `−i√6 z/(4√π ρ)` | `0` | `0` ✓ |

`L_z` (Cartesian) has eigenvalue `m` on `Y'(1,m)`. [VERIFIED-numeric] by finite differences at six random
points on `S²_{r=2}`: `max |L_± Y' − √2 Y'| = 6.8e−12`.

### 3.3 `r` does not matter

None of the operators contains `∂_r` (they are tangent to the spheres), so `L(Y/r) = (LY)/r`; checked for
all six cases. The coefficients are the same for every `r > 0`.

### 3.4 The magnitude `√2` is forced by the norm

`⟨L₋Y,L₋Y⟩ = ⟨Y,L₊L₋Y⟩ = l(l+1) − m(m−1)`. Direct integration on `S²_r`:

```
∫|L₋Y'(1,1)|² dS = 2   ∫|L₋Y'(1,0)|² dS = 2   ∫|L₋Y'(1,−1)|² dS = 0
∫|L₊Y'(1,−1)|² dS = 2  ∫|L₊Y'(1,0)|² dS = 2   ∫|L₊Y'(1,1)|² dS = 0
```

So for harmonics of **equal norm** (any common scale, since `L` is linear) the coefficient has modulus
`√2`; a different modulus can only come from unequal norms in the set.

### 3.5 What a different normalisation or phase does (P5)

Replace `Y(1,−1)` by `κ·Y(1,−1)`: `L₋Y(1,0) = (√2/κ)·[κY(1,−1)]` and `L₊[κY(1,−1)] = κ√2·Y(1,0)`.

| κ | `L₋Y(1,0)` coeff. | `L₊Y(1,−1)` coeff. |
|---|---|---|
| 1 | `√2` | `√2` |
| −1 | `−√2` | `−√2` |
| 2 | `√2/2` | `2√2` |
| 1/2 | `2√2` | `√2/2` |
| √2 | `1` | `2` |
| 1/√2 | `2` | `1` |

This table is an illustration of the dependence only; it is **not** a claim about which normalisation
any particular text or calculation used. Two negative controls: dropping the Condon–Shortley sign of
`Y(1,1)` turns `L₊Y(1,0) = √2 Y(1,1)` into `−√2 Y(1,1)`; flipping the sign of `Y(1,−1)` turns
`L₋Y(1,0)` into `−√2` times it. So "all coefficients `+√2`" selects **equal norms (any common scale)** and the
phase `Y(1,−1) = −Y*(1,1)`; it does not select unit normalisation: the basis `(−e₁/√2, e₂, e₃/√2)`, with
Gram matrix `(4π/3)·I`, and `7·Y'` both give `√2, √2` (check P5d).

## 4. The matrices

Row = input. Three bases (all `1/r` factors dropped; they cancel). Gram matrices at the top.

| basis | Gram | `M(L₊)` | `M(L₋)` |
|---|---|---|---|
| `e = ((x+iy)/r, z/r, (x−iy)/r)` | `diag(8π/3, 4π/3, 8π/3)` | `[[0,0,0],[−1,0,0],[0,2,0]]` | `[[0,−2,0],[0,0,1],[0,0,0]]` |
| `u = ((x+iy)/(√2 r), z/r, (x−iy)/(√2 r))` (unitary, no CS phase) | `(4π/3)·I` | `[[0,0,0],[−√2,0,0],[0,√2,0]]` | `[[0,−√2,0],[0,0,√2],[0,0,0]]` |
| `Y' = (Y'(1,1), Y'(1,0), Y'(1,−1))` | `I` | `[[0,0,0],[√2,0,0],[0,√2,0]]` | `[[0,√2,0],[0,0,√2],[0,0,0]]` |

Basis `u` shows the effect of the phase alone: entries `−√2` and `+√2`. The Condon–Shortley sign is what
makes both `+√2`. `M(L_z) = diag(1,0,−1)` in all three.

**The generator matrices.** The correspondent's complex-basis matrices (his notes' equations 123–125, as
encoded and verified in C205 step 3, basis `e`) are

```
Γ'(T12) = diag(1,0,−1)    Γ'(T23) = [[0,−1,0],[−½,0,½],[0,1,0]]    Γ'(T31) = [[0,−i,0],[i/2,0,i/2],[0,−i,0]]
```

- In basis `e`: `M(L_z) = Γ'(T12)`, `M(L_x) = Γ'(T23)`, `M(L_y) = Γ'(T31)`, and therefore
  `M(L₊) = Γ'(T23) + iΓ'(T31)`, `M(L₋) = Γ'(T23) − iΓ'(T31)` exactly [VERIFIED-sympy]. This is the
  observation that the non-symmetric `(−1, 2)` forms are Γ'-combinations.
- Negative control: with `e₁` and `e₃` swapped, `M(L_x)` no longer equals `Γ'(T23)`.
- Passing to `Y'`: `Y'ₐ = Σ_b D[a][b] e_b` with `D ∝ diag(−1/√2, 1, 1/√2)`. Then
  `Γ'' = D Γ' D⁻¹`:

```
Γ''(T12) = diag(1,0,−1)
Γ''(T23) = (1/√2) [[0,1,0],[1,0,1],[0,1,0]]
Γ''(T31) = (i/√2) [[0,1,0],[−1,0,1],[0,−1,0]]
```

  and these equal `M_{Y'}(L_z), M_{Y'}(L_x), M_{Y'}(L_y)`. They are Hermitian (as they must be in an
  orthonormal basis); the `e`-basis matrices are not.
- **The printed `Γ'` work only in basis `e`.** The equality `M(L±) = Γ'(T23) ± iΓ'(T31)` with the
  *printed* matrices holds in basis `e` and in any **common** rescaling of it (`7·e`: check P6l). In the
  sphere-normalised basis `Y'` it fails: `Γ'(T23) + iΓ'(T31)` is `[[0,0,0],[−1,0,0],[0,2,0]]`, while
  `M_{Y'}(L₊)` is `[[0,0,0],[√2,0,0],[0,√2,0]]` (negative control P6k). In `Y'` the correct matrices
  are the conjugated `Γ'' = DΓ'D⁻¹` above, and for those the identity is just linearity (it follows
  from the previous bullet). So: **if the printed `Γ'` are to be kept, the harmonics must be the
  equal-weight set `(x+iy, z, x−iy)` (squared norms 2:1:2), not the sphere-normalised set; if the
  sphere-normalised set is wanted, the `Γ` matrices must be replaced by `DΓ'D⁻¹`.** The `√2, √2`
  symmetric forms are exactly `M_{Y'}(L±)`. The matrices of the saved C205/C206 results reproduce
  exactly (checks G1–G3), and a numerical computation in both bases agrees to `6e−12` (F4).

## 5. "Discovering" the harmonics from the ladder operators

1. **`L_z` eigenfunctions.** `−i F'(φ) = m F(φ)` ⇒ `F = C e^{imφ}` (sympy `dsolve`). Single-valuedness
   forces integer `m`; for `l = 1`, `m ∈ {−1,0,1}`. So `ψ = g(r) χ_m(θ) e^{imφ}`.
2. **Highest weight.** `L₊[χ(θ)e^{iφ}] = e^{2iφ}(χ' − cotθ χ) = 0` ⇒ `χ = C sinθ`.
3. **Lowest weight.** `L₋[χ(θ)e^{−iφ}] = e^{−2iφ}(cotθ χ − χ') = 0` ⇒ `χ = C' sinθ`.
   **Negative controls:** the wrong annihilation conditions `L₋[χe^{iφ}] = 0` and `L₊[χe^{−iφ}] = 0` give
   `χ = C/sinθ`, and `∫dθ/sinθ` diverges at both poles, so this is not normalisable and is rejected.
4. **Normalisation** with `g(r) = 1/r`: `∫|C sinθ e^{iφ}|² dΩ = 8π|C|²/3 = 1` ⇒ `|C| = |C'| = √(3/8π)`.
5. **`Y(1,0)` two ways.** `L₋(C sinθ e^{iφ}) = −2C cosθ` and `L₊(C' sinθ e^{−iφ}) = 2C' cosθ`.
   `‖L₋Y11‖² = 2` (Section 3.4), so the normalised `Y(1,0)` is `L₋Y11/√2 = −√2 C cosθ`; route 2 gives
   `√2 C' cosθ`. **Taking both ladder coefficients to be `+√2`, the two routes agree only if
   `C' = −C`.** The condition is conditional on that convention: if instead
   `L₊Y(1,−1) = √2 e^{iα} Y(1,0)`, the relation is `C' = −C e^{iα}` (check E6c).
6. **What remains a convention.** One overall phase per multiplet, and the choice that the ladder
   coefficients are real and positive. Requiring `Y(1,0) > 0` at `θ = 0` (the sign is computed: `C = +|C|`
   gives `−√3/(2√π)`, `C = −|C|` gives `+√3/(2√π)`) gives `C = −√(3/8π)`, and `C'` is then taken from the
   relation of step 5, and then `Y(1,1) = −√(3/8π) sinθ e^{iφ}`, `Y(1,0) = √(3/4π) cosθ`,
   `Y(1,−1) = +√(3/8π) sinθ e^{−iφ}`, identical to Section 2 and to sympy's `Ynm`.

## 6. Pre-registered predictions

| # | Prediction | Result |
|---|---|---|
| P1 | `∫x² dS = 4πr⁴/3`; mixed vanish; `r²` value belongs to `x/r`; fails dimension test | **holds** |
| P2 | `x'ᵢ = √(3/4π) xᵢ/r² = ½√(3/π) xᵢ/r²`; Gram = I | **holds** |
| P3 | raw norms `8π,4π,8π · r⁴/3`, orthogonal; normalised CS harmonics; polar form `Y/r`; = sympy `Ynm` | **holds** |
| P4 | `L_±Y' = √2 Y'` (0 at ends), polar and Cartesian, any `r`; `∫|L₋Y'|² = 2` | **holds** |
| P5 | `κ`-dependence `√2/κ`, `κ√2`; CS sign flips the coefficient sign; (restated) positive `√2` selects equal norms, not unit norm | **holds** as restated |
| P6 | basis `e`: `(−1,2)` forms `= Γ'(T23) ± iΓ'(T31)`; basis `Y'`: `√2,√2`; `DΓ'D⁻¹` Hermitian | **holds**; the original wording "identity holds in both bases" was wrong for the *printed* `Γ'` and is restated in Section 4 |
| P7 | discovery route; `C' = −C`; non-normalisable negative control | **holds**, with `C' = −C` conditional on the `+√2` convention |

## 7. What this does not show

1. **What McMurry p.92 says for `m < 0`.** This project has not seen that page. C201 took `Y(1,−1)` from
   the standard relation `Y_{l,−m} = (−1)^m Y*_{l,m}`. This round shows the result is *forced*: given
   `Y(1,0)` and requiring `L₋Y(1,0) = +√2·Y(1,−1)`, one gets `Y(1,−1) = +√(3/8π) sinθ e^{−iφ}`, which is the
   standard-relation value. Whether the book's printed definition agrees is unverified.
2. **Known imprecision in C201 (not edited here).** C201's `decision.md` says it used "ONLY McMurry's own
   stated definitions"; for `m < 0` it used the standard relation instead (comment at
   `c201_l1_ladder_intertwiner.py:40-43`), and the ledger entry for C201 carries a similar phrase.
3. **How anyone else's numbers arose.** The `κ` table is a statement about the dependence of the
   coefficients on the normalisation, not about any particular calculation.
4. **The spinor (`j = 1/2`) representation.** Not covered; the announced next step.
5. **The Condon–Shortley phase is a choice.** It is the choice for which every ladder coefficient is `+√2`.
6. The correspondent's `Γ'` matrices are the ones encoded in C205 (his notes' equations 123–125 as
   transcribed there). They are now tied to C205's saved results by computation (check G3: `z · M_saved ·
   z⁻¹` with `z` defined by basis `e`), but their definition in his notes was not re-read for this round.
7. The operator definitions `L_z, L_±` (polar) are those used in C201/C206 and attributed there to
   McMurry p.144; they are not re-checked against the book here. The Cartesian ones satisfy
   `[L_x,L_y] = iL_z` and `L₊` raises `m` by 1 (verified by the skeptic by hand).
8. Part F is independent of sympy's differentiation and integration but retypes the definitions, so it
   catches a calculus error, not a convention error.

## Skeptic concerns (FL step 8a, claim.md + code only)

Independent pass: a skeptic agent given only `claim.md`, the script and its output (no reasoning
chain). It verified by hand the integral, the norms, all twelve ladder results, the Cartesian
commutation relation, the basis-`e` matrices, `DMD⁻¹`, and every step of Part E. It could not run the
script, could not see the correspondent's PDF, and did not check McMurry p.92 or p.144. Its findings, each
checked against the output before acting:

| # | Severity | Concern | Response |
|---|---|---|---|
| 1 | MUST-FIX | P5: "`+√2` selects unit normalisation" is false (`L` is linear) | **Fixed**: restated as equal norms; check P5d |
| 2 | MUST-FIX | P6: printed `Γ'` do **not** give `M(L±)` in `Y'`; P6e/P6i cannot fail | **Fixed**: confirmed by hand (`(G23+iG31)[1][0] = −1` vs `√2`); negative control P6k, check P6l; P6e/P6i relabelled restatements; Section 4 rewritten |
| 3 | SHOULD | the `r²` value has two routes; the script cannot say which was used | **Fixed**: A6, A6b; wording |
| 4 | SHOULD | `C' = −C` is conditional on the `+√2` convention | **Fixed**: E6 relabelled, E6c |
| 5 | SHOULD | E7 did not use E6; sign of `C` set by hand | **Fixed**: `C'` from E6, sign computed |
| 6 | SHOULD | nothing loaded from C201/C205/C206 results | **Fixed**: G1–G3. C205's JSON stores the real-basis matrices, not the complex-basis `Γ'`, so `Γ'` is tied through `z · M_saved · z⁻¹` (G3) |
| 7 | SHOULD | Part F is independent of sympy calculus, not of definitions; covered P1–P4 only | **Fixed**: wording; extended to the matrices (F4) |
| 8 | SHOULD | "McMurry harmonics" overstates the source | **Fixed**: relabelled |
| 9 | NIT | several checks cannot fail on their own | **Fixed**: nine labelled `restatement`, excluded from the count |
| 10 | NIT | structural `!=` used for a negative direction | **Fixed**: `not zero(...)` |

No concern was dismissed. Remaining, unverified: McMurry pp.92 and 144; the correspondent's own
definition of `Γ'`.
