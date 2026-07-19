# Round124 — Decision

**Date:** 2026-07-18
**Verdict:** `CANDIDATE_FOUND` — `su(3)⊕u(1)⊕u(1)` (SU(3) plus its own
2-dimensional abelian centralizer in `so(8)`) gives `Hom=0` for **all
three** off-diagonal pairs among `8_v, 8_s, 8_c`, and fixes zero vectors
in `8_v` (escapes confinement to `SO(7)`). A second, independent,
algebraically cleaner candidate for triality channel distinguishability —
by direct Schur-lemma non-isomorphism, not an explicit matching argument.

**Go/no-go:** does **not** close L3b (same physical-realization gap as
round119's `SO(4)×SO(4)` candidate applies here too), but strengthens
`GATE 1 OF 7 DONE` with a second, structurally different route to the
same algebraic milestone.

## Results [VERIFIED-tool, this round]

Reusing G102's own verified machinery (octonion table, `su(3)` basis,
centralizer computation, `Cl(0,8)`-built `v/s/c` representations,
`hom_dim`) by direct import, not re-derived:

| Quantity | `su(3)` alone (G102, unchanged) | `su(3)⊕u(1)⊕u(1)` (this round) |
|---|---|---|
| `Hom(v,v)`, `Hom(s,s)`, `Hom(c,c)` | 6, 6, 6 | 4, 4, 4 |
| `Hom(v,s)`, `Hom(v,c)`, `Hom(s,c)` | 6, 6, 6 | **0, 0, 0** |
| Fixed vectors in `8_v` | 2 | **0** |

**Independent verification performed this round (not just the skeptic's
analytical trace — I re-ran these myself with Bash):**
1. Confirmed `su(3)` alone fixes exactly 2 vectors in `8_v` (the expected
   control — matches the 2-dim singlet subspace of `8_v|su(3)=3⊕3̄⊕1⊕1`).
