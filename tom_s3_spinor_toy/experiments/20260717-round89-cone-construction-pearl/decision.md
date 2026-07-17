# E19 (round89) — Decision

**Date:** 2026-07-17
**Verdict:** `PARTIAL_OPPOSITE_SIGN_STRUCTURAL` — the bridge is REAL (not the
"wrong parameter axis" round86 assumed), and the bare `|λ|=1/2` magnitude
match to AHL2023 is exact and non-trivial, tool-verified. But the SPECIFIC,
load-bearing fact round86/E18 needed AHL2023 to supply — a coexistence
argument matching this project's `t=0`/`t=1` pair — does **not** transfer: the
sign structure this project's own connection family FORCES (`λ(1)=-λ(0)`,
an unavoidable, convention-independent identity, not a choice) is the
**opposite** of the ONE most-specific, directly-relevant AHL2023 statement for
this exact case (`S³=SU(2)`, `n=1`, p.48: a **same-sign** pair, "the constant
`1/2`," singular). The magnitude match is a genuine, new, if narrow,
mathematical fact for this project; the coexistence gap E18 flagged is not
narrowed by it — if anything it is sharpened into a precise, named
incompatibility instead of an untested "wrong axis" guess.

**Go/no-go:** The `|λ|=1/2` result is promotable as a pearl (a genuine,
previously-unknown structural fact about this project's own `∇^t` family).
It is **not** promotable as progress on E18's parent-action/coexistence
question — Section 4 below states precisely why not.

## Bottom line, stated plainly first

Using ONLY formulas this project has already derived and tool-verified
(E9's `Ω_i(t)=-(tc/2)Z_i` spin-lift, E7's `t=1/2=`Levi-Civita
identification, round76's explicit `t=1` parallel spinor under `c0=-2`), this
experiment built the one bridge round86 flagged as unattempted but did NOT
build (the cone construction) — instead using a MORE DIRECT bridge already
implicit in this project's own formulas: the connection-difference between
`∇^t` and `∇^{LC}=∇^{1/2}`. This bridge is real: substituting either of this
project's own already-established parallel spinors (`t=0`, any `c`; `t=1`,
`c0=-2` only) into it produces an EXACT Riemannian Killing-spinor equation for
`∇^{LC}`, with a computed constant `λ(t)=(c/2)(t-1/2)`. At `c=c0=-2`:
`λ(0)=+1/2`, `λ(1)=-1/2` — the magnitude matches AHL2023's stated Killing
constant `1/2` for round `S³=SU(2)` EXACTLY, with **no extra scaling factor
needed** (Section 3). But the sign PATTERN — this project's `t=0`/`t=1` pair is
structurally FORCED into OPPOSITE signs, for every value of the structure
constant, not just the calibrated ones (Section 2, `λ(1)=-λ(0)` identically) —
does **not** match AHL2023's own `S³`-specific statement (p.48: BOTH of the
paired Killing spinors share the SAME sign, `1/2`, at the round metric),
though it IS consistent with the general, other-`n` wording of Corollary 3.14
("constants `1/2,-1/2`"). Section 4 explains exactly what this means, and
does not mean, for E18's coexistence question.

## 1. The bridge itself — fresh derivation, tool-verified [VERIFIED-tool]

Script: `e19_killing_bridge_check.py`, reusing E9's `Z_i=i·σ_i`,
`Γ^k_{ij}(t)=t·c·ε_{ijk}`, `Ω_i(t)=-(tc/2)Z_i` byte-identically
(`e9_explicit_parallel_spinor.py:90-99,137-178`).

**Torsion re-derivation (fresh, not merely citing E7).** `T^k_{ij}(t) :=
Γ^k_{ij}(t)-Γ^k_{ji}(t)-c·ε_{ijk}` (the bracket term is `[Z_i,Z_j]=c·ε_{ijk}Z_k`,
E7/E9's own convention) equals **exactly** `c·(2t-1)·ε_{ijk}` for all 27
`(i,j,k)` triples, vanishing **iff** `t=1/2`
(`step1_torsion_check.torsion_zero_iff_t_half = true`,
`all_entries_match_c_times_2t_minus_1_times_eps_form = true`). This
independently confirms, by direct computation, that `t=1/2` is genuinely the
torsion-free member of the family — combined with the already-established fact
that `∇^t` is metric-compatible for every `t` (E9's own `so3_valued_all_i`
check, any `t`), this makes `∇^{1/2}` the unique torsion-free,
metric-compatible connection, i.e. the actual Levi-Civita connection of the
round metric this project's frame realizes — not merely "the value E7 named
LC," an independently re-derived structural fact.

**Connection-difference formula.** `Ω_i(t) - Ω_i(1/2) = -(c/2)(t-1/2)·Z_i`
exactly, symbolic in `t,c`, verified for all `i=1,2,3`
(`step2_diff_formula_check.diff_formula_matches = true`, after fixing a sign
slip in this experiment's own first draft of the verification helper — see
"Self-caught bug" below).

**Derivation (standard connection-1-form algebra, not previously written down
anywhere in this project):** for ANY spinor field `ψ` satisfying
`∇^t_{Z_i}ψ=Z_i(ψ)+Ω_i(t)ψ=0` (i.e. `∇^t`-parallel, in whichever
trivialization this project has already established that parallelism holds),
substituting `Z_i(ψ)=-Ω_i(t)ψ` into `∇^{LC}_{Z_i}ψ:=Z_i(ψ)+Ω_i(1/2)ψ` gives
`∇^{LC}_{Z_i}ψ = [Ω_i(1/2)-Ω_i(t)]ψ = (c/2)(t-1/2)·Z_i·ψ` — an EXACT Riemannian
Killing-spinor equation `∇^{LC}_{Z_i}ψ=λ(t)·Z_i·ψ` with `λ(t)=(c/2)(t-1/2)`.
Because `{Z_1,Z_2,Z_3}` is a global frame and both sides are `C^∞`-linear in
the frame direction, this extends to `∇^{LC}_Xψ=λ(t)·X·ψ` for every tangent
vector `X`, not merely the three frame vectors — the genuine, full Killing
equation.

## 2. `t=0`/`t=1` Killing checks [VERIFIED-tool]

**`t=0`:** the generic constant spinor `ψ=(a,b)` (E9's own ansatz,
`decision.md:44-62`, unconditional in `c`) satisfies
`Ω_{1/2}(i)·ψ = λ_0·Z_i·ψ` identically in `a,b`, for all `i=1,2,3`
simultaneously, with `λ_0=-c/4` (`step3_t0_killing_check.t0_killing_check =
true`, all three residuals the exact zero matrix, not approximately zero).

**`t=1`:** round76's own explicit spinor `ψ(x)=ḡ(x)ψ₀`
(`e10_right_invariant_frame.py:548-614`, `run_part4`), re-verified parallel
here using the SAME `c0` (found fresh via `find_structure_constant`, not
hardcoded `-2`: `c0_found = "-2"`, confirming round76's own value
independently), satisfies the Killing equation with `λ_1=c0/4=-1/2`, checked
via **two independent routes** that agree exactly
(`route1_direct_residuals` — literal `Z_i(ψ)` computed by direct symbolic
differentiation via `directional_derivative(XL[i],·)`, reused from round76's
own machinery; `route2_shortcut_residuals` — the algebraic shortcut using the
already-established parallel condition — `two_independent_routes_agree =
true`, `t1_killing_check = true`).

**Sign structure (the sharper, previously-unasked question).** `λ(t)=(c/2)
(t-1/2)` is linear and homogeneous in `(t-1/2)`, so `λ(1)=-λ(0)`
**identically, for every value of `c`** — this is not a coincidence of the
calibrated values `c=±2`; it is forced by the already-established LINEAR
form of `Ω_i(t)` (E9's own formula, unchanged) —
(`step5_sign_structure_check.lambda1_equals_minus_lambda0_symbolic = true`,
checked symbolically, not merely at the two numeric calibrations). **There is
no choice of sign convention (`c=+2` vs `c0=-2`) that can make this project's
`t=0`/`t=1` pair a SAME-sign Killing pair** — the opposite-sign structure is
load-bearing, not an artifact.

## 3. Magnitude comparison to AHL2023 [VERIFIED-tool for the arithmetic; reused citation for AHL2023's own stated values]

Using the single, self-consistent `c=c0=-2` (forced by the fact that the
`t=1` parallel spinor is established ONLY under this value — `CONVENTION_
TABLE.md` §5): `λ(0)=+1/2`, `λ(1)=-1/2`
(`verdict.lambda0_at_c0_minus2 = "1/2"`, `verdict.lambda1_at_c0_minus2 =
"-1/2"`, `verdict.lambda0_magnitude_is_half = true`,
`verdict.lambda1_magnitude_is_half = true`). **This is an exact match, no
extra scaling factor, to AHL2023's own stated Killing constant `1/2` for the
round `S³=SU(2)` metric** (reused via `experiments/20260717-round86-parent-
action-discriminator/decision.md:129-141`, itself `[VERIFIED-tool: pdftotext
extraction]` — not re-extracted from the PDF in this experiment).

**Why the exact numeric match (not merely the functional FORM) is credible,
not coincidental — supporting argument, [INFERRED], not independently
re-derived here.** This project's own `c=2`/`c0=-2` calibration was fixed via
`h_H=3` (E2/E9), itself calibrated against this project's own established
`n=0` Dirac eigenvalue `=3/2`. The value `3/2` is the standard literature
eigenvalue for the round-`S³` (unit, `sec=1`) Dirac operator's smallest mode
(`±(n/2+k)`, `n=3,k=0` gives `±3/2` — Hitchin 1974 / Friedrich, [DOCS], not
re-derived from scratch here). Since this SAME metric-normalization anchor
underlies both this project's calibration and the standard convention in
which Killing spinors on round `S^n` have constant exactly `±1/2` (Friedrich/
Bär), the exact match found here is corroborated by an independent
pre-existing anchor, not merely a lucky arithmetic coincidence of this
specific experiment.

## 4. What this means, and does NOT mean, for E18's coexistence question

**The most important distinction in this whole experiment.** AHL2023's own
text (reused from round86, not re-extracted here) contains TWO different
statements about the round `S³=SU(2)` case, and they say different things:

1. **Corollary 3.14, general form** (parametrized family `g_{a,b}`,
   `a=2b/n`): "we recover the usual Sasakian Killing spinors for the
   constants `1/2,-1/2` **(or `1/2,1/2`, depending on `n`)**." This general
   statement explicitly allows for EITHER a same-sign OR an opposite-sign
   pair, depending on `n`.
2. **p.48, `§6` case `(II) G=SU(2)=Sp(1)`, i.e. `n=1` — the EXACT case this
   project studies:** "the round metric `g_{a,b}|_{a=b=1/2}` admits **a PAIR
   of invariant Killing spinors for THE constant 1/2**" — one constant,
   singular, shared by BOTH basis spinors. Per the parenthetical in item 1
   above ("or `1/2,1/2`, depending on `n`"), `n=1` is the case that falls
   into the SAME-sign bucket, not the opposite-sign one.

**This project's own bridge (Sections 1-2) produces an OPPOSITE-sign pair,
`λ(0)=+1/2, λ(1)=-1/2`, structurally forced (Section 2, `λ(1)=-λ(0)`
identically in `c`).** This does NOT match statement 2 — the one
most-specific, directly-relevant AHL2023 fact for `S³=SU(2)` itself. It DOES
match the general form of statement 1's wording ("constants `1/2,-1/2`"), but
that wording is explicitly for the case AHL2023 itself says does NOT apply
to `n=1`.

**Consequently:** the specific hope round86/E18 flagged — that AHL2023's
"round `S³` admits a PAIR of Killing spinors, coexisting for a structural
reason" fact could license "this project's `t=0` and `t=1` connections'
worth of physical content must coexist too" — is **not** rescued by this
experiment. If anything, this experiment SHARPENS round86's original,
softer "wrong parameter axis" dismissal into a precise, checked reason: not
merely "these are different mathematical objects in general" (round86's
level of argument), but "when the actual bridge between them is built
explicitly, the SPECIFIC coexistence structure AHL2023 states for `S³=SU(2)`
itself (a same-sign pair) is the OPPOSITE of what this project's own
connection family is capable of producing (an opposite-sign pair, by an
unavoidable linear-algebra identity)." The gap round86 flagged as "would
require new argument, not attempted" is not merely still open — this
experiment gives a first, checked reason to expect that filling it with
THIS specific analogy will not work, without abandoning something else
already established (the linear form of `Ω_i(t)`, or the identification
`t=1/2=`LC, both independently re-confirmed in Section 1).

**What this experiment does NOT establish, either way (regardless of the
sign-mismatch finding):**

1. It does **not** prove no version of the coexistence argument can ever be
   built — only that the MOST DIRECT reading of it (matching AHL2023's own
   `S³`-specific statement against this project's own `t=0`/`t=1` connection
   pair via the connection-difference bridge) does not work. A genuinely
   different bridge (the cone construction round86 flagged, still not
   attempted; or a different identification of which of AHL2023's `ψ+`/`ψ-`
   pair corresponds to which physical sector) might behave differently — not
   attempted here, out of this experiment's scope.
2. Even a full sign-match (had one been found) would only have supplied a
   MATHEMATICAL coexistence fact (Killing spinors of both eigenvalue signs
   exist simultaneously on the round metric) — not a PHYSICAL one (an action
   with independent fields and equations of motion requiring both sectors to
   appear in a 13D compactification). E18's core missing ingredient (a stated
   parent action, `preprint.tex:1370-1419`, KT-1) is untouched either way —
   this experiment could only ever have narrowed, never closed, that gap.
3. Does **not** reopen or re-litigate E15's `NULL_OMEGA_PROPORTIONAL_TO_
   IDENTITY` (Clifford-volume-element grading) result — a completely
   different candidate mechanism (E12/E15's doublet-splitting question, not
   the `t=0`/`t=1` coexistence question), untouched here.
4. Does **not** re-derive or challenge E7's `t=1/2=LC` identification, E9's
   `Ω_i(t)` formula, or round76's explicit `t=1` spinor — all reused exactly
   as established, with one independent fresh re-derivation (torsion,
   Section 1) as a non-circular cross-check.
5. Does **not** independently re-verify AHL2023's own Clifford/metric
   normalization from the PDF text directly — the magnitude match is
   corroborated (Section 3) by this project's own pre-existing `n=0`
   eigenvalue anchor, which is an [INFERRED]-level supporting argument, not
   an independent re-derivation from AHL2023's own source text.
6. Does **not** affect `N_gen=3`, `KT-8`, H1c, or any headline claim — this
   experiment concerns only the same narrow, already-non-load-bearing
   torsion-escape-route program E18/round86 concerned, explicitly flagged
   `preprint.tex:1467-1497` as "physically unmotivated, not a resolution."

## Self-caught bug (honesty note, per this project's own Claim Scope Discipline)

The FIRST run of this script reported `diff_formula_matches = false` — a
genuine sign error in the "predicted" formula inside `check_diff_formula`
(predicted `+(c/2)(t-1/2)Z_i`, actual `Ω_i(t)-Ω_i(1/2)` is
`-(c/2)(t-1/2)Z_i`). This was caught by re-deriving the connection-difference
by hand (`Ω(1/2)-Ω(t) = +(c/2)(t-1/2)Z_i`, the direction actually used in
`check_t0_killing`/`check_t1_killing`, both of which passed on the FIRST run
already) and comparing signs — the bug was isolated to one redundant
verification helper, not to the substantive Killing-equation derivation
itself, which used the correct sign from the start. Fixed
(`check_diff_formula`'s `predicted` now reads `-(c*HALF)*(t-HALF)*Z[i]`) and
re-run; all checks now pass consistently. Reported here per this project's
own norm of not silently editing out a first-pass discrepancy.

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result kills:** round86's implicit assumption that the bridge
  between AHL2023's Killing-spinor pair and this project's `t=0`/`t=1`
  connection pair, IF it existed at all, would need genuinely new,
  unwritten machinery (the cone construction) — Sections 1-2 show a bridge
  already implicit in this project's OWN formulas, no cone construction
  needed. It also kills the possibility that this project's own connection
  family could ever reproduce a SAME-sign Killing pair (Section 2,
  `λ(1)=-λ(0)` for every `c` — a hard, structural fact, not a convention
  choice).
- **What this result does NOT kill:** E18's parent-action gap itself
  (untouched, Section 4); the possibility that a DIFFERENT bridge (cone
  construction, or a different `ψ+`/`ψ-` identification) might still connect
  AHL2023's same-sign fact to this project's pair; the general Corollary
  3.14 wording for other `n` (untouched, not this project's case anyway).
- **What survives, confirmed stronger than before:** a new, tool-verified,
  previously-unknown structural fact about this project's own `∇^t` family —
  its `t=0`/`t=1` pair IS, via a clean and now-explicit bridge, an exact
  `λ=±1/2` Riemannian-Killing-spinor pair for the round metric, matching
  AHL2023's stated magnitude exactly. This is real mathematical content
  (Section 3), even though it does not resolve E18 (Section 4).

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Try the cone construction round86 originally flagged | Build the flat cone `C(S³)` and the standard Killing-spinor↔parallel-spinor correspondence explicitly; check whether IT (rather than the connection-difference bridge used here) produces a same-sign pair — a genuinely different construction, not attempted here |
| Re-examine which of AHL2023's `ψ+`/`ψ-` corresponds to which of this project's `t=0`/`t=1` | This experiment assumed the natural pairing (this project's `t=0`↔one sign, `t=1`↔the other); AHL2023's own `ψ+`,`ψ-` labeling might not line up this way — not checked here |
| Independently re-derive AHL2023's own metric/Clifford normalization from the PDF text directly | Would upgrade Section 3's `[INFERRED]` supporting argument to a `[VERIFIED-tool]` one; not attempted here (out of this experiment's scope, per the task's own instruction not to re-extract from the PDF) |

## Assumptions carried, unresolved

- `∇^t_{Z_i}ψ=Z_i(ψ)+Ω_i(t)ψ` as a connection-1-form identity valid for ANY
  spinor field (not just constant ones), in the fixed left-invariant
  trivialization — [DOCS/standard], unchanged from E9/E10's own usage.
- This project's own Clifford/metric normalization matches AHL2023's
  "unit round `S³`" convention — [INFERRED], supported but not independently
  re-verified from the PDF (Section 3, Relaxation Map).
- `D_full²=D_{S3,t}²⊗I+I⊗D_{S6,twisted}²` (E2/E12's decoupling assumption) —
  not touched by this experiment; not needed for anything computed here.

## Pearl-registry candidate

**Observation, concrete enough to flag:** this project's own `∇^t` family,
via the connection-difference bridge to `∇^{LC}=∇^{1/2}` derived fresh in
this experiment, produces an EXACT `λ=±1/2` Riemannian-Killing-spinor pair at
`t=0,1` — matching AHL2023's stated round-`S³` Killing constant magnitude
exactly, with no extra normalization needed, and corroborated by this
project's own pre-existing `n=0` Dirac-eigenvalue calibration anchor.
**Falsifiable prediction, if pursued further:** IF the cone-construction
bridge (Relaxation Map, row 1) is built explicitly, it should ALSO produce
`λ=±1/2` for the SAME `t=0,1` pair (since both bridges, if correct, describe
the same underlying geometric fact) — but might resolve the sign-structure
mismatch differently (e.g. by identifying a different physical pairing
between `ψ+`/`ψ-` and `t=0`/`t=1` than the natural one assumed here).
**Impact score ~3** (narrow: affects only this project's own
torsion-escape-route program, already flagged non-load-bearing for
`N_gen=3`; the underlying "characteristic-connection ↔ Killing-spinor"
correspondence itself is well-known in the broader field, so the pearl here
is specifically "this project's own `t=0`/`t=1` connections realize it with a
forced opposite-sign structure, which does not match AHL2023's `n=1`-specific
same-sign fact" — a narrow, if clean, negative-plus-partial result). Not
registered to the global `pearl_registry/INDEX.md` — project-internal, not
cross-domain.
`next_check`: if the torsion-escape-route program (E1-E19) is ever revisited,
check whether the cone construction (Relaxation Map row 1) resolves the
sign-structure mismatch found here before assuming the coexistence question
is fully closed either way.

## Check (reproduces this decision)
`python e19_killing_bridge_check.py` →
`verdict.torsion_zero_iff_t_half==true`, `verdict.diff_formula_matches==true`,
`verdict.t0_killing_check==true`, `verdict.t1_killing_check==true`,
`verdict.lambda0_at_c0_minus2=="1/2"`, `verdict.lambda1_at_c0_minus2=="-1/2"`,
`verdict.lambda0_magnitude_is_half==true`,
`verdict.lambda1_magnitude_is_half==true`,
`verdict.lambda1_equals_minus_lambda0_symbolic==true`,
`verdict.label=="PARTIAL_OPPOSITE_SIGN_STRUCTURAL"`.
