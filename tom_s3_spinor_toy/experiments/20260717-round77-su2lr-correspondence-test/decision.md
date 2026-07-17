# E11 (round77) — Decision

**Date:** 2026-07-17
**Verdict:** **CLEAN_COMPLEMENTARY_REP_PATTERN_FOUND__SPECULATIVE_CONVENTION_DEPENDENT**
— Part 2's representation-labeling computation PASSES cleanly and unambiguously
(`ψ⁽⁰⁾` is an exact `SU(2)_L` singlet / genuine `SU(2)_R` doublet; `ψ⁽¹⁾` is a
genuine `SU(2)_L` doublet / exact `SU(2)_R` singlet). Part 3's correspondence
to S⁶'s "left-handed" convention (`preprint.tex:906-908`) is a real, clean
pattern match — but it is **SPECULATIVE-ONLY**, exactly the pre-registered
expected outcome, because it stacks three independent, unverified/unstated
assumptions (see below). **This does NOT upgrade round74's [SPECULATIVE] flag
to PASS** — it resolves round74's blocking reason (2) ("whether the spinor
inherits the same triviality pattern... requires a representation-theory
computation... not checked") with a clean YES, while reasons (1) and (3) from
round74 remain fully open and unresolved, exactly as before.
**Go/no-go:** Does not promote H1c, KT-8, E2/E3/E7/E9/round74/round76, or any
`preprint.tex` claim. Contributes one fully-worked-out, tool-verified
representation-theory fact to the project's internal record, with an explicit
three-part caveat stack that must travel with it every time it is cited.

## What was checked, and how

