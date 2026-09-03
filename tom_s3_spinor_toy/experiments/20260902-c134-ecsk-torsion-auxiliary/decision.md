# C134 — Decision (convergent-mode, FL Full-Ladder)

**Date:** 2026-09-02
**Experiment:** `20260902-c134-ecsk-torsion-auxiliary`
**Question type (EstimandOps L0):** Descriptive — existence of a fixed point.
**Script:** `c134_ecsk_torsion_check.py` · **Results:** `results_c134.json`
**Skeptic record:** `skeptic_verdict.md` (two independent context-blind passes)

**Revision note.** This file was rewritten after two FL Step 8a skeptic passes
(both `WEAKENED`). Every correction they forced is listed with its disposition
in `skeptic_verdict.md`. Three of their findings changed the verdict itself:
**F6 was downgraded `PASS → PARTIAL`**, **E8 criterion 6 was rescored
`PASS → FAIL`**, and the claim that ECSK poses a different question from
round72's E8 preliminary was **substantially retracted**. The central kill
survives both passes and is *stronger* than the first draft claimed.

## Verdict

```text
KILL_BRANCH_A_FIRES__SOURCE_VANISHES__t_FORCED_TO_ONE_HALF
  __KILL_IS_STRONGER_THAN_NON_SELECTION__ECSK_IN_VACUUM_FORCES_T_EQUALS_0_FOR_EVERY_t
  __SO_THE_NABLA_t_ANSATZ_IS_INCONSISTENT_WITH_ECSK_FOR_ALL_t_NOT_EQUAL_HALF
  __ROUTE2_IS_AN_EXACT_REPRESENTATION_INDEPENDENT_OPERATOR_IDENTITY
  __POSITIVE_CONTROL_PASSES__REPRODUCES_MINUS_3_KAPPA_OVER_16_AND_CARTAN_RELATION
  __NEGATIVE_CONTROL_PASSES_BUT_ONLY_IN_THE_4D_DIRAC_REGIME__RESCOPED
  __SCOPING_HOLDS_ONLY_IN_THE_4D_DIRAC_REGIME_AND_NEEDS_EQUAL_DOUBLET_OCCUPANCY
  __F6_PARTIAL_NOT_PASS__TORSION_EOM_DERIVED_BUT_VIELBEIN_EOM_NOT__AND_BACKGROUND_VIOLATES_IT
  __F4_FAILS__E8_FAIL_CRITERIA_t_EQUALS_HALF_AND_t_SWAP_SYMMETRY_BOTH_FIRE
  __ECSK_BOSONIC_SECTOR_IS_ROUND72_E8_AT_a_EQUALS_0__NOVELTY_RETRACTED
  __CLAIM_SIGN_PREDICATE_FALSIFIED_ON_ITS_OWN_TERMS
  __ASSUMPTIONS_INTRODUCED_FIVE_NAMED_NOT_ONE
```

**One line:** the ECSK torsion equation for this background is real, derived,
and checkable — and it says the torsion is **zero**, hence `t = 1/2`. `P2` is
killed on kill-branch (a). The round's positive deliverable is the *torsion*
half of an F6 EOM, which is `PARTIAL`, not a pass.

---

## Prior Result Gate — opened against round72's **LIVE** E8 gate

`claim.md` requires this be verified directly against the primary, not against
any paraphrase (this one included). Done `[VERIFIED-tool, read this session]`.

Round72's `decision.md` contains four status tables. Line 123 reads verbatim
`## Final summary table (supersedes the earlier one above)`.

* The **unambiguous** live statement is that Final summary table, line 132:
  *"Equations of motion selecting t=0/1 (H2, E8 preliminary):
  **BLOCKED/UNDERDETERMINED**."*
* The **superseded** content is the pre-recomposition pair: line 231
  *"**Not tested. Explicitly out of scope.**"* and line 310
  *"OPEN — not attempted, out of scope"*. This is the row C132's first draft
  quoted (C132 `decision.md:333-334`, §7 finding 9).
* **Ambiguity, stated rather than resolved by assertion** (skeptic finding
  B19): round72's own phrase *"the earlier one above"* is ambiguous — the only
  table physically above line 123 is the `## Updated verdict table` at line 78,
  whose H2 row (line 85) says the *same* thing as the final table
  (`OPEN, now sharpened … BLOCKED/UNDERDETERMINED as currently posable`).
  The first draft asserted line 85 as LIVE, which is not safely derivable.
  **Both readings give the same operative status**, so this round's opening
  position is unaffected.

**Round72's adverse preliminary**, re-derived by round72 itself in sympy
(`decision.md:69-76`): for `F(t)=a|R^t|²+b|T^t|²`,
`F'(t)=2(2t−1)[aA·t(t−1)+2bB]`; `t=1/2` is always stationary, `t=0,1` only if
`b=0`.

