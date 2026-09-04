# Parent Action Gate — pre-registered checklist for OB1/OB2

**Purpose:** before any future attempt at OB1 (parent action search) or OB2
(spectral-triple architecture), this gate freezes what a candidate
construction must supply and states the pass/fail criterion for each field
— per this project's own FL discipline (define the gate before running the
test), and per the user's own recommended next step ("заморозить минимальный
`PARENT_ACTION_GATE`"). **This file supplies no answer** — it is a template
a candidate construction is checked against, matching `claim.md`'s own
kill-criterion discipline applied one level up (to the whole OB1/OB2
research direction, not a single experiment).

A candidate construction PROMOTES past this gate only if every field below
is answered, cited, and internally consistent. A construction that answers
some fields and leaves others as "not yet supplied" is not a failure — it
is accurately `PARTIAL`, and should be logged as such, not rounded up.

## The 7 required fields

### F1 — Background

**Must state:** the exact manifold and metric ansatz. Already frozen by
this project: `S³×S⁶` (dim 3+6=9 internal, +4 spacetime = 13 total,
`RESEARCH_STATUS_REPORT.md`'s own 2026-07-17 correction). A candidate
construction may reuse this unchanged, or explicitly propose a
modification — but if it modifies the background, it must state whether
`N_gen=3`'s own S⁶-only chain (G73/G74A/G74B, independent of this program)
is preserved or affected.

**Pass criterion:** background stated explicitly, with an explicit
yes/no on whether it's the frozen `S³×S⁶` product or a named modification.

### F2 — Twist

**Must state:** which bundle is twisted, and by what. Already frozen:
twisting only on `S⁶` (`D_{S⁶,twisted}`, dim-1 kernel per channel, round59/
dolan-casimir), `S³` left untwisted in the paper's own baseline
(`D_{S³}^{\mathrm{LC}}`).

**UPDATE (C139, 2026-09-04):** round59's kernel=1 result now has its
first genuine wrong-twist `kernel≠1` result. Twisting `D_{S⁶}` by
`m_C` (the tangent/isotropy representation, module type `3+3bar`,
instead of `Sigma`'s `1+1+3+3bar`) gives kernel=0, robust across the
whole admissible connection family (13-angle sweep, not a
single-point accident) — after four prior attempts (C73/C73b) all
failed to discriminate. Round59's specific twist choice (`Sigma`) is
therefore not the unique construction giving a nontrivial invariant
kernel; independent physical justification for `Sigma` is now a
well-posed, testable open question, not previously even askable. Two
independent skeptic passes qualified the strength of this finding: the
kernel-value difference partly reflects a forced representation-theory
shape (any zero-singlet twist bundle would show the same `Term1=0`),
not purely dynamics — the genuinely load-bearing, non-forced content
is `Term2`'s (the twist connection's own contribution) robust
non-vanishing. The decisive follow-up (a matched-singlet-count twist
bundle, e.g. `m⊕2·1`) remains unbuilt. Does NOT change `N_gen=3`'s
CONDITIONAL status. See `CLAIM_LEDGER.yaml`
`C139_ALTERNATE_TWIST_M_KERNEL_ZERO`, `pearl_registry/INDEX.md` row 89
(closed), and
`experiments/20260904-c139-twisted-s6-alternate-representation-negative-control/decision.md`.

**UPDATE (C141, 2026-09-04) — the both-skeptic-recommended matched-
singlet-count follow-up (`m⊕2·1`) is now built, and its finding is
more consequential than either provisional verdict along the way:**
after TWO successive context-blind skeptic passes each overturned the
round's own prior verdict in the same session (`BLOCKED` → `PROMOTE` →
final), the round found that the invariant-sector kernel of EVERY
twisted-`D_S6` construction ever computed in this project (round59,
C139, C141, and a newly-built "`Σ` self-twisted, unrestricted"
comparison) **exactly equals a graded rank-nullity floor computable
from pure `su(3)` branching data alone** — given only the
already-established fact that individual connection channels don't
vanish. Verified 4/4, independently re-derived by hand (orchestrating
session) before registration, not merely accepted from the round's own
script or its skeptic passes. **This means the "kernel of `D_{S⁶}`"
test family, as practiced so far, may not discriminate `Σ`'s specific
geometric content from an alternative at all** — a more fundamental
obstacle to "why `Σ`, not `m`" than any single twist-bundle result,
including C139's own. Does NOT retroactively falsify round59's or
C139's own computed kernel values (both independently re-confirmed
here) — questions the INTERPRETIVE weight placed on them. Falsifiable
escape route named: a twist bundle whose kernel exceeds its own graded
floor. See `CLAIM_LEDGER.yaml`
`C141_KERNEL_IS_GRADED_BRANCHING_FLOOR_NOT_DYNAMICS`,
`pearl_registry/INDEX.md` (2026-09-04 row, impact 9), and
`experiments/20260904-c141-matched-singlet-count-twist-m-plus-2singlets/decision.md`.

**Pass criterion:** states explicitly which factor(s) carry a nontrivial
twist in the candidate construction, and whether this matches or departs
from the frozen baseline.

### F3 — Torsion family [RESOLVED, round113, 2026-07-17]

~~Two DIFFERENT parameterizations already exist in this project and must
not be silently conflated~~ — **resolved: they are the same connection.**
`preprint.tex`/round67-68's `D_{S³}(t)=D_{S³}^{\mathrm{LC}}+(t-\tfrac12)h_H`
(Kostant Dirac-operator shift) and round99/round111's curvature
`R^t(X,Y)Z=t(t-1)[[X,Y],Z]` are both built from the **literal same
connection**, `∇^t_X Y = t[X,Y]` — round113 verified this directly by
reading round99's own script (`e26_toy_Vt_curvature_double_well.py` lines
63-89), which explicitly defines `nabla_t(X,Y,tt)=tt*[X,Y]` and derives its
`R^t` from it — not a coincidental match of two independently-asserted
formulas. Mandatory skeptic review initially found this only one-
directionally verified (round113's own script showed `∇^t⟹R^t`, not that
round99 itself used that `∇^t`); closed by the direct source-read above.
`t=0,1` in both conventions refer to the SAME physical (flat,
left/right-invariant) configuration; `t=1/2` in both is the SAME
Levi-Civita point. See
`experiments/20260717-round113-t-convention-reconciliation/decision.md`
for the full verification chain and the residual bi-invariant-metric-
compatibility caveat (stated explicitly in both original sources, not
independently re-verified here).

