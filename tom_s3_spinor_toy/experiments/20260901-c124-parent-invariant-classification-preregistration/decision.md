# C124 decision -- blind execution of the frozen pre-registration.
#
# THEOREM STATEMENT, class-qualified in the first line per same-day
# external review: there exists no LOCAL, POLYNOMIAL, FIRST-ORDER,
# BOSONIC 13D-Lorentz-covariant invariant -- built from the vielbein
# e, torsion T=De, curvature R=dω+ω^ω, and their eta/epsilon
# contractions only (the Lovelock-Cartan class, plus the wider
# mismatched-index-contraction class V5 also checked and killed below)
# -- that reduces, on the strict product M13=M4xS3xS6, to the target
# CS3(omega_S3)^ch3(E_S6)^vol4 term. The two factors that term needs
# live in MUTUALLY EXCLUSIVE sectors of THIS invariant algebra.
# Outcome (c). Everything the class excludes is listed explicitly in
# "What this round does NOT kill", not left implicit.
#
# NOT covered, NOT closed, by this theorem (see that section for the
# full list, itemized per the same review): explicit extra covariant
# derivatives (DT, DR, ...) beyond Bianchi-reducible ones; the inverse
# vielbein / Hodge star used non-polynomially (e.g. a genuine
# Yang-Mills-type integral R{AB}^Hodge-dual(R{AB}), which is what
# C123's own Yang-Mills claim actually was -- an S3-INTERNAL 3D
# functional using S3's own Hodge star, never claimed to be a
# reduction of a 13D-covariant invariant in the first place, and in
# any case dimensionally EXCLUDED from this classification's own
# epsilon-sector S3 leg, which admits at most one explicit curvature
# factor (n_R in {0,1}, forced by 2n_R+n_e=3) -- a genuine |R|^2-type
# term cannot even be written as a leg of this algebra); an enlarged
# gauge algebra beyond Lorentz SO(1,12) (e.g. (A)dS/Poincare gauging
# with e and omega as one connection -- checked in Sector III only for
# the specific AdS Pfaffian, not exhaustively); non-polynomial local
# functions; additional p-form matter fields; boundary/defect terms;
# nonlocal or quantum effective actions.

**Verdict (2026-09-01, blind execution in a fresh context; SKEPTIC-
CONFIRMED same day, see correction block below):**
`STRUCTURAL_NO_GO__CONFIRMED_BY_FL_STEP_8A__CRITERION_1_AND_CRITERION_2_BOTH_FAIL__NO_13D_CHERN_SIMONS_FORM_BECAUSE_DEGREE_14_CHERN_WEIL_RING_GENERATOR_UNREACHABLE_MOD_4__EPS_SECTOR_IS_EXACTLY_TORSION_FREE_HENCE_EVEN_IN_T__NONEPS_SECTOR_VANISHES_ON_FROZEN_BACKGROUND_NO_DEGREE_6_S6_LEG_EXISTS__BOTH_NEGATIVE_CONTROLS_FAIL__V5_MISMATCHED_INDEX_CLASS_ALSO_CHECKED_AND_DIES__PARTIAL_SCOPE_LOVELOCK_CARTAN_PLUS_V5_CLASS_BOSONIC_STRICT_PRODUCT_BACKGROUND`

**Status:** OB1 stays PARKED. No reopen condition met. This is the
`(c)` branch of `claim.md`'s own three-outcome list -- the *stronger*
structural no-go, not the "dies honestly at the gate" branch `(b)` and
certainly not `(a)`.

**Completeness:** `PARTIAL` in exactly one named respect -- the
classification is complete and exhaustive **within the Lovelock-Cartan
class** (Lagrangian = polynomial in `e`, `T^A`, `R^{AB}`, bosonic, no
explicit extra covariant derivatives), on a **strict product**
background. Outside that class it is not attempted. Scope boundary is
stated in full below rather than smoothed over; per `claim.md`'s own
instruction, reporting PARTIAL with a named boundary is preferred to
manufactured completeness.

**Gate fields assessed:** `PARENT_ACTION_GATE.md` F1 (background, reused
unchanged), F2 (twist, reused unchanged), F4 (t-selection mechanism --
this is the field the round is about). F3 reused by citation
(round113). F5, F6, F7 not assessed.

---

## ⚠️ SKEPTIC PASS RUN AND CONFIRMED, 2026-09-01, same day (context-blind,
`Agent(skeptic, model=opus)`, claim.md+decision.md+script only, no
session history). **Verdict: CONFIRMED. Two real factual errors found
and repaired below, one missed check run and found to STRENGTHEN the
result, several framing overreaches narrowed. No verdict flips.**

**Errors found, both non-load-bearing, both repaired in place further
down:**
1. **"`so(1,12)` has odd rank" is factually wrong** -- `rank so(2n) =
   rank so(2n+1) = n`, so `rank so(13) = 6` (even). The document even
   self-contradicts eight lines later, calling `SO(12,2)`
   "even rank 14" when `rank so(14) = 7` is itself odd. The correct
   criterion for Pfaffian/Euler-class existence is the **parity of the
   defining representation's dimension** (13 is odd -- a Pfaffian needs
   an even-size antisymmetric matrix), not the rank. **Consequence:
   none** -- a hypothetical `so(13)` Euler form would be a **13-form**
   (odd), never the degree-14 object L3 needs, so the sub-claim was
   irrelevant to the argument it sat inside.
