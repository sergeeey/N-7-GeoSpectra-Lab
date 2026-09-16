# Completeness Theorem — G₂/SU(3)-restricted mechanisms cannot discriminate triality channels

**Date:** 2026-09-16 (rev 7, same day — see §0b-§0g for what changed and
why)
**Status:** DRAFT. rev 1 through rev 6 were each reviewed and each found
to have a real defect (§0b-§0f). A sixth skeptic pass on rev 6 found the
most substantive defect yet found in this document's escape criteria —
not a citation error, an actual mathematical gap: `E1`'s `SO(7)`-exclusion
(added in rev 6) only blocks ONE of three `Spin(7)` conjugacy classes in
`Spin(8)`, and `su(3) ⊂ g₂` sits inside a DIFFERENT one (the stabilizer of
a spinor in `8_s`, not a vector in `8_v`) that `E1` as worded did not
exclude, under which `8_v≅8_c` remain undistinguished — the theorem's own
failure mode, admitted by its own escape condition. Also found: `E2`'s
rev 6 justification ("`build_numeric_dirac` has no `t` argument") was
simply wrong — the function's own `test_deformation` routine builds
exactly such a family — though the conclusion happened to still hold, for
an unstated, different, correct reason (scale-invariance of the
commutant). Both fixed properly in rev 7 (§0g), not just re-labeled. The
theorem's core mechanism (§1 steps 1-3, Hom-space/Schur's lemma) has now
survived all six skeptic passes UNCHANGED — every defect across all six
rounds was in material ABOUT the core result (mostly citation/scope
precision; this round's `E1` finding is the first to be a genuine
mathematical gap rather than an attribution error), never the core
computation. **Still pending a fresh skeptic pass on rev 7 before this
document is cited externally or propagated into
`OPEN_BLOCKERS.md`/`pearl_registry`.**
**Purpose:** upgrade the informal `G44 Information-Retention Gate` (C150,
`experiments/20260904-c150-g44-information-retention-gate/GATE.md`) from a
pre-filter heuristic into an explicit, citable theorem with a stated,
checkable set of sufficient conditions for what would escape it (§3 —
corrected in rev 4 from an earlier, false "necessary and sufficient"
claim; see §0d).

---

## 0. Recomposition Gate — run before writing rev 1

The originating plan (this session, 2026-09-13/16) proposed "formalize
G44 + C173 into one completeness theorem." Re-reading both `decision.md`
files in full, verbatim, before drafting anything found that **no
combination is actually needed**: `C173` (2026-09-06, §2, skeptic-confirmed
§8b) is already the fully general statement, and `G44` (2026-06-20) is its
`G₂`-restriction special case, explained (not merely cited) by `C173`'s
own §0 points 1-2 (found by the fifth skeptic pass reviewing rev 5, fixed
here in rev 6/§0f — this line previously cited `C173` §8c, which is about
`C78`'s numerical commutant result, not `G44`'s branching; §1's identical
citation was fixed in rev 5 but this one, in the same file, was missed
until the fifth pass caught it). This is unchanged from rev 1 and still
holds after the rev-2 fix below.

## 0b. What rev 1 got wrong, found by an independent skeptic pass + direct re-verification against 3 primary sources

