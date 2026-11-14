# C218 — Claim: an explicit real structure J on round59's Σ, and its su(3)-equivariance, checked directly

**Date:** 2026-10-03
**FL tier:** [x] Full (research claim touching OB11(ii) / C149 prerequisite)
**Question type:** [x] descriptive (does a specific, explicitly constructed operator have a specific algebraic property — no causal or predictive content)

---

## Why this round exists (read first)

`C149` (2026-09-04) named a prerequisite for OB11(ii)'s never-run transport step
(transport `D`, `J`, `γ` through `U`): *"`J` is not constructed in round59's own file; its
su(3)-equivariance must be checked separately."* `C193` (2026-09-09) then argued the
`su(3)`-equivariance of `J` is automatic once `J` is built — **but its `J` was the
nearly-Kähler almost-complex structure (a real `6×6` matrix on `m`), not the object OB11(ii)
names.** Evidence that OB11(ii)'s `J` is the NCG **real structure** (antiunitary), not the
almost-complex structure: (a) the triple `D, J, γ` is the data of a real even spectral triple;
(b) the project's own usage of `J_F` as the finite triple's real structure (OB10: "`J_F²`
stated as −1, actually +1"); (c) `PARENT_ACTION_GATE.md:946` lists "Real structure `J` — Not
checked" as a separate row from the nearly-Kähler `J` (line 204). `[INFERRED]`, high
confidence, not stated verbatim in any file read. **So C193's corollary did not address
OB11(ii)'s `J`.** This round builds the right object explicitly, and (as a secondary,
clearly separated check) also builds the nearly-Kähler `J` that C193 only argued for.

## Prior Result Gate

