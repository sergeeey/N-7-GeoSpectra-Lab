# C123 decision -- both candidate mechanisms fail as OB1 selectors, for
DIFFERENT reasons than originally suspected; the round's most valuable
output is a correction to OB13's own overstated rule, not either claim.
**Same-day external review found Gap B itself overbroad (see correction
above) -- Claim 2 is now OPEN, not killed, pending C124.**

**Verdict (2026-09-01, revised same day):** `PARTIAL__NEITHER_MECHANISM_PROMOTES_YET__CLAIM1_DUPLICATE_AT_F4_NOT_F6_PLUS_NEW_STABILITY_RESULT__CLAIM2_NOT_KILLED_REDUCES_TO_BARE_CS_SHAPE_PENDING_C124_PARENT_INVARIANT_CHECK__OB13_TEXT_ITSELF_FOUND_SELF_INCONSISTENT`
**Status:** OB1 stays PARKED. No reopen condition met. Per
`PARENT_ACTION_GATE.md`'s own discipline, a construction answering some
fields and failing others is accurately `PARTIAL`, not rounded to
PROMOTE or REJECT.
**Gate fields assessed:** F1 (Claim 2 only), F4 (both claims, novelty).
F2, F3 (already resolved by citation), F5-F7 not assessed for either.

## New finding, same day: Yang-Mills has a stability structure along `t`

[VERIFIED, independent re-derivation] `E(t)=Ct²(1-t)²=C(t²-2t³+t⁴)`
(the Yang-Mills energy along the 1-parameter family, C123's own Claim 1
object). `E'(t)=C(2t-6t²+4t³)=2Ct(1-t)(1-2t)` -- three stationary
points, `t=0,1/2,1`, matching round99's own critical-point list.
`E''(t)=C(2-12t+12t²)`:
```
E''(0)  = 2C   (>0, for C>0)
E''(1)  = 2C   (>0)
E''(1/2)= -C   (<0)
```
**`t=0,1` are locally stable (minima) along the `t`-direction; `t=1/2`
is a local maximum -- Levi-Civita sits at the top of a barrier between
two flat vacua, restricted to this 1-parameter family.** This is new
content beyond round99 (which recorded the critical-point locations but
not their second-derivative character or the barrier interpretation) --
still F4-level (same duplicate `[t(t-1)]²` shape, still cannot prefer
`0` over `1`), and still only a 1D slice: whether `t=0,1` remain stable
under the FULL fluctuation operator (not just this 1-parameter family)
is F6 content, unassessed, named in the Relaxation Map below.

---

## Where this came from

An external multi-model panel (7 independent LLM responses to a homework
framing of OB1, `torsion-selection-problem.html` artifact) converged on
several candidate mechanisms. Two were extracted and checked here because
they were the least redundant with mechanisms already on OB1's
"already tried" list. This round does NOT evaluate the panel's own
confidence or reasoning -- only the two extracted, falsifiable
mechanisms, against this project's own established gates.

---

## Claim 1 -- Yang-Mills curvature functional

### What was claimed and what survived

