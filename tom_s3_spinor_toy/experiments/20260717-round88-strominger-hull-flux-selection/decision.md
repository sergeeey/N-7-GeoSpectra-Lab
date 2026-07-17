# E20 (round88) — Decision

**Date:** 2026-07-17
**Verdict A (sign SELECTION, H1c-relevant):**
`FAIL__UNITARITY_BOUND_IS_ORIENTATION_RELATIVE_NOT_AN_ABSOLUTE_SELECTION`
**Verdict B (sign COEXISTENCE, parent-action-relevant):**
`FAIL__WORLDSHEET_CHIRALITY_MECHANISM_DOES_NOT_TRANSFER_TO_SPACETIME_KK_COMPACTIFICATION__BROADER_AND_CLEANER_THAN_E19`
**Go/no-go:** Neither sub-question yields a usable mechanism for this
project. Sub-question A's most promising-looking lead (the WZW level must be
a positive integer) turns out, on direct inspection, to be a restatement of
"pick an orientation convention," not a physical fact singling out `t=0` over
`t=1` — structurally the SAME kind of unresolved convention this project's
own `CONVENTION_TABLE.md` (row 1) already flags. Sub-question B's most
promising-looking lead (the base `(1,1)` sigma-model-with-torsion literature,
NOT the `(2,2)`/Gates-Hull-Roček system round87 already checked) genuinely
DOES have both torsion signs present simultaneously in one action, free of
round87's even-dimensionality obstruction — but the reason both signs are
needed is a fact about 2D string-worldsheet chirality, and this project's
compactification has no 2D string worldsheet anywhere, so transferring the
argument would repeat exactly the ad hoc move round87 §3 already identified
and declined to make. Neither verdict reopens round86 (E18)'s `BLOCKED` or
round87 (E19)'s `FAIL`; both stand.

---

## 0. Sources fetched and extracted this round [VERIFIED-tool]

