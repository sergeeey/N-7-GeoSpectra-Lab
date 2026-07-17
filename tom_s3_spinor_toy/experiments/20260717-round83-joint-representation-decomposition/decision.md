# E16 (round83) — Decision

> **⚠️ Provenance correction (2026-07-17, added after this file was written):**
> this file's citations of "G74A" for `dim ker(D_{S6,twisted})=1` point to a
> superseded argument (G74A's own two lemmas are now known to be
> insufficient, per `preprint.tex`'s own current text) — the $\dim\ker=1$
> NUMBER is correct and this file's PASS verdict is unaffected (the argument
> here only used the fact that the S6-side kernel is 1-dimensional and
> unique, not which proof establishes that), but the correct citation is the
> later `dolan-casimir-g2su3`+`round59` computation, not G74A. See
> `reports/PROJECT_360_ROUND3_SYNTHESIS.md`, "Provenance correction" section.

**Date:** 2026-07-17
**Verdict:** `PASS__ONE_WEAK_ISOSPIN_DOUBLET__NARROW_SCOPE`
**Go/no-go:** This resolves the SPECIFIC question E12/E13/KT-13 left open
(whether the 2-vs-1 excess per triality channel is genuine family duplication,
or expected internal SU(2) structure): the honest answer, from this project's
own already-established artifacts, is **the latter** — PASS. This does **not**
by itself certify the torsion-escape-route program as complete, physical, or
selected; those separate open items (H1c, KT-8, whether both `t=0` and `t=1`
sectors are simultaneously required for a full generation) are untouched. Read
"What this does NOT mean" before citing this as closing E12/E13's gap in full.

## Bottom line, stated plainly first

The two basis states of `ker(D_{S3,t}) ⊗ ker(D_{S6,twisted})` (one fixed
channel) are **the two `T₃`-components of a single irreducible SU(2)
weak-isospin doublet**, not two independent copies of the same particle. This
follows from four already-established, tool-verified facts combined with one
newly-checked structural point:

1. **[VERIFIED-tool, round77/E11]** The 2-dim S3-side kernel is an exact
   fundamental-representation `SU(2)` doublet (differing in `T₃`), not two
   unrelated states — reconfirmed independently in this experiment's own
   script, Part 2 (see Section A below).
