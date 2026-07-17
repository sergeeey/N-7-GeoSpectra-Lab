# E20 (round88) Claim — Strominger-Hull / WZW flux-selection search

**Date:** 2026-07-17
**FL tier:** [x] Full
**Question type:** [x] descriptive (literature-classification round; no new numerical
script) — both sub-questions below ask "does an existing, cited construction do X,"
not "what value does X take," so this is descriptive against the external
literature, exactly as round86 (E18) and round87 (E19) were classified.

---

## Prior Result Gate (MANDATORY)

1. **Exact claim:** does the Strominger-Hull / heterotic-with-torsion literature
   (or, if that literature turns out structurally not to apply, the WZW-model
   literature for `SU(2)=S³` directly) contain (A) a mechanism selecting ONE
   sign of torsion/flux over the other, or (B) a construction requiring BOTH
   signs to be physically present simultaneously?
2. `decision.md` grep (E18, E19, E11 formula + synonyms `Strominger`, `Hull`,
   `WZW`, `Bismut`, `contorsion`): [x] done — E18 (round86) names this exact
   literature as the most concrete Relaxation Map item; E19 (round87) already
   searched the Gates-Hull-Roček/bi-Hermitian corner of it and found FAIL
   (even-dimensionality); E11 (round75) already cited `∇^±=∇^{LC}±(1/2)H`
   generically, unsourced. 0 unreviewed hits — all three are the explicit
   starting point for this round, cited throughout.
3. `round*_claim.md` + scripts grep: [x] done, 0 hits for a round already
   asking sub-question A (sign-selection, H1c) or sub-question B restated for
   the WZW-specific (non-bi-Hermitian) literature — reviewed at E11/E18/E19
   above; none of them ran the WZW-level-quantization or worldsheet-parity
   argument this round develops.
4. `null_results/` + `parked/` grep: [x] done, 0 hits (this project keeps
   `null_results`/`parked` at the repo root, not per-subproject; this
   sub-project's own rejected/archived branches are tracked inline in each
   round's own decision.md instead — consistent with how E18/E19 handled this
   same check).
5. `git log -S`/`-G` pickaxe: not run — this is a literature round with no
   code changed by prior rounds to pickaxe against; the relevant prior state
   is fully captured by items 2-4 above (direct `Read` of E11/E18/E19).
6. **Primary source re-read (not from memory):** done this round for every
   external source cited — see `decision.md` §0 for the full list of
   downloaded/extracted PDFs and exact grep/read commands. Strominger 1986
   itself was NOT read as a full primary text this round (see `decision.md`
   §1's honest scope note on why — ScienceDirect returns HTTP 403 for the
   original 1986 Nuclear Physics B article, confirmed this round); its
   requirements are instead confirmed via two independent secondary sources
   that quote/cite it directly, each `[VERIFIED-tool]` via direct extraction.
7. **Status:** [x] NEW

---

## Estimand

