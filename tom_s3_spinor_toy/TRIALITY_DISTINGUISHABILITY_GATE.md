# Triality Distinguishability Gate — status audit (Round119, 2026-07-17)

**Gauge/Hilbert/Triality closure program, item 4** of the user's own 8-step
sequence (after `SPIN13_TO_SPIN4_DECOMPOSITION.md` and the round118
matter-generation factorization test).

**What this file is:** a dated application of an *already-built* gate to an
*already-verified* candidate — not a new gate, not new physics. The gate
itself (precise question, five-condition existence spec, anti-circularity
screen, PASS/PARTIAL/NO/DISQUALIFIED rubric) was built in
[`L3B_SPIN8_INTERFACE_SPEC.md`](L3B_SPIN8_INTERFACE_SPEC.md) on 2026-07-15
and is not duplicated here. What that document had not yet done, as of this
round, is apply its own §4 rubric formally to its own most-advanced
same-day result and propagate the verdict into the project's status
registries (`OPEN_BLOCKERS.md`, `CLAIM_LEDGER.yaml`), which currently
undersell it.

## 1. The gate being applied (cited, not rebuilt)

Per `L3B_SPIN8_INTERFACE_SPEC.md` §2-§4: L3b (channel independence) closes
only if an object `(F, U, ρ)` exists satisfying five conditions — a unitary
triality operator `U` on a 24-dim fiber `F = 8_v⊕8_s⊕8_c` (condition 1,
already geometrically given, not new); the physical Dirac operator commuting
with `U` (condition 2); a genuine Spin(8) action extending `U` with three
pairwise-inequivalent irreps (condition 3); physical (not just mathematical)
inequivalence of the three sectors (condition 4); and the corresponding
projectors surviving compactification to 4D (condition 5). A candidate must
also pass the §3.5 anti-circularity screen: does it *derive* three
distinguishable sectors from the *same* triality automorphism already fixed
by condition 1, or does it *postulate* three separate copies matching the
desired count from the outset (the Furey-Hughes trap, explicitly named and
rejected in that document)?

## 2. The candidate being evaluated (cited, not recomputed)

`L3B_SPIN8_INTERFACE_SPEC.md` §1 (lines ~390-602, all same-day, 2026-07-15)
constructs and verifies, by direct Clifford-algebra computation: split
`𝕆=ℝ⁸` into two 4-dim blocks (`H`, `Hℓ`), take the full `SO(4)×SO(4)`
(not restricted to octonion automorphisms), define block-chirality operators
`Γ_A, Γ_B`. Result: `8_s` is the same-block-chirality sector
(`Γ_A=Γ_B`), `8_c` is the opposite-block-chirality sector (`Γ_A=-Γ_B`) —
**the first candidate in that document's entire investigation to
distinguish all three channels, not just `v` from `{s,c}`.** Further
verified same day: the `SO(4)×SO(4)` subalgebra is itself genuinely
triality-invariant (eigenvalues of the transport matrix `T` are exactly
`{+1(×6), ω(×3), ω̄(×3)}`, `T³=I`), and the vector-rep and spinor-rep
findings are the *same* structure (explicit intertwiners `P, Q` built,
residuals ~1e-15).

## 2b. A second, independent candidate found (round124, 2026-07-18)

**User-requested new route via `SU(3)`-representation coordinates**, not
the octonion `H⊕Hℓ` split above. Combining `su(3)` (the isotropy
subalgebra of `S⁶=G₂/SU(3)`) with its OWN centralizer in `so(8)`
(2-dimensional, abelian — already computed by gate G102, `[VERIFIED]`
`dim=2`) gives a rank-4 algebra `su(3)⊕u(1)⊕u(1)` (rank `2+1+1=4`, the
same rank-escape mechanism as `SO(4)×SO(4)`). Result, `[VERIFIED-tool]`,
independently re-run and checked for basis-rotation invariance (two
different rotated bases of the same 2-dim centralizer span give identical
results):

| Quantity | `su(3)` alone (G102) | `su(3)⊕u(1)⊕u(1)` (round124) |
|---|---|---|
| `Hom(α,α)`, all three | 6 | 4 |
| `Hom(α,β)`, `α≠β`, all three pairs | 6 | **0** |
| Fixed vectors in `8_v` | 2 | **0** |

`Hom=0` for all three off-diagonal pairs is a direct Schur-lemma proof of
pairwise non-isomorphism — arguably cleaner than the `SO(4)×SO(4)`
route's explicit same/opposite-block-chirality matching argument. Zero
fixed vectors in `8_v` confirms this algebra also escapes confinement to
`SO(7)`, the same structural signature that let `SO(4)×SO(4)` work.

