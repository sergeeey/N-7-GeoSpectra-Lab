# C125 decision -- the full gauge-equivalence gate for the `t=0` vs `t=1` pair.
#
# THEOREM STATEMENT, class-qualified in the first line per this project's own
# C124 precedent: on `S³` with the round bi-invariant metric, the set of
# isometries carrying the Cartan-Schouten connection `∇⁰` to `∇¹` is EXACTLY
# the orientation-reversing coset `O(4)\SO(4)`. The proof is one line and is
# the reason, not a coincidence: `T^t = (2t-1)[·,·]` is a constant multiple of
# the VOLUME TENSOR, so `φ_*T⁰ = det(dφ)·T⁰`, and `T¹ = -T⁰ ≠ 0`; hence
# `φ_*∇⁰ = ∇¹ ⟺ det(dφ|_{TS³}) = -1`. "Exchanges the two Cartan-Schouten
# endpoints" and "reverses the orientation of `S³`" are therefore the SAME
# `Z₂` character. Consequently no `g` satisfying C125's condition (i) is
# isotopic to the identity in `Diff(M₄×S³×S⁶)`, whatever it does on `M₄` and
# `S⁶`. The claim is FALSIFIED -- but see the verdict's own precise
# apportionment: the failing condition is (ii)'s "genuine gauge
# transformation, not parity" clause, universally; it is NOT condition (iii)
# for both survivors, and reporting it as such was an error caught by the FL
# Step 8a skeptic pass and corrected below.
#
# NOT covered, NOT closed, by this theorem (full list in "What this round does
# NOT show"): whether `(t=0,E)` and `(t=1,Ē)` are the same MODEL; whether
# LRSM parity (Family C) is excluded by anything -- this project currently has
# no certified fact that excludes it, which is exactly round95's recorded gap;
# non-product / warped backgrounds; which of `t=0`,`t=1` is selected; and any
# change to `N_gen=3`'s CONDITIONAL status.

**Verdict (2026-09-01, FL Step 8a skeptic pass run and incorporated; a
SECOND, independent skeptic pass run same day, corrections below):**
`FALSIFIED__ON_S3_THE_SET_REALIZING_w0_TO_w1_IS_EXACTLY_THE_ORIENTATION_REVERSING_COSET_O4_MINUS_SO4_PROVEN_BY_TORSION_EQUALS_VOLUME_TENSOR_CONFIRMED_AND_STRENGTHENED_BY_SECOND_SKEPTIC_HOLDS_FOR_ANY_ISOMETRY_NO_UNSTATED_ASSUMPTION__CONDITION_ii_GAUGE_FAILS_FOR_ALL_8_SIGN_TRIPLES_BY_A_DE_RHAM_TORSION_FORM_ARGUMENT_NEEDING_NO_PRODUCT_MAP_OR_ISOM_FACTORIZATION_ASSUMPTION_REPAIRED_SAME_DAY__ITS_BARE_ORIENTATION_CLAUSE_ADMITS_EXACTLY_2_COMPENSATED_FAMILIES__FAMILY_B_VIOLATES_CLAIMS_OWN_TWIST_CONDITION_AND_SENDS_c3_PLUS2_TO_MINUS2__FAMILY_C_STATUS_UNDER_CONDITION_iii_IS_UNDECIDED_NOT_EXCLUDED_DOWNGRADED_SAME_DAY_THE_RELABELING_ARGUMENT_WAS_CIRCULAR_AND_UNRECONCILED_AGAINST_OB13_C38_GENUINELY_DISTINCT_STATES_LANGUAGE__WHETHER_OB1_COLLAPSES_UNDER_FAMILY_C_IS_CONDITIONAL_ON_RESOLVING_iii_NOT_IMMOVABLE_AS_ORIGINALLY_CLAIMED_THAT_CLAIM_COMMITTED_THE_SAME_CATEGORY_ERROR_DEFECT_3_HAD_ALREADY_DIAGNOSED_ONE_SECTION_EARLIER__OBSTRUCTION_IS_A_Z2_COMPONENT_CLASS_NOT_A_TUNABLE_QUANTITY`

**Status:** OB1 stays PARKED. The `t=0`-vs-`t=1` question is **not** dissolved
by gauge redundancy and remains a genuine, unresolved physical choice. OB13's
C37/C39 content is **strengthened**: C39 showed `ι` *is* orientation-reversing;
this round shows *every* map that could do the job is, and that the
coincidence C39 observed is forced by `T ∝ vol`, not accidental.

**Completeness:** `PARTIAL`, in three named respects. (1) The enumeration is
exhaustive over the **sign triple** `(ε₄,ε₃,ε₆)`, not over `π₀(Isom(M₁₃))`,
which has `2·2·2·2 = 16` classes because `O(1,3)` has four (`P`, `T`, `PT`);
this is inert here because `ε₃ = −1` already excludes every row, but the
enumeration should not be called exhaustive over `π₀`. (2) The `Isom`
factorisation assumes a strict product metric. (3) Family C's status under
condition (iii) is **UNDECIDED, not FAIL** -- deciding it requires a link this
project does not have (round95).

**Gate fields assessed:** `PARENT_ACTION_GATE.md` F1 (background, reused
unchanged), F2 (twist, reused unchanged -- and Family B is killed precisely
*on* F2), F3 (reused by citation, round113), F5 (reused). F4 is the field this
round bears on, negatively: it removes a proposed dissolution of F4's question
and sharpens what a selector must look like; it supplies no F4 mechanism.
F6, F7 not assessed.

---

## ⚠️ FL STEP 8a SKEPTIC PASS RUN AND INCORPORATED, 2026-09-01, same day
(context-blind, `Agent(skeptic, model=opus)`, `claim.md` + `decision.md` +
script only, no session history). **Verdict returned: WEAKENED -- "right
answer, and three of the load-bearing arguments are wrong." Every finding was
independently re-verified by this session before being accepted; three were
real defects, all repaired below rather than argued away. The headline verdict
does not flip; its apportionment across conditions (ii) and (iii) does.**

**Defect 1 -- the old `B1` gate check was a TAUTOLOGY.** [CONFIRMED by direct
re-run] It compared `-ad_e[i] @ A` against a hand-expanded
`brack[l,j] = Σ_k A[k,j]·2ε[i,k,l]`; renaming the dummy index shows
`brack ≡ ad_e[i] @ A` **identically, for any 3×3 `A` whatsoever**. Re-run with
`A = np.ones((3,3))` and with `A = 1e6·noise`: residual `0.0` in every case.
The claimed derivative `d/ds Ad_{conj(g e^{s e_i})} = −ad_{e_i}Ad_ḡ` was never
differentiated. The old "negative control" was correspondingly vacuous.
**Repaired:** new `B0` is a genuine finite-difference test of exactly that
derivative (measured error `6.7e−10`; **wrong-sign negative control deviates
by `4.00`**, so it can fail), and `B1` now assembles the cancellation from the
*measured* derivative (`6.8e−10`) rather than from a re-expansion of the same
symbol.

**Defect 2 -- the stated `Z₂` law for `γ₅` was FALSE as written, and was
applied exactly where it fails.** [CONFIRMED by direct computation] `γ₅` has
two routes: `γ₅ = iΩ₄` (transforms as `ε₄`) and `γ₅ = −iΩ₃Ω₆` (transforms as
`ε₃ε₆`). The previous text asserted the second unconditionally, in the same
`[VERIFIED]` block that also asserted `Ω₄ → ε₄Ω₄`. The two agree **only** on
`ε₄ = ε₃ε₆`, i.e. only on `ε₁₃ = +1` -- and the text then applied the law to
the uncompensated `ι̃`, which has `ε₁₃ = −1`. Measured:

| case | `ε₁₃` | `ω₁₃` preserved | routes agree |
|---|---|---|---|
| none | `+1` | ✓ | ✓ |
| `M₄` only | `−1` | ✗ | ✗ |
| `S³` only (`ι̃`) | `−1` | ✗ | ✗ |
| `M₄`+`S³` (Family C) | `+1` | ✓ | ✓ |
| `S³`+`S⁶` (Family B) | `+1` | ✓ | ✓ |

