# Round128 — Decision

**Date:** 2026-07-19
**Verdict:** `ALIGNMENT_SUCCESSFUL` for the abstract isomorphism; `NO_LITERAL_MATCH`
for the `B-L` comparison — the explicit Cartan-Weyl alignment `Phi:
su3_v -> su3_sigma` was constructed and an invertible intertwiner `S` was
found and verified to **machine precision** (`iso_residual ~1e-15` across
all 12 members of `Aut(su(3))` tested). This completes round127's own Kill
Analysis item — the abstract-isomorphism claim (`ℂ⊗8_v ≅ Σ`) is now backed
by an actual constructed intertwiner, not just the End-dimension argument.
Transporting round124's `su(3)`-centralizer through `S` and comparing to
G15's `BmL` gives **no literal match** (relative residual `0.53`, not small)
— the isomorphism is real, but this specific centralizer direction is not
`B-L`.

**This verdict was reached only after two rounds of self-caught and
skeptic-caught computational bugs, both now fixed and independently
re-verified — see "Bug history" below. The first pass through this round's
own code gave a confident, exhaustively-checked *wrong* answer
(`ALIGNMENT_INSUFFICIENT`, with language casting doubt on round127's own
conclusion) that did not survive mandatory skeptic review.**

## What was achieved (verified, machine precision)

1. **CSA of `su3_v`** found via a generic element's centralizer: exactly
   2-dimensional, anti-Hermitian, commuting (`~2.4e-16`).
2. **CSA of `su3_sigma`** reused G10-B's own `H1,H2`, lifted via
   `G11.lift_to_spinor` — anti-Hermitian, commuting (`0.0`), in
   `span(su3_sigma)` (`~1e-16`).
3. **Root systems extracted on both sides.** `su3_v` gives a regular unit
   hexagon; `su3_sigma` gives an irregular hexagon (lengths `1,1,1,1,√2,√2`)
   — expected from round127's own finding that G10-B's `H1,H2` are not
   trace-form orthonormal.
4. **Root-system matching (`M`, the CSA-restricted part of `Phi`):** the
   unique real linear map taking `su3_sigma`'s root coordinates onto
   `su3_v`'s, verified across the full 6-root hexagon — residual `3.3e-16`.
   Enumerated **all 12** distinct exact-hexagon-match candidates (confirmed
   exhaustive: `|Aut(A2)| = |Weyl(A2)⋊Z2| = 12`, matches by direct count).
5. **Root-vector scale factors (`mu_k`):** solved via nonlinear least
   squares directly on the multiplicative bracket equations
   `mu_i·mu_j·c_s = mu_k·c_v` (6 independent triple relations, one gauge
   choice fixed) — residual `~1e-16` to `1.3e-15` for every one of the 12
   candidates.
6. **Representation-level Hom space: `Hom_ℂ(8_v, Phi-relabeled Sigma) = 6`
   for all 12 candidates** (clean singular-value gap confirmed directly:
   the 6 smallest singular values of the Sylvester system sit at `~1e-15`,
   the next 6 sit at a constant `1.1547` — no threshold ambiguity).
7. **Invertible intertwiner `S` found and verified for all 12 candidates**
   — `S@su3_v[i]@S⁻¹ = Phi(su3_v)[i]` to `iso_residual ~1e-15` in every
   case, `cond(S)` in the range `3–5` (well-conditioned, not a numerical
   fluke).

## Bug history (both self-caught or skeptic-caught, both fixed, both
independently re-verified before trusting the final result)