**Same remaining obstruction, not a further advance:** `g₂` is simple
(zero center), so it has no room for an abelian ideal commuting with its
own `su(3)` subalgebra beyond `su(3)` itself — the 2-dim centralizer used
here sits OUTSIDE `g₂`, in the larger `so(8)`. Realizing `su(3)⊕u(1)⊕u(1)`
physically would therefore ALSO require breaking `G₂`, triggering the
identical G74A Lemma B obstruction (§3 below) as `SO(4)×SO(4)`. Physical
identification of the two `u(1)` charges with any known quantum number is
also unattempted, the same gap as `SO(4)×SO(4)`'s unidentified factors.

**Consequence:** two independent, structurally different rank-4 algebras
now both achieve algebraic distinguishability (`GATE 1 OF 7`'s
prerequisite) via two different mechanisms (octonion block-chirality vs.
isotropy-group centralizer) — this strengthens confidence that Gate 1 is
genuinely, robustly satisfied, but does not touch Gates 2-6, which remain
exactly as open as before. See
`experiments/20260718-round124-su3-centralizer-triality-candidate/decision.md`
for full detail.

## 3. Applying the gate

**First-draft table (below) was skeptic-reviewed; two cells corrected, not
silently rewritten — see the "Skeptic correction" notes attached to each.**