**Pass criterion (now satisfied by citation):** any future construction
may cite round113 directly rather than re-deriving this reconciliation.

### F4 — t-selection mechanism (the central question)

**Must state:** the specific action/symmetry/anomaly/topology principle
that selects a specific `t` value (or forces `t=0` and `t=1` together)
rather than leaving it as an arbitrary choice.

**Already tried and found insufficient** (see `OPEN_BLOCKERS.md` OB1,
`CURRENT_STATE_ROUND111.md`): external string-worldsheet analogies (rounds
86-89, formula-matched but mechanism didn't transfer); Pati-Salam gauge/
anomaly forcing (rounds 90-112, fully computed within `G_eff`, no forcing
found in any mixed-`U(1)_Y` channel; cubic non-abelian channels
`[SU(2)_{L,R}]³` still untested); gate G97 closes the standard product-
manifold SU(4) realization entirely (rounds 102/108/109); flux-quantization
torsion-selection (round115, circular for unconditional selection, one
honest near-integer pearl); "spectral flow"/innermost-crossing-pair
structure (round116, equivalent restatement, no new content).
**Round80/E14 (found missing from this registry, added retroactively):**
a genuine, tool-verified geometric `Z2` isometry `iota(g)=g^{-1}` pulls
back the WHOLE Cartan-Schouten family exactly, `iota*(∇^t)=∇^{1-t}` for
all `t` — but gauging it as an orbifold identification `S³/⟨iota⟩` forces
`t=1/2` UNIQUELY (the zero-mode-free Levi-Civita value), killing that
specific route. Three readings tried for whether this forces `t=0,1`
together: two point toward under-counting/collapse, the third
(Left-Right-symmetric model-building analogy) is the only one pointing
the right direction but is an explicit model-building CHOICE in
unreconciled tension with this project's own asymmetric chirality
mechanism (Lemma L5). **This tension (Reading 3 vs Lemma L5) is the one
genuinely open thread from this line — a candidate starting point for a
future F4 attempt, not yet resolved.** See `CLAIM_LEDGER.yaml` `C18`.
**Localized further (C125, 2026-09-01):** Reading 3 is exactly C125's
"Family C" (4D parity composed with the S³-orientation-reversing map),
shown to be the UNIQUE residual freedom surviving every other condition
of a full gauge-equivalence test on the frozen 13D background. C125
proved a stronger, general no-go for the OTHER 7 of 8 possible
compensated combinations (none is a genuine gauge transformation — a
de Rham/torsion-cohomology argument, no product-map or `Isom`-
factorization assumption needed) but left Reading 3/Family C itself
honestly `UNDECIDED` — not resolved, not silently assumed either way —
after a second independent skeptic pass caught the first draft
asserting mutually incompatible answers to the same open question. The
missing link is exactly this tension's own: does the relative M₄↔S⁶
orientation carry physical content, or is it a labelling convention?
See `experiments/20260901-c125-full-gauge-equivalence-gate/decision.md`.

**Also tried and found insufficient (C119, 2026-08-31):** the
Bismut-Ricci-flat condition `Rc(g)=¼H_g²` from the generalized-Ricci-
flow literature -- reproduces round111's `Ric^t` exactly on `S³`
alone, but F1 (applicability to the frozen `S³×S⁶` product) FAILS:
the nearly-Kähler `S⁶` factor is never Bismut-Ricci-flat (`ρ=5`
exactly, radius-independent), and a topological argument (Künneth,
`b₁(S⁶)=b₂(S⁶)=b₃(S⁶)=0`) shows NO harmonic k-form (k≤3) on ANY
product `M×S⁶` can have a leg on the `S⁶` factor -- a reusable
pre-filter for future candidates of this shape. See `OPEN_BLOCKERS.md`
OB1 and `pearl_registry/INDEX.md`.

**Also checked, gate-fill only, no computation (C120, 2026-09-01):** an
externally-proposed candidate `I9 ∝ (2t−1)·Vol(S³)·Vol(S⁶)` does not
clear F6 as literally described -- under this project's own already-
established constraint surface (G51/G54A/G57), it reduces to a linear
function of `t` alone with its only zero at the wrong point (`t=1/2`).
FL Step 8a skeptic reconstructed a likely real referent for the
proposal's own unexplained `\|a\|=2\|b\|` criterion (`a=h_H=3`,
`b=σ(3/2)=3/2`, from the already-assessed E2 Dirac family) pointing to
**round116** ("equivalent restatement, no new content") as the actual
duplicate, not round115. The skeptic pass also surfaced a genuinely
new, unattempted candidate: `η(D^t)` (the eta-invariant / gravitational
Chern-Simons level) at general `t`, structurally odd by C44's own
identity and radius-independent by construction -- not yet computed,
see `pearl_registry/INDEX.md`.