2. **[VERIFIED-tool, E14/round80 + E15/round81]** This doublet is irreducible
   under the surviving SU(2) — two independent methods (an isometry/`Z2`
   search, and a Clifford-algebra/Schur's-lemma argument) both confirm no
   SU(2)-invariant or Clifford-algebra-natural operator can split it into two
   separate 1-dim pieces.
3. **[VERIFIED-tool, G74A/G74B; DOCS, round82]** The S⁶-side chirality
   (`sign(ind)=+1`, `L=1,R=0` per channel) and the triality-channel label
   (G73/G67) are properties of the S⁶ factor **alone** — round82 already
   tool-verified, by direct citation of G73/G74A/G74B's own derivations, that
   no S³ quantity appears anywhere in either computation.
4. **[CODE, direct Read + this experiment's script Part 1]** This project's
   own S³-side quantum-number bookkeeping (G6) assigns ONLY `(T3L, T3R,
   chir_s3)` to an S3-side state — no SU(3)/color/B-L field is ever defined
   there. There is no competing bookkeeping anywhere in this project that
   could assign DIFFERENT SU(3)/B-L labels to the two S3-side kernel states.
5. **[VERIFIED-tool, this experiment's script Part 3]** Given (3)+(4) and the
   already-established tensor-product kernel identity
   `ker(D_full)=ker(D_S3)⊗ker(D_S6)` (E12 Section C, dim ker(D_S6,twisted)=1),
   BOTH joint-kernel basis vectors are (their own S3 vector) tensored with the
   **exact same, single, fixed** S⁶ vector — so any operator that depends only
   on the S⁶ factor (whatever specific SU(3)/B-L/triality-channel value that
   factor turns out to carry) necessarily gives the identical eigenvalue on
   both. This is checked concretely with a toy operator in Section C below,
   not merely asserted as "obvious by linearity."

Together: same SU(3)/channel label (2), same S⁶-side chirality (3), same
(whatever it is) B-L-type charge (5) — because all three are properties of
the one shared S⁶ factor — but DIFFERENT `T₃` (1) under the SAME `SU(2)`
factor (2). This is **exactly** the pre-registered PASS criterion.

## Result, section by section

### Section A — the S3-side doublet, reconfirmed independently [VERIFIED-tool]

Script: `e16_joint_representation_check.py`, Part 2. Built the S3-side kernel
basis `v1=(1,0)`, `v2=(0,1)` (the full `C²` is the kernel at `t=0`, per
E9/E12) and a generic `SU(2)` element `h(y)=y0*I+y1*Z1+y2*Z2+y3*Z3` in this
project's own concrete Pauli/quaternion matrix family (`Z_i=i*sigma_i`, the
SAME convention used throughout E9/E10/E11/E12). Result:

```
h*v1 = (y0 + i*y3, i*y1 - y2)   -- moved by generic h: True
h*v2 = (i*y1 + y2, y0 - i*y3)   -- moved by generic h: True
doublet_confirmed = True
T3(v1) = 1/2, T3(v2) = -1/2, different_T3_eigenvalues = True
```

This reproduces round77/E11's already tool-verified finding
(`psi0_is_SU2R_doublet_not_singlet=true`,
`psi1_is_SU2L_doublet_not_singlet=true`) on this project's own basis, and adds
the explicit `T₃`-eigenvalue computation (`+1/2` vs `-1/2` under the standard
Cartan generator `sigma3/2`) that licenses calling `v1,v2` the two `T₃`
components of one doublet, rather than merely "two vectors that transform
nontrivially."

**Which SU(2) is this, L or R?** Per round77's own already-flagged, unresolved
caveat (reused here without re-deriving): "`SU(2)_L`=left-translation" is an
IMPORTED convention, not stated anywhere in `preprint.tex`
(grep re-confirmed by round77/E13, not re-run in this experiment). Under that
convention, at `t=0` this is the `SU(2)_R` doublet (round77); at `t=1` under
`c0=-2`, the mirror `SU(2)_L` doublet. **This labeling ambiguity does not
affect the PASS/FAIL question** — it only affects which name (`L` or `R`) is
attached to "the surviving SU(2)," not whether the 2-dim space is one doublet
or two copies.

### Section B — G6's own bookkeeping assigns no SU(3)/B-L field to an S3 state [CODE]

Direct Read of
`experiments/20260615-g6-s3xs6-spinor-content/g6_spinor_decomposition.py`,
lines 29-36:

```python
s3_states = [
    {"T3L": sp.Rational(1, 2), "T3R": sp.Integer(0), "chir_s3": "+"},
    {"T3L": sp.Rational(-1, 2), "T3R": sp.Integer(0), "chir_s3": "+"},
    {"T3L": sp.Integer(0), "T3R": sp.Rational(1, 2), "chir_s3": "-"},
    {"T3L": sp.Integer(0), "T3R": sp.Rational(-1, 2), "chir_s3": "-"},
]
```

Every S3-side state carries exactly three fields: `T3L`, `T3R`, `chir_s3`.
The SU(3)-representation-assigning function `su3_label()` (lines 72-102) and
the B-L-assigning function `bl_charge()` (lines 40-69) BOTH take only the
**S⁶ weight** `(±1/2,±1/2,±1/2)` as their argument — neither is ever called
with, or defined in terms of, an S3-side quantity anywhere in the file
(confirmed by reading the file in full; `n=0` loop at lines 157-174 builds the
32-state product strictly as `T3L,T3R` from `s3` × `BL,su3,color` from `s6`,
with no cross term). This experiment's script Part 1 re-imports these exact
dicts verbatim (not retyped with any new field) and confirms programmatically:

```
Keys G6 assigns to an S3-side state: ['T3L', 'T3R', 'chir_s3']
no_su3_or_bl_field_on_s3_side = True
```

**Direct answer to the assigned question:** this project's own quantum-number
bookkeeping does NOT assign a triality-channel/SU(3) label, or a B-L charge,
to an S3-side state at all, in ANY artifact. Triality-channel and B-L are, in
this project's existing bookkeeping, purely S⁶-side properties.

### Section C — the "shared S⁶ factor" argument, made concrete [VERIFIED-tool]

Confirmed independently by `preprint.tex:1533-1536` (Fermion mass hierarchy
item, `\S`Universality context): "in the construction that defines
`N_gen=3`... the `S³` spinor factor is a **fixed, generation-independent
block**, and the generation index lives **entirely within the S⁶/octonion
triality structure** — so no such cross-term can exist." This is the paper's
own explicit statement that the S³ factor carries no generation/channel index
of its own — fully consistent with Section B's code-level finding.

Given this, and E12 Section C's already tool-verified identity
`ker(D_full)=ker(D_{S3,t})⊗ker(D_{S6,twisted})` (with `dim ker(D_{S6,twisted})
=1` per channel, G74A), every vector in the 2-dim joint kernel for a FIXED
channel is `v⊗w` for `v` ranging over the 2-dim S3 kernel and `w` a SINGLE
FIXED S6 vector (up to overall complex scale) — because a 1-dimensional
kernel has only one basis direction. **Whatever quantum number that shared
factor `w` carries (channel label, chirality, any future-assigned B-L/SU(3)
value), it is necessarily identical for both `v1⊗w` and `v2⊗w`.**

This experiment's script Part 3 makes this concrete with an explicit toy
computation (not a re-verification of the physical operators themselves,
which is E12/G74A's job, but a check that the LOGICAL structure of the
argument is sound): built a toy 2×2 `D_S6` with 1-dim kernel `w=(1,-1)`, a
toy "S6-only conserved quantum number" operator `Q_S6` that commutes with
`D_S6` (so it preserves the kernel, i.e. represents a genuine conserved
S6-side label), and checked directly:

```
D_S6 * w == 0 (w spans ker D_S6):        True
[D_S6, Q_S6] == 0 (Q_S6 is S6-conserved): True
Q_S6 acts as scalar mu=2 on w:            True
(I_S3 (x) Q_S6) * (v1(x)w) == mu*(v1(x)w): True
(I_S3 (x) Q_S6) * (v2(x)w) == mu*(v2(x)w): True
same_S6_eigenvalue_on_both_joint_states = True
```

Both joint-kernel basis vectors receive the IDENTICAL eigenvalue `mu` under
the S6-only operator, while (Section A) the same two vectors receive
DIFFERENT eigenvalues (`+1/2` vs `-1/2`) under the S3-side `T₃` operator. This
is precisely the structural signature of "one doublet, not two copies."

### Section D — consistency with E13's CPT/particle-antiparticle finding [DOCS, reused]

Per E13 (round79), the particle/antiparticle (CPT-conjugate) doubling in this
project's existing bookkeeping is carried ENTIRELY by the S6 factor's B-L
sign, NOT the S3 factor — confirmed there by direct computation on G6's own
table (`cpt_doubling_independent_of_chir_s3 = True`, all 8 checked
particle/antiparticle pairs share `chir_s3`). This is fully consistent with
what is found here: the S3-side doublet's two `T₃` components are NOT related
by CPT conjugation (that operation, in this project's bookkeeping, lives
entirely on the shared S6 factor and is orthogonal to which `T₃` component of
the S3 doublet is being tensored with it). The two `T₃` components are two
genuinely distinct weak-isospin partners (structurally analogous to, e.g.,
`u_L` and `d_L` within the same `SU(2)_L` doublet of the same generation — a
completely standard multiplet structure, not a duplication), not a
particle/antiparticle pair and not two copies of one particle.

## Applying the pre-registered criteria

| Criterion | Same/Different across the 2 joint-kernel basis states | Basis |
|---|---|---|
| `SU(3)_c` / triality-channel label | **SAME** | Section C (shared S6 factor); Section B/preprint.tex:1533-1536 (S3 carries no channel label of its own) |
| `B-L` charge | **SAME** (in the sense: whatever value the twisted-kernel S6 factor carries, it is shared — this project has not explicitly tabulated a numeric B-L value for the twisted `S⁻`-kernel object specifically, see caveat below) | Section C (shared S6 factor); Section B (no S3-side B-L field exists to differ) |
| S⁶-side chirality / `sign(ind)=+1` (G74B) | **SAME** | Section C (shared S6 factor); G74A/G74B/round82 (chirality is an S6-only property) |
| `SU(2)_L×SU(2)_R` (`T3L`,`T3R`) | **DIFFERENT** (`T₃=+1/2` vs `-1/2` under the same SU(2) factor; both singlets under the other factor) | Section A (round77/E11, reconfirmed here) |

This matches the **PASS** row exactly: same triality-channel/SU(3), same B-L
(in the shared-factor sense), same S6-side chirality, different `T₃` under
the same `SU(2)` factor — one weak-isospin doublet, not two family copies.

**FAIL is directly and cleanly ruled out**, not merely "not confirmed": FAIL
requires the two states to have IDENTICAL full quantum numbers, including
`T₃` — but Section A shows `T₃=+1/2` for `v1` and `T₃=-1/2` for `v2`,
confirmed both by round77's original computation and by this experiment's own
independent re-derivation. Two states with different `T₃` eigenvalues are, by
definition, not identical copies.

**BLOCKED is not the honest verdict here**, despite the genuine gap that
this project has never explicitly tabulated a numeric B-L/SU(3)-representation
value for the twisted `S⁻` kernel object (as opposed to G6's untwisted 8-weight
bookkeeping) — because the relevant question for PASS/FAIL is not "what is the
value" but "is it the SAME for both states," and that narrower question is
answered by the shared-factor structural argument (Section C) independent of
knowing what the value is. If a future need arises to know the ACTUAL
numeric B-L/SU(3)-representation content of the twisted kernel (e.g. to check
anomaly cancellation for the "3" version of the theory, or to reconcile with
G6's "32-state, one generation" convention as E12/E13 already flagged remains
open), that WOULD require the richer bookkeeping this decision's BLOCKED
criterion anticipates — but it is not needed to answer the specific
PASS/FAIL question this experiment was asked.

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result kills:** the reading (implicitly worried about by E12's
  own "Excess factor 2" framing, and explicitly named as a legitimate FAIL
  possibility in this experiment's own pre-registration) that the S³-side
  kernel's multiplicity 2 represents two independent, degenerate copies of
  the same particle content (would give a genuine `N_family=6` doubling). That
  reading is now cleanly and specifically refuted: the two states have
  different `T₃` eigenvalues under the same SU(2) factor, not identical
  quantum numbers.
- **What this result does NOT kill:** E12/E13's own finding that the
  multiplicity is 2, not 1, at the level of raw dimension count — that stands
  exactly as established. It also does not kill any of the still-open items
  E12/E13/E14 already flagged: H1c (physical selection of `t`), KT-8 (full
  9D operator zero-mode existence), or the separate question (E12 Section
  E.2, E14 Reading 3) of whether the escape route needs BOTH the `t=0` AND
  `t=1` doublets simultaneously to supply a complete single generation's full
  `(2,1)⊕(1,2)` content.
- **What survives, confirmed stronger than before:** the "multiplicity 2 = one
  weak doublet, not family duplication" reading, which E12 Section E.2 already
  flagged as "real but unresolved" (blocked there because E12 had not checked
  G6's own `chir_s3` table nor the shared-tensor-factor structural argument),
  is now supported by a direct combination of (a) round77/E11's representation
  labels, (b) E14/E15's irreducibility results, (c) G6's own field inventory,
  (d) `preprint.tex`'s own "generation-independent S3 block" statement, and
  (e) a concrete toy verification of the shared-factor argument. This closes
  the SPECIFIC sub-question E12/E13 left open (is 2 malignant or benign?) with
  an honest PASS, without overclaiming resolution of the LARGER open items
  (H1c, KT-8, full-generation completeness) that are independent of it.

## Relaxation Map (for future work, if this PASS is revisited)

| Option | What it would require |
|---|---|
| Reconcile with G6's "32-state, one generation" convention (E12 Section E.2, E13 Section C) | Still open, unchanged by this experiment: does the escape route need to supply the OTHER doublet too (the `t=1` sector if `t=0` is realized, or vice versa) to match `preprint.tex:292-298`'s full `(2,1)⊕(1,2)` convention? This experiment shows the multiplicity-2 excess WITHIN one sector is benign; it does not address whether BOTH sectors are separately required |
| Explicit numeric B-L/SU(3)-representation value for the twisted `S⁻` kernel | Not needed for this experiment's PASS verdict (Section C's shared-factor argument does not require it), but WOULD be needed for a future anomaly-cancellation check on the "3-total-channel" internal content, or to fully reconcile with G6's untwisted 32-state table (E13's own remaining open item) |
| Independent verification of the `SU(2)_L`=left-translation convention | Unchanged from E11/E13: still an imported, not paper-derived, assumption; does not affect this experiment's PASS verdict, only terminology |
| Verify the `D_full²` decoupling assumption for the torsion-deformed S3 factor | Unchanged from E2/E12: this experiment's classification is conditional on it holding, exactly as E12's own multiplicity-2 finding is |

## Assumptions carried, unresolved

- `D_full² = D_{S3,t}²⊗I + I⊗D_{S6,twisted}²` (E2/E12's own
  `[INFERRED, NOT independently literature-verified]` assumption) — this
  experiment's classification presupposes it holds, exactly as E12/E13's own
  findings do; if it fails, the entire premise (including this PASS) is
  separately in question.
- `SU(2)_L`=left-translation (E11's imported convention, `preprint.tex` never
  states this) — does not affect PASS/FAIL, only which name is attached to
  "the surviving doublet."
- No explicit numeric B-L/SU(3)-representation value has ever been assigned
  in this project to the twisted `S⁻` kernel object specifically (as opposed
  to G6's untwisted 8-weight bookkeeping) — this experiment's PASS verdict
  does not require that value, only that it is SHARED between the two joint
  states (Section C), which is a strictly weaker and separately-justified
  claim.

## What this does NOT mean

1. Does **not** establish H1c (physical selection between `t=0` and `t=1`, or
   whether either is ever realized) — untouched.
2. Does **not** resolve KT-8 (whether ANY zero mode of the untwisted `D_full`
   exists) — untouched.
3. Does **not** certify the torsion-escape-route program as physically
   complete or selected — even under this PASS, the program still needs (a)
   a physical selection principle for `t` (H1c, open), and (b) a resolution of
   whether BOTH the `t=0` and `t=1` doublets are simultaneously required to
   match `preprint.tex`'s full one-generation convention (E12 Section E.2,
   E14 Reading 3, both still open) — neither is addressed by this experiment.
4. Does **not** re-derive or challenge G73/G74A/G74B's own S⁶-only results —
   reused here purely by citation, consistent with round82's independent
   confirmation that these are untouched by anything on the S³ factor.
5. Does **not** claim a specific numeric B-L or SU(3)-representation VALUE for
   the twisted `S⁻` kernel state — only that whatever that value is, it is
   necessarily shared between the two joint-kernel basis states, which is a
   distinct and strictly weaker (but sufficient for PASS/FAIL purposes) claim.
6. Does **not** imply the multiplicity-2 finding (E12/E13, KT-13) was in any
   way computationally wrong — the dimension count of 2 (not 1) per channel
   stands exactly as established; what this experiment adds is the
   representation-theoretic READING of that dimension-2 space, not a
   recomputation of its size.
7. Does **not** claim novelty in the underlying representation-theory fact
   that an irreducible SU(2) doublet's two members share every OTHER quantum
   number while differing in `T₃` — this is standard weak-isospin
   multiplet structure (e.g. `u_L`/`d_L`); what is new here is the concrete,
   tool-verified demonstration that THIS project's own specific tensor-product
   kernel construction actually has this structure, checked rather than
   assumed.

## Check (reproduces this decision)
`python e16_joint_representation_check.py` →
`verdict.no_su3_or_bl_field_on_s3_side==True`,
`verdict.doublet_confirmed==True`,
`verdict.different_T3_eigenvalues==True`,
`verdict.same_S6_eigenvalue_on_both_joint_states==True`,
`verdict.structural_pass_supported==True`,
`verdict.label=="STRUCTURAL_SUPPORT_FOR_ONE_WEAK_DOUBLET"`.