"Routes agree **iff** `ω₁₃` is preserved" -- exactly as §1b's own module-
exchange statement predicts, and exactly contradicting the old §4 inference.
**Repaired:** the law is now stated with its `ε₁₃ = +1` side condition, the
`ι̃` handedness inference is **RETRACTED**, and gate check `E2` (which was
named for a `γ₅` claim its body never touched, and was forced by
multilinearity) is replaced by the two-route table above.

**Defect 3 -- §3c did not kill Family C on condition (iii).** [ACCEPTED after
re-derivation] Both of the old arguments were condition-(ii) arguments in
disguise: "it implements an outer automorphism, hence is not gauge" *is* the
gauge reading of (ii), already settled in §2b; and "gauged parity ⟹
vector-like ⟹ `ind = 0`" applies a symmetry-of-one-configuration argument to a
map *between two* configurations, while the index it invokes lives on `S⁶`,
which Family C does not touch. Worse, §3a's own disclaimer ("the L/R
*labelling* is a convention") licenses reading `(1,2) → (2,1)` as a
physically-equivalent configuration, which `claim.md:50` explicitly permits.
**Repaired:** §3c is rewritten to say plainly that **Family C is not excluded
by condition (iii)**; it is excluded by (ii)'s "not parity" clause alone. This
is a *stronger* and more useful result than the one it replaces, because it
identifies exactly which missing link (round95's) would be needed to exclude
it on physics.

**Findings accepted and repaired, no verdict impact:** the Ricci
eigen-distribution route needed a radius-genericity condition
(`ρ₆/ρ₃ ≠ √(5/2)`) it never stated, and was missing the step from
"preserves eigen-distributions" to "is a product map" -- demoted to a remark,
with de Rham as the sole route, plus the skeptic's own much better `H³`
argument added; `π₀(Diff(S³)) = Z₂` is **Cerf (1968)**, not Hatcher (1983)
(Hatcher gives the stronger `Diff(S³) ≃ O(4)`) -- attribution fixed; "every
orientation-reversing isometry of `S⁶` sends the structure to its **conjugate**"
was over-quantified (`r = −h` gives `−φ` only for `h ∈ G₂`; otherwise a third
structure -- a worse failure, so the conclusion survives) -- narrowed;
`block_F` is hardcoded arithmetic, **not** a tool check -- tag corrected to
`[INFERRED]`; the Kaluza-Klein premise "the 4D gauge group descends from
`Isom₀`" was tagged `[VERIFIED, results_c125.json:C]` against a truth table
containing nothing about Kaluza-Klein -- **downgraded to `[CITED]` standard
lore, with its contested status noted**, and the `H³` argument added so the
mathematical backbone no longer depends on it.

**Finding accepted that makes a result LESS novel, recorded rather than
buried:** `Ω₃Ω₆ = iγ₅` is not a discovery about the `S³/S⁶` split at all. It
is forced in *every* irrep of `Cl(1,12)`: `ω₁₃ = Ω₄·(Ω₃Ω₆)` is central in odd
dimension, hence a scalar `c`; with `Ω₄² = −1` and `γ₅ := iΩ₄` this gives
`Ω₃Ω₆ = i·c·γ₅`, and `c = ω₁₃ = +1` predicts the measured `0+1i` without
touching the split. This **strengthens** the settlement of the external
document's dispute (the identity is convention-independent, not an artifact of
the chosen embedding) and **weakens** the pearl (it is the odd-dimensional
volume-element identity, not an unexpected finding). Both changes made.

**One item the skeptic could not settle without execution** (it had no
execution tool): an independent re-derivation of the central theorem outside
the quaternionic parametrisation. Its analytic route -- the torsion /
volume-tensor argument -- has now been implemented as `B3` and **passes**,
including the discriminating half (`φ_*T⁰ = T¹` **iff** `det < 0`, checked
over 400 random `O(3)` elements of both signs). That route is now the primary
proof and the old sampled frame test is demoted to a cross-check.

---

## ⚠️ SECOND, INDEPENDENT FL STEP 8a SKEPTIC PASS, 2026-09-01, same day
(context-blind, fresh `Agent(skeptic, model=opus)`, `claim.md`+`decision.md`
+script only, no session history, no knowledge of the FIRST skeptic pass'
own corrections). **Verdict: the headline `FALSIFIED` survives and its
mathematical core (§2a torsion theorem) is CONFIRMED, even strengthened
(holds for ANY isometry, no unstated assumption). But §3c and §5's item 4
were found to assert MUTUALLY EXCLUSIVE conclusions -- repaired below,
not smoothed over.**

