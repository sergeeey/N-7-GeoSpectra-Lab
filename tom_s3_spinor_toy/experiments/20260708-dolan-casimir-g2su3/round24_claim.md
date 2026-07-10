---
experiment_id: 20260708-dolan-casimir-g2su3
round: 24
date: 2026-07-10
tier: Full-Ladder
status: skeptic_reviewed_C1-C3_confirmed_C4_rewritten
parent: round23 (F_{S^-} derivation, merged main@9145917)
---

# claim.md — Round 24: isolating ∇*∇ independently of F_{S^-}

## Background

Round 23 derived F_{S^-} (the twist-curvature endomorphism in the Weitzenböck
identity `(D_{S^6}⊗S^-)^2 = ∇*∇ + R/4 + F_{S^-}`) but could not isolate ∇*∇ or
R/4 independently — only the combined "remainder" `:= D^2 - F_{S^-}`, which
was shown to be non-scalar on the 2-dim SU(3)-invariant subspace. This left
open whether the preprint's norm-bound argument (`‖F_{S^-}‖/(R/4) ≤ 8/45`)
compares against a well-defined R/4 at all.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — algebraic/spectral decomposition check. NOT
empirical, NOT causal.

## Construction under test (code: `g2su3_Sminus_weitzenbock.py`, function
`main()`, section "STEP D")

`M_p` (p=1..6) are the pre-existing Levi-Civita connection operators on the
8-dim Clifford module Σ = Λ*(ℂ^3) (built by `build_Mp()`, reused unmodified
from Round 23). Define the total twisted connection on Σ⊗Σ:

  `N_p := M_p⊗Id + Id⊗M_p`   (p = 1..6, Leibniz rule)

and the Bochner Laplacian

  `∇*∇ := -Σ_p N_p^2`

This is built ONLY from `M_p` — it does not reference `D64`, `D64^2`, or
`F_{S^-}` anywhere in its construction. `S^6 = G_2/SU(3)` is naturally
reductive (standard fact for this coset), so the frame self-derivative
`∇_{e_p} e_p` vanishes; this is the standard justification that `-Σ_p N_p^2`
computes the genuine Bochner Laplacian for this frame, not an ad hoc
substitute.

## Falsifiable Claims

**C1:** `∇*∇` as constructed above is Hermitian and positive semi-definite.
(Necessary condition for it to be a genuine connection Laplacian; a metric
connection makes each `M_p` skew-Hermitian, hence each `N_p` skew-Hermitian,
hence `-N_p^2` positive semi-definite.)

RESULT: `[VERIFIED-tool]` — all six `M_p` skew-Hermitian; `∇*∇` restricted
to the 16-dim Γ(S^+⊗S^-) block is Hermitian with eigenvalues
`{0:1, 1/3:8, 2/3:6, 4/3:1}` (all ≥ 0).

**C2:** The three-term split `Δ := D64^2 - ∇*∇ - F_{S^-}` is a scalar
multiple of the identity (i.e. the clean Lichnerowicz form holds), both on
the full 16-dim Γ(S^+⊗S^-) fibre and on the 2-dim SU(3)-invariant
(trivial-component) subspace spanned by `w_a, w_b`.

RESULT: `[VERIFIED-tool]` — FALSE on both. On the 2-dim subspace,
`Δ = [[5/2, 4/3], [4, 5/2]]`, not scalar. Adding Round 22's already-derived
torsion cross-term (`TORSION_E`, restricted to the same subspace) does NOT
restore scalarity either.

