# C170 — Decision

**Date:** 2026-09-06
**Verdict:** **Mixed, co-firing per claim.md's own allowance:**
`EXPLICIT-VECTOR-EXTRACTED-AND-EIGENVALUE-COMPUTED` for **`t=0` only**, plus
`BLOCKED-BASIS-MISMATCH` for **`t=1`** (a genuine, found holonomy-convention
discrepancy, not merely a suspected one), plus **`CHEAPER-THAN-EXPECTED` for
`t=0`** and **`NOT-CHEAPER-THAN-EXPECTED` for `t=1`** — the skeptic's C169
§10a lead ("item 1 may be cheaper than a full round") is **confirmed for
half the task and not for the other half**.
**Independent skeptic pass (2026-09-06, strict Context Asymmetry): `CONFIRMED-REAL`** -- see Section 12a below.
**Go/no-go:** This round supplies a genuinely new, `[VERIFIED-tool]` result
(the explicit `t=0` kernel, and a concrete, checked `t=1` candidate with an
honestly-reported convention gap) — but does **not** complete C169's overall
escalation (§5 items 2–3 remain untouched and `BLOCKED-NEEDS-NEW-MACHINERY`),
and the `t=1` half of even item 1 alone is not yet fully certified.

---

## 0. Summary, before the detail

C169 named item 1 of its 3-item escalation as: build `ker(D_S3(t))` as an
**explicit vector**, not merely "an eigenvalue of 0 exists" (round72/E7,
round67/E2). This round did the actual construction, all steps checked by
direct sympy computation (`c170_explicit_ker_ds3.py`, `results_c170.json`),
not asserted from memory or by analogy:

1. **`t=0`: fully done, cheap, rigorous.** The explicit kernel is **any**
   vector in `C²` — literally the full 2-dimensional space of constant
   spinors `psi(g)=psi_0`. This follows in one line from Agricola's own
   eq.(5) (already cited by E2): `D^0(constant psi) = 0·H·psi = 0` for any
   constant `psi`, no new machinery needed beyond reading the formula at
   `t=0`. `[VERIFIED-tool]`, Step 3.

