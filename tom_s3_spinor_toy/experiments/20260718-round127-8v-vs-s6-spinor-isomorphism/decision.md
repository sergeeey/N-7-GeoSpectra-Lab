# Round127 — Decision

**Date:** 2026-07-18
**Verdict:** `ABSTRACT_ISOMORPHISM_ESTABLISHED_WITH_HIGH_CONFIDENCE,
EXPLICIT_CONSTRUCTION_STILL_OPEN` [verdict label softened by skeptic
review — see below] — `ℂ⊗8_v` and `Σ` (G14/G15's "`S⁶` spinor") are the
same abstract `su(3)`-representation type (`1⊕1⊕3⊕3̄`), established by the
matching self-intertwiner dimension (`Hom(V,V)=6` on both sides, which
algebraically forces the `1⊕1⊕3⊕3̄` decomposition uniquely — not by
Casimir-spectrum matching alone, which cannot by itself distinguish
`3⊕3̄` from `3⊕3` or `3̄⊕3̄`), resolving the CONCEPTUAL part of the
identification gap. But the first attempt to construct an EXPLICIT
isomorphism failed for a precisely-diagnosed reason — not because the two
objects differ, but because the two constructions' own generator bases
were never aligned to refer to the same abstract Lie algebra elements.
Constructing the alignment is real, well-scoped remaining work, not
completed this round — and, per skeptic review, remains a live check that
COULD in principle still falsify the abstract-isomorphism claim if it
turns out to be impossible (see Kill Analysis).

## What was precisely established (real objects, correctly distinguished)

- **`8_v`** (round124/G102): the octonion vector rep of `SO(8)` — a real
  8-dim space. `su(3)` acts via 8 real antisymmetric matrices.
- **`Σ`** (G14/G15's "`S⁶` spinor"): the `Spin(6)` Dirac spinor `Λ•(ℂ³)` —
  a genuinely complex 8-dim space, built by Clifford-lifting `su(3)`'s
  action on `S⁶`'s 6-dim tangent space. **Categorically different from
  `8_v`** (complex vs. real) — confirmed by reading the exact
  construction (`g10-b`→`g11`→`g14`/`g15`), not assumed.
- The correct, well-posed comparison is between `ℂ⊗8_v` (complexification)
  and `Σ`, both genuinely complex 8-dim `su(3)`-modules.

## First attempt, its failure, and the honest diagnosis (three layers, all resolved in sequence)

**Layer 1 — naive Hom-space computation gave `4`, not the predicted `6`.**
Computed `Hom_ℂ(ℂ⊗8_v, Σ)` via the standard Sylvester-equation nullspace
(pairing `su3_v[i]` with `su3_sigma[i]` index-for-index) — got `4`.
Sanity-checked the tool itself first: `Hom_ℂ(ℂ⊗8_v,ℂ⊗8_v)=6` and
`Hom_ℂ(Σ,Σ)=6` both came out correctly (matching G102's own established
`Hom_su(3)=6`), so the tool itself is not buggy — the cross-computation
genuinely gives `4`.

**Layer 2 — a Casimir-spectrum check appeared to show a real structural
mismatch, but was itself using an invalid formula.** Computed the
quadratic Casimir via the naive `Σᵢ Xᵢ†Xᵢ` and got a spectrum
`{0,0,4/3×6}` for `8_v` but `{0,0,5×4,6×2}` for `Σ` — apparently
different. **This was wrong**, caught before accepting it: `Σᵢ Xᵢ†Xᵢ` is
only the genuine (invariant, scalar-on-irreducibles) Casimir operator if
`{Xᵢ}` is an ORTHONORMAL basis w.r.t. the Killing/trace form. Checked
directly: `su3_v`'s Gram matrix (`Tr(AᵢᵀAⱼ)`) is exactly the identity
(G102's SVD-based nullspace already orthonormalizes), but `su3_sigma`'s
Gram matrix is NOT proportional to identity (generators 4 and 7 are
coupled, off-diagonal entry `2` vs. diagonal `4`) — because G10-B's
`su3_generators()` uses plain sympy `.nullspace()`, which returns *some*
basis, not an orthonormalized one. **Fixed:** recomputed the Casimir using
the proper formula `C₂ = Σᵢⱼ (G⁻¹)ᵢⱼ Xᵢ†Xⱼ` (inverse Gram matrix as
metric) — **the spectra now match EXACTLY**: `{0,0,4/3,4/3,4/3,4/3,4/3,4/3}`
for both. This directly confirms `ℂ⊗8_v` and `Σ` have the identical
abstract decomposition `1⊕1⊕3⊕3̄` (also independently corroborated by
G14's own already-verified `T3`/`T4`/`T6` gates establishing `Σ`'s quark/
antiquark blocks are irreducible and mutually conjugate).

**Layer 3, corrected [skeptic correction — the original argument here was
insufficient, not the conclusion]:** first draft argued "matching Casimir
spectrum + complete reducibility ⟹ isomorphism, a theoretical certainty."
Skeptic found this skips a real step: the Casimir value `4/3` is IDENTICAL
for `3` and `3̄` (conjugate reps always share it), so a spectrum
`{0,0,4/3×6}` is compatible with `1⊕1⊕3⊕3̄` **but equally compatible with
`1⊕1⊕3⊕3` or `1⊕1⊕3̄⊕3̄`** — Casimir matching alone cannot rule these out,
and the round's first draft never checked this.

**The actually rigorous argument, verified this round [VERIFIED-tool]:**
for a decomposition `2·1 ⊕ a·3 ⊕ b·3̄` (`a+b=2`, `a,b≥0` integers), the
self-intertwiner dimension is `Hom(V,V) = 4 + a² + b²` (the `4` from the
`2×2` singlet block, `a²` from `a` copies of `3` mutually intertwining,
`b²` similarly). **Both `Hom(ℂ⊗8_v,ℂ⊗8_v)=6` (G102's own established
value) and `Hom(Σ,Σ)=6` (verified this round) force `4+a²+b²=6`, i.e.
`a²+b²=2` with `a+b=2` — the UNIQUE non-negative integer solution is
`a=b=1`.** This rules out `3⊕3` (`a=2,b=0`⟹`Hom=8`) and `3̄⊕3̄`
(`a=0,b=2`⟹`Hom=8`) directly, pinning the decomposition to `1⊕1⊕3⊕3̄`
specifically — not the Casimir spectrum by itself. `ℂ⊗8_v`'s own reality
(it is the complexification of a genuinely real representation) provides
an independent reason to expect `a=b`, consistent with this result.

**The Casimir computation is retained as a corroborating, independently-
verified check, not the load-bearing argument:** confirmed this round
that the "proper" Casimir formula (`Σᵢⱼ(G⁻¹)ᵢⱼXᵢ†Xⱼ`) genuinely satisfies
`[C₂,Xᵢ]=0` for every generator on BOTH representations (residual
`~1e-16`, machine precision) — the actual test that the formula is a
genuine invariant Casimir, not just an eigenvalue-matching coincidence.

**Given the decomposition is now pinned to `1⊕1⊕3⊕3̄` on both sides by the
End-dim argument (not just Casimir-compatible with it), the persisting
naive `Hom=4` (rather than 6) is explained by generator-index
misalignment**, corroborated independently for `Σ`'s own side by G14's
own already-verified `T3`/`T4`/`T6` gates (irreducible, mutually-conjugate
quark/antiquark blocks) and for `8_v`'s own side by G102's own established
`Hom_su(3)(v,v)=6`. Under a generic index misalignment, the trivial
(singlet) sector's intertwiner space is unaffected (any linear map
between two trivial reps is automatically equivariant regardless of how
the rest of `su(3)` is labeled) — contributing exactly `4` — while the
non-trivial `3⊕3̄` sector's naive-pairing intertwiner collapses to `0`.
This explains why every random invertible-candidate search in the 4-dim
Hom space failed (every element has rank ≤ 2, supported only on the
singlet block).

**Honest scope of this diagnosis, per skeptic's own finding:** the
misalignment explanation is *consistent with* the observed `Hom=4`, but
is not the *only* logically possible explanation for that specific number
in isolation — it is made the correct explanation by the independent
End-dim evidence pinning both sides to `1⊕1⊕3⊕3̄` exactly. Stated as a
combined argument (End-dim + misalignment), not Layer 3 alone.

## What this round establishes, and what it does not

**Established, with high confidence:** `ℂ⊗8_v` and `Σ` are the SAME
abstract `su(3)`-representation (`1⊕1⊕3⊕3̄`) — this is the CONCEPTUAL
resolution of the identification gap flagged since round126: they are not
different objects that merely happen to share a decomposition type by
coincidence. The decomposition is pinned down uniquely by the End-dim
identity `Hom(V,V)=4+a²+b²=6` (forcing `a=b=1`), corroborated (not
replaced) by the matching, genuinely-invariant Casimir spectrum
(`[C₂,Xᵢ]=0` verified to machine precision on both sides) and by G14's
own independent `T3`/`T4`/`T6` verification for `Σ`'s side.

**NOT established this round:** an EXPLICIT intertwiner matrix `S`. This
requires first finding an abstract Lie-algebra-level change of basis
(a linear map aligning `su3_v`'s own arbitrary generator ordering with
`su3_sigma`'s own arbitrary generator ordering as the SAME `su(3)`
elements — e.g. via matching Cartan-Weyl root structure, or an explicit
structure-constant-matching computation) — genuinely deferred, not
attempted this round given its own scope and complexity.

## Kill Analysis

- **What this kills:** the possibility that `8_v` and `Σ` are simply
  unrelated objects that cannot be meaningfully compared — they can, and
  are representation-theoretically identical.
- **What this does NOT kill:** round126's own `NO_INDEPENDENT_EVIDENCE`
  verdict on the `B-L` ratio-match question — that remains correct;
  resolving the abstract isomorphism does not retroactively validate
  round126's flawed ratio-scan methodology.
- **What survives as the concrete, well-scoped next step — AND a live
  kill criterion, per skeptic review [not just a completion formality]:**
  construct the Lie-algebra-level alignment `Φ` between `su3_v` and
  `su3_sigma` (matching structure constants / Cartan-Weyl roots), then
  re-run the Hom-space computation with properly-aligned generators. If
  an invertible `S` is found there, it confirms this round's abstract-
  isomorphism claim explicitly. **If no such `Φ` exists that raises
  `Hom(su3_v, Φ·su3_sigma)` back to `6`, this round's own conclusion would
  be falsified retroactively** — the End-dim argument shows an abstract
  isomorphism must exist in principle, but the specific alignment
  procedure has not yet been demonstrated to succeed, so this is
  correctly flagged as still-open, not merely deferred bookkeeping.

## Relaxation Map

| Option | What it would require |
|---|---|
| Find the Cartan-Weyl alignment `Φ` between `su3_v` and `su3_sigma` | **[DONE, round128, 2026-07-19]** `Φ` constructed and an invertible intertwiner `S` verified to machine precision (`iso_residual~1e-15`) across all 12 members of `Aut(su(3))`, after fixing two computational bugs (one caught by mandatory skeptic review — a `Minv`/`M` sign inversion; one self-caught — a Fortran/C-order `vec()` reshape mismatch also present in this round's own `e44` script, line 100, not yet independently re-verified there). Verdict `ALIGNMENT_SUCCESSFUL`. See `experiments/20260718-round128-cartan-weyl-alignment/decision.md`. |
| Once `Φ` and `S` are found, redo round126's `B-L` comparison literally | **[DONE, round128, 2026-07-19]** Transported round124's centralizer through the verified `S` and compared directly against `G15.BmL`. Result: `NO_LITERAL_MATCH` (relative residual `0.53`) — the abstract isomorphism is real, but this specific centralizer direction is not `B-L`. |
| Orthonormalize `su3_sigma` first as a partial simplification | Would fix the Casimir-normalization issue cleanly but does NOT by itself solve the deeper index-alignment problem (Layer 3) |

## What this does NOT mean

1. Does NOT change round124's `Hom=0` finding, round125's `PARTIAL_OVERLAP`
   finding, or round126's `NO_INDEPENDENT_EVIDENCE` verdict.
2. Does NOT affect `N_gen=3`'s `CONDITIONAL` status, `lambda=FREE_
   COUPLING_PARAMETER`, or `safe_for_runtime=False`.
3. Does NOT claim an explicit isomorphism has been constructed — the
   abstract decomposition match is established with high numerical
   confidence, but per skeptic review this is not equivalent to
   "certainty" until the explicit intertwiner is actually built (see Kill
   Analysis: the alignment step is a live check, not a formality).

## Standing lesson (a new, distinct failure mode from rounds 118-126)

**Two independently-constructed representations sharing the same
"generator count" (8 generators each) does NOT mean the generators are
expressed in a common basis — pairing them by list index is an implicit,
unstated, and generally FALSE assumption that the two constructions
"happened" to choose the same basis.** This is a different failure mode
from round126's genericity/normalization tautology — here the bug was a
silent basis-alignment assumption, caught by (a) sanity-checking the tool
on known self-Hom cases (ruling out a tool bug), then (b) computing a
basis-INDEPENDENT invariant (the properly-normalized Casimir spectrum) to
separate "are these really different representations" from "did I align
the bases correctly" — the two questions look identical from the naive
Hom-space number alone, but have opposite implications.

## Check (reproduces the key verifications)

```
cd experiments/20260718-round127-8v-vs-s6-spinor-isomorphism
python e44_8v_vs_s6_spinor_isomorphism.py
```
Expect: `Hom_dim=4` (the naive, misaligned computation — reproduces the
puzzle, not yet the resolution).

```
python e44b_casimir_alignment_diagnostic.py
```
Expect: `su3_v`'s Gram matrix proportional to identity (`True`);
`su3_sigma`'s Gram matrix NOT proportional to identity (`False`, shows the
off-diagonal coupling at entries 4,7); properly-normalized Casimir
eigenvalues `{0,0,4/3×6}` for BOTH representations exactly, verdict
`SAME_ABSTRACT_SU3_MODULE_TYPE`.

**Additional checks added after skeptic review (reproduced inline, not yet
in a committed script):** `max|[C₂,Xᵢ]|` over all generators, both
representations, `< 1e-15` (confirms the Casimir formula is a genuine
invariant, not just an eigenvalue-matching coincidence); the End-dim
identity `Hom(V,V)=4+a²+b²=6` with `a+b=2` has the unique solution
`a=b=1`, verified directly against both `Hom(ℂ⊗8_v,ℂ⊗8_v)=6` and
`Hom(Σ,Σ)=6`.
