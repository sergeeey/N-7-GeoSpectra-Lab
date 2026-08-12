# decision -- dual representation gives a valid su(2) q-side generator, distinct from R_i, Hermiticity matches the already-known R-pattern

## Verdict

`DUAL_REPRESENTATION_VALID_SU2_REP__HERMITICITY_MATCHES_KNOWN_R_PATTERN`
-> **P1 CONFIRMED (all k=1..5). P2 CONFIRMED (all k=1..5). P3 (exploratory):
Hermiticity holds only at k=1, exactly matching R_i's own already-known
pattern.**
**Date:** 2026-08-12 · L0: descriptive · script:
`c93_dual_representation_q_side_generator.py`, results: `results_c93.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** su(2) bracket holds | yes, `k=1..5` | **CONFIRMED** -- `[L1,L2]=2L3` cyclic, exact (symbolic), for every `k` tested. | [VERIFIED-sympy] |
| **P2** `L_i` distinct from `+-l_{e_i}` | yes, `k=1..5` | **CONFIRMED** -- not equal to `l_{e_i}` or its negative for any tested `k`. A genuinely different operator, not a trivial re-labeling. | [VERIFIED-sympy] |
| **P3** anti-Hermiticity (exploratory) | not predicted either way | **`L_i` is anti-Hermitian only at `k=1`; NOT anti-Hermitian for `k=2,3,4,5`.** Crucially, `R_i=l_{e_i}` itself shows the EXACT SAME pattern (anti-Hermitian at `k=1` only) -- `L_i` inherits `R_i`'s own already-documented Hermiticity behavior, not a new independent problem. | [VERIFIED-sympy] |

## What this genuinely establishes

**The dual/contragredient construction `L_i := -l_{e_i}(k)^T` is a
genuine, distinct `su(2)` representation for every level `k`, and its
Hermiticity behavior is not a new obstruction -- it exactly tracks
`l_{e_i}` itself, which this project already knows (from C87/C88) is
only genuinely Hermitian at `k=1`, requiring the general-eigensolver
fallback (`_real_eigvals` in C86) at `k>=2`. This is a reassuring
consistency, not a fresh complication: whoever eventually embeds `L_i`
on the `q` index will need the SAME Hermiticity-awareness this project
already built and uses routinely for `R_i`/`D-bar` -- no new discipline
to invent.**

**Resolves last round's apparent contradiction.** C92 (quaternion
left-multiplication in the `(a,b)` row/column encoding) and this round
(abstract dual representation) were never actually competing answers to
the same question -- C92's approach is inescapably antilinear because it
conflates `q` with a LITERAL matrix row, tied to its own conjugate by
unitarity; this round's approach works in the abstract `V_j*` picture,
where no such conjugation-tying exists. The scoping note in `claim.md`
records this precisely so the distinction is not re-confused later.

## Kill Analysis

**Not killed:** the dual-representation hypothesis for `L_i` -- survives
this round's checks (bracket, distinctness, Hermiticity-consistency)
cleanly.

**Still open, explicitly:** whether `L_i` is the CORRECT construction
for Meier's own specific `q`-index (as opposed to merely A valid `su(2)`
representation) -- this round tests algebraic validity in the abstract,
not physical correctness for this specific codebase's substrate.

## Same-day correction (found while scoping the next round)

This section originally named "a Casimir/`so(4)` check" as "the
genuinely decisive next check." **That overclaimed what such a check
would show.** Verified directly (sympy, `k=1..4`): `C_R := l1^2+l2^2+l3^2`
is exactly scalar (`-k(k+2)` times identity, e.g. `-3,-8,-15,-24`), and
because `L_i=-l_{e_i}^T`, `C_L := L1^2+L2^2+L3^2 = C_R^T = C_R`
**automatically** -- this holds for ANY choice built via the
`-(...)^T` construction, not specifically because `L_i` is correct.
`su(2)` has a unique irrep per dimension, so its Casimir eigenvalue is
fully determined by dimension alone -- EVERY valid `(k+1)`-dim `su(2)`
representation has this same eigenvalue. A Casimir-match check would
have passed for any candidate, discriminating nothing; treating a PASS
as validation would have been a real error, caught before running it
(not after, per this project's own Spot-Check discipline extended
proactively rather than reactively here).

**What would actually be decisive, corrected:** a check that works at
the GROUP level, not just the infinitesimal Lie-algebra level -- e.g.
verifying `g1 . D^j(g) . g2^-1 = D^j(g1 g g2^-1)`-type identities under
EXPONENTIATED generators for concrete group elements, not just that the
generators satisfy the right bracket relations and Casimir. This is a
substantially larger undertaking than this round's algebraic checks and
was not attempted.

## What this does NOT show

1. Does **not** prove `L_i` is physically the correct `q`-side generator
   for Meier's own construction -- only that it is algebraically valid.
2. Does **not** check the combined `(q,p)` system against the full
   Peter-Weyl `G x G` bimodule structure (Casimir/`so(4)` check).
3. Does **not** build or test any coupling/multiplication operator.
4. Does **not** change `N_gen=3`'s CONDITIONAL status.
5. Does **not** solicit or reference Tom Lawrence's unpublished Part 5.

## Reproduction

```
python experiments/20260812-c93-dual-representation-q-side-generator/c93_dual_representation_q_side_generator.py
```
Self-contained -- reuses only C85's own certified `build_l_matrices`
(unmodified).