2. **`t=1`: substantial new derivation was required, not a short mechanical
   step.** Building the analogous explicit vector required (a) deriving the
   spin-connection matrices `M_i(t)` implied by Agricola's `Nabla^t_XY=t[X,Y]`
   — new to this project, self-consistency-checked against eq.(5)
   `[VERIFIED-tool]`, Step 2; (b) identifying the abstract structure-constant
   generator `Z_i` with a concrete `su(2)` matrix `e_i`, where the sign is
   **forced** (not a free choice) by the project's own calibrated `c=2` —
   checked both signs explicitly, only `e_i=-i*sigma_i` works,
   `[VERIFIED-tool]`, Step 4a; (c) a genuine ansatz-construction step
   (`psi_1(g):=g^{-1}.psi_0`, "defining representation composed with
   inversion") that turned out to satisfy the parallel-transport PDE exactly
   — but only after resolving what first looked like a real sign
   inconsistency by hand (documented honestly below, §5) and confirming it
   symbolically, `[VERIFIED-tool]`, Step 4b.

3. **A genuine basis/convention mismatch was found, not assumed.** The
   candidate `psi_1(g)=g^{-1}.psi_0`'s own derived holonomy under the
   deck transformation `g -> zeta_p.g` is `zeta_p^{-1}`, **not** `zeta_p` as
   C168 modeled `H_1`. `zeta_p^{-1} != zeta_p` as matrices (only their
   eigenvalue *sets* coincide), `[VERIFIED-tool]`, Step 5. This means C168's
   own `H_1=zeta_3` cannot be applied to this specific candidate vector's
   transformation law as-is without further work — reported honestly as
   `BLOCKED-BASIS-MISMATCH`, per the task's own explicit permission to do so
   rather than force a number past it.

4. **The literal task item 4 question, read at the level the vectors
   actually live in (`H_t` alone, not `H_t (x) tau`), has a clean,
   convention-independent answer, `[VERIFIED-tool]`, Step 6:** at `t=0`,
   every vector trivially has `H_0`-eigenvalue 1 (`H_0=I`, C168's own
   *modeling assumption*, not independently derived — so this is vacuous,
   not informative). At `t=1`, **no** vector — regardless of which specific
   `psi_1` candidate is used, and regardless of the `zeta_p` vs `zeta_p^{-1}`
   ambiguity in item 3 above (both have the *same* eigenvalue set) — can
   ever have `H_1`-eigenvalue exactly 1, because `zeta_3`'s eigenvalues are
   the two non-trivial cube roots of unity, neither equal to 1. This is a
   real, checked, convention-independent answer, not left open.

---

## 1. Step 1–2 — self-consistency of the new spin-connection derivation
`[VERIFIED-tool]`

Rebuilt E2's Clifford generators `Z_i=i*sigma_i` fresh and re-confirmed
`omega=Z1.Z2.Z3` is exactly `I2` (matches E2's own already-published result,
not copied — recomputed). Derived the connection matrices
`M_i(t) := (1/4) sum_{j,k} Gamma^t_{ijk} Z_j Z_k`, `Gamma^t_{ijk}=t*c*eps_ijk`
(the general formula for the spin connection of a metric connection with
antisymmetric connection coefficients, applied here for the first time in
this project to Agricola's `Nabla^t_XY=t[X,Y]`). The critical
self-consistency check — does `sum_i Z_i.M_i(t)` reproduce eq.(5)'s own
`t*H` term (`H=(3c/2)*omega=(3c/2)*I`)? — **passes exactly**:
`sum_i Z_i.M_i(t) = (3ct/2)*I2 = t*H`, confirmed symbolically for generic
`t,c` (`results_c170.json`, `step2_connection_self_consistency.
matches_eq5_H_term = true`). Without this check passing, nothing downstream
about `M_i(t)` could be trusted (this script's own internal Substrate Gate);
it passed on the first correct attempt (after fixing a Levi-Civita-symbol
sign slip caught by the check itself during script development — see §7).

## 2. Step 3 — `t=0` kernel, cheap and certified `[VERIFIED-tool]`

`M_i(0)=0` for all `i` (immediate, `M_i(t)` is linear in `t`), so
`Nabla^0_{Z_i}psi = Z_i(psi)` and the parallel condition at `t=0` reduces to
"`psi` is a constant function on `SU(2)`" — **any** nonzero vector in `C²`
qualifies, giving the full 2-dimensional kernel explicitly, e.g.
`psi_0_A=(1,0)^T`, `psi_0_B=(0,1)^T`. This required zero new machinery beyond
reading eq.(5) at `t=0` — genuinely the cheap half of item 1, confirming
half of C169 §10a's skeptic lead.

## 3. Steps 4a–4b — `t=1` candidate, real derivation, self-consistent
`[VERIFIED-tool]`

**4a — the sign is forced, not chosen.** Checked both `e_i=-i*sigma_i` and
`e_i=+i*sigma_i` against the requirement `[e_1,e_2]=c*e_3` at the project's
own calibrated `c=2` (E2's h_H=3=(3/2)c). Only `e_i=-i*sigma_i` satisfies
this exactly (`[e_1,e_2]` matches `2*e_3` for the minus sign, and manifestly
fails — off by an overall sign — for the plus sign). This resolves what a
first hand-derivation attempt (mid-session, not in the final script)
initially flagged as a possible genuine obstruction — it turned out to be
resolvable, but only by tracking this sign correctly, not by assumption.

**4b — the candidate satisfies the parallel-transport PDE exactly.** With
`psi_1(g) := g^{-1}.psi_0` (matrix inverse of `g` in `SU(2)`, any fixed
`psi_0 in C²`), elementary calculus of the matrix inverse gives
`Z_i(psi_1) = -e_i.psi_1` identically (no representation-theoretic
assumption beyond the `e_i` identification just fixed). Checked directly,
for all three `i`, against the *required* condition
`Z_i(psi)=-M_i(1).psi` (the parallel condition `Nabla^1_{Z_i}psi=0`): **all
three match exactly** (`results_c170.json`,
`step4b_t1_parallel_condition_check.all_i_match = true`). This is a genuine,
non-trivial construction — it required identifying the correct sign twice
(once for `e_i`, once implicitly in the inverse-vs-identity ansatz choice: a
naive `psi_1(g)=g.psi_0` ansatz does **not** give a `g`-independent PDE
coefficient at all and was rejected during derivation, not tested in the
final script) — genuinely more than "a short mechanical step," confirming
the other half of C169 §10a's lead (that this might turn out cheaper) was
**too optimistic** for `t=1` specifically.

## 4. Step 5 — a real, checked basis/holonomy mismatch, not assumed
`[VERIFIED-tool]`

The candidate family `psi_1[psi_0](g):=g^{-1}.psi_0` transforms under the
deck map `g -> zeta_p.g` as `psi_1[psi_0](zeta_p g) = psi_1[zeta_p^{-1}
psi_0](g)` — i.e. the family maps to itself via `psi_0 -> zeta_p^{-1}.psi_0`.
Evaluated at the basepoint, this means the derived holonomy for this
specific candidate is `zeta_p^{-1}`, not `zeta_p` as C168 modeled `H_1`.
Checked directly: `zeta_p^{-1} != zeta_p` as matrices (`step5.
zeta_p_inverse_equals_zeta_p = false`) — they are not the same operator,
only their eigenvalue *sets* coincide (`{omega,omega^2}` either way).

**This means C168's own T5/T6 eigenvector computation (which basis vector
of `H_1=zeta_3` pairs with which channel) cannot be reused verbatim for
`psi_1` as constructed here** — it would need to be redone with
`H_1'=zeta_p^{-1}`, or the ansatz itself re-derived to target `zeta_p`
directly (e.g. investigating whether `psi_1(g)=g.psi_0` can be rescued with
a different, `g`-dependent bookkeeping than the naive attempt rejected in
§3). **Neither was attempted this round** — reported as
`BLOCKED-BASIS-MISMATCH`, honestly, per the task's own explicit instruction,
rather than silently patched by picking whichever sign makes the numbers
line up (a real risk this project's own methodology — the `research-
methodology.md` classifier's "Type 1: symbolic overload" and this project's
"DERIVED vs FITTED" discipline — explicitly warns against).

## 5. Step 6 — the literal task item-4 question, answered where it is
well-posed `[VERIFIED-tool]`

Read narrowly (does `H_t` alone, not `H_t (x) tau`, fix `psi_0`/`psi_1` with
eigenvalue 1?) rather than the full three-tensor-factor question (which
needs C169 §5 items 2–3, out of scope here):

- **`t=0`:** `H_0=I2` (C168's own explicit **modeling assumption**, not
  independently derived from the frame holonomy) has eigenvalue 1 for
  *every* vector — so yes, trivially, but this is **vacuous**: it says
  nothing specific about `psi_0` being a `D_S3(0)`-kernel vector, since it
  would hold for any vector whatsoever.
- **`t=1`:** `H_1=zeta_3` has eigenvalues `{omega,omega^2}` (the two
  non-trivial cube roots of unity), **neither equal to 1**
  (`step6.H1_has_eigenvalue_1 = false`, confirmed symbolically). Hence **no**
  vector — independent of exactly which `psi_1` candidate is used, and
  independent of the `zeta_p` vs `zeta_p^{-1}` ambiguity of §4 (both share
  the same eigenvalue set) — can ever be an `H_1`-eigenvalue-1 eigenvector.

This is a genuine, checked, convention-independent finding: **at the bare
`H_t` level (not tensored with `tau`), the `t=1` "survives the ℤ₃ quotient"
question has a clean NO**, regardless of how the §4 basis-mismatch is
eventually resolved. It does not, by itself, say anything about the
`H_t (x) tau` question C168 already answered generically (§6 below).

## 6. Relation to C168's own result — no re-litigation

C168's own T7/T8 generality check already showed that the `H_t (x) tau`
classification (dim-2 invariant subspace, all three channels participate)
is **forced by `tau` alone**, for **any** order-3 (or even identity) `H_1`.
This round's `t=1` candidate, being *some* concrete vector living in the
same `C²` `H_t` acts on, does not change that generic result — C168's own
conclusion (§6, C169 decision.md §4) that the "three copies" fallback
carries no new discriminating weight beyond C168 stands **unaffected**. This
round is about supplying the concrete `S³`-side input for a *future*,
still-`BLOCKED`, full three-factor construction (C169 §5 items 2–3) — not
about revisiting the tensor-product classification itself.

## 7. Honesty note on process (Hindsight Distortion Gap discipline)

The `t=1` derivation in §3–§4 involved a mid-derivation hand-algebra attempt
(done before writing the final script) that initially appeared to hit a real
sign inconsistency (an incorrectly-normalized ansatz gave a bracket mismatch
`[A_1,A_2] != c.A_3`). On redoing the derivation more carefully by hand, and
then confirming by direct sympy computation in the final script, the
inconsistency turned out to be a bookkeeping error in that earlier attempt,
not a genuine mathematical obstruction — the corrected construction (§3–§4)
passes all its own self-consistency checks. This is recorded here (per the
Hindsight Distortion Gap Heuristic: the record is written the same session
as the derivation, not reconstructed later) so that a future reader does not
mistake the smoothness of the final write-up for the actual difficulty of
getting there — this construction is genuinely non-trivial, not a one-line
lookup, which is itself part of the honest answer to C169 §10a's "may be
cheaper" lead.

---

## 8. Kill Analysis (Perelman/OSA discipline)

**What this round kills:**
1. The unqualified version of C169 §10a's lead ("item 1 may be cheaper than
   a full round") — **true for `t=0` only**, false for `t=1` as a "short
   mechanical step" (real new derivation was needed, even though it
   ultimately succeeded).
2. Any implicit assumption that `H_1=zeta_3` (C168's own convention) applies
   directly to whatever explicit `t=1` vector construction one might pick —
   this round's own candidate demonstrates a concrete counter-example
   (derived holonomy is `zeta_p^{-1}`, not `zeta_p`).

**What this round does NOT kill:**
1. The `t=1` explicit-vector goal itself — a valid, self-consistent
   candidate (`psi_1(g)=g^{-1}.psi_0`) was found and verified against the
   parallel-transport PDE; only its match to C168's *specific* holonomy
   convention remains open.
2. C169's own overall verdict — `CHANNEL-STRUCTURE-MAKES-QUESTION-
   ILL-POSED` + `BLOCKED-NEEDS-NEW-MACHINERY` for the FULL escalation stands
   unchanged; items 2 and 3 of C169 §5 are entirely untouched.
3. C168's own T5–T8 results — untouched, re-cited only.

**Relaxation Map (if a future round pursues the `t=1` gap further):**
- Remove: the assumption that C168's literal `H_1=zeta_3` (as already
  coded) can be applied without modification to any candidate `t=1` vector
  construction — shown false for this round's own candidate.
- Weaken: none needed — the `t=0` half of item 1 is reported at its true
  (fully certified) strength, and the `t=1` half at its true (candidate,
  convention-open) strength.
- Replace: the correct next assumption to relax, per the Minimal Relaxation
  Rule, is to attempt ONLY the holonomy-convention reconciliation next (does
  `H_1'=zeta_p^{-1}` reproduce a dim-2 invariant-subspace-with-all-channels
  classification identical to C168's, by the SAME T7-style generality
  argument — plausible, since `zeta_p^{-1}` is also order-3 with the same
  eigenvalue set, but not yet checked) — a small, well-scoped, single-focus
  follow-up, not a full new round, and not bundled with items 2 or 3.

---

## 9. Floor–Ceiling Interval (FL Step 4a) — reasoned through

This round's result is a mixed construction/existence verdict, not a
continuous metric, so Floor–Ceiling applies in spirit: the "floor" is the
null check that the construction was already trivial/vacuous throughout
(checked directly and did NOT fire for `t=0` beyond the already-known
"any constant vector" — genuinely the simplest possible non-trivial answer,
not an artifact) — nor for `t=1`, where a real obstruction was found and
worked through, not sidestepped. The "ceiling" would be a fully-certified,
convention-matched `t=1` vector applied through the complete `H_t (x) tau`
construction and combined with round59's kernel per C169 §5 items 2–3 — not
attempted, explicitly out of scope. No single efficiency ratio is
meaningful here; the discriminating content is the honest split between the
cheap (`t=0`) and non-cheap (`t=1`) halves.

---

## 10. What this does NOT mean

1. Does NOT complete C169's escalation — items 2 (`Cl(9)` twisted `D_S6`)
   and 3 (`SU(3)`-to-triality basis bridge) remain entirely untouched and
   `BLOCKED-NEEDS-NEW-MACHINERY`.
2. Does NOT license combining this round's `S³`-side vectors with round59's
   actual kernel vector into a genuine `ker(D_full)` on `S³×S⁶` — that
   composition needs items 2–3, not attempted here.
3. Does NOT establish that the `t=1` candidate (`psi_1(g)=g^{-1}.psi_0`) is
   the UNIQUE or even the physically-preferred explicit construction — it is
   ONE self-consistent candidate found this round; a differently-parametrized
   ansatz might match C168's `H_1=zeta_3` convention directly without the
   found mismatch (not attempted).
4. Does NOT change C168's own T7/T8 generic classification result (dim-2,
   all-channels-participate, forced by `tau` alone) — re-cited only, not
   re-derived or contradicted.
5. Does NOT resolve OB1 or reopen P4 beyond the scope C169 already
   described — `PARKED — REOPEN ONLY ON NEW EXTERNAL INPUT` for OB1 stands
   unchanged; this round is confined to C169's own named escalation item 1.
6. Does NOT claim the `H_t`-alone eigenvalue-1 answer (§5, Step 6) settles
   the physically meaningful `H_t (x) tau` survival question — that remains
   C168's own already-answered (and, per C169, low-discriminating-weight)
   result; §5/Step 6 here answers a narrower, literal reading of the task's
   own item 4 wording, reported separately and explicitly as such.

---

## 11. Verification substrate (FL Step 2a, abbreviated)

This round performed new symbolic (sympy) computation, not merely grep/read
verification of prior results (unlike C169). All load-bearing claims in
`c170_explicit_ker_ds3.py` are checked by direct `sympy` symbolic equality
(`sp.simplify(... ) == sp.zeros(...)` or equivalent), not floating-point
approximation, and the full script + `results_c170.json` output are
committed alongside this decision. No blocked-infrastructure or
untrusted-environment issue was encountered; sympy was already an installed,
already-used dependency throughout this project (E2, E7, C167, C168 all use
it identically). READY.

---

## 12. Recommendation on independent skeptic pass

**Yes, recommend a skeptic pass**, for reasons specific to this round:

1. The `t=1` construction (§3–§4) is the single most load-bearing NEW claim
   this round makes — a multi-step derivation (spin-connection formula,
   forced-sign identification, inverse-ansatz calculus) with several places
   a sign error could hide despite the self-consistency checks passing. A
   skeptic should independently re-derive at least one step (e.g. the
   `M_i(t)` formula itself, or the `d/ds(g.exp(sZ_i))^{-1}=-Z_i.g^{-1}`
   calculus fact) from scratch, context-blind, to confirm it is not an
   internally-consistent but externally-wrong construction (self-consistency
   checks catch *some* errors, not all — e.g. a globally-flipped overall
   sign convention could pass every check here and still be wrong relative
   to Agricola's own stated orientation convention, which this round did not
   re-verify against the PDF directly).
2. The §5 `BLOCKED-BASIS-MISMATCH` finding (`zeta_p^{-1}` vs `zeta_p`) is a
   genuinely new claim about C168's own construction, not previously
   flagged anywhere in this project's history (confirmed by this session's
   own grep) — worth independent confirmation before being treated as
   settled, since it bears on whether C168's own `H_1=zeta_3` choice was
   itself an arbitrary convention pick that happens not to match the most
   natural explicit-vector construction.
3. Per the Paraphrase-Sensitivity Probe guidance (high-stakes PROMOTE claims
   only) — this round is NOT a PROMOTE of a headline claim (it stays mixed/
   partial), so the double-Skeptic-run probe is not required by cost
   discipline; a single Context-Asymmetric skeptic pass (claim.md + the
   script, no reasoning chain) is the appropriate level here.

I have NOT run that skeptic pass myself this round (out of scope per the
task's own instruction to report back rather than continue the FL pipeline
autonomously).

---

## 12a. Update -- independent context-blind skeptic pass (orchestrating
     session, 2026-09-06), strict Context Asymmetry, verdict CONFIRMED-REAL