| Condition (§3) | Status per `L3B_SPIN8_INTERFACE_SPEC.md`'s own record |
|---|---|
| 1 — `U` exists, `U³=1` | **Holds** — the baseline geometric `ℤ₃` triality automorphism, already established before any candidate (§2's own parenthetical: "this operator is not new, it is the geometric input already in the paper"). |
| 2 — `[D,U]=0` for the *physical* Dirac operator | **Undetermined, not merely unverified [skeptic correction].** First draft called this "holds at the bare-geometry level... not independently re-verified." Skeptic found this understates the problem: §3's condition 2 explicitly means the *physical* `D`, and the `SO(4)×SO(4)` route *requires* breaking `G₂` (source line 433: "using the full 12-dimensional group necessarily breaks `G₂`-invariance"). The source's own G74A discussion (lines 622-644) shows Lemma B's proof "does not degrade gradually with perturbation size; it simply no longer applies, at any nonzero perturbation" once `G₂` breaks. So the physical-`D` case isn't just "not yet checked" — the source's own tooling says it cannot be checked this way at all; a genuinely new argument would be needed. |
| 3 — a *Spin(8)* action extending `U`, three pairwise-inequivalent irreps, commuting with the physical Hamiltonian on the *full compactification* | **Only the algebraic half holds [skeptic correction].** First draft claimed this condition "Holds, verified" in full. Skeptic found this conflates two things the source itself keeps separate: `SO(4)×SO(4)` is a 12-dim proper subgroup of the 28-dim `Spin(8)`, not a full `Spin(8)` action — and the source's own §7 (added *after* §3/§4, more granular) marks only gate 1 ("are `8_v,8_s,8_c` algebraically distinguished as `K=Spin(4)²`-branchings?") as "already done today, verified," while gate 2 ("does `K` act globally... over the actual compactification") is named explicitly as "**the blocker**, needs Part 5." Condition 3 as stated in §3 bundles the algebraic-distinguishability half (done) with the global/physical half (open) — only the former is established. |
| 4 — physical (not just mathematical) inequivalence | **Open** — per the document's own final assessment: "Nothing establishes that either `SO(4)` factor corresponds to `S³`'s actual `SU(2)_L×SU(2)_R` gauge fields." Blocked on Part 5 (unpublished, not solicited per this project's standing constraint). |
| 5 — projectors survive compactification | **Open** — same blocker; §7 gate 2 is explicitly named "the blocker, needs Part 5." |

**§3.5 anti-circularity screen:** **PASSES**, but the stated reason in the
first draft was itself wrong [skeptic correction]. First draft argued the
screen passes because "the three falls out of the transport matrix `T`'s own
eigenvalue structure (`{+1(×6), ω(×3), ω̄(×3)}`)" — skeptic found those
eigenvalues describe how the 12-dim `SO(4)×SO(4)` *subalgebra itself*
decomposes under triality (6+3+3), which is a different fact from what
distinguishes the three *channels*. The actual distinguishing structure is
`Γ_A, Γ_B` (source lines 410-418), derived from the discrete choice of
quaternionic subalgebra `H=span(e₀,...,e₃)` — a choice that itself breaks
`G₂` (line 432-434: `SO(4)²∩G₂` is only 6-dim). **Corrected reasoning:** the
screen still passes, because this discrete choice acts on the *same* single
octonion fiber and the *same* triality automorphism already fixed by
condition 1 — it is not three independently-postulated copies (the
Furey-Hughes pattern) — but the "falls out of `T`'s eigenvalues" justification
in the first draft was the wrong citation for the right conclusion.

**Cross-check against `L3B_SPIN8_INTERFACE_SPEC.md` §7's own later,
gate-based framing — genuine discrepancy with §3/§4, not "no discrepancy"
[skeptic correction].** First draft claimed "no discrepancy found between the
document's two internal framings (§3/§4 vs §7)." Skeptic found this is
wrong: §7 is a *sharper* re-framing, specifically because it splits what §3's
condition 3 bundles together (algebraic distinguishability vs. global
physical action) into separate gates (1 vs. 2). Applying §3/§4's coarser
condition-3 language gives a more generous reading than applying §7's own
finer gate table to the same evidence. This is a real internal-consistency
gap in the source document's two framings, not a confirmation that they agree.

## 4. Verdict

**First draft's flat `PARTIAL` label was skeptic-reviewed and found stronger
than the source's own record supports — corrected below, not silently
rewritten.**

Per `L3B_SPIN8_INTERFACE_SPEC.md`'s own §4 rubric, `PARTIAL` requires "a
genuine Spin(8) symmetry commuting with `D`" to exist — per §3 above, only
the algebraic-distinguishability half of that is established; the
global/physical half is exactly what the source's own §7 gate 2 flags as
"the blocker." A flat `PARTIAL` label therefore overclaims relative to the
source's sharper §7 framing.

**Corrected verdict: narrower than `PARTIAL`, stated using the source's own
§7 gate numbering rather than forcing it into one of the four §4 bins.**
`GATE 1 OF 7 DONE` (algebraic distinguishability of all three channels, and
triality-invariance of the `SO(4)×SO(4)` subalgebra itself, both verified in
the source) — `GATES 2-6 OPEN` (global principal-bundle action, gauge-orbit
audit, zero-mode map after `K` acts on the full construction, derivation of
a 4D effective action, basis-invariant-observable check — all blocked on
Part 5, per the source's own words). Gate 7 (anti-circularity) passes, per
the corrected §3.5 reasoning above.

This is still **not** `NO` (a genuine algebraic distinguishing structure was
found — this contradicts a flat "no candidate exists" reading) and **not**
`DISQUALIFIED` (passes the anti-circularity screen, corrected reasoning).
It sits between `NO` and `PARTIAL` on the source's own four-bin rubric,
which is why the source's own finer §7 table — not a forced §4 label — is
the honest way to state it.

## 5. Cross-check against Round118 (matter-generation factorization)

**First draft of this section contained a hard arithmetic/category error,
caught by skeptic review — corrected below, not silently rewritten.** First
draft claimed "`SU(3)×SU(2)×SU(2)` embeds inside `SO(6)` (rank 3), same rank
ceiling as every `G_2`/`SO(7)`-subgroup candidate." This is wrong on two
counts: (a) `SU(3)×SU(2)×SU(2)` has rank `2+1+1=4`, not 3 — a rank-4 group
cannot embed in rank-3 `SO(6)` at all, by the exact maximal-torus argument
this same document correctly uses elsewhere against `SO(4)×SO(4)`
embedding in `SO(7)`; (b) more fundamentally, `SU(2)_L×SU(2)_R` is realized
on the **`S³` factor** (as `SO(4)≅SU(2)×SU(2)` acting on the `S³` frame
bundle), not as a subgroup of `SO(6)` acting on `S⁶` at all — only
`SU(3)_c` (rank 2, from `SO(6)⊃SU(3)×U(1)`) is even the right *kind* of
object to compare against the `S⁶`-side `G_2`/`SO(6)`/`SO(7)`-subgroup
candidates this document's §1 rules out. The "same rank ceiling" analogy in
the first draft conflated an `S³`-side gauge factor with an `S⁶`-side one.

**Corrected, much more modest connection:** Round118
([`experiments/20260717-round118-matter-generation-factorization-test/`](experiments/20260717-round118-matter-generation-factorization-test/decision.md))
found, independently, that the charge formula (`Q=T₃L+Y`) is channel-uniform
across `8_v/8_s/8_c`. That result and this gate's finding both bear on
channel-distinguishability, but no supported argument connects them beyond
that surface-level observation — the rank/embedding reasoning that would
have made the connection precise does not hold, per the correction above.
Round118's own `OB11` question (does triality act purely as `1⊗t` with no
admixture on the matter factor, for the already-realized gauge content) and
this gate's condition-4/5 gap (does `SO(4)×SO(4)`-breaking, if physically
realized, introduce channel-mixing terms) remain two separately open
questions. **Flagged as a possible connection worth checking directly
(does an explicit `SO(4)×SO(4)`-breaking term introduce off-diagonal terms
between the `S⁶` channels in the full Dirac operator?), not an established
one.**

## 6. What this does NOT mean

1. Does NOT close L3b — conditions 4-5 remain open, blocked on Part 5
   (unpublished, not solicited).
