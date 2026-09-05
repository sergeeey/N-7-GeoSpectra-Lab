---
# C162 Claim — scoping OB14's "why Sigma, not m" blocker: a cheap,
# hand-derived necessary-condition refinement of C142's BLOCKED-INTERNAL
# verdict, before any new geometric construction is attempted

**Date:** 2026-09-06
**FL tier:** [x] Full (touches OB14's central blocker; this file's own central
observation is this session's synthesis, not primary literature, so the
AI-Hypothesis Pre-Gates apply)
**Question type:** [x] descriptive (does pure `su(3)` representation theory,
combined with already-certified numeric facts, constrain `W_cand`'s behavior
in advance — or does it not)

**Mode:** This file is a SCOPING document only, per the orchestrating
session's explicit instruction: no computation, no construction attempt, no
decision.md. Its central content (Section "The argument," under Estimand/
Claim below) is a **hand-derived** (pen-and-paper, not tool-executed)
argument built entirely from already-certified project facts and standard
`su(3)` Clebsch-Gordan rules already used throughout this project's own
code — it is explicitly **not** `[VERIFIED-tool]` and must not be cited as
such until a future round runs the short verification script this file
proposes.

---

## 0. What OB14 and its `W_cand` sub-question are, precisely (fixed target)

`OPEN_BLOCKERS.md` OB14 ("why `Sigma`, not `m`, is the physically correct
twist for round59's `D_S6` construction") has, as of C142 (2026-09-04), an
**"Owner / next step"** that reads (quoted exactly): *"no internally-
buildable test remains identified... Remaining options are all higher-cost/
higher-risk: (a) a genuinely new, independently-motivated geometric
construction supplying a second copy of `3bar` (C142's named gap, high
AOG-5 risk without independent motivation), or (b) external input from Tom
Lawrence's own framework."*

This file's target is precisely: **before attempting (a) or (b), is there a
cheap, already-derivable-from-existing-content necessary condition that
narrows what KIND of new construction in (a) could possibly matter** — i.e.
does this project's own already-certified machinery (C139/C141/C143/C146/
C147) already say something about `W_cand=3⊕3̄⊕3̄`'s behavior, short of the
full construction C142 found blocked?

---

## Prior Result Gate (MANDATORY — filled BEFORE any future round computes
anything)

1. **Exact claim to check.** Read in full this session, from the primary
   `decision.md` files (not summaries): `experiments/20260904-c139-twisted-
   s6-alternate-representation-negative-control/decision.md` (1030 lines),
   `experiments/20260904-c141-matched-singlet-count-twist-m-plus-2singlets/
   decision.md` (1057 lines), `experiments/20260904-c142-graded-floor-
   candidate-scan/decision.md` (193 lines), `experiments/20260904-c143-
   graded-floor-equality-theorem/decision.md` (370 lines, including its
   2026-09-04 same-day addendum), `experiments/20260904-c144-kostant-cubic-
   dirac-identification/decision.md`, `experiments/20260904-c145-twisted-
   operator-vs-kostant-mu-block/decision.md`, `experiments/20260904-c146-
   schur-forced-vanishing-theorem/decision.md`. Also read `OPEN_BLOCKERS.md`
   OB14 section in full (lines 2229-2367) and `PARENT_ACTION_GATE.md`'s F2
   gate as amended by C143/C144/C145/C146/C147 (lines ~75-210).
   **Note on the task's own summary, corrected:** the task brief that
   initiated this file omitted C143 entirely — C143 is the round that
   first proved the `Delta_dyn` diagnostic (Lemma 1: `Hom`-dim-1 ⟹
   equality forced; Lemma 2: `Hom`-dim-`≥2` genuinely open, illustrated by
   a **hypothetical 2×2 toy example** unrelated to `W_cand`'s actual
   shape) and proposed the standing `PARENT_ACTION_GATE.md` F2 gate that
   was in fact adopted (verified this session: `PARENT_ACTION_GATE.md`
   lines 88-121 contain C143's gate verbatim). This file's own central
   contribution (Section "The argument," below) is precisely a Lemma-2-type
   analysis, but applied to `W_cand`'s **actual** `(2,1)` shape rather than
   C143's own hypothetical `(2,2)` illustration — see Section "Novelty
   Check" for why this distinction matters and was not previously made.
2. **Registry grep, done by hand this session**, for `W_cand`, `3+3bar+3bar`,
   `3̄⊕3̄`, "second copy", "independently-sourced" against
   `null_results/INDEX.md`, `parked/INDEX.md`, `pearl_registry/INDEX.md`,
   `OPEN_BLOCKERS.md`, `PARENT_ACTION_GATE.md`, and the full `experiments/`
   tree. Hits confined to C142/C143/C144/C145/C146's own rows (already read
   in full, item 1) and one `pearl_registry` row from C141 (also read).
   **No round has ever computed `W_cand`'s domain/target-side su(3)-
   branching structure explicitly enough to determine whether its escape
   route (`Delta_dyn>0`) survives combination with C146's `Term1≡0` theorem
   and C147's already-proven holomorphic non-vanishing of `m`'s own
   channel.**
