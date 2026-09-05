# C165 decision -- ZERO-ON-3BAR-SUMMAND confirmed by direct computation,
# matching the pre-registered Schur's-Lemma prediction exactly.

**Date:** 2026-09-06
**Experiment:** `20260906-c165-canonical-connection-curvature-check`
**Script:** `c165_canonical_curvature_check.py` -- `results_c165.json`
**Checks:** 19/19 passed.

## Verdict

```
ZERO-ON-3BAR-SUMMAND
  R^c RESTRICTED TO THE FUNDAMENTAL (3(+)3bar) CASIMIR-EIGENSPACE OF
  LAMBDA^2(m) VANISHES AT MACHINE PRECISION (relative 1.7e-15)
  THIS MATCHES THE PRE-REGISTERED SCHUR'S-LEMMA PREDICTION IN claim.md
  EXACTLY -- su(3)_C=8 (adjoint, irreducible) AND 3bar (dim 3) ARE
  NON-ISOMORPHIC su(3)-IRREPS, SO Hom_su3(3bar,8)=0 FORCES THIS
  REGARDLESS OF THE SPECIFIC CURVATURE, AND THE NUMERIC CHECK CONFIRMS IT
  DOES NOT FAIL FOR SOME UNFORESEEN REASON (e.g. R^c not actually landing
  purely in su(3)_C, or a basis-matching error)
  C164's THIRD CANDIDATE IS NOW CLOSED: NEITHER OB14 SUB-PATH GAINS AN
  INDEPENDENT SOURCE FROM THIS OBJECT
  UPDATE_2026_09_06__INDEPENDENT_SKEPTIC_PASS_RUN__VERDICT_CONFIRMED_REAL__SEE_SECTION_7
```

**One line.** The canonical connection's curvature 2-form `R^c`, restricted
to the `3(+)3bar` (fundamental) summand of `Lambda^2(m)` -- a superspace of
the specific `3bar`-summand the task asked about -- is the zero map, at
machine precision (`1.735e-15` relative to `R^c`'s own overall scale of
`0.43`, i.e. six orders of magnitude below the smallest nonzero component
found anywhere else in the tensor). This was predicted, in `claim.md`,
*before* running the computation, from Schur's Lemma alone (`su(3)_C`, the
adjoint, is an irreducible 8-dim module; `3bar` is a non-isomorphic
irreducible 3-dim module; any `su(3)`-equivariant linear map between
non-isomorphic irreducibles is forced to be zero). The computation confirms
the prediction rather than merely failing to falsify it: `R^c` itself is
genuinely nonzero overall (`max|R^c| = 0.43`, `t2_r_tensor_is_genuinely_
nonzero_somewhere` passed), so this is not a degenerate "everything is zero"
construction -- the vanishing is specific to the fundamental block, exactly
as the representation theory demands.

---

## 1. What was computed, concretely

**T1 (rebuild g2 = su(3) (+) m from octonions).** Reused `g96_g2_su3.py`'s
own certified functions (`build_phi`, `g2_condition_matrix`,
`find_g2_generators`, `commutator`) to independently reconstruct the full
14-dim `g2` Lie algebra as 7x7 matrices acting on `Im(O)=R^7`, and its
`su(3)`-stabilizer/complement split. Re-verified (not merely cited)
`dim(g2)=14`, closure (`1.18e-15`), Jacobi (`5.55e-17`),
`dim(su3)=8`/`dim(m)=6`, and the reductive property `[h,m] subset m`
(`1.17e-15`) -- all machine-precision, matching `G96`'s own certified
`VERIFIED` status.

