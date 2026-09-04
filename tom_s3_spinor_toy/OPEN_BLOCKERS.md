# Open Blockers Registry

**Purpose:** genuinely open items, each with what would resolve it. Phase 0
(Freeze) deliverable per MASTER_TZ_RDR22 Section 21. Companion to
`CLAIM_LEDGER.yaml` (status per claim) and `SUPERSEDED_RESULTS.md` (what
changed). Ordered roughly by how directly each blocks the `N_gen=3` headline.

---

## OB1 — KT-8: no zero mode for the full S3xS6 Dirac operator [PARKED 2026-07-17]

```
STATUS: PARKED — REOPEN ONLY ON NEW EXTERNAL INPUT
```

**Why parked, not closed:** after rounds 114-117 (4 independent mechanism
attempts, all honestly null/falsified — see below) plus the earlier
round62-113 arc, the search has reached the point of diminishing returns.
Continuing to sweep more internally-generated candidates
(non-geometric flux, doubled/exceptional field theory, cobordism
invariants, `F₄`, `Spin(10)`, etc.) without a new external constraint is
not a good use of further effort right now. Not falsified — the parent
action may well exist — just not found by anything triable from inside
this project's current toolkit.

**Reopen condition (any one of):**
1. A concrete candidate action is found (external literature or new
   internal insight).
2. A directly relevant parent mechanism is published somewhere new.
3. A new derivation map linking geometry → Dirac operator → torsion
   emerges from OTHER work in this project (e.g. the gauge/Hilbert/
   triality closure program below).
4. Any candidate MUST pass `PARENT_ACTION_GATE.md`'s checklist before
   being attempted, not just be "interesting."

**What's open (original framing, preserved):** the untwisted (Levi-Civita) S³ connection gives the full
internal Dirac operator on `S³×S⁶` zero zero-modes. A torsion-deformed S³
connection (`t≠0`) is a mathematically available escape route, but **no
selection principle** is known for *which* `t` (or whether both `t=0,1`
together) is physically required.

**What would resolve it:** a "parent action" — some action/symmetry/anomaly/
topology principle that forces a specific `t` (or forces `t=0` and `t=1`
together) rather than leaving it as an arbitrary choice. This is the target of
the entire round62-111 search (see `CURRENT_STATE_ROUND111.md`).

**Current best lead:** round111's `Scal(t)=Scal_LC-6(2t-1)²` decomposition
sharpens the question to: what is the actual sign/magnitude of the
torsion-squared coefficient in a real gravitational or spectral action (not
yet derived from first principles)?

**Owner / next step:** open; `/boyko-goal-expansion-100`'s remaining ~90
untried candidates (non-geometric flux, generalized/doubled/exceptional field
theory, discrete torsion, cobordism invariants — see the skill's own
2026-07-17 report) are the next place to look if the Pati-Salam route (OB2)
doesn't reopen. **Any future attempt: check against
`PARENT_ACTION_GATE.md` first** — its F3 field (the `t`-convention
question) is now RESOLVED (round113): `preprint.tex`'s `D_{S³}(t)`
Dirac-shift and round99/111's Cartan-Schouten `∇^t` are the same
connection, cite directly rather than re-deriving.

**Attempted, FALSIFIED exactly (C107, 2026-08-29):** following
`/boyko-project-radar` + `/tracy`'s converged recommendation to point the
C90-C106 Peter-Weyl multiplication-operator apparatus at OB1, this round
first checked the necessary prerequisite: is C85/Meier's certified
`D-bar_k` (the operator C90-C106 is built from) the SAME object as
round67/Agricola's already-certified `D^t(n,sigma)` torsion family, under
the natural `n=k` identification? Answer: no, exactly and provably — see
`experiments/20260829-c107-meier-vs-kostant-bridge-attempt/decision.md`.

**Attempted, FAILED on PARENT_ACTION_GATE field F1 (C119, 2026-08-31):** a
read-only literature search surfaced a genuinely new candidate not on the
already-tried list below — the **Bismut-Ricci-flat condition**
`Rc(g)=¼H_g²` from the generalized-Ricci-flow literature (Gutiérrez
arXiv:2401.03332; Lauret-Will arXiv:2301.02335; Fusi-Lafuente-Stanfield
arXiv:2608.25619, published 2026-08-26, proving dynamical stability for
exactly this class on compact simply-connected semisimple Lie groups —
`S³=SU(2)` qualifies). Applied to `S³` alone, the condition reproduces
round111's `Ric^t=8t(1-t)δ` exactly and gives roots `t∈{0,1}` — but F1
(geometric applicability to the FROZEN `S³×S⁶` background, not `S³` in
isolation) **FAILS, three ways:** the frozen nearly-Kähler `S⁶` factor is
never itself Bismut-Ricci-flat (`ρ_{S⁶}=5` exactly, radius-independent —
a property of the whole nearly-Kähler class, not this specific `S⁶`);
its characteristic torsion is co-closed but not closed (`dT≠0`, forced
by `S⁶`'s own nearly-Kähler structure equations, not a choice); and —
the round's main free finding — a topological (Künneth) argument shows
`H³(S³×S⁶;ℝ)=ℝ` generated only by `vol_{S³}`, forcing any admissible
harmonic `H` to vanish on `S⁶` entirely, hence `Ric(g_{S⁶})=0` —
contradicted by the frozen `S⁶`'s `Ric>0` for ANY `t`, torsion, or
radius. Scope, added after FL Step 8a skeptic review: this topological
kill holds for the compact 9-dim internal factor with a strict product
metric and exact (no-dilaton) closure — verified by the skeptic to
extend to the full 13d background and to survive a non-constant dilaton
too, so the scope qualifiers narrow the *documentation*, not the
*result*. **The `S³`-only root is not new content at the equation
level** (identical to round111/round99's already-certified `Ric^t`,
`R^t`) — whether it is new content at the F4 justification level remains
unassessed. Full record, including the FL Step 8a skeptic pass and nine
corrections applied in place:
`experiments/20260831-c119-bismut-ricci-flat-f1-test/decision.md`.
**Reusable pre-filter this round adds to the "already tried" list below:**
any future candidate parent action stated as a harmonic-form condition
with a nonzero leg on the `S⁶` factor is dead-on-arrival for `S³×S⁶` (or
any `M×S⁶`), because `b₁(S⁶)=b₂(S⁶)=b₃(S⁶)=0` — check this first, one
line, before building anything.

**Checked, gate-fill only, no computation (C120, 2026-09-01):** an
externally-proposed candidate `I9 ∝ (2t−1)·Vol(S³)·Vol(S⁶)` (from a
sibling research project's own summary, unverified beyond the chat
description) does not clear F6 as literally stated — under this
project's own already-established constraint surface (G51/G54A/G57
SM-coupling ratio), it reduces to a linear function of `t` alone with
its only zero at the wrong point (`t=1/2`, KT-8's already-known
zero-mode-free point). FL Step 8a skeptic reconstructed a likely real
referent for the proposal's unexplained `\|a\|=2\|b\|` criterion
(`a=h_H=3`, `b=σ(3/2)=3/2`, from the already-assessed E2 Dirac family
`σ(n+3/2)+(t-1/2)h_H`), redirecting the actual duplicate match from
round115 to **round116** ("equivalent restatement, no new content").
**The round's genuinely useful output:** skeptic surfaced an
unattempted candidate, `η(D^t)` (eta-invariant / gravitational
Chern-Simons level) at general `t` — structurally odd by C44's own
spectral identity, radius-independent by construction, immune to
round115's volume-circularity failure mode. Not computed this round.
See `experiments/20260831-c120-i9-selector-gate-check/decision.md` and
`pearl_registry/INDEX.md`.

**Attempted, REJECTED (C121, 2026-09-01):** `η(D^t)`, the candidate
C120 surfaced. Closed form found (`P(a)=a(3-4a^2)/6`, `a=3(t-1/2)`),
independently confirmed via two separate derivation routes (Hurwitz
zeta; heat-kernel Mellin transform, matching pole residues and the
`dP/da=-2(a^2-1/4)` APS variation-formula identity). The round's own
first draft declared the decisive multi-interval comparison "not yet
evaluable" — FL Step 8a skeptic completed it in ~15 lines (independently
re-derived by this session before trusting it): `η(a) = P(a) +
2*sum_{n<=J}mu(n)` on each successive interval, the SAME polynomial
shifted only by an even integer. `η mod 2` is therefore identical on
every interval — nothing distinguishes `t in {0,1}` from any other
crossing pair, the same underlying reason round116 already found for
the `(n,sigma)` crossing family itself. One genuinely different,
unattempted variant survives: the APS **reduced** eta `xi=(eta+h)/2
mod 1` (mod 1, not mod 2 — materially different since the kernel
dimension `h` also jumps at each crossing). See `null_results/INDEX.md`
(C121-EtaInvariant) and
`experiments/20260901-c121-eta-invariant-general-t/decision.md`.

**Attempted, PARTIAL — neither mechanism promotes (C123, 2026-09-01):**
two candidates extracted from an external multi-model panel review (7
independent LLM responses to a homework framing of OB1). (1) Yang-Mills
`S_YM=∫|R^t|²` — duplicate of `round99`'s own curvature-norm toy at F4
(selection): `R^t=t(t-1)·T`, `T` t-independent, so every quadratic
curvature invariant is `[t(t-1)]²` up to a positive constant, which
cannot move a critical point. NOT a duplicate at F6 — round99 had no
action framing. (2) Transgression `S_mix=k∫CS₃(ω_{S³})∧P₄(M₄)∧
ch₃(E_{S⁶})`, reusing this project's own certified S⁶ twist topology
(`c₃(S⁻)=2`, G73) — survives C119's topological pre-filter (`ch₃` is
degree-6, filter only kills degree≤3) and does NOT collapse into C121's
just-rejected `η(D^t)` (checked directly: cubic/linear coefficient
ratios of the two odd functions differ by 9x, not proportional). **A
naive `∫_{M₄}P₄(M₄)=0` kill (for curvature-based `P₄` only) was found
OVERBROAD same day**: `P₄=vol₄` is always closed (no curvature needed)
and survives, reducing the mechanism to a t-dependent 4D vacuum-energy
term with the SAME shape as the bare CS mechanism — not new content,
not fatally killed either. This open question was pre-registered as
`C124` (six criteria, bottom-up search order, two negative controls,
design-freeze against HARKing), then blindly executed the same day by
a fresh agent with no memory of the pre-registering session, then FL
Step 8a skeptic-confirmed. **Result: `STRUCTURAL_NO_GO` — the
CS/transgression family, and a wider mismatched-curvature-contraction
class beyond it, is CLOSED as an OB1 F4 mechanism** — class-qualified
(local, polynomial, first-order, bosonic 13D-Lorentz-covariant
invariants only, per same-day external review). **Does NOT close
C123's separate Yang-Mills claim** (an S3-internal Hodge-star
functional, never a 13D-covariant reduction, and dimensionally
impossible to fit this classification's own epsilon-sector S3 leg
anyway) — YM's own status stays `PARTIAL` per C123, not killed. Also
does not close: extra covariant derivatives, non-polynomial
functions, additional p-form fields, an enlarged gauge algebra beyond
Lorentz, boundary/defect terms, nonlocal/quantum effective actions —
all named explicitly, not left implicit. A 13D-Lorentz-
covariant 13-form splits into two disjoint sectors by exact index/
degree counting: the sector that can carry `ε` (needed for `vol₄` or
any `S⁶` topological density) is forced exactly torsion-free — its full
reduced 4D contribution is `A+B·t(1-t)`, stationary only at the
zero-mode-free `t=1/2`, the wrong value — and the sector carrying
torsion is forced to odd torsion count, but the available block degrees
`{3,4,5,7,8,9,11,12,13}` are missing degree 6, so its `S⁶` leg is
identically empty. No 13D Lorentz Chern-Simons form exists at all
(Chern-Weil-ring generators sit at degree ≡0 mod 4; 14≡2 mod 4).
Skeptic-confirmed independently, with two prose errors found and
repaired (neither load-bearing) and L1 shown even stronger (adding a
13D gauge field cannot rescue this route either, only a genuine
degree-14 characteristic class could). Scope: bosonic, strict product
background — leaves open a parent action with an independent 13D gauge
field, a non-product background, or fermion bilinears (named,
unattempted, in the Relaxation Map). See
`experiments/20260901-c124-parent-invariant-classification-
preregistration/decision.md`. **Also same day: a genuine
new F4 finding on Yang-Mills** —
`E(t)=Ct²(1-t)²` has `E''(0)=E''(1)=2C>0` (stable) and `E''(1/2)=-C<0`
(unstable) along the 1-parameter family — Levi-Civita is a barrier top
between two flat vacua, though only checked in this 1D slice, not the
full fluctuation operator.

**F6 completed same day (C126, 2026-09-01→02, blind execution +
FL Step 8a skeptic pass, verdict `WEAKENED`, 9/9 skeptic findings
accepted).** The full second variation (not just the 1D slice) of
`S_YM` at `t=0,1` is positive semi-definite for general metric
perturbations, kernel exactly the gauge orbit — **but the pre-
registered kill criterion could not have fired**: `S_YM≥0` and `=0`
at flat points is a theorem, not a finding, so stability there carries
zero selection information. **Genuinely new content instead:** the
exhaustive homogeneous critical set is `{0}⊔SO(3)` (5 flat points +
4 saddles, 9 total, none newly stable) — the vacuum degeneracy is
LARGER than the family reveals, making selection harder, not easier;
the Levi-Civita saddle has Morse index exactly 1 (stable to `2j≤14`,
with an analytic bound at every `j`), its unique unstable direction
IS the family direction; and `∇^0`,`∇^1` are related by a LARGE gauge
transformation of winding number `n=-1` — meaning they are ONE point
of the full gauge-equivalence class `𝒜/𝒢` (so `S_YM` and every
`𝒢`-invariant functional of the connection alone is structurally
blind between them, a stronger reason than OB13's evenness argument)
but DISTINCT points of `𝒜/𝒢₀` (identity component only) — and
**the `t=1/2` barrier is therefore topologically FORCED, not an
artifact of the chosen path**, since Chern-Simons is exactly a
`𝒢₀`-invariant functional and already distinguishes them (`CS(0)=0≠
CS(1)`, C123). As affine connections (with the soldering form/torsion
kept) `t=0,1` remain genuinely distinct — nothing here revives C25's
already-refuted M2 branch (`ι` is still orientation-reversing,
C37-C39). Net: Yang-Mills is WEAKENED, not promoted, as an OB1
F4/F6 candidate. See `experiments/20260901-c126-yang-mills-full-
fluctuation-stability/decision.md`.
**Unplanned byproduct, found defending Claim 1, not this round's own
target: `OB13`'s own summary sentence below ("any selector must be
linear, never quadratic... even functionals carry no information") is
itself overstated** — an even functional cannot PREFER `t=0` over
`t=1`, but it CAN select the set `{0,1}` uniquely (round99's `V(t)`
does exactly this), which is real information toward the "forces `t=0`
and `t=1` together" branch OB1/F4 already accept. The project's own
later practice already contradicts the literal OB13 sentence: C119
(three weeks later) took an even/quadratic condition seriously as a
selector and killed it on geometry, not by a one-line parity dismissal.
Corrected wording proposed, not yet applied to OB13's prose below —
see `experiments/20260901-c123-ym-cs-transgression-panel-review/
decision.md` for the full FL Step 8a skeptic pass, both re-derivations,
and the Relaxation Map.

**F4 bordism/global-anomaly route scoped, not closed (C127, 2026-09-02,
run at explicit user request despite being the lowest-priority
Relaxation Map item):** the Zero-Signal Gate splits cleanly into two
readings `claim.md` itself pre-registers. SELECTING one `t in {0,1}` via
any topological invariant of a single fixed background is structurally
impossible — definitional, not a discovery: a bordism/characteristic-
class datum is a lift of a classifying map, and a lift of a classifying
map is not a connection. FORCING the pair (or a sign) is NOT excluded
and is well-posed: the mapping torus of C126's own winding-`(-1)` large
gauge transformation carries a genuinely nonzero class (`int c2=-1`),
but evaluating the actual anomaly on it is blocked on a newly-surfaced,
genuinely unrecorded gap — **this project has never reconciled whether
`nabla^t` is C125's metric affine connection (torsion a tensor, no
gauge relation between `t=0,1`) or C126's Yang-Mills connection
(`t=0,1` one gauge orbit, related by winding `n=-1`)** — plus round95's
already-known missing S6-S3 link. Both `Omega^Spin_13(pt)=0` and the two
further degrees the Anderson-dual sequence actually needs
(`Omega_14=Omega_15=0`) independently verified against a secondary
literature table, structurally cross-checked against the rational free
rank. Own FL Step 8a skeptic pass: `WEAKENED`, all 12 findings accepted
and repaired (including withdrawal of the first draft's own overbroad
universal no-go). OB1 stays `PARKED`; no reopen condition met. See
`PARENT_ACTION_GATE.md` F4 and
`experiments/20260901-c127-bordism-global-anomaly-scoping/decision.md`.