**C3:** The scalar (trace-average) part of `Δ` on the 2-dim subspace equals
exactly `5/2` (the preprint's nominal `Scal/4` value), and the remainder
`Δ - (5/2)·Id` is trace-free.

RESULT: `[VERIFIED-tool]` — both hold exactly (sympy exact rationals, not
floating point): trace(Δ)/2 = 5/2 exactly; trace(Δ - (5/2)·Id) = 0 exactly.

**C4 (interpretation — REWRITTEN post-skeptic, see "Skeptic Verdict" below):**
The trace-free residual `[[0, 4/3], [4, 0]]` is **unresolved** between
(i) a frame/Leibniz correction term specific to the non-normal invariant
frame on a naturally reductive (non-symmetric) space, and (ii) a sign that
`F_{S^-}` is not the complete twist-curvature. No derivation currently
favors (i) over (ii): trace-freeness is consistent with a commutator/torsion
origin but is NOT diagnostic (a missing curvature piece could equally be
trace-free on this 2-dim block). One concrete (i)-candidate is already
RULED OUT: Round 22's `TORSION_E` (the known `nabla_{[e_p,e_q]}` torsion
term) does not restore scalarity when added to Δ. The cheapest differentiating
test between (i) and (ii) — computing the naturally-reductive canonical-
connection torsion `T^c(e_p,e_q)` restricted to `span(w_a,w_b)` and comparing
it to the observed `[[0,4/3],[4,0]]` — has NOT been done; this is Round 25.

## Kill Conditions

- C1 killed if: the skeptic finds `N_p` is not actually independent of
  `D64`/`F_{S^-}` in this code (i.e. some hidden circularity — e.g. `M_p`
  itself was derived from `D64` rather than being the pre-existing Round
  17-23 connection object), OR finds the PSD result is a sign/algebra
  error rather than a structural guarantee.
- C2/C3 killed if: the skeptic finds an arithmetic error in the matrix
  construction (e.g. `kron`, `project_2x2`, or the `Ms`/`Es` primitives)
  that would change `Δ`'s value, or finds the "exactly 5/2" result is an
  artifact of choosing `w_a, w_b` non-orthonormally (the `project_2x2`
  routine uses a Gram-matrix correction — skeptic should verify this
  correction is applied correctly and doesn't silently rescale the result).
- C4 should be treated as SPECULATIVE regardless of skeptic verdict — it is
  presented as the most likely reading, not a proven one. Skeptic's job here
  is to check whether ANY reading is currently justified, or whether C4
  should be flagged as unsupported until the frame term is explicitly
  derived and compared.

## What this does NOT mean

- Does NOT establish `dim ker(D+_{S^-})=1` (the L4B rank question) — this
  round only concerns whether R/4 is a well-defined isolated scalar in the
  Weitzenböck split, a separate question from the kernel rank.
- Does NOT change F_{S^-}'s own spectrum (`{1/6:15, -5/2:1}`, Round 23,
  unaffected by this round's work).
- Does NOT resolve the preprint's `8/45 vs ~1.03` norm-ratio tension to a
  specific number — it reframes the tension as "R/4 is not cleanly isolated
  from a frame/torsion term," which is a different (more precise) statement
  than "the numbers disagree."
- Does NOT establish any mechanistic link between Δ's scalar (trace-average)
  content and R/4 beyond the numeric match itself — `trace(Δ)/2 = 5/2`
  exactly equaling the preprint's nominal `Scal/4` is reported as an exact
  algebraic fact, not as evidence that this scalar content IS R/4 in a
  structural/mechanistic sense (per this project's own recurring lesson,
  see memory `feedback-numerical-coincidence-not-mechanism.md`).

## Skeptic Verdict (FL Step 8a, 2026-07-10, two independent context-blind
skeptics, no arbitration needed — both converged identically)

| Claim | Verdict | Note |
|---|---|---|
| C1 | CONFIRMED-REAL | independence + structural PSD both verified by code inspection |
| C2 | CONFIRMED-REAL | non-scalarity is basis-invariant, robust to non-orthonormal-basis concerns |
| C3 | CONFIRMED-REAL | trace/traceless split is basis-invariant, exact rational arithmetic |
| C4 | WEAKENED → rewritten above | "most likely (i)" was unsupported; now presented as genuinely unresolved (i) vs (ii), with the concrete Round-25 differentiating test named |

Author cross-check: the script was independently executed by the author
(not just code-inspected) prior to and after this skeptic round —
EXIT=0, ruff clean, all in-script asserts passed — so C1/C3's numeric
content carries `[VERIFIED-tool]` status (author execution), not merely
`[HYPOTHESIS]` (skeptics' own passes were code-inspection only,
`ran_code:false` on both).
