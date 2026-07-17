# E21 (round90) — Decision

> **⚠️ CORRECTION (2026-07-17, added retroactively after user review — original
> text below unchanged):** the specific claim in Section 3a/4 below that
> **Witten's `SU(2)` global anomaly** requires "an even number of gauged
> `SU(2)` doublets" and thereby forces both `F_L~(4,2,1)` and `F_R^c~(4̄,1,2)`
> to coexist is **REFUTED**. Verified directly (elementary group theory,
> independently checked): each Pati-Salam multiplet ALONE already contains
> **4** `SU(2)`-doublets (the `4` of `SU(4)` supplies the multiplicity), which
> is even — so `F_L` alone (or `F_R^c` alone) is already Witten-anomaly-free
> on its own; Witten's criterion does NOT single-handedly force the pair.
> **The correct, standard mechanism is the PERTURBATIVE (cubic) `SU(4)^3`
> gauge anomaly instead**: `F_L~(4,2,1)` contributes anomaly coefficient
> `A=+2` (`A(4)×\dim(2)×\dim(1)=1×2×1`), `F_R^c~(4̄,1,2)` contributes `A=-2`
> (`A(4̄)×\dim(1)×\dim(2)=(-1)×1×2`) — **only their SUM vanishes**, so a
> genuinely gauged, CHIRAL `SU(4)_{\mathrm{PS}}` (not merely `SU(2)_R`
> alone) requires both pieces for anomaly cancellation. This does NOT
> overturn the section's overall `BLOCKED` verdict — it sharpens it: the
> correct anomaly mechanism is tied even MORE directly to `SU(4)` gauging
> specifically (Section 5a's `SU(4)`-incompleteness, gate G97, is now the
> single dispositive gap, not one of three loosely-related concerns). All
> other findings in this file (Section 1: `SU(2)_R` genuinely gauged in
> `preprint.tex`, not a bookkeeping label) are UNAFFECTED by this
> correction. See `reports/PROJECT_360_ROUND3_SYNTHESIS.md` "Round90
> correction" for the full registration (R90-A through R90-E).

**Date:** 2026-07-17
**Verdict:** `BLOCKED__SU2R_GAUGING_IS_GENUINE_AND_STRONGER_THAN_PRIOR_ROUNDS_CREDITED__BUT_FULL_SU4xSU2LxSU2R_COMBINATION_IS_SELF-ADMITTED_INCOMPLETE`
**Go/no-go:** This experiment finds a genuine, previously under-credited
positive fact — `preprint.tex` commits to `SU(2)_R` as an actual GAUGED 4D
symmetry (a real gauge boson from the Kaluza-Klein spin-connection mechanism,
entering the spectral action's gauge kinetic term and the Higgs bidoublet
assignment), not merely a `T3R` bookkeeping label — and this is a
STRUCTURALLY DIFFERENT, stronger claim than the "assumed coupling equality for
one phenomenological formula" that round86/round87/E14/E17 examined and
correctly found insufficient. Combined with the external, well-established
Pati-Salam/left-right fermion-completeness requirement (grounded below), this
DOES supply a genuine, spacetime-native (not string-worldsheet-borrowed)
argument for why a complete theory needs both an `SU(2)_L`-doublet's and an
`SU(2)_R`-doublet's worth of matter. **But it does not reach PASS**, because
this project's own text explicitly admits (gate G97, cited independently in
round87 and reconfirmed here) that the full `SU(4)` unification this argument
is normally checked against is NOT geometrically realized in this framework —
only `SU(3)_c×SU(2)_L×SU(2)_R` is, with `U(1)_{B-L}` patched in from fermion
charges, not gauged. This is precisely the pre-registered second disjunct of
the BLOCKED criterion. The pre-existing Lemma-L5 asymmetric-chirality tension
(E17 Section 5) is also not resolved by this experiment. No stated parent
action (E18/KT-1's core gap) is supplied either way.

---

## 1. Is `SU(2)_R` genuinely gauged in `preprint.tex`, or only a label? [VERIFIED-tool: direct `Grep`+`Read`]

**Answer: genuinely gauged — a real 4D gauge symmetry, not merely a
bookkeeping label. This is stronger than how round86/E18 and E17 Section 5
characterized this project's `SU(2)_R` commitment (they examined a narrower,
later claim — see the crucial distinction in Section 3 below).**

Direct quotes, read this round at the cited lines:

- **Abstract, `preprint.tex:78-80`:** "By identifying the spin connection with
  gauge fields (following Lawrence...), we obtain the gauge group
  `SU(3)×SU(2)_L×SU(2)_R` geometrically." — this states, in the paper's own
  summary of its own result, that the spin connection is IDENTIFIED WITH gauge
  fields (not merely labeled by analogy), and that `SU(2)_R` is one of the
  resulting gauge factors.