2. Does NOT change `N_gen=3`'s conditional status, `lambda=FREE_COUPLING_
   PARAMETER`, or `safe_for_runtime=False`.
3. Does NOT redo any verified computation from `L3B_SPIN8_INTERFACE_SPEC.md`
   — all cited, none recomputed.
4. Does NOT claim Tom Lawrence's framework supplies this structure — open
   for his framework specifically (§5 of the spec document).
5. Does NOT resolve the OB4/OB11 connection flagged in §5 above — a
   scoped-but-not-attempted next step, not a finding.

## 7. Registry updates made this round

- `OPEN_BLOCKERS.md` OB4 — updated from "not internally derivable, model
  postulate" (undersells the `SO(4)×SO(4)` finding) to the corrected `GATE 1
  OF 7 DONE / GATES 2-6 OPEN` status (not `PARTIAL` — see §4 correction
  above).
- `CLAIM_LEDGER.yaml` `C_G67C3_THIRD_CHANNEL` — `evidence_status` and `notes`
  updated to cite the `SO(4)×SO(4)` candidate and this gate's corrected
  verdict, `truth_status` remains `OPEN` (conditions 4-5 unresolved).

## 8. C75 update (2026-08-11) — Gate 2 tested directly, for round124's candidate: NO

**What changed and why this was newly possible.** Row "2" of the §3 table
above says Gate 2 (`[D,U]=0` for the *physical* `D`) is "Undetermined... the
source's own tooling says it cannot be checked this way at all" — because at
the time this document was written, no round had *both* a real, non-surrogate
physical Dirac operator *and* a verified bridge into its representation
space at the same time. Both pieces now exist independently of this document
(round59's `D`, extensively characterized by C73/C73b this session; C70's
verified intertwiner `U_v` bridging round59↔round124's `so(8)` construction),
so C75 (`experiments/20260811-c75-gate2-physical-d-vs-extended-symmetry/`)
ran the direct test for the first time.

**Candidate tested:** round124's `su(3)+u(1)+u(1)` centralizer construction
(§2b above) — the SPECIFIC Gate-1 candidate this document already treats as
established, not the `SO(4)×SO(4)` route (§2), which was never bridgeable to
a physical `D` at all.

**Result: NO.** `[D, Leibniz(u1_a)]` and `[D, Leibniz(u1_b)]` (the two extra
centralizer generators, transported to `Sigma` via `U_v`) are both large and
nonzero — Frobenius norms `5.241` and `28.187` against `|D|_F=8.000` (65.5%
and 352% relative violation respectively), many orders of magnitude above a
positive-control noise floor of `2.8e-17` (confirmed via the genuine su(3)
generators, which `D` IS known to commute with). This is not a small,
perturbative effect — it computationally confirms this document's own §3 row
2 reasoning (citing G74A's Lemma B: "does not degrade gradually with
perturbation size; it simply no longer applies, at any nonzero perturbation")
for the first time with an actual number, rather than as an abstract
argument.

**Updated status for this candidate:** `GATE 2: TESTED, NO` (was
`Undetermined`). Gates 3–6 remain open regardless — Gate 2 failing for this
candidate does not touch them, and no other candidate has been bridged to a
physical `D` to re-attempt Gate 2 differently.

**Explicit non-transfer, stated per this project's own Gate 1 provenance
discipline:** this result says nothing about the `SO(4)×SO(4)` candidate's
own Gate 2 status (§2, still untested — no bridge to a physical `D` exists
for it) or about `predictions_before_data.md`'s separate, harder
channel-permutation/redundancy commutant test (still fully open — see C75's
own `decision.md` for why that is a different question this round does not
attack).

## Sources

- `tom_s3_spinor_toy/L3B_SPIN8_INTERFACE_SPEC.md` §1 (SO(4)×SO(4) candidate,
  lines ~390-686), §2-§4 (gate definition), §3.5 (anti-circularity), §7
  (gate table)
- `tom_s3_spinor_toy/experiments/20260717-round118-matter-generation-factorization-test/decision.md`
- `tom_s3_spinor_toy/experiments/20260705-g102-spin8-fiber-obstruction/decision.md` (G102)
- `tom_s3_spinor_toy/experiments/20260811-c75-gate2-physical-d-vs-extended-symmetry/decision.md` (§8, Gate 2 tested directly)
- `tom_s3_spinor_toy/experiments/20260718-round124-su3-centralizer-triality-candidate/decision.md`
  (second independent candidate, `su(3)⊕u(1)⊕u(1)`)
- `tom_s3_spinor_toy/OPEN_BLOCKERS.md` OB4, OB11
- `tom_s3_spinor_toy/CLAIM_LEDGER.yaml` `C_G67C3_THIRD_CHANNEL`