2. **"No closed invariant 14-form exists" is literally false as
   written.** Skeptic exhibits a counterexample:
   `Ω₁₄ = ε_{A₁…A₁₃}T^{A₁}∧e^{A₂}∧…∧e^{A₁₃} = (1/13)·d(vol₁₃)` --
   closed (`dΩ₁₄=0` since its two terms vanish by `R^{AA}=0` and
   `T∧T` symmetric-vs-`ε` antisymmetric respectively) and manifestly
   Lorentz invariant. **Consequence: none to the conclusion, but the
   premise needed repair.** The correct statement is about the
   **Chern-Weil ring** (non-trivial transgressions), not about closed
   invariant forms as such -- `Ω₁₄` is *exact with a globally-defined
   invariant potential* (`vol₁₃` itself), and characteristic-class
   theory is exactly the theory that quotients such forms out. Repaired
   statement: *with every ring generator (Pontryagin, Nieh-Yan) at
   degree ≡0 mod 4, every quasi-invariant CS/transgression Lagrangian
   has degree ≡3 mod 4; `13≡1 mod 4`, unreachable.* Same conclusion,
   correct reason -- see the corrected Step-(b) Sector III text below.

**Check run that was missing, found to STRENGTHEN the no-go:** the
round's scope was "Lovelock-Cartan class" (polynomial in 2-forms,
bosonic, no explicit extra derivatives) -- but that excludes a genuine
third class: mismatched-index-pair curvature contractions
(`R_{AB}{}^{CD}R_{CD}{}^{AB}`-type scalar densities) which use no extra
derivatives but are not polynomials in the 2-forms `e,T,R` wedged
together. Skeptic checked this class directly (scalar-density
language, `L=f·vol₁₃`): the SAME parity result holds
(`3N_T+4N_R even/odd` mirrors the form-language result exactly, since
`ε·ε=δ` maps one language's ε-sector to the other's no-ε-sector), and
an odd-in-`x` member of this wider class must carry `ε₁₃`, whose S⁶
slots can only be filled by round-`S⁶` curvature components -- which
vanish identically against `ε^{abcdef}` (repeated index, since
round-`S⁶` curvature is built purely from `δ`'s). **This class also
dies, for a related-but-distinct reason** -- named as new Relaxation
Map item V5 below, strengthening rather than narrowing the verdict.

**Also found, independent of both above:** L1 is provably STRONGER than
originally derived -- not just `n_T=0`, but **no η-contractions at all**
inside the ε-sector (the document's split into "ε-carried" vs
"extra η-contracted" fields was never justified against a field
putting some indices on ε and some on η; skeptic re-derived without
that assumption and got the same `n_T=0` plus this extra fact). Bonus,
checked by skeptic, not attempted by this round: **adding an
independent 13D gauge field does not rescue Sector I either** -- the
identical count with a gauge-field term added still forces
`n_T=n_F=0`. Any V1 rescue attempt (gauge field addition) must
therefore route entirely through Sector III (a genuine degree-14
characteristic class like `tr F⁷`), never through Sector I -- this
sharpens V1's own kill criterion in the Relaxation Map below.

**Framing overreaches, narrowed, no verdict change:** criterion 2's
"two independent ways" is really one way -- way (ii), "the frozen
framework takes the product as primitive," is circular given this
round's own admission that the question is only non-vacuous under a
*hypothetical* 13D parent; the verdict rests on way (i) alone (`ch₃(E)`
is not seen by any 13D-covariant invariant), which is sound. Control 1's
"a covariant invariant **necessarily** fails this control" overreaches --
narrow to: the specific closest cousin's S³ leg (`ε_{ijk}R^{ij}e^k`) is
nonzero for *any* 3-manifold, so *that* term does not distinguish S³;
the universal claim was not shown. The Step-(d) one-liner "`vol₄` ...
require[s] the ε" is also literally wrong (contradicted by the round's
own `results_c124.json`, which lists degree-4 η-blocks `[A₄,C₄,P₄]` on
M₄) -- corrected inline below.

**Evidence-tier correction:** the script's `[VERIFIED]` tags on the
Sector I/III arithmetic overstate the tier -- `epsilon_sector()` and
`so_1_12_has_euler_class` hard-code the very quantities (`deg_extra=0`,
`13%2==0`) the lemmas are supposed to establish; the script restates the
hand derivation rather than independently checking it. Downgrade those
specific tags to `[VERIFIED -- hand derivation, script is a
restatement]`. Does not affect truth (skeptic re-derived both lemmas
independently, by hand, from scratch).

**The one place the verdict could still move, per skeptic's own
assessment (confidence MEDIUM-HIGH on this leg only, HIGH on L1/L2):**
completeness of "the closed-invariant ring is exactly Pontryagin +
Nieh-Yan, nothing else" is literature-asserted (Zanelli hep-th/0502193),
never verified in this repo -- L3 is the only leg covering bare-`ω`
(non-polynomial) Lagrangians. Marked `[UNKNOWN]` alongside the already-
flagged Mardones-Zanelli exhaustiveness item. **Concrete, cheap, named
next check:** directly enumerate η-sector 14-forms (even `N_T`, block
products summing to 14: `B₃∧B₁₁`, `B₅∧B₉`, `B₃∧{A₄,C₄,P₄}∧B₇`, ...) and
test each for closedness under `De=T, DT=Re, DR=0` -- a finite,
mechanical computation. Not attempted this round.

---

## Search-order compliance (mandatory, per `claim.md`)

The frozen order was
`all admissible 13D invariant tensors -> all admissible 13-forms ->
4+3+6 reduction -> search the reduced output for a CS_3-shaped term`,
with the reverse order explicitly forbidden.