**T2 (compute `R^c` itself).** Using the standard closed-form curvature
formula for a reductive homogeneous space's canonical connection,
`R^c(X,Y) = -[X,Y]_h` for `X,Y in m` (Nomizu 1954; Kobayashi-Nomizu Vol.II
Ch.X -- cited, not re-derived, per `claim.md` Prior Result Gate step 6), the
`su(3)`-part of `[e_i,e_j]` was extracted for all 6 basis vectors of `m`
(`comp_gens`, `G96`'s own orthonormalized complement) via projection onto
the orthonormalized `su3_gens` basis. Confirmed `[m,m]` lands entirely in
`g2=h(+)m` (residual `2.18e-15`), the tensor is antisymmetric in `(i,j)`
(required of any curvature 2-form), and is genuinely nonzero overall
(`max|R^c|=0.431`).

**T3 (Casimir decomposition of `Lambda^2(m)`).** Built the `su(3)`
vector-representation `V_a := ad(su3_gens[a])|_m` (6x6 real antisymmetric),
confirmed `m` itself is Casimir-irreducible (all 6 eigenvalues of
`sum_a V_a^2` equal `-1.333333` exactly = `-4/3`, spread `3e-15`) -- the
expected single scalar for an irreducible real 6-dim module (`3(+)3bar`
complexified), by Schur's Lemma applied to the real representation. Extended
`V_a` to `Lambda^2(m)` (15-dim) and found its Casimir spectrum: **exactly 3
distinct eigenvalues, `{0: mult 1, -4/3: mult 6, -3: mult 8}`** -- matching
`1 (+) (3(+)3bar) (+) 8` = `1+6+8=15` exactly, with the fundamental block's
eigenvalue (`-4/3`) matching `m`'s own Casimir value exactly (`-1.33333` in
both cases) -- direct confirmation that the numerically-found 6-dim block
really is the `3(+)3bar` summand the task's own stated decomposition
(`Lambda^2(3(+)3bar) = 3bar(+)1(+)8(+)3`) predicts, not merely a
coincidentally-6-dimensional subspace.

**T4 (restrict `R^c` to that block, check zero; irreducibility side-check).**
Projected the `8x15` matrix representation of `R^c` (rows = `su(3)`
components, columns = the 15 basis 2-forms `e_i^e_j`) onto the 6-dim
fundamental eigenspace found in T3: **the result is zero at
`1.735e-15` relative precision.** Also independently re-verified that
`su(3)_C` is Casimir-irreducible under its own adjoint action (spread
`4.44e-15`), confirming it really is the single 8-dim irreducible module
(not, say, an accidental direct sum that could contain a `3bar`-isomorphic
piece) -- ruling out the one way the Schur's-Lemma argument could have
failed to apply.

---

## 2. Why the combined `3(+)3bar` check answers the `3bar`-specific question

The task asked specifically about the `3bar`-summand of `Lambda^2(m)`, not
the combined `3(+)3bar` block this script actually tested. This is not a
scope-widening substitute -- it is a **strictly stronger, and sufficient,**
result: `3bar` is a linear subspace of the 6-dim fundamental block (the
block's own eigenvalue and dimension, confirmed in T3, show it decomposes
*exactly* as `3(+)3bar` under the full `su(3)` action, with no other irrep
type sharing that Casimir eigenvalue possible within `Lambda^2(m)`'s
15-dimensional total, since the only other pieces are the singlet
(eigenvalue 0) and the adjoint (eigenvalue -3) -- both already excluded by
their own distinct eigenvalues). A linear map that is zero on a superspace
is zero on every subspace of it, `3bar` included. Separately identifying
`3` from `3bar` inside this 6-dim block (e.g. via the nearly-Kähler complex
structure `J`) was therefore not necessary to answer the question asked,
and was not attempted -- noted explicitly as a scope simplification, not an
oversight (see "What this does NOT mean" below).

---

## 3. Comparison against claim.md's kill-criterion table

| Outcome | Result |
|---|---|
| `ZERO-ON-3BAR-SUMMAND` | **CONFIRMED** -- exactly as pre-registered, machine-precision zero on the full fundamental block (superspace of `3bar`) |
| `PROPORTIONAL-NOT-INDEPENDENT` | Not applicable -- the restriction is zero, not merely proportional to something nonzero |
| `INDEPENDENT-SOURCE-FOUND` | Ruled out |
| `COMPUTATION-INFEASIBLE` | Ruled out -- `G96`'s octonion construction reproduced its own certified dimension/closure/Jacobi facts to machine precision, and the curvature computation itself is a direct, well-conditioned linear-algebra projection, not an ill-posed or numerically fragile calculation |

