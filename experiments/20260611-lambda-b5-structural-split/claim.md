# LAMBDA-B5-G0: Structural Split Required

**Date:** 2026-06-11
**Tier:** FL Standard (research, structural/mathematical claim)
**Question type:** [x] descriptive (structural) [ ] predictive [ ] causal
**Status:** CLOSED — **STRUCTURAL_SPLIT_REQUIRED**

---

## Claim

The invariant one-form sector on S³ (the Killing one-forms ξ̃, ξ̃′) is **not contained**
in the current Ben Achour coexact mode basis E_i/E′_i. Therefore the current V ansatz

```
V = λ Σ_{a,I} γ^a A_a^I(x) T_I,    A^I(x) = Σ_i c_i^I E_i(x) + Σ_i c_i'^I E'_i(x)
```

**cannot** be matched to a Dereli-style spin-connection/background coupling
(arXiv:1904.08146) by restricting or tuning coefficients c_i^I.
The invariant forms lie outside span(E_i, E′_i).

## Primary Result

For the constant scalar seed Φ = 1 (label L = 0), with conventions pinned to the
preserve-branch code (`ben_achour_one_form_modes.py`, `test_p13a1`):

```
ξ̃  = ( 0,  cos²α,  sin²α )     *d ξ̃  = −2 ξ̃
ξ̃′ = ( 0, −cos²α,  sin²α )     *d ξ̃′ = +2 ξ̃′

B  = *d(Φ ξ̃)  = −2 ξ̃          C  = *d B  = +4 ξ̃
E  = (L+2)B + C = 2B + C = 0                          (identically)

B′ = *d(Φ ξ̃′) = +2 ξ̃′         C′ = *d B′ = +4 ξ̃′
E′ = (L+2)B′ − C′ = 2B′ − C′ = 0                      (identically)
```

The E/E′ combinations **annihilate** the invariant forms at the constant seed:
ξ̃ and ξ̃′ are seed/background objects, not basis elements produced by the tower.

## Evidence (three independent lines)

| Line | Source | Marker |
|---|---|---|
| Symbolic computation | `evidence_sympy_invariant_sector.py` (this folder), exact sympy, exit 0 | [VERIFIED-sympy 2026-06-11] |
| Code architecture | preserve: `ben_achour_one_form_modes.py:193-198` — `mode_applicability_status` returns `VANISHING_OR_EXCLUDED` for L ≤ 1; `test_p13a1:76` asserts L=0,1 excluded | [VERIFIED-git-show 2026-06-11] |
| Independent skeptic | adversarial review C3: invariant sector carries L=0 (Δ_HdR = 4 = (L+2)²); both external label guesses (L=2, L=1) refuted | [VERIFIED-agent + sympy 2026-06-11] |

## Controls

- **Positive control:** L=2 scalar mode Φ = cos(2α) (Δ-eigenvalue 8 = L(L+2), verified
  in script) produces a **nonzero** E mode — the construction is not degenerate away
  from the invariant sector. Norm formula cross-check: ‖E_{2,0,0}‖² = 2·2·3·4 = 48 ≠ 0.
- **Negative control (the result itself):** constant seed Φ=1 → E ≡ 0, E′ ≡ 0.
- **Convention pin:** seed *d eigenvalues (−2, +2) reproduce the preserve-branch test
  `test_killing_one_forms_are_metric_duals_and_star_d_smoke_checks` exactly.

## Kill Conditions (what would falsify this claim)

1. E(L=0) ≠ 0 or E′(L=0) ≠ 0 under the pinned conventions → claim dead.
2. Invariant forms found in span(E_i, E′_i) for any implemented L ≥ 2 → claim dead.
3. Positive control E(L=2) = 0 → construction degenerate everywhere → claim vacuous.

None triggered. (Orientation-flip robustness: reversing orientation swaps the roles of
the primed/unprimed branches but the vanishing persists in the matching combinations.)

## Verdict

```
LAMBDA-B5-G0 = STRUCTURAL_SPLIT_REQUIRED
```

## Consequence

Any Dereli-style spin-connection comparison requires an **explicit decomposition**:

```
V = λ_geom · V_ω  +  Σ_i c_i · V_modes(E_i, E′_i)

V_ω      = canonical geometric / spin-connection-like background term
            (built from invariant forms; NOT representable in the E/E′ tower)
V_modes  = dynamical / mode-expanded Ben Achour sector (L ≥ 2)
```

These are structurally different objects. The previous question
"can c_i^I be chosen so that A_a^I becomes the spin connection?" is **answered: no** —
not in the current E_i/E′_i ansatz.

## λ Status (exact wording — use verbatim)

```
λ total      = NOT fixed   (S³-only mode-expanded λ remains free; P14 no-go intact)
λ_geom       = MAY be canonically normalized IF V_ω is explicitly identified with
               the geometric Dirac spin-connection term (conditional; identification
               is a modeling choice — Tom's Q3)
c_i (modes)  = free
```

## What This Result Does NOT Mean

1. Does NOT mean "λ fixed" — the full coupling remains free.
2. Does NOT mean a Dereli match passed — no match was attempted; the gate shows the
   *precondition* for any match (a separate geometric term) is absent from the ansatz.
3. Does NOT overturn the S³-only no-go (P14) — it refines it: the no-go applies to the
   mode sector; the geometric sector was never in the ansatz to begin with.
4. Does NOT derive a physical V operator — research_only, PROMOTION_BLOCKED intact.
5. Does NOT select λ = κ/ρ — that requires importing a gravity sector the model
   does not contain (Newton constant G is not available here).

## Next Gates (recorded, not started)

- **G2:** cot(2α)-frame-artifact hypothesis: tan α − cot α = −2cot(2α) exactly;
  Hopf-coframe spin connection ω₁₂ = tan α·e², ω₁₃ = −cot α·e³, ω₂₃ = 0 vs
  invariant-frame ω_ij = ε_ijk σ_k/ρ (constant coefficients). Candidate answer to
  Tom's Q2. Status: HYPOTHESIS → needs G2 verification.
- **G1:** canonical Dirac in invariant frame reproduces spectrum ±(n+3/2)
  (positive control = existing E0 harness).
- **G3:** [D_a, D_b] curvature kill-test with su(2)_L ⊂ su(4) embedding (Dereli eq 4.12).

Order: G0 (this) → G2 → G1/G3 only if G0/G2 clean.

---

**Fence:** lambda = FREE_COUPLING_PARAMETER; runtime = research_only;
selection_rules = smoke_only; safe_for_runtime = False. Nothing here is written to Tom
until he replies to the 2026-06-09 four-question message.
