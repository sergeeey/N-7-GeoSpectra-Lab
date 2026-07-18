# Claim — Round107 (Codex items 2+3): SU(4)=Spin(6) Orbit of the Physical
Twisted Kernel Vector

**Question type:** Descriptive (a direct, tool-computable branching
question — is the physical zero mode an `SU(4)` singlet, or does it sit
in a nontrivial multiplet?).

## Section 1 — Background

Round93 (Part D) already constructed the FULL `so(6)=su(4)` action on the
8-dim `S6` spinor space `Σ` (15 generators, `so6_spin_gens`, via
`so6_generators()`+`lift_to_spinor()`, reused from `g10_s6_so6_gauge.py`/
`g11_block_generators.py`) and showed it closes into `S⁺=`"4"⊕`S⁻=`"4̄"
(chirality-preserving, tool-verified). Round94 constructed the physical
twisted kernel vector `k_vec` explicitly, in the 64-dim `Σ⊗Σ` fibre
(reusing round59's `v_a,v_b,leibniz64,D_full,herm`). Round92 established
the kernel is an `SU(3)_c` SINGLET (since it lies in the `G₂`-trivial
isotypic component, and `SU(3)⊂G₂`).

**What has NOT been checked anywhere in this project:** whether `k_vec`
is a singlet under the FULL 15-generator `SU(4)=Spin(6)`, or whether the
6 generators OUTSIDE the `su(3)⊕u(1)` subalgebra (round93 Part A.6 found
`B-L` does not commute with all 15 raw generators, but never applied the
FULL Leibniz-lifted `so(6)` action to `k_vec` itself) move it to a
linearly-independent vector — i.e., whether `k_vec` sits in the `SU(4)`
**singlet** ("1") or **adjoint** ("15") piece of the standard
`4⊗4̄=1⊕15` branching of `Σ⁺⊗Σ⁻`. This is Codex/round105's items 2+3,
directly addressing its flagged concern: "a `G₂`-trivial (hence
`SU(3)`-singlet) state cannot by itself represent a Pati-Salam `4`, whose
restriction is `3⊕1`... needs an explicit intertwiner."

## Section 2 — Method

1. Reuse round94's exact `k_vec` construction (`v_a,v_b`→`u1,u2`→
   `k_vec=alpha*u1+beta*u2`, `alpha=b_coeff=-√3`, `beta=-a_coeff=1`).
2. Reuse round93's exact `so6_spin_gens` (15 8×8 matrices on `Σ`).
3. Leibniz-lift each of the 15 generators to the 64-dim `Σ⊗Σ` fibre
   (reusing round59/94's own `leibniz64` function, applied here to `so(6)`
   generators instead of `su(3)` or `B-L` alone — the SAME reusable
   pattern flagged as a pearl in round94's own decision.md).
4. Apply each of the 15 Leibniz-lifted generators to `k_vec`; determine
   the dimension of `span{k_vec, G_1·k_vec,...,G_15·k_vec}`.

## Section 3 — Pre-registered criteria

- **SU(4) SINGLET (Pati-Salam-incompatible, confirms Codex's concern):**
  all 15 generators annihilate `k_vec` (span dimension 1) — the kernel
  is a genuine `SU(4)` singlet, structurally unable to represent
  Pati-Salam `4`/`4̄` matter, independent of and stronger than round92's
  `SU(3)`-singlet finding alone.
- **NONTRIVIAL SU(4) ORBIT:** at least one of the 6 "extra" generators
  moves `k_vec` to a linearly independent vector — the kernel sits in a
  larger multiplet (most likely the adjoint "15", given the standard
  `4⊗4̄=1⊕15` branching), still NOT a fundamental `4`/`4̄`, but a
  genuinely different (and structurally still Pati-Salam-incompatible,
  since matter must be in `4`/`4̄`, not the adjoint) finding.
- **BLOCKED:** the computation cannot be completed cleanly (e.g. basis/
  convention mismatch between round93's `Σ` ordering and round59's
  `SUBSETS` ordering).

## Section 4 — Escalation note

Per this session's now-standard practice for this exact research
territory (three prior self-corrections: rounds 102, 103, 106), this
round's conclusion goes through mandatory context-asymmetric skeptic
review before being reported as more than a hypothesis.
