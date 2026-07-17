# E12 (round78) — Decision

**Date:** 2026-07-17
**Verdict:** `FAIL_MULTIPLICITY_2_CONFIRMED__NO_NATURAL_PROJECTION_FOUND`
**Go/no-go:** This is a **real, unresolved problem for the torsion-escape-route
program** (E2/E3/E7/E9/E9-followup). It is NOT resolved here, and no attempt is
made to manufacture a resolution. Read this decision in full before citing any
part of E2/E3/E7/E9/E9-followup as "the zero mode" without the caveat below.

## Bottom line, stated plainly first

`dim_C ker(D_{S3, t=0}) = 2`, confirmed by two independent tool-verified
routes (Peter–Weyl representation theory, Section A; direct symbolic
re-construction, Section B). The same holds at `t=1` in the right-invariant
frame under the concrete `c0=-2` sign convention (Section B). Combined with
`dim ker(D_{S6,twisted}) = 1` per channel (G74A, already PROMOTE) and the
tensor-product kernel identity for a decoupled sum-of-squares operator
(verified concretely on a toy example, Section C), this gives
**`dim ker(D_full) = 2` per triality channel, `6` total across the 3 channels
— not the `3` the torsion-escape-route program needs.** No Majorana/reality
condition, no orbifold projection, and no already-established
gauge-multiplet-counting convention in this project currently resolves this
gap. **The frozen claim ("exactly one physical internal mode per S⁶ zero
mode") is FALSE as stated**, pending a genuinely new physical input this
project does not currently have.

## Result, section by section

### Section A — independent Peter–Weyl derivation [VERIFIED-tool]

Built `X_i^{(j)} := 2i·J_i^{(j)}` (standard spin-`j` angular-momentum
matrices), verified `X_i^{(1/2)} = Z_i = i·σ_i` exactly
(`sanity_X_half_equals_Z = true`), then diagonalized
`D^{1/2}|_{V_j⊗ℂ²} = Σ_i X_i^{(j)}⊗Z_i + (3/2)·I` for `j = 0, 0.5, 1, 1.5, 2, 2.5`.

At `j=0` (the n=0, constant-spinor level): eigenvalue `+1.5` with multiplicity
**2**, exactly `(0+1)(0+2)=2` — this reproduces E2's own claimed n=0
multiplicity **independently**, not by trusting E2's citation
(`n0_multiplicity_matches_(n+1)(n+2)_at_n=0 = true`).

**Honest side-finding, reported not covered up:** the SAME naive extension of
Agricola's `D^{1/2}ψ=ΣZ_i·Z_i(ψ)+(3/2)ψ` formula to `j=0.5` gives eigenvalues
`{0.5 (mult 3), 4.5 (mult 1)}` — this does NOT match the expected
`±(1+3/2)=±2.5` with multiplicity `(1+1)(1+2)=6` for the n=1 level. This
mismatch is real and unresolved by this experiment; it is consistent with
E2's own claim.md already flagging the n=0→n≥1 extension as
`[DEDUCTION, low-risk]`, not independently verified. **It does not weaken the
n=0 finding**, which is the only level this experiment's physics question
(t=0,1 crossings) depends on, and which is independently confirmed by Section
B's completely different method. The general `(n+1)(n+2)` formula for n≥1 is
separately corroborated by standard literature (Hitchin 1974; Bär 1996;
Camporesi & Higuchi 1996 — the same Camporesi-Higuchi reference already used
in this project's own G74A/E4 chain, for S⁶ rather than S³), marked
`[DOCS/WEAK]` since these papers were not re-fetched this session.

### Section B — self-contained kernel re-verification [VERIFIED-tool]

At `t=0`: `Ω_i(0)=0` for all `i`, and the FULLY GENERIC constant spinor
`(a,b)` (both symbolic, not spot-checked at `(1,0)`/`(0,1)` alone) satisfies
`∇⁰_{Z_i}ψ=0` for all `i`, and `D⁰ψ=0` identically. This re-confirms, fresh
and independently of citing E9, that the ENTIRE 2-dimensional space is the
kernel, not merely that "some nonzero vector" is in it.

At `t=1` (right-invariant frame, `c0=-2`): re-built the quaternion model
`g(x)=x0·I+Σx_i·Z_i`, verified `g·ḡ=|x|²I`, and checked the fully generic
family `ψ(x)=ḡ(x)·(a_,b_)` satisfies `∇¹_{Z_i}ψ=0` for all `i` and `D¹ψ=0`
identically — using a robust closed-form trace-projection coordinate
extraction (`a_i = -tr(M·Z_i)/2`) rather than a fragile linear solve. This
confirms the FULL 2-dimensional family is parallel at t=1 too, not a single
spinor — **caveat carried forward exactly as E10 stated it: only under
`c0=-2` (the concrete Pauli-realization sign), not under this project's own
abstractly-calibrated `c=+2`**, which E10 already found fails for the single
candidate tested there.

### Section C — toy tensor-product kernel verification [VERIFIED-tool]

For explicit 2×2 Hermitian `A,B` each with a 1-dimensional kernel, computed
`ker(A²⊗I+I⊗B²)` directly via `nullspace()` and confirmed: (a) the dimension
equals `dim ker(A) × dim ker(B)` exactly, and (b) the actual kernel vector
found is proportional to the predicted `kron(ker A, ker B)` vector — i.e. the
general sum-of-squares argument (`A²,B²≥0` ⟹ a zero of the sum forces both
terms to vanish separately ⟹ `ker = ker(A)⊗ker(B)`) is grounded in an actual
computation here, not merely asserted algebra.

### Section D — total count

| Quantity | Value |
|---|---|
| `dim ker(D_{S3,t=0 or 1})` | **2** |
| `dim ker(D_{S6,twisted})` per channel (G74A) | 1 |
| Triality channels (G67/G73) | 3 |
| `dim ker(D_full)` per channel | **2** |
| **Total internal zero modes** | **6** |
| Needed for N_gen=3 | 3 |
| **Excess factor** | **2** |

### Section E — investigated (not forced) reductions

1. **Majorana/reality/Weyl condition:** grepped `preprint.tex` for "Majorana",
   "reality condition", "Weyl condition", "Weyl spinor" — **none found**. No
   reality condition is currently imposed anywhere in this project's spinor
   content that could halve a complex 2-dimensional space to a real
   1-dimensional one.

2. **SU(2)-doublet-counting-as-one-state:** E11 already tool-verified that the
   t=0 kernel is an EXACT `SU(2)_L` singlet / genuine `SU(2)_R` doublet (not
   two unrelated states — one irreducible 2-dim multiplet). This is a real,
   relevant structural fact, reused here by citation. **However, checking it
   against this project's OWN existing convention reveals it does NOT cleanly
   resolve the excess:** `preprint.tex:292-298` already defines "one
   generation" as requiring the FULL **4**-component SO(4) spinor
   representation `(2,1)⊕(1,2)` — i.e. BOTH an `SU(2)_L` doublet AND an
   `SU(2)_R` doublet SIMULTANEOUSLY (4 real S3-side states), applied
   identically at every KK level regardless of whether any `ker(D_{S3,t})` is
   realized (`G7`'s own script: "all 32 SM states appear at every (m,n)
   level"). The torsion-escape zero mode, by contrast, supplies only ONE
   2-dimensional doublet at a SINGLE fixed `t` (either the `SU(2)_L`-singlet/
   `SU(2)_R`-doublet at t=0, or its mirror at t=1) — not both doublets at
   once. Whether "1 doublet = 1 generation slot" is even the right way to
   read the existing 32-state convention, or whether the 32-state convention
   is a completely separate bookkeeping exercise (representation/quantum-number
   assignment) unconnected to the zero-mode-existence question, is **not
   settled anywhere in this project**. Concluding "the doublet IS the
   generation, so multiplicity 2 is fine" would be exactly the kind of forced,
   comfortable resolution this experiment was explicitly instructed not to
   manufacture — the honest status is: **this avenue is real but unresolved,
   requiring new reconciliation work this project has not done**, not a valid
   PASS.

3. **Orbifold/projection condition:** G27 (Z₃ orbifold, killed by Smith
   theory, χ(S⁶)=2) and G31 (S³ **adjoint**-bundle route, killed by
   Lichnerowicz + parity) are the only orbifold/projection-flavored results in
   this project, and both target either the S⁶ factor or a completely
   different (adjoint, not fundamental-spinor) bundle on S³ — grepped
   project-wide for "orbifold"; confirmed no existing construction targets a
   projection ON `ker(D_{S3,t})` itself. This escape route has not been
   attempted, let alone found, anywhere in this project.

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result kills:** the implicit treatment, throughout
  E2/E3/E7/E9/E9-followup, of "the t=0 (or t=1) constant spinor" as A SINGLE
  physical zero mode. It is not — it is a genuine 2-dimensional space (one
  `SU(2)` doublet). Any future citation of "the torsion-crossing zero mode" as
  contributing exactly 1 state per channel is, as of this experiment,
  unsupported.
- **What this result does NOT kill:** the t=0/t=1 flatness result itself
  (E7), the explicit parallel-spinor constructions (E9/E10) as MATHEMATICAL
  facts about `ker(D^t)`, or G74A's own S⁶-side result. All of these survive
  completely intact — only the IMPLICIT "dim=1" assumption used when
  combining them into a generation count is affected.
- **What survives, confirmed stronger than before:** the multiplicity-2
  structure is not an accident or computational artifact — it is confirmed by
  TWO independent methods (Section A representation theory, Section B direct
  construction) and is furthermore shown (E11, reused here) to be a clean,
  irreducible `SU(2)` doublet, not an arbitrary degeneracy. This means any
  future resolution attempt has real structure to work with (a specific
  gauge-multiplet, not unstructured noise) — but "has structure to work with"
  is not the same as "already resolved."

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Reconcile the 32-state and zero-mode-kernel frameworks | Show explicitly whether "1 generation = 1 S3-side SU(2) doublet" is a valid re-reading of `preprint.tex:292-298`, or find the missing mechanism supplying the OTHER 2 states (the opposite-chirality SU(2) doublet) |
| New reality/Majorana condition | Would need independent physical motivation, not invented post hoc to force multiplicity 1 |
| New projection specific to the S3 factor | No candidate currently exists in this project; would be new work, not a re-application of G27/G31 (both inapplicable here) |
| Show the product-decoupling assumption itself fails for torsion-deformed S3 | Would remove the premise entirely (a different, larger finding) — not investigated here |

## Assumptions carried, unresolved

Per claim.md: the `D_full² = D_{S3,t}²⊗I + I⊗D_{S6,twisted}²` decoupling
formula for the TORSION-DEFORMED S3 factor remains E2's own
`[INFERRED, NOT independently literature-verified]` assumption — this
experiment computes the consequence of it holding, and does not re-examine
whether it holds. If it does NOT hold, the entire premise of E2/E3's
candidate mechanism is separately in question, independent of this
experiment's own finding.

## What this does NOT mean

1. Does **not** resolve H1c (which of t=0/t=1 is physically selected) —
   untouched.
2. Does **not** imply E7's flatness result, or E9/E10's explicit parallel-spinor
   constructions, are wrong — they are correct as mathematical facts about
   `ker(D^t)`; what is wrong is the IMPLICIT assumption that this kernel is
   1-dimensional when it is used to build a generation count.
3. Does **not** claim this is unfixable — Section E's "SU(2)-doublet-counting"
   avenue is real and worth pursuing, but is NOT yet a resolution.
4. Does **not** touch G74A's own S⁶-side result, which stands exactly as
   established (dim ker(D_{S6,twisted})=1 per channel, both directions
   closed).

## Recommended next action (not attempted here)

If the torsion-escape-route program is pursued further, the FIRST question to
resolve, before any further work on H1c/H2/H3, is whether `preprint.tex`'s
existing "32 complex components = one generation" convention and the
torsion-crossing zero mode's kernel-dimension count are talking about the same
object at all — this is a prerequisite question this project has not yet
asked, let alone answered, and this experiment's main contribution is
surfacing that it needs to be asked.

## Check (reproduces this decision)
`python e12_multiplicity_gate.py` →
`verdict.core_multiplicity_2_confirmed_at_t0==true`,
`verdict.multiplicity_2_confirmed_at_t1_under_c0==true`,
`verdict.natural_physical_reduction_found==false`,
`verdict.label=="FAIL_MULTIPLICITY_2_CONFIRMED__NO_NATURAL_PROJECTION_FOUND"`.
