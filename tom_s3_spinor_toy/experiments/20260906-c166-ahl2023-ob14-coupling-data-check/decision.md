# C166 — Decision

**Date:** 2026-09-06
**Verdict:** `NO-RELEVANT-CONTENT__ISOTROPY-IRREDUCIBLE-ON-S6-CLOSES-THE-GAP`

---

## What was checked [VERIFIED-primary-source]

Read AHL2023 (arXiv:2203.02961v3, "Invariant Spinors on Homogeneous
Spheres", Agricola-Hofmann-Lawn) directly from its own LaTeX source (not
from the round114 PDF, not from memory, not from round114's own partial
prior read which only covered §2.1-2.2 and the S³ theorem):

- `§2.3` "Invariant Metric Connections on Homogeneous Spaces" — the
  general Nomizu-map formalism (`Λ: m → so(m)`, torsion/curvature at the
  origin in terms of `Λ` and the Lie bracket `[·,·]_m`).
- `§2.4` "Metric Connections with Torsion" — the three-way `O(n)`-module
  splitting of torsion classes (vectorial / totally skew / cyclic
  traceless), all still valued in tensor powers of `TM ≅ m`.
- `§4.1.1` "The isotropy representation" (quaternionic spheres
  `Sp(n)·K/Sp(n-1)·K`) — read specifically as an adversarial check (kill
  condition C) for a genuine cross-summand coupling construction
  elsewhere in the paper.
- `§5.1` "`S⁶=G₂/SU(3)`" — the coset OB14 actually needs, in full
  (statement, theorem, proof, both remarks, the Ambrose-Singer torsion
  proposition).

## Findings against the kill criterion

**A (independent su(3)-equivariant object beyond `Λ^k m`, on `S⁶`): FAIL.**
`§5.1` opens by stating the isotropy representation is irreducible ("The
isotropy representation here is irreducible, so the only invariant
metrics are obtained from multiples of the Killing form") and every
object subsequently constructed is valued in `Λ^• m`:
- `Σ_inv = span_C{1, y₁∧y₂∧y₃}` — the invariant spinors, living inside
  `Σ ≅ Λ^{0,•}m` (as `SU(3)`-modules).
- The nearly-Kähler 2-form `J = e₁∧e₂ + e₃∧e₄ + e₅∧e₆` ∈ `Λ²m`.
- The Ambrose-Singer torsion `T^AS = (1/√3)(-e₁₃₆-e₁₄₅-e₂₃₅+e₂₄₆)` ∈
  `Λ³m` (totally skew type, per the Proposition immediately following).

No object in this section is valued in a representation independent of
`m` itself. This is the SAME pool of objects (torsion, curvature,
connection difference tensor) that C134 (ECSK torsion), C162 (decoupled
`3̄_extra`), and C164→C165 (canonical-connection curvature `R^c`) already
built and killed via Schur's-Lemma/branching arguments — AHL2023 supplies
no object outside that already-exhausted pool for this specific coset.

**B (general theorem making the method reducibility-independent): FAIL.**
`§2.3`'s Nomizu-map formalism is fully general (any invariant connection
on any reductive homogeneous space), but it does not claim or imply
independence from isotropy reducibility — it says only that `Λ: m→so(m)`
determines the connection; when `m` is irreducible (as `§5.1` states for
`S⁶=G₂/SU(3)`), any invariant `Λ` is forced to be (by Schur's Lemma
applied to the irreducible `m`) built from the same structure constants
already available, not an independent free parameter into a new sector.
No section of the paper states a reducibility-independent general
coupling theorem.

