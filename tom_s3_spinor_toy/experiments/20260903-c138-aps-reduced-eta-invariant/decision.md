# C138 decision -- APS reduced eta invariant xi(D^t)=(eta(D^t)+h(t))/2 mod 1:
# CONFIRMED, ALGEBRAICALLY, to be a smooth (mod-1-continuous) function of `t`
# with no discontinuity or distinguished value at any crossing, `t in {0,1}`
# included -- NULL, closing pearl_registry row 116

**Date:** 2026-09-03
**Experiment:** `20260903-c138-aps-reduced-eta-invariant`
**Question type (EstimandOps L0):** Descriptive.
**Script:** `c138_reduced_eta_invariant.py` · **Results:** `results_c138.json`

## Verdict

```text
NULL__XI_MOD_1_IS_ALGEBRAICALLY_CONTINUOUS_ACROSS_EVERY_CROSSING
  __H_T_JUMP_EXACTLY_CANCELS_HALF_OF_ETAS_2MU_N_JUMP__PROVEN_NOT_JUST_OBSERVED
  __T_IN_0_1_NOT_DISTINGUISHED_FROM_ANY_OTHER_CROSSING_OR_ANY_OTHER_POINT
  __XI_MOD_1_EQUALS_P_A_OVER_2_MOD_1_EVERYWHERE__ONE_SMOOTH_FORMULA_NO_N_DEPENDENCE
  __KILL_CRITERION_A_FIRES_IN_SUBSTANCE__NOT_IN_ITS_LITERAL_LETTER
  __NUMERIC_VALUES_DIFFER_CROSSING_TO_CROSSING_BUT_HAVE_NO_STRUCTURAL_MEANING
  __CLOSES_PEARL_REGISTRY_ROW_116__CANDIDATE_EXHAUSTED
```

**One line:** the entire reason C121's raw `eta mod 2` was NULL (a smooth
polynomial `P(a)` shifted by an even integer that vanishes mod 2) has a
direct analogue here, discovered by actually computing `h(t)`, not assumed:
the reduced invariant's own `+h(t)` term is EXACTLY the piece needed to turn
`eta`'s discontinuous jump (`2*mu(n)` at each crossing) into a smooth,
continuous function of `t` under division by 2 -- proven algebraically, for
every crossing computed (`n=0..5`, both signs), not just observed
numerically at `t in {0,1}`.

---

## 0. Background, read in full before computation (per claim.md)

- `experiments/20260901-c121-eta-invariant-general-t/decision.md` -- read in
  full. Certified: `eta(a) = P(a) + 2*sum_{n=0}^{J} mu(n)`, `P(a) =
  a(3-4a^2)/6`, `mu(n)=(n+1)(n+2)`, `a=3(t-1/2)`; `eta mod 2` identical on
  every interval (NULL, closed); the AT-the-point convention correction
  (`eta_at(t=1)=+1/2`, not the one-sided limit `-3/2`); `xi=(eta+h)/2` at
  `t=1` computed in passing as `5/4`, i.e. `1.25 mod 1 = 0.25` -- **verified
  from scratch below, not copied** (§4).
- `pearl_registry/INDEX.md` rows 115-116, quoted exactly in claim.md and
  re-quoted below (§0a).
- `null_results/INDEX.md` `C121-EtaInvariant` entry -- raw `eta mod 2` NULL,
  quoted in full in claim.md; this round tests the genuinely different `xi`
  quantity, not a re-test.

### 0a. Pearl rows 115-116, verbatim (from `pearl_registry/INDEX.md`)

Row 115 (2026-09-01, C120 skeptic pass, resolved by C121): names `eta(D^t)`
as an F4 candidate, closes with *"One unattempted variant survives: the APS
reduced eta `xi=(eta+h)/2 mod 1` (materially different, mod 1 not mod 2)."*

