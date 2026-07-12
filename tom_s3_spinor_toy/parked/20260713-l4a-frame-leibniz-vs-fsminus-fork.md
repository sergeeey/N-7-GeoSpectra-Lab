# PARKED: L4A fork — frame/Leibniz correction vs F_{S^-} incomplete
(for Delta_2x2's trace-free residual K)

**Date:** 2026-07-13
**Source:** experiments/20260708-dolan-casimir-g2su3/decision.md, Rounds
24-45 (21 rounds spanning 2026-07-10 to 2026-07-13)
**Status:** PARKED — genuinely unresolved, not falsified, deprioritized
pending a genuinely differentiating test design

## Parked Pearl fields

| Field | Content |
|---|---|
| Original branch | Round 24's own open fork for `Delta_2x2`'s trace-free residual `K:=[[0,4/3],[4,0]]`: is it (i) a frame/Leibniz correction the naive 3-term Weitzenböck formula (`D²=∇*∇+Scal/4+F_{S^-}`) doesn't capture, or (ii) evidence `F_{S^-}` itself is incomplete? |
| What was killed | The entire "M_p-vs-Z_p" sub-program (Rounds 26/41/42): no per-index bivector connection operator, of ANY connection (Levi-Civita, Agricola's canonical, any t-family member), can ever satisfy Round 26's own aggregate identity — proven as a GENERAL chirality/grading no-go theorem (Round 43), independently confirmed via Agricola 2002's own primary-source definition of `Z_i` (Round 44: `Z_i` is a vector, never a bivector connection). Round 45's specific "blind Leibniz-correction" test design: proven to be a structural tautology (any `kron(X,Id8)`-shaped operator has zero off-diagonal on `span(w_a,w_b)` regardless of `X`, since `w_a`,`w_b` have disjoint index support in BOTH tensor factors) — cannot discriminate fork (i) from fork (ii) by construction, confirmed by 2 independent skeptics + synthesis, with git-timestamp-confirmed empirical circularity on top. |
| What survives | Round 41's complete, exact 5-piece algebraic decomposition of `Delta` (piece_H+step2_rem, T12+T21, TORSION_E, cross_casimir — all individually closed-form, summing exactly to `Delta_2x2`). `Delta_2x2`'s own clean split: trace-average diagonal EXACTLY `5/2=Scal/4` (Round 24), trace-free residual `K` (unexplained). `D64`'s confirmed match to the textbook Leibniz-rule twisted-Dirac-operator TEMPLATE (`D64=Σ_i(e_i⊗Id)·N_i`, Round 45 — though this is a content-free Kronecker identity, not itself a physics check). |
| Revival condition | Resume ONLY when a genuinely NEW differentiating observable is proposed — one that is NOT forced by tensor-support structure (i.e. not automatically zero/nonzero on `span(w_a,w_b)` purely from which basis indices are populated, regardless of the actual connection/curvature content) and NOT assembled purely from already-known pieces of `Delta`'s own 5-piece decomposition. Concretely, the new direction must supply at least ONE of: (a) a prediction on a DIFFERENT SU(3)-multiplicity block (not `span(w_a,w_b)`, where the two singlets happen to be tensor-factor-separable); (b) behavior in NORMAL COORDINATES (a genuinely different computational route, not a re-grouping of the same matrices); (c) an INDEPENDENT closed-form for the curvature term `F_{S^-}` derived from a PRIMARY SOURCE (not this project's own prior construction), to cross-check against; (d) a sign/spectrum prediction on a HELD-OUT representation (not yet used to build or calibrate any existing piece); (e) an operator-INVARIANCE property that a genuine Leibniz correction and an incomplete `F_{S^-}` would satisfy DIFFERENTLY (not just "both give K numerically"). |
| Related future gates | Any future revisit of the L4A norm-bound tension itself (`8/45 vs ~1.03`, still completely untouched by this entire 21-round arc); `Casimir_su3 vs Jac_h` (Round 46, next) shares some of the same primitive-construction toolkit (T-table, curv_h) and could, if it reveals a new structural relationship, indirectly suggest a genuine differentiator for this fork. |
| Forbidden use | Do NOT cite Round 41's 5-piece decomposition, or Round 45's K-match, as evidence favoring EITHER fork (i) or (ii) — both are now known to be uninformative on this specific question (Round 45's own true-kill finding). Do NOT re-attempt a test on `span(w_a,w_b)` using any re-grouping of the SAME 5 known pieces — the disjoint-tensor-support tautology applies to ANY single-factor-embedded split on THIS subspace, not just the one already tried. Do NOT treat `M_p`-vs-`Z_p` (Rounds 26/41/42) as a live avenue — Rounds 43/44 closed it generally and via primary source, independently. |

## Cheapest differentiating test (when revived)

Per the user's own Round 45 wrap-up: the next attempt must be scoped
against ONE of the five revival-condition options above BEFORE any
construction begins (per this project's own Cheapest Differentiating
Test Protocol) — simply re-deriving `Delta`'s already-known pieces in
a new order is not a valid next step, regardless of how it's framed.
