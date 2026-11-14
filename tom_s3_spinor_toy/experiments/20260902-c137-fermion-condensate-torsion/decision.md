# C137 — Decision (convergent-mode, FL Full-Ladder)

**Date:** 2026-09-02
**Experiment:** `20260902-c137-fermion-condensate-torsion`
**Question type (EstimandOps L0):** Descriptive — existence of a *dynamically
derived* (not postulated) condensate solution.
**Script:** `c137_condensate_structure_check.py` · **Results:** `results_c137.json`
**Skeptic record:** §12 below.

> **Revision note.** This file was substantially rewritten after an FL Step 8a
> context-blind skeptic pass returned `WEAKENED`. Every finding it raised was
> independently re-verified with my own tools before being accepted; **all were
> real.** The verdict direction (`REJECT`) is unchanged and was confirmed by the
> pass. What changed: the **leading reason was wrong** and is replaced (§3f);
> **three of five claimed novelties are withdrawn** (N2, N3, and N5's
> significance); the §5a "measured, not argued" claim is **retracted** and its
> proposed pearl **withdrawn**; an **undisclosed `1/ρ₃` insertion** is now
> derived and flagged (§5c); the check accounting is corrected; and `L5`'s own
> conditionality is now carried. Full disposition: §12.

## Verdict

```text
REJECT__NO_DYNAMICALLY_DERIVED_CONDENSATE_IS_AVAILABLE_IN_THIS_PROJECTS_FROZEN_CONTENT
  __PEARL_ROW_32_BAR_FAILS_IN_TRANSFER__THE_STANDARD_DERIVATION_EXISTS_BUT_CANNOT_RUN_HERE
  __NO_SUSY_NO_GAUGE_MULTIPLET_NO_CONFINING_SECTOR__G97_CLOSES_THE_SU4_REALIZATION
  __TWO_BODY_READ_PRIMARIES_STATE_THAT_THEY_ASSUME_THE_CONDENSATE_RATHER_THAN_DERIVING_IT
  __MPZ_VERBATIM_WE_SIMPLY_WORK_IN_AN_EFFECTIVE_APPROACH_WHERE_WE_ASK_WHAT_WOULD_HAPPEN_IF_SUCH_CONDENSATES_WERE_GENERATED
  __GEMMER_LECHTENFELD_VERBATIM_WE_WILL_REPLACE_ALL_TERMS_DEPENDING_ON_FERMION_BILINEARS_BY_THEIR_QUANTUM_EXPECTATION_VALUES
  __BAR_a_IS_NOT_A_FREE_CHOICE_INSIDE_MINIMAL_COUPLING__REPRODUCTION_OF_PEARL_ROW_145_NOT_A_NEW_MEASUREMENT
  __BAR_b_UNMET_ON_THE_CERTIFIED_ZERO_MODE_SECTOR__J_NONZERO_REQUIRES_BOTH_4D_CHIRALITIES_PAIRED_BY_THE_DIRAC_ADJOINT
  __BAR_b_IS_CONDITIONAL_ON_L4B_RANK_1_WHOSE_EXTERNAL_REVIEW_IS_OUTSTANDING__AND_DOES_NOT_COVER_THE_MASSIVE_KK_TOWER
  __MAJORANA_ESCAPE_CLOSED__NO_MAJORANA_IN_Cl_1_12_BBSTAR_MINUS_1_QUATERNIONIC__NEGATIVE_BRANCH_CLOSED_BY_CENTRAL_PARITY_NOT_BY_SEARCH_FAILURE
  __BAR_c_UNMET__MAGNITUDE_HAS_NO_INDEPENDENT_SOURCE__THE_LAMBDA_RHO3_SHARPENING_IS_WITHDRAWN_AS_A_STRENGTHENING
  __SIGN_ALSO_UNDETERMINED__RESTATEMENT_OF_C134_5d__P3_RELOCATES_THE_t_QUESTION_INTO_A_CONDENSATE_PHASE_QUESTION
  __STRONGEST_ORIGINAL_CONTENT_IS_CANDIDATE_D_CIRCULARITY__THE_TORSION_INDUCED_FOUR_FERMION_TERM_IS_THE_TORSION_EOM_SUBSTITUTED_BACK
  __THREE_SELF_CAUGHT_AND_TEN_SKEPTIC_CAUGHT_DEFECTS_DIAGNOSED_NOT_TUNED_AWAY
```

**One line:** `P3` fails **in transfer**, at a different joint from rounds
87/88: the standard dynamical derivation of a gaugino condensate
(`⟨λλ⟩ ~ Λ³` by dimensional transmutation in a confining `N=1` sector) is real
and exists in the literature — it simply **cannot run here**, because this
project has no supersymmetry, no gauge multiplet and no confining sector; and
the four retrieved papers that *do* work on nearly-Kähler cosets take the
condensate as a **free input** rather than deriving it, so they supply no
substitute route either.

**This is the permitted outcome `claim.md` names in advance**, not a failure of
the round.

---

## 1. The bar, quoted exactly

### 1a. `pearl_registry/INDEX.md` row 32 — and a disambiguation it needs

**Disambiguation first, because "row 32" is ambiguous in that file.** Counting
table rows, row 32 is at file line 38 (Round 65, Killing-spinor). Counting file
lines, line 32 is the Tejinder P. Singh entry. `claim.md`'s description matches
the **file-line-32** entry, and C132's own `P3` section quotes that entry's
sentence verbatim (`C132 decision.md:376-379`), so **file line 32 is what is
meant** and is what this round is scored against. `[VERIFIED-tool, both files
read this session]`

Verbatim, the two load-bearing clauses (`pearl_registry/INDEX.md:32`):

> "A genuinely THIRD, structurally distinct mechanism-type, less circular than
> Furey-Hughes: … Differentiation comes from genuine spontaneous symmetry
> breaking (vacuum selects/freezes one of 7 octonionic imaginary directions per
> E6 factor), **backed by an actual Coleman-Weinberg effective-potential
> calculation, not a bare assertion.**"

> "…establishes 'vacuum selection + effective-potential derivation' as a genuine
> third mechanism-type … **If a future L3b proposal invokes spontaneous vacuum
> selection, check for an analogous dynamical derivation of WHY that direction
> is selected, not just an assertion**"

**Scope correction, flagged not absorbed (skeptic-anticipating, and exactly the
C135 failure mode of an unflagged narrowing).** `claim.md` says row 32 "names
the fermion-condensate mechanism as a genuinely third mechanism-type." It does
not. Row 32 names *vacuum selection backed by an effective-potential
calculation* as the third mechanism-type, and its literal `trigger_condition` is
an **L3b** (third-triality-channel) proposal, not a torsion-selection proposal.
Applying it to `P3` is an application of its **substance** by analogy — which
C132 did explicitly and this round accepts — but the analogy is a choice this
round is making, not something row 32 states. Nothing below depends on reading
row 32 more broadly than its own words support: the bar used here is exactly
*"an actual dynamical derivation of why that direction is selected, not a bare
assertion."*

### 1b. C134's three-part addendum — verbatim

`experiments/20260902-c134-ecsk-torsion-auxiliary/decision.md:440-443`,
under "What this round does NOT kill" `[VERIFIED-tool, read in full]`:

> "**`P3`** (fermion condensate sourcing torsion). This round **redirects into
> `P3`** and **raises its bar**: `P3` must now supply a *4D-pseudoscalar*
> condensate, reconcile it with 4D chirality (route 2), and explain the
> fine-tuning (route 3) — on top of `pearl_registry` row 32's existing bar."

Call these **(a)** pseudoscalar, **(b)** chirality reconciliation, **(c)**
fine-tuning. All four bars (row 32 + a + b + c) are scored in §5.

---

## 2. Zero-Signal Gate (FL Step −5) — run before any computation

