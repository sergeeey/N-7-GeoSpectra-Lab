# decision -- direct solve finds the round59<->G102 su(3) intertwiner; OB11(ii) hard half closed

## Verdict

`INTERTWINER_FOUND__MACHINE_PRECISION__CONTROLS_PASS__OB11II_HARD_HALF_CLOSED`
-> **C70 SUPPORTED (P1-P4 all resolved).**
**Date:** 2026-08-11 · L0: descriptive · script: `c70_bridge_diagnostics.py`, results:
`results_c70.json`. Two independent runs (different seeds for the negative control) agree
to within expected numerical noise.

---

## Results, all [VERIFIED-numpy]

| # | predicted | found |
|---|---|---|
| **P1** non-normality test | normal or non-normal | **REFUTED** -- `commutator_norm=3.0e-17`, `max_eigenvector_residual=1.1e-15`. round59's `ad(H)` is normal; C69's identified suspect is ruled out. |
| **P2** bracket invariant | match or mismatch | **MATCH** -- `24.0` (r59) vs `24.0` (g102), ratio `1.0000000000000002`. No structure-constant scale/normalization mismatch between the two constructions. |
| **P3** direct global solve for `Phi` | nondegenerate isomorphism or clean failure | **FOUND, ROBUSTLY** -- 15/15 random restarts converge to `max_residual` in the `1e-14`-`1e-15` range with `\|det(Phi)\|=1.0000` (to 12+ significant figures) every time. A first, unconstrained version of this solve (not saved as a separate run) had collapsed to the trivial sink `Phi=0` on all restarts (`max_residual~1e-324`, `det=0.0`) -- the bracket-preservation residual is quadratic-minus-linear in `Phi`, so `Phi=0` is always an exact root of an unconstrained least-squares objective; adding a soft non-triviality constraint (`\|Phi\|_F^2 -> 8`) removes that sink. |
| **P4** representation-space intertwiner `U`, given `Phi` | matches ground-truth benchmark or falls short | **CONFIRMED, MACHINE PRECISION** -- pushing round59's representation forward through the found `Phi` and re-running `hom_basis`/`search_nonzero_intertwiner` (both reused unmodified from C68) gives `hom_dim=6` (matching C69's own `G102`-vs-`G102` ground truth exactly, not the previously-stuck `4`), a nondegenerate `U` is found (`\|det(U)\|=0.069`), and **explicit direct verification** `max_k \|\|U @ M_k @ U^-1 - Xk_g102\|\|` = **3.8e-16 to 4.4e-16** across two independent runs -- `U` genuinely intertwines the transported representation, not merely "some nonzero matrix in a null space." |

## Controls (Gate 3 / Perelman no-collapse discipline)

The clean 15/15-identical-signature result for P3 is exactly the shape
`skeptic-triggers.md` flags for mandatory verification before trusting it. Two controls
were run before accepting the result:

| Control | Setup | Result |
|---|---|---|
| **Positive (ground truth)** | `g102`-vs-`g102` self-match (identical structure tensor both sides; `Phi=I_8` is an exact solution of both the bracket condition and the norm constraint, since `\|\|I_8\|\|_F^2=8` exactly) | `max_residual` in `1.8e-14`-`1.6e-13`, `\|det(Phi)\|=1.0000` -- **same signature as the real result.** |
| **Negative (impossibility check)** | `r59`-vs-8-independent-random-anti-Hermitian-matrices (no genuine Lie-algebra closure, not isomorphic to `su(3)`) | `max_residual` in `0.17`-`0.27` (**13 orders of magnitude worse**), `\|det(Phi)\|` collapses toward `~1.6e-6`-`4.7e-6` (near-singular, the norm constraint fighting the `Phi->0` pull with nothing genuine to converge to) -- **fails cleanly.** |

The test discriminates a known-good case from a known-impossible case by 13 orders of
magnitude in residual. This satisfies Gate 3's requirement ("a test that cannot
distinguish your control from your target is not a test") and gives strong confidence the
r59-vs-g102 result (identical signature to the positive control) is genuine, not an
artifact of an under-constrained or vacuously-satisfiable objective.

## What this means, stated carefully

1. **The round59<->G102 su(3) bridge is closed, at both levels.** `Phi` (the abstract
   Lie-algebra isomorphism, matching structure constants) and `U` (the representation-space
   intertwiner, the object actually needed downstream) both exist and were found to machine
   precision, verified two independent ways (residual of the solve itself, and explicit
   direct re-verification of the intertwining property).
2. **This does not contradict C69's P4 finding** ("genuinely obstructed" root-matching
   search) -- it explains it. C69's root-matching pipeline searched only a *discrete* space
   of candidates (Weyl group x outer automorphism x real mu-rescaling) around CSA roots
   extracted at one *fixed* linear combination (`combo_weight=0.37123`). The genuine
   isomorphism apparently requires a *continuous* inner-automorphism component (`Inn(su(3))`
   is 8-real-dimensional) that a fixed-weight, discrete-candidate search structurally
   cannot reach. This diagnosis is plausible and consistent with all observations but is
   **[INFERRED]**, not independently confirmed by a dedicated reconciliation test (out of
   scope for this round; flagged in claim.md).
3. **Non-uniqueness of `U` is expected, not a defect.** `Inn(su(3))` acts transitively on
   the solution set (composing the found `Phi`/`U` with any inner automorphism of the
   source algebra gives another valid solution) -- this is exactly why 15 random restarts
   of the constrained solve land on 15 *different* `Phi` matrices (all with `\|det\|=1`,
   consistent with `Ad(g)` preserving the Killing form for connected `g`), not one.

## Kill Analysis

**Not killed, resolved positively:** the specific numerical-pipeline obstruction C68/C69
had localized (root-matching pipeline cannot extend to a full isomorphism) is now
understood as a limitation of that SPECIFIC method, not evidence against the bridge's
existence -- exactly as C69's own "what this does NOT show" section anticipated ("a
failure of every numerically constructed candidate correspondence to extend is a statement
about the construction procedure's remaining blind spot, not about abstract existence").

**What survives:** C65's module-type match (prerequisite, now fully cashed out into an
explicit intertwiner); C68's complex-CSA fix and localization (correct, superseded in
approach but not in content); C69's ground-truth-control discipline (directly reused here
as this round's own verification method).

## What this does NOT show

1. Does **not** transport `D`, `J`, `gamma`, `B-L` -- that is the next round (C71, ledger
   numbering).
2. Does **not** establish uniqueness of `U` -- see above; C71 must fix one representative.
3. Does **not** independently confirm the "fixed-weight root extraction misses continuous
   inner-automorphism freedom" diagnosis -- plausible, not separately tested.
4. Nothing about `N_gen=3`'s CONDITIONAL status changes -- one blocker (OB11(ii) hard half)
   is closed within a still-open larger program.

## Reproduction

`python experiments/20260811-c70-independent-bridge-fingerprint-and-direct-solve/c70_bridge_diagnostics.py`
-- self-contained, reuses `round128`'s `ad_matrix`/`orthonormalize` and C68's
`to_numpy_su3_r59`/`su3_g102_on_channel_v`/`hom_basis`/`search_nonzero_intertwiner`
unmodified via the same `load_module` pattern C68 established. Full output in
`results_c70.json`.
