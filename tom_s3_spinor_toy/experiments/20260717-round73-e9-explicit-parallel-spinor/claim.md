# E9 — Claim: explicit ∇^t-parallel spinor, direct construction and verification

**Date:** 2026-07-17
**FL tier:** [x] Full (research claim; methodology per project CLAUDE.md)
**Question type:** [x] descriptive [ ] predictive [ ] causal

Descriptive: for the naturally-reductive one-parameter connection family ∇^t on
S³=SU(2)/{e} (Agricola, arXiv:math/0202094 — the same G/{e} presentation used by
E2 and E7), does an *explicit*, symbolically-constructed, constant (left-invariant)
spinor ψ satisfy ∇^t_{Z_i}ψ=0 for all three frame vectors simultaneously at t=0
and/or t=1, and does substituting that *same* ψ into Agricola's own eq.(5)
`D^tψ = Σ_i Z_i·Z_i(ψ) + t·H·ψ` give exactly zero?

## Stakes
Internal-only (mechanical verification of an already-accepted abstract argument
from E7's `decision.md` "Recomposition" section — H1b). Not promoted to
`preprint.tex` here.

## Background (established, not re-derived here)
- E2 (`experiments/20260717-round67-e2-s3-torsion-deformation/`): Cl(3) built via
  Pauli matrices `Z_i = i·σ_i`, `{Z_i,Z_j}=-2δ_ij`, structure constant `c := <[Z1,Z2]_m,Z3>`,
  Kostant cubic element `H = (3c/2)·ω` with `ω = Z1·Z2·Z3` verified **exactly** the
  2×2 identity matrix (scalar, central), calibrated `h_H = 3` (⟺ `c=2` since
  `h_H=(3/2)c`). Agricola eq.(5): `D^t ψ = Σ_i Z_i·Z_i(ψ) + t·H·ψ`.
- E7 (`experiments/20260717-round72-e7-t-selection-principle/`): full curvature
  `R^t(X,Y)Z = t(t−1)·S(X,Y,Z)` vanishes **exactly** at t=0,1 (Cartan–Schouten flat
  connections), verified over all 27 basis triples, symbolic in `c`.
- E7's `decision.md` "Recomposition" (H1b) argues, via a **general abstract
  theorem** (flat + metric-compatible connection on simply-connected S³ ⟹ trivial
  holonomy in Spin(3) ⟹ a global ∇^t-parallel spinor exists at t=0,1 ⟹ D^tψ=0
  identically), that this is not a numerical coincidence. This step was **not**
  independently verified by direct construction — that is exactly this experiment's job.

## Claim (falsifiable)

There exists an explicit, exactly-computable spin-connection 1-form
`Ω_i(t) = (1/4) Σ_{j,k} Γ^k_{ij}(t) · Z_j·Z_k` (the standard spin lift of the
so(3)-valued frame connection `Γ^k_{ij}(t) := ` coefficient of `Z_k` in
`∇^t_{Z_i}Z_j = t[Z_i,Z_j]`), such that:

1. `Σ_i Z_i·Ω_i(t) = t·H` **exactly** (symbolic in t,c) — i.e. the spin-lift
   construction, derived independently from the connection's own definition (NOT
   copied from Agricola's eq.5), exactly reproduces the algebraic term Agricola's
   eq.(5) asserts abstractly. This is the "derive, don't assert" requirement.
2. At **t=0**: `Ω_i(0)=0` for all i=1,2,3 (since each Ω_i is proportional to t)
   ⟹ **every** constant (left-invariant) spinor ψ is exactly ∇^0-parallel (a full
   2-dimensional space, not a single vector) ⟹ substituting into eq.(5) gives
   `D^0ψ = 0` exactly, for any such ψ.
3. At **t=1**: the *same* ansatz (ψ a constant left-invariant spinor) is tested.
   The claim is agnostic in advance about whether this succeeds — see kill
   criterion below. (Framed honestly: it is logically possible the naive ansatz
   fails at t=1 even though the abstract holonomy argument for *some* parallel
   spinor's existence remains valid — the abstract argument does not specify
   which trivialization the t=1 parallel spinor is constant in.)

## Kill criterion (MANDATORY — filled BEFORE running)

| Kill condition | Threshold |
|---|---|
| Spin-lift cross-check fails (Ω_i construction does not reproduce ±t·H exactly, symbolic in t,c) | `crosscheck_matches_tH == False` — would mean the "standard formula" stated in the task is mis-specified or mis-applied here; the whole construction would need to be redone |
| Frame connection Γ^k_{ij}(t) is NOT so(3)-valued (antisymmetric in j,k) for some i | `so3_valued_all_i == False` — would mean ∇^t as coded is not actually metric-compatible, contradicting E2/E7's own established fact |
| Ω_i(0) ≠ 0 for some i | `t0_omega_all_zero == False` — would directly contradict "∇^0 is flat" (E7) and falsify the whole t=0 claim |
| D^0ψ ≠ 0 for the constructed t=0 spinor (exact symbolic substitution into eq.5) | `t0_D_psi_is_zero == False` |
| At t=1, a nonzero ψ satisfying `Ω_i(1)ψ=0` for all i IS found | if found → claim 3 is **stronger** than expected (both signs work with the naive ansatz) — report as PASS-BOTH, not a kill, but flag if this happens since it was not the expected outcome |
| At t=1, only the trivial ψ=0 solves `Ω_i(1)ψ=0` for all i simultaneously | this is the anticipated "ansatz too naive" outcome flagged in the task — NOT a kill of the t=0 result, but downgrades the t=1 sub-claim to PARTIAL/OPEN, to be reported honestly, not forced into a fake PASS |

If the t=0 checks all pass and the cross-check (claim 1) holds → the CORE claim
(E7's abstract argument is concretely, mechanically verified at t=0) is PASS,
regardless of what happens at t=1. If the t=0 checks fail → the core claim is
FALSIFIED and E7's Recomposition argument needs re-examination (a genuine,
consequential result, not merely a formality).

## Method

1. Reuse E2's exact Cl(3) construction (Pauli matrices, `Z_i=i·σ_i`) and verify
   Clifford relations hold (repeat E2's own check, not assumed).
2. Reuse E7's exact su(2) bracket convention (`eps(i,j,k)`, symbolic structure
   constant `c`, `[Z_i,Z_j]=c·ε_{ijk}Z_k`) to build the frame-connection
   coefficients `Γ^k_{ij}(t) = t·c·ε_{ijk}` directly from the task's own stated
   definition `∇^t_XY=t[X,Y]` (not from Agricola's eq.5).
3. Verify `Γ^k_{ij}(t)` is so(3)-valued (antisymmetric in j,k) for every i,
   exhaustively — a structural sanity control, analogous to E7's Jacobi-identity
   check.
4. Build the spin lift `Ω_i(t) = (1/4)Σ_{j,k}Γ^k_{ij}(t)·Z_j·Z_k` using the
   **standard** spin-connection formula (Lawson–Michelsohn / Friedrich, spin
   geometry textbook fact — cited as [DOCS], not re-derived from scratch, but its
   *application* to this specific ∇^t here is derived, not assumed).
5. Cross-check `Σ_i Z_i·Ω_i(t) = ± t·H` exactly, symbolic in t,c, against E2's
   own established `H=(3c/2)ω`. This is the independent verification link
   required by the task ("derive/state this explicitly... don't just assert it").
6. At t=0: verify `Ω_i(0)=0` for all i; take ψ = e1=(1,0), e2=(0,1), and a
   generic symbolic combination (a,b); verify `Ω_i(0)ψ=0` trivially for all
   three, then substitute into eq.(5) `D^0ψ = Σ_iZ_i·Z_i(ψ) + 0·H·ψ` (orbital term
   0 since ψ constant) and verify exactly 0.
7. At t=1 (c=2, the project's own calibrated value): solve the combined linear
   system `Ω_i(1)ψ=0` for i=1,2,3 simultaneously (6 scalar equations in 2 unknowns
   a,b, over ℂ) via sympy `solve`/nullspace; report whether a nonzero solution
   exists. Independently cross-check via Agricola's own Theorem-4.2 route: since
   `H=3·I₂` (calibrated, invertible), `D^1(constant ψ) = 1·H·ψ = 3ψ`, which is
   zero only for ψ=0 — a second, independent confirmation of whatever the direct
   parallel-transport computation finds.

## What this does NOT mean

1. Does **not** re-derive or challenge E7's abstract holonomy theorem itself
   (flat + simply-connected ⟹ trivial holonomy ⟹ parallel spinor exists) — that
   is a standard, general fact this experiment takes as given [DOCS]. This
   experiment only checks whether the *specific*, simplest candidate (a constant
   spinor in the left-invariant trivialization already used throughout this
   project) realizes that abstract guarantee.
2. A t=1 failure of the naive ansatz would **not** falsify E7's abstract argument
   for t=1 — the abstract theorem only guarantees existence of *some* global
   parallel spinor, in *some* trivialization; it does not promise that trivialization
   is the same left-invariant one used for t=0. A failure at t=1 would show the
   *specific, concrete, same-frame* construction requested by the task does not
   extend symmetrically to t=1, which is itself the honest, useful finding the
   task explicitly anticipated as a possible outcome.
3. Does **not** touch H1c, H2, H3 (E7's still-open physical-selection questions)
   at all — this experiment is purely about the mathematical mechanics of the
   zero mode at t=0/1, not about which of t=0 or t=1 (if either) is physically
   realized.
4. Does **not** verify the generalized product-decoupling formula for the full
   S³×S⁶ operator (E2/E3's own flagged open item) — this experiment only concerns
   the S³ factor's Dirac operator D^t alone.

## Assumptions (status)

| Assumption | Status |
|---|---|
| Standard spin-lift formula `∇^spin_Xψ = X(ψ) + (1/4)Σω_{jk}(X)γ^jγ^kψ` for an so(n)-valued connection ω | [DOCS] — standard spin-geometry fact (Lawson–Michelsohn / Friedrich); applied here, not re-derived from first principles of spin geometry itself |
| `∇^t_XY = t[X,Y]` (task's own stated definition, matching E2/E7's convention) | [VERIFIED-external-source, inherited from E2/E7] |
| E2's established `H=(3c/2)ω`, `h_H=3`, `c=2` | [VERIFIED-tool, inherited from E2] — not re-fit here, used only as the cross-check target |
| "Constant spinor" ⟺ `Z_i(ψ)=0` for a left-invariant vector field Z_i acting on a function ψ:G→Δ that does not depend on the group element | [DOCS/standard identification] — same identification E2 already used via Agricola's Theorem 4.2 |
| Sign convention of Ω_i(t) (sign ambiguity noted in E2's own docstring re: Clifford normalization) | resolved empirically by the cross-check (claim 1) — either +tH or −tH is accepted as PASS, since E2 itself flags this sign as a convention artifact, not physical |

## Check
`python e9_explicit_parallel_spinor.py` →
`verdict.crosscheck_matches_tH == true`, `verdict.so3_valued_all_i == true`,
`verdict.t0_omega_all_zero == true`, `verdict.t0_D_psi_is_zero == true`.
t=1 outcome (`verdict.t1_nonzero_solution_exists`) reported honestly either way —
not a kill condition for the t=0 core claim.