| field | content |
|---|---|
| Entity | a fermion bilinear condensate `⟨χ̄Γ_{abc}χ⟩` on the frozen `M₄×S³×S⁶`, with `χ` **named** — four candidate identifications are enumerated in §4 and each is scored separately, so the entity is not left as "some field" |
| Falsifiable predicate | that condensate arises from an actual dynamical mechanism available in this project's frozen content (a derived vacuum condition, a minimisation, a symmetry-breaking pattern of this geometry) |
| Measurable outcome | either an explicit derivation, or a stated, sourced finding that none exists and the condensate must be postulated |

All three fillable ⇒ **gate PASSES** (not `REFUSE`). The measurable outcome
realised is the second branch, and it is realised from **primary sources read
this session**, not from absence of evidence — see §3.

---

## 3. Literature, with the Mechanism-Transfer-Gate applied to every source

`claim.md` requires stating, per source, whether what is imported is the
transferable algebraic relation or the non-transferable heterotic packaging.
Done below. **Both C132 sources that were only abstract-read there have now been
read in body text this session** `[VERIFIED-tool: arXiv HTML retrieved and
searched, quotes reproduce text at the cited offsets]`.

### 3a. Manousselis–Prezas–Zoupanos, `arXiv:hep-th/0511122`

**What is transferable — the algebraic relation, and it is confirmed:**
`Σ_{MNP} = (1/16) tr(χ̄Γ_{MNP}χ)` sources the supercovariant `Ĥ`. Generic,
not string-specific. **Imported.**

**What is NOT transferable, and is decisive here — verbatim:**

> "here we simply work in an effective approach where we ask what would happen
> **if** such condensates were generated. Hence, our treatment is entirely
> analogous to the usual chiral Lagrangian approach to hadron physics. In this
> approach, one simply assumes that in the IR a non-vanishing quark condensate
> breaking chiral symmetry is formed, although the microscopic theory (i.e. QCD)
> governing this effect is out of reach in this regime."

and

> "the only extra assumption is that some unknown quantum effects can lead to
> non-trivial condensates"

**This is the paper telling us, in its own words, that it does not do what pearl
row 32 asks for.** There is no effective-potential derivation of the condensate;
it is an assumed IR input. `[CITED, primary, body text]`

**A second, independent transfer obstruction visible in the same paper.** Its
4D condensate is

> `Σ_{mnp} = −(Λ³ Ω_{mnp} + c.c.)`, with `Λ³ = ψ†₋ψ₊` "the 4-dimensional
> condensate"

— `ψ†₋ψ₊` pairs **opposite 4D chiralities**. That is C134's route-2 structure,
appearing independently in the primary literature: an all-internal 3-form
condensate in a 4D compactification *is* a 4D-chirality-off-diagonal object.
MPZ can have it non-zero because their 10D Majorana–Weyl gaugino decomposes as
`χ = ψ₊⊗η₊ − ψ₋⊗η₋`, i.e. **carries both 4D chiralities**. That decomposition —
not the algebraic relation — is the ingredient this project lacks (§5b).

### 3b. Gemmer–Lechtenfeld, `arXiv:1308.1955`

The closest source to this project's situation, because its solutions are
**non-supersymmetric** ("none of the solutions … is supersymmetric"), and this
project has no supersymmetry.

**Transferable:** the bilinears `Σ`, `Δ` and the field equations' *shape*.

**Not transferable, verbatim:**

> "From now on, we will **replace all terms depending on fermion bilinears by
> their quantum expectation values.** Furthermore, we assume that the only
> non-vanishing expectation values are `Σ` and `Δ`."

and, from the summary:

> "the radius of the de Sitter or anti-de Sitter space is **not fixed but
> related to the amplitudes of the condensates** and `H`-flux by the equations
> of motion."

**The logical direction is the reverse of what `P3` needs.** The condensate
amplitudes are free inputs; the *geometry* is the output. `P3` needs a derived
condensate whose output is `t ∈ {0,1}`. `[CITED, primary, body text]`

**One genuinely useful structural remark from this paper**, cross-confirming
C134's kill mechanism from an independent direction: in a **3D** spacetime a
purely internal condensate is impossible, "due to the fact that
`Γ⁰Γ¹Γ² = −1`", whereas "in [the 4D] case one may consistently confine the
condensate to the compactification space." The obstruction is the *4D volume
element*: in 4D it is `γ₅`, so an internal 3-form condensate survives only as a
4D **pseudoscalar**. Same algebra as C134 route 2, arrived at independently.

### 3c. Cardoso–Curio–Dall'Agata–Lüst, `arXiv:hep-th/0310021` (abstract only)

> "H-fluxes, which deform the geometry of the internal manifold, and a gaugino
> condensate which breaks supersymmetry. We focus on the **compensation of the
> two effects** in order to obtain vacua with zero cosmological constant"

Transferable: nothing beyond the shared algebraic relation. Not transferable:
the whole construction is an explicit **compensation** (tuning) between two free
inputs — the shape of C134 route 3's fine-tuning, not its resolution.
`[CITED, abstract only — not body-read this session, flagged]`

### 3d. Frey–Lippert, `arXiv:hep-th/0507202` (abstract only)

> "for **a particular combination of fluxes and condensate**, [the internal
> geometry] is nearly Kähler" … "we point out **subtleties in deriving the
> effective superpotential and understanding the heterotic supergravity in the
> presence of a gaugino condensate**."

Same verdict as 3c, plus the authors' own flag that the derivation side is
unsettled. `[CITED, abstract only, flagged]`

### 3e. Not repeating the round87/round88 error

Rounds 87/88 failed by *formula match without mechanism transfer* — GHR/WZW's
`∇^± = ∇^{LC} ± ½H` matched this project's `∇^t` exactly, and the "why both
signs" reason turned out to be 2D **worldsheet** chirality, which this project
does not have `[VERIFIED-tool, both decision.md read in full this session]`.

The error this round could have repeated: reading `Σ = (1/16)tr(χ̄Γχ)` as
evidence that "a condensate sources torsion here too". The algebraic relation is
real and importable — but it is an *identity about spin currents*, not a
mechanism, and it is **already in this project** via C134's own derived torsion
EOM, so importing it buys nothing. No formula-matching step is performed below.

### 3f. **Correction to this round's own first draft** — the failure IS a transfer failure

`[This section replaces a claim the first draft made and the FL Step 8a skeptic
pass falsified. Recorded rather than silently edited.]`

The first draft's headline read: *"there is no dynamical derivation at the source
to transfer"*, and claimed this put `P3` **one step earlier** in the chain than
rounds 87/88. **That is wrong, and the document contradicted itself about it** —
§5e simultaneously asserted that in heterotic gaugino condensation the
condensate's phase *is* dynamically fixed by R-symmetry breaking, which presumes
the very mechanism §3 denied existed.

**The correct statement.** Gaugino condensation **does** have a standard
dynamical derivation: in a confining `N=1` hidden sector,
`⟨λλ⟩ ~ Λ³` with `Λ = M·exp(−8π²/(b g²))` — dimensional transmutation, the
Veneziano–Yankielowicz effective superpotential and holomorphy/instanton methods.
That is precisely the "actual dynamical derivation of magnitude" pearl row 32
asks for, and it exists — it is simply **not in these four papers**, which work
in an effective/parameterised regime instead (§3a, §3b).

So the honest finding is:

* **the mechanism exists**, and it needs `N=1` SUSY, a gauge multiplet, and a
  confining hidden group to run;
* **this project has none of the three** (§4 candidate B), so the derivation
  cannot be instantiated here;
* **and the four papers nearest this project's geometry do not offer a
  substitute route**, because they parameterise rather than derive.

That is the **round87/88 shape** — a real mechanism that does not transfer —
at a different joint (missing gauge/SUSY sector rather than missing worldsheet).
It is a `REJECT` either way; what is withdrawn is the claim that this round found
a *stronger and different kind* of failure than rounds 87/88 did.

