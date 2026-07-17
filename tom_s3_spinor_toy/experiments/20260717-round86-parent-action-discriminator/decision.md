# E18 (round86) — Decision

**Date:** 2026-07-17
**Verdict:** `BLOCKED__NO_PARENT_ACTION_FOUND_IN_PROJECT_OR_CITED_LITERATURE__MISSING_INGREDIENT_NAMED`
**Go/no-go:** None of the three pre-registered candidate constructions can be
built from anything this project has established or from anything found by
reading its own three already-cited geometry references. This is,
word-for-word, what `claim.md`'s FAIL criterion describes — but per this
project's own precedent (E17) and the task's explicit framing, the honest
verdict here is **BLOCKED, not FAIL**: the reason no construction was found
is a concretely-named, specific missing ingredient (a stated parent action /
field-content statement), not a proof that no such construction CAN exist.
No such proof was attempted or found; only an absence, in the sources
actually available to this project, was established. See "Why BLOCKED, not
FAIL" below for the exact reasoning.

## Bottom line, stated plainly first

Searching this project's own three cited geometry references
(`Agricola_2002_Dirac_naturally_reductive.pdf`,
`Agricola_Hofmann_Lawn_2023_invariant_spinors.pdf`,
`Charbonneau_Harland_2016_NK_instantons.pdf`) turned up **zero** instances of
any construction combining both torsion signs / both ends of a one-parameter
connection family into one simultaneous physical object (no "bi-torsion"
bundle, no domain-wall/kink interpolating between connections, no
parity-symmetric action with two coupled connection fields). All three
papers treat the relevant one-parameter families (Agricola 2002's own
`∇^t` — the literal source of this project's `t`-family) or connection
choices (AHL 2023's generalized Killing spinors; Charbonneau-Harland 2016's
canonical NK connection) as objects to be studied **one value / one
connection at a time**, never as a pair required to coexist by one action.
The single closest structural analogue found — AHL 2023's PAIR of
Killing spinors on round `S³=SU(2)` with eigenvalues `±1/2` — is a
genuinely different mathematical object (same, single, torsion-free
Levi-Civita connection; two eigenvalues, not two connections) and does not
transfer to the project's `t=0`/`t=1` question without new argument (Section
2 below).

Re-examining this project's own prior work (E11's Freund-Rubin exploration,
candidate 3; `preprint.tex`'s Pati-Salam/left-right text, candidate 2) finds
no unexplored piece that closes the gap either — E11's own Q2/Q3 findings
are reused, not re-derived, and `preprint.tex`'s one explicit "left-right
symmetry of S³" assumption (line 409) is a phenomenological input to a
gauge-coupling formula, not an action with independent fields and equations
of motion.

The missing ingredient is precisely nameable, and this project's own text
already flags the SAME class of gap (KT-1) for a structurally analogous
question (the physical origin of the `S⁶`-twist `D⊗S⁻`) — see Section 5.

---

## 1. Literature check — the three cited PDFs [VERIFIED-tool: pdftotext extraction + direct text search/read]

Extracted full text via `pdftotext -layout` (poppler, confirmed installed at
`/mingw64/bin/pdftotext`) for all three PDFs into a scratch directory, then
searched and directly read the relevant sections. Page numbers below were
computed from form-feed (`\f`) page-break markers in the extracted text,
cross-checked against `pdfinfo`'s page counts (Agricola 2002: 26pp;
AHL 2023: 53pp; Charbonneau-Harland 2016: 29pp — all three confirmed via
`pdfinfo`).

### 1a. `Agricola_2002_Dirac_naturally_reductive.pdf` — the DIRECT SOURCE of this project's `∇^t` family

This is not merely "a paper this project cites" — `preprint.tex:1470`
(`\cite{Agricola2002}`) states this project's own `t`-family construction
**is** Agricola's one-parameter family, so this is the single most important
literature check for this experiment.

- **p.1 (abstract):** "we study the one-parameter family of connections
  `∇^t` joining the canonical and the Levi-Civita connection." Confirms:
  the family is framed, from its origin, as a family to be studied pointwise
  (one `t` at a time), not as a two-sector coexistence structure.
