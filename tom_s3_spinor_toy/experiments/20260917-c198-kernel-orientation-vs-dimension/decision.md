# C198 Decision — kernel LINE is exactly fixed across C73b's whole torsion-angle family; my own pre-registered prediction was WRONG

**Date:** 2026-09-17
**Verdict:** **MAIN CLAIM FALSE** (pre-registered prediction that the kernel
direction would rotate is REJECTED). `Δ_geo=0` really does coincide with
ZERO geometric movement of the kernel LINE across this specific family —
strengthened, not weakened, by an exact algebraic mechanism found along the
way. All 4 checks (2 positive controls + 2 method-consistency checks) PASS.

All numbers trace to `c198_kernel_orientation.py` and `results_c198.json`.

---

## 0. Where this idea came from, and why it's in scope

The user forwarded a cross-domain methodological analogy from an external
paper on random circulant graphs / the Lovász number: after a Fourier-basis
reduction turns an SDP into a kernel/null-space problem, the paper studies
the null-space's *geometry* (a null-space property bound
`‖x‖₂ ≤ (log²n/√n)‖x‖₁`), not just its dimension. The user's own
transferred question, stated explicitly and pre-registered before any
computation: **"если размерность kernel полностью forced, остаётся ли
информация в геометрии самого kernel subspace?"** — i.e., this project's own
`Δ_geo = dim ker D − F_graded` diagnostic (C148) only asks whether an EXTRA
DIMENSION appeared. It has never asked whether the kernel's ORIENTATION
inside the ambient space moves even when the dimension doesn't.

## 1. Novelty check (Prior Result Gate)

Two dedicated Explore-agent searches (this session) confirmed: no file
anywhere in this repo compares kernel projectors / kernel eigenvectors
between two different connections/operators (the closest precedents —
`round125`'s principal angles between two STATIC Lie-subalgebra spans, and
`C79/C80/C81/C86`'s single FIXED kernel-projector-as-reference — are
methodologically adjacent but do not do this comparison). Full detail in
`claim.md`'s Prior Result Gate section. **Status: NEW.**

The second search also established a genuinely important SUBSTRATE fact:
**every family sweep in the C139/C141/C147 evidentiary chain has `dim ker
D(∇)=0` identically throughout** — there is no nonzero, dimension-stable
kernel there to compare orientations of. The ONLY place in the repo with a
genuinely different (non-scalar-rescaled) connection family giving nonzero
kernel at multiple points is **C73b**'s own 13-angle sweep of the admissible
`Hom_su(3)(m,Λ²m)` torsion family (`kernel_dim=1` at all 13 angles,
`results_c73b.json`) — with the explicit, already-documented caveat that
`calibration_passes: false` at every one of those 13 points (round59's own
NOMIZU point is the only calibration-admissible one, and it was never itself
one of the 13 sampled angles). This experiment uses C73b's substrate, and
inherits that caveat explicitly (see §5).

## 2. Method

Reused C73b's own, unmodified functions (`equivariant_torsion_basis`,
`vec_to_nomizu_dict`, `matdict_to_nomizu`) and C73's own, unmodified
`build_numeric_dirac`/`invariant_basis`. `domain_inv` (2-dim,
SU(3)-invariant sector of `Σ_odd⊗Σ_even`) and `target_inv` (1-dim, of
`Σ_even⊗Σ_even`) are θ-independent; `block(θ) = target_inv† · D(θ) ·
domain_inv` is a `1×2` row `[a(θ),b(θ)]`. Since `target_inv` is 1-dim,
`kernel_dim=1` whenever `rank(block)=1` (i.e. whenever `(a,b)≠(0,0)`), and
the kernel LINE in `domain_inv`'s 2-dim coordinates is the null vector of
that row: `v(θ) = (b(θ),−a(θ))/‖·‖`. Overlap between two angles:
`overlap(θ,θ') = |v(θ)†v(θ')|`.

## 3. Pre-registered prediction (stated in `claim.md` BEFORE running)

*"the kernel direction WILL move non-trivially across the family (overlap
will drop measurably below 1 for at least some pairs)"* — based on the
algebraic reasoning that `block(θ)=cos(θ)·Block_t1+sin(θ)·Block_t2` is a
genuine linear pencil of two independent basis vectors of a 2-dim Hom-space,
and a generic pencil's null direction rotates. **This turned out to be
WRONG** (see §4) — recorded here, not edited after the fact, per this
project's own discipline of stating predictions before seeing results.

## 4. Results

**T1 — kernel_dim + |a|,|b| magnitudes reproduce C73b's own independently-run
sweep exactly: PASS.** `kernel_dim=1` at all 13 angles (matches). Raw
complex `a(θ),b(θ)` do NOT match C73b's saved values component-for-component
— expected and understood: `invariant_basis()`'s SVD-based nullspace basis
is only defined up to an arbitrary (θ-independent) unitary rotation `U`
across separate process runs, which changes raw components but leaves
`|a|,|b|`, `kernel_dim`, and every overlap invariant. Cross-checked directly:
**both this run and C73b's own original saved JSON give `|a|=1.000000`,
`|b|=1.732051=√3` EXACTLY at all 13 angles** — the same values as round59's
own certified `(a,b,s)=(∓1,∓√3,4)` headline result (`c73_dirac_battery.py`'s
`test_ground_truth_reproduction`). Confirms both runs see the identical
underlying structure.

