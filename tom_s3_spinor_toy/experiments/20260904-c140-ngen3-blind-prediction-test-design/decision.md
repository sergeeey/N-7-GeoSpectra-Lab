# C140 decision — DESIGN-ONLY round (no physics computation, per its own
# claim.md). Verdict: DESIGN READY, WITH A MAJOR PRE-EXISTING-WORK
# CORRECTION found during the round's own mandatory novelty check — the
# population this design proposed (the 4 Butruille homogeneous
# nearly-Kähler 6-manifolds) is NOT a fresh idea in this project. It is
# already the subject of an active, partially-completed "Universality"
# program (round51, round59, round64, round65, round70, round71), and
# that program's own track record (2 of 4 spaces give clean results, 2
# of 4 give ILL-POSED) is strong evidence this design's most likely
# execution outcome is INCONCLUSIVE, not a clean PROMOTE/REJECT.

**Date:** 2026-09-04
**Type:** DESIGN round, not an FL experiment execution. No `results_c140.json`,
no physics claim tested, no PROMOTE/REJECT/NULL verdict — only a design-readiness
assessment plus a corrected next-step recommendation.

## 1. Source-trace verification (FL Step -4) — the Butruille/Wolf citation

`[VERIFIED via WebSearch, this session]`: the classification of homogeneous,
simply-connected, strictly nearly-Kähler 6-manifolds is real, closed, and
independently pre-existing (Butruille 2005, building on J.A. Wolf's earlier
classification of 3-symmetric spaces). Four members, confirmed by independent
secondary sources returned by the search (e.g. the arXiv papers "Totally
geodesic submanifolds of the homogeneous nearly Kähler 6-manifolds and their
G2-cones" and "S6 and the geometry of nearly Kähler 6-manifolds"):

1. `S^6 = G2/SU(3)`
2. `S^3 x S^3 = (SU(2)xSU(2)xSU(2))/SU(2)`
3. `CP^3`
4. `F(1,2) = SU(3)/T^2` (the flag manifold)

This citation is genuine and predates this project by two decades. It is a
legitimate, independently-fixed "blind" population, as claim.md required.

## 2. Novelty check (FL Step -3) — MAJOR FINDING, corrects this round's own
## framing

Per claim.md's own verification-plan instruction ("check null_results/INDEX.md
and pearl_registry/INDEX.md for any prior attempt at exactly this comparison
under a different name"), a grep for `nearly-Kahler`, `Butruille`, `S3xS3`,
`CP3`, `flag manifold` across the registry surfaced an existing, substantial,
still-open project program that this claim.md's first draft did not know
about:

| Round | Manifold | Question | Verdict |
|---|---|---|---|
| `round59` (2026-07-14) | `S^6` (base case) | trivial-block rank of twisted Levi-Civita Dirac | PASS, `rank=1`, mechanism-forced by Killing-spinor existence |
| `pearl_registry:24` | (proposes generalizing) | *"On any other nearly-Kähler coset admitting Killing spinors ... the analogous trivial-block rank should also be 1 ... a cheap partial answer to the Universality open problem"* | names the SAME 4-manifold population this design independently arrived at |
| `round51` (2026-07-13) | scoping | Universality open problem, initial scoping | — |
| `round64` (2026-07-15) | `CP^3` | reuse Charbonneau-Harland 2016's Weitzenbock formula for the trivial-block route | **ILL-POSED** — probe could not be executed as scoped |
| `round65` (2026-07-15) | `SU(3)/T^2` | Killing-spinor route (same mechanism as round59, re-derived from scratch, not copy-pasted) | **PROMOTE** — `rank=1` forced there too, 2/9 weight-pairs check clean |
| `round70` (2026-07-17) | `CP^3` + `S^3xS^3` | E5, second attempt at Universality | mixed / see file |
| `round71` (2026-07-17) | `S^3xS^3` | Nomizu torsion audit, two independent repair attempts | **ILL-POSED** — no forced construction found either way |

**What this means for C140's own design:** the "genuinely blind population of
4 independently-classified manifolds" this design proposed is real and sound
as an IDEA, but the specific population is not novel to identify — this
project already uses it, under the name "the Universality open problem," and
has a 3-year-old (relative to session time) track record on it: **1 trivial
base case (`S^6`), 1 clean success (`SU(3)/T^2`), 2 ILL-POSED (`CP^3` twice,
`S^3xS^3` twice)**, all for a DIFFERENT specific construction than the one
C140 proposes (round59/64/65/70/71 test trivial-block RANK via a
Killing-spinor/Weitzenbock argument; C140 asks about G102's TRIALITY-CHANNEL
DISTINGUISHABILITY via the `dim c_{so(8)}(g)`-style fiber-obstruction check —
related, both inputs to `N_gen=3`, but not the same question, so this is not
a duplicate in the Mechanism-Transfer-Gate sense of re-testing an
already-answered question).

**Per the Mechanism-Transfer-Gate's own discipline** (verify FORMULA / OBJECT
/ ROLE / GENERATOR / SECTOR / OBSERVABLE before calling something a
duplicate): the OBJECT (4-manifold population) and GENERATOR (nearly-Kähler
homogeneous structure) are shared with the Universality program; the FORMULA/
OBSERVABLE (channel-counting/`Spin(8)`-fiber-obstruction vs. trivial-block
Dirac rank) differ. This is judged NOT a duplicate, but a closely-related
sibling question that inherits the parent program's own empirical track
record as a strong prior on execution difficulty — stated honestly below,
not discovered only after a future round wastes effort re-hitting `CP^3`'s
and `S^3xS^3`'s already-documented ill-posedness.

