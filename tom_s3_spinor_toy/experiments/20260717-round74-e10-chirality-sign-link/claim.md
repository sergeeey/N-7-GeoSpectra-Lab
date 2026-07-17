# E10 — Claim: does an existing project convention link S³'s torsion sign (t=0 vs t=1) to S⁶'s already-fixed chirality?

**Date:** 2026-07-17
**FL tier:** [x] Full (research claim; methodology per project CLAUDE.md)
**Question type:** [x] descriptive [ ] predictive [ ] causal

Descriptive (literature/text-search + representation-theoretic reasoning, no new
numerical computation): does this project's *own already-established* framework
(`preprint.tex`, `reports/PROJECT_360_ROUND3_SYNTHESIS.md`) contain any existing
convention, consistency requirement, or orientation-dependent quantity that
already links, or would need to be made consistent with, the still-open H1c
choice between the two Cartan–Schouten flat connections on S³ (t=0 vs t=1,
opposite-sign torsion $T^0=-[X,Y]$ vs $T^1=+[X,Y]$, frozen open in
`experiments/20260717-round72-e7-t-selection-principle/decision.md` and
`experiments/20260717-round73-e9-explicit-parallel-spinor/decision.md`) —
analogous to how this project's headline mechanism already pins SM chirality to
a single discrete choice, the orientation of S⁶ (`sign(ind)=sign(c_3)=+1`,
preprint.tex:120, :884-908)?

## Stakes

Internal-only (scoping/exploration note on the still-open H1c question; explicitly
NOT promoted to `preprint.tex`, NOT a resolution of H1c, NOT a new claim about
the physical world). This experiment produces at most a **candidate future gate**
(a new, not-yet-tested sub-question), not a result.

## Background (established, not re-derived here — read-only citations)

- **S⁶ chirality mechanism (already accepted, single discrete input):**
  `sign(ind(D_{S^6}\otimes S^-)) = sign(c_3(S^-)) = +1` for the standard
  orientation of $S^6$ (preprint.tex:120-124, :884-912). Lemma L5
  (preprint.tex:884-892) states this fixes SM chirality "up to a single $\ZZ_2$
  choice; no additional discrete inputs are required," and explicitly (line
  906-908) requires *"matching the $S^6$ orientation convention to the SM
  convention for $\mathrm{SU}(2)_L$"* — i.e. the paper already performs one
  explicit orientation$\leftrightarrow$chirality matching step, for $S^6$ only.
- **Full-operator decoupling (already established, load-bearing):**
  preprint.tex:1421-1465 ("Full-operator zero-mode gap") proves
  $D_{\mathrm{full}}^2 = D_{S^3}^2\otimes\mathbf 1 + \mathbf 1\otimes D_{S^6,S^-}^2$
  for the product ansatz, and preprint.tex:1479-1482 states this decoupling
  "survive[s]... for *any* operator on the $S^3$ factor, not only the torsion
  family, since the cross-term cancellation depends only on the $S^6$ factor's
  own chirality operator."
- **S³ torsion-deformed connection family (this session, rounds 72-73):**
  Agricola's $\nabla^t$ family on $S^3=\mathrm{SU}(2)/\{e\}$ has exactly two flat
  (Cartan–Schouten) connections at $t=0,1$ (E7, `results_e7.json`), with opposite
  torsion sign, and E9 explicitly constructed a $\nabla^0$-parallel spinor (clean
  PASS) while the *same* left-invariant ansatz fails at $t=1$ — the naive
  left-invariant frame is only $\nabla^0$-parallel, and E9's decision.md
  ([INFERRED, NOT verified there]) attributes this to the classical
  left-/right-invariant duality of the two Cartan–Schouten connections:
  $t=0$ parallelized by **left**-invariant vector fields, $t=1$ by
  **right**-invariant vector fields.
- **S³ gauge-sector identification (already established elsewhere in this
  project, independent of E7/E9):** preprint.tex:273-279 (`\S`\,sec:gauge-S3)
  identifies $\mathrm{Iso}(S^3)=\mathrm{SO}(4)\cong\mathrm{SU}(2)_L\times
  \mathrm{SU}(2)_R$ directly with the electroweak-plus-right gauge factors, with
  $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ acting as the standard left/right
  translation action of $\mathrm{SU}(2)$ on itself. The paper does **not**, at
  this citation or anywhere else found by this experiment, state which
  translation direction (left multiplication vs. right multiplication) is
  identified with the physical "$\mathrm{SU}(2)_L$" label.
- **Preprint's own flagged gap (unprompted, pre-existing, not introduced by this
  experiment):** preprint.tex:1493-1495 already states the S³ torsion crossing
  values are "convention-dependent (torsion normalization, **orientation**,
  choice of Levi-Civita reference point) and must always be quoted together with
  the full frozen convention" — i.e. the project's own text names "orientation"
  as an open convention-dependency for exactly this torsion family, without
  specifying what that S³ orientation convention is.

## The three sub-questions (frozen before searching further)

**Q1 (product-orientability link):** Does this project's construction impose,
anywhere, an orientability/spin-structure constraint on the full 9D product
$S^3\times S^6$ that ties an orientation choice on $S^3$ to the one already
fixed on $S^6$?