2. **Basis-rotation invariance, checked with two different rotated
   bases of the same 2-dim centralizer space** (rotation angles `θ`
   drawn from `Random(seed=42)` and a second fixed `θ=1.3179`): both
   give **identical** results (`Hom` off-diagonal all 0, diagonal all 4,
   commute residual `~1e-15`) — confirming the result depends only on the
   centralizer's linear span, not on which arbitrary orthonormal basis
   `centralizer_dim`'s SVD happened to return. This was the one thing
   the skeptic pass could not itself execute (no Bash access in that
   agent's tool set) and flagged as needing empirical confirmation.

## Single skeptic pass — analytical trace, CONFIRMED-REAL with a
noted limitation, independently re-verified by me

Ran the mandatory skeptic review (claim.md + script + results +
G102's own script, no reasoning chain). Verdict: `CONFIRMED-REAL`.
Confirmed by code trace and independent arithmetic:
- The `6→4` diagonal drop is exactly explained: `8_v|su(3)=3⊕3̄⊕1⊕1`
  gives `Hom(v,v)=1²+1²+2²=6` (the `2²=4` term from the isotypic block
  of the two trivial summands); if the centralizer's two `U(1)`
  generators give the two singlets **different** characters, that
  isotypic block splits into two rank-1 blocks, giving `1+1+1+1=4`.
- No tunable parameter or post-hoc choice in the round124 script —
  `derivation_basis()`, `stabilizer_basis(der, point_index=1)` (one
  arbitrary but immaterial choice of imaginary unit, any choice gives a
  conjugate `su(3)` with identical `Hom` structure), and
  `centralizer_dim(su3)` are all deterministic, reused unmodified from
  G102.
- Skeptic's one honest limitation: it traced the code analytically but
  could not literally execute it (no Bash in that agent's tools) — per
  this project's own `audit-verification-gate.md` ("agent's `[VERIFIED]`
  = my `[INFERRED]`"), I did not accept this as sufficient and
  independently re-ran the script plus the two rotation checks myself
  (above) before finalizing this decision.

## What this does NOT mean

1. Does **NOT** close L3b — matching round119's `SO(4)×SO(4)` precedent
   exactly, the same two obstructions apply: (a) **physical
   identification** — nothing establishes that these specific `u(1)×u(1)`
   charges correspond to any actual physical quantum number (analogous to
   the open question of whether `SO(4)×SO(4)`'s factors correspond to
   `S³`'s `SU(2)_L×SU(2)_R`); (b) **dynamical consistency** — this
   candidate is, like `SO(4)×SO(4)`, an algebra OUTSIDE `g₂` (the
   centralizer of `su(3)` inside the full `so(8)`, not inside `g₂` itself
   — `g₂` is simple with zero center, so it has no room for an abelian
   ideal commuting with its own `su(3)` subalgebra beyond `su(3)` itself),
   meaning realizing this symmetry physically would ALSO require breaking
   `G₂` — triggering the same G74A Lemma B obstruction (exact-`G₂`-only
   proof technique for `dim ker=1`) documented in round119's own
   `TRIALITY_DISTINGUISHABILITY_GATE.md` §3.
2. Does **NOT** contradict G102's own `Hom_su(3)=6` finding — that
   result concerns `su(3)` ALONE, unaffected, still correct.
3. Does **NOT** identify these `u(1)×u(1)` charges with any known physical
   quantum number (hypercharge, `B-L`, etc.) — that would be fresh
   model-building input, same caveat pattern as round119.
4. Does **NOT** affect `N_gen=3`'s `CONDITIONAL` status, `lambda=FREE_
   COUPLING_PARAMETER`, or `safe_for_runtime=False`.

## Kill Analysis

- **What this kills:** nothing previously established — this is a new,
  additive finding.
- **What this does NOT kill:** the physical-realization gap remains
  exactly as open as round119 found it; the STRONG-vs-WEAK reading
  distinctions from round118 (matter-generation factorization) are
  unaffected.
- **What survives as a scoped next step:** identify whether these
  `u(1)×u(1)` charges correspond to any physically meaningful quantity —
  not attempted here, would require input beyond this project's own
  established geometry (same class of gap as `SO(4)×SO(4)`'s physical
  identification question).

## Relaxation Map

| Option | What it would require |
|---|---|
| Physical identification of the `u(1)×u(1)` charges | **[ATTEMPTED, round126, 2026-07-18]** Scanned all combinations of the 2 centralizer generators for a charge-ratio match to `B-L`'s `3:1` singlet:triplet pattern — found a crossing, but skeptic review (independently re-verified) showed it is a **tautological consequence** of the scan's own Frobenius-norm normalization convention (any target ratio would produce an equally "clean" closed-form value; hitting ratio 3 at all is guaranteed by IVT over the achieved range `[0.077,38.8]`), not independent evidence. Verdict: `NO_INDEPENDENT_EVIDENCE` — genuinely still open, needs a fundamentally different method (see `experiments/20260718-round126-u1-charges-vs-bl-hypercharge/decision.md` Relaxation Map). |
| Resolve the shared G74A Lemma B obstruction | Same as round119 — no `K`-equivariant analogue of Lemma B exists with current tools, since this candidate (like `SO(4)×SO(4)`) acts only on the fiber, not the base |
| Cross-check against `SO(4)×SO(4)`: are these two candidates the SAME underlying structure in different language, or genuinely different? | **[ATTEMPTED, round125, 2026-07-18 — see `experiments/20260718-round125-so4xso4-vs-su3-centralizer-comparison/decision.md`]** `PARTIAL_OVERLAP` — genuinely different (12-dim vs 10-dim) but share an exact, non-generic 3-dim abelian `u(1)³` core. |

## What survives, honestly stated

Two independent, structurally different rank-4 algebras (`SO(4)×SO(4)`
from the octonion `H⊕Hℓ` split; `su(3)⊕u(1)⊕u(1)` from the isotropy
group's own centralizer) now both achieve algebraic distinguishability of
all three triality channels, both by escaping the rank-3 `SO(7)`
confinement that killed every earlier candidate. This round's route is
arguably cleaner (direct `Hom=0`, full Schur non-isomorphism, not an
explicit chirality-matching argument) but shares the identical remaining
obstruction. `GATE 1 OF 7 DONE / GATES 2-6 OPEN` remains the accurate
status — now with a second, independently-derived confirmation.

## Check (reproduces the verification)

```
cd experiments/20260718-round124-su3-centralizer-triality-candidate
python e41_su3_centralizer_triality_candidate.py
```
Expect: `Hom_(su(3)+centralizer)` off-diagonal all `0`, diagonal all `4`,
`n_fixed_vectors_in_8v_under_combined_algebra = 0`, verdict
`CANDIDATE_FOUND`.
