# E11 (round77) — Claim: do ψ⁽⁰⁾ and ψ⁽¹⁾ label as clean SU(2)_L×SU(2)_R
# representations, and does that labeling connect to S⁶'s left-handed
# chirality convention?

**Date:** 2026-07-17
**FL tier:** [x] Full (research claim; methodology per project CLAUDE.md)
**Question type:** [x] descriptive [ ] predictive [ ] causal

Descriptive: for the two explicit parallel-spinor profiles already constructed
in this project — `ψ⁽⁰⁾ = const` (E9, left-invariant frame, ∇⁰-parallel for
ALL sign/value of the structure constant) and `ψ⁽¹⁾(x) = ḡ(x)·ψ₀` (round76
Part 4, ∇¹-parallel ONLY under the concrete `c0=−2` sign convention, NOT under
this project's own physics-calibrated `c=+2`) — do these two spinors carry
clean, definite representation labels under `SU(2)_L×SU(2)_R` when `SU(2)_L`
is identified with LEFT group-translation on `S³=SU(2)` and `SU(2)_R` with
RIGHT group-translation (round74's "only geometrically natural convention" —
**not** explicitly stated anywhere in `preprint.tex`), and if so, is that
labeling suggestive of, or in tension with, the ALREADY-FIXED "left-handed"
convention S⁶ independently fixes (`preprint.tex:885-908`, Lemma L5)?

## Stakes
Internal-only. This is explicitly flagged (by the task, and by round74's own
decision.md) as **[SPECULATIVE] synthesis** — a candidate follow-up question,
not a claim about `preprint.tex`. Nothing here is promoted to the paper.

## Background (established, not re-derived here)

- `preprint.tex:273-279` (§ gauge-S3): `Iso(S³) = SO(4) ≅ SU(2)_L×SU(2)_R` from
  the bi-invariant metric on `S³`, identified DIRECTLY with the Pati–Salam
  `SU(2)_L×SU(2)_R` gauge factors. **The paper never states which translation
  direction (left vs. right group-multiplication) is "`SU(2)_L`"** — confirmed
  by grep of the full section text (round74, Q3) and independently re-confirmed
  here (no occurrence of "left-invariant"/"right-invariant"/"acts on the left"
  language anywhere in `preprint.tex`).
- `preprint.tex:304, 332`: `SU(2)_L` in this paper is used exactly as the
  Standard-Model/Pati–Salam convention (`T_{3L}` = weak isospin; the
  right-handed neutrino is explicitly identified as the "`SU(2)_L` singlet").
  This is the standard left-right-symmetric-model convention: SU(2)_L doublet
  = left-handed field, SU(2)_L singlet = right-handed field (e.g. ν_R).
- `preprint.tex:885-908` (Lemma L5): `sign(ind)=+1` on `S⁶` forces a
  left-handed excess; line 906-908 states explicitly: **"Matching the `S⁶`
  orientation convention to the SM convention for `SU(2)_L`, the left-handed
  Dirac zero mode corresponds to the left-handed SM fermion doublet."** This is
  itself a convention-MATCHING step (not a derivation) — it fixes which of the
  two 4D chirality labels ("left-handed"/"right-handed") the `S⁶`-side
  zero-mode gets, by hand, to agree with the SM's own labeling convention. It
  says nothing about which `S³` translation is `SU(2)_L` — that is a
  completely independent convention question, addressed by this experiment.
- `preprint.tex:1421-1445` ("Full-operator zero-mode gap", KT-8): **blocking
  gap, not resolved** — for the round, untwisted Levi-Civita `S³` ansatz used
  throughout the paper, `ker D_full = 0` identically; no zero mode of the
  physical 9D internal operator currently exists on the `S³` factor at all.
  `preprint.tex:1471-1495` (torsion-deformation item): the `t=0,1` crossings of
  the one-parameter family `∇^t` are a "candidate mechanism... physically
  unmotivated, not a resolution" — **no physical principle currently selects
  `t=0` or `t=1` over the Levi-Civita value `t=1/2`.** This means: even if the
  representation labeling below comes out clean, it labels spinors of a
  connection family that is not currently known to produce any physical zero
  mode at all (H1c fully open).
- `experiments/20260717-round73-e9-explicit-parallel-spinor/`: `ψ⁽⁰⁾=const` is
  ∇⁰-parallel, `D⁰ψ⁽⁰⁾=0` exactly, for ANY sign/value of the structure
  constant (t=0 kills the algebraic term regardless).
- `experiments/20260717-round76-e9followup-right-invariant-frame/` (Part 3-4):
  `ψ⁽¹⁾(x)=ḡ(x)ψ₀` is ∇¹-parallel and `D¹ψ⁽¹⁾=0` **exactly**, but ONLY under
  the concrete `c0=−2` (the literal Pauli-commutator structure constant of the
  quaternion realization) — the SAME candidate `ψ⁽¹⁾` **demonstrably fails**
  (nonzero, generic residuals) under this project's own abstractly-calibrated
  `c=+2`. No alternative candidate has been found or tested under `c=+2`.
  **This sign caveat is carried forward unconditionally below — every
  statement about `ψ⁽¹⁾` in this experiment is implicitly qualified by
  "under `c0=−2`, not under this project's own physics calibration."**
- `experiments/20260717-round74-e10-chirality-sign-link/`: flagged the
  candidate synthesis under test here as **[SPECULATIVE]**, explicitly NOT
  verified, for exactly three reasons (see "What this does NOT mean" below,
  items 1-3, which restate round74's own three blocking caveats).

## Claim (falsifiable, three parts)

**Part 1 — pin down the convention (bookkeeping, not physics).** Define
`SU(2)_L` to act on `g ∈ S³=SU(2)` by LEFT translation, `g ↦ h·g` (`h∈SU(2)_L`),
and `SU(2)_R` by RIGHT translation, `g ↦ g·h⁻¹` (`h∈SU(2)_R`) — the unique
geometrically natural realization of `SO(4)` acting by isometries of the
bi-invariant metric (round74's own framing, reused here, still NOT stated in
`preprint.tex`). Verify this gives two well-defined, commuting group actions
(closure/associativity), realized concretely via the quaternion model
`g(x)=x0·I+x1·Z1+x2·Z2+x3·Z3` (Z_i = round76's own `i·σ_i`).

**Part 2 — transformation of ψ⁽⁰⁾ and ψ⁽¹⁾ under both actions.** For a
spinor-valued function `ψ: SU(2)→ℂ²` expressed in components relative to the
LEFT-invariant frame `{Z_i}` (the frame both E9 and round76 build their
connections in), the natural combined action of an isometry on such a section
is: (a) under `SU(2)_L` (left translation) — PULLBACK ONLY,
`(h⋆ψ)(g):=ψ(h⁻¹g)`, because the left-invariant frame is itself invariant
under left translation (`(L_h)_*Z_i^L=Z_i^L` exactly — the defining property
of "left-invariant"); (b) under `SU(2)_R` (right translation) — PULLBACK PLUS
A COMPENSATING TARGET ROTATION, `(h⋆ψ)(g):=h·ψ(gh)`, because the
left-invariant frame rotates under right translation via the ADJOINT action
(`(R_h)_*Z_i^L = h Z_i h^{-1}`), and for spinors (the fundamental/double-cover
representation) the lift of this `SO(3)`-adjoint frame rotation to the
`SU(2)`-valued spinor components is exactly `h` itself. Compute both actions
on `ψ⁽⁰⁾=const` and `ψ⁽¹⁾(x)=g(x)⁻¹ψ₀` explicitly (symbolic sympy, concrete
representative `h(θ)` mixing all three generators), and report, for each
spinor and each action, whether the result is (i) EXACTLY the original
(singlet), or (ii) a genuinely nontrivial transformation for generic `h`
(candidate doublet/fundamental).

**Part 3 — connect (or fail to connect) to S⁶'s chirality convention.** IF
Part 2 finds `ψ⁽⁰⁾` is an `SU(2)_L`-singlet/`SU(2)_R`-doublet and `ψ⁽¹⁾` is an
`SU(2)_L`-doublet/`SU(2)_R`-singlet, THEN report explicitly whether this
matches the SM/Pati–Salam convention already fixed at `preprint.tex:304,332`
(SU(2)_L doublet = left-handed, SU(2)_L singlet = right-handed) combined with
the S⁶-side "left-handed" fixing at `preprint.tex:906-908` — i.e. whether
`ψ⁽¹⁾` (the t=1 candidate) carries the SAME representation content
("SU(2)_L doublet") as the label S⁶ independently calls "left-handed." Report
this ONLY as a suggestive pattern match between two independently-fixed
conventions (S³-translation↔gauge-label convention; S⁶-orientation↔4D-chirality
convention), explicitly NOT as a derivation, and explicitly flag every
unstated assumption the correspondence requires (see "What this does NOT
mean").

## Pre-registered PASS/FAIL/OPEN/SPECULATIVE-ONLY criteria

| Outcome | Condition |
|---|---|
| **PASS (representation labeling)** | Part 2 finds `ψ⁽⁰⁾` and `ψ⁽¹⁾` each transform as an EXACT singlet under one action and a genuinely nontrivial (non-degenerate for generic `h`) transformation under the other, for BOTH spinors, with NO ambiguity in the computation |
| **FAIL (representation labeling)** | Either spinor fails to give an exact singlet/nontrivial split (e.g. an unexpected extra `x`-dependence survives, or the "nontrivial" transformation degenerates to the identity for all `h`, not just special `h`) |
| **PASS (correspondence to S⁶ chirality)** | The representation labeling matches the Pati–Salam left/right-handed convention (`ψ⁽¹⁾`→SU(2)_L doublet↔"left-handed", matching `preprint.tex:906-908`'s independently-fixed label), **stated together with all three caveats below, never as an unqualified match** |
| **SPECULATIVE-ONLY (correspondence)** | The representation labeling PASSES cleanly (Part 2), but the connection to S⁶'s chirality convention requires the SU(2)_L=left-translation assumption (never stated in `preprint.tex`) AND/OR the c0=−2 sign convention (not this project's own calibration) AND/OR an unstated physical postulate that the S³ zero mode must "match" S⁶'s label — this is the PRE-REGISTERED EXPECTED OUTCOME, not a failure |
| **OPEN** | The representation-labeling computation itself does not resolve cleanly (ambiguous sign, frame-dependence not controlled, etc.) |

Per the task's explicit instruction: a SPECULATIVE-ONLY or OPEN verdict is a
fully valid, expected-likely result. This experiment does **not** upgrade
round74's [SPECULATIVE] flag to PASS unless Part 2's computation is completely
unambiguous AND every one of the caveats below is stated, not glossed.

## Kill criteria (MANDATORY — filled BEFORE running)

| Part | Kill condition | Threshold |
|---|---|---|
| 1 | `h(θ)` is not a genuine SU(2) element | `det_h_is_one==False` or `h_hbar_equals_I==False` — would invalidate the whole computation |
| 2 | `ψ⁽⁰⁾` is NOT an exact singlet under the left action | `action_L_psi0_equals_psi0_exactly==False` — would directly contradict the "left-invariant frame is invariant under left translation" fact this whole claim rests on |
| 2 | `ψ⁽⁰⁾`'s right-action transform degenerates to the identity for ALL θ (not just θ=0) | `action_R_psi0_nontrivial_at_concrete_theta==False` — would mean ψ⁽⁰⁾ is ALSO an SU(2)_R singlet, killing the "doublet" half of the claim |
| 2 | `ψ⁽¹⁾` is NOT an exact singlet under the right action | `is_singlet_exact_for_all_theta_and_all_x==False` — would directly contradict the algebraic cancellation `h(gh)^{-1}=g^{-1}` this half of the claim rests on |
| 2 | `ψ⁽¹⁾`'s left-action transform degenerates to the identity for ALL θ | `nontrivial_at_concrete_theta==False` (action_L branch) — would mean ψ⁽¹⁾ is ALSO an SU(2)_L singlet, killing the "doublet" half |
| 3 | The clean complementary pattern does not hold (any of the four Part-2 sub-results fails) | `clean_complementary_rep_pattern_found==False` — Part 3's correspondence claim is void if Part 2 is not clean; report as FAIL on Part 2, not forced |

## Method

1. Reuse round76's own `Z_i=i·σ_i` Clifford generators and quaternion group
   element `g(x)` unchanged (no new geometric machinery).
2. Build a concrete, generic one-parameter SU(2) element `h(θ)` (all three
   generators mixed, fixed axis `n=(1,2,2)/3`), verify `h·h̄=I`, `det h=1`
   directly (not assumed).
3. Define `ACTION_L(h,ψ)(G):=ψ(h⁻¹G)` and `ACTION_R(h,ψ)(G):=h·ψ(Gh)` as the
   two candidate group actions (derivation of why the compensating factor
   appears on exactly one side: see claim text above and decision.md).
4. Apply both actions to `ψ⁽⁰⁾=(a,b)` (constant) and `ψ⁽¹⁾(G)=G⁻¹·(a,b)`
   (generic invertible symbolic matrix argument `G`, sympy `.inv()` — no
   unit-norm constraint needed since the identities checked are pure
   consequences of `(AB)⁻¹=B⁻¹A⁻¹`, valid for any invertible matrices).
5. Verify symbolically (sympy `simplify`) whether each of the four
   (spinor × action) combinations is an EXACT identity (singlet) or a
   genuinely nontrivial map (checked concretely at `θ=π/3` to rule out
   accidental universal degeneracy).
6. Cross-reference the resulting labels against `preprint.tex:304,332`
   (SU(2)_L doublet↔left-handed convention) and `preprint.tex:906-908`
   (S⁶'s independently-fixed left-handed label), reporting the match (or
   mismatch) with every assumption stated explicitly.

## What this does NOT mean

1. Does **not** show `preprint.tex` commits to SU(2)_L=left-translation — this
   remains an assumption imported from round74's "only geometrically natural
   convention" framing, not a stated project convention. **If the convention
   were reversed** (SU(2)_L=right-translation, SU(2)_R=left-translation), every
   label in this experiment flips, and `ψ⁽⁰⁾` (not `ψ⁽¹⁾`) would carry the
   "SU(2)_L doublet" (left-handed-like) content instead.
2. Does **not** show `ψ⁽¹⁾` exists under this project's own calibrated
   connection (`c=+2`) — round76 Part 4 found it does NOT (fails, generic
   nonzero residuals). Every statement about `ψ⁽¹⁾`'s representation content
   here describes an object that currently only exists under `c0=−2`.
3. Does **not** establish any physical requirement that the eventual S³-factor
   zero mode must "match" S⁶'s left-handed label — round74's point (3) stands
   untouched: this would be an independent physical postulate, stated nowhere
   in this project, and moreover H1c/KT-8 mean **no S³-factor zero mode of the
   full 9D operator currently exists at all** for the round Levi-Civita
   ansatz used throughout the paper — the torsion family (which is where
   t=0,1 live) is explicitly "physically unmotivated, not a resolution"
   (`preprint.tex:1471-1495`).
4. Does **not** resolve H1c, H2, H3, KT-3, or any open item in
   `preprint.tex §discussion` — untouched.
5. Does **not** claim this is a novel general theorem about Lie groups —
   the underlying representation-theoretic fact (constant sections in a
   one-sided-invariant trivialization transform as the fundamental
   representation under the OPPOSITE side's translation) is standard,
   general Lie theory, not discovered here; what this experiment adds is a
   concrete, tool-verified check for THIS project's specific spinor
   construction and an honest audit of whether it connects to an existing
   project convention (it does, but only under stacked, explicitly-flagged
   assumptions).

## Assumptions (status)

| Assumption | Status |
|---|---|
| SU(2)_L acts on S³ by LEFT translation, SU(2)_R by RIGHT translation | [WEAK] — round74's "only geometrically natural convention"; **not stated in `preprint.tex`** |
| Left-invariant frame `{Z_i}` is invariant under left translation, transforms via Ad(h) under right translation | [VERIFIED-tool, round76 Part 1] — reused, not re-derived here |
| Spinor components inherit the frame's transformation via the tautological SU(2) lift of the Ad(h) rotation | [INFERRED] — standard associated-bundle/spin-lift argument, stated explicitly in claim text; VERIFIED-tool for the specific computation via sympy below, not re-derived from first principles of bundle theory |
| `ψ⁽¹⁾=ḡ(x)ψ₀` is ∇¹-parallel ONLY under `c0=−2`, fails under `c=+2` | [VERIFIED-tool, round76 Part 4] — reused unchanged |
| SU(2)_L doublet = left-handed, SU(2)_L singlet = right-handed (Pati–Salam convention) | [DOCS] — standard left-right-symmetric-model convention; also this project's OWN usage (`preprint.tex:304,332`, ν_R as SU(2)_L singlet) |
| No physical principle currently selects t=0 or t=1 as the physically realized connection | [DOCS, this project] — `preprint.tex:1471-1495`, explicitly stated as an open gap |

## Check
`python e11_su2lr_representation_check.py` →
`verdict.core_setup_ok==true`, `verdict.psi0_is_SU2L_singlet==true`,
`verdict.psi0_is_SU2R_doublet_not_singlet==true`,
`verdict.psi1_is_SU2L_doublet_not_singlet==true`,
`verdict.psi1_is_SU2R_singlet==true`,
`verdict.clean_complementary_rep_pattern_found==true`,
`verdict.label=="CLEAN_COMPLEMENTARY_REP_PATTERN_FOUND__SPECULATIVE_CONVENTION_DEPENDENT"`.