**Q2 (chirality-matching link):** Does the sign of $t$ (equivalently, the sign
of $S^3$'s torsion) enter the chirality grading of whatever zero mode of
$D_{\mathrm{full}}$ might eventually be found — in a way that could, in
principle, be required to match the already-fixed left-handed excess from the
$S^6$ factor?

**Q3 (existing S³ orientation convention):** Does this project's existing
spin-structure/orientation conventions fix the $S^3$ factor's own orientation or
chirality convention *anywhere else* in the paper, which the $\nabla^t$ family
should be consistent with?

## What would constitute PASS vs FAIL/OPEN

**PASS** (for any sub-question): a **real, already-implicit** consistency
requirement is found — i.e. a textual or structural fact *already present* in
`preprint.tex` / `reports/` (not newly invented in this experiment) that
constrains the t=0-vs-t=1 choice via a mechanism the project already commits to
elsewhere, without requiring new physical input beyond what is already in the
paper.

**FAIL/OPEN** (the honest default, per this project's own methodology — do not
force a positive result): no such already-implicit link exists; any connection
identified is a **new candidate synthesis** proposed by combining previously
unconnected established facts, which would itself require independent
verification (new representation-theory computation) before being anything more
than [SPECULATIVE]. A FAIL/OPEN verdict is a legitimate, valuable outcome per
this project's own falsification-ladder discipline (`~/.claude/rules/
falsification-ladder.md`, `research-methodology.md` — NULL = progress) and must
not be dressed up as a resolution of H1c.

## Kill criterion (filled before searching)

| Condition | Threshold |
|---|---|
| No orientability/spin-structure statement about the full 9D product's dependence on S³'s orientation is found anywhere in `preprint.tex` or `reports/` | Q1 → OPEN, not PASS |
| The established decoupling identity (`D_full^2` splits, cross-term cancellation depends only on $S^6$'s chirality operator, preprint.tex:1480-1482) shows $t$ does **not** enter the chirality grading of $D_{\mathrm{full}}$'s kernel at all | Q2's *direct* mechanism → FAIL/OPEN (no matching-chirality gate through the established Clifford-product structure); any *indirect* link found must be reported as a new, unverified candidate, not an existing one |
| No sentence in `preprint.tex` fixes which translation direction (left vs. right multiplication on $S^3=\mathrm{SU}(2)$) is the physical $\mathrm{SU}(2)_L$ | Q3 → OPEN (existing gauge-sector text under-specifies this, does not answer the question) |

## Method

1. Read `preprint.tex` for every occurrence of "orientation", "sign(ind)",
   "$c_3$", "chirality", and the full text of the "Full-operator zero-mode gap"
   and "$S^3$ torsion deformation" items (\S\,sec:open items).
2. Read `experiments/20260717-round72-e7-t-selection-principle/decision.md` and
   `experiments/20260717-round73-e9-explicit-parallel-spinor/decision.md`
   (read-only, this session's own prior results) for the frozen H1c status and
   the left-/right-invariant-frame duality claim.
3. Read `reports/PROJECT_360_ROUND3_SYNTHESIS.md` around "KT-8" for any
   additional orientation/chirality discussion not in `preprint.tex`.
4. Cross-reference the S³ gauge-sector identification
   (\S\,sec:gauge-S3, preprint.tex:273-279) against the left-/right-invariant
   duality to check whether a *representation-theoretic* (not merely
   nominal/naming) link between t=0/t=1 and SU(2)_L/SU(2)_R can be constructed
   from facts already on record — and, if so, explicitly flag it as a **new
   synthesis**, not a pre-existing project convention, with the specific
   additional unverified assumption required to promote it further.
5. Report the verdict on Q1, Q2, Q3 honestly and separately; do not average them
   into a single false "PASS."

## What this does NOT mean

1. Does **not** resolve H1c (which of t=0, t=1 is physically realized) — that
   remains exactly as open as `experiments/20260717-round72-.../decision.md` and
   `experiments/20260717-round73-.../decision.md` left it.
2. Does **not** establish that the S³ torsion-deformed mechanism is required, or
   correct, or promotable to `preprint.tex` — the E2/E3 scope gaps remain
   unaffected.
3. If a suggestive synthesis is reported (combining the SU(2)_L/R gauge
   identification with the left-/right-invariant-frame duality), it does
   **not** constitute a verified representation-theoretic result — no new
   computation checking how the constructed $\nabla^t$-parallel spinor
   transforms under $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ was performed in
   this experiment; this would be a well-defined but separate follow-up.
4. Does **not** claim the project's silence on "which translation is
   $\mathrm{SU}(2)_L$" is a defect in the paper — Pati-Salam-type constructions
   are often deliberately left/right-symmetric at the gauge-group level, with
   handedness fixed by a separate mechanism (here, the S⁶ index sign) — this
   experiment only notes that this particular convention is not available as an
   *additional* independent handle on t=0-vs-t=1.

## Assumptions (status)

| Assumption | Status |
|---|---|
| preprint.tex line numbers and quoted text as of this session's read | [VERIFIED-tool] — read directly, this session |
| E7/E9 decision.md verdicts on H1c, left-/right-invariant duality | [VERIFIED-tool, inherited] — read-only, this session; E9 itself marks the left/right-invariant duality claim [INFERRED, NOT verified there] |
| Left-invariant vector fields on a Lie group are invariant (trivial) under left translation and transform under right translation via the adjoint action (standard Lie theory fact) | [DOCS] — standard differential-geometry fact, not re-derived symbolically in this experiment |
| Whether the *spinor* (not just the vector frame) inherits the same left/right-translation triviality pattern | **[UNVERIFIED — flagged explicitly, not assumed true for the verdict]** |

## Check

No script. This is a pure literature/cross-reference exploration (as explicitly
allowed by the task): "if this ends up being a pure literature/text-search
exploration with no computation needed, that's fine, just document it thoroughly
in decision.md." Verdict recorded in `decision.md` with file:line citations for
every claim.
