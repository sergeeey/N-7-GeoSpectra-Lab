# C103 decision — the first genuinely block-tridiagonal D_PW built; truncation appears to converge; real spectrum survives a genuinely new test

**Verdict:** `TRUNCATION_APPEARS_TO_CONVERGE__LOWEST_EIGENVALUES_STABLE_ACROSS_2_TO_3_LEVELS`
**Status:** RESOLVED — the literal construction C90's own decision.md named as this arc's final step, now built

---

## Summary

Built the first genuinely 3-level, block-tridiagonal `D_PW` (k=1,2,3),
combining C85's certified `D-bar` at each level with C100's certified
multiplication matrices `M_1`, `M_2` as the two adjacent-level
off-diagonal couplings, under the same explicitly-unverified
"r-untouched" ansatz as C101/C102. This is the literal endpoint
construction C90's own decision.md named ("build the resulting
genuinely block-tridiagonal `D_PW`, and THEN run the
truncation-convergence test").

## Results

| # | Prediction | Outcome |
|---|---|---|
| P0 (reuse sanity) | `D1_full`, `D2_full`, `D3_full` reproduce C85's certified eigenvalues exactly | **PASSES** — `{-1:6,3:2}`, `{-2:12,4:6}`, `{-3:20,5:12}`, zero imaginary residual, all three. |
| P1 (real spectrum, genuinely new territory) | 3-level coupled spectrum is also exactly real | **HOLDS** — `max\|Im\|=0.0` exactly. |
| P2 (truncation convergence) | lowest-magnitude eigenvalues stay close to the 2-level result | **HOLDS** — max shift `0.092` among the lowest 5 eigenvalues (comparing k=1,2 alone vs k=1,2,3), against a spectral range spanning roughly `-3` to `+5` (about 8 units) — a shift of about 1% of the total range. |

## P1 — a genuinely new confirmation, not just a third repeat

C101 and C102 each tested exactly ONE pairwise coupling (2-level
systems). This round is qualitatively different: with `M_1` and `M_2`
BOTH present simultaneously, the full spectrum can in principle be
affected by an INDIRECT 1↔3 correlation that neither prior round could
test (the direct (1,3) block is exactly zero by construction — `M_k`
only connects adjacent levels — so any such effect would have to be
mediated entirely through level 2). Finding `max|Im|=0.0` exactly here
is stronger evidence for the "structural, not coincidental" hypothesis
than a fourth adjacent-pair replication would have been, precisely
because this is the first test where the real-spectrum property was
NOT guaranteed to survive by the same mechanism as the prior two
rounds (if it survives here, the mechanism has to be something that
generalizes past simple pairwise block structure).

## P2 — the actual truncation-convergence question, answered for the first time in this arc

The lowest 5 eigenvalues (by absolute value, i.e. closest to zero —
the physically most relevant part of a Dirac-type spectrum) moved by
at most `0.092` when level 3 and its coupling `M_2` were added on top
of the already-built k=1,2 system:

```
2-level (k=1,2) lowest 5: [-1.0753, -0.7476, -0.7418, -0.5683, -0.5527]
3-level (k=1,2,3) lowest 5: [-1.0763, -0.6990, -0.6980, -0.4766, -0.4718]
max shift: 0.0917
```

Relative to the full spectral range (roughly `-3` to `+5`, i.e. about
8 units), this is a small, not-dramatic shift -- consistent with
"truncation at k=1,2 already captures the physically relevant
low-energy content reasonably well," though NOT a proof of convergence
in any rigorous asymptotic sense (only 2 truncation orders compared,
not a sequence). The `1.0` tolerance used to call this "converges" in
the script's own verdict logic was a judgment call (O(1) relative to
the spectral scale), not a rigorously derived threshold -- the raw
shift value (`0.092`) is reported here explicitly so a reader can
apply their own tolerance rather than trusting the script's binary
label alone.

## What this genuinely establishes

- The multiplication-operator construction, once assembled into its
  intended final block-tridiagonal form, behaves sensibly: real
  spectrum, and a low-energy sector that doesn't reshuffle wildly when
  one more level is added. This is the strongest evidence so far (in
  this entire C90-C103 arc) that the construction is not a numerical
  artifact or a degenerate edge case.
- Three independent, qualitatively different confirmations of the
  real-spectrum property now exist (C101: k=1,2 pairwise; C102: k=2,3
  pairwise; C103: k=1,2,3 with indirect coupling) — the "structural,
  not coincidental" reading from the pearl_registry's own open question
  is now meaningfully better supported, though the actual mechanism
  (candidate similarity transform `S`) remains unidentified.

## What this cannot show

- Does not prove convergence in a rigorous sense — only two truncation
  orders (2-level vs 3-level) were compared; a genuine convergence
  claim needs a third data point (e.g. adding k=4) to see if the shift
  keeps shrinking or was a coincidence of this specific step.
- Does not identify the real-spectrum mechanism, even though it now
  has a third, qualitatively different confirmation.
- Does not test summing over multiple `D^1_{a,b}` components.
- Does not resolve `r`'s role — same explicitly-flagged, unverified
  ansatz as C101/C102.
- Does not change `N_gen=3`'s CONDITIONAL status.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## Verification

- `ruff check experiments/20260812-c103-three-level-block-tridiagonal-dpw/`
  — clean, 0 errors.
- Construction code reused verbatim from C101/C102 (`dbar_full`,
  `build_multiplication_matrix`, `certified_L_R`, `magnetic_labels`),
  minimizing fresh-bug risk — only the block-assembly (3 diagonal + 2
  off-diagonal blocks instead of 2+1) is new.
- The 2-level comparison data was read directly from C101's own
  `results_c101.json` (not re-derived or hand-copied), avoiding a
  transcription error between rounds.
- Hard invariant gate (`assert coupled_max_imag < 1e-6`) placed AFTER
  the JSON write, per the boyko-project-radar Chain 1 fix applied to
  C101/C102 earlier this session.