- **p.2 (`Agricola2002` text, "The one-parameter family of G-invariant
  connections defined by...", matching this project's own
  `∇^t_XY=t[X,Y]_m`):** introduces `∇^t` exactly as this project already
  uses it. No combined two-`t` object is defined anywhere in this
  introduction.
- **p.3:** "`t=0` corresponds to the canonical connection `∇^0`, which, by
  the Ambrose-Singer..." — `t=0` is named and studied individually.
- **p.5 (the single most relevant sentence found in this entire search):**
  "the connection with `t=1` has also special properties, for example, it
  has the same Ricci tensor than the canonical connection. This is why we
  propose to call it the **anticanonical connection**." This confirms
  `t=1` has a name and a real, tool-citable property (matching Ricci
  tensor with `t=0`) — but this is a STATIC, individual property of the
  `t=1` connection alone (a fact ABOUT it), not a construction that USES
  both `t=0` and `t=1` together in one action or one Hilbert space. No
  sentence anywhere in this paper says "the canonical and anticanonical
  connections together form..." or gives any joint object built from both.
- **p.18 (Theorem 4.2, "Some particular spinor fields"):** studies constant
  spinor fields and their parallelism under the canonical connection
  (`t=0`) specifically; the general formula `∇^t_Z ψ = (t/3)(Z⌟H)·ψ` is
  given for ANY single `t`, evaluated one value at a time in every
  subsequent proposition (Theorem 4.3, Proposition 4.1, p.18–19). No
  proposition anywhere combines `t=0` and `t=1` parallelism conditions into
  one joint condition or one combined operator.
- **p.19–20 (Propositions 4.1–4.3, "vanishing theorems"):** existence/
  non-existence results for parallel spinors, stated and proved for one
  connection at a time (`∇^{1/3}` is the other specially-treated value here,
  for an unrelated reason — the Kostant-Parthasarathy formula's natural
  scale). No construction requiring two specific `t`-values to coexist is
  present.
- **Search performed, zero hits:** `domain wall`, `kink`, `both sign`,
  `left-right`, `left and right`, `doubled`, `bi-torsion`, `two torsion`,
  `simultaneous` (case-insensitive grep across the full extracted text,
  37 raw hits for "torsion" total, all read in context above or confirmed
  irrelevant to coexistence).