**Round72's FAIL criteria are FIVE, not four** `[VERIFIED-tool, round72
decision.md:118-121]` — the first draft dropped one, and the dropped one fires
(see below).

### Is ECSK a different question from E8's preliminary? — **substantially NO**

The first draft claimed `[VERIFIED] Yes, structurally`. **Retracted**, per
skeptic finding B8, verified by machine check:

ECSK's gravitational sector is `(1/2κ)R(Γ) = (1/2κ)[R(g) − ¼|T|²]`. `R(g)` is
`t`-independent, so its **entire** `t`-dependence is `−(1/8κ)|T^t|²` — which is
**exactly E8's `F(t)` at `a = 0`**, the case round72 computed in July 2026.
Machine-checked: that functional is **even** in `(2t−1)` to `10⁻¹⁰` and its
unique stationary point is `t = 0.5000`.

**What survives of the distinction, and it is the round's real content:** the
*fermionic* term `T·B` is genuinely outside E8's `F(t)` — it is **linear** in
torsion and **odd** in `(2t−1)`, so it could in principle have broken the
symmetry E8's bosonic functional cannot. That is the one new ingredient, and
**this round's result is that it vanishes**. So: same answer as E8, and once
the fermion source is gone, the same reason too.

## Other prior art checked

* **round111** `decision.md:105` Relaxation Map row 1 — *"Derive `α` … from an
  actual physical action | Requires committing to a specific action principle
  (Einstein-Cartan, …)"*. **Answered conditionally, not derived** (skeptic
  finding B21). Round111 pre-empted exactly this at `decision.md:53-64`: an
  Einstein–Cartan action treats the two pieces as *"SEPARATE terms with
  INDEPENDENTLY-determined coefficients"*, and the torsionful Ricci scalar
  *"happens to correspond to one SPECIFIC choice of `α`"*. ECSK's `(1/2κ)R(Γ)`
  **is** that specific choice. ECSK fixes `α` once chosen; choosing ECSK is the
  choice of `α`.
  **But round111 also supplies a free, independent cross-check this round now
  uses** `[VERIFIED-tool]`: with C125's `T_abc = 2(2t−1)ε_abc`,
  `|T|² = 24(2t−1)²`, so `R(Γ) = 6 − 6(2t−1)² = 24t(1−t)` — **identical** to
  round111's independently derived `Scal(t)`. That confirms the `−1/4`
  coefficient of §2 step 1 against a result computed in this project two months
  earlier by a different route.
* **round75/E11 Q2** — still `OPEN`; *"zero wiring exists in `preprint.tex`"*
  between flux and any torsion object `[CITED]`. Unchanged: this round wires
  torsion to a **fermion bilinear**, not to flux.
* **C124** `decision.md:527-528`, verbatim `[VERIFIED-tool]` — under
  *"### What this round does NOT kill"*: *"**Higher-derivative invariants**
  (explicit `D^k R` beyond Bianchi-reducible ones) and **fermion-bilinear
  terms**."* **This round lives entirely inside that carve-out.** (The first
  draft cited `542-550`, which is C124's Relaxation Map — corrected, skeptic
  finding B20.)
* **C125 §0a/2a** — `T^t(X_i,X_j) = 2(2t−1)ε_{ijk}X_k`, *"a constant multiple
  of the volume tensor"* `[CITED]`.
* **C125 §4** — `Ω₃·Ω₆ = i·γ₅` `[CITED]`, reproduced independently here (§7).
  C125's own downgrade of that identity (*"not a discovery about the `S³/S⁶`
  split … forced in every irrep of `Cl(1,12)`"*) is carried forward, not
  dropped.
* **Pre-filters** `O1`, `O3`, `O5` (C128's framing correction respected — no
  gauge sector enters), `O6`, `O7`. **All cleared.**

---

## 1. Zero-Signal Gate (FL Step −5) — run before any computation

| field | content |
|---|---|
| Entity | the ECSK torsion field equation on `M₄×S³×S⁶`, restricted to the `S³` legs, sourced by the certified `S⁶`-twisted zero modes |
| Falsifiable predicate | that equation has a solution with `2t−1 ≠ 0` whose sign is fixed by L5's `sign(ind)=+1` |
| Measurable outcome | the explicit source bilinear, the explicit equation, and its complete solution set |

All three fillable ⇒ **gate PASSES**. (Not `REFUSE`.)

## 2. The action and its equations of motion

```
S = (1/2κ₁₃) ∫ e R(e, ω)  +  (i/2) ∫ e (ψ̄ Γ^M D_M ψ − h.c.)
```

on `M₄×S³×S⁶`, `ω` varied independently of the vielbein.

**Torsion (connection) EOM**, dimension-independent, machine-checked:

0. *Stated step, not an opening assumption* (skeptic finding B22): the Palatini
   variation runs over all torsion components; the trace and tensor parts
   decouple because a minimally-coupled Dirac field sources neither. Only the
   totally antisymmetric sector is retained below, for that reason.
1. For totally antisymmetric `T_{ABC}` the contorsion is `K = T/2`, all
   contorsion traces vanish, and `R(Γ) = R(g) − (1/4)|T|²` up to total
   divergences. **Independently confirmed against round111** (above).
2. The connection enters the Dirac Lagrangian only as
   `(i/4) ω_{Mab} ψ̄Γ^{Mab}ψ`, because `{Γ^M, Γ^{ab}} = 2Γ^{Mab}`
   `[VERIFIED-tool: all 2028 ordered 13D triples and 48 in 4D]`. This is why
   the Dirac spin current is totally antisymmetric in **any** dimension — and
   hence why the `∇^t` ansatz's own torsion shape is the one ECSK produces.
3. `L(T) = −(1/8κ₁₃)|T|² + (1/8) T·B`, with `B^{ABC} := i ψ̄Γ^{ABC}ψ` (real).
4. Stationarity in `T` (algebraic — torsion is auxiliary):

```
   T^{ABC} = (κ₁₃/2) · B^{ABC} = (κ₁₃/2) · i ψ̄Γ^{ABC}ψ
