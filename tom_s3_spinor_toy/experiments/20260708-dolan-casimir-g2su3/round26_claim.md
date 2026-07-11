---
experiment_id: 20260708-dolan-casimir-g2su3
round: 26
date: 2026-07-11
tier: Full-Ladder
status: skeptic_reviewed_bug_found_and_fixed_C1-C6_confirmed_post_fix
parent: round25 (K-derivation via Kostant's H, inconclusive; step2_remainder promoted as open lead)
---

# claim.md — Round 26: deriving the Jac_h/Jac_m curvature-Jacobi term
explicitly, per Agricola 2002 Theorem 3.2, read from the primary source

## Background

Round 25 found `step2_remainder := cubic_and_curvature_L - (-H)` compresses
to a non-scalar diagonal on the 2-dim SU(3)-invariant subspace, and both
skeptics flagged this as evidence of a real, unbuilt piece —
`g2su3_H_element.py`'s own docstring explicitly said the "Jac_h-dependent
piece of Theorem 3.2's quartic term... requires full g2 structure
constants beyond what's been built so far" and was not computed. This
round reads Agricola 2002's Theorem 3.2 (General Kostant-Parthasarathy
formula) directly from the PDF in this repo
(`Agricola_2002_Dirac_naturally_reductive.pdf`, pages 5, 8-9, 12-14 —
text-extracted via `pymupdf`, NOT reconstructed from memory) and builds
every term the formula requires.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — algebraic derivation from a cited theorem,
tested against ground truth. NOT empirical, NOT causal.

## Source material (verbatim formula, page 14, n≥5 case — our case,
dim m = 6)

```
(D^t)^2 = Omega_g
        + (1/2)(1-3t) sum_{i,j,k} <[Zi,Zj]_m,Zk> Zi.Zj.Zk(.)
        - (1/2) sum_{i<j<k<l} <Zi, Jac_h(Zj,Zk,Zl) + 9t^2 Jac_m(Zj,Zk,Zl)> Zi.Zj.Zk.Zl .
        + (1/8) sum_{i,j} Qh([Zi,Zj],[Zi,Zj]) . + (3/8)t^2 sum_{i,j} Qm([Zi,Zj],[Zi,Zj]) .
```
with (page 5): `Jac_m(X,Y,Z) := [X,[Y,Z]_m]_m + [Y,[Z,X]_m]_m + [Z,[X,Y]_m]_m`,
`Jac_h(X,Y,Z) := [X,[Y,Z]_h] + [Y,[Z,X]_h] + [Z,[X,Y]_h]` (both land in m
by reductivity — stated explicitly in the source). `Omega_g := -sum Zi^2
+ C~h` (eq. 9, page 13) where `C~h`'s own degree-0/degree-4 parts are
given by Prop. 3.3 (page 11): `(C~h)_0 = (1/8)sum Qh(...)`, `(C~h)_4 =
-(1/2)sum<Zi,Jac_h(Zj,Zk,Zl)>ZiZjZkZl`. At `t=1/2` (this project's
established Levi-Civita convention): the cubic term is `-H` (already
established, `g2su3_H_element.py`); `9t^2=9/4`; `(3/8)t^2=3/32`.

## Construction (code: `g2su3_round26_jach_derivation.py`)

`Jac_m`, `Jac_h` built as 6-vectors from ALREADY-VALIDATED, `M_p`-
INDEPENDENT primitives only: the torsion table `T(i,j,k)` (`Jac_m`,
double sum) and the su(3)-curvature table `curv_h` combined with
`ad_nu_m_trusted` — the su(3)-on-**vectors** (6-dim m) action, already
built and calibrated in `g2su3_appendix_a_construction.py` against
Remark 5.2's trusted formula (48/48 pairs match, per that file's own
`main()`) — for `Jac_h`. `C~h` and the degree-4 term are then assembled
as explicit 8×8 Clifford matrices (4-fold `e_action` composition), and
the scalar term as a plain rational. All FOUR of these pieces (H, C~h,
degree4_term, scalar_term) are built with ZERO dependence on `M_p`
(this project's own Levi-Civita connection operators) — only `Omega_g`'s
own `-sum Zi^2` piece needs a differential-operator proxy, and per the
source (eq. 8, page 12) `Zi(psi)` there means the CANONICAL (t=0)
derivative, not necessarily this project's `M_p` (labelled "Levi-Civita",
i.e. t=1/2) directly. This is NOT assumed — it is tested by direct
subtraction from ground truth (`Dslash_mat^2`, computed via direct matrix
composition, reused from Round 24/25).

## Falsifiable Claims

**C1:** `C~h`, built from `curv_h`+`Jac_h` alone, is Hermitian, and its
trace-average equals its own predicted `(C~h)_0` (Prop 3.3's self-
consistency, mirroring the check `g2su3_H_element.py` already has for
H²).

RESULT: `[VERIFIED-tool]` — Hermitian confirmed; `Tr(C~h)/8 = 1 = (C~h)_0`
exactly (post-fix value; the first version had a `Qh_sum` bug giving
`1/2` — see Skeptic Verdict below).

