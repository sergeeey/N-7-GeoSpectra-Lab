# C136 — Decision (convergent-mode, FL Full-Ladder)

**Date:** 2026-09-02
**Experiment:** `20260902-c136-joint-killing-spinor-constraint`
**Question type (EstimandOps L0):** Descriptive — existence of a solution set with a
stated structure. Explicitly **not** causal, **not** predictive.
**Script:** `c136_joint_killing_spinor_check.py` · **Results:** `results_c136.json`
**Skeptic record:** `skeptic_verdict.md` (two independent context-blind passes)
**Candidate under test:** C132's `P14` (tied at CDT 6.5 with `P2`; the last of C132's
top-tier candidates to be run).

> **⚠️ Read §14 and `skeptic_verdict.md` before quoting anything above them.** Two
> independent, context-blind FL Step 8a skeptic passes both returned **`[FALSIFIED]`**
> and **agreed** on the core defects. **This document is the post-repair version.** The
> pre-repair draft's headline check could not fail, its round114 discriminator was
> factually wrong, and its central structural argument was a non-sequitur. All three
> are corrected below — the *conclusion about `P14`* survives, but its **evidence tier
> is materially lower** than the first draft claimed.

## Verdict

```text
P14_IS_DEAD__KILL_BRANCH_b_FIRES__THREE_CHANNEL_COLUMNS_IDENTICAL
  __BUT_THE_KILL_IS_A_RESTATEMENT_NOT_INDEPENDENT_EVIDENCE
  __ONE_LINE_DERIVABLE_FROM_EL3B_COROLLARY_PLUS_L5_WITH_NOTHING_THIS_ROUND_COMPUTED
  __BY_ROUND114S_OWN_STATED_CRITERION_APPLIED_TO_THIS_ROUNDS_OWN_HEADLINE__CHECK_F7
  __PRIOR_ART_SAYING_THE_SAME__G44_B1__GAP_4__ROUND81__PEARL_ROWS_22_AND_36
  __Z2_VS_Z3_BANDWIDTH_ARGUMENT_WITHDRAWN_AS_NON_SEQUITUR_NOT_NARROWED
  __A_2_PLUS_1_SPLIT_WOULD_SATISFY_THE_PREDICATE__AND_CHANNEL_DEPENDENT_S6_DATA
    _PAIRS_t_TO_THE_CHANNEL_THROUGH_THE_SHARED_SCALAR_WITH_NO_Z2_INVOLVED
  __PARITY_THEOREM_REPAIRED__REQUIRES_BLOCK_DIAGONAL_A__OFF_BLOCK_COUNTEREXAMPLE_J1
  __NOT_BLOCKED_ON_13D_SUSY__NAHM_DOES_NOT_BITE__SPIN_1_12_MODULE_IS_THE_REAL_PRICE
  __GENUINE_POSITIVE_CONTENT_IS_SECTION_G__C134_ROUTE_2_NON_TRANSFER_VERIFIED
  __AND_SECTION_J__TWO_COUNTEREXAMPLES_REPAIRING_THE_ROUNDS_OWN_THEOREM
  __S6_SOLUTION_SPACE_NOT_COMPUTED__SELF_CAUGHT_OVERCLAIM_WITHDRAWN
  __ALGEBRAIC_DILATINO_HALF_NOT_IMPOSED_IN_D_E__COMPUTED_SEPARATELY__ALSO_CHANNEL_BLIND
  __57_CHECKS_0_FAILURES__TWO_CHECKS_DELETED_AS_UNFAILABLE__BOTH_MODULES_AGREE
```

**One line.** The joint constraint can be posed geometrically and it does couple the
factors — but the three channel columns come out identical, so `P14` dies on
kill-branch **(b)**. **The honest finding is what that kill is worth:** it follows in
one line from E-L3B's Corollary plus L5, with nothing this round computed, which is
precisely the shape round114 was falsified for. C136 supplies an *encoding and a
reduction*, not independent evidence.

---

## MANDATORY FIRST MOVE, stated before anything else

