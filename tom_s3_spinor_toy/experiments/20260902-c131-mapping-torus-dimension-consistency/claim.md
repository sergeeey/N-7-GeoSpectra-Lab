# C131 claim -- is `M_ι` (the S³-level mapping torus) actually the right
# dimensional object, or did C130 compare it against the wrong table?
# (C130's Relaxation Map item W1, "cheaper than round95, now ahead of it")

## Question type (EstimandOps L0)

**Descriptive/existence, of a specific kind: convention/consistency
verification.** Not causal, not predictive. C130 flagged that `M_ι` (a
4-manifold) does not appear in C127 §4's dimension audit (`Ω₁₃,Ω₁₄` /
`Ω₁₄,Ω₁₅` / `Ω₅,Ω₆`, never `Ω₄`) and called this "adversely indicated."
This round's job is to determine whether that comparison is even the
right one to make -- i.e. whether C127 §4's audit and C127 §5d's actual
`S³×S¹` mapping-torus construction are answering the SAME dimensional
question (in which case C130's flag is a real problem) or are two
SEPARATE constructions with their own, individually self-consistent
dimensional conventions that were never meant to be cross-checked against
each other (in which case C130's flag may be a false alarm, or at least
needs restating).

## Background, stated honestly before any computation

Read, in FULL, before doing anything else:
- `experiments/20260901-c127-bordism-global-anomaly-scoping/decision.md`
  **§4** (the dimension audit C130 compared against) AND **§5d** (the
  actual mapping-torus construction that produced `M_ι` -- read both
  slowly and carefully, they are asking different sub-questions within
  the same file, and this round's entire job is to determine whether
  they need to agree on a dimension or not).
- `experiments/20260902-c128-nabla-t-gauge-group-reconciliation/decision.md`
  §6 (where `M_ι` was chosen as a substitute because the frozen `M₄` is
  non-compact, so no 13D mapping torus is closed).
- `experiments/20260902-c129-pin-structure-existence-mapping-torus/decision.md`
  and
  `experiments/20260902-c130-twisted-pin-structure-existence/decision.md`
  in full, especially C130 §0 finding C1 and §11 Pearl 2 (the exact
  "adversely indicated" claim this round tests) -- read C130's own
  reasoning critically, do not simply assume it is correct because it
  passed two skeptic passes on ITS OWN document; those passes checked
  C130's internal consistency and its citation of C127 §4, not whether
  C127 §4 and §5d are actually the same question.

**The specific historical/physics fact this round must nail down, stated
so the round knows exactly what literature question to chase:** Witten's
original 1982 global SU(2) anomaly is a statement about a gauge theory
whose GAUGE FIELD lives on some manifold `X` (in the original paper,
4-dimensional spacetime; in Hamiltonian/canonical formulations, sometimes
phrased via a spatial slice), and a large gauge transformation
`g: X → SU(2)` detected by `π_{dim X}(SU(2))`. The standard modern
(Dai-Freed / Freed-Hopkins) restatement of this uses a MAPPING TORUS of
`X` under the interpolation, which has dimension `dim(X) + 1`, and the
relevant bordism/anomaly group lives at that dimension.

**The precise question this round must answer:** in C127 §5d's
construction, what does the `X` in "Witten's construction, applied here"
actually correspond to -- is it (a) the internal `S³` factor itself
(dimension 3, giving mapping torus dimension 4, i.e. `M_ι` IS the right
object and C130's flag is comparing it to an unrelated table), or (b)
some other object this project should be using instead (e.g. the full 4D
spacetime, or the 13D or 4D EFFECTIVE-THEORY readings C127 §4's table is
actually about, which would make C130's flag correct)? This is NOT
obvious and must be determined by actually reading how the Witten/
Dai-Freed construction is standardly applied to an INTERNAL
COMPACTIFICATION MANIFOLD (as opposed to spacetime itself) -- search the
literature for this specific distinction, do not assume by analogy.

## The Zero-Signal Gate check, required before proceeding

Per `falsification-ladder.md` Step -5: `(∃ entity) ∧ (∃ falsifiable
predicate) ∧ (∃ measurable outcome)`, all three required.

- **Entity:** the specific claim "C127 §4's dimension audit and C127
  §5d's mapping-torus construction are answering the same dimensional
  question, hence must use consistent `Ω_d` bookkeeping" -- a precise,
  checkable proposition about this project's own two sections.
- **Falsifiable predicate:** either the two sections' conventions are the
  SAME (C130's flag stands, `M_ι` is likely the wrong object) or they are
  GENUINELY DIFFERENT, self-consistent conventions answering different
  sub-questions (C130's flag needs restating/softening, and `M_ι` may be
  perfectly fine for the specific Witten-style question C127 §5d posed).
- **Measurable outcome:** an explicit, citation-backed statement of what
  dimension the Witten/Dai-Freed mapping-torus construction should use
  when applied to an internal S³ factor of a Kaluza-Klein compactification
  (not spacetime itself) -- retrieved from the actual anomaly-inflow /
  Dai-Freed literature, not inferred by this project's own analogy.

**If the literature does not clearly settle which convention applies to
an INTERNAL manifold (as opposed to spacetime), this round should return
`BLOCKED` or explicit `[UNKNOWN]` -- NOT pick whichever answer makes
C128-C130's prior work "count," and NOT pick whichever answer makes it
"not count." This is explicitly permitted and is not a failure of the
round. The round's job is to find the truth, not to vindicate or
invalidate prior rounds.**

## Falsifiable claim (only if the Zero-Signal Gate passes)

State precisely, with citation, whether `M_ι` (dimension 4, built from the
internal `S³` factor) is a dimensionally consistent object for the
specific Witten-style "does interpolating between `∇⁰` and `∇¹` via a
large gauge transformation create an anomaly" question C127 §5d posed --
independent of, and not to be confused with, the SEPARATE questions C127
§4 addresses (a 13D parent action's own topological terms/anomaly, or the
4D spacetime effective theory's anomaly).

**Kill criterion:** the round fails its own purpose if it (a) asserts an
answer without a directly-applicable citation for how the Witten/Dai-Freed
mapping-torus construction's dimension is determined when the "space" in
question is an internal compactification factor rather than spacetime,
(b) conflates C127 §4's and §5d's questions without explicitly checking
whether they are actually the same question, or (c) resolves the
ambiguity in whichever direction is more convenient rather than following
the citation.

## What this round does NOT show

- Does not itself attempt any new anomaly computation -- purely a
  dimensional-consistency / scope-clarification question.
- Does not touch round95's missing S⁶-S³ link.
- Does not reopen C125's, C126's, C127's, C128's, C129's, or C130's actual
  mathematical content -- if this round concludes `M_ι` was the wrong
  object, their MATH stays correct (about the object they studied); only
  the PHYSICAL RELEVANCE of that object to OB1 is in question.
- Does not change `N_gen=3`'s CONDITIONAL status, `lambda=
  FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.
- Does not solicit Tom Lawrence's Part 5.

## Verification plan

- Read all cited decision.md files and sections in full before anything
  else, paying special attention to distinguishing C127 §4 from §5d.
- Literature-first: search for how Witten-type / Dai-Freed global
  anomalies are computed for GAUGE FIELDS OR CONNECTIONS ON AN INTERNAL
  COMPACTIFICATION MANIFOLD specifically (not spacetime) -- this is a
  real, established topic in Kaluza-Klein / string-compactification
  anomaly literature (e.g. anomalies of internal gauge bundles, "bundle
  of theories" / family-index framings, or KK-reduction of anomaly
  polynomials) -- retrieve and read primary or well-established secondary
  sources directly, matching this session's established standard (C129,
  C130 both retrieved and read primaries rather than trusting memory).
- Determine explicitly whether the internal-manifold case uses the SAME
  `Ω_d` bookkeeping as the spacetime case (dimension of the internal
  space + 1 for the mapping torus, matching `M_ι`'s construction) or a
  DIFFERENT one tied to the ambient/total spacetime dimension.
- FL Step 8a skeptic pass, and a SECOND independent pass with a
  differently-worded prompt (Paraphrase-Sensitivity Probe) unless the
  first pass returns a clean, unqualified confirmation with zero
  findings -- matching this session's established precedent for rounds
  closing a live, high-impact Relaxation Map item.
