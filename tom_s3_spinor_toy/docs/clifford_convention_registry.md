# Clifford sign-convention registry

**Status:** canonical. Written 2026-08-10 by the repo-wide audit
(`experiments/20260810-clifford-convention-repo-audit/`), which the 2026-08-09
pearl left as an open next-check after OB10.

**Why this file exists.** OB10 (2026-08-03) tensored the S³ and S⁶ spinor
constructions for the first time, got a mixed `Cl(6,3)` signature, and reported
it as a geometric finding. It was a codebase fact: the two sub-projects carry
opposite Clifford sign conventions. That produced a wrong reality-type verdict
(C28), a wrong downstream no-go (C31), a wrong correction of the no-go (C32),
and finally the right answer (C33) — four claims, one unwritten convention.

**Read this table before tensoring, comparing, or labelling any Clifford
construction in this repo.**

---

## The one thing to know

`Cl(p,q)` is used with **two opposite meanings** in this repo. The generators
tell you the truth; the label does not.

| Sub-project | generators | `e²` | label used | label correct? |
|---|---|---|---|---|
| **S³** — `round67` and descendants (`round68/69/73/76/78/81/89/113/114`) | `Z_i = i·σ_i` | **−1** | `Cl(0,3)` | ✅ |
| **S⁶** — `20260615-s6-harm-g0`, `g13` | `Γ_a` hermitian | **+1** | `Cl(6,0)` | ✅ |
| **Octonion** — `g68`, `g2su3_round31/32/34`, dolan-casimir | `L_i` (Fano table) | **−1** | `Cl(7,0)` | ❌ should be `Cl(0,7)` |
| **CSDR** — `g69_csdr.py:121-124` | *(none built; documentary constant)* | — | `Cl(6,0) ≅ M₈(ℝ)` | ❌ that isomorphism is `Cl(0,6)`'s |
| **Spin(8)** — `g101`, `g102` | doubled from `g68` | **−1** | `Cl(0,7)` / `Cl(0,8)` | ✅ |
| **so(4)×so(4)** — `20260715-l3b-so4xso4-candidate` | `Γ_i`, `{Γ,Γ}=+2δ` | **+1** | `Cl(8)` (unsigned) | ⚠️ ambiguous, code is +1 |

**The genuinely opposite pair is S³ (−1) vs S⁶ (+1).** That one is a real
mathematical difference, both labels are correct, and it is the pair OB10 hit.

**The octonion/CSDR rows are label bugs, not math bugs.** Every matrix, every
assertion, and every result in those experiments is correct. Only the *name* is
inverted — and `g101`/`g102`, which build on `g68`, already write `Cl(0,7)` for
the same object. The repo therefore contains both names for one thing.

---

## How each verdict above was established

Not from a periodicity table recited from memory — computed in
`label_vs_code_check.py`, which builds the generators and measures:

**n = 7 (octonion).** The pseudoscalar `ω = e₁…e₇` is central and
`ω² = ε⁷·(−1)²¹ = −ε⁷`. So `ε = −1 → ω² = +1`, the algebra **splits** as
`M₈(ℝ)⊕M₈(ℝ)` with `ω = ±I` picking the summand; `ε = +1 → ω² = −1`, no real
split (`M₈(ℂ)`). `g68`-D4 and `round34` both *claim* the split (`Ω_L = +I₈`,
`Ω_R = −I₈`) — a claim only available at `ε = −1`. Verified: rebuilding the
Fano-table `L_i` gives `L_i² = −1`, all 21 pairs anticommuting, `ω = ±I`; and
the contrast case `i·L_i` (a true `Cl(7,0)`) gives `ω² ≠ +I`.

**n = 6 (CSDR constant).** The pseudoscalar does **not** discriminate here
(`ω² = −1` for both signs), so the audit uses the commutant instead: the real
algebra is `M₈(ℝ)` iff an antilinear `J` **commuting** with every generator has
`J² = +1`, and `M₄(ℍ)` iff `J² = −1`. Computed over the factorized Pauli
ansatz:

```
ε = +1  (a true Cl(6,0))  ->  J = σ₁⊗σ₂⊗σ₁, J² = −1  ->  M₄(ℍ)  quaternionic
ε = −1  (Cl(0,6))         ->  J = σ₂⊗σ₁⊗σ₂, J² = +1  ->  M₈(ℝ)  real
```