Executed in that order. Steps (a)-(c) are implemented in
`c124_invariant_enumeration.py`, whose output
(`results_c124.json`) was produced and frozen **before** any comparison
against the target expression; the script's own docstring records this.
Step (d) is the "Inspection of the reduced output" section below, and
nothing in steps (a)-(c) refers to `CS_3`, `ch_3`, or `vol_4`.

---

## Step (a) -- the admissible 13D field content, established first

[VERIFIED, from project docs] The frozen content
(`PARENT_ACTION_GATE.md` F1/F2/F3/F5) supplies, as parent-level fields:

| Object | Lorentz indices | Form degree | Source |
|---|---|---|---|
| vielbein `e^A` | 1 | 1 | F1 (metric ansatz) |
| torsion `T^A = De^A` | 1 | 2 | F3 (`∇^t_XY = t[X,Y]` is a *metric connection with torsion*) |
| curvature `R^{AB} = dω^{AB} + ω^A{}_C ω^{CB}` | 2 | 2 | F3 |
| invariant tensors `η_{AB}`, `ε_{A_1…A_13}` | -- | -- | Lorentz structure |

[VERIFIED, from project docs -- **this is a finding, not a formality**]
**There is no independent 13D gauge field in the frozen content.**
`PARENT_ACTION_GATE.md` F1/F2/F5 name only a metric ansatz, a twist
bundle *on `S⁶`*, and Dirac operators. The twist bundle is
`E = S⁻ = T^{1,0}S⁶ ⊕ ℂ` (G69/G73) -- a summand of `S⁶`'s **own spinor
bundle**, constructed from the `S⁶` `SU(3)`-structure, i.e. it exists
only *after* the product ansatz and the `SO(6)→SU(3)` reduction. The
`G_eff` Pati-Salam content (rounds 90-112) arises from internal
isometry/holonomy, not from a fundamental 13D Yang-Mills field. The one
flux-like object ever considered (round115) is on F4's *already-tried
and rejected* list, not in the frozen content.

[VERIFIED, `SPIN13_TO_SPIN4_DECOMPOSITION.md:5-16`] The project's own
audit states, verbatim, that *"There is no established `Spin(1,12)`
structure group in this project ... no consistent 13D parent theory is
claimed"*, and that the `4 × S³ × S⁶` product is **treated as
independent factors from the start**. C124's question is therefore only
non-vacuous under a *hypothetical* 13D parent with local `SO(1,12)`;
that hypothetical is what is classified below. This is stated up front
because it already bears on criterion 2: at the level of the frozen
framework the split is primitive, i.e. inserted by construction.

**Scope boundary (named, not hidden):** fermion bilinears are excluded
(bosonic background, `⟨ψ⟩ = 0`); terms with explicit extra covariant
derivatives beyond the Bianchi-reducible `DT^A = R^A{}_B e^B`, `DR = 0`
are excluded -- this is exactly the standard Lovelock-Cartan class.

---

## Step (b) -- exhaustive enumeration of admissible 13-forms

A local Lorentz scalar 13-form must contract every index either with the
single `ε_{A_1…A_13}` or pairwise with `η_{AB}`. That splits the space
into two disjoint sectors. Both are enumerated exhaustively.

### Sector I -- the `ε` sector: exactly 7 terms, all torsion-free

[VERIFIED, own derivation + `results_c124.json:epsilon_sector_*`]
Write a monomial as `ε_{A_1…A_13} × (fields carrying those 13 indices)
× (extra η-contracted fields)`. For the `ε`-carried part,
```
index count : 2 n_R + n_T + n_e = 13
form degree : 2 n_R + 2 n_T + n_e = 13 - deg_extra
subtract    : n_T = - deg_extra
```
Since every field has non-negative form degree, `deg_extra ≥ 0`, so
**`n_T = 0` and `deg_extra = 0` exactly.** Brute-force enumeration
returns exactly 7 solutions, all with `n_T = 0`:
```
(n_R, n_T, n_e) = (0,0,13) (1,0,11) (2,0,9) (3,0,7) (4,0,5) (5,0,3) (6,0,1)
```
i.e. precisely the Lovelock series
`L_p = ε_{A_1…A_13} R^{A_1A_2}…R^{A_{2p-1}A_{2p}} e^{A_{2p+1}}…e^{A_13}`,
`p = 0…6`, and **nothing else**. No explicit torsion can appear in a
13-form carrying the `ε`.

[CITED, Zanelli hep-th/0502193 eqs. (49)-(50)] This reproduces the
standard Lovelock Lagrangian series in `D` dimensions.

### Sector II -- the `η`-contracted sector: odd torsion count, forced

[VERIFIED, own derivation + `results_c124.json:noneps_parity`]
Pairwise `η` contraction forces an even index count, so
`n_T = 13 - even = ODD`. All 12 admissible `(n_R, n_T, n_e)` solutions
have odd `n_T`. **Every non-`ε` 13-form carries an odd number of
torsion 2-forms** -- this is the only place odd powers of the torsion
parameter can come from, and the classification finds it without ever
looking for it.

