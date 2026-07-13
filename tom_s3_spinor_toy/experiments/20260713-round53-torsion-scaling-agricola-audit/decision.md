# Round53-TorsionScaling Decision

**Date:** 2026-07-13
**Verdict: PARTIAL** — one of two torsion-correction pieces gets real
theoretical grounding from existing literature; the other remains
genuinely open, with a sharper, more tractable next question identified

## Summary

Read I. Agricola's 2002 paper in full (the correct file —
`Agricola_2002_naturally_reductive_Dirac.pdf` is mislabeled and is
actually an unrelated Okounkov-Pandharipande paper; flagged, not fixed,
out of this round's scope). Her **Theorem 3.2** gives the general,
*exact* (not asymptotic) formula for `(D^t)²` on any naturally reductive
`G/H`:

```
(D^t)²ψ = Ω_g(ψ)
        + (1/2)(1-3t) Σ ⟨[Z_i,Z_j]_m, Z_k⟩ Z_i·Z_j·Z_k(ψ)     [degree-3, the "torsion cross-term"]
        - (1/2) Σ ⟨Z_i, Jac_h(...) + 9t² Jac_m(...)⟩ Z_i·Z_j·Z_k·Z_l·ψ  [degree-4]
        + (1/8) Σ Q_h([Z_i,Z_j],[Z_i,Z_j])ψ + (3/8)t² Σ Q_m(...)ψ  [degree-0 scalars]
```

**Key structural fact, verified directly from the theorem's own form**:
every torsion-dependent piece is built from the FIXED structure
constants of the FIXED n=6-dimensional space m (basis Z_1..Z_6), acting
via Clifford multiplication on the FIXED spinor fiber Δ_m — while only
`Ω_g` (the Casimir operator) acts on the GROWING Peter-Weyl multiplicity
space V_λ. On the full Hilbert space `Δ_m ⊗ V_λ`, this means the torsion
pieces act as `(fixed matrix) ⊗ (identity on V_λ)` — and `‖A⊗I‖=‖A‖`
regardless of `dim V_λ`. **This is a genuine, general, already-published
theorem showing the torsion piece is representation-INDEPENDENT (not
merely slower-growing) — stronger than what this round's frozen claim
asked for.**

## Where this breaks down for this project's actual operator

This project's L4B operator (`D_{S^6}⊗S^-`) is not literally Agricola's
bare `D^t` — it's TWISTED by the auxiliary bundle `S^-=T^{1,0}S^6⊕1`,
and Round 22's own explicit ρ=7 construction (`decision.md:3332-3343`)
splits `D_7²` into five pieces, two of which are the relevant
"correction" terms:

1. **TORSION-CROSS-TERM** — built purely from "the already-built
   torsion table T(p,q,r)" (`decision.md:3340-3341`). This is exactly
   the fixed-structure-constant object Agricola's theorem describes —
   **this piece has genuine theoretical grounding for representation-
   independence.**
2. **MIXED-A-B-CROSS-TERM** — built "from T_A.T_B + T_B.T_A, an
   anticommutator {e_p,D64} contracted against rho_7(e_p)"
   (`decision.md:3342-3343`, verified by direct read, not paraphrase).
   **`ρ_7(e_p)` is the representation matrix of generator `e_p` ON
   V_7 — this term explicitly, structurally depends on which
   representation ρ is being used, and does NOT have the clean
   `(fixed)⊗(identity)` form.** This piece arises specifically because
   the operator is twisted (it comes from `TERM_A·TERM_B+TERM_B·TERM_A`,
   i.e. the cross-term between the base-geometry piece and the twist
   piece) — Agricola's bare, untwisted theorem has no analog of this
   term at all, so it provides zero guidance on how it scales with ρ.

## Kill Analysis

**What was tested:** whether Agricola's already-cited general theorem
resolves Round 52's parked sub-claim (B) (torsion-correction
boundedness) either fully or via a derivable general bound.

**What was killed:** the hope that Agricola's theorem cleanly resolves
the WHOLE torsion-correction question. It does not — it only covers the
piece of this project's construction that has no twisting-dependence.

**What was NOT killed, and is new, positive ground gained:**
- The TORSION-CROSS-TERM piece now has genuine theoretical justification
  for representation-independence (not just intuition) — a real
  strengthening of the preprint's own existing hedge language
  (`preprint.tex:740-741`, "the torsion correction is a fixed, bounded
  algebraic operator on the fibre (independent of ρ)" — this claim was
  asserted without proof before; it is now partially, honestly
  justified for the TORSION piece specifically, via a citable theorem).
- The genuinely open question is now sharply localized: not "the whole
  torsion correction, unknown," but specifically "does `‖ρ_ρ(e_p)‖`
  (operator norm of a fixed Lie-algebra generator on a growing
  irrep ρ) admit a general bound in terms of `C₂(ρ)`?" — a standard-
  shaped Lie-theory question, not equivalent to building the full
  Dirac-operator matrix for any specific ρ.

**Relaxation Map:**
A. Derive or look up a general bound `‖ρ_ρ(X)‖ ≤ f(C₂(ρ))` for a fixed
   Lie algebra element X acting on irrep ρ of a compact group — this is
   closer to standard representation theory than to this project's own
   novel constructions, and may already exist in the literature
   (operator-norm-vs-Casimir bounds for compact Lie group
   representations are a known topic, not investigated in this round).
B. Build a second explicit per-ρ construction (e.g. ρ=27) specifically
   to measure how `MIXED-A-B-CROSS-TERM`'s norm compares to `ρ=7`'s
   — the "second data point" option Round 52 already named, now with a
   sharper target (isolate MIXED-A-B specifically, not the whole
   torsion correction) rather than a full from-scratch computation.
C. Accept the status quo (ρ=7 established, ρ=14 strongly supported,
   remaining ρ formally open with a stronger-than-before but still
   incomplete theoretical hedge) and move on.

## Recommendation

Update `L4B-HIGHER-REPS`'s parked entry (do not un-park — the practical
conclusion is unchanged: the higher-reps sweep is still not licensed to
proceed) with the sharper revival condition below, replacing the
Round-52-era generic one.

## Scope discipline check

No Dirac-operator matrices built for any ρ (per explicit user
constraint, both this round and Round 52). `preprint.tex` not touched —
this round's finding could, in principle, motivate a future citation-
only strengthening of the `preprint.tex:740-741` hedge (citing
Agricola's Thm 3.2 for the TORSION piece specifically), but that is a
separate, small editorial action not taken here without explicit
confirmation, consistent with this project's "one round, one
deliverable" discipline.

## Files

- `claim.md` — this round's FL Standard-tier artifact
- No script — pure literature + structural cross-check, no numeric
  computation performed or needed for this round's conclusion.