**C (a second, reducible-isotropy `SU(3)`-structure coset as structural
analogy): FAIL (for `SU(3)`-equivariance specifically), but a genuine
coupling construction DOES exist elsewhere in the paper.** `§4.1.1`
(quaternionic spheres `Sp(n)·K/Sp(n-1)·K`) explicitly builds an invariant
metric that couples two DISTINCT isotropy summands, `L := (C^{2n-2}⊗C) ⊕
(C⊗C)` and `L' := (C^{2n-2}⊗C')⊕(C'⊗C')`, via a shared symplectic-form
pairing — this is a real instance of the general SHAPE OB14's sub-path
(ii') needs (independent coupling data linking one summand's structure to
another's). But: (i) it is `sp(n-1)`-equivariant, not `su(3)`-equivariant;
(ii) its precondition is a REDUCIBLE isotropy representation with
genuinely distinct summands — exactly the precondition `§5.1` states
`S⁶=G₂/SU(3)` does NOT have. The method is real but does not transfer to
this coset without inventing new geometric content (a second, currently
nonexistent invariant summand on `S⁶=G₂/SU(3)`'s own tangent space) — which
is precisely what C142's and C164's own searches already found does not
exist in this project, not a shortcut around that finding.

All three kill conditions fail (A and B outright; C confirms the pattern
exists in the paper but shows structurally why it cannot transfer to this
specific coset). Per the pre-registered kill criterion: verdict is
`NO-RELEVANT-CONTENT`.

## Applying the Round114 pearl (one-line-reducibility discipline)

`pearl_registry/INDEX.md` (2026-07-17, Round114) warns: before accepting
a "literature cross-check" as informative, check whether the conclusion
is derivable in one line from the source's own stated theorem. This
round is not a cross-check of a *computed value* (Round114's failure
mode) — it is a scope/content check ("does the source contain construction
X for coset Y"), a different question type. The relevant discipline here
is instead: did the check actually read the coset-specific section, not
just infer from the paper's general abstract/title? Yes — `§5.1` was read
in full, including the proof and both remarks, not inferred from the
paper's title or abstract alone.

## Kill Analysis

- **What this kills:** the specific, previously-unactioned hope named in
  `experiments/20260906-c164-ob14-path-i-vs-ii-scoping/decision.md`
  Section 9 Concern 4 — that AHL2023, unread for this exact question
  until now, was quietly already supplying OB14's missing coupling data.
  It was not. This closes that named scope gap as "checked, found empty,"
  converting it from an open unactioned note into a settled negative.
- **What this does NOT kill:** OB14's own status (`BLOCKED-INTERNAL` /
  `BLOCKED-EXTERNAL-OR-THEORETICAL`, unchanged — this round's outcome was
  never a precondition for that status, only a named residual check
  against it), round59/C139-C165's own certified results (untouched), or
  `N_gen=3` (untouched).
- **What survives, genuinely new to this project:** an explicit,
  citable, primary-source confirmation that `S⁶=G₂/SU(3)`'s isotropy
  representation is irreducible (AHL2023 §5.1's own opening sentence) —
  a structural reason, independent of and complementary to C142's
  representation-theoretic search and C164/C165's holonomy argument, for
  why no internally-buildable "new independent summand" can arise from
  this coset's own homogeneous presentation alone. Three independent
  routes (C142's branching search, C165's holonomy/Schur argument, and
  now this round's irreducibility citation) now converge on the same
  structural conclusion via different arguments — a modest but genuine
  strengthening of confidence that (i')/(ii') require content this
  project's current geometric data cannot supply, not merely that no one
  has found it yet.
- **Relaxation Map (per Minimal Relaxation Rule, not pursued here, named
  for future reference):** AHL2023's own `§4.1.1`-style coupling
  construction (real, existing, `sp(n-1)`-equivariant) is a genuine
  candidate STRUCTURAL TEMPLATE for a not-yet-conceived construction on
  `S⁶` — but building an analogous `su(3)`-equivariant version would
  require inventing a second reductive summand on `S⁶=G₂/SU(3)` that does
  not exist in this project's (or AHL2023's own) current geometric
  content. This is explicitly high-AOG-5-risk territory (no independent
  motivation for inventing such a summand beyond wanting to rescue OB14),
  already named and correctly not pursued by C142/C164. Recorded here for
  completeness, not endorsed as a next step.

## What this does NOT mean

1. Does NOT establish that no such construction could ever exist for
   `S⁶=G₂/SU(3)` in principle — only that AHL2023, as published, does not
   supply one, because its own stated isotropy representation for this
   coset is irreducible.
2. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`,
   `safe_for_runtime=False`, or any prior round's certified result.
3. Does NOT close OB14 itself — remains `BLOCKED-INTERNAL` /
   `BLOCKED-EXTERNAL-OR-THEORETICAL`; this round only closes one named,
   previously-unactioned scope gap about whether AHL2023 was quietly
   relevant.
4. Does NOT violate "DO NOT INITIATE CONTACT [with Tom Lawrence]" — this
   round read an already-published, already-cited paper; no contact with
   its authors occurred.

## Check (reproduces the primary-source read)

```
Fetch arXiv:2203.02961 (v3), LaTeX source, sections 2.3, 2.4, 4.1.1, 5.1.
Confirm: §5.1 opens "The isotropy representation here is irreducible..."
Confirm: Σ_inv, J, T^AS all stated as elements of Λ^k(m) for various k.
Confirm: §4.1.1 builds L, L', C_0 as a genuine cross-summand coupling,
  conditioned on reducibility of the Sp(n)·K/Sp(n-1)·K isotropy rep.
```

## Recommendation on independent skeptic pass

**Recommend one independent context-blind skeptic pass (claim.md + this
decision.md only, no session history) before this finding is registered**
in `pearl_registry/INDEX.md` / `OPEN_BLOCKERS.md` OB14's own update
chain, per this project's own FL Step 8a convention for any PROMOTE-shaped
verdict entering the permanent record. Specific things worth adversarial
re-checking, named honestly rather than left implicit:

1. Whether "isotropy representation irreducible" (a REAL representation
   claim) is being read correctly against this project's own established
   fact that `m ⊗ C ≅ 3 ⊕ 3̄` as a COMPLEX `su(3)`-module (C139/round59's
   own convention) — these are not in tension (a complex non-self-dual
   irrep's underlying real space is real-irreducible), but the skeptic
   should verify this equivalence explicitly rather than take this
   round's word for it, since a convention mismatch here would undercut
   the whole verdict.
2. Whether kill condition B was assessed too generously in AHL2023's
   favor — i.e., whether §2.3's Nomizu-map formalism, despite not stating
   a reducibility-independent theorem explicitly, nonetheless permits a
   construction this round did not consider.
3. Whether §4.1.1's cited coupling construction has a closer non-obvious
   analogue elsewhere in the paper (e.g. §4.2-4.4, not read this round)
   that could transfer more directly than assessed here — this round did
   not exhaustively read every quaternionic subsection, only §4.1.1 as
   the adversarial check for kill condition C.

This verdict is a scope/content-of-a-published-source finding (Gate 1/2
artifact-provenance territory: the artifact is AHL2023 itself, published,
identity and provenance not in question), not a numeric computation — so
no positive/negative numeric control or Floor-Ceiling interval applies;
the applicable rigor check is the adversarial re-read named above.

---

## Update -- independent context-blind skeptic pass (orchestrating
   session, 2026-09-06), verdict CONFIRMED-REAL

Per the recommendation above, ran an independent `Agent(skeptic)` pass:
claim.md + this decision.md only, plus the skeptic's own independent fetch
of AHL2023's LaTeX source (not trusting this round's paraphrase).
**Verdict: `CONFIRMED-REAL`.** All three named concerns resolved cleanly
by direct re-reading of the primary source, plus one additional check the
skeptic ran on its own initiative:

1. **Real-vs-complex irreducibility convention:** confirmed no conflict --
   AHL2023 works over R throughout §5.1 ("`m` real-irreducible"), switching
   to C only for `Σ_inv`; fully consistent with `m⊗C≅3⊕3̄`.
2. **Kill condition B (Nomizu §2.3) not assessed too generously:** the
   skeptic re-derived §2.3's own formulas (`Λ:m→so(m)`, torsion/curvature
   eq. 10/11) directly and confirmed every object stays within `m⊗m`,
   `Λ^k m`, `so(m)` -- no hidden reducibility-independent theorem exists.
3. **§4.2-4.4 (not read by this round) checked independently:** ALL of
   §4.2, §4.3, §4.4, and even §5.3 (`Spin(9)/Spin(7)`) explicitly state
   REDUCIBLE isotropy as their own precondition (2-4 distinct summands
   each) -- reinforcing, not weakening, kill condition C.
4. **Skeptic's own additional check** (G₂-structures / other invariant
   tensors on `S⁶`): none found -- the invariant 2-form space is
   1-dimensional (AHL2023's own Prop., spanned by `J` alone), and no
   associative/coassociative calibration or other tensor is mentioned for
   this coset.

**Bonus finding, worth citing forward:** the skeptic surfaced AHL2023's
own Remark 4.10 ("any decomposition of the isotropy representation into
irreducible submodules doesn't contain pairwise isomorphic nontrivial
summands") as an independent, citable statement of essentially the same
Schur's-Lemma barrier this project's own C165 used -- a fourth,
independent primary-source citation now converging on the same structural
conclusion (alongside C142's branching search, C165's holonomy argument,
and this round's irreducibility citation).

**No correction to the verdict required.** `NO-RELEVANT-CONTENT` stands as
written above.
