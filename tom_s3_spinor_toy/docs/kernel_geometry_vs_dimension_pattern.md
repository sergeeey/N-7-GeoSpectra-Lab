# Kernel geometry vs. kernel dimension pattern

**Added:** 2026-09-17, after C198 tested this on the one substrate the
project has for it. **Status:** ACTIVE, methodology convention (not itself a
research claim — the specific test it motivated, C198, is a REJECT; see
`null_results/INDEX.md`). **Source:** a user-forwarded cross-domain
methodological analogy from an external paper on random circulant graphs
and the Lovász number (Fourier-basis reduction of an SDP to a null-space
problem, then studying that null-space's *geometry*, not just its
dimension) — logged as `pearl_registry/INDEX.md` (2026-09-17).

Sibling of `ko_dimension_registry.md` and `gates_tracker.md`'s own
`Δ_geo = dim ker D − F_graded` diagnostic (C148). Those ask *did an extra
kernel DIMENSION appear beyond what representation theory forces?* This
pattern asks a different question about the same object: *even when the
dimension is exactly forced, is the kernel's ORIENTATION inside the ambient
Hilbert space also forced, or does it still carry information `Δ_geo`
cannot see?*

---

## The source paper's mechanism, abstracted

```
structured object (random circulant graph)
    --[symmetry / Fourier]-->
right basis (DFT-diagonalized SDP)
    -->
kernel / null-space CONSTRAINTS
    -->
strong bound (Lovász number estimate)
```

The paper's own Lemma 5 (null-space property): for `x` in a specific random
Fourier-kernel, `‖x‖₂ ≤ (log²n/√n)‖x‖₁`. The point is not the specific
bound — it is that **membership in the kernel already sharply constrains the
possible SHAPE of the vector**, not merely its count of dimensions. This
project's own C143–C148 chain independently arrived at a structurally
identical warning, from the opposite direction: `K = dim ker D` can *look*
like a dynamical, hard-won result, when it is actually forced in advance by
representation structure (`K = F_graded`). Both stories are the same
warning stated from opposite ends:

> **A structural constraint can pre-determine a large part of an observed
> result, and when it does, that part cannot be credited to dynamics.**

## The actual new idea: track the projector, not just the dimension

Two operators can have `dim ker D₁ = dim ker D₂ = 1` — `Δ_geo = 0` for
both — with completely different normalized zero modes `ψ₁ ≠ ψ₂`.
Representation theory can force the *dimension* of a kernel to exist
without forcing *which line inside the Hilbert space* that kernel occupies.

**Diagnostic, stated precisely.** For a Dirac-type operator `D(∇)` varying
over a connection family, instead of only `K(∇) = dim ker D(∇)`, also track
the projector `P_ker(D(∇))` onto the kernel, and compare two points of the
family via

```
overlap(∇₁,∇₂) = |v(∇₁)† v(∇₂)|          (kernel is 1-dim: a single unit vector)
d(∇₁,∇₂) = ‖P_ker(D(∇₁)) − P_ker(D(∇₂))‖  (kernel is higher-dim: principal angles / operator norm)
```

**Two outcomes, both informative, pre-registered as equally likely before
testing (do not let a preference for either one leak into the test
design):**

- `Δ_geo=0` **and** `overlap ≈ 1` (or `d ≈ 0`) across the family →
  representation theory has consumed essentially the whole kernel — not
  just its size but its direction. Strengthens the case that `Δ_geo` is not
  just a dimension count but a *complete* description of the kernel here.
- `Δ_geo=0` **and** `overlap` moves away from `1` (or `d` grows) →
  `Δ_geo=0` does NOT mean zero geometric information; the kernel's
  orientation is doing work the scalar diagnostic is blind to. This would be
  a genuinely new observable this project did not have before.

## Worked example: C198 (first, and so far only, application)

Substrate: C73b's own 13-angle admissible-torsion-family sweep — the only
place in the project's own C139/C141/C147/C148 evidentiary chain where
`dim ker D(∇)` is nonzero AND dimension-stable at more than one point
(every OTHER swept family has `dim ker = 0` identically; see C198's own
`claim.md` Prior Result Gate for the two Explore-agent searches that
established this). Standing caveat, inherited from C73b unchanged: every
one of the 13 points **fails calibration** — this substrate is
mathematically well-defined, not physically admissible.

