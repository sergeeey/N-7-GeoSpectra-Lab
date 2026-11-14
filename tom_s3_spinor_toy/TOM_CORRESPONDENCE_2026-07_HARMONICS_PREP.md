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

---

# ADDENDUM — the 2026-09-07 message and this project's response (C179-C181)

**Status: internal. NOT sent. Submission Gate NOT passed.** Same standing
"DO NOT INITIATE CONTACT" constraint as the note above — Tom initiated
this exchange himself; nothing here has been returned to him.

## What arrived

Tom's email of 2026-09-07 plus an 18-page attachment, *"Ket spaces and
harmonics of S^n"* (`Notes to Sergey re harmonics v5.pdf`, read in full
this session). He states that the notes were prompted by **our own notes
of 3 August**, and names the specific correction they caused:

> "My main mistake immediately prior to this was in assuming that the
> representation of SO(n+1) acting on the vector multiplet is the defining
> representation. Actually, it's the 'dual representation' ... given by
> taking the inverse (or equivalently, the transpose)."

**Provenance chain, now closed:** that is precisely the artifact this
project isolated on 2026-07-28 in
`experiments/20260728-tom-so3-harmonics-sign-check/TRANSPOSE_LEMMA.md`
("the honestly-built matrix `M` satisfies `M = T^T` ... NOT `M = T`"),
which produced his `L_x = -T'_x` sign discrepancy. Our note -> his
correction -> his new general framework.

## What he asked for (the two italicised passages he pointed at)

- **Section 1.4, italic:** his eqs (72)/(77) "could be crucial to finding
  the harmonics for the spinor multiplets".
- **Section 3.3, italic (the actual ask):** harmonics of `S^2` forming a
  basis for a **two-component spinor**, then harmonics of `S^3` for a
  **four-component spinor**; a proposed verification (outer product of the
  spinor multiplet with its adjoint, gamma-projected to the vector
  multiplet); then eigenfunctions in Riemann normal coordinates, giving a
  local section of a true local spinor field.

## What this project established in response

| Round | Verdict | Content |
|---|---|---|
| **C179** | `NOGO-CONFIRMED-AND-DIMENSION-TRAP-CONFIRMED`, skeptic `CONFIRMED-REAL` | A spinor multiplet of **ordinary functions** cannot exist, for `S^2` or `S^3`. Proved inside his own eqs (4) and (40): a `2*pi` rotation is `+Id` on functions (measured: point shift `3.3e-16`, function-value change `1.8e-15`) but `-Id` on spinors (exact), forcing `Phi = -Phi`. This resolves the `[*check*]` marker on his own section 2.2. **Dimension trap:** `dim(1/2,1/2) = dim[(1/2,0)+(0,1/2)] = 4`, so a dimension count gives a FALSE PASS on `S^3`; only the kernel-element phase (`+1` vs `-1`) discriminates. Skeptic supplied a second independent proof for `S^3` (Peter-Weyl: `L^2(G)` contains only diagonal `(j,j)` blocks). |
| **C180** | `BOTH-CONFIRMED-PLUS-CONNECTION-CONSTANT` | The construction he wants, built explicitly for `S^3` in the group (parallelizing) trivialization. Spectrum at `k=0..3` reproduces the established `S^3` Dirac degeneracy `(k+1)(k+2)` / `k(k+1)` exactly. **The spin-connection constant `3/2` was SOLVED FOR, uniquely, from seven independent (eigenvalue, multiplicity) pairs -- not supplied.** Also verifies his eq (77) for the `S^3` VECTOR multiplet under his own convention (exactly one of three candidate conventions works, and it is his) -- an `n=3` extension his own section 3 does not carry out. |
| **C181** | `PROJECTION-WORKS-BUT-DOES-NOT-DISCRIMINATE` | His item-4 verification recovers the vector multiplet exactly (`x_mu = (1/2)Tr(sigma_mu^dag g)`, error `0.0`) -- **but it does not discriminate**: an alternative built from the opposite chirality, a genuinely different operator, passes the identical test. Necessary, not sufficient. **Wording correction:** `psi psi^dag` for ONE chirality has an invariant trace (`3.6e-15`), so it reduces as `1 + 3` and is NOT the irreducible `SO(4)` vector; that requires one index from EACH chirality, `(1/2,0) (x) (0,1/2)`. Riemann normal coordinates verified (`g(0)=delta` on 5 exact directions, all 9 first derivatives vanish identically). |

## The strategic point to carry into any reply

**The order he proposed should be inverted.** `S^2` is not parallelizable
(its spinor bundle is non-trivial); `S^3 = SU(2)` is. So the `S^3` case is
the tractable one and `S^2` should be obtained by descent from it at fixed
`U(1)` weight, not attacked independently first.

## Side effect on this project's own record

C180's construction is an **independent cross-check of round67's own
multiplicity claim**, which round67's `claim.md:73` marks `[INFERRED]` and
explicitly flags as *"not independently cross-checked against a second
source."* C180 supplies that second source, by a different method
(quaternionic vector fields on harmonic polynomials vs. Peter-Weyl matrix
elements).

## Open / not done

- `S^2` spinor harmonics: NOT built (should come by descent from `S^3`).
- The local spinor field itself (his item 5's endpoint): only the
  coordinate groundwork is done, the harmonics were not transported into
  those coordinates.
- **Transcription fidelity of his eqs (61)/(77)/(89)/(99) has been
  re-checked against the PDF by this session, but the skeptic could not
  verify it independently and named it as the one residual risk a
  self-check is weakest against -- it wants a human re-read before
  anything is sent.**
- Submission Gate (`integrity.md`) NOT run. Nothing drafted for sending.

## Sources

- `Notes to Sergey re harmonics v5.pdf` (Tom, 2026-09-07, 18pp, read in full)
- `experiments/20260907-c179-spinor-multiplet-of-functions-nogo/`
- `experiments/20260907-c180-explicit-s3-spinor-harmonics/`
- `experiments/20260907-c181-gamma-projection-and-normal-coordinates/`
- `experiments/20260728-tom-so3-harmonics-sign-check/TRANSPOSE_LEMMA.md` (the provenance)