`S_YM[∇^t] = ∫_{S³}|R^t|² dvol` was claimed to duplicate `round99`'s
"curvature-norm toy" (`OPEN_BLOCKERS.md` OB13's own name for it) as an
OB1 F4 (t-selection) mechanism.

**CONFIRMED, with a field-specific scope correction.** `round99`
(`experiments/20260717-round99-toy-Vt-curvature-double-well/
e26_toy_Vt_curvature_double_well.py:129-147`) computed
```
V(t) = ‖R^t(Z₁,Z₂)Z₁‖²_Frobenius = [t(t-1)]² · ‖[[Z₁,Z₂],Z₁]‖²
```
-- a fixed-point curvature-norm, no volume integral. Since `R^t =
t(t-1)·T` with `T` a t-INDEPENDENT tensor (round99 PART 2 and round113's
independent re-verification both confirm 27/27 components), every
quadratic curvature invariant -- including `S_YM`'s volume integral --
factors as `[t(t-1)]²` times a positive t-independent constant. As
functions of `t`, `V_round99(t)` and `S_YM(t)` are identical up to a
positive multiplicative constant. **A positive constant cannot move a
stationary point** -- so `S_YM` supplies no new t-selection information
beyond what `round99` already supplied.

**Mechanism Transfer Gate (6-field), applied explicitly, not just
formula-matched:** FORMULA identical (`[t(t-1)]²` up to scale) · OBJECT
identical (`R^t` on S³) · GENERATOR identical (`∇^t_XY=t[X,Y]`, same
connection per round113's F3 reconciliation) · SECTOR identical (S³ leg
only) · **ROLE differs** (round99: bare kinematic tensor norm; `S_YM`:
a named action term with an EOM) · **OBSERVABLE differs** (a shape vs
a variational principle). 4/6 identical, 2/6 differ.

**The 2 differing fields matter, but at a DIFFERENT gate field than the
one this claim was about.** `PARENT_ACTION_GATE.md` F6 ("what equations
of motion, if any, has the candidate configuration been required to
satisfy... currently: none have been derived for this program... the
single largest gap in the whole OB1 program") is genuinely unaddressed
by `round99` (no volume integral, no kinetic term -- `round99`'s own
`decision.md:37` records this exact gap, skeptic-accepted at the time).
`S_YM` DOES supply a named action principle. **So: `S_YM` is a duplicate
at F4 (selection) -- it selects nothing round99 didn't already select --
but it is NOT a duplicate at F6 -- it is the first candidate in this
program's F4 attempts to actually be framed as an action, not a bare
invariant.** Neither field alone earns a PROMOTE (F6 still needs the
question F4 asks -- does this action actually follow from the 13D parent
-- unanswered), but conflating the two fields would misclassify a real,
if narrow, contribution as pure duplication.

### The unplanned finding: OB13's own rule is self-inconsistent

This claim's own verification (checking WHY round99 and `S_YM` should be
considered duplicates) forced a direct read of `OPEN_BLOCKERS.md` OB13's
prose, which states (verbatim, `OPEN_BLOCKERS.md:329-333`):

> Consequence: both curvature-based searches were structurally incapable
> of selecting. Their nulls were *necessary* and carry **no** information
> about whether a selector exists -- they were never tests of H1c. Any
> selector must be **linear (odd) in the torsion**, never quadratic.

**FALSIFIED as literally written**, on three independent grounds, none
of which were the target of this round -- all surfaced defending Claim 1:

1. **Conflates two different questions.** Evenness in `(t-1/2)` proves
   only that a functional cannot PREFER `t=0` over `t=1` (or vice
   versa). It does not prove the functional is uninformative about
   whether `{0,1}` is selected over other `t` at all.
   `V(t)=[t(t-1)]²` has its unique global minimum SET at exactly
   `{0,1}` (round99's own output: `V0=V1=0, Vhalf=1/16,
   critical_points={0,1/2,1}, V''(0)=V''(1)=64>0`) and nowhere else.
   Selecting a two-point set out of a continuum IS information. Two
   distinct questions were merged: "which of the two?" (even ⟹
   provably blind -- OB13 correct on THIS) and "why that pair rather
   than any other `t`?" (even ⟹ CAN answer, and here DOES -- OB13
   wrong on THIS).
2. **Contradicts this project's own gate as written.** `OPEN_BLOCKERS.md`
   OB1 (line ~42-44) and `PARENT_ACTION_GATE.md` F4 both define a
   passing mechanism as one that selects a specific `t` "**(or forces
   `t=0` and `t=1` together)**" -- the both-together branch is
   explicitly in scope, and it is precisely the branch an even
   functional serves and an odd one cannot serve symmetrically. OB13's
   "any selector must be odd, never quadratic" rules out, by fiat, half
   of the project's own stated pass criterion.
3. **"Linear" conflates polynomial degree with parity, and this bites
   Claim 2 directly.** The correct requirement is "has a nonzero
   component odd under `t↔1-t`" -- strictly weaker than "linear." A
   cubic generally has a nonzero odd part (this is exactly the shape of
   the Chern-Simons functional every panel member who tried it derived,
   and which this project's own C121 computed for `η(D^t)`). OB13's
   literal wording would misfile any cubic degeneracy-breaker as dead
   on parity grounds alone.

**The project's own later work already contradicts OB13's rule in
practice, not just in principle.** C119 (2026-08-31, three weeks after
OB13's C37-C39) took an EVEN/quadratic condition (`Rc-¼H²=8t(1-t)δ`,
Bismut-Ricci-flat) seriously as a candidate t-selector and killed it on
GEOMETRY (the frozen S⁶ factor's own curvature), not by a one-line
parity dismissal. If OB13's rule were sound and applied consistently,
C119 would have been unnecessary -- a single sentence citing OB13 would
have sufficed. It was not applied. This is the strongest available
evidence the rule is mis-stated, not merely imprecisely worded.

**Also found, minor:** OB13 calls round99 and round111's `Scal(t)`
results "nulls." `round99`'s own script label is
`CONFIRMED__DOUBLE_WELL_PLAUSIBLE_FROM_CLASSICAL_CURVATURE`
(`decision.md:65`: "CONFIRMED (double-well plausible) -- for the narrow
mathematical claim"). These were not null results; OB13 mislabels
confirmed, narrow-scope results as uninformative nulls.

**Recommended corrected statement of OB13's actual, defensible rule**
(not applied to `OPEN_BLOCKERS.md` in this round -- a separate editorial
step, flagged in the Relaxation Map below):

> A functional even in `(t-1/2)` cannot PREFER `t=0` over `t=1` -- that
> half of the selection question is structurally closed to it. It CAN,
> however, select the set `{0,1}` uniquely against all other `t` (the
> "forces both together" branch OB1/F4 already accept as a valid
> resolution). What breaks the residual `t=0`-vs-`t=1` degeneracy must
> be odd in `(t-1/2)` -- but "odd" is not "linear"; any odd-degree term,
> cubic included, qualifies.

---

## Claim 2 -- transgression mechanism `S_mix = k∫CS₃(ω_{S³})∧P₄(M₄)∧ch₃(E_{S⁶})`

### The three narrow technical checks -- all CONFIRMED

1. **`c₃(S⁻)=2`, `ind=+1`, chain PROMOTE status** -- confirmed directly
   from `experiments/20260621-g73-three-channel-dirac/decision.md`
   (29/29 tests) via `χ(S⁶)=2` (Chern-Gauss-Bonnet, G33) →
   `S⁻=T^{1,0}S⁶⊕trivial` (G69) → `c₃(S⁻)=2` (Whitney) → `Â(S⁶)=1`
   (`p₁=0`, G50) → `ind=1` (G73-D). **Citation correction:** "31/31
   tests" belongs to G74B specifically, not the whole chain (G73=29/29,
   G74A=30/30); the load-bearing numbers for THIS claim (`c₃`, `ind`)
   live in G73 alone. **Also found:** G74A's own `decision.md:3-25`
   carries an in-place supersession -- both of its original lemmas are
   now flagged insufficient/invalid by later work, though the `dim
   ker=1` conclusion survives via a different argument. Does not affect
   `c₃` or `ind` (untouched by G74A's revision), but "G73/G74A/G74B,
   PROMOTE, certified" should not be cited as one undifferentiated
   block going forward.
2. **`ch₃(E)≡c₃(E)/2` for this bundle -- not a symbol-overload error.**
   The general reduction `ch₃=(c₁³-3c₁c₂+3c₃)/6 → c₃/2` requires
   `c₁=c₂=0`. This is FORCED, not assumed: `c₁∈H²(S⁶;ℤ)=0`,
   `c₂∈H⁴(S⁶;ℤ)=0`, since `S⁶`'s cohomology is concentrated in degrees
   0 and 6 -- the identical fact G73 already uses to get `Â(S⁶)=1` from
   `p₁=0`. Consistency check: `ind=∫Â·ch(E)`, degree-6 part
   `=ch₃+Â₁·ch₂=ch₃` (since `ch₂=0`), so `ind=∫ch₃=c₃/2=1` --
   reproduces G73's own formula exactly, read backwards. **`∫_{S⁶}
   ch₃(E_{S⁶})=1≠0`, confirmed, zero new computation.**
3. **C119's topological pre-filter does not apply to a degree-6 class.**
   The pre-filter's own stated scope (`c119/decision.md:459-470`,
   `OPEN_BLOCKERS.md:101-105`) is explicitly "harmonic **k-form
   (k=1,2,3)**." `S⁶` compact/connected/oriented ⟹ `H⁶(S⁶;ℝ)≅ℝ`
   (Poincaré duality with `H⁰`), `b₆(S⁶)=1`, harmonic representative
   `vol_{S⁶}`. Künneth: `H⁶(S³×S⁶;ℝ)=H⁰(S³)⊗H⁶(S⁶)⊕H³(S³)⊗H³(S⁶)
   =ℝ⊕0=ℝ`, generated by `vol_{S⁶}` -- the exact mirror of C119's own
   `H³(S³×S⁶;ℝ)=ℝ·vol_{S³}` result. A degree-6 class with its whole leg
   on S⁶ is precisely what survives this Künneth computation, not what
   it kills.

### Two gaps NOT in the original kill criterion, both found by the skeptic

**Gap A (raised, then resolved this session): possible collapse into
C121's already-REJECTED `η(D^t)`.** `S_mix`'s entire `t`-dependence
lives in `CS₃(ω^t)` (`P₄`, `ch₃` are `t`-independent constants). C121
(2026-09-01, one day earlier) rejected `η(D^t)` as an OB1 selector:
closed form `P(a)=a(3-4a²)/6`, `a=3(t-1/2)`, `η mod 2` identical on
every interval. If `CS₃(ω^t)` and `η(D^t)` are the same object up to
normalization, `S_mix` would inherit C121's REJECT immediately.

**Resolved this session** [own re-derivation, not yet independently
skeptic-reviewed -- flagged accordingly]. Write both as functions of
`x=t-1/2`, normalized to unit linear coefficient:

```
eta (C121):  P(a) = a/2 - (2/3)a^3,  a = 3x
             = 1.5x - 18x^3
             normalized:  x - 12x^3

CS (this round, matching every panel member's independent derivation,
    verified repeatedly this session):
             S~_CS(x) = K(2/3 x^3 - 1/2 x)
             normalized (divide by -1/2):  x - (4/3)x^3
```

The cubic-to-linear coefficient ratio differs by a factor of exactly 9
(`12` vs `4/3`). **`CS₃(ω^t)` is NOT proportional to `η(D^t)`** -- they
are both odd cubics in `x`, but genuinely different functions, not the
same object under a normalization choice. `S_mix` does **not** inherit
C121's REJECT verdict by this route.

> **⚠️ STRENGTHENED same day, second independent skeptic pass
> (context-blind, fresh re-derivation from scratch, arithmetic
> re-verified by this session before accepting it).** The
> coefficient-ratio argument above is the WEAKEST available evidence
> for non-proportionality, and genuinely fragile: [VERIFIED, this
> session's own re-check] `P(a) = a/2 - (2/3)a³` is, **as a bare
> polynomial, exactly `-S(a)`** -- the identical cubic as `CS`'s own
> `S(x)=-x/2+(2/3)x³`, up to an overall sign. The entire "not
> proportional" finding therefore rests entirely on `a=3x` (not
> `a=x`) being the correct substitution: had either derivation used
> `a=x` by mistake, the two functions would have come out looking
> exactly (anti-)proportional. `a=3x` is not a free choice -- it is
> pinned by C121's own crossing lattice (`a=3/2 ⟺ t=1`) -- but the
> finding's robustness rode entirely on that one substitution being
> remembered correctly in both derivations, which is exactly the kind
> of single point of failure a normalization-immune check should not
> have. **A normalization-immune, scale-free discriminator exists and
> is stronger:** the two functions' STATIONARY POINTS are disjoint,
> and stationary points of `f` and `k·f` are identical for any nonzero
> `k`, so no rescaling (correct or mistaken) can erase this.
> ```
> S'(x) = 2x²-1/2 = 0  ⟹  x=±1/2  ⟹  t ∈ {0,1}        (CS)
> dP/da = -2(a²-1/4) = 0  ⟹  a=±1/2 ⟹ x=±1/6 ⟹ t ∈ {1/3,2/3}  (eta)
> ```
> [VERIFIED, independently re-derived by this session] Disjoint
> critical sets -- `{0,1}` vs `{1/3,2/3}` -- cannot be reconciled by
> any normalization choice. **Cite this, not the coefficient ratio, as
> the load-bearing evidence for non-proportionality.**
>
> **Caveat correctly separated by the skeptic, not previously named:**
> non-proportionality of the two SHAPES does not by itself show `S_mix`
> escapes C121's actual kill mechanism, which was about
> **periodicity** (`η mod 2` identical across every crossing interval
> under the family's own large-diffeomorphism structure), not about
> shape. Whether `∫_{S³}CS₃(ω^t)` has an analogous periodicity
> ambiguity under large gauge transformations (the standard
> `CS mod (2π)²`-type shift) is a SEPARATE, unanswered question --
> named here, not attempted.

**Gap B (found, then NARROWED same day -- see correction below):
`∫_{M₄}P₄(M₄)=0` for `P₄` built from spacetime curvature alone.**
`S_mix`'s three-way integral factors as
`(∫_{S³}CS₃)·(∫_{M₄}P₄)·(∫_{S⁶}ch₃)`, and is nonzero only if ALL THREE
factors are nonzero. `S⁶` factor confirmed nonzero above. `S³` factor
(odd cubic, generically nonzero for `t≠0,1/2,1`) is fine. **The `M₄`
factor: for a `P₄` required to be a nontrivial curvature-based
characteristic class (Pontryagin/Chern-type) on topologically trivial
4D spacetime, `P₄=0` identically** -- this specific subclass is dead.

> **⚠️ CORRECTED 2026-09-01, same day, external review.** The
> conclusion drawn from Gap B above was **overbroad** -- it silently
> generalized "curvature-based `P₄`=0" into "the transgression
> mechanism is fatally killed," without checking the simplest
> alternative: **`P₄=\mathrm{vol}_4}`, the ordinary spacetime volume
> form.** [VERIFIED, trivial] any top-degree form on an n-manifold is
> automatically closed (`d` has no `(n+1)`-forms to land in on an
> n-manifold), so `d\,\mathrm{vol}_4=0` unconditionally -- no curvature
> input needed, no vanishing on a trivial background. With this choice,
> `S_mix` reduces to `κ(t)·∫_{M₄}\mathrm{vol}_4`, i.e. an ordinary
> **t-dependent 4D cosmological-constant/vacuum-energy term**, with
> coefficient `κ(t)=[∫_{S³}CS₃(ω^t)]·[∫_{S⁶}ch₃(E)]` -- a completely
> standard construction (the same shape this project's own `round115`
> flux potential `V_flux∝C³` already used: an internal integral sourcing
> a 4D effective potential). Since `∫_{S⁶}ch₃(E)=1` (confirmed above,
> a positive constant), `κ(t)` is proportional to `CS₃(ω^t)` itself, up
> to an overall positive rescaling -- **the rescued mechanism has the
> IDENTICAL t-dependence (same odd cubic, same critical points `t=0,1`)
> as the bare S³-only Chern-Simons proposal already covered elsewhere in
> the panel (students 1/2/4/7).** The `S⁶`-coupling does not change the
> SHAPE of the selector; it only multiplies by a positive constant. So
> Gap B, corrected, is: `S_mix` with `P₄=\mathrm{vol}_4` is **not fatally
> killed**, but it is also **not new content beyond the bare CS
> mechanism** -- its only potential value is as a candidate PARENT-ACTION
> ORIGIN story for that already-known cubic, IF a genuine 13D-covariant
> local invariant reduces to `T₃(ω^t)∧ch₃(E)∧\mathrm{vol}_4` (transgression,
> not a bare, non-gauge-invariant `CS₃`) without a hand-inserted
> `4+3+6` splitting. This is now the decisive open question for the
> whole CS/transgression family -- not answered by this round, named as
> a candidate next round (`C124`) in the Relaxation Map below.

**One favorable finding, stated because it undercuts rather than
supports this round's own earlier work:** `CS(0)=0≠CS(1)=-B/3` (an
explicit skeptic re-derivation) confirms `CS₃(ω^t)` sits in the ODD
sector -- so Claim 2 is NOT a variant of Claim 1's `S_YM` (which is
EVEN). The two claims are genuinely independent mechanisms, not two
readings of one thing.

---

## Kill Analysis (per this project's Anti-Overfitting Gate)

**What was killed:**
- Claim 1 AS AN F4 (t-selection) MECHANISM -- duplicate of round99,
  killed by a positive-constant-cannot-move-a-critical-point argument,
  not by parity.
- Claim 2 AS LITERALLY STATED (with `P₄` built from pure spacetime
  curvature) -- killed by `∫_{M₄}P₄=0` on the trivial background, a
  gap unrelated to either of its two originally-suspected failure
  modes (both of which it actually survives).

**What was NOT killed:**
- Claim 1 as an F6 candidate (a named action principle for the S³
  connection) -- genuinely unaddressed territory, though still gated
  behind the unchanged, largest OB1 gap: deriving it from the 13D
  parent action.
- Claim 2's S⁶-coupling idea in general -- only the SPECIFIC choice of
  a pure-spacetime-curvature `P₄` is dead; a `P₄` built from some other
  bosonic field strength present in the compactification (not yet
  named or attempted) is untouched by this round's finding.
- `N_gen=3`'s CONDITIONAL status, `lambda=FREE_COUPLING_PARAMETER`,
  `safe_for_runtime=False` -- all unaffected, as pre-registered.
- OB13's underlying C37-C39 result itself (`ι` is orientation-reversing,
  parity not gauge) -- untouched. Only the DERIVED "any selector must
  be linear, never quadratic" summary sentence is found overstated.

## Relaxation Map (named, priority-ordered per same-day external review;
none attempted this round except where marked DONE)

| Priority | Option | What it would require / kill criterion |
|---|---|---|
| 1 (**C124 -- DONE, same day, see below**) | `P₄=\mathrm{vol}_4` / vierbein parent-invariant check | Binary question: does a genuine 13D-covariant local invariant (Lovelock/Chern-Simons/transgression, first-order `e,ω` formalism) reduce, via `M₁₃=M₄×S³×S⁶`, to `T₃(ω^t)∧ch₃(E_{S⁶})∧\mathrm{vol}_4` WITHOUT a hand-inserted `4+3+6` splitting? Flagged by the reviewer as "a major undertaking, not a routine check" (matches `round86`'s own precedent language) -- three possible outcomes: (a) term arises automatically with nonzero coefficient → Claim 2 upgrades from PARTIAL toward a serious candidate; (b) arises only after explicit manual insertion → dies honestly at the parent-action gate; (c) forbidden by 13D Lorentz/gauge symmetry → a STRONGER structural no-go than the original (now-corrected) Gap B |
| **2 (re-promoted, new #1 for actual next work, same-day re-review)** | **Full gauge-equivalence gate**: `(e,ω₀,E_{S⁶},Ψ,…) ∼? (e,ω₁,E_{S⁶},Ψ,…)` -- not just abstract flat `SU(2)` connections, the FULL 13D configuration (vielbein, twist bundle, fermion content) | Now the highest information-value next step, since C124 closed off the CS/transgression route (former priority 1) and this one is near-binary: if `0∼1` under the full config, OB1 collapses to "why the flat Cartan-Schouten gauge orbit at all" and the sign-choice question dissolves entirely; if `0≁1`, the obstruction found IS the long-sought differentiating structure. Kill/confirm criterion: find or rule out a `g` taking the FULL pair (including fermion couplings) from one to the other -- student 2's original large-gauge-equivalence idea, never closed at the vielbein-inclusive level. |
| 3 | Full F6 for Yang-Mills: fluctuation operator + Hessian beyond the 1D `t`-slice | **Untouched by C124** (C124 classified 13D-covariant invariants; Yang-Mills is an S3-internal Hodge-star functional, never claimed as such a reduction, and dimensionally excluded from C124's own epsilon-sector S3 leg regardless). Does the `t=0,1` stability found above (this round) survive the FULL space of fluctuations, not just the 1-parameter family? Kill criterion: `t=0,1` are not stable under the full operator, or new stable homogeneous vacua appear outside `{0,1}` |
| 4 | Systematic classification of allowed low-derivative-order 13D local invariants | **DONE, same round as priority 1** -- C124's own execution WAS this classification (exhaustive within the Lovelock-Cartan class plus a checked wider mismatched-index class); superseded, not separately attempted. |
| 5 | Correct `OPEN_BLOCKERS.md` OB13's overstated summary sentence in place | **DONE** -- see the `⚠️ CORRECTED` block added directly to OB13's text this round |
| 6 | Find a non-curvature `P₄(M₄)` for Claim 2 | **SUPERSEDED** -- `\mathrm{vol}_4` found this round (see correction above); C124 (priority 1) is the sharper remaining question |
| 7 | Re-run this round's own CS₃-vs-η algebra through a second, independent skeptic pass | Not yet done -- this session's own re-derivation is marked accordingly, not yet adversarially reviewed |
| 8 | Parallel-spinor/SUSY gate, one-loop `V_eff(t)`, bordism/global-anomaly branch | Named by the reviewer, correctly deprioritized below the above -- expensive, only after 1-4 |

**Priority 1 (C124) outcome, same day:** `STRUCTURAL_NO_GO`, skeptic-
confirmed. No 13D-covariant local invariant reduces to the target term
-- the CS/transgression family (and a wider mismatched-index
class beyond it) is now closed as an OB1 F4 mechanism, on a bosonic,
strict-product background, **class-qualified explicitly** (local,
polynomial, first-order invariants only -- does NOT touch this round's
own separate Yang-Mills claim, which stays `PARTIAL`, or extra
derivatives, enlarged gauge algebras, or non-polynomial actions, per
same-day external review; see `decision.md`'s own theorem-statement
header for the full itemized exclusion list). See
`experiments/20260901-c124-parent-
invariant-classification-preregistration/decision.md` for the full
account and `PARENT_ACTION_GATE.md` F4 / `OPEN_BLOCKERS.md` OB1 for the
registry entries.

## What this round does NOT show

1. Does not resolve OB1 or move it out of PARKED -- no reopen condition
   met (per `OPEN_BLOCKERS.md`'s own 4-condition list).
2. Does not edit `OPEN_BLOCKERS.md` OB13's actual prose -- flags the
   defect and proposes corrected wording, in the Relaxation Map above,
   as a separate, not-yet-taken step.
3. Does not evaluate any of the panel's other proposed mechanisms
   (large-gauge-equivalence, parallel-spinor/SUSY, bordism/Spin(13)
   extension, Weyl-semimetal analogy) -- only the two extracted here.
4. Does not change `N_gen=3`, `lambda`, or `safe_for_runtime`.
5. Does not solicit Tom Lawrence's Part 5.

## Verification

- `round99`'s script (`e26_toy_Vt_curvature_double_well.py`) and
  `decision.md` read directly this round (via the skeptic sub-agent,
  context-blind, then cross-checked here).
- `G73`/`G74A`/`G74B` `decision.md` files read directly.
- `C119`, `C121`, `PARENT_ACTION_GATE.md`, `OPEN_BLOCKERS.md` OB1/OB13
  read directly (both by this session before the skeptic pass, and
  independently by the skeptic).
- FL Step 8a skeptic pass: `Agent(skeptic, model=opus)`, context-blind
  (claim.md text + file pointers only, no session history, no
  reasoning chain, no prior confidence statements).
- This round's own CS₃-vs-η coefficient comparison shown in full above;
  marked `[own re-derivation, not yet independently skeptic-reviewed]`
  per this project's audit-verification-gate discipline.
- No pytest suite touched (no shared code modified); this round is a
  literature/gate-check + one independent algebraic re-derivation, no
  new production code.