**T1b — `block(θ) = exp(−iθ)·Block_t1` EXACTLY: PASS**, to machine precision
(`max diff < 3×10⁻¹⁶` at every one of the 13 angles). Equivalently: `Block_t2
= −i·Block_t1` exactly (verified directly: `Block_t1=(0.879−0.477j,
1.523−0.826j)`, `−i·Block_t1=(−0.477−0.879j,−0.826−1.523j)`, matches
`Block_t2` to machine precision). **This is the exact mechanism**: the
real-2-dimensional admissible torsion family, seen through this specific
bilinear pairing, collapses onto a single COMPLEX LINE (spanned by
`Block_t1`), traversed by a pure phase rotation `e^{−iθ}` as `θ` sweeps the
real parameter circle. A vector's projective direction (the LINE it spans)
is invariant under multiplying it by an overall complex phase — so the
kernel line CANNOT rotate on this family, by exact algebraic construction,
not by numerical coincidence.

**T2 — antipodal positive control, `overlap(θ,θ+180°)≈1`: PASS** (all 13
values `=1.0000000000000000±2×10⁻¹⁶`), consistent with `block(θ+180°) =
−block(θ)` (an overall sign flip cannot change a null line) — confirms the
overlap methodology itself is sound.

**T3 — reduced-coordinate overlap vs full-64-dim-embedding overlap agree:
PASS** (`diff<10⁻⁸` at every angle) — confirms `domain_inv`'s columns are
genuinely orthonormal (verified directly, `orthonormal_domain_inv=true`) and
the shortcut of working in 2-dim coordinates is valid.

**MAIN CLAIM: `overlap(θ,θ_NOMIZU)=1.000000` at ALL 13 swept angles — the
kernel direction is NOT constant is FALSE.** Given T1b's exact mechanism,
this holds continuously on the entire circle, not merely at the 13 sampled
points.

## 5. What this does and does NOT mean

**Does NOT** bear on the physical `N_gen=3` question directly, and does NOT
retest C73b's own calibration verdict — every point on this family except
possibly round59's own exact angle (never itself swept as a discrete point)
fails calibration (`calibration_passes: false`, C73b's own
`results_c73b.json`, reconfirmed here). This is a statement about the
MATHEMATICAL structure of an abstract Hom-space, not a claim about
physically realized geometry — the same honest scope C73b's own decision.md
already used.

**Does** answer the user's own transferred question, for this specific
family: **`Δ_geo=0` here really does mean zero additional geometric
information** — not just the kernel DIMENSION but its ORIENTATION is rigid
across the whole admissible torsion-angle family, and now for an exact,
understood algebraic reason (the family collapses to a phase-rotation orbit
of a single complex line under this pairing), not merely an unexplained
numerical coincidence. This is a STRONGER form of C73b's own "topologically
protected" framing: not just dimension-protected, but orientation-protected.

**Does NOT generalize** beyond this one family — a genuinely different
connection family (one not related to round59's NOMIZU by this specific
2-dim `Hom_su(3)(m,Λ²m)` structure), or a calibration-admissible one were it
ever found, could still show real kernel-orientation movement. The general
cross-domain idea (kernel geometry vs. kernel dimension) is NOT killed by
this result — only this specific, currently-testable instance of it.

## 6. Kill Analysis

**Killed:** the specific hypothesis that THIS family's kernel line moves
while `Δ_geo=0`. Also killed, more specifically: my own pre-registered guess
that a generic 2-parameter linear pencil would show a rotating null
direction — it doesn't here, because the pencil is secretly rank-1 over ℂ
(`Block_t2=−i·Block_t1`), a fact that wasn't visible before computing it.

**Not killed:** the general cross-domain idea itself (kernel orientation as
a diagnostic distinct from kernel dimension) — this project has simply never
had a second, independently-varying, calibration-admissible family to test
it on. C73b's own admissibility finding (every angle fails calibration)
remains the actual bottleneck, not this experiment's result.

**Relaxation Map:** the natural next differentiating test, if this line of
inquiry is pursued further, is NOT re-sweeping this same family (its
structure is now exactly understood and provably rigid) — it would require
either (a) a genuinely different connection FAMILY not built from the same
`Hom_su(3)(m,Λ²m)` 2-dim space (none currently exists in this project, per
§1's substrate finding), or (b) two independent, calibration-admissible
constructions on the SAME ambient space to compare directly (also does not
currently exist, confirmed by the second Explore-agent search). Both are
new, nontrivial constructions, not "cheap" tests — no such test is available
today.

## 7. Pearl Registry candidate

**Observation:** a real, transferable methodological gap existed (kernel
DIMENSION vs kernel ORIENTATION as separate diagnostics) — worth recording
even though this specific instance came back null, since the general idea
survives and the null result itself is informative (it strengthens, not
weakens, confidence in `Δ_geo` as a diagnostic, AT LEAST for phase-rotation-
type families). **Falsifiable prediction:** if this project ever produces a
SECOND connection family (not derived from the same `Hom_su(3)(m,Λ²m)`
2-space) with a nonzero, dimension-stable kernel, repeating this exact
`overlap(θ,θ_ref)` test on it could show genuine movement — worth re-running
then, not now. **Trigger:** the next experiment that produces a
calibration-admissible OR genuinely structurally-different nonzero-kernel
family. **Next check:** no fixed date — event-triggered.

## 8. Reproduction

```bash
cd experiments/20260917-c198-kernel-orientation-vs-dimension
python c198_kernel_orientation.py
```

`ruff format` + `ruff check`: clean. All 4 checks (T1, T1b, T2, T3) PASS;
main claim FALSE (kernel direction provably fixed).
