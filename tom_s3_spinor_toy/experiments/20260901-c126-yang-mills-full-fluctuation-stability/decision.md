# C126 decision -- the full fluctuation operator of `S_YM` at `t=0,1`.
#
# RESULT STATEMENT, scope-qualified in the first line per this project's
# own house discipline, and REVISED after the FL Step 8a skeptic pass
# (which returned WEAKENED; see the response matrix below -- the
# mathematics was independently reproduced and confirmed, the FRAMING was
# corrected on five counts, and one printed sentence was simply false):
#
# The second variation of `S_YM[∇] = ∫_{S³}|R^∇|² dvol` at the flat
# Cartan-Schouten connections `∇^0` and `∇^1`, for a general METRIC
# (`𝔰𝔬(3)`-valued) 1-form perturbation `δω ∈ Ω¹(S³,𝔰𝔲(2))` at FIXED
# metric -- the full fluctuation space in that class, not the
# 1-parameter-family direction -- is POSITIVE SEMI-DEFINITE, with kernel
# exactly the tangent space of the metric gauge orbit (`H¹_{d_A} = 0`).
# So `t=0,1` are genuine local minima within that class; they are in fact
# GLOBAL minima (`S_YM=0`, the absolute floor of a non-negative
# functional). The pre-registered kill criterion is NOT met.
#
# BUT -- and this is the round's honest headline, not a caveat --
# **THE PRE-REGISTERED KILL CRITERION COULD NOT HAVE FIRED.** `S_YM ≥ 0`
# and `S_YM[∇^{0,1}] = 0`, so a negative eigenvalue there is impossible
# by construction. Positivity and `H¹=0` are THEOREMS available before
# any code ran, not findings. `claim.md` pre-registered an unfalsifiable
# criterion; recording that defect is worth more than the "CONFIRMED" it
# would otherwise have produced.
#
# The genuinely new content, promoted here because the skeptic correctly
# objected that the original label buried it:
#   (N1) the EXHAUSTIVE homogeneous critical set: exactly 9 points on the
#        diagonal slice (5 flat + 4 saddles), classified in closed form
#        and independently reproduced by hand in the skeptic pass;
#   (N2) the Morse index at Levi-Civita is EXACTLY 1, stable from
#        `2j≤8` to `2j≤14`, with an analytic `H ≥ -1/2` bound valid at
#        every `j`; the unique unstable direction IS the family direction;
#   (N3) `∇^0` and `∇^1` are separated by a LARGE gauge transformation of
#        winding number `n = -1` (computed exactly two independent ways),
#        which makes the `t=1/2` barrier TOPOLOGICALLY FORCED rather than
#        an artifact of the chosen path -- a strengthening of C123's
#        barrier reading, not a demotion of it.
#
# And the round still WEAKENS Yang-Mills as an OB1 F4/F6 candidate:
#   (1) the stability is AUTOMATIC, hence carries no selection
#       information whatever;
#   (2) `∇^0` and `∇^1` are ONE point of `𝒜/𝒢` (full gauge group), so
#       every `𝒢`-invariant functional of `ω` alone -- `S_YM` and every
#       curvature-norm invariant -- gives them the same value. **They are
#       NOT the same point of `𝒜/𝒢₀`** (identity component): there they
#       are distinct winding sectors, and a Chern-Simons functional DOES
#       distinguish them. Both halves must be stated; the first alone is
#       a tautology dressed as a physical exclusion, and the second alone
#       would contradict C123's own `CS(0) ≠ CS(1)`;
#   (3) the homogeneous vacuum set is `{0} ⊔ SO(3)`, a point plus a
#       3-manifold, not the two points `{t=0,t=1}` -- `S_YM`'s minimum is
#       MORE degenerate than the family reveals, making selection
#       strictly harder for `S_YM`, not easier.
#
# NOT covered by this round: the affine-connection question (as affine
# connections on `TS³` the two are NOT equivalent -- their torsions have
# opposite sign, `T^t=(2t-1)[X,Y]`, and relating those still requires the
# orientation-reversing `ι` of C37-C39/OB13); the full 13D configuration
# (vielbein + twist bundle + fermions), which is C125's question, not
# this one; **variation of the metric `g` itself, which is never done
# anywhere in this round**; the parent-action origin of `S_YM` (F4/F6's
# actual blocker, unchanged); Lorentzian signature (the positivity
# argument is Riemannian and says so); the LEAST barrier over all paths
# (the true sphaleron energy), which is a variational problem not
# attempted.

