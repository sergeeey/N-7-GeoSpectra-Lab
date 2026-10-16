# C144 — Decision

## Structural argument (derived directly from Landweber's own equations)

Kostant's operator (Landweber eq. `kostantdirac`): `Ð := Σᵢ Xᵢ⊗Xᵢ* + 1⊗v`, acting
on `V_λ⊗𝕊`. Restricted to `λ=0` (trivial G-representation — exactly round59's
setup: `ψ± = 1±y123 ∈ Σ` alone, no `V_λ` tensor factor), the `r(Xᵢ)`-type term is
IDENTICALLY ZERO — differentiating a constant function is zero regardless of any
connection choice, this needs no geometric input at all. So:

```
Ð|_{V_0} = c(v)   exactly — a PURE algebraic Clifford-cubic operator.
```

This is the first result of this round, and it required nothing beyond reading
Landweber's own eq. (13)/(kostantdirac) — no computation needed.

**The actual open question was therefore:** does round59's `D` (built from the
Levi-Civita connection, which is generically DIFFERENT from the canonical/torsion
connection implicit in Kostant's own construction, since G2/SU(3) is a
non-symmetric, torsion-carrying 3-symmetric nearly-Kähler space) equal `c(v)` —
even though the two are, a priori, Dirac operators for two different connections?

## Computation (symbolic, exact, SymPy — `c144_kostant_vs_round59.py`)

1. Reproduced round59's own Clifford algebra (`E[i]`, AHL2023 eq. 5) and Levi-Civita
   Nomizu operators (`NAB[i]`, AHL2023 Remark 5.2 `Lam` table) **verbatim** — same
   code, so this is not a re-transcription that could introduce a NEW error, it
   reuses round59's already-certified construction directly.
2. Recalibrated against Theorem 5.1 (Killing equation) and the untwisted Dirac
   eigenvalue (`D ψ+ = −√3 ψ+`) — both PASSED, confirming byte-identical behavior
   to the original round59 script.
3. Extracted structure constants `C[i,j,k]` from the RAW (unscaled ±1) `Lam[i]`
   coefficients, interpreting them as `⟨eᵢ,[eⱼ,eₖ]⟩` in the SAME orthonormal frame
   `{eᵢ}` already used for the Clifford algebra (i.e. the SAME `⟨,⟩` throughout —
   no separate normalization was assumed).
4. **Verified total antisymmetry** of `C[i,j,k]` in all three indices (not assumed
   — checked on all 216 index triples): `True`. This confirms the `m`-restricted
   bracket of `g2` really is a genuine 3-form (the geometric hallmark of a
   nearly-Kähler / 3-symmetric space), independent of any assumption about Kostant.
5. Quantized `ω = Σ_{i<j<k} C[i,j,k]·eᵢ·eⱼ·eₖ` via the Chevalley map (exact for
   distinct indices — no lower-order Clifford correction terms needed).
6. **Result: `D == (√3/4) · c(ω)` exactly on all 64 matrix entries** (symbolic
   equality, not a numerical near-match) — confirmed by direct residual check
   `D − (√3/4)c(ω) == 0` (all 64 entries), not merely a first-entry-ratio guess.