**Consequently corrected elsewhere:** the verdict block no longer says "all four
primaries in their own words" (two are abstract-only, §3c/§3d), and novelty claim
N1 is downgraded in the evidence tier.

---

## 4. What could `χ` be? Four candidates, each scored on AOG-5

`claim.md`'s Zero-Signal entity requires naming the field. Enumerated:

| # | candidate `χ` | what it needs | status |
|---|---|---|---|
| **A** | the certified KK zero modes themselves (the project's own `ψ`) | nothing new | **DEAD on bar (b)** — `J = 0` identically, §5b. Not "small": an exact operator identity. |
| **B** | a hidden-sector **gaugino** (the literal heterotic import) | an `N=1` gauge multiplet, a confining hidden gauge group, a condensation scale | **DEAD on AOG-5, and this is the round's load-bearing ground.** This project has no supersymmetry and no gauge multiplet; `SPIN13_TO_SPIN4_DECOMPOSITION.md` states no 13D parent theory is claimed, and gate G97 (rounds 102/108/109) closes the standard product-manifold `SU(4)` realisation three independent ways. Corroborating (not decisive) in-repo remark, verbatim `[VERIFIED-tool, RESEARCH_STATUS_REPORT.md:173, 439]`: *"Non-perturbative origin (brane instantons, gaugino condensation) is **outside the scope of this geometric framework**"*; *"both requiring a **UV completion beyond the geometric framework studied here**."* **Scope caveat the first draft omitted (skeptic-caught):** that passage sits in the **λ-origin** section and is about non-perturbative origins of `exp(−λ/ρ₆²)`, not about whether a gaugino sector exists here. It is a scoping note on a neighbouring question, so it is corroboration, not the "decisive in-repo statement" the first draft called it. The AOG-5 point stands on its own without it. |
| **C** | a new vector-like Dirac fermion supplying the missing opposite-chirality partner | new field content | **DEAD on AOG-5** — added for no reason except that it would make `J ≠ 0`. Its condensation scale is then also free, so bar (c) worsens rather than improves. |
| **D** | the certified modes condensing via the **torsion-induced four-fermion interaction** — the only interaction this project actually derives | nothing new; C134 §3 derives `L* = −(3κ/16) A·A` | **the strongest internal candidate, and still DEAD.** Three independent reasons: (i) the pseudoscalar channel operator is the *same* one that vanishes identically on 4D-chiral content (§5b) — condensing a channel whose operator is zero is not possible; (ii) the coupling is `κ₁₃`, i.e. gravitational strength, so NJL-type criticality needs a cutoff at the 13D Planck scale, where the effective description that produced the equation no longer holds; (iii) it is **circular as a selection mechanism** — that four-fermion term *is* the torsion EOM substituted back in, so "the condensate sources the torsion" and "the torsion generated the interaction that made the condensate" are the same equation, not two. |

No fifth candidate was found. **Honest scope statement:** this is an enumeration
over what the project's frozen content and the retrieved literature suggest, not
a proof of exhaustiveness.

---

## 5. Scoring the four bars

### 5a. Bar (a) — "must be a genuine 4D pseudoscalar": **not a free choice, but this is a REPRODUCTION of row 145, not a new result** `[VERIFIED-tool, with a retraction]`

**Retraction first.** The first draft claimed this section "measured, not
argued" a result that "upgrades C134's pearl (registry row 145) from a
`γ₅`-parity argument to a measurement, and extends it from the `S³` leg to every
internal leg." **Both halves are false and are withdrawn**, together with the
`pearl_registry` entry the first draft proposed for them:

* Row 145 already states the result for *"the torsion component with **all three
  legs internal**"* in *"**any** Kaluza-Klein Einstein-Cartan setup with
  `M₄ ×` (internal manifold)"*, gives the `γ₅`-parity argument itself, and was
  *"verified **representation-independent** across 40 basis changes"*
  `[VERIFIED-tool, pearl_registry/INDEX.md:145 re-read]`. Nothing is extended,
  and a single-representation run is **weaker**, not stronger, than what row 145
  already carries. C134 §4 also already swept the same 84 components.
* The "measurement" does not measure what the first draft said. `[S2.8]`
  **demonstrates this by construction**: replacing the internal gammas with
  **random non-Clifford matrices** returns the *identical* pure-`γ₅`
  decomposition. Every internal gamma is `i·γ₅ ⊗ (·)` by the embedding, so
  `S2.3–S2.7` are forced by that embedding and would pass for any input. They are
  reproductions; the script now labels them so, and `S2.8` exists to stop the
  distinction being lost again.

**What is actually established here, and it is enough for bar (a):**

* `γ₅` is the **unique** element of the 16-element `Cl(1,3)` basis that
  anticommutes with all four `γ^μ`. `[S2.0]` Since those 16 span `End(ℂ⁴)`, any
  operator anticommuting with all four `Γ^μ = γ^μ⊗1` lies in `γ₅ ⊗ End(internal)`.
  **This**, not the embedding, is why every internal gamma carries exactly one
  `γ₅` — it is a statement about `Cl(1,3)` given the KK product ansatz, and it is
  the same argument row 145 states.
* `Γ^aΓ^bΓ^c = sign(abc)·Ω₃` for all six orderings of the `S³` legs — the
  `ε_{abc}` structure, obtained from **anticommutativity**, with a non-Clifford
  negative control that genuinely fails it. `[S2.1, S2.2]` *(The first draft's
  version of this was degenerate: its six list entries were the identical matrix,
  so "rank 1 over 6 orderings" was a property of the loop, not of the algebra.
  Skeptic-caught, re-verified by me, replaced.)*

**Bar (a) verdict, unchanged in substance:** within the minimal Dirac spin
current the 4D structure is forced to be pseudoscalar, so bar (a) cannot be met
by choosing a different structure. Escaping it requires leaving minimal coupling
— C134's V2 (non-minimal Freidel–Minic–Takeuchi `α` / Holst–Immirzi `γ`),
already registered as `pearl_registry` row 146 and **a different candidate, not
`P3`**. **The credit for this belongs to C134/row 145, not to this round.**

### 5b. Bar (b) — chirality reconciliation: **unmet on the certified zero-mode sector, conditional on L4B** `[VERIFIED-tool, with two named scope conditions]`

Reconfirmed independently of C134's script (different Clifford construction,
built from `Cl(9,0)` with the `S³` legs first):

* `P_L Γ⁰ Ω₃ P_L = P_R Γ⁰ Ω₃ P_R = 0` **exactly** (deviation `0.00e+00`), while
  `P_L Γ⁰ Ω₃ P_R ≠ 0` (`0.500`), so the vanishing is not trivial. `[S3.1–S3.3]`
  A harness control confirms the projector sandwich *can* be non-zero. `[S3.4]`

**The positive form.** Writing the 4D part as `ψ₄ = a·u_L + b·u_R` and fitting
`J` over 200 random `(a,b)`: purely left-handed → `|J| = 5e−17`; purely
right-handed → `|J| = 5e−18`; both chiralities → `|J| = 1.2277`, with **no**
`|a|²` or `|b|²` component (diagonal weight `5e−16` vs off-diagonal `1.2277`).
`[S3.6–S3.9]`

**Status of that scan, corrected:** `S3.6–S3.9` are **corollaries of the operator
identity above, not independent evidence** — once `P_LΓ⁰Ω₃P_L = 0` holds as a
64×64 matrix identity, every one of those numbers follows, and the fit residual
is guaranteed by construction (it is no longer part of the pass condition).
Their value is illustrative. The skeptic pass attacked the "only if" direction
directly — non-factorised spinors, other `S³` doublet components, superpositions
across `S⁶` channels — and **found no falsifier**, correctly, because the
identity is an operator statement that holds for arbitrary 13D spinors.