**C2:** The degree-4 term (`-(1/2)sum<Zi,Jac_h+(9/4)Jac_m>ZiZjZkZl`) is
Hermitian and traceless (pure degree-4 Clifford element, no degree-0
part).

RESULT: `[VERIFIED-tool]` — both confirmed exactly.

**C3:** `sum Qm([Zi,Zj],[Zi,Zj]) = 8` (cross-check against
`g2su3_H_element.py`'s own established `Tr(H²)/8=3=(3/8)*8`).

RESULT: `[VERIFIED-tool]` — asserted and confirmed, `= 8` exactly.

**C4:** `-sum Zp^2`, isolated by DIRECT SUBTRACTION from `Dslash_mat^2`
(ground truth) minus `[-H + C~h + degree4_term + scalar_term]` (all four
`M_p`-independent), equals `-sum M_p^2` (this project's own Levi-Civita
connection Casimir) exactly.

RESULT: `[VERIFIED-tool]` — **FALSIFIED**. They do NOT match directly.

**C5 (REWRITTEN post-skeptic — see "Skeptic Verdict" below; sign
corrected):** the mismatch (`diff := implied[-sum Zp^2] - [-sum Mp^2]`)
is NOT scalar, but IS EXACTLY `H - (1/2)*Id - (7/4)*Casimir_su3(Sigma)`,
where `Casimir_su3` is the SU(3) Casimir on the 8-dim Clifford module Σ
(`= -sum_k L_k²`, `L_k` the already-established su(3) spin-representation
generators, reused unchanged since Round 17-20).

RESULT: `[VERIFIED-tool]` — confirmed exactly (sympy exact equality,
asserted in-script), **after fixing a real bug** (see Skeptic Verdict):
the FIRST version of this script had `Qh_sum` silently summing over only
`p<q` (since `curv_h` is stored only for `p<q`, unlike the `T`-table which
stores both orders explicitly — a `.get()` default-to-zero silently
dropped every `i>j` term), giving `Qh_sum=4` and a coefficient `+1/2`.
Skeptic 2 caught this from code inspection alone (no execution needed)
and predicted the fix's exact consequence (sign flip on the `Id` term,
nothing else) BEFORE it was run. Fixed (`Qh_sum` now `= 8`, matching the
ordered-sum convention `Qm_sum` already used correctly); re-run confirms
the sign flip EXACTLY as predicted — this is stronger cross-validation
than a single clean closure would have been.