**Also tried and found insufficient (C121, 2026-09-01):** `η(D^t)`,
the candidate C120 surfaced. Closed form `P(a)=a(3-4a^2)/6` found and
confirmed by two independent derivation routes. But the decisive
multi-interval computation (initially thought too costly to attempt)
turns out to be a short, exact correction: `η(a) = P(a) +
2*sum_{n<=J}mu(n)` on the `J`-th interval -- the SAME polynomial on
every interval, shifted only by an even integer. `η mod 2` is
identical everywhere; nothing distinguishes `t in {0,1}` from any
other crossing pair. Same underlying reason as round116: this whole
`(n,sigma)` family has no `n`-dependent structure privileging `n=0`.
One genuinely different, unattempted variant survives: the APS
reduced eta `xi=(eta+h)/2 mod 1` (mod 1, not mod 2 -- a materially
different quantity, since the kernel dimension `h` also jumps at each
crossing). See `null_results/INDEX.md` (C121-EtaInvariant) and
`experiments/20260901-c121-eta-invariant-general-t/decision.md`.

**Also tried and found insufficient (C138, 2026-09-03):** the APS
reduced eta invariant `ξ=(η+h)/2 mod 1` C121 itself left open.
Algebraically NULL, not just numerically observed: `h(t)`'s own
non-constant jump (`mu(n)=(n+1)(n+2)`, `2/6/12/...` across crossings —
the exact mechanism hoped to break the symmetry) is EXACTLY what
cancels `η`'s discontinuous `2*mu(n)` jump under division by 2, leaving
`ξ mod 1 = P(a)/2 mod 1` smoothly everywhere, `t in {0,1}` included
(general `n`-independent proof, independently re-derived this session
from a fresh script, not just C138's own report). The `η`/`gravitational
Chern-Simons` family is now closed in both raw (C121) and reduced
(C138) forms for the same reason: nothing in this construction singles
out `n=0`. See `null_results/INDEX.md` (C138-ReducedEtaInvariant) and
`experiments/20260903-c138-aps-reduced-eta-invariant/decision.md`.

**Also tried and found insufficient (C123, 2026-09-01):** two mechanisms
extracted from an external multi-model panel review. (1) Yang-Mills
curvature functional `S_YM=∫|R^t|²` -- duplicate of `round99`'s own
curvature-norm toy at THIS field (F4, selection): `R^t=t(t-1)·T`, `T`
t-independent, forces every quadratic curvature invariant into the same
`[t(t-1)]²` shape up to a positive constant, and a positive constant
cannot move a critical point. NOT a duplicate at F6 (background
equations) -- round99 had no action framing, `S_YM` does; F6 remains
the open gap regardless. **Byproduct finding, not this claim's own
target:** the reason OB13 gives for expecting such duplication
("any even functional carries no information, selector must be linear")
is itself overstated -- see OB13's note below. (2) Transgression term
`S_mix=k∫CS₃(ω_{S³})∧P₄(M₄)∧ch₃(E_{S⁶})`, coupling S³ torsion to this
project's own already-certified S⁶ twist topology (`c₃(S⁻)=2`, reused
from G73, `ind=+1`) -- survives C119's own topological pre-filter
(`ch₃` is degree-6, the pre-filter only kills degree≤3) and does NOT
collapse into C121's already-rejected `η(D^t)` (checked: the two odd
cubics in `(t-1/2)` have cubic/linear coefficient ratios differing by
a factor of 9, not proportional). **A naive `∫_{M₄}P₄(M₄)=0` kill (for
curvature-based `P₄`) was found OVERBROAD same day by external
review**: `P₄=vol₄` is always closed (top-degree form, no curvature
needed) and survives, reducing `S_mix` to a t-dependent 4D
vacuum-energy term `κ(t)∝CS₃(ω^t)` -- same shape as the bare CS
mechanism, not new content, but NOT fatally killed either. This question was pre-registered (design-freeze against
HARKing) as `C124`, then blindly executed same day by a fresh agent
with no memory of the pre-registering session, then FL Step 8a
skeptic-reviewed same day. **Result: `STRUCTURAL_NO_GO`, confirmed --
the Chern-Simons/transgression family, and a wider
"mismatched-index-contraction" class beyond it (V5), is now CLOSED as an
OB1 F4 mechanism** -- **class-qualified explicitly, per same-day
external review, so a future candidate is not mistakenly treated as
already covered: this closes local, polynomial, first-order, bosonic
13D-Lorentz-covariant invariants (Lovelock-Cartan + the checked V5
class) only.** It does NOT close, and was never asked to close,
C123's own separate Yang-Mills claim -- that was always an
S3-INTERNAL 3D functional using S3's own Hodge star (∫R∧*R), never
proposed as a reduction of a 13D-covariant invariant, and in any case
dimensionally impossible to write as a leg of this classification's
own epsilon-sector (which admits at most one explicit curvature
factor per 3D leg). Yang-Mills's own status is unchanged from C123:
`PARTIAL` (duplicate of round99 at F4; F6 still open) -- not "killed."
Nor does C124 close a parent action using explicit extra covariant
derivatives, non-polynomial functions, additional p-form fields, an
enlarged gauge algebra beyond Lorentz `SO(1,12)`, boundary/defect
terms, or nonlocal/quantum effective actions -- all named explicitly
in `decision.md`'s own theorem-statement header, not left implicit.
Mechanism: a 13D-Lorentz-
covariant 13-form built from `(e,T,R)` splits into two disjoint sectors
by an exact index/degree count -- the sector that can carry `ε` (needed
for `vol₄` or any `S⁶` topological density) is forced exactly
torsion-free (hence even in `t-1/2`, and its full reduced contribution
to the 4D vacuum energy is `A+B·t(1-t)`, stationary only at the
zero-mode-free `t=1/2`); the sector that carries torsion (odd content)
is forced to have odd torsion count, but the available block degrees
`{3,4,5,7,8,9,11,12,13}` are missing degree 6, so its `S⁶` leg is
identically empty. No 13D Lorentz Chern-Simons form exists at all
(Chern-Weil ring generators sit at degree ≡0 mod 4; 14≡2 mod 4,
unreachable). Both mandatory negative controls fail structurally, not
per-candidate. Confirmed independently by skeptic re-derivation (two
prose errors found and repaired, neither load-bearing; L1 shown even
stronger -- adding a 13D gauge field still cannot rescue Sector I,
only Sector III). Scope: Lovelock-Cartan + V5 class, bosonic, strict
product background -- does NOT close a parent action with an
independent 13D gauge field, a non-product/warped background, or
fermion bilinears. See `experiments/20260901-c124-parent-invariant-
classification-preregistration/decision.md` for the full derivation,
both agent passes, and the named Relaxation Map (V1-V5). See also
`experiments/20260901-c123-ym-cs-transgression-panel-review/
decision.md` for the panel review this closes.

**Also tried and scoped, not closed (C127, 2026-09-02, lowest-priority
Relaxation Map item, run at explicit user request over a recommendation
to stop):** bordism/global-anomaly route. The Zero-Signal Gate had to be
split into the two readings `claim.md` itself pre-registers. **SELECTION**
(pick one `t=0` or `t=1`) FAILS structurally: a bordism/characteristic-class
datum of a single fixed background is a lift of a classifying map, not a
connection, hence definitionally connection-blind — this is a diagnosis,
not a discovery. **PAIR-FORCING** (force the pair, or a sign) PASSES the
gate: the mapping torus of C126's own winding-`(-1)` large gauge
transformation carries `int c2 = -1 != 0` [INFERRED — standard instanton-
number/Chern-Simons-difference identity, using C126's already-computed
`n=-1`, not re-derived here]. Blocked downstream, not excluded, on two
named ingredients: **(1)** this project has never reconciled two live,
mutually incompatible descriptions of what `nabla^t` even is — C125's
metric affine connection (torsion a tensor, `t=0,1` related only by an
orientation-reversing isometry, never a gauge transformation) versus
C126's Yang-Mills connection (`t=0,1` one point of the full gauge orbit
`A/G`, related by a large gauge transformation) — each round named its
own half, neither reconciled the pair, confirmed genuinely unrecorded by
grep over this file and `CLAIM_LEDGER.yaml` this session (new Relaxation
Map item X2, prerequisite for X1 and the new X6); **(2)** round95's
already-known missing S6-S3 link. `Omega^Spin_13(pt)=0` independently
verified, plus the two further degrees the Anderson-dual sequence
actually needs (`Omega_14=Omega_15=0`, never stated by the external
source this round started from) [VERIFIED-tool, secondary source —
arXiv:2108.13542 Table 1 citing ABP67/Gia71 — cross-checked structurally
against the rational free rank `p(k)` at degree `4k`]. Own FL Step 8a
skeptic pass: `WEAKENED`, all 12 findings accepted and repaired in place;
the first draft's own blanket "should not be retried" and its universal
no-go are explicitly withdrawn — what survives is narrower and, in one
respect, more useful than the first draft claimed. See
`experiments/20260901-c127-bordism-global-anomaly-scoping/decision.md`.

**C127's ingredient 1 (X2) CLOSED (C128, 2026-09-02, TWO independent FL Step
8a skeptic passes, differently worded per the Paraphrase-Sensitivity Probe,
both `WEAKENED`, concordant):** no smooth map of `S³` at all — diffeomorphism
or not — has frame-transition function equal to C126's `g=Ad` (Maurer-Cartan
integrability: `dΦ+Φ∧Φ=0` for the candidate family reduces to `λ(1+λ)=0`,
vanishing only at `λ=0,-1`; `λ=-1` is C125's `ι`, `λ=+1` is `g`, which does
not integrate). **C125 and C126 are NOT in contradiction — they answer
questions about two different configuration spaces.** Fixing the vielbein
(this project's own frozen ansatz) is a *complete* gauge-fixing of C126's
gauge group `𝒢` (it acts freely on orthonormal frames), so the ansatz's own
configuration space is `𝒜` itself, not `𝒜/𝒢` — C126 quotiented by a group
the ansatz had already fixed. **Genuinely new, and the round's strongest
content**: C125's result is strengthened from "no ISOMETRY relates `t=0,1`
without reversing orientation" to "no DIFFEOMORPHISM whatsoever does" — any
`f` with `f_*∇⁰=∇¹` is automatically an isometry with `det=-1`, proven
algebraically (`c^Tc=-det(c)·I` forces `μ=1`, sign `-`) and confirmed by an
exact symbolic (Groebner-basis) computation, a second independent
implementation. **The first draft's own "genuinely different transformation
groups" framing was withdrawn by the skeptic passes**: `M_ι=(-I)·Ad`, and
`-I` is central and cancels in `u⁻¹du`, so under an `O(3)` (not C126's
stated `SO(3)`) structure group the two readings coincide exactly — the
real, trivialisation-invariant obstruction is `det` (C125's already-
certified parity `ℤ₂`), not winding number, which is NOT invariant under
change of frame for orientation-reversing maps. **Consequence for X6**: the
mapping torus of `g` joins gauge-equivalent configurations by construction
(vacuous); the mapping torus of the map that actually relates `∇⁰,∇¹` (an
orientation-reversing isometry) is non-orientable, so `Ω^Spin` is the wrong
functor — X6 is re-specified as new item **Y1**: does this non-orientable
mapping torus admit a `Pin^±` structure at all (`w₂=0` or `w₂+w₁²=0`,
`[UNKNOWN]`, checked before any bordism-group lookup) — still gated on
round95 (ingredient 2) for which `Pin` type the fermion content needs. See
`experiments/20260902-c128-nabla-t-gauge-group-reconciliation/decision.md`.

**Y1's structure-existence half CLOSED (C129, 2026-09-02, two independent
FL Step 8a skeptic passes, differently worded, both split
`CONFIRMED-REAL` on the math / `WEAKENED` on the evidence apparatus,
concordant):** the mapping torus of `ι` (and of every candidate relating
map — the answer is provably independent of which one) admits BOTH a
`Pin⁺` and a `Pin⁻` structure, exactly two of each. Reason: `H²(M;𝔽₂)=0`
for the mapping torus of ANY self-map of `S³` (the fibre is 2-connected),
confirmed by 5 independent routes including one (`π₁` + Euler
characteristic + Poincaré duality) using no chain complex at all — so
`w₂` and `w₁²` both vanish for dimension reasons, and BOTH Pin conditions
hold simultaneously, not by cancellation. A separate constructive route
(explicit Clifford-algebra lift, `S³×ℝ` parallelizable) builds both
structures directly, using none of the same machinery — the conclusion
survives withdrawal of any single citation. **Correction to this
project's own record**: `Pin⁺⟺w₂=0`, `Pin⁻⟺w₂+w₁²=0` (Kirby-Taylor,
consulted directly), the OPPOSITE of what C128 §6c stated — C128
self-contradicted (its own Completeness section had it right); harmless
for C128's own verdict (nothing there depended on which label was which)
but load-bearing downstream since `Ω^{Pin+}_4=ℤ/16` vs `Ω^{Pin-}_4=0` are
very different. **Consequence**: via the BARE tangential structure alone
the manifold imposes NO constraint — both types are always available, so
this route cannot discriminate anything by itself. The real gate is now
narrower: whether the TWISTED structure (`Pin^±×_{ℤ₂}G`) the fermion
content actually needs exists is a different, unevaluated question (new
item **Z1**, named as cheaper than round95 and the recommended next
step), and round95 (ingredient 2) is still needed to know which `Pin`
type is physically required. See
`experiments/20260902-c129-pin-structure-existence-mapping-torus/decision.md`.

**Z1's twisted-structure existence ANSWERED, and a higher-priority scope
problem surfaced (C130, 2026-09-02, two independent skeptic passes,
concordant `WEAKENED`, 22/23 findings repaired):** as a theorem about
`M_ι`, the twisted structure `Pin^±×_{ℤ₂}G` exists uniformly — for EVERY
Lie group `G` with a central order-2 element and every `Ḡ`-bundle, both
`Pin⁺` and `Pin⁻` twisted structures exist (proved by genuine transfer
via a `K(ℤ₂,2)`-fibration obstruction argument, not by assuming C129's
untwisted vanishing simply carries over — the round explicitly checked
the transfer is non-vacuous by exhibiting cases on other manifolds where
twisting flips the answer both ways). So this route also cannot
discriminate `t=0` from `t=1` — the last cheap candidate before round95
is now closed too. Self-caught: the group `G` this project's own frozen
content would supply (the frame bundle's group) turns out to be a type
error, not a valid twisting group (it IS the tangential structure, not
independent of it — already diagnosed once by C127 and never
propagated); `SU(3)` from the `S⁶` twist bundle is excluded too
(`Z(SU(3))=ℤ₃` has no order-2 element). **⚠️ NEW TOP-PRIORITY ITEM,
AHEAD OF ROUND95 (`W1`, cheaper to resolve):** the object all of C128
§6b, C129, and C130 have been analyzing (`M_ι`, a 4-manifold) does not
appear ANYWHERE in C127's own already-verified dimension audit (13D
topological terms need `Ω₁₃,Ω₁₄`; the 13D parent's anomaly needs
`Ω₁₄,Ω₁₅`; the 4D effective theory's anomaly needs `Ω₅,Ω₆` — `Ω₄` never
appears). `Ω₄` is the home of a 3-dimensional theory's own anomaly, and
this project has no 3D theory — so the relevance of the manifold three
consecutive rounds analyzed is not merely untested, it is **adversely
indicated by this project's own verified table**. Either a reading
exists in which a 4-manifold is the right Dai-Freed object (and the
three rounds stand), or it does not (and they answer a well-posed
question about the wrong manifold). See
`experiments/20260902-c130-twisted-pin-structure-existence/decision.md`.

**⚠️ W1 TESTED AND CORRECTED (C131, 2026-09-02; three drafts, four
context-blind skeptic passes total, two direction-reversals, synthesized
here rather than taken from any single draft — the round's own final
draft was itself internally inconsistent and its 4th, dedicated review
found real, specific overclaims in it).** C130's two stated PREMISES
above are both false as written: C127 §4's list is non-exhaustive (it
omits the 4D-topological-terms row, which needs `Ω₄` and `Ω₅` by the same
Anderson-dual sequence) — so `Ω₄` is not homeless; and "this project has
no 3D theory" cannot be established by a string-grep for "3D theory" when
the project's actual object is called `CS₃` (C123's
`∫_{S³}CS₃(ω^t)`) — though the premise turns out to be true in substance,
since that object is a NUMBER (a coefficient of a 4D term), not a
partition function of an actual 3D QFT. **The real, correct reason `M_ι`
is not the object C127 §5d needed is ORIENTABILITY, not dimension**:
`H₄(M_ι;ℤ)=0` (independently re-derived twice, once via C129's computed
table and once from scratch via the Wang sequence) — `M_ι` is closed and
non-orientable, carries no integral fundamental class, so `∫c₂` (the very
number C127 §5d computed) is literally undefined on it. Every reading
that legitimately makes a 4-manifold anomaly-relevant here (Chern-Simons
level quantization, a `Q/Z` coefficient on a coboundary, APS spectral
flow) needs an ORIENTABLE 4-manifold and produces C127 §5d's `S³×S¹`
(where `∫c₂=−1` is defined) — not `M_ι`. **But this does NOT mean `M_ι`
is homeless in every sense** — C128 §6c itself already named the correct
reformulation: a `Pin^±` class on a non-orientable 4-manifold is
"textbook Dai-Freed practice," and that is exactly what C129/C130
established `M_ι` supports (both untwisted `Pin⁺`/`Pin⁻` exist). **New
result, computed by the 4th review pass, not by C128-C130**: the
UNTWISTED Pin route on `M_ι` is trivial — `[M_ι]=0` in `Ω^{Pin+}_4` for
both Pin structures (explicit null-bordism, `M_ι=∂W` with
`W=D⁴×_ι S¹`) — so it, too, cannot force or select anything by itself.
**The one surviving live question across every route this project has
tried is the TWISTED Pin structure** on `M_ι` (C130's Z1/Z2, the
swap-monodromy fermion bundle), which needs the twisting group `G` —
itself blocked on round95. Net: C128's, C129's, and C130's mathematics is
all correct and untouched; every route this program has attempted now
converges, independently, on round95 as the sole remaining blocker — the
4th such convergence (C127's ingredient 2, C129's Z2, C130's `G`-naming
failure, and now this). See
`experiments/20260902-c131-mapping-torus-dimension-consistency/decision.md`
(read critically — its own final draft over- and under-claimed in turn
across three revisions; this entry is this session's own synthesis, not
a transcription of any one draft).

**DIVERGENT-mode survey run (C132, 2026-09-02; user-directed exploration
after H1c/round95 was recognized as needing a full 13D parent action —
not a convergent falsification round, no candidate below is claimed
correct):** 18 candidate parent-action mechanisms generated (outside the
class C124 already closed — independent 13D gauge field, non-product
background, spectral action, fermion bilinears, etc.), 15 survived a
Novelty-Check + Zero-Signal-Gate screen (Novelty Check itself `PARTIAL`
— the project's ~90-item goal-expansion brainstorm list could not be
read; disclosed, not hidden). One context-blind skeptic pass ran and
`[FALSIFIED]` the first draft's ranking reasoning, catching a real
inversion (the top candidate's first-draft argument had `G₂`-equivariance
backwards — it constrains NOTHING about the channel label, since `G₂`
acts trivially on it; only the triality `ℤ₃` forces genuine
channel symmetry, and even that borrows the same un-derived
fiber-`Spin(8)`/triality credit line `N_gen=3` already rests on, G102)
and a stale citation (a "not tested, out of scope" prior-art quote that
its own source file marks superseded 100 lines later by a registered
`E8` gate with an adverse preliminary — `t=½` always stationary for the
bosonic curvature-plus-torsion class; `t=0,1` only if the torsion term
is dropped by hand). **Top-ranked, by this project's own Cheapest-
Differentiating-Test protocol, after correction:** (1) the "symmetry
ladder" itself — a cheap, ~1-round meta-result stating exactly which
symmetry assumption buys which reduction of the pairing-rule space
(`G₂`: none; `Spin(8)`: block-diagonal only; triality `ℤ₃`: full channel
symmetry) — ready-to-run as sketch `C133`; (2)/(2) tied — Einstein-Cartan
torsion-as-auxiliary (torsion solved for algebraically from the fermion
spin current rather than postulated, so its sign would be fixed by L5's
already-certified `S⁶` chirality; must open against round72's own
registered `E8` gate, not its superseded row) — ready-to-run as sketch
`C134` — and a joint 13D generalized-Killing-spinor constraint (found by
the skeptic pass, not the survey); (4) a diagonal `ℤ₃` orbifold of `S³`
breaking the `t↔1−t` parity OB13 asks about. See
`experiments/20260902-c132-13d-parent-action-survey/decision.md` for the
full ranked list (15 candidates), the two ready-to-run sketches, and 4
proposed pearls.

**C132's `P0` candidate tested to completion (C133, 2026-09-02, two
independent skeptic passes, both `WEAKENED`, agreeing):** the symmetry
ladder is confirmed on the channel matrix — `9` (free) under `G₂` alone,
`3` (block-diagonal) under `Spin(8)`, `1` (fully symmetric) under
`Spin(8)`+triality `ℤ₃` — with the general law `dim = number of orbits
of the assumed symmetry on {v,s,c}` verified across all six subgroups of
`S₃`, not just the three originally asked. Honestly scoped: only the
middle rung (`Spin(8)` block-diagonality, via inequivalence of `8_v,
8_s, 8_c`) is genuinely falsifiable as tested — the `G₂` and `ℤ₃` rungs
are entailed by the construction and could not have come out otherwise,
stated explicitly rather than claimed as independent confirmations.
**New scope caveat:** `Spin(8)` forbids channel MIXING only for
one-in-one-out (endomorphism) couplings — a nonzero `Spin(8)`-invariant
TRILINEAR form (octonion multiplication itself) genuinely mixes all
three channels, so "no channel mixing" must always carry this
qualifier. **Corrected cost accounting (self-corrected twice — first
under-corrected, then over-corrected, before settling):** rung 2
(`Spin(8)`) is NOT free, contrary to C132's original pricing — it is a
postulate the S⁶=G₂/SU(3) geometry does not supply. That postulate, and
the earlier round119/round124 channel-distinguishing routes, **draw on
the same un-derived ingredient** (a fibre structure beyond geometric
`G₂`, which G102 already flags as needed) — used in OPPOSITE
directions: this ladder keeps it unbroken to force channel-uniformity,
round119/124 break it to distinguish channels. **Directly relevant to
the Blind-Prediction-Test pearl (2026-09-02, on `N_gen=3` itself):**
this confirms part of that concern is concrete, not just philosophical
— the SAME un-derived credit line underwrites both this ladder's rung
2-3 pricing and (via G102) the project's own headline generation count.
Cheap, concrete next step named: check whether the same explicit `ℤ₃`
(built this round from octonions/`J₃(O)`) cyclically permutes
round119's own `(Γ_A,Γ_B)` sign patterns — closes `pearl_registry` row
40's long-standing open `next_check`. See
`experiments/20260902-c133-symmetry-ladder-pairing-space/decision.md`.

**C132's `P2` candidate tested to completion — REJECT (C134, 2026-09-02,
two independent skeptic passes, both `WEAKENED`, agreeing):**
Einstein-Cartan (ECSK) torsion, sourced algebraically by this project's
own already-certified `S⁶`-twisted zero-mode chirality, forces `T=0`
(i.e. `t=1/2`) in vacuum — killed on three independent routes, the
strongest being an EXACT operator identity (not a sample): the `S³`-leg
source bilinear `Ω₃=γ₅⊗1⊗Γ₇` is a 4D-chirality-FLIPPING operator
(`P_L Γ⁰Ω₃P_L=0` identically, verified representation-independent
across 40 basis changes), so it vanishes exactly on the chirality-
definite content `N_gen=3` requires — the chirality hoped to fix
torsion's sign is precisely what kills the source. Stronger than mere
non-selection: ECSK is incompatible with the whole `∇^t` torsion
ansatz for every `t≠1/2`, and the one point it permits (`t=1/2`) has no
zero modes at all (KT-8) — self-consistent but phenomenologically
empty. Both mandatory controls passed (positive: exactly reproduces
Perez-Rovelli's four-fermion coefficient and Popławski's Cartan
relation, both primaries retrieved and read this session; negative:
vector-like content correctly kills the sign preference). Also found:
ECSK's bosonic sector reduces exactly to round72's already-tested `E8`
functional at `a=0` — same answer, same reason, not a genuinely new
question. **F6 progress, honestly scoped**: this is the project's
FIRST genuinely derived torsion equation of motion (a real advance over
C123/C126's bare-stationarity results) — but the companion metric EOM
was not derived and the frozen background actively VIOLATES it (Ricci
`0⊕2g₃/ρ₃²⊕5g₆/ρ₆² ≠ 0` required to be zero in vacuum), so F6 is logged
`PARTIAL`, not `PASS`, per this file's own no-rounding-up rule. See
`experiments/20260902-c134-ecsk-torsion-auxiliary/decision.md`.

**C132's `P14` candidate tested to completion — REJECT, tier
`[RESTATEMENT]` (C136, 2026-09-02, two independent skeptic passes, both
`[FALSIFIED]`, agreeing):** a joint generalized-Killing-spinor
constraint on `M₄×S³×S⁶`, posed geometrically (no 13D supergravity
needed — Nahm's theorem doesn't apply to an ordinary, non-SUSY
constraint), genuinely couples the two compact factors through a
first-order odd term. But the three `S⁶` triality channels give
IDENTICAL solution tables — not because of any new obstruction this
round found, but because E-L3B's own Corollary already makes the three
twisted Dirac operators literally the same operator, and L5/G74B
already fixes one shared chirality across all three. **Self-caught by
the round's own trap-detector, applied to its own conclusion**: by
round114's actual stated criterion (one-line derivability from a cited
source), the headline is a restatement, not new evidence — four prior
results (`null_results` G44-B1, GAP-4, Round81; `pearl_registry` rows
22, 36) already established this. Genuine new content: VERIFIED (not
just asserted) that C134's chirality-flip kill mechanism does NOT
transfer here — the vanishing there came specifically from the
Dirac-adjoint `Γ⁰` insertion, absent in a linear-in-spinor constraint.
Also named two real counterexamples any future cross-factor no-go on
this split must address: an off-block symmetric `A` (breaks the whole
factorization), and channel-dependent `S⁶` data entering through a
shared scalar (produces a 3-way pairing with no `Z₂` bottleneck). See
`experiments/20260902-c136-joint-killing-spinor-constraint/decision.md`.

**Status of C132's top-tier candidates, all three now resolved:** `P0`
(→C133) confirmed with real scope narrowing; `P2` (→C134) killed
cleanly with a genuine mechanism; `P14` (→C136) killed as a restatement
of prior art. No candidate from today's 13D-parent-action survey
supplies a working `t`-selection mechanism.

**C132's `P3` candidate tested to completion — REJECT (C137,
2026-09-02, one context-blind skeptic pass, `WEAKENED`, verdict
direction confirmed):** fermion-condensate-sourced torsion (`P3` —
explicitly what C134 itself "redirects into" after killing `P2`),
tested against pearl_registry row 32's original bar (a genuine
dynamical derivation, not an assertion) plus C134's own three-part
addendum (4D-pseudoscalar structure, chirality reconciliation, the
fine-tuning explanation). **Add to C132 §1c's "already tried" table:**
*fermion-condensate-sourced torsion (`P3`) — the standard
gaugino-condensation derivation cannot run here (no SUSY, no gauge
multiplet, no confining sector; `G97`); the source bilinear vanishes
identically on the certified zero-mode sector (conditional on L4B rank
= 1) via the SAME `P_LΓ⁰Ω₃P_L=0` mechanism as `P2`/C134, independently
reconfirmed here with a different Clifford construction; the required
magnitude has no independent source; the four retrieved nearly-Kähler-
coset papers (Manousselis-Prezas-Zoupanos hep-th/0511122,
Gemmer-Lechtenfeld arXiv:1308.1955, Cardoso-Curio-Dall'Agata-Lüst
hep-th/0310021, Frey-Lippert hep-th/0507202) parameterise the
condensate rather than deriving it (C137)*. The Majorana escape is
closed two ways (`Cl(1,12)` central-parity argument, `13 mod 8 = 5`
regime; the in-repo C33 zero-mode closure). **F6 unchanged at
`PARTIAL`** — this round derives no new EOM, only evaluates C134's
torsion EOM on candidate content; the metric-EOM gap C134 named is
untouched. See
`experiments/20260902-c137-fermion-condensate-torsion/decision.md`.

**Status of C132's full candidate queue: `P0`, `P2`, `P14`, `P3` all
now resolved, none supplies a working `t`-selection mechanism.**
Lower-priority, untested candidates remain (`P1`, `P4`–`P13`), all
below `P3`'s already-low CDT rank.

**Pass criterion:** names a mechanism NOT already in the above list, or
explicitly names which item above it is extending and states the new
structural argument that distinguishes it from the already-failed version
(per `feedback-mechanism-transfer-gate-2026-07-17`'s 6-field gate).

### F5 — Fermionic Dirac operator

**Must state:** the exact operator, `D_full` or its replacement, and its
relationship to the background/twist/torsion choices above. Already
frozen (baseline): `D_full² = D_{S³,t}²⊗1 + 1⊗D_{S⁶,S⁻}²` (E2/E12), with
KT-8's own finding that this has NO zero mode at the Levi-Civita point
(`t=1/2` in the `h_H` convention).

**Pass criterion:** operator stated explicitly (not just "a modified
operator"), and its zero-mode structure computed, not assumed.

### F6 — Background equations

**Must state:** what equations of motion (if any) the candidate
background/torsion configuration is required to satisfy. **Currently: none
have been derived for this program** — round111 computed a bare curvature
scalar `Scal(∇^t)`, explicitly NOT the same as a derived action's
Euler-Lagrange equation (its own honest scope note). This is the single
largest gap in the whole OB1 program.

**One F6 candidate fully assessed (C126, 2026-09-01→02):** `S_YM=
∫_{S³}|R^∇|²` (C123's Claim 1) — its full second variation (not just the
1D `t`-slice) IS positive semi-definite at `t=0,1`, but this is a
theorem (any non-negative functional is stable at its own zeros), not a
finding, so it clears F6's own "an action principle is named and its
EOM derived" bar only in the narrow, uninformative sense that the EOM
solution set at `t∈{0,1}` carries zero selection content. Genuinely
new: the homogeneous vacuum set is `{0}⊔SO(3)` (more degenerate than
the family reveals), and `t=0,1` are ONE point of the full gauge orbit
`𝒜/𝒢` but distinct points of `𝒜/𝒢₀`, making the `t=1/2` barrier
topologically forced (winding number `n=-1`) rather than an artifact
of the family path. See `experiments/20260901-c126-yang-mills-full-
fluctuation-stability/decision.md`. F6 for any OTHER candidate action
remains fully open.

**Second F6 candidate assessed (C134, 2026-09-02):** Einstein-Cartan
(ECSK), with torsion sourced algebraically by the `S⁶`-twisted zero
modes. **This is the first candidate to clear F6's bar in the genuine
sense** — an actual, non-trivial torsion equation of motion is derived
(`T^{ABC}=(κ₁₃/2)·i⟨ψ̄Γ^{ABC}ψ⟩`), literature-cross-checked against two
primaries (Perez-Rovelli, Popławski) and independently confirmed
against round111's own `Scal(t)=24t(1-t)` computed by a different route
two months earlier. It gives a real, checkable answer: `T=0`, `t=1/2`
(REJECT, see F4 and `null_results/INDEX.md`). **Still logged `PARTIAL`,
not `PASS`**, because ECSK's OTHER field equation (the metric/Einstein
equation) was not derived and is actively violated by the frozen
background in vacuum (`Ric≠0` where the torsion-free EOM requires
`Ric=0`) — a construction answering the torsion sector while leaving
the metric sector unaddressed is accurately `PARTIAL` per this file's
own rule, not rounded up because the answered half was informative. F6
for any candidate deriving BOTH the torsion and metric EOMs
self-consistently remains fully open.

**Pass criterion:** an actual action principle is named (Einstein-Cartan,
Chamseddine-Connes-Marcolli spectral action, or another explicitly cited
framework) and its equations of motion are derived or cited, not merely
gestured at.

### F7 — Stability

**Must state:** whether the selected configuration(s) are stable under
small perturbations of the torsion parameter, the background metric, or
the gauge content. **Currently: not checked at all** for any candidate in
this program.

**Pass criterion:** an explicit perturbative check (e.g. second-variation
sign, spectral gap under a symbolic small parameter) is performed, not
assumed from the existence of a critical point alone.

## For OB2 specifically (spectral-triple architecture) — 6 additional fields

If the candidate construction is a non-product/twisted spectral triple
(Connes-style `(A,H,D)`, round103's still-open fork), it must ALSO supply:

| Field | Status in round110's toy attempt |
|---|---|
| Algebra `A` | Not stated beyond the finite matrix model |
| Hilbert space `H` | `H_block=ℂ²⊕ℂ²`, a toy, not the intended continuum space |
| Dirac operator `D` | `D_block=diag(0,0,3c/2,3c/2)`, self-adjoint, trivially bounded (finite matrix) |
| Grading `γ` | Not checked |
| Real structure `J` | Not checked |
| Physical interpretation | Not stated — what does each block physically represent? |

**Pass criterion for OB2:** all 6 fields stated and the standard NCG axiom
checklist (first-order condition, orientability, Poincaré duality,
KO-dimension) checked — round110 only partially addressed 2 of these
(construction + swap-symmetry), explicitly flagged as such.

## How to use this gate

1. Before starting a new OB1 or OB2 round, fill this checklist's fields for
   the SPECIFIC construction being proposed — as a section in that round's
   own `claim.md`, referencing this file, not copying it.
2. Any field left `NOT SUPPLIED` must be stated as such explicitly in the
   round's own verdict — do not round a `PARTIAL` construction up to
   `PROMOTE`.
3. F3's convention-reconciliation check is flagged as the single highest-
   priority item to resolve FIRST, independent of which of OB1/OB2 is
   pursued — both directions currently risk silently mixing two different
   `t`-parameterizations without knowing it.

## What this gate does NOT do

1. Does NOT propose a parent action itself — purely a checklist.
2. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.
3. Does NOT supersede `claim.md`'s own per-experiment template — this is a
   program-level gate, one level above a single experiment's kill
   criterion.