```

**Vielbein (metric) EOM — NOT derived here, and the background violates it.**
`[VERIFIED-tool; skeptic finding B7, the heaviest of the round]` The same
action has a second field equation, `R_{MN} − ½g_{MN}R = κ₁₃ T_{MN}`. In
vacuum (§5b route 1) the RHS vanishes and the torsion EOM gives `T = 0`, so the
requirement is `Ric(g) = 0` on `M₄×S³×S⁶`. This project's certified Ricci is
`0 ⊕ (2/ρ₃²)g₃ ⊕ (5/ρ₆²)g₆` (C125 `decision.md:335`) — **manifestly non-zero.**
**The frozen background is not a solution of the action this round names.**
This is why F6 is `PARTIAL` and not `PASS` (§9), and it is also why E8's
criterion 5 is scored FAIL.

## 3. MANDATORY POSITIVE CONTROL — flat-space ECSK: **PASSED**

Literature retrieved and read **this session**, two independent primaries:

* `[CITED, primary]` **Popławski, arXiv:1102.5667** (Gen. Rel. Grav. **44**
  (2012) 491), LaTeX source read directly. The Dirac spin tensor is
  `s^{ijk} = ½ e^{ijkl}A_l` with `A^k = ψ̄γ⁵γ^kψ` the **axial** current; the
  Hehl–Datta equation is `iγ^kψ_{:k} = mψ − (3κ/8)A_kγ⁵γ^kψ`; the effective
  Lagrangian carries `(3κ/16)(γ²/(γ²+1))A_kA^k`. Also verbatim, and decisive
  for §5b: *"since the ECSK torsion tensor is proportional to the spin density
  of matter, **it vanishes in vacuum**."*
* `[CITED, primary]` **Perez & Rovelli, arXiv:gr-qc/0505081** (Phys. Rev. D
  **73** (2006) 044013), LaTeX source read directly:
  `S_int = −(3/2)πG (γ²/(γ²+1)) ∫ e (ψ̄γ₅γ_Aψ)(ψ̄γ₅γ^Aψ)`, with *"In the limit
  `γ→∞`, we recover the standard coupling of the Einstein-Cartan theory."*
  They also note the **vector** current cancels against its complex conjugate.

**Reproduction:**

| quantity | this round | literature | match |
|---|---|---|---|
| `γ^{[ABC]}` in 4D | `= −i ε^{ABCD}γ₅γ_D`, all 4 triples, exact | Perez–Rovelli's stated identity | ✓ `[VERIFIED-tool]` |
| spin current is dual to the **axial** current only | `B^{ABC} = ε^{ABCD}A_D` on 50 random spinors, with the vector current verified non-zero so the statement is not vacuous | Popławski `s^{ijk}=½e^{ijkl}A_l`; Perez–Rovelli's cancellation | ✓ `[VERIFIED-tool]` |
| `ε^{ABCD}ε_{ABCE}` | `−6 δ^D_E` | standard, mostly-minus | ✓ `[VERIFIED-tool]` |
| Cartan relation | `T^{ABC} = (κ/2)B^{ABC}` | Popławski (Car4) at `α=0,γ→∞`, with `T=2S`: `κ/2` | ✓ **magnitude** `[DERIVED, hand-entered constants]` |
| four-fermion term | `L* = −(3κ/16) A·A` | Perez–Rovelli `−(3/2)πG` with `κ=8πG` | ✓ **exactly, sign included** `[DERIVED]` |
| | | Popławski `3κ/16` | ✓ **magnitude only** — he writes the gravitational term as `−R√−g/(2κ)`, the opposite sign to the `+(1/2κ)R` used here, so his overall sign is not directly comparable (skeptic finding B10; the first draft wrongly wrote "✓ exactly, both") |

**Why two anchors:** the `−3/16` match alone constrains only the combination
`b²/a`; Popławski's Cartan relation pins the ratio `b/2a` separately. Both
land. **Honest limitation** (skeptic findings B2, B10): the two gravity/Dirac
coefficients are **hand-entered constants** in the script — the arithmetic on
them is machine-checked, the constants themselves are hand-derived, and are
independently corroborated by the round111 cross-check in §2 rather than by the
script's own arithmetic. Marked `[DERIVED]`, not `[VERIFIED-tool]`.

## 4. Scoping — holds, but in the 4D-Dirac regime only, and with a condition

`claim.md` names silent scope growth as the most likely failure mode. It did
not occur in the sense claim.md meant (no `S⁶` torsion dynamics were needed),
but the first draft's statement was too strong on two counts, both found by the
skeptic passes and both now machine-checked.

The torsion EOM fixes **every** `T_{ABC}`, not just the `S³` ones. Checked over
all 84 internal 3-index components on the certified content `[VERIFIED-tool]`:

| component class | count | 4D-Dirac regime | 4D-Weyl regime |
|---|---|---|---|
| 3 × `S³` | 1 | **non-zero** | `0` |
| 2 × `S³` + 1 × `S⁶` | 18 | `0` | `0` |
| 1 × `S³` + 2 × `S⁶` | 45 | `0` | `0` |
| 3 × `S⁶` | 20 | `0` | `0` |

**Limitation 1 — regime (skeptic finding B5).** The sweep is meaningful only in
the **4D-Dirac** reading. In the 4D-**Weyl** reading — the one `N_gen=3`
physically requires — *all 84* components vanish (max `8.8×10⁻¹⁶`), so the
isolation statement is vacuous (`0 = 0`) exactly where the conclusion is drawn.
The first draft disclosed this regime problem for the negative control but not
for the scoping; that asymmetry was a real defect and is corrected here.

**Limitation 2 — a hidden condition (skeptic finding B6).** The
`1×S³+2×S⁶` class vanishes only after summing, via
`Σ_s η₃ₛ†σ_a η₃ₛ = tr σ_a = 0`. That needs **not only** doublet completeness
(C64 multiplicity 2; C125 `ker(D_{S³},t=0)=(1,2)`) **but also equal 4D
occupancy across the two doublet members** — which C64/C125 do not supply.
Machine-checked: with unequal occupancy the class is **non-zero** (max `4.63`).

**What is unconditional:** the `2×S³+1×S⁶` and `3×S⁶` classes vanish *per mode*,
because an odd number of `S⁶` gammas anticommutes with `Γ₇` and the certified
`S⁶` content is a `Γ₇`-eigenstate. Components with a free `M₄` index are killed
by 4D Lorentz invariance.

**Internal control** `[VERIFIED-tool]`: truncating the `S³` doublet to one
spinor makes the mixed class non-zero (`6.62`), so the check is discriminating
and not degenerate. Re-run with an independent 4D spinor per `S⁶` channel:
identical verdict.

## 5. The computation, and the kill

### 5a. What sources the `S³` torsion

`[VERIFIED-tool, exact]`

```
Γ^{[abc]}|_{S³}  =  ε_{abc} · Ω₃ ,      Ω₃ := Γ⁴Γ⁵Γ⁶  =  γ₅ ⊗ 1₂ ⊗ Γ₇
```

so the `S³`-leg torsion equation is

```
2(2t−1)·ε_{abc}  =  (κ₁₃/2)·ε_{abc}·J ,      J := i⟨ψ̄ (γ₅ ⊗ 1₂ ⊗ Γ₇) ψ⟩
⇒   2t − 1  =  (κ₁₃/4) · J
            =  (κ₁₃/4) · ⟨ψ̄₄ γ₅ ψ₄⟩ · ‖η₃‖² · (S⁶ chirality)