Per claim.md, this experiment does NOT re-derive round76's connection/
parallelism machinery (already done, tool-verified there). It checks a
different, independent question: how the two ALREADY-CONSTRUCTED spinor
profiles — `ψ⁽⁰⁾=const` (E9) and `ψ⁽¹⁾(x)=g(x)⁻¹ψ₀` (round76 Part 4, `c0=−2`
only) — transform under the two candidate isometry actions this project's own
gauge-identification convention (`preprint.tex:273-279`, round74's framing)
would assign to `SU(2)_L` (left translation, `g↦hg`) and `SU(2)_R` (right
translation, `g↦gh⁻¹`).

**The key structural fact, derived and then verified [VERIFIED-tool]:** a
spinor expressed in components relative to the LEFT-invariant frame `{Z_i}`
(the frame both E9 and round76 build their connections in) transforms under
left translation by PULLBACK ONLY — no compensating rotation on the ℂ² target
is needed, because the left-invariant frame is *itself* invariant under left
translation (`(L_h)_*Z_i^L=Z_i^L` — the defining property of "left-invariant").
Under right translation, the SAME frame rotates via the adjoint action
(`(R_h)_*Z_i^L = h Z_i h^{-1}`), so a compensating rotation by `h` itself (the
tautological lift of the `SO(3)`-adjoint rotation to the `Spin(3)=SU(2)`
spinor bundle) is required to keep the spinor's transformation law consistent
with the frame's own behavior. This gives two candidate group actions:
```
ACTION_L(h,ψ)(G) := ψ(h⁻¹G)          [pullback only]
ACTION_R(h,ψ)(G) := h·ψ(Gh)          [pullback + compensating h]
```
This is standard associated-bundle theory (the connection between a
one-sided-invariant trivialization and the transformation law of sections
under the opposite-sided translation), applied here concretely, for the first
time in this project, to its own spinor construction.

## Result — Part 2 (representation labeling) [VERIFIED-tool]

Script: `e11_su2lr_representation_check.py`. Uses a SECOND generic symbolic
quaternion `h(y0,y1,y2,y3)` (same matrix family as `g(x)`, no unit-norm
constraint imposed) rather than a trig-parametrized rotation angle — the
identities under test (`(h⁻¹g)⁻¹=g⁻¹h`, `h(gh)⁻¹=g⁻¹`) are pure consequences
of matrix-inverse/associativity algebra, valid for ANY invertible matrices,
hence valid a fortiori on the unit-norm (genuine `SU(2)`) subfamily — this
made the computation purely rational-function algebra (no trig simplification
needed at all), fast and unambiguous.

```
verdict.core_setup_ok = true                          (quaternion-norm identity holds for both g,h)
verdict.psi0_is_SU2L_singlet = true                    (EXACT, trivially — psi^(0) has no g-dependence)
verdict.psi0_is_SU2R_doublet_not_singlet = true         (h*psi0 != psi0 for concrete h=(3,1,2,-1))
verdict.psi1_is_SU2L_doublet_not_singlet = true         ((h^-1 g)^-1 psi0 = g^-1(h psi0), != psi1(g) for concrete h)
verdict.psi1_is_SU2R_singlet = true                     (h*(gh)^-1*psi0 = g^-1*psi0 EXACTLY, for ALL h, ALL x)
verdict.clean_complementary_rep_pattern_found = true
verdict.label = "CLEAN_COMPLEMENTARY_REP_PATTERN_FOUND__SPECULATIVE_CONVENTION_DEPENDENT"
```

Concretely, `ψ⁽¹⁾`'s `SU(2)_R`-invariance is EXACT and holds identically for
ALL `x0..x3, y0..y3` (not merely at the concrete test point) — verified by
`sp.expand(psi1_action_R - psi1_at_g) == zeros(2,1)` with fully symbolic
arguments; this is the strongest of the four checks, a genuine algebraic
identity, not a numerical coincidence. `ψ⁽⁰⁾`'s `SU(2)_L`-invariance is
likewise exact for all `y0..y3` (trivially, since `ψ⁽⁰⁾` carries no
`g`-dependence at all to pull back).

**Clean summary table:**

| | SU(2)_L (left translation) | SU(2)_R (right translation) |
|---|---|---|
| `ψ⁽⁰⁾ = const` (t=0, exists for ALL sign/value of structure constant) | **exact singlet** | **doublet** (fundamental, nontrivial) |
| `ψ⁽¹⁾(x)=g(x)⁻¹ψ₀` (t=1, ONLY under `c0=−2`) | **doublet** (fundamental, nontrivial) | **exact singlet** |

This is a fully unambiguous, complementary (opposite) pattern between the two
spinors — Part 2's kill criteria (an accidental universal degeneracy at all
`h`, or the identity failing to hold for generic `h`) are both avoided
cleanly.

## Result — Part 3 (correspondence to S⁶'s chirality convention)

Cross-referencing against this project's OWN, ALREADY-FIXED conventions:
- `preprint.tex:304,332`: `SU(2)_L` doublet content = weak-isospin-charged =
  the standard Pati–Salam left-handed assignment; `SU(2)_L` singlet is
  explicitly used for the right-handed neutrino `ν_R`.
- `preprint.tex:906-908` (Lemma L5): "Matching the `S⁶` orientation convention
  to the SM convention for `SU(2)_L`, the left-handed Dirac zero mode
  corresponds to the left-handed SM fermion doublet."