- **`preprint.tex:187-198`:** extends Lawrence's own already-established
  Kaluza-Klein mechanism ("the spin connection of the compact factor acts as a
  gauge potential," demonstrated by Lawrence for `U(1)` in 6D and `SU(2)` in
  7D) to `S³×S⁶`: "the `S³` spin connection yields `SU(2)_L×SU(2)_R` from the
  bi-invariant metric on `S³`... while the `G_2` holonomy of `S⁶=G_2/SU(3)`
  provides `SU(3)_c` — together giving the Pati-Salam gauge algebra."
- **Section 2.1 "Gauge structure from `S³`," `preprint.tex:258-279`
  (the paper's own dedicated section constructing this claim, read in full
  this round):** "Lawrence... established that in product Kaluza-Klein
  manifolds, components of the Levi-Civita connection with mixed indices (4D
  spacetime $\leftrightarrow$ compact space) transform as gauge potentials of
  the orthogonal symmetry `O(s_2)` of the compact factor." Applied to this
  project: "The `S³` factor has isometry group `SO(4)≅SU(2)_L×SU(2)_R` from
  its bi-invariant round metric, **giving two independent `SU(2)` gauge
  factors**." This is the load-bearing sentence for this experiment: `SU(2)_L`
  AND `SU(2)_R` are BOTH asserted as independent gauge factors, via the SAME
  established KK mechanism this project already uses (and Lawrence 2022/2023
  already established in a peer-reviewed, cited context) for the `U(1)` and
  `SU(2)` cases — this is not a new or ad hoc claim invented for this project;
  it is a direct application of an already-published mechanism.
- **Gauge kinetic term, Section "Gauge coupling ratio prediction,"
  `preprint.tex:359-374` (read in full this round):** "The spectral action
  `Tr f(D²/Λ²)` on `S³×S⁶` produces gauge kinetic terms with coupling squared
  proportional to the inverse volume of the cycle threaded: `g_2² ∝
  1/Vol(S³)`..." — this is an actual, computed GAUGE KINETIC TERM (via the
  Chamseddine-Connes-Marcolli spectral-action formalism this paper explicitly
  builds on, `preprint.tex:1162-1201`), not a bare label; it produces a
  specific numerical coupling ratio `g_2²/g_3²=15/(16\pi)≈0.298`, compared
  against the measured SM value.
- **Higgs bidoublet, `preprint.tex:355-357`:** "The Higgs field appears as a
  bidoublet `(2,2)_0` under `SU(2)_L×SU(2)_R` from the `D_F` Yukawa
  intertwiner." — assigning a physical field's representation under
  `SU(2)_L×SU(2)_R` as a genuine gauge symmetry is standard GUT model-building
  practice and would be meaningless if `SU(2)_R` were merely a label with no
  associated gauge action.
- **Summary comparison table, `preprint.tex:1174`:** "SM gauge group...
  `SU(3)×SU(2)_L×SU(2)_R` from spin connection" — restated as the paper's own
  headline characterization of its result, in a table explicitly comparing
  against Chamseddine-Connes-Marcolli's derivation of the SAME gauge group
  from a different (algebraic, NCG-axiom) route. Comparing "from spin
  connection" against CCM's "Derived from `A_F`" as two alternative
  DERIVATIONS OF THE SAME GAUGE GROUP is only a meaningful comparison if both
  sides are claims about a genuine gauge symmetry, not a labeling scheme.

**Conclusion for Step 1: `SU(2)_R` is genuinely, repeatedly, and
foundationally committed as a gauged 4D symmetry in this project's own text —
independent of, and prior to, any later numerical coupling-value assumption.**

---

## 2. The crucial distinction this experiment adds: gauging commitment vs. the coupling-VALUE assumption [re-reading round86/E18 and E17 Section 5 against this finding]

Round86/E18 (`experiments/20260717-round86-parent-action-discriminator/
decision.md:292-298`) and E17 Section 5
(`experiments/20260717-round85-e17-sector-coexistence-gate/decision.md:299-330`)
both examined `preprint.tex:408-409`'s statement "With `g_{2R}=g_{2L}=g_2`
(left-right symmetry of `S³`)" and correctly found this specific sentence
insufficient to license coexistence: it is "a stated numerical EQUALITY
ASSUMPTION between two gauge coupling constants... used to derive a
phenomenological formula for `sin²θ_W`," explicitly flagged in the paper
itself (`preprint.tex:420-431`) as "illustrative pending... input, not as a
computation with a well-defined completion path" — genuinely a narrow,
unverified, model-building CHOICE, exactly as E14 Reading 3 and E17 Section 5
characterized it.

