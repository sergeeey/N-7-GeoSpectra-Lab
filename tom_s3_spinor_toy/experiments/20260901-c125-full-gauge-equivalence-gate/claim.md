# C125 claim -- full gauge-equivalence gate for the t=0 vs t=1 pair,
re-prioritized to #1 in C123's Relaxation Map by same-day external
review, after C124 closed the CS/transgression route

## Question type (EstimandOps L0)
**Descriptive/existence.** Does a diffeomorphism/gauge transformation
exist relating the FULL 13D configuration at t=0 to the full
configuration at t=1 -- not merely the abstract S³ connection ω^t
alone (already known, C37-C39/OB13: ι(g)=g⁻¹ realizes ω^0↔ω^1, but ι
is orientation-REVERSING on S³). No causal or predictive claim.

## Background

Already established, cited not re-derived:
- (C37-C39, OB13) `ι:g↦g⁻¹` on `S³=SU(2)` is an isometry realizing
  `t↦1-t`, and is **orientation-reversing** (verified numerically,
  tangent determinant −1 at 200 sampled points); a gauge symmetry
  (connected to the identity) would be orientation-PRESERVING, so `ι`
  is parity, not gauge, per this project's own prior finding.
- (C124) the S³ "ε-sector" leg admits at most one explicit curvature
  factor; `R^t = t(t-1)·R₀` is even in `x=t-1/2`; the odd-in-`x`
  content on S³ lives entirely in the torsion `T^t=(2t-1)[X,Y]`.
- (external, UNVERIFIED here, from an independent multi-agent
  document supplied by the user 2026-09-01 -- `Kimi_Agent` zip,
  `torsion_solution.agent.final.md`) claims that (a) `ι` also swaps
  left- and right-invariant framings, hence `∇^0 ↔ ∇^1`; (b) at the
  level of the FULL 13D spinor structure, `Γ₄ = ±ω₃·Γ₆` is an
  operator identity that would need checking in THIS project's own
  Clifford conventions before being trusted; (c) the same document's
  own internal red team found this specific identity **refuted** in
  its "final" synthesis (§4.3α) after an earlier sub-report
  (`s6_half_dirac_report.md`) asserted it uncorrected -- i.e. the
  external material itself is split on this exact point and must not
  be cited without independent verification in this project's own
  conventions (`docs/clifford_convention_registry.md`).

## Falsifiable claim

There exists a diffeomorphism/gauge transformation `g` of the frozen
13D background `M₁₃=M₄×S³×S⁶` such that `g` simultaneously maps:
(i) the vielbein/connection pair `(e,ω^{t=0}) → (e,ω^{t=1})` on the
S³ factor (or an equivalent pair related by an isometry of the full
product, not just of S³ alone);
(ii) the twist bundle / index data on `S⁶` to itself (unchanged,
since `g` is not claimed to touch the `S⁶` factor);
(iii) the fermion content (the actual zero-mode representations found
this session: `t=0 → (1,2)` of `SU(2)_L×SU(2)_R`, `t=1 → (2,1)`,
per the external document's independently-checkable representation
computation -- to be re-derived in this project's own conventions,
not imported) to itself or to a physically-equivalent configuration.

**Kill criterion:** if no single `g` exists that is simultaneously (i)
an isometry of the FULL product `M₄×S³×S⁶` (not merely S³), (ii)
orientation-preserving on the full 13D manifold (a genuine gauge
transformation, not parity), and (iii) consistent with the fermion
representation content found by G73/G74A/G74B and this session's own
zero-mode analysis -- the claim is FALSIFIED, and the "0 vs 1"
question remains a genuine, unresolved physical choice (not dissolved
by gauge redundancy). If such a `g` DOES exist, OB1 collapses from
"which of t=0,1 is selected" to "why the flat Cartan-Schouten gauge
orbit is realized at all" -- a narrower, and per C124's own findings,
now-unsolved-by-topological-action-means question.

## What this round does NOT show

- Does not re-attempt or re-derive C124's own killed CS/transgression
  mechanism, or C123's Yang-Mills claim (status unchanged: `PARTIAL`).
- Does not trust the external `Kimi_Agent` document's own claims about
  Γ₄=±ω₃Γ₆ or the LRSM representation structure without independent
  re-derivation in this project's own conventions -- that document is
  cited only as a source of hypotheses to check, per this project's
  external-agent-findings gate (agent's [VERIFIED] = this session's
  [INFERRED] until re-checked).
- Does not change `N_gen=3`'s CONDITIONAL status, `lambda=
  FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.
- Does not solicit Tom Lawrence's Part 5.

## Verification plan

- Re-derive, in this project's own established Clifford/orientation
  conventions (`docs/clifford_convention_registry.md`,
  `CONVENTION_TABLE.md`), whether any isometry of the FULL product
  `M₄×S³×S⁶` can realize `ω^0↔ω^1` while preserving orientation of the
  full 13-manifold and the twist/fermion data on S⁶.
- Cross-check against C42 (`OPEN_BLOCKERS.md` OB2/OB13 history): "no
  member of the Cartan-Schouten family has a 4-dimensional kernel" and
  the C38/C39 finding that `(1,2)` and `(2,1)` are the two chiral
  halves of one `Spin(4)` spinor, connected by `ι` -- already
  established in this project, reuse not re-derive.
- FL Step 8a skeptic pass on the result before treating it as settled.