So: **`J ≠ 0` if and only if the 4D content contains both chiralities paired by
the Dirac adjoint.** `L5`/`G74B` certify the opposite for the zero-mode sector —
`preprint.tex:899-901`, verbatim: *"with the verified `dim ker(D⁻)=0` … all three
zero modes are in `D⁺` — they are **left-handed**"* `[VERIFIED-tool]`.

**Two scope conditions this must carry, and the first draft did not:**

1. **`L5`'s own conditionality.** `preprint.tex:892` states L5 as *"unconditional
   net asymmetry; **full statement under the certified L4B rank**"*, and the
   "all three purely left-handed" half rests on `dim ker(D⁺|₁)=1` whose own
   parenthetical reads *"**external review outstanding**"*. The paper itself
   names the excluded contingency: rank 0 *"would have given a subdominant
   right-handed partner (`dim ker(D⁻)=1`) alongside two left-handed modes"*
   `[VERIFIED-tool]`. **If that contingency were realised, the certified sector
   would carry both chiralities and `J` need not vanish.** Bar (b)'s failure is
   therefore `[VERIFIED-tool]` *conditional on L4B rank = 1*, not unconditional,
   and the phrase "a certified chirality fact" is corrected accordingly.
2. **Zero modes are not the whole field.** The identity kills `J` on the
   **certified zero-mode sector**. The massive KK tower is 4D-Dirac and is not
   covered — see W4 in §8, honestly listed as not attempted.

**The Majorana escape, closed twice independently.** A single 4D Weyl field
*does* have a non-vanishing transpose-type bilinear `ψᵀCγ₅ψ`, so the natural
escape is `ψ̄ = ψᵀC`, i.e. a Majorana condition. Two independent closures:

1. **Algebra level, computed here.** For the conjugation intertwiner
   `B Γ^A B⁻¹ = ε(Γ^A)*` in `Cl(1,12)`: the `ε = +1` branch exists with
   `B B* = −1` (**quaternionic**), and the `ε = −1` branch does not exist —
   **no Majorana condition in 13D Lorentzian.** `[S4.1–S4.3]` Positive control:
   the same routine finds a genuine Majorana intertwiner (`B B* = +1`) in
   `Cl(1,3)`. `[S4.1]`
   **Rigour repair (skeptic-caught).** The `ε = −1` branch is the load-bearing
   one, and the first draft's justification did not cover it: `B` is
   *constructed* (as an ordered product of generators) and then verified, so
   Schur uniqueness applies only where a candidate **worked** — "my two
   candidates failed" is not "none exists", and a broken solver would have
   passed the check. Now closed independently, by central parity: `ω = Γ⁰…Γ¹²`
   is a scalar (`−1`), preserved under `Γ → +Γ*` but **flipped** under
   `Γ → −Γ*`; the two inequivalent `Cl(1,12)` irreps are distinguished exactly
   by that sign, so the `ε = −1` image is the *other* irrep and no intertwiner
   can exist, for any construction. `[S4.4]`
   Cross-check against the standard reality table: `13 mod 8 = 5`, the
   symplectic-Majorana/quaternionic regime — exactly the measured `−1`. What
   `Cl(1,12)` admits instead is symplectic Majorana, requiring an **even number**
   of spinors, i.e. doubled field content — new content again, AOG-5 (see W3).
2. **Zero-mode level, already in-repo.** C33 (2026-08-10), quoted from
   `OPEN_BLOCKERS.md:1549-1553` `[VERIFIED-tool]`: *"restricting to the zero mode
   collapses the `S⁶` factor to a **scalar**, which cannot supply the second
   minus sign. The induced structure is quaternionic again → **no Majorana
   condition on the zero mode, solution dimension 0**."*

**Honest narrowing of "two independent routes" (skeptic-caught).** They are not
symmetric. C33's own record notes that a Majorana structure *does* exist on the
16-dimensional internal **module** and that only the *zero-mode restriction* is
quaternionic; C137's `S4` works on the full 13D Lorentzian spinor. The two agree
on the conclusion relevant here but describe different objects — "same answer" is
accurate, "two independent proofs of the same statement" would not be.

**Bar (b) is unmet** — an exact operator identity, plus a chirality fact that is
certified *conditional on L4B rank = 1*, plus a closed escape.

### 5c. Bar (c) — the magnitude: **unmet; the first draft's "sharpening" is WITHDRAWN** `[VERIFIED-tool for the algebra; the sharpening was [SPECULATIVE] and is retracted]`

**Disclosure the first draft omitted.** C125 §2a's normalisation is
`T^t(X_i,X_j) = 2(2t−1)ε_{ijk}X_k` — **at unit radius, with no `ρ₃`**
`[VERIFIED-tool, C125 decision.md:385]`. C134 §6 assumption 4 says so explicitly
and warns against exactly the step the first draft took: *"Route 3's
`|κ₁₃J| = 4` is a **unit-radius statement, not a `ρ₃` one**"* — and records that
C125's own second skeptic pass **downgraded that normalisation to `[INFERRED]`**
`[VERIFIED-tool, C134 decision.md:366-369]`. The first draft inserted a `1/ρ₃`,
did not flag it, and re-marked the normalisation `[CITED]`, dropping C134's
downgrade.

**Repaired: the `ρ₃` is now this round's own derived step, marked as such.** On
`S³` of radius `ρ₃` the metric scales by `ρ₃²`, so the orthonormal frame is
`e_i = X_i/ρ₃` and `[e_i,e_j] = (2/ρ₃)ε_{ijk}e_k`, giving all-frame-index
`T_{abc} = 2(2t−1)/ρ₃ · ε_{abc}`. Verified as a **scaling law** across four radii
against a wrong-exponent (`1/ρ₃²`) negative control `[S5.1]`. It carries C125's
`[INFERRED]` marker forward, plus this round's own derivation on top. Then

```
2(2t−1)/ρ₃ = (κ₁₃/2)·J      ⇒      t ∈ {0,1}  ⟺  |κ₁₃ J| ρ₃ = 4
```

with an off-point control confirming other `t` give other values, so the relation
constrains `J` rather than being an identity `[S5.2]`.

**The withdrawn sharpening.** The first draft argued that NJL criticality of the
`κ₁₃` four-fermion coupling turns this into `Λ·ρ₃ ≈ 4`, "a required coincidence
between two independently-determined scales", and listed it as novelty N5.
**Withdrawn, for three reasons the skeptic pass raised and I confirmed:**

1. **Internal contradiction.** §4 candidate D rules NJL criticality *out of
   bounds* — the criticality scale is trans-Planckian, where the effective
   description that produced the equation fails. §5c then used that same
   criticality as its sole premise. An assumption declared invalid one section
   earlier cannot carry a headline one section later.
2. **It runs the wrong way.** `Λ·ρ₃ ≈ 4` says the `S³` radius is a few
   fundamental lengths — the *generic* expectation in a KK compactification, not
   a tuning. As "sharpened", bar (c) became **weaker**, not stronger.
3. **Its own premise is conceded.** The paragraph admitted `ρ₃`/`ρ₆` are fixed
   "to the extent they are"; if they are not independently fixed, there is no
   coincidence to require.
4. **The old supporting checks did not support it.** Old `S5.1` computed
   `−(D−2)+(D−1)`, which is `1` for **every** `D` and cannot fail; old `S5.4`
   recomputed the identical expression; old `S5.3` compared `|4·(±1)|` to `4`.
   All three are removed or demoted to recorded data.

**What survives, and it is sufficient:** the condensate magnitude required for
`t ∈ {0,1}` has **no independent source anywhere in this project** — no
condensation scale is defined, and candidates B/C/D each fail to supply one for
their own separate reasons (§4). That is C134 route 3's finding, applied to `P3`,
**not strengthened by this round**.