Combining: `ψ⁽¹⁾` (the t=1 candidate) is an `SU(2)_L` **doublet** — EXACTLY
the representation content the paper's own convention (line 906-908) assigns
to "left-handed." `ψ⁽⁰⁾` (the t=0 spinor, the one that actually exists under
this project's own calibration for ALL structure-constant values) is an
`SU(2)_L` **singlet** — exactly the content assigned to "right-handed" (cf.
`ν_R` at line 332). **This is a clean, non-forced pattern match**: the t=1
candidate carries the SAME gauge-representation label the paper independently
calls "left-handed," and the t=0 spinor carries the "right-handed" label.

**This is reported as SPECULATIVE-ONLY, per the pre-registered criteria, for
three independent, stacked reasons — each individually sufficient to block
promotion to PASS:**

1. **The `SU(2)_L`=left-translation identification is an assumption, not a
   stated project convention.** Grepped the full `preprint.tex` text again in
   this experiment (searching "left-invariant," "right-invariant," "acts on
   the left/right," "translation") — confirms round74's Q3 finding: NO
   occurrence anywhere. The convention used here (round74's "only
   geometrically natural" framing) is imported, not derived from the paper.
   **If the convention is reversed** — `SU(2)_L`=right-translation,
   `SU(2)_R`=left-translation — every label in the table above flips: `ψ⁽⁰⁾`
   becomes the `SU(2)_L` doublet ("left-handed"-like) and `ψ⁽¹⁾` becomes the
   `SU(2)_L` singlet ("right-handed"-like) — i.e. the OPPOSITE correspondence
   to S⁶'s label. Nothing in `preprint.tex` or in this experiment's own
   computation can distinguish these two possibilities; the "match" found
   here is exactly as likely, a priori, as its own mirror-image mismatch,
   under the sole assumption that governs which is which.
2. **`ψ⁽¹⁾` exists ONLY under `c0=−2`, NOT under this project's own
   physics-calibrated `c=+2`.** Round76 Part 4 tool-verified that the SAME
   candidate `ψ=g(x)⁻¹ψ₀` FAILS (nonzero, generic residuals) under `c=+2`. No
   alternative candidate has been constructed or tested under `c=+2` anywhere
   in this project. Every statement above about `ψ⁽¹⁾`'s representation
   content describes an object that, under this project's own calibration,
   is not currently known to exist at all.
3. **No physical principle requires the eventual S³-factor zero mode to
   "match" S⁶'s left-handed label in the first place.** This would be an
   independent physical postulate (e.g., "the full 9D zero mode's S³-factor
   content must carry the same chirality label as its S⁶-factor content"),
   stated nowhere in this project. Moreover — and this is the more basic
   blocker — `preprint.tex:1421-1445` (KT-8) establishes that **no zero mode
   of the full 9D operator `D_full` currently exists at all** for the round,
   untwisted Levi-Civita ansatz used throughout the paper (`ker D_full = 0`
   identically); the torsion family where `t=0,1` live is explicitly
   characterized (`preprint.tex:1471-1495`) as "a candidate mechanism...
   physically unmotivated, not a resolution" with "no physical principle...
   for selecting `t=0` (or any other crossing) over the Levi-Civita value
   `t=1/2`." So even granting (1) and (2), the entire question of whether
   `t=0` or `t=1` is ever physically realized (H1c) remains completely open,
   and this experiment's finding is about representation content of spinors
   in a connection family that is not currently tied to any known physical
   zero mode of the operator this paper's physics actually depends on.

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result establishes, unconditionally [VERIFIED-tool]:** the pure
  representation-theory fact that constant sections in a left-invariant
  trivialization on `SU(2)` transform as an exact singlet under left
  translation and a genuine (nondegenerate) fundamental-representation doublet
  under right translation, and the specific spinor `g(x)⁻¹ψ₀` transforms with
  the exact OPPOSITE assignment — singlet under right translation, doublet
  under left translation. This is now a settled fact about THIS project's own
  constructions (E9's `ψ⁽⁰⁾`, round76's `ψ⁽¹⁾`), not merely a cited general Lie
  theory fact.
- **What this result rules out:** the possibility (left open by round74) that
  the spinor representation content might NOT mirror the vector-field
  singlet/doublet pattern round74 speculated about by analogy — it does
  mirror it, cleanly, with no ambiguity in either check.
- **What remains unresolved / open (unchanged from round74, restated
  precisely):** (a) whether `SU(2)_L`=left-translation is the convention this
  project should adopt — a bookkeeping choice never made in `preprint.tex`;
  (b) whether `ψ⁽¹⁾` exists under this project's own calibrated `c=+2` — it
  demonstrably does not, for the one candidate tried; (c) whether there is any
  physical reason the S³-factor zero mode (which does not currently exist at
  all, per KT-8) should carry S⁶'s "left-handed" label — no such reason is
  stated anywhere in this project.
- **Relaxation Map for the two live open items:** (a) is pure bookkeeping —
  cheapest possible next step, a one-line convention decision (or derivation,
  if one exists) for which `S³` translation direction is "`SU(2)_L`"; (b)
  requires either accepting `c0=−2` as this project's convention (with
  justification) or searching for a DIFFERENT `t=1` candidate spinor under
  `c=+2` (round76's own "Recommended next action," not attempted here or
  there); (c) requires either abandoning the `t=0/1` framing entirely (since
  KT-8 blocks it structurally) or resolving KT-8's blocking gap first — a
  substantially larger, unrelated open problem in this project.

## Assumptions (status)

| Assumption | Status |
|---|---|
| `SU(2)_L` acts on `S³` by LEFT translation, `SU(2)_R` by RIGHT translation | [WEAK] — round74's "only geometrically natural convention"; **confirmed again here, by direct grep, that `preprint.tex` never states this** |
| Left-invariant frame is invariant under left translation, transforms via `Ad(h)` under right translation | [DOCS] — standard Lie theory; reused from round76 Part 1 (there, [VERIFIED-tool] for the vector-field bracket sign), not re-derived here |
| Spinor components inherit the frame's transformation via the tautological `SU(2)` lift of the `Ad(h)` rotation (i.e. `ACTION_R(h,ψ)(G):=h·ψ(Gh)` is the correct combined action) | [INFERRED] — standard associated-bundle argument, stated explicitly in claim.md; the ALGEBRAIC CONSEQUENCES of this specific action definition are [VERIFIED-tool] here, but the definition itself (that `h`, not `h⁻¹` or some other lift, is the correct compensating factor) rests on general spin-geometry reasoning, not re-derived from a bundle-theoretic construction inside this project |
| `ψ⁽¹⁾=g(x)⁻¹ψ₀` is ∇¹-parallel ONLY under `c0=−2`, fails under `c=+2` | [VERIFIED-tool, round76 Part 4] — reused unchanged, restated as caveat (2) above |
| `SU(2)_L` doublet = left-handed, `SU(2)_L` singlet = right-handed (Pati–Salam convention) | [DOCS] — standard left-right-symmetric-model convention; also this project's OWN usage (`preprint.tex:304,332`) |
| No zero mode of the full 9D operator currently exists on the round Levi-Civita `S³×S⁶` ansatz; `t=0,1` live only in the physically-unmotivated torsion family | [DOCS, this project] — `preprint.tex:1421-1495`, restated as caveat (3) above |

## What this does NOT mean

1. Does **not** show `preprint.tex` commits to `SU(2)_L`=left-translation —
   confirmed again by direct grep that this is unstated; if the convention
   were reversed, every label in this decision flips.
2. Does **not** show `ψ⁽¹⁾` exists under this project's own calibrated
   connection (`c=+2`) — it demonstrably does not (round76 Part 4).
3. Does **not** establish any physical requirement that the S³-factor zero
   mode must match S⁶'s left-handed label, nor that such a zero mode
   currently exists at all (KT-8 blocking gap, untouched).
4. Does **not** resolve H1c, H2, H3, KT-3, or any open item in
   `preprint.tex §discussion`.
5. Does **not** claim novelty in the underlying representation theory — a
   constant section in a one-sided-invariant trivialization transforming as
   the fundamental representation under the opposite side's translation is
   standard, general Lie theory (see e.g. the general theory of
   left/right-regular representations on a compact Lie group). What is new
   here is the concrete, tool-verified check for THIS project's own specific
   spinor construction, and the honest three-part caveat audit of whether it
   connects to an existing convention (it does, cleanly, but only pending
   three unresolved/unstated assumptions).
6. Does **not** imply the "SPECULATIVE-ONLY" verdict is a weak or
   uninteresting result — round74 explicitly could not check whether spinors
   (as opposed to vector fields) inherit the singlet/doublet pattern; this
   experiment closes exactly that gap with a clean, unambiguous YES, while
   correctly declining to promote the larger physical correspondence, which
   depends on assumptions this project has not made.

## Pearl-registry candidate

One transferable insight, concrete enough to state as a falsifiable lesson
for future rounds in this line of work: **whenever this project builds a
spinor "constant relative to frame X" and asks how it transforms under a
DIFFERENT (opposite-handedness) isometry of the same space, the correct
combined action is pullback-plus-frame-compensation, NOT pullback alone** —
the compensation is absent for the SAME-handedness action and present for the
OPPOSITE one, and which is which follows directly from whether the frame
itself is invariant or rotates under that specific translation (checked here
concretely for `S³=SU(2)`'s left/right-invariant frames; the same reasoning
would apply to any future construction on a group manifold or coset space in
this project that builds one-sided-invariant trivializations). Impact score
~3 (narrow methodological point, useful mainly if this project revisits
`SU(2)_L×SU(2)_R` representation content for other S³-factor constructions) —
not registered to `pearl_registry/INDEX.md` as this is a project-internal
lesson already fully captured in this decision.md and claim.md, not a
cross-domain or high-impact structural finding.

## Summary table

| Sub-question | Verdict | Basis |
|---|---|---|
| Do `ψ⁽⁰⁾`, `ψ⁽¹⁾` transform as clean, definite `SU(2)_L×SU(2)_R` representations? | **PASS — clean, unambiguous, [VERIFIED-tool]** | `ψ⁽⁰⁾`: SU(2)_L singlet / SU(2)_R doublet. `ψ⁽¹⁾`: SU(2)_L doublet / SU(2)_R singlet. Both checked as exact symbolic identities (singlet cases) or confirmed-nontrivial-for-generic-h (doublet cases) |
| Does this labeling connect to S⁶'s already-fixed "left-handed" convention (`preprint.tex:906-908`)? | **SPECULATIVE-ONLY — a real, clean pattern match, explicitly NOT a PASS** | `ψ⁽¹⁾` (SU(2)_L doublet) matches "left-handed" exactly UNDER three stacked, unverified/unstated assumptions: (1) SU(2)_L=left-translation convention (unstated in `preprint.tex`), (2) `ψ⁽¹⁾` exists under `c=+2` (round76 found it does NOT, only under `c0=−2`), (3) a physical requirement that the S³ zero mode match S⁶'s label (unstated; also KT-8 blocks any S³-factor zero mode from existing at all in the current ansatz) |

## Why this is an honest SPECULATIVE-ONLY, not a forced PASS

Per this project's own methodology and the task's explicit instruction: a
computation that comes out clean does not, by itself, license promoting the
larger correspondence it was hoped to support. Part 2's representation-theory
computation is unambiguous and now [VERIFIED-tool] — this genuinely resolves
round74's blocking reason (2). But round74's reasons (1) and (3) are
independent of the computation just done and remain exactly as open as
before; a new tool-verified fact about representation content does not
retroactively fix an unstated convention or manufacture a physical postulate
that was never made. Reporting the clean pattern honestly, while explicitly
refusing to call it more than SPECULATIVE-ONLY, is the correct application of
this project's Anti-Overfitting Gate and Zero-Signal Gate discipline — the
computation adds real information (closing one of three gaps), it does not
close all three.

## Check (reproduces this decision)
`python e11_su2lr_representation_check.py` →
`verdict.core_setup_ok==true`, `verdict.psi0_is_SU2L_singlet==true`,
`verdict.psi0_is_SU2R_doublet_not_singlet==true`,
`verdict.psi1_is_SU2L_doublet_not_singlet==true`,
`verdict.psi1_is_SU2R_singlet==true`,
`verdict.clean_complementary_rep_pattern_found==true`,
`verdict.label=="CLEAN_COMPLEMENTARY_REP_PATTERN_FOUND__SPECULATIVE_CONVENTION_DEPENDENT"`.