**No standard Minkowskian supergravity exists at `D = 13`.** Standard supergravity caps
at `D = 11` (Nahm's theorem). This project's own `SPIN13_TO_SPIN4_DECOMPOSITION.md:3-16`
`[VERIFIED-tool, read in full this round]`:

> *"the original task named this `Spin(1,12)→Spin(1,3)×Spin(3)×Spin(6)`. **This framing
> is not used** … There is no established `Spin(1,12)` structure group in this project —
> standard supergravity caps at 11D (Nahm's theorem), and no consistent 13D parent theory
> is claimed. This audit instead covers what the project **actually has**: a Kaluza-Klein
> **product ansatz** … **not a unified higher-D spacetime**."*

**Therefore the constraint tested here is NOT imported supergravity.** Its two halves
are dispositioned separately, adopting C134 §6's own correction rather than re-deriving it:

| half of the objection | does it bite? |
|---|---|
| **Nahm / supersymmetry** | **NO.** `[INFERRED — chain stated]` Nahm classifies *supersymmetric supergravities*. A generalized Killing spinor equation `∇^g_X ψ = A(X)·ψ` is ordinary Riemannian spin geometry, defined on **any** spin manifold with **no supersymmetry**. AHL2023 introduces it exactly that way (§1, quoted in §1 below). No SUSY algebra appears anywhere in this round. |
| **The `Spin(1,12)` module** | **YES — this round's single largest assumption.** A *joint* constraint needs one spinor on the 13-manifold, i.e. a `Cl(1,12)` module. Mathematically routine (a product of spin manifolds is spin), but the project **tried this framing, identified it as a conflation, and retired it**. Supplied here because the premise forces it; named as assumption 1 in §8. |

**Consequence:** this round is **not** `BLOCKED` on a 13D-SUSY import. It reports a
kill, not a block, because the obstruction is *computed* rather than *not-found*.

---

## Prior Result Gate — everything read from the primary this session

`SPIN13_TO_SPIN4_DECOMPOSITION.md` (full) · C132 `decision.md` (`P14` 655-693, §6 spec
900-912, §1b pre-filters, §7 finding 1) · C134 `decision.md` (§5b route 2, §6, **§8's
"does not kill `P14`"**) · round114 `decision.md` (full — the collapse *and its stated
criterion*) · round98 (full) · round86 (full) · round72 (H1a 20-25, H1b 27-52, the five
`t↔1−t` breakers 62-65) · C125 (§0a-0c, §2a, §4 **and its downgrade**) · E-L3B
`20260625-l3b-bundle-obstruction/decision.md` (Theorem + Corollary + level table) ·
round67/E2 (21, 75) · C107 (25) · `null_results/INDEX.md` (G44-B1, GAP-4, Round81) ·
`pearl_registry/INDEX.md` (rows 22, 34, 36, 37) · `docs/clifford_convention_registry.md`
(26-27) · both Agricola PDFs via `pdftotext -layout` (Agricola 2002 §3.1, §4.1 incl.
**Theorem 4.1**, §4.2 **Theorem 4.2(1)**; AHL2023 §1, §6 case (II) **in full**).
All `[VERIFIED-tool]`.

**round98's blocking gap does NOT block this round.** Round98 could not read
Friedrich–Ivanov's *uniqueness* theorem. This round never needs uniqueness: it *posits*
the frozen `∇^t` and asks what the solution set is. Round98 stays `INCONCLUSIVE`.

**round86 does not transfer, and is not re-attempted.** Round86's near-miss was
AHL2023's `ψ±` pair — two spinors under *one* connection, split by **Killing-eigenvalue
sign**, not by the affine parameter `t`. **This round does not identify the two.** §3
computes `∇^t` on invariant spinors directly and *derives* the `∓1/2` constants at
`t = 1/2` as a **consequence**, used as a control (`C7`), never as an input.

---

## 1. Zero-Signal Gate (FL Step −5), run before any computation

| field | content |
|---|---|
| **Entity** | `(∇^{LC}_M + (1/4)(∂_M⌟H)· − A(∂_M)·)ε = 0` on `M₄×S³×S⁶`, `H = H₃^t ⊕ H₆` the frozen factor-wise torsion, `A` symmetric, `ε = ε₄⊗η₃⊗η₆` |
| **Falsifiable predicate** | the solution set pairs one `S³` `t`-sector with one `S⁶` triality channel asymmetrically |
| **Measurable outcome** | the explicit `3×2` table, `results_c136.json:data.E_table_3x2` |

All three fillable ⇒ **gate PASSES** (not `REFUSE`).

**Both terms are standard forms taken from the primaries, not invented:**

* AHL2023 §1, verbatim `[CITED]`: *"generalized Killing spinors, i.e. spinors ψ which
  are solutions of the equation `∇^g_X ψ = A(X)·ψ`, where `∇^g` and `·` are respectively
  the spin Levi-Civita connection and the Clifford multiplication on M, and **A is a
  symmetric endomorphism**."* (The emphasis matters — see `J1`.)
* Agricola 2002 §3.1 `[CITED]`: `T^t(X,Y,Z) = (2t−1)⟨[X,Y]_m,Z⟩`, `T^t = (2(2t−1)/3)H`;
  §4.2 Theorem 4.2(1): `∇^t_Z ψ = (t/3)(Z⌟H)·ψ` for a constant spinor. This is the
  literal source of this project's own `t`-family (round86 §1a).
* `claim.md`'s `c·H_{MNP}Γ^{NP}` **is** the `(1/4)(∂_M⌟T)·` term at `c = 1/8`.

**The construction is LINEAR in the spinor**, as `claim.md` asks to be stated
explicitly: `ε` appears once in every term. There is no bilinear anywhere. That is what
makes §7's non-transfer question live.

---

## 2. The Clifford-parity theorem — **repaired**, with its hypotheses now explicit

> **Theorem (parity).** Let `M = M₄ × M³ × M⁶` carry a **strict product metric**, a
> torsion 3-form with **factor-wise legs**, and a symmetric `A` with **no off-block
> component**. Then on `ε = ε₄⊗η₃⊗η₆`:
>
> 1. Every **Clifford-even** term — spin connection *and* torsion — acts as
>    `(operator on its own factor) ⊗ 1`; the system **factorises exactly** and carries
>    **zero** cross-factor information.
> 2. Every **Clifford-odd** term — the `A(∂_M)·` term — does not factorise. It is the
>    only source of coupling.
> 3. The cross-factor operators an odd `S³` term carries are exactly `γ₅` and `Γ₇`.
> 4. An odd `S⁶` term carries `γ₅` and `1₂` — **no `S³` operator**. One-directional.

Machine-verified in representation-independent form (`B1`, `B2`, `B7`): `[Γ^iΓ^j, Γ^a]=0`
on all 54 triples and `{Γ^i, Γ^a}=0`, both following from the anticommutation relations
alone; plus explicit block forms `B3`-`B6` and `B8`/`B9`.

**⚠️ The third hypothesis was missing from the first draft, and both skeptic passes
falsified the theorem without it.** AHL2023 requires only that `A` be *symmetric*. With
an off-block `A_{ia}` the `S³` equation acquires `Σ_a A_{ia}Γ^{6+a}` — a full `Cl(6)`
**vector**, six operators, not one grading bit. **Check `J1` exhibits the
counterexample.** The hypothesis is not vacuous but it must be *argued*: `G₂`-invariance
forces it, since `SU(3)` acts on `T_pS⁶ = ℝ⁶ = 3⊕3̄` with **no trivial summand**, so any
`SU(3)`-invariant vector is zero `[INFERRED — chain stated; the `ℝ⁶` irreducibility is
the same fact §8 assumption 3 already relies on]`. **A non-`G₂`-invariant `A` is exactly
route (b)**, carrying `pearl_registry` row 37's cost.

**Novelty, narrowed on my own initiative before the passes returned.** Three pieces are
already in the repository:

| already established | where |
|---|---|
| on `S³` (`dim m = 3`) Kostant's cubic torsion element collapses to a scalar, *"because H has only one Clifford triple (`Z₁Z₂Z₃` = `Cl(3)`'s central volume element) — there is nothing for it to mix"* | round67/E2 `decision.md:21,75` |
| *"An odd-dimensional Clifford factor has a central volume element; it cannot be a grading. This is the general reason, not a convention artifact."* | C125 §4 |
| `Ω₃ = γ₅⊗1₂⊗Γ₇` — the embedded `S³` volume element has **zero `S³` content** | C134 §5a item 1 |

Plus `null_results` **Round81**: *"`ω=Z₁Z₂Z₃=I₂` is central (odd-dim Clifford fact);
Schur's lemma forces it scalar … so no `S³`-Clifford grading operator can split it."*

**What is actually new, and only this:** the even/odd split of a *first-order* constraint
with the even part shown to factorise exactly (the `O1` decoupling at first order rather
than at `D²`), and the one-directionality stated as a property of the coupling rather
than of a single operator. **The bandwidth *count* that the first draft built on top of
this is withdrawn — see §5b.**

---

## 3. `∇^t` on invariant `S³` spinors — the round's genuinely computed half

From the `su(2)` structure constants (verified from explicit `2×2` matrices, `C1`), the
Levi-Civita form `ω_{i;jk} = ±(1/ρ₃)ε_{ijk}`, and C125's `T^t_{ijk} = 2(2t−1)ε_{ijk}/ρ₃`,
with `∇^t = ∇^{LC} + (1/4)(X⌟T^t)·`:

```
        nabla^t_X  eta_L  =  -( t /rho3) X . eta_L        (left-invariant frame)
        nabla^t_Y  eta_R  = +((1-t)/rho3) Y . eta_R       (right-invariant frame)
```

`[VERIFIED-tool, C3/C4 — 10 `(t,ρ₃)` points × 3 directions]`. **Both skeptic passes
independently re-derived this, including factors of two and signs, and confirmed it.**

Four corroborations, all reproduced rather than cited:

| consequence | matches |
|---|---|
| `t = 0`: `η_L` parallel; `t = 1`: `η_R` parallel (`C5`,`C6`) | round72 **H1b** |
| `t = 1/2`: constants `∓1/2` (`C7`) | AHL2023 §6 (II) |
| `D^t(n=0) = 3t·I₂` on `η_L` (`C8`) | **C64's certified value** |
| `D^t(n=0) = (3t−3)·I₂` on `η_R` (`C9`) | **round67's other branch**, quoted verbatim by C107:25 — *"the two `n=0` branches are `3t` and `3t−3`; zero at `t=0` and `t=1` respectively, never simultaneously"* |

`C8`/`C9` are the strongest evidence that §3 is not round114 again: at `t = 1/2` they
give `±3/2`, the same Friedrich-1980 constant round114 obtained by trace collapse — but
here it arrives *with its entire `t`-dependence* and matches two certified values.

**AHL2023 §6 (II) in full, since the first draft truncated it** `[VERIFIED-tool,
`ahl2023.txt:3212`, skeptic finding]`: *"the round metric … admits a pair of invariant
Killing spinors for the constant `1/2`, **but no invariant generalized Killing
spinors**."* The dropped clause **closes Relaxation-Map variant `V2`** — see §10.

**Convention alignment** `[VERIFIED-tool, `docs/clifford_convention_registry.md:26-27`]`:
`S³` is `Z_i = i·σ_i`, `e² = −1`, `Cl(0,3)`; `S⁶` is `Γ_a` Hermitian, `e² = +1`,
`Cl(6,0)`. The script uses exactly these — the pair the registry flags as *"the genuinely
opposite pair"*.

**Sector-label caveats, both inherited.** The **set** `{(1,2),(2,1)}` is
convention-independent (round90:268, round95:162); *which* label attaches to *which* `t`
is a convention (E17 §1 prints both), and E17:66 records `ker D^{t=1}` as established
*"only under `c0 = −2`"*. **The labels in §5's table are hard-coded strings cited to C38,
not computed here** (skeptic finding, accepted). §3's own law depends on neither.

---

## 4. The decomposed system, and the one coupling it produces

Solving the `S³` equation as a genuine `64×64` operator equation (`D1` confirms the block
is the restriction of the real 13D operator):

```
        lambda  =  mu * chi4 * chi6 ,        mu = -t/rho3   or   +(1-t)/rho3
```

`[VERIFIED-tool, D2 — 24 configurations; `λ` solves it, `λ + 0.37` does not.]` The `S⁶`
equation carries `1₂` on the `S³` slot (`D3`): no `S³` datum flows back.

**Two readings of `A`, and only one of them can carry the coupling:**

| reading | `A` | `t`-content | cross-factor content |
|---|---|---|---|
| **(i)** one constant | `λ·1₁₃` | flat `M₄` forces `λ = 0` (`D4`), so only `t∈{0,1}` survive (`E3`) | **none — `λ = 0` annihilates `χ₆` by arithmetic** (skeptic finding, accepted) |
| **(ii)** block-scalar — AHL2023's own, more general form | `diag(0₄, α1₃, β1₆)` | `α` free ⇒ every `t` solves (`E4`) — zero `t`-selection content | `α` is a genuine function of `χ₆` |

**The `3×2` table is therefore filled in reading (ii)**, where the coupling is live.
Reading (i) is reported separately and is *not* used for the table — precisely because
its cross-factor content is zero by arithmetic. Reading (i)'s `t∈{0,1}` is in any case a
restatement of round72 H1b (`F5`).

---

## 5. The `3×2` table (reading (ii); `α` solved from the 64-dim residual)

| | **`t = 0`** | **`t = 1`** |
|---|---|---|
| **`8_v`** | `η₃`: left-inv, `α = 0.000000`; right-inv, `α = +1.000000` · `ε₄` constant, `dim_C 4` · `η₆`: **`[UNKNOWN]`** | `η₃`: left-inv, `α = −1.000000`; right-inv, `α = 0.000000` · `ε₄` constant · `η₆`: **`[UNKNOWN]`** |
| **`8_s`** | *identical, entry for entry* | *identical* |
| **`8_c`** | *identical* | *identical* |

**⚠️ Self-caught overclaim, withdrawn.** A first draft wrote the `S⁶` cell as *"NK
canonical spinor, `dim_C 1`"* and multiplied it into a `total_dim_C = 8`. **The `S⁶`
solution space was never computed** — the script builds no `S⁶` spin connection, no NK
torsion, no twist bundle `E` (the limitation C134 §7 disclosed for itself). And with `ε`
a section of `S(M₁₃)⊗E`, `E|_{SU(3)} = 3⊕3̄⊕1⊕1` has **two** trivial summands, so `dim 1`
was not even a safe guess. Now `[UNKNOWN]`; the spurious total is gone. *(Both skeptic
passes independently confirmed the defect.)*

**KILL BRANCH (b) FIRES** (`E1`): the three columns are identical. **`E1` is now a check
that can fail** — `solve_cell` solves for `α` from the residual, so `χ₆` reaches the cell
content, and `F4` confirms the injected-difference case returns **2** distinct `α`-sets
against **1** for the real inputs.

**Why the rows are identical — a fact about the INPUTS.** E-L3B's Theorem and Corollary
(read from the primary this round): `E_v ≅ E_s ≅ E_c` as `G₂`-equivariant bundles **with
identical canonical connections**, and the twisted Dirac operators *"are THE SAME
OPERATOR."* Plus L5/G74B: `sign(ind) = +1` for all three, hence one `χ₆`. Identical
inputs, identical outputs. **No claim is made that `G₂`-equivariance forces channel
symmetry** — C132 §7 finding 1 established it does not, and this round does not need it.

**Kill branch (c), precisely.** The `t=0` and `t=1` cells carry different `α` on the two
frames but equal dimension, so nothing in the constraint *prefers* one.

### 5b. The bandwidth argument is **WITHDRAWN**, not narrowed

A previous draft claimed a second, E-L3B-independent kill: the only carrier is `χ₆ ∈ Z₂`,
a `Z₂` carrier can 2-colour three channels but never 3-colour them, therefore no
asymmetric pairing. **Both skeptic passes refuted this, and they are right, twice over:**

1. **`claim.md`'s predicate is *"NOT every channel pairs equally with every sector"*. A
   2+1 split satisfies that.** So a `Z₂` carrier is entirely *sufficient* to produce the
   asymmetry the claim asks for; the cardinality argument never reached the conclusion.
   E-L3B's own level table contains exactly such a row (`SO(7)` separates `8_v` from
   `{8_s,8_c}`). **Check `E5` now demonstrates this** rather than asserting the refuted
   claim: with a 2+1 `χ₆` assignment the table *is* channel-asymmetric.