**Honest scope note:** the full 26-page paper was extracted and grepped for
all of the above terms; the specific sections most likely to contain a
"combine `t=0` and `t=1`" construction (the definition of the family, the
parallel-spinor existence theorems, the vanishing theorems) were read
directly, not merely grepped. Sections on curvature/scalar-curvature
computations for individual homogeneous spaces (roughly pp.6–17, the bulk of
the paper's worked examples) were grepped but not read line-by-line in full;
this is flagged as **not exhaustively read**, though the grep found no
hits for any of the relevant terms in that range either.

**Verdict for this source: no construction resembling candidates 1, 2, or 3
found.** The paper studies `∇^t` as exactly what this project's own
Convention Table (`CONVENTION_TABLE.md` §5) already describes: a
one-parameter family evaluated pointwise, with `t=0` and `t=1` sharing one
named property (Ricci tensor) but never combined into one physical or
mathematical object.

### 1b. `Agricola_Hofmann_Lawn_2023_invariant_spinors.pdf` — closest (but non-matching) analogue found

- **p.14 (Theorem 3.7), p.16–17 (Corollary 3.12, Theorem 3.13, Corollary
  3.14):** For `S^{2n+1}=\mathrm{SU}(n+1)/\mathrm{SU}(n)` (which specializes
  to `n=1`, i.e. `S³=SU(2)`, the exact case this project studies), the space
  of invariant spinors is **2-dimensional**, spanned by
  `ψ+ := 1` and `ψ- := y1∧...∧yn` (for `n=1`: `ψ- = y1`). Corollary 3.14
  (p.17): "The spinors `ψ±` are Killing spinors if and only if
  `a = 2b/n`... The round metric corresponds to the parameters
  `a=n/(n+1), b=1/2`, in which case we recover the usual Sasakian Killing
  spinors for the constants `1/2, -1/2` (or `1/2, 1/2`, depending on `n`)."
- **p.48 (§6, case "(II) `G=SU(2)=Sp(1)`"):** "By Theorem 3.7 and Corollary
  3.14, the round metric `g_{a,b}|_{a=b=1/2}` admits a PAIR of invariant
  Killing spinors for the constant `1/2`, but no invariant generalized
  Killing spinors."

**Why this is the closest analogue, and why it does NOT satisfy any of the
three candidates:** this IS a genuine, tool-citable mathematical fact about
`S³=SU(2)` with the round metric in which **two spinors coexist
simultaneously, under one action/connection, for a structural reason (the
2-dimensional invariant-spinor space, forced by the isotropy representation
of `S³` at trivial isotropy)** — i.e. it has the flavor of candidate 1's
"physically derived two-sector Hilbert space." But on direct inspection it
is the wrong pair for this project's question:

1. **Single connection, not two.** Both `ψ+` and `ψ-` are Killing spinors
   for the SAME connection (the Levi-Civita connection of the round metric,
   i.e. this project's own `t=1/2` — the value KT-8 already shows has
   **zero** zero modes for the full operator, `preprint.tex:1421-1465`,
   reused via E14 `decision.md:224-232`). This project's `t=0`/`t=1` question
   is about TWO DIFFERENT connections (`∇^0`, `∇^1`), not two spinors under
   one connection.
2. **Different structure (eigenvalue sign, not connection-parameter
   value).** The "pair" here is a `±1/2` split of the KILLING CONSTANT
   (`∇_X ψ = λ X·ψ`, a Riemannian Killing-spinor equation with a scalar
   eigenvalue `λ`), not a split of the AFFINE connection-family parameter
   `t` this project's `∇^t=∇^{LC}+t[·,·]_m` uses. These are different
   mathematical structures on `S³` that happen to both be called "the
   `1/2`" in their respective papers — conflating them would repeat exactly
   the kind of symbol-overload error this project's own methodology
   (`research-methodology.md` § Classificateur, Type 1) is designed to
   catch. No argument connecting the two is given in either paper, and
   constructing one here would be new work, not a citation.
3. **Consequently, this does not supply a physically-derived reason to
   split into `t=0`/`t=1` sectors** — it supplies a physically-derived
   reason (the 2-dim invariant-spinor space at trivial isotropy) for a
   DIFFERENT pair (`±1/2` Killing eigenvalues at the SINGLE Levi-Civita
   value `t=1/2`), which is not the pair candidate 1 needs.

**Honest scope note:** AHL 2023 is a 53-page paper; the sections read in
full are those specifically on the `SU(n+1)/SU(n)` family (§3.3, pp.13–17)
and the summary case-by-case table (§6, p.48), since these are the sections
containing the `S³=SU(2)` case. The remaining sections (roughly pp.18–47,
covering `Sp(n)Sp(1)`, `Sp(n)U(1)`, and `3-(α,δ)`-Sasaki families not
relevant to `S³` itself) were grepped for the same keyword list as 1a
(`domain wall`, `kink`, `chirality`, `two connections`, `pair of
connections`, `opposite torsion`) with zero hits, but not read in full;
flagged as not exhaustively read.

**Verdict for this source: no construction satisfying candidates 1–3 found**
— the one genuinely relevant "pair" result found (the `±1/2` Killing-spinor
pair) is a different object from what any of the three candidates need, for
the concrete, checkable reasons given above.

### 1c. `Charbonneau_Harland_2016_NK_instantons.pdf` — least relevant of the three, confirmed

This paper concerns instanton deformation theory on nearly-Kähler
six-manifolds (`S⁶`-type geometry, this project's OTHER factor, not `S³`),
cited by this project for the G₂/SU(3) torsion discussion, not the S³-side
torsion-escape-route.

- **p.1 (abstract):** the paper studies deformations of a SINGLE canonical
  connection (the NK canonical connection, defined by fixed skew-symmetric
  torsion and `SU(3)`-holonomy) and proves it is a **rigid** instanton on
  three of the four homogeneous NK six-manifolds — i.e. it has NO
  deformations, the opposite of a construction that would need two
  connections to coexist.
- **p.1–2 ("bubbling" discussion):** the one genuinely "one-parameter
  family" mentioned in this paper is a family of R⁷ instantons parameterized
  by **instanton SIZE** (a conformal-symmetry modulus), interpolating
  between a flat connection (size→large) and a singular connection
  converging to the NK canonical connection (size→small). This is
  structurally a size/scale family, not a torsion-sign or left/right family
  — it does not resemble any of candidates 1–3.
- **p.11–12 (definition of the canonical connection on a principal
  bundle):** defines ONE canonical connection per homogeneous space
  `G/H`, studied individually throughout; no combined "both signs" or
  "both torsion values" object appears anywhere.
- **Search performed, zero hits:** `domain wall`, `kink`, `torsion sign`,
  `opposite sign`, `bi-torsion`, `two torsion` (case-insensitive grep,
  16 raw hits for "torsion" total, all consistent with single-connection
  usage).

**Honest scope note:** this 29-page paper's core deformation-theory proofs
(roughly pp.13–28) were grepped for the keyword list but not read in full,
since the paper's own subject (instanton rigidity on `S⁶`) is a full factor
removed from this experiment's `S³`-side question; the introduction and
canonical-connection definition (pp.1–2, 11–12) were read directly.

**Verdict for this source: no construction resembling candidates 1–3
found**, and structurally the least likely of the three to contain one
(different manifold, different question — rigidity of ONE connection, not
coexistence of two).

---

## 2. Re-examining this project's own constructions

### 2a. E11/round75's Freund-Rubin exploration — candidate 3 (flux sign as selector)

Reused, not re-derived, per the task's own scoping instruction (this
question was already directly investigated by E11 for exactly this
purpose). `experiments/20260717-round75-e11-freund-rubin-torsion-link/
decision.md:171-212` (Q3, already `[VERIFIED-tool]`): the flux-induced
moduli potential `V_flux ∝ C³ ∝ q²` (`preprint.tex:985-989`) is
**quadratic** in the flux quantum `q`, hence blind to `sign(q)` — the
existing bosonic EOM (`dV_total/dρ6=0`, fixing `ρ6`, not `q`) provides no
mechanism to select a sign, let alone a specific value corresponding to
`t=0` or `t=1`. `decision.md:113-167` (Q2): a generic mechanism exists in
the broader flux-compactification literature (torsionful connections
`∇^± = ∇^{LC} ± (1/2)H` sourced by an NS-NS 3-form, standard in
Strominger-Hull systems) that COULD in principle be the right shape for
candidate 3 — but is explicitly `[DOCS]`-level, generic, **not wired into
this project's `preprint.tex` anywhere** (zero grep hits for "contorsion",
"H-flux", "NS-NS", or "connection deformation" in the full paper, confirmed
there and not re-checked here since nothing in this experiment's remit
would change that grep result).