### 5d. Bar row 32 — dynamical motivation: **unmet, in transfer** `[CITED; corrected, see §3f]`

Row 32 asks for "an actual dynamical derivation of WHY that direction is
selected, not just an assertion", with Singh's Coleman–Weinberg calculation as
the exemplar.

* **The analogue exists in the field** — gaugino condensation by dimensional
  transmutation in a confining `N=1` sector (§3f). The first draft's claim that
  it does not is retracted.
* **It cannot be instantiated here**, because its three ingredients (SUSY, a
  gauge multiplet, a confining hidden group) are all absent — §4 candidate B.
* **The four papers closest to this project's geometry offer no substitute**:
  two say in body text that they assume the condensate (§3a, §3b); two are
  abstract-only and describe explicit flux/condensate *compensation*, i.e.
  tuning, not derivation (§3c, §3d).

**Bar row 32 is unmet** — not because no derivation exists in physics, but
because none is available to this project's frozen content.

### 5e. A fifth failure, inherited: the **sign** is not selected either

`[RESTATEMENT of C134 §5d, flagged as such per round114's own criterion]` The
absolute sign of `2t−1` is the sign of the 4D pseudoscalar condensate; `L5` fixes
only a *relative correlation*. Confirmed here independently: flipping the `S⁶`
chirality flips `J` exactly (`+1.2277 → −1.2277`) `[S3.10]`, and `J` depends on
the L–R overlap through its **imaginary part** — `J(a=1,b=1) = 0` while
`J(a=1,b=i) = 1.2277` `[S3.8]`. So `J`'s sign is the sign of a condensate
**phase**.

**Consequence for `P3` specifically (this part is not a restatement):** even a
fully successful `P3` would replace "why `t=0` and not `t=1`?" with "why this
condensate phase and not the opposite?" — an equally unfixed `Z₂`. In heterotic
gaugino condensation that phase *is* fixed (discretely, by R-symmetry breaking
`Z_{2N}→Z₂` in an `N=1` gauge theory) — which is one more piece of
non-transferable packaging, since this project has neither the SUSY nor the
gauge theory that quantises it. **`P3` relocates the selection question; it does
not answer it.**

---

## 6. Verification

`c137_condensate_structure_check.py` — **30 check call sites, 0 failures**, plus
**22** recorded data values kept in a separate `DATA` dict and explicitly not
counted as checks. An **AST self-audit** runs at import and refuses to start if
any `check()` receives a literal constant (adopted from C134). `ruff check`
clean.

**Honest recount, forced by the skeptic pass** (the first draft said "29 boolean
checks … 10 data values", both wrong, in the section whose whole point is exact
accounting). **30 is a count of call sites, not of independent evidence.** They
partition as:

| class | which | what they are worth |
|---|---|---|
| **Independent content (≈9)** | `S1.1`–`S1.5`, `S2.0`, `S2.1`, `S3.1`–`S3.3`, `S4.1`, `S4.4`, `S5.1` | real, failable, discriminating |
| **Reproductions of row 145, forced by the embedding (7)** | `S2.3`–`S2.8` | reproduce a cited result in one representation; `S2.8` **proves they are forced** and would pass for random non-Clifford input |
| **Corollaries of an already-passed check (5)** | `S2.6` (of `S2.3`), `S3.6`, `S3.7`, `S3.9` (of `S3.1`/`S3.2`), `S4.3` (of `S4.2`) | illustrative, not additional |
| **Controls (6)** | `S1.3`, `S2.2`, `S3.4`, `S3.8`, `S4.1`, `S5.2` | genuinely discriminating; each fails on a perturbed input |
| **Removed since the first draft (3)** | old `S5.1`, `S5.3`, `S5.4` | unfailable — see §5c item 4 |