```

1. **It has zero `S³` content.** `Ω₃` is built from the 4D and `S⁶`
   chiralities alone — consistent with C125's finding that the *intrinsic*
   `S³` volume element is a scalar (`ω₃ = +1` in this repo's `Cl(0,3)`
   convention; the script cross-checked the `Cl(3,0)` value `i·1₂` — skeptic
   finding B16, conclusion unchanged). This is the `S⁶`↔`S³` pairing round95
   records as missing, exhibited structurally — while carrying forward C125's
   own downgrade that the underlying identity is forced in every `Cl(1,12)`
   irrep and is not a discovery about the split.
2. **Kill-branch (b) does NOT fire.** *Corrected justification* (skeptic
   finding B3): the first draft argued from linearity in `t`, which silently
   assumes `J` is `t`-independent — and it is not, since the zero-mode content
   is `t`-dependent (E2 crossings at `t∈{0,1}`; KT-8: none at `t=1/2`). The
   correct argument, valid for **any** `J(t)`: the LHS `2(2t−1)` is not
   identically zero, so the equation is never satisfied for every `t`.
   Machine-checked with an explicitly `t`-dependent `J(t)`.
3. **Kill-branch (c) is not manufactured.** `J = 0 ⇒ t = 1/2` is always a
   solution, as `claim.md` said. No "no solution" claim is made anywhere.

### 5b. Kill-branch (a) fires — three independent routes

**Route 1 — vacuum. `[CITED, primary + VERIFIED]`** In ECSK torsion is not a
degree of freedom; it is algebraically zero wherever the spin density is zero
(Popławski, verbatim, §3). This project's background is a vacuum
configuration — **no fermion condensate is specified anywhere in this project**.
`⟨ψ̄γ₅ψ⟩ = 0 ⇒ J = 0 ⇒ t = 1/2`, the Levi-Civita point.

**Route 2 — chirality. `[VERIFIED-tool, EXACT]`** `Ω₃` commutes with `γ₅` while
`Γ⁰` anticommutes with it, so `ψ̄Ω₃ψ` is a **4D-chirality-flipping**
(mass-type) bilinear. This is an **exact operator identity**, not a sample:
`P_L Γ⁰ Ω₃ P_L = P_R Γ⁰ Ω₃ P_R = 0` identically as `64×64` matrices. It is
**representation-independent**: verified under 20 random unitary changes of
gamma representation (worst residual `3×10⁻¹⁶`) and 20 general
`GL(64,ℂ)` similarities with the correctly transformed Dirac adjoint
`A = (S†)⁻¹Γ⁰S⁻¹` (worst relative residual `6×10⁻¹⁵`). Structural reason: any
representation with `Γ^μ = γ^μ⊗1` forces `Γ^{internal} ∝ γ₅⊗e_M`, so `Ω₃`
carries `γ₅` to an odd power and always commutes with it.
**The chirality that `P2` hoped would fix the torsion's sign is precisely what
makes the source vanish**, and 4D-chiral content is what `N_gen=3` requires.
**Route 2 does not depend on §6's contested assumption** (skeptic finding B12):
it is `Cl(1,3)⊗Cl(9)` product-module algebra, which the project *does* have.

**Route 3 — magnitude. `[VERIFIED]`** Even postulating a 4D pseudoscalar
condensate, `2t−1 = (κ₁₃/4)J` varies continuously with it. `t ∈ {0,1}` requires
`|κ₁₃J| = 4` exactly (unit-radius `S³`) — the condensate tuned to the 13D
Cartan density. Fine-tuning, not selection.

### 5c. The kill is stronger than "fails to select" (skeptic finding B14)

In vacuum ECSK forces `T = 0` — i.e. `T^t = 2(2t−1)ε ≠ 0` is inconsistent for
**every** `t ≠ 1/2`, not merely unselected. So **ECSK is incompatible with this
project's entire `∇^t` torsion ansatz**, and the one configuration it does
permit (`t=1/2`) has **no zero modes at all** by KT-8: self-consistent and
phenomenologically empty. The first draft buried this in a Relaxation-Map row.

### 5d. The claim's sign predicate is falsified on its own terms

`claim.md` asserts a solution *"whose SIGN is fixed by L5's `sign(ind)=+1`"*.
`[VERIFIED-tool]` Flipping the `S⁶` chirality flips `J` exactly
(`+39.708 → −39.708`), so the **correlation** is real. But `sign(ind)=+1` enters
as a **positive multiplicative factor**; the absolute sign of `2t−1` is
`sign(⟨ψ̄₄γ₅ψ₄⟩)`, an undetermined 4D pseudoscalar. **L5 fixes a relative
correlation, not the sign.** The claim as worded is false even in its most
favourable reading.

## 6. Assumptions this round introduces — FIVE, named, not one

The first draft named one. Both skeptic passes found more, and the first draft
contradicted its own count in its evidence-tier section. Corrected list:

1. **A `Spin(1,12)` spinor.** An Einstein–Cartan *action* on a 13-manifold
   requires one. The project's own file says, verbatim and in full
   `[VERIFIED-tool, SPIN13_TO_SPIN4_DECOMPOSITION.md:3-16]`: *"the original
   task named this `Spin(1,12)→Spin(1,3)×Spin(3)×Spin(6)`. **This framing is
   not used** — `preprint.tex`'s own 'Total dimension is 13, not 10'
   open-problems entry (line 1375) already caught and corrected exactly this
   conflation… This audit instead covers what the project **actually has**: a
   Kaluza-Klein **product ansatz** … **not a unified higher-D spacetime**"*,
   and *"There is no established `Spin(1,12)` structure group in this project —
   standard supergravity caps at 11D (Nahm's theorem), and no consistent 13D
   parent theory is claimed."*
   **Disposition, both halves** (the first draft quoted only the second
   sentence — skeptic finding B18): the Nahm reason **does not bite**
   `[INFERRED — Nahm classifies supersymmetric supergravities; ECSK is ordinary
   Einstein–Cartan gravity plus a Dirac field, with no supersymmetry, defined in
   every dimension]`. The **other** half does bite, and harder than the first
   draft allowed: the framing was not merely "not yet established", it was
   **tried, identified as a conflation, and retired**. This round supplies it
   anyway, because its own premise forces it. §5b **route 2 does not need it**;
   §4, §5a's factorisation and §5b routes 1 and 3 do.
2. **Equal 4D occupancy across the `S³` doublet** — required for §4's isolation
   (§4 Limitation 2), supplied by neither C64 nor C125.
3. **A common 4D configuration across mirror partners** — required for the
   negative control's cancellation (§7).
4. **The `T_abc = 2(2t−1)ε_abc` normalisation at unit radius**, imported from
   C125. C125's own second skeptic pass downgraded that to `[INFERRED]`; this
   round cites it as `[CITED]` and now carries the downgrade. Route 3's
   `|κ₁₃J| = 4` is a unit-radius statement, not a `ρ₃` one.
5. **No non-fermionic source of torsion** — §4's sweep is run only against the
   fermion bilinear.

Not an assumption but a **gap**: the vielbein EOM (§2), which the background
violates.

## 7. Verification

`c134_ecsk_torsion_check.py` — **53 boolean checks from 53 call sites, 0
failures**, plus **18 recorded data values kept in a separate `DATA` dict and
explicitly not counted as checks**. The first draft reported "52 machine
checks", which conflated 41 booleans with 11 data values and included three
`check(..., True, ...)` calls that could not fail — one of them carrying the
kill-branch (b) determination (skeptic finding B2). All three are replaced by
real computations, and an **AST self-audit** now runs at import and refuses to
start if any `check()` is passed a literal constant.

**Independent reproduction of certified project constants** `[VERIFIED-tool]`:

| certified value | C134's independent rebuild |
|---|---|
| all 169 `Cl(1,12)` anticommutators vs `η=diag(+,−,…,−)` (C125) | ✓ |
| `ω₁₃` central and scalar `= +1` (C125 E3) | ✓ `(1+0j)` |
| `Ω₃·Ω₆ = i·γ₅`, measured `0+1i` (C125 D4) | ✓ `(1j)·γ₅` |
| `Scal(t) = 24t(1−t)` (round111, different route, July 2026) | ✓ recovered from `R(g) − ¼|T|²` — confirms §2's `−1/4` |

**Controls:**

| control | result |
|---|---|
| **Positive (mandatory)** | **PASS** — Perez–Rovelli exactly (sign included); Popławski in magnitude. Two hand-entered constants, corroborated independently by round111. |
| **Negative (mandatory)** | **PASS, re-scoped.** Chiral `→ 39.708`; vector-like `→ 1.8×10⁻¹⁵`; chirality flip `→ −39.708`. |
| Internal — is the scoping check degenerate? | **PASS** — truncating the doublet gives `6.62` ≠ 0. |
| Internal — unequal doublet occupancy | **Class becomes non-zero (`4.63`)** — names §6 assumption 2. |
| Internal — 4D-Weyl scoping sweep | **All 84 components `→ 8.8×10⁻¹⁶`** — names §4 Limitation 1. |
| Internal — independent 4D spinor per mode | **Negative control does NOT cancel (`30.13`)** — names §6 assumption 3. |

**Disclosed limitations of the negative control** (skeptic finding B4). It
discriminates only in the 4D-Dirac reading; in the 4D-Weyl reading the source
already vanishes for chiral *and* vector-like content, so it is
non-discriminating there and is not claimed as evidence in that reading.
Further, the *cancellation* half is an algebraic corollary of the already-passed
factorisation check (`3(+1) + 3(−1) = 0` with a shared 4D spinor), and it
**fails** when each mode carries its own 4D spinor — so what it actually tests
is a vector-like **vacuum**, not merely mirrored content. **The
non-corollary half is the sign-flip test**, which genuinely establishes that the
machinery senses `Γ₇`.

**What was NOT built** (skeptic finding B11): the twisted `S⁶` Dirac operator.
The script uses three basis vectors of the `Γ₇ = +1` eigenspace. Only the
chirality **sign** (`ind = +1`, G73/G74B) and the **channel count** (3) do any
work in the argument — which is sufficient for it, but the first draft's phrase
"evaluated on this project's own certified zero modes" overstated the input.

**Pre-registration deviation, flagged not absorbed** (skeptic finding B15):
`claim.md:167-169` says `S⁶` enters through *"multiplicity (2 per C64)"*. C64's
`2,2,6,6,12,12` are **`S³`** crossing multiplicities; the `S⁶` count is 3
channels × dim 1 (G73/G74B). The round used 3 for `S⁶` and 2 for the `S³`
doublet — i.e. the correct numbers, but not the ones `claim.md` literally
pre-registered.

## 8. Kill Analysis (Anti-Overfitting Gate)

**What this round KILLS.** `P2` is **FALSE**, on kill-branch (a), under the
conjunction {vacuum background} ∪ {4D-chiral content} ∪ {no fine-tuning to the
Cartan density} — any one suffices. The sign sub-predicate is separately false
(§5d). Stronger than the claim asked: ECSK is incompatible with the `∇^t`
ansatz for every `t ≠ 1/2` (§5c).

**What this round does NOT kill.**
* **`P3`** (fermion condensate sourcing torsion). This round **redirects into
  `P3`** and **raises its bar**: `P3` must now supply a *4D-pseudoscalar*
  condensate, reconcile it with 4D chirality (route 2), and explain the
  fine-tuning (route 3) — on top of `pearl_registry` row 32's existing bar.
* **`P14`** (joint 13D generalized-Killing-spinor constraint), untouched. A
  gravitino-type constraint is **linear** in `ψ`, so route 2 does not transfer.
* Round72's **H1b**, **H1c**, **H3**.
* `N_gen=3`'s CONDITIONAL status, `lambda = FREE_COUPLING_PARAMETER`,
  `sm_derivation_claimed = False`, `safe_for_runtime = False`.

**Relaxation Map** (one assumption per variant; **none attempted here**):

| variant | single assumption changed | kill criterion |
|---|---|---|
| V1 | Add a 4D pseudoscalar condensate | Derived, or added to rescue this (AOG-5)? Survives routes 2 and 3? — **this is `P3`** |
| V2 | Non-minimal fermion–torsion coupling (Freidel–Minic–Takeuchi `α`; Holst/Immirzi `γ`) | Both are in the retrieved literature and generate **vector–vector** and **vector–axial** terms alongside axial–axial. Does either produce an internal-torsion source with a 4D-**scalar** or **vector** structure? If so, route 2 does not apply to it. Cheap; not checked here. |
| V3 | Add a bosonic source (`p`-form flux, cosmological term) so the background solves the **metric** EOM | This is what G54/Freund-Rubin already does elsewhere in this project, and §2 shows bare ECSK **needs** it. Distinct from round115's already-NULL flux-selection route: here flux would support the *background*, not select `t`. **The most informative surviving variant.** |
| V4 | Accept `t=1/2` | Contradicts KT-8 — no massless fermions at all. Listed so it is not silently re-tried. |

## 9. Gate fields

| field | status after C134 |
|---|---|
| **F6 — background equations** | **`PARTIAL`, not `PASS`** (downgraded after skeptic finding B7). The **torsion** EOM is genuinely derived and literature-cross-checked — a real advance over C126's `S_YM`, which cleared F6 *"only in the narrow, uninformative sense"*. But F6's own "Must state" is *"what equations of motion the candidate **background**/torsion configuration is required to satisfy"*, and the **metric** EOM is not derived here and is **violated** by the frozen background (`Ric ≠ 0`). `PARENT_ACTION_GATE.md:15-16,545-546`: *"A construction that answers some fields and leaves others as 'not yet supplied' … is accurately `PARTIAL`, and should be logged as such, not rounded up."* Logged as `PARTIAL`. |
| **F4 — `t`-selection** | **FAILS.** Add to C132 §1c's "already tried" table. |
| **F5 — Dirac operator** | Untouched; tension recorded (ECSK's `t=1/2` collides with KT-8) — noting C124 already recorded this collision for a different sector, so it is not newly surfaced. |
| F1, F2, F3 | Reused unchanged. |
| F7 — stability | N/A (algebraic equation, unique root). |

**Round72 E8 gate, scored against all SIX PASS and FIVE FAIL criteria:**

| PASS criterion | ECSK |
|---|---|
| 1 — not built after the fact from `D^tψ=0` | **PASS** |
| 2 — fixed coefficients not tuned to the answer | **PASS with caveat** — `κ₁₃` is untuned, but per round111 the `|T|²` coefficient is *inherited* by choosing ECSK, not derived |
| 3 — `δS/δt = 0` at `t=0` or `1` | **FAIL** |
| 4 — stable extremum | N/A |
| 5 — compatible with background/EOM constraints | **FAIL** — the background violates the metric EOM (§2) |
| 6 — interprets or breaks `t↔1−t` physically | **FAIL** (rescored from the first draft's PASS) — the fermionic term is odd in `(2t−1)`, but its coefficient is zero, leaving a functional that is **exactly even**, machine-checked |

| FAIL criterion | fires? |
|---|---|
| `t=0,1` only after coefficient tuning | no |
| the stationary point is at `t=1/2` | **YES** |
| the action is `t↔1−t`-symmetric and cannot distinguish the pair | **YES** — the criterion the first draft dropped |
| the zero-mode condition substituted into the action | no |
| no 13D parent theory supplied | no — ECSK supplies one, at §6's price |

**E8 gate: NOT passed.** Two of five FAIL criteria fire.

## 10. What this round does NOT show

* Does **not** supply a full 13D parent action; it supplies one half of one
  sector's EOM, on §6's five assumptions.
* Does **not** reopen C123–C133's verdicts.
* Does **not** change `N_gen=3`'s CONDITIONAL status,
  `lambda = FREE_COUPLING_PARAMETER`, `sm_derivation_claimed = False`, or
  `safe_for_runtime = False`.
* Does **not** close H1c, OB1, or round95's gap. It exhibits the round95 pairing
  structurally, attached to a vanishing source — and C125 already downgraded the
  underlying identity as forced in every `Cl(1,12)` irrep.
* Does **not** show ECSK is wrong, nor that torsion cannot be selected — only
  that *this* mechanism, on *this* background, in vacuum, gives `T = 0`.
* Does **not** rule out `P14`, `P3`, or V2/V3 above.
* Does **not** solicit Tom Lawrence's Part 5.
* Round90's anomaly coefficients were not touched; they are `[WEAK]`, not
  `[DOCS]`.

## 11. Registry actions — NOT performed by this round, proposed only

This round does not edit `PARENT_ACTION_GATE.md`, `OPEN_BLOCKERS.md`,
`null_results/INDEX.md`, or `pearl_registry/INDEX.md`. Proposed:

* `null_results/` entry for `P2` (REJECT, kill-branch (a), three routes).
* `PARENT_ACTION_GATE.md` **F6**: record the first derived non-trivial torsion
  EOM, logged **`PARTIAL`** with the metric-EOM gap named.
* C132 §1c "already tried": *ECSK algebraic torsion sourced by the certified
  zero modes → `T=0`, `t=1/2` (C134); ECSK's bosonic sector = round72's E8 at
  `a=0`*.
* **Pearl (Pearl Gate).** *observation:* in any Kaluza–Klein Einstein–Cartan
  setup with `M₄ ×` (internal), the torsion component with all three legs
  internal is sourced by a **4D-chirality-flipping** bilinear, so it vanishes
  identically on 4D-chiral content and needs a 4D *pseudoscalar* condensate.
  *falsifiable_prediction:* any future spin-current-sourced internal-torsion
  mechanism here dies the same way unless it supplies one. *impact_score:* 7.
  *trigger_condition:* any candidate sourcing internal torsion from a fermion
  bilinear (`P3` first). *next_check:* at `P3`.
* **Pearl (Caveat Gate).** §8 V2 names a specific untested alternative —
  non-minimal fermion–torsion couplings (Freidel–Minic–Takeuchi; Holst/Immirzi),
  both in the retrieved literature, both generating vector–vector and
  vector–axial four-fermion terms. *falsifiable_prediction:* if either yields an
  internal-torsion source with a 4D-**scalar** or **vector** structure, route 2
  does not apply. *impact_score:* 5. *next_check:* whenever this line is revisited.
* **Pearl (methodology).** The Paraphrase-Sensitivity Probe **earned its cost
  here**: the two passes agreed on the verdict but the *paraphrased* pass alone
  found the round's heaviest defect (the undervaried vielbein EOM, which forced
  `F6: PASS → PARTIAL`). *falsifiable_prediction:* over the next 5 high-stakes
  PROMOTE-candidate rounds, ≥1 more finding of verdict-changing severity will
  come from the second, differently-worded pass only. *impact_score:* 6.
  *next_check:* after 5 more Full-Ladder rounds.

## 12. FL Step 8a — skeptic passes

**Two independent context-blind passes, both `WEAKENED`, agreeing on the
verdict.** Full record, verbatim findings, and disposition of all 26 items:
`skeptic_verdict.md`. Both explicitly confirmed the central kill and said it is
stronger than the first draft claimed. Per the Response Matrix, `WEAKENED` ⇒
promote with a `[WEAK]` marker and documented caveats — done throughout.

## Check

* Round72's live-vs-superseded status re-verified from the primary, and its own
  ambiguity now stated rather than asserted away.
* Both mandatory controls run and passed before any positive statement, and both
  are now reported **with their regime limits**.
* Five assumptions named (was one).
* The permitted kill was reported as a kill; no positive `t`-selection was
  forced; kill-branch (c) was not manufactured.
* One check **failed** during repair and was **diagnosed, not tuned away**
  (ill-conditioned similarity + wrong transformed Dirac adjoint); the diagnosis
  is in the script's own comment.
* **Correction to the first draft's own §Check:** it claimed every prior-art
  status was read from the primary this session. The C124 carve-out was taken
  from C132's quoting and its line reference was wrong; corrected in §"Other
  prior art" after reading C124 directly.

---

## Evidence tier of the central conclusion

**Central conclusion:** *the ECSK algebraic torsion equation on `M₄×S³×S⁶`,
evaluated on this project's certified `S⁶`-twisted zero-mode chirality, forces
`T = 0` and hence `t = 1/2`; it selects neither `t=0` nor `t=1`, and is in fact
incompatible with the `∇^t` ansatz for every `t ≠ 1/2`. `P2` is killed on
kill-branch (a).*

**Tier: `[VERIFIED-tool]`, confidence HIGH** for the mathematics — 53 machine
checks, 0 failures, with an AST self-audit excluding checks that cannot fail;
the load-bearing facts are exact operator identities, not samples; route 2 is
representation-independent across 40 basis changes; the positive control
reproduces Perez–Rovelli exactly and Popławski in magnitude; the `−1/4` gravity
coefficient is independently corroborated by round111's July-2026 result.

**Tier of the physics reading: `[INFERRED]`, confidence MEDIUM-HIGH.** Route 2
is `[VERIFIED-tool]` and independent of every contested assumption in §6 — it
alone kills `P2` for 4D-chiral content. Route 1 depends on the absence of a
fermion condensate, which is an *absence of evidence* in this project rather
than a derived vacuum-alignment theorem. Route 3 is `[VERIFIED]` arithmetic
under §6 assumption 4 (unit-radius normalisation). §4 and §5a's factorisation
carry §6 assumptions 1, 2 and 5.

**Tier of the F6 claim: `[VERIFIED]` that the torsion EOM is derived;
`PARTIAL`, confidence HIGH, that F6 as a whole is not met** — the metric EOM is
neither derived nor satisfied by the frozen background.

**Marker on the whole round: `[WEAK]`** per the FL Response Matrix, both
skeptic passes having returned `WEAKENED`.
