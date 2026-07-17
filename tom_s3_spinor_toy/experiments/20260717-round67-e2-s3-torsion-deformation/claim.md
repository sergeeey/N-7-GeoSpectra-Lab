# E2 — Claim: torsion-deformed S³ Dirac operator, does ker(D_S3(t)) ever leave zero?

## Stakes
Internal-only for now (a candidate-mechanism note feeding the open KT-8 gap). Would become
external-facing only if promoted into `preprint.tex` — not done here.

## Question type
[x] descriptive  [ ] predictive  [ ] causal

Descriptive: for the one-parameter family of metric connections ∇^t on S³ = SU(2) (naturally
reductive, G/H with G=SU(2), H={e}), does the associated Dirac operator D^t ever have a
non-trivial kernel, and at which t?

## Background (established, not re-derived here)
- KT-8 (`experiments/20260615-g8-chirality-obstruction/`, `reports/PROJECT_360_ROUND3_SYNTHESIS.md`
  §"KT-8"): the full product Dirac operator on S³×S⁶ has **no** zero mode under the standard
  construction (twist only on S⁶, S³ round/Levi-Civita), because `D_full² = D_S3²⊗1 + 1⊗D_S6,twisted²`
  (exact Clifford-algebra identity, [VERIFIED-tool] + [VERIFIED-external-source, Sire & Xu
  arXiv:2005.01448]) and S³'s own Levi-Civita spectrum ±(n+3/2)/ρ₃ (n≥0) never reaches 0.
- This experiment asks whether replacing S³'s Levi-Civita connection with a **torsion-deformed**
  connection from the standard naturally-reductive one-parameter family closes that gap.

## Claim (falsifiable)
Using Agricola's one-parameter family of connections on naturally reductive spaces
(Agricola, arXiv:math/0202094, "Connections on naturally reductive spaces, their Dirac operator
and homogeneous models in string theory" — PDF present in this repo, read directly this session,
`Agricola_2002_Dirac_naturally_reductive.pdf`), realizing S³ = SU(2)/{e} (G=SU(2), H trivial,
**not** the symmetric-space presentation (SU(2)×SU(2))/SU(2)_diag, which gives zero deformation
freedom since torsion there is identically forced to vanish — see caveats):

**ker(D_S3(t)) ≠ 0 for infinitely many explicit, exactly-computable values of t**, specifically
t = 1/2 − σ(n+3/2)/h_H for every n≥0 and σ=±1, where h_H=±3 is a single calibrated constant.
For n=0,1,2 (the levels this experiment computes explicitly): t ∈ {−2/3, −1/3, 0, 1, 4/3, 5/3}.

## Method
1. Build Cl(3) explicitly (Pauli matrices), verify Clifford relations exactly (sympy, symbolic).
2. Compute Kostant's cubic element H (Agricola eq. 5) for n=dim(m)=3: since there is only ONE
   Clifford triple (Z1,Z2,Z3) for n=3, H reduces to a multiple of Cl(3)'s volume element
   ω=Z1·Z2·Z3. Verify ω is *exactly* a scalar multiple of the 2×2 identity (central, ω²=1) —
   this is the crux structural fact and is specific to n=3 (does NOT hold for higher-dimensional
   cosets like S⁶, where H has multiple non-central terms).
3. Since H = h_H·Id (a pure scalar operator on the spinor factor, with zero dependence on which
   Peter-Weyl / KK level the spinor lives in — H is purely algebraic, no orbital/differential
   part at all), Agricola's eq. (5) `D^t ψ = Σ Z_i·Z_i(ψ) + t·H·ψ` forces
   **D^t = D^{1/2} + (t−1/2)·h_H** as an *exact* operator identity — every eigenvalue of the
   known Levi-Civita operator D^{1/2} shifts by the *same* additive constant (t−1/2)·h_H,
   regardless of n or sign.
4. Calibrate h_H using Agricola's own Theorem 4.2 (constant/j=0 spinors: D^tψ = t·H·ψ exactly,
   since the orbital term vanishes for constant ψ) matched against this project's own
   already-established [VERIFIED-sympy, G8/G4] n=0 eigenvalue 3/2: h_H/2 = 3/2 ⟹ h_H = 3
   (up to an overall sign choice/orientation convention, which only swaps t↔1−t).
5. Build the closed-form family D^t(n,σ) = σ(n+3/2) + (t−1/2)·h_H for n=0,1,2, σ=±1, solve for
   the exact zero-crossing t in each case (sympy), and independently cross-check against a dense
   numeric grid scan (not reusing the symbolic solver).