**Independent rebuild of certified project constants** (different Clifford
construction from C134's — built from `Cl(9,0)` with `S³` legs first):

| certified value | C137's independent rebuild |
|---|---|
| all 169 `Cl(1,12)` anticommutators vs `η = diag(+,−,…,−)` | ✓ worst `0.00e+00` |
| `Ω₃ = γ₅ ⊗ 1₂ ⊗ Γ₇` (C134 §5a) | ✓ dev `0.00e+00` |
| `ω₁₃` central and scalar (C125 E3) | ✓ scalar `+1.000` |
| `Ω₃·Ω₆ = ±i γ₅` (C125 D4) | ✓ **up to a convention sign** — see §7.1 |

**Limit of the Majorana computation, stated.** The intertwiner is **constructed**
(as the ordered product of the purely-real, resp. purely-imaginary, generators)
and then **verified** against the defining relation, rather than obtained from a
null-space solve — the solve requires an SVD of a `53k × 4k` matrix and was
abandoned on cost after it ran past a 120 s budget. Verification makes the
**positive** branch rigorous (once the relation holds, Schur fixes `B` up to
scale and the sign of `B B*` is scale-invariant). It does **not** make the
negative branch rigorous, which is why `S4.4`'s central-parity argument was added
— see §5b.

**What was NOT built.** No twisted `S⁶` Dirac operator (the script uses basis
vectors of the `Γ₇ = +1` eigenspace); no dynamical calculation of any kind; no
effective potential. §5d's verdict rests on **reading the sources**, not on
computing that no condensate can form — those are different claims and only the
first is made.

---

## 7. Three self-caught test-design defects — diagnosed, not tuned away

*(Read together with §12: a context-blind pass later found that this section's
own repairs were over-credited. See 7.2b.)*

Recorded because this project's own registry (rows 144, 149) treats repair
quality as a first-class risk.

**7.1 `S1.4` failed on the first run (dev `2.00e+00`).** The first draft asserted
`Ω₃Ω₆ = +i γ₅`, matching C125 D4's measured `0+1i`. This embedding gives
**`−i γ₅`**. Diagnosis: a **convention** difference — C125 works in the repo's
`Cl(0,3)` `S³` convention with its own index ordering; this script builds
`Cl(1,12)` from `Cl(9,0)` with the `S³` legs first. The convention-independent
content (a unit-modulus imaginary multiple of `γ₅`) holds exactly. The check now
tests `±i` and **records the measured sign**, because this repo has already lost
weeks to silently mismatched Clifford conventions (`pearl_registry` 2026-08-09).
**Nothing in this round's conclusions depends on that sign.**

**7.2 `S2.5` failed on the first run — and the failure produced a better
result.** The first draft's control asserted that a mixed `2×S³+1×S⁶` triple is
**not** pure-`γ₅`. That expectation was simply **wrong**: every product of an odd
number of internal gammas carries `γ₅` to an odd power, so *every* internal
3-form is 4D-pseudoscalar. The computation was right and the expectation was
wrong. The invalid control was replaced by a valid one (two-leg internal → 4D
scalar, `[S2.5]`) and the statement re-run over all 84 triples `[S2.7]`.

**7.2b — and the repair was itself over-credited.** The first draft called the
84-triple version "the round's cleanest new structural fact". The skeptic pass
showed it is neither new (row 145 already has it, stronger) nor a measurement
(`S2.8`: forced by the embedding). **This is the single most instructive thing
that happened in this round**: a defect was caught honestly, the confession was
written up, and the *repair* was then over-sold in the same paragraph — exactly
the pattern `pearl_registry` row 144 predicts. See the rewritten methodology
pearl in §11.

**7.3 `S3.10` failed on the first run** because the test point `(a,b) = (1,1)`
sits exactly on `J`'s zero locus (`J` depends on `Im(ā b)`). Bad test point, not
a bad identity; changed to `(1, i)` with the diagnosis recorded in the source.

---

## 8. Kill Analysis (Anti-Overfitting Gate)

**What this round KILLS.** `P3` as posable from this project's frozen content is
**FALSE**, under the disjunction

1. {**no field of the required kind exists here**} — no SUSY, no gauge multiplet,
   no confining sector; G97 closes the `SU(4)` realisation (§4 candidate B).
   **This is the load-bearing ground**, and it survived every skeptic finding
   untouched;
2. {**`J ≡ 0` on the certified zero-mode sector**} — the exact operator identity,
   conditional on L4B rank = 1 (§5b);
3. {**the magnitude has no independent source**} — no condensation scale is
   defined anywhere in this project (§5c);
4. {**the four retrieved papers parameterise rather than derive**}, so they offer
   no substitute route (§3a–§3d).

**Any one suffices**, and grounds 1 and 2 are independent of each other and of
every correction made in §12. Additionally: bar (a) is unmeetable by structure
choice inside minimal coupling — but credit for that belongs to C134/row 145,
not to this round (§5a).

**What this round does NOT kill.**

* **C134's V2 / `pearl_registry` row 146** — non-minimal fermion–torsion
  couplings (Freidel–Minic–Takeuchi `α`; Holst/Immirzi `γ`). §5a *narrows* it
  usefully: any escape must leave minimal coupling, because inside it the
  4D structure is forced. Untouched otherwise.
* **C134's V3** — adding a bosonic source so the background solves the metric
  EOM. Untouched; still "the most informative surviving variant" per C134.
* **`P14`, `P4`, `P5`, `P13`, `P8`** and the rest of C132's ranked list.
* The **algebraic relation** "fermion bilinear sources totally-antisymmetric
  torsion" — real, generic, already in-repo via C134's derived EOM, and
  unaffected.
* `N_gen=3`'s CONDITIONAL status, `lambda = FREE_COUPLING_PARAMETER`,
  `sm_derivation_claimed = False`, `safe_for_runtime = False`.
* Whether a condensate could exist in some *extension* of this project. This
  round is about the frozen content, as `claim.md` scopes it.

**Relaxation Map** (one assumption changed per variant; **none attempted here**):

| variant | single assumption changed | kill criterion |
|---|---|---|
| W1 | Leave minimal coupling (C134 V2) | Does a non-minimal coupling give an internal-torsion source with 4D **scalar** or **vector** structure? §5a says it must, to escape — but it then needs its own existence and magnitude argument, i.e. bars row-32 and (c) are inherited unchanged. |
| W2 | Add opposite-chirality 4D content (a mirror/vector-like sector) | Purely AOG-5: is there an independent reason for it? It must also not disturb `ind = +1` / `L5`. Currently none. |
| W3 | Symplectic-Majorana doubling of the 13D spinor | `Cl(1,12)` admits `B B* = −1` (§5b), so a doubled spinor pair **can** carry a reality condition. Does the resulting `ψ̄ = εψᵀC` bilinear reach the `Ω₃` channel non-trivially on single-chirality content? **Not computed.** Cheapest surviving variant; needs new field content, so AOG-5 applies. |
| W4 | Condensate in the **massive KK tower** rather than the zero modes | Massive modes are 4D-Dirac, so `J` is **not** identically zero there — §5b's identity does not reach them. **The first draft dismissed this by saying "a pseudoscalar VEV needs CP violation, which this project has no source for"; that dismissal is withdrawn (skeptic-caught, and it also conflated P with CP): the object under test, `T^t = 2(2t−1)ε` for `t ≠ 1/2`, is itself a parity-odd background, so the ansatz supplies exactly the P-violation the dismissal claimed was absent.** This makes W4 the **most live** surviving variant, and notably the only one that needs **no new field content** and therefore does **not** inherit AOG-5. What it does inherit unchanged: bars row-32 and (c) — a massive-tower condensate still needs a derivation and a magnitude. Not attempted. |

---

## 9. Gate fields (`PARENT_ACTION_GATE.md`)

| field | status after C137 |
|---|---|
| **F4 — `t`-selection** | **FAILS.** Add to C132 §1c's "already tried" table: *fermion-condensate-sourced torsion (`P3`) — the standard gaugino-condensation derivation cannot run here (no SUSY, no gauge multiplet, no confining sector; G97); the source bilinear vanishes identically on the certified zero-mode sector (conditional on L4B rank = 1); the required magnitude has no independent source; the four retrieved nearly-Kähler-coset papers parameterise the condensate rather than deriving it (C137)*. |
| **F6 — background equations** | **Unchanged at `PARTIAL`.** This round derives no new EOM; it evaluates C134's torsion EOM on candidate content. The metric-EOM gap C134 named is untouched. |
| F1, F2, F3, F5, F7 | Reused unchanged / not assessed. |

---

## 10. What this round does NOT show

* Does **not** show that fermion condensates are impossible in general, nor that
  the heterotic constructions are wrong. It shows the four retrieved papers
  *parameterise* the condensate, and that the ingredients of the standard
  derivation are absent here.
* Does **not** claim that no dynamical derivation of a gaugino condensate exists
  in physics. **One does** (dimensional transmutation in a confining `N=1`
  sector); the first draft denied this and is corrected in §3f. The claim is that
  it **cannot be instantiated on this project's frozen content.**
* Does **not** compute that no condensate can form on this background. It reports
  an availability failure, not an impossibility proof. Those are different
  claims; only the first is made.
* Does **not** establish bar (b) unconditionally: it holds **conditional on L4B
  rank = 1** (whose external review is outstanding, `preprint.tex:892`) and
  **only on the zero-mode sector**, not the massive KK tower (W4).
* Does **not** claim any of `S2.3`–`S2.8` as new results — they reproduce
  `pearl_registry` row 145 in one representation, and `S2.8` shows they are
  forced by the embedding (§5a).
* Does **not** reopen C123–C136's verdicts, and does not re-verdict C134 (whose
  route 2 is here independently reconfirmed, not revisited).
* Does **not** change `N_gen=3`'s CONDITIONAL status,
  `lambda = FREE_COUPLING_PARAMETER`, `sm_derivation_claimed = False`, or
  `safe_for_runtime = False`.
* Does **not** close H1c, OB1, OB13, or round95's gap. It removes one candidate.
* Does **not** claim the enumeration in §4 is exhaustive over all conceivable
  fields — it is exhaustive over what the frozen content and the retrieved
  literature suggest.
* Does **not** claim Cardoso et al. or Frey–Lippert were body-read; both are
  abstract-only this session and are marked as such (§3c, §3d).
* Does **not** edit `PARENT_ACTION_GATE.md`, `OPEN_BLOCKERS.md`,
  `null_results/INDEX.md`, or `pearl_registry/INDEX.md`.
* Does **not** solicit Tom Lawrence's Part 5.

---

## 11. Registry actions — NOT performed by this round, proposed only

* `null_results/INDEX.md` entry: `C137-P3Condensate | 2026-09-02 |
  fermion-condensate-torsion | REJECT | …` (four independent grounds, §8).
* `PARENT_ACTION_GATE.md` **F4** "already tried" row, as worded in §9.
* ~~**Pearl (Pearl Gate).** every internal 3-form Clifford structure is a 4D
  pseudoscalar, "measured over all 84 triples"; "upgrades and generalises row
  145 from the `S³` leg to every internal leg", impact 6.~~ **WITHDRAWN before
  reaching the registry**, on the skeptic pass's finding, re-verified by me:
  row 145 already states this for *all three legs internal* in *any*
  `M₄ ×` (internal) setup and was verified representation-independent across 40
  basis changes; and `S2.8` shows the "measurement" is forced by the embedding.
  Writing this row would have entered a false novelty claim into the registry.
  See §5a. *(Recorded rather than deleted, because a withdrawn pearl is itself
  the useful artifact here.)*