**Checked freshly for this experiment (not merely re-cited): does anything
change if the SIGN-SELECTION question is asked directly, rather than
E11's original "does the flux sign relate to torsion at all" framing?**
No — the identical structural fact applies: `V_flux ∝ q²` is manifestly an
even function of `q` (a quadratic-form potential built from a scalar `C`
that itself only ever appears squared or cubed in even total powers,
`preprint.tex:985-989, 371`), so no continuous or discrete minimization of
this SPECIFIC potential can distinguish `q` from `-q`, regardless of which
question is asked of it. A sign-selecting mechanism would require either
(a) a NEW, linear-in-flux term in the potential (not present, and not
derivable from anything currently in `preprint.tex`), or (b) the
fermionic-sector coupling described in Q2, which — even if built — was
shown by E11's Q3 (reusing E7's E8-gate result) to generically push the
resulting stationary point AWAY from `t∈{0,1}` toward `t=1/2`, absent an
unmotivated fine-tuning.

**Verdict: candidate 3 not satisfied by anything in this project's own
Freund-Rubin construction.** The one path that COULD in principle work
(the fermionic contorsion coupling) is explicitly unbuilt, and this
project's own prior result (E7's E8 gate, reused via E11) suggests building
it in the most natural way would not select `t=0,1` even if attempted.

### 2b. `preprint.tex`'s Pati-Salam / left-right text — candidate 2 (parity-related connection pair)