**Verdict (2026-09-01; label revised 2026-09-02 after the FL Step 8a
skeptic pass, per that pass's finding E3):**
`WEAKENED_BY_FL_STEP_8A__MATH_CONFIRMED_FRAMING_CORRECTED__PSD_AND_H1_ZERO_AT_T0_T1_ARE_FORCED_THEOREMS_NOT_FINDINGS_AND_THE_PRE_REGISTERED_KILL_CRITERION_WAS_UNFALSIFIABLE_BY_CONSTRUCTION__SCOPE_IS_METRIC_SO3_PERTURBATIONS_AT_FIXED_METRIC_GL3_ADDS_NULL_DIRECTIONS_AND_THE_METRIC_ITSELF_WAS_NEVER_VARIED__NEW_CONTENT_IS_EXHAUSTIVE_HOMOGENEOUS_CRITICAL_SET_9_POINTS_PLUS_MORSE_INDEX_EXACTLY_1_AT_T_HALF_STABLE_TO_2J14_PLUS_WINDING_MINUS_1__T0_T1_ARE_ONE_POINT_OF_A_MOD_G_BUT_DISTINCT_IN_A_MOD_G0_SO_THE_BARRIER_IS_TOPOLOGICALLY_FORCED_AND_CHERN_SIMONS_DOES_DISTINGUISH_THEM__YANG_MILLS_WEAKENED_NOT_PROMOTED_AT_F4_AND_F6`

**Status:** OB1 stays PARKED. No reopen condition met (per
`OPEN_BLOCKERS.md`'s own 4-item list). C123's Claim 1 stays `PARTIAL`;
this round supplies the F6 content C123 named and C124 explicitly scoped
out, and the F6 answer turns out to be uninformative for selection.

**Completeness:** `PARTIAL` in exactly four named respects.
1. The positivity result is **complete and exact** for metric
   (`𝔰𝔬(3)`-valued) perturbations -- Step 3's argument is cutoff-free and
   the numerics only confirm it. Step 8 shows positivity also survives on
   `𝔤𝔩(3)`.
2. The **kernel** result (`H¹=0`, "no extra zero modes") is complete
   **only within metric connections**; on `𝔤𝔩(3)` the kernel is strictly
   larger (Step 8). The metric `g` itself is never varied at all.
3. The **homogeneous** critical-point classification is complete up to the
   verified `SO(3)×SO(3)` symmetry. The **inhomogeneous** critical set of
   `S_YM` on `S³` was **not** classified -- named, not attempted, and not
   needed for the pre-registered question.
4. The `t=1/2` Morse index is `1` at `2j≤14` **and** bounded below by an
   analytic argument valid at every `j` (Step 5b) -- but the *number* of
   modes at the saturating depth is established numerically, not proved.
   Whether `3/16` is the LEAST barrier over all paths (the sphaleron
   energy) is `[UNKNOWN]`, named in Step 9.

**Gate fields assessed:** `PARENT_ACTION_GATE.md` **F6** (stability /
equations of motion) -- the field C123's Relaxation Map priority 3 named
and C124 explicitly declined. F4 is **not re-litigated** (status
unchanged: duplicate of round99) but the round produces a new, stronger
structural reason for the F4 failure, recorded below. F1, F2, F3, F5, F7
not assessed.

---

## ⚠️ FL Step 8a skeptic pass -- RUN, verdict **WEAKENED**, all 9 findings answered

`Agent(skeptic, model=opus)`, context-blind (claim.md + script + log +
results JSON only; no session history, no reasoning chain, no confidence
statements), 26 minutes, 2026-09-01→02.

**Substrate note, recorded per the Substrate Gate:** the skeptic's `Write`
was denied by this repo's own agent-tool-scope guard and it had no `Bash`,
so **every check it ran was an analytic hand-derivation**, not
tool-executed. Per the gate this is a fact about its substrate, not
evidence about the claim -- and hand-derivation was sufficient for every
algebraic question posed. It is also, unusually, a *strength* here: its
confirmations are genuinely independent of this round's code rather than
re-runs of it.

**What it independently reproduced and CONFIRMED (T1-T10):** the frame
formulas for `F` and `d_A` including the `−ε_{ijk}a_k` coframe term,
derived from scratch; `A^t_i{}^b = tδ_i^b` with no transpose ambiguity;
the closed-form `F`-term and its matrix wiring; the linear term
`L_k^c = 4t(t−1)(t−½)δ_kc` **to the digit**; the entire `2j=0` spectrum
at `t=1` (`{0,0,0,1,4,4,4,4,4}`) **by hand, matching the JSON exactly**;
the `F`-term sign via `Q=−3/2` at `t=½`; `d_A∘d_A=0` at `t=1`; `A^1 =
G^{-1}dG`; the Peter-Weyl normalisation (explicitly: signs and
eigenvalues are right within *and across* blocks); and -- reproducing
PART 7b by an independent algebraic route -- **exactly 9 real
homogeneous critical points, 5 flat + 4 saddles**. It also derived the
winding number independently: `tr(T_iT_jT_k) = −¼ε_{ijk}`, `tr(ω³) =
−(3/2)vol`, `K=1/4 ⟹ R=2 ⟹ Vol=16π²`, `n = −1` -- **identical to PART
6b's sympy result, obtained a different way.**

**Response matrix (per `falsification-ladder.md` Step 8a). Every finding
is answered; nothing is waved through.**

| # | Finding | Response |
|---|---|---|
| **E1** | Claim (B)'s "consequently no gauge-invariant functional can EVER distinguish them" is **false** (CS does, and CS is small-gauge-invariant) **or vacuous** (if "gauge-invariant" means `𝒢`-invariant, it just restates "same orbit"). `G=Ad` is LARGE, winding `∓1`. | **Accepted and FIXED, and the round is strengthened by it.** The skeptic read a version of the artifact that predated PART 6b; the winding computation it demanded was added independently before its report arrived, and **the two derivations agree exactly** (`n=−1`). But its *framing* objection is sound and was only half-addressed: the `𝒢` vs `𝒢₀` distinction is now stated explicitly in both directions, and the tautology is named as a tautology whose content is the *classification* of which functionals sit in which class. **Its point 3 is adopted outright as new content (PART 9):** since CS is an integer-valued continuous function on the flat set, `A^0` and `A^1` lie in different components of it, so any path between them must leave the flat set -- **the `t=1/2` barrier is topologically FORCED**, not an artifact of the path. C123's barrier reading is thereby strengthened, not narrowed. |
| **E2** | The metric-connection (`𝔰𝔬(3)`) assumption is never named; on `𝔤𝔩(3)` there are 6 extra null directions per `Ω⁰` mode, so "no extra zero modes" fails. | **Accepted; verified rather than conceded (new PART 8).** Built the `𝔤𝔩(3)` operator explicitly: positivity **survives** (it only ever used "sum of squares, zero at a flat connection"); `ker = rank(d_A on Ω⁰(𝔤𝔩₃))` still holds (`H¹=0` too); and the kernel is **strictly larger** (e.g. `18` vs `6` at `2j=1,t=0`; `8` vs `3` at `2j=0,t=1` -- `8` not `9` because the `𝔤𝔩(3)` centre is covariantly constant). Correct scope now stated everywhere: **kernel = the METRIC gauge orbit, within metric connections**. Its further point that **the metric `g` itself is never varied** is accepted and added to the scope list. |
| **E3** | The pre-registered kill criterion cannot fire (`S_YM≥0`, `=0` there); the verdict label headlines theorems as findings. | **Accepted; this is the single most valuable finding and the verdict LABEL was rewritten because of it.** The body already said the result was forced (PART 3, PART 4b, "as it must be for a flat connection"), but the label did not. New label states the pre-registration defect outright and promotes N1/N2/N3 instead. |
| **E4** | PART 5's "the full min-eig curve tracks it exactly" is **contradicted by its own table** (`t=0.1`: min eig `−0.106` vs family `+0.46`). | **Accepted -- a real false sentence, mine. FIXED in place**, with the contradiction quoted in the script's own output rather than silently deleted. Correct statement: the minimum is dominated by near-gauge modes away from the critical points and coincides with the family direction only at `t=½`, where gauge modes are exact zeros. |
| **E5** | "kernel = gauge orbit" rests on a dimension count; `d_A∘d_A=0` -- the identity linking the two independently built matrices -- is never checked, and a sign error in `build_dA_0form` would still pass the count. | **Accepted; FIXED (new PART 4f)**, with its own negative control since `d_A∘d_A = [F,·]`: `‖d_A∘d_A‖ = 8.5e-15` at `t=0,1` and `1.837` at `t=½`. The check can now fail, which is the point. |
| **E6** | The positive control is partly circular -- `E(t)` in PART 1 is built with the same `F_sym` as the Hessian, so a shared systematic error cancels. | **Accepted, already mitigated before the report arrived.** PART 4c (added independently) is a genuinely external anchor: the `t=0` spectrum matches the closed-form `S³` coexact-1-form Hodge spectrum in **eigenvalue AND integer multiplicity for `k=1..7`** -- multiplicities cannot be rescued by any normalisation error. PART 4d (component-level rebuild on generic input) and PART 4e (agreement with C85's certified module) close the rest. |
| **E7** | The `t=½` Morse index was computed only at `2j≤8`; the robustness sweep ran only at `t=0,1`, i.e. exactly where it was unnecessary. Its reasoning (at a critical point the gauge directions are exact zeros and `D^†D` is `O(1)` on them, so "large `j` is safe" does not follow from `j²` growth) is sound. | **Accepted; FIXED (new PART 5b).** Re-run at `2j≤14`: index **unchanged at exactly 1**, single eigenvalue `−0.5`, zero negative modes in every block `2j≥1`. Added an analytic backstop valid at **every** `j`: the `F`-term is `(t²−t)` times a form with spectrum `{+2,+1,−1}` tensored with the identity on the mode index, so `H ≥ min(F-term) = −½` for all `j` at once; the observed minimum saturates it. |
| **E8** | "no NEW vacua **in any sense**" is false -- `{0}` and `SO(3)` are different components in different winding sectors; the full flat set is the `θ`-vacuum ladder. | **Accepted -- and the original sentence was self-undermining, since the winding label is exactly what CS uses. FIXED**: the statement is now scoped to `S_YM` ("no new vacuum that `S_YM` ITSELF could use"), with the topological sense stated explicitly alongside it. |
| **E9** | PART 0 calls `T_a=−Z_a/2` "a rescaled radius"; it is a rescaling **composed with an orientation flip** (`X_i→−X_i`, `det=−1`), unflagged in a repo that uses orientation elsewhere. | **Accepted; NAMED in place.** Nothing load-bearing depends on it (`S_YM` is orientation-even; only the *sign* of `n` is convention-dependent, `|n|=1` is not), but the flag is now in the script's own PART 0 output, together with the warning not to reuse the bridge in an orientation-sensitive round without fixing round99's frame handedness -- which round99 never fixes, since it works with matrices and no frame. |

**Nothing dismissed. No finding overturned the core result** -- the
skeptic's own verdict is that (A) is *"true but trivial and narrower than
stated"*, which is precisely what the revised label now says.

**Carried forward from the skeptic's own recommendation 6, as a second
pearl** (see the Proposed pearl section): *"`t=0` and `t=1` are separated
by a `ℤ`-valued small-gauge winding label; the `S_YM` barrier `3/16` is
its sphaleron"* -- with the falsifiable prediction that any functional
built from `CS` or from the winding of the interpolating path **does**
distinguish them.

---

## The result, in one paragraph

Write `∇ = ∇^{t} + δω` with `δω ∈ Ω¹(S³,𝔰𝔲(2))` arbitrary. Yang-Mills is
quartic, so the expansion terminates exactly:
`F(A+a) = F(A) + d_A a + [a,a]`, hence
```
S_YM[A+a] = S_YM[A] + 2∫⟨F_A, d_A a⟩
                    + ∫( |d_A a|² + 2⟨F_A,[a,a]⟩ )   +  O(a³).
```
At `t=0` and `t=1` the connection is FLAT (`F^t = (t²-t)·const`), so the
linear term vanishes -- these are genuine critical points with respect to
the full space, not merely along the family -- and the quadratic form
collapses to `Q[a] = ∫|d_A a|² = ⟨a, d_A^† d_A a⟩ ≥ 0`, manifestly
positive semi-definite, with kernel `ker d_A|_{Ω¹}`. Computing that
kernel explicitly in Peter-Weyl modes gives `dim ker Q = rank(d_A:
Ω⁰→Ω¹)` in **every** block up to `2j = 14`, i.e. the kernel is exactly
the *metric* gauge-orbit tangent space and `H¹_{d_A}(S³,𝔰𝔲(2)) = 0` -- as
it must be for a flat connection on a simply-connected manifold.
**Modulo gauge the Hessian is strictly positive definite, with spectral
gap `1` in the units below.**

Both the positivity and the `H¹=0` are **forced** -- neither could have
come out otherwise, which is exactly why the pre-registered kill
criterion could not fire (see the header and the skeptic block). The
scope qualifier "metric" is load-bearing: Step 8 shows `𝔤𝔩(3)`
perturbations keep the positivity but strictly enlarge the kernel.

---

## Step 0 -- convention bridge (done first, not assumed)

[VERIFIED, `run_c126.log` PART 0] round99's generators `Z_a = i σ_a` obey
`[Z_1,Z_2] = -2Z_3` (`c₀ = -2`), reproduced verbatim here. This round
uses `T_a := -Z_a/2`, which obeys `[T_i,T_j] = ε_{ijk}T_k` (`c₀ = +1`) --
the same Lie algebra in a rescaled basis, i.e. a rescaled `S³` radius.
Both facts are checked symbolically, not asserted.

[VERIFIED, PART 6b] In this normalisation the sectional curvature of the
Levi-Civita member is `K = 1/4`, so `R_{S³} = 2` and `Vol = 16π²` -- both
derived from the connection family itself, needed only for the winding
number in Step 6b.

[VERIFIED, PART 1b, 200 random curvature tensors] The two possible
readings of `|R^∇|²` -- the affine one `R_{ijkl}R^{ijkl}` and the
Yang-Mills one `Σ_{i<j,b}(F_{ij}^b)²` -- differ by the **constant factor
4** for a metric connection (`R_{ijkl} = ε_{ijb}F_{kl}^b`). A positive
constant moves no critical point and flips no sign, so every statement
below holds in both readings. This is the identical
"positive-constant-cannot-move-a-stationary-point" step C123 used to
identify `S_YM` with round99's `V(t)`.

## Step 1 -- the expansion is EXACT, not a truncation

[VERIFIED, PART 1, sympy, all 9 `(i<j,b)` components]
`F(A+a)_{ij}^b = F(A)_{ij}^b + (d_A a)_{ij}^b + [a_i,a_j]^b` identically,
with the frame formulas
```
F_{ij}^b     = X_i A_j^b − X_j A_i^b − ε_{ijk}A_k^b + ε_{bcd}A_i^c A_j^d
(d_A a)_{ij}^b = X_i a_j^b − X_j a_i^b − ε_{ijk}a_k^b
                 + ε_{bcd}(A_i^c a_j^d − A_j^c a_i^d)
```
The `−ε_{ijk}(·)_k` term is the coframe's non-closedness
(`de^k = −½ε_{ijk}e^i∧e^j`), not a typo; it is what makes `A^0 = 0`
have `F = 0` while `A^{t}` for `t≠0,1` does not.

[VERIFIED, PART 1] For the family `A^t(X_i)^b = t δ_i^b` this gives
`F^t_{ij}{}^b = (t²−t)ε_{bij}` and
`S_YM(t)/Vol = 3t²(t−1)²`, i.e. **C123's `E(t)=C t²(1−t)²` with `C = 3`
in these units**, `E''(0) = E''(1) = 6 = 2C`, `E''(1/2) = −3 = −C`. The
apparatus reproduces the prior round's numbers before being used for
anything new.

## Step 2 -- `t=0` and `t=1` are critical points of the FULL functional

[VERIFIED, PART 2, symbolic] The linear term's coefficient against an
arbitrary perturbation is
```
L_k{}^c(t) = 4 t (t−1) (t − ½) · δ_k^c ,
```
identically zero exactly at `t ∈ {0, ½, 1}`. (The derivative terms drop
out because `F^t` is constant and `∫_{S³} X_i f = 0`.) So the three
stationary points round99 found **within the family** are stationary
points of `S_YM` on the **whole** space of connections -- a fact the 1D
slice could not establish and did not claim.

## Step 3 -- the structural argument (cutoff-free)

`S_YM[A] = ∫Σ_{i<j,b}(F_{ij}^b)²` is a sum of squares, because the metric
on `S³` is Riemannian (positive definite). It is therefore `≥ 0`, with
equality iff `F = 0`. `F^0 = F^1 = 0`, so **`A^0` and `A^1` attain the
absolute minimum**. A zero of a non-negative functional is automatically a
global minimum; its second variation cannot have a negative direction.
Explicitly, with `F_A = 0` the exact expansion of Step 1 gives
```
S_YM[A + a]  =  ∫ Σ_{i<j} | (d_A a)_{ij} + [a_i,a_j] |²  (exactly),
Q[a] := ½ δ²S_YM[a,a]  =  ∫ Σ_{i<j} |(d_A a)_{ij}|²   ≥ 0 ,
```
so the Hessian is `2 d_A^† d_A`, positive semi-definite by construction.

**This is not a subtle result and the write-up does not pretend it is.**
It is the standard fact that flat connections are absolute minima of
Yang-Mills. Its value here is that the pre-registered question is
answered definitively and for a reason that no refinement of the
computation can overturn -- and, more importantly, that it makes the
consequences in Steps 6-7 unavoidable rather than optional.

**Load-bearing assumption, named:** Riemannian signature. In Lorentzian
signature `|F|²` is not a sum of squares and the argument fails. On `S³`
it does not.

**Scope, named (sharpened after skeptic finding E2, and now VERIFIED
rather than inferred -- see Step 8):** the perturbation space is
`Ω¹(S³,𝔰𝔬(3)) ≅ Ω¹(S³,𝔰𝔲(2))`, i.e. **metric** connections at fixed
metric -- which is what claim.md asks for ("a general `𝔰𝔲(2)`-valued
1-form") and what the Cartan-Schouten family lives in. A general affine
connection on `TS³` has 27 frame components, not 9. Step 8 builds the
`𝔤𝔩(3)` operator explicitly and finds: **positivity survives, the
kernel statement does not survive verbatim** -- so the correct wording
throughout is "kernel = the METRIC gauge orbit, within metric
connections", not "no extra zero modes" full stop.

**A second scope item, named because it was silently absent:** the
metric `g` itself is **never varied anywhere in this round**. A
stability statement about the *geometry* would need `δg`; the
connection/metric split is exactly what `S_YM` cannot see.

## Step 4 -- the kernel, computed explicitly in Peter-Weyl modes

[VERIFIED, PART 4] `L²(SU(2)) = ⊕_j V_j ⊗ V_j^*`; a left-invariant field
`X_k` acts on the right index by `ρ_j(T_k) = -i J_k^{(j)}` (checked
anti-hermitian and bracket-correct for `2j = 0..8`), the left index being
a spectator of multiplicity `2j+1`. The operator is block diagonal in
`j`; each block acts on `ℂ³_{frame} ⊗ ℂ³_{internal} ⊗ ℂ^{2j+1}`.

```
 2j   dim |  t=0: min eig  ker dim  rk d_A |  t=1: min eig  ker dim  rk d_A
  0     9 |   1.000000000        0       0 |  -0.000000000        3       3
  1    18 |  -0.000000000        6       6 |  -0.000000000        6       6
  2    27 |  -0.000000000        9       9 |  -0.000000000        8       8
  3    36 |  -0.000000000       12      12 |  -0.000000000       12      12
  4    45 |  -0.000000000       15      15 |  -0.000000000       15      15
  5    54 |  -0.000000000       18      18 |  -0.000000000       18      18
  6    63 |  -0.000000000       21      21 |  -0.000000000       21      21
  7    72 |  -0.000000000       24      24 |  -0.000000000       24      24
  8    81 |  -0.000000000       27      27 |  -0.000000000       27      27
```
* **all blocks PSD** at both `t=0` and `t=1`;
* **`dim ker Q = rank(d_A: Ω⁰→Ω¹)` in every block** -- the kernel is
  exactly the *metric* gauge-orbit tangent space, `H¹_{d_A} = 0`, no
  extra flat direction **within metric connections** (Step 8 shows the
  qualifier is load-bearing);
* **spectral gap (lowest nonzero eigenvalue) = 1.000000000** at both,
  i.e. modulo gauge the Hessian is strictly positive definite and
  uniformly so.

Two internal consistency signals worth recording, because they are the
kind of thing a mis-built operator gets wrong:
* at `t=0`, `2j=0`: `rk d_A = 0` -- constants are covariantly constant at
  the trivial connection, so the `j=0` block contributes no gauge
  direction, and correspondingly `ker Q = 0` there with `min eig = 1`;
* at `t=1` those three covariantly-constant adjoint sections have MOVED
  to the `2j=2` block (`rk d_A = 8` out of 9, i.e. one per multiplicity
  copy, `×3 = 3`). This is direct evidence that the gauge transformation
  relating the two mixes Peter-Weyl blocks, which Step 6 needs.

[VERIFIED, PART 4b] Pushing the cutoff to `2j = 14`: global minimum
eigenvalue `-0.000000000000` and `ker = gauge` in every block, at both
`t=0` and `t=1`. **The truncation is not load-bearing here** -- Step 3's
argument is cutoff-free and the numerics merely agree with it. What the
numerics *do* establish independently is the KERNEL statement
(`H¹_{d_A}=0`) and the spectral gap, which Step 3 does not give.

**Skeptic finding E7, accepted and fixed:** this robustness sweep
originally ran *only* at `t=0,1` -- exactly the two points where the
answer is already a theorem -- and *not* at `t=1/2`, the one point where
a truncation could actually bite. See Step 5b.

[VERIFIED, PART 4f, added after skeptic finding E5] The "kernel = gauge
orbit" conclusion needs `im d_A ⊆ ker d_A`, i.e. `d_A∘d_A = 0`, which
originally went unchecked -- and a dimension count alone would survive a
sign error in `build_dA_0form`. Now checked at the operator level, with
its own negative control (since `d_A∘d_A = [F,·]` it must vanish exactly
where `F` does):
```
 t=0     max_j ||d_A o d_A|| = 8.5e-15      (expected ZERO)     ok
 t=1/2   max_j ||d_A o d_A|| = 1.837        (expected NONZERO)  ok
 t=1     max_j ||d_A o d_A|| = 8.5e-15      (expected ZERO)     ok
```

## Step 5 -- controls

**Positive control** [VERIFIED, PART 4]: feeding the general operator the
1-parameter-family direction `a = ∂_t A^t` (`a_i^b = δ_i^b`) must
reproduce C123's already-known `½E''(t) = 3(6t²−6t+1)`. It does, exactly,
at `t = 0, 0.25, 0.5, 0.75, 1, 1.7` (`match = True` at every point;
`+3` at `t=0,1`, `−1.5` at `t=1/2`). The known answer is recovered before
any new answer is reported.

**Implementation control** [VERIFIED, PART 4d]: the assembled matrices are
checked against a direct, index-by-index rebuild of the component formula
they claim to implement, on GENERIC input rather than on the one control
vector. The closed-form `F`-term
`2Σ_{i<j}⟨F_{ij},[a_i,a_j]⟩ = (t²−t)[(tr a)² − tr(a a)]` matches a direct
component sum to `1.4e-14` over 500 random `(a,t)` pairs; the full
quadratic form `Q` on a nontrivial Peter-Weyl block (`2j=3`, derivatives
included) matches a term-by-term rebuild to `2.3e-13` over 50 random
`(a,t)`. This closes the gap that the positive control alone leaves --
one vector cannot validate a 9×9 form.

**External control** [VERIFIED, PART 4c] -- the strongest check available,
and the one that tests the Peter-Weyl normalisation rather than assuming
it. At `t=0` the operator IS `d^†d` on `Ω¹(S³,𝔰𝔲(2))`, whose nonzero
spectrum is the Hodge Laplacian spectrum on **coexact** 1-forms of the
round `S³`, a closed-form standard result. With `R=2` fixed independently
by PART 6b's `K=1/4` (no free parameter), the prediction is
`λ_k = (k+1)²/R² = (k+1)²/4` with multiplicity `2k(k+2)`, `×3` for the
internal index. Computed against predicted, `k = 1..7`:
```
   k  predicted lambda  computed lambda  pred mult  computed mult  match
   1          1.000000         1.000000         18             18   True
   2          2.250000         2.250000         48             48   True
   3          4.000000         4.000000         90             90   True
   4          6.250000         6.250000        144            144   True
   5          9.000000         9.000000        210            210   True
   6         12.250000        12.250000        288            288   True
   7         16.000000        16.000000        378            378   True
```
**All 7 levels match in eigenvalue AND multiplicity.** Multiplicities are
integers and cannot be rescued by a normalisation error: a wrong `L²`
inner product, a wrong coframe term `−ε_{ijk}a_k`, or a wrong action of
`X_i` on the Peter-Weyl index would all break them. [CITED] the coexact
1-form spectrum of the round `S³` is standard spectral geometry, used
here as an external prediction and not re-derived in this project.

**Reuse check** [VERIFIED, PART 4e] -- claim.md asked to reuse this
project's certified Peter-Weyl apparatus rather than rebuild. **Honest
position: the fluctuation operator had to be built.** C85's module builds
`D̄_k`, a Dirac-type operator (quaternion right-multiplication ⊗ `su(2)`
L-matrices), and C107 already established `D̄_k` is **not** the same object
as the torsion family `D^t`; it contains no 1-form/2-form complex, no
`d_A`, no Yang-Mills `F`-term. What *is* shared is the `su(2)`
representation, so that piece is **cross-checked against the certified
module** instead of merely re-derived: for `k = 2j = 0..6`, C85's
`build_l_matrices(k,"repaired")` passes its own bracket and Casimir
certifications, this round's `ρ_j(T_i)` has Casimir `−j(j+1)`, the
rescaled Casimirs agree exactly (`l_i = 2ρ_i` up to similarity, since
C85 uses `[l_1,l_2]=2l_3` and this round uses `[ρ_i,ρ_j]=ε_{ijk}ρ_k`),
and the diagonal generator's spectra agree. All `True`, `k=0..6`.

**Negative control** [VERIFIED, PART 5]: the operator must find the
instability C123 already knows about at `t=1/2`, or it is not measuring
anything. Morse index (negative eigenvalues, with multiplicity) at the
three critical points:
```
 t=0    : 0
 t=1/2  : 1     (the single eigenvalue -0.5)
 t=1    : 0
```
and the unstable eigenvector's overlap with the family direction is
`1.000000000000`. **New content beyond C123:** the Levi-Civita saddle has
Morse index **exactly 1** modulo gauge, and its unique unstable direction
IS the Cartan-Schouten family direction -- the full operator neither adds
nor removes unstable directions there. C123's barrier-top reading is
confirmed and sharpened, not just repeated.

**Counting caveat, stated because it is easy to misread:** away from
`t ∈ {0,½,1}` the gradient is nonzero, so counting negative eigenvalues is
not a Morse index of anything -- the gauge directions then acquire
nonzero eigenvalues of either sign, since
`δ²S[d_Aφ,d_Aφ] = −δS[2nd-order orbit term] ≠ 0` off-critical.

> **CORRECTION (skeptic finding E4 -- a genuinely false sentence, mine).**
> An earlier draft of this section said the minimum-eigenvalue curve
> *"tracks `3(6t²−6t+1)` and turns negative exactly on
> `(0.211325, 0.788675)`"*. **The round's own table refutes that**: at
> `t=0.1` the minimum is `−0.1056` while the family direction is `+0.46`,
> and at `t=0.25` the minimum `−0.1553` is *below* the family value
> `−0.125`. The correct statement is the one two lines above: away from
> the critical points the minimum is dominated by near-gauge modes and has
> nothing to do with the family direction; the two coincide **only at
> `t=1/2`**, where the gauge modes are exact zeros. Corrected in the
> script's own printed output as well, with the contradiction quoted
> rather than silently deleted.

## Step 5b -- the `t=1/2` index, re-checked at the higher cutoff (skeptic E7)

[VERIFIED, PART 5b] The index-1 claim was originally computed only at
`2j≤8`, and the skeptic's objection is not idle: at a critical point the
gauge directions are *exact* zero modes and `D^†D` is `O(1)` on them, so
"large `j` is safe" does not follow from `D^†D ~ j²`. Re-run at `2j≤14`:
```
  2j= 0   min eig = -0.500000000   negative modes in block = 1
  2j= 1..14  min eig = -0.000000000   negative modes in block = 0  (every one)
  Morse index at t=1/2:  2j<=8 -> 1 ;  2j<=14 -> 1   (unchanged)
```
**Plus an analytic backstop valid at every `j` at once**, so the claim no
longer rests on a cutoff at all: the `F`-term is `(t²−t)` times the form
`(tr a)² − tr(aa)`, whose spectrum on `3×3` real matrices is `{+2` (trace,
×1)`, +1` (antisymmetric, ×3)`, −1` (symmetric-traceless, ×5)`}`, tensored
with the identity on the mode index -- so it has the **same** spectrum in
every block. With `D^†D ≥ 0`, `H ≥ min(F-term) = −½` for all `j`
simultaneously, and the observed minimum `−0.5` saturates that bound
exactly. [This backstop was prompted by the skeptic's own T9 observation
and is credited accordingly.]

## Step 6 -- `t=0` and `t=1` are ONE point, related by a LARGE gauge transformation

[VERIFIED, PART 6, finite differences on the group at 50 random points]
With `G = Ad : SU(2) → SO(3)`,
```
max_{x,i} | R(x)^{-1} (X_i R)(x) − ad(T_i) |  =  2.1e-10 ,     R := Ad ,
```
and `ad(T_i)` is exactly the connection form of `∇^1` in the
left-invariant frame. So **`A^1 = G^{-1}dG` is pure gauge and `A^0 = 0`
is the trivial connection**: the two are related by a bundle automorphism
of the `SO(3)` frame bundle covering the **identity** diffeomorphism of
`S³` -- no orientation reversal is involved anywhere.

[VERIFIED, PART 6] Operational consequence, checked rather than assumed:
the two Hessians must then be unitarily equivalent. Comparing total
spectra (with multiplicity `2j+1`) up to `2j=14`, restricted to
eigenvalues `< 6` so the truncation edge cannot bite: **3873 eigenvalues
on each side, agreeing to `3.9e-14`.** (Block-by-block they need not
agree, and do not, because `G` is not left-invariant and mixes
`j → j±1` -- see the covariantly-constant-section migration in Step 4.)

[VERIFIED, PART 6b, exact rational arithmetic] The transformation is
**LARGE**:
```
Σ_{ijk} ε_{ijk} tr(T_i T_j T_k) = −3/2 ,
n = (1/24π²) ∫_{S³} tr((g^{-1}dg)³) = (−3/2)(16π²)/(24π²) = −1 .
```
`|n| = 1`: `G` generates `π₃(SO(3)) = ℤ`. [CITED, standard covering-space
theory, not re-derived] `Ad` induces an isomorphism on `π₃`, so the
winding of `G` equals that of its `SU(2)` lift, the identity map, which
is what the integral above computes.

**This is the sharp structural statement the round contributes -- and it
has TWO halves that must be stated together** (the skeptic's finding E1:
the first half alone is a tautology dressed as a physical exclusion, the
second half alone would contradict C123's own `CS(0) ≠ CS(1)`):

* **`𝒜/𝒢` (full, disconnected gauge group).** `A^0` and `A^1` are ONE
  point. So every `𝒢`-invariant functional of `ω` alone -- `S_YM` and
  every curvature-norm invariant -- gives them the same value.
  *Honest about what this is:* the implication itself is a **tautology**
  ("orbit-invariants do not separate points of an orbit"). Its content is
  entirely in the **classification** -- in the fact that `S_YM` and the
  curvature norms *are* in that class, and that this is a strictly
  stronger reason than "even in `x = t−½`" (evenness forbids *preferring*
  one; orbit-sameness forbids *distinguishing* them at all).
* **`𝒜/𝒢₀` (identity component only).** They are **NOT** the same point:
  they sit in winding sectors `0` and `−1`. A functional invariant only
  under `𝒢₀` can and does distinguish them, shifting by the winding
  number -- which is exactly what a Chern-Simons functional does, and
  exactly why C123 measured `CS(0) = 0 ≠ CS(1) = −B/3`. **The two results
  cross-check each other**: had `n` come out `0`, C123's finding would
  have been in trouble.

**Consequence adopted from the skeptic (its E1 point 3), and it
STRENGTHENS C123 rather than narrowing it -- see Step 9:** because the
winding label is a locally constant integer on the flat set, `A^0` and
`A^1` lie in different *components* of it, so **any** continuous path
between them must leave the flat set. The `t=1/2` barrier is
**topologically forced**, not an artifact of the particular path the
1-parameter family happens to take.

**SCOPE, stated because it is easy to overread, and because C125 owns the
neighbouring question.** This is gauge equivalence of the `SO(3)`
CONNECTION alone, i.e. after **forgetting the soldering form**. As AFFINE
connections on `TS³` the two are NOT equivalent: their torsions have
opposite sign, `T^t(X_i,X_j) = (2t−1)[X_i,X_j]`, so `T^0 = −T^1 ≠ T^1`
[VERIFIED, PART 6]. Relating those still requires the
orientation-reversing `ι(g)=g^{-1}` of C37-C39/OB13, exactly as that
round found. **Nothing here settles C125's question** (an isometry of the
full `M₄×S³×S⁶` preserving vielbein, twist bundle and fermion content),
and nothing here contradicts C37-C39: `ι` and `G=Ad` are different maps
answering different questions.

**Does the argument prove too much?** This is the check that matters, and
the answer is no, for a reason worth stating precisely because it is the
whole content of the scope boundary. A gauge transformation `Λ` of the
frame bundle acts on the PAIR `(e, ω)`, rotating the frame as well:
```
(e, ω^0)  ↦  (Λe, Λω^0Λ^{-1} − dΛ·Λ^{-1})  =  (Λ e, ω^1)   ≠  (e, ω^1).
```
So the configuration reached from `t=0` by gauge is `(Λe, ω^1)`, **not**
the `t=1` configuration `(e, ω^1)`. Anything that depends on the pair --
the torsion `T = De`, the vielbein, the Dirac operator `D^t` (whose
Clifford multiplication is soldering) -- therefore still separates them.
Concretely and consistently with what this project already established:
* `T^0 = −T^1` [VERIFIED here], `Scal(∇^t) = Scal_LC − 6(2t−1)²`
  (round111), `B₃ = e_i∧T^i` (C124 Sector II), `(2t−1)Vol·Vol` (C120) --
  all still `t`-dependent, none touched;
* `D^0` and `D^1` are related by `ι`, an orientation-REVERSING isometry
  (C37-C39), which is why they give the two opposite chiral halves
  `(1,2)` vs `(2,1)` rather than being identical. Nothing here makes them
  gauge-equivalent, and the argument would be wrong if it did.

**Relation to C25's "M2" branch (the ill-posedness world).** C25 named
`M2 = "t=0 and t=1 are gauge-equivalent via ι"`, and C37-C39 refuted it:
`ι` is orientation-reversing, hence parity, not gauge. **This round does
NOT resurrect M2.** It finds a genuinely different map -- a bundle
automorphism over the identity, orientation-preserving -- but one that
only relates the CONNECTIONS, leaving the soldering behind; and the
soldering is physical. What the round does supply is a better diagnosis
of the pattern M2 was trying to explain: the long run of even/null
results is not primarily a parity fact and not an ill-posedness fact, it
is a **structure-usage** fact --
> functionals of `ω` alone are blind to `t=0` vs `t=1` because those are
> one point of `𝒜/𝒢`; functionals that use the soldering form are not
> blind, and every `t`-dependent quantity this project has ever computed
> lives in the second class.

This is a sharper and more actionable statement than OB13's (already
once-corrected) "must be odd in `x`", and it is consistent with, not a
replacement for, that corrected rule.

## Step 7 -- the homogeneous vacuum set is bigger than `{0,1}`

claim.md's secondary clause asks whether new stable homogeneous vacua
appear outside `{0,1}`. A general left-invariant connection is a `3×3`
real matrix `M` (`M_i^b`), of which the family `A^t = t·Id` is one line.

[VERIFIED, PART 7b] `V(M)` is invariant under `M ↦ h M R^T` for
`h,R ∈ SO(3)` (checked numerically, 200 random cases each: `h` = global
internal gauge rotation, `R` = a right translation of `S³` acting on the
left-invariant frame). Every orbit therefore has a **diagonal**
representative, and on the diagonal
```
V(diag(m₁,m₂,m₃)) = (m₁m₂−m₃)² + (m₁m₃−m₂)² + (m₂m₃−m₁)²
```
(closed form verified against the general numeric `V` at 50 random
points). Solving `∇V = 0` exactly with sympy gives **9 real points**:
```
  m = (0,0,0)                                    V=0       sig (−,0,+) = (0,0,9)
  m = (1,1,1), (1,−1,−1), (−1,1,−1), (−1,−1,1)   V=0       sig (−,0,+) = (0,3,6)
  m = ½·(those same four)                        V=3/16    sig (−,0,+) = (1,3,5)
```
* **flat (global minima): 5**  -- `M=0` (this is `t=0`) and the four
  diagonal representatives of `SO(3)` (one of which is `Id`, i.e. `t=1`);
* **non-flat saddles: 4** -- the `½·SO(3)` orbit, containing `t=1/2`,
  each with exactly one negative direction and three zero directions
  (its own orbit);
* **non-flat critical points with NO negative direction: 0.**

[VERIFIED, PART 7, independent 800-random-start root-find] the same three
orbit classes and nothing else; every `SO(3)` matrix is flat; a `det=−1`
orthogonal matrix (`diag(1,1,−1)`) is **not** flat -- correct and not a
defect, since `Aut(𝔰𝔲(2)) = SO(3)`, not `O(3)`: a `det=−1` map reverses
the cross product and is an anti-automorphism. The algebraic reason
behind the whole classification: `F = 0 ⟺ [M_i,M_j] = ε_{ijk}M_k ⟺ M` is
a Lie-algebra homomorphism `𝔰𝔲(2)→𝔰𝔲(2)`; `𝔰𝔲(2)` is simple, so its
kernel is `0` or everything, i.e. `M = 0` or `M ∈ Aut(𝔰𝔲(2)) = SO(3)`.

**Answer to the secondary clause: no new homogeneous vacuum appears that
`S_YM` ITSELF could use to break the degeneracy -- and the vacuum set is
`{0} ⊔ SO(3)`, a point plus a 3-manifold, not the two points
`{t=0,t=1}`.** All of it sits at `S_YM = 0`. This makes the selection
problem strictly **harder** for `S_YM`: a continuum of exactly degenerate
minima, of which the 1-parameter family sampled two points.

> **CORRECTION (skeptic finding E8).** An earlier draft said "no NEW
> vacua **in any sense**". That is false, and self-undermining: `{0}` and
> `SO(3)` are two **different connected components** of the flat set,
> lying in different small-gauge winding sectors (Step 6b), and the full
> flat set has one component per winding number -- the standard
> `θ`-vacuum ladder. That *is* a sense, and it is precisely the sense a
> Chern-Simons functional uses. The correct claim is scoped to `S_YM`,
> which cannot see the label; it is not universal.

## Step 8 -- non-metric (`𝔤𝔩(3)`) perturbations: what survives (skeptic E2)

[VERIFIED, PART 8] Built the `𝔤𝔩(3)`-valued operator explicitly
(`A_i = t·L_i` acting by matrix commutator), rather than reasoning about
it. At `t=0` and `t=1`, `2j = 0..4`:

| | result |
|---|---|
| positivity | **survives** -- the Step 3 argument only ever used "sum of squares, zero at a flat connection", which is blind to the structure group |
| `dim ker = rank(d_A on Ω⁰(𝔤𝔩₃))` | **still holds** (`H¹ = 0` for `𝔤𝔩(3)` too, since `b₁(S³)=0`) |
| kernel size | **strictly larger** -- e.g. `18` vs `6` at `2j=1,t=0`; `8` vs `3` at `2j=0,t=1` (`8`, not `9`, because the `𝔤𝔩(3)` centre is covariantly constant) |

So **"no extra zero modes" does not survive verbatim.** The extra null
directions are gauge directions of the larger `GL(3)` group, which is not
a symmetry of a theory that has a metric -- they deform the connection
into a flat *non-metric* one. Correct scope, now used everywhere above:
**kernel = the metric (`𝔰𝔬(3)`) gauge orbit, within metric connections.**

## Step 9 -- the barrier is topologically forced (skeptic E1 point 3, adopted)

[VERIFIED where computable, PART 9] Chain, each link either computed here
or standard:
1. `S³` is simply connected, so **every** flat connection is pure gauge:
   the flat set is the gauge orbit of `0`.
2. Chern-Simons restricted to that set equals the winding number up to a
   fixed positive constant -- an **integer-valued continuous** function,
   hence locally constant.
3. `CS(A^0) = 0`, `CS(A^1) = −1` [VERIFIED, Step 6b, and independently
   re-derived by the skeptic]. So `A^0` and `A^1` lie in **different
   connected components of the flat set.**
4. Therefore **any** continuous path from `A^0` to `A^1` must leave the
   flat set, i.e. `S_YM > 0` somewhere along it. **The barrier is
   forced.**

Checked for the family path specifically: `S_YM(t)/Vol = 3t²(t−1)²` has
zeros exactly at `t ∈ {0,1}`, is strictly positive on the open interval,
and peaks at `3/16` at `t = 1/2`.

**SCOPE, stated rather than glossed:** this shows the family path's
barrier is `3/16` and that *some* barrier is unavoidable. It does **not**
show `3/16` is the LEAST barrier over all paths (the true sphaleron
energy) -- a variational problem not attempted. Step 7b's index-1 saddle
at `½·SO(3)` is *consistent* with it being the sphaleron; consistency is
not proof. [UNKNOWN], named.

**This is a strengthening of C123, not a demotion.** C123 read `t=1/2` as
a barrier top between two flat vacua and correctly scoped that to the 1D
slice. Step 6 might have looked like it dissolved the picture ("one point
modulo gauge"); Step 9 shows the opposite -- the barrier is there for a
topological reason that no choice of path can remove.

---

## Kill Analysis (Anti-Overfitting Gate)

### What this round KILLS

* **The pre-registered kill criterion is NOT met, and that is itself the
  kill of the interesting reading.** There is no negative mode at `t=0,1`
  -- but the reason (a non-negative functional vanishing at a flat
  connection) is automatic and therefore carries **zero** selection
  information. "`S_YM` selects a stable pair" is now shown to be a
  statement with no content beyond "`S_YM` vanishes on flat connections".
* **NOT C123's barrier reading -- that is STRENGTHENED, and an earlier
  draft of this line got it backwards.** Modulo the FULL gauge group
  there is one vacuum sampled twice; modulo the IDENTITY COMPONENT there
  are genuinely two, in winding sectors `0` and `−1`, and the barrier
  between them is **topologically forced** (Step 9), with a Morse-index-1
  saddle. C123's arithmetic is untouched and its interpretation survives
  with a better reason behind it. What *is* killed is the weaker reading
  in which the barrier is an artifact of the particular 1-parameter path.
  [INFERRED, no literature search run this round] the whole structure is
  the textbook Yang-Mills winding-/`θ`-vacuum picture, not a feature
  specific to this project's construction -- flagged in the Relaxation Map
  for a novelty check rather than asserted.
* **Any remaining hope that a FULL-gauge-invariant functional of `ω`
  alone could break the `t=0` vs `t=1` degeneracy**, by a mechanism
  stronger than the parity argument OB13 was corrected to. This closes
  that class by sameness-modulo-`𝒢`, not by evenness. **Scope, per
  skeptic E1: this does NOT close functionals invariant only under `𝒢₀`
  -- Chern-Simons is precisely such a functional and it DOES distinguish
  them.** (Whether a CS-type term can descend from a parent action is
  C124's separate, already-closed question; nothing here reinforces or
  weakens that, and this clause must not be cited as if it did.)

### What this round does NOT kill

* **`S_YM` as an F6 candidate in the narrow sense C123 credited it with**
  -- it does supply a named action principle with an EOM, which round99's
  bare invariant did not. That remains true; it is just now clear the
  EOM's solution set at `t∈{0,1}` is uninformative for selection.
* **The affine-connection / torsion question.** `T^0 = −T^1`; the two are
  genuinely different affine connections. Everything the project has
  built on that (round111's `Scal(t)`, C124's Sector II `B₃`, C120's
  `(2t−1)Vol`, the Dirac family `D^t`) is untouched.
* **C125's question** (full 13D configuration equivalence including
  vielbein, twist bundle, fermion representations) -- different question,
  different objects, not answered here in either direction.
* **C25's `M2` ("the question is ill-posed, `t=0`~`t=1` via `ι`") stays
  refuted**, as C37-C39 left it. This round finds a different map, which
  relates the connections but not the soldered configurations, so it does
  not revive M2. Recorded explicitly so a later reader does not mistake
  Step 6 for a resurrection of a branch this project already closed.
* **The parent-action gap.** Why the `S³` connection should have its own
  Yang-Mills dynamics at all remains exactly as open as before this
  round, per claim.md's own pre-registration.
* **Non-metric perturbations, Lorentzian signature, higher-derivative
  curvature functionals, the inhomogeneous critical set of `S_YM`.**
* `N_gen=3`'s CONDITIONAL status, `lambda = FREE_COUPLING_PARAMETER`,
  `safe_for_runtime = False` -- all unaffected, as pre-registered.

### Relaxation Map (one assumption changed per variant; V2 attempted and closed this round, the rest not)

| Variant | Single assumption changed | Kill criterion / what it would settle |
|---|---|---|
| V1 | Replace `S_YM` by a functional that **uses the soldering form** (torsion-dependent, e.g. `∫\|T\|²`, `∫e∧T`, Nieh-Yan) | The blindness result of Step 6 does NOT apply to these -- they see `T^0 = −T^1`. Kill criterion: does any such functional have `t=0,1` as its minima AND break their degeneracy? (Note C124 already killed the 13D-covariant route to them; this variant asks about `S³`-internal ones, a different question.) |
| V2 | Allow non-metric (`𝔤𝔩(3)`-valued) perturbations | **DONE this round (Step 8, prompted by skeptic E2).** PSD survives; `H¹=0` survives; the kernel is strictly larger, so "no extra zero modes" is metric-only. Closed. |
| V3 | Add a `θ`-term / Chern-Simons piece to `S_YM` | The ONLY way, per Step 6, that a functional of `ω` alone can distinguish `t=0` from `t=1` -- and per the skeptic's E1 it genuinely can, so this is not a dead end for the *reason* Step 6 gives. But it is precisely C123's Claim 2 route, which C124 closed at the **parent-action** level for a different reason. Listed so it is neither silently re-tried as if new nor wrongly treated as killed by this round. |
| V4 | Classify the INHOMOGENEOUS Yang-Mills connections on `S³` | Would complete the critical-point picture and settle whether `3/16` is the true sphaleron energy (Step 9's named `[UNKNOWN]`). No bearing on the pre-registered question; genuinely open. |
| V5 | Vary the METRIC `g`, not just the connection | Named by skeptic E2 and never attempted anywhere in this round. A stability statement about the *geometry* needs `δg`; `S_YM` is blind to the connection/metric split by construction. |
| V6 | Novelty check: is the winding-vacuum + forced-barrier + index-1-saddle structure a known result for `S³` Yang-Mills? | Cheap literature check, **not run this round**. Would determine whether Steps 6/6b/9 are a reproduction (like round99's Cartan-Schouten result) or new content. Until run, treat them as **probably a reproduction** -- the honest default given round99's own precedent. |

---

## Proposed pearl (reusable pre-filter, sibling to C119's Künneth filter and C124's ε/η filter)

Not written to `pearl_registry/INDEX.md` by this round -- proposed here
for the orchestrator, since editing the registry is outside this round's
brief. Per the FL Pearl Gate, this is a side-finding that is real and
testable but is not the claim this round was about.

* **observation:** on `S³=SU(2)`, `ω^{t=0}` and `ω^{t=1}` are ONE point of
  `𝒜/𝒢` -- related by a bundle automorphism over the identity with
  winding number `n=−1`. So a candidate `t`-selector can be pre-filtered
  in one line, before any computation, by asking **which structure it
  uses**: if it is a function of the connection `ω` alone and is
  invariant under the full gauge group, it is dead on arrival for the
  `t=0`-vs-`t=1` half of the selection question. It survives the filter
  only if it (a) uses the soldering form / vielbein / torsion, or (b) is
  invariant under the identity component only (Chern-Simons-type, and
  must then shift by the winding number).
* **falsifiable_prediction:** every future OB1 F4 candidate of the shape
  "gauge-invariant local functional of the `S³` connection alone" is even
  in `x=t−½` AND, more strongly, exactly equal at `t=0` and `t=1` -- with
  no computation needed. Checkable against every such candidate the
  project has already tried (round99, round111's curvature part, `S_YM`).
* **impact_score:** 6 -- touches an assumption several OB1 branches
  depend on; does not change the main task's structure.
* **trigger_condition:** any new OB1 F4 candidate stated as a functional
  of the `S³` connection.
* **companion observation:** the corresponding blindness does NOT extend
  to the soldering-using class, which is exactly where every
  `t`-dependent quantity this project has computed lives -- so the filter
  is a pre-filter, not a no-go for the whole selection question.
* **⚠ MANDATORY qualifier, added after skeptic finding E1** -- without it
  the pre-filter is WRONG: "gauge-invariant" must mean invariant under
  the **full, disconnected** gauge group `𝒢`. A functional invariant only
  under the identity component `𝒢₀` -- Chern-Simons is the canonical one
  -- **passes** the filter and does distinguish `t=0` from `t=1`, by the
  winding number. A pre-filter stated without this qualifier would
  wrongly kill the CS family on grounds that do not apply.

**Second pearl, carried over from the skeptic's own recommendation 6:**

* **observation:** `t=0` and `t=1` are separated by a `ℤ`-valued
  small-gauge winding label (`n=−1`, computed exactly two independent
  ways), and the `S_YM` barrier `3/16·Vol` between them is topologically
  forced -- a sphaleron-type barrier, not an artifact of the path.
* **falsifiable_prediction:** any functional built from `CS(ω^t)`, or
  from the winding number of the interpolating path, **does** distinguish
  `t=0` from `t=1` -- directly contradicting the unqualified form of the
  blindness clause above, and testable against C123's already-computed
  `CS(0)=0 ≠ CS(1)=−B/3` without new machinery.
* **impact_score:** 7 -- it names the exact structural slot any future
  `t=0`-vs-`t=1` selector must occupy, and it explains an existing C123
  result rather than only predicting a new one.
* **trigger_condition:** any future attempt to break the `t=0`-vs-`t=1`
  degeneracy (as opposed to selecting the pair `{0,1}` as a set).
* **next_check:** the moment OB1 reopens, or the next candidate selector
  claiming to distinguish the two endpoints -- whichever is first.

---

## What this round does NOT show

1. Does **not** resolve OB1 or move it out of PARKED; no reopen condition
   is met.
2. Does **not** change C123's Claim 1 F4 status (`duplicate of round99`)
   -- as claim.md pre-registered, that is untouched by whatever F6 finds.
3. Does **not** touch C124's `STRUCTURAL_NO_GO` -- independent question,
   independent math, and C124 itself recorded that `S_YM` is
   dimensionally excluded from its own classification.
4. Does **not** answer C125's full-13D gauge-equivalence question. Step 6
   is about the `S³` `SO(3)` connection with the soldering form
   forgotten; C125 is about the full configuration with it, plus the
   `S⁶` twist and the fermions. The two must not be conflated.
5. Does **not** derive `S_YM` from a 13D parent action.
6. Does **not** claim novelty for the mathematics. Flat connections
   minimising Yang-Mills, `H¹` vanishing on a simply-connected manifold,
   and `π₃(SO(3))=ℤ` are standard; the round applies them, and Relaxation
   Map V5 flags the novelty check as unrun.
7. Does **not** change `N_gen=3`, `lambda`, or `safe_for_runtime`.
8. Does **not** solicit Tom Lawrence's Part 5.

---

## Verification

**Every claim above, with its evidence tier.**

| Claim | Tier |
|---|---|
| round99 convention reproduced; `T_a=-Z_a/2` gives `c₀=+1` | [VERIFIED] sympy, PART 0 |
| `\|R\|²_affine = 4·\|F\|²_YM`, constant | [VERIFIED] PART 1b, 200 random tensors |
| `F(A+a) = F(A)+d_Aa+[a,a]` exactly, all 9 components | [VERIFIED] sympy, PART 1 |
| `S_YM(t)/Vol = 3t²(t−1)²`; `C=3`; `E''(0)=E''(1)=6`, `E''(½)=−3` | [VERIFIED] sympy, PART 1 — reproduces C123 |
| Linear term `= 4t(t−1)(t−½)δ_k^c`; zero exactly at `t∈{0,½,1}` | [VERIFIED] sympy, PART 2 |
| `Q[a]=∫\|d_Aa\|² ≥ 0` at `t=0,1` (Hessian `=2d_A^†d_A`) | [VERIFIED] analytic, Step 3, cutoff-free |
| `ρ_j(T_k)` anti-hermitian, bracket-correct, `2j=0..8` | [VERIFIED] PART 4 |
| Assembled matrices reproduce the component formula on generic input (`F`-term `1.4e-14` / 500 cases; full `Q` at `2j=3` `2.3e-13` / 50 cases) | [VERIFIED] PART 4d |
| All blocks PSD at `t=0,1`, `2j≤8` and `2j≤14` | [VERIFIED] numeric, PART 4/4b |
| `dim ker Q = rank d_A` in every block ⟹ `H¹_{d_A}=0` | [VERIFIED] numeric, PART 4/4b |
| Spectral gap `= 1` at both `t=0` and `t=1` | [VERIFIED] numeric, PART 4 |
| Positive control: family direction reproduces `½E''(t)` at 6 values of `t` | [VERIFIED] PART 4 |
| External control: `t=0` spectrum matches the closed-form `S³` coexact-1-form Hodge spectrum, eigenvalue AND multiplicity, `k=1..7` | [VERIFIED] PART 4c — formula itself [CITED], not re-derived |
| `ρ_j(T_i)` agrees with C85's certified `build_l_matrices` (`l_i = 2ρ_i` up to similarity), `k=0..6` | [VERIFIED] PART 4e, certified module loaded dynamically per project convention |
| The rest of the apparatus (1-form/2-form complex, `d_A`, `F`-term) has no C85 counterpart and had to be built | [VERIFIED] by inspection of C85's public functions; C107 already separated `D̄_k` from `D^t` |
| Negative control: Morse index `0/1/0` at `t=0/½/1`; unstable eigenvector overlap with family direction `= 1.000000000000` | [VERIFIED] PART 5 |
| `A^1 = G^{-1}dG`, `G=Ad`, error `2.1e-10` at 50 random group points | [VERIFIED] PART 6, finite differences |
| Total spectra at `t=0,1` identical below `λ=6` (3873 each, `3.9e-14`) | [VERIFIED] PART 6 |
| `K=1/4`, `R=2`, `Vol=16π²` | [VERIFIED] sympy, PART 6b |
| Winding number `n = −1` (exact rationals) | [VERIFIED] sympy, PART 6b |
| `Ad` induces an isomorphism on `π₃`, so the lift's winding is `G`'s | [CITED] standard covering-space theory, not re-derived here |
| `T^0 = −T^1 ≠ T^1` (torsion still distinguishes them) | [VERIFIED] PART 6 |
| `V(M)` invariant under `SO(3)×SO(3)`; diagonal slice meets every orbit | [VERIFIED] numeric (200 cases each) + SVD argument |
| Diagonal closed form; 9 exact real critical points; 5 flat, 4 saddles, 0 new stable vacua | [VERIFIED] sympy `solve`, PART 7b |
| Flat homogeneous set `= {0} ⊔ SO(3)`; `det=−1` orthogonal is not flat | [VERIFIED] PART 7 numeric + the `Aut(𝔰𝔲(2))=SO(3)` argument |
| `d_A∘d_A = 0` at `t=0,1` (`8.5e-15`) and `≠0` at `t=1/2` (`1.837`) — so the dimension count does license "kernel = gauge orbit" | [VERIFIED] PART 4f, added after skeptic E5 |
| `t=1/2` Morse index still exactly `1` at `2j≤14`; analytic bound `H ≥ −½` at every `j` | [VERIFIED] PART 5b, added after skeptic E7 |
| PSD survives non-metric `𝔤𝔩(3)` perturbations; `H¹=0` too; kernel strictly larger | [VERIFIED] PART 8, added after skeptic E2 — no longer [INFERRED] |
| The metric `g` is never varied anywhere in this round | [VERIFIED] by inspection — named as a scope gap, Relaxation Map V5 |
| Barrier topologically forced: `CS` locally constant on the flat set, `CS(A^0)=0 ≠ CS(A^1)=−1`, so any path leaves the flat set | [VERIFIED] for the computed links (Step 6b winding, `S_YM>0` on `(0,1)`); the "every flat connection on a simply-connected base is pure gauge" link is [CITED] standard |
| `3/16` is the LEAST barrier over all paths (true sphaleron energy) | [UNKNOWN] variational problem, not attempted |
| The winding-vacuum + index-1-saddle structure is textbook YM, not new | [INFERRED] no literature search run — Relaxation Map V5 |
| Whether the inhomogeneous YM critical set on `S³` holds anything else | [UNKNOWN] not attempted |
| Whether C125's full-13D question resolves either way | [UNKNOWN] not this round's object |

**Tool-checked in this session:** `c126_ym_fluctuation_hessian.py`
(self-contained inside this experiment folder), output `run_c126.log`,
machine-readable `results_c126.json`, `python -m ruff check` clean,
`python -m ruff format` applied. No shared code modified, so **no pytest
suite touched**.

**Reproduce:**
```
cd experiments/20260901-c126-yang-mills-full-fluctuation-stability
python c126_ym_fluctuation_hessian.py
```
Expect the `WEAKENED_BY_FL_STEP_8A__...` label quoted at the top of this
file, and every boolean entry of `VERDICT INPUTS` `True` (23 of them),
with the four non-boolean diagnostics reading `t_half_morse_index: 1`,
`winding_number: -1`, `truncation_two_j_max_main: 8`,
`truncation_two_j_max_robustness: 14`.

**[CITED] project facts reused, not re-derived:** round99's generator
convention and `R^t = t(t−1)[[X,Y],Z]`; C123's `E(t)=Ct²(1−t)²`,
`E''(0)=E''(1)=2C`, `E''(½)=−C`, and `CS(0)=0≠CS(1)=−B/3`; C124's scope
note that `S_YM` is dimensionally excluded from its own classification;
C37-C39/OB13's finding that `ι(g)=g^{-1}` is orientation-reversing;
round111's `Scal(t)`; `PARENT_ACTION_GATE.md` F6's text.

**FL Step 8a skeptic pass:** RUN and answered in full -- see the response
matrix near the top of this file. Verdict **WEAKENED**; 9 findings, **9
accepted, 0 dismissed**; 4 new script sections added in response
(PART 4f, 5b, 8, 9), 3 printed statements corrected in place (E4, E8,
E9), and the verdict label rewritten (E3). Its independent hand
re-derivations confirmed the linear term to the digit, the entire `2j=0`
spectrum at `t=1`, the exhaustive 9-point homogeneous critical set, and
the winding number `n=−1` -- the last of which this session had computed
independently (PART 6b) before the report arrived, by a different route,
with the same answer.

**Per the FL Step 8a response matrix, `WEAKENED` promotes with a `[WEAK]`
marker plus documented caveats, which is what the revised label and the
four-item Completeness list above encode.** The round is not a PROMOTE
and does not claim to be; the honest summary is that the pre-registered
question had an answer that could not have come out any other way, and
the round's value is in what it found while establishing that.
