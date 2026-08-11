# decision — C68's hypothesis refuted by ground truth; obstruction is real, sharper, and precisely characterized

## Verdict

`PIPELINE_VALIDATED_ON_GROUND_TRUTH__C68_HYPOTHESIS_REFUTED__OBSTRUCTION_REAL_AND_CHARACTERIZED`
→ **C69 SUPPORTED (P1-P4 all resolved).**
**Date:** 2026-08-11 · L0: descriptive · diagnostics run inline (transcript-traceable commands
against `ob11ii_complexification_bridge.py`'s own importable functions; no separate script file —
each check is a direct invocation of the already-committed C68 module, reproducible from the
commands quoted below).

---

## Results, all [VERIFIED-numpy]

| # | predicted | found |
|---|---|---|
| **P1** self-match validates pipeline | `hom_dim=6` reachable | **CONFIRMED** — G102-vs-G102 through the identical pipeline (independent seeds 7/99) reaches `hom_dim=6` with mu-residual 3.3e-16 at a matched candidate. **C68's "likely directionality error in the Cartan transport" hypothesis is REFUTED** — the transport formula, root matching, and mu-fit are all correct. |
| **P2** the 4 = singlet block only | exact | **CONFIRMED** — all 4 Hom-basis elements act as **exactly 0** (to machine precision) on the non-singlet sector of round59's side. The cross-construction Hom is precisely `2×2` singlet↔singlet; the `3⊕3̄` sectors contribute **nothing**. |
| **P3** not a chirality swap | conjugation doesn't help | **CONFIRMED** — `Hom(r59, conj(g102))` and `Hom(conj(r59), g102)` both still give 4. |
| **P4** missing `[E,E⁻]→H` relations | distinguishes under-constrained vs obstructed | **(b) GENUINELY OBSTRUCTED** — augmenting the mu-fit with the E-to-Cartan relations (verified internally clean on each side separately, residual ~1e-15) yields a residual of **~2.0e-3 across all 48 candidates × 20 random restarts each** — not a local-minimum artifact, a systematic inconsistency. Under every root correspondence in the full `Weyl×Out` family, the candidate map cannot be extended to a Lie-algebra isomorphism consistent with both the `[E,E']∝E''` and `[E,E⁻]∝H` bracket structures simultaneously. |

## What this means, stated carefully

1. **The pipeline is exonerated.** C68's parting hypothesis was wrong and is corrected here —
   the same code, same formulas, same fit reach the right answer on a known case.
2. **The obstruction is real and now sharply characterized:** the two constructions' singlet
   sectors intertwine freely (as they trivially must), while their `3⊕3̄` sectors refuse to,
   under every candidate correspondence, including with the previously-missing bracket
   relations enforced and with global multi-restart search.
3. **This does NOT contradict C65** — an abstract isomorphism still exists (module types match).
   What fails is every correspondence *this specific construction procedure* generates. The
   remaining concrete suspect, identified but NOT yet tested (next round's hypothesis, not
   asserted): round59's genuinely complex CSA makes the adjoint action `ad(H)` **non-normal**,
   and `extract_csa_and_roots_complex` reads root values off Rayleigh quotients
   (`v†·ad(H)·v/v†v`) — which equal eigenvalues only for normal operators. For G102 (real
   antisymmetric, skew-Hermitian adjoint — normal) the Rayleigh shortcut is exact, which is
   exactly why the self-test passes; for round59's side the root *values* driving the matching
   may be systematically off in a way the hexagon-consistency check cannot detect (it only
   checks internal consistency of the same possibly-shifted values). This would produce
   precisely the observed signature: internally clean structure on each side, systematic ~1e-3
   scale inconsistency when cross-matched.

## Kill Analysis

**Killed:** C68's "directionality error" hypothesis — cleanly, by ground truth, one round after
it was proposed. Recorded as a same-arc self-correction.

**Not killed:** C65 (abstract existence), C68's genuine achievements (the complex-CSA fix is
validated further by this round — it is what makes the self-test runnable at all; the
localization to the correspondence pipeline was correct even though the specific suspect within
it was wrong).

**Sharpened for the next round:** test the non-normality/Rayleigh-quotient hypothesis directly —
compute `‖ad(H)·ad(H)† − ad(H)†·ad(H)‖` for round59's extracted `H1,H2` (nonzero would confirm
non-normality), then replace the Rayleigh-quotient root extraction with true simultaneous
diagonalization (e.g. via a Schur decomposition or generalized eigenvectors) and re-run the
matching. That is a well-defined, single-hypothesis follow-up.

## What this does NOT show

1. Does **not** find the intertwiner — the goal remains open.
2. Does **not** prove the non-normality hypothesis — identified as the next single-variable test,
   deliberately not bundled into this round (Minimal Relaxation Rule).
3. Does **not** contradict C65's existence guarantee.
4. Nothing about `N_gen=3`'s CONDITIONAL status changes.

## Reproduction

All commands are direct invocations against the committed C68 module
(`../20260811-ob11ii-complexification-bridge-test/ob11ii_complexification_bridge.py`):
P1: two independent `extract_csa_and_roots_complex` calls on `su3_g102_on_channel_v()` (seeds
7/99) + the standard candidate loop → `hom_dim=6` found. P2: `hom_basis` on the direct pair +
projector onto round59's non-singlet sector → all 4 elements annihilate it exactly. P3:
`hom_basis` with either side conjugated → still 4. P4: mu-fit extended with
`[E_α,E_{−α}]→(H1,H2)` decomposition constraints, 48 candidates × 20 LM restarts → best residual
2.0e-3.