[VERIFIED, own derivation] The index-contraction graph of such a
monomial decomposes into closed `R`-cycles and open chains terminating
on `e`'s or `T`'s, giving exactly four families; the (anti)symmetry of
`R^{ab}`, of `e^a ∧ e^b` (1-forms anticommute) and of `T^a ∧ T^b`
(2-forms commute) kills half of each:
```
A_{2n}   = e R^{n-1} e   (n even, n≥2)  -> degrees 4, 8, 12
B_{2n+1} = T R^{n-1} e   (any n≥1)      -> degrees 3, 5, 7, 9, 11, 13
C_{2n+2} = T R^{n-1} T   (n odd, n≥1)   -> degrees 4, 8, 12
P_{2n}   = tr R^n        (n even)       -> degrees 4, 8, 12
```
[CITED, Zanelli hep-th/0502193 eqs. (65)-(68), attributing the general
construction to Mardones & Zanelli, *Lovelock-Cartan theory of gravity*,
Class. Quantum Grav. **8** (1991) 1545] -- the independently derived
list above matches the published one term for term, including the
even/odd `n` restrictions. This is the round's one genuine external
cross-check of the classification.

**Available block degrees: `{3, 4, 5, 7, 8, 9, 11, 12, 13}`. Degrees 6
and 10 are missing.** This is not an accident of the search; it is
forced by the parity restrictions above.

### Sector III -- Chern-Simons / transgression 13-forms: none exist

[VERIFIED -- own derivation, corrected by same-day skeptic pass, see
the correction block above] A 13D Chern-Simons Lagrangian (equivalently,
a transgression / "difference of two Chern-Simons forms", the escape
hatch `claim.md` explicitly allows) requires a nonzero element of the
**Chern-Weil ring** at degree 14 -- i.e. a genuinely non-trivial
characteristic class, not merely a closed invariant 14-form (closed
invariant forms with a globally-defined invariant potential, such as
`Ω₁₄=ε T e^{12}=(1/13)d(vol₁₃)`, exist trivially and are exactly what
the Chern-Weil ring quotients out -- their "transgression" back down to
13D is itself Lorentz-invariant and contains no bare `ω`, i.e. no CS
content). The ring's generators (Pontryagin forms `P_{4k}`, the Nieh-Yan
form `N_4=T^aT_a-e^ae^bR_{ab}`, and products) all sit at degree ≡0
(mod 4); `so(13)`'s odd-dimensional (13) defining representation admits
no Pfaffian/Euler generator at all (the operative criterion is the
**parity of the defining representation's dimension**, not the algebra's
rank -- `rank so(13)=6`, itself even; a hypothetical Euler form would in
any case sit at degree 13, never at the needed degree 14). So the ring
has no generator, and no product of generators, at degree 14: `14≡2
(mod 4)`, not representable as a sum from `{4,8,12}`.

**Conclusion: no quasi-invariant (bare-`ω`-carrying) Chern-Simons 13-form
exists.** [CITED, Zanelli hep-th/0502193, footnote to §4.4: the number of
torsion-dependent terms "grows as the partitions of `D/4`" --
independent corroboration that this whole sector is organised in
multiples of 4.] [UNKNOWN, flagged by skeptic pass: the completeness of
"the ring is exactly Pontryagin+Nieh-Yan, nothing else" is
literature-asserted, not verified in this repo -- see the correction
block above for the named, cheap follow-up check.]

The one degree-14 invariant that *does* exist requires enlarging
`SO(1,12)` to the AdS group `SO(12,2)` (`rank so(14)=7`, itself odd --
the earlier "even rank 14" phrasing conflated rank with representation
dimension, same error as above, corrected here), whose Euler form
`E_14 = ε_{A_1…A_14}F^{A_1A_2}…F^{A_13A_14}` transgresses to the 13D
AdS Chern-Simons gravity Lagrangian. [CITED, Zanelli hep-th/0502193
eqs. (107)-(109)] That Lagrangian is
`L^{(A)dS}_{2n-1} = Σ_p ᾱ_p L^{(2n-1,p)}` -- **a Lovelock combination
with the coefficients fixed**, i.e. it lies *inside Sector I*, is
manifestly Lorentz invariant, and contains no bare `ω`. It supplies no
new structure. [VERIFIED, arithmetic] "Exotic" (Pontryagin-based) CS
gravities require `D+1 ≡ 0 (mod 4)`, i.e. `D = 4k-1` (3, 7, 11, 15);
`D = 13` is not of that form, so **13D admits no exotic CS gravity
either**.

---

## Step (c) -- reduction on the frozen background `M₄ × S³ × S⁶`

The frozen F1 background is a **strict product with a product metric**,
so `η_{AB}` and `R^{AB}` are block diagonal and every `η`-contraction
chain lies entirely inside one factor; `ε_{A_1…A_13}` factorises as
`ε_4 ⊗ ε_3 ⊗ ε_6`. A 13-form must therefore split as
`(4-form on M₄) ∧ (3-form on S³) ∧ (6-form on S⁶)`.

### Sector II collapses to zero

[VERIFIED, `results_c124.json:noneps_factor_content`] Partitioning by
factor:
* `M₄` leg (degree 4): `A_4`, `C_4`, or `P_4`.
* `S³` leg (degree 3): **`B_3 = e_i ∧ T^i` and nothing else.**
* `S⁶` leg (degree 6): **empty.** Degree 6 is not an available block
  degree, and the only product route `3+3` is `B_3 ∧ B_3 = 0` (an
  odd-degree form wedged with itself).

**Every non-`ε` 13-form vanishes identically on the frozen background.**
This does not depend on `M₄` being flat, on `S⁶`'s radius, or on `t` --
the `S⁶` leg simply cannot be built.

### Sector I: the `t`-dependence, computed

[VERIFIED, own symbolic computation, `results_c124.json:S3_*`] For
`∇^t_X Y = t[X,Y]` on `S³` with `[X_i,X_j] = 2ε_{ijk}X_k`:
* torsion `T^t(X_i,X_j) = (2t-1)[X_i,X_j]` -- **linear and odd** in
  `x := t - 1/2` (checked: `T^{01} = 4t-2`);