## 3. Design-readiness verdict

**DESIGN READY**, with the risk assessment revised upward using real,
in-project evidence rather than this design's own a priori guess:

- (a) Citation confirmed — ✅ (Section 1).
- (b) A plausible construction recipe exists for at least one other manifold
  — ✅, and now evidenced, not merely plausible: `SU(3)/T^2`'s isotropy is
  abelian (`T^2 = U(1)xU(1)`) and round65 already built a from-scratch,
  independently-verified analogous computation there for the SIBLING
  question (trivial-block rank). The infrastructure (weight decomposition
  under `T^2`, explicit Killing-spinor convention shared across all 4
  Butruille spaces per Charbonneau-Harland 2016 §4, confirmed in round65)
  is directly reusable for building a channel-distinguishability check on
  `SU(3)/T^2` specifically.
- (c) ICE/inapplicability handling — ✅ in design, and now independently
  motivated: `CP^3` and `S^3xS^3` have EACH already produced two
  independent ILL-POSED verdicts for the sibling question (round64+round70
  for `CP^3`; round70+round71 for `S^3xS^3`). This does not prove the
  channel-distinguishability question will ALSO be ill-posed there — a
  different observable can behave differently on the same manifold — but it
  is real, specific, on-point evidence that these two spaces' isotropy
  structure has repeatedly resisted this project's own attempts to build
  well-posed comparative constructions on them, for structural reasons (not
  effort). Any future execution round attempting `CP^3` or `S^3xS^3` MUST
  read `round64`, `round70`, and `round71` in full first and state
  explicitly why the channel-counting construction differs from what
  already failed there — not attempt it fresh.

## 4. Corrected recommendation — which manifold to attempt first, IF this is
## ever executed

**`SU(3)/T^2`, not `S^6` (trivial/base) and not `CP^3`/`S^3xS^3` (both
carry two prior ILL-POSED verdicts each for the sibling question).** This is
a change from what an uninformed first attempt might guess (try the "next
simplest" looking manifold) — the actual best next step is the ONE manifold
this project has already shown, via a DIFFERENT but structurally related
construction, to admit a well-posed from-scratch computation using shared
Butruille-space machinery (Charbonneau-Harland 2016's common Killing-spinor
convention, confirmed applicable across all 4 spaces per round65's own
`claim.md`).

**Minimal execution spec for a future C141 (not built here):**
1. Reuse round65's `T^2`-weight decomposition of `SU(3)/T^2`'s isotropy
   representation.
2. Adapt G102's `dim c_{g}(su(3))`-style fiber-obstruction check (the
   construction that showed `dim c_{so(8)}(g2) = 0` for `S^6`) to `SU(3)/T^2`'s
   own structure group — check explicitly whether an analogous "how many
   independently-distinguishable channels" question is even well-posed for
   an ABELIAN isotropy group (`T^2`) the way it was for `G2`'s specific
   non-abelian structure — this is the step most likely to reveal the test
   is ill-posed here too, and should be checked FIRST, before any heavier
   computation, exactly per this project's own Substrate/Oracle-Adequacy
   gate discipline.