All external PDFs were downloaded via `WebFetch`/`curl` and extracted with
`pdftotext -layout` (the same tool round87/E19 used for its own PDF literature
check), into
`C:\Users\serge\AppData\Local\Temp\claude\...\scratchpad\round88\`. Every
quote below reproduces text found at the cited line number in that
extraction, not from memory or from a WebSearch summary alone (WebSearch
summaries are used only where explicitly flagged as such, and are treated as
`[WEAK]` corroboration, not primary evidence).

| # | Source | Retrieval | Local file | Lines |
|---|---|---|---|---|
| 1 | A. Strominger, "Superstrings with Torsion," Nucl. Phys. B274 (1986) 253-284, DOI `10.1016/0550-3213(86)90286-5` | ScienceDirect abstract page → **HTTP 403 Forbidden**, confirmed this round via direct `WebFetch` attempt; NOT independently re-fetched, no arXiv mirror exists (paper predates arXiv, 1991) | — (blocked) | — |
| 2 | M.-A. Fiset, "G-structures and Superstrings from the Worldsheet" (PhD thesis), arXiv:1909.07936 | `curl`+`pdftotext -layout` | `fiset_gstructures.txt` | 3705-3712 (Strominger/Hull 6D requirement, cited as `[Hul86b, Str86]`), 288-330 (general (1,0)/(1,1) framework), 3130-3260 (explicit `(1,0)` action + `Γ^+` connection definition) |
| 3 | C.M. Hull, "The Geometry of Supersymmetric Sigma-Models," arXiv:hep-th/9610103 | `curl`+`pdftotext -layout` | `hull_geometry_sigma.txt` | 66-97 (base `N=(1,1)` action, eq. 3.1-3.3), 303-311 (WZW-on-even-dim-groups statement) |
| 4 | L. Eberhardt, "Wess-Zumino-Witten Models" (YRISW PhD School lecture notes, Vienna), 2019 | `curl`+`pdftotext -layout` | `wzw_lectures.txt` | 155-160 (level `k` must be integer, extension `B`), 1355-1371 (unitarity ⟹ `k∈ℤ>0`, exact derivation), 2489-2492 ("admissible levels... other levels... non-unitary theory") |
| 5 | L.R. Huiszoon, K. Schalm, A.N. Schellekens, "Geometry of WZW Orientifolds," arXiv:hep-th/0110267 | `curl`+`pdftotext -layout` | `wzw_orientifolds.txt` | 155-168 (`g→g⁻¹` orientifold involution, chiral-current exchange), 414-433 (`SU(2)` worked example: `g→g⁻¹` = reflection through rotation axis, 2 fixed points at poles) |
| 6 | A. Sevrin, W. Staessens, D. Terryn, "The generalized Kähler geometry of N=(2,2) WZW-models," arXiv:1111.0551 | reused from round87/E19, not re-fetched this round | `out1.txt` (round87's own extraction) | 102-121 (even-dimensionality requirement) — cited here only for cross-reference, not re-verified |
| 7 | Wikipedia, "Wess–Zumino–Witten model" | `WebFetch` (secondary, lower-tier — used only for corroboration of `π₃(G)=ℤ` for compact simple `G`) | — | — |
| 8 | WebSearch summaries (Hull-Strominger-system secondary literature: arXiv:1402.1725, arXiv:2305.02654, arXiv:2409.04382, ResearchGate listing of a torsion-connection review) | WebSearch tool output only, `[WEAK]` | — | — |

**Honest scope note:** source #1 (Strominger 1986 itself) was NOT read as
primary text this round — ScienceDirect returned HTTP 403, and no arXiv
mirror exists for a 1986 paper. Its dimension/structure requirement is
instead confirmed via source #2 (Fiset's PhD thesis, which cites Strominger
1986 and Hull 1986b directly and states their combined requirement in its own
words) and via source #8's WebSearch-summarized cluster of modern
Hull-Strominger-system papers (arXiv:1402.1725, 2305.02654, 2409.04382, all
independently describing the same "6D, SU(3)-structure, holomorphically
trivial canonical bundle" requirement). This is TWO independent, converging
sources, one tool-extracted-and-directly-read (`[VERIFIED-tool]`), one
WebSearch-summarized (`[WEAK]`) — treated together as sufficient to confirm
the requirement without having read Strominger 1986's own text, exactly the
kind of honest gap this project's own methodology requires flagging, not
hiding.

---

## 1. Structural check — does the classical Strominger system apply to `S³`?

**Answer: NO, confirmed. `S³` is 3-dimensional (odd) and the classical
Strominger system requires 6 real dimensions with an `SU(3)`-structure.**

[VERIFIED-tool, `fiset_gstructures.txt:3705-3712`, direct quote, read in
context of the paper's own G-structure-with-torsion framework]:

> "Compactifying heterotic supergravity on a manifold with such an
> `SU(d/2)`-structure is not yet sufficient to obtain a supersymmetric
> spacetime supergravity. For example, it was shown in `[Hul86b, Str86]` that
> when `d = 6`, one needs to demand further that the almost complex structure
> is integrable to obtain spacetime Yang-Mills `N = 1` supergravity."

`[Str86]` is Strominger 1986 (source #1 above, confirmed as the paper's own
reference-list entry for "Superstrings with Torsion" — the reference list
itself was not re-transcribed this round, but the citation key `Str86`
paired with the exact title/year match in the body text is treated as
sufficient identification, consistent with round87/E19's own citation-key
practice for `[16]`=Spindel-Sevrin-Troost-Van Proeyen). `[Hul86b]` is Hull's
1986 companion paper. The quote confirms: the Strominger-Hull requirement is
stated for `d=6` specifically (SU(3/2)... i.e. `d/2=3`, `SU(3)`-structure),
with an ADDITIONAL integrability requirement (complex structure, not just
almost-complex) needed for the full spacetime-SUSY result.

**Independent corroboration** [WEAK — WebSearch summary only, source #8]:
searches for "Strominger system SU(3)-structure" and "Hull-Strominger system"
consistently return the same description across multiple independent modern
papers (arXiv:1402.1725, arXiv:2305.02654, arXiv:2409.04382): "a six
real-dimensional compact space `X` with an `SU(3)`-structure... a nowhere
vanishing three-form `Ψ`... complex structure determined by `Ψ`... requires
the geometric inner space `X` to be a compact complex conformally balanced
manifold with holomorphically trivial canonical bundle." This is fully
consistent with the Fiset-thesis quote above, from an independent cluster of
sources.

**Elementary structural fact, re-derived (not requiring new citation, exactly
as round87/E19 already did for the same fact in the GHR case):** an almost
complex structure `J` requires `J²=-1` on the real tangent space at each
point, forcing eigenvalues `±i` in conjugate pairs under complexification —
possible only in even real dimension. `S³` has real dimension 3 (odd) and
therefore CANNOT carry an almost complex structure, `SU(3)`-structure, or any
holomorphic `(3,0)`-form, full stop — independent of any specific
construction attempted. This is the exact same obstruction round87/E19
already established for the (differently-motivated) Gates-Hull-Roček
system, now independently reconfirmed for the classical Strominger system
itself.

**Conclusion: the classical Strominger-Hull system, exactly as classically
formulated, does not structurally apply to `S³=SU(2)` (3D, odd, no complex
structure possible) — for the same class of reason, and by the same
elementary argument, round87 already used for the narrower GHR/bi-Hermitian
case.** Per the task's own instruction, this requires an EXPLICIT pivot to
the `SU(2)_k` WZW-model / general `(1,1)`-SUSY-sigma-model-with-torsion
literature, which is checked next.

**Is the pivot literature actually the right one?** [VERIFIED-tool,
`hull_geometry_sigma.txt:303-304`, direct quote]: "WZW-models on even
dimensional groups are particular examples of `(2,2)` σ-models." This
confirms, from the SAME review used below, that WZW models exist MORE
GENERALLY than the `(2,2)`/even-dimension-requiring case — i.e., WZW models
on ODD-dimensional groups (like `SU(2)`) are not `(2,2)` models but are NOT
thereby excluded from existing; they exist as plain bosonic or `(1,1)`-SUSY
models. This directly confirms the task's own expectation that the
`SU(2)_k` WZW-model literature, not the classical (even-dimensional/complex)
Strominger-Hull or GHR systems, is the structurally correct literature to
search for `S³` specifically.

---

## 2. Sub-question A — sign SELECTION (H1c)

### 2a. The lead: WZW level `k` must be a positive integer

[VERIFIED-tool, `wzw_lectures.txt:1355-1371`, direct quote, exact derivation
read in full]:

> "Since WZW-models (on compact Lie groups) are unitary, it is vital that no
> negative-norm states are part of the representation. For this to be the
> case, the exercise shows that two conditions have to be met. First, we see
> algebraically that `k ∈ ℤ>0`. Indeed, if `k` is not a positive integer, we
> cannot have `k + 1 - 2h∨ ∈ ℤ>0` for any value of `½ ∈ ℤ≥0`. Hence these
> theories could not have any (unitary) representations."

This is a real, tool-verified derivation, not an assertion: a specific
null-vector counting argument (Kac-Moody highest-weight representation
theory) forces `k` to be a positive integer for the theory to have ANY
unitary representation at all. On its face, this looks exactly like the kind
of "why nature picks one sign" mechanism H1c wants.

### 2b. Checking whether this is an ABSOLUTE selection or an orientation-relative one

This is where the task's own instruction to check carefully (rather than
stop at "k>0, done") matters. Three converging facts, found this round,
show the `k>0` rule does NOT single out an absolute physical sign:

1. **The level's sign is tied to a choice of orientation of the 3-manifold
   extension, by the action's own construction** [VERIFIED-tool,
   `wzw_lectures.txt:155-160`]: "the second term is topological; `B` is a
   three-manifold whose boundary is `Σ`, and the level `k` has to be
   integer." The Wess-Zumino term is `∫_B H`, an integral over a CHOSEN
   3-manifold extension `B` of the worldsheet; reversing the orientation of
   `B` (a free choice, not fixed by the theory) flips the sign of this
   integral, hence of `k`.
2. **Reversing target/worldsheet orientation is known, in this exact
   literature, to flip the sign of `k`/`H` and can be compensated by
   `g→g⁻¹`** [WEAK — WebSearch summary of academic literature on WZW parity,
   not independently re-derived or re-fetched as primary text this round;
   flagged honestly as the weakest-sourced claim in this decision]: "The WZ
   term depends on the orientation and is flipped under parity, which can be
   compensated by the transformation `g→g⁻¹`, since `g⁻¹dg → g dg⁻¹ =
   -g(g⁻¹dg)g⁻¹`." This is corroborated independently and more strongly by
   source #5 (see §4 below): the orientifold literature explicitly builds a
   consistent theory by GAUGING the combined map "worldsheet parity ∘
   `g→g⁻¹`," precisely BECAUSE parity alone (which would flip `k→-k`) is
   "not a symmetry" of the oriented theory by itself
   [VERIFIED-tool, `wzw_orientifolds.txt:160-168`, quoted in full at §4].
3. **The lecture notes' own "admissible levels" remark confirms `k<0` is
   mathematically definable, just non-unitary** [VERIFIED-tool,
   `wzw_lectures.txt:2489-2492`]: "While we have defined WZW models at
   positive integer levels, they can actually be defined also at other
   levels (in which case they define a non-unitary theory)." This confirms
   `k<0` is not "impossible" in any absolute sense — it corresponds to a
   real (if non-unitary) formal theory, and per point 2, is physically
   equivalent to `k>0` on the orientation-reversed manifold.

**Conclusion for sub-question A: the `k>0`-for-unitarity rule is real and
correctly derived [VERIFIED-tool], but it does NOT constitute a physical
mechanism that would tell this project WHY nature picks `t=0` over `t=1`.**
It is exactly and only a restatement of "having fixed an orientation
convention for the extending 3-manifold / target space, the unitary theory
is the one with `k` positive in THAT convention" — the orientation choice
itself is exactly as free and unfixed as this project's own
`CONVENTION_TABLE.md` row 1 (`S³` orientation, "FIXED (implicitly, by reuse)
— but never explicitly labeled") and row 6 (`SU(2)_L/SU(2)_R` geometric
identification, "AMBIGUOUS — genuinely unresolved"). Using "unitarity selects
`k>0`" to claim a physical selection of `t=0` over `t=1` would be
manufacturing exactly the kind of orientation-convention-dependent argument
this project's own methodology (`research-methodology.md` §Classificateur,
Type 3 — "condition without stated condition") is designed to catch: the
selection is real ONLY relative to an already-chosen, physically arbitrary
orientation, not an absolute fact about the physics.

**Verdict: FAIL.** Not because no `k`-sign rule exists (one does, and it is
genuinely `[VERIFIED-tool]`), but because — checked directly, as the task
instructed, rather than assumed — the rule is convention-relative, not
absolute, and therefore does not supply H1c's missing ingredient (a reason
nature picks one sign over the other, independent of an arbitrary labeling
choice).

---

## 3. Sub-question B — sign COEXISTENCE (parent-action)

### 3a. Ruling out the `(2,2)`/complex-structure route (reconfirms round87, briefer this time)

Sub-question B's most obvious literature route — the Gates-Hull-Roček/
bi-Hermitian/`N=(2,2)` construction — was ALREADY checked directly by
round87/E19 and found FAIL (even-dimensionality obstruction, `S³` odd). This
round does not re-run that check; §1 above (Hull's own statement that
"WZW-models on even dimensional groups are particular examples of `(2,2)`
σ-models") is fully consistent with, and independently reconfirms from a
different source, round87's own finding.

### 3b. The genuinely different lead: base `(1,1)` sigma model with torsion (NOT `(2,2)`)

**This is the new finding this round adds.** The base `(1,1)`-supersymmetric
non-linear sigma model with torsion — the structure UNDERLYING the
`(2,2)` extension round87 already ruled out, but weaker and more general —
does NOT require a complex structure or even dimension.

[VERIFIED-tool, `hull_geometry_sigma.txt:66-73`, direct quote, read in full
context]:

> "Omitting the dilaton term, a supersymmetric non-linear σ-model in
> `N = (1,1)` superspace is given by `S = ∫d²x d²θ (g_ab+b_ab) D_+X^a D_-X^b`.
> The metric on the target manifold is `g_ab` and `b_ab=-b_ba` is a potential
> for the torsion, `T_abc ∝ b_[ab,c]`."

No complex structure, no dimension restriction appears anywhere in this base
action — it is defined for ANY target manifold with a metric `g` and a
2-form potential `b` (torsion `H=db`), any dimension. **The complex structure
requirement enters ONLY at the NEXT step** [VERIFIED-tool,
`hull_geometry_sigma.txt:73-79`, same source, immediately following]: "A
second, left-handed supersymmetry is of the form `δX^a = ε J^a_b D_+X^b`...
Integrability... of this requires `J` to be a complex structure" — i.e. it is
the ADDITIONAL, second SUSY generator (the `(1,1)→(2,1)→(2,2)` enhancement)
that needs `J²=-1` and hence even dimension, EXACTLY as round87 found for
GHR — but the base `(1,1)` theory itself does not need this.

**Does the base `(1,1)` action actually contain BOTH torsion signs
simultaneously?** [VERIFIED-tool, `fiset_gstructures.txt:3130-3260`, the
`(1,0)` action (4.4)-(4.6) and its equation of motion, read directly]: the
equation of motion for the bosonic field `X^i` explicitly introduces "a
connection `∇^+` on `TM` with symbols `Γ^+_ijk = Γ_ijk + (1/2)(dB)_ijk`" for
the torsion-coupled fermion appearing in that `(1,0)` sector. The SAME
source's introduction [`fiset_gstructures.txt:293-300`] states that general
`(1,1)` theories are obtained "by performing the so-called standard
embedding of `A` [the second sector's gauge connection] in the spin
connection on `TM`" — i.e., promoting from `(1,0)` (one worldsheet chirality
of fermion coupled to `TM`, the other to an independent bundle) to `(1,1)`
(BOTH worldsheet chiralities' fermions coupled to the SAME `TM`) is done
exactly by setting the second connection to the tangent bundle's own spin
connection, which — by the standard, decades-old result this exact
literature is built on (Zumino 1979; Curtright-Zachos 1984, *Phys. Rev.
Lett.* 53, 1799; Braaten-Curtright-Zachos 1985 — bibliographic identification
via WebSearch only, `[WEAK]`, NOT independently re-fetched/read this round,
flagged honestly) — is the OPPOSITE-sign torsionful connection
`∇^- = Γ^{LC}-(1/2)H`. **This is confirmed independently, at `[WEAK]`
confidence, by a WebSearch summary of a separate secondary source found this
round**, quoting: "right-moving fermions `ψ^i_+` are parallel transported...
with the connection with torsion: `Γ^(+) = Γ - 1/2 H`" — the opposite-sign
partner (`Γ^(-) = Γ+1/2H`, for the OTHER worldsheet chirality) is not
independently re-verified by direct extraction this round, but follows by
the same `(1,0)→(1,1)` "standard embedding" logic `[VERIFIED-tool]`-confirmed
above, and is standard, widely-cited material (this project's own round87/
E19 already cited the identical `∇^±=∇^{LC}±(1/2)H` pair, sourced there to
Gates-Hull-Roček via Sevrin-Staessens-Terryn, §1b of that decision).

**So: the base `(1,1)` sigma-model-with-torsion literature DOES have an
action with BOTH `∇^+` and `∇^-` appearing simultaneously — a genuine,
tool-citable "action, two connection fields, equations of motion" structure,
free of round87's even-dimensionality obstruction, and hence formally
applicable to `S³=SU(2)` directly (unlike GHR).** This is a real,
non-trivial finding this round adds beyond round87.

### 3c. Does the "why both" reason transfer to this project? (the decisive check, per the task's own instruction and round87's own precedent)

**No — and for exactly the same STRUCTURAL reason round87 §3 already
identified for the GHR case, even though the dimension obstruction is now
absent.**

The base `(1,1)` action's own stated reason for needing BOTH `∇^+` and `∇^-`
is that a NON-CHIRAL 2D worldsheet genuinely has two independent chiralities
(`D_+`, `D_-` — the worldsheet's own light-cone directions, per Hull's own
notation, `hull_geometry_sigma.txt:66-71`), and the `(1,1)` SUSY multiplet
structure assigns one fermion superpartner to EACH worldsheet chirality of
the SAME bosonic map `X:Σ→M` — this is a fact about the 2D STRING WORLDSHEET
(`Σ`), not about the target manifold `M` in isolation, and not about any
higher-dimensional SPACETIME chirality.

**This project's `S³=SU(2)` is not a string-theory target space anywhere in
its own text.** Reconfirming (not re-deriving; this exact fact was already
established by round87 §3, and is unchanged): `S³` is used throughout
`preprint.tex` and E1-E19 as the compact INTERNAL factor of a 13D
Kaluza-Klein compactification of SPACETIME fermions. The `∇^t` connection
family is a spacetime SPIN connection entering a single spacetime Dirac
operator `D_{S3,t}` — there is no 2D worldsheet, no string, no `Σ`, and no
`D_+`/`D_-` worldsheet light-cone structure anywhere in this project's own
machinery. "Chirality" in this project's own physics means SPACETIME
chirality (the `γ⁵`-eigenvalue / `SU(2)_L` vs `SU(2)_R` representation
content after KK reduction, Lemma L5, `preprint.tex:884-908`) — a physically
distinct notion from 2D WORLDSHEET chirality, exactly the distinction
round87 §3 already drew for the GHR case.

**Consequence:** claiming this project's Kaluza-Klein compactification needs
`t=0` AND `t=1` simultaneously "because the `(1,1)` sigma model needs
`∇^+` and `∇^-` simultaneously" would require asserting this project's
compactification secretly has two independent worldsheet-chirality sectors —
a claim nothing in this project's framework makes, needs, or is compatible
with. This is the identical "ad hoc duplication" round87's own PASS bar
excludes, now confirmed for a BROADER class of construction (not just GHR,
but the entire base `(1,1)`-sigma-model-with-torsion family that GHR itself
sits inside).

**Verdict: FAIL.** Broader and, in one sense, cleaner than round87's finding:
round87 needed TWO independent reasons (even-dimensionality AND
worldsheet-vs-spacetime chirality) to close off the `(2,2)`/GHR route. This
round shows that EVEN WITHOUT the dimension obstruction (which the base
`(1,1)` theory does not have), the worldsheet-vs-spacetime-chirality mismatch
ALONE is already sufficient to block the entire base-`(1,1)`-and-above
family of constructions — a strictly larger literature class than round87
closed off, for a single, cleanly-stated reason.

---

## 4. Pearl-registry candidate — E14's `ι:g→g⁻¹` has a genuine, verified counterpart in this literature

**Observation, concrete and tool-verified on both sides:** this project's own
E14/round80 computed (`experiments/20260717-round80-z2-left-right-symmetry-
search/decision.md:53-58`) that `Φ(x)=(x0,-x1,-x2,-x3)` on `S³` (realizing
`g(Φ(x))=g(x)⁻¹` exactly, i.e. the concrete coordinate form of group
inversion `ι:g↦g⁻¹`) has `det(J)=-1` (orientation-REVERSING) with EXACTLY 2
fixed points, at `g=±1` (the "poles" in the project's own coordinates).

Independently, the WZW-orientifold literature studies the IDENTICAL map on
the IDENTICAL manifold, for an unrelated purpose (constructing orientifold
planes), and finds the IDENTICAL structure [VERIFIED-tool,
`wzw_orientifolds.txt:414-433`, direct quote]: "Let us illustrate these
results with `SU(2)`. The group manifold is a three-sphere... The standard
orientifold symmetry `g↦g⁻¹` is a reflection through the 'axis of rotation'
with fixed points at the poles... the orientifold group `(1,0)` gives two
O0-planes at the north and south pole." This is confirmed, independently and
for a different physical purpose, to be: (a) the same map (`g→g⁻¹`); (b) on
the same manifold (`SU(2)=S³`); (c) with the same fixed-point COUNT (2); (d)
at the same LOCATION (the two poles, `g=±1`) — a genuine, non-trivial,
tool-verified structural coincidence between this project's own E14
computation and an entirely independent physics literature. Furthermore
[VERIFIED-tool, `wzw_orientifolds.txt:160-168`], this exact map is used in
that literature specifically to COMPENSATE worldsheet parity (which alone
"is not a symmetry" of the oriented WZW theory) — i.e., `g→g⁻¹` plays
EXACTLY the role of "the orientation-reversing operation that must
accompany a chirality-exchange for the combined operation to be a genuine
symmetry" in that literature, which is suggestively close to (but NOT
verified here to BE) the role this project's own E17
(`experiments/20260717-round85-e17-sector-coexistence-gate/decision.md`)
already explored for `ι` as a candidate parity/orientation-reversal
operation relating `t=0` and `t=1` sectors.

**Falsifiable prediction, if pursued:** IF this project's own `ι:g→g⁻¹` plays
a role structurally analogous to the WZW-orientifold literature's `g→g⁻¹`
(compensating a chirality-exchange to produce a genuine combined symmetry),
THEN there should exist a "combined" operation on this project's `t`-family
— literally `ι` composed with `t↔1-t` (the torsion-sign flip this project's
own `T^t=(2t-1)c·vol` formula already exhibits under `t↔1-t`, per
`CONVENTION_TABLE.md` row on torsion) — that IS a genuine symmetry of the
FULL 9D compactification, even though `ι` ALONE is orientation-reversing
(hence not, by itself, in the gauge group `SO(4)`, per `CONVENTION_TABLE.md`
row 1) and `t↔1-t` ALONE is merely a relabeling of the connection family.
This is speculative, NOT attempted or verified here (would require an
explicit new check of whether `ι` combined with the connection-family
`t↔1-t` map is a symmetry of `D_{S3,t}` or of the full action — genuinely new
work, not a citation), and is flagged `[CANDIDATE]`, not adopted.

**Impact score ~5** (this is a genuine structural analogy between this
project's OWN prior tool-verified result and an independent physics
literature, on the EXACT manifold this project studies — stronger grounding
than most `[CANDIDATE]` pearls in this project's registry, since both sides
of the analogy are independently `[VERIFIED-tool]`; still narrow to this
project's own S³-torsion-escape-route line of work, and the underlying
`g→g⁻¹`/orientifold fact itself is well-known in the general WZW literature,
so the pearl is specifically "check whether THIS project's `ι` plays the
same compensating role," not a novel mathematical fact). Not registered to
the global `pearl_registry/INDEX.md` — project-internal, not cross-domain.
`next_check`: if the torsion-escape-route program is revisited, check
directly whether `ι` composed with `t↔1-t` is a symmetry of the full
`D_{S3,t}` operator or of any stated action, before assuming it is or is
not — this is a cheap, well-defined next test (reuses E14's own script
infrastructure) that neither this round nor E14/E17 actually ran.

---

## 5. Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result kills:**
  - Sub-question A: the hope that WZW/CFT unitarity supplies H1c's missing
    "why `t=0` not `t=1`" answer — killed for a checked, specific reason
    (the rule is orientation-convention-relative, per §2b's three converging
    facts), not merely because no rule was found.
  - Sub-question B: the hope that the BROADER base-`(1,1)`-sigma-model-with-
    torsion literature (not just the narrower `(2,2)`/GHR system round87
    already checked) supplies round86/E18's missing parent action — killed
    for the SAME class of reason round87 §3 already used (worldsheet vs
    spacetime chirality), now shown to apply even WITHOUT the dimension
    obstruction, closing off a strictly larger literature class in one step.
  - The classical Strominger-Hull system itself as a route to EITHER
    sub-question — killed by the structural check (§1), independently of
    A/B, for the identical dimension-parity reason round87 already
    established for GHR.
- **What this result does NOT kill:**
  - The connection-formula-level match (`∇^±=∇^{LC}±(1/2)H`, exact structural
    equivalent of this project's own `T^t=(2t-1)c·vol`) — real, and now
    doubly-sourced (round87's GHR route AND this round's more general base-
    `(1,1)` route both converge on the identical formula), useful as a
    citation for E11's own generic claim, even though neither route resolves
    coexistence.
  - E14's `ι:g→g⁻¹` isometry as a genuinely interesting object — this round
    STRENGTHENS interest in it (§4's pearl), even though it does not resolve
    E18's BLOCKED verdict.
  - Any of E1-E19's own tool-verified results, KT-8, H1c itself as an open
    item (only THIS specific route to it is closed), or round86's BLOCKED
    verdict — all untouched.
- **What survives, confirmed stronger than before:** round86/E18's
  Relaxation Map item "broaden the literature search beyond this project's
  3 currently-cited geometry references... Strominger-Hull flux-
  compactification literature" is now CLOSED (both the classical system
  itself, §1, and its natural non-complex-structure-requiring generalization,
  §3, fail for named, checked reasons) — narrowing E18's remaining Relaxation
  Map to: (a) a genuinely new 13D-parent-action derivation, or (b) the AHL
  2023 cone-construction pearl E18 already flagged, neither attempted here.

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Check whether `ι` composed with `t↔1-t` is a genuine symmetry of `D_{S3,t}` or the full action | Reuses E14's own script infrastructure (`e14_z2_left_right_symmetry.py`); a concrete, cheap next test (§4's Pearl falsifiable prediction) — NOT attempted here |
| Directly read Strominger 1986's own primary text (currently blocked by ScienceDirect 403) | Would require an alternate access route (library, ILL, or a citing paper that reproduces its exact equations) — not attempted; current confirmation rests on 2 independent secondary sources, honestly flagged as such |
| Independently re-verify the `Γ^(-)=Γ+1/2H` (left-mover) half of the `(1,1)` `∇^±` pair by direct extraction (currently `[WEAK]`, WebSearch-summary-only for this specific half) | Fetch and extract Curtright-Zachos 1984 (*Phys. Rev. Lett.* 53, 1799) or Braaten-Curtright-Zachos 1985 (*Ann. Phys.* 162, 49) directly — not attempted this round, flagged honestly as the weakest-sourced sub-claim in §3b |
| Pursue candidate 3 (flux sign-selection) directly | Unchanged from E11/E18/E19's own Relaxation Maps: still no explicit `q↔(2t-1)` normalization built anywhere in this project |

## Assumptions carried, unresolved

- `SU(2)_L`=left-translation vs its mirror (`CONVENTION_TABLE.md` row 6) —
  not resolved by anything in this round; the WZW-orientifold literature's
  own `L`/`R`-invariant-vielbein-built `J±`/current conventions (round87
  §3) are a parallel, independently unresolved labeling ambiguity, not
  cross-usable to resolve this project's own version.
- `t=1`'s existence only under `c0=-2` (`CONVENTION_TABLE.md` row 5) —
  carried forward unchanged, untouched by this round.
- The `Γ^(-)=Γ+1/2H` half of the `(1,1)` `∇^±` pair (§3b) — confirmed only
  at `[WEAK]` (WebSearch-summary) confidence this round, not independently
  extracted from a primary source; flagged in the Relaxation Map above as
  the cheapest concrete follow-up if ever needed (though §3c already makes
  the broader sub-question B answer moot regardless of this specific gap).
- Whether `ι` combined with `t↔1-t` is a genuine symmetry (§4's Pearl) —
  explicitly NOT checked this round; flagged as the most concrete open item.

## What this does NOT mean

1. Does **not** prove no Strominger-Hull/WZW/`(1,1)`-sigma-model-derived
   mechanism can EVER apply to this project's compactification in any form —
   only that the SPECIFIC constructions checked this round (classical
   Strominger-Hull system, WZW-level unitarity bound, base-`(1,1)`
   sigma-model-with-torsion `∇^±` pair) fail for the two stated, checked
   reasons (orientation-relativity for A; worldsheet-vs-spacetime chirality
   for B).
2. Does **not** reopen or re-verdict round86 (E18)'s `BLOCKED` finding or
   round87 (E19)'s `FAIL` finding — both stand exactly as left.
3. Does **not** affect this project's `N_gen=3` headline claim
   (`activeContext.md`, `reports/PROJECT_360_ROUND3_SYNTHESIS.md`) — this
   round concerns only the S3-side torsion-escape-route program.
4. Does **not** claim Strominger 1986's own primary text was read this round
   — it was not (ScienceDirect 403, confirmed); the dimension/structure
   requirement rests on two independent secondary sources instead, honestly
   marked `[VERIFIED-tool]` (Fiset thesis, directly extracted and quoted) and
   `[WEAK]` (WebSearch summary of a modern paper cluster) respectively — NOT
   both `[VERIFIED-tool]`.
5. Does **not** claim the `Γ^(-)=Γ+1/2H` half of the base-`(1,1)` `∇^±` pair
   was independently, directly extracted this round — it rests on the
   `(1,0)→(1,1)` "standard embedding" logic (`[VERIFIED-tool]`, Fiset thesis)
   plus a `[WEAK]` WebSearch-summarized confirmation of the specific sign for
   ONE chirality; the opposite-sign half for the OTHER chirality is inferred
   by the standard construction logic, not independently re-derived from a
   primary source read directly this round.
6. Does **not** re-derive or challenge any of E1-E19's own tool-verified
   results — all reused here purely by citation.
7. Nothing in this experiment was submitted, posted, or sent anywhere
   external; this project's standing rule against arXiv submission and
   against contacting Tom Lawrence is unaffected and was not approached.

## Check (reproduces this decision)

This is a literature-search-and-classification round; there is no new
numerical script (per this project's own precedent, round86/round87). The
"check" is: (1) every PDF cited above (`fiset_gstructures.pdf`,
`hull_geometry_sigma.pdf`, `wzw_lectures.pdf`, `wzw_orientifolds.pdf`) was
downloaded via `curl`/`WebFetch` and extracted via `pdftotext -layout` this
round, confirmed by file size and line count in the scratchpad directory
(`fiset_gstructures.txt`: 6047 lines; `hull_geometry_sigma.txt`: 393 lines;
`wzw_lectures.txt`: 2548 lines; `wzw_orientifolds.txt`: 1986 lines); (2)
every exact quote above reproduces text found via direct `grep`/`sed` at the
cited line range in that extraction, not from memory or from a WebSearch
summary alone (WebSearch-only claims are explicitly marked `[WEAK]`
throughout, never presented as `[VERIFIED-tool]`); (3) the ScienceDirect
HTTP 403 for Strominger 1986 itself was directly observed this round via
`WebFetch`, not assumed; (4) every internal project citation (E11, E14/
round80, E18/round86, E19/round87, `CONVENTION_TABLE.md`) was reused by
direct `Read` of the cited file this round, at the start of this experiment,
not from memory.