So `M₈(ℝ)` belongs to `Cl(0,6)`, and `g69`'s constant is labelled with the
other one.

---

## ⚠️ Do not confuse the commutant `J` with the charge conjugation `B`

These are **different objects answering different questions**, and they give
different signs on the same generators. Getting this wrong is the same class of
error as the convention mixing itself.

| | condition | what its square tells you |
|---|---|---|
| **commutant `J`** | `J conj(Γ) = +Γ J` (commutes) | the type of the **algebra**: `M₈(ℝ)` vs `M₄(ℍ)` |
| **charge conjugation `B`** (OB10/C32/C33) | `B conj(Γ) = −Γ B` (anti-intertwines) | the reality type of the **spinor module** |

On the uniformised S⁶ generators (`Γ' = iΓ`, `ε = −1`) both exist and disagree:

```
J = σ₂⊗σ₁⊗σ₂   commutes       J conj(J) = +I   -> algebra is M₈(ℝ)
B = σ₁⊗σ₂⊗σ₁   anti-intertwines B conj(B) = −I  -> module is quaternionic  (C33)
```

**No contradiction.** C33's `B conj(B) = −I` and this registry's `J² = +1` are
both correct and are not comparable. Verified explicitly during this audit
precisely because the two looked like a contradiction at first sight.

---

## Rules going forward

1. **Before tensoring two Clifford constructions from different experiments,
   assert both signs explicitly in code.** Do not infer the sign from a `Cl(p,q)`
   label anywhere in this repo — read the anticommutator assertion.
2. **A mixed-signature result is a suspected codebase inconsistency first**, a
   geometric finding only after that is ruled out. That is the OB10 lesson.
3. **State the convention in the same sentence as any signature, reality-type,
   or KO-dimension verdict.** The answer is convention-dependent; the
   geometrically correct convention is fixed by the manifold (S³×S⁶ is a
   Riemannian product → one uniform negative-definite convention), not by
   whichever sub-project's matrices were nearest to hand.
4. **Store KO-dimension as the full tuple** `(J², JDJ⁻¹/D, JγJ⁻¹/γ)` **plus the
   sign convention**, never as a bare "KO-dim N".
5. **A residual-form check reads backwards.** `{Γ_a,Γ_b} + 2δ_ab I == 0` asserts
   `{Γ,Γ} = −2δ`, the *negative* convention, despite the visible `+2`. This
   audit's own first scanner pass misread exactly that in `g102` and had to be
   fixed.

---

## Affected files (label only — no math or result changes)

The inverted `Cl(7,0)` / `Cl(6,0)` label appears in, and none of these needed a
correction to their content:

| file | occurrences |
|---|---|
| `README.md:58` | 1 |
| `experiments/20260621-g68-octonion-channels/g68_channels.py` | 2 |
| `experiments/20260621-g68-octonion-channels/decision.md` | 3 |
| `experiments/20260621-g69-csdr-coset/g69_csdr.py` | 2 (`Cl(6,0)`) |
| `experiments/20260708-dolan-casimir-g2su3/g2su3_round31_full_combinatorial_derivation.py` | 4 |
| `experiments/20260708-dolan-casimir-g2su3/g2su3_round32_curvh_combinatorial.py` | 7 |
| `experiments/20260708-dolan-casimir-g2su3/g2su3_round34_octonion_derivation.py` | 4 |
| `experiments/20260708-dolan-casimir-g2su3/round31_claim.md` / `round32_claim.md` / `round34_claim.md` | 3 / 6 / 7 |
| `experiments/20260708-dolan-casimir-g2su3/decision.md` | 4 |
| `tests/test_g68_octonion_channels.py` | 10 |
| `tests/test_g69_csdr_coset.py` | 3 |

**Historical `decision.md` / `claim.md` files are annotated, not rewritten**, per
this repo's retract-in-place convention. `tests/` is write-protected in the
current session and is listed here for a future pass; the tests assert the
*correct* relation (`−2δ`) and pass — only their prose says `Cl(7,0)`.

---

## Reproduce

```bash
python experiments/20260810-clifford-convention-repo-audit/clifford_convention_scan.py
python experiments/20260810-clifford-convention-repo-audit/label_vs_code_check.py
```