**C6 (consequence — connects back to Round 25; sign corrected):** since
`+H` in C5's correction cancels the formula's own `-H` cubic term, Round
25's `step2_remainder` (`:= cubic_and_curvature_L - (-H)`) equals `H +
C~h + degree4_term + (scalar_term-1/2)*Id - (7/4)*Casimir_su3` — this
ALGEBRAIC IDENTITY is now `[VERIFIED-tool]` (re-verified after the fix).
It does **not**, however, constitute a first-principles EXPLANATION of
`step2_remainder` — see "What this does NOT mean" below, unchanged by
the fix.

RESULT: `[VERIFIED-tool]` — this predicted decomposition, computed
independently (re-deriving `step2_remainder` from scratch via the same
recipe Round 25 used: `Dslash_mat^2 - (-sum Mp^2) - (-H)`), matches
EXACTLY post-fix.

## Kill Conditions

- C1/C2/C3 killed if: skeptic finds `ad_nu_m_trusted`'s calibration
  (48/48 pairs, from an EARLIER session's own established check in
  `g2su3_appendix_a_construction.py`) is not actually being invoked
  correctly here — e.g. an index-order or sign mismatch in `jac_h`'s
  `[Z_i,X]=-ad(X)(Z_i)` convention (skeptic should verify this sign
  against Lemma 3.4's own convention, page 12: "X(psi)=-ad(X)·psi" for
  X∈h — the MINUS sign used in `h_bracket_action_on`/`jac_h` mirrors
  this).
- C4 is a NEGATIVE result already (not subject to "kill" in the usual
  sense) — but skeptic should verify it is not itself an artifact of a
  sign/normalization error that would make C5's "clean" correction
  spurious (i.e., check whether SOME simpler, more "obviously right" M_p
  convention would have made C4 pass instead, which this round did not
  search for — only the two most natural candidates, `-sum Mp^2` and,
  implicitly via C5, the corrected version, were tested).
- C5/C6 killed if: skeptic finds an arithmetic error in the `H - (1/2)Id
  - (7/4)Casimir_su3` formula (re-derive independently — note: this sign
  was ITSELF corrected once already, per the Skeptic Verdict below,
  precisely because a skeptic re-derived it independently and found a
  bug; a second independent re-derivation is exactly the right check to
  ask for again), or finds this
  "clean decomposition" is a numerological coincidence rather than a
  structurally meaningful identity — e.g. by checking whether an
  UNRELATED, differently-constructed matrix could ALSO happen to equal
  `diff` by chance (low prior, given `diff` is an 8×8 matrix with a
  specific rank-1-off-diagonal-plus-diagonal structure exactly matching
  H's own signature, but the skeptic should assess this critically, not
  take "it worked" as self-evidently meaningful).
- Skeptic should ALSO independently verify (per the project's own
  numerical-coincidence-not-mechanism lesson, `feedback-numerical-
  coincidence-not-mechanism.md`) that C5/C6 are not merely accepted
  because they closed cleanly — check whether an INDEPENDENT argument
  (not just "it matched") supports the specific coefficients `1/2` and
  `-7/4` appearing, or whether this should be flagged as an unexplained
  (if verified) numeric fact pending a cleaner derivation.

## What this does NOT mean

- Does NOT resolve the preprint's `8/45 vs ~1.03` norm-ratio tension —
  this round did not touch the 2-dim SU(3)-invariant-subspace projection
  or `Scal/4` question directly; it explains WHERE `step2_remainder`
  comes from algebraically, not what it means physically for the L4A
  norm bound.
- Does NOT establish which of `M_p` (this project's Levi-Civita
  operators, used throughout Rounds 14-25) or `Z_p` (Agricola's
  canonical derivative) is the "correct" object for computing R/4 in
  the preprint's Weitzenböck identity — both are legitimate, well-
  defined operators; this round shows they differ by an EXACT amount,
  not which one the preprint's own R/4=Scal/4 convention intends.
- Does NOT claim a first-principles UNDERSTANDING of WHY the correction
  is exactly `H - (1/2)Id - (7/4)Casimir_su3` (i.e. no independent
  argument for these specific coefficients beyond "it matches ground
  truth exactly, twice, including after a bug fix") — this is reported
  as a verified FACT, not a fully explained mechanism. Both skeptics'
  kill conditions on this point stand even after the bug fix.
- Does NOT change F_{S^-}'s own spectrum, the Atiyah-Singer index=1, or
  any other previously-established result — this round is purely about
  decomposing `step2_remainder`.

## Skeptic Verdict (FL Step 8a, 2026-07-11, two independent context-blind
skeptics, neither had code-execution tools this pass — both flagged this
limitation themselves; author independently re-ran and re-verified
everything both before AND after responding to their findings)

| Claim | Verdict | Note |
|---|---|---|
| C1 | WEAKENED (both) | `Tr(C~h)/8=(C~h)_0` is a structural tautology (any degree-4 Clifford element is traceless by construction) — does NOT verify `Jac_h` was computed correctly, only that the general shape is right. Accepted as a valid methodological limitation; not fixed (would require an independently-computed cross-check of `C~h`, not attempted this round). |
| C2 | CONFIRMED-REAL (S2) / WEAKENED (S1) | Hermiticity+tracelessness are likewise structural (real coeffs × Clifford quartic products), not strong tests of the specific `Jac_h+(9/4)Jac_m` coefficient. Same limitation as C1, accepted. |
| C3 | CONFIRMED-REAL (both) | Genuine independent cross-check (`Qm_sum=8` ties to `H`'s own established `Tr(H²)/8=3`) — this one is NOT tautological, both skeptics agreed. |
| C4 | NEEDS-REAL-DATA → CONFIRMED-REAL after fix | Both skeptics wanted PDF verification before trusting this; author independently re-extracted page 14 fresh (`pymupdf`) and confirmed the transcription matches exactly, both before and after the bug fix below. |
| **C5/C6** | **WEAKENED → real bug found (Skeptic 2), fixed, re-verified** | **Skeptic 2 found, from code inspection alone:** `Qh_sum` summed only over `p<q` entries of `curv_h` (stored `p<q`-only, unlike `T` which stores both orders) — a silent factor-of-2 undercount (`4` instead of `8`). Skeptic 2 explicitly predicted the fix's consequence ("if confirmed, the reported identity becomes `H - (1/2)Id - (7/4)Casimir_su3`... sign flip on `Id`") before the fix was applied or re-run. **Author fixed the bug and re-ran: the prediction was exactly right** — sign flipped on the `Id` term only, nothing else changed. This is stronger cross-validation than the original (buggy) clean closure was, precisely because it survived an independent, differently-reasoned prediction test. **Skeptic 1's separate, still-standing concern**: `-sum Zp^2` is *operationally defined* by subtraction from the transcribed formula, so C5/C6 cannot, by construction, rule out *some other* undetected transcription error being silently absorbed into a coincidentally-clean-looking correction. This is a valid, unresolved epistemic limitation — mitigated but not eliminated by (a) two independent fresh PDF re-extractions matching, (b) the bug-fix/prediction cross-validation above, (c) C1-C3's independent (non-tautological, for C3) sanity checks all passing — but NOT eliminated, since no first-principles derivation of the specific coefficients `H, -1/2, -7/4` exists. Reported with this caveat explicit, not resolved. |

**Durability fix applied**: hard asserts added for C5/C6's specific values
(`diff_matches_prediction`, `step2_matches`) — these were already present
in the original script (not merely printed), so no additional change
needed here beyond the sign correction itself.