Grepped the full `preprint.tex` (this experiment, fresh) for "Pati--Salam"
(LaTeX en-dash spelling — plain-hyphen "Pati-Salam" gives zero hits, an
artifact of the paper's own typesetting, confirmed by direct `Read`) and
"parity" (zero hits for "parity" anywhere in the paper) and "left-right"
(one hit).

- **`preprint.tex:280-281`:** "The `U(1)_{B-L}` factor needed to complete
  the Pati--Salam algebra... is not itself an isometry of `S³×S⁶`" — this
  is about gauge-GROUP completeness (a missing `U(1)` generator), not about
  two connections on the S³ factor.
- **`preprint.tex:408-409` (the one "left-right" hit, in §Weinberg angle
  estimate):** "the Weinberg angle follows from the Pati--Salam mixing
  formula. With `g_{2R}=g_{2L}=g_2` (**left-right symmetry of `S³`**)..."
  This is the single closest textual anchor in `preprint.tex` itself to
  candidate 2. **On direct inspection it does not satisfy candidate 2's
  requirements:** it is a stated numerical EQUALITY ASSUMPTION between two
  gauge COUPLING CONSTANTS (`g_{2L}`, `g_{2R}`) used to derive a
  phenomenological formula for `sin²θ_W` — it is not an action, has no
  independent fields `∇_L`, `∇_R` with their own equations of motion, and
  is never connected anywhere in the paper to the `t=0`/`t=1` torsion
  question (a fully separate part of the paper, §"S³ torsion deformation",
  `preprint.tex:1467-1497`, with zero cross-references to §"Weinberg angle
  estimate" in either direction — confirmed by direct read of both
  sections this round). Using it to license candidate 2 would require
  inventing a new argument connecting "the paper assumes equal L/R gauge
  couplings for one formula" to "therefore an action exists producing
  both `t=0` and `t=1` torsion connections" — a leap this experiment
  declines to manufacture, per `claim.md`'s own kill criterion against
  ad hoc duplication.
- **E14/round80's own Reading 3** (`experiments/20260717-round80-z2-
  left-right-symmetry-search/decision.md:234-251`, reused, not re-derived
  here): already identifies this exact Pati-Salam-parity analogy as the
  reading CLOSEST to supplying candidate 2 — and already flags it as an
  **unadopted model-building CHOICE**, in direct, unreconciled tension with
  this project's own established ASYMMETRIC chirality mechanism (Lemma L5,
  `preprint.tex:884-908`, `sign(ind)=+1`, a left-handed EXCESS on the S6
  factor, not a parity-symmetric result). E17 (`decision.md:299-326`,
  Section 5) reaches the identical conclusion independently. This
  experiment adds no new argument beyond what E14/E17 already established;
  it confirms, by direct re-reading of `preprint.tex` itself (not merely
  citing E14/E17's characterization of it), that the ONLY textual anchor
  for "left-right symmetry" in the entire paper is the gauge-coupling
  equality assumption at line 409, and that this assumption is never
  elevated to, or connected with, an action with independent `∇_L`/`∇_R`
  fields and their own equations of motion anywhere in the paper.

**Verdict: candidate 2 not satisfied.** The one textual anchor found is a
phenomenological coupling-equality assumption for an unrelated formula
(Weinberg angle), not an action; E14/E17's own prior identification of the
Pati-Salam-parity reading as an unadopted, tension-carrying model-building
choice (not a derived construction) is independently reconfirmed here by a
fresh, direct read of `preprint.tex`.

### 2c. Candidate 1 — checked directly against this experiment's own literature findings (Section 1b)

No independent physical reason for a two-copy Hilbert space split by `t`
value was found anywhere in this project's text (E12's own negative result,
reused via E17 `decision.md:96-152`, already established that no
Majorana/reality condition or orbifold/projection route supplies the
missing content from a single sector). Section 1b above is the closest this
search came to a "physically derived 2-dim space" result (AHL 2023's
`ψ±` pair) — and Section 1b explains concretely why it is the wrong pair
(different connection, different structure), not a version of candidate 1
that could be adapted with modest new argument.

**Verdict: candidate 1 not satisfied**, by anything in this project's text
or its cited literature.

---

## 3. Applying the pre-registered criteria

| Candidate | Found in project's own text? | Found in cited literature? | PASS? |
|---|---|---|---|
| 1 — physically-derived 2-sector Hilbert space | No (E12/E17 already ruled out known routes) | No (AHL 2023's `ψ±` pair is a different, non-transferable structure — Section 1b) | **NO** |
| 2 — parity-related `∇_L`/`∇_R` action with EOMs | No (only a phenomenological coupling-equality assumption, unconnected to the torsion question — Section 2b) | No (none of the three PDFs construct paired L/R connections from one action) | **NO** |
| 3 — sign-selecting dynamical/topological field | No (flux potential is quadratic in `q`, blind to sign; fermionic coupling unbuilt — Section 2a) | No (no domain-wall/kink or sign-selection construction found in any of the three PDFs) | **NO** |
| Fourth alternative | Searched for; none found beyond the AHL 2023 near-miss (Section 1b), which does not qualify | | **NO** |

All three pre-registered candidates, and the one near-miss fourth
alternative found during the literature search, fail to satisfy the PASS
requirements.

---

## Why BLOCKED, not FAIL

`claim.md`'s FAIL criterion is, read in isolation, literally satisfied by
Section 3's table. The distinction that matters — and the reason this
experiment reports BLOCKED, following E17's own precedent and the task's
explicit framing — is what KIND of negative result this is:

- A **FAIL** verdict would require having shown that no such construction
  CAN exist — e.g., a no-go theorem, an explicit contradiction derived from
  attempting to build one, or a structural obstruction proven the way E12's
  Majorana/reality-condition check or `preprint.tex`'s Lichnerowicz-bound
  argument (KT-8) are genuine proofs of non-existence for the things THEY
  rule out.
- What this experiment actually establishes is an **absence-of-evidence**
  result: a systematic search of the specific sources available to this
  project (its own text, its own three cited geometry references) did not
  turn up a construction meeting the PASS bar. This is not the same claim
  as "no construction is possible" — a differently-scoped literature search
  (a broader flux-compactification or Strominger-Hull-system search, per
  E11's own Relaxation Map, `decision.md:236-247`), or an explicit new
  13D-parent-action derivation, might yet find or build one.
- Crucially, the missing ingredient is **specifically nameable**, which is
  the operative BLOCKED criterion: "a specific parent theory... that this
  project does not currently have access to or has explicitly deferred."
  Section 5 below shows this project's own text already has a named,
  precedented example of exactly this class of gap (KT-1), independently
  of this experiment.

This mirrors E17's own reasoning exactly (`experiments/20260717-round85-
e17-sector-coexistence-gate/decision.md:391-399`): "neither PASS nor FAIL
is honestly supportable; BLOCKED is the correct verdict," because the
deciding factor is a missing physical-input statement, not a demonstrated
impossibility.

---

## 4. Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result kills:** the specific hope that this project's own
  ALREADY-CITED geometry literature (Agricola 2002, AHL 2023,
  Charbonneau-Harland 2016) contains an off-the-shelf construction closing
  the `t=0`/`t=1` coexistence gap — a systematic, term-by-term search of
  all three found none. It also kills, more narrowly than before, the
  temptation to read AHL 2023's `S³=SU(2)` `ψ±` Killing-spinor pair
  (p.48, Corollary 3.14) as evidence for candidate 1 — Section 1b shows
  concretely why this specific result, despite superficially resembling
  "two spinors coexisting for a structural reason," is the wrong pair for
  this project's question.
- **What this result does NOT kill:** the possibility that a construction
  exists in literature this project has NOT yet cited (a broader
  Strominger-Hull-system or flux-compactification search, candidate 3's
  natural next step per E11's own Relaxation Map); the possibility that a
  genuinely new 13D-parent-action derivation could supply one directly;
  H1c, KT-8, or any of E9–E17's own tool-verified results, all untouched.
  It does not kill AHL 2023's `ψ±` result itself as a mathematical fact —
  only its applicability to THIS project's specific coexistence question
  without further, currently-unwritten argument.
- **What survives, confirmed stronger than before:** the precise
  characterization of what's missing. Before this experiment, KT-8/E17
  described the gap as "a stated 13D parent action." This experiment
  sharpens that into a checked, term-by-term negative literature result
  (Section 1) plus a concrete identification of the ONE candidate (fourth,
  unlisted) construction that superficially resembles a solution and a
  specific, checkable reason it fails (Section 1b) — this narrows future
  search from "check whether known literature already has this" to
  "either search literature this project has not yet cited, or derive the
  parent action directly," a strictly smaller remaining search space.

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Broaden the literature search beyond this project's 3 currently-cited geometry references | Search Strominger-Hull flux-compactification literature directly for an explicit `H`-flux-sources-contorsion construction with a stated `q↔(2t-1)` normalization (E11's own next step, `decision.md:236-247`) — candidate 3's most concrete remaining path |
| Attempt to adapt AHL 2023's `ψ±` Killing-spinor result | Would require an explicit NEW argument connecting the Riemannian Killing-spinor eigenvalue split (`λ=±1/2` under the Levi-Civita connection) to the project's affine-connection-family split (`t=0` vs `t=1`, both torsionful) — not attempted here, flagged as speculative and NOT the same structure without this argument |
| State an explicit 13D parent action directly | The single missing ingredient per KT-8/E17/this experiment: how many independent Dirac fields on `S³` this compactification contains, and how each couples to `∇^t` — acknowledged by this project's own text (`preprint.tex:1370-1396`) to fall outside any standard supergravity framework at `13`D (Nahm's theorem caps supergravity at 11D), so this is not a routine "look it up" task |
| Resolve candidate 2's Lemma-L5 tension | Either find an independent reason parity-symmetric model-building applies to `S³` specifically but not to `S⁶` (where Lemma L5's asymmetric result already holds), or abandon candidate 2 as a route — unchanged from E14/E17's own already-stated Relaxation Map item |

## Assumptions carried, unresolved

- `SU(2)_L`=left-translation vs its mirror (`CONVENTION_TABLE.md` row 6) —
  not needed for any finding in this experiment; no candidate reached the
  point where this convention would matter.
- `t=1`'s existence only under `c0=-2` (`CONVENTION_TABLE.md` row 5) —
  carried forward unchanged; not re-litigated here.
- `D_full² = D_{S3,t}²⊗I + I⊗D_{S6,twisted}²` (E2/E12's decoupling
  assumption) — presupposed wherever E11/E12/E14/E17's own findings are
  cited, exactly as those experiments themselves presuppose it.
- Whether a construction exists in flux-compactification or
  Strominger-Hull-system literature NOT currently cited by this project —
  explicitly NOT searched here (out of scope, per the task's own
  instruction to check "literature already cited by this project first");
  flagged as the most concrete open item in the Relaxation Map above.

## What this does NOT mean

1. Does **not** prove no parent action or field-theoretic construction
   satisfying the frozen claim CAN exist — only that none was found in this
   project's own text or its three currently-cited geometry references.
   See "Why BLOCKED, not FAIL" above.
2. Does **not** resolve KT-8 (whether ANY zero mode of the full untwisted
   `D_full` exists) or H1c (physical selection of `t`) — both untouched,
   exactly as E17 left them.
3. Does **not** affect this project's `N_gen=3` headline claim, which rests
   on the independently-established G73/G74A/G74B S6-only triality/index/
   chirality chain (per `activeContext.md` and `reports/
   PROJECT_360_ROUND3_SYNTHESIS.md`) — this experiment concerns only the
   separate S3-side torsion-escape-route program, already characterized in
   `preprint.tex:1467-1497` as a "candidate mechanism... physically
   unmotivated, not a resolution," not load-bearing for `N_gen=3`.
4. Does **not** claim the three PDFs were read to their last page — Section
   1's per-source "Honest scope note" states exactly which sections were
   read directly versus grepped only, for each of the three sources.
5. Does **not** claim AHL 2023's `S³=SU(2)` `ψ±` Killing-spinor pair
   (p.48) is irrelevant to this project generally — only that, as it
   currently stands in the cited paper, it does not satisfy any of the
   three candidate constructions for THIS specific question. Adapting it
   would be new work (see Relaxation Map), not a citation.
6. Does **not** re-derive or challenge any of E2/E3/E7/E9–E17's own
   tool-verified results — all reused here purely by citation.
7. A BLOCKED verdict here does **not** mean further progress is impossible
   — the Relaxation Map above gives three concrete, if substantial, next
   steps, not an appeal to general uncertainty.

## 5. Why this is the same class of gap as an already-acknowledged item (KT-1) — context, not a new finding

This project's own text already contains a directly analogous open item,
independently identified by a prior external audit (not by this
experiment): `preprint.tex:1398-1419` ("Physical origin of the twisted
operator `D⊗S⁻` [open — no parent action identified]") states, for the
`S⁶`-factor twist choice: "No higher-dimensional parent action — an
explicit thirteen-dimensional Lagrangian..., background flux, or gauge
bundle from which this specific twist would follow by dimensional
reduction — is stated anywhere in this paper or its cited sources," and
further notes that the nearest structural analogue (the heterotic
"standard embedding") "does not directly transplant" because this
framework has no pre-existing independent gauge sector. This is labeled
KT-1 in this project's own audit trail (`activeContext.md:90-93`,
`reports/PROJECT_360_ROUND3_SYNTHESIS.md`).

**This experiment's `t=0`/`t=1` coexistence question is a structurally
identical gap, on the OTHER factor (`S³`, not `S⁶`) and for a different
specific construction (torsion-connection choice, not twist choice), but
the SAME root cause: no stated 13D parent action exists anywhere in this
project for EITHER the `S³`-side connection family or the `S⁶`-side twist.**
Sharpening this further, `preprint.tex:1370-1396` (the item immediately
preceding KT-1 in the paper's own Open Problems list) states explicitly
that a literal 13-dimensional parent action is not a routine, off-the-shelf
object to look up: "standard supergravity is capped at eleven spacetime
dimensions (Nahm's theorem)... a literal thirteen-dimensional supergravity
completion is not available off the shelf." This is why this experiment's
BLOCKED verdict names a genuinely substantial missing ingredient, not a
citation this project merely hasn't looked up yet.

## Pearl-registry candidate

**Observation, concrete enough to flag:** AHL 2023's `S³=SU(2)` result
(Corollary 3.14, p.17/48) — that the round metric's 2-dimensional invariant-
spinor space splits into Killing spinors with eigenvalues `±1/2` under the
SINGLE Levi-Civita connection — is a genuine, tool-citable "coexisting pair"
structure on the exact manifold (`S³`, round metric) this project's
torsion-escape-route already studies, but for the WRONG parameter axis
(Killing eigenvalue sign, not the affine connection-family parameter `t`).
**Falsifiable prediction, if pursued:** IF an explicit map could be
constructed relating the Riemannian Killing-spinor equation's `λ=±1/2`
split to the affine family's `t=0`/`t=1` split (e.g., via the standard
cone-construction correspondence between Killing spinors on `S^n` and
parallel spinors on the flat cone `C(S^n)`, which is a well-known,
independently-citable mechanism in Riemannian spin geometry, NOT verified
or attempted here), THEN this might supply exactly the missing "physically
derived 2-sector split" candidate 1 needs — but this is speculative,
requires new argument this experiment does not attempt, and is flagged
`[CANDIDATE]`, not adopted. **Impact score ~4** (narrow to this project's
own torsion-escape-route line of work; the general cone-construction
mechanism cited is well-known in the broader field, so the pearl here is
specifically "check whether it applies to THIS project's `t`-family," not a
novel mathematical fact). Not registered to the global
`pearl_registry/INDEX.md` — project-internal, not cross-domain.
`next_check`: if the torsion-escape-route program is revisited (e.g. after
KT-8 or a parent-action item is otherwise addressed), check whether the
cone-construction correspondence connects `λ=±1/2` Killing spinors to
`t=0/1` parallel spinors before assuming it does or doesn't.

## Check (reproduces this decision)

This is a literature-search-and-classification round; there is no new
numerical script (per the task's own framing — "constructing or identifying
a parent action is a major undertaking, not a routine check"). The "check"
is: (1) `pdftotext -layout` extraction of all three PDFs was performed this
round (confirmed installed at `/mingw64/bin/pdftotext`; page counts
cross-verified against `pdfinfo`: 26/53/29 pages respectively, matching the
extracted texts' form-feed counts exactly); (2) every keyword search
reported above (`domain wall`, `kink`, `bi-torsion`, `left-right`,
`doubled`, `both sign`, `simultaneous`, `chirality`, `two connections`,
`pair of connections`, `torsion sign`, `opposite sign`) was actually run
against the extracted text and its exact hit-count is reported, not
estimated; (3) every `preprint.tex` line cited above (280-281, 292-298,
408-429, 884-908, 1370-1419, 1467-1497) was read directly this round, not
cited from memory or from a prior experiment's paraphrase; (4) every prior
experiment citation (E11, E12, E14, E17) was reused by direct `Read` of
that experiment's own `decision.md` this round, not from memory.