**Ingredient 1 (X2) CLOSED, C125-vs-C126 conflict resolved, NOT a
contradiction (C128, 2026-09-02, two independent skeptic passes,
differently worded, both `WEAKENED`, concordant):** by Maurer-Cartan
integrability, no smooth map of `S³` at all realizes C126's large gauge
transformation `g` as a frame transition (`dΦ+Φ∧Φ=0` reduces to
`λ(1+λ)=0`, roots only at `λ=0,-1`; `g` is `λ=+1`, non-integrable). C125
and C126 turn out to be about two different configuration spaces, not
in tension: this project's own frozen ansatz fixes the vielbein, which
is a *complete* gauge-fixing of C126's `𝒢`, so the ansatz lives in `𝒜`
itself (C125's category), not `𝒜/𝒢`. **Strengthened, not just
reconciled**: any diffeomorphism (not only an isometry) carrying
`∇⁰→∇¹` is automatically an orientation-reversing isometry — proven
algebraically and confirmed by an independent exact symbolic (Groebner)
computation. The apparent "different transformation groups" was an
artifact of a central factor (`-I`) that cancels in the connection
formalism; the real invariant is `det`, i.e. C125's already-certified
parity `ℤ₂` — winding number is not trivialisation-invariant here and
carries no obstruction. **X6 re-specified**: the mapping torus that
actually matters (of the orientation-reversing relating map, not of
`g`) is non-orientable, so `Ω^Spin` was the wrong functor; the honest
question (`Y1`) is whether it admits a `Pin^±` structure at all, still
gated on round95 for the fermion content's `Pin` type. See
`experiments/20260902-c128-nabla-t-gauge-group-reconciliation/decision.md`.

**Y1's existence question ANSWERED: both Pin types exist, so this route
alone cannot discriminate (C129, 2026-09-02, two independent skeptic
passes, concordant `CONFIRMED-REAL`/`WEAKENED` split):** the mapping
torus of the relating map admits BOTH `Pin⁺` and `Pin⁻` (exactly two of
each), because `H²(M;𝔽₂)=0` for the mapping torus of any self-map of
`S³` — confirmed 5 independent ways, including one using no chain
complex at all (`π₁`+`χ`+Poincaré duality). **Self-caught correction**:
C128 §6c had stated the Pin⁺/Pin⁻ existence criteria backwards
(contradicting its own Completeness section); fixed by consulting
Kirby-Taylor directly, harmless for C128's own verdict, load-bearing
downstream (`Ω^{Pin+}_4=ℤ/16` vs `Ω^{Pin-}_4=0` differ enormously). Via
the bare tangential structure alone the manifold gives NO discriminating
constraint — both types are always available on any such mapping torus.
The live gate narrows to: does the TWISTED structure the fermion content
actually needs exist (new item Z1, unevaluated, flagged as cheaper than
round95), and round95 (ingredient 2) is still required to know which
type is physically needed. See
`experiments/20260902-c129-pin-structure-existence-mapping-torus/decision.md`.

**Z1's twisted structure ANSWERED (also cannot discriminate), and a
higher-priority scope problem found (C130, 2026-09-02, two independent
skeptic passes, concordant `WEAKENED`):** the twisted structure
`Pin^±×_{ℤ₂}G` exists on `M_ι` uniformly, for EVERY group `G` with a
central order-2 element and every bundle — proved by a genuine transfer
argument (not assumed from C129), and shown non-vacuous by exhibiting
other manifolds where twisting flips the Pin verdict. So the twisted
route, like the bare one, gives no `t=0`-vs-`t=1` discriminator. The
frame-bundle's group (the only `G` this project's frozen content would
otherwise supply) turns out to be a type error as a twisting group — it
IS the tangential structure, not independent of it. **⚠️ New top-priority
item, promoted AHEAD of round95 (`W1`, cheaper to resolve):** `M_ι` (a
4-manifold) does not appear in C127's own already-verified dimension
audit at all (13D terms need `Ω₁₃,Ω₁₄`; 13D's own anomaly needs
`Ω₁₄,Ω₁₅`; the 4D effective theory's anomaly needs `Ω₅,Ω₆` — never `Ω₄`,
which is the home of a *3-dimensional* theory's anomaly, and this
project has none). The relevance of the manifold three consecutive
rounds (C128 §6b, C129, C130) analyzed is therefore **adversely
indicated**, not merely untested — either a reading exists where a
4-manifold is the right object, or these rounds answer a well-posed
question about the wrong one. See
`experiments/20260902-c130-twisted-pin-structure-existence/decision.md`.

**⚠️ W1 TESTED AND CORRECTED (C131, 2026-09-02; three drafts, four
context-blind skeptic passes, two direction-reversals — this entry is
this session's own synthesis after independently weighing all four
passes, not a transcription of any one draft, since the round's own final
draft was itself found internally inconsistent by its 4th, dedicated
review).** C130's two premises above are both false as stated: C127 §4's
list is non-exhaustive (omits the 4D-topological-terms row, which needs
`Ω₄` and `Ω₅`); and "no 3D theory" cannot be shown by grepping for that
string when the project's object is called `CS₃` — though the premise is
true in substance, since `∫_{S³}CS₃(ω^t)` is a number (a 4D term's
coefficient), not an actual 3D QFT's partition function. **The real
reason `M_ι` fails C127 §5d's specific question is ORIENTABILITY, not
dimension**: `H₄(M_ι;ℤ)=0` (re-derived independently twice, including
from scratch via the Wang sequence, not just read off a table) — `M_ι`
is closed and non-orientable, so `∫c₂` (the number C127 §5d needed) is
literally undefined on it; every legitimate reading needs an orientable
4-manifold and produces `S³×S¹` instead. **But `M_ι` is not homeless in
every sense** — C128 §6c already named the right reformulation (a
`Pin^±` class on a non-orientable 4-manifold, "textbook Dai-Freed
practice"), and C129/C130 already established `M_ι` supports it. **New
this round**: the UNTWISTED Pin route on `M_ι` is trivial —
`[M_ι]=0` in `Ω^{Pin+}_4` for both structures (explicit null-bordism,
`M_ι=∂(D⁴×_ι S¹)`) — so it also cannot discriminate anything. **The one
surviving live question is the TWISTED Pin structure** (the actual
swap-monodromy fermion bundle), needing group `G` — itself blocked on
round95. Net: C128/C129/C130's mathematics stands, untouched; every
route this program has tried now converges independently on round95 as
the sole remaining blocker (the 4th such convergence). See
`experiments/20260902-c131-mapping-torus-dimension-consistency/decision.md`
(read critically, not at face value — see `PARENT_ACTION_GATE.md` F4 for
the fuller account).

**DIVERGENT-mode 13D-parent-action survey run, H1c's actual remaining
gap (C132, 2026-09-02, user-directed exploration, not a convergent
verification — no candidate claimed correct):** 15 candidate mechanisms
survived a Novelty Check + Zero-Signal-Gate screen, outside the class
C124 already closed. Top-ranked after a skeptic pass corrected a real
inversion (`G₂`-equivariance constrains nothing about the S6 triality-
channel label; only an assumed triality `ℤ₃` symmetry buys full channel
symmetry, and even that borrows N_gen=3's own un-derived credit line):
(1) the symmetry-assumption ladder itself, cheap, ready to run as `C133`;
(2)/(2) Einstein-Cartan torsion-as-auxiliary (fermion-sourced, ready to
run as `C134`, must open against round72's own registered `E8` gate) and
a joint 13D Killing-spinor constraint; (4) a diagonal `ℤ₃` orbifold of
`S³`. Full ranked list, both ready-to-run sketches, and 4 pearls in
`PARENT_ACTION_GATE.md` F4 and
`experiments/20260902-c132-13d-parent-action-survey/decision.md`.

**Checked, external survey, no computation in N-7 itself (sibling
project H-19 "Геометрия калибровки", 2026-08-31 — the source of C120's
`I9` proposal above):** a targeted literature survey of 6 known
geometric-gauge/parameter-selection schemes, run specifically to look
for a transferable OB1 mechanism — Randall-Sundrum/Goldberger-Wise
(bulk-scalar radion stabilization), Calabi-Yau flux compactification
(GKP/KKLT, plus its own generalization to `SU(3)`-structure manifolds
without an integrable complex structure — the most-investigated
candidate, see below), `G₂`-holonomy M-theory (Acharya-Witten), Horava-
Witten heterotic M-theory (anomaly-fixed `E₈`+coupling, radius NOT
fixed), and Coset Space Dimensional Reduction (CSDR — found to be a
**kindred stuck problem**, not a solution: 45 years of literature never
selected the isotropy embedding either). **None of the 6 transfers.**
The `SU(3)`-structure generalization of GKP (Benmachiche-Louis-
Martínez-Pedrera CQG 25 (2008) 135006) got the deepest check: its one
torsion precondition (`𝒲₁≠0`) is satisfied EXACTLY by this project's own
frozen `S⁶` (`\|𝒲₁\|²=4/3`, independently re-derived from the imported
`build_T_table`, matching C119) — refuting the naive expectation that
non-integrability alone would block it — but the mechanism still fails
because it is a functional of purely 6-dimensional (`S⁶`-only) data,
structurally blind to `t` (which lives on the `S³` factor), not because
of non-integrability. Full write-up, including an FL Step 8a skeptic
pass that corrected several overreaches in the original framing:
`E:\Проверка Гипотез\работаю над проверкой гипотез\H- 19 geometria kalibrovki\phase2_transferable_patterns\gkp-su3-structure-generalization.md`
and `phase3_red_team_recomposition\recomposition.md` (external to this
repo — cited, not imported; verify independently before relying on it,
per this project's own G2 rule for external-source GO/PROMOTE
criteria). **The `I9` candidate checked as C120 above is that survey's
own concrete proposed follow-up test — already run and superseded by
the sharper `η(D^t)` lead**, so no further action item remains open
from H-19 specifically; its main residual value is the negative result
itself (6 independently-researched external schemes, zero transfers)
as context for any *future* external-literature candidate.

`D-bar_0` has an exact doubly-degenerate zero eigenspace that round67's
own family can never produce at `n=0` for any single `t` (its two
branches `3t` and `3t-3` are never simultaneously zero). This means the
C90-C106 apparatus cannot be trivially torsion-deformed by importing
round67's already-known crossing values — no cheap shortcut exists. Two
untested relaxations remain (a nonlinear `n=f(k)` map; building a torsion
deformation natively inside C85's own Peter-Weyl framework via its
certified `L_i(k)`/`R_i(k)` generators rather than importing round67's
abstract Kostant-cubic result) — neither attempted yet. Does not affect
KT-8's own established result or round67's own crossing values, both
independently unaffected.

**Checked, nothing new (2026-08-29):** before pursuing either relaxation
above, checked whether round68's own "recommended next action (a)" (plug
the real G73/G74A-certified twisted `D_S6` into round68's Cl(9) framework
and confirm `ker(D_full)=0` at `t=0`) could be done cheaply. Two findings,
for the benefit of any future session tempted to retry this: (1) G73/G74A's
own zero-mode result (`dim ker=1`) is established purely via Atiyah-Singer
index theory + Lichnerowicz gap + G2-Schur argument -- **no explicit matrix
realization of the real, curvature-twisted `D_S6` exists anywhere in this
repo.** Building one (a Peter-Weyl-for-G2/SU(3) analog of what C85 did for
SU(2)/S3) would be a genuinely new, multi-round research undertaking, not a
quick plug-in. (2) The logical deduction itself -- decoupling (round68) +
`D_S3(0)`'s zero eigenvalue (round67) + `D_S6,twisted`'s zero eigenvalue
(G73/G74A) implies `D_full` has a zero eigenvalue at t=0 -- was **already
written out explicitly**, with correct caveats, in round68's own
`results_e3.json` (`verdict.logical_conclusion_ker_d_full_nonzero_at_t0`,
2026-07-17). There is nothing to "formalize" -- it already exists,
correctly scoped. The only two ways to move OB1 forward from here remain
unchanged: (a) build the real `D_S6,twisted` matrix (large, novel
undertaking, not attempted), or (b) find a physical selection principle
for `t` (the already-PARKED, externally-blocked search).

**Attempted, FALSIFIED (round114):** a claimed "independent cross-check"
of round67's `h_H=3` calibration via
`Agricola_Hofmann_Lawn_2023_invariant_spinors.pdf` (arXiv:2203.02961, a
real, previously-unused, already-downloaded source in this repo) turned
out to reduce algebraically to citing that paper's own already-stated
Killing constant (`Cor 3.14`, itself the classical Friedrich 1980 round-S³
value) — no independent evidence. See `null_results/INDEX.md`
`Round114-AHL2023` and `pearl_registry/INDEX.md`'s new entry (the
"one-line-reducibility test" for future literature cross-checks). Genuine
literature searches in this direction remain worthwhile — this specific
round's SPECIFIC computation, not the whole approach, was the failure.

**Attempted, NULL-with-a-pearl (round115):** tested whether this project's
own already-established quantized `H³(S³)` flux (Hodge corollary,
`lambda-dim-gate/decision.md`) could select `t=0,1` via standard flux
quantization, if the torsion is identified with a genuine NS-NS-type flux.
**Confirmed circular for unconditional selection** (any target `t` admits
some `ρ₃`) — but found, along the way, that `ρ₃` is not actually "fully
free" as first assumed: a candidate stabilization mechanism exists (G94,
`ρ₃≈1.93`, itself conditional on an admittedly free coupling). Plugging
G94's value into the flux-quantization formula gives `K≈1.14` — 14% from
an integer, suggestive but explicitly **not** treated as evidence (rests
on 3 stacked unverified inputs). Logged as a genuine Pearl (recompute if a
future, non-coupling-conditional `ρ₃`-stabilization result appears),
`pearl_registry/INDEX.md`. See
`experiments/20260717-round115-flux-quantization-torsion-selection/decision.md`.

**Attempted, NULL-orthogonal-mechanism (2026-08-10, C41-C57 vs OB1, C58):**
the day's C11 chain investigated a fifth candidate mechanism rounds 114-117 did
not try: does forming a spectral triple from BOTH `t=0` and `t=1` together
(as two sectors of one Hilbert space) satisfy NCG's own axioms — i.e. is the
*combination itself* geometrically necessary? Full 14-round chain (C41-C57):
algebra does not earn it (C45/C46), the axioms force the deformation family to
`(0,0)` making the isolated kernel a selection rather than a fragility (C47/C48),
no real structure `J` admits a sector-mixing algebra factorizing or not (C50/C51),
and even taken as given, the resulting even triple fails orientability and
Poincaré duality (C49/C52-C54) — closed on a **derived**, not assumed, input
(C55/C56/C57). **Result: null, same shape as 114-117.** This rules out "the
combination is NCG-necessary" as an answer to why nature might care about
`t=0,1` together — but it is **orthogonal to OB1's actual question** (single `t`
selection for KT-8's single-copy operator, not the two-sector combination), so
it does not touch the zero-mode blocker itself. See
`experiments/20260810-c11-vs-ob1-kt8-crossreference/decision.md`. **OB1 stays
PARKED — no reopen condition met.**

**Attempted, equivalent-restatement (round116):** applied brainstorm item
28 ("spectral flow") in modest form to round67's own crossing family —
proved (general closed form, not spot-check) that `t=0,1` are the unique
innermost, symmetric pair closest to the Levi-Civita point, for all `n`.
Skeptic: this is an **equivalent restatement** of `D^t` being affine with
scalar slope, not new information — and silently drops the `(n+1)(n+2)`
eigenspace multiplicity, a real gap if "spectral flow" is ever invoked
more formally. Logged as a methodological Pearl (multiplicity must be
tracked in any future formal spectral-flow attempt). See
`experiments/20260717-round116-minimal-crossing-pair-structure/decision.md`.

**Attempted, consequence worked out (2026-08-10, C64, step-5 scoped
sub-question):** round116 flagged the `(n+1)(n+2)` multiplicity gap but
explicitly declined to justify its own claim that this "does NOT affect
`N_gen=3`." This round verifies the multiplicity directly (explicit `D^t`
matrix at `n=0`: exactly `3t·I₂`, exactly the zero matrix at `t=0`, `dim
ker=2` not 1) and works out the consequence via E3's product-decoupling
identity (`ker(D_full)=ker(D_S6)⊗ker(D_S3)`): round116's dismissal is
correct **only** for the construction as it currently stands (Levi-Civita,
`t=1/2`, `dim ker(D_S3)=0`) — if the torsion-deformation escape route is
ever picked up to resolve OB1 itself, it would multiply the generation
count by at least 2 at its cheapest crossing (multiplicities `2,2,6,6,12,12`
across all six known crossings, none equal to 1). **New caveat for this
blocker's own future record: the torsion-deformation mechanism is not just
unselected (the existing problem) but also never multiplicity-safe (a
second, independent problem any future attempt to use it would need to
solve).** Does not meet any of OB1's 4 reopen conditions — OB1 stays
PARKED. See
`experiments/20260810-step5-s3-torsion-multiplicity-safety/decision.md`.

---

## OB13 — C25/H1c: the two searches for a `t`-selector were in a provably blind parity sector [OPENED 2026-08-10, C37]