## Kill criterion
If ω were **not** a scalar multiple of the identity (i.e. if it had off-diagonal structure or
unequal diagonal entries), the whole "uniform additive shift" argument would collapse and a
much harder n-dependent matrix diagonalization would be required — this would most likely still
allow *some* crossing to exist (generic 1-parameter perturbation of a discrete spectrum almost
always crosses zero somewhere) but the clean closed form claimed above would be **falsified** as
stated. Kill signal: `step2_omega_ok == False` in `results_e2.json`.
Also: if the numeric grid scan disagreed with the symbolic crossing values by more than
floating-point tolerance, that would falsify the closed-form derivation (arithmetic error) —
kill signal: `verdict.numeric_exact_cross_check_passed == False`.

## Assumptions (status)
| Assumption | Status |
|---|---|
| Agricola eq. (5), Theorem 4.2 | [VERIFIED-external-source] — read directly from the PDF this session |
| Cl(3) Clifford relations, ω scalar & central | [VERIFIED-tool] — sympy, exact, this script |
| S3's Levi-Civita spectrum ±(n+3/2)/ρ₃ | [VERIFIED-sympy] — already established, G8/G4, not re-derived |
| "j=0 constant-spinor sector = n=0, one sign, of the known ladder" | [INFERRED] — justified by multiplicity match (dim 2 = (0+1)(0+2)), not independently cross-checked against a second source |
| Uniform shift applies to n=1,2 (not just n=0) | [DEDUCTION, low-risk] — direct consequence of H being a scalar *matrix* (step 2), not an extrapolation from representation theory |
| Product-decoupling formula `D_full² = D_S6,twisted²⊗1 + 1⊗D_S3(t)²` remains valid once S³'s factor is torsion-deformed (not Levi-Civita) | **[INFERRED, NOT independently literature-verified for this generalized case]** — KT-8's own literature citation (Sire & Xu) only covers Levi-Civita-on-both-factors; the generalization to an arbitrary per-factor metric connection is a natural but unverified extension of the same Clifford-algebra cross-term-cancellation argument |
| t ranges over all of ℝ with no restriction | [VERIFIED-external-source] — Agricola: Λ^t_m(X)Y=t[X,Y]_m is skew-symmetric (hence ∇^t a valid metric connection) for *every* real t on a naturally reductive space; no positivity or other constraint restricts t |

## What this does NOT mean
1. Does **not** by itself resolve KT-8. This experiment only establishes ker(D_S3(t))≠0 for the
   **S³ factor alone**; it does not compute the full 9D product operator's kernel under a
   torsion-deformed S³ factor, and the product-decoupling formula needed to combine this with
   the S⁶ twist's own zero mode is [INFERRED], not independently verified for this generalized
   (torsion-on-one-factor) case.
2. Does **not** provide any physical motivation for why nature (or this project's own
   compactification ansatz) would select t=0, t=1, or any of the other crossing values instead
   of t=1/2 (Levi-Civita). Finding "some t works" is a different, and much weaker, claim than
   "there is a principled reason to pick this t" — the same FITTED-vs-DERIVED distinction this
   project's own methodology flags elsewhere (e.g. the G56/λ=0.30 lesson). This is a genuinely
   open follow-up question if this candidate mechanism is pursued further.
3. Does **not** claim the symmetric-space presentation S³=(SU(2)×SU(2))/SU(2)_diag gives the
   same freedom — that presentation is a symmetric space, and Agricola's paper states explicitly
   that for symmetric spaces "all connections of this one-parameter family coincide" (torsion
   ≡ 0 identically, since [m,m]⊂h there) — i.e. **no deformation freedom exists** under that
   presentation. The freedom used here comes specifically from realizing S³ as G/{e} (the full
   Lie group with H trivial), where [m,m]=g≠0.
4. Does **not** verify that a torsion connection on S³ is compatible with the rest of this
   project's established compactification structure (metric on S³ itself is unchanged — only
   the connection/spin-connection changes — but whether this integrates consistently with the
   S⁶ side, the NCG spectral-triple construction (G18+), or the Freund-Rubin flux setup used
   elsewhere in the preprint is not examined here).

## Check
`python e2_s3_torsion_deformation.py` → `verdict.label == "PASS_CANDIDATE_MECHANISM_FOUND"`,
`verdict.clifford_and_omega_verified == true`, `verdict.numeric_exact_cross_check_passed == true`.
