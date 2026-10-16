# C144 — round59's untwisted Dirac operator IS Kostant's cubic Dirac operator (up to scale)

## L0 gate (EstimandOps)

**Question type:** Descriptive (algebraic identification of two operators) — NOT causal, NOT predictive.
This asks "are object A and object B the same object (up to a known scalar)?", not
"does A cause B" or "what will A be." No causal layer required.

## Trigger

User (2026-09-04) flagged, during a critique of C143's own Lemma 1, that Kostant's
cubic Dirac operator (B. Kostant, *A cubic Dirac operator and the emergence of Euler
number multiplets of representations for equal rank subgroups*, Duke Math. J. 100
(1999), 447–501) and its geometric form (G. Landweber, *Harmonic Spinors on
Homogeneous Spaces*, arXiv:math/0005056) might already establish, as known
mathematics, what C143 proved as a bespoke lemma — specifically for **maximal-rank**
pairs H⊂G (both same rank), which G2⊃SU(3) is (rank 2 = rank 2). This round is the
FIRST item of the queue authorized by the user's "го все по очереди" in response to
that flag — verifying the connection was named explicitly as higher priority than the
user's own remaining 9-item list.

## Falsifiable claim

Round59's own untwisted Dirac operator `D = Σᵢ eᵢ·NABᵢ` (built from the AHL2023
Remark 5.2 **Levi-Civita** Nomizu spin-connection operators, already independently
verified in `experiments/20260714-round59-trivial-rank-certification/`) is EXACTLY
proportional, as an 8×8 matrix, to the Chevalley quantization `c(ω)` of the
fundamental 3-form `ω(X,Y,Z) = ⟨X,[Y,Z]⟩` — i.e. to Kostant's algebraic cubic
correction term `v` in `Ð := Σᵢ Xᵢ⊗Xᵢ* + 1⊗v` — built from the SAME AHL2023
structure-constant data (the raw, unscaled coefficients underlying the Lam[i] table),
with no additional su(3)-sector (AD[k]) input needed.

**Kill criterion:** if `D` is NOT an exact scalar multiple of `c(ω)` (i.e. the
residual `D − α·c(ω)` is nonzero for every candidate scalar α, checked symbolically
on all 64 matrix entries), the claim is FALSIFIED — round59's construction would then
be only "structurally similar to" but not "an instance of" Kostant's operator, and
C143's Lemma 1/2 would stand as the primary framework (not superseded).

## What this does NOT mean

1. Does NOT (yet) establish that the TWISTED constructions (C139, C141, C142's
   `W_cand`) are literal instances of Landweber's twisted operator `Ð_μ`
   (`L²(G×_H(𝕊⊗U_μ))`) — that requires a separate check (same method, twisted
   setting) and is explicitly logged as an open follow-up, not claimed here.
2. Does NOT establish the specific numeric value Kostant's closed-form kernel
   formula (`Ð²|_{U_μ} = ‖λ+ρ_G‖² − ‖μ+ρ_H‖²`) would predict for round59's block —
   only the ALGEBRAIC IDENTIFICATION (operator ≅ operator up to scale) is checked
   here, not an independent root-system Casimir-norm cross-check.
3. Does NOT change `N_gen=3`'s CONDITIONAL status. Round59's kernel dimension
   (=1) was already established; this round explains WHY via a general theorem
   rather than a bespoke construction — it does not change the number.
4. Does NOT retract C143's Lemma 1/2 — they remain correct and useful as the
   FIRST-PRINCIPLES (Schur's-lemma-based) explanation reachable without invoking
   Kostant's theorem. This round adds a MORE GENERAL, previously-unconnected
   explanation for the SAME untwisted-block phenomenon (see Mechanism-Transfer
   note in decision.md).
5. **(added post-skeptic, 2026-09-04) Does NOT independently confirm, beyond what
   AHL2023's own already-verified Killing-spinor calibration (round59 Step 1)
   already established, that this specific geometry is "special."** The STEP 4
   proportionality (`D == (√3/4)c(ω)` on all 64 entries) is **algebraically
   forced** by STEP 2 (total antisymmetry of the raw Nomizu-table structure
   constants) plus the absence of repeated indices in any `Lam[i]` entry — and
   total antisymmetry of the `m`-bracket is itself a GENERIC consequence of using
   an Ad-invariant form to build a naturally reductive metric (not a G2/SU(3)-
   specific fact). Skeptic-verified (2026-09-04, context-blind pass): a
   coherent, antisymmetry-preserving sign perturbation of `Lam` still produces
   `D == (√3/4)c(ω)` even though it would BREAK the Killing-spinor calibration
   in Step 1. So STEP 4 tests only "is this a genuine naturally-reductive Nomizu
   table" (already tested, more specifically, by Step 1's calibration) — it is
   NOT independent per-geometry evidence that round59's operator is a
   *surprising* instance of Kostant's construction. The algebraic identity
   itself (`D = (√3/4)c(ω)`) is still correct and still establishes that
   Kostant/Slebarski's FRAMEWORK genuinely applies to this project's Dirac
   operators — that part is real and useful. What is corrected here is only the
   INTERPRETIVE weight the original framing gave to STEP 4 specifically.

## Novelty check (source trace, per FL AI-Hypothesis Pre-Gate)

Both papers verified as real via WebSearch + `mcp__arxiv__get_abstract` +
`mcp__arxiv__get_paper_latex` (full LaTeX source read, not abstract-only):
- Kostant 1999, Duke Math. J. 100, 447–501 — cited inside Landweber's own
  bibliography (`\bibitem{K}`), confirmed present.
- Landweber, arXiv:math/0005056 — fetched directly, all 4 sections read in full
  (~25,000 chars of LaTeX, not summary).
Neither paper is already cited anywhere in this project's `experiments/` tree
(checked: no prior round references Kostant, Landweber, or "cubic Dirac" by name).