Ran an independent `Agent(skeptic)` pass: claim.md + script + results only,
this decision.md withheld. **Verdict: `CONFIRMED-REAL`** for all four
load-bearing algebraic claims -- the skeptic independently hand-derived
`sum_i Z_i.M_i(t)=t*H` (tracing `Z_j Z_k=-(delta_jk*I+i*eps_jkl*sigma_l)`
through to `(3tc/2)*I`, confirming no missing factor could hide behind
the check), the `e_i=-i*sigma_i` bracket computation, the
`Z_i(g^{-1}psi_0)=-e_i.psi_1` calculus fact (direct flow-derivative
computation), and the `zeta_p^{-1}` holonomy result (elementary group
theory, `(AB)^{-1}=B^{-1}A^{-1}`) -- all confirmed exactly, matching this
round's own numbers.

**One accepted framing correction, non-load-bearing.** The skeptic found
Section 3's "the sign is forced, not chosen" (Step 4a) slightly
overclaims: the bracket condition `[e_1,e_2]=c*e_3` alone is satisfied by
FOUR Weyl-related sign patterns (not requiring all three signs identical),
not just the two uniform choices this round checked -- "forced" holds only
under the (reasonable, and ultimately the one that matters) UNIFORM-sign
convention this round implicitly assumed. **What actually pins the sign
uniquely, per the skeptic's own observation, is the STRONGER joint
constraint from Step 4b** (matching all three `M_i(1)` simultaneously,
not the bracket alone) -- a 3-equation system only the uniform `(-,-,-)`
choice satisfies. This round's own Step 4a and Step 4b TOGETHER already
supply this stronger justification (Step 4b was already computed and
reported, just not cited as the reason Step 4a's sign is truly unique) --
**no correction to the numeric result is needed**, only this framing
nuance, recorded here for completeness.

**Net effect: no change to the verdict.** The mixed verdict (t=0 done and
cheap; t=1 constructed but basis-mismatched against C168's own
convention) stands exactly as reported above.

---

## 13. Status

`experiments/20260906-c170-p4-step3-item1-explicit-ker-ds3/` — item 1 of
C169's escalation attempted in isolation. `t=0` explicit kernel: DONE,
cheap, certified. `t=1` explicit kernel: a self-consistent CANDIDATE
constructed and verified against the parallel-transport PDE, but with an
honestly-reported `BLOCKED-BASIS-MISMATCH` against C168's own `H_1=zeta_3`
holonomy convention. The literal task item-4 question, read at the `H_t`-
alone level, is fully answered (`t=0`: trivially yes, vacuous; `t=1`:
convention-independent no). C169's own overall verdict and items 2–3 remain
untouched. Registry files (`OPEN_BLOCKERS.md`, `pearl_registry/INDEX.md`,
`null_results/INDEX.md`, `CLAIM_LEDGER.yaml`) deliberately NOT touched by
this round, per the task's own scope boundary. No git operations run.