7. Cross-check: `c(ω) ψ+ = −4 ψ+` (exact eigenvector), so
   `D² ψ+ = (√3/4)²·16·ψ+ = 3·ψ+`, matching round59's own independently-verified
   `D²=3` (Friedrich-bound saturation, already in round59's Step 2) — internally
   self-consistent.

## Verdict

**PROMOTE, qualified — narrowed after skeptic pass (see below).** Round59's
untwisted Dirac operator is symbolically, exactly proportional to Kostant's
algebraic cubic term (`D = (√3/4)c(ω)`, all 64 matrix entries, no free-fit
component). **Post-skeptic correction:** this specific numeric check is a
consequence of AHL2023's data being a genuine naturally-reductive Nomizu table
(a fact already established, more discriminatingly, by round59's own Step-1
Killing-spinor calibration) — it is not new, independent, G2/SU(3)-specific
evidence in itself. What the round DOES establish, robustly: **Kostant's
algebraic framework (and, by extension, Landweber/Slebarski's twisted
generalization) genuinely applies to this project's Dirac-operator family** —
this is a real, previously-unconnected, citable fact, even though the specific
STEP-4 numeric match that first revealed it turned out to be less discriminating
than initially framed.

**Why this is not surprising in hindsight, but was not obvious in advance:**
`Σᵢ eᵢ·ρ(ad(eᵢ)|_m)` (a sum of degree-1 times degree-2 Clifford elements — i.e. the
literal shape of round59's `D`) is a standard way to build a cubic Clifford element
from totally-antisymmetric structure constants, and reduces to a scalar multiple of
the pure Chevalley-quantized 3-form exactly when that antisymmetry holds (step 4
above). What was NOT obvious in advance: (a) whether AHL2023's `Lam` table, built
for a completely different purpose (calibrating the Levi-Civita Killing-spinor
equation, Theorem 5.1), would even BE totally antisymmetric — that is a real,
falsifiable geometric fact about this specific 3-symmetric space, not a tautology;
(b) whether the resulting scalar would come out clean (it did: `√3/4`, not some
uglier irrational ratio, which is itself a mild positive signal that the
identification is the "right" one and not an artifact).

**Qualification (why not unconditional PROMOTE):** the antisymmetry check in step 4
used ONLY the `m`-restricted data (`Lam`), not an independently-sourced g2
structure-constant table — so this is a **within-AHL2023-convention** consistency
check, not a check against a second, wholly independent primary source for g2's
structure constants. This is the same caveat C143 itself already carried for its
`m`-type scalars (established by direct computation within this project's own
convention, not by an external general theorem) — except HERE the direct
computation now connects to an external, independently-published general theorem
(Kostant 1999), which is a strictly stronger footing than C143 had for the same
family of claims.

## Skeptic pass (Step 8a, context-blind: claim.md + script only, no reasoning chain)

**Verdict: WEAKENED.** Ran independently (own read of `claim.md` + the script; the
"verbatim reproduction" claim was diffed line-by-line against the original round59
script and confirmed faithful). No fatal concern found — the symbolic identity
`D == (√3/4)c(ω)` itself is real and correctly computed.

**The decisive finding of the skeptic pass:** the STEP 4 proportionality check is
**algebraically forced**, not independent evidence. Derivation (independently
re-verified by me, not just accepted): since `C[i,j,k]` is totally antisymmetric
(STEP 2) and no `Lam[i]` entry has `i∈{a,b}`, the sum
`Σᵢ Σ_{(c,a,b)∈Lam[i]} c·Eᵢ·E_a·E_b` collapses via a standard Clifford-algebra fact
(a totally antisymmetric 3-index contraction against a totally-antisymmetric-under-
permutation triple product hits each unordered triple exactly 6 times with identical
sign) to exactly `3·c(ω)` — giving `D = (1/(4√3))·3·c(ω) = (√3/4)c(ω)` as a forced
algebraic consequence of STEP 2 passing, not a delicate coincidence STEP 4
independently discovers. The skeptic also showed (Test A, symbolic) that a
coherent, antisymmetry-preserving sign perturbation of the WHOLE `Lam` table still
produces `D == (√3/4)c(ω)` — even though such a perturbation would BREAK the
Killing-spinor calibration in STEP 1. This means **STEP 1 (Killing-spinor
calibration) is the real, discriminating, geometry-specific test; STEP 4 tests only
"is this internally a genuine naturally-reductive Nomizu table," which is a more
generic, already-implied fact.**

Further: total antisymmetry of the `m`-restricted bracket is ITSELF a generic
consequence of building a naturally reductive metric from any Ad-invariant form
(standard fact, re-derived independently here, not just accepted from the skeptic:
for `X,Y,Z∈m⊂g` with `h⊥m` under an Ad-invariant `⟨,⟩`, `⟨[X,Y]_m,Z⟩=⟨[X,Y],Z⟩=
⟨X,[Y,Z]⟩=⟨X,[Y,Z]_m⟩`, giving total antisymmetry directly) — so it is not a
G2/SU(3)-specific surprise either.

### Response Matrix (per FL Step 8a)

| Concern | Skeptic severity | Response |
|---|---|---|
| STEP 4 proportionality algebraically forced by STEP 2 + no-diagonal-Lam, not independent evidence | scope (weakens, does not falsify) | **Accepted, documented.** claim.md caveat 5 added; script docstring corrected; framing throughout downgraded from "confirms round59's operator IS Kostant's" to "confirms Kostant/Slebarski's framework genuinely applies here — the general algebraic identity holds, discriminating power sits in STEP 1's Killing-spinor calibration, already independently verified in round59 itself." |
| "raw Lam = structure constants" wording elides a `-1/2` factor | wording only | **Fixed.** Script docstring now states the exact `-(1/2)` relation; claim/decision reworded to "proportional to" throughout, not "equals." |
| Kill-check tests `PSI_P` only, not `PSI_M` | minor, non-fatal (same `NAB`, redundant) | **Dismissed** — no independent information lost; `PSI_M` calibration is identical in structure and already covered by round59's own original script. |
| Verbatim-reproduction faithfulness | none found (pass) | No action. |

**True kill condition (per FL): NOT met.** The core predicate — round59's D is
proportional to Kostant's algebraic cubic term — survives, symbolically exact. What
was corrected is the INTERPRETIVE claim about how much that fact, by itself,
demonstrates. Final verdict below reflects the corrected, narrower framing.

## What remains open (explicitly, not silently deferred)

1. **Does NOT resolve C142's `W_cand=3⊕3̄⊕3̄` question.** That requires the SAME
   method applied to Landweber's TWISTED operator `Ð_μ` (Theorem `th:slebarski`,
   kernel `= V_{w(μ+ρ_H)−ρ_G}` or `0`) — a promising, NOT YET CHECKED next round.
   If C139/C141's twisted constructions are literal instances of `Ð_μ`, Slebarski's
   theorem would give a general, PROVEN (not Hom-dim-1-restricted) kernel formula
   for every irreducible SU(3) summand — potentially subsuming C143's Lemma 1 AND
   resolving C143's still-open Lemma 2 (Hom-dim ≥ 2). This is flagged as the
   natural C145 candidate, not executed here (scope discipline — one new theorem
   per round, per this project's own Minimal Relaxation Rule spirit).
2. No independent root-system Casimir-norm computation (`‖ρ_g2‖²−‖ρ_su3 ‖²`) was
   attempted — the `√3/4` scale factor was derived self-consistently from AHL2023's
   own data, not cross-checked against Kostant's `dsquared` formula computed from
   g2/su(3) root systems independently. Would be a valuable, independent
   confirmation; not required for this round's narrower claim.

## Pearl / Caveat gate

`pearl_registry/INDEX.md` new row: Kostant/Landweber connection to the twisted case
(item 1 above) — falsifiable, has a `next_check`, logged below.