3. If well-posed: report the channel count for `SU(3)/T^2`. If it is NOT 3
   (or the question doesn't even have a "3-like" analogue there), this is
   suggestive (not conclusive, n=1) evidence against pure selection. If it
   IS well-posed and gives an analogous "3", that is a genuine, if narrow,
   positive data point FOR row 141's blind-prediction standard.
4. If ill-posed (the single most likely outcome given the sibling program's
   own 50% ill-posed rate across `CP^3`/`S^3xS^3`, though `SU(3)/T^2` itself
   has NOT been ill-posed for the sibling question): report honestly, and
   note that with only `S^6` (the base case, not a real test) and a second
   ill-posed manifold, pearl row 141's risk would remain fully open and
   possibly UNTESTABLE by this specific approach — a genuinely informative,
   if disappointing, outcome, worth stating plainly rather than searching
   for a third population.

## 5. Self-check (per claim.md, in place of a full skeptic pass for a
## design-only round)

**Does this design actually test what row 141 asks, or a nearby easier
question?** Read plainly: row 141 asks whether `N_gen=3`'s TRIALITY
structure specifically was selected because it gives 3. This design's
proposed C141 execution would test whether an ANALOGOUS channel-counting
construction is even well-posed, and if so what it gives, on ONE other
Butruille space (`SU(3)/T^2`, realistically the only accessible one). This
is a genuine but PARTIAL answer — a positive result on one manifold (out of
3 real alternatives, `S^3xS^3`/`CP^3`/`SU(3)/T^2`) would be suggestive, not
decisive; a full answer would need all 3, and 2 of those 3 already carry a
strong prior toward ill-posedness from the sibling program. This partiality
is now stated explicitly, per the self-check requirement, rather than left
implicit.

## 6. Registry actions — NOT performed by this round, proposed only

**`pearl_registry/INDEX.md` row 141** — append (do not overwrite) an update
note in the same style C121/C138 used to close/advance prior rows:

```
**SCOPED, NOT YET RUN (C140, 2026-09-04).** Design-only round confirmed the
Butruille/Wolf 4-manifold classification (S6, S3xS3, CP3, SU(3)/T2) as a
genuine independent "blind" population -- but found this is NOT a fresh
population for this project: it is already the subject of the "Universality
open problem" program (round51/59/64/65/70/71), with S6 (trivial base) and
SU(3)/T2 (round65, clean PROMOTE) giving well-posed results and CP3/S3xS3
each carrying TWO independent ILL-POSED verdicts (round64+round70 for CP3;
round70+round71 for S3xS3) for a related but distinct sibling question
(trivial-block Dirac rank, not triality-channel counting). Recommended next
step if pursued: attempt the channel-counting construction on SU(3)/T2 ONLY
first (reusing round65's T^2-weight machinery), since it is the sole
non-trivial Butruille space without a standing ill-posedness precedent for
constructions of this general type. A full answer to row 141 would need
CP3/S3xS3 too, both carrying a real risk of inconclusiveness independent of
this specific question. See
experiments/20260904-c140-ngen3-blind-prediction-test-design/decision.md.
```

**No `null_results/INDEX.md`, `CLAIM_LEDGER.yaml`, `PARENT_ACTION_GATE.md`,
or `OPEN_BLOCKERS.md` edits proposed** — this round produced no PROMOTE/
REJECT/NULL verdict and touched no headline claim's evidentiary status.

## Evidence tier

**Tier: `[VERIFIED]` for the citation** (WebSearch, this session, multiple
converging independent sources) **and for the novelty-check finding**
(direct `grep`/`Read` of `round59`/`round64`/`round65`/`round70`/`round71`
decision.md headers this session, not from memory). **`[CITED]`** for the
detailed content of round64/70/71's specific ILL-POSED reasoning (headers
and verdict lines read directly; full derivations not re-read line-by-line
in this design-only round — a future execution round MUST read them in full
before attempting `CP^3`/`S^3xS^3`, per Section 3(c) above). No physics
claim is asserted by this round; nothing here is `[SPECULATIVE]` beyond the
explicitly-labeled forward-looking execution spec in Section 4, which is a
proposal, not a finding.