2. **The pairing need not pass through a Clifford carrier at all.** In reading (i) a
   single shared `λ` couples the factor equations, so channel-dependent `S⁶` data `β_α`
   gives `μ(t) = β_α·χ₄·χ₆` and hence `t = t(α)` — a genuine 3-way channel-selective
   pairing with **no `Z₂` bottleneck**. **Check `J2` exhibits three distinct `t` values.**

**So what actually kills `P14` is `χ₆`'s CONSTANCY across the channels (L5/G74B) and the
equality of the `S⁶` inputs (E-L3B)** — both prior art. Not a bandwidth count.

---

## 6. Round114 trap battery — and it fires on this round's own headline

**`F1` — the collapse is reproduced explicitly.** `Σᵢ Γ^i A(eᵢ) = −tr(A)·1` for 20
random diagonal `A`. No quantity of this shape appears in §3–§5.

**`F2` — corrected, and its old framing was wrong.** The first draft said *"round114's
`−tr(A)` moved under none of its analogous inputs."* **That is false**: round114 computed
`D^s = s/2 − 3/2`, which moves under `s` and has a zero crossing at `s = 3`
(`decision.md:23-26`). Input-dependence was never round114's criterion. `F2` therefore
establishes only that `λ` is a non-constant function of its own arguments (7/7
perturbations move it) — useful, but not the round114 test.