**(a) Torsion=volume-tensor theorem -- CONFIRMED, strengthened.** Re-
derived independently from scratch: no requirement that the isometry fix
`e`, be a group automorphism, or be left-invariant -- holds for literally
any isometry of `S³`. **Evidence-tier correction:** script `B3` mostly
restates its own construction (`comp[i,j,k]=2(2t-1)ε_{ijk}` asserted then
checked against itself) rather than independently verifying that the
`left_frame()`/`qmul()` machinery actually produces an orthonormal frame
with `[X_i,X_j]=2ε_{ijk}X_k` -- that one load-bearing fact is asserted,
not computed. Downgrade `B3`'s tag to `[INFERRED -- hand derivation,
correct; script wrapper does not independently verify the frame itself]`.
Rebuilt `B1` (from the FIRST skeptic pass) is algebraically identical to
`B0` -- zero independent information, "14 of 14 checks" double-counts one.
**Pearl correction:** the reusable pre-filter ("Cartan-Schouten torsion
IS the volume tensor") holds **only in `dim=3`** -- on any bi-invariant
`G` with `dim≥4` the torsion is the Cartan 3-form, not the volume form,
and the argument does not transfer. Added to the pearl's own text below.

**(b) `H³` degree argument -- arithmetic CONFIRMED, but the document's own
"needs no `Isom` factorisation... survives every scope caveat" claim is
WEAKENED to false, and the document contradicts itself on this point**
(`decision.md`'s own §"What this round does NOT kill" already says the
`H³` argument "still assumes the candidate is a product map, which §1a
supplies" -- directly contradicting §2b's "needs no factorisation"
framing). **Repaired with a strictly stronger, genuinely assumption-free
version, supplied by the skeptic and verified by this session:** the
torsion-as-a-CLOSED-3-FORM argument. `H^t = c(2t-1)·π₃^*vol_{S³}` is
closed (top-degree on its own factor) with `∫_{S³×pt}H^t≠0`, hence
`[H^t]≠0` in `H³_{dR}(M₁₃)` directly -- condition (i) forces
`g^*[H⁰]=[H¹]=-[H⁰]≠[H⁰]`, so `g^*≠id` on `H³`, so `g` is not homotopic to
`id`. **This needs no product-map assumption, no `Isom` factorisation, no
Künneth, and not even `M₄` contractible** -- strictly more robust than
the original, and survives W3 (warped/non-product backgrounds), which
the original explicitly did not. Replaces §2b Argument 2 below.

**(c) "Family C NOT excluded by (iii), at all, by nothing else" --
DOWNGRADED to UNDECIDED (matching the Completeness note's own, more
careful wording, which §3c's heading and the verdict string had already
overridden without saying so).** Three findings, none individually fatal
to the round, together forcing the downgrade:
1. **The relabelling argument is circular.** The map licensing
   `(1,2)→(2,1)` as "just a relabelling" is `ι` itself (the round's own
   `A2`, `ι φ_{a,b} ι = φ_{b,a}`) -- i.e. the argument is "the image is
   equivalent to the source because the map under test relates them,"
   which if applied consistently would let (iii) exclude nothing, yet
   §3b **does** use (iii) to kill Family B via `c₃`/`ind`, genuine
   invariants no relabelling touches. Condition (iii) has content exactly
   where an invariant exists; the open question is whether one
   distinguishes the two `SU(2)` factors here, not whether the label is
   a convention.
2. **`OPEN_BLOCKERS.md` OB13 (the C38/C39 chain, already in this
   project) states, verbatim: "`(1,2)` and `(2,1)` are genuinely
   distinct states exchanged by parity, exactly as `SU(2)_L`/`SU(2)_R`
   relate in the SM."** C125 cited C38 only for the two kernel labels
   and never engaged with this sentence. **On reflection [this session's
   own check, not fully resolving the tension]: this may not be a strict
   logical contradiction** -- "(1,2) and (2,1) are distinct
   representations" (true, they manifestly are) is a different claim
   from "a specific isomorphism `g` mapping one to the other cannot
   satisfy (iii)'s own permissive 'or a physically-equivalent
   configuration' clause" -- but C125 should have cited and explicitly
   reconciled this pre-existing project sentence rather than silently
   omitting it, and did not.
3. **Checked directly this session, per the skeptic's own named cheap
   test:** does G74B derive the S⁶-orientation↔4D-handedness link, or
   assume it? [VERIFIED, direct read, `experiments/20260621-g74b-
   chirality-from-index/decision.md`] G74B's own text: *"Does NOT prove
   parity violation from first principles -- the orientation choice is
   an input. The claim is that parity violation is encoded in the
   orientation, NOT DERIVED FROM IT... Does NOT explain WHY nature chose
   left-handed over right-handed."* G74B's entire computation is `S⁶`-
   only and never references `S³`, `t`, or any relative orientation.
   **This partially SUPPORTS the original §3c intuition** (G74B does
   not itself supply a proof that would exclude Family C -- consistent
   with round95's "no link" framing) **but does not resolve finding 2
   above**, which comes from a different, independent project source
   (OB13/C38), not from G74B.

**Net: `UNDECIDED`, not `NOT EXCLUDED AT ALL`.** The cheapest remaining
test, if this is ever revisited: explicitly reconcile OB13's "genuinely
distinct states" sentence against (iii)'s own permissive clause -- not
attempted further this round.

**(d) "Even granting Family C, OB1 does not collapse" -- the argument
given is FALSIFIED (category error); the conclusion is no longer
asserted as a fact, only as CONDITIONAL on (c).** The skeptic found this
argument re-commits, one section later, the *exact same category error*
Defect 3 (first skeptic pass) already diagnosed and fixed: "the SM
breaks parity" is a statement about ONE configuration (P is not a
symmetry of it); Family C is an isomorphism BETWEEN TWO configurations;
whether P is a symmetry of `X₀` says nothing about whether `g:X₀→X₁`
identifies them. The textbook counter-example points the other way too:
spontaneously broken discrete symmetries relate degenerate vacua that
ARE physically indistinguishable (same spectrum, same S-matrix) -- "the
symmetry is broken" does not imply "the two configurations it relates
are physically distinct." **What actually decides it, per the skeptic
and independently confirmed [VERIFIED, re-checked this session]: whether
`ε₄ε₆` (the relative `M₄`↔`S⁶` orientation Family C flips) is a genuine
physical datum or a pure labelling convention -- exactly what (c) leaves
UNDECIDED. If `ε₄ε₆` is physical, (d) holds AND (c) should exclude
Family C (contradicting the UNDECIDED-not-excluded framing); if `ε₄ε₆`
is convention, (c)'s "not excluded" stands BUT (d) fails (the two
configurations are identical in every transported datum, and OB1 WOULD
collapse under Family C). Exactly one of (c)'s and (d)'s favourable
readings can hold, not both -- the document previously asserted both.**
Corrected in §3c/§5 below to state this explicitly as the genuinely open
question, rather than resolving it either way.

---

## 0. What was asked, restated precisely

C125's kill criterion asks whether a single `g` exists that is simultaneously

* **(i)** an isometry of the FULL product `M₁₃ = M₄×S³×S⁶` carrying
  `(e, ω^{t=0})` to `(e, ω^{t=1})`;
* **(ii-orient)** orientation-preserving on the full 13-manifold, glossed in
  the same breath as **(ii-gauge)** "a genuine gauge transformation, not
  parity";
* **(iii)** consistent with the certified fermion representation content.

`claim.md`'s numbered list has its *own* second condition -- **(ii-twist)**,
"the twist bundle / index data on `S⁶` to itself (unchanged)". **There are two
different (ii)s in the pre-registration and they are not the same condition.**
They are named `(ii-orient)`, `(ii-gauge)`, `(ii-twist)` throughout below; the
undifferentiated label "(ii)" is not used again.

Three preliminaries, all load-bearing, all established before anything is
searched:

**(0a) The only available notion of equivalence here is a diffeomorphism, not
a frame rotation.** [VERIFIED, elementary] A local Lorentz / frame gauge
transformation `(e,ω) → (Λe, ΛωΛ⁻¹+ΛdΛ⁻¹)` does not change the connection as
a covariant derivative -- only its matrix representation. Torsion is a
`(1,2)`-**tensor**, and `T¹ = −T⁰ ≠ 0` [CITED, C124 Step (c);
round99/round113]. Two connections with different torsion tensors are
different connections; no frame rotation relates them. Condition (i) also
fixes the vielbein `e`, so `φ` is metric-preserving by construction, i.e. an
isometry -- the restriction is forced by the claim's own wording.

**(0b) `(ii-orient)` is strictly weaker than `(ii-gauge)`.** [VERIFIED, group
theory] Orientation-preserving on `M₁₃` is the kernel of ONE `Z₂` character on
`π₀(Isom(M₁₃))`; connected-to-the-identity is the kernel of the full map to
`π₀`, which here has 16 classes. **The two are not equivalent, and Family C
below is an explicit witness: it is orientation-preserving on `M₁₃` AND is
parity.** So `claim.md`'s condition (ii), read as a conjunction, is
unsatisfiable *by construction of its own wording* -- not because of any
physics. Both halves are carried through separately.

**(0c) Untagged hinge, now supplied.** The step "`φ_*∇⁰ = ∇¹` iff `dφ` carries
the left-invariant frame to the right-invariant frame up to a constant matrix"
is true because both connections are flat and `S³` is simply connected, so
parallel fields are exactly constant combinations of the invariant frame. It
is no longer load-bearing regardless: §2a's primary proof is the torsion
argument, which does not use it.

---

## 1. `ι` on the FULL product, and the full-13D orientation (question 1)

### 1a. `Isom(M₄×S³×S⁶)` factorises

[CITED for the theorem, VERIFIED for its application here] Every isometry
preserves the canonical de Rham decomposition of the tangent bundle into a
flat part plus irreducible non-flat parts, and permutes the irreducible
factors. Here those are `TS³` (dim 3) and `TS⁶` (dim 6) -- different
dimensions, so no permutation; and `M₄` is Lorentzian and flat, so no isometry
carries a timelike direction into a Riemannian factor. Hence

```
Isom(M₁₃)  =  Isom(M₄) × Isom(S³) × Isom(S⁶)  =  Poin(1,3) × O(4) × O(7)
```

and every candidate is a triple `g = (g₄, g₃, g₆)` with a well-defined
component class in each factor.

> **Remark, demoted from a claimed "independent route" (skeptic-corrected).**
> An earlier draft offered `Ric = 0 ⊕ (2/ρ₃²)g₃ ⊕ (5/ρ₆²)g₆` with
> "eigen-distributions of dimensions `4/3/6`, all distinct" as an independent
> argument. **What separates eigen-distributions is distinct eigenvalues, not
> distinct dimensions.** At `ρ₆/ρ₃ = √(5/2) ≈ 1.5811` the two positive
> eigenvalues coincide and the Ricci operator has a single 9-dimensional
> eigenspace, separating nothing. The route also silently skipped
> "preserves each eigen-distribution ⟹ is a product map". It is kept only as
> a remark; the conclusion rests on de Rham, and on §2b's `H³` argument, which
> needs neither.

### 1b. The natural extension of `ι` reverses the full 13D orientation

[VERIFIED, `results_c125.json:A3`] Write `ε_F := det(dg|_{TF})`. For
`ι̃ := (id₄, ι, id₆)`:

| factor | dim | action | `ε` |
|---|---|---|---|
| `M₄` | 4 | identity | `+1` |
| `S³` | 3 | `ι(g)=g⁻¹` | `−1` (measured `det ∈ [−1.0000000002, −0.9999999998]`, 100 random coset maps; negative control, `SO(4)` maps, `+1` to the same precision) |
| `S⁶` | 6 | identity | `+1` |

`ε₁₃ = ε₄·ε₃·ε₆ = −1`. **The full 13-manifold orientation is REVERSED.**

The reason answers question 1 directly and is worth stating so it is not
mistaken for a dimension-parity accident: `ε₁₃` is a *product* of per-factor
determinants, and `dim M₄ = 4`, `dim S⁶ = 6` being even is **irrelevant** --
those factors are *untouched*, so their `ε` is `+1` whatever their dimension.
The single `−1` from the `S³` leg is unopposed.

**Consequence, sharper than "it is parity":** [VERIFIED,
`results_c125.json:E3,E2`] in odd total dimension `ω₁₃ = Γ⁰Γ¹…Γ¹²` is central
and equals a scalar (computed: `+1`), and the two inequivalent irreducible
`Cl(1,12)` modules are distinguished by its sign. An orientation-reversing map
sends `ω₁₃ → −ω₁₃`. So `ι̃` **does not act on the 13D spinor module as an
automorphism at all -- it exchanges the two inequivalent modules.** This is
strictly stronger than C39's `det = −1`, and it is also, per Defect 2 above,
the reason no determinate statement about "which way the 4D handedness flips"
is available for `ι̃`.

---

## 2. Systematic search: does ANY other map realize `ω⁰ ↔ ω¹`? (question 2)

### 2a. The S³ leg: a theorem with a one-line proof, no sampling

[VERIFIED, `results_c125.json:B3`; own derivation]

In the orthonormal left-invariant frame, `[X_i,X_j] = 2ε_{ijk}X_k`, so

```
T^t(X_i,X_j) = (2t−1)[X_i,X_j] = 2(2t−1)·ε_{ijk}X_k
```

-- the torsion is a **constant multiple of the volume tensor**. For any
isometry `φ`, the volume tensor pulls back by the determinant, so
`φ_*T⁰ = ε₃·T⁰`; and `T¹ = −T⁰ ≠ 0`. A metric connection is
`LC + contorsion(T)` and every isometry preserves `LC`, so equality of torsion
*is* equality of connection. Therefore

> **`φ_*∇⁰ = ∇¹` ⟺ `det(dφ|_{TS³}) = −1`.**
> Equivalently `{φ ∈ Isom(S³) : φ_*∇⁰ = ∇¹} = O(4)\SO(4)`, the
> orientation-reversing coset, EXACTLY.

Measured [VERIFIED]: `T⁰ = −2ε`, `T¹ = +2ε = −T⁰ ≠ 0`; pullback by a random
`R ∈ O(3)` scales the tensor by `det R` (400 elements, both signs); and the
**discriminating** half -- `φ_*T⁰ = T¹` **iff** `det R < 0` -- holds on all
400. No sampling over `Isom(S³)` is involved: the statement is a scaling law,
verified as a law.

This is the round's central result, and it says the coincidence C39 found for
the single map `ι` is not a property of `ι`: on `S³`, *exchanging the two
Cartan-Schouten endpoints* and *reversing the orientation* are one `Z₂`
character, because the torsion **is** the volume form up to a constant.
**`ε₃ = −1` is forced by condition (i), for every candidate.**

**Cross-check, explicitly labelled as sampled** [VERIFIED,
`results_c125.json:B0,B1,B2`]: the independent frame-transition test agrees.
`SO(4)` maps give a constant left-frame transition (spread `2.10e−10`) and a
wildly non-constant right-frame one (`≥1.650`); the `ι`-coset gives the mirror
(`≥1.745` / `2.24e−10`). This samples 12 `(a,b)` pairs per coset × 25 base
points -- it corroborates the theorem, it does not prove it. (An earlier draft
called it "exhaustive, not sampled" on the grounds that `O(4)` has two
components; that is a non-sequitur and has been removed.)

Two would-be escapes, closed:

* **Non-isometric diffeomorphisms.** Closed by (0a). Independently, [CITED,
  Cerf 1968 for `π₀(Diff(S³)) = Z₂`; Hatcher 1983 for the stronger
  `Diff(S³) ≃ O(4)`] `ι` is not isotopic to the identity even in the full
  diffeomorphism group. Neither theorem was re-derived here; marked `[CITED]`.
* **Frame/bundle gauge transformations.** Closed by (0a).

### 2b. The full product: `(ii-gauge)` fails for all 8 sign triples

Two independent arguments, the second added after the skeptic pass because the
first rests on a physics premise that had been mis-tagged.

**Argument 1 -- component class** [VERIFIED for the group theory; **`[CITED]`,
standard lore, for the physics premise**]: in Kaluza-Klein reduction the 4D
gauge group descends from the **identity component** `Isom₀` of the internal
isometry group (gauge bosons ↔ Killing vectors); disconnected components give
discrete GLOBAL symmetries. By §1a the component class is a per-factor
invariant, and by §2a condition (i) puts `g₃` in the non-identity class of
`π₀(O(4))`. Hence no candidate is in `Isom₀(M₁₃)`. **The premise is
`[CITED]`, not `[VERIFIED]`** (an earlier draft tagged it against
`results_c125.json:C`, a truth table containing nothing about Kaluza-Klein),
and it is *contested* lore -- the "no global symmetries in quantum gravity"
position would treat geometric discrete symmetries as gauged. That is exactly
why argument 2 exists.

**Argument 2, ORIGINAL VERSION [self-contradicted, see correction]:** `M₄` is
contractible, so `M₁₃ ≃ S³×S⁶`, and Künneth gives `H³(M₁₃;ℤ) = ℤ`, generated
by the `S³` class. A product map acts on that generator by `deg = ε₃ = −1`,
while any diffeomorphism isotopic to the identity acts as `+1` on `H^*`.
This was originally claimed to need "no `Isom` factorisation" -- **false as
stated, and self-contradicted elsewhere in this same file** (see "What this
round does NOT kill" below: "the `H³` argument is more robust but still
assumes the candidate is a product map, which §1a supplies"). Caught by the
second, independent skeptic pass.

> **Argument 2, REPAIRED [VERIFIED, this session's own re-derivation,
> genuinely assumption-free -- supplied by the second skeptic pass]: the
> torsion itself, viewed as a 3-form, is the obstruction, with no product-
> map assumption, no `Isom` factorisation, no Künneth, and not even `M₄`
> contractibility.** `H^t := c(2t-1)·π₃^*\mathrm{vol}_{S³}` is a closed
> 3-form on `M₁₃` (top-degree on its own `S³` factor, hence `d(π₃^*
> \mathrm{vol}_{S³})=0` trivially), with `∫_{S³×\{pt\}} H^t ≠ 0` for any
> point in `M₄×S⁶`. So `[H^t] ≠ 0` in `H³_{dR}(M₁₃)` directly. Condition
> (i) forces `g^*[H⁰] = [H¹] = -[H⁰] ≠ [H⁰]` (since `H¹=-H⁰`, `H⁰≠0`), so
> `g^*` is not the identity on `H³_{dR}(M₁₃)`, so `g` is not homotopic to
> `\mathrm{id}_{M₁₃}` -- hence not isotopic to it, hence not a gauge
> transformation. **This version genuinely survives every scope caveat in
> this file, including W3 (non-product/warped backgrounds), which the
> original Künneth-based version explicitly does not.** This is now the
> mathematical backbone of the verdict; the original Künneth phrasing above
> is retained only for its historical derivation, not as the load-bearing
> argument.

> **`(ii-gauge)` fails universally. 0 of 8 sign triples both realize `ω⁰↔ω¹`
> and lie in the identity component.**

*Supporting remark, demoted from a kill (skeptic-corrected):* `ι` also
implements an OUTER automorphism of `SO(4) = (SU(2)_a×SU(2)_b)/Z₂` -- verified
independently, see §3a. "Outer ⟹ not gauge" is **not** a general theorem: the
block swap `J = [[0,I₂],[I₂,0]]` has `det = +1`, lies in the *connected* group
`SU(4)`, and conjugates `diag(u,v)` to `diag(v,u)`. The escape is closed here
only *relative to this project's own gauge content* -- gate G97
(rounds 102/108/109) closes the product-manifold `SU(4)` realization
[CITED] -- so the argument is stated as relative, not general, and is not used
as an independent kill.

### 2c. The full product: `(ii-orient)` alone leaves exactly two families

[VERIFIED, `results_c125.json:C_table`] All 8 assignments of
`(ε₄,ε₃,ε₆) ∈ {±1}³`, with `ε₃ = −1` forced and `ε₁₃ = +1` required:

| `ε₄` | `ε₃` | `ε₆` | `ε₁₃` | realizes `ω⁰↔ω¹` | `(ii-orient)` | `(ii-gauge)` |
|---|---|---|---|---|---|---|
| `+1` | `−1` | `−1` | `+1` | ✓ | ✓ | ✗ |
| `−1` | `−1` | `+1` | `+1` | ✓ | ✓ | ✗ |
| (other 6) | | | | ✗, or `ε₁₃ = −1` | | ✗ |

**Family B** (`ε₆ = −1`): compensate on `S⁶`.
**Family C** (`ε₄ = −1`): compensate on `M₄` -- `g` is 4D parity (or time
reversal; both `P`- and `T`-type elements of `O(1,3)` have `det = −1`, `PT`
does not) composed with `ι`.

**Scope note (skeptic-corrected):** this enumerates the 8 sign **triples**.
`π₀(Isom(M₁₃)) = (ℤ₂×ℤ₂) × ℤ₂ × ℤ₂` has **16** classes, since `O(1,3)` has
four components and `PT = −I₄` has `det = +1` while lying outside the identity
component -- so `ε₄ = +1` does **not** imply `g₄ ∈ Isom₀(M₄)`. Inert for the
count (`ε₃ = −1` excludes every row either way), but the table is not
exhaustive over `π₀` and is no longer described as such.

---

## 3. Condition (iii): the certified fermion content (question 3)

### 3a. What is actually certified, stated before it is used

[CITED, G73, 29/29 tests] `c₃(S⁻) = χ(S⁶) = 2`, `Â(S⁶) = 1`,
`ind(D⁺_{S⁶}⊗S⁻) = +1` per triality channel.
[CITED, G74B, 31/31 tests] `dim ker(D⁺)=1`, `dim ker(D⁻)=0`,
`LEFT_HANDED_EXCESS`; verbatim: *"The orientation of `S⁶` is the single
discrete input... Reversed orientation: `ind → −1` → right-handed excess
(unphysical)."*
[CITED, G74A, with its own 2026-07-17 superseded-lemma note respected -- the
NUMBER `dim ker = 1` is cited, the two lemmas are not.]
[CITED, C38, VERIFIED-numpy with a passing negative control]
`ker(D_{S³},t=0) = (1,2)`, `ker(D_{S³},t=1) = (2,1)` under
`SO(4) = (SU(2)_a×SU(2)_b)/ℤ₂`.
[CITED, round90] `SU(2)_R` is genuinely GAUGED in `preprint.tex`, not a label.
The working assignment is `t=0` → `SU(2)_R` doublet, `t=1` → `SU(2)_L` doublet
(round91). **The L/R *labelling* of the two factors is a convention; only the
exchange is invariant.**
[CITED, round95] G74B/L5's chirality is an **`S⁶`-only** statement,
**not currently linked** in this project to which `t`-sector the `S³` side
realizes. This is respected as a hard constraint below, not worked around.

**Independently re-derived here** [VERIFIED, `results_c125.json:A2`, max error
`2.7e−16`, 200 random triples; negative control -- comparing against
`φ_{a,b}` instead of `φ_{b,a}` -- gives median difference `0.96`]:

```
ι ∘ φ_{a,b} ∘ ι  =  φ_{b,a}
```

`ι` conjugates `SO(4)` by exchanging the two `SU(2)` factors. This is the
group-theoretic mechanism behind C38's `(1,2) ↔ (2,1)`, obtained independently
of C38's own construction.

### 3b. Family B (`ε₆ = −1`) FAILS -- on `(ii-twist)` first, on (iii) second

[VERIFIED, own derivation; `results_c125.json:F` is arithmetic, see the tag
correction] Any orientation-reversing isometry of `S⁶` is `r = −h` with
`h ∈ SO(7)` (since `det(−I₇) = −1`). The `G₂`-structure is the stabilizer of
the associative 3-form `φ`, and `(−I)*φ = (−1)³φ = −φ`, so `r*φ = −h*φ`.

> **Narrowed (skeptic-corrected):** `r*φ = −φ` only when `h ∈ G₂`. For
> `h ∉ G₂` the structure is carried to a *third* structure, neither `J` nor
> `−J` -- a worse failure, not a milder one, so the conclusion survives; the
> universal quantifier "carries it to its conjugate" does not, and has been
> removed.

In every case the frozen twist `E = S⁻ = T^{1,0}S⁶ ⊕ ℂ` is not preserved.
With `c_k(Ē) = (−1)^k c_k(E)`: `c₃: +2 → −2`, `ind: +1 → −1`.

Three failures, any one decisive, in order of strength:

1. **`(ii-twist)` -- the claim's own pre-registered condition.** `claim.md:44`
   requires *"the twist bundle / index data on `S⁶` to itself (unchanged,
   since `g` is not claimed to touch the `S⁶` factor)"*. Family B touches it.
   **This kill is definitional and needs no physics.**
2. Contradicts G73's `c₃(S⁻) = +2` and G74B's `ind = +1` for the frozen twist.
3. G74B names the `S⁶` orientation as *the single discrete physical input*
   fixing SM handedness; a gauge redundancy cannot act on a discrete physical
   input without making that derivation vacuous.

### 3c. Family C (`ε₄ = −1`) status under condition (iii): **UNDECIDED**
(downgraded from "NOT EXCLUDED AT ALL" by a SECOND, independent skeptic
pass, same day -- see the correction block above for the full three-part
reasoning: the relabelling argument is circular; `OPEN_BLOCKERS.md`
OB13's "genuinely distinct states" sentence was never reconciled; G74B's
own text disclaims deriving the link at all, partially but not fully
supporting the original reading).

**This section previously reversed an even earlier draft's claim, per the
FIRST FL Step 8a skeptic pass. That correction (survival, not a kill) is
retained below and remains correct as far as it goes -- what changed is
the CONFIDENCE this section is entitled to claim for it.**

`g = P₄ ∘ ι̃` leaves `S⁶`, the twist, and the whole index chain untouched, so
§3b is unavailable. Checked against the pre-registration line by line:

| condition | Family C |
|---|---|
| (i) isometry of `M₁₃`, `ω⁰→ω¹` | ✓ (`P₄`, `ι`, `id₆` are isometries; `ι` realizes the swap) |
| `(ii-orient)` | ✓ `ε₁₃ = (−1)(−1)(+1) = +1` |
| `(ii-twist)` | ✓ `S⁶` untouched |
| `(ii-gauge)` "not parity" | ✗ -- it **is** parity (§2b) |
| (iii) fermion content → itself **or a physically-equivalent configuration** (`claim.md:50`) | **NOT EXCLUDED.** It maps `(1,2) → (2,1)`, which *is* the certified `t=1` content. |

Why (iii) cannot exclude it, with this project's own facts:

* §3a's own disclaimer -- the L/R **labelling** is a convention -- licenses
  reading `(1,2) ↔ (2,1)` as a relabelling, and `claim.md:50` explicitly
  permits "a physically-equivalent configuration".
* The only certified chirality datum, `ind = +1`, lives on `S⁶`, which
  Family C does not touch. Nothing about it changes, so no contradiction is
  produced.
* The argument that *would* work -- Family C flips `γ₅` (`ε₄ = −1`) while
  leaving the `S⁶` orientation datum untouched, hence flips the
  **correlation** between `S⁶` orientation and 4D handedness -- requires
  exactly the `S⁶`-channel ↔ `S³`-`t`-sector link that **round95 records as
  absent from this project**, and that §4's `γ₅ = −iΩ₃Ω₆` supplies only inside
  a hypothetical `Spin(1,12)` parent this project does not claim.

**So Family C is excluded by `(ii-gauge)` alone -- i.e. by §2b's `H³` degree
obstruction -- and by nothing else.** Two corollaries worth having:

* The **residual freedom** left by (i) + `(ii-orient)` + `(ii-twist)` + (iii)
  is exactly LRSM parity. That is `PARENT_ACTION_GATE.md` F4's own
  "**Reading 3**", which F4 already flags as *"the only one pointing the right
  direction but... an explicit model-building CHOICE in unreconciled tension
  with this project's own asymmetric chirality mechanism (Lemma L5)... the one
  genuinely open thread from this line."* **This round localizes that thread
  precisely:** Reading 3 is not excludable with anything currently certified,
  and what would exclude it is round95's missing link -- not a new mechanism.
* **Even granting Family C, OB1 does not collapse.** `claim.md`'s stated
  consequence ("OB1 collapses from *which of `t=0,1`* to *why the flat orbit
  is realized at all*") requires `g` to be a **redundancy**. Family C is a
  discrete symmetry that the SM **breaks**. A broken discrete symmetry relates
  two physically distinct configurations; it does not identify them. So the
  C125 consequence fails on both readings of (ii) -- which is the one part of
  this verdict that no reading, tagging, or scope caveat can move.

### 3d. What condition (iii) does NOT show

For the **minimal** map `ι̃`, no inconsistency arises on `S⁶` at all -- `S⁶` is
untouched, the twist is preserved, `ind` stays `+1`. Question 3's "does the
map force an inconsistent action on the `S⁶` twist bundle" therefore has the
answer: **no, not for `ι̃`; only for Family B, where the `S⁶` action is forced
by the orientation bookkeeping rather than by the connection map.** And per
§3c, not in a way that decides Family C either.

---

## 4. The `Γ₄ = ±ω₃·Γ₆` identity, re-derived from scratch (the external item)

The external `Kimi_Agent` document asserts this in one file and, by its own
internal red team, refutes it in another. Neither side is taken on trust.

Setup [VERIFIED, `results_c125.json:D0-D3`]: `Cl(1,3) ⊗ Cl(3) ⊗ Cl(6)`, spinor
dimension `4·2·8 = 64 = 2^⌊13/2⌋` ✓; `Cl(9,0)` via `e_i = σ_i⊗Γ₇`,
`e_{3+a} = 1⊗Γ_a`; then `Γ^μ = γ^μ⊗1₁₆`, `Γ^{3+m} = iγ₅⊗e_m`. All `13×13`
anticommutators verified against `η = diag(+,−,…,−)`. `ω₁₃` verified central
and scalar, `= +1`.

**Reading 1 -- INTRINSIC (`ω₃` = the `S³`-intrinsic pseudoscalar, `Γ₆` = the
`S⁶` chirality, on the factorised module): FALSE.** [VERIFIED,
`results_c125.json:D5`] `1 ⊗ ω₃ ⊗ Γ₇` is not `+γ₅`, not `−γ₅`, and not even
proportional to `γ₅`, in **either** `Cl(3)` convention. One-line reason, and
it is sharp in this project's own convention:

> In this repo's own `S³` convention (`Z_i = iσ_i`, `Z² = −1`, `Cl(0,3)` --
> the registry's row for `round67` and descendants), the intrinsic
> pseudoscalar is `ω₃ = Z₁Z₂Z₃ = +1`, **the identity operator** [VERIFIED,
> `results_c125.json:D1`]. So "`ω₃·Γ₆`" intrinsically is just `Γ₆`, carrying
> no `S³` information whatsoever. (In `Cl(3,0)`, `ω₃ = i·1` -- still a scalar,
> still no `S³` information. The conjugate module `Z_i = −iσ_i` gives
> `ω₃ = −1` -- still a scalar.) An odd-dimensional Clifford factor has a
> *central* volume element; it cannot be a grading. **This is the general
> reason, not a convention artifact.**

**Reading 2 -- EMBEDDED (`Ω₃ := Γ⁴Γ⁵Γ⁶`, `Ω₆ := Γ⁷…Γ¹²`): TRUE, and forced.**
[VERIFIED, `results_c125.json:D4`] `Ω₃·Ω₆ = i·γ₅` exactly on the 64-dim module
(measured constant `0+1i`).

> **Not a discovery about the `S³/S⁶` split (skeptic-corrected downgrade).**
> It is forced in *every* irrep of `Cl(1,12)`: `ω₁₃ = Ω₄·(Ω₃Ω₆)` is central in
> odd dimension, hence a scalar `c`; with `Ω₄² = −1` and `γ₅ := iΩ₄` this
> gives `Ω₃Ω₆ = i·c·γ₅`, and `c = ω₁₃ = +1` predicts the measured `0+1i`
> without ever touching the split. **This makes the settlement of the external
> dispute STRONGER** -- the identity is convention-independent, not an
> artifact of the embedding chosen here; a different valid construction moves
> only the phase, which the measurement shows is `±i` either way.

**The `Z₂` law, with the side condition the previous draft omitted**
[VERIFIED, `results_c125.json:E2`]:

```
Ω₃ → ε₃Ω₃ ,  Ω₆ → ε₆Ω₆ ,  Ω₄ → ε₄Ω₄       under frame reflection
γ₅ = iΩ₄        ⟹  γ₅ → ε₄ γ₅              (route A)
γ₅ = −iΩ₃Ω₆     ⟹  γ₅ → ε₃ε₆ γ₅            (route B)
routes agree  ⟺  ε₄ = ε₃ε₆  ⟺  ε₁₃ = +1  ⟺  ω₁₃ preserved
```

Measured on all five reflection cases; the biconditional holds on all five.

**RETRACTED from the previous draft:** the inference "an `S³`-orientation
reversal with `S⁶` untouched flips 4D handedness, therefore `ι̃` flips SM
handedness". `ι̃` has `ε₁₃ = −1`, which is precisely where the two routes
disagree and where §1b says the reflected gammas generate the *other*
inequivalent module -- so no conjugation implements the map and "the handedness
flips" is not a determinate statement there, it is a choice of identification
between two modules. **The inference is withdrawn, not weakened.**

**What survives, and its tier.** On `ε₁₃ = +1` (i.e. on Families B and C, the
only ones that matter), the identity does give a determinate law:
`γ₅ → ε₄γ₅ = ε₃ε₆γ₅`. Inside a hypothetical `Spin(1,12)` parent -- the same
hypothetical C124 granted, and the one `SPIN13_TO_SPIN4_DECOMPOSITION.md`
explicitly disclaims -- this is exactly the `S⁶`-channel ↔ `S³`-`t`-sector
link round95 records as absent. `[INFERRED, conditional]`. **It is NOT used as
a kill argument anywhere in this file**; the verdict rests on §2a (torsion),
§2b (`H³` degree), and §3b (`(ii-twist)`), none of which need a 13D parent.

---

## 5. Answer to the kill criterion (question 4), stated plainly

**The claimed `g` does NOT exist. C125 is FALSIFIED.** Not softened: the
gauge-equivalence claim is false, and the `t=0`-vs-`t=1` question is a genuine
physical choice, not gauge redundancy.

Which condition fails, apportioned honestly:

| condition | verdict | why |
|---|---|---|
| (i) | **satisfiable** | the whole coset `O(4)\SO(4)` on the `S³` leg realizes it -- and nothing else does (§2a). |
| **`(ii-gauge)` "a genuine gauge transformation, not parity"** | **FAILS, universally, 8 of 8** | `H³(M₁₃;ℤ) = ℤ` on the `S³` class; every candidate acts by `deg = −1`; an isotopy-to-identity acts by `+1`. Needs no `Isom` factorisation, no Cerf/Hatcher, no KK premise. **This is the failing condition.** |
| `(ii-orient)` alone | satisfiable by exactly 2 families | `ε₄ = −ε₆` (§2c). |
| `(ii-twist)` | FAILS for Family B | `S⁶` is touched; `E ≠ Ē`. |
| (iii) | FAILS for Family B; **UNDECIDED for Family C** | Family B: `c₃ +2→−2`, `ind +1→−1`. Family C: nothing certified excludes it -- deciding it needs round95's missing link (§3c). |

**Corrected by the second skeptic pass -- there is no statement here that
no reading can move; the opposite was claimed and it does not survive.**
"Family C is a discrete symmetry the SM breaks, therefore OB1 does not
collapse" was found to commit the same category error Defect 3 already
diagnosed one section earlier (a fact about whether `P` symmetrizes ONE
configuration says nothing about whether `g` identifies TWO). **The
honest statement is conditional:** whether OB1 collapses under Family C
depends on whether `ε₄ε₆` (the relative orientation Family C flips) is a
physical datum or a labelling convention -- exactly what §3c leaves
UNDECIDED. If physical, OB1 does not collapse, but then (iii) should
also exclude Family C (contradicting "not excluded"). If convention,
Family C is not excluded, but then the two configurations are identical
in every transported datum and OB1 WOULD collapse. **Only one of these
two readings can hold; this round does not decide which.**

**The obstruction, named -- this is what C125's claim.md asks for.** It is a
**`Z₂` degree/component class**: the orientation character of the `S³` factor,
which §2a shows is *identical to* the `∇⁰↔∇¹` exchange character rather than
merely correlated with it, because the torsion **is** the volume tensor. Four
properties, stated including the unflattering one:

1. **Discrete.** No continuous parameter -- coupling, radius, normalization,
   `t` -- can move a `Z₂` class. Same shape as C124's `mod 4` argument, and
   equally immune to tuning.
2. **Exact, with a one-line proof.** Not a sampled result; a scaling law.
3. **It sharpens OB13's requirement, and adds a genuinely new half.** OB13:
   a selector must have a component odd in `(t−½)`. C125 says *why* -- the odd
   datum must be an **`S³`-orientation pseudo-invariant** (Chern-Simons-type,
   eta-type, or torsion-linear) -- **and adds**: it must not be accompanied by
   a compensating `M₄` or `S⁶` orientation flip, or the two `Z₂`s cancel and
   the selector goes blind. The second half is new; the first restates OB13.
4. **It does not narrow OB1 in the direction C125 hoped.** The hoped-for
   collapse does not happen. What *does* happen is a re-identification, and it
   is sharper than before: after `(ii-orient)` + `(ii-twist)` + (iii), the
   residual freedom is exactly LRSM parity (Family C), which nothing certified
   in this project excludes. **So "which of `t=0`, `t=1`" is now pinned to a
   named, concrete gap -- round95's unlinked-invariants gap -- rather than to
   an open-ended search.** OB1 is re-expressed and localized, not narrowed.

---

## Kill Analysis (Anti-Overfitting Gate)

### What this round KILLS

* **The C125 claim as pre-registered.** No `g` satisfies (i) + `(ii-gauge)`.
* **The "gauge redundancy" dissolution of OB1 / C25 / H1c, in general, not
  just for `ι`.** Now a theorem over the full isometry group with an `H³`
  backbone, not an observation about one map.
* **The intrinsic reading of `Γ₄ = ±ω₃Γ₆`**, for a general reason (an odd
  Clifford factor's volume element is central), sharpened in this project's
  own convention (`ω₃ = +1` in `Cl(0,3)`).
* **The claim's own equation of "orientation-preserving" with "gauge".**
  Family C is an explicit witness that they differ.
* **The previous draft's own §3c and §4 inferences** -- retracted above, not
  quietly amended.

### What this round does NOT kill

* **Family C / LRSM parity.** Not excluded by anything certified. This is the
  live residue and is stated as such.
* **Whether `(t=0,E)` and `(t=1,Ē)` are the same MODEL.** Family B is an
  honest isometry taking one to the other; C125 freezes `E` per F2, so this
  round kills Family B *as an answer to C125's question*, not as a possible
  statement about the model. **Caveat Gate: named alternative, pearled below.**
* **Whether a `t`-selector exists.** Untouched; OB1's own question.
* **Non-product / warped `M₁₃`.** §1a assumes a strict product metric. (The
  `H³` argument is more robust but still assumes the candidate is a product
  map, which §1a supplies.)
* **The hypothetical-13D-parent question itself.**
* `N_gen=3`'s CONDITIONAL status, `lambda = FREE_COUPLING_PARAMETER`,
  `safe_for_runtime = False`, C123's `PARTIAL`, C124's `STRUCTURAL_NO_GO`,
  OB1's `PARKED` -- all unaffected, as pre-registered.

### Relaxation Map (one assumption changed per variant, none attempted here)

| Variant | Single assumption changed | Kill criterion |
|---|---|---|
| W1 | Allow the vielbein to change | Vacuous as stated (§0a: frame rotations do not change `∇`). Non-trivial only if the METRIC also moves -- then it is a moduli question and must state which moduli are frozen. |
| W2 | Allow the twist to move: is `(t=0,E) ≅ (t=1,Ē)` as a model? | Does `ind = +1` survive relative to the *transported* orientation, and does anything physical distinguish the two? If nothing does, F2's freezing of `E` is itself the hand-insertion C124's criterion 2 was written to detect. |
| W3 | Drop the strict-product background | Does §1a's factorisation survive on a warped/fibred `M₁₃`? If the factors mix, the per-factor `Z₂` bookkeeping is unavailable -- though the `H³` argument may survive independently. |
| W4 | Accept LRSM parity (Family C) as a real, broken global symmetry | **This is where §3c says the question actually goes.** Kill criterion: does closing round95's `S⁶`↔`S³` link exclude Family C, or does it instead certify it? Both outcomes are informative. |
| W5 | Grant the hypothetical `Spin(1,12)` parent and use §4's `γ₅ = −iΩ₃Ω₆` | Does the link survive once the parent is concrete enough to carry its own consistency conditions? C124 already showed the parent's invariant algebra is severely constrained; this may be self-defeating. |

---

## Proposed pearls (not written to `pearl_registry/INDEX.md` by this round --
editing the registry is outside this round's brief, per C124's precedent)

**Pearl Gate.** *Impact score revised down from 6 to 4 after the skeptic pass
showed the identity is forced rather than unexpected -- recorded, not hidden.*
* **observation:** in any irrep of `Cl(1,12)`, `γ₅ = −i·Ω₃·Ω₆` -- the 4D
  chirality is the product of the two internal pseudoscalars -- but the
  resulting `Z₂` law is determinate **only on `ε₁₃ = +1`**; off that locus the
  map exchanges the two inequivalent modules and the law is not merely wrong,
  it is ill-posed.
* **falsifiable_prediction:** any future construction linking G74B's `S⁶`-only
  chirality to the `S³` `t`-sector must reproduce `γ₅ → ε₄γ₅ = ε₃ε₆γ₅` **and
  must state its `ε₁₃ = +1` side condition**; a proposed link making 4D
  handedness depend on `ε₆` alone, or on `ε₃` alone, or stated without the
  side condition, is wrong.
* **impact_score:** 4 -- forced identity, but it touches an assumption
  round90/91/95 and L5 all depend on.
* **trigger_condition:** any attempt to close round95's unlinked-invariants
  gap, or any concrete 13D parent proposal.
* **next_check:** 2026-11-01.

**Caveat Gate (named, untested alternative written down in this file's own
scope caveat):**
* **observation:** Family B is a genuine isometry taking `(t=0, E)` to
  `(t=1, Ē)`; whether those are the same MODEL has never been tested.
  Separately, Family C (LRSM parity) is excluded by nothing certified.
* **falsifiable_prediction:** if `(t=0,E) ≅ (t=1,Ē)`, then F2's freezing of
  `E` rather than `Ē` is a hand-insertion and OB1's `t` question is a proxy
  for an `S⁶`-orientation-convention question.
* **impact_score:** 7 -- it would relocate OB1's question to a different
  factor of the product.
* **trigger_condition:** any OB1 round varying the `S⁶` orientation
  convention, or any F2 re-examination.
* **next_check:** 2026-11-01.

**Reusable pre-filter (sibling to C119's Künneth filter and C124's
ε/η-sector filter):**
* On a product of pairwise non-isomorphic irreducible factors, the component
  class in `π₀(Isom)` is a **per-factor** invariant, and on a product with a
  contractible factor the `H^k` degree of each sphere factor is an independent
  homotopy obstruction. Any proposed "gauge equivalence" acting in a
  non-identity component of ONE factor is not a gauge transformation, no
  matter what is done elsewhere -- **and arranging the TOTAL orientation to be
  `+1` by compensating on another factor does not help.** Total orientation is
  one `Z₂` quotient of a `Z₂ⁿ`-graded obstruction. Companion: on a Lie group
  with a bi-invariant metric **of dimension exactly 3** [scope-corrected,
  second skeptic pass -- does NOT generalize to `dim≥4`, where the
  Cartan-Schouten torsion is the Cartan 3-form, not the volume top-form],
  the Cartan-Schouten torsion **is** the volume
  tensor, so "swaps the `±` connections" and "reverses orientation" are the
  same character -- check this before treating them as independent conditions,
  and check `dim=3` before reusing this fact on any other factor of a product.

---

## What this round does NOT show

1. Does **not** resolve OB1 or move it out of PARKED. No reopen condition is
   met.
2. Does **not** identify a `t`-selector or show one exists.
3. Does **not** exclude Family C (LRSM parity). It shows nothing certified in
   this project does.
4. Does **not** establish that `ι̃` flips SM handedness -- that inference was
   made in a previous draft and is **RETRACTED** (§4).
5. Does **not** claim anything about the external `Kimi_Agent` document beyond
   that its disputed identity is TRUE in the embedded reading (and forced, not
   convention-dependent) and FALSE in the intrinsic reading. Which reading
   each of its files intended is `[HYPOTHESIS]`; its internals were not
   inspected.
6. Does **not** touch C123's `PARTIAL`, C124's `STRUCTURAL_NO_GO`, C119's F1
   FAIL, or C121's eta NULL.
7. Does **not** change `N_gen=3`, `lambda`, or `safe_for_runtime`.
8. Does **not** solicit Tom Lawrence.

---

## Verification

**Gate checks:** 14 of 14 pass (`ruff` clean). Three of the original eleven
(`B1`, `B1b`, `E2`) **could not fail** and were replaced; the count went up
because `B0`, `B0b`, `B3` were added. Reported here rather than as "all checks
pass". **Second skeptic pass found the rebuilt `B1` is algebraically
identical to `B0` (both test the same finite-difference derivative) --
"14 of 14" double-counts one check; the genuinely independent count is 13.
And `B3` itself only partially independently verifies its own claim, see
the tag correction above.**

| tag | claim |
|---|---|
| `[VERIFIED]` | `ι(g) = g⁻¹` (max err `4.4e−16`, 200 samples). |
| `[VERIFIED]` | `ι ∘ φ_{a,b} ∘ ι = φ_{b,a}` (max err `2.7e−16`, 200 samples). **Negative control passes** (median diff `0.96` against `φ_{a,b}`). |
| `[VERIFIED]` | `det(dφ|_{TS³}) = −1` on the `ι`-coset, `+1` on `SO(4)`, 100 maps each, ambient-orientation-pinned frame (C39's QR lesson applied). Reproduces C39 independently. |
| `[VERIFIED]` | **B0**: `d/ds Ad_{conj(g e^{s e_i})} = −ad_{e_i}Ad_ḡ` by finite difference, max err `6.7e−10`. **Negative control (wrong sign) deviates by `4.00`** -- this test can fail. |
| `[VERIFIED]` | **B1** (rebuilt): `∇¹` has the right-invariant frame parallel, assembled from the *measured* derivative, max err `6.8e−10`. Negative control `1.998`. |
| `[INFERRED -- hand derivation confirmed correct by TWO independent skeptic passes; script wrapper does not itself verify the frame]` | **B3**: `T⁰ = −2ε`, `T¹ = +2ε = −T⁰ ≠ 0`; pullback by `R ∈ O(3)` scales by `det R` (400 elements, both signs); `φ_*T⁰ = T¹` **iff** `det R < 0` on all 400. **Second skeptic pass found**: the script constructs `comp[i,j,k]` from the formula and checks it against itself (tautological, like the FIRST pass's `B1` defect); the one genuinely load-bearing fact -- that `left_frame()`/`qmul()` actually produces an orthonormal frame with `[X_i,X_j]=2ε_{ijk}X_k` -- is asserted, not computed. The underlying mathematics is independently confirmed correct by hand (both skeptic passes, and this session); only the script's own claim to be an independent numerical check is downgraded. |
| `[VERIFIED, SAMPLED]` | **B2** cross-check: frame-transition spreads `2.10e−10` (`SO(4)`, left) / `≥1.650` (`SO(4)`, right) / `≥1.745` (`ι`-coset, left) / `2.24e−10` (`ι`-coset, right). **12 `(a,b)` pairs per coset × 25 base points -- a corroboration, not the proof. These four are RNG-stream-dependent and shift between runs; the pass/fail thresholds (`<1e−4` vs `>1e−2`) are what is stable.** |
| `[VERIFIED]` | 8-row sign-triple table; 2 survivors under `(ii-orient)`, 0 under `(ii-gauge)`. **Exhaustive over the sign triple, NOT over `π₀` (16 classes).** |
| `[VERIFIED]` | `Cl(1,12)` rebuilt, all `13×13` anticommutators match `η`; `dim = 64`; `ω₁₃` central and scalar (`+1`). |
| `[VERIFIED]` | `Ω₃Ω₆ = iγ₅` exactly; `1⊗ω₃⊗Γ₇` not proportional to `γ₅` in either `Cl(3)` convention. |
| `[VERIFIED]` | `ω₃ = Z₁Z₂Z₃ = +1` in this project's own `Cl(0,3)` convention. |
| `[VERIFIED]` | **E2 (rebuilt)**: the two `γ₅` routes agree **iff** `ω₁₃` is preserved, on all 5 reflection cases. This is the over-determination, measured. |

**`[VERIFIED]` -- own derivation, hand, not script:**
* `T^t ∝` volume tensor on `S³`, hence §2a's theorem (implemented as B3).
* Frame gauge transformations cannot relate `∇⁰`, `∇¹` (torsion is a tensor).
* `H³(M₁₃;ℤ) = ℤ` by Künneth with `M₄` contractible; degree `= ε₃`.
* Every orientation-reversing isometry of `S⁶` is `−h`, `h ∈ SO(7)`, hence
  fails to preserve the `G₂`-structure (to `−φ` if `h ∈ G₂`, else to a third
  structure).
* Exchanging the two factors of `SU(2)×SU(2)` is an outer automorphism
  (relative statement only -- see §2b's remark on the `SU(4)` counter).

**`[INFERRED]` -- logical consequences, chain stated, tier corrected from an
earlier `[VERIFIED]` mis-tag:**
* `c₃(Ē) = (−1)³c₃(E) = −2`, `ind → −1`. `block_F` is hardcoded arithmetic on
  G73's cited `c₃(S⁻)=+2`, **not a computational check**.
* §4's relevance to round95's gap -- valid only inside the hypothetical
  `Spin(1,12)` parent.

**`[CITED]` -- project facts reused, not re-derived:** G73; G74A (number only,
lemmas not); G74B; C38; C39; round90; round91 (with its own REFUTED-premise
correction noted); round95; round113; C124; gate G97 (rounds 102/108/109);
`docs/clifford_convention_registry.md`; `SPIN13_TO_SPIN4_DECOMPOSITION.md`;
`PARENT_ACTION_GATE.md` F1/F2/F3/F4/F5.

**`[CITED]` -- external, NOT re-derived here:**
* J. Cerf (1968) -- `π₀(Diff(S³)) = ℤ₂`. A. Hatcher, *A proof of the Smale
  conjecture*, Ann. Math. **117** (1983) 553 -- the stronger `Diff(S³) ≃ O(4)`.
  Attribution corrected after the skeptic pass; used only to close an escape
  that (0a) already closes.
* de Rham decomposition theorem -- standard.
* **Kaluza-Klein: "the 4D gauge group descends from `Isom₀`."** Standard lore
  (gauge bosons ↔ Killing vectors), **and contested** (the "no global
  symmetries in quantum gravity" position would gauge discrete geometric
  symmetries). Previously mis-tagged `[VERIFIED]` against a truth table.
  §2b's `H³` argument was added specifically so the verdict does not depend
  on it.

**`[HYPOTHESIS]`:** that the external document's two files each took one of
§4's two readings. Not inspected.

**`[UNKNOWN]` / not checked:**
* Everything in "What this round does NOT kill" and W1-W5.
* Whether Family C is excluded by anything at all beyond `(ii-gauge)`.
* Whether Lorentzian de Rham subtleties (Wu's theorem) admit an exotic
  isometry of a Lorentzian × Riemannian product. The `H³` argument does not
  depend on this; §1a's factorisation does.

**No pytest suite touched** (no shared code modified); the one new script is
self-contained inside this experiment folder.

## Check

```bash
python experiments/20260901-c125-full-gauge-equivalence-gate/c125_full_gauge_equivalence.py
```
Expect all 14 checks `true`; `candidates surviving the LITERAL orientation
reading: 2`; `candidates surviving the GAUGE (identity-component) reading: 0`;
embedded-reading constant `0+1i`; intrinsic reading `false` in both
conventions; and in `results_c125.json`, `E2_gamma5_two_routes` showing
`routeA_equals_routeB == omega13_preserved` on all five rows.

Falsifier for the B1 tautology that this round repaired (should now be
impossible to reproduce): feed the old `B1` body an arbitrary `A`
(`np.ones((3,3))`) -- the old residual stayed `0.0`; the rebuilt `B1` uses a
finite-difference derivative and moves.