**But this is a DIFFERENT and narrower claim than "is `SU(2)_R` gauged at
all."** Section 1 above shows the gauging of `SU(2)_R` ITSELF — as an
independent 4D gauge symmetry with its own gauge boson, arising from the
`S³` isometry via the same KK mechanism used for `SU(2)_L` and `SU(3)_c` — is
asserted in Section 2.1 (`preprint.tex:258-279`) and reinforced by the
spectral-action gauge-kinetic-term computation (`preprint.tex:359-374`),
**entirely prior to, and independent of, the LATER, narrower `g_{2R}=g_{2L}`
VALUE assumption** used only in the Weinberg-angle estimate
(`preprint.tex:405-431`). Round86/E17's skepticism targeted the numerical
equality assumption specifically (which remains exactly as unverified as they
found it — this experiment does not rehabilitate it); it did not, on a close
re-reading, examine whether the more basic "`SU(2)_R` exists as a gauge
symmetry at all" claim is itself solid. Section 1 shows it is — this is a
genuinely new sub-finding this experiment adds, not a re-litigation of
round86/E17's own conclusion (which stands, on its own narrower question,
unchanged).

---

## 3. External grounding: what does standard Pati-Salam/left-right model-building actually require, and why? [VERIFIED-tool + WEAK, mixed — reported honestly by source]

### 3a. Bibliographic and content confirmation [VERIFIED-tool: `WebFetch`, cross-checked]

**Gauge group and representation content** [VERIFIED-tool, `WebFetch` of
`https://en.wikipedia.org/wiki/Pati%E2%80%93Salam_model`, direct quote
retrieved this round]: "The Pati–Salam model states that the gauge group is
either `SU(4) × SU(2)_L × SU(2)_R` or `(SU(4) × SU(2)_L × SU(2)_R)/Z_2`" and
"the fermions form three families, each consisting of the representations
`(4, 2, 1)` and `(4, 1, 2)`." This is a direct, tool-fetched quote from a
standard modern reference, not a WebSearch summary.

**Chirality assignment and the reason both are needed** [WEAK — WebSearch
summary of multiple converging modern sources (arXiv:1712.06844, arXiv
review material on `SU(4)×SU(2)_L×SU(2)_R` anomaly-freedom), NOT
independently re-extracted from a primary PDF this round, honestly flagged as
the weakest-sourced sub-claim in this section]: "left-handed states [are] in
the `(4,2,1)` representation and right-handed states in the `(4,1,2)`
representation... The specific pairing of the `(4,2,1)` representation
(containing left-handed quarks and leptons) with its conjugate `(4̄,1,2)`
representation (containing right-handed quarks and leptons) is essential for
satisfying all the anomaly cancellation conditions."

**A stronger, independently rigorous, well-known consistency fact
[VERIFIED-tool: bibliographic cross-check via `WebSearch`, converging across
Princeton University's own publication listing, `ui.adsabs.harvard.edu`, and
ScienceDirect]:** E. Witten, "An `SU(2)` anomaly," *Phys. Lett.* B117 (1982)
324-328. This paper proves, independently of Pati-Salam or any GUT-specific
context, that "an `SU(2)` gauge theory with an ODD number of left-handed
fermion doublets (and no other representations) is mathematically
inconsistent" — a nonperturbative, global anomaly (`π_4(SU(2))=Z_2`), distinct
from and in addition to the ordinary triangle anomaly. **This is the more
fundamental, more rigorously citable version of "why both are needed": IF
`SU(2)_R` is gauged and matter is charged under it, that matter must organize
into complete `SU(2)_R` representations (doublets), and moreover an EVEN
number of them — a hard, non-negotiable consistency requirement on any
genuinely gauged `SU(2)`, independent of whether the larger `SU(4)`
unification is also achieved.**

### 3b. Primary-source attempt, reported honestly [attempted, largely
unsuccessful — flagged, not hidden]

Attempted to fetch Pati-Salam's own primary text directly (matching this
project's own round87-90 `pdftotext` discipline) via
`https://inspirehep.net/files/3e03067e904f967d6c18f412650d8200` (a proceedings
reprint headed "LEPTON NUMBER AS THE FOURTH COLOUR," pages 111-85 through
111-87). `pdftotext -layout` extraction succeeded mechanically (271 lines) but
the OCR is heavily corrupted (short, fragmented lines, column-interleaving
artifacts from the two-column proceedings layout) — **only a handful of
phrases are reliably legible**, e.g. (line 79-80) "The basic scheme...
consists of two 16-folds of chiral fermionic multiplets," (line 88-92)
"transforming as `(4,1,4)` and `(4,1,4)`... under the fundamental symmetry
structure `G = SU(4)_L × SU(4)_R × SU(V)_{L+R}`," and (line 95) "Note the
left-right symmetric nature of this Lagrangian." **Honest caveat: this
specific retrieved document uses a LARGER, more general `SU(4)_L×SU(4)_R×
SU(4')` gauge structure (an earlier or alternative Pati-Salam formulation),
not the more commonly cited minimal `SU(4)_c×SU(2)_L×SU(2)_R` — this is
either a different paper in the "three recent notes" the text itself
references (line 62), or an early/generalized variant; it was NOT
independently confirmed this round which specific published version this
corresponds to.** This primary-source fragment is used ONLY as weak,
qualitative corroboration that the historical motivation is explicitly
"left-right symmetric" pairing of conjugate chiral multiplets — it is
**not** used as the source for the specific `(4,2,1)`/`(4̄,1,2)` notation,
which rests on the Wikipedia `[VERIFIED-tool]` quote and the `[WEAK]`
WebSearch-summarized modern-paper cluster in 3a instead.

