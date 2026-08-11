# N_gen=3 decisive-experiment program — predictions recorded BEFORE C70-C76 run

**Date frozen:** 2026-08-11, before any C70+ computation.
**Mode shift (user-directed):** from "closing accumulated blockers" to a decisive-experiment
program around `N_gen=3`. New registries/gates/pearls FROZEN unless a new class of systematic
error is found. **L0 (EstimandOps):** each round below is descriptive (existence/structure of
finite operators); each gets its own claim.md at kickoff.

## The strong testable thesis

> S³×S⁶ geometry naturally produces exactly three equivalent matter channels, where "three" is
> a structural property of the full operator — not a basis choice (C63 closed), not S³ doubling
> (C41-C60 closed), not a Casimir coincidence (fingerprint test below), not triality bookkeeping.
> Target form: `H_phys ≅ H_matter ⊗ G`, `dim G = 3`, with compatible `(D, A, J, γ)`, where the
> 3-dimensionality of `G` cannot be removed by any admissible transformation.

**Status: CONDITIONAL hypothesis, not an established result.** Survived attempts ≠ proof.

## Numbering note

The user's proposed "C69" is ledger-C70: C69 (ground-truth control) already ran — it refuted
C68's directionality-bug hypothesis, validated the pipeline on a known case, characterized the
obstruction (cross-Hom = exactly singlet block; EEE+EH fit systematically inconsistent ~2e-3
across 48 candidates × 20 restarts), and identified the non-normal-`ad(H)`/Rayleigh-quotient
suspect. C70 is the independent method that supersedes that pipeline entirely.

## Correction note, added 2026-08-11 after C71