* curvature `R^t = t(t-1)·R_0` with `R_0` `t`-independent -- verified on
  all 12 non-vanishing components of `R(X_i,X_j)X_k` (the check was
  first written in a form that was silently vacuous -- several
  components vanish identically -- and was rewritten to require
  `len(nonzero) > 0`; the corrected check is what is reported);
* `Scal(∇^t) = -24t(t-1) = 6 - 24x²`, **even** in `x`, `= 6` at
  `t = 1/2`, `= 0` at `t = 0` and `t = 1`. Cross-check: this reproduces
  round111's `Scal(t) = Scal_LC - 6(2t-1)²` **exactly**
  (`matches_round111_Scal_formula: true`) -- an independent
  re-derivation, not a citation.

[VERIFIED, `results_c124.json:epsilon_sector_leg_options`] With
`n_T = 0` forced, each leg satisfies `2n_R^F + n_e^F = dim F`:
* `M₄`: `(n_R,n_e) ∈ {(0,4), (1,2), (2,0)}` -- a bare `vol₄` requires
  `n_R = 0`;
* `S³`: `{(0,3), (1,1)}` -- i.e. `vol₃`, or `ε_{ijk}R^{ij}∧e^k`;
* `S⁶`: `{(0,6), (1,4), (2,2), (3,0)}` -- the last being the `S⁶` Euler
  density `ε_{abcdef}R^{ab}R^{cd}R^{ef}`.

Only the `S³` leg carries `t`, and only through `R^t ∝ t(t-1)`.
Therefore **the entire 13D Lovelock-Cartan `ε`-sector, reduced on the
frozen background, produces the 4D effective vacuum-energy coefficient**
$$
V(t) \;=\; A + B\,t(1-t), \qquad A,B \ \text{$t$-independent constants,}
$$
**whose unique stationary point is `t = 1/2`** (verified by `sympy`),
and which is **even in `x`** -- so it cannot break the `t=0` vs `t=1`
degeneracy either.

---

## Step (d) -- inspection of the reduced output for a `CS₃`-shaped term

Only now, with steps (a)-(c) fixed, is the output compared to the
target.

**`CS₃(ω_{S³})` does not appear anywhere in the reduced output, and
cannot.** The reason is structural and can be stated in one line
(**corrected same day by skeptic pass** -- the original phrasing, "vol₄
... require[s] the ε", was contradicted by this round's own
`results_c124.json`, which lists degree-4 η-blocks `[A₄,C₄,P₄]` on `M₄`;
any 4-form on `M₄` is proportional to `vol₄` by dimension regardless of
sector):

> A degree-6 `ε₆` on the `S⁶` leg is available **only** inside the full
> `ε₁₃ = ε₄⊗ε₃⊗ε₆`, and `ε₁₃`'s own counting lemma forces `n_T=0`
> (Sector I is exactly torsion-free). Without `ε₁₃`, the `S⁶` leg must
> be built as a degree-6 **η**-invariant, and the block enumeration
> (Sector II) shows none exists. So the odd-in-`x` `S³` leg (needs
> torsion, hence Sector II) and a degree-6 `S⁶` leg (needs `ε₆`, hence
> Sector I) are **mutually exclusive within a single 13D-covariant
> invariant.**

Three specific disposals, each of a route that looks like a rescue:

1. **`CS₃(ω^t)` itself is not a covariant tensor** -- it contains a bare
   `ω`, so it can only enter as a Chern-Simons/transgression term. Those
   do not exist in 13D (Sector III). A "difference of two Chern-Simons
   forms" dies by the identical mod-4 argument, since a transgression
   also needs a closed invariant 14-form.
2. **A 3-form transgression `T₃(ω^t, ω^{LC})` on the `S³` factor alone**
   *is* gauge invariant -- but it requires choosing a reference
   connection on a **hand-identified 3-dimensional factor**. That is
   precisely criterion 2's hand-insertion, made explicit.
3. **`(2t-1)·Vol(S³)·Vol(S⁶)`** -- the shape externally proposed and
   assessed in C120 -- is *rediscovered here bottom-up* as
   `B_3|_{S³} ∧ vol₆|_{S⁶}`, and is now shown to be **not the reduction
   of any 13D-covariant local invariant**: its `S³` leg lives in Sector
   II and its `S⁶` leg (`vol₆ = ε_{abcdef}e^a…e^f`) lives in Sector I.
   This supplies the *structural* reason behind C120's numerical
   finding.

**The closest admissible cousin that does exist** is
`vol₄ ∧ [ε_{ijk}R^{ij}∧e^k] ∧ [ε_{abcdef}R^{ab}R^{cd}R^{ef}]`, a genuine
Lovelock term. Its `S⁶` leg *is* proportional to `χ(S⁶) = 2` by
Chern-Gauss-Bonnet -- i.e. it does reproduce the number
`∫_{S⁶}ch₃(E) = 1` [CITED, G73: `c₃(S⁻) = c₃(T^{1,0}S⁶) = χ(S⁶) = 2`,
`ind = +1`, reused not re-derived, per criterion 3]. But its `S³` leg is
`ε_{ijk}R^{ij}e^k ∝ Scal(∇^t) ∝ t(1-t)`: the **Einstein-Cartan 3-form,
even in `x`**, not `CS₃`.

---

## The six admissibility criteria