**Result: REJECT** (of the pre-registered prediction that the kernel would
rotate). `overlap(θ, θ_NOMIZU) = 1.000000` exactly at all 13 angles, and —
found, not assumed — the exact mechanism why: `block(θ) = exp(−iθ)·Block_t1`
identically (residual `< 3×10⁻¹⁶`), i.e. the real-2-parameter torsion
family collapses, under this specific bilinear pairing, onto a single
COMPLEX line traversed by pure phase rotation. A phase rotation cannot move
the projective direction (the kernel LINE) a vector spans — so the result
is a proved fact about this family, not a numerical coincidence. Full
detail: `experiments/20260917-c198-kernel-orientation-vs-dimension/decision.md`.

**What this does and does not establish.** It does NOT mean the general
diagnostic is empty — it means this project's ONE currently-available test
substrate happens to be secretly rank-1 over ℂ, for a clean, explicit
algebraic reason found along the way. The general question (does kernel
orientation ever carry information `Δ_geo` misses?) remains open — this
project has simply never had a SECOND, structurally-different,
dimension-stable nonzero-kernel family to test it on.

## A companion principle from the same source paper: right basis before diagonalizing

The paper reaches its result by using circulant symmetry to pass through a
DFT into a basis where the SDP becomes a simple LP/kernel problem — it never
diagonalizes the original large matrix directly. This project's own
Peter–Weyl/representation-decomposition practice already does the same
thing implicitly; worth stating as an explicit rule for the next genuinely
dynamic `Hom ≥ 2` candidate this project builds:

```
do NOT diagonalize a large equivariant operator directly.
first decompose the Hilbert space by irreps:  H = ⊕_λ V_λ ⊗ M_λ
then any equivariant operator has the block form  D = ⊕_λ I_{V_λ} ⊗ A_λ
the actual dynamics live entirely in the small multiplicity matrices A_λ.
```

Every operator this project has built to date (`round59`'s `D`, C73/C73b's
family, C139/C141/C147's twisted variants) already has `dim Hom = 2` or
smaller for the relevant channel pairs — small enough that this was never a
practical bottleneck. It becomes load-bearing the first time a candidate has
`Hom ≥ 2` between channels that are NOT already forced to be proportional
(C198's own finding shows this can happen invisibly even in a small
example) — at that scale, diagonalizing directly would waste effort
re-discovering block structure the representation theory already hands you
for free.

## A red-team lesson from the same source paper: name what a relaxation drops

The paper's own authors flag, honestly, that their RIP-based route drops the
constraint `y ≥ 0` to get a clean theorem, while suspecting that exact
constraint is what a sharper bound would need. This is the same shape as
this project's own information-loss tradition (`C150/GATE.md`, the
`G₂`/`SU(3)`-restriction non-discrimination theorem in
`experiments/20260916-g44-completeness-theorem/`): a relaxation can produce
a clean, correct, PUBLISHABLE bound while silently discarding exactly the
structure a sharper answer would have needed.

**Rule, generalized:** every time this project passes from a full operator
to representation content, kernel dimension, a commutant, or
`G₂`/`SU(3)`-restricted data, name explicitly what information that specific
map is known or suspected to discard — not as a disclaimer appended after
the fact, but as a line written down at the point of the reduction, before
results are seen. `experiments/20260916-g44-completeness-theorem/THEOREM.md`
§4 ("What this does NOT claim") and its own "gray zone" acknowledgments (§4
point 6: `S³`-isometry data neither included nor excluded) are the closest
existing precedent for doing this consistently already.

## Scope and enforcement

Like `negative_control_pattern.md` and `vacuity_gate_pattern.md`, this is a
methodology pattern, not a Falsification-Ladder step of its own — it is a
DIAGNOSTIC to reach for at FL Step 6 ("run test") whenever a family of
connections/operators is being swept and `dim ker` is the only quantity
being recorded. It does not replace `Δ_geo` — it is a follow-up question to
ask precisely when `Δ_geo = 0` and a reader might otherwise conclude
"nothing here."

**Precondition to even attempt this pattern:** a family of at least 2
points with EQUAL, NONZERO `dim ker D`. Check this BEFORE designing the
overlap test — C198's own Prior Result Gate found that most of this
project's own swept families (`dim ker = 0` throughout) do not satisfy it,
and running the test on the wrong substrate would silently produce a
vacuous "overlap undefined" or a meaningless comparison of `{0}` to itself.

## Event trigger for the next application

`pearl_registry/INDEX.md` (2026-09-17 row): re-run this exact test the next
time this project produces EITHER (a) a calibration-admissible nonzero-kernel
family, or (b) a nonzero-kernel family not derived from the same
`Hom_su(3)(m,Λ²m)` 2-space C73b uses. Do **not** re-run it on C198's own
substrate — that family's structure is now exactly, provably understood
(`Block_t2 = −i·Block_t1`); re-running would not produce new information.