> **✅ ONE BRANCH KILLED SAME DAY (C39).** `ι` is an **orientation-reversing**
> isometry of `S³` (tangent determinant −1.000 at all 200 sampled points;
> negative control: left translation gives +1 at all 100). A gauge symmetry is
> connected to the identity and hence orientation-preserving, so **`ι` is NOT
> gauge — it is parity.** The "H1c is ill-posed" branch this blocker opened is
> therefore **dead**, and C38 stands: `(1,2)` and `(2,1)` are genuinely distinct
> states exchanged by parity, exactly as `SU(2)_L`/`SU(2)_R` relate in the SM.
> **C37 and C39 are the same statement reached two ways** — "the selector must be
> odd in `(t−½)`" and "the endpoints are a parity pair". The question is not
> ill-posed; it is *what breaks parity*, and in the SM parity is broken. See
> `experiments/20260810-iota-gauge-or-parity/decision.md`.
>
> **✅ STRENGTHENED INTO A THEOREM, FALSIFIED AS A DISSOLUTION (C125,
> 2026-09-01, blind execution + TWO independent FL Step 8a skeptic
> passes).** C125 asked whether the FULL 13D configuration (vielbein,
> connection, S⁶ twist, fermion content) at `t=0` is gauge-equivalent to
> `t=1` — not just the abstract S³ connection ι already knew about. Answer:
> **no genuine gauge transformation exists, provably, not just "none found
> yet".** Central theorem (one-line proof, independently re-verified
> twice): on S³, torsion `T^t=(2t-1)[·,·]` **is** a constant multiple of
> the volume tensor, so `φ_*T⁰=det(dφ)·T⁰`; since `T¹=-T⁰≠0`,
> `{φ:φ_*∇⁰=∇¹}=O(4)\SO(4)` **exactly** — C39's finding for `ι` specifically
> is now proven forced for *every* candidate map, not observed for one.
> Extended to the full product via a de Rham argument (the torsion
> 3-form's own cohomology class is non-zero and flips sign under any
> candidate `g`, needing no product-map or `Isom`-factorization
> assumption): **`(ii-gauge)` fails for all 8 sign-triple combinations of
> per-factor orientation choices — compensating on `M₄` or `S⁶` cannot
> rescue it.** So OB1/H1c does **not** dissolve into gauge redundancy —
> `t=0` vs `t=1` remains a genuine physical choice. **One residual,
> honestly UNDECIDED (not resolved either way, after a second skeptic
> pass caught the first draft asserting incompatible answers to the same
> open question):** the purely-orientation-compensated "Family C" (4D
> parity composed with `ι`, S⁶ untouched) satisfies every condition except
> "not parity" — whether this survives condition (iii) (fermion content)
> depends on whether the relative M₄↔S⁶ orientation is a physical datum
> or a labelling convention, which nothing currently certified in this
> project decides (needs round95's missing S⁶↔S³ link) — and whether OB1
> would even collapse if Family C survived is ITSELF conditional on that
> same unresolved question, not an independent fact. See
> `experiments/20260901-c125-full-gauge-equivalence-gate/decision.md` for
> the full derivation and both skeptic passes.
>
> **⚠️ NARROWED SAME DAY (C38).** The `t=0` and `t=1` kernels are the **two chiral
> halves of one 4-dimensional `Spin(4)` spinor** — `(1,2)` and `(2,1)`, verified
> under the `SO(4)` isometry action with the frame lift, negative control passing.
> So "which `t` is selected" is very likely **ill-posed: both are needed**, which
> is precisely the inversion branch this blocker flagged. `C27`, `C25`/`H1c` and
> `C11` collapse into **one** question — is the product ansatz with both `t`
> simultaneously realized coherent? See
> `experiments/20260810-c27-bundle-equivalence/decision.md`.
>
> **✅ `C11` ANSWERED (same day, later in the session): NO — not coherent as a
> geometry.** The full C41-C60 chain (14 rounds) settled this exact question:
> the axioms force the deformation family to a single isolated point (C47/C48),
> no real structure admits a sector-mixing algebra (C50/C51), and even granting
> the construction, it fails BOTH orientability (C52) and Poincaré duality (C49)
> — independent of the KO-dimension question C54-C60 separately closed. **This
> item's own "coherent?" question has a definite answer: no.** Cross-referenced
> here since this note (written during the arc) predates that closure and would
> otherwise read as still-open. See `experiments/20260810-c11-*/decision.md`
> (C41 through C60) for the full chain; `CLAIM_LEDGER.yaml` C41-C60.

`t → 1−t` is exactly `(t−½) → −(t−½)`, so **any even function of `(t−½)` is
identically blind** to the `t=0` vs `t=1` question. Checked [VERIFIED-sympy]:
round111's `Scal(t) = Scal_LC − 6(2t−1)²` **EVEN**; round99's curvature-norm toy
**EVEN**; E2's Dirac family `σ(n+3/2) + (t−½)h_H` **ODD** in the shift.

**Consequence:** both curvature-based searches were structurally incapable of
selecting. Their nulls were *necessary* and carry **no** information about
whether a selector exists — they were never tests of H1c. Any selector must be
**linear (odd) in the torsion**, never quadratic.

> **⚠️ CORRECTED 2026-09-01 (C123, FL Step 8a skeptic pass, found
> defending an unrelated claim — not this section's own target).** The
> paragraph above **overstates what evenness rules out**, on three
> independent grounds. (1) It conflates "cannot PREFER `t=0` over `t=1`"
> (true for any even functional) with "carries NO information about
> whether a selector exists" (false — an even functional like
> `V(t)=[t(t-1)]²`, `round99`'s own curvature-norm toy, selects the SET
> `{0,1}` uniquely against every other `t`; that is information). (2) It
> contradicts OB1/`PARENT_ACTION_GATE.md` F4's own stated pass criterion,
> which explicitly accepts a mechanism that "forces `t=0` and `t=1`
> together" — exactly the branch an even functional CAN serve. (3)
> "Linear" conflates polynomial degree with parity: the correct
> requirement is "has a nonzero component odd in `(t-1/2)`," which any
> odd-degree term (cubic included — e.g. the Chern-Simons functional
> every one of 4 independent derivations this project has now produced
> gives) satisfies; "linear" wrongly excludes those. **The project's own
> later practice already reflects this**: C119 (2026-08-31) took an
> even/quadratic condition (`Rc=¼H²`) seriously as a candidate selector
> and killed it on geometry, not by a one-line parity dismissal, which
> the literal rule above would have made unnecessary. **Corrected
> statement:** an even functional in `(t-1/2)` cannot break the residual
> `t=0`-vs-`t=1` degeneracy (OB13's real, defensible content, and C37-C39
> below stand unaffected) — but it CAN legitimately select `{0,1}` as a
> set, and "round99's own null carries no information" was itself
> mislabeled: `round99`'s script status is
> `CONFIRMED__DOUBLE_WELL_PLAUSIBLE_FROM_CLASSICAL_CURVATURE`, not a
> null. See `experiments/20260901-c123-ym-cs-transgression-panel-review/
> decision.md` for the full derivation. Round80/E14 makes this a
symmetry statement: `ι(g)=g⁻¹` pulls the whole family `∇^t → ∇^(1−t)` exactly, so
`t↔1−t` is a genuine symmetry and only an odd term can break it.

**Unrepresented branch:** `C25` is recorded as OPEN, which presupposes an answer
exists. If `ι` is a **gauge** symmetry rather than merely an isometry, "which
endpoint" is like asking which gauge representative is physical — and every
even-parity null to date is exactly what that predicts. **Cheapest test:** does
`ι` act trivially on all physical observables (spectrum *and* zero-mode content)?
Trivially → close `C25` as ill-posed (a result, not a failure). Moves something →
that something is the selector, and it is necessarily torsion-odd.

See `experiments/20260810-consortium-c25-parity-of-t-selection/decision.md`.

---

## OB12 — KO-dimension mapping: the sign tuple is verified, the NUMBER is not [OPENED 2026-08-10, C36 fallout]

**The gap, stated precisely.** G18's finite triple has the tuple
`(J², JDJ⁻¹/D, JγJ⁻¹/γ) = (+1, +1, −1)`, all three **computed in this repo**
[VERIFIED-sympy]. The label `KO-dim 6` attached to it is **inherited from CCM**
and has never been derived here — this repo holds no sign-triple table, no CCM
source file, and no internal mapping. `G26`'s own comparison already marked
CCM's KO-6 as `[DOCS] postulated`, so *both* sides of "same KO-dim
independently" (its original wording, corrected 2026-08-10) were inherited.

**Status:** `BLOCKED_BY_EXTERNAL_INPUT` — a dependency, not a failure. Unchanged by this
consolidation pass (2026-08-10) — still genuinely needs a cited primary source, nothing
computable from inside this repo closes it. Noted for context, not as a substitute: C49/C52
(OB2, below) already prove the specific `t=0,1` doubled construction this number would classify
is not a valid geometry regardless of what the number turns out to be — low-stakes as things
currently stand, not because the gap itself is resolved.

**What closes it** (either one): a cited primary source for the sign-triple ↔
KO-dimension table, transcribed with *its own* convention stated — in particular
which sign that source calls `ε`, `ε′`, `ε″`, since G18's docstring ordering and
the common literature ordering do not obviously agree; **or** an internal
derivation over `n mod 8` for the model Clifford triple. The machinery for the
reality-type half already exists (`label_vs_code_check.py`), but the
finite-geometry conventions relating `J` to `D` are subtle enough that this must
be derived, not assembled by analogy.

**Until then:** quote the tuple, never the number. Registry:
`docs/ko_dimension_registry.md`. Enforced by `hooks/claim_scope_gate.py`.

**Do not fold this into the geometric side.** `C32`/`C33`'s reality types are
for the **geometric** `S³×S⁶` module — a different object. Combining finite and
geometric KO-dimensions is a theorem with hypotheses, not arithmetic; OB10's
original `3+6=9 ≡ 1 mod 8` is exactly the shape that needs that care.

---

## OB2 — D4: does "two coexisting D's" even make sense as a spectral triple? [ANSWERED 2026-08-10 (C60): NO — see C11's full closure below]

> **Header updated 2026-08-10, consolidation pass.** This item's own body
> (below) already reaches a complete, final answer as of C60: the KO-2/KO-4
> ambiguity is proven irreducible (not merely observed), and, independent of
> that question entirely, C49/C52 already proved the doubled `t=0,1`
> construction fails BOTH Poincaré duality and orientability — it is not a
> valid NCG geometry. Everything below is genuine, verified content;
> "bookkeeping on bookkeeping on a non-geometry" (C60's own words) is the
> accurate, final characterization, not a hedge. No further work is expected
> here absent new external input (matching OB1's own PARKED framing).

> **KO TUPLE COMPUTED, 2026-08-10 (C57) — and it CORRECTS C56. The Pin choice
> cancels. `(ε,ε',ε'') = (−1,+1,±1)`, KO-dim 2 or 4 by an internal choice in `J`.**
>
> **C56's `U5` was WRONG** and is amended in place: it said `ε''` flips with the
> Pin choice, from `J(cX)J⁻¹ = c̄·JXJ⁻¹`. That accounting never asked what `J_M`
> does to `U_ι`. With `U_ι = c'·W` (`W` = the **real** swap), C56's own condition
> `c·c' = ±1` makes **`γ = ±(W⊗s₁)` — the same real operator for both Pin
> choices** — and a real `γ` picks up no phase under `J` at all. The `c̄/c` flip is
> compensated exactly by `η = J_M U_ι J_M⁻¹/U_ι = c̄'/c'`: `(+1)(+1)` vs
> `(−1)(−1)`. **Two flips, no net effect.** Second red herring of the session,
> after `U_ι²` itself.
>
> **The tuple:** `ε = −1` for every diagonal `k` (from `J_M² = −1`); `ε' = +1` is
> **forced** and forces `k` diagonal — `s₁`,`s₂` fail outright; `Jγ = ε''γJ`
> narrows `k` to `{I, s₃}` — `diag(1,i)` fails. So `k=I → KO 4`, `k=s₃ → KO 2`,
> and `diag(1,−1) = −s₃` reproduces `s₃` (phase-of-`k` coherence check).
> **The KO 2 / KO 4 choice is internal to `J`, not geometric.** Metric dim is 3,
> so the mismatch is 7 or 1 mod 8 — reported, not interpreted.
> **Control:** the machinery recovers `S³`'s own KO-dim 3 from its declared
> inputs. *Scope fix recorded: `K3` was asserted over all `k` but claimed only for
> diagonal `k`; `s₂` is imaginary so `s₂·conj(s₂) = −I` gives `ε = +1`. Claim
> right, test wider than the claim.*
> **The KO table is `[DOCS]`, not re-derived** — C36's lesson. And C49/C52 still
> stand: this is bookkeeping on a **non-geometry**.
> See `experiments/20260810-c11-ko-tuple-pin-choice/`.
>
> **`U_ι² = ±1` RETIRED, 2026-08-10 (C56). The C45 flag was a FALSE ALARM,
> carried for ten rounds. Every named unknown in this line is now closed.**
>
> Saying the null plainly: **nothing was discovered except that the worry did not
> apply.** `γ = c·U_ι⊗s₁` is a valid grading for **either** sign —
> `c = ±1` when `U_ι² = +1` (self-adjoint), `c = ±i` when `U_ι² = −1`
> (**anti**-self-adjoint, and the imaginary phase compensates:
> `γ² = i²·(−1) = +1`, `γ† = γ`). **The mismatched pairings genuinely fail**, so
> it is not a vacuous rescue; `{γ,D}=0` holds in all eight rows because it is
> phase-blind — shown, not hidden.
> *Why the freedom exists:* by C55 `U_ι` maps `(j,j±½)→(j±½,j)` and `j ≠ j±½`, so
> it is **purely off-diagonal** — no fixed blocks — and `i` moves between the two
> cases.
>
> **Phase-independent:** `‖[D_M,V]‖ = 11, 19, 35, 67` — *identical* for both
> lifts. C50/C51/C53/C54's `V ∉ 𝔅`, C52's locality, C55's L↔R swap: all untouched.
> **Where it does matter:** `J` is antilinear, so `c̄/c` = `+1` (real) / `−1`
> (imaginary) — **the `ε''` sign of the KO tuple flips with the choice.** That is
> exactly the combination C48 declined to make, and the abstention now has a
> *reason*: it depends on a choice nothing in the construction fixes.
> **Geometry:** in the canonical `S³` convention (`Z_i = i·σ_i`, `e²=−1`,
> `Cl(0,3)` — per `docs/clifford_convention_registry.md`) `ω = +I`, `ω² = +I`; the
> opposite convention gives `ω² = −I`. **The sign of `ω²` is the convention** —
> C34's point, a third time. Pinning `U_ι²` is a **Pin⁺/Pin⁻ choice**; `S³` admits
> both and nothing here needs one. Recorded as a choice, not a fact.
> See `experiments/20260810-c11-uiota-squared-sign/`.
>
> **KO TUPLE, FINALLY, 2026-08-10 (C60). The KO-2/KO-4 split is REAL, not a
> gauge artifact — C57's characterization is now a PROOF, not an assertion.**
>
> Transformation law: for sector-only `V=I_M⊗v` and `J=J_M⊗(k·conj)`,
> `k' = v k v^T` (not `v k v†` — the extra transpose is from antilinearity).
> **G1:** any `V` preserving `D_block` must be sector-diagonal (commutant of
> `s3` = exactly the diagonals). **G2:** requiring it to send `γ` to a
> phase-times-itself forces `v ~ I` or `v ~ s3`, nothing else. **G3/G4, proved
> for ALL admissible `v` at once:** `k=I`'s orbit is exactly `{phase·I}`;
> `k=s3`'s orbit is exactly `{phase·s3}` — two **disjoint** 1-dim rays, since
> `I`,`s3` are linearly independent. **G5 discriminator:** the same machinery
> correctly recovers the known trivial equivalence `k=I ∼ e^{iθ}I`.
> *Two harness bugs caught before accepting the verdict, neither touching the
> algebra: a sympy `==` that didn't know `σ²=1`; a grid search whose tolerance
> was tighter than its own step size (fixed by solving `α=θ/2` exactly).*
>
> **Consequence: nothing in `(A,H,D_block,γ)` selects KO-4 over KO-2 — this is
> now proven, not just observed.** Residual: only sector-only automorphisms
> checked; a fuller `V_M⊗v` search remains untested but has little room to
> matter given C59's own uniqueness result for `V_M`.
> **Zero consequence for whether the object is a geometry** — C49/C52 already
> settled that. Bookkeeping on bookkeeping on a non-geometry.
> See `experiments/20260810-c11-ko-final-gauge-or-real/`.
>
> **W1-LIFT RUN, 2026-08-10 (C59). `A1-lift` is a THEOREM, not an assumption.**
>
> `ι(ag)=g⁻¹a⁻¹` (pure associativity) means `ι` intertwines `L_a` with `R_{a⁻¹}`.
> Any unitary implementing `ι` **equivariantly** — the definition of "lift of an
> isometry," independent of any convention — is forced by **Schur's lemma** to
> map isotypic block `(j,k)` only to `(k,j)`, unique up to a phase, because
> `V_j⊗V_k*` is one irrep per factor of a product group.
> **[VERIFIED-numpy], not just cited:** built the equivariance condition from
> explicit `su(2)` generators, solved as a linear system. `S2` matching pairs →
> null dim exactly **1** (existence + uniqueness); `S3` **negative control**
> (same dimension, label *not* swapped) → null dim **0** — dimension alone does
> not force a solution, only the label match does; `S5` applied to C55's own
> `(0,½)` pair reproduces exactly the phase freedom C56 already used.
> *A real bug was caught here: the first `dual_generators` used `conj(J)`, which
> flips the `su(2)` commutator's sign and isn't even a valid representation on
> its own — caught by hand-checking `(0,½)` against Pauli matrices before
> accepting the result. Correct contragredient generator: `J* = −conj(J)`.*
> **Consequence: the whole `U_ι`-dependent chain (C50/C51/C53/C54/C57) now rests
> on zero named assumptions about the lift** — only on what "lift of an isometry"
> means, plus the already-used phase freedom.
> See `experiments/20260810-c11-a1lift-schur-block-preservation/`.
>
> **A1 VERIFIED, 2026-08-10 (C55). After ten rounds as an inherited assumption,
> it is DERIVED — and it independently reproduces round67's own spectrum.**
>
> Peter–Weyl on `SU(2)`: label each isotypic piece `(j,k)` = (left spin, right
> spin), `k = j ± ½`. Then
> **`λ(j,k) = (j+k+1)·sign(k−j)`, mult `(2j+1)(2k+1)`** — and with `n = 2j` on the
> `+` branch, `n = 2j−1` on the `−` branch this reproduces `±(n+3/2)` with
> `(n+1)(n+2)` **exactly**, for both branches. That is an **independent derivation
> of the spectral data this project has used since round67.**
> `ι(g) = g⁻¹` exchanges left and right translations, so `ι*` maps `(j,k) → (k,j)`.
> The swap **preserves** `j+k+1` and **flips** `sign(k−j)`, so
> **`λ(k,j) + λ(j,k) = 0` identically**, with symmetric multiplicities — a
> bijection from each `D`-eigenspace onto the `(−D)`-eigenspace. **That is A1.**
> **Cross-check:** A1 ⟹ `U_ι D^t U_ι† = −D^{1−t}` = C44's mirror relation, which
> C44 got from the closed form. Two routes now corroborate instead of sharing a
> source. **Control** (same code path, opposite answers): `ι`'s swap flips `λ`;
> left translation's identity map does not. **Discrimination:** drop `sign(k−j)`
> and nothing flips. *Seventh cannot-fail check written out here too — the first
> control was `λ(j,k) − λ(j,k) == 0`.*
>
> **What the chain inherits now is the strictly weaker `A1-lift`** (the geometric
> lift may differ by a unitary preserving the isotypic decomposition — a phase,
> not the sign of `D`). **`U_ι² = ±1` remains OPEN since C45** and is now the only
> named unknown in this line.
> See `experiments/20260810-c11-a1-iota-flips-dirac/`.
>
> **CAVEAT O′ RUN AND DISSOLVED, 2026-08-10 (C54). The LAST open door in the
> C11 line is closed — and the chain's single unverified input is now named.**
>
> **The worry was not empty:** cancellation is real — `U_ι` and `I − U_ι` both
> have `‖[D_M,·]‖ = 67.0` at N=32 and growing, their sum has `0.0`.
> **But it aimed at a step the proof does not take.** It presupposes a
> *decomposition* argument; orientability needs a **span** argument, which is
> immune to cancellation. With `𝔅 = {Z bounded : [D_M,Z] bounded}`:
> `𝔅` is a linear subspace and an algebra (Leibniz, 200 random pairs);
> `U_ι ∉ 𝔅` (`[D_M,U_ι] = 2D_M U_ι`, norms `11→19→35→67`);
> **every available operator is in `𝔅`**. So everything reachable is in `𝔅` and
> `U_ι` is not. **Cancellation would have to happen *inside* `𝔅`, and a sum of
> `𝔅`-elements is a `𝔅`-element.** `U_ι` is precisely the *unavailable* operator.
> *Sixth cannot-fail check of the session written out here too — the obvious
> control was `I @ γ == γ`; replaced by a two-directional soundness test of the
> growth detector (level shift `n→n+1`: bounded ✓; long range `n→2n`: unbounded ✓).*
>
> **⚠️ WHAT THE WHOLE CHAIN NOW RESTS ON — `ASSUMPTION A1`
> (`U_ι D^{1/2} U_ι† = −D^{1/2}`), inherited from C39 and NEVER re-derived here.**
> It is exactly what makes `[D_M,U_ι]` unbounded, so C50, C51, C53 and C54 all
> depend on it. If A1 were false, `U_ι` could lie in `𝔅` and all four would need
> rebuilding. **The most valuable remaining check in this line is A1 itself, not
> another escape route.**
> See `experiments/20260810-c11-caveat-o-prime-cancellation/`.
>
> **CAVEAT O RUN AND CLOSED, 2026-08-10 (C53). `J` cannot supply the `U_ι`.
> Only CAVEAT O′ (a fine-tuned cancellation) is left in the whole C11 line.**
>
> The escape was real: with `B =` the `ι`-**even** functions the commutant of `B`
> on `H_M` has **dim 24**, and every element decomposes as `m + m'·U_ι` — `U_ι`
> itself is in `A'`, because `m·U_ι` commutes with `b` exactly when `b∘ι = b`.
> **But `[D_M, m'U_ι] = {D_M,m'}U_ι` is ORDER ONE** — norms `11 → 19 → 35 → 67`
> as the cutoff rises — while `[D, Jb*J⁻¹]` is **bounded** (because `[D,b*]` is
> and `J` is antiunitary). So `JAJ⁻¹` is `U_ι`-**free**.
> For the extreme `B = C·1`, where `A'` is everything and locality says nothing,
> a different bookkeeping closes it: the algebra generated by `A ∪ [D,A]` has
> `H_M` factor identically **`I`** (counter-case: admitting `U_ι⊗I` breaks it in
> 8/16 elements). **Discriminator:** *allow* `JuJ⁻¹ = U_ι⊗s₁` and `γ` is
> reproduced **exactly** — boundedness is doing all the work, not genericity.
> *Two of my own errors caught here: O1's Z₂-average split returned False for a
> true claim (the average keeps `X`-off-diagonal entries — the split is by
> `X`-block); and O3 was hardcoded `True`, the fifth cannot-fail check this
> session.*
> **CAVEAT O′, the honest limit:** `JuJ⁻¹` could be a sum whose `U_ι` term's
> unbounded commutator cancels against another unbounded term. A finite model has
> no unbounded operators. Such a `J` must still satisfy order-zero, `J² = ±1` and
> `JD = ±DJ` alongside that fine-tuning.
> See `experiments/20260810-c11-caveat-o-a-tensor-aop/`.
>
> **Y2 RUN AND CLOSED, 2026-08-10 (C52) — and it retires Y1′ and the Lipschitz
> residual with it. `γ` is built from a DIFFEOMORPHISM, and that is fatal.**
>
> Y2 **is** a real escape from the `J` chain, exactly as predicted: with
> `B = C·1`, `A = C⊕C` is sector-mixing, `dim A' = 128`, `u = 1⊗s₁` sits in its
> **own** commutant, `[D,u]` is bounded — C50's W1a/W1c do not apply at all.
>
> **A different axiom closes it.** Every `a ∈ A` and every `[D,a]` is **LOCAL**
> (`g·T·f = 0` for disjoint supports). `γ = U_ι⊗s₁` is **NOT** — witness
> `‖1_c·γ·1_{c'}‖ = 2.0`. Products of local operators are local (400/400), so
> `π_D(c)` is local for **every** Hochschild chain and can never equal `γ`.
> **ORIENTABILITY FAILS.** The argument never mentions `B`, `J`, or `A'`.
> Counter-case (so the lemma can fail): smuggle one `U_ι` in → **400/400
> non-local**, and `γ` becomes reachable exactly. Discrimination: any **local**
> replacement for `U_ι` removes the obstruction — but C45 already showed a local
> `γ` cannot anticommute with `D_block`. **Anticommutation demands `ι`;
> orientability forbids it.**
>
> This also **explains C49**: orientability produces the fundamental class, PD
> needs it non-degenerate, both fail for one reason. **Only CAVEAT O remains** —
> the `A⊗A°` formulation, where `π_D` also carries `Ja*J⁻¹`; local iff `JAJ⁻¹`
> is, which C50/C51 gave only for `A ⊇` twisted diagonal.
> See `experiments/20260810-c11-y2-smaller-diagonal/`.
>
> **Y1 RUN AND CLOSED, 2026-08-10 (C51). Mixing without a swap unitary is
> excluded too, and C50 becomes its `f ≡ 1` special case. Only Y2 is left.**
> The sliver was real and had a concrete inhabitant: `A = ⟨twisted diagonal,
> x₀⊗s1⟩` mixes sectors, and every off-diagonal element `G·x₀⊗s1` vanishes on
> the equator, so none is unitary — C50 genuinely did not reach it.
> **The mechanism is a mass term only mixing elements get:**
> `|[D, f⊗s1]|² = (|df|² + 9f²)⊗I` but `|[D, λI⊗I]|² = |dλ|²⊗I` — no `9λ²`,
> because `(3/2)I⊗s₃` commutes with anything diagonal. `J` must send mixing to
> diagonal (C50), so it would carry an operator **bounded below by 1**
> (`|df|²+9f² = 1+8x_i²` on `S³`) onto `c(dλ)`, which **must vanish** at a
> maximum of `λ` — every smooth function on a compact boundaryless manifold has
> one. Contradiction.
> *Third random-sampling/tautology trap of the session caught here: `min |dλ|²`
> over 200k random points gave `5.5e−04` and reported **False for a true
> statement**, because `|∇x₀|²` vanishes only at the two poles. Replaced by
> gradient ascent to the actual maximiser.*
> **Cost named:** ASSUMPTION R (regularity, `λ` smooth) — C50's special case did
> not need it. **Residuals:** Y1′ (off-diagonal functions all vanishing to
> *second* order at a common point), the Lipschitz loophole, and **Y2**
> (diagonal part smaller than the twisted diagonal) — the only untouched one.
> See `experiments/20260810-c11-y1-mixing-without-unitary/`.
>
> **W1 RUN AND CLOSED, 2026-08-10 (C50). The last escape route is gone, and
> C48/C49 are now ANSATZ-FREE.**
> The expectation going in was that W1 would **succeed** — the crossed product's
> Tomita–Takesaki conjugation *is* non-factorizing and satisfies order-zero for
> free. It fails for an unrelated reason. Chain: `A'`'s off-diagonal blocks all
> carry `U_ι` → those have **unbounded** commutator with `D` → but `[D,u] =
> −3i(I⊗s₂)` is **bounded**, so `JuJ⁻¹` must be sector-**diagonal** `= h⊗I`
> (**this step uses boundedness alone — no factorization assumption**) →
> `J(I⊗s₂)J⁻¹ ∝ [D_M,h]⊗I` must be a unitary involution, so `[D_M,h]` invertible
> → but bounded `[D_M,h]` forces `h` to commute with all Clifford multiplication,
> whose commutant is 1-dim and scalar, so `h = ±I` and `[D_M,h] = 0`. **Contradiction.**
> **No `J`, factorizing or not, admits a sector-mixing algebra containing the
> sector swap.** Discrimination: it does **not** kill sector-diagonal `T7` (step 5's
> `J` still stands); control: same code reproduces C48's factorizing no-go.
> *Two more of my own weak checks were caught here — `W1b` v1 grew by construction,
> v2's "bounded" comparison side was exactly 0.*
> **Net: the doubling is unearned from FOUR directions, the last ansatz-free.**
> Remaining slivers: a sector-mixing algebra with **no** swap unitary (Y1), and a
> diagonal part smaller than the twisted diagonal (Y2). Neither is the crossed
> product. See `experiments/20260810-c11-w1-nonfactorizing-J/`.
>
> **STEP 6 RUN, 2026-08-10 (C49). PORTFOLIO COMPLETE except step 7 (deferred).
> Poincaré duality FAILS: the even index pairing vanishes identically.**
> `γ` must be sector-OFF-diagonal (that is what made it exist), so it maps
> `ker(D^0)` onto `ker(D^1)` and `Tr(γ|ker) = 0` → `ind(D_block) = 0`. The
> pairing vanishes for every `p ∈ A` **because C48 forced `A` sector-diagonal** —
> and the discriminating counter-case confirms it: sector-*mixing* projections
> give `Tr = 0.78, 1.68, 1.93`, non-zero. *A tautological test was caught here
> too: the first version compared block-diagonal `p` against an off-diagonal
> `γ`, where `Tr=0` holds by shape for any algebra at all.*
> **The grading and the vanishing pairing are two faces of one structure**, so
> the doubling does not merely fail to earn itself — it cancels the very
> spectral asymmetry an odd (single-sector) triple would pair with.
> **Gate: `H`,`D`,`γ`,`A`,`J` supplied · `PD` FAILS · physics NOT.**
> Highest-value open question is now escape **W1** (a `J` that does not factor
> as `J_M ⊗ j`), which could readmit a sector-mixing algebra.
> See `experiments/20260810-c11-step6-index-pairing/`.
>
> **STEPS 3+4+5 RUN, 2026-08-10 (C47/C48). The doubling is UNEARNED from THREE
> independent directions now — but the axioms do force `(α,β) = (0,0)`.**
>
> **C47.** The block admits exactly one minimal off-diagonal family,
> `α(I⊗s₂) + β(D^{1/2}⊗s₁)` (the parities are forced in *opposite* directions by
> `{γ,D}=0`), with eigenvalues `μ ± √(9/4 + β²μ² + α²)`. The 4-dim kernel matching
> C38's Spin(4) spinor survives **only at the origin** — the `n=0` condition is
> `α² + (9/4)β² = 0`, positive-definite. Other crossings over-produce (12, 24, 40).
> *A tolerance bug was caught here: probing `α=1e-6` gave "ker = 4" because the
> eigenvalue `≈α²/3 ≈ 3e-13` sat inside my own `atol=1e-9`.*
>
> **C48.** `β = 0` by **boundedness** (the `β` term carries the unbounded `f·D^{1/2}`
> unless `[s₁,m]=0`), `α = 0` by **first-order**. So the isolation is a **SELECTION**,
> not a fragility — the branch named in advance. Note the same bounded-commutator
> axiom that was *completely blind* in C45 is *sharp* here.
> **But `J` excludes the MAXIMAL algebra**, the opposite of C45's hope V2: `T4`'s
> sector part is all of `M₂(C)`, whose commutant is `C·I`, so order-zero has no
> solution; `T7`/`T6` survive. **With `J` imposed the algebra is sector-DIAGONAL and
> cannot force the doubling in any form.** Escape W1 (a `J` that does not factor as
> `J_M ⊗ j`) is untested and is the one real route left.
> See `experiments/20260810-c11-step34-offdiagonal-deformation/` and
> `experiments/20260810-c11-step5-real-structure/`.
>
> **STEP 1 RUN, 2026-08-10 (C45/C46). The algebra does NOT earn the doubling
> either — but it does constrain its FORM.** C45 as worded is **REFUTED**: three
> typed candidates are admissible and nested (`A+⊗I ⊂ twisted-diagonal ⊂ crossed
> product`), because admissibility is inherited by every unital subalgebra. The
> maximal one, `C^∞(S³) ⋊_ι Z₂`, **is** unique up to a sector-preserving unitary —
> but only *given maximality*, which NCG does not supply (the algebra is input
> data, not derived). Two supporting facts: `D^0 − D^1 = −3·Id` is **bounded**, so
> the bounded-commutator axiom **cannot see the sector index at all**; and the
> grading moduli are ~5·10⁴-dimensional, so `γ` needs the extra demand of being
> *geometric* before "the algebra selected by the grading" even parses.
>
> **What survives is C46, and it does not need maximality:** if the doubling is
> taken it is a **parity doubling** — `odd⊗I` is `γ`-forbidden, so the second
> sector necessarily carries `f∘ι`. `A₀⊗I` (duplicate) and `A₀⊗{I,s₃}`
> (independent copies) are both closed unital algebras and both **fail**.
> Controls: `I⊗s₁`, `U_ι⊗I`, `U_ι⊗s₃` all fail to anticommute; `U_ι⊗s₂` passes.
> **`ι` is load-bearing.** Gate → **3.5/6**. Next: `J` + first-order (step 5),
> which could exclude the small subalgebras and earn the maximal one *without* an
> axiom of convenience. See
> `experiments/20260810-c11-step1-algebra-search/decision.md`.
>
> **⚠️ DEFLATED SAME DAY (C44) — the grading is GENERIC. Read this before the
> C43 block below.** `spec(D^{1−t}) = −spec(D^t)` is an **identity in `t`** (the
> family is affine, `spec(D^{1/2})` already symmetric), so the grading exists for
> **every** mirror pair `(t, 1−t)` — confirmed at `t = 0, 1, ¼, ½, −⅓, 4/3, 2.7`
> and a random `−1.12`; non-mirror pairs all fail (control). **It therefore says
> nothing about `t=0,1` and must NOT be cited as evidence that the doubling is
> structurally motivated.** What survives: the grading is not *obstructed* for the
> block where C35 showed it is for one operator — a **removed obstacle, not a
> positive reason to double**.
>
> **The specificity lives in the KERNEL:** `dim ker(D^t ⊕ D^{1−t})` = 0 generic,
> **4 at `t=0,1`**, 12 at `−⅓,4/3`, 40 at `t=2`. So `(0,1)` is not just the
> innermost crossing pair but the one with the **smallest non-zero kernel** —
> a minimality observation, **not** a selection principle.
>
> **Net: the doubling is NOT yet earned, and the algebra now carries the full
> weight** without the grading as support. See
> `experiments/20260810-c11-step0-specificity/decision.md`.
>
> **✅ FIRST POSITIVE RESULT ON THIS LINE — 2026-08-10 (C43). GATE NOW 3/6.**
> The block `D⁰ ⊕ D¹` **supplies the grading C35 proved impossible for a single
> operator**. `spec(D¹) = −spec(D⁰)` **exactly**, multiplicities included — an
> identity, not a truncation artifact: the pairing is level-by-level at
> *identical* `n` (`−[n] = −n` ↔ `D¹`'s `σ=−1`; `−[−n−3] = n+3` ↔ `D¹`'s `σ=+1`,
> same `(n+1)(n+2)` each), confirmed at `N_MAX = 3, 6, 12, 20`. So the block
> spectrum is symmetric where each alone is not, an explicit `γ` was built
> (`γ²=I`, `γ=γ†`, `{γ,D}=0` all verified), and `dim ker = 4` matches C38's
> `Spin(4)` spinor. **Negative control:** the identical logic on `D⁰` alone
> **fails** — that control *is* C35's result.
>
> **Not a coincidence.** C39 showed `ι` is orientation-**reversing**, and
> reversing orientation flips a Dirac operator's sign. The mirror spectra are
> that fact expressed spectrally — the same structure reached a third time.
>
> | gate field | status |
> |---|---|
> | Hilbert space `H` | ✅ `L²(S³,S) ⊕ L²(S³,S)` |
> | Dirac `D` | ✅ `D⁰ ⊕ D¹`, round67's closed form |
> | **Grading `γ`** | ✅ **NEW** |
> | Algebra `A` | ❌ round110's `ℂ⊕ℂ` was a toy |
> | Real structure `J` | ❌ C35: pointwise only |
> | Physical interpretation | ❌ **why two copies at all** |
>
> **Cheapest remaining field: the algebra `A`** — first-order, orientability and
> Poincaré duality are all defined relative to it, so it gates three checks at
> once. See `experiments/20260810-c11-block-construction/decision.md`.
>
> **⚠️ NARROWED 2026-08-10 (C42) — and this blocker's ORIGINAL NAME was right.**
> The one-operator escape is closed: **no member of the Cartan–Schouten family
> has a 4-dimensional kernel** [VERIFIED-sympy]. Solving round67's closed form
> exactly, `n=0,σ=+1` vanishes at `t=0` and `n=0,σ=−1` at `t=1`, and **no `t`
> zeroes two levels at once** — structurally, because the torsion shift
> `(t−½)·h_H` is the *same for every level* while the levels are separated by
> `2σ(n+3/2)`. A uniform shift cannot zero two distinct levels.
>
> So "both `t` are realized" **cannot** mean one operator with a bigger kernel.
> Since C27 and C25 both reduce to C11 (C38/C39), and C11's only alternative
> reading is now gone, **the question this section's title already asks is the
> whole remaining question.**
>
> Not incoherent from the kernel side, though: the two sectors are **independent
> subspaces of one section space** — `dim(V₀+V₁) = 4`, `dim(V₀∩V₁) = 0`
> [VERIFIED-numpy, negative control passing]. They are not rival descriptions of
> the same states.
>
> **Constraints the two-operator construction must now satisfy are already on
> record, not hypothetical:** C35 showed the grading **cannot** exist for the toy
> `D` (non-symmetric spectrum) and that `J` exists only pointwise. See
> `experiments/20260810-c11-first-cut/decision.md`.

> **CORRECTION 2026-08-09 (external audit).** The 2026-08-03 entry below
> claims an "internal Z2 exchange symmetry". That is **too strong** — it is
> **pointwise orbit equivalence**. The construction built `S_n = m̂·σ` with
> `m̂` depending on `n`; a symmetry needs one fixed operator for all `T`. No
> single global unitary exists (exhaustive Pauli search + 40 000 random
> unitaries, both empty; structurally, `T(n)→T(−n)` is `R = −I₃`, `det = −1`,
> outside `SO(3)`). The original code also silently patched two charts via a
> `|n_z| < 0.9` case split — the hairy-ball obstruction, unnamed.
>
> **UPGRADE, not just a demotion:** the genuine global operator is
> **antiunitary**, `Θ = i·σ₂·K`, with `Θ T Θ⁻¹ = 1−T` everywhere and
> `Θ² = −I` (negative control: `i·σ₁` correctly rejected). ~~This **fills the
> "real structure `J`" field**~~ **← RETRACTED 2026-08-10, see below.** It does
> **explain** the recorded grading failure: the exchange is order-two on the
> projector space but lifts *projectively* to spinors, so a linear `Z₂` grading
> was the wrong object. See
> `experiments/20260809-ob2-antiunitary-correction/decision.md`.
>
> **⚠️ CORRECTION 2026-08-10 (C35) — `Θ` does NOT fill the `J` field.** The
> claim above was written as a plausible next step and is false. `Θ` was built
> to satisfy `Θ T Θ⁻¹ = 1−T` — it **exchanges** the algebra's two minimal
> projectors — while a real structure must satisfy the **order-zero axiom**
> `[a, J b* J⁻¹] = 0`, i.e. **commute** with the algebra. An operator built to
> exchange `A`'s generators cannot commute with them. Verified: `Θ` lifted as
> `(iσ₂)⊗I₂` is a valid `J` at **0 of 12** Bloch points. `Θ` is a symmetry *of*
> the algebra; `J` is *spectral data*. **The checklist field below stays
> `NOT ATTEMPTED`.**
>
> Three further facts about the toy triple, from the same round:
> - **No grading `γ` can exist** — `spec(D) = {0,0,3,3}` is not symmetric under
>   `λ→−λ` while `{γ,D}=0` requires it. Stronger than "the naive `γ` failed":
>   *none exists*. The triple is necessarily **odd**, and the `D`-sign is
>   **forced** to `+1` before any search.
> - **`J` exists pointwise (12/12, forced tuple `(J²,JDJ⁻¹/D)=(+1,+1)`) but
>   never globally** — blocked by the *same determinant obstruction* as `Θ`:
>   `J` is antilinear, so `T ↦ JTJ⁻¹` is a reflection (`det=−1`) composed with
>   a rotation (`det=+1`), and the composite can never be the identity a global
>   `J` needs. One obstruction, two casualties.
> - **The first-order condition is vacuous** — `D = 3(T⊗I₂)` lies *inside*
>   `A = span{T,1−T}⊗I₂`, so `[D,a]=0` identically and `Ω¹ = 0`.
>
> See `experiments/20260810-ob2-theta-ncg-axioms/decision.md` (C35).
>
> Still open regardless: the physical action (`F6`); orientability and Poincaré
> duality; and whether a `D` that does **not** commute with `A` would give the
> axiom checks any content at all. Original text preserved below.

**Codex's item 5 now attempted — genuine partial progress, not full
resolution.** Round110's own attempt tested the WRONG question (literal
self-invariance of `D_block` under a fixed swap — correctly found
`False`, but that's not the Z2 statement Codex's proposal actually
describes). Promoted `t` to a general rank-1 Hermitian projector `T`
(Bloch-sphere parametrized, not restricted to the diagonal `T=diag(0,1)`
case) and confirmed the CORRECT Z2 statement holds: `D(T)=T⊗H` and
`D(1-T)` are unitarily equivalent via an internal `SU(2)` conjugation
`S_n=m̂·σ` (`m̂⊥n̂`), verified exactly for the diagonal case and via a
numeric spot-check (8 random Bloch-sphere points, residual ~1e-16) for
the general case — realizing Codex's own "off-diagonal fluctuations
possible" language. See
`experiments/20260803-ob2-t-matrix-order-parameter-z2/decision.md`.
**Still open per `PARENT_ACTION_GATE.md`'s 6-field OB2 checklist:** a
naive grading candidate (`γ=(I-2T)⊗I₂`) explicitly FAILS `{γ,D}=0`
(reported honestly, not smoothed over); real structure `J` not
attempted; the physical action (F6) remains entirely unaddressed, as
Codex's own text already flagged.

**Original description (superseded framing, kept for history):**
round103 found this genuinely unresolved, not closed. `t`
indexes the spin connection, a spectral-triple geometric datum; a
block-diagonal `D=diag(D^0,D^1)` construction (round110's toy) is a
legitimate NCG move per round105's cross-model audit, but nothing yet shows
it corresponds to an actual physical S³×S⁶ construction with a first-order
condition, correct off-diagonal terms, or spectral-action coefficients.

**What would resolve it:** either (a) a properly specified non-product
spectral triple that satisfies the standard NCG axiom checklist (only
partially checked so far, round110), or (b) an argument that the product
ansatz genuinely cannot be left this way, closing the route negatively.

**Owner / next step:** grading and real structure remain genuinely open
(see 2026-08-03 update above); the physical action (F6) is the harder,
still fully open task. **Any future attempt: check against
`PARENT_ACTION_GATE.md` first** (6 additional fields for a non-product
spectral triple — algebra, Hilbert space, Dirac operator, grading, real
structure, physical interpretation — now 3 of 6 supplied, 1 attempted-
and-failed, 1 not attempted, 1 stated as interpretation).

---

## OB3 — B-L operator on the twisted kernel [CORRECTED + FORMALIZED 2026-07-17]

**This entry's own original text was WRONG, not just incomplete — flagged
honestly, not smoothed over.** It claimed "no construction of B-L directly
on the twisted kernel exists." This is false: **round94 (E24), already
committed BEFORE this Phase 0 registry was written, constructs exactly
that** — `BL_64 = leibniz64(BmL)` on the 64-dim twisted `Σ⊗Σ` fibre, with
the physical kernel vector `k` confirmed an exact `BL_64` eigenvector,
`B-L=0`. The multi-lens exercise this entry originally referenced was run
BEFORE round94's own result was cross-checked against it, and the
resulting stale framing was carried into this registry without re-verifying
against round94's own decision.md at write time — an audit-verification-
gate lapse in this registry's own construction, corrected here.

**Now formalized:** `BL_TWISTED_KERNEL_CANONICAL_STATEMENT.md`
(`tom_s3_spinor_toy/`) consolidates round94+round107+G98+round61 into one
canonical statement with 5 explicit scope constraints (the specific lifted
operator, the specific zero mode, confirmed-but-irrelevant non-
commutativity with `D_full`, B-L as a constructed not physically-derived
label, and the mode being a genuine `SU(4)` singlet not Pati-Salam matter).
**Nothing new computed** — pure consolidation of already-adjudicated
results, correcting this registry's own error in the process.

**Residual genuinely open items** (per the canonical statement's own "what
this does NOT mean"): whether the physical zero mode should be interpreted
as one particle in a tensor-product bundle vs. a different physical
identification of the two `Σ` factors (round94's own Relaxation Map, still
open); and `B-L`'s own non-uniqueness among a `dim≥3` admissible family
(round61) — no additional physical principle singles it out.

---

## OB4 — C_G67C3: the third triality channel (8_v) is a model postulate, not derived [UPDATED 2026-07-19, round128 + boyko-agent disposition review]

> **⚠️ 2026-08-10 — THE QUESTION QUEUED FOR TOM IS STALE. Re-ground before spending the contact.**
> The pearl standing at `next_check: at next Tom contact` was written **2026-07-05**
> and asks *"does Tom's framework carry an independent fiber Spin(8)?"* — rounds
> 119-128 moved that target. Gate 1 is CLOSED (two independent routes + a verified
> `ℂ⊗8_v ≅ Σ`), so the live question is narrower: does the rank-4 structure act
> **globally on the compactification**, and does the Dirac operator survive the
> `G₂`-breaking both candidates require? Four worlds (two of them — a `Φ`-background,
> and *three generations as an input rather than an output* — **not** in the original
> pearl) are recorded **before** the reply in
> `experiments/20260810-consortium-ob4-third-channel/predictions_before_data.md`.
>
> **Historical framing (external, verified) — STRUCTURAL RELATIVE, not identity
> [CORRECTED 2026-08-10, same day].** Witten 1981 + Atiyah–Hirzebruch: the
> character-valued index of the Dirac operator **vanishes on any manifold with a
> continuous symmetry group** [VERIFIED-WebSearch]. This *rhymes* with the local
> tension here — the `G₂` that makes G74A Lemma B work is the same continuous
> symmetry that obstructs chirality.
>
> **It was first written here as "the same tension, not an analogy". That was an
> overclaim and is withdrawn.** Establishing identity would require showing this
> setup satisfies the hypotheses of the relevant index theorem — and it plainly
> may not: the operator here is **twisted** (`D_{S⁶} ⊗ S⁻`), and twisting by a
> non-trivial bundle is precisely the *standard escape* from Witten's no-go. So
> the theorem quite possibly does **not** apply, and the resemblance is a
> structural relative until someone checks the hypotheses. Treat it as a source
> of candidate escape routes, never as a derivation.
>
> **Precedent for exactly this failure mode in this project:** round114's
> AHL2023 "cross-check" was FALSIFIED because the computation collapsed to
> restating the source's own theorem. A literature parallel is not evidence
> until its hypotheses are checked against the local setup.
>
> **What survives, and is genuinely useful:** the historical escape routes are
> real and two of the four are already present here under other names —
> **metric connections with topologically non-trivial torsion** (the `t`-family)
> and **orbifold projections** (C27's open Relaxation Map row).
>
> **That test has now been RUN (C40), and the answer goes the WRONG WAY.** Lemma B
> is a singlet count, so under `G₂ → H` the bound becomes an `H`-singlet count —
> a computable joint-kernel dimension. [VERIFIED-numpy, reusing G102's own
> generators] `g₂`-singlets in `𝕆` = 1 vs `su(3)`-singlets = 2; in the `7`,
> 0 vs 1. G74A's "does not degrade *gradually*" is right — the degradation is
> **discrete** — but it is **not unknowable**, and it is **+1 singlet**, which
> turns `dim ker ≤ 1` into `dim ker ≤ 2`. So the `G₂`-breaking both rank-4
> candidates require does not merely make Lemma B's argument inapplicable: it
> **quantifiably costs the uniqueness** that `N_gen=3` per channel rests on.
> **This blocker is NOT dissolved — it is made precise.**
>
> **Next, and now a finite computation rather than a wait:** the relevant `H` for
> the actual candidates is `g₂ ∩ (candidate)` — round125's non-generic 3-dim
> abelian `u(1)³`. If its singlet count is also 1, the candidates survive Lemma B
> and the blocker genuinely narrows; if larger, they need an independent
> exclusion argument. See `experiments/20260810-lemmab-quantitative/decision.md`.

**Disposition, made explicit (2026-07-19):** this OB conflates two
sub-branches with different correct status — splitting them out, per
`boyko-agent`'s go/no-go review of the whole line:

- **Gate 1 (algebraic distinguishability of `8_v/8_s/8_c`) — DONE.** Two
  structurally independent routes reach it (`SO(4)×SO(4)` block-chirality,
  round119; `su(3)⊕u(1)⊕u(1)`, round124, `Hom=0` for all three off-diagonal
  pairs). Round127→128 went further and constructed + verified (machine
  precision, `iso_residual~1e-15`, exhaustive over all 12 members of
  `Aut(su(3))`) an explicit isomorphism `ℂ⊗8_v ≅ Σ`. This is a completed
  **positive** result, not open work — do not re-list it under "open."
- **Gates 2-6 (physical realization) — formally `PARKED`, not open-in-
  progress and NOT `REJECT`/falsified.** Per this project's own Substrate
  Gate (`falsification-ladder.md`: "test could not run ≠ claim failed"),
  a block on unpublished external input (Tom Lawrence's Part 5, which the
  project's own hard constraint forbids soliciting) must never be recorded
  as evidence against the claim. Revival condition: Part 5's actual
  content, or an independent `G₂`-breaking-compatible spectral-gap argument
  (none currently exists). Directly precedented by OB1/KT-8's own park
  decision ("not falsified, just not found — reopen only on new external
  input").
- **B-L physical-identification sub-thread — near-closed.** round126
  (`NO_INDEPENDENT_EVIDENCE`, tautology) + round128 (`NO_LITERAL_MATCH` for
  the first of 12 `Aut(su(3))` candidates) leave one live kill criterion
  (`S_NOT_UNIQUE_UP_TO_SCALE`, only 1/12 checked) — see round128's own
  decision.md Relaxation Map for the cheap follow-up.

Original 2026-07-18 entry preserved below for the detailed derivation
history.


**What's open, current status (`GATE 1 OF 7 DONE / GATES 2-6 OPEN`, per
`TRIALITY_DISTINGUISHABILITY_GATE.md`):** G102 found no fiber symmetry inside
`so(8)` alone large enough for a Spin(8)-Schur argument to coexist with the
S⁶ geometry. But `L3B_SPIN8_INTERFACE_SPEC.md`'s own later work (same day,
2026-07-15) found a genuine advance beyond that: the `SO(4)×SO(4)`
block-chirality construction **algebraically distinguishes all three
channels** (`8_v,8_s,8_c`, not just `v` from `{s,c}`) and is itself
triality-invariant — a rank-4 structure that categorically escapes the
rank-3 `SO(7)` ceiling every earlier candidate hit. This is genuinely more
than "no candidate found" — it is "an algebraic candidate exists; its
physical realization does not." What remains a **model postulate** for Tom
Lawrence's specific framework is narrower than before: whether `SO(4)×SO(4)`
(or an equivalent structure) acts *globally* on the actual compactification
(not just the fiber), and whether the physical Dirac operator is consistent
with it once `G₂` is broken (mandatory for this route) — both explicitly
named "the blocker, needs Part 5" in the source document itself.

**What would resolve it:** Part 5's actual content (unpublished, not
solicited per this project's standing constraint), or an independent
`G₂`-breaking-compatible spectral-gap argument (no such tool currently
exists — this project's own G74A Lemma B explicitly requires exact `G₂`
symmetry and does not degrade gradually).

**Second, independent candidate found (round124, 2026-07-18):**
`su(3)⊕u(1)⊕u(1)` — `su(3)` combined with its own 2-dim abelian
centralizer in `so(8)` (already computed by G102) — gives `Hom=0` for
*all three* off-diagonal channel pairs (direct Schur-lemma non-
isomorphism, arguably cleaner than `SO(4)×SO(4)`'s explicit chirality-
matching argument) and fixes zero vectors in `8_v` (also escapes `SO(7)`
confinement). Verified tool-side, including basis-rotation invariance.
**Same remaining obstruction, not a further advance:** this candidate is
also outside `g₂` (which has zero center, hence no room for an abelian
ideal commuting with its own `su(3)`), so it requires the identical
`G₂`-breaking and hits the identical G74A Lemma B obstruction. Two
independent, structurally different candidates now both reach Gate 1 —
strengthens confidence Gate 1 is robust, does not touch Gates 2-6.

**Are the two candidates secretly the same structure? Checked, answer no
(round125, 2026-07-18):** `SO(4)×SO(4)` (12-dim) and `su(3)⊕u(1)⊕u(1)`
(10-dim), both as subspaces of `so(8)`'s 8-dim vector representation,
share an exact 3-dimensional intersection (two independent SVD methods
agree, tolerance-swept 1e-4 to 1e-12, skeptic-reviewed CONFIRMED). The
shared 3-dim subalgebra is abelian (`u(1)³`, all pairwise commutators
zero to ~1e-15) — genuinely non-generic (generic expectation for a 12-dim
and 10-dim subspace of a 28-dim ambient is exactly 0, not "small"), but
**not** the same structure: `PARTIAL_OVERLAP`, neither identical nor one
containing the other. Does not touch Gates 2-6; does not identify the
shared `u(1)³` with any known physical charge. See
`experiments/20260718-round125-so4xso4-vs-su3-centralizer-comparison/decision.md`.

**Owner / next step:** genuinely blocked without new input; flagged as one of
the two irreducible open premises in `DERIVATION_GRAPH.yaml`'s D2 chain. See
`TRIALITY_DISTINGUISHABILITY_GATE.md` for the full gate application,
`experiments/20260717-round119-triality-distinguishability-gate/decision.md`
for the skeptic-reviewed correction history, and
`experiments/20260718-round124-su3-centralizer-triality-candidate/decision.md`
for the second candidate.

---

## OB5 — Public-wording consistency check [RESOLVED 2026-07-17]

**Re-verified directly** (grep + read, `README.md`, `tom_s3_spinor_toy/README.md`,
`tom_s3_spinor_toy/preprint.tex`, `tom_s3_spinor_toy/preprint_abstract.md`)
against the exact June 25 `CLAIM_BOUNDARY_AUDIT` findings:

- **HIGH-1 (author-line "in collaboration with Tom Lawrence")** —
  **FIXED.** `preprint.tex`'s current author block (line ~55-58) reads only
  "Sergey Boyko, Independent researcher, Ronin Institute for Independent
  Scholarship" — no co-authorship/collaboration claim at the author level.
  `tom_s3_spinor_toy/README.md`'s own Attribution section (line 341-344) is
  unambiguous: "Developed independently by Sergey Boyko... All errors and
  interpretations are entirely my own," plus an explicit "**This is NOT:**...
  Endorsed by Tom Lawrence or affiliated with his research group" fence
  (line 337).
- **HIGH-2 (N_gen=3 stated as unconditional/derived)** — **FIXED** in every
  file checked. Root `README.md`'s own Verdict line (line 23) and
  `tom_s3_spinor_toy/README.md`'s top-of-file correction (lines 11-42)
  both carry the full KT-8 caveat. Every later "N_gen=3" restatement in
  `tom_s3_spinor_toy/README.md` (lines 85, 144, 236 — inside the
  Three-Generation Investigation section) sits under an explicit blanket
  override (line 39-42: "This status correction is authoritative... over any
  'N_gen=3' statement elsewhere in this file that does not carry this same
  caveat") — a deliberate, honest design choice rather than an oversight.
  `preprint.tex`'s own abstract (lines 70-77) states the full-operator
  zero-mode gap caveat inline, in the abstract itself, not just in a later
  section.
- **Residual, minor (not a HIGH-1 violation, but adjacent language worth
  naming):** `preprint.tex:434` and `:1294` still use the phrase
  "collaboration with T. Lawrence" / "to be addressed in collaboration with
  T. Lawrence" to describe an open question awaiting his input. This is
  materially weaker than the original HIGH-1 finding (no co-authorship
  implied, correctly scoped to "his expertise would resolve this"), but given
  the project's own hard "DO NOT INITIATE CONTACT" fence and that no
  confirmed collaboration exists, the word "collaboration" itself is
  slightly more definite than warranted — a candidate one-word wording fix
  ("input from" or "clarification from" rather than "collaboration with"),
  not urgent, not a fence violation.

**Verdict: substantially resolved.** No overclaim found beyond the one
minor wording item above.

---

## OB6 — Codex items 5 and 8 (item 8 re-scoped 2026-07-17; not yet well-posed)

**What's open:**
- **Item 5 [UPDATED 2026-08-10, consolidation pass — grading and real
  structure now extensively closed, physical action genuinely still open]:**
  promote `t` to a finite matrix-valued order parameter with internal Z2
  exchange symmetry — the Z2 exchange itself is verified (unitary
  equivalence of `D(T)` and `D(1-T)`). Of the three originally-open pieces:
  **grading** (`γ`) — closed by the C41-C60 chain (C50/C51/C53/C57/C60
  exhaust the admissible `γ`-compatible structures for the doubled
  construction). **Real structure** (`J`) — closed by the same chain
  (C55/C56/C57/C59/C60 pin `J`'s admissible forms exactly, up to the
  proven-irreducible KO-2/KO-4 choice). **Physical action** — genuinely
  untouched by C41-C60 (a different kind of question — deriving an actual
  Lagrangian/spectral-action functional, never attempted in that chain) and
  remains open. Given C49/C52 already show the doubled construction is not
  a valid geometry regardless, pursuing the physical action for THIS
  specific construction would not be a productive use of effort.
- **Item 8 — re-scoped, NOT ready-to-run as originally logged:** Codex's
  exact wording (`codex_review_2026-07-17.md:172-174`) is "If the actual
  gauge group is `SO(6)`, `Spin(6)`, or a quotient of
  `SU(4)×SU(2)_L×SU(2)_R`, global anomalies and permitted representations
  depend on that quotient... The precise global group should be derived
  after the spin lift rather than assumed." **This presupposes `SU(4)` is
  realized as an actual local gauge symmetry of the construction** — but
  gate G97's closure (rounds 102/108/109, `CLAIM_LEDGER.yaml` `C7`) already
  established it is **not**, within the standard `S³×S⁶` product-manifold
  framework (only `su(3)⊕u(1)`, 9/15 generators, is geometrically realized;
  the full `su(4)` doesn't preserve `B-L`, gate G98). Item 8's question is
  therefore contingent on round103's still-open non-product-ansatz fork
  (`C11_D4_PRODUCT_ANSATZ_FORK`) actually succeeding first — attempting it
  now, against the current closed-G97 state, risks the same
  answering-the-wrong-question trap round102's and round103's first drafts
  fell into (see `SUPERSEDED_RESULTS.md` SR4). Surfaced this scoping issue
  during a 2026-07-17 re-read of Codex's exact wording, before starting a
  round — not attempted, deliberately, rather than forced through a shaky
  premise.

**Owner / next step:** item 5 remains ready whenever OB2 is picked up. Item
8 should be re-attempted only after (or explicitly conditional on) OB2/C11
progress — re-read Codex's wording again at that point to confirm the
premise then holds, rather than assuming this note's conclusion is still
current.

---

## OB7 — round111 uncommitted [RESOLVED 2026-07-17]

~~What's open: round111 + the Phase 0 deliverable set written but not
committed.~~ **Resolved:** committed (`6e7c5ac`), merged (`bd4363f`), and
pushed to `origin/main` on 2026-07-17, same day. Kept here (struck through,
not deleted) so anyone reading this file's history sees the item was real
and closed, not silently dropped — matches this registry's own purpose of
tracking status changes honestly (see `SUPERSEDED_RESULTS.md` for the
general pattern this follows).

---

## OB8 — round96's mixed-Y anomaly sweep is incomplete: two channels never computed [RESOLVED 2026-07-17]

~~What's open: round96 only computed three of five mixed-anomaly
conditions...~~ **Resolved by round112 (E26):** computed
`[SU(2)_L]²U(1)_Y` and `[SU(2)_R]²U(1)_Y` for both `t=0,1` endpoints —
both vanish identically at both endpoints and in union
(`FAIL__BOTH_REMAINING_CONDITIONS_COMPUTABLE_NONE_SHOW_FORCING__EXTENDS_ROUND96`).
SM sanity check confirms the formula itself is correctly stated.

**Important scope correction, per mandatory skeptic review (kept, not
smoothed over):** the skeptic found this closure carries **far less
discriminating power** than it first appears — each of the four zeros
(this round's two + it retroactively applies to round96's three at `t=1`)
traces to `U(1)_Y` being either identically zero or degenerate with an
internal `SU(2)` Cartan generator at the relevant endpoint, **given the
current frozen inputs** (round94's `B-L=0` specifically) — not to a
nontrivial cancellation between competing, independently-charged states.
Sharpened conclusion: at `t=1`, `Y≡0` identically, so **every** mixed-`U(1)_Y`
anomaly condition (all 5, not just these 2) is forced to zero there for one
shared structural reason, not five separate confirmations. Round100's
"anomaly route exhausted" framing must still **not** be broadened beyond the
mixed-`U(1)_Y` class — cubic non-abelian channels (`[SU(2)_L]³`, `[SU(2)_R]³`)
remain a genuinely untested class.

**Full detail:** `tom_s3_spinor_toy/experiments/20260717-round112-remaining-mixed-y-anomaly-channels/decision.md`.

**New, smaller follow-up surfaced by this closure (not logged as its own
OB — low priority):** a cleaner test of the code's own discriminating power
would use an adversarial input (`B-L≠0` at one endpoint) to confirm the
formula would actually flag forcing if present, since the current FAIL
can't distinguish "no forcing exists" from "the inputs make forcing
undetectable by construction" — a Validation-Theater-Guard-style concern,
not required to accept this closure but worth naming.

**Original description (superseded, kept for history):** round96 only
computed three mixed-anomaly conditions — `[SU(3)_c]²U(1)_Y`, `[U(1)_Y]³`,
`[grav]²U(1)_Y` — for both `t=0,1` endpoints; `[SU(2)_L]²U(1)_Y` and
`[SU(2)_R]²U(1)_Y` were never computed, in round96 or round92.

**Source:** `tom_s3_spinor_toy/experiments/20260717-round96-mixedY-anomaly-with-bl0/decision.md`;
`tom_s3_spinor_toy/experiments/20260717-round112-remaining-mixed-y-anomaly-channels/decision.md`
(correction note, top of file); `CLAIM_LEDGER.yaml` entry `C10_MIXED_Y_ANOMALY_FAIL`
(already scoped correctly to "three conditions," not "all").

---

## OB9 — E7-E13 chain deserves its own Phase-0-style consolidation pass [RESOLVED 2026-07-19]

~~What's open: while fixing round80/E14's registry omission
(`SUPERSEDED_RESULTS.md` SR7), confirmed that the whole preceding chain —
round72 (E7, t-selection principle), round73 (E9, explicit parallel
spinor), round74 (E10, chirality sign link), round75 (E11, Freund-Rubin
torsion link), round78 (E12, multiplicity gate) — is committed to git
(`92e5fb2`) but not individually represented in `CLAIM_LEDGER.yaml` or
`DERIVATION_GRAPH.yaml`.~~

**Resolved:** read rounds 72-78 in full (`decision.md` for each), added 6
new `CLAIM_LEDGER.yaml` entries (`C22`-`C27`, covering H1a/REFUTED,
H1b/PROVED-with-sign-caveat, the sign-convention gap itself, H1c/OPEN, the
SU(2)_L/R representation pattern, and the multiplicity-2 FAIL) and one new
`DERIVATION_GRAPH.yaml` chain (`D4_TORSION_ESCAPE_ROUTE_MULTIPLICITY_
BLOCKED`), cross-checked against round80/E14's own Z2-symmetry finding for
consistency — the iota isometry strengthens E7's algebraic `t<->1-t`
symmetry to a genuine geometric diffeomorphism but does not resolve H1c.

**Headline synthesis (new, from this consolidation, not previously stated
anywhere as a single claim):** the torsion-escape-route program has TWO
independent, currently unresolved blockers, not one — (1) H1c (which of
`t=0`/`t=1` is physically selected, C25, OPEN) and (2) the multiplicity-2
gap (C27, REFUTED as stated — even a selected `t=0` or `t=1` zero mode is
2-dimensional, giving 6 total internal modes across 3 triality channels,
not the needed 3). Resolving (1) alone would NOT complete the program;
(2) is a logically separate problem requiring new physical input (a
reality/Majorana condition, an orbifold projection, or a reconciliation
with `preprint.tex`'s own 32-state SO(4)-spinor convention — none of
which exist in this project yet).
**Update 2026-08-10 (C33):** the first of those three — a reality/Majorana
condition — is now positively CLOSED, not merely absent. Two remain. See
the OB10 section below for the full C31→C32→C33 correction chain.

**Prompted by:** external correspondence with Tom Lawrence (2026-07,
message batch referencing his own independent harmonics-on-S³/chirality/
Dirac-to-Weyl-massless-reduction analysis) — this consolidation exists so
a future technical exchange can cite the project's own established
results precisely rather than re-deriving them under time pressure.

---

## OB10 — geometric spinor bundle's own reality/Majorana condition [RESOLVED 2026-08-03, CORRECTED 2026-08-09, CORRECTION NARROWED 2026-08-10]

> **⚠️ CORRECTION 2026-08-09 — read this before anything below.** The
> 2026-08-03 resolution reached the WRONG ANSWER. It concluded the bundle is
> PSEUDO-REAL from a mixed `Cl(6,3)` signature; both were artifacts of gluing
> two sub-projects with OPPOSITE Clifford sign conventions (S³/round67 uses
> `Cl(0,3)`; S⁶/s6-harm-g0 uses `Cl(6,0)`), which OB10 was the first round
> ever to combine. S³×S⁶ is a 9-dim RIEMANNIAN product and needs ONE uniform
> convention. Under uniform `Cl(0,9)`: signature `(0,9)`, unique
> `B = σ₂⊗σ₁⊗σ₂⊗σ₁`, `B·conj(B) = +I` → **REAL**, independently matching
> `Spin(9)`'s `Δ₉ = ℝ¹⁶` (`9 mod 8 = 1`).
>
> **Downstream — SUPERSEDED 2026-08-10, see the next block.** This originally
> read: "C31's 'Majorana branch CLOSED' is INVERTED — that row of C27's
> Relaxation Map is OPEN and is now a live candidate mechanism." The first
> half stands (C31's *reasoning* was wrong); the second half does not.
>
> **⚠️ NARROWING 2026-08-10 (C33) — the correction above over-corrected.**
> The 16-real-dimensional Majorana solution space is a fact about the 16-dim
> **module**. C27 is about the **zero mode**,
> `ker(D_S³) ⊗ ker(D_S⁶,twisted) = ℂ² ⊗ (1-dim)`. The module's reality is a
> product of TWO quaternionic factors (`B_S³ conj(B_S³) = −I` and
> `B_S⁶ conj(B_S⁶) = −I`, so `(−1)(−1) = +1`); restricting to the zero mode
> collapses the S⁶ factor to a **scalar**, which cannot supply the second
> minus sign. The induced structure is quaternionic again → **no Majorana
> condition on the zero mode, solution dimension 0** (verified over nine λ;
> negative control returns 2). **That row of C27's Relaxation Map is CLOSED
> after all** — C31's conclusion survives, its reasoning does not. Net effect
> of the whole OB10 episode on C27: **zero**. See
> `experiments/20260810-majorana-vs-multiplicity2/decision.md` (C33).
>
> **What OB10 genuinely found:** a real latent inconsistency — two
> long-standing sub-projects carrying incompatible Clifford conventions.
> Correct finding, misread as geometry instead of as a codebase fact. Any
> future round tensoring S³ and S⁶ constructions hits the same trap.
>
> **AUDITED REPO-WIDE 2026-08-10 (C34).** 370 `.py` files scanned by asserted
> anticommutator sign: **no second instance of the mixing exists** — OB10's own
> two files are the only ones that ever combine the conventions, and **zero**
> cross-directory import edges cross the boundary. The audit did find a
> distinct, systematic **label** inversion (the octonion sub-project names its
> `e²=−1` generators `Cl(7,0)`; `g69` hardcodes `Cl(6,0) ≅ M₈(ℝ)`, which is
> `Cl(0,6)`'s isomorphism) — naming only, no result affected, and `g101`/`g102`
> already write the correct `Cl(0,7)`/`Cl(0,8)` for the same object.
> **Canonical reference now exists: `docs/clifford_convention_registry.md`** —
> read it before tensoring or labelling any Clifford construction. See
> `experiments/20260810-clifford-convention-repo-audit/decision.md`.
>
> Found by an EXTERNAL audit, not internally: the error survived this
> experiment's own checks, a ledger entry, a `decision.md` with an explicit
> "what this does NOT mean" section, and a merge. See
> `experiments/20260809-ob10-convention-correction/decision.md` (C32).
>
> Original 2026-08-03 text preserved below for the record.

**Resolved:** built the 16-dim product Clifford module from this repo's own
already-established S³ (`Cl(0,3)`, round67) and S⁶ (`Cl(6,0)`, s6-harm-g0/G13)
generators, per preprint.tex:1467-1480's own stated tensor-product formula.
Found the product signature is actually **mixed, `Cl(6,3)`** (not the uniform
`Cl(9,0)`/`Cl(0,9)` the "3+6=9≡1 mod 8" text below implicitly assumed — the
two established sub-constructions use opposite Clifford sign conventions).
Despite that correction, a direct, adversarially-widened search (256
candidates, `{I,σ1,σ2,σ3}⁴` factorized ansatz) found a unique, Hermitian,
unitary charge-conjugation operator `B`, `B·conj(B)=-I` → **PSEUDOREAL
(quaternionic) type** — matching, not contradicting, the finite algebra's own
`J_F²=-1` (also pseudo-real) [BOTH HALVES WRONG, C32 + C36: OB10's own
pseudo-real verdict was a Clifford-convention artifact, AND `J_F²` is `+1`, not
`-1` — so this "corroboration" was void twice over]. No-collapse-checked
(reproduced under an
independent, equally-valid Clifford-factor ordering). See
`experiments/20260803-ob10-ko-dimension-majorana-check/decision.md`.

**What this does NOT mean:** does not check `[D_full,B]`/`{D_full,B}` against
the actual differential Dirac operator (only the algebraic Clifford-module
type was checked); does not construct a combined `J=B⊗J_F`; does not touch
OB1/OB2/OB4/OB11 or the `N_gen=3` headline (confirmed free-standing per
`GLOBAL_RECOMPOSITION_AUDIT.md`'s own C19 audit).

**Downstream consequence found 2026-08-06 (C31) — this result was NOT
free-standing after all, in one specific direction.** `B` factorizes exactly
as `B_{S³}⊗B_{S⁶}` with the S³ slot pseudo-real (`−I₂`) and the S⁶ slot real
(`+I₈`) — i.e. the pseudo-reality sits entirely in the S³ factor, which is
also exactly where C27's multiplicity-2 excess lives. That closes the
"new reality/Majorana condition" row of C27's Relaxation Map as a positive
no-go (exhaustive: no compatible REAL antilinear structure exists on that
factor at all). C27 itself remains unresolved. See
`experiments/20260806-ob10-c27-majorana-halving/decision.md`. Note this
does not contradict the C19 audit above, which correctly found OB10 does not
feed `D2`'s zero-mode COUNTING argument — the link found here is to C27's
option space, a different object.

> **Status of that 2026-08-06 paragraph, as of 2026-08-10 (C33):** its
> CONCLUSION (row closed) is right; its stated reason is not. Under the
> uniform convention the S⁶ slot is quaternionic too (`−I₈`, not `+I₈` —
> that `+I₈` was the convention artifact), so the closure does not come from
> "pseudo-reality sits entirely in the S³ factor". It comes from the S⁶
> factor collapsing to a **scalar** on a 1-dim kernel, leaving the S³
> quaternionic factor unopposed. Same verdict, different mechanism.

**Original description (superseded framing, kept for history):** the
finite/NCG algebra's real structure `J_F` is
established (`J_F²=`**`+1`**` [sign corrected 2026-08-10, C36 — this line said
`-1``], `{J_F,γ_F}=0`, `[D_F,J_F]=0`, `preprint.tex:349`).
> ⚠️ **`J_F² = −1` IS WRONG — 2026-08-10, C36.** G18's actual `J_F` is 16 real
> transpositions; loading it and squaring gives `J_F conj(J_F) = +I₃₂`, and
> `g18_ncg.py` itself **asserts** `J_F**2 == eye(32)` with its docstring saying
> `J_F² = I`. **The correct value is `+1`.** The `−1` propagated into
> `docs/gates_tracker.md:38`, `g18/decision.md:9`, `g26/claim.md` (×2), OB10's
> `claim.md` (×2) and `decision.md`, this file (×2), and **`preprint.tex:349,354`**.
> Consequence for OB10: its pseudo-real verdict was justified as "matching the
> finite algebra's own pseudo-real `J_F²=−1`" — wrong twice over, since C32
> already showed OB10's verdict was a convention artifact AND the value it was
> matched against is `+1`. **FIXED 2026-08-10** across all 11 documents
> including `preprint.tex` (which now also states that the KO-dimension
> *label* follows CCM rather than being independently derived — the three
> relations are what this project verifies). Manuscript **rebuilt** 2026-08-10
> (3 × `pdflatex`, exit 0, 0 errors, 0 unresolved citations, 30 pages). See
> `experiments/20260810-ob2-theta-ncg-axioms/decision.md` and
> `experiments/20260810-c36-jf-square-propagation-fix/decision.md`.
But whether the GEOMETRIC `S³×S⁶` spinor bundle itself — independent of
the separately-reconstructed finite algebra `A_F` — satisfies a
compatible reality/Majorana condition is **not addressed anywhere** in
`preprint.tex` or `experiments/`. Confirmed after a 12-term search
(`Killing spinor`, `KO-dimension`, `quaternionic`, `pseudo-real`,
`nearly-Kähler`, `parallel spinor`, `symplectic Majorana`,
`spectrum-symmetric`, and others) across both the paper and every
experiment file — the only hits found are about a DIFFERENT question
(`SU(2)` gauge-representation pseudo-reality, used for anomaly
cancellation; Killing-spinor existence/multiplicity arguments), not the
geometric spinor bundle's own reality-type classification.

**What would resolve it:** determine the KO-dimension of the GEOMETRIC
factor (`S³` has KO-dim 3, `S⁶` has KO-dim 6; product KO-dim would be
`3+6=9 ≡ 1 mod 8` — the quaternionic/symplectic-Majorana regime in the
standard 8-fold KO-periodicity table) and check whether this project's
own spinor bundle construction is consistent with that regime, or derive
the reality structure directly from the explicit Clifford/Pauli
realizations already used throughout rounds 67-117.

**Owner / next step:** surfaced during `SPIN13_TO_SPIN4_DECOMPOSITION.md`
(gauge/Hilbert/triality closure program, item 2 of that audit). Genuinely
new — not previously logged anywhere in this project's registries.

---

## OB11 — matter-generation tensor factorization: necessary condition verified, sufficiency open [PARTIAL, 2026-08-03; (ii) hard-half intertwiner FOUND 2026-08-11 (C70), Clifford-compatibility test still not attempted; (iii) partly confirmed 2026-08-10; (iii) hard half CLOSED EXHAUSTIVELY 2026-08-11 (C78) — see synthesis below, 2026-08-30]

> **SYNTHESIS 2026-08-30 — connects C78/C79 (2026-08-11) to C90-C111
> (2026-08-11 to 2026-08-30) and traces both to a single 2026-06-20 root
> cause (G44). Written in response to an external (ChatGPT-generated)
> proposal for a "triality bridge to N_gen=3" that substantially restated
> this OB's own already-closed ground; the cross-check that caught this is
> recorded here so it doesn't need repeating.**
>
> **CORRECTION, same session, 2026-08-30 (caught while responding to
> "continue C90-C111"):** point 3 below, as originally written, claimed
> "C90-C111 IS, structurally, that same non-product-coupling door." This
> is WRONG, verified by directly reading `experiments/20260812-c90-
> selection-rule-structural-nogo/decision.md` and `experiments/20260811-
> ngen3-decisive-program/predictions_before_data.md`'s own C90 entry:
> C90-C111 is entirely INTERNAL to the S³ factor -- a multiplication-
> operator construction connecting S³'s own Peter-Weyl LEVELS (k=1, k=2,
> k=3...), with no S⁶ or triality content whatsoever. Its own predictions
> log states explicitly, on every entry: "Outside the closed P1-P5
> program; does not change N_gen=3's CONDITIONAL status." C78/C79's
> "non-product D" is a categorically different object -- an operator
> entangling the S³-FRAME index with the S⁶-TRIALITY index across the two
> DIFFERENT factors of the product manifold. C90-C111 touches neither
> S⁶ nor triality; conflating the two was an error, not a finding. Point
> 3 (and the pearl_registry row it motivated) is corrected below/there.
> The rest of this synthesis (points 1, 2, 4) is unaffected -- C78's
> exhaustive closure, C79's non-product-postulate NULL, and G44's root
> cause all stand as originally written; only the claimed link to
> C90-C111 is retracted.
>
> **1. Condition (iii)'s "hard half" (state-level triality intertwiner,
> `T·D_v = D_s·T`) is now CLOSED, exhaustively, not just "still open."**
> `experiments/20260811-c78-exhaustive-so8-commutant-of-physical-D/decision.md`
> (verdict `EXHAUSTIVE_COMMUTANT_EQUALS_SU3_EXACTLY__DIM8`): the ENTIRE
> `so(8)` commutant of the physical `D` is exactly `su(3)`, dimension 8,
> proven via a single SVD of the full `4096×28` commutator map (rank 20,
> exactly 8 zero singular values, no near-zero stragglers). This is not one
> more failed candidate (C75/C77 tested two specific subalgebras and
> failed) — it is a proof that **no candidate subalgebra of `so(8)`,
> known or yet-to-be-proposed, can ever commute with the physical `D`**.
> Condition (iii) as an so(8)-Lie-algebra-symmetry question is closed.
>
> **2. C78 itself names the one remaining door: a structurally different,
> non-product `D`** (S³-frame index entangled with the S⁶-triality index
> at the operator level, not as a tensor product). **C79, the SAME day**
> (`experiments/20260811-c79-nonproduct-s3s6-coupling-attempt/decision.md`),
> already tried ONE specific, honestly-postulated non-product coupling
> (round119's `so(4)₁` self-dual triple + round67's `Z_i`, restricted to
> `S3`'s `n=0` `+`-branch) — clean NULL (the one apparent zero-mode
> crossing was fully explained as an artifact of `D_S6`'s own 36-dim raw
> kernel, unrelated to the physically-relevant 1-dim `su(3)`-invariant
> sector). Two valuable side-findings survived: C70's intertwiner `U_v` is
> **not unitary** (found, fixed, `T=(T_raw+T_raw^dagger)/2`), and C75/C77/
> C78's own conclusions are robust to `U_v`'s residual gauge freedom
> (checked with 4 independently-seeded valid `U_v` choices).
>
> **3. RETRACTED (see correction box above) — C90-C111 is NOT the same
> door as C78/C79.** C90-C111 (`experiments/20260811-ngen3-decisive-
> program/predictions_before_data.md`, run 2026-08-11 through 2026-08-30)
> is a self-contained investigation of S³'s own internal Peter-Weyl LEVEL
> structure (a multiplication operator connecting levels `k, k+1, k+2...`
> of `S³`'s representation theory) — it never involves `S⁶` or triality
> at all, and its own log states on every entry that it is "outside the
> closed P1-P5 program" and does not touch `N_gen=3`. The actual
> "non-product-`D` door" C78 names remains genuinely untouched since C79's
> single NULL attempt — not silently being worked by a differently-scoped
> investigation. No cross-check against C79's artifact diagnostic applies
> to C90-C111's own findings (they concern only `D_S3`'s level structure,
> not `D_S6`'s kernel at all); the pearl_registry row this point motivated
> has been corrected to not claim otherwise.
>
> **4. The root cause both (1) and the external proposal's topological
> variant trace back to is `G44` (2026-06-20,
> `experiments/20260620-g44-d4-triality/decision.md`, REJECT, 34/34
> tests, six weeks before C78/C79/C90 existed) — the oldest, and in
> hindsight the most load-bearing, negative result on this whole
> question.** G44's argument: `G₂` has NO 8-dimensional irreducible
> representation (only `{1,7}` up to dim 8, next is 14) — so ANY 8-dim
> `SO(8)` rep restricted to `G₂` decomposes uniquely as `7⊕1`, meaning
> `8_v|_{G₂} = 8_s|_{G₂} = 8_c|_{G₂}` are IDENTICAL, not just
> isomorphic-by-coincidence. G44's own conclusion, verbatim: **"S⁶ =
> G₂/SU(3) cannot distinguish the three reps → triality invisible."**
> This is the SAME branching identity the external proposal's Bridge A/D
> cites as a positive enabling fact (`8_v↓SU(3) = 8_s↓SU(3) = 8_c↓SU(3) =
> 3⊕3̄⊕1⊕1`, `SU(3)⊂G₂` so the `G₂`-level identity forces the `SU(3)`-level
> one too) — G44 already showed six weeks before C78 that this identity is
> the CAUSE of the collapse, not evidence a genuine distinguishing
> structure exists to build an intertwiner or a triality-summed
> topological invariant from. A 2026-08-30 novelty-check for a proposed
> "Bridge F'" (does triality act non-trivially on the canonical `G₂→S⁶`
> bundle's clutching map, summing three images to winding number 3 in
> `π₅(SU(3))`?) found it sits on the identical branching data G44 already
> showed collapses — assessed as high-risk-of-repeat, NOT built as a
> round. See `experiments/20260830-triality-bridge-program/PROGRAM_TZ.md`
> Part 1 for the full novelty-check trail (G32/G36/G40-B2/G41-B3/G43-B5/
> G48/G52 — the `π₅(SU(3))→π₅(G₂)→π₅(S⁶)` machinery this would have
> needed is already fully mapped in this project, going back to
> 2026-06-20).
>
> **Net effect on this OB's own status:** condition (iii)'s so(8)-algebra
> half is now CLOSED (item 1), not merely "confirmed 2026-08-10." The
> non-product-`D` door remains the only live path, still untouched beyond
> C79's single NULL attempt — **not** being worked by C90-C111, which is a
> genuinely separate, S³-internal investigation (see correction box
> above). No change to `N_gen=3`'s CONDITIONAL status.

> **UPDATE 2026-08-10 (C65), condition (ii) hard half, step 1 of a planned
> bridge.** A correction first: C61's own framing that `Hom_su3≠0` is
> "necessary, not sufficient" for a G2-invariant mixing term was imprecise
> — by Frobenius reciprocity for homogeneous vector bundles, a nonzero Hom
> space already suffices for *existence* of such a term; the real remaining
> question is whether a Hermitian, genuinely Clifford-compatible combined
> operator can be built (a materially different, harder question). Toward
> that: round59's real, already-PROVED Clifford construction (`Σ`, the one
> object in this project with an actual curvature-twisted Dirac operator,
> not an abstract stand-in) carries the **same `su(3)`-module** as the
> triality channels — Casimir spectrum exactly `2×0, 6×(-4/3)`, matching
> C29/C61's own channels precisely, not just qualitatively. This confirms
> (via general representation theory) that an explicit basis-alignment
> isomorphism between round59's presentation and G102's *exists* — finding
> it, and then testing the actual Clifford-compatibility question, is the
> next step, not yet attempted. See
> `experiments/20260810-ob11ii-round59-su3-bridge/decision.md`.
>
> **Attempted, BLOCKED-SUBSTRATE (same day, step 2):** tried to find the
> explicit isomorphism by directly reusing round128's Cartan-Weyl matching
> algorithm. Hit a genuine reality-type mismatch, not a bug: round59's
> `su(3)` (via `spin_lift`) is **complex, anti-Hermitian**; G102's (via
> `stabilizer_basis`, embedded in `so(8)`) is **real, antisymmetric** —
> round128's algorithm assumes a shared reality type between the two sides
> it aligns, which this pair doesn't satisfy. C65's finding (isomorphism
> exists) is untouched; this narrows only which *algorithm* applies.
> Needed next: either realify round59's representation or adapt the
> matching algorithm for a real/complex boundary — a genuine, non-trivial
> extension, not a quick fix. Parked here given the rest of the queue. See
> `experiments/20260810-ob11ii-round59-g102-explicit-isomorphism/decision.md`.
>
> **UPDATE 2026-08-11 (C68), directed follow-up to an external review of the
> above.** Dropped the real-coefficient constraint (the fix identified
> above) — **works**: complex CSA extraction now succeeds cleanly for both
> `su(3)` presentations, 6 genuine roots each, exact root-matching. The
> explicit intertwiner still isn't found, but a cheap control check (each
> side's `Hom_su3(V,V)` computed alone, no cross-matching at all — both
> give exactly `6`, as predicted) decisively rules out the shared machinery
> and either individual construction as the source of the remaining gap.
> **Localized precisely: the cross-construction correspondence pipeline
> itself** (root-matching → Cartan-generator transport → root-vector
> rescaling) gives a uniform, wrong `Hom_su3` dimension (`4`, not `6`)
> across all 48 candidate correspondences tried — most likely a
> directionality error in the Cartan-transport formula, the same step
> round128's own source comments flag as needing independent verification
> when first written for a different pair. Genuine progress in
> localization, not a resolution — narrower than before, not yet positive.
> See `experiments/20260811-ob11ii-complexification-bridge-test/decision.md`.
>
> **UPDATE 2026-08-11 (C69) — the "directionality error" hypothesis just
> above is REFUTED, same arc, by a ground-truth control.** The identical
> pipeline applied to G102-vs-G102 (self-match, two independent random-seed
> extractions) reaches the predicted `hom_dim=6` cleanly — the pipeline is
> correct, and the round59↔G102 obstruction is **real**, now sharply
> characterized: (a) the 4-dim cross-Hom is **exactly** the singlet↔singlet
> block — the `3⊕3̄` sectors contribute nothing under any correspondence;
> (b) wholesale conjugation (`3↔3̄` swap) doesn't help — still 4; (c)
> augmenting the fit with the `[E,E⁻]→Cartan` bracket relations (missing
> from round128's original fit, automatically consistent in self-matches)
> exposes a systematic ~2e-3 inconsistency across all 48 candidates × 20
> restarts — genuinely obstructed, not under-constrained. **Next
> single-variable suspect (identified, NOT yet tested):** round59's complex
> CSA makes `ad(H)` non-normal, and the root extraction reads roots off
> Rayleigh quotients — exact only for normal operators; G102's side IS
> normal, which is exactly why the self-test passes while the cross-match
> fails, and the hexagon check cannot detect this. C65's abstract existence
> guarantee remains untouched throughout. See
> `experiments/20260811-ob11ii-ground-truth-refutes-directionality-hypothesis/decision.md`.
>
> **UPDATE 2026-08-11 (C70) — condition (ii) hard half CLOSED. The
> intertwiner is found.** Superseding the C68/C69 Cartan-Weyl root-matching
> pipeline (shown genuinely obstructed by C69, not buggy) with an
> independent, pipeline-free method: a direct global nonlinear solve for
> the abstract Lie-algebra isomorphism `Phi: su(3)_r59 → su(3)_g102`
> converges to **machine precision** (`max_residual ~1e-14`-`1e-15`,
> `|det(Phi)|=1.0000`) on **15/15** random restarts. (A first, unconstrained
> version of this solve had collapsed to the trivial `Phi=0` sink — always
> an exact root of the quadratic-minus-linear bracket residual; a soft
> non-triviality constraint fixed this.) Given `Phi`, the actual target — the
> **representation-space intertwiner `U`** — was constructed and **verified
> explicitly**: `hom_dim=6` (matching C69's own ground-truth benchmark
> exactly, not the previously-stuck `4`), and direct re-verification
> `max_k ‖U·M_k·U⁻¹ − Xk_g102‖ = 3.8e-16` to `4.4e-16` across two independent
> runs. **Gate-3 controls both pass cleanly:** a positive control
> (`g102`-vs-`g102` self-match) reproduces the identical signature; a
> negative control (`r59` vs 8 random anti-Hermitian matrices with no
> genuine `su(3)` structure) fails by **13 orders of magnitude**
> (`max_residual` `0.17`-`0.27`, `det` collapses toward `~1e-6`) — the test
> genuinely discriminates. C69's identified non-normality suspect was
> independently retested and **REFUTED** (`ad(H)` commutator norm `3.0e-17`,
> eigenvector residual `1.1e-15` — round59's `ad(H)` IS normal). A
> basis-independent bracket-structure invariant also **matches** exactly
> (`24.0` both sides), ruling out any structure-constant scale mismatch.
> **Plausible but not independently confirmed diagnosis** for why
> root-matching missed this: fixed-weight CSA root extraction
> (`combo_weight=0.37123`) explores only one point in the CSA's continuous
> re-parametrization freedom, while the genuine isomorphism needed a
> continuous `Inn(su(3))` component (8-real-dimensional) the discrete
> Weyl×Out×real-mu search structurally cannot reach — this does NOT
> contradict C69's finding, it explains it. **Non-uniqueness is expected,
> not a defect:** `Inn(su(3))` acts transitively on the solution family, so
> the next round (transporting `D`, `J`, `γ`, `B-L` through `U`) must fix one
> representative and use it consistently. C65's existence guarantee is now
> fully cashed out into an explicit, verified intertwiner. See
> `experiments/20260811-c70-independent-bridge-fingerprint-and-direct-solve/decision.md`.
>
> **UPDATE 2026-08-11 (C71) — bridge extended to all 3 channels; a candidate
> "no admixture" test turned out to be void, self-caught before being
> reported.** C70's bridge extends cleanly to `channel_s` and `channel_c`
> (same machine-precision signature: `hom_dim=6`, explicit intertwining
> residual `~5e-16` both). Mid-round, found that
> `experiments/20260717-round118-matter-generation-factorization-test/`
> (a PRIOR round, 2026-07-17) had already precisely scoped the user's
> `H_physical=H_matter⊗H_generation` hypothesis with `H_matter` being G18's
> **32-dim** NCG finite spectral triple, not round59's 8-dim `Σ` — and had
> already left three specific sufficiency conditions explicitly open. A
> proposed shortcut (compose the three channel intertwiners around the
> `v→s→c→v` cycle and check if the "monodromy" is a clean scalar, as a
> candidate test of condition (iii), "triality acts with no admixture") gave
> a suspiciously clean result — `monodromy = Identity` to machine precision,
> robust across 4 independent random seeds — but is a **pure algebraic
> tautology**: `V_cv·V_sc·V_vs=(U_v U_c⁻¹)(U_c U_s⁻¹)(U_s U_v⁻¹)=Identity` by
> matrix cancellation alone, for ANY three invertible matrices, regardless of
> su(3) content. Caught by direct algebraic inspection after the numerics
> looked clean, before being reported as evidence. **Round118's sufficiency
> conditions (i)-(iii), at the actual 32-dim level, remain genuinely open** —
> answering them needs an S⁶-zero-mode-to-SM-content embedding this project
> has not built anywhere; inventing one without physical motivation was
> explicitly declined, matching round110's own prior conclusion in a
> structurally similar situation. See
> `experiments/20260811-c71-triality-bridge-extension-and-mixing-test/decision.md`.
>
> **UPDATE 2026-08-11 (C71 follow-up) — "take stock" of the S⁶-embedding
> gap: it is deeper than round118 itself realized.** Traced round118's
> "necessary condition VERIFIED" (charge-formula channel-independence) back
> to its actual construction. Found: `K3_32`/`T3L_32`/`J3_32` (the
> `SU(2)_L`/`SU(2)_R` piece of `Y`, feeding that charge formula) are built
> via `kron(K_S3, I8)` with `I8 = eye(8)` — **a bare identity-matrix
> placeholder for the S⁶ spinor factor** (`g11_block_generators.py:57`),
> not any actual curved-space construction, built 2026-06-17/18, a full
> month before round59's real twisted Dirac operator (2026-07-14) or
> G102's triality channels (2026-07-05) existed. `B-L` is better off —
> `[VERIFIED-tool]`, via g15's own T8 check, genuinely proportional to
> `lift_to_spinor(complex_structure())`, a real object from g10's `SO(6)`
> tangent-bundle construction — but via a **different, never-reconciled**
> geometric route than round59/G102's spinor module. Net effect: the
> charge-uniformity round118 verified was never tested against a genuine
> channel-dependent alternative, because the charge-operator chain feeding
> `H_matter` has no channel-index parameter at all — "uniform" because
> channel-dependence was never a variable, not because real per-channel
> geometry was checked and found to agree. **Does not retract round118's
> own verdict** (correctly reported at the time) — adds a caveat neither
> round118's two skeptic passes nor any downstream citation caught.
> **What closing this for real would require:** rebuild `K3_32`/`T3L_32`
> using round59's real `Σ` (transported per-channel via C70/C71's
> `U_v/U_s/U_c`) in place of `I8`; separately reconcile g10's
> tangent-bundle-representation `su(3)` (acting on the 6-dim `3⊕3̄`) with
> round59/G102's spinor-module `su(3)` (acting on the 8-dim `1⊕1⊕3⊕3̄`) —
> different natural representations of what should be the same abstract
> algebra, never explicitly bridged; then re-derive `G18`'s KO-dimension-6
> structure and particle-content labeling from the result (not guaranteed
> to survive). **Scope: comparable to redoing the entire G10-G19 program
> (13 rounds, 2026-06-17 to 2026-06-19) plus reconciling it with the
> round59/G102/C70/C71 chain (~15 more rounds)** — not a quick follow-up.
> Logged as a pearl (`pearl_registry/INDEX.md`, 2026-08-11) and as a caveat
> on `CLAIM_LEDGER.yaml`'s `C20_MATTER_GENERATION_FACTORIZATION_THREE_WAY`.
> No new construction attempted this round — investigation/provenance-audit
> only, per Gate 1/Gate 2 (`artifact-provenance-gates.md`) discipline.
>
> **UPDATE 2026-08-11 (C72) — the su(3)-level bridge survives to the full
> `g2`, vanishes exactly at `so(8)`; `T³=1` confirmed vacuous at every
> equivariance level, not just su(3).** Continuing the C70-C76 queue with
> the S⁶-embedding gap explicitly left open per user direction. Extended
> C70/C71's channel-bridge Hom-space computation from `su(3)` (dim 8,
> `Hom=6`) to the full `g2` (dim 14, the whole `S6=G2/SU(3)`
> isotropy+coset algebra) and to the ambient `so(8)` (dim 28). **Monotone
> shrinkage, all `[VERIFIED-numpy]`: `6 → 2 → 0`.** `g2=2` matches Schur's
> lemma exactly given the already-published (pearl #33, 2026-07-15)
> `8_v=1+7` `g2`-branching — independently reconfirmed here via
> `g2`-Casimir eigenvalues on `channel_v` (one `~0`, seven equal `=2.0`) —
> not a new discovery by itself. **What IS new:** an explicit, invertible
> cross-channel `g2`-equivariant isomorphism, constructed for all three
> channel pairs (`det` `0.013`/`0.0018`/`0.0047`, intertwining residual
> `5.0e-16`–`7.0e-16` across all 14 generators) — pearl #33 established the
> branching for ONE channel symbolically, never a map BETWEEN channels.
> `so(8)=0` independently re-verifies G102's own module-docstring assertion
> (`g102_spin8_fiber.py:19`) directly, rather than trusting the citation —
> the textbook statement that `8_v`,`8_s`,`8_c` are inequivalent
> `so(8)`-representations, confirmed as the structural negative control.
> **Separately, generalized C71's own methodological finding:** re-ran the
> "chain three intertwiners through a common reference" `T³=1` check with
> THREE INDEPENDENT RANDOM matrices (no `su(3)`/`g2` structure at all) —
> `monodromy − I` residual `1.156e-14`, confirming the telescoping
> tautology is fully general, not specific to `su(3)`. **OB11(iii)'s
> state-level question remains open** — this stays entirely at the
> algebra-equivariance level (necessary, not sufficient, for a genuine
> state-level operator); a non-tautological `T³=1` test needs `τ` fixed
> INDEPENDENTLY of the intertwiners under test (e.g. via Baez's explicit
> `S3⊂F4` construction, pearl #33's own follow-up direction) — named, not
> attempted. Compatibility with `D,J,γ` stays explicitly deferred. See
> `experiments/20260811-c72-state-level-triality-g2-equivariance-test/decision.md`.

> **UPDATE 2026-08-10 (C62), condition (iii).** The `SU(3)` gauge/charge
> structure is genuinely **triality-fixed** — confirmed by an INDEPENDENT
> construction (Baez's octonion trilinear-covariance realization,
> `solve_triality_partners`), not just G102's Cl(0,8) route: all 8 `su(3)`
> generators satisfy `solve_triality_partners(a)=(a,a)` exactly (residual
> ~1e-15), while a generic non-`g2` element does not (negative control,
> deviation ~3-4.5) — the machinery genuinely discriminates. This is a real,
> if narrow, positive result: the matter/gauge content is represented by the
> **identical matrix** across all three triality channels, independently of
> which construction realizes them. **What remains open, and is the harder
> half of condition (iii):** an explicit state-level operator `t` (mapping an
> actual vector in `8_v` to a vector in `8_s`) has **not** been constructed —
> this is a genuinely unresolved question in the pure-math literature itself
> (pearl entry #29, McRae 2025, arXiv:2502.14016 — Euclidean-signature
> triality "has no intertwining action upon the representation space," left
> open by that paper too). Condition (iii), as originally posed, stays open
> on that half. See
> `experiments/20260810-ob11iii-triality-su3-invariance/decision.md`.
>
> **UPDATE 2026-08-10 (C67), primary-source re-confirmation of the above.**
> The McRae citation just above was independently re-verified against the
> full 18-page primary source (not from memory, not secondhand — fetched
> and read this round, saved to repo as
> `McRae_2025_Exploring_Triality_Explicitly.pdf`). Confirmed, not
> corrected: the 2026-07-15 pearl entry was already based on a full read.
> Precisely characterized what was left implicit before: McRae's own
> Section 5 states the state-level operator as an **open question the
> paper's own author does not resolve** ("no novel research has been done
> in this work"), not a proven no-go theorem. New: McRae's own `H`
> (Euclidean) is structurally the SAME KIND of object as this project's own
> `T` (C62, `triality_so4xso4_invariance.py`) — both algebra-level, not
> state-level, automorphisms. This project's own construction independently
> reaches exactly the primary literature's current state of the art, not
> behind it. Attempting a state-level construction here would mean
> attempting genuinely unresolved research — deliberately not attempted.
> See `experiments/20260810-ob11iii-mcrae-primary-source-verification/decision.md`.

> **UPDATE 2026-08-10 (C61).** The cheapest possible route to proving condition
> (ii) — bare `SU(3)`-representation theory alone forcing `X_ij=0` — is now
> **closed, refuted, not merely untried**. Built `m=g2/su3` (the tangent/
> isotropy representation, the object the actual Dirac operator is built
> from) and computed `dim Hom_su3(m⊗channel_i,channel_j)` for all 9 pairs
> using G102's own unmodified machinery: **10 for every pair, diagonal and
> off-diagonal alike** — no distinction whatsoever. This is the direct,
> predictable consequence of already-established facts (condition (i)/C29:
> identical `su(3)` block structure; G102 S6/S7: `su(3)` alone cannot tell
> the channels apart even at the bare fiber level) — it closes off the
> possibility that folding in the tangent bundle might have broken that
> degeneracy. It doesn't. Condition (ii) stays **open**, narrowed to a
> genuinely harder question: whether the actual **G2-invariant differential
> operator** (not bare pointwise equivariance) picks a nonzero element out of
> this now-confirmed 10-dimensional Hom-space. See
> `experiments/20260810-ob11ii-channel-mixing-necessary-condition/decision.md`.
> Condition (iii) untouched, separately scoped, not attempted this round.

> **EVIDENCE CORRECTED 2026-08-09 (external audit).** Condition (i)'s
> conclusion stands, but the evidence cited below does not carry it:
> `C₂(3) = C₂(3̄) = 4/3` identically, so the quadratic-Casimir spectrum
> cannot separate `1⊕1⊕3⊕3̄` from `1⊕1⊕3⊕3`. The sufficient evidence was
> already in the repo since **G102**: `Hom(V,V) = 6` excludes the
> alternatives (which give 8), and round127 had already made this argument.
> Nothing recomputed — only re-cited. Negative control: explicit
> `1⊕1⊕3⊕3̄` → 6, explicit `1⊕1⊕3⊕3` → 8. See
> `experiments/20260809-ob11-weight-spectrum-correction/decision.md`.

**Condition (i) now VERIFIED, (ii)/(iii) still open.** Scope-clarifying
finding first: `SU(2)_L×SU(2)_R` lives entirely on the S³ factor of
`H_matter` (round90, `preprint.tex:292-310`) and never acts on the
S⁶-side `8_v/8_s/8_c` fiber at all (round119 corrected an earlier false
`SU(3)×SU(2)×SU(2)`-in-`SO(6)` embedding claim) — so condition (i)'s
`SU(2)_L×SU(2)_R` part is vacuous (the S³-side factor is identical
across channels by construction); the only substantive part is
`SU(3)_c`. Directly verified by diagonalizing the quadratic Casimir of
G102's own already-established `su(3)` action on each channel: all three
(`8_v,8_s,8_c`) give an IDENTICAL spectrum (2 zero + 6 equal-nonzero
eigenvalues, matching the predicted `1⊕1⊕3⊕3̄` pattern), not just an
equal-dimension `Hom`-count as before. See
`experiments/20260803-ob11-internal-block-structure-check/decision.md`.
Conditions (ii) (no channel-mixing in the Dirac operator) and (iii)
(triality acting purely as `1⊗t`) remain open — (ii) specifically
requires assembling a genuinely new channel-decomposed differential
Dirac operator, entangled with the still-open OB1 (per the 2026-07-19
substrate-check below), not attempted this round.

**Original description (superseded framing for condition (i) alone, kept
for history — (ii)/(iii) below are unaffected and still fully open):** the user's own proposed hypothesis
(`H_physical=H_matter⊗H_generation`, WEAK reading: `H_matter`=32-dim
already-realized `SU(3)_c×SU(2)_L×SU(2)_R` content, `H_generation`=3-dim
triality-channel label) has one necessary condition **verified**
(`grep`-confirmed, `preprint.tex`): the charge formula `Q=T₃L+Y` has no
per-channel index, so the gauge group acts uniformly across all 3
triality channels. **But this is necessary, not sufficient** — a genuine
tensor factorization also requires (i) identical internal block
structure of the 3 32-dim blocks, not just identical charges, (ii) no
channel-mixing terms in the full Dirac operator, (iii) triality acting
purely as `1⊗t` with no admixture on the matter factor. **None of these
three are checked anywhere in this project.**

**Note — the STRONG reading (genuine gauged `SU(4)` Pati-Salam matter,
`(4,4̄)`) is separately BLOCKED** by gate G97 (see
`null_results/INDEX.md` `Round118-STRONG-reading`) — this OB is only
about the WEAK reading, which remains a live, partially-checked
candidate, not a dead end.

**What would resolve it:** check the Dirac operator's block structure
across the 3 triality channels (`8_v`,`8_s`,`8_c`) for cross-channel
mixing terms.

**Substrate check (2026-07-19, `boyko-agent` disposition review) — the
"likely extractable from round107/round110" claim below does NOT hold,
verified by direct read:** round110's Dirac object is a 4×4 constant-
spinor toy (`D_block=diag(0,0,3c/2,3c/2)`) for the `t=0/t=1` torsion
block — it contains no `8_v/8_s/8_c` channel structure at all. round107
computes the 15 `so(6)=su(4)` generators Leibniz-lifted onto the 64-dim
`Σ⊗Σ` fibre (the SU(4)-orbit of the twisted kernel) — a different
construction from the Cl(0,8)-built `v/s/c` reps where the triality
channels actually live (G102/round124/127/128). **Neither file contains a
channel-decomposed physical Dirac operator with off-diagonal
`8_v↔8_s↔8_c` blocks.** This OB's own "cheap, well-scoped follow-up"
label below is therefore substrate-unverified and should not be treated
as ready — resolving it requires *assembling* a channel-decomposed
physical Dirac operator (a new, not-yet-costed construction), which is
also entangled with the still-open OB1/KT-8 full-operator question.

**Owner / next step:** NOT cheap as originally labeled (see substrate
check above) — requires scoping as its own SMALL–LARGE round if pursued,
not a quick extraction. Full detail (superseded "cheap" framing):
`experiments/20260717-round118-matter-generation-factorization-test/decision.md`.

## OB14 — why `Sigma`, not `m` (or another twist bundle), is the physically
correct twist for round59's `D_S6` construction [OPENED 2026-09-04, C139]

**Background.** round59 certified `dim ker(D_{S6,twist=Sigma})=1`, a
load-bearing input to `N_gen=3` (`CLAIM_LEDGER.yaml`
`C2_ROUND59_KERNEL_DIM1`, 6 direct ledger dependents including
`C4_NGEN3_HEADLINE`). Until C139, no wrong-twist negative control had
ever discriminated — four attempts (C73/C73b) all gave the identical
kernel or a result forced by construction. This meant the question "why
`Sigma` specifically" could not even be posed as a real alternative: with
no discriminating control, `Sigma` was the only twist bundle this
project had ever tried, not a twist bundle shown to be privileged over
any specific alternative.

**What changed.** C139 built a genuinely different twist bundle
(`m_C`, the tangent/isotropy representation, module type `3+3bar`,
zero `su(3)` singlets, vs `Sigma`'s `1+1+3+3bar`, two singlets) using
the identical `NOMIZU`/`ADNU` connection data and Leibniz-rule
construction, and found `kernel=0`, not `1` — robust across the whole
admissible connection family (13-angle sweep, not a single-point
accident), verified two independent ways (numeric SVD, exact sympy),
and independently re-verified by two context-blind skeptic passes plus
the orchestrating session (script re-run, sign-convention bug
independently re-derived from the Clifford algebra). This establishes,
for the first time, that `Sigma` is NOT the unique twist bundle
compatible with this project's own calibration discipline — an
alternative WITH a different kernel genuinely exists.

**What this does NOT do:** identify what the independent physical
justification for `Sigma` actually is. `Sigma` remains Tom Lawrence's
own construction, directly motivated by AHL2023's spinor-bundle
framework — C139 does not argue `Sigma` is wrong, only that it is no
longer the unique twist giving a nontrivial invariant kernel structure.
Two independent skeptic passes also qualified C139's own result:
`Term1=0` (part of the original justification for the result's
significance) is FORCED by `su(3)` Schur's lemma for ANY zero-singlet
twist bundle, not special to `m` — the genuinely load-bearing,
non-forced fact is narrower (`Term2`'s robust non-vanishing). A more
directly comparable test (a matched-singlet-count twist bundle, e.g.
`m⊕2·1`, preserving `Sigma`'s own two-singlet shape) remains unbuilt
and would more decisively test whether `D_S6` discriminates `Sigma`
from a same-shape alternative, not merely a different-shape one.

**Status:** `BLOCKED-EXTERNAL-OR-THEORETICAL`. Likely requires either a
physical argument from Tom Lawrence's own framework for why the twist
bundle must be another copy of the spinor bundle specifically (external,
subject to this project's own "DO NOT INITIATE CONTACT" constraint), or
an internal argument this project has not yet attempted (e.g. the
matched-singlet-count follow-up named above).

**Owner / next step:** build the matched-singlet-count twist bundle
(`m⊕2·1` or similar) as the next concrete, internally-computable test —
comparable in scope to C139's own build, not a large undertaking. Full
detail:
`experiments/20260904-c139-twisted-s6-alternate-representation-negative-control/decision.md`.