| # | Criterion | Verdict | Why |
|---|---|---|---|
| 1 | Admissible under FULL 13D symmetry before any ansatz | **FAIL** | The complete admissible list (7 Lovelock terms + the Mardones-Zanelli `A/B/C/P` products + the AdS-CS combination) contains **no** object with a `CS₃`-type factor. No degree-14 closed invariant ⟹ no 13D CS form at all. |
| 2 | `4+3+6` split not hand-inserted | **FAIL** | Rests on **one** way, not two (skeptic-corrected: the original "way (ii)" -- "the frozen framework takes the product as primitive" -- is circular, since Step (a) itself already grants a *hypothetical* 13D parent to ask the question at all, so citing the frozen framework's own product-primitiveness against that hypothetical proves nothing). The sound way: `ch₃(E_{S⁶})` is not a characteristic class of any 13D field -- `E` is built from `S⁶`'s own `SU(3)`-structure and exists only post-ansatz, so any `ch₃(E)` term must be inserted by hand. This single argument is class-independent, product-independent, and derivative-independent (survives every scope caveat named below), which is why it carries the criterion alone. |
| 3 | Nonzero coefficient on the actual background | N/A (moot) | *Would* be satisfiable for a covariant `S⁶`-side surrogate -- the Lovelock `S⁶` leg gives `χ(S⁶)=2 ≠ 0` -- but for the wrong (even) `S³` leg, and using `χ(S⁶)` here is itself the forbidden bundle-swap this criterion's own text warns against (swapping `ch₃(E_{S⁻})` for `TS⁶`'s Euler density) -- flagged as such, not offered as a partial pass. `B`'s actual numeric coefficient was never computed (`results_c124.json` leaves it symbolic); this line is `[INFERRED]`, not `[VERIFIED]`. |
| 4 | `t`-dependence from the invariant, not spectral data | PASS (moot) | Both sectors' `t`-dependence enters only via `R^t`/`T^t`. No Dirac spectrum, no eigenvalue crossing, was used anywhere in this round. |
| 5 | Gauge/Lorentz variation zero or boundary | PASS-vacuous | Every member of the admissible list is *exactly* Lorentz invariant; the quasi-invariant CS option, which is what criterion 5 was written to accommodate, does not exist in 13D. |
| 6 | Not a relabelled prior candidate | **FAIL for the cousins** | The even cousin reproduces **round111**'s `Scal(t)` exactly; the odd cousin reproduces **C120**'s `(2t-1)Vol·Vol`. The only non-duplicate content this round produces is the no-go itself. |

**Per `claim.md`'s Hard rule, criteria 1 and 2 both failing kills the
branch structurally.** Stated plainly, without rounding up: this is not
"a promising direction requiring further study", not a normalization
issue, and not an ansatz adjustment. The requested object does not exist
in the classified space.

---

## The two mandatory negative controls

Both were run. Both **FAIL**, and -- worth recording -- both fail
*structurally, for every member of the admissible list*, not for one
candidate.

### Control 1 -- permutation / arbitrary-3-subspace: **FAIL**

[VERIFIED, narrowed same day by skeptic pass] Replacing `S³ × S⁶` by
`X³ × Y⁶` for *any* 3-manifold `X³` and 6-manifold `Y⁶` gives the
identical Lovelock reduction `vol₄ ∧ [ε_{ijk}R^{ij}e^k]_{X³} ∧
[Euler₆]_{Y⁶}` for the *specific closest cousin* found in this round.
`S³` is singled out **only** by which factor the ansatz happens to
name -- that cousin is an artifact of the decomposition, exactly as
this control was designed to detect. **Corrected scope:** this is not
a universal statement about every covariant invariant (a term like
`B₃=T_a∧e^a`, if it could be built into a full 13-form, *would* be
sensitive to which 3-factor carries torsion, e.g. it vanishes on flat
`T³`) -- only that the *reachable* candidates in this round's
classification (the ε-sector cousins) cannot distinguish `S³`.

### Control 2 -- untwisted `S⁶`, `ch₃(E) = 0`: **FAIL**

[VERIFIED] Formally trivialising the twist bundle changes **nothing**
in any admissible invariant. The only `S⁶` topological datum a
13D-covariant invariant can see is `S⁶`'s **own** Euler density
(`χ(S⁶) = 2`), which is a property of `TS⁶` and is completely
insensitive to which bundle the Dirac operator is twisted by. The `S⁶`
factor is therefore "along for the ride" in the strongest possible
sense: **no 13D-covariant local invariant of the frozen field content
can see `E` at all.** Any `ch₃(E)` in a reduced action is inserted by
hand, or comes from an independent 13D gauge field the frozen content
does not contain.

---

## Kill Analysis (Anti-Overfitting Gate)

### What this round KILLS

* **The C124 target as pre-registered** -- no 13D-covariant local
  invariant of the frozen field content reduces to
  `CS₃(ω_{S³}) ∧ ch₃(E_{S⁶}) ∧ vol₄`, or to a gauge-invariant
  transgression equivalent. Criteria 1 and 2 both fail. Outcome `(c)`.
* **The whole Chern-Simons / transgression family as a 13D
  parent-action origin story** -- not just this one term. There is no
  13D Lorentz CS form of any kind, for a reason (mod 4) that no choice
  of coupling, normalization, radius, or `t` can move.
* **The entire Lovelock-Cartan class as an OB1 F4 selector**, in one
  shot rather than one candidate at a time: its complete reduced
  contribution to the 4D vacuum energy is `A + B·t(1-t)`, even in `x`,
  stationary only at `t = 1/2` -- the zero-mode-free Levi-Civita value,
  the same wrong answer round80/E14's orbifold route already gave.
