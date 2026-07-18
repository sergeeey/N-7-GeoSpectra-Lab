# Claim — Round106: Codex's Item 7 Follow-Up (Spin-Level `ι`-
Equivariance, Attempted Properly)

**Question type:** Descriptive (completing round101's own flagged gap,
per Codex/round105's item 7: "compute the missing `U⁻¹dU` inhomogeneous
term — a finite symbolic calculation").

## Section 1 — Background

Round101 found the NAIVE component-substitution
`Ω_i^R(t)(x):=Σ_j b_i^j(x)Ω_j(t)` is `x`-dependent, and attributed this to
a missing inhomogeneous (Maurer-Cartan-type) term in the connection
pullback formula. Round105 (Codex cross-review) called completing this
"a finite symbolic calculation," the cheapest of its 8 proposed next
steps.

## Section 2 — What this round attempts, precisely

1. **Verify `b(x)` is literally the matrix of `Ad(g(x)⁻¹)`** in the
   `{Z_i}` basis (i.e. `Σ_j b_i^j(x)Z_j = g(x)⁻¹Z_i g(x)` exactly) — this
   was implicit in round80's own construction but not stated/verified as
   such explicitly.
2. **Re-examine what the naive `Σb·Ω` computation actually IS**: since a
   connection 1-form `ω^t` is LINEAR in its vector argument at each
   point, `ω^t(Z_i^R) = ω^t(Σ_j b_i^j(x)Z_j^L) = Σ_j b_i^j(x)ω^t(Z_j^L) =
   Σ_j b_i^j(x)Ω_j(t)` — meaning round101's "naive" computation is, in
   fact, the CORRECT value of `ω^t` evaluated at `Z_i^R`, by linearity
   alone, not an incomplete/naive shortcut. The genuine subtlety is
   elsewhere: pulling back a CONNECTION (not just evaluating a 1-form at
   a different vector) additionally requires identifying/transporting
   the FIBER via the spin lift of `ι`'s OWN action on spinors — a
   different, so-far-unaddressed piece.
3. **Check the actual physically-relevant object directly**: E9/round73's
   own Dirac-operator formula, `D^t(ψ)=Σ_iZ_i·Z_i(ψ)+t·H·ψ`
   (`H=(3c/2)·ω`), for CONSTANT spinors (`Z_i(ψ)=0`), reduces to
   `D^t(ψ)=t·H·ψ`. Verify whether `H` is a scalar multiple of the
   identity (E2's own established fact, `ω=Z_1Z_2Z_3=I_2` exactly) —
   if so, `D^t` acts as PURE SCALAR multiplication `t·(3c/2)` on constant
   spinors, and check what this implies for whether ANY spin-lift
   conjugation could relate the `t` and `1-t` eigenvalues.

## Section 3 — Pre-registered criteria

- **COMPLETED:** a correct, full spin-level pullback formula (including
  the fiber/spinor-transport piece) is constructed and directly checked
  against `Ω_i(1-t)`.
- **PARTIAL, GENUINE SHARPENING:** the linearity point (step 2) and the
  scalar-`H` point (step 3) are established, giving real new information
  about WHY the naive approach cannot work and WHAT would be needed for
  a full treatment — without claiming the full spin-lift construction is
  completed, if genuine ambiguity remains about how `ι` acts on which
  spinors are "constant" in which frame.
- **BLOCKED:** neither of the above is achieved cleanly.

## Section 4 — Escalation note

Given this session's established pattern (two of three prior attempts at
"finishing" a hard question in this exact research line required
correction after skeptic/Codex review), this round's conclusion goes
through the same context-asymmetric skeptic review before being reported
as more than a hypothesis, regardless of which pre-registered outcome is
reached.
