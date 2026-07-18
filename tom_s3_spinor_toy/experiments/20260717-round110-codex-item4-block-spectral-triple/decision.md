# Round110 (Codex item 4) — Decision

**Date:** 2026-07-17
**Verdict:** `WEAKENED__CORRECTED_TO_PROPER_BLOCK_SWAP_QUESTION__NO_EXCHANGE_SYMMETRY__PRESENTATIONAL_NOT_INDEPENDENT_EVIDENCE`
(skeptic verdict)
**Go/no-go:** the block spectral triple `D_block=diag(D^0,D^1)` is a
well-defined, self-adjoint, finite-dimensional construction; no
block-exchange symmetry relates it to itself. **Honest downgrade,
skeptic-driven:** this round does NOT supply independent evidence beyond
round106 — it restates round106's own two established facts in explicit
NCG/block-spectral-triple language, which has organizational/
presentational value (directly answers Codex's own item-4 checklist) but
should not be cited as a fresh confirmation.

## What was computed [VERIFIED-tool: sympy]

1. `D_block=diag(0,0,3c/2,3c/2)` (4×4), reusing E9's own established
   `H=(3c/2)·ω` (scalar, `ω=Z₁Z₂Z₃=I₂`). Self-adjoint, confirmed.
2. Finite-dimensional NCG-axiom triviality, stated explicitly per Codex's
   own checklist: bounded (any finite matrix is a bounded operator) and
   compact resolvent (any finite matrix has discrete spectrum) — NOT
   deep content, honestly scoped as an artifact of this project's own
   finite/discrete modeling choice, not a claim about the intended
   full, continuum `L²(S³)` triple.
3. **Codex's own explicit question, "whether a symmetry exchanges the
   two blocks" — corrected after skeptic review, see below.**
4. Minimal diagonal algebra `A=ℂ⊕ℂ` commutes trivially with `D_block` —
   flagged honestly as tautological by construction (both objects are
   block-diagonal in the same split), not a substantive finding; any
   physically interesting first-order-condition/off-diagonal structure
   needs a richer algebra this project has not specified.

## Correction, per skeptic review [both points accepted, not dismissed]

**First-draft error:** tested whether a unitary `U` satisfies
`U·D^0·U⁻¹=D^1` directly, using an eigenvalue-preservation argument.
**Skeptic correctly identified this as the WRONG question, needlessly
elaborate for something trivial:** since `D^0=0` (the zero matrix),
`T·0·T⁻¹=0` for literally ANY invertible `T` (unitary or not) — the
eigenvalue-preservation flourish was decorative, not informative, for a
fact that's immediate. **The physically meaningful question is whether
a symmetry `S` acting on the FULL 4-dim `H_block` exchanges the two
`ℂ²` blocks as a PAIR** (`S·D_block·S⁻¹=D_block`, with `S` permuting the
summands) — **fixed and re-computed**: the explicit block-swap unitary
`S=[[0,I₂],[I₂,0]]` gives `S·D_block·S⁻¹=diag((3c/2)I₂,0)≠D_block` —
confirming NO block-exchange symmetry, but via the CORRECT formulation
this time, independently computed by the skeptic by hand before I
re-ran it.

**Second correction, per skeptic review:** the claim that this round
supplies "a genuine cross-check via a different framing" of round106's
finding was **overreach** — both round106's scalar argument and this
round's block-swap computation rest on the SAME two established inputs
(`H` is a scalar; `D^0=0` at `t=0`, `D^1=(3c/2)I₂` at `t=1`). Re-feeding
the same inputs into a differently-worded question is a RESTATEMENT in
NCG/block-spectral-triple language (useful because it directly and
correctly answers Codex's own item-4 checklist item), not independent
confirming evidence. Downgraded accordingly, per skeptic's own
recommendation, not smoothed over.

## Applying the pre-registered criteria (claim.md Section 4)

**NO EXCHANGE SYMMETRY**, exactly as pre-registered — but the
pre-registered framing ("a genuine cross-check via a different route")
is corrected to "a presentational restatement," per the skeptic response
matrix.

## Kill Analysis

- **What this kills:** the FIRST-DRAFT wrong-question formulation
  ("conjugate `D^0` into `D^1` directly") — replaced with the correct
  block-swap question, both giving the same (negative) answer but only
  the second is the right thing to have checked.
- **What this does NOT kill:** round106's own finding (reused, not
  re-derived); round103's own general "block construction is legitimate"
  argument (untouched — this round confirms the construction is
  well-defined, just shows it has no block-exchange symmetry).
- **What survives:** Codex's item-4 checklist is now directly and
  correctly answered (construction built, basic properties confirmed,
  swap-symmetry question correctly posed and answered) — but the
  ALGEBRA/real-structure/off-diagonal-coupling/first-order-condition/
  spectral-action-coefficient parts of the SAME checklist remain
  genuinely open, honestly not attempted with invented, unjustified
  choices.

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Specify a richer algebra `A` (beyond `ℂ⊕ℂ`) with genuine off-diagonal/first-order-condition content | A new physical modeling choice this project has not made — substantially larger undertaking |
| Construct an explicit `D_F`-type off-diagonal coupling term between the two blocks and check self-adjointness/spectral-action consequences | Requires a physical motivation for what such a term should represent — not attempted here |
| Full Seeley-DeWitt/spectral-action coefficient computation for `D_block²` | Round99/Codex-item-6's own still-open task, not this round's scope |

## Assumptions carried, unresolved

- `H=(3c/2)I₂` (E9) and `D^t=t·H` on constant spinors (round106) — both
  reused unchanged.
- Whether the finite, constant-spinor model used throughout this
  project's `t`-family work is an adequate stand-in for the FULL,
  continuum spectral triple Codex's checklist literally describes — not
  independently re-examined here.

## What this does NOT mean

1. Does NOT supply independent confirmation of round106's finding — an
   honest downgrade, per skeptic review.
2. Does NOT resolve the algebra/real-structure/off-diagonal-coupling
   questions Codex's item 4 also asked about — genuinely open.
3. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`. Does NOT modify `preprint.tex` or any prior
   experiment folder.

## Check (reproduces this decision)

```
cd experiments/20260717-round110-codex-item4-block-spectral-triple
python e33_block_spectral_triple.py
```
Expect: `D_block_self_adjoint=True`, `S_block_swap_is_unitary=True`,
`block_swap_is_symmetry_of_D_block=False`,
`minimal_diagonal_algebra_commutes_trivially=True`.