**P2's premise needs revision, discovered mid-C71.** `D_59` (round59's `build_dirac()`) is
64-dim (`Σ⊗Σ`, an S⁶-only construction for a different prior round's purpose), not
transportable through the 8-dim `U` as literally described; no `J`/`γ` exists for it; no
`P_i` projectors exist anywhere. Separately,
`experiments/20260717-round118-matter-generation-factorization-test/` (a PRIOR round,
2026-07-17) already precisely scoped this exact hypothesis with `H_matter` = G18's
**32-dim** NCG finite spectral triple, not round59's `Σ` — and already found: STRONG
reading (gauged SU(4)) BLOCKED by G97; WEAK reading necessary condition (charge
uniformity) VERIFIED; WEAK reading sufficiency (identical 32-dim block structure per
channel; no channel-mixing in D; triality acting with no admixture on the matter factor)
left explicitly OPEN. C71 attempted a shortcut toward the "no admixture" sufficiency
condition using C70's fresh channel intertwiners (a "monodromy" composition) — this turned
out to be a pure algebraic tautology (self-caught, see C71 decision.md), supplying zero
evidence. **P2, as originally worded, is superseded by round118's own more precise
scoping — the actual open question is round118's sufficiency conditions (i)-(iii) at the
32-dim level, still unresolved.** P1, P3, P4, P5 are unaffected by this correction.

## Correction note, added 2026-08-11 after C72

**P3's `T^3=1` premise needs revision, discovered while attempting it.** Building `T` by
chaining three independently-found pairwise channel intertwiners through a common reference
(`V_vs=U_s U_v^-1` etc., C70/C71's own bridge) makes `T^3=1` a pure algebraic telescoping
tautology -- proven, and re-confirmed for arbitrary random invertible blocks with zero
su(3)/g2 structure (C72). It cannot discriminate genuine triality from arbitrary invertible
relabeling at ANY equivariance level. **What C72 actually tested instead:** the other stated
condition, `T*rho(a)*T^-1=rho(tau(a))`, as `a` ranges over successively larger algebras --
`su(3)` (Hom=6, established) -> `g2` (Hom=2, invertible cross-channel isomorphism newly
constructed) -> `so(8)` (Hom=0, structural negative control, matches triality's own
definition). A genuine, non-tautological `T^3=1` test needs `tau` fixed independently of the
intertwiners under test (e.g. Baez's explicit `S3 subset F4`) -- not attempted. Compatibility
with `D,J,gamma` remains explicitly deferred (S6-embedding gap, 2026-08-11). P1, P2, P4, P5
are unaffected by this correction.

## Predictions (falsifiable, frozen now)

| # | Prediction | If it FAILS |
|---|---|---|
| **P1 (C70)** | An independent, pipeline-free method (weight/character/cubic-invariant fingerprint + direct linear solve of `U·ρ59(X)·U⁻¹=ρ102(φ(X))` over the 2 outer classes of `Aut(su(3))`, inner automorphisms absorbed into `U`) finds a nondegenerate intertwiner, `dim Hom = 6` | First serious anomaly in the Clifford↔triality bridge: same-Casimir ≠ same-module identification was too weak; C65 must be downgraded; headline weakens materially |
| **P2 (C71)** | The transported operator `D_102 = U·D_59·U⁻¹` (with `J`, `γ`, real structure carried along) respects the three-channel structure: mixing matrix `M_ij = P_i D P_j` is either exactly 0 off-diagonal (H1, strict factorization) or has a strictly symmetric form (H2, `D = D_m⊗I₃ + Σ K_α⊗M_α`) | H3: no factorization — three triality channels are representation bookkeeping, not three generations; headline weakens strongly |
| **P3 (C72)** | The state-level triality obstruction system (`T³=1`, `Tρ(a)T⁻¹=ρ(τ(a))`, compatibility with `D,J,γ` — solved as intertwining equations, obstruction-theory style, not blind construction) has a NONZERO solution space | A genuine in-class no-go for `1⊗τ` — OB11(iii) closes negatively; generation label loses its symmetry realization |
| **P4 (C73)** | round59's real twisted `D_S⁶` retains index/kernel=1 under admissible connection deformations, with correct chirality and SU(3) kernel content, negative controls (wrong twist) failing as they must | The S⁶ anchor of the whole construction is accidental, not topological — major weakening |
| **P5 (C74)** | The full product lowest-sector computation — properly framed as `ker D_S⁶ ⊗ (lowest S³ KK level)`, NOT `ker D_full` (which is already KNOWN to be 0: KT-8 NULL, `dim ker D_S³=0` at Levi-Civita, C64) — yields three physically distinguishable sectors without using `t=0/1` as a multiplicity factor | The 4D fermion content does not realize the three channels; headline weakens strongly |

**Pre-commitment:** if P1, P3, or P5 fail, `N_gen=3`'s status must be explicitly weakened in
RESEARCH_STATUS_REPORT.md — recorded here before any computation, per house discipline.

## Known-NULL guards (Adaptive Iteration Branch Rule, checked now)

- **KT-8 / C3:** full 9D `ker D_{S³×S⁶} = 0` — established NULL. C74 is framed to NOT re-run
  this (see P5). Any C74 claim.md must cite KT-8 and state the 4D-reduction framing explicitly.
- **GAP-4:** S³↔S⁶ mode mixing structurally impossible (no S³ quantum number to mix) — C71's
  mixing matrix concerns S⁶-side channel mixing only, orthogonal to GAP-4.
- **Round118-STRONG / G97:** all work remains in the WEAK reading (generation = triality label);
  no gauged SU(4) content is assumed anywhere in C70-C76.
- **G102:** only non-acting so(8) distinguishes channels — C75's observable-distinguishability
  test is precisely the physical-level sharpening of this, not a re-run.

## The C75 adversarial round, made concrete (sharpening the user's point 7)

The most dangerous alternative: the three channels are gauge redundancy — three descriptions of
one physical degree of freedom. C63 closed this at the basis-change level (Spin(8)-Schur), but
NOT at the observable level. Concrete test: compute the commutant of the full physical operator
algebra `{gauge generators, D, γ, J, B-L}` on the three-channel space. If the channel
permutations lie inside that commutant (no physical observable distinguishes channels), the
redundancy reading is LIVE and the headline is in genuine danger; if some physical operator
separates the channels, redundancy is excluded at the observable level — far stronger than C63.

## Round order

| Round | Content | Kill power |
|---|---|---|
| **C70** | independent bridge: fingerprint (weights, characters at generic torus elements, cubic `d_abc` invariant — distinguishes `3` vs `3̄` where quadratic Casimir cannot) + direct intertwiner solve over 2 outer classes | resolves the 6/6/4 anomaly definitively |
| **C71** | transport `(D,J,γ)` through `U`; compute `M_ij = P_i D P_j`; classify H1/H2/H3 | strongest single test of the generation factor |
| **C72** | obstruction system for state-level triality; solution-space dimension | closes OB11(iii) one way or the other in-class |
| **C73** | real twisted `D_S⁶` full battery (chirality, index, gap, deformations, negative controls) | removes the surrogate; tests topological protection |
| **C74** | full product lowest sector (KT-8-aware framing) + unified Clifford convention asserted in-script both sides before tensoring (OB10 lesson) | direct product-level check |
| **C75** | adversarial: observable-distinguishability / redundancy attack | the most dangerous alternative, attacked head-on |
| **C76** | status synthesis: re-grade `N_gen=3` against P1-P5 outcomes | honest posterior update |
