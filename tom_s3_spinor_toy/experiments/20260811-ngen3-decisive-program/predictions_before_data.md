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

## Correction note, added 2026-08-11 after C73

**P4's target needed precise identification before testing -- a naive first attempt (raw
kernel of round59's full 64-dim D) gave 36, not 1.** Resolved by reading `preprint.tex`
sec:kernel directly: "kernel=1" refers to D restricted to the SU(3)-invariant sub-blocks
specifically (domain_inv=2, target_inv=1), not the raw or full-bigrading-block kernel (which
are larger, physically-broader quantities addressed separately by Rounds 52-56's certified
Casimir bound). Once correctly scoped: ground-truth reproduction matches round59 exactly;
chirality (ker(D+)=1, ker(D-)=0) verified DIRECTLY from round59's own matrix for the first
time (G74B/C21's claim predates round59 by 3 weeks, was never cross-checked against it until
now); deformation-robustness proven in closed form (D(t)=t*D(1) exactly, kernel=1 for every
t!=0, degenerating only at the singular t=0). **Negative control genuinely FAILS, honestly
reported, not smoothed over:** three attempts within round59's fixed construction (Nomizu
sign flip, alternate bigrading pairing, mismatched-parity pairing) are each either
non-independent (hidden even/odd duality) or algebraically forced (parity constraint), none
testing whether the twist is physically correct. A real wrong-twist control needs twisting by
a different representation than Sigma -- a new construction, not attempted. P1, P2, P3, P5 are
unaffected by this correction.

## Strengthening note, added 2026-08-11 after C73b (user-directed follow-up before C74)

**P4's deformation-robustness result was narrower than it needed to be -- C73's own 1-parameter
sweep covered only the RADIAL direction through NOMIZU's specific point in a larger family that
had not yet been identified.** Direct computation: `dim Hom_su(3)(m, Lambda^2 m) = 2`, not 1 --
NOMIZU is one point on a genuine 2-real-dimensional (one complex-parameter) admissible torsion
family. Sweeping the previously-untested ANGULAR direction (13 angles, full circle): kernel
dimension stays EXACTLY 1 everywhere, with `|b|=sqrt(3)` exact at every point (only the phase
varies, linearly -- a clean U(1) structure). **This substantially strengthens the
deformation-robustness result from a narrow 1-parameter slice to the FULL admissible family.**
Calibration (Killing-spinor existence) stays isolated to NOMIZU's own angle, consistent with
Killing-spinor rigidity -- a genuinely different, sharper condition than kernel-rank protection.
Separately, a fourth negative-control attempt (twisting by `S+` instead of `S-`) was tried and,
like the first three, found NOT independent (same magnitude, consistent with a known conjugation
symmetry) -- the negative-control gap persists, now across four attempts. P1, P2, P3, P5 are
unaffected.

## Correction note, added 2026-08-11 after C74

**P5 is neither PASS nor FAIL -- genuinely inconclusive, not triggering the pre-commitment
below.** Groundwork is rigorous: Clifford sign match confirmed for round59 x round67 (a real,
previously-unchecked risk per OB10), S3's n=0 level cited exactly, S6's kernel vector explicit
(residual 1.665e-16). Transporting this kernel content through C70/C71's independently-verified
`U_v`/`U_s`/`U_c` (each used once, avoiding C71's tautology trap) gives NONZERO content in all
three channels -- but this relies on a marginal-projection heuristic explicitly flagged as NOT
rigorously derived (the kernel is a genuinely entangled bipartite state, not a simple product).
**"Yields three physically distinguishable sectors" is NOT established either way** -- three
formally-distinct constructed objects are not automatically three physically distinguishable
generations; that determination requires an observable that tells them apart, explicitly
deferred to C75 by the round table's own division of labor. The pre-commitment ("if P5 fails,
weaken N_gen=3") is NOT triggered, since nothing here constitutes a failure -- it is an honest
"not yet resolved," to be closed by C75. P1, P2, P3, P4 are unaffected.

## Correction note, added 2026-08-11 after C75

**C75 did NOT run the redundancy/commutant attack this section specifies below --
it ran a narrower, adjacent test that became newly possible: `TRIALITY_
DISTINGUISHABILITY_GATE.md`'s own Gate 2 (does the physical `D` commute with
the extended, channel-DISTINGUISHING `su(3)+u(1)+u(1)` symmetry that document's
Gate 1 already constructed), for round124's specific candidate.** Result: NO --
large, unambiguous violation (65.5% and 352% relative to `|D|_F`, against a
positive-control noise floor of `2.8e-17`), computationally confirming G74A's
Lemma B for the first time. **This is genuinely useful (closes a previously
"cannot be checked this way at all" gate) but is NOT the channel-PERMUTATION
commutant test described below.** That test needs an operator that maps
`channel_v -> channel_s -> channel_c`; no non-tautological construction of one
exists in this codebase (C71 showed the natural composition is a pure
matrix-algebra tautology, `I=I` for any three invertible matrices built this
way, reconfirmed fully general in C72) and none is built in C75. **The
redundancy question below remains entirely open**, to be either attempted by a
future round with a genuinely new construction, or carried forward as an
explicit open question into C76's synthesis. C75 carries no pre-commitment in
the P1-P5 table below (it was never one of the five), so nothing here weakens
`N_gen=3`'s status either way -- it is an honest "still open," not a failure.

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