* **`(2t-1)·Vol(S³)·Vol(S⁶)` (C120's externally-proposed shape) as a
  13D-covariant reduction** -- shown here to require both sectors at
  once, hence unreachable. C120 killed it on its value; this kills it on
  its origin.

### What this round does NOT kill

* **A parent action with an independent 13D gauge field.** Add a
  fundamental Yang-Mills field and degree-14 invariant polynomials exist
  immediately (e.g. `tr F⁷`, `P₄ ∧ P₄ ∧ ch₃(F)`), so Sector III becomes
  non-empty. That is a **change of frozen field content**, i.e. a
  different F1/F2, and would need its own gate pass -- but it is not
  closed by this round.
* **Non-product backgrounds** -- warping, KK gauge fields turned on in
  the background, or a genuinely fibred (non-product) `M₁₃`. The block
  factorisation that drives the Sector II collapse assumes a strict
  product metric.
* **Higher-derivative invariants** (explicit `D^k R` beyond
  Bianchi-reducible ones) and **fermion-bilinear terms**. Note the
  Sector III kill survives both, since a characteristic class is by
  definition polynomial in curvature; the Sector I parity result does
  not.
* **A torsionful `S⁶`.** The frozen baseline uses Levi-Civita on `S⁶`
  (G73's `Â`-genus / Atiyah-Singer chain). With the nearly-Kähler
  canonical connection instead, `C_{2n+2}`-type blocks could become
  non-zero on the `S⁶` leg -- but degree 6 is still not an available
  block degree, so the `S⁶` leg stays empty; and C119 already found the
  nearly-Kähler route F1-fails for a separate reason.
* `N_gen=3`'s CONDITIONAL status, `lambda = FREE_COUPLING_PARAMETER`,
  `safe_for_runtime = False`, C123's `PARTIAL` verdict, OB1's `PARKED`
  status -- all unaffected, as pre-registered.

### Relaxation Map (one assumption changed per variant, none attempted here)

| Variant | Single assumption changed | Kill criterion |
|---|---|---|
| V1 | Add an independent 13D gauge field to F2 | **Sharpened same day by skeptic pass**: re-running the L1 count with a gauge-field term `F` added still forces `n_T=n_F=0` in the ε-sector -- so V1 CANNOT be rescued through Sector I at all; the only route is a genuine degree-14 characteristic class in Sector III (e.g. `tr F⁷`). Kill criterion: does the added field have independent motivation, or was it added precisely to rescue this (AOG-5)? |
| V2 | Drop the strict-product background (warped / fibred `M₁₃`) | Does the Sector II `S⁶`-leg obstruction survive when `η` is no longer block diagonal? |
| V3 | Allow explicit higher covariant derivatives | Does the `ε`-sector `n_T = 0` lemma survive? (Sector III's mod-4 kill does.) |
| V4 | Accept `t = 1/2` as the answer the Lovelock sector actually gives | Directly contradicts KT-8 (no zero mode at Levi-Civita) -- i.e. this variant is already falsified by the project's own C3, and is listed only so it is not silently re-tried. |
| **V5** | **Drop "polynomial in wedged 2-forms", keep "no extra derivatives"** (mismatched-index curvature-contraction scalars, e.g. `R_{AB}{}^{CD}R_{CD}{}^{AB}`) | **Checked same day by skeptic pass, not by this round -- dies too, for a distinct reason.** In scalar-density language the identical parity split holds (`ε·ε=δ` maps one language's sectors onto the other's); an odd-in-`x` member of this wider class must carry a full `ε₁₃`, whose `S⁶` slots can only be filled by round-`S⁶` curvature components -- which vanish identically against `ε^{abcdef}` (built purely from `δ`'s, forcing a repeated index). Strengthens rather than narrows the verdict; folded into the scope statement, not left as an open variant. |

---

## Proposed pearl (reusable pre-filter, sibling to C119's Künneth filter)

Not written to `pearl_registry/INDEX.md` by this round -- proposed here
for the orchestrator to add, since editing the registry is outside this
round's brief.

* **observation:** on a strict product background, a candidate term
  whose internal legs require BOTH the `ε` sector (any volume form or
  Euler/Pfaffian density) AND the `η`-contracted sector (any factor odd
  in the torsion) cannot be the reduction of a single covariant
  invariant -- the `ε` sector is exactly torsion-free by index/degree
  counting.
* **falsifiable_prediction:** every future OB1 F4 candidate of the shape
  `[odd-in-torsion internal leg] × [volume or characteristic-class leg]`
  fails this filter without any computation.
* **trigger_condition:** any new candidate parent term factorising as a
  product over the frozen factors.
* Companion observation: `ch₃(E_{S⁶})` is invisible to 13D-covariant
  invariants of the frozen content, because `E` is not a 13D field.

---

## What this round does NOT show

1. Does **not** resolve OB1 or move it out of PARKED; no reopen
   condition (`OPEN_BLOCKERS.md`'s 4-item list) is met.
2. Does **not** prove that *no* 13D parent action exists -- only that
   none in the Lovelock-Cartan class, on a strict product background,
   with the frozen (gauge-field-free) content, yields the target term.
3. Does **not** touch C123's `PARTIAL` verdict, its Yang-Mills stability
   finding, or its `CS₃`-vs-`η(D^t)` non-collapse result -- all cited,
   none re-derived, none re-litigated.
4. Does **not** attempt F6 (fluctuation-operator stability), which
   `claim.md` explicitly scoped out of C124.
5. Does **not** re-derive `c₃(S⁻) = 2` / `∫ch₃ = 1`; reused from G73 by
   citation exactly as criterion 3 instructs.
6. Does **not** change `N_gen=3`, `lambda`, or `safe_for_runtime`.
7. Does **not** solicit Tom Lawrence.

---

## Verification

**FL Step 8a skeptic pass run and CONFIRMED same day** (context-blind,
`Agent(skeptic, model=opus)`, artifact-only). Independently re-derived
L1 (found provably stronger: no η-contractions at all inside the
ε-sector, and a gauge field doesn't rescue Sector I either), L2 (block
table reproduced from scratch without citing Zanelli), and checked a
missed class (V5) that also dies. Found and repaired two real errors in
the prose (`so(1,12)` "odd rank" claim; "no closed 14-form exists"
claim) -- neither load-bearing, both fixed in place above. Full detail
in the correction block near the top of this file.

**Tool-checked in this session (own derivation, script
`c124_invariant_enumeration.py`, output `results_c124.json`,
`ruff check` clean -- skeptic-downgraded tier: the script restates the
hand-derived `deg_extra=0`/`13%2==0` facts rather than independently
deriving them, so these are `[VERIFIED -- hand derivation, script is a
restatement]`, not full independent computational verification):**
* `ε`-sector enumeration -> exactly 7 terms, all `n_T = 0` (re-derived
  independently by skeptic in a stronger form, see correction block).
* non-`ε` parity lemma -> all 12 solutions have odd `n_T` (re-derived
  independently by skeptic from scratch, matches Zanelli without citing
  it).
* block-degree table -> degrees 6 and 10 absent; `S⁶` leg provably
  empty (skeptic-confirmed).
* degree-14 Chern-Weil-ring generator unreachable from `{4,8,12}`;
  `14 mod 4 = 2`; `so(13)`'s odd-dimensional (13) defining
  representation admits no Pfaffian/Euler generator (corrected --
  the *rank* of `so(13)` is 6, even; parity of the representation
  dimension is the operative criterion, not rank); `D=13` is not
  `4k-1`.
* symbolic `su(2)`: `T^t` linear/odd in `x`; `R^t = t(t-1)R_0` on all 12
  non-vanishing components; `Scal = 6 - 24x²`, even (independently
  hand-verified by skeptic, matches round111 exactly).
* `V(t) = A + B t(1-t)`, unique stationary point `t = 1/2`, even in `x`.

**Independent cross-check against the project's own prior work
(reproduced, not cited):** `Scal(∇^t)` matches round111's
`Scal_LC - 6(2t-1)²` exactly.

**[CITED] literature (retrieved and read this session via the arXiv
tool, not quoted from memory):**
* J. Zanelli, *Lecture notes on Chern-Simons (super-)gravities*, 2nd ed.,
  arXiv:hep-th/0502193 -- §4.1 eqs. (49)-(50) Lovelock series; §4.2
  eqs. (65)-(68) the `A/B/C/P` torsional classification; §4.3 eqs.
  (70)-(73) and Table 1, `C₃^{Lor} = ω dω + ⅔ω³` with `dC₃^{Lor} = P₄`,
  and `C₃^{Tor} = e^aT_a` with `dC₃^{Tor} = N₄`; §5.2 eqs. (107)-(109)
  the AdS CS gravity Lagrangian as a *fixed-coefficient Lovelock
  combination*; §5.4 eq. (113) "exotic" gravity as the AdS-Pontryagin
  transgression; §4.4 footnote, torsional term count growing as
  partitions of `D/4`.
* A. Mardones & J. Zanelli, *Lovelock-Cartan theory of gravity*,
  Class. Quantum Grav. **8** (1991) 1545 -- the primary source for the
  torsional classification, cited **at second hand** through Zanelli's
  ref. [41]; the 1991 paper predates arXiv and was **not** read
  directly. Marked accordingly, not as `[VERIFIED]`.
* H. T. Nieh & M. L. Yan (1982), the Nieh-Yan invariant -- likewise
  second-hand through Zanelli eq. (64)/[39], not read directly.

**[CITED] project facts reused, not re-derived:** `c₃(S⁻) = 2`,
`ind = +1` (G73 `decision.md`, 29/29 tests); F1/F2/F3/F5 frozen content
(`PARENT_ACTION_GATE.md`); C123's already-tried list and its
`P₄ = vol₄` correction; C120's `(2t-1)Vol·Vol` assessment; C119's
Künneth pre-filter and `S⁶` nearly-Kähler facts; round111's `Scal(t)`;
`SPIN13_TO_SPIN4_DECOMPOSITION.md`'s "no established `Spin(1,12)`"
statement.

**[UNKNOWN] / not checked:**
* Whether the Mardones-Zanelli `A/B/C/P` list is *provably exhaustive*
  in the primary source (the independent graph-decomposition derivation
  above argues it is, and it matches Zanelli's published list term for
  term, but the 1991 completeness proof was not read).
* Everything in the "What this round does NOT kill" list.

**Run same day, after this round completed:** FL Step 8a skeptic pass,
context-blind (`Agent(skeptic, model=opus)`, artifact-only, no session
history). Verdict: CONFIRMED, with two real prose errors found and
repaired (neither load-bearing) and the missed V5 class checked and
found to also die. Full detail in the correction block near the top of
this file. The one item the skeptic flagged as still `[UNKNOWN]` --
completeness of the closed-invariant-ring generator list at degrees 10
and 14 -- remains the single highest-value follow-up if this result is
ever pushed further, per the named cheap check in that same block.

**No pytest suite touched** (no shared code modified); the one new
script is self-contained inside this experiment folder.