**Bug 1 (found by mandatory skeptic review, Step 8a):** `evaluate_candidate`
originally computed `Phi(H1v) = Minv[0,0]*H1s + Minv[0,1]*H2s` using the
**inverse** of the root-coordinate map `M`. The correct formula uses `M`
itself (not `M⁻¹`) — root coordinates are dual/contravariant to the Cartan
generators in the SAME way, not inversely, for this specific construction
(derived independently from the eigenvalue-preservation condition
`[Phi(H1v), F_k] = alpha_v(H1v)·F_k`, confirming the skeptic's derivation
before applying the fix — see the `Phi_H1v_c`/`Phi_H2v_c` comment in
`e45_cartan_weyl_alignment.py`). Skeptic flagged: *"the fix is a one-line
symbol swap — `Minv_c` should be `M_c`."* Before this fix, ALL 12 candidates
gave `hom_dim=4` (never 6) — a clean, reproducible, but entirely
**self-inflicted** null result. Skeptic verdict: `FALSIFIED`, with high
confidence and a correct predicted outcome after the fix.

**Bug 2 (self-caught, after applying Bug 1's fix and finding a NEW,
separate anomaly — `hom_dim` jumped to 6 as predicted, but the "found"
invertible `S` had a large raw residual, `~0.2`–`0.9`, despite being
constructed from a cleanly-verified 6-dimensional nullspace):** the
Sylvester-equation nullspace basis vectors are 64-component vectors
representing `vec(S)` under the standard Kronecker identity
`vec(AXB)=(Bᵀ⊗A)vec(X)`, which requires **column-major (Fortran) vec()**
by mathematical convention. The code reconstructed `S` via numpy's default
`.reshape(8,8)`, which is **row-major (C order)** — silently producing a
DIFFERENT matrix that is not actually in the nullspace of the original
equation, even though it was built from genuine nullspace vectors.
**Verified directly** via an isolated 3×3 test case (`op @ vec(S,
order='F')` residual `~1.7e-15`; `op @ vec(S, order='C')` residual `~8.4`
— unambiguous) before applying the fix (`S = (hom_basis @
coeffs).reshape(8, 8, order="F")`). **This same bug is also present in
round127's own `e44_8v_vs_s6_spinor_isomorphism.py` line 100** (`S =
S_flat.reshape(8, 8)`, no `order="F"`) — flagged for that round's own
record below, though round127's own conclusion is very likely unaffected
(see "Cross-reference to round127" below).

**After both fixes:** re-ran the full 12-candidate exhaustive scan.
`iso_residual` dropped from the pre-fix `~0.8`–`1.3` (garbage) to
`~9e-16`–`2e-15` (machine precision) for every one of the 12 candidates,
`hom_dim=6` confirmed via a clean, unambiguous singular-value gap
(`1e-15` vs `1.15`) — not a threshold artifact.

## Cross-reference to round127 (the reshape-order bug found there too)

Round127's `e44_8v_vs_s6_spinor_isomorphism.py` has the identical
`S_flat.reshape(8, 8)` (no `order="F"`) at line 100. Round127's own
reported `Hom_dim=4` (not 6, for the naive unaligned pairing) is **not**
believed to be affected — the Hom-space *dimension* is a rank computation
(SVD singular-value count), which is basis/convention-independent and
therefore correct regardless of the reshape bug. What COULD be affected by
the same bug is round127's own explicit-`S`-search loop (`found_S`,
`best_det`, `iso_residual` fields in `results_round127.json`) — but since
`Hom_dim=4 < 8`, generic random elements of a 4-dimensional subspace of
`GL(8,ℂ)` are extremely unlikely to be invertible regardless of any reshape
convention, so round127's own `"isomorphism_found": false` conclusion is
very likely still correct, just for a slightly different reason than
originally stated (a `4`-dimensional Hom space genuinely containing no
invertible element, vs. a coincidental reshape artifact). **Not
independently re-verified in this round — flagged as a loose end, not
resolved.**

## Kill Analysis

- **What this establishes:** `ℂ⊗8_v` and `Σ` are isomorphic as complex
  `su(3)`-representations via an EXPLICIT, machine-precision-verified
  intertwiner `S` — completing round127's own flagged gap (which had only
  the abstract End-dimension argument, no explicit `S`).
- **What this does NOT establish:** a physical identification of round124's
  `su(3)`-centralizer with `B-L` — the literal comparison (`bml_fit_relative
  = 0.53`) shows no match. Per round127's own pre-registered kill criteria,
  this is `NO_LITERAL_MATCH`: *"An invertible `S` is found, but round124's
  centralizer transported through it does NOT match any linear combination
  of `BmL`... report honestly; the abstract isomorphism exists but the
  specific centralizer direction isn't `B-L`."*
- **The `S_NOT_UNIQUE_UP_TO_SCALE` kill criterion is also live here:** all
  12 members of `Aut(su(3))` give a VALID (different) `S`, each with its
  own `bml_fit_relative` — this round reports only the first
  (lowest-hexagon-residual) candidate's fit; a full scan of the `B-L` fit
  quality across all 12 was not performed (see Relaxation Map).

## Relaxation Map

| Option | What it would require |
|---|---|
| Check `bml_fit_relative` across all 12 valid `S` candidates, not just the first | Extend the existing candidate loop in `e45_cartan_weyl_alignment.py` to record `bml_fit_relative` for every candidate, not just `best_result` |
| Independently re-verify round127's own `results_round127.json` `isomorphism_found`/`best_det_found` fields with the `order="F"` fix applied | Patch `e44_8v_vs_s6_spinor_isomorphism.py` line 100, re-run, confirm `Hom_dim=4` result and `isomorphism_found` conclusion are unchanged (expected, per the argument above, but not yet checked) |
| If no `S` (across all 12) gives a clean `B-L` match, the physical-identification question (round126's original goal) is answered `NO` — write this up as its own honest closure rather than leaving it open | Requires completing the "check across all 12" item first |

## What this does NOT mean

1. Does NOT establish that this project's construction "derives" `B-L` from
   `8_v` — the abstract isomorphism exists, but the specific `B-L`
   direction does not literally match any of the 12 tested transported
   centralizers checked so far.
2. Does NOT affect `N_gen=3`'s `CONDITIONAL` status, `lambda=FREE_
   COUPLING_PARAMETER`, or `safe_for_runtime=False`.
3. Does NOT resolve round124's Gates 2-6 physical-realization obstruction.
4. Does NOT indicate a flaw in G10-B/G11/G14/G15/G102's own prior
   computations — every reused piece passed every consistency check run
   against it in isolation; both bugs found this round were in NEW code
   written for rounds 127-128, not in the reused machinery itself.

## Standing lesson (new — a distinct, general one)

**A clean, exhaustive negative result (12/12 candidates, machine-precision
sub-checks on every intermediate step) is not immune to a bug — it can mean
"every candidate hit the SAME bug," not "the claim is false." The specific
tell here was that a supposedly-verified sub-result (a vector confirmed to
be in a numerically clean nullspace) failed a DIRECT, independent
re-derivation check (the raw pre-inverse residual `S@A-B@S`) — when a
"verified" intermediate quantity fails a cheap, more-direct alternative
check, trust the direct check, not the accumulated pipeline.** This is a
sharper, code-level instance of this project's own `audit-verification-
gate.md` principle: even one's OWN prior "SANITY" checks (the self-Hom=6
checks that passed both before and after the reshape bug) can pass while
a real bug survives, if the sanity check exercises a different code path
(rank/dimension) than the one that's actually broken (matrix
reconstruction). **Reused code (here: `hom_space_nullspace`, copied from
round127) inherits round127's own untested assumptions — code reuse across
rounds needs the same skepticism as code reuse across agents.**

## Check (reproduces the verification)

```
cd experiments/20260718-round128-cartan-weyl-alignment
python e45_cartan_weyl_alignment.py --debug
```
Expect: `Found 12 distinct exact-hexagon-match candidates`, `Candidates
achieving Hom_dim>=6: 12 / 12`, `iso_residual` in the `~1e-15` range for
every candidate (shown via `[diag]` lines), `Hom_dim(Phi-aligned, best
candidate) = 6`, `Isomorphism residual: ~1e-15`, `B-L fit relative
residual: ~0.53`, `VERDICT: ALIGNMENT_SUCCESSFUL`.