* **Pearl (Pearl Gate).** *observation:* `Cl(1,12)` admits **no** Majorana
  condition (`B B* = −1`, quaternionic; `Cl(1,3)` control gives `+1`), matching
  the standard `13 mod 8 = 5` reality-table entry. The reusable part is **not**
  the classification (textbook) but the **method for the negative branch**: an
  absent intertwiner must be closed by the parity of the central element
  `ω = Γ⁰…Γ^{D−1}` under `Γ → ±Γ*`, because a constructive search returning
  nothing is indistinguishable from a broken search.
  *falsifiable_prediction:* any future in-repo claim of the form "no
  intertwiner / no reality structure / no such operator exists", justified by a
  constructive search that came back empty, will be found to have no
  independent closure — check for a central-element or invariant argument
  before accepting it.
  *impact_score:* 5. *trigger_condition:* any candidate invoking Majorana
  bilinears, Majorana masses, or reality conditions on the 13D spinor; or any
  in-repo no-existence claim resting on a search that found nothing.
  *next_check:* whenever the neutrino-Majorana-mass open question (open question 2
  in `RESEARCH_STATUS_REPORT.md`) is next touched.
* **Pearl (Caveat Gate — a specific untested alternative named here).**
  *observation:* W3 (symplectic-Majorana doubling) is a concrete, buildable
  construction that `Cl(1,12)`'s measured quaternionic structure actually
  permits, and it is the only escape from §5b that the algebra does not forbid
  outright. *falsifiable_prediction:* if the `εψᵀC Ω₃ ψ` bilinear of a doubled
  13D spinor is non-zero on single-4D-chirality content, C134 route 2 does not
  apply to it and `P3` reopens in that extension (with bars row-32 and (c) still
  to clear). *impact_score:* 4. *trigger_condition:* any future proposal doubling
  the 13D fermion content, or any OB10-adjacent reality-structure round.
  *next_check:* whenever the 13D reality-structure line is revisited.
* **Pearl (methodology) — REWRITTEN, and the rewrite is the point.**
  *first draft's version:* "a failing control produced this round's best result
  — the invalid `S2.5` expectation, diagnosed rather than deleted, became
  `S2.7`'s 84-triple measurement, strictly stronger than the check it replaced."
  **That is exactly the pattern `pearl_registry` row 144 predicts** (repairs made
  in response to a skeptic pass reintroducing the same defect class): the
  "stronger" replacement was itself unfailable, and its novelty claim was false.
  A defect was diagnosed honestly and its *repair* was then over-credited in the
  same breath.
  *observation (rewritten):* **self-caught defects are systematically
  over-credited by the same document that catches them.** This round confessed
  three defects in §7 and used that confession to buy credibility for repairs
  that a context-blind pass then falsified. A partial confession is worse than
  none — it is the exact shape row 144 already recorded for C133.
  *falsifiable_prediction:* over the next 5 Full-Ladder rounds here, any round
  whose decision.md contains a "self-caught defects" section will, on a
  context-blind pass, be found to have **at least one over-credited repair**
  inside that same section — the confession section is a *higher*-risk region
  than the rest of the document, not a lower one.
  *impact_score:* 6. *trigger_condition:* any round writing a self-caught-defects
  section. *next_check:* after 5 more Full-Ladder rounds.
* **Pearl (methodology, cost-effectiveness of the pass).** *observation:* this
  round's single context-blind pass overturned the verdict block's **leading
  reason**, withdrew **three of five** novelty claims, and stopped a **false
  pearl** from entering the registry — while confirming the verdict direction.
  The defects it found were concentrated where the document was **most
  confident** (§5a's "measured, not argued"; §6's exact accounting), not where
  it hedged. *falsifiable_prediction:* over the next 5 rounds, the skeptic pass's
  highest-severity finding will land in a section the document marked with a
  strengthening adverb ("measured", "exactly", "decisive", "stronger than")
  rather than in a section carrying a caveat. *impact_score:* 5.
  *trigger_condition:* any FL Step 8a pass. *next_check:* after 5 more rounds.

---

## 12. FL Step 8a — skeptic pass

**One context-blind pass** (`Agent(skeptic, model=opus)`, given `claim.md` +
`decision.md` + the script + `results_c137.json` only, no session history, per
the Context Asymmetry Rule). **Verdict returned: `WEAKENED`.**

Per `claim.md`'s own scope note, a single pass suffices for this
literature/argument-based round **unless the pass changes the verdict's
direction**. It did not — it explicitly confirmed `REJECT` is right, on grounds
1 and 2 of §8's disjunction, which hold independently of every finding. So no
Paraphrase-Sensitivity second pass was run. *(That decision is itself a risk,
given `pearl_registry` row 144's prediction that ≥1 repair-introduced defect
survives whenever 3+ repairs are made in one cycle — and this cycle made ~13.
Stated as an accepted, named limitation rather than absorbed: **this document has
not been re-audited after its repairs.**)*

**Disposition of every finding** (all were independently re-verified with my own
tools before acceptance — `audit-verification-gate.md`; **all were real, none was
dismissed**):

| # | finding | verified how | disposition |
|---|---|---|---|
| HIGH-1 | all seven `S2` checks unfailable; `S2.1`'s six list entries were the identical matrix | re-ran the loop (`max dev = 0`) and re-ran `decompose_4d` on **random non-Clifford** internals → still pure `γ₅` | **Accepted.** `S2.1` replaced by a real anticommutativity test + non-Clifford control; `S2.0` added; `S2.8` added as a standing self-indictment; §5a's "measured, not argued" **retracted** |
| HIGH-2 | `N2`'s novelty claim contradicted by row 145, which the round says it read | re-read `pearl_registry:145` and `C134:306-308` | **Accepted.** N2 **withdrawn**; the §11 pearl **withdrawn before reaching the registry**; §5a now credits row 145 |
| HIGH-3 | undisclosed `1/ρ₃` insertion; `[INFERRED]` downgrade dropped | re-read `C125:385` (no `ρ₃`) and `C134:366-369` ("a unit-radius statement, not a `ρ₃` one") | **Accepted.** Now derived (`S5.1`, with a wrong-exponent control), flagged as this round's own step, downgrade restored |
| HIGH-4 | "no derivation at the source" is wrong; document contradicts itself (§5e presumes the mechanism) | re-read my own §3/§5e | **Accepted.** §3f added; verdict block and "One line" rewritten to the transfer framing; N1 downgraded |
| MED-1 | `S5` constrained nothing; old `S5.1` is `D`-independent; `S5.3` a hidden literal; `S5.4` a duplicate | evaluated `−(D−2)+(D−1)` for `D ∈ {4,10,11,13,26}` → `1` every time | **Accepted.** `S5` rewritten; identities demoted to `DATA` |
| MED-2 | check accounting wrong (10 vs 17 data values; unfailable checks counted) | counted `results_c137.json` keys | **Accepted.** §6 recount table added |
| MED-3 | `S4.2`'s negative branch rests on search failure, not proof | computed `Γ⁰…Γ¹² = −I` and its parity under `Γ → ±Γ*` | **Accepted.** `S4.4` added, using the skeptic's own suggested argument |
| MED-4 | `L5` is conditional on L4B (external review outstanding); zero modes ≠ whole field | re-read `preprint.tex:892-905` | **Accepted.** Both conditions now carried in §5b and the verdict block |
| MED-5 | `W4`'s CP-violation dismissal contradicted by the parity-odd `T^t` background | inspection | **Accepted.** Dismissal **withdrawn**; W4 upgraded to most-live variant |
| MED-6 | §5c's sharpening runs the wrong way and contradicts §4 candidate D | inspection | **Accepted.** Sharpening **withdrawn**; N5 withdrawn |
| LOW-1 | restatement self-test applied inconsistently (N3 = §5e) | inspection | **Accepted.** N3 withdrawn in the evidence tier |
| LOW-2 | `RESEARCH_STATUS_REPORT:173` re-scoped (it is a λ-origin note) | re-read `:170-174` | **Accepted.** Demoted from "decisive" to "corroborating" |
| LOW-3 | "two structurally different routes" is generous | re-read `OPEN_BLOCKERS:1543-1553` | **Accepted.** Narrowed in §5b |