1. Exact claim: an explicit antiunitary `J = B∘K` on round59's 8-dim `Σ = Λ•L'` exists with
   `J E_k J⁻¹ = ε E_k` (k=1..6), and commutes with `RHO[a] = spin_lift(ADNU[a], E)` for all
   `a = 1..8`.
2. `decision.md` grep (real structure / charge conjugation): hits reviewed — OB10
   (`20260806-ob10-c27-majorana-halving`, reality type of the 9-dim geometric bundle under
   Cl(0,9)), the C11 chain (`20260810-c11-step5-real-structure`, `…-w1-nonfactorizing-J`,
   finite-toy / coexisting-D context), `20260809-ob2-antiunitary-correction`. None builds
   `B` on round59's 8-dim `Σ` and tests it against `RHO`.
3. `round59*` scripts: `Ec = build_clifford(conj=True)` is used only as a convention-robustness
   check of the kernel certificate (script lines ~388-396), never as a real structure.
4. `null_results/INDEX.md`, `parked/INDEX.md`: 0 hits for "real structure".
5. Pickaxe/primary source: not run; the construction is elementary linear algebra, no external
   formula is imported.
6. **Status:** [x] NEW.

## Estimand

**Population:** round59's spinor module `Σ = Λ•L'` (dim 8, exact `sympy` entries), Clifford
generators `E[1..6]` and `Ec[1..6]` (`build_clifford(conj=False/True)`), su(3) generators
`RHO[a] = spin_lift(ADNU[a], E)`.
**Intervention:** solve the linear system `B·Ec[k] = ε·E[k]·B` (k=1..6) for `ε = ±1`; set
`J = B∘K` (`K` = entrywise complex conjugation in round59's basis).
**Comparator:** a negative control operator that must fail the same check (below).
**Endpoint:** (i) `dim` of the solution space per `ε`; (ii) `J²` and the (anti)commutation of
`J` with the chirality grading `γ` (EVEN/ODD split); (iii) `max_a ‖J·RHO[a]·J⁻¹ − RHO[a]‖`.
**Summary measure:** exact `sympy` zero / residual magnitude.
**MCID:** any nonzero exact residual on a real-coefficient `spin_lift` element is a failure.

## Falsifiable claims (pre-registered before running)

- **P1 (existence + uniqueness).** For each sign `ε ∈ {+1, −1}` the solution space of
  `B·Ec[k] = ε·E[k]·B` (k=1..6) is exactly **1-dimensional** (Schur: `E` is irreducible on ℂ⁸).
- **P2 (KO-6 signature).** After normalizing `B` to be unitary, at least one of the two
  solutions has the KO-dimension-6 pattern `J² = +1`, `Jγ = −γJ` (project convention, OB10:
  `J_F² = +1`). I report both solutions' `J²` and (anti)commutation with `γ`.
- **P3 (equivariance, direct).** `J·RHO[a]·J⁻¹ = RHO[a]` exactly for all `a = 1..8` and for
  both `ε`. **Predicted reason (stated now, so a pass is not a surprise):** forced by structure —
  `RHO[a]` is a *real*-coefficient combination of products `E_iE_j`, and `J` maps `E_i ↦ ε E_i`,
  so `J(E_iE_j)J⁻¹ = ε²E_iE_j`. The check therefore does not probe su(3) specifically and is
  not substantive evidence about the `su(3)` embedding — same status as C149's own finding for
  `γ`. Stated up front, not discovered afterwards.
- **P4 (the check can fail — negative control).** `T = i·RHO[1]` (a *complex*-coefficient
  element, i.e. `RHO[1]` times `i`) gives `J T J⁻¹ = −T`, so the residual is `2‖T‖`, order 1,
  not zero. A random unitary `B'` in place of `B` also fails `J'E_kJ'⁻¹ = ±E_k`.
- **P5 (secondary, separate object — the nearly-Kähler `J` C193 argued for).** The commutant of
  `{terms_to_matrix(ADNU[a])}` in the real `6×6` matrices has dimension **exactly 2**
  (`R⁶ = ℝ`-realification of `3` of SU(3): commutant ≅ ℂ), containing an antisymmetric `J_NK`
  with `J_NK² = −1`, unique up to sign; and `[spin_lift(J_NK), RHO[a]] = 0` holds directly
  (not via C193's identity). This part does **not** bear on OB11(ii) if `J` there is the real
  structure; it is included to repair C193's loose end and is reported separately.

## Kill criterion

**REJECTED** if any of: (a) no nonzero `B` exists for both `ε` (a real structure cannot be
built on round59's `Σ` in this basis — a significant finding); (b) a solution space has
dimension ≠ 1; (c) `J` fails to commute with `RHO[a]` for any `a` (this would indicate a bug in
`build_clifford(conj=True)` or a non-real coefficient in `ADNU` — both contradict P3's
predicted mechanism); (d) the negative control P4 passes (the check could not fail); (e) P5's
commutant dimension ≠ 2.

## What this result would NOT mean

1. It does **not** run OB11(ii)'s transport step or show `U`-transport of `J` is Clifford- or
   Hermiticity-compatible; it only builds `J` and checks the prerequisite C149 named.
2. It does **not** change `N_gen=3`'s CONDITIONAL status, nor OB1/H1c, nor any registered value.
3. P3's pass is structural (forced), so it is **not** evidence that round59's `ADNU` realizes
   su(3) correctly — that is established elsewhere (G96, C70).
4. It does **not** show `J` on round59's `Σ` is *the* real structure of the physical `H_matter`
   (G18's 32-dim finite triple); only that the S⁶-spinor-module real structure exists, is explicit,
   and commutes with `RHO`.

## Reproduction

```
cd experiments/20261003-c218-ob11ii-real-structure-j-explicit
python c218_real_structure_j.py
```

---

## Post-skeptic annotations (2026-10-03; original text above unedited)

- Wording: where this file says Ec[k] / "conj(E)", run_output.txt confirms build_clifford(conj=True) equals the entrywise complex conjugate of E; the solved equation is B*conj(E_k) = eps*E_k*B.
- P1/P2 are reproductions of standard facts (Schur; KO-6 sign pattern), not discoveries.
- P3 and P5c were pre-declared FORCED; skeptic tool-checked they hold for any real ADNU / any scale of spin_lift. Treat as arithmetic consistency, not evidence.
- P4a is the antilinearity identity (equals equivariance of exp(i theta T) in the Hermitian convention); P4c (random anti-Hermitian 8x8) added as a genuine failing control.
- J_NK = SU(3)-invariant complex structure, unique up to sign; nearly-Kahler identification is by theory, (nabla_X J)X=0 and sign untested. eps' and J(x)J untested. See decision.md.