**`F3` — the parity theorem is representation-generic**, surviving 5 random `Cl(6)` basis
changes. Declared a **limitation**, not a result: it is a fact about `dim 3` odd /
`dim 6` even, true for any `M³×M⁶`. *(Scope, per skeptic: `F3`/`F6` re-check `B1`/`B2`/`B7`
and anticommutation only, not `B5`/`B6`. Since the count resting on `B5`/`B6` is
withdrawn, nothing depends on the gap.)*

**`F4` — a real positive control on the SOLVER.** The first draft's version injected `χ₆`
while `λ` was pinned to `0`, so the injection could not reach the solution set and `F4`
established only that two different dicts differ. Now: real inputs → **1** distinct
solved-`α` set; injected → **2**.

**`F5` — reading (i)'s `t∈{0,1}` restates round72 H1b.** `λ = 0` turns the constraint
into *"a `∇^t`-parallel spinor exists"*, already **PROVED** at `t = 0,1`.

**`F7` — round114's ACTUAL criterion, applied to this round's own conclusion.**
Round114 `decision.md:108-112`, verbatim: *"before claiming 'independent confirmation,'
check whether the computation's OWN output is derivable in one line directly from the
source's stated theorem … if so, it is a restatement."*

`F7` returns **`True`**: the three `S⁶` input dicts are literally equal, so *"the columns
are identical"* follows from E-L3B's Corollary + L5 with **nothing this round computed**.
**By its own stated test, the headline is a `[RESTATEMENT]`.** Prior art saying the same:
`null_results` **G44-B1** (*"S⁶ blind to τ"*), **GAP-4** (*"no S³ quantum number to mix,
structurally not just empirically"*), **Round81**, and `pearl_registry` rows **22** and
**36**. *The first draft applied `F5` to a sub-result and never to its own conclusion;
both skeptic passes caught that.*

**`F6`, `H1`-`H3`** — representation independence (10 `GL(64,ℂ)` similarities, worst
`1.25×10⁻¹⁵`) and agreement across **both** inequivalent `Cl(1,12)` modules. *(`H4` was
deleted: `channels_uniform()` takes no representation argument, so it re-ran `E1` in
neither module. `A7` had earlier caught the first draft building the `ω₁₃ = −1` module
against C125's certified `+1`; that failure is preserved in the check's detail string.)*

**Two checks were DELETED for being unfailable**, per the round's own discipline: `C2`
(`abs(1.5*(2/ρ)² − 6/ρ²) < TOL` is `6 = 6`) and `H4`. **Recorded limitation:** the AST
self-audit does **not** catch the `C2` shape — `abs(x) < TOL` is a `Compare` node, not an
`ast.Constant`.

---

## 7. C134 §8's non-transfer claim — verified, not assumed

`[VERIFIED-tool, G1-G5]` **Both skeptic passes call this the round's strongest section.**

| object | result |
|---|---|
| C134's **bilinear** `P_L Γ⁰Ω₃ P_L`, `P_R Γ⁰Ω₃ P_R` | **`= 0`** exactly (`G1`) |
| this round's **linear operator** `P_L Ω₃ P_L`, `P_R Ω₃ P_R` | **`≠ 0`** (`G2`) |
| reason | `Ω₃` **commutes** with `γ₅` (`G3`); `Γ⁰` **anticommutes** (`G4`) |

The vanishing C134 found comes entirely from the `Γ⁰` insertion of the Dirac adjoint,
which a linear-in-spinor constraint does not have. The `S³` torsion 2-forms likewise
preserve 4D chirality (`G5`). **C134's chirality-flip kill genuinely cannot fire here** —
this round dies of a different cause.

## 7b. The algebraic half, which §4/§5 did NOT impose

Agricola 2002 §4.1 `[CITED]` gives four equations; with constant dilaton,
`Ric^∇ = 0`, `δT = 0`, `∇ψ = 0`, `T·ψ = 0`. §4/§5 impose only the third.

`[VERIFIED-tool, I1]` `Ω₃ ε = χ₄·χ₆·ε` exactly, so
`T₃·ε = (2(2t−1)/ρ₃)·χ₄·χ₆·ε`, **zero iff `t = 1/2`** (`I2`, 41-point grid). With the
`S⁶` torsion off this **reproduces C134's kill from a different direction**; it is **also
channel-blind** (`I3`). With `T₆` restored it becomes a `t`–`S⁶` relation — a genuine
cross-factor `t`-selection candidate (Relaxation Map `V3`). **`c₆` is `[UNKNOWN]` and is
deliberately not invented.**

**Agricola's Theorem 4.1** (via Alexandrov/Friedrich–Ivanov): on a **compact** manifold
all four force `T = 0`. `M₁₃` is not compact and `S⁶`'s `Ric^∇ ≠ 0`, so **its hypotheses
are not met** — recorded as context, `[CITED]`, explicitly **not applied**.

---

## 8. Assumptions this round introduces — six, named

1. **A `Spin(1,12)` module on `M₁₃`** (see MANDATORY FIRST MOVE). §2's theorem does not
   depend on which module (`H1`-`H3`).
2. **A factorised ansatz** `ε = ε₄⊗η₃⊗η₆` with `ε₄`,`η₆` chirality eigenstates.
   Non-factorised solution sets are not enumerated.
3. **A block-diagonal, isometry-invariant `A`** — now an explicit *hypothesis* of §2's
   theorem, with the `SU(3)`-on-`ℝ⁶` Schur argument supplied and `J1` showing what
   happens without it.
4. **`T^t = 2(2t−1)ε` at unit radius**, from C125 §2a; C125's own `[INFERRED]` downgrade
   is carried, and §3's `ρ₃`-dependence makes it explicit.
5. **Factor-wise torsion legs** (no mixed `H`) — §2's other hypothesis, and `V1`.
6. **The `S⁶` side is used only by citation** — `χ₆ = +1` and the channel count 3, from
   L5/G74B/G73. The twisted `S⁶` operator was **not** built. **And `sign(ind)=+1` is
   itself `CONDITIONAL`** per `SPIN13_TO_SPIN4_DECOMPOSITION.md` item 3, which this round
   carries rather than silently upgrading (skeptic finding).

---

## 9. Verification

`c136_joint_killing_spinor_check.py` — **57 boolean checks from 57 call sites, 0
failures** (counts now reconcile exactly; `C2`, the only multi-firing site, is deleted).
**23 recorded data values** kept in a separate `DATA` dict, not counted as checks. An
**AST self-audit** runs at the start of `section_A` (not at import — first draft said
otherwise) and refuses to start if any `check()` is passed a literal constant. `ruff`
clean.

**Certified project constants independently rebuilt** `[VERIFIED-tool]`: all 169
`Cl(1,12)` anticommutators (worst residual `0.0`); `ω₁₃ = +1` (C125 E3 — *and it caught a
real error*); `Ω₃Ω₆ = iγ₅` (C125 D4, **with C125's downgrade carried**); `Ω₃ = γ₅⊗1₂⊗Γ₇`
(C134 §5a); `ω₃ = +1` scalar (C125 §4); AHL2023's `1/2` (derived, `C7`); round72 H1b
(`C5`/`C6`); **C64's `3t` and round67/C107's `3t−3` (`C8`/`C9`)**.

**Checks that are reproductions or bookkeeping, not independent evidence** (skeptic
finding, accepted): `D1` duplicates `B3`; `E4` re-substitutes `D2`'s own law; `F5`'s name
asserts more than its boolean tests; the `(1,2)`/`(2,1)` labels are cited strings.

---

## 10. Kill Analysis (Anti-Overfitting Gate)

**What this round KILLS.** `P14` is **FALSE** on kill-branch **(b)** under
{factor-wise torsion} ∪ {`S⁶` inputs identical, E-L3B} ∪ {`χ₆` constant, L5} ∪
{`ε` factorised} ∪ {block-diagonal `A`}. **Tier: `[RESTATEMENT]`** — see `F7`.

**What this round does NOT kill.** `P4`, `P5`, `P13`, `P1`/`P3`/`P6`-`P12` — untouched.
**`P5` is specifically unaffected**: it introduces structure *outside* the `S⁶` frame
bundle, which is what `J2` shows would break the whole picture. Round72 H1b/H1c/H3; C38;
C64; round98's `INCONCLUSIVE`; `N_gen = 3`'s CONDITIONAL status,
`lambda = FREE_COUPLING_PARAMETER`, `sm_derivation_claimed = False`,
`safe_for_runtime = False`.

**Relaxation Map** (one assumption per variant; none attempted):

| variant | changed assumption | status / kill criterion |
|---|---|---|
| **`V1`** | **Mixed-leg torsion** `H_{amn}` | §2 hypothesis 5 fails; a full `Cl(6)` element enters the `S³` equation. Must break `G₂` to distinguish channels (E-L3B) → row 37's cost. **Most informative surviving variant.** Requires a new field. |
| **`V2`** | Non-scalar `A₃` | **CLOSED.** AHL2023 §6 (II): the round `S³ = SU(2)` admits *"no invariant generalized Killing spinors"* — exactly a non-scalar symmetric `A`. `[CITED, verified in full this round]` |
| **`V2b`** | **Off-block `A_{ia}`** (non-`G₂`-invariant `A`) | **NEW, from `J1`.** Lifts the bandwidth restriction entirely; route (b), row 37's cost. Not swept. |
| **`V3`** | Impose the algebraic half with `T₆` on | §7b: becomes a `t`–`S⁶` relation. Needs `c₆`, currently `[UNKNOWN]`. Still channel-blind. |
| **`V4`** | Curved `M₄` (AdS₄), `λ ≠ 0` | Removes `D4`'s forcing; gives single-`t` selection but still channel-blind, so it belongs to H1c, not the pairing line. Listed so it is not mistaken for a rescue. |
| **`V5`** | Non-factorised `ε` | Linearity makes the constraint act termwise on each factorised summand, so no *new* solutions arise from superposition; a genuinely entangled `ε` is not covered and is not swept. |
| **`V6`** | **Pose the constraint on `S(M₁₃)⊗E`** rather than the untwisted bundle | **NEW, skeptic finding.** The channel label lives on `E`, and the constraint as posed has no slot for it. The `S⁶` equation would gain `1⊗∇^E`; by E-L3B the three `(E,∇^E)` are isomorphic *with identical connections*, so it is expected inert — **but that is a one-line argument now made explicitly, where the first draft simply omitted the variant.** |

---

## 11. Gate fields

| field | status after C136 |
|---|---|
| **F4** | **FAILS** for `P14`. Add to C132 §1c: *joint generalized-Killing-spinor constraint on the frozen product → channel-uniform; and the conclusion is one-line derivable from E-L3B + L5 (C136)*. |
| **F6** | **not assessed.** A Killing-spinor constraint is not an action and supplies no EOM. |
| F1, F2, F3, F5, F7 | untouched / N/A. |

**Round72 E8 gate: not opened.** E8 governs bosonic `F(t) = a|R^t|² + b|T^t|²` and its
stationarity in `t`. This round poses no action and extremises nothing, so E8 does not
apply — and, unlike C134, this round claims **no** distinction from E8 as a positive
result, and no F4/F6 credit needing E8's clearance.

---

## 12. What this round does NOT show

* Does **not** claim the constraint derives from a 13D supergravity — none exists here.
* Does **not** claim the kill is independent evidence — `F7` says it is a restatement.
* Does **not** claim the parity theorem is a fact about *this* background (`F3`), nor
  that it holds without block-diagonal `A` (`J1`).
* Does **not** claim a `Z₂`-vs-`Z₃` obstruction — **withdrawn** (`E5`, `J2`).
* Does **not** claim a new `t`-selection: reading (i) restates H1b (`F5`), reading (ii)
  has none (`E4`).
* Does **not** re-present `Ω₃Ω₆ = iγ₅` as fresh — C125's downgrade is carried.
* Does **not** compute the `S⁶` solution space (`[UNKNOWN]`).
* Does **not** reopen C123–C135, round98, or round86.
* Does **not** rule out `P4`, `P5`, `P13`, or `V1`-`V6`.
* Does **not** change `N_gen = 3`'s CONDITIONAL status,
  `lambda = FREE_COUPLING_PARAMETER`, `sm_derivation_claimed = False`, or
  `safe_for_runtime = False`. Does **not** close H1c, OB1, or round95's gap.
* Does **not** solicit Tom Lawrence's Part 5.

---

## 13. Registry actions — NOT performed by this round, proposed only

This round does not edit `PARENT_ACTION_GATE.md`, `OPEN_BLOCKERS.md`,
`null_results/INDEX.md`, or `pearl_registry/INDEX.md`. Proposed:

* `null_results/` entry for `P14`: REJECT, kill-branch (b), **tier `[RESTATEMENT]`**,
  with the F7 note so a future round does not cite it as independent evidence.
* C132 §1c "already tried": the F4 row above.
* **Pearl-Gate entry as first drafted is WITHDRAWN** — the proposed pre-filter is covered
  by G44-B1, GAP-4, Round81 and rows 22/36 (skeptic finding, verified against all five),
  and its bandwidth form is refuted (§5b).
* **Pearl (replacement, narrower and about the counterexamples).** *observation:* on a
  strict product, a first-order spinorial constraint's cross-factor content depends on
  hypotheses that are easy to leave unstated — an off-block symmetric `A` (`J1`) or
  channel-dependent data entering through a shared scalar (`J2`) each restore arbitrary
  coupling. *falsifiable_prediction:* any future no-go of the form *"structure X cannot
  cross the `S³`/`S⁶` split"* that does not state its `A`-block and shared-scalar
  hypotheses will admit one of these two counterexamples. *impact_score:* 5.
  *trigger_condition:* the next cross-factor no-go proposed for this split.
  *next_check:* at the next F4 pairing attempt.
* **Pearl (methodology, and this one is the round's real lesson).** A round can build a
  correct trap-detector for a *past* failure and then fail to point it at its own
  headline. C136's `F5` audited a sub-result for one-line derivability and passed; its
  **conclusion** was one-line derivable from a cited corollary and nobody checked until
  two independent skeptic passes did. *falsifiable_prediction:* over the next 5
  Full-Ladder rounds, explicitly running the round's own restatement test against its own
  verdict string (not just its sub-results) will reclassify ≥1 headline.
  *impact_score:* 7. *next_check:* after 5 more Full-Ladder rounds.
* **Pearl (Caveat Gate).** `V1` names a specific untested alternative — mixed-leg
  torsion, the only frozen-background escape from §2's theorem. *impact_score:* 6.
  *next_check:* whenever a flux candidate with legs on both compact factors is picked up.

---

## 14. FL Step 8a — skeptic passes

**Two independent context-blind passes, both `[FALSIFIED]`, in agreement.** Full record,
all findings and dispositions: `skeptic_verdict.md`. Because the two agree, the
Paraphrase-Sensitivity Probe's disagreement branch does not fire.

Per the FL Response Matrix, `[FALSIFIED]` means *"specific concerns needing a response"*,
not a kill. Ten major/critical concerns were **all** responded to: three by **repairing
the code** (`E1`/`F4` made falsifiable; `F7` added), two by **deleting unfailable checks**
(`C2`, `H4`), two by **withdrawing arguments outright** (the bandwidth claim; the Pearl),
two by **adding counterexamples** (`J1`, `J2`), and one by **retiering the verdict**.
**Nothing was dismissed.** The `P14` conclusion survives; its evidence tier does not.

---

## Check

* Every prior-art status was read from the **primary this session**, including the five
  sources the skeptics named as covering the withdrawn Pearl.
* The MANDATORY FIRST MOVE was stated before any computation, its two halves
  dispositioned separately.
* The Zero-Signal Gate ran before the script was written.
* The round114 trap was checked **automatically**, and — after the skeptic passes — the
  *correct* round114 criterion (`F7`) was applied **to this round's own conclusion**,
  which it fails. That is recorded as the verdict, not as a caveat.
* Three checks **failed or were found unfailable during construction and were diagnosed,
  not tuned away**: `A7` (wrong `Cl(1,12)` module), `C2` and `H4` (deleted).
* The permitted kill was reported as a kill; no positive result was forced; neither
  `BLOCKED` branch was invoked where a computation was available.

---

## Evidence tier of the central conclusion

**Central conclusion:** *a joint generalized-Killing-spinor constraint on the frozen
`M₄×S³×S⁶` background — posed geometrically, with no supergravity import — has a solution
set identical across all three `S⁶` triality channels. `P14` is killed on kill-branch (b).*

**Tier of the mathematics: `[VERIFIED-tool]`, confidence HIGH.** 57 checks, 0 failures,
AST self-audit, exact operator identities rather than samples, representation-independent
under 10 `GL(64,ℂ)` similarities and 5 `Cl(6)` basis changes, identical in both
inequivalent `Cl(1,12)` modules, eight certified project constants independently rebuilt.

**Tier of the KILL: `[RESTATEMENT]` — `[CITED]` inputs + `[INFERRED]` one-line step,
confidence HIGH in the conclusion, LOW in its novelty.** Check `F7`, applying round114's
own criterion, returns `True`: the conclusion follows from E-L3B's Corollary plus L5 with
nothing this round computed, and four prior in-repo results say the same thing. **This is
the round's honest headline and it should be cited this way, not as independent evidence.**

**Tier of §3 (`∇^t` law): `[VERIFIED-tool]`, confidence HIGH** — and independently
corroborated against C64, round67/C107, AHL2023 and round111. But it is a
**reproduction**, not a new result.

**Tier of §7 (C134 route-2 non-transfer): `[VERIFIED-tool]`, confidence HIGH — and this
is the round's strongest genuinely new content.** Both skeptic passes re-ran it and
confirmed it. C134 §8's assertion is now verified rather than assumed.

**Tier of §2 (parity theorem): `[VERIFIED-tool]` that it is true *under its repaired
hypotheses*, `[GENERIC]` in scope (`F3`), and its `S³` half is inherited from round67 /
C125 / Round81.** The bandwidth count built on it is **withdrawn**.

**Tier of §J (counterexamples): `[VERIFIED-tool]`, confidence HIGH** — and they are, with
§7, the round's real positive deliverable: they price two hypotheses that any future
cross-factor no-go on this split will need to state.

**Marker on the whole round: `[WEAK]`**, per the FL Response Matrix — two independent
skeptic passes returned `[FALSIFIED]`, every concern was responded to rather than
dismissed, and the surviving conclusion is a restatement of prior art rather than new
evidence.