Rev 1's proof sketch made the "inner cannot realize outer" argument
(`C173` §2's second half) the SOLE mechanism (its own "step 5"). A skeptic
pass flagged this, and independently re-reading `G102/decision.md`,
`OPEN_BLOCKERS.md`, and `C150/GATE.md` directly (not trusting the
skeptic's own compressed summary — its final report was itself degraded
by an unrelated harness bug, see the pearl entry this session added to
`~/.claude/rules/pearl_registry/INDEX.md`) confirmed the objection is
real, on two independent counts:

1. **Wrong primary mechanism.** The actual, foundational reason `M` can't
   discriminate is Hom-space filtration under Schur's lemma — `dim
   Hom(channel_i, channel_j)` shrinks `6` (`su(3)`) → `2` (`g₂`) → `0`
   (`so(8)`) (`C72`, tabulated in `C150/GATE.md` §1) — NOT the inner/outer
   automorphism argument. Rev 1 inverted this hierarchy, making inner/outer
   the main proof step. **Correction, §0c below: the claim in this
   paragraph that the inner/outer point "correctly says no" to the
   centralizer helping was ITSELF wrong** — round124 shows the centralizer,
   once adjoined, genuinely does discriminate at the Gate-1 (algebraic)
   level. The inner/outer argument is real and load-bearing, but at Gate 2
   (physical realization), not Gate 1 — see §0c and §2b.
2. **Wrong scope, contradicted by this project's own record.** `G102`'s
   own P5/P6 (`decision.md` lines 16-17) show the channels ARE
   distinguishable within the FULL `so(8)` — `Hom(channel_i,channel_j)=0`
   for `i≠j` there. `C150/GATE.md` itself states the scope explicitly
   (§"Scope, stated so the gate is not over-applied", point 1): "This is
   about `Spin(8) → G₂` restriction specifically. It says nothing about
   mechanisms that never route triality data through `G₂` at all." Rev 1
   did not carry this caveat, and as a result its own escape criterion
   (E1, "outside `Spin(8)` entirely") was too narrow to admit the
   `SO(4)×SO(4)` block-chirality construction this project's OWN `OB4`
   record (`OPEN_BLOCKERS.md`, Gate 1) already uses — a REAL, already-
   built, rank-4 subgroup of `Spin(8)` (hence inside it, failing rev 1's
   E1 as literally worded) that algebraically distinguishes all three
   channels. `OB4`'s own header calls this "a model postulate, not
   derived" — i.e. the open question there is PHYSICAL REALIZATION on the
   actual geometry, not algebraic non-existence, and this theorem must
   not imply otherwise.

Both fixed in rev 2, below.

## 0c. What rev 2 got wrong — found by a second independent skeptic pass + direct re-verification against TRIALITY_DISTINGUISHABILITY_GATE.md

rev 2's own §1 kept an "inner cannot help" argument (its steps 4-5) as a
secondary point supporting the main theorem. A second, independent
skeptic pass (a fresh agent, not the one that reviewed rev 1) flagged
this as a real, decisive objection, and direct re-reading of
`TRIALITY_DISTINGUISHABILITY_GATE.md` confirmed it:

1. **rev 2's steps 4-5 were flatly false, not merely narrow.** `round124`
   (`TRIALITY_DISTINGUISHABILITY_GATE.md` §2b) computes exactly what
   steps 4-5 claimed was impossible: adjoining `su(3)`'s own centralizer
   gives `su(3)⊕u(1)⊕u(1)`, under which `Hom(channel_i,channel_j)=0` for
   `i≠j` — genuinely discriminating, `[VERIFIED-tool]`. The inner/outer
   argument does not block this, because Gate-1 discrimination via a
   Hom-space computation never required constructing an element that IS
   the triality automorphism.
2. **The inner/outer argument was real, but misplaced.** It is exactly
   the mechanism behind `C78`'s exhaustive result (§10 of the same file):
   the full commutant of THIS project's physical Dirac operator `D`
   within all of `so(8)` is exactly `su(3)`, nothing larger, for any `D`
   built from `G₂/SU(3)` data — this is a Gate-2 (physical realization)
   fact, not a Gate-1 (algebraic distinguishability) fact. `round124` and
   `SO(4)×SO(4)` were each individually tested against the actual physical
   `D` (`C75`/`C77`) and both fail — consistent with, and explained by,
   `C78`'s exhaustive result. **Correction, §0d below: the "for any `D`"
   universal in this paragraph is ITSELF the error a THIRD skeptic pass
   found** — `C78` computed this for the ONE `D` tested, not universally;
   see §0d and the rewritten §2b.

Fixed in rev 3: steps 4-5 withdrawn from the main proof; a new §2b states
the Gate-1-vs-Gate-2 distinction explicitly, with the inner/outer argument
relocated to where it actually applies; the escape table (§3) split `E1`
into `E1a` (Gate-1 escape, real) and `E1b` (Gate-2 escape, proven
impossible for the current `D`).

## 0d. What rev 3 got wrong — found by a third independent skeptic pass with direct primary-source verification (all six cited sources read in full)

rev 3's own NEW §2b — written specifically to relocate the inner/outer
argument to where it belongs — reinstalled the identical invalid inference
one level down, and propagated it into an overclaim about `OB4`'s status
that directly contradicts `OPEN_BLOCKERS.md` itself. Three distinct,
source-verified defects (full report on file; the theorem's core §1
steps 1-3 were re-verified against `G102`/`C173` and confirmed CLEAN,
including the exact `Hom` dimensions and the `Σm²` counts):

1. **"commutant = `su(3)`, nothing larger, for ANY `D`" is a non-sequitur,
   not licensed by `C78` or the inner/outer argument.** `C78`
   (`TRIALITY_DISTINGUISHABILITY_GATE.md` §10) computed the commutant for
   ONE specific, already-built operator — `C73`'s `build_numeric_dirac` —
   and its own decision.md says so explicitly: "the largest symmetry `D`
   HAS, full stop, within `so(8)`" (about that `D`; corrected in rev 7 —
   an earlier draft dropped "within `so(8)`" from this quote), not "the
   largest symmetry any such `D` could ever have." The inner/outer argument (triality outer,
   `Spin(8)` connected) bounds whether triality can be REALIZED by an
   inner automorphism; it says nothing about the DIMENSION of a
   commutant, which is a computed fact about one operator's actual matrix
   entries, not a structural consequence of connectedness. This is the
   SAME category error §0c already identified and removed at the
   algebraic (Gate-1) level — §0c's own point 1 states the reason it
   fails ("Gate-1 discrimination via a Hom-space computation never
   required constructing an element that IS the triality automorphism")
   — and rev 3's §2b reinstated it one level down, at the operator-
   commutant question. Corrected: universality over `D` is `[UNKNOWN]`;
   only the single computed instance is `[VERIFIED-tool]`.
2. **"`OB4` Gates 2-6 … PROVEN CLOSED" is false, on two independent
   counts.** (a) Operator scope: per point 1, only one `D` was tested, so
   nothing about other possible `D`s follows. (b) A naming collision
   inside `TRIALITY_DISTINGUISHABILITY_GATE.md` itself, missed by rev 3:
   its own §3 uses a FIVE-condition numbering (from
   `L3B_SPIN8_INTERFACE_SPEC.md` §3) where "condition 2" means `[D,U]=0`;
   its §4 verdict switches to a DIFFERENT SEVEN-GATE numbering (spec §7)
   where "Gate 2" means the global principal-bundle action — an entirely
   different, never-tested question. `C78` closes condition 2 of the
   five-condition list, for one `D`. It says nothing about the seven-gate
   list's Gates 2-6 (principal-bundle action, gauge-orbit audit, zero-mode
   map under `K`, 4D effective action, basis-invariant observable) — none
   of which has ever been attempted. `OPEN_BLOCKERS.md` OB4 — compressed a
   MONTH AFTER `C78`, and citing `C78` by name in its own `OB11(iii)`
   entry — still correctly records Gates 2-6 as "PARKED, not falsified."
   rev 3's claim directly contradicted this project's own current
   registry.
3. **§3's "necessary and sufficient" escape criterion was false, and its
   `E1a`/`E1b` split was internally incoherent.** `E1b` was listed as a
   disjunct of an escape "if and only if" while its own Status cell said
   it was impossible — an anti-escape contributing nothing to an "if."
   `E1a`'s "postulated independently of the holonomy" qualifier, read
   literally, EXCLUDED `round124`'s own construction (built FROM
   `su(3)`'s own centralizer, per `TRIALITY_DISTINGUISHABILITY_GATE.md`
   §2b's own description) even though `E1a`'s Status cell cited `round124`
   as its example. Separately, `C150/GATE.md`'s own "Scope" point 2 —
   dropped from this document entirely — states plainly that a different
   morphism-level or extension-level datum "could in principle escape,"
   which is neither ruled out nor represented by any of `E1a`-`E5`,
   directly falsifying the "necessary and sufficient" claim.

**Fixed in rev 4:** §2b rewritten below with "Gate 2" language dropped in
favor of "the Commutant Condition," specifically to stop colliding with
`OB4`'s own seven-gate numbering (defect 2b above); every claim about the
commutant now states explicitly which one operator it is about; the
escape criterion (§3) downgraded from "necessary and sufficient" to
"known sufficient conditions, not proven exhaustive," with `GATE.md`'s own
Scope point 2 carried forward explicitly as an acknowledged open door
rather than silently dropped; `E1a` merged back into a single `E1` with
its qualifier corrected to admit `round124`; `E1b` demoted from an escape
disjunct to a downstream caveat on `E1`; the `S³`-clause citation in §1
swapped for the correctly-scoped, more recent source (`C191`/`OB1`); `§5`
gains the `C83`/§11 citation the trail previously omitted.

## 0e. What rev 4 got wrong — found by a FOURTH independent skeptic pass, direct verification against seven primary sources

rev 4's own fixes were the right shape (scope every claim to the one `D`
tested; stop conflating numbering schemes) but got the details wrong in
several places — the same relocation pattern one level further down, plus
new citation errors introduced by rev 4's own new material. In descending
order of importance:

1. **"`C78` closes condition 2 (`[D,U]=0`)" is itself wrong — a fourth
   instance of the same relocated fallacy.** `TRIALITY_DISTINGUISHABILITY_GATE.md`
   §1 defines condition 2 as `[D,U]=0` for the SPECIFIC triality operator
   `U` (order 3, realizing the outer automorphism, condition 1). `C78`
   computed a commutant WITHIN the Lie algebra `so(8)` — and `U`, realizing
   an OUTER automorphism, is not and cannot be an element of `so(8)` at
   all (the same inner/outer fact this document already uses elsewhere).
   A Lie-algebra commutant computation therefore cannot test `[D,U]=0` for
   `U` itself, regardless of how exhaustive it is. What `C78` actually,
   precisely closed is its OWN stated scope (§10): "Gate 2, for the entire
   class 'some subalgebra of `so(8)` distinguishes the channels and is
   respected by the physical `D`,' is now CLOSED (NO), exhaustively" — a
   claim about candidate DISCRIMINATING SUBALGEBRAS, not about the literal
   condition-2 operator `U`. Whether `U` itself commutes with `D` is the
   project's own separately-named, explicitly UNRESOLVED
   "channel-permutation/redundancy" question (`C75`, `C78`'s own "what
   this does NOT show" §2, and `C77`'s Kill Analysis all state this test
   was never run) — which this document's own §3 `E1` note already flags
   as untested, without previously connecting it back to §2b. rev 4's §2b
   claimed to fix the operator-scope error and, in doing so, introduced a
   condition-scope error in its place.
2. **`[VERIFIED-tool]` `Hom=0` was wrongly attributed to `SO(4)×SO(4)`.**
   Only `round124`'s `su(3)⊕u(1)⊕u(1)` has a computed `Hom`-space table
   (`TRIALITY_DISTINGUISHABILITY_GATE.md` §2b). `SO(4)×SO(4)`'s
   distinguishing argument is the DIFFERENT, also-real block-chirality
   matching (`Γ_A=Γ_B` vs `Γ_A=-Γ_B`, §2 of the same file) — the source
   itself contrasts the two ("arguably cleaner than the `SO(4)×SO(4)`
   route's explicit... matching argument"), not treating them as the same
   computation.
3. **`E1`'s "larger than `g₂`/`su(3)`" wording is imprecise for its own
   cited example.** `su(3)⊕u(1)⊕u(1)` (rank 4, dim 10) does not CONTAIN
   `g₂` (dim 14) — it is larger than `su(3)` alone and sits OUTSIDE `g₂`
   (the source's own words), not "larger than `g₂`."
4. **The `S³`-clause fix in rev 4 mischaracterized `C191`.** `C191`'s
   REJECT verdict is about a specific `t`-sector PAIRING claim (which
   channel ↔ which `t`-value), tested only under an ALREADY-POSTULATED
   `SO(4)×SO(4)`-in-`Spin(8)` embedding (`C191` §0: explicitly a
   postulate, not derived) — not a test of bare `S³` isometry data
   without that additional structure, and not about `8_v` at all. Worse:
   `C191`'s OWN split-identification reading (§3.6) finds the opposite of
   what rev 4 claimed — `S³`'s `SU(2)_L×SU(2)_R` data, combined with that
   postulated embedding, DOES cleanly separate `8_s` from `8_c` BY TYPE
   ("real and unconditional," per `C191`'s own Kill Analysis) — it just
   doesn't supply the specific `t`-sector pairing `C191` was testing for.
   `C191` is evidence relevant to `E1`'s territory (an additional
   `Spin(8)`-subgroup postulate), not evidence that bare `S³` isometry
   data adds no content.
5. **Frobenius-violation range misattributed.** `65.5%-352%` is `C75`'s
   own range (round124 candidate only); `C77`'s range (`SO(4)×SO(4)`) is
   `35.4%-353%`. Both were cited as one shared range in two places.
6. **`§5`'s `C83` citation swapped subject and complement.** The
   1-dimensional intersection with `su(3)` belongs to the CANDIDATE
   ALGEBRA `so(4)_1+so(4)_2` itself, not to its 20-dim complement (a
   complement of `su(3)` intersecting `su(3)` in more than the zero
   subspace would be a contradiction in terms).
7. Minor: `C173` §8c's quote in §1 (about `C78`'s numerical result, not
   about `G44`'s branching) was cited for the wrong claim, with an
   ellipsis hiding that its full sentence ends in the same "for any
   physical `D`" universal §0d already withdrew; `OB11(iii)` is `OB11`'s
   own condition, not part of `OB4`'s entry, and was described as if it
   were.

**Fixed in rev 5:** §2b rewritten again to state `C78`'s scope in its own
words (candidate-subalgebra class, not the literal `[D,U]=0` condition),
explicitly naming the channel-permutation/redundancy question as the
thing that condition genuinely requires and that remains untested;
`SO(4)×SO(4)`'s discriminating argument corrected to block-chirality
matching, not a Hom computation; `E1`'s wording, the Frobenius range (both
occurrences), the `C83` citation, and the `C173`/`OB11` citations all
corrected; §1's `S³`-clause rewritten to accurately scope what `C191`
does and does not show, dropping the incorrect "REJECTED as literally
stated" framing for this clause specifically (that framing is accurate
for `C191`'s OWN pairing claim, not for this theorem's `S³`-data clause).

This is now the FOURTH round of the identical underlying pattern — a
fallacy or scope error caught, "fixed," and reappearing one level further
down or sideways into an adjacent claim. The header's own prediction
(newest section = least verified) has held every time. §1's theorem core
(steps 1-3) is the one part of this document that has never needed a
correction across all four passes — every defect, all four times, has
been in material ABOUT the core result, never the core computation
itself.

## 0f. rev 5 → rev 6 — a fifth skeptic pass, escalated per the Evaluator-Optimizer Guard instead of auto-fixed

A fifth skeptic pass on rev 5 found six issues, per its own verdict
section. **Correction, rev 7 (§0g): this section's own count of "two
mechanical + three substantive" is five, not six — a sixth skeptic pass
found the arithmetic didn't add up and that the sixth item's fate was
never recorded here. That sixth item was the fifth pass's finding that
this document's own "Honesty note" (§2b) overclaimed `C78`'s scope
statement as "precise about" a distinction the source does not actually
draw — resolved in rev 7, §0g/§2b, not resolved when this section was
first written.** Of the six: two were mechanical citation errors (a
stale `C173` §8c reference left in §0 after §1's copy of it was fixed; a
wrong section number for the seven-gate list) and were fixed directly,
without a sixth full skeptic round. Three were substantive and were
surfaced to the user rather than resolved autonomously, per this
project's own Evaluator-Optimizer Guard — the fifth pass itself is the
one that named this document as having exceeded the stack's own 3-cycle
cap. The user's explicit decision: drop the `S³`-clause from the theorem
statement entirely, and narrow `E1`/`E2` rather than keep patching them.
Applied as follows:

1. **`S³`-clause removed from §1's theorem statement, not merely
   re-cited.** The fifth pass found the clause had essentially no proof
   coverage of its own (steps 1-3 never mention `S³`) and that its best
   available support — the `Spin(3)×Spin(6)`-type inner/outer argument
   (`C173` §8b point 5) — is the SAME class of argument this document
   already withdrew (§0c) as invalid for Hom-space distinguishability
   claims specifically. Rather than hunt for a fourth citation, the
   clause is dropped: the theorem now states only the `G₂`/`SU(3)`-
   restricted-data premise it actually proves. Nothing about `S³`'s
   isometry is claimed either way by this document any longer — that
   question is untouched, not resolved.
2. **`E1` narrowed to exclude `SO(7)`.** The fifth pass found the prior
   wording ("larger than `su(3)`, rank > 2, not confined within `g₂`")
   admits `so(7)` (rank 3) as a passing example — but under `SO(7)`
   confinement (the stabilizer of a single vector in `8_v`), `8_v=7⊕1`
   and `8_s≅8_c` remain UNDISTINGUISHED, exactly the failure this theorem
   is about. `round124`'s own decision.md already checks and reports this
   exact point (`TRIALITY_DISTINGUISHABILITY_GATE.md` §2b: "Zero fixed
   vectors in `8_v` confirms this algebra also escapes confinement to
   `SO(7)`, the same structural signature that let `SO(4)×SO(4)` work") —
   the missing condition was already sitting in a source this document
   already cites, just not carried into `E1`'s own wording. Fixed by
   adding the same zero-fixed-vector condition explicitly.
3. **`E2`'s "a different `t`" example removed, not reworded.** The fifth
   pass found this example was likely NULL: `C73`'s `build_numeric_dirac`
   takes `(E, nomizu)`, no `t` argument at all; `t` parametrizes a
   separate `S³`-side factor that `C173` states decouples `t`-independently
   from the `S⁶`/`so(8)` sector `C78` actually tested. Varying `t` would
   not change the operator `C78`'s exhaustive result is about, so it does
   not illustrate `E2`'s general point (a genuinely different operator) at
   all. Removed rather than replaced with an unverified substitute — `E2`
   as a category (a structurally different Dirac operator/connection)
   remains valid and real; this document does not currently have a
   concrete example of it.

`§5`'s reproduction trail drops the `C191` citation, which existed only to
support the now-removed `S³`-clause and is not cited by anything else in
this document.

This is the FIFTH round of self-correction, and the first one resolved by
explicit human decision rather than another autonomous skeptic cycle —
consistent with, not an exception to, the pattern named in §0e: once a
correction loop has run its useful course (here, 3+ cycles per the
stack's own cap), the right move is to surface the remaining judgment
calls, not keep autonomously re-guessing at them.

## 0g. rev 6 → rev 7 — a sixth skeptic pass, requested by the user, found the first genuine mathematical gap (not just a citation error)

The user explicitly asked for a sixth pass after rev 6. It found the most
substantive defect in this document's history — the fix in `E1` (rev 6)
was not merely imprecisely worded, it was FALSE — plus a wrong
justification in `E2` that happened to reach a correct conclusion, plus
several provenance errors introduced by rev 6's own "mechanical" fixes
(the same "fix relocated, not removed" pattern, now inside the
bookkeeping itself). All fixed directly, no further escalation needed —
these are checkable mathematical/citation facts, not judgment calls:

1. **`E1`'s `SO(7)`-exclusion (rev 6) blocks only ONE of THREE conjugacy
   classes of `Spin(7)` in `Spin(8)`, and `su(3)` sits inside a different
   one.** `Spin(8)` has three inequivalent embeddings of `Spin(7)`, one
   as the stabilizer of a vector in each of `8_v`, `8_s`, `8_c`
   (triality permutes them). Step 1 of this document's own proof
   establishes `8_v|_{g₂}=8_s|_{g₂}=8_c|_{g₂}=7⊕1` — `g₂` fixes a line in
   ALL THREE 8-dim reps, hence `g₂` sits inside all three `Spin(7)`
   copies at once, and so does `su(3)⊂g₂`. `round124`'s "zero fixed
   vectors in `8_v`" check (used by rev 6 to build `E1`'s exclusion) only
   rules out `so(7)_v` (the vector-stabilizing copy). It does nothing
   against `so(7)_s` (stabilizer of a spinor in `8_s`, dim 21, rank 3):
   under `so(7)_s`, `8_s=7⊕1` while `8_v≅8_c≅Δ₇` (the 8-dim spin rep of
   this `Spin(7)` copy, irreducible — zero fixed vectors in `8_v`,
   passing round124's own check vacuously) — `8_v` and `8_c` remain
   UNDISTINGUISHED, `su(3)⊂g₂⊂so(7)_s` passes every one of rev 6's proxy
   conditions, and the theorem's own failure mode occurs anyway. The same
   construction works with `8_c` singled out instead. **Fixed by
   replacing the geometric proxy (rank, containment, named-subgroup
   exclusion) with the actual mechanism**: `E1` now states the real test
   directly — `Hom_h(channel_i,channel_j)=0` for all `i≠j` — the same
   Schur's-lemma computation as step 1, just for a bigger `h`, checked
   case by case (as `round124` and `round119` already were) rather than
   inferred from a shortcut that turns out not to hold in general.
2. **`E2`'s rev-6 justification ("`build_numeric_dirac` has no `t`
   argument") is false, though its conclusion survives for a different
   reason.** `C73`'s own `test_deformation` function builds exactly a
   `t`-parametrized family (`nomizu_t` = `t` times the Nomizu structure
   constants, then `build_numeric_dirac(E, nomizu_t)`), swept over eight
   values including negative and `>1`. The reason this family cannot
   escape `C78`'s result is not that the parameter doesn't exist — it is
   that `commutant(t·D)=commutant(D)` for any nonzero scalar `t`, a
   uniform rescaling never changes what commutes with an operator. This
   project also uses `t` for something unrelated (`OB1`/`OB13`'s `S³`-
   connection torsion, which `C78`'s `D` never touches at all) — the two
   should not be conflated, which the rev-6 text did by attributing the
   "decouples" language to the wrong `t`. Fixed: `E2`'s "why it escapes"
   column now states the real reason (scale-invariance), and the example
   is restored with the correct framing rather than removed — `C73`'s own
   script's honest limitation ("no genuinely different admissible `S6`
   connection... exists anywhere in this project") is cited directly.
3. **Two provenance errors from rev 6's own "mechanical" fixes.** Both
   the `C173` §8c stale-citation fix (§0) and the seven-gate section-
   number fix (§2b) were labeled "corrected in rev 5, §0e" — but neither
   fix was actually applied until rev 6, and §0e does not contain an
   entry for the section-number error at all (it is a rev-6/§0f finding).
   Fixed: both now correctly say "found by the fifth pass, fixed in
   rev 6/§0f."
4. **The §2b "Honesty note" (written in rev 5) itself overclaimed.** It
   called `C78`'s scope statement (§10 of `TRIALITY_DISTINGUISHABILITY_GATE.md`)
   "precise about" the candidate-subalgebra-class vs. literal-`[D,U]=0`
   distinction — but that distinction is this document's OWN correction;
   the source draws no such line (§8/§9/§10 use "Gate 2" for both
   uniformly). Fixed: the note now says so explicitly, and the separate
   claim that this was "independently checked against `C78`'s own code"
   is withdrawn — `C78`'s script never constructs the 24-dim fiber `F`
   at all (it works in a transported 64-dim `Σ⊗Σ` space), so nothing in
   that code checked this specific claim; it is a general representation-
   theory fact, not a code-verified one.
5. **§1's `C173`-summarizing quote about `G102`** was attributed directly
   to `G102`'s own decision.md, where it does not appear — it is `C173`
   §0 point 2's characterization of `G102`. Fixed. A truncated quote from
   `C78` ("the largest symmetry `D` HAS, full stop") dropped its own
   qualifier "within `so(8)`" — restored.
6. **§4 gains an explicit point (point 6) naming the `S³`-data gray zone**
   left by rev 6's removal of the `S³`-clause — it was dropped from §1
   correctly but never added to the "what this does NOT claim" list or
   flagged as a gap the way the morphism-level "un-enumerated door" (§3)
   already is.

The theorem's core (§1 steps 1-3) was re-verified independently in this
pass too — Hom dimensions, residuals, and negative-control numbers all
recomputed from the representation theory directly, not merely re-quoted
— and remains clean. Every defect across six rounds now has landed in
either scope/citation precision or, this once, a genuine escape-condition
gap — never in the core mechanism.

---

## 1. Theorem statement (corrected)

**Theorem (G₂/SU(3)-restriction Non-Discrimination).** Let `M` be any
candidate mechanism whose observable factors ENTIRELY through data that
survives `Spin(8) → G₂` restriction (or the weaker `→ SU(3)` restriction)
of a single channel — its isomorphism class, its `g₂`- or `su(3)`-module
structure, or its trilinear covariance relations (`C62`). Then `M` cannot
distinguish the three triality channels `8_v`, `8_s`, `8_c`.

**Removed in rev 6, per explicit user decision (§0f):** earlier drafts
optionally extended this premise to include `S³`'s own `SU(2)_L×SU(2)_R`
isometry data. The proof below (steps 1-3) never uses `S³` data at all,
and every citation offered in support across three revisions (`C173` §8b
point 5, then `C191`) was independently found unable to carry the claim —
see §0e/§0f. Rather than keep patching the citation, the clause is
dropped. This document makes NO claim about whether `S³`'s isometry data
adds discriminating content — that question is untouched, not resolved
either way.

**Proof (primary mechanism — Schur's lemma / Hom-space filtration):**

1. `G102` P7/P8 (independently re-verified by `C72`): `dim
   Hom_{g₂}(channel_i,channel_j) =
   2` and `dim Hom_{su(3)}(channel_i,channel_j) = 6`, IDENTICAL for every
   ordered pair `i,j ∈ {v,s,c}` including `i=j`. `C72` additionally
   constructs EXPLICIT invertible `g₂`-equivariant isomorphisms between
   all three channels (residual `5e-16`–`7e-16`).
2. Any object built entirely from `g₂`- or `su(3)`-equivariant data is,
   by definition, invariant under composing with these explicit
   isomorphisms — i.e. it takes the IDENTICAL value on all three channels
   (`C72`'s own point: "isomorphic objects take equal values under any
   functor"). This is the base mechanism and needs nothing beyond Schur's
   lemma plus the explicit isomorphisms already built.
3. `C62` checked the one plausible escape at the morphism/trilinear level
   (not just the object level) — Baez's octonion trilinear-covariance
   construction — and found it ALSO collapses to the identical matrix on
   all three channels (deviation `1.6e-15`, vs `4.53`/`2.91` for a generic
   non-`g₂` negative control).

**`G44`'s branching computation is the `G₂`-restriction special case of
step 1**, at `n=8`: `8_v|_{G₂} = 8_s|_{G₂} = 8_c|_{G₂} = 7⊕1` is exactly
what `dim Hom_{g₂}=2`, uniform across pairs, predicts by Schur's lemma —
this connection is §0's own point (`C173` §0 point 2, characterizing
`G102`: "the SAME fact, sharpened to the `SU(3)` level and quantified" —
corrected in rev 7, a sixth skeptic pass found an earlier draft attributed
this quote directly to `G102`'s own decision.md, where it does not
appear; it is `C173`'s summary OF `G102`), not a separate citation.
**Corrected in rev 5, §0e:** an earlier draft cited `C173` §8c here with an ellipsis
hiding that §8c's full sentence is about `C78`'s numerical commutant
result, not `G44`'s branching, and that its unquoted tail is exactly the
"for any physical `D`" universal §0d withdrew — that citation is dropped
from this paragraph.

**rev 2's steps 4-5 are WITHDRAWN here — they were wrong, not merely
imprecise, per a second independent skeptic pass and direct
re-verification against `TRIALITY_DISTINGUISHABILITY_GATE.md`.** rev 2
claimed the centralizer of `g₂`/`su(3)` in `so(8)`, being inner, "cannot
help" distinguish channels even if adjoined. **This is false as a
statement about algebraic (Gate 1) distinguishability**: `round124`
(`TRIALITY_DISTINGUISHABILITY_GATE.md` §2b, lines 62-65) computes exactly
this — adjoining `su(3)`'s own 2-dim centralizer gives the bigger algebra
`su(3)⊕u(1)⊕u(1)` (rank 4), under which `dim Hom(channel_i,channel_j)=0`
for `i≠j`, i.e. GENUINELY discriminating, `[VERIFIED-tool]`, basis-
rotation-invariance checked. The inner/outer argument does not rule this
out, because Gate-1 discrimination via a Hom-space computation does not
require literally constructing an element that IS the triality
automorphism — see §2b below for where this argument actually applies.

---

## 2. Scope — read before applying the escape criterion

**This theorem is about mechanisms confined to `G₂`/`SU(3)`-restricted (or
weaker) data. It says NOTHING about mechanisms using data that survives at
the FULL `so(8)` level.** `G102`'s own P5/P6 (`Hom_{so(8)}(channel_i,
channel_j)=0` for `i≠j`) show the channels genuinely ARE algebraically
distinguishable there — `C150/GATE.md`'s own "Scope" section states this
explicitly (point 1) and its "constructive reading" section (point on
`C63`) says plainly: "What this project lacks is not the existence of
distinguishing information, but a construction in which that information
is PHYSICALLY REALIZED."

## 2b. Algebraic distinguishability vs the Commutant Condition — and exactly what `C78` proved

Two DIFFERENT questions, corrected in rev 4 (§0d) to also fix a naming
collision inside the project's own terminology: this document previously
called these "Gate 1" and "Gate 2," but the project's own two related
documents use "Gate 2" for TWO different things in two different
numbering schemes — `TRIALITY_DISTINGUISHABILITY_GATE.md` §3's
five-condition list, where condition 2 = `[D,U]=0` for the SPECIFIC
triality operator `U` (found by the fifth skeptic pass, fixed here in
rev 6/§0f: the "§4/§7" citation for the second scheme was itself
imprecise — the seven-gate enumeration lives in
`L3B_SPIN8_INTERFACE_SPEC.md` §7, which `TRIALITY_DISTINGUISHABILITY_GATE.md`
§3/§4 cite, not in that file's own §7, a registry-updates section); and
the seven-gate list, where Gate 2 = the global principal-bundle action —
a different, untested question — and `OB4`'s own "Gates 2-6" are the
seven-gate list. To stop re-creating that collision, this document drops
"Gate 1"/"Gate 2" from here on and uses plain names instead.

**Honesty note, corrected in rev 7 (§0g) after a sixth skeptic pass found
the rev-5 version of this note itself overclaimed:** the distinction just
drawn (candidate-discriminating-subalgebra class vs. the literal
`[D,U]=0` condition on `U`) is this document's OWN correction, and it is
NOT something `TRIALITY_DISTINGUISHABILITY_GATE.md` itself states cleanly
— that file's own §8/§9/§10 treat "Gate 2" and "`[D,U]=0` for candidate
generators" as the SAME thing throughout, with status lines reading
`GATE 2: TESTED, NO` / `CLOSED (NO), exhaustively` on that basis; an
earlier draft of this note called `C78`'s own scope statement (§10)
"precise about this" distinction, which overstates it — §10 does not
draw this distinction, this document does. The underlying MATH for why
they are not the same thing is sound (`U` realizes an outer automorphism
and cannot be represented in `so(8)`'s action on the 24-dim fiber
`F=8_v⊕8_s⊕8_c`, which — by general representation theory, since `so(8)`
preserves each channel — is block-diagonal per channel, while `U`
permutes channels). **Corrected in rev 7:** an earlier draft claimed this
was "independently checked against `C78`'s own code" — false: `C78`'s
script (`c78_so8_commutant_exhaustive.py`) works entirely in a
transported 64-dimensional `Σ⊗Σ` space and never constructs the 24-dim
`F` at all, so nothing in that code checks this claim; it is a general
structural fact about how `so(8)` acts, not a code-verified one. Flagged
explicitly here so a reader who goes to check
`TRIALITY_DISTINGUISHABILITY_GATE.md` §8-§10 directly is not surprised to
find it calling this same test "Gate 2, TESTED, NO" throughout.

- **Algebraic distinguishability.** Escapable, and already escaped twice,
  independently, by two DIFFERENT arguments: `round124`'s
  `su(3)⊕u(1)⊕u(1)` gives `Hom(channel_i,channel_j)=0` for `i≠j`,
  `[VERIFIED-tool]` (§1 above); `round119`'s `SO(4)×SO(4)`
  (`OPEN_BLOCKERS.md` OB4) uses a DIFFERENT, also-real argument —
  block-chirality matching (`8_s`: `Γ_A=Γ_B`; `8_c`: `Γ_A=-Γ_B`,
  `TRIALITY_DISTINGUISHABILITY_GATE.md` §2), not a computed `Hom`-space
  table. **Corrected in rev 5 (§0e):** an earlier draft attributed
  `[VERIFIED-tool] Hom=0` to BOTH candidates; only `round124` has that
  specific computation — the source itself contrasts the two arguments
  rather than treating them as one.
- **The Commutant Condition — does the candidate symmetry actually
  commute with THIS PROJECT'S ONE SPECIFIC, ALREADY-BUILT physical Dirac
  operator `D` (`C73`'s `build_numeric_dirac`)?** `C75`/`C77` tested
  `round124`'s and `round119`'s candidates DIRECTLY against this `D` —
  both FAIL: `round124`'s two extra generators violate by `65.5%` and
  `352%` (`C75`, `TRIALITY_DISTINGUISHABILITY_GATE.md` §8); all 12 of
  `SO(4)×SO(4)`'s generators violate by `35.4%`-`353%` (`C77`, §9) — both
  far above the `2.8e-17` positive-control noise floor. **(Corrected in
  rev 5: rev 4 quoted `65.5%-352%`, `C75`'s own range, as if it also
  covered `C77`; the two candidates have separate, though overlapping,
  ranges.)** `C78` (§10) then computed the FULL commutant of this SAME,
  ONE `D` within all of `so(8)` at once (a single 28-dim SVD null-space
  computation): `commutant_dim = 8`, exactly `su(3)`, nothing larger —
  for THIS operator, `[VERIFIED-tool]`.

**What this does NOT establish, part 1 (corrected in rev 4, §0d):**
`C78`'s own decision.md is explicit that this result is about the one `D`
tested, not a universal over every `D` built from `G₂/SU(3)` data — its
own wording is "the largest symmetry `D` HAS," not "the largest symmetry
any such `D` could ever have." The inner/outer argument (triality outer,
`Spin(8)` connected) bounds whether an inner automorphism can REALIZE
triality; it does NOT bound the DIMENSION of a commutant, which is a
computed fact about one operator's specific matrix, not a structural
consequence of connectedness.

**What this does NOT establish, part 2 (corrected in rev 5, §0e — rev 4's
own attempted fix introduced this error while removing the first one):**
`C78`'s commutant computation is ALSO not a test of condition 2 as
formally defined (`[D,U]=0` for the specific triality operator `U`).
`U` realizes an OUTER automorphism (condition 1) and therefore is not,
and cannot be, an element of the Lie algebra `so(8)` — a commutant
computation within `so(8)`, however exhaustive, structurally cannot
include or exclude it. `TRIALITY_DISTINGUISHABILITY_GATE.md`'s own
summary of `C78` (§10 — corrected in rev 7: an earlier draft called this
"`C78`'s own stated scope," but the wording quoted is that file's summary
of `C78`, not a quote from `C78`'s own decision.md, which does not use
the phrase "distinguishes the channels" — see §0g) states: "Gate 2, for
the entire class '**some subalgebra of `so(8)`** distinguishes the
channels and is respected by the physical `D`,' is now CLOSED (NO),
exhaustively" — a claim about candidate DISCRIMINATING
SUBALGEBRAS (the `round124`/`SO(4)×SO(4)`-shaped candidates and anything
like them), not about whether `U` itself commutes with `D`. Whether `U`
does is the project's own separately-named, still fully open
"channel-permutation/redundancy" question: `C75`, `C78`'s own "what this
does NOT show" §2, and `C77`'s Kill Analysis all state this specific test
has never been run — the same gap this document's own `E1` note (§3)
already flags without, until this correction, connecting it back here.

**Corrected status:** `commutant(D_physical, so(8)) = su(3)` —
`[VERIFIED-tool]`, for `C73`'s specific `D` — closes the entire class of
candidate DISCRIMINATING SUBALGEBRAS of `so(8)` for that one `D` (part 2
above). Whether ANY OTHER `D` built from `G₂/SU(3)` data would also have
commutant exactly `su(3)` is `[UNKNOWN]` (part 1). Whether the literal
triality operator `U` commutes with `D` — a question no `so(8)`-only
computation can even address — is `[UNKNOWN]`, untested, per the same
sources.

**Corrected consequence for `OB4`:** `C78` closes the candidate-subalgebra
class described above, for the one `D` tested — it does not close
condition 2 of `TRIALITY_DISTINGUISHABILITY_GATE.md` §3's five-condition
list literally, and it says nothing about the seven-gate list's Gates 2-6
(principal-bundle action, gauge-orbit audit, zero-mode map under `K`, 4D
effective action, basis-invariant observable) — none of which has ever
been attempted. `OPEN_BLOCKERS.md` OB4 — compressed a month after `C78`,
and citing `C78` by name in `OB11`'s own condition (iii) — correctly
still records Gates 2-6 as "PARKED, not falsified." This document does
not change that; rev 3's claim that it did ("PROVEN CLOSED") is
withdrawn.

## 3. Known sufficient conditions for escape (not proven exhaustive)

A candidate mechanism `M` is **outside this theorem's scope** — i.e.
worth attempting, though not thereby guaranteed to work — if at least one
of `E1`-`E5` below holds. **Corrected in rev 4 (§0d): this is a list of
known sufficient conditions, NOT a proven necessary-and-sufficient
criterion.** `C150/GATE.md`'s own "Scope" point 2 states that a different
morphism-level or extension-level datum "could in principle escape" this
theorem while still satisfying its premise, and no such datum is
represented by `E1`-`E5` — see the note after the table; that door stays
explicitly open rather than silently closed.

| # | Escape condition | Why it escapes | Status in this project |
|---|---|---|---|
| E1 | `M` uses data equivariant under a subalgebra `h ⊆ so(8)` for which `Hom_h(channel_i,channel_j) = 0` for ALL `i≠j` — i.e. `h` genuinely, computably breaks the Schur's-lemma degeneracy that step 1 establishes for `g₂`/`su(3)`, checked directly, not inferred from rank or from avoiding any one named subgroup (corrected in rev 7, §0g, after a sixth skeptic pass found the rev-6 proxy criterion FALSE in general: `g₂`, hence `su(3) ⊂ g₂`, sits inside not one but THREE conjugate copies of `spin(7)` in `so(8)` — one per channel, since step 1's own `8_v\|_{g₂}=8_s\|_{g₂}=8_c\|_{g₂}=7⊕1` means `g₂` fixes a line in EACH of the three 8-dim reps, i.e. `g₂` ⊆ stabilizer-of-a-line-in-`8_x` for every `x∈{v,s,c}`. `round124`'s own zero-fixed-vector check (`TRIALITY_DISTINGUISHABILITY_GATE.md` §2b) only rules out the copy `so(7)_v` (stabilizer of a vector IN `8_v`) — but `su(3) ⊂ g₂ ⊂ so(7)_s` (stabilizer of a spinor in `8_s`, dim 21, rank 3) satisfies every rev-6 proxy condition (rank>2, not within `g₂`, not `so(7)_v`) while leaving `8_v≅8_c` (both `≅Δ₇`, the 8-dim spin rep of this `so(7)` copy) UNDISTINGUISHED — the theorem's own failure mode, passing its own escape condition. The proxy is replaced here by the actual mechanism, matching step 1's own method) | This is the SAME mechanism as step 1 (Schur's lemma / Hom-space filtration), applied to a bigger algebra where the `g₂`/`su(3)`-level degeneracy happens to break — not a separate geometric criterion | **Already used, ALGEBRAICALLY real, not hypothetical, by two DIFFERENT arguments, each independently verified for the SPECIFIC construction, not derived from a general proxy** (corrected in rev 5: rev 4 wrongly attributed a `Hom`-space computation to both): `round124`'s `su(3)⊕u(1)⊕u(1)` gives `Hom(channel_i,channel_j)=0` for `i≠j`, `[VERIFIED-tool]`, directly computed; `round119`'s `SO(4)×SO(4)` (`OPEN_BLOCKERS.md` OB4 Gate 1) distinguishes ALL THREE channels via block-chirality matching (`Γ_A=Γ_B` vs `Γ_A=-Γ_B`), a separate, also-real, also directly-verified argument — the source describes it as the first candidate in that investigation to separate `8_s` from `8_c` as well as `8_v`. **This clears algebraic distinguishability only, and only for these two SPECIFIC, checked constructions — not for any subgroup merely resembling them** — see the Commutant Condition note below before treating either as a working physical mechanism |
| E2 | `M` uses a physical Dirac operator/connection genuinely STRUCTURALLY different from `C73`'s `build_numeric_dirac(E, nomizu)` — not merely a uniform rescaling of the SAME `nomizu` input, since `commutant(t·D) = commutant(D)` for any nonzero scalar `t` (scaling an operator never changes what commutes with it) | `C78`'s commutant computation is about that ONE operator up to the scale-invariance just noted; a genuinely different connection/Nomizu structure is an untested premise, not covered by the same computation | Not attempted; no concrete candidate identified. **Corrected in rev 7, §0g, after a sixth skeptic pass found the rev-6 justification here FALSE:** rev 6 removed an earlier "a different `t`" example on the grounds that "`build_numeric_dirac` takes no `t` argument" — wrong: `C73`'s own `test_deformation` routine builds exactly this family (`nomizu_t = {i: [(t*cf,a,b) for (cf,a,b) in R59.NOMIZU[i]] for i in R59.NOMIZU}`, then `build_numeric_dirac(E, nomizu_t)`, swept over `t ∈ [-1,0,0.5,0.9,1,1.1,1.5,2]`). The conclusion (this family does not escape) happens to still be correct, but for the reason stated in this row's own "Why it escapes" column (scale-invariance of the commutant), not because the parameter doesn't exist. Separately: this project uses `t` for TWO unrelated things — this NOMIZU-rescaling parameter (`S⁶`-side, what `C73`/`C78` actually vary) and `OB1`/`OB13`'s `S³`-connection torsion parameter (a genuinely different, decoupled quantity `C78`'s `D` never touches) — do not conflate them. `C73`'s own script states the honest limitation directly: "this is a 1-parameter uniform-scale family only — no genuinely different admissible `S6` connection... exists anywhere in this project" — a real gap, not a vacuous one |
| E3 | `M` invokes a group element outside `Spin(8)` entirely (e.g. `Pin(8)\Spin(8)`, or another exceptional construction) | Only elements outside the connected group `Spin(8)` can be outer automorphisms | Not attempted; `G102`'s own stated conclusion names this as one reading of "an independent fiber-Spin(8) postulate" |
| E4 | `M` is supplied by genuinely external input (literature, or Tom Lawrence) carrying triality-channel content not derived from this project's own `S³×S⁶` geometry | External data is not subject to an internal-symmetry argument at all | `BLOCKED-EXTERNAL` per `OPEN_BLOCKERS.md` OB1/OB4/OB14 |
| E5 | `M` uses a geometric factor OTHER than `S⁶=G₂/SU(3)` (a different internal manifold entirely) | Changes the premise, not a mechanism within it | Out of scope; would be a different project |

**Un-enumerated door, per `GATE.md`'s own Scope point 2 — do not treat
`E1`-`E5` as exhaustive.** A different morphism-level or extension-level
datum could in principle escape this theorem even while satisfying every
stated premise: `C62`'s trilinear-covariance check (used in step 3 of
§1's proof) is ONE tested instance, not a general categorical closure. No
specific such datum is known to this project; this is an acknowledged
gap, not a sixth named escape route.

**On `E1` and the Commutant Condition:** `E1` clears algebraic
distinguishability only. Whether a mechanism built this way ALSO
satisfies the Commutant Condition against `C73`'s specific `D` is a
SEPARATE, already-tested question for the two constructions on record:
`round124` and `SO(4)×SO(4)` were BOTH individually tested (`C75`/`C77`)
and both FAIL against that one `D` — `round124`'s extra generators violate
by `65.5%`/`352%`, `SO(4)×SO(4)`'s by `35.4%`-`353%` (corrected in rev 5:
these are two separate ranges, not one shared range) — both far above a
`2.8e-17` noise floor. This closes the class of candidate DISCRIMINATING
SUBALGEBRAS for `C73`'s `D` (`C78`, §2b), but per §2b's own correction it
does NOT close whether the literal triality-permutation operator itself
commutes with `D` — `C75`'s and `C78`'s own "what this does NOT show"
sections and `C77`'s Kill Analysis all flag that specific test as never
run, precisely because a permutation could in principle map `D`'s
spectrum to itself without commuting with every generator of a candidate
subalgebra. `E1` alone is a real but incomplete escape — cite
`C75`/`C77`/`C78` and this caveat; do not present algebraic escape alone
as resolving anything, and do not present the Commutant Condition's
current failure as "still open" without noting the candidate-subalgebra
class is proven closed for `C73`'s `D` specifically (not for `D` in
general, §2b part 1), while the channel-permutation operator itself
remains untested (§2b part 2).

## 4. What this does NOT claim

1. Does NOT claim `N_gen=3` is false, or triality irrelevant — only that
   `G₂`/`SU(3)`-restricted mechanisms specifically cannot supply channel
   discrimination.
2. Does NOT claim `OB4` Gates 2-6 or `OB11(iii)` are resolved in either
   direction — `OB4` Gates 2-6 (the seven-gate numbering's principal-
   bundle action, gauge-orbit audit, zero-mode map, 4D effective action,
   basis-invariant observable) have never been tested and remain exactly
   as `OPEN_BLOCKERS.md` records them: PARKED, not falsified (corrected
   in rev 4, §0d — rev 3 wrongly claimed these were "PROVEN CLOSED",
   conflating them with a different, already-closed question — see
   point 4 and §2b).
3. Does NOT re-derive `G102`, `C65`, `C72`, `C78`, or `C173`'s own
   computations — cites and formalizes them.
4. Does NOT itself edit `OB1`/`OB4`/`OB14`'s status lines in
   `OPEN_BLOCKERS.md`, and does not claim they should change. What `C78`
   DID close — for `C73`'s one specific `D` — is the entire class of
   candidate DISCRIMINATING SUBALGEBRAS of `so(8)` (corrected in rev 5,
   §0e: NOT literally condition 2 of `TRIALITY_DISTINGUISHABILITY_GATE.md`
   §3's five-condition list, `[D,U]=0` for the specific triality operator
   `U` — `U` realizes an outer automorphism and is not an `so(8)` element,
   so no `so(8)`-commutant computation can test it). This is separately
   a DIFFERENT thing from `OB4`'s seven-gate-list "Gates 2-6" (point 2
   above). Whether the Commutant Condition also fails for some OTHER `D`
   built from `G₂/SU(3)` data is `[UNKNOWN]` (§2b part 1); whether `U`
   itself commutes with `D` is `[UNKNOWN]`, untested (§2b part 2) — see
   §2b and `E2` in §3.
5. Does NOT claim completeness against a construction not yet conceived
   that would fail one of the premise's own stated assumptions.
6. **Added in rev 7, §0g, after a sixth skeptic pass:** does NOT claim
   anything about mechanisms built from `S³`'s own `SU(2)_L×SU(2)_R`
   isometry data — that clause was removed from the theorem statement in
   rev 6 (§0f), and no such mechanism is covered by the premise OR listed
   among `E1`-`E5`. This is an acknowledged gray zone, alongside the
   morphism-level "un-enumerated door" already noted after the `E1`-`E5`
   table in §3 — not resolved either way by this document.

## 5. Reproduction / verification trail

- `experiments/20260620-g44-d4-triality/decision.md` (G44)
- `experiments/20260705-g102-spin8-fiber-obstruction/decision.md` (G102, P1-P8 table — the primary mechanism)
- `experiments/20260904-c150-g44-information-retention-gate/GATE.md` (C72/C63/C62 synthesis, the gate's own scope section)
- `experiments/20260906-c173-p4-items23-scoping-g44-nogo/decision.md` (the inner/outer strengthening, §2, §8b)
- `OPEN_BLOCKERS.md` OB4 (Gate 1 DONE — the `E1` escape route, already
  real; Gates 2-6 PARKED, not falsified — the status this document leaves
  unchanged, per §4 point 4). **Dropped in rev 6:** `experiments/20260909-
  c191-p5-so4-postulate-pairing-test/decision.md` (C191) was cited here
  only to support the `S³`-clause removed from §1 (§0f); nothing else in
  this document depends on it, so the citation is removed rather than left
  dangling.
- `TRIALITY_DISTINGUISHABILITY_GATE.md` §1 (the five-condition spec's own
  definitions — condition 1 = `U` exists, condition 2 = `[D,U]=0` for
  THAT specific `U`, condition 3 = a genuine `Spin(8)` action extending
  `U`), §2b (round124's `su(3)⊕u(1)⊕u(1)` construction, the
  algebraic-distinguishability escape this document's §2b/§3 `E1` cites),
  §2 (round119's `SO(4)×SO(4)` block-chirality argument, `E1`'s other
  cited construction), §8-9 (C75/C77 — round124 and `SO(4)×SO(4)` each
  individually fail the Commutant Condition against the physical `D`,
  with their own separate Frobenius ranges), §10 (C78 — commutant
  computation for that one `D`, `commutant_dim=8`, exactly `su(3)`,
  closing the candidate-discriminating-subalgebra class for that
  operator, per §2b — NOT literally condition 2 above, corrected in
  rev 5), §11 (C83 — the CANDIDATE ALGEBRA `so(4)_1+so(4)_2` itself, not
  its complement, has an exact 1-dimensional intersection with `su(3)`;
  corrected in rev 5 from an earlier subject/complement mix-up), §12
  (C173 cross-reference — the general Lie-theory inner/outer reason,
  bounding triality-realizability, not commutant dimension — see §2b for
  why these are different claims)