3. `git log --all -S"W_cand" -S"3bar+3bar" -S"independently-sourced"
   -S"decoupled"`: **run this session** (not merely planned) — hits
   confined to the C142-C146 commits themselves (already read, item 1) and
   unrelated older commits (`decoupled` also matches several pre-2026-09
   commits on unrelated topics, checked and confirmed irrelevant by
   inspection of commit messages). **No prior commit performs this file's
   specific combination.**
4. **Primary source re-read:** [x] done this session — C139, C141, C142,
   C143 (including its addendum), C144, C145, C146 read directly via
   `Read`, in full, not from summary. `PARENT_ACTION_GATE.md` and
   `OPEN_BLOCKERS.md` OB14 section read directly, in full, this session.
   The C144-C158 "SU(3)/T²" sub-thread was also checked this session (see
   Section "Why the C147-C158 SU(3)/T² sub-thread does not supply the
   missing datum" below) — read `experiments/20260904-c151-stage0-su3t2-
   scoping/decision.md` (full, 291 lines, including its own same-day
   retraction/correction by C152), `experiments/20260905-c155-canonical-
   quadratic-form-comparison/decision.md` (full), `experiments/20260905-
   c156-root-relation-rule/decision.md` (full), and grepped C153/C154/C157/
   C158 for `3bar`/`W_cand`/`OB14`/"second copy" — zero hits in all four.
5. **Status:** [x] NEW — this specific combination (C146's Term1 theorem +
   C147's holomorphy result + a fresh Clebsch-Gordan derivation of
   `W_cand`'s own domain/target structure, applied to determine whether a
   *buildable-today* instantiation of `W_cand` could ever show
   `Delta_dyn>0`) has not been attempted. Built entirely from already-
   certified prior rounds' numeric/theorem content plus standard `su(3)`
   tensor-product rules this project's own code already uses (`3⊗3=3̄⊕6`,
   `3⊗3̄=1⊕8`, `3̄⊗3̄=3⊕6̄` — cross-checked against C139 Section 4's own
   listed decomposition of `EVEN_IDX⊗m`, which uses exactly these facts and
   matches this file's own re-derivation term-by-term).

---

## Explicit AI-Hypothesis Pre-Gates (mandatory — this file's central
observation is this session's own synthesis across five prior rounds'
already-certified results plus a fresh representation-theory computation,
not from primary literature)

**Step -4, Source Trace.** Every fact this file's argument depends on is
this project's OWN internal, already-certified result, re-cited at
file:section from its own `decision.md` (quoted directly above and below,
not paraphrased from memory): C139's own computed value `c=-2√3/3`
(Section 6, exact sympy) and its family-wide robustness (Section 8c, 13-
angle sweep); C146's `Term1≡0` theorem for any zero-singlet/`3̄`-type
summand (Checks 1-4, independently skeptic-confirmed); C147's holomorphic
non-vanishing of `m`'s own connection coefficient across its ENTIRE
admissible family, vanishing only at the zero connection (`PARENT_ACTION_
GATE.md` lines 193-210, quoted below). The one non-project fact used
(standard `su(3)` Clebsch-Gordan rules `3⊗3=3̄⊕6`, `3⊗3̄=1⊕8`, `3̄⊗3̄=3⊕6̄`)
is elementary representation theory this project's own C139/C141/C142
scripts already use without independent citation (not a new external claim
requiring literature verification).

**Step -3, Novelty Check.** Searched `null_results/INDEX.md`, `parked/
INDEX.md`, `pearl_registry/INDEX.md`, `OPEN_BLOCKERS.md`,
`PARENT_ACTION_GATE.md`, and the full `experiments/` tree (Prior Result Gate
items 2-3 above) for this specific combination — **0 hits.** C143's own
Lemma 2 (the closest prior content) explicitly uses a **hypothetical**
illustration (`domain_k` 2-dim, `target_k` 2-dim — quoted: *"take
`domain_k` 2-dimensional, `target_k` 2-dimensional, `Hom` space
2-dimensional"*) to argue the Hom-dim-`≥2` case is genuinely open — it does
**not** compute `W_cand`'s own actual shape (which C141's own F7 search had
already found: `domain=2, target=1`, NOT `2,2`) and does not connect this to
C147's later (same-day, but written after C143) holomorphy result. This gap
— a hypothetical illustration with a different shape than the real
candidate, left unconnected to the specific numeric facts later established
the same day — is exactly the kind of cheap, high-value recombination this
project's own methodology names as worth doing before any expensive new
construction. Per this project's brand-new 5-gate "discovery" mandate
(C157/C158, 2026-09-05): the expected disposition of this file's finding,
if verified, is closer to "a small, genuine, if somewhat deflationary,
addition" than "pure discovery" — flagged so a future executing agent does
not oversell it.

---

## Estimand

**Population:** This project's own already-certified `su(3)`-representation-
theoretic facts about round59/C139/C141/C143/C146/C147's twisted-`D_S6`
family, applied (via hand derivation, not new computation) to `W_cand
=3⊕3̄⊕3̄` (`OPEN_BLOCKERS.md` OB14, C142's own candidate), specifically the
one construction of `W_cand` that is buildable with **zero new geometric
input**: `m` (this project's own, already-fully-computed `S⁶` tangent/
isotropy representation, module type `3⊕3̄`) supplying one `3` and one `3̄`
constituent, plus a single additional, fully **decoupled** (block-diagonal,
zero-cross-coupling) `3̄`-type summand supplying the second `3̄` — the
*only* fallback this project's own machinery currently supports (exactly
analogous to how C141 supplied its two "extra" trivial summands for
`m⊕2·1` by leaving them decoupled, per C139's own Section 17 addendum,
because "there is no `NOMIZU`-derived data for the two 'extra' singlets").

**Intervention:** A hand derivation (not yet tool-executed) of the
domain-invariant / target-invariant sector structure for this specific,
buildable `W_cand` instantiation, using only: (i) C141's own already-built
`trivial_mult()`-based Clebsch-Gordan counting formula (`domain =
mult_W(3̄)+mult_W(1)`, `target = mult_W(1)+mult_W(3)`), (ii) C146's own
proven theorem (`Term1` vanishes identically on any domain-invariant vector
drawn from `Σ_odd`'s `3`-constituent, for ANY twist bundle summand lacking
a trivial constituent — Checks 1-4, matrix-verified), and (iii) standard
`su(3)` tensor-product rules to determine which su(3)-invariant vectors
exist in `Σ_even⊗(\text{decoupled }3̄)` and `Σ_odd⊗(\text{decoupled }3̄)`
separately from `m`'s own contribution.

**Comparator:** `OPEN_BLOCKERS.md` OB14's own current framing, which treats
"a genuinely new, independently-motivated geometric construction supplying
a second copy of `3bar`" as a single, undifferentiated expensive option —
without asking whether the CHEAPEST version of that option (reuse `m` for
one channel, decouple the other) is itself already predictable, in advance,
from content this project has already certified.

**Endpoint:** Does the hand-derived argument show (a) `Delta_dyn=0` is
FORCED for this specific, buildable `W_cand` instantiation, REGARDLESS of
what connection the decoupled extra `3̄` summand carries (even a
hypothetically independent, nonzero one) — the finding this file's
derivation below argues for; (b) the derivation is inconclusive/depends on
details not yet pinned down; or (c) the derivation shows `Delta_dyn>0` is
in fact reachable this way, contradicting C142's implicit expectation that
no cheap route exists?

**Summary measure:** A precise statement of which KIND of new geometric
construction (if any) could still make `W_cand` informative, sharper than
`OPEN_BLOCKERS.md`'s current "a second copy of `3bar`" framing — plus an
explicit flag that this is `[INFERRED]`, hand-derived, not `[VERIFIED-tool]`.

**MCID:** Not applicable — structural (forced-zero vs. not) question, not a
magnitude estimate.

**Intercurrent events (ICE):** If a future round's tool-verification of this
file's derivation (Section "The argument," Check-by-check) finds a sign,
branching-multiplicity, or block-diagonality error that invalidates the
conclusion, that is the expected, honest outcome of an unverified hand
derivation being checked — not a reason to silently revise the derivation
to fit a preferred answer. Report exactly which step failed.

---

## The argument (hand-derived this session — `[INFERRED]`, not
`[VERIFIED-tool]`; propose tool verification as the concrete next step)

### Step 1 — `W_cand`'s domain/target shape, re-derived from already-used rules

`W_cand = 3⊕3̄⊕3̄`, i.e. `(mult_1, mult_3, mult_3̄) = (0,1,2)` — this is
exactly C141's own F7-search candidate (`decision.md` Section 2, "F7 --
exhaustive check," `(0,1,2)`), the ONLY module type other than `EVEN_IDX`
itself achieving round59's own `(2,1)` shape:

```
domain = mult_W(3̄) + mult_W(1) = 2 + 0 = 2
target = mult_W(1) + mult_W(3) = 0 + 1 = 1
```

matching C141's own already-published F7 finding exactly (re-derivation,
not a new claim).

### Step 2 — decompose `W_cand`'s ONLY buildable instantiation as `m ⊕ 3̄_extra`

`m = 3⊕3̄` already supplies one `3` and one `3̄` — this project's own,
already-fully-computed `S⁶` tangent/isotropy representation (C139). The
SECOND `3̄` (`3̄_extra`) has, per C142's own exhaustive search, **no**
identified geometric source in this project's content — the only buildable
option is to add it as a fully **decoupled** summand (zero cross-coupling
to `m`'s own connection), exactly the fallback C139's own Section 17
addendum and C141's own construction both already use for `m⊕2·1`'s two
"extra" singlets (quoted, C139 Section 17: *"The only natural way to build
a connection on `m⊕2·1`... is to leave them decoupled... there is no
`NOMIZU`-derived data for the two 'extra' singlets — they do not come from
any existing geometric construction."*). **This file's argument applies
specifically to this buildable, decoupled instantiation — not to a
hypothetical, not-yet-found, genuinely CROSS-COUPLED construction; see
"What this does NOT mean," item 2, for that distinction stated explicitly.**

### Step 3 — target-invariant sector is entirely `m`'s own, already-computed channel

`target_inv` (1-dim) comes from `mult_W(3) = 1`, i.e. `EVEN_IDX`'s own
`3̄`-constituent pairing with `W_cand`'s single `3`-constituent — and
`W_cand`'s ONLY `3`-constituent is `m`'s own (`3̄_extra` is a pure `3̄`,
contributing zero `3`-multiplicity). **`target_inv` is therefore, in this
specific buildable instantiation, IDENTICAL to C139's own already-computed
`target_inv`** (the same 1-dimensional invariant vector, since it is built
from the same `EVEN_IDX⊗m` pairing C139 already certified).

### Step 4 — `3̄_extra`'s own contribution to `target_inv` is forced to be ZERO, by standard `su(3)` branching, regardless of its connection

`Σ_even⊗3̄_extra = (1⊕3̄)⊗3̄_extra`. Using the standard rules this project's
own C139 Section 4 already cites (`1⊗3̄=3̄`; `3̄⊗3̄=3⊕6̄`, the conjugate of
`3⊗3=3̄⊕6`): `Σ_even⊗3̄_extra = 3̄ ⊕ 3 ⊕ 6̄` — **containing NO `su(3)`
singlet.** This means there is literally **no `su(3)`-invariant vector** in
`Σ_even⊗3̄_extra` for a decoupled `3̄_extra`-connection to land in — so,
under block-diagonality (Step 2's only-buildable assumption), ANY vector
built from `domain_inv`'s `3̄_extra`-component, acted on by the FULL
operator `D = Term1+Term2`, projects to **exactly zero** inside
`target_inv` — not merely "generically small," but forced to be the zero
vector by the absence of any invariant target for it to map to, independent
of what connection `3̄_extra` itself carries (even an independently-sourced,
nonzero one, so long as it stays decoupled from `m`).

(`Σ_odd⊗3̄_extra = (3⊕1)⊗3̄_extra = (1⊕8) ⊕ 3̄` — DOES contain one singlet,
from `3⊗3̄_extra→1`, consistent with Step 1's `domain=2` count: one
dimension from `m`'s own `3̄`, one from `3̄_extra`.)

### Step 5 — the resulting `1×2` matrix is forced to have rank exactly 1

Combining Steps 3-4: the `domain_inv(2) → target_inv(1)` matrix (call its
two entries `(d_m, d_extra)`, one per domain basis vector) has
`d_extra ≡ 0` (Step 4, forced, unconditionally). `d_m` is, by Step 3,
**exactly C139's own already-certified value** `c = -2√3/3` for the
`Term2` piece (Term1 is 0 here too, by C146's theorem, since this
component also comes from `Σ_odd`'s `3`-piece) — a value C139 (Section 6)
and C147 (Section "connection-geometry route... closed, over the
continuum") both already established is **nonzero across the ENTIRE
admissible connection family**, vanishing ONLY at the identically-zero
connection (`PARENT_ACTION_GATE.md`, C147 update, quoted: *"the real 2×2
matrix is an EXACT similarity — `det = 4/3`... `c = 0` ONLY at the zero
connection"*).

Therefore the row vector is `(-2√3/3, 0)` — **rank exactly 1**, regardless
of `3̄_extra`'s own connection (even a hypothetical independent, nonzero
one) — because `d_extra` is forced to zero not by any property of
`3̄_extra`'s connection, but by the ABSENCE of an invariant target for it to
land in at all (Step 4).

### Step 6 — conclusion: `Delta_dyn=0` is FORCED for this buildable instantiation

`floor(W_cand) = max(0, domain-target) = max(0,2-1) = 1`. Rank 1 (Step 5)
gives `kernel = domain - rank = 2-1 = 1 = floor`. **`Delta_dyn = 0`,
FORCED — not merely "expected" or "generic" — for the ONE currently-
buildable instantiation of `W_cand` (`m` for one channel, a decoupled extra
`3̄` for the other), regardless of what connection that extra `3̄` carries,
provided only that it stays decoupled (block-diagonal) from `m`.**

---

## Claim

**Falsifiable statement:** When the argument above (Steps 1-6) is verified
by a short script reusing C139/C141/C146's own already-built functions (no
new geometric construction, no new physics), it will show that `W_cand
=3⊕3̄⊕3̄`, built as `m ⊕ (\text{decoupled }3̄_extra)` — the ONLY
instantiation buildable with this project's existing content — has
`Delta_dyn=0` FORCED, independent of `3̄_extra`'s own connection value. If
this verification instead finds an error in Steps 1-6 (a branching-
multiplicity miscount, a sign error, or a case where block-diagonality
does not force `d_extra=0` as claimed), that specific step's failure is the
result, not a silent revision of the argument to a more convenient
conclusion.

**Consequence for OB14, if the argument survives verification:** the
"genuinely new, independently-motivated geometric construction supplying a
second copy of `3bar`" that `OPEN_BLOCKERS.md` names as option (a) is, in
its cheapest and most natural form (reuse `m`, decouple the addition),
**provably insufficient** — no matter how the new source's own connection
turns out, `Delta_dyn=0` is forced by pure representation theory, as long
as the construction (i) reuses `m` for one of `W_cand`'s two `3̄`
constituents and (ii) leaves the new constituent decoupled from `m`. A
genuinely informative construction would need EITHER (i') to avoid using
`m` at all (building `W_cand` from two entirely new, independent `3̄`
sources — a strictly more expensive ask than "a second copy," since it
requires abandoning the one already-available channel too), OR (ii') a
new geometric mechanism that specifically COUPLES the new `3̄` to `m`'s own
tangent bundle (not merely supplies it independently) — a narrower,
more specific, and arguably higher-AOG-5-risk kind of construction than
`OPEN_BLOCKERS.md`'s current wording ("a second copy of `3bar`") conveys.

---

## Kill criterion (MANDATORY — filled BEFORE any future round computes)

| Outcome (of the proposed tool-verification script) | Verdict |
|---|---|
| Steps 1-6 all confirmed by direct computation (branching counts, `d_extra≡0`, `d_m` matches C139's registered value exactly) | `PROMOTE-AS-NECESSARY-CONDITION` — the sharpened OB14 framing above (two sub-paths, (i') and (ii'), replace the single undifferentiated "second copy" framing) is correct and should be folded into `OPEN_BLOCKERS.md` OB14 by the orchestrating session |
| Step 4's branching claim is wrong (`Σ_even⊗3̄_extra` DOES contain a singlet) | `ARITHMETIC_ERROR` — this file's central argument is void; re-derive from scratch, do not patch |
| Step 2's block-diagonality assumption turns out not to be the only buildable option (a genuinely cheap coupled construction is found) | `ASSUMPTION_NARROWER_THAN_STATED` — re-scope; this file's conclusion applies only to the decoupled sub-case, name the coupled one separately |
| `d_m` (the `m`-channel's own contribution) is found to vanish for some admissible connection after all (contradicting C147's own "vanishes only at the zero connection" finding, re-checked) | `C147_ITSELF_NEEDS_REVISITING` — a much bigger finding than this file's own scope, would reopen C147 |
| The specific recombination (C146+C147+fresh branching count) is found to already exist somewhere once the executing agent re-runs Prior Result Gate item 3 (git pickaxe) more thoroughly than this file did | `ALREADY-KNOWN` — cite it, close this round immediately |

**Explicit escape route:** if the verification script confirms Steps 1-6
cleanly, STOP — do not proceed from there to attempting sub-path (i') or
(ii') in the same round. Each of those is a separate, much larger
undertaking (see Cost estimate) and deserves its own Prior Result Gate,
estimand, and kill criterion once this cheaper scoping's outcome is
tool-verified.

---

## Why this is the cheapest first differentiating test (CDT protocol)

- **Differentiation:** distinguishes "any second `3̄` source would make
  `W_cand` informative" (`OPEN_BLOCKERS.md`'s current implicit framing)
  from "only a source that couples to `m` specifically, or that avoids
  `m` altogether, would" — a distinction that does not currently exist
  anywhere in this project's registries.
- **Kill power:** genuinely can fail — Step 4's branching claim, once
  tool-verified, could in principle be wrong (a miscounted tensor product,
  though checked twice by hand against C139's own already-used listing in
  this file and found consistent).
- **Rescue power:** if Steps 1-6 are confirmed, the finding actively
  REDIRECTS future effort away from the naive "just find any second `3̄`"
  reading of OB14's option (a), toward the two sharper, more specific
  sub-paths named in the Claim section — cheap information that changes
  what a future expensive round should even attempt.
- **Non-circularity:** does not assume the conclusion — every fact used
  (C139's own `c` value, C146's Term1 theorem, C147's holomorphy result,
  standard `su(3)` CG rules) was independently established by prior rounds
  for OTHER purposes, before this file combined them.
- **Reuse value:** high — if confirmed, this becomes a citable addition to
  `PARENT_ACTION_GATE.md` F2's own `Delta_dyn` gate (C143), giving it a
  THIRD branch (currently only "Hom-dim 1 ⟹ uninformative" and "Hom-dim
  ≥2 ⟹ potentially informative, pre-register `H0` vs `H1`") — namely
  "Hom-dim ≥2 but reachable only via a decoupled reuse of an
  already-robustly-nonzero channel ⟹ ALSO uninformative, check this
  BEFORE assuming branch 3 (`POTENTIALLY-INFORMATIVE`) applies."
- **Cost:** VERY LOW — a script reusing `C139`/`C141`/`C146`'s own already-
  built functions (`trivial_mult()`, the `su(3)`-branching tables, C139's
  own certified `c`-value import), computing Steps 1, 3, 4, 5 directly (no
  new Dirac operator, no new connection, no new physics) — comparable in
  scope to C143's own "DESIGN/THEOREM round, no new Dirac-operator
  computation" framing, not to a construction round.

---

## Why the C147-C158 SU(3)/T² sub-thread does not supply the missing datum

Per the task's explicit instruction, checked whether the C144-C158 "SU(3)/
T²" methodology sub-thread (`experiments/20260904-c151-stage0-su3t2-
scoping/`, `.../c152-term2-vanishing-mechanism/`, `.../c153-nk-linearity-
structural-derivation/`, `.../c154-connection-coefficient-magnitude-vs-
killing-eigenvalue/`, `experiments/20260905-c155-canonical-quadratic-form-
comparison/`, `.../c156-root-relation-rule/`, `.../c157-chirality-balance-
weyl/`, `.../c158-weyl-invariance-kernel-gate/`) — built AFTER C142, and
therefore not considered by C142's own search — supplies an independently-
sourced `su(3)`-equivariant map into `3` or `3̄` after all.

**It does not, for a structural reason, not merely "wasn't found":** the
C147-C158 thread studies a DIFFERENT homogeneous space, `SU(3)/T²` (the
full flag manifold of `SU(3)`, read in full: C151 Stage 0, `decision.md`
lines 14-33), whose own isotropy group is `T²` (the maximal torus,
ABELIAN, rank 2) acting on its OWN 6-real-dimensional tangent bundle — not
`su(3)` acting as the isotropy of `S⁶=G₂/SU(3)` on `S⁶`'s own tangent
bundle `m`. The `SU(3)` in "`SU(3)/T²`" plays the role of the FULL
isometry group of a different space, not the isotropy subgroup C142 needed
new data for. C151 Stage 0's own regression explicitly confirms this
distinction is real, not cosmetic: `dim Hom_{su(3)}(m, Λ²m) [S⁶] = 2`
(C73b's own family) vs. `dim Hom_{T²}(m, Λ²m) [SU(3)/T²] = 6`, three times
larger, precisely BECAUSE the constraining group is weaker (abelian `T²`,
not the full `su(3)`). A `T²`-equivariant structure on `SU(3)/T²`'s
tangent bundle is not automatically an `su(3)`-equivariant map into `3` or
`3̄` relative to `S⁶`'s own isotropy action — no natural map between the
two settings was found, and none is asserted here. Grepped C153/C154/C157/
C158 for `3bar`/`W_cand`/`OB14`/"second copy" this session — **zero hits
in all four**, confirming this sub-thread's own authors never connected it
to OB14 either (its stated purpose throughout — C155's own framing — is
testing a nearly-Kähler holomorphy-universality hypothesis for the
connection coefficient `c(J∇)=i·c(∇)` across different flag manifolds, a
different research question).

---

## Cost estimate, stated honestly (per the orchestrating session's explicit
instruction not to undersell the risk)

**This file's own proposed verification (the actual recommendation):
plausibly 1 round, likely well under a full session.** It requires only:
importing C139's own already-certified `c=-2√3/3` value and `su3_ops_np`/
branching machinery, importing C146's own `Term1`-vanishing check function,
computing `Σ_even⊗3̄_extra`'s and `Σ_odd⊗3̄_extra`'s own singlet
multiplicities via the SAME `trivial_mult()`-style formula C141 already
built, and confirming the resulting `1×2` matrix has the predicted `(c,
0)` shape. No new Dirac operator, no new connection, no new twist bundle
construction — comparable in scope to C143/C146's own "theorem synthesis,
no new computation" rounds, NOT to C139/C141's own construction rounds.

**Sub-path (i') — building `W_cand` from two entirely new, independent `3̄`
sources (abandoning `m` altogether): this is NOT a 1-3 round test.**
Neither candidate source this project has ever considered (C70/C71's
`Inn(su(3))`-orbit intertwiners; G102's own triality channels, both
rejected by C142 for identifiable reasons) supplies even ONE independent
source, let alone two. This would be at minimum as expensive as C142's own
assessment of the ORIGINAL "second copy" ask, likely more so (needing two
new geometric objects instead of one), and carries the same high AOG-5 risk
`OPEN_BLOCKERS.md` already flags.

**Sub-path (ii') — a new geometric mechanism that specifically COUPLES a
new `3̄` to `m`'s own tangent bundle: likely MORE expensive and MORE
speculative than either C142's original framing or sub-path (i').**
This project has no precedent anywhere in its history for a twist-bundle
connection that couples two SEPARATE geometric objects (as opposed to a
single object's own internal structure, as `NOMIZU` does within `m`
itself) — inventing one would be, by this project's own Anti-Overfitting
Gate discipline, exactly the kind of ad hoc addition AOG-5 (independent
motivation) is designed to block, UNLESS a specific, independently-motivated
physical reason for such a coupling is found (e.g., from Tom Lawrence's own
framework, `OPEN_BLOCKERS.md`'s option (b)). No such reason is known to
exist in this project today. **Do not undersell this**: this sub-path is,
if anything, HARDER to justify than the "any second copy" framing
`OPEN_BLOCKERS.md` currently states, not easier — this file's own
contribution is making that difficulty explicit and specific, not
resolving it.

---

## What this does NOT mean

- Does NOT itself constitute a verified physics result — the argument in
  "The argument" section is `[INFERRED]`, hand-derived this session, and
  explicitly NOT `[VERIFIED-tool]`. A future round must run the proposed
  short script before this file's conclusion is trusted for anything
  beyond scoping.
- Does NOT claim `W_cand` can NEVER show `Delta_dyn>0` — only that the ONE
  currently-buildable instantiation (reuse `m`, decouple the rest) cannot,
  regardless of what verification eventually confirms about the decoupled
  piece's own connection.
- Does NOT resolve OB14 — `Sigma` remains unexplained as the physically
  preferred twist; this file only narrows what KIND of future construction
  could possibly matter.
- Does NOT change `N_gen=3`'s CONDITIONAL status, `lambda =
  FREE_COUPLING_PARAMETER`, `sm_derivation_claimed = False`, or
  `safe_for_runtime = False`.
- Does NOT touch OB1, OB4, OB11, OB12, OB13, or the C144-C158 SU(3)/T²
  methodology thread's own open questions (that thread's own findings —
  C155's rank-mismatch REJECT, C156's dimensional-impossibility REJECT of
  its own replacement hypothesis, C157/C158's "not a discovery" verdicts —
  are read here only to confirm irrelevance to OB14, not engaged with on
  their own merits).
- Does NOT edit `OPEN_BLOCKERS.md`, `PARENT_ACTION_GATE.md`,
  `pearl_registry/INDEX.md`, `CLAIM_LEDGER.yaml`, or `preprint.tex` —
  registry updates are the orchestrating session's, per C124-C161
  precedent.
- Does NOT solicit Tom Lawrence's Part 5.
- Does NOT commit to any further round regardless of outcome — this is a
  scoping document, not a pre-authorization to proceed, per the same
  explicit instruction C161 was given.