**Population:** the Strominger-Hull heterotic-with-torsion system, and (after
the structural check below) the `SU(2)_k` Wess-Zumino-Witten model and its
associated `(1,1)`-supersymmetric non-linear sigma model with torsion, as
these are actually defined and used in their own primary/secondary literature
— NOT this project's own `preprint.tex` machinery, which is only compared
against the literature's stated requirements.
**Intervention:** none — this is a literature-classification exercise, not an
experiment run on this project's own code.
**Comparator:** round86 (E18)'s three pre-registered candidate constructions
(none satisfied by this project's own 3 cited geometry references) and
round87 (E19)'s Gates-Hull-Roček/bi-Hermitian instantiation of candidate 2
(FAIL, even-dimensionality obstruction).
**Endpoint:** for each of sub-questions A and B — does a genuine, citable,
primary-or-secondary-sourced construction exist that satisfies the PASS bar
below, when checked directly against `S³=SU(2)` (this project's actual
manifold)?
**Summary measure:** categorical verdict (PASS / FAIL / BLOCKED), assigned
SEPARATELY for A and B, per this project's own round86 3-category convention.
**MCID:** not applicable to a categorical literature-classification verdict.

---

## Claim

**Structural check (run FIRST, before either sub-question):** the classical
Strominger system (Strominger 1986, Hull 1986) requires the internal manifold
to be 6 REAL dimensions with an `SU(3)`-structure (a complex, non-Kähler
manifold with a nowhere-vanishing holomorphic `(3,0)`-form and holomorphically
trivial canonical bundle). `S³=SU(2)` is 3 real dimensions (odd) and admits no
almost complex structure at all (elementary linear algebra: `J²=-1` forces
even real dimension pointwise) — so the classical Strominger system, exactly
as classically formulated, cannot apply to `S³` directly, for the SAME class
of reason round87 (E19) already found for the Gates-Hull-Roček/bi-Hermitian
system. If this is confirmed [it is — see `decision.md` §1], the task
requires pivoting explicitly to the `SU(2)_k` WZW-model / `(1,1)`-SUSY
sigma-model-with-torsion literature, which is NOT subject to the same
dimension restriction, and re-asking sub-questions A and B there.

**Sub-question A (sign SELECTION, H1c-relevant):** in the (pivoted-to, per
the structural check) WZW/`(1,1)`-sigma-model-with-torsion literature, is
there a genuine physical mechanism (quantization, anomaly cancellation, an
equation of motion, a stability/BPS/unitarity condition) that selects ONE
specific sign of the torsion/flux/level over the other — i.e. a mechanism
that would answer WHY nature picks `t=0` over `t=1` (or vice versa), as
opposed to leaving it a free, relabelable choice of orientation convention?

**Sub-question B (sign COEXISTENCE, parent-action/round86-relevant):** in
the same (pivoted) literature, is there a construction requiring BOTH signs of
the torsion/flux to be PHYSICALLY PRESENT SIMULTANEOUSLY (not one merely
dynamically selected) — reusing round86 (E18)'s own PASS bar: an action, two
explicit connection fields, a stated symmetry, equations of motion, and a
non-ad-hoc necessity argument for why both signs must coexist, verified
directly against `S³=SU(2)` (not merely against the literature's own
preferred worked examples)?

Supporting sub-claims:
1. Strominger's own literature states its dimension/structure requirement
   explicitly and this requirement is checkably violated by `S³` (structural
   check).
2. The WZW-level quantization condition (`k∈ℤ`, and `k>0` required for
   unitarity) is a real, checkable, tool-citable fact — but whether it
   constitutes a genuine physical sign-SELECTION mechanism (sub-question A),
   as opposed to a convention-relative restatement of "pick an orientation,"
   requires checking the map `k→-k` under target/worldsheet orientation
   reversal, not simply citing `k>0`.
3. The base `(1,1)`-SUSY non-linear sigma model with torsion (NOT the
   `(2,2)`/Gates-Hull-Roček extension round87 already checked) has BOTH
   torsion-sign connections `∇^±=∇^{LC}±(1/2)H` appearing SIMULTANEOUSLY in
   ONE action, for a reason that does NOT require even dimension or a
   complex structure — this is a genuinely different (weaker-premise, more
   general) candidate for sub-question B than round87 checked, and must be
   verified on its own terms, including whether its OWN "why both" reasoning
   transfers to this project's Kaluza-Klein-compactification setting (the
   same transfer-check round87 §3 already ran for the GHR case).

---

## Kill criterion (MANDATORY — fill BEFORE running)