---

## 4. Kill Analysis (Anti-Overfitting Gate discipline, applied to this
   negative finding)

- **What this round kills:** the specific hope, raised by C164's own
  independent skeptic pass, that the canonical connection's curvature
  `R^c` could supply the missing `su(3)`-equivariant map either OB14
  sub-path (i') or (ii') needs. It cannot -- not because it happens to be
  proportional to already-used data (the C70/C71-style rejection), but for
  a more fundamental reason: it is representation-theoretically FORCED to
  vanish on exactly the summand type (`3bar`, or `3`) that would be useful,
  regardless of the specific geometry of `S^6=G2/SU(3)`. This closes the
  candidate more decisively than a "proportional" verdict would have --
  there is no normalization or basis choice under which this object could
  ever become useful for this purpose, on this coset.
- **What this round does NOT kill:** OB14 itself, or the possibility that
  some OTHER not-yet-considered geometric object (not `R^c`) could supply
  independent data. This closes exactly the one candidate C164 Section 9
  raised, per claim.md's own explicit scope limitation (item 1, "What this
  does NOT mean").
- **Relaxation Map (one assumption per variant, none attempted here):**

| variant | changed assumption | status |
|---|---|---|
| R1 | Check the OTHER curvature-adjacent object mentioned in C164 Section 9 Concern 4 -- AHL2023's own text, grepped for OB14-specific coupling data (not yet done, an honest scope gap C164 itself flagged, unrelated to this round's `R^c` computation) | Not actionable in this round -- named as the orchestrating session's next cheap check, per C164 Section 9 |
| R2 | Accept OB14 sub-paths (i')/(ii') as `BOTH-HIGH-RISK-NO-CHEAP-DIFFERENTIATOR` again, now that this round closes the one gap the skeptic pass found in that verdict | A verdict/registry decision for the orchestrating session, not a physics construction |
| R3 | Attempt to identify a genuinely new, not-yet-conceived geometric object on `G2/SU(3)` (beyond `R^c`, the shape operator, C134's torsion, C70/C71, G102 -- all now checked and rejected) | Would be new mathematics-research, out of scope for this round, same AOG-5 concern C164 Section 4 already raised for (i')/(ii') themselves |

---

## 5. What this round does NOT mean

- Does NOT prove no OTHER not-yet-conceived `su(3)`-equivariant object could
  supply independent data for OB14 -- only that this ONE candidate
  (`R^c`'s restriction to the `3(+)3bar` block, a superspace of the
  `3bar`-summand specifically named in the task) is now closed.
- Does NOT separately verify the `3`-vs-`3bar` split within the 6-dim
  fundamental block via the nearly-Kähler complex structure `J` -- not
  needed, per Section 2 above (zero on the superspace implies zero on
  either named subspace), but named explicitly as an unattempted
  refinement, not a silent gap.
- Does NOT reopen or re-derive C142's rejections of C70/C71 or G102, or
  C164's confirmation of the shape-operator dismissal -- all cited, none
  re-verified here.
- Does NOT change `N_gen=3`'s `CONDITIONAL` status, `lambda =
  FREE_COUPLING_PARAMETER`, `sm_derivation_claimed = False`, or
  `safe_for_runtime = False`.
- Does NOT close OB14 itself as permanently unreachable -- narrows the
  currently-known candidate set to zero (C70/C71, G102, C134 torsion,
  shape operator, and now `R^c` all rejected), consistent with C164's own
  `BLOCKED-INTERNAL`, not `IMPOSSIBLE`, framing.
- Does NOT edit `OPEN_BLOCKERS.md`, `pearl_registry/INDEX.md`,
  `null_results/INDEX.md`, or `CLAIM_LEDGER.yaml` -- registry updates are
  the orchestrating session's, per C124-C164 precedent.
- Does NOT run any git operations.

---

## 6. Recommendation on an independent skeptic pass

**Recommend: YES**, per this project's C159/C161/C162/C163/C164
convention, for two concrete reasons specific to this round:

1. This round's conclusion is again a NEGATIVE one (closes the one
   candidate C164's own skeptic pass surfaced) -- the same "did we
   under-invest in a genuinely available cheap test" concern that
   motivated C164's own skeptic pass applies here too: an independent,
   context-blind reviewer should check whether the Schur's-Lemma argument
   and its numeric confirmation are actually airtight, or whether the
   reduction from "restrict to `3bar`" to "restrict to the combined
   `3(+)3bar` block" (Section 2 above) silently smuggled in an error.
2. The specific numeric construction (reusing `G96`'s octonion-derivation
   frame, which was built independently of `round59`'s `NOMIZU`/`ADNU`
   frame, with no explicit cross-normalization check performed in this
   round -- `T3b` was planned in `claim.md` but not executed, since the
   Casimir-based verification path made a direct `ADNU`-frame cross-check
   unnecessary for the specific question asked) is new to this project and
   has not been reviewed by anyone other than the process that built it.

**Not run in this round** -- matching C162/C164's own practice of
recommending rather than executing the skeptic pass within the same round,
so the orchestrating session can decide whether/when to invoke it.

---

## 7. Update -- independent context-blind skeptic pass (orchestrating
   session, 2026-09-06), verdict CONFIRMED-REAL

Per Section 6's own recommendation, ran an independent `Agent(skeptic)`
pass: claim.md + this decision.md + script + results, plus C164 Section 9
for background. **Verdict: `CONFIRMED-REAL`.** All 5 stress-tests
(Schur's-Lemma correctness, superspace-to-subspace validity, frame-
independence, curvature-formula implementation, connection-identity scope)
held up. No correction to `ZERO-ON-3BAR-SUMMAND` required.

**One documentation-drift note, accepted and fixed:** the skeptic found
this round's own claim.md pre-registered an equivariance spot-check (`R^c`
under `Ad(g)` for a nontrivial `g`) that Section 6's text mislabeled as
"`T3b`" when it is actually the plan's own `T3` — a naming slip, not a
missing check: the reductive-property confirmation (`[h,m]⊂m`, `1.17e-15`)
already structurally implies the equivariance the spot-check would have
verified, so the substance is unaffected, only the label was wrong.

**One methodological observation, worth recording (not a defect in this
round):** the skeptic noted the result is close to tautological once
stated representation-theoretically -- ANY connection with holonomy
contained in `H=SU(3)` has curvature valued in the 8-dim adjoint, which by
Schur has no `3̄`-component, regardless of the specific geometry of
`S⁶=G2/SU(3)`. Nothing about this coset specifically was needed. This
does not change the verdict (the candidate is still correctly closed) but
is worth flagging for the orchestrating session's own methodology
awareness when scoping future OB14 candidates: a one-paragraph
representation-theory check (holonomy group vs. target irrep dimension)
can sometimes close a candidate before any numeric construction is
needed -- see pearl_registry entry below.

**Tier: `[VERIFIED-tool]`** for all of T1-T4 (direct numeric computation,
19/19 checks passed, `results_c165.json` persisted) -- not `[HYPOTHESIS]`
or `[INFERRED]`: the zero result is a directly computed, machine-precision
numeric fact, and the Schur's-Lemma argument that predicted it is a
standard, citable mathematical theorem (irreducible representations of a
simple Lie algebra; non-isomorphic irreducibles have no nonzero equivariant
maps between them), not a novel derivation specific to this project. No
physics claim about `S^6`, `su(3)`, or `N_gen=3` is made or implied beyond
resolving the one specific candidate-independence question C164 Section 9
raised.