Row 116 (2026-09-01, C121's own skeptic pass, the pearl THIS round closes):
*"the APS **reduced eta invariant** `xi(D^t) = (eta(D^t)+h(t))/2 mod 1`...
Materially different from the raw `eta mod 2`... because `xi` is mod 1 (not
mod 2) AND incorporates `h(t)`'s own jump, which raw `eta` does not... `h(t)`
jumps differently at different crossings depending on multiplicity
`(n+1)(n+2)`, which is NOT constant across crossings (2 at n=0, 6 at n=1, 12
at n=2, ...)"* -- **this is the falsifiable prediction this round tests, and
it is FALSE**: `h(t)`'s non-constancy does not survive into `xi mod 1` at
all, because it is EXACTLY what division by 2 needs to make the answer
integer-shift-invariant (§6-7 below).

## 1. Zero-Signal Gate (FL Step -5)

| field | content |
|---|---|
| Entity | `xi(D^t) = (eta(D^t)+h(t))/2 mod 1`, at the first three crossing pairs of the certified `D^t` family |
| Falsifiable predicate | `xi` at `t in {0,1}` is structurally distinguished from other crossings, OR identical everywhere |
| Measurable outcome | an explicit table of `xi(t) mod 1` at every computed crossing, shown not asserted |

All three fillable => gate **PASSES**.

## 2. Re-derive `P(a)`, independently, before trusting it

`c138_reduced_eta_invariant.py` §1 re-types (not copies) C121's own
Hurwitz-zeta decomposition (`f(0,a) = z2 - 2a*z1 + (a^2-1/4)*z0` via
Bernoulli-polynomial `zeta_H(-n,q)`) from scratch and forms
`P(a)=f(0,a)-f(0,-a)`.

`[VERIFIED-tool]` Result: `a*(3-4*a**2)/6` -- symbolically identical to
C121's certified closed form (`sp.simplify(diff)==0`). Cross-checked two
further ways, both independent of the Hurwitz-zeta arithmetic:

- `dP/da = -2*(a^2-1/4)` (APS variation identity C121's skeptic pass also
  confirmed via a structurally different heat-kernel route) -- `PASS`.
- `P` is odd (`P(-a)=-P(a)`) and `P(0)=0` (matches `t=1/2`, `k_grav=0`,
  G34-B3, spot-check of `P` only, not a re-derivation of G34-B3 itself).

## 3. Crossing lattice map, shown not asserted

`a = 3(t-1/2)`, `a_c = +-(3/2+n)`, `t = a/3+1/2`. Inverted symbolically and
checked against claim.md's own stated values for `n=0,1,2`
(`[VERIFIED-tool]`, `crossing_lattice_matches_claim_md_stated_t_values`):

| n | `a_c` (+) | `t` (+) | `a_c` (-) | `t` (-) |
|---|---|---|---|---|
| 0 | 3/2 | 1 | -3/2 | 0 |
| 1 | 5/2 | 4/3 | -5/2 | -1/3 |
| 2 | 7/2 | 5/3 | -7/2 | -2/3 |

`mu(n)=(n+1)(n+2)`: `mu(0)=2, mu(1)=6, mu(2)=12` -- matches claim.md's own
stated values, and is a product of two consecutive integers, hence **always
even** -- the fact §7's cancellation proof rests on.

## 4. `eta` AT each crossing, two independent routes, cross-checked

**Route (i), direct.** The AT-the-point value is the average of the two
one-sided limits. This is not an ad hoc convention: the zeta-regularized
definition `eta(s)=sum_{lambda!=0} sign(lambda)|lambda|^{-s}` EXCLUDES zero
eigenvalues from the sum by construction. At an exact crossing, the
crossing eigenspace (multiplicity `mu(n)`) contributes `-mu(n)` on the
near-origin side and `+mu(n)` on the far-from-origin side, with every other
eigenvalue continuous across the point; excluding the crossing eigenspace's
contribution entirely (setting it to `0`, its own average) is exactly the
average of the two one-sided sums, since only that one term changes between
them. This is the SAME convention C121's skeptic pass used
(`eta_at(t=1)=+1/2`, not the one-sided limit `-3/2`) -- re-derived here from
the definition, not copied.

**Route (ii), closed-form shortcut.** `eta_at = P(a_c) + 2*S(n-1) + mu(n)`,
`S(n) = sum_{k=0}^{n} mu(k)`, `S(-1):=0`.

`[VERIFIED-tool]` Routes (i) and (ii) agree EXACTLY (symbolic equality,
`sp.simplify(r1-r2)==0`) at all 6 crossings for `n=0,1,2`.

**Spot-checks against C121's own already-independently-confirmed numbers**
(not re-derived, only reproduced): `eta_at(t=1)=+1/2` (matches
C121's skeptic-corrected value exactly); `eta(a=2)=-1/3` (an ordinary
interval-0 point, not a crossing, matches C121's own reported number
exactly); `P(0)=0` (`t=1/2` spot-check). All `PASS`.

## 5. `h(t)` -- kernel dimension AT each crossing, cross-checked against an
   INDEPENDENT, project-wide-certified source, not just C121's abstract table

`h(t) = mu(n)` at each crossing (`0` elsewhere, not needed elsewhere). This
is not merely asserted equal to the eta-jump multiplicity by convenient
labeling: `mu(n)` is the SAME multiplicity that generates `eta`'s own
`2*mu(n)` jump at that point (§6), so identifying it with the kernel
dimension is forced by internal consistency of C121's own already-certified
formula, not an independent free input.

**Independent cross-check at `t=0` `[VERIFIED-tool via grep, this
session]`**: `dim ker(D_{S3,t=0})=2` is certified, UNCONDITIONALLY, by an
explicit parallel-spinor construction over the FULL 2-dimensional
constant-spinor space (`experiments/20260717-round73-e9-explicit-parallel-
spinor/decision.md:44-62`), and reused verbatim by at least four later
rounds (C27/round78's `ob10_c27_majorana_halving.py:4`, round83, round85,
round92, round93). This independently confirms `h(0)=mu(0)=2` from a
DIFFERENT derivational route than round67's abstract Peter-Weyl multiplicity
table C121's formula is built from.

**Honest caveat surfaced by this cross-check, at `t=1`
`[VERIFIED-tool via grep, this session]`**: the SAME round73 found the
*naive* constant-left-invariant-spinor ansatz gives ONLY the trivial
solution at `t=1` (kernel dimension 0 among constant spinors, with the
project's calibrated `c=2`) -- `dim ker(D_{S3,t=1})=2` is recovered only by
a DIFFERENT, right-invariant-frame construction in round76, and explicitly
tagged *"under `c0=-2` only"*
(`experiments/20260717-round92-endpoint-anomaly-audit/decision.md:53-55`,
`CONVENTION_TABLE.md` row 5). So `h(1)=2` IS independently confirmed via a
second, explicit route (matching `mu(0)=2`) -- but that explicit route
needed an extra calibration input `t=0`'s did not. **This is a real,
specific asymmetry in how much machinery each endpoint's kernel needed to
construct explicitly, not a numeric discrepancy in the value used here** --
named honestly rather than silently absorbed; see §12 and the proposed Pearl
entry in §15.

## 6. The `xi(t)` table -- the round's central, explicit result

`t`, `n`, `sign`, `eta_at`, `h`, `xi_at = (eta_at+h)/2` (raw), `xi mod 1`:

| t | n | sign | eta_at | h | xi_at | xi mod 1 |
|---|---|---|---|---|---|---|
| 1 | 0 | + | 1/2 | 2 | 5/4 | **1/4** |
| 0 | 0 | - | 7/2 | 2 | 11/4 | **3/4** |
| 4/3 | 1 | + | 5/6 | 6 | 41/12 | 5/12 |
| -1/3 | 1 | - | 115/6 | 6 | 151/12 | 7/12 |
| 5/3 | 2 | + | 7/6 | 12 | 79/12 | 7/12 |
| -2/3 | 2 | - | 329/6 | 12 | 401/12 | 5/12 |
| 2 | 3 | + | 3/2 | 20 | 43/4 | 3/4 |
| -1 | 3 | - | 237/2 | 20 | 277/4 | 1/4 |
| 7/3 | 4 | + | 11/6 | 30 | 191/12 | 11/12 |
| -4/3 | 4 | - | 1309/6 | 30 | 1489/12 | 1/12 |
| 8/3 | 5 | + | 13/6 | 42 | 265/12 | 1/12 |
| -5/3 | 5 | - | 2171/6 | 42 | 2423/12 | 11/12 |

(`n=3,4,5` computed as an extra check beyond claim.md's "optionally n=2 if
cheap" -- it was cheap, and turned out to matter, see §9.)

**`xi(t=0)=3/4` and `xi(t=1)=1/4` are DIFFERENT numbers** -- this is real
and machine-checked, and superficially looks like it could be "distinguished
structure." §7 shows algebraically why it is not.

## 7. The algebraic cancellation proof -- why this is NULL, not a discovery

`[VERIFIED-tool]` For every computed crossing (`n=0..5`, both signs):

```
xi_at mod 1  =  P(a_c)/2 mod 1
```

**Proof, not just numeric agreement.** `eta_at + h = P(a_c) + 2*S(n-1) +
mu(n) + mu(n) = P(a_c) + 2*S(n-1) + 2*mu(n)`, an INTEGER multiple of `2`
added to `P(a_c)`. Dividing by `2`: `xi_at = P(a_c)/2 + S(n-1) + mu(n)`, and
`S(n-1)+mu(n)` is an integer (sum of the integer-valued `mu`), so `xi_at mod
1 = P(a_c)/2 mod 1` exactly, with NO dependence on `n` surviving beyond
which point of the smooth curve `P(a)/2` is being evaluated. Checked
computationally at all 12 crossings (`xi_mod1_equals_P_over_2_mod1_at_every_
crossing`, `PASS`) and the integer-shift fact itself checked concretely
(`S_nminus1_plus_mu_n_is_integer_for_every_n`, `PASS`).

**Contrast, to show the mechanism explicitly (not asserted):** raw `eta`
itself jumps by `2*mu(n)` at each crossing (`eta_far - eta_near = 2*mu(n)`,
verified: `4` at `n=0`, `12` at `n=1`, `24` at `n=2`, matching `2*mu(n)`
exactly -- **an earlier version of this check asserted the jump was
`mu(n)`, off by a factor of 2; caught on first run against the printed
near/far limit values in §6's table (jump `5/2-(-3/2)=4`, not `2`), fixed
before this document was written, not after a skeptic pass found it** --
see §12, this is disclosed as a self-caught defect, not hidden). Half of
that jump (`mu(n)`) is exactly what `+h(t)` supplies, and the remaining
`S(n-1)`-worth of shift was already an even integer in `eta` itself
(C121's own NULL, `eta mod 2` identical everywhere) -- so `xi=(eta+h)/2`
inherits BOTH cancellations at once.

## 8. Continuity of `xi mod 1` through every crossing, proven directly

`[VERIFIED-tool]` Computed independently of §7's algebraic shortcut: the
near-origin one-sided limit of `xi` (interval `n-1`, `h=0` there) and the
far-from-origin one-sided limit (interval `n`, `h=0` there) both equal
`xi_at mod 1` exactly, at all 12 crossings
(`xi_mod1_is_continuous_through_every_crossing`, `PASS`). So `xi mod 1` has
**no discontinuity anywhere** in this family -- unlike raw `eta` (jumps by
`2*mu(n)`) and unlike `h` itself (jumps `0 -> mu(n) -> 0`). This reproduces,
on this project's own specific operator, the textbook design purpose of the
APS reduced eta invariant (§11): it is built to vary smoothly across
spectral flow. `t in {0,1}` sit on this same smooth curve, at no more
special a point than any other `t`.

## 9. Duplicate-value honesty check (not tuned to pass -- and it doesn't)

Since `xi mod 1 = P(a_c)/2 mod 1`, the unordered PAIR of values at each `n`
(`{xi(-a_c), xi(+a_c)}`) is a function purely of `n`. Computed for
`n=0..5`:

| n | pair |
|---|---|
| 0 | {1/4, 3/4} |
| 1 | {5/12, 7/12} |
| 2 | {5/12, 7/12} |
| 3 | {1/4, 3/4} |
| 4 | {1/12, 11/12} |
| 5 | {1/12, 11/12} |

**`n=0`'s pair recurs EXACTLY at `n=3`.** The genuine, failable check
`every_n_gives_a_DISTINCT_unordered_xi_pair_ie_n0_would_be_unique` **FAILS**
-- correctly, and left failing, not tuned away: it is asking exactly the
question "would `n=0`'s value even be a CANDIDATE for uniqueness", and the
answer is no. This is additional, independent (numeric, not just algebraic)
evidence against any "`t in {0,1}` is special" reading: whatever makes
`{1/4,3/4}` occur at `n=0` also makes it occur at `n=3`, so it cannot be a
marker of `n=0` specifically. No structural explanation for the `n=0`/`n=3`
(and `n=1`/`n=2`, and `n=4`/`n=5`) pairing is claimed here -- it is most
plausibly generic behaviour of a cubic polynomial's fractional part at a
half-integer-spaced lattice, not investigated further as it is out of this
round's scope and, per §7-8, is not needed to reach the verdict.

## 10. Kill criterion evaluation (claim.md's own three branches)

Claim.md's kill criterion (a) is worded for a literal "identical value at
every crossing" outcome (matching C121's raw-`eta` precedent); this round
does **not** find that literally (§6's table has different numbers at
different crossings). But (a)'s deeper request -- *"show algebraically WHY
(the `h(t)` jump structure... is the natural place to look for the
cancellation mechanism)"* -- is satisfied in full (§7), and criterion (b)'s
own test -- *"state what would make the specific values AT `t=0,1`
meaningful... before treating any numeric difference as a result"* -- comes
back negative: `xi(0)` and `xi(1)` are not integers, not simpler fractions
than other crossings, and do not match any already-certified project
quantity: `kappa^2=7/6` (G66), `rho_min=1.179` (G66), `N_gen=3` are all
structurally unrelated numbers, and a targeted grep of
`docs/load_bearing_formulas.md` (this project's own canonical formula
reference -- not an exhaustive project-wide search, which would be too
noisy to be decisive either way and is not needed given §7's proof) for
`1/4` or `3/4` as a certified value returns **zero matches**
`[VERIFIED-tool, this session]`. And §9 shows the
SAME pair recurs at `n=3` -- there is no stated structural meaning to the
difference, precisely (b)'s condition for FALSE. Both (a) and (b) fire in
substance; (c) does not apply (no missing convention blocked completion).

**Verdict: FALSE by the conjunction of (a)-in-substance and (b) -- NULL.**

## 11. Literature check: is `xi=(h+eta)/2 mod 1` the real APS definition?

Per claim.md's explicit instruction, not invented ad hoc. Checked this
session via `WebSearch`/`WebFetch`/`mcp__arxiv__*` (multiple independent
queries, results treated as external data, not instructions):

- Multiple independent secondary/tertiary sources (general web synthesis
  covering several arXiv papers on APS theory, lens-space eta invariants,
  and differential K-theory) converge on the SAME formula: *"the reduced
  eta invariant... `xi(A) = (1/2)(h(A)+eta(A))`"*, *"taking values in
  R/Z"* (i.e. mod 1/mod integers), attributed to Atiyah-Patodi-Singer.
- `nLab`'s eta-invariant page (fetched directly) shows the closely related
  combination `exp(pi*i*(eta_X(0)+dim(ker D_X)))` in a determinant-line
  context -- algebraically `exp(2*pi*i*xi)`, independently confirming the
  `(eta+h)` combination's role and its well-definedness mod integers.
- The genuine primary source, **Atiyah, Patodi, Singer, "Spectral asymmetry
  and Riemannian geometry III", Math. Proc. Camb. Phil. Soc. 79 (1976)
  71-99**, was retrieved and its first two pages read directly (image PDF,
  `repository.ias.ac.in/33549/1/33549.pdf`) -- confirmed as a genuine,
  on-topic primary paper introducing exactly this family of `R/Z`-valued
  invariants built from `eta_A(0)` and kernel-related corrections
  (`eta~_alpha(0,A) in R/Z`, its intro states). **The literal `(h+eta)/2`
  formula's canonical page was NOT read verbatim from a primary source**
  (Part III's introduction defines a twisted version for this exact
  purpose but with a different, `alpha`-flat-bundle-dependent
  construction; the untwisted `xi=(h+eta)/2` boundary-correction form more
  likely lives in Part I, 1975, which was not successfully retrieved as
  readable text -- paywalled/scanned).

`[CITED, MEDIUM confidence]`: the formula used here (and by C121's own
skeptic pass, matching exactly) is corroborated by ≥3 independent secondary
sources plus confirmed existence of an on-topic primary paper, but not by a
verbatim primary-source read of the specific equation. This is disclosed
honestly rather than marked `[VERIFIED]` (would need the literal primary
page) or presented as invented (`[SPECULATIVE]`) -- it is not invented,
it is the standard, widely-cited APS definition, evidenced short of the
single strongest possible citation.

## 12. FL Step 8a -- skeptic pass (context-blind, self-administered)

Per claim.md's instruction, reviewed after the full first draft was
complete, as if seeing only claim.md + this decision.md + the code (not the
derivation process). Actively tried to falsify the central conclusion,
focused on claim.md's three named risk areas plus anything else found.

| # | Finding | Severity | Disposition |
|---|---|---|---|
| S1 | Does the round use AT-the-point crossing values, or one-sided limits (C121's own first-draft mistake)? | Would be fatal if wrong | **Checked, correct.** §4 derives the AT-the-point convention from the definition (excluding zero eigenvalues), not by copying C121's number; route (i) [direct average] and route (ii) [closed-form] agree exactly at all 6 primary crossings, and both reproduce C121's own certified `eta_at(t=1)=+1/2`. |
| S2 | Is any `check()` call unfailable regardless of its argument? | Would undermine every PASS if present | **Two found and fixed, both self-caught before this document was drafted, not by an external reviewer.** (i) A first draft had `check(name, True if recurs_at else True, ...)` -- syntactically dodges the AST self-audit's literal-`Constant` test (it's an `IfExp`, not a `Constant`) while being semantically unfailable either way. Removed; replaced with a genuine failable check on pair-distinctness (§9), which correctly FAILS. (ii) An f-string bug (`{{...}}` double-brace escaping) silently printed literal source text instead of the computed `pair_by_n` dict as a check's detail string -- a reporting bug, not a math bug, but exactly the kind of thing that could hide a wrong result behind a plausible-looking message; fixed, verified the printed detail now shows real computed values. |
| S3 | Is the `mod 1` reduced-eta definition confirmed against a real citable source, or invented? | Would violate claim.md's explicit instruction if invented | **Not invented; not fully `[VERIFIED]` either.** §11's literature search found strong converging secondary corroboration and a confirmed genuine primary paper (APS III), but not a verbatim primary-source equation read. Marked `[CITED, MEDIUM confidence]` rather than overclaimed as `[VERIFIED]`. |
| S4 | Is `h(t)=mu(n)` at `t in {0,1}` an independently-confirmed number, or only asserted from C121's own abstract table (single source)? | Could weaken confidence in the central table if `h` were wrong | **Cross-checked against an independent, project-wide-certified source** (§5): `h(0)=2` matches round73/C27/round78/round83/round85/round92/round93's UNCONDITIONAL explicit-construction result; `h(1)=2` matches round76's explicit construction, but that construction needed an extra calibration (`c0=-2`) round73's `t=0` construction did not. Named honestly as an asymmetry in construction difficulty, not a numeric discrepancy -- and (critically) the central NULL result (§7-8) does not depend on the specific numeric value of `mu(n)` at all, only on `h(t)` being IDENTIFIED with the crossing multiplicity that generates `eta`'s own jump, which is forced by self-consistency with C121's already-certified formula, not a free input this round could get wrong independently. |
| S5 | Does kill criterion (a) as LITERALLY worded ("identical... across every crossing") actually fire, given the table shows different numbers? | Could make the verdict look self-contradictory if not addressed head-on | **Addressed explicitly in §10, not glossed over.** The literal wording does not fire; the deeper request (show the cancellation mechanism algebraically) does, and criterion (b) independently fires on the "no stated structural meaning" test. This is stated as a genuine wording mismatch between claim.md's anticipated NULL shape (copied from C121's raw-eta precedent) and this round's actual (different, but equally clean) NULL mechanism -- not hidden. |
| S6 | Could the `n=0`/`n=3` pair-recurrence (§9) itself BE the interesting result, inverted -- i.e. is there a real period-3-like structure worth flagging as a pearl in its own right? | Low -- speculative, not this round's claim | **Named, not chased.** §9 explicitly declines to explain the recurrence, since (i) it is not needed for the verdict, (ii) a cubic polynial's fractional part at a linear lattice recurring is unremarkable without a further argument this round does not have time to build, and (iii) chasing it risks exactly the kind of premature-pattern-matching this project's culture warns against. Not proposed as a pearl (see §15) -- if it recurs it undermines, rather than supports, "n=0 is special," so it is evidence FOR this round's own NULL, not a new candidate. |

**Verdict of the skeptic pass: `[CONFIRMED-REAL]` with two self-caught,
pre-draft defects disclosed (S2) and one honest evidence-tier limitation
disclosed (S3) rather than overclaimed.** The central conclusion (xi mod 1
is algebraically continuous, no crossing including `t in {0,1}` is
distinguished) did **not** change direction under this pass -- per claim.md's
own instruction, a second, differently-worded pass is required only if the
verdict's direction would change or an unresolved convention question
remains open. Neither applies (S3's limitation is disclosed, not
unresolved-and-blocking; nothing here reverses NULL to PROMOTE or vice
versa) -- **a second pass is not run**, per claim.md's own stated threshold.

## 13. Kill Analysis (Anti-Overfitting Gate discipline)

**What this round kills:** pearl row 116's specific falsifiable prediction
-- that `h(t)`'s non-constant jump (`2,6,12,...` across crossings) would
break the symmetry that made raw `eta mod 2` featureless, producing a
genuine, distinguished value or discontinuity at `t in {0,1}`. It does not:
the SAME non-constancy that was hoped to break the symmetry is EXACTLY what
makes `(eta+h)/2 mod 1` well-defined and smooth (§7), the reduced eta
invariant's own textbook design purpose (§11). This is not merely observed
numerically -- it is proven for the whole family (`n=0..5` computed, and the
proof in §7 is manifestly `n`-independent, so it holds for every `n`, not
just the ones computed).

**What is NOT killed:**
- `P(a)` itself, the `dP/da` identity, `eta mod 2`'s NULL -- C121's own
  results, untouched, only reused.
- The eta-invariant / gravitational-Chern-Simons family as a WHOLE is not
  exhausted -- only the raw (`mod 2`) and reduced (`mod 1`) forms of THIS
  specific spectral quantity. Neither pearl row 115 nor 116 named any
  further un-attempted eta-invariant variant; none is proposed here either.
- `h(1)=2`'s explicit-construction asymmetry (§5, §12 S4) -- a real,
  specific, named gap, not resolved by this round, proposed as a Pearl
  entry (§15).

**Relaxation Map** (none attempted this round):

| Assumption relaxed | What it would take | Status |
|---|---|---|
| Look at a DIFFERENT reduction of `eta`+`h` (e.g. mod 4, or a different combination entirely) | Would need an independent argument for why some OTHER combination is the physically/mathematically meaningful one -- APS's own `xi=(h+eta)/2 mod 1` is already the standard, citable choice (§11); no candidate reason to look elsewhere | Not attempted; no candidate reason identified |
| Full spectral-flow formal integer (not the finite-correction AT-the-point convention used here) | C121 itself already found this unnecessary for the raw-eta question (its own finite-correction approach answered the same question); the same logic applies here, since §7's proof is exact, not an approximation the formal machinery would sharpen | Superseded, as in C121 |
| Resolve the `h(1)=2` construction asymmetry (§5) -- does round67's abstract multiplicity table at `t=1` genuinely not need `c0=-2`, or does it inherit that dependency invisibly? | Would require tracing round67's own derivation of `mu(n)` back to its source and checking whether it is independent of the `c0` convention round76 needed for the EXPLICIT construction -- out of this round's scope (claim.md instructs reuse, not re-derivation, of round67's table) | Not attempted; proposed as a Pearl (§15) |

## 14. What this round does NOT show

- Does NOT reopen C121's own already-closed NULL on raw `eta mod 2` -- that
  question stays closed, untouched.
- Does NOT reopen C123-C137's verdicts.
- Does NOT change `N_gen=3`'s CONDITIONAL status, `lambda =
  FREE_COUPLING_PARAMETER`, `sm_derivation_claimed = False`, or
  `safe_for_runtime = False`.
- Does NOT close H1c, OB1, or round95's own diagnosed gap -- this closes one
  more F4/F6-shaped candidate among several still needed
  (`PARENT_ACTION_GATE.md` F4/F6), the same status C121 itself had.
- Does NOT claim the `mod 1` convention was invented here -- §11 states
  explicitly what was and was not confirmed against a primary source.
- Does NOT resolve the `h(1)=2` construction-asymmetry caveat (§5, §13) --
  named, not settled.
- Does NOT solicit Tom Lawrence's Part 5.

## 15. Registry actions -- NOT performed by this round, proposed only

This round does not edit `PARENT_ACTION_GATE.md`, `OPEN_BLOCKERS.md`,
`null_results/INDEX.md`, `pearl_registry/INDEX.md`, or
`.claude/memory/activeContext.md`. Proposed exact wording:

**`null_results/INDEX.md`** new row:

```
| C138-ReducedEtaInvariant | 2026-09-03 | aps-reduced-eta-invariant | REJECT | Tested pearl row 116's own falsifiable prediction: does the APS reduced eta invariant xi(D^t)=(eta(D^t)+h(t))/2 mod 1 show a special value or discontinuity at t in {0,1} that raw eta (C121, NULL) did not? Answer: no -- proven algebraically, not just observed numerically. h(t)'s own non-constant jump (mu(n)=(n+1)(n+2), 2/6/12/... across crossings, the exact mechanism row 116 hoped would break the symmetry) is EXACTLY what cancels eta's discontinuous 2*mu(n) jump under division by 2, making xi mod 1 a smooth, continuous function of t equal to P(a)/2 mod 1 EVERYWHERE (a=3(t-1/2), P(a)=a(3-4a^2)/6 C121's own certified closed form), with no special feature at any crossing including t in {0,1}. Verified via two independent eta-at-crossing routes (direct average-of-limits and closed-form shortcut, agreeing exactly), an explicit continuity proof (near/at/far-limit xi mod 1 all match at every crossing), and a duplicate-value check showing t=0,1's own {1/4,3/4} pair recurs exactly at the n=3 crossing pair -- further evidence against, not for, any t in {0,1} privilege. h(t) cross-checked against an independent, project-wide-certified kernel-dimension result at t=0 (round73, unconditional); h(1)=2 also independently confirmed but via a construction needing an extra calibration (c0=-2) t=0's did not -- named as an open, unresolved caveat, not load-bearing for the NULL verdict itself. See experiments/20260903-c138-aps-reduced-eta-invariant/decision.md for the full derivation, literature check, and skeptic pass. |
```

**`pearl_registry/INDEX.md`** -- close row 116 (append to its existing row,
matching the style C121 used to close row 115):

```
**RESOLVED, C138 (2026-09-03), NULL, algebraically proven.** This row's own falsifiable prediction is FALSE: h(t)'s non-constancy does not survive division by 2 -- it is exactly what the standard APS reduced-eta construction uses to cancel raw eta's own 2*mu(n) jump, leaving xi mod 1 = P(a)/2 mod 1 smoothly everywhere, t in {0,1} included. Both the eta-invariant/gravitational-Chern-Simons family's raw (row 115, C121) and reduced (this row, C138) forms are now closed for the same underlying reason: nothing in this construction singles out n=0. See null_results/INDEX.md C138-ReducedEtaInvariant.
```

**`PARENT_ACTION_GATE.md`** F4 "already tried" list, one-line addition (same
style as C121's own entry): *"APS reduced eta invariant xi=(eta+h)/2 mod 1
(C138) -- algebraically NULL, h(t)'s jump exactly cancels eta's, no crossing
distinguished."*

**Pearl (new, from §5/§12 S4)**: *observation:* `dim ker(D_{S3,t=1})=2` is
independently confirmed (matching `mu(0)=2`) but ONLY via a construction
(round76's right-invariant frame) needing an extra calibration input
(`c0=-2`) that `t=0`'s construction (round73's naive constant-spinor
ansatz) did not need -- an asymmetry in construction difficulty across the
two endpoints this project's `t`-selection program treats as a symmetric
pair. *falsifiable_prediction:* if round67's abstract Peter-Weyl
multiplicity table `mu(n)` (which C121's and this round's `eta`/`xi`
formulas are built from) turns out to itself depend on `c0` at `t=1` in a
way not shared at `t=0`, some already-certified "symmetric" spectral
results (crossing multiplicities, `eta`'s own jump structure) may carry a
hidden asymmetry not currently flagged anywhere. *impact_score:* 4 (narrow
-- touches the specific `t=0` vs `t=1` symmetry assumption underlying
several rounds' multiplicity tables, not the whole project).
*trigger_condition:* any future round that needs to trust round67's
multiplicity table's `t=1` value at a precision finer than "the dimension
is 2" (e.g. an exact eigenvector/eigenspace construction at `t=1`).
*next_check:* the next round that explicitly builds on round67's
multiplicity table at a crossing other than `t=0`.

## 16. Verification

- `python -m ruff check experiments/20260903-c138-aps-reduced-eta-invariant/`
  -- clean (one `UP031` percent-format finding fixed during drafting, before
  this document was written).
- `c138_reduced_eta_invariant.py` -- **21 distinct boolean check names from
  16 call sites, 20 PASS, 1 intentional FAIL** (the honesty check in §9,
  which is SUPPOSED to fail and would be a red flag if it passed -- a
  passing "every pair distinct" check would silently hide the `n=0`/`n=3`
  recurrence that is itself part of the evidence for NULL). AST self-audit
  confirms no `check()` call is passed a literal constant.
- Two real defects self-caught and fixed BEFORE this document was written
  (not found afterward by an external reviewer): an unfailable check that
  dodged the AST self-audit syntactically (§12 S2), and a factor-of-2 error
  in a contrast-check's own expectation (raw eta jumps by `2*mu(n)`, not
  `mu(n)` -- caught against the script's own printed near/far-limit values
  on first run, before any claim about it was written down).
- Both load-bearing numeric routes (average-of-limits vs closed-form; direct
  `(eta_at+h)/2 mod 1` vs the `P(a_c)/2 mod 1` algebraic shortcut) agree
  exactly at every crossing checked -- the "verify from at least two angles"
  discipline applied throughout, not just once.
- Repo-wide test suite not run (no shared code touched; only new files
  inside this experiment's own directory).

---

## Evidence tier of the central conclusion

**Central conclusion:** *the APS reduced eta invariant `xi(D^t)=(eta(D^t)+
h(t))/2 mod 1`, computed at the first six crossing pairs of the certified
S3 torsion-deformed Dirac operator family, is algebraically continuous (mod
1) through every crossing, equal everywhere to `P(a)/2 mod 1` for C121's own
certified `P(a)`, with no discontinuity, special value, or distinguishing
feature at `t in {0,1}` relative to any other crossing or any other point
of the domain.*

**Tier: `[VERIFIED-tool]`, confidence HIGH** for the mathematics -- 20 of 21
machine checks PASS (the 1 FAIL is an intentional, correctly-firing honesty
check, not a defect), exact sympy `Rational` arithmetic throughout (no
floating point in any load-bearing comparison), the central cancellation
proven algebraically (not merely observed at the 6 primary crossings) and
independently corroborated by a direct continuity check using a completely
different computational route, two self-caught defects disclosed and fixed
before this document was drafted, and the `h(t)=mu(n)` input cross-checked
against an independently-certified project result at `t=0`.

**Tier of the `mod 1` definition itself: `[CITED, MEDIUM confidence]`** --
converging secondary sources plus a confirmed genuine primary paper, but not
a verbatim primary-source equation read (§11). Does not affect the
mathematics tier above, since the SAME `xi=(eta+h)/2` formula this round
uses is exactly what claim.md and C121's own skeptic pass already specified
-- this round's contribution is the computation, not the definition.

**Tier of the `h(1)=2` construction-asymmetry caveat: `[VERIFIED-tool via
grep]` that the asymmetry exists in the project's record; `[UNKNOWN]`
whether it has any bearing on round67's abstract multiplicity table** --
named, not resolved, does not weaken the central conclusion's tier (§12 S4
explains why the NULL result is structurally independent of this specific
numeric detail).

**Marker on the whole round: none required** -- no skeptic pass returned
`WEAKENED` or `FALSIFIED` on the central conclusion; the one open item
(`h(1)=2` construction asymmetry) is disclosed as a caveat on a
non-load-bearing input, not a qualifier on the verdict itself.
