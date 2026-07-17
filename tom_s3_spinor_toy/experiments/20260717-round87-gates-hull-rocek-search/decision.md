# E19 (round87) — Decision

**Date:** 2026-07-17
**Verdict:** `FAIL__EVEN_DIMENSIONALITY_OBSTRUCTION_PLUS_WORLDSHEET_CHIRALITY_MISMATCH__CANDIDATE_2_INSTANTIATION_ONLY`
**Go/no-go:** The Gates-Hull-Roček (1984) twisted-multiplet / bi-Hermitian /
N=(2,2)-WZW-model construction is real, well-established, external physics
— and it IS, formally, exactly the shape E18's candidate 2 asked for (an
action, two connection fields, a stated symmetry, equations of motion, and a
non-ad-hoc necessity argument for both signs). But on direct inspection of
its own primary and secondary sources, it **cannot be instantiated on
`S³=SU(2)` alone** — the literature's own stated existence condition
(the target group manifold must be even-dimensional) is violated by `S³`
(dimension 3, odd) for an elementary, checkable reason, independent of this
project's specific compactification. This is a genuine **FAIL**, not a
`BLOCKED` — a structural obstruction was found and verified, not merely an
absence of evidence. This is a narrower, this-candidate-only verdict; it does
**not** by itself reopen or overturn E18's overall `BLOCKED` finding for the
parent-action question as a whole (see "Scope" in `claim.md`).

---

## 1. What was found, verified against primary/secondary sources

### 1a. The Gates-Hull-Roček (1984) paper itself

**Bibliographic record** (cross-confirmed across three independent sources
this round — a WebSearch summary of the paper directly, its ResearchGate
listing, and its citation as reference [4] in a 2011 arXiv paper that
reproduces its exact title):
S. J. Gates, C. M. Hull, M. Roček, "Twisted Multiplets And New
Supersymmetric Nonlinear Sigma Models," *Nucl. Phys.* B248 (1984) 157–186.
[VERIFIED-tool: WebSearch, 2 independent listings converging on identical
journal/volume/page/year] No arXiv ID exists for this paper (it predates
arXiv, which began in 1991); no DOI could be independently confirmed this
round (an `inspirehep.net` fetch attempt returned no bibliographic content —
flagged honestly as not verified, not fabricated).