## Program CLOSED, 2026-08-11 — final status

**Pre-commitment does NOT fire.** P1 passed cleanly; P3's literal form
proved a pure tautology at every equivariance level (inapplicable, not
failed), its revised form passed as expected; P5 is genuinely inconclusive,
not a failure. `N_gen=3` stays CONDITIONAL, unweakened by rule. Full
synthesis, including an independent context-asymmetric skeptic review:
`experiments/20260811-c76-status-synthesis-ngen3-regrade/decision.md`.

**Honest posterior in one paragraph:** the program substantially hardened
the mathematical scaffolding around the claim (the round59↔G102
triality-channel bridge is now machine-precision-verified through the full
`g2` algebra; round59's real S⁶ kernel=1 is now directly matrix-verified
and robust across the entire admissible torsion family, not a narrow
slice; G74A's Lemma B is now a computational fact via C75, not only an
abstract argument) — while leaving the single question this document
itself named most dangerous (§"The C75 adversarial round, made concrete":
physical channel-distinguishability vs. gauge redundancy of one degree of
freedom) exactly as untested as before the program started. Not from a
negative result — because no non-tautological way to construct the needed
channel-permuting operator has yet been found in this codebase (C71/C72
proved the natural chained construction is a pure tautology at every
equivariance level tried). One concrete, unattempted lead for a future
round: `TRIALITY_DISTINGUISHABILITY_GATE.md`'s own `SO(4)×SO(4)` transport
matrix `T` (already constructed, genuinely non-tautological, never bridged
into round59's `D`) — see C76's decision.md for why this is real,
nontrivial work, not a quick follow-up.

**Post-closure follow-up, C77 (2026-08-11):** user asked to pursue the `T`
lead directly. `experiments/20260811-c77-so4xso4-gate2-and-t-bridge-scoping/
decision.md` found the actual `T`-bridge requires infrastructure that does
not exist (an `SO(4)×SO(4)`-equivariant `Sigma`<->`8_s`/`8_c` identification,
plus resolving round119's own open vector-vs-spinor consistency gap) and is
not a same-round task -- so instead extended C75's Gate 2 methodology to
round119's `SO(4)×SO(4)` candidate directly. Result: fails Gate 2
comprehensively, all 12/12 generators, same pattern as round124's candidate
in C75. Both known Gate-1 candidates now fail Gate 2 -- second, independent
confirmation of G74A's Lemma B's generality. The `T`-bridge's motivation is
correspondingly reduced (see `TRIALITY_DISTINGUISHABILITY_GATE.md` §9). The
channel-redundancy/permutation question itself remains exactly as open as
C76 left it. This round is outside the closed P1-P5 program (not a P1-P5
outcome, does not reopen the pre-commitment), a direct continuation of
C76's own named next step.

**Post-closure follow-up, C78 (2026-08-11):** user asked to try a genuinely
new construction (not another candidate). Rather than testing a third
hand-picked subalgebra, `experiments/20260811-c78-exhaustive-so8-commutant-
of-physical-D/decision.md` computed the FULL commutant of round59's real D
within all 28 dimensions of `so(8)` at once (one SVD null-space
computation, not per-candidate guessing). Result: `commutant_dim=8`,
exactly `su(3)`, no larger symmetry exists at all -- an exhaustive,
theorem-level closure of the entire "does some so(8) subalgebra distinguish
the channels and commute with D" question, superseding C75's and C77's
individual negative results. This directly closes `L3B_SPIN8_INTERFACE_
SPEC.md` section 1.5's own long-standing "Dynamics" open item. The one
remaining door -- a structurally non-product, `G2`-breaking `D` -- is
outside what any `so(8)`-symmetry search can address and needs content
(Part 5) this project does not have. Same as C77: outside the closed P1-P5
program, does not reopen the pre-commitment, does not change `N_gen=3`'s
CONDITIONAL status.

**Post-closure follow-up, C79 (2026-08-11):** user asked to go for the
non-product construction -- the one door C78 explicitly left open.
`experiments/20260811-c79-nonproduct-s3s6-coupling-attempt/decision.md`
built an actual off-diagonal S3-S6 coupling term (round67's `Z_i` + round119's
`so(4)_1` self-dual triple, `S3`'s `n=0` sector), the first genuine joint
operator this project has ever constructed explicitly. Result: NULL for
this specific postulate -- an apparent zero-crossing was found and then
fully explained as an artifact of `D_S6`'s already-known 36-dim raw kernel,
unrelated to any new physics. Two valuable side-findings: `U_v` (C70's
bridge, reused since) is not unitary (found, fixed, documented), and
C75/C77/C78's own conclusions were confirmed ROBUST to this via an explicit
check across multiple valid intertwiner choices. Does not solicit Tom
Lawrence's Part 5; does not change `N_gen=3`'s CONDITIONAL status; does not
close the non-product door in general, only for this one postulate.

**Post-closure follow-up, C80 (2026-08-11, self-directed -- user left this
round's scope open):** completed C79's self-dual/anti-self-dual pair
(`experiments/20260811-c80-status-resynthesis-and-methodology-fix/
decision.md`) -- the anti-self-dual half produces the SAME artifact
(crossing at `eps=-1.5`, sign-mirrored, `99.9999999999996%` inside `D_S6`'s
raw kernel). This upgrades C79's single-instance finding to a generalized
conclusion: the test design itself (sweep coupling strength, look for any
crossing in the full space) cannot discriminate genuine physics from this
artifact for ANY generic coupling, not a fluke of one postulate. Re-
synthesized C76-C79 given this and recommended pausing blind non-product
postulate testing with the current design -- not because the door is
closed, but because testing more candidates the same way is unlikely to
produce new information. Named two genuinely different next steps (fix the
test design by excluding the raw kernel; scale to the full Peter-Weyl
tower) for a future round. Outside the closed P1-P5 program; does not
change `N_gen=3`'s CONDITIONAL status.

**Post-closure follow-up, C81 (2026-08-11):** user asked to implement
C80's own named fix directly: "Fix the test design and re-run so(4)_1
both halves." `experiments/20260811-c81-raw-kernel-excluded-retest/
decision.md` compressed `D_joint` onto `Delta_m (x) D_S6`'s 28-dim
non-kernel eigenspace (spectrally gapped at `|0.8165|`, confirmed by
direct read of `D_S6`'s full spectrum), so the deterministic raw-kernel
mechanism cannot occur by construction. Result: ZERO crossings for
EITHER `so(4)_1` half; the closest approach was verified by a fine
31-point scan to be a genuine avoided crossing (level repulsion), not a
near-miss. A full-spectrum cross-check confirms no non-artifact signal
was hidden by the compression. This specific postulate is now a clean,
rigorously-confirmed NULL -- the fix worked exactly as C80 predicted it
would. Outside the closed P1-P5 program; does not change `N_gen=3`'s
CONDITIONAL status; does not solicit Tom Lawrence's Part 5.

**Post-closure follow-up, C82 (2026-08-11):** user asked to test `so(4)_2`
directly. `experiments/20260811-c82-so4-2-raw-kernel-excluded-test/
decision.md` applied C81's corrected test unmodified to round119's
second octonion block (`BLOCK2=[4,5,6,7]`, never before tested with this
methodology). Both `su(2)` halves: zero crossings, closest approach
verified genuine avoided crossings via fine scan (magnitude ~9x larger
than `so(4)_1`'s own, unexplained, logged as a pearl). Full-spectrum
cross-check: all near-zero eigenvalues classified as raw-kernel
artifacts. **Both octonion blocks of round119's `SO(4)xSO(4)` candidate
(all 4 `su(2)` halves) are now clean, rigorously-confirmed NULLs.**
Outside the closed P1-P5 program; does not change `N_gen=3`'s
CONDITIONAL status; does not solicit Tom Lawrence's Part 5.

**Post-closure follow-up, C83 (2026-08-11):** user asked to test the
remaining complement elements. `experiments/20260811-c83-remaining-
complement-test/decision.md` found, while scoping (not guessing), that
`so(4)_1+so(4)_2` has an EXACT 1-dim intersection with `su(3)` itself (a
specific linear combination commutes with `D`, machine precision) --
refines, does not contradict, C77's own basis-by-basis finding. This
leaves a genuine 9-dim untested remainder (computed rank-aware after
catching and fixing three flawed attempts during scoping), tested in 3
systematic groups via C81's corrected methodology: zero crossings, all
fine-scan-verified. **Combining C75+C77+C79-C83: every dimension of
C78's 20-dim `so(8)` complement is now tested against the physical `D`
-- no candidate anywhere has produced a genuine crossing.** Outside the
closed P1-P5 program; does not change `N_gen=3`'s CONDITIONAL status;
does not solicit Tom Lawrence's Part 5.

**Post-closure follow-up, C84 (2026-08-12):** user asked to try the full
Peter-Weyl tower directly ("Continue with C84 -- try the full Peter-Weyl
tower"). `experiments/20260812-c84-sigma-minus-branch-and-n1-ansatz-null/
decision.md` first resolved a genuine internal ambiguity by tracing
C74/C79-C83's own WORKING CODE (not docstrings): "sigma" has always meant
a choice between two SEPARATE scalar*I2 constructions at n=0, never a
subspace of one physical `Delta_m`. Built and tested `sigma=-1` at n=0 as
a real extension (clean NULL for round119's `so(4)_1` pair, mirror-
symmetric to `sigma=+1`). Attempted `n=1` honestly: the cheapest naive
ansatz (`Delta_m (x) V_1`, standard spin-1/2 angular momentum) was built
and diagonalized -- it does NOT match round67's own closed-form target
(mult 3,1 found vs 6,6 required), an explicit, numerically-verified NULL
for this specific construction, with a Kill Analysis + Relaxation Map
recorded for the surviving attempts (full outer(x)inner Peter-Weyl block;
consult Sire & Xu arXiv:2005.01448 directly). **The full Peter-Weyl tower
is NOT completed -- n=0 (both branches, one candidate pair) is now
covered, n>=1 remains genuinely open.** Outside the closed P1-P5 program;
does not change `N_gen=3`'s CONDITIONAL status; does not solicit Tom
Lawrence's Part 5.

**Post-closure follow-up, C85 (2026-08-12):** an external reviewer
proposed restructuring the Peter-Weyl tower effort into staged
certification (C84A) -> selection-rule computation (C84B) -> coupled
spectral flow (C84C), with C84A requiring a real certification gate
(bracket relations, Casimir identity, negative control), not just an
eigenvalue-match check. `experiments/20260812-c85-peter-weyl-
representation-certification/decision.md` executed C84A: found the
"Sire & Xu" citation attached to round67's own multiplicity formula
since 2026-06-20 (g34) does not actually support it (read directly, no
S3 content in that paper) -- the real source is Meier (2011,
arXiv:1103.4097). Building Meier's explicit construction, the LITERAL
transcription of his eq 6.3 fails hard structural invariants (Lie
brackets, Casimir, the quadratic Dirac identity) at k>=2. Tested and
CONFIRMED a reviewer-supplied falsifiable repair hypothesis (a likely
transcription typo, "p-1" for "p-k") exactly for k=0..10, with a working
negative control. Independently cross-confirmed via a SECOND, unrelated
source (Camporesi & Higuchi 1995/96) giving the identical closed-form
formula via a completely different method (separation of variables, no
representation theory). **round67's own long-uncited formula is now
correctly sourced and independently confirmed twice over, and this
codebase has its first explicit, certified S3 Peter-Weyl representation
substrate for k>=1.** Named next step (C84B, not attempted): compute
selection-rule matrix elements to determine whether the coupling
operator is diagonal in Peter-Weyl level or genuinely mixes levels.
Outside the closed P1-P5 program; does not change `N_gen=3`'s
CONDITIONAL status; does not solicit Tom Lawrence's Part 5.