**Nothing was dismissed and nothing was accepted-as-limitation-only** — every
finding produced an edit. Per the FL Response Matrix, `WEAKENED` ⇒ promote with a
`[WEAK]` marker and documented caveats; done throughout.

**The pass also identified something the document under-credited**, and it is
adopted: the strongest genuinely original content in this round is **§4 candidate
D's circularity argument** — the torsion-induced four-fermion term *is* the
torsion EOM substituted back, so "the condensate sources the torsion" and "the
torsion generated the interaction that made the condensate" are one equation, not
two. That was not among N1–N5 and is now named in the evidence tier.

---

## Check (reproduces this decision)

1. Every internal citation above was obtained by **direct `Read`/`Grep` of the
   cited file this session**, not from memory: `pearl_registry/INDEX.md` (rows
   32 and 145/146), C132 `decision.md` §`P3`, C134 `decision.md` **in full**,
   C125 `decision.md` §0a/§2a, round87 and round88 `decision.md` **in full**,
   `null_results/INDEX.md` in full, `preprint.tex` §sec:chirality (Lemma L5),
   `OPEN_BLOCKERS.md` OB10/C33, `RESEARCH_STATUS_REPORT.md:173,439`,
   `PARENT_ACTION_GATE.md` F1–F7.
2. `claim.md`'s instruction to check round87/round88's failure reasons was
   followed by reading both decisions in full. The first draft's conclusion from
   that (§3e, "one step earlier in the chain") was **wrong and is corrected in
   §3f**: this is a transfer failure, of the same kind, at a different joint.
3. The four C132 literature sources were re-retrieved this session; **two were
   read in body text** (MPZ, Gemmer–Lechtenfeld) and every quote reproduces text
   at the retrieved offset; **two are abstract-only** and are labelled as such
   everywhere they are used. **Not verified:** the skeptic pass had no network
   access and so could not independently re-check the two verbatim quotes; they
   rest on my retrieval alone.
4. All machine checks ran before any positive statement in §5 was written; three
   failed on the first run (§7) and ten more defects were found by the skeptic
   pass (§12). **Every one of the thirteen was diagnosed; none was tuned away**,
   and three checks were **deleted** rather than repaired because they could not
   fail.
5. The permitted `REJECT` was reported as a `REJECT`. No positive result was
   forced, and "a condensate that would work" was at no point treated as "a
   condensate that is derived" — §4 scores each candidate field separately for
   exactly that reason.
6. The round's own restatement test (C136's lesson) was applied to this round's
   own headline. **It was applied too generously on the first attempt** — the
   skeptic pass showed that three of the five things it certified as
   non-restatement were restatements or false. Corrected in the evidence tier
   below. *(This is itself the C136 lesson recurring: a round can build the
   right self-check and still run it too kindly on itself.)*
7. **Not done:** no second, differently-worded skeptic pass over the *repaired*
   document. See §12 for why, and for the named risk that carries.

---

## Evidence tier of the central conclusion

**Central conclusion (rewritten after the skeptic pass):** *`P3` is REJECTED.
No dynamically-derived condensate is **available** to this project's frozen
`S³×S⁶` content: the standard derivation (gaugino condensation by dimensional
transmutation) exists in physics but needs SUSY, a gauge multiplet and a
confining sector that this project does not have, and the four retrieved papers
nearest this geometry parameterise the condensate rather than deriving it. On
the certified zero-mode sector the source bilinear vanishes identically — an
exact operator identity, conditional on L4B rank = 1 — with the Majorana escape
closed at the `Cl(1,12)` algebra level, and inside minimal coupling the 4D
Lorentz structure is forced rather than chosen. The magnitude required for
`t ∈ {0,1}` has no independent source anywhere in this project.*

**Restatement self-test — re-run honestly after the pass.** The REJECT
*direction* was substantially foreseeable from C132's own Mechanism-Transfer-Gate
caution: **`[CONFIRMATION]`, not discovery.** The first draft then listed five
things as non-restatement. Re-scored:

| | claim | verdict after the pass |
|---|---|---|
| N1 | the primaries' verbatim "we assume it" statements | **kept, but downgraded.** Real and new to the repo (C132 had abstracts only) — but it does **not** show "no mechanism at the source" (§3f). It shows these four papers do not supply one. |
| N2 | `S2.7`'s 84-triple result closing bar (a) | **WITHDRAWN.** One-line derivable from `pearl_registry:145`, which is strictly stronger; and forced by the embedding (`S2.8`). |
| N3 | the positive iff-condition and its phase dependence | **WITHDRAWN.** One line from C134 §5a's displayed equation plus route 2; the phase half is §5e, which the document itself flags as a restatement. |
| N4 | the `Cl(1,12)` no-Majorana result | **kept, narrowed.** The classification is a textbook reality-table entry (which §5b itself cites). What survives as content is the **method** for the negative branch (`S4.4`'s central-parity closure) — see the rewritten §11 pearl. |
| N5 | bar (c) sharpened to `Λ·ρ₃ ≈ 4` | **WITHDRAWN** (§5c). |
| — | **§4 candidate D's circularity argument** | **added, and it is the strongest original content in the round** — it was not on the first draft's own list. The torsion-induced four-fermion term *is* the torsion EOM substituted back, so `P3`'s only internally-available condensation mechanism is the same equation it is meant to source. |

**Tier of the mathematics: `[VERIFIED-tool]`, confidence HIGH — but for a
smaller set than the first draft claimed.** 30 check call sites, 0 failures,
`ruff` clean, AST self-audit, and a from-scratch Clifford rebuild reproducing
C134 §5a and C125 E3. **Of those 30, roughly 9 carry independent content and 6
are genuine controls** (§6 recount); 7 are reproductions forced by the embedding
and 5 are corollaries. The load-bearing identity `P_LΓ⁰Ω₃P_L = 0` is exact at
deviation `0.00e+00`, holds as a 64×64 operator statement for arbitrary 13D
spinors, and **the skeptic pass attacked it directly and found no falsifier.**

**Tier of the literature finding: `[CITED, primary]`, confidence MEDIUM-HIGH**
for MPZ and Gemmer–Lechtenfeld (body text retrieved and quoted this session, but
**not independently re-verified** — the skeptic had no network access);
**`[CITED, abstract-only]`, confidence MEDIUM** for Cardoso et al. and
Frey–Lippert. The claim is "these four papers parameterise rather than derive",
**not** "no derivation exists" — that stronger claim was made in the first draft
and is retracted (§3f).

**Tier of the physics reading: `[INFERRED]`, confidence MEDIUM-HIGH.** The
load-bearing ground is §4 candidate B's AOG-5 failure (no SUSY, no gauge
multiplet, G97) — `[INFERRED]` from certified in-repo facts, and independent of
every skeptic finding. Bar (b) is `[VERIFIED-tool]` **conditional on L4B rank = 1
(external review outstanding)** and **scoped to the zero-mode sector**, not the
massive tower (W4). Bar (a) is `[VERIFIED-tool]` **scoped to minimal coupling**
(W1). Bar (c) and bar row-32 are `[CITED]`/`[INFERRED]` arguments about
availability, not impossibility proofs.

**Marker on the whole round: `[WEAK]`** — per the FL Response Matrix, one
context-blind pass returned `WEAKENED`, every finding was real, and the document
was rewritten rather than defended. **Additional named limitation:** the repaired
document has **not** been re-audited, and `pearl_registry` row 144 predicts that
a repair cycle of this size (~13 repairs) leaves at least one repair-introduced
defect behind. Treat the repairs with the same suspicion as the original text.