| Kill condition | Threshold |
|---|---|
| Sub-question A: no source states a `k`-sign-selection condition, OR the condition found is shown to be orientation-relative (equivalent to `+k` on `M` = `-k` on `-M`, not an absolute physical fact) | → sub-question A is FAIL, not PASS, even if a `k>0` rule is cited |
| Sub-question B: no source has an action with an explicit necessity argument for BOTH signs present at once, OR the necessity argument found is specific to a structure (2D worldsheet chirality, complex-structure-pair) this project's framework does not have | → sub-question B is FAIL, not PASS, even if the connection-formula-level match is exact |
| Structural check: Strominger's own stated dimension requirement is NOT 6D/`SU(3)`-structure, or IS satisfiable by a 3D odd manifold | → the whole pivot-to-WZW premise is wrong; would need to restart against the ACTUAL Strominger requirement |

If sub-question A FAILS → kills: the hope that this literature supplies H1c's
missing "why `t=0` not `t=1`" answer via a WZW/CFT-level unitarity argument;
narrows H1c's remaining search space by ruling out this specific route.
If sub-question B FAILS → kills: the hope that this literature supplies
round86/E18's missing parent action via the (structurally closer, non-complex-
structure-requiring) base `(1,1)` WZW/sigma-model route, IN ADDITION to
round87's already-ruled-out `(2,2)`/GHR route — a stronger, more general
closure of this literature class than round87 alone achieved.
If either PASSES → survives: a genuinely new, literature-sourced mechanism
for H1c or the parent-action question, not previously available to this
project.

If no hypothesis is killed by FAIL → gate is not scientifically motivated.
(Not applicable here: both FAILs directly narrow H1c's and E18's respective
Relaxation Maps, exactly as round87's FAIL did for candidate 2.)

---

## Checks planned

- T1: WebSearch/WebFetch + `pdftotext -layout` extraction (same tool round87
  used) of Strominger 1986's stated dimension/structure requirement, via
  secondary sources that quote it directly (ScienceDirect blocks direct
  access to the primary 1986 text, confirmed this round).
- T2: WebSearch/WebFetch + extraction of the WZW level-quantization argument
  (unitarity, `k∈ℤ>0`) AND the orientation-reversal/parity argument
  (`g→g⁻¹`, `k→-k`) from independent primary/secondary sources, to determine
  whether sub-question A's condition is an absolute selection or a
  convention-relative one.
- T3 (adversarial/edge case): explicitly check whether the base `(1,1)`
  sigma-model-with-torsion literature's OWN stated reason for needing
  `∇^+` AND `∇^-` simultaneously is specific to 2D worldsheet chirality (a
  structure this project's framework does not have, per round87 §3's
  already-established finding that this project's `S³` is a spacetime KK
  factor, not a string worldsheet target) — do not accept a superficial
  formula match as sufficient, per round87's own precedent.
- T4: check E14/round80's own `ι:g→g⁻¹` orientation-reversing isometry
  (`det(J)=-1`, exactly 2 fixed points at `g=±1`) against the WZW-orientifold
  literature's own `g→g⁻¹` involution, to see whether this project's own
  prior finding already has a named counterpart/role in this literature.

---

## What this does NOT mean

1. Does NOT prove no Strominger-Hull/WZW-derived mechanism can EVER apply to
   this project's compactification in any form — only what is checked
   directly against the specific constructions found this round.
2. Does NOT reopen or re-verdict round86 (E18)'s overall `BLOCKED` finding
   for the parent-action question as a whole, nor round87 (E19)'s `FAIL` for
   the Gates-Hull-Roček instantiation specifically — both stand independent
   of this round's outcome, exactly as round87 left round86 untouched.
3. Does NOT affect this project's `N_gen=3` headline claim (G73/G74A/G74B
   S6-only chain) — this round concerns only the S3-side torsion-escape-route
   program, exactly as round86/87 already state.
4. Does NOT attempt to construct a NEW 13D parent action — per round86/87's
   own scoping, that remains a substantially larger, unattempted undertaking.

---

## Fence (do not change without postmortem)

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False
- No file outside this experiment folder is modified by this round.
- No contact with Tom Lawrence; nothing submitted to arXiv.

---

## Verdict

[See `decision.md` — filled after research: two SEPARATE verdicts, one for
sub-question A, one for sub-question B.]