**Content** [VERIFIED-tool: WebSearch summary, cross-checked against the
2011 paper's own restatement — see 1b]: the paper introduces the "twisted
chiral multiplet," a new D=2 supersymmetric representation, to formulate
non-linear sigma models with `N=2,4` extended worldsheet supersymmetry on
target spaces with torsion (going beyond the Kähler-only sigma models of
Alvarez-Gaumé–Freedman). The key finding: `N=(1,1)` sigma models promoted to
`N=(2,2)` supersymmetry require **two** (generally non-commuting) complex
structures on the target space, each compatible with its own torsionful
connection — this pair is what the field now calls bi-Hermitian or
"Gates-Hull-Roček" geometry, later subsumed into Hitchin/Gualtieri's
generalized complex geometry.

### 1b. Modern accessible secondary source, read directly (not from memory)

**Source:** A. Sevrin, W. Staessens, D. Terryn, "The generalized Kähler
geometry of N=(2,2) WZW-models," arXiv:1111.0551 (JHEP). [VERIFIED-tool:
fetched via `WebFetch`, PDF saved locally, extracted with `pdftotext -layout`
(same tool this project's E18 used for its own PDF literature check),
2877 lines of text directly grepped and read this round.] This paper cites
Gates-Hull-Roček 1984 as reference [4] and Spindel-Sevrin-Troost-Van Proeyen
1988 as reference [16] — both primary sources for the construction — and
gives the precise formulas.

**Exact bi-Hermitian definition** (§2.1, p.2 of the extracted text,
`out1.txt:120-145`, quoted near-verbatim, symbols cleaned of PDF-extraction
artifacts):

> "An N=(2,2) non-linear σ-model requires a bihermitian geometry
> `{M, g, H, J+, J-}` defined by: an even dimensional (target) manifold `M`
> endowed with a metric `g` and a closed 3-form `H`... Two (integrable)
> complex structures `J+` and `J-` which are such that the metric is
> hermitian with respect to both of them... The complex structures are
> covariantly constant though with different connections `∇^±` (known as the
> Bismut connections), `∇^± = {}^{LC} ± (1/2)H`, where `{}^{LC}` is the
> standard Levi-Civita connection."

This is `∇^± = ∇^{LC} ± (1/2)H` — the exact formula this project's own E11
already cited generically, unsourced, as "standard in the connections-with-
skew-torsion literature" (`experiments/20260717-round75-e11-freund-rubin-
torsion-link/decision.md:122-124`). **This experiment supplies the missing
citation E11 flagged as absent**: this formula traces directly to the
Bismut connection construction underlying Gates-Hull-Roček 1984, as restated
in eq. (2.4) of Sevrin-Staessens-Terryn 2011.

**`H` is built from the SAME generator this project's `[X,Y]` bracket uses**
[VERIFIED-tool, `out1.txt:2769-2773`, Appendix A, eq. A.10-A.12]:
`H = (k/24x)·Tr[(g⁻¹dg)³] = (k/48x)·R^a_D R^b_E R^c_F f_{DEF} dx^a∧dx^b∧dx^c`
— `H` is proportional to the totally antisymmetric structure constants
`f_{DEF}` of the Lie algebra, contracted with the right-invariant vielbein
`R`. This is, up to normalization by the WZW level `k`, the Cartan 3-form
built from `[X,Y]` — structurally the SAME 1-dimensional generator this
project's E11 already established the Freund-Rubin flux and `T^t` both live
in (`experiments/20260717-round75-.../decision.md:96-109`, Q1). **This is a
genuine structural match on the connection-formula level**, not a
superficial one: `∇^±=∇^{LC}±(1/2)H` with `H∝f_{DEF}` is the same
mathematical shape as this project's `∇^t_XY=∇^{LC}_XY+t[X,Y]_m`
(`CONVENTION_TABLE.md` row 4), with `∇^{LC}` at `t=1/2` (already established,
`CONVENTION_TABLE.md` row 5) and `∇^±` corresponding to a symmetric `±s`
deviation from `t=1/2` for some normalization constant `s(k)` fixed by the
WZW level and the metric normalization — **the precise numeric value of `s`
(whether it lands exactly at `t=0,1` or some other symmetric pair) was NOT
computed this round; this is flagged honestly as an open normalization
question, not assumed to land at `t=0,1`.**

**Existence condition — the crux finding** [VERIFIED-tool, `out1.txt:854`,
§3, direct quote]:

> "In [16] it was shown that the model has an N=(2,2) supersymmetry provided
> `G` is an even-dimensional reductive Lie group."

`[16]` is Spindel-Sevrin-Troost-Van Proeyen, "Complex structures on
parallelized group manifolds and supersymmetric sigma models," Phys. Lett.
B206 (1988) 71, and "Extended Supersymmetric Sigma Models on Group
Manifolds. 1. The Complex Structures," Nucl. Phys. B308 (1988) 662
[VERIFIED-tool, `out1.txt:2790-2792`, reference list entry [16], read
directly].

This condition is independently reinforced by an even more general statement
in the SAME paper's discussion of the generalized-complex-geometry version
of the same structure [VERIFIED-tool, `out1.txt:282`, §2.2, direct quote]:

> "A necessary requirement for a HGCS [H-twisted generalized complex
> structure] to exist is that the manifold `M` is even dimensional."

**This "even-dimensional" requirement is not an arbitrary restriction of
this specific paper — it is forced by elementary linear algebra** [DERIVED,
not requiring external citation]: an almost complex structure `J` is a
bundle map `J:TM→TM` with `J²=-1`. At each point, `J` acting on the
tangent space `T_pM` (a real vector space) must have `J²=-Id`, which forces
the eigenvalues of `J` (as a complexified operator) to be `±i` in
conjugate pairs — this is only possible if `dim_ℝ(T_pM)` is even. An
odd-dimensional real manifold cannot carry **any** almost complex structure,
full stop, regardless of which specific construction is attempted. Combined
with the paper's own stated theorem (a group-manifold-specific refinement of
this general fact), this is airtight.

**Confirmed examples in this literature are all even-dimensional, and never
`S³=SU(2)` alone** [VERIFIED-tool, `out1.txt` throughout, §§4–5 headers +
discussion §6]: the paper's two worked examples are `SU(2)×U(1)` (the "Hopf
surface `S³×S¹`," 4-real-dimensional) and `SU(2)×SU(2)` (6-real-dimensional).
The paper's own discussion section states explicitly (`out1.txt:2555-2556`):
"even-dimensional reductive group manifolds provide a very explicit and
manageable class of models" and separately (`out1.txt:2560-2568`) gives the
full classification of hypercomplex (`N=(4,4)`) group manifolds — an
exhaustive list (`U(1)^4`, `SU(2)×U(1)`, `SU(2n+1)`, `SU(2n)×U(1)`,
`SO(4n)×U(1)^{2n}`, etc.) in which `SU(2)` never appears as a standalone
factor; every entry is even-dimensional by construction (e.g. `SU(2n+1)` at
`n=1` gives `SU(3)`, 6-real-dimensional, not `SU(2)`, which would require
`n=1/2`).

### 1c. `S³` (dimension 3) directly checked against this requirement

`S³ = SU(2)` has real dimension 3 (odd). This project's `preprint.tex`
(`:274`, reused from E18 §1) and every prior experiment in this project's
own chain (E2 onward) treat `S³` as the sole compactification factor of
interest for this torsion-connection family — never as a factor of a larger
product manifold for the purposes of the `∇^t` construction. **`S³` alone,
taken as the target manifold `M` of a hypothetical bi-Hermitian/WZW
construction, fails the even-dimensionality requirement outright** — this is
not a gap in what has been tried; it is a structural impossibility, checked
directly against the primary literature's own stated existence condition.

---

## 2. Applying the pre-registered criteria (`claim.md`)

| PASS sub-requirement | Satisfied by GHR/WZW literature IN GENERAL? | Satisfied when specifically applied to THIS project's `S³=SU(2)`? |
|---|---|---|
| Action exists | YES — WZW action, `out1.txt:830-834`, eq. 3.1 | N/A — construction does not exist on `S³` alone (§1b, §1c) |
| Explicit fields (`J±`, `∇^±`) | YES — eq. 2.4, eq. 3.5-3.7 | N/A |
| Stated symmetry | YES — `N=(2,2)` worldsheet SUSY | N/A |
| Equations of motion | YES — eq. 3.2 | N/A |
| Explanation for WHY both signs present | YES, in the 2D-worldsheet setting (§3 below) | **NO — the "why" is worldsheet-chirality-specific and does not transfer (§3)** |
| No manual/ad hoc duplication | YES, within its own 2D-worldsheet domain | **Importing it here WOULD be the ad hoc move the PASS bar excludes (§3)** |
| Same object as this project's `∇^t`? | Structurally YES on the connection-formula level (§1b) | Exact normalization NOT established; existence itself already fails independently (§1c) |

**Verdict for this candidate: FAIL.** The dimension-parity obstruction alone
(§1c) is dispositive and sufficient by itself: `S³` cannot carry the
required pair `(J+,J-)` at all, for a reason stated in the construction's
own founding literature and independently derivable from elementary linear
algebra. Section 3 below gives a SECOND, independent reason the construction
would not transfer even if the dimension obstruction were somehow evaded
(e.g. by embedding `S³` in a larger even-dimensional auxiliary space) —
included because the task specifically asked whether the "why both are
present" mechanism is honestly transferable, not merely whether a
dimension-count technicality can be checked off.

---

## 3. Second, independent reason: worldsheet chirality vs. Kaluza-Klein spacetime chirality

Even setting aside §1c (imagining `S³` were somehow embedded as a factor of
a larger even-dimensional target, so `J±` could formally exist on the
product), the GHR/WZW construction's own stated reason for requiring BOTH
`J+` and `J-` (equivalently both `∇^+` and `∇^-`) is specific to a **2D
string worldsheet** setting:

- [VERIFIED-tool, `out1.txt:80-82`, quoted above]: the two complex
  structures are needed "one for the left-handed and one for the
  right-handed extra supersymmetry transformations" — i.e. the SUSY
  transformations associated with the two independent **worldsheet**
  chiralities of a 2D `(1,1)`-supersymmetric non-linear sigma model (the
  worldsheet fermions `ψ_+^μ`, `ψ_-^μ` of a string propagating in the target
  space `M`), not spacetime chirality of a higher-dimensional fermion field.
- [VERIFIED-tool, `out1.txt:851-853`, eq. 3.5-3.6]: `J+` multiplies the
  `D_+gg^{-1}` term (associated with the SUSY parameter `ε_+`) and `J-`
  multiplies the `D_-gg^{-1}` term (`ε_-`) — confirming the pairing is with
  the two INDEPENDENT worldsheet supercovariant derivatives `D_±`, the
  standard `(1,1)`-superspace objects for the two 2D worldsheet chiral
  sectors. **Honest caveat, per the task's explicit instruction not to
  assume the convention:** whether `J+`'s associated sector is what a given
  author would separately label "left-moving" versus "right-moving" in
  spacetime terms is itself a convention (exactly the same style of
  unresolved labeling ambiguity this project's own
  `CONVENTION_TABLE.md` row 6 already flags for `SU(2)_L`/`SU(2)_R`) — not
  re-derived or resolved here, since it does not affect the structural
  conclusion below.
- Eq. 3.7 [VERIFIED-tool, `out1.txt:855-859`] confirms `J+^A_B` is built from
  the LEFT-invariant vielbein `L` and `J-^A_B` from the RIGHT-invariant
  vielbein `R` — i.e., structurally, `J+` ↔ left-invariant geometric data,
  `J-` ↔ right-invariant geometric data, in the SAME sense this project's
  own `t=0` ↔ left-invariant / `t=1` ↔ right-invariant correspondence is
  stated (`CONVENTION_TABLE.md` row 5). This is a genuine, checkable
  structural parallel — **but it is a parallel in the GEOMETRIC DATA used
  (left- vs. right-invariant frames), not a match of the PHYSICAL REASON the
  two are required to coexist.**

**The physical setting is fundamentally different.** The GHR/WZW
construction's "why both" answer is: a 2D string worldsheet genuinely has
two independent chiral sectors (left-movers and right-movers, `D_+` and
`D_-`), and closing `(2,2)` worldsheet supersymmetry requires a compatible
complex structure for EACH sector separately — this is a fact about 2D
conformal field theory, not about the target space in isolation. **This
project's own framework has no 2D string worldsheet anywhere.** `S³=SU(2)`
is used, throughout this project's own text (`preprint.tex`, all of
E2–E18), as the compact INTERNAL factor of a higher-dimensional (13D)
Kaluza-Klein compactification of SPACETIME fermions — the `∇^t` connection
family is a SPIN connection entering a single spacetime Dirac operator
`D_{S3,t}`, not a target-space connection for a 2D sigma model coupling to
worldsheet fermions. "Chirality" in this project means SPACETIME chirality
(the `γ⁵`-eigenvalue / `SU(2)_L` vs. `SU(2)_R` representation content of the
resulting 4D fermion after KK reduction, per `preprint.tex:884-908`, Lemma
L5) — a physically distinct notion from 2D WORLDSHEET chirality (left- vs.
right-movers on the string). Nothing in this project's own text
(`preprint.tex`, `activeContext.md`, or any of E1–E18's decision files)
introduces, needs, or references a 2D string worldsheet at any point.

**Consequence:** even granting the connection-formula-level structural match
found in §1b, importing the GHR/WZW "why both are present" argument to
explain why THIS project's Kaluza-Klein compactification needs `t=0` AND
`t=1` simultaneously would require asserting that this project's
compactification secretly has two independent worldsheet-chirality sectors
— a claim nothing in this project's framework makes, needs, or is compatible
with (there is no worldsheet). Manufacturing that assertion just to satisfy
candidate 2's PASS bar is exactly the "manual/ad hoc duplication" the PASS
bar's own clause excludes (see `claim.md`'s Kill criterion). This is a
second, independent reason for FAIL, on top of §1c's dimension-parity
obstruction.

---

## 4. Does this resolve, worsen, or leave unchanged E18's overall verdict?

**Unchanged.** E18's `BLOCKED` verdict concerned the parent-action question
as a whole, across three candidates. This experiment:
- Supplies a genuine, previously-missing citation for E11's own generic,
  unsourced `∇^±=∇^{LC}±(1/2)H` claim (§1b) — strengthening E11's own
  finding without changing its conclusion (E11 already found this mechanism
  "not currently wired into `preprint.tex` anywhere," a fact this experiment
  does not touch).
- Closes off, with a genuine structural reason (not absence-of-evidence),
  the SPECIFIC route of instantiating E18's candidate 2 via the
  Gates-Hull-Roček/bi-Hermitian/WZW literature. Candidate 2 was ALREADY
  found unsatisfied by E18 (via the `preprint.tex` Pati-Salam/left-right
  text) — this experiment adds a second, independent, and more decisive
  reason (a real no-go, not merely "not written down") for the SAME
  candidate, via the literature this project had not yet checked.
- Does NOT touch candidates 1 or 3, E12's Majorana/orbifold NULL, KT-8, H1c,
  or E17's representation-content PASS — all untouched, exactly as before.
- Does NOT reopen the Relaxation Map's OTHER two remaining items (a genuinely
  new 13D-parent-action derivation; the AHL 2023 cone-construction pearl,
  §Pearl-registry below for a related item found this round).

E18's overall `BLOCKED` verdict for the parent-action question stands.

---

## 5. Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result kills:** the hope that the Gates-Hull-Roček / bi-
  Hermitian / N=(2,2)-WZW-model literature — the single most natural,
  best-established external candidate for E18's candidate 2 — supplies a
  ready-made parent action for `t=0`/`t=1` coexistence on `S³`. It is killed
  for a STRUCTURAL reason (even-dimensionality is required; `S³` is
  3-dimensional) reinforced by a SECOND, independent reason (worldsheet
  chirality ≠ spacetime/KK chirality) — not merely because no one has tried
  it. This also narrows the general SEARCH CLASS for future candidates: ANY
  future candidate route based on almost-complex-structure / generalized-
  complex-geometry machinery (Hitchin/Gualtieri generalized Kähler geometry,
  generalized Calabi-Yau conditions, etc.) is subject to the SAME
  even-dimensionality obstruction and cannot apply to `S³` (3D, odd) or to
  the FULL internal space `S³×S⁶` (9D, odd) without first passing through
  an auxiliary even-dimensional construction not currently present anywhere
  in this project.
- **What this result does NOT kill:** the connection-FORMULA-level
  structural match found in §1b (`∇^±=∇^{LC}±(1/2)H` with `H` built from the
  same structure-constant generator this project's `[X,Y]` uses) is a real,
  citable fact, useful as a SOURCED reference for E11's own generic claim,
  even though it does not resolve the coexistence question. It also does
  NOT kill the possibility that a genuinely different (non-complex-
  structure-based) construction in the broader Strominger-Hull flux-
  compactification literature — one that does not require an almost complex
  structure at all, e.g. a purely metric/flux Killing-spinor-equation-based
  torsion construction, which is what E11's original citation was gesturing
  at before this round traced it specifically to the GHR/WZW family — could
  still supply candidate 3 (a sign-selecting dynamical field) without
  running into the even-dimensionality obstruction, since candidate 3 does
  not require a complex structure at all. **This is flagged as the most
  concrete remaining next step, narrower than E18's original Relaxation Map
  entry.**
- **What survives, confirmed stronger than before:** E11's own generic,
  previously-uncited `∇^±=∇^{LC}±(1/2)H` claim now has an actual citation
  trail (Gates-Hull-Roček 1984 → Sevrin-Staessens-Terryn 2011 eq. 2.4), and
  the reason this mechanism does not straightforwardly solve this project's
  question is now a checked structural fact (even-dimensionality +
  worldsheet-vs-spacetime chirality mismatch), not merely an unexamined gap.

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Search non-complex-structure-based torsion constructions in Strominger-Hull literature | Specifically exclude any construction requiring an almost complex structure (ruled out for `S³` by §1c/Kill-Analysis); look instead for a purely Killing-spinor-equation / flux-quantization-based sign-selection mechanism for candidate 3 |
| Embed `S³` in an even-dimensional auxiliary space | Would require a NEW, independently-motivated reason for this project's physics to actually live on `S³×(\text{something 1-dimensional})` or similar — not attempted, not currently motivated by anything in `preprint.tex` |
| Pin down the exact `s(k)` normalization from §1b | Would require redoing Sevrin-Staessens-Terryn's `SU(2)×U(1)` computation (§4 of `out1.txt`, not read in full this round — flagged as not exhaustively read) with this project's own `c0=-2` convention substituted in, to see whether `∇^±` lands at exactly `t=0,1` or some other symmetric pair — a genuinely new calculation, not attempted here since §1c already makes the broader question moot for `S³` alone |
| Resolve candidate 3 directly (unaffected by this experiment) | Unchanged from E11/E18's own Relaxation Map: an explicit `q↔(2t-1)` normalization for a literal flux-sources-contorsion coupling, still not attempted anywhere in this project |

## Assumptions carried, unresolved

- `SU(2)_L`=left-translation vs its mirror (`CONVENTION_TABLE.md` row 6) —
  the GHR/WZW literature's own `J+`↔left-invariant/`J-`↔right-invariant
  convention (§3) does not resolve this project's own version of the same
  ambiguity; both are noted as parallel, unresolved conventions, not
  cross-used to resolve each other.
- `t=1`'s existence only under `c0=-2` (`CONVENTION_TABLE.md` row 5) —
  carried forward unchanged.
- Whether Sevrin-Staessens-Terryn 2011's §4 (`SU(2)×U(1)`, `out1.txt`
  lines ~960-2280, not read in full this round, only grepped for keywords
  plus §6 discussion read directly) contains an explicit numeric value for
  the `∇^±` normalization in a form directly comparable to this project's
  `t` — NOT checked this round; flagged as the cheapest concrete next step
  in the Relaxation Map above if this specific numeric comparison is ever
  wanted (though §1c already makes it moot for `S³` alone).
- Whether the broader bi-Hermitian/generalized-complex-geometry literature
  contains ANY construction avoiding the even-dimensionality requirement
  (e.g. via a weaker structure than an honest almost complex structure) —
  not searched this round; the even-dimensionality requirement was checked
  against the SPECIFIC (2,2)-SUSY / HGCS constructions actually found, not
  against every conceivable generalized-geometric structure in the field.

## What this does NOT mean

1. Does **not** prove no bi-Hermitian-flavored or complex-structure-adjacent
   construction can EVER apply to this project's compactification in any
   form — only that the specific, standard Gates-Hull-Roček/WZW instantiation
   of candidate 2, applied directly to `S³=SU(2)` alone, fails for the two
   stated reasons (§§1c, 3).
2. Does **not** reopen or re-verdict E18's overall `BLOCKED` finding for the
   parent-action question (§4) — candidates 1 and 3, KT-8, and H1c remain
   exactly as E18 left them.
3. Does **not** affect this project's `N_gen=3` headline claim, which rests
   on the independently established G73/G74A/G74B S6-only chain
   (`activeContext.md`, `reports/PROJECT_360_ROUND3_SYNTHESIS.md`) — this
   experiment concerns only the S3-side torsion-escape-route program.
4. Does **not** claim the entire Sevrin-Staessens-Terryn 2011 paper, or the
   broader bi-Hermitian/generalized-complex-geometry literature, was read
   exhaustively — §§1-3 above and the "Assumptions carried" section state
   precisely which parts were read directly versus grepped/not checked.
5. Does **not** claim a confirmed DOI for the Gates-Hull-Roček 1984 paper —
   the journal/volume/page/year citation is cross-confirmed across
   independent sources, but a direct DOI lookup this round returned no
   usable content and is honestly reported as unconfirmed, not fabricated.
6. Does **not** re-derive or challenge any of E2/E3/E7/E9–E18's own
   tool-verified results — all reused here purely by citation.
7. Nothing in this experiment was submitted, posted, or sent anywhere
   external — this project's standing rule against arXiv submission and
   against contacting Tom Lawrence is unaffected and was not approached.

## Pearl-registry candidate

**Observation:** the even-dimensionality requirement for almost complex
structures (§1c) is a general, transferable fact that applies to EVERY
complex-structure-based or generalized-complex-geometry-based candidate
construction this project might consider in the future for `S³` (3D) or the
full internal space `S³×S⁶` (9D) — both odd-dimensional. **Falsifiable
prediction, if pursued:** any future round proposing a generalized-complex-
geometry, Hitchin-pair, or bi-Hermitian-flavored mechanism for this
project's torsion-connection coexistence question will fail the identical
even-dimensionality check unless it first identifies a genuine auxiliary
even-dimensional structure this project does not currently have. **Impact
score ~4** (narrows an entire CLASS of future candidate searches for this
project's own torsion-escape-route line of work; the even-dimensionality
fact itself is elementary and well-known in the general field, so the pearl
here is specifically "this project's manifolds are odd-dimensional, so this
whole class of constructions is foreclosed," not a novel mathematical fact).
Not registered to the global `pearl_registry/INDEX.md` — project-internal.
`next_check`: before attempting any future complex-structure-based or
generalized-Kähler-based parent-action candidate for this project's S³ or
S³×S⁶ torsion/twist questions, check manifold dimension parity FIRST.

## Check (reproduces this decision)

This is a literature-search-and-structural-comparison round; there is no new
numerical script. The "check" is: (1) `WebSearch` was run for the Gates-
Hull-Roček 1984 paper and cross-confirmed bibliographically across 2+
independent listings; (2) `WebFetch` retrieved arXiv:1111.0551 (Sevrin-
Staessens-Terryn 2011), which downloaded as a PDF, extracted this round via
`pdftotext -layout` into a 2877-line text file, `grep`-searched for
`even-dimensional`, `left-handed`, `right-handed`, `torsion`, `WZW-model`,
and directly read at the specific line ranges cited above (§§1b, 3, and the
reference list, `out1.txt` lines 1-300, 824-960, 2540-2877); (3) every
exact quote above reproduces text found at the cited line number in that
extraction, not from memory or from the initial WebFetch/WebSearch summaries
alone; (4) the even-dimensionality linear-algebra argument (§1b) is stated
as [DERIVED], not [VERIFIED-tool], since it is elementary and was not looked
up in a separate source this round; (5) every internal project citation
(`CONVENTION_TABLE.md` rows 2,4,5,6; E11 `decision.md`; E18 `decision.md`;
`preprint.tex` line references) was reused by direct `Read` of the cited
file this round or carried from E18's own already-verified reads, not from
memory.