**Conclusion for Step 2: the requirement is real, standard, and doubly
grounded — a `[VERIFIED-tool]`-sourced statement of WHAT the required content
is (Wikipedia), a `[WEAK]`-sourced statement of WHY (modern paper cluster on
anomaly cancellation), and a `[VERIFIED-tool]`-sourced, independently
rigorous QFT fact (Witten's SU(2) global anomaly) that supplies an even
stronger and more general version of the same "why," not contingent on
Pati-Salam specifically.** The primary 1974 text itself was not cleanly
read (3b), honestly flagged as a gap, not a blocker — the Wikipedia +
Witten-anomaly combination is treated as sufficient grounding for Step 3.

---

## 4. Does this project's specific commitment trigger the requirement? [Applying 1-3 together]

**Yes, in the following precise sense, distinct from — and stronger than —
E14 Reading 3 / E17 Section 5's characterization of the coupling-equality
assumption.** Since Section 1 establishes `SU(2)_R` is genuinely gauged in
this project (a real 4D gauge boson, independent of the later `g_{2R}=g_{2L}`
VALUE assumption), and since this project's own text assigns physical matter
charges under it (the electric-charge formula uses `T3R` via
`Y=T3R+(B-L)/2`, `preprint.tex:408`; the Higgs bidoublet is assigned under
it, `preprint.tex:355-357`), the Witten-anomaly-grounded consistency fact
from Section 3a applies directly and generically: **a genuinely gauged
`SU(2)_R` with charged matter cannot leave that matter as `SU(2)_R` singlets
— it must organize into complete `SU(2)_R` doublets, and the theory needs an
even number of them.** This is NOT contingent on the specific `g_{2R}=g_{2L}`
numerical equality (a different, still-unverified claim, Section 2) — it
follows from `SU(2)_R` being gauged AT ALL, which Section 1 establishes
independently.

Combined with `E9`/`E12`'s own already tool-verified fact (reused, not
re-derived here) that the ONLY values of this project's connection parameter
`t` with any nonzero `S³`-side kernel at all are `t=0` and `t=1` — if this
project's torsion-escape-route mechanism is meant to supply the `S³`-side
matter content for a genuinely `SU(2)_R`-gauged theory (as `preprint.tex`'s
own Section 2.1/spectral-action claims commit it to), **there is nowhere else
within this specific connection family to obtain the required `SU(2)_R`
doublet's worth of matter except `t=0`'s kernel** (per E17 Section 1's
already-established representation content, `t=0`↔`(1,2)`, `t=1`↔`(2,1)`,
under either labeling convention) — making the "why both" argument here
GENUINELY FORCED by (a)+(b)+(c) together, not a free "model-building choice"
in the way E14 Reading 3 characterized the coupling-equality reading. **This
is a materially stronger argument than anything round86-89 examined or
rejected** — it does not rely on borrowing a 2D string-worldsheet chirality
argument (round87-89's failure mode), and it does not rely on the specific,
still-unverified `g_{2R}=g_{2L}` coupling value (round86/E17's failure mode).

**Reused, not re-derived — the specific identification (per the task's own
instruction):** E17 Section 1 (`experiments/20260717-round85-e17-sector-
coexistence-gate/decision.md:50-80`) already tool-verified that, under either
labeling convention, `{ker D^{t=0}, ker D^{t=1}} = {(1,2),(2,1)}` exactly —
never two copies of the same piece. This maps directly onto Pati-Salam's own
`(4,2,1)`/`(4̄,1,2)` pattern (Section 3a): `t=1`'s `(2,1)` ↔ the `SU(2)_L`
doublet (Pati-Salam's `F~(4,2,1)`, left-handed), `t=0`'s `(1,2)` ↔ the
`SU(2)_R` doublet (Pati-Salam's `F^c~(4̄,1,2)`, right-handed) — modulo the
`SU(4)`-color index, which Section 5 below shows is NOT established in this
project's own construction.

---

## 5. Where the argument stops short of PASS — three independent, self-admitted gaps

### 5a. `SU(4)` itself is not geometrically realized — the pre-registered BLOCKED trigger [VERIFIED-tool, reused + reconfirmed]

`preprint.tex:280-284` (read directly this round): "The `U(1)_{B-L}` factor
needed to complete the Pati--Salam algebra `SU(3)_c×SU(2)_L×SU(2)_R×
U(1)_{B-L}` is **not** itself an isometry of `S³×S⁶`: an internal check (gate
G97, this work) finds **no `SU(4)` subgroup in `Iso(S³×S⁶)`**, so the `B-L`
charge cannot be embedded via `SU(4)_{PS}≃SO(6)` as an isometry generator."
Restated even more starkly in the paper's own Open Problems list
(`preprint.tex:1586-1601`, read in full this round): "an internal check (gate
G97, this work) finds `SU(4)` is **absent from** `Iso(S³×S⁶)=SO(4)×SO(7)`
**entirely**... an additional physical principle beyond representation
content and anomaly cancellation would be needed to single [`U(1)_{B-L}`]
out." And the paper's own CCM-comparison table (`preprint.tex:1174`, `1187-
1189`) flags `U(1)_{B-L}$ as "open" in the same row that credits
`SU(3)×SU(2)_L×SU(2)_R` "from spin connection."

**Consequence for this experiment:** the STANDARD Pati-Salam
completeness/anomaly-cancellation argument (Section 3a) is normally stated
and checked against the FULL `SU(4)×SU(2)_L×SU(2)_R` gauge group (in which
`SU(3)_c` and `U(1)_{B-L}$ are UNIFIED into one single `SU(4)` generator
set, and anomaly-freedom is checked against ALL of `SU(4)`'s generators, not
only `SU(3)_c`'s). This project's own text explicitly, repeatedly (three
independent citations above) admits this full unification is NOT
geometrically achieved — `SU(3)_c` and the `SU(2)_R$-gauging claim (Section 1)
are both real, but they are not shown to combine into one single,
geometrically well-defined `SU(4)` gauge symmetry; `U(1)_{B-L}$ is patched in
from fermion charge content post hoc, not gauged from the isometry group.
**This is precisely the second disjunct of the pre-registered BLOCKED
criterion** ("the `SU(4)×SU(2)_L×SU(2)_R` combination itself is
incomplete/open in this project's own text").

The narrower argument (Section 4, resting only on `SU(2)_R`'s own Witten-
anomaly consistency, not on full `SU(4)`) survives this gap — it does not
need `SU(4)` to be established. But the task's own PASS bar requires "no
further gap" in the FULL transfer, and the full Pati-Salam-style
completeness argument, AS STANDARDLY STATED (Section 3a), is not fully
available here because of this admitted incompleteness.

### 5b. This project's own explicit anomaly check does not verify the specific `SU(2)_R`-gauged condition [VERIFIED-tool, checked fresh this round]

`preprint.tex:309-320` (read directly this round, the paper's own explicit,
symbolically-verified anomaly-cancellation computation): checks four
conditions — `[Grav]²U(1)_Y`, `[U(1)_Y]³`, `[SU(3)]²U(1)_Y`,
`[SU(2)]²U(1)_Y` — using ONLY `T3L$ and the SM hypercharge `Y=T3R+(B-L)/2`
as a single derived combination. **This is the STANDARD MODEL's own anomaly
structure (right-handed fermions as `U(1)_Y`-charged `SU(2)_L$-singlets),
not a check phrased in terms of an independently, manifestly gauged
`SU(2)_R$** — nowhere in this computation is a `[SU(2)_R]²(anything)` or a
Witten-global-anomaly (doublet-parity) condition checked separately.
**This means this project has not itself verified, anywhere in its own text,
the SPECIFIC consistency condition (Section 3a/4) that would confirm its own
`SU(2)_R`-gauged construction is anomaly-free in the manifestly-left-right-
symmetric phase**, as opposed to only in the SM's own already-broken
low-energy phase. This is a further, independent gap this experiment
surfaces (not previously flagged by round86-89 or E14/E17, since none of
them examined the anomaly-cancellation section at all) — it does not itself
determine the verdict (Section 5a's G97 finding is dispositive on its own for
BLOCKED), but it means even a hypothetical future closing of gap 5a would
still leave this second, independent verification gap open.

### 5c. Lemma L5's asymmetric-chirality tension — unchanged, not resolved [DOCS, reused from E17]

E17 Section 5 (`experiments/20260717-round85-e17-sector-coexistence-gate/
decision.md:299-326`, reused, not re-derived here) already flagged: Lemma L5
(`preprint.tex:884-908`) derives an explicitly ASYMMETRIC left-handed excess
on the `S⁶` factor (`sign(ind)=+1`), not a parity-symmetric result — any
argument that Pati-Salam-style left-right symmetry forces both `S³`-side
sectors "would need to explain why the identical logic does not equally
force a symmetric (rather than the paper's own already-established
asymmetric) result on the `S6` factor." This experiment's stronger grounding
of the `SU(2)_R`-gauging claim (Sections 1-4) makes the ARGUMENT FOR
NEEDING both sectors more solid than E17 credited it — but it does **not**
resolve this specific tension, which remains exactly as open as E17 left it.
If anything, a more solidly-grounded "both sectors are needed" argument
SHARPENS the puzzle of reconciling it with `S⁶`'s asymmetric chirality
result, rather than dissolving it.

### 5d. No stated parent action either way [reused, unchanged from E18/KT-1]

Exactly as flagged in `claim.md`'s own pre-registered scope: even a full PASS
on the representation-completeness ARGUMENT (Sections 1-4) would only
establish WHY the matter content must exist in a complete theory — it would
not, by itself, supply E18/KT-1's core missing ingredient, a stated 13D
Lagrangian with independent fields for `t=0` and `t=1` and their own
equations of motion. This experiment does not attempt to supply one, and
none is found as a byproduct of the argument above.

---

## 6. Applying the pre-registered criteria

| Criterion | Finding |
|---|---|
| Does `preprint.tex` genuinely commit to gauging `SU(2)_R` (real gauge boson, not label)? | **YES** — Section 1, four independent, mutually-reinforcing citations (`:78-80`, `:187-198`, `:258-279`, `:355-357`, `:359-374`, `:1174`) |
| Does standard Pati-Salam/left-right model-building genuinely require both `(4,2,1)`/`(4̄,1,2)` given a gauged `SU(2)_R`? | **YES** — Section 3, grounded in a `[VERIFIED-tool]` Wikipedia quote, a `[WEAK]` converging modern-paper cluster, and a `[VERIFIED-tool]`-bibliographically-confirmed independent QFT fact (Witten's SU(2) anomaly) |
| Does this project's specific commitment level trigger the requirement (not merely resemble it)? | **YES** — Section 4: the argument rests on `SU(2)_R` being gauged AT ALL (established, Section 1), not on the separate, still-unverified `g_{2R}=g_{2L}` value assumption (Section 2) — a genuinely forced argument, not a free choice |
| Does the specific `t=0`/`t=1` ↔ `(4̄,1,2)`/`(4,2,1)` identification hold, reusing E16/E17? | **YES, qualitatively** — Section 4, reusing E17 Section 1's tool-verified representation labels |
| Is there "no further gap" in the transfer (PASS's own explicit bar)? | **NO** — Section 5: (a) full `SU(4)` unification self-admittedly absent from `Iso(S³×S⁶)` (gate G97, three independent citations); (b) this project's own anomaly check does not verify the `SU(2)_R`-gauged-specific condition; (c) Lemma L5's asymmetric-chirality tension (E17 Section 5) unresolved; (d) no parent action supplied either way |

**Verdict: BLOCKED**, via the pre-registered criterion's second disjunct
("the `SU(4)×SU(2)_L×SU(2)_R` combination itself is incomplete/open in this
project's own text, per an honest reading") — NOT FAIL, because Section 1
decisively rules out the FAIL criterion ("`SU(2)_R` stays label-only"); NOT
PASS, because Section 5 identifies concrete, self-admitted (not
manufactured) gaps that the task's own PASS bar ("no further gap") does not
tolerate.

---

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result kills:** the implicit assumption, carried since E14/E17,
  that this project's `SU(2)_R`/Pati-Salam-parity reading is ONLY a narrow,
  ad hoc "assumed coupling equality for one formula" with no deeper grounding
  — Sections 1-2 show the underlying GAUGING claim is real, independently
  established (via the same KK mechanism already used for `SU(2)_L`/`SU(3)_c`,
  reinforced by an actual spectral-action gauge-kinetic-term computation),
  and prior to the narrower coupling-value assumption E14/E17 correctly
  flagged as unverified. It also kills the possibility that a purely
  representation-theoretic/gauge-consistency argument (no worldsheet, no
  cone construction) could FULLY close E18's coexistence gap without further
  work — Section 5 shows concrete, independent reasons it does not, most
  decisively the self-admitted `SU(4)`-incompleteness (gate G97).
- **What this result does NOT kill:** the underlying `SU(2)_L×SU(2)_R`
  gauge-structure claim itself (real, and now shown stronger than previously
  credited); the possibility that resolving gap 5a (an explicit geometric
  `SU(4)` embedding, or an independently-derived `U(1)_{B-L}$) could, in
  future work, upgrade this experiment's BLOCKED to a genuine PASS without
  needing a fundamentally different argument; E16/E17's own representation-
  content findings (reused, unchanged); KT-8, H1c, or any headline claim
  (untouched, Section 5d).
- **What survives, confirmed stronger than before:** the distinction between
  "gauging commitment" (real, robust, independent of any specific coupling
  value) and "coupling-VALUE assumption" (narrow, still unverified) is now
  explicit and tool-grounded — narrowing the open question from "is there
  ANY real argument for Pati-Salam-style coexistence" (round86-89's
  territory, all closed negatively for string-worldsheet-borrowed
  candidates) to the SPECIFIC, nameable remaining gap: resolve gate G97's
  `SU(4)`-incompleteness (or find an independent argument that the narrower
  `SU(2)_R`-only Witten-anomaly consistency suffices without full `SU(4)`),
  and reconcile with Lemma L5's asymmetric chirality (E17 Section 5,
  unchanged).

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Resolve gate G97's `SU(4)`-incompleteness | An explicit geometric embedding of `U(1)_{B-L}$ into the isometry group, or an independently-motivated non-geometric origin — flagged as open in `preprint.tex:1586-1601` itself, unchanged by this experiment |
| Check whether the NARROWER `SU(2)_R`-only Witten-anomaly argument (Section 4) suffices WITHOUT full `SU(4)` | Would require explicitly verifying the `SU(2)_R$ global-anomaly (even-doublet) condition using ONLY this project's own already-established fermion content (Section 5b's gap) — not attempted here |
| Reconcile with Lemma L5's asymmetric `S⁶`-side chirality | Unchanged from E17 Section 5's own Relaxation Map item — either an independent reason `S³` needs L/R-symmetric doubling while `S⁶` does not, or abandonment of this route |
| Supply an explicit parent action | Still E18/KT-1's core missing ingredient — a stronger completeness ARGUMENT (this experiment) is not a substitute for a stated Lagrangian with independent `t=0`/`t=1` fields and their own equations of motion |

## Assumptions carried, unresolved

- `SU(2)_L`=left-translation vs. its mirror (`CONVENTION_TABLE.md` row 6) —
  not resolved here; per E17 Section 1, the qualitative finding (`{(1,2),
  (2,1)}`, never two copies) is convention-independent, so this ambiguity
  does not affect the BLOCKED verdict.
- `t=1`'s kernel exists only under `c0=-2` (`CONVENTION_TABLE.md` row 5) —
  carried forward unchanged, not re-litigated here.
- `D_full²=D_{S3,t}²⊗I+I⊗D_{S6,twisted}²` (E2/E12's decoupling assumption) —
  presupposed wherever E16/E17's findings are reused, exactly as those
  experiments themselves presuppose it.
- The specific published version of Pati-Salam's own primary text
  corresponding to the retrieved (heavily OCR-garbled) `inspirehep.net`
  proceedings reprint was NOT independently confirmed this round (Section
  3b) — the `(4,2,1)`/`(4̄,1,2)` notation itself rests on the `[VERIFIED-
  tool]` Wikipedia quote and the `[WEAK]` modern-paper cluster instead, not
  on this specific primary-source fragment.
- Whether a more careful, dedicated future check of the `SU(2)_R`-specific
  Witten/global-anomaly condition against this project's own already-derived
  32-state fermion content (Section 5b) would pass or fail — NOT checked
  this round; flagged as the single cheapest, most concrete next step in the
  Relaxation Map above.

## What this does NOT mean

1. Does **not** establish PASS for E18/round86's coexistence question — a
   BLOCKED verdict, per Section 6.
2. Does **not** reopen or overturn round86 (E18)'s `BLOCKED`, round87
   (E19)'s `FAIL`, round88 (E20)'s `FAIL`/`FAIL`, or round89's `PARTIAL`
   findings — this experiment supplies a FOURTH, independent, spacetime-
   native candidate argument, found stronger in one specific respect
   (Sections 1-2, 4) than prior characterizations credited, but still
   short of PASS for the reasons in Section 5, none of which contradict
   rounds 87-89's own (unrelated, worldsheet-specific) closure reasons.
3. Does **not** prove the `SU(2)_R`-Witten-anomaly argument can NEVER close
   this gap — only that, AS THIS PROJECT'S TEXT CURRENTLY STANDS, the full
   transfer has a self-admitted incompleteness (gate G97) and an
   independent, previously-unexamined verification gap (Section 5b), neither
   of which this experiment attempts to close.
4. Does **not** affect this project's `N_gen=3` headline claim, which rests
   on the independently-established G73/G74A/G74B `S⁶`-only triality/index/
   chirality chain (`activeContext.md`, `reports/
   PROJECT_360_ROUND3_SYNTHESIS.md`) — this experiment concerns only the
   separate, already-non-load-bearing S³-side torsion-escape-route program
   (`preprint.tex:1467-1497`, "candidate mechanism... physically
   unmotivated, not a resolution").
5. Does **not** claim the retrieved `inspirehep.net` proceedings text is a
   clean, reliable primary source — Section 3b reports the extraction
   attempt honestly, including its OCR corruption and the mismatch with the
   more commonly cited minimal `SU(4)_c×SU(2)_L×SU(2)_R` formulation; it is
   used only as weak corroboration of the general "left-right symmetric
   Lagrangian" motivation, not as the source for any specific notation or
   numerical claim.
6. Does **not** claim this project's own explicit anomaly-cancellation
   computation (`preprint.tex:309-320`) is wrong — only that it checks a
   DIFFERENT (SM-broken-phase, `U(1)_Y`-based) set of conditions than the
   one this experiment's argument would need verified (a manifestly
   `SU(2)_R`-gauged, Witten-anomaly condition), per Section 5b.
7. Does **not** re-derive or challenge any of E1-E20's own tool-verified
   results — all reused here purely by citation.
8. Nothing in this experiment was submitted, posted, or sent anywhere
   external; this project's standing rule against arXiv submission and
   against contacting Tom Lawrence is unaffected and was not approached.

## Pearl-registry candidate

**Observation, concrete enough to flag:** the distinction this experiment
turned on — "a gauge symmetry's mere EXISTENCE (a structural, KK-mechanism-
derived commitment) is a categorically different and often much STRONGER
claim than a SPECIFIC coupling-VALUE or symmetry-assumption used downstream
for one phenomenological estimate" — is a general pattern worth watching for
elsewhere in this project (and in gauge-theory model-building generally):
prior rounds (E14, E17, round86) correctly rejected the narrower,
downstream claim (`g_{2R}=g_{2L}`) but this had the side effect of under-
crediting the more basic, independently solid claim (`SU(2)_R` is gauged at
all) that the narrower claim was built on top of. **Falsifiable prediction,
if pursued:** any future round examining whether a "left-right symmetric" or
"parity" argument applies to this project should first separately check (a)
whether the underlying gauge symmetry genuinely exists in the project's own
construction, independent of (b) whether a SPECIFIC numerical or exact-
symmetry assumption about it has been verified — these are logically
independent questions, and this experiment shows conflating them can hide a
real, well-grounded structural fact under an already-and-correctly-rejected
narrower claim. **Impact score ~4** (affects how this project's own future
S³-torsion-escape-route rounds read the `SU(2)_L×SU(2)_R` gauge claim; the
general "gauging-commitment vs. coupling-value" distinction is standard
practice in the broader gauge-theory field, so the pearl here is specifically
"re-check this project's own prior BLOCKED/FAIL verdicts on this exact
axis before assuming they covered the ground they look like they covered" —
narrow, project-internal, not cross-domain). Not registered to the global
`pearl_registry/INDEX.md` — project-internal.
`next_check`: before the torsion-escape-route program's next round, if any,
check whether Section 5b's specific gap (this project's own anomaly
computation not yet checked in the manifestly-`SU(2)_R`-gauged language) can
be closed cheaply using G6's own already-existing 32-state bookkeeping,
before assuming it requires new physics input.

## Check (reproduces this decision)

This is a literature-and-text classification round; there is no new
numerical script (per this project's own precedent, round86-90). The
"check" is: (1) every `preprint.tex` line cited above (78-80, 187-198,
258-287, 292-320, 355-374, 405-431, 1174, 1179, 1187-1189, 1586-1601) was
read directly this round via `Read`, not from memory or a prior round's
paraphrase — confirmed by direct quotation matching the file's exact text;
(2) the Wikipedia quote (Section 3a) was retrieved via a direct `WebFetch`
call this round, not a `WebSearch` summary, and is marked `[VERIFIED-tool]`
accordingly; the anomaly-cancellation-reason quote and the Witten-anomaly
bibliographic identification were retrieved via `WebSearch` and are marked
`[WEAK]`/`[VERIFIED-tool: bibliographic cross-check]` respectively, per this
project's own evidence-marker discipline; (3) the `inspirehep.net` PDF was
fetched via `WebFetch`, saved locally, and extracted via `pdftotext -layout`
this round (271 lines), with its OCR-corruption and structural mismatch
honestly reported (Section 3b), not hidden; (4) every internal project
citation (E9, E12, E14, E16, E17, E18/round86, E19/round87, E20/round88, `CONVENTION_TABLE.md`) was
reused by direct `Read` of the cited file this round, at the start of this
experiment, not from memory; (5) the final verdict follows deductively from
the pre-registered criteria table (`claim.md`) applied to Sections 1-5, with
no step skipped or forced.
