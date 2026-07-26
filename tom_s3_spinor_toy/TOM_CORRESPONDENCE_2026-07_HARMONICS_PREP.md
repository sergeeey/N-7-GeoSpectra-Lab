# Prep note: this project's S3-harmonics chain vs Tom Lawrence's own framing

**Purpose:** Tom's message (2026-07, post-Part-4) describes his own,
independently-derived framing of harmonics on S3 and the massless-Weyl to
massive-Dirac transition, and previews a technical concern about "your
proposed solution to my problem with the harmonics on S3." This note maps
his stated framing onto this project's own already-established results
(round72-78, the E7-E12 chain, OB9 consolidation) so a future response can
cite precisely, not re-derive under time pressure. **Not sent to Tom. Not
a response draft.** Internal reference only, per this project's standing
"DO NOT INITIATE CONTACT" constraint.

## Tom's own framing (his words, paraphrased for internal use)

- S3 represents the spatial universe at a fixed moment of cosmic time;
  harmonics on it are field configurations with no dependence on that
  time coordinate.
- The 4 spinor components are distinguished by two quantum numbers:
  chirality and "extended isospin" — no explicit spin.
- SM fermions, by contrast, live in a local frame with explicit time
  dependence, and exist in two forms: massless (before Higgs, obeying a
  Weyl equation for two doublets, identical helicity/chirality) and
  massive (after Higgs, obeying the Dirac equation, carrying both spin
  and chirality).
- He has derived a Dirac equation in his own model and wants to check its
  reduction to the Weyl equation in the massless limit.

## What this project already has that maps onto it

| Tom's concept | This project's closest result | Status |
|---|---|---|
| "Harmonics on S3, cosmic-time-independent" | The nabla^t family of Cartan-Schouten connections on S3=SU(2), parametrized by torsion `t` | round72/E7 — flatness at t=0,1 PROVED (C23) |
| "Chirality + extended isospin, no explicit spin" | SU(2)_L x SU(2)_R representation content of the S3-side spinors: t=0 spinor = SU(2)_L singlet / SU(2)_R doublet; t=1 spinor = SU(2)_L doublet / SU(2)_R singlet | round77 — clean, unconditional PASS on the representation labeling itself (C26); the *physical* correspondence to a chirality label is explicitly SPECULATIVE (3 stacked assumptions, see C26's notes) |
| Massless harmonic -> massive Dirac reduction | Not directly attempted in this project. This project's zero modes ARE massless (kernel of D^t), and there is no Higgs-mechanism step connecting them to a massive 4-component field anywhere in the current construction | Genuinely open on our side — Tom's question is, if anything, ahead of where this project's own S3-factor construction currently reaches |
| "4 spinor components" | This project's S3-side kernel is 2-complex-dimensional (C27), not 4 — an SU(2) doublet, not a full Dirac fourplet | **Mismatch worth naming explicitly if this is ever discussed:** Tom's harmonic decomposition already speaks of a 4-component object; this project's own S3-side zero mode is a 2-component SU(2) doublet at a single t, and per C27 (round78/E12) is *itself* already flagged as double the expected multiplicity relative to a single generation slot |

## The single most important thing to carry into any future exchange

**This project's own S3-side "zero mode" is not yet a clean, single
physical object.** Per C27 (round78/E12, REFUTED-as-stated), the kernel
of D^t at t=0 (or t=1, under a specific sign convention) is
2-dimensional, not 1-dimensional — an SU(2) doublet, not one state. If
Tom's own harmonic analysis independently arrives at a 4-component
structure with definite chirality + isospin quantum numbers, and asks how
our own S3-side construction's representation content compares, the
honest answer is: **our own 2-dimensional doublet is itself an
unresolved multiplicity, not a settled building block** — presenting it
as clean would misrepresent this project's own already-documented
uncertainty (OB9/C27, `experiments/20260717-round78-e12-multiplicity-
gate/decision.md`).

## Also open, independent of the above

Which of t=0 or t=1 (not both) is physically realized remains OPEN (C25,
H1c) — no equations-of-motion or anomaly argument in this project selects
one over the other, and a later symmetry (round80/E14's `iota` isometry)
suggests they may even be the same physics in different coordinates
rather than two independent sectors.

## Sources (all internal, all read in full for this consolidation)

- `experiments/20260717-round72-e7-t-selection-principle/decision.md` (H1a/H1b/H1c split, flatness proof)
- `experiments/20260717-round73-e9-explicit-parallel-spinor/decision.md` (explicit t=0 spinor)
- `experiments/20260717-round74-e10-chirality-sign-link/decision.md` (chirality/orientation scoping, OPEN)
- `experiments/20260717-round75-e11-freund-rubin-torsion-link/decision.md` (flux-torsion structural link, OPEN)
- `experiments/20260717-round76-e9followup-right-invariant-frame/decision.md` (explicit t=1 spinor, sign caveat)
- `experiments/20260717-round77-su2lr-correspondence-test/decision.md` (SU(2)_L/R representation pattern)
- `experiments/20260717-round78-e12-multiplicity-gate/decision.md` (multiplicity-2 FAIL)
- `experiments/20260717-round80-z2-left-right-symmetry-search/decision.md` (iota isometry cross-check)
- `CLAIM_LEDGER.yaml` (C22-C27), `DERIVATION_GRAPH.yaml` (D4) — this consolidation's own formal entries
