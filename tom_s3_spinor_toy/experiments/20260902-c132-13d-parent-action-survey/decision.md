# C132 — Decision (DIVERGENT-mode survey)

**Date:** 2026-09-02
**Mode:** DIVERGENT (D1–D5 of `research-methodology.md`), per `claim.md`'s own
explicit mode declaration and the skeptic-leaning-tie-breaker override stated
there. Outputs below are `[CANDIDATE]`/`[SPECULATIVE]` by design.

**Verdict:**
`SURVEY_COMPLETE_BUT_NOVELTY_CHECK_PARTIAL__18_GENERATED__15_PROPOSED__TOP_ITEM_P0_MATERIALLY_CORRECTED_BY_SKEPTIC_PASS__G2_EQUIVARIANCE_DOES_NOT_FORCE_CHANNEL_SYMMETRY_TRIALITY_Z3_DOES__TWO_MISSED_CANDIDATE_CLASSES_ADDED_AFTER_REVIEW__P2_MUST_OPEN_AGAINST_ROUND72_E8_GATE_NOT_ITS_SUPERSEDED_ROW`

**⚠️ Read §7 before quoting anything above it.** A context-blind FL Step 8a
skeptic pass returned `[FALSIFIED]` on **both** things in its scope — the
Novelty Check's completeness and the ranking's reasoning — and its two
CRITICAL findings were independently re-verified by this session against the
primary files before being accepted. **This document is the post-repair
version**; the pre-repair `P0` argument was wrong in a specific, load-bearing
way, and the pre-repair `P2` cited a table its own source marks as superseded.
Both are corrected in place below, and §7 records what changed.

**What this round produced, in one paragraph.** 18 candidate mechanisms
generated, 15 proposed after the Novelty Check. The most useful output is
`P0`, but **not** in the form first written: `G₂`-equivariance does **not**
force the pairing rule to be channel-symmetric — it imposes *no constraint at
all* on the channel label, because `G₂` acts trivially on it (this project's
own `pearl_registry` row 34 says so explicitly, and the first draft of this
document had it exactly backwards). What is true, and is the corrected `P0`,
is a **three-tier symmetry ladder**: `G₂` buys nothing, `Spin(8)` buys
block-diagonality (no channel mixing, by Schur on inequivalent irreps), and
only the **triality `ℤ₃`** buys equal coefficients, i.e. genuine channel
symmetry. That tells a future round exactly which symmetry assumption
purchases which reduction of the pairing-rule space — which is a cheaper and
more honest deliverable than the "the space has 3 elements" claim it replaces.
Beyond `P0`, the strongest genuine mechanisms are Einstein–Cartan
torsion-as-auxiliary (`P2`) and a joint 13D generalized-Killing-spinor
constraint (`P14`, **found by the skeptic pass, not by the survey**), tied on
CDT; then a diagonal `ℤ₃` orbifold (`P4`).

---

## 0. Scope, stated before anything else

* Does **not** derive or verify any parent action.
* Does **not** claim any candidate is correct. All are `[CANDIDATE]`/`[SPECULATIVE]`.
* Does **not** reopen or re-litigate C123–C131.
* Does **not** change `N_gen=3`'s CONDITIONAL status, `lambda=FREE_COUPLING_PARAMETER`,
  or `safe_for_runtime=False`.
* Does **not** solicit Tom Lawrence's Part 5.
* Does **not** edit `PARENT_ACTION_GATE.md`, `OPEN_BLOCKERS.md`,
  `null_results/INDEX.md` or `pearl_registry/INDEX.md` — registry updates are
  the orchestrating session's, per C124–C131 precedent.
* **The Novelty Check is `PARTIAL`, not complete** — three named reasons in
  §1d. "15 proposed" means *survived the check over the sources actually read*.

---

## 1. Step 1 — MANDATORY Novelty Check (run FIRST, before any candidate was written)

### 1a. Sources read this session

Counts below are **file line counts**, not data-row counts — the first draft
reported them as row counts and was wrong in all three cases (skeptic finding
16, verified: `null_results` has 42 data rows in 47 lines; `parked` 6 in 12;
`pearl_registry` 129 in 136).

| File | What was read | Tag |
|---|---|---|
| `null_results/INDEX.md` | entire file (47 lines, 42 data rows) | `[VERIFIED-tool]` |
| `parked/INDEX.md` | entire file (12 lines, 6 data rows) | `[VERIFIED-tool]` |
| `pearl_registry/INDEX.md` | full scan of all 129 data rows; rows 36–42, 114–122 read in full | `[VERIFIED-tool]` |
| `PARENT_ACTION_GATE.md` | entire file (490 lines), F1–F7 + OB2 block | `[VERIFIED-tool]` |
| `OPEN_BLOCKERS.md` | OB1 (10–511), OB13 (514–631), OB2 (668–760), OB11 (1655–1785) | `[VERIFIED-tool]` |
| round95 `decision.md` | entire file (403 lines) | `[VERIFIED-tool]` |
| round72/E7 `decision.md` | lines 1–130 — **including the E8 gate and the superseding summary table, read only AFTER the skeptic pass flagged the omission** | `[VERIFIED-tool]` |
| round86 / 87 / 88 / 89 `decision.md` | verdict + bottom-line sections | `[VERIFIED-tool]` |
| round98 `decision.md` | verdict block (`INCONCLUSIVE__SOURCE_ACCESS_INSUFFICIENT`) | `[VERIFIED-tool]` |
| C124 `decision.md` | Relaxation Map V1–V5 (lines 542–550) + verdict string | `[VERIFIED-tool]` |
| C126 / C127 / C130 / C120 `decision.md` | Relaxation Maps + skeptic tables | `[VERIFIED-tool]` |
| H-19 sibling project, `phase1_mechanism_atlas/coset-space-dimensional-reduction.md` | entire file (57 lines) | `[VERIFIED-tool]` |

**Two disclosures the first draft did not make (skeptic findings 10, 17):**

1. **C125, C128, C129 and C131 `decision.md` were NOT read directly.** Every
   citation of them below is **second-hand via `PARENT_ACTION_GATE.md` F4 and
   `null_results/INDEX.md`**. This matters — it is how the `P0` C125-inversion
   error (§7 finding 3) got in.
2. The H-19 file read is `phase1_mechanism_atlas/...`. `OPEN_BLOCKERS.md:393`
   actually cites `phase2_transferable_patterns/gkp-su3-structure-generalization.md`
   and `phase3_red_team_recomposition/recomposition.md` — **different files,
   not read**. The first draft's "the file IS reachable at the path OB1 cites"
   was wrong. Also: quoted H-19 material is **translated from Russian**, so
   quotation marks around it indicate sense, not verbatim text.

**Prior "100 directions" brainstorm:** the generated list is **not committed to
this repo**. What exists is
`.claude/checkpoints/2026-07-17_ob1-mechanism-search-rounds114-115.md:35-41`,
naming item 26 (`Spin(8)`-equivariant …), item 28 ("spectral flow" — since run
as round116), item 29 (**Callias index on the cone over `S⁶` — untried, and
this survey does not cover it either**; recorded here so it is not lost again),
plus "~90 candidates not yet touched". **That list could not be read. The
Novelty Check therefore cannot certify novelty against it.**

### 1b. The seven pre-filters any candidate must clear

Quoted or closely paraphrased from the actual registry entries. A candidate
failing one of these was not proposed as new.

| # | Pre-filter | Source |
|---|---|---|
| **O1** | **Product/decoupling.** `D_full² = D_{S³,t}²⊗1 + 1⊗D_{S⁶,S⁻}²` exactly. GAP-4 (REJECT): *"generation index lives entirely in S6/octonion channels — no S3 quantum number to mix, structurally not just empirically."* Pearl: *"any FUTURE generation-distinguishing mechanism … must break the tensor-product structure between the compact factors."* **Caveat carried from round95's own "Assumptions carried, unresolved": the decoupling is a presupposed ansatz (E2/E12), not proven.** | `null_results` GAP-4; `pearl_registry` row 22 |
| **O2** | **`G₂`-blindness — stated precisely, because the first draft over-read it.** `8_v\|_{G₂}=8_s\|_{G₂}=8_c\|_{G₂}=7⊕1` (G44, REJECT: *"S⁶ = G₂/SU(3) cannot distinguish the three reps → triality invisible"*); E-L3B: the three bundles are the same bundle with the same connection and *"the twisted Dirac operators … are THE SAME OPERATOR."* **What this does NOT say:** it does not say a `G₂`-equivariant coupling is channel-symmetric. `pearl_registry` row 34 states the opposite explicitly — *"A `Φ` CAN be built at the `G₂`-only level (E-L3B's corollary gives one trivially, since the operators are literally identical)"* — and that such a `Φ` exists *"BECAUSE `G₂` can't distinguish the channels."* The real content of `O2` is: **`G₂` cannot be the source of a channel-distinguishing structure, and (row 37, via G86B's Hopf/Liouville) no `G₂`-invariant scalar or tensorial entangling structure can be either.** See `P0`. | `null_results` G44; `pearl_registry` rows 26, 34, 37; OB11 §4 |
| **O3** | **13D-covariant local bosonic invariants are closed.** C124 `STRUCTURAL_NO_GO`. Scope explicitly named as **NOT** closed: independent 13D gauge field, non-product/warped background, extra covariant derivatives, non-polynomial functions, additional p-form fields, enlarged gauge algebra, **boundary/defect terms**, nonlocal/quantum effective actions, **fermion bilinears**. | `null_results` C124; C124 `decision.md:542-550`; `PARENT_ACTION_GATE.md` F4 |
| **O4** | **A topological invariant of a single fixed background cannot select `t`** — a `ξ`-structure is a lift of a classifying map, not a connection. Two carve-outs are part of the filter: differential/secondary invariants, and invariants of the *relation* between two backgrounds. | `pearl_registry` row 120 (C127) |
| **O5** | **A functional of the `S³` connection alone, invariant under the FULL disconnected gauge group, is dead on arrival.** ⚠️ **Stale justification, flagged by the skeptic pass and confirmed:** C126's stated reason (*"`t=0,1` are one point of `𝒜/𝒢`"*) is **superseded by C128** — `OPEN_BLOCKERS.md:280-281`: *"Fixing the vielbein … is a complete gauge-fixing of C126's `𝒢`, so the ansatz lives in `𝒜` itself (C125's category), not `𝒜/𝒢`"* — and `pearl_registry` row 122 turns it around: *"Every future claim of the form 'a LARGE gauge transformation relates/dissolves `t=0` vs `t=1`' is wrong with no computation."* Use the filter's operational content (a `𝒢`-invariant connection-only functional is even in `t−½`), not its `𝒜/𝒢` framing. `𝒢₀`-only invariants (Chern–Simons) and torsion/soldering-form functionals are outside it. | `pearl_registry` rows 118, 122; `OPEN_BLOCKERS.md:272-294` |
| **O6** | **Künneth filter.** No harmonic 1-, 2-, or 3-form on ANY product `M×S⁶` has a nonzero leg on `S⁶` (`b₁=b₂=b₃(S⁶)=0`). | `pearl_registry` row 114 (C119) |
| **O7** | **`ε`/`η`-sector filter.** On a strict product, a candidate needing BOTH `ε` and torsion cannot exist. Companion: a twist bundle from one factor's **post-ansatz** structure group is invisible to any 13D-covariant invariant. | `pearl_registry` row 117 (C124) |

### 1c. Mechanisms already tried — do NOT re-propose

The skeptic pass checked this table against `PARENT_ACTION_GATE.md` F4
item-for-item and **found no F4 mechanism omitted from it.**

| Mechanism | Verdict | Source |
|---|---|---|
| External string-worldsheet analogies (Gates–Hull–Roček; Strominger–Hull flux) | round87 `FAIL` (even-dimensionality — `S³` is odd); round88 `FAIL` (*"this project's compactification has no 2D string worldsheet anywhere"*) | rounds 86–89 |
| Pati-Salam gauge/anomaly forcing | rounds 90–112 computed in `G_eff`, no forcing; **G97 closes the standard product-manifold `SU(4)` realization entirely** (102/108/109) | OB1, F4 |
| Flux-quantization torsion selection | round115 NULL — circular (any target `t` admits some `ρ₃`) | round115 |
| "Spectral flow" / innermost-crossing-pair | round116 — equivalent restatement | round116 |
| `ℤ₂` orbifold `S³/⟨ι⟩` (round80's `ι(g)=g⁻¹`) | forces `t=½` **uniquely** — killed. **Non-free: 2 fixed points at `g=±1`** | F4; round80 `decision.md:216-220` |
| Bismut-Ricci-flat `Rc=¼H²` | C119 F1 **FAIL** three ways | C119 |
| `I9 ∝ (2t−1)·Vol(S³)·Vol(S⁶)` | C120 — reduces to a linear function of `t`, zero at `t=½`; duplicate of round116 | C120 |
| `η(D^t)` raw eta / grav. CS level | C121 REJECT — `η mod 2` identical on every interval | C121 |
| Yang–Mills `∫\|R^t\|²` | C123/C126 WEAKENED — `S_YM≥0` vanishing at flat points is a theorem, zero selection content | C123, C126 |
| CS transgression `CS₃∧P₄∧ch₃(E)` and the whole CS/transgression family | C124 `STRUCTURAL_NO_GO` | C124 |
| **Generic quadratic curvature-plus-torsion action `F=a\|R^t\|²+b\|T^t\|²`** | **round72 E8 gate, `BLOCKED/UNDERDETERMINED`:** `F'(t)=2(2t−1)[aA·t(t−1)+2bB]`, so **`t=½` is always stationary and `t=0,1` are stationary only if `b=0`** (re-verified in sympy by round72 itself). **Missed by the first draft — see §7 finding 9.** | round72 `decision.md:69-121` |
| Bordism/global anomaly of a single background | C127 — structurally excluded in the SELECTION reading | C127 |
| Bare `Pin^±` on `M_ι`; twisted `Pin^±×_{ℤ₂}G` on `M_ι` | C129 + C131 (`[M_ι]=0`, explicit null-bordism); C130 (exists uniformly in `G`) — neither discriminates | C129–C131 |
| Two-sector NCG spectral triple | C41–C60 — fails orientability AND Poincaré duality | OB2 |
| `S³`-frame ⊗ `S⁶`-triality non-product `D` (one postulated coupling) | C79 NULL — artifact of `D_{S⁶}`'s 36-dim raw kernel | C79 |
| 6 external parameter-selection schemes (RS/GW, GKP-KKLT + `SU(3)`-structure generalization, `G₂`-holonomy M-theory, Hořava–Witten, CSDR) | H-19: **none transfers**; CSDR is a *kindred stuck problem* | H-19, via OB1 |
| Modular-flavor-symmetry hierarchy | ModFlav REJECT — `(a,N)` discrete, wrong type | ModFlav |
| Free `ℤ₃` orbifold **of `S⁶`** | G27 REJECT — `χ(S⁶)=2` not divisible by 3 | G27 |
| Friedrich–Ivanov characteristic-connection uniqueness | round98 `INCONCLUSIVE__SOURCE_ACCESS_INSUFFICIENT` — **genuinely open, not closed** | round98 |

### 1d. Novelty Check outcome — `PARTIAL`

**18 generated, 15 proposed, 3 recorded as not-new/unavailable.** The check is
`PARTIAL` for three named reasons, all disclosed rather than inferred:

1. The ~90-item goal-expansion list was unreadable (§1a).
2. C125/C128/C129/C131 were read second-hand (§1a) — and that is exactly how
   the `P0` inversion (§7 finding 3) survived the first draft.
3. **The first draft missed two whole candidate classes**, both added below as
   `P13`/`P14` and both traceable to specific causes, not to breadth:
   `claim.md:52-53` mis-numbers C124's Relaxation Map (it says *"`V5`:
   boundary/defect terms — V5 alone was separately checked and also closed"*;
   C124's actual V5 is *mismatched-index curvature contractions*, and
   boundary/defect terms appear in C124's **not-closed** list), and round72's
   own five-item list of things that could break `t↔1−t` — *"an
   orientation/flux sign convention, **a supersymmetry equation**, a chirality
   convention inherited from a parent theory, **a boundary condition**, or any
   action not symmetric under `t↦1−t`"* — was not mined.

**Not proposed (recorded so they are not re-proposed):**

* **`N1`** warped background / `t` varying over `S⁶` — pre-closed for the
  `G₂`-invariant case by `pearl_registry` row 37 + G86B's Liouville argument
  (*"needs compactness only, not warp-specifics"*); survives only in the
  `G₂`-breaking case, where it collapses into `P5`/`P10`.
* **`N2`** APS reduced eta `ξ=(η+h)/2 mod 1` — **already registered**
  (`pearl_registry` row 116, `pending`; C127 item X3). Also not a *pairing*
  mechanism: `S³`-internal.
* **`N3`** mapping-torus / twisted-`Pin` Dai–Freed route — **circular here**.
  C131: *"every route this program has attempted now converges, independently,
  on round95 as the sole remaining blocker."* round95's blocker **is** this
  round's question.

---

## 2. The two obstructions that organize the space — corrected

Round95's requirement has two halves:

* **(P-I)** independent fields for `t=0` and `t=1` — i.e. `t`-sector content;
* **(P-II)** *how each couples to the 3 triality channels* — the pairing proper.

`O1` bites on both. **`O2` does NOT bite on (P-II) the way the first draft
claimed.** The correct statement, which is `P0`:

> `G₂` acts **trivially** on the channel label. Equivariance under a group that
> acts trivially on a label constrains nothing about dependence on that label.
> So `G₂`-equivariance permits *arbitrary* channel-asymmetric couplings —
> `pearl_registry` row 34 exhibits one.

Every candidate is tagged by which escape route it takes on (P-II):

* **(a) channel-blind by assumption** — the coupling is uniform. Cheap, but
  now known to require a **triality-`ℤ₃`** assumption, not a `G₂` one.
* **(b) explicit `G₂`-breaking** — a background, condensate or vev. Must
  independently justify not undermining G73/E-L3B/G102's `G₂`-equivariant index
  machinery (`pearl_registry` row 37's stated cost).
* **(c) an independent structure outside the `S⁶` frame bundle** — G102's
  fiber-`Spin(8)` postulate, C124's V1 gauge field. Model-building input.

---

## 3. Step 2 — the candidate space (18 generated, 15 proposed)

Format: **Mechanism** / **New ingredient** / **Literature** / **Compatibility**.

---

### `P0` — the symmetry ladder: which symmetry assumption buys which reduction of the pairing-rule space *(route (a); meta-candidate, not itself an action)*

**⚠️ This candidate was materially wrong in the first draft and is rewritten.
The error and its verification are in §7 finding 1.**

**Mechanism.** Not a parent action — a statement of what each available
symmetry assumption purchases. Write the combined channel bundle as
`E_v ⊕ E_s ⊕ E_c`. Each rung is a Schur-lemma computation on already-certified
content:

| assumed symmetry of the parent action | what a coupling to the `S³` sector may look like | consequence for the pairing rule |
|---|---|---|
| **`G₂` only** | `E_v ≅ E_s ≅ E_c` as `G₂`-bundles (G44, E-L3B), so the three are `V ⊗ ℂ³` for one common module `V`; a `G₂`-equivariant endomorphism is `1_V ⊗ M` for an **arbitrary** `3×3` matrix `M` | **no constraint whatsoever.** Channel-selective pairings are permitted, and `pearl_registry` row 34 exhibits one explicitly (*"A `Φ` CAN be built at the `G₂`-only level"*) |
| **`Spin(8)`** | `8_v, 8_s, 8_c` are **inequivalent** irreps, so Schur forces `M` block-diagonal with independent scalars `λ_v, λ_s, λ_c`. `pearl_registry` row 34: *"if `Φ` were genuinely `Spin(8)`-equivariant it would be a nonzero element of `Hom_{Spin(8)}(8_v,8_s)`, which Schur's lemma forces to exactly 0"* | **no channel mixing**, but **independent per-channel coefficients still allowed** |
| **triality `ℤ₃`** (the explicit `U`, `U³=1`, built in `pearl_registry` row 33 from Baez's named `S₃ ⊂ F₄` permuting the three octonion slots, and commuting with the same `g₂` used throughout) | `U` conjugates the three blocks into each other, forcing `λ_v = λ_s = λ_c` | **channel symmetry**, hence the pairing-rule space is exactly `{all→t=0, all→t=1, all→both}` |

**The deliverable is the ladder, not a number.** A future round that wants the
3-element reduction must **assume triality symmetry of the parent action and
say so** — and that assumption is not free: it is close to the same
fiber-`Spin(8)`/triality postulate G102 already showed `N_gen=3` rests on, so
the reduction and the generation count would be buying from the same
un-derived credit line. Naming that shared dependence is the round's actual
finding here.

**New ingredient required.** For the `G₂` and `Spin(8)` rungs: none. For the
`ℤ₃` rung: a triality-symmetric parent action (model-building input).

**The anomaly step, deflated (§7 finding 2).** The first draft claimed the
cubic `SU(4)` condition *discriminates* among the three options. It does not
discriminate in any interesting way: with round95 §3's `n_L = n_R` and
`n_L + n_R = N_gen`, the one-sector options give `{0, N_gen}` and fail for
**every** `N_gen ≥ 1`, odd or even. So the anomaly says only that a one-sided
`SU(4)` assignment is anomalous — the textbook statement — and the surviving
option `all→both` is `3×[(4,2,1) ⊕ (4̄,1,2)]`, i.e. the standard Pati-Salam
generation content, which was the assumed input. **Real, but not novel and not
`N_gen`-sensitive.** It is retained here only as a consistency filter.

**Three further corrections carried from §7, so they are not re-imported:**
1. The reduction "3 elements → 2 up to `t↔1−t` relabelling" is **withdrawn**.
   C125's actual verdict is the opposite of a relabelling result
   (*"`t=0` vs `t=1` remains a genuine physical choice"*), and C125 left the
   orientation-convention question `UNDECIDED` and **gated on round95** — the
   very question being surveyed. The set has 3 elements, full stop.
2. The generation-count consequence is `3 × 2 = 6`, not `3 × (2+2) = 12`. Both
   `t`-sectors together make **one** Pati-Salam generation
   (`(4,2,1) ⊕ (4̄,1,2)`), so the only genuine factor is C64's `S³` kernel
   multiplicity 2. That reproduces C64's already-recorded number and is **not
   a new prediction**.
3. C64's `D^t(n=0) = 3t·I₂` gives `dim ker = 2` at **`t=0` only**; the `t=1`
   kernel comes from the other branch `3t−3` of round67's family
   (`D^t(n,σ) = σ(n+3/2) + 3(t−½)`). The multiplicity list `2,2,6,6,12,12`
   (C64) is unaffected; the first draft's derivation was.
4. **Evidence-marker correction.** Round95's inputs are **not** uniformly
   `[DOCS]`. Round95's own "Assumptions carried, unresolved" says round90's
   anomaly coefficients are *"reused from round90's own `[VERIFIED-tool]`-sourced
   **Wikipedia** quote and **`[WEAK]`**-sourced modern-paper cluster; not
   independently re-verified against a primary source"*, and flags E17's
   exhaustiveness and the `D_full²` decoupling as presupposed. Load-bearing
   inputs here are `[WEAK]`, not `[DOCS]`.

**One remaining open flag on `P0`'s own inputs.** Round95's pearl-candidate
second argument (*"`n_L=3` is odd, so Witten's `SU(2)` anomaly is violated"*)
appears to count **generations** where Witten counts **`SU(2)_L` doublets**; a
`(4,2,1)` contains 4 doublets, so 3 generations give 12 (even). `[SPECULATIVE
— flagged for verification, NOT asserted.]`

---

### `P1` — Chamseddine–Connes spectral action of the full torsionful Dirac operator *(route (a))*

**Mechanism.** Parent action `S = Tr f(D_full/Λ)` + fermionic term — the
framework `PARENT_ACTION_GATE.md:434-437` names in its own pass criterion
(*"Einstein-Cartan, Chamseddine-Connes-Marcolli spectral action, or another
explicitly cited framework"*), **never attempted in this project** (G28/G29
used a spectral-action *argument* for coupling ratios; G38 computed
`S_spec(c₃)`; no torsionful `Tr f(D/Λ)` exists in the repo).

Two structural reasons it is not a restatement:
* **Non-polynomial** → escapes `O3` by C124's own named scope.
* **Does not factorize across the two compact factors.** The heat kernel does
  (`Tr e^{-sD_full²} = Tr e^{-sD_{S³,t}²} · Tr e^{-sD_{S⁶}²}`), so the
  Seeley–DeWitt coefficients of the product are **products** of the factors',
  not sums — a genuine cross-factor coupling **with no new field**, the only
  candidate here that gets past `O1` for free.

**Literature — abstracts retrieved and read this session, `[VERIFIED-tool]`.**
* Hanisch, Pfäffle, Stephan, arXiv:0911.5074 — *"a formula for the
  gravitational part of the spectral action for Dirac operators … with totally
  anti-symmetric torsion. We find that the torsion becomes dynamical…"*
* Pfäffle, Stephan, arXiv:1101.1424, *On Gravity, Torsion and the Spectral
  Action Principle*.
* Pfäffle, Stephan, arXiv:1203.5898 — *"For the induced Dirac operators,
  **twisted Dirac operators** and Dirac operators of Chamseddine-Connes type we
  compute the spectral action. In addition to the Einstein-Hilbert action …
  we find the **Holst term**…"* — machinery for exactly this project's object
  (a *twisted* Dirac operator with totally antisymmetric torsion), producing one
  of the two odd-in-torsion invariants C120's own skeptic pass flagged as
  *"never checked at all"*.

**Compatibility.** Clears `O1`, `O3`, `O7`. **The sharpest screen in this
survey, and it is a screen against itself:** a functional of `D²` alone is even
in `t−½` by C44's `spec(D^{1-t}) = −spec(D^t)`, so all odd content must come
from the chiral-asymmetry/Holst sector — that is the one thing a future round
should test first. **Channel-blind**, so it serves (P-I) and must be combined
with `P0`'s `ℤ₃` rung for (P-II).

---

### `P2` — Einstein–Cartan / ECSK: torsion is auxiliary and algebraically equal to the fermion spin current *(route (b), obtained rather than postulated)*

**Mechanism.** In ECSK the torsion field equation is **algebraic**: torsion is
fixed pointwise by the fermion spin current; integrating it out leaves a
four-fermion contact term. So `t` is not a free parameter — `(2t−1)` is fixed
by `⟨ψ̄γ₅γ^aψ⟩`. Since this project's fermion content is the `S⁶`-twisted zero
modes, and L5/G74B fixes their **chirality** (`sign(ind)=+1`, all three modes
in `D⁺`), the sign of the `S³` torsion would be fixed by an `S⁶` datum —
structurally the pairing round95 asks for, obtained from an EOM rather than
postulated.

**⚠️ Prior-art status — corrected after the skeptic pass (§7 finding 9),
and this is the most consequential single repair in the document.** The first
draft quoted round72's *"H2: Not tested. Explicitly out of scope"* — a row
that round72 itself marks superseded (`decision.md:123`: *"## Final summary
table (**supersedes the earlier one above**)"*). The **live** status is:

* `H2` → **`OPEN, now sharpened … BLOCKED/UNDERDETERMINED as currently
  posable`** (round72 line 85);
* a **registered, pre-frozen E8 gate** exists for exactly this class of
  action (round72 lines 89–121), with 6 PASS criteria and explicit FAIL
  criteria, and an **adverse preliminary computation, re-verified by round72
  itself in sympy**: for `F(t)=a|R^t|²+b|T^t|²`,
  `F'(t)=2(2t−1)[aA·t(t−1)+2bB]` — **`t=½` is always stationary; `t=0,1` are
  stationary only if `b=0`**, i.e. only by discarding the torsion-energy term
  by hand. E8's FAIL criteria include *"the stationary point is at `t=½`"*.

**Why `P2` nonetheless survives that gate rather than dying in it — the
distinction a future round must make explicitly.** E8's preliminary is about a
**bosonic** functional whose stationarity in `t` is a variational condition on
`t`. ECSK is structurally different: torsion is **auxiliary**, its equation is
**algebraic and fermion-sourced**, and `t` is *solved for*, not extremized.
E8's PASS criterion 6 (*"interprets or breaks the `t↔1−t` symmetry
physically"*) is exactly what a chiral fermion source would do. **That claim is
`[SPECULATIVE]` and is the thing to test — but it is a different question from
the one E8's preliminary answered.**

Other prior art, checked: round111's Relaxation Map names *"Derive `α` … from
an actual physical action | Requires committing to a specific action principle
(Einstein-Cartan, spectral action…)"* — named, never done. round75/E11 Q2
found **zero** wiring between flux and any torsion object in `preprint.tex`.
C124 names **fermion bilinears** as un-closed, three times.

**Compatibility.** Clears `O1` (a fermion bilinear is not a tensor-product
operator), `O3` (C124's named carve-out), `O5` (uses torsion/soldering and
fermions), `O7`. **Crux and cheapest test: self-consistency** — the torsion
sourced by the zero modes must equal the torsion whose `t` produced them.
**Named risk:** the axial current may vanish identically by homogeneity, forcing
`t=½` and killing the candidate the same way round80's orbifold died — which is
also E8's own FAIL criterion firing.

---

### `P3` — Gaugino / fermion condensate sourcing the 3-form torsion *(route (b))*

**Mechanism.** The condensate version of `P2`: `H` (hence `t`) fixed by
`⟨χ̄Γ_{abc}χ⟩`. A vacuum-selection mechanism — `pearl_registry` row 32 names
this as a *genuinely third mechanism-type* and sets its acceptance bar:
*"check for an analogous dynamical derivation of WHY that direction is
selected, not just an assertion."*

**Literature — abstracts read this session, `[VERIFIED-tool]`.**
* Manousselis, Prezas, Zoupanos, arXiv:hep-th/0511122 — *"…in the presence of
  H-flux and general condensates … We revisit the examples based on
  **nearly-Kähler coset spaces** and show that supersymmetric solutions, where
  the Bianchi identity is satisfied, can be obtained when both gaugino and
  dilatino condensates are present."* — established on **this project's own
  class of `S⁶`**.
* Gemmer, Lechtenfeld, arXiv:1308.1955 (`M_{1,2}×X₇`, `G₂`-structure,
  condensates, gauge field a `G₂`-instanton — and, per the authors,
  *"none of the solutions … is supersymmetric"*).
* Cardoso, Curio, Dall'Agata, Lüst, arXiv:hep-th/0310021; Frey, Lippert,
  arXiv:hep-th/0507202.

**Compatibility.** As `P2`, at higher cost (needs a gauge sector + a
condensation scale). **Mechanism-Transfer-Gate caution applied to myself:**
these are 10D heterotic constructions, and rounds 87/88 killed two earlier
string imports precisely because the mechanism did not transfer. The
transferable object is the *algebraic relation* "fermion bilinear sources
totally-antisymmetric torsion", which is not string-specific; a future round
must say that and not lean on the heterotic packaging.

---

### `P4` — Diagonal `ℤ₃` orbifold: `(S³/ℤ₃) × S⁶` with the `ℤ₃` correlated to triality *(route (b); breaks the parity OB13 asks about)*

**Mechanism.** Quotient the **`S³`** factor by a free `ℤ₃ ⊂ U(1) ⊂ SU(2)`
acting by **left** translation → lens space `L(3,1)`.

1. **The `t↔1−t` symmetry is broken by the quotient, not by hand.** `∇^{t=0}`'s
   parallel frame is left-invariant, preserved by left translations, so it
   descends with trivial holonomy; `∇^{t=1}`'s is right-invariant and acquires
   `Ad(ζ)` holonomy. round72/E7's H1b proof uses **simple connectivity**
   explicitly (*"`S³` is simply connected (`π₁(S³)=0`), so there is no monodromy
   obstruction"*) — unavailable on `L(3,1)` for one endpoint, available for the
   other. `[INFERRED — from `ι∘L_ζ = R_{ζ⁻¹}∘ι` plus non-centrality of `ℤ₃` in
   `SU(2)`; NOT computed.]`
2. **The order is 3**, matching the triality `ℤ₃` this project already uses
   (`pearl_registry` rows 33/41, explicit `T³=I`) — which is what makes a
   *diagonal* (translation × channel-permutation) quotient a candidate
   **pairing** mechanism, not merely a `t`-selector.

**New ingredient.** A modification of F1 — declared, per F1's own pass criterion.

**Novelty — checked.** G27 killed free `ℤ₃` **on `S⁶`** (`χ(S⁶)=2`); `S³` has
`χ=0`, so that obstruction does not apply and free `ℤ₃` actions on `S³` exist.
round80's `S³/⟨ι⟩` is **non-free** (2 fixed points, `g=±1`) and order 2. A
grep for "lens space" / `S³/ℤ` found nothing in the repo — `[VERIFIED-tool]`
for the grep; the skeptic could not independently re-run it (no Grep tool
available to that agent), so treat the negative as this session's own.

**Costs, stated up front.** (a) `Vol(S³)→Vol/3` propagates into G28/G29's
coupling ratio. (b) `H¹(L(3,1);ℤ₂)=0` for odd `p`, so the spin structure is
unique `[CITED]`. (c) **Circularity risk is the main liability**: choosing 3
because `N_gen=3` is the pattern G33-A1 was rejected for (*"A1 circular:
`c₃=6=N_gen×2` embeds `N_gen=3`"*). A future round must pre-register an
independent motivation for `p=3` (AOG-5) or sweep `p=2,3,4,5` and report `p=3`
as one point. (d) The subtlety that makes it well-posed: `ι` maps left-cosets
to right-cosets, so whether parity genuinely fails to descend, or descends as
an orientation-reversing `L(3,1)→L(3,2)≅L(3,1)`, is exactly what the round
would compute — it has a definite answer either way.

---

### `P5` — Gauged fiber `Spin(8)`, its `SO(4)×SO(4)` branch identified with `S³`'s own `SO(4)` *(route (c))*

**Mechanism.** G102: the third channel rests on an explicit fiber-`Spin(8)`
postulate (`c_{so(8)}(g₂)=0`). `pearl_registry` row 40 found the first structure
distinguishing **all three** channels: `SO(4)×SO(4) ⊂ SO(8)`, with
`8_v=(4,1)+(1,4)`, `8_s` equal block chirality (`Γ_A=Γ_B`), `8_c` opposite
(`Γ_A=−Γ_B`) — working because rank 4 = rank `SO(8)`, so it cannot sit in
`SO(7)` where every earlier dead candidate lived. Row 41: `so(4)⊕so(4)` is
triality-invariant as a set, with explicit `T`, `T³=I`.

**The move this round adds:** identify **one** `so(4)` summand with `S³`'s own
`so(4)=su(2)_L⊕su(2)_R`. Then "which block chirality" — the datum separating
`8_s` from `8_c` — becomes "which `SU(2)` factor", i.e. **which `t`-sector**,
since C38 gives `{ker D^{t=0}, ker D^{t=1}} = {(1,2),(2,1)}`. That is a pairing
rule.

**Novelty — honest.** The *structure* is registered (rows 39/40/41, `pending`);
its **application to the `t`-sector pairing** is what is new. Row 39's own kill
criterion points here: *"`S³`'s `SO(4)` must NOT be realized as a subgroup of
`G₂` … it would need to be visible only at the full `Spin(8)/Spin(10)` level."*
Row 39 already **killed the most natural embedding** (`Stab_{G₂}(ℍ)`, dim 6, a
subgroup of `G₂`, channel-blind by inheritance), so only a genuinely non-`G₂`
identification survives — row 40's.

**Compatibility.** Breaks `G₂`, so row 37's cost applies in full. Inherits
row 42's warning: the vector-rep and spinor-rep `SO(4)²` findings live in **two
never-reconciled `Cl(8)` realizations** and must not be asserted to be the same
embedding. Note also `pearl_registry` row 36: `Spin(6)=SU(4)` separates `8_v`
from `{8_s,8_c}` but not `8_s` from `8_c` — a weaker but cheaper partial route.

---

### `P6` — 13D `p`-form Chern–Simons term with mixed flux *(route (a) or (c))*

**Mechanism.** C124's F4 not-closed list includes *"additional p-form
fields"* (**not** V3 — V3 is *higher covariant derivatives*; the first draft
mislabelled this, §7 finding 11). In `D=13`, `∫C_p∧(dC_p)^k` with
`p+(p+1)k=13` gives `p=6,k=1` (`∫C₆∧dC₆`) and `p=1,k=6` (`∫A∧F⁶`). Take
`G₇=dC₆` with legs `vol_{S³} ∧ (\text{4-form on }S⁶)`, the natural
`SU(3)`-structure 4-form being `ω∧ω` — an `S³` leg exactly where torsion lives
and an `S⁶` leg exactly where the twist bundle's structure group lives.

**Literature.** Archetype: M-theory's `∫C₃∧G₄∧G₄` in 11D. `[CITED — not
re-verified this session.]`

**Compatibility.** Escapes `O3`/`O7` for a specific reason: C124 kills
invariants built from `(e,T,R)` and kills `ch(E)` because `E` is **post-ansatz**;
a *fundamental* 13D `p`-form is neither, and its **vev** may be the
`SU(3)`-structure. Escapes `O6` (degree-4 `S⁶` leg is above the `k≤3` filter).
Weakness: AOG-5 exposure.

---

### `P7` — 13D gauge Chern–Simons `∫CS₁₃(A)` via C124's own Sector III *(route (c))*

**Mechanism.** C124 proved no 13D **Lorentz** CS form exists (Chern–Weil
generators at degree ≡0 mod 4; 14≡2). For an **independent gauge field** with a
degree-7 primitive invariant, `dCS₁₃(A)=tr F⁷` exists. C124's own skeptic pass
sharpened V1 to exactly this: *"V1 CANNOT be rescued through Sector I at all;
the only route is a genuine degree-14 characteristic class in Sector III (e.g.
`tr F⁷`)"* — verbatim, C124 `decision.md:546`.

**New ingredient.** A 13D gauge group with a degree-7 Casimir. `su(n≥7)` has
one; **`so(8)` does not** (invariant degrees 2, 4, 6 + the degree-4 Pfaffian)
`[CITED]` — a cheap, decisive screen that puts `P7` in direct tension with
`P5`'s preferred `Spin(8)`.

**Compatibility.** The escape C124 itself named. Clears `O5`'s qualifier on the
right side (CS is `𝒢₀`-invariant only).

---

### `P8` — Non-product background: `S³`-bundle over `S⁶`, clutching in one `SU(2)` factor *(route (b))*

**Mechanism.** C124's V2 made concrete. Principal `SO(4)`-bundles over `S⁶` are
classified by `π₅(SO(4)) ≅ ℤ₂⊕ℤ₂` `[CITED — `π₅(S³)=ℤ₂` standard (Freudenthal,
`π_{n+2}(S^n)=ℤ₂`, `n≥2`); NOT re-derived, and this project's own
homotopy-verification gate must run before any future round uses it]`. The two
`ℤ₂` summands are the two `SU(2)` factors — exactly those whose spinor reps
`(1,2)`, `(2,1)` are C38's `t=0`, `t=1` kernels. A clutching nontrivial in
**one** factor breaks `L↔R` using `S⁶` data.

**A cheap structural screen this round can already supply.** A
`G₂`-**homogeneous** `S³`-bundle over `S⁶=G₂/SU(3)` is associated to a
homomorphism `SU(3)→SO(4)`. `su(3)` is simple and 8-dimensional;
`so(4)=su(2)⊕su(2)` is 6-dimensional, so no nonzero Lie-algebra homomorphism
exists, and a connected group has connected image. **Hence every
`G₂`-homogeneous `S³`-bundle over `S⁶` is trivial** `[INFERRED — standard
associated-bundle argument, not machine-checked]`. `P8` therefore requires
breaking `G₂`-homogeneity, exactly as row 37 predicts. This prices the
candidate rather than killing it.

---

### `P9` — `S³`-internal odd-in-torsion invariants: Holst, Nieh–Yan, `∫e∧T` *(route (a); deflated)*

**Mechanism.** C120's skeptic pass recorded, and the round **accepted**, a
search-completeness gap: *"The F6 search never checked the standard
Einstein-Cartan odd-in-torsion invariants (Nieh-Yan, Holst) at all."* C126's V1
names the same family: *"The blindness result of Step 6 does NOT apply to these
— they see `T⁰ = −T¹`."*

**⚠️ Deflated after review (§7 finding 19).** The first draft made the
`S³`-internal case the deliverable — but that dies because *every* 4-form
vanishes on a 3-manifold, using no property of Nieh–Yan at all. That is a
triviality, not a result, and C120's actual gap is an **F6 question about a 13D
parent action**, not an `S³`-internal one. **The live sub-case is the one with
`M₄` legs** (`M₄×S³` is 7-dimensional and admits a 4-form with 1 `M₄` and 3
`S³` legs) — a genuinely different question, and where a future round should
look. `P9`'s `differentiation` is scored 0 accordingly.

---

### `P10` — Explicit symmetry-breaking background `Φ` as a channel↔sector Yukawa *(route (b))*

**Mechanism.** `pearl_registry` row 26 (RESOLVED) states this verbatim as
*"the ONLY remaining door"*: *"a genuinely non-invariant/symmetry-breaking
extension (explicit background `Φ`, `D_E → D_E + Φ`) — a new physical structure
requiring its own justification."* Applying it to the **pairing** question is
new: `Φ` couples a triality label to an `S³` `t`-label directly.

**Independent motivation — supplied after review (§7 finding 13).** The AOG-5
exposure is partly removable by a source **already in this round's own
read-list**: the H-19 CSDR card cites Dolan & Szabo, *"Solitons and **Yukawa
Couplings** in **Nearly Kähler** Flux Compactifications"*, arXiv:1208.1006, and
Chatzistavrakidis–Manousselis–Zoupanos, arXiv:0811.2182, which reduces heterotic
supergravity on `G₂/SU(3)` specifically. `[CITED via H-19 — abstracts not
retrieved this session.]`

**Compatibility.** Breaks `G₂`; row 37's cost applies. `P2`/`P3` **derive** such
a `Φ` where `P10` postulates it, so they dominate it on AOG-5 — which is why
`P10` ranks last despite being a registered "only remaining door".

---

### `P11` — The narrow CSDR sub-question `claim.md` asks for *(route (a)/(c))*

**Mechanism and honest correction (§7 finding 18).** `claim.md` asks whether a
*narrower* CSDR question escapes the broad verdict.

* The broad answer, and the type-mismatch diagnosis, are **the H-19 card's own
  conclusion, not this round's**: embedding selection is a discrete combinatorial
  choice while `t` is a continuous parameter, so the "solution" cannot transfer
  because CSDR has none.
* **Corrected:** the first draft claimed CSDR's constraints are *"vacuous"* on
  `S³=SU(2)/{e}`. Forgacs–Manton has **two** parts — (i) invariance of the
  fields under the `G`-action up to gauge, and (ii) the `H`-equivariance/
  embedding condition. At `H={e}` only **(ii)** is vacuous. Part (i) survives as
  a Scherk–Schwarz-type reduction on the group manifold, producing a scalar
  potential built from `SU(2)`'s structure constants — whose extrema are a live
  selection mechanism, not a vacuous one. `[INFERRED — NOT verified against
  Forgacs–Manton this session.]`
* What remains genuinely live is the *other* half: `S⁶`'s isotropy `SU(3)`
  embedded in a 13D gauge group that also contains `S³`'s `SO(4)` would make the
  CSDR branching rules *output* a channel↔sector assignment — which is `P5` in
  different language, said rather than double-counted.

---

### `P12` — Coleman–Weinberg effective potential for `t` from the `S⁶`-sector fermion determinant *(route (a))*

**Mechanism.** Promote `t` to a 4D modulus; compute `V(t)` from
`log det D_full`. Because the determinant depends on the *joint* spectrum, the
`S⁶` sector contributes — same structural reason as `P1`, with no new fields.
round99 already found a double-well `V(t)` from **classical curvature** (status
`CONFIRMED__DOUBLE_WELL_PLAUSIBLE_FROM_CLASSICAL_CURVATURE`, per C123's
correction to OB13); the quantum version has never been computed.
`pearl_registry` row 32 sets the bar: an actual Coleman–Weinberg calculation,
*"not a bare assertion"*.

**Compatibility.** Overlaps `P1` (the fermionic part of the spectral action *is*
a regularized `log det`) — listed separately because it is strictly cheaper
(needs only the two known spectra, not a full heat-kernel expansion) and its
output is a potential, which F6 and F7 both want (F7: *"not checked at all"* for
any candidate). Channel-blind → `differentiation` 0 for the pairing question.

---

### `P13` — Boundary / defect terms *(route (a) or (c)) — **ADDED AFTER REVIEW***

**Mechanism.** A parent action on `M₁₃` **with boundary**, or with a defect /
end-of-the-world brane, contributes a term that is naturally **odd under
orientation reversal of the `S³` factor** — exactly the parity-odd content OB13
says any selector needs, and exactly what a closed-manifold classification
cannot produce. Concretely: a Hořava–Witten-type boundary contribution, or an
APS-type boundary condition on the `S³` factor whose `η`-term is
orientation-odd by construction.

**Why it was missed, and why it is genuinely open (§7 finding 11).** `claim.md`
mis-numbers C124's Relaxation Map, stating *"`V5`: boundary/defect terms — V5
alone was separately checked and also closed"*. **C124's actual V5 is
mismatched-index curvature contractions** (`decision.md:550`); boundary/defect
terms appear in C124's and F4's **not-closed** lists verbatim: *"Nor does C124
close a parent action using explicit extra covariant derivatives,
non-polynomial functions, additional p-form fields, an enlarged gauge algebra
beyond Lorentz `SO(1,12)`, **boundary/defect terms**, or nonlocal/quantum
effective actions."* The class was excluded from generation on a wrong label.
*(Also corrected: `claim.md`'s "`V1-V4` remain genuinely open" — C124's V4 is
*"already falsified by the project's own C3, and is listed only so it is not
silently re-tried."*)*

**Compatibility.** Escapes `O3` by C124's own named scope. Escapes `O4`
(a boundary term is not a topological invariant of a closed background).
Relation to `N3`: C131 found `M_ι` closed and non-orientable with `[M_ι]=0`;
a **manifold with boundary** is a different object and C131's null-bordism
argument (`M_ι=∂(D⁴×_ι S¹)`) is, if anything, an invitation to look at the
bounding `W` rather than at `M_ι`. Route to (P-II) is weak — a boundary term
sees orientation, not the channel label — so it serves (P-I) primarily.

---

### `P14` — Joint 13D generalized / torsion-Killing-spinor constraint *(route (a)) — **ADDED AFTER REVIEW, and it is the best-shaped mechanism in the survey***

**Mechanism.** Impose a single first-order constraint on a 13D spinor,
`(∇_M + c·H_{MNP}Γ^{NP} + …)ε = 0` (a generalized/torsion-Killing-spinor or
gravitino-variation equation), and decompose `ε = ε₄ ⊗ η₃ ⊗ η₆`. Because the
equation is **one** equation on the **joint** spinor, it produces a *coupled*
condition tying which `S³` spinor (hence which `t`-sector) goes with which `S⁶`
spinor (hence which channel). **That is a pairing rule obtained from an
equation rather than postulated** — the exact shape round95 asks for, and the
only candidate here that delivers (P-II) without either breaking `G₂` or
postulating a fiber `Spin(8)`.

**Why it was missed (§7 finding 12).** round72's own list of what could break
`t↔1−t` names five things — *"an orientation/flux sign convention, **a
supersymmetry equation**, a chirality convention inherited from a parent
theory, **a boundary condition**, or any action not symmetric under
`t↦1−t`"* — and the survey mined none of them. The two unmined ones are
`P14` and `P13`.

**Prior art — checked, and it is open.** round86 examined AHL2023's generalized
Killing spinors for the *coexistence* question and found the pair-of-eigenvalues
structure does not transfer. round114's AHL2023 cross-check was FALSIFIED as a
*calibration* check (it reduced to citing the source's own constant) — neither
touches a **joint 13D** constraint. round98's Friedrich–Ivanov applicability
check is `INCONCLUSIVE__SOURCE_ACCESS_INSUFFICIENT`, i.e. the
characteristic-connection/parallel-spinor uniqueness literature is **genuinely
unresolved here, not closed**. Both `Agricola_2002_Dirac_naturally_reductive.pdf`
and `Agricola_Hofmann_Lawn_2023_invariant_spinors.pdf` are already in-repo.

**Compatibility, and the honest screen a future round must make.** Both
endpoints already have the required spinors: round72's H1b **PROVED** a
`∇^t`-parallel spinor exists at `t=0` and `t=1` on `S³`, and `S⁶` is
nearly-Kähler with Killing spinors — so `η₃⊗η₆` exists at both endpoints and
the question is purely whether a **joint** equation with one torsion parameter
pairs them asymmetrically. **The screen the survey owes and does not have: no
standard Minkowskian supergravity exists at `D=13`**, so the constraint must be
posed as a geometric generalized-Killing-spinor equation, not imported from a
`D=13` SUGRA that does not exist. Saying that is an argument the round must
make, not assume.

---

## 4. Step 3 — Zero-Signal Gate screen

A screen, not a verdict. `H` = the ingredient is an explicitly-labelled
hypothetical extension rather than frozen content.

| # | Entity | Falsifiable predicate | Measurable outcome | Gate |
|---|---|---|---|---|
| `P0` | the symmetry ladder `G₂` ⊂ `Spin(8)` ⊂ +`ℤ₃` | "each rung buys exactly the stated reduction: none / block-diagonal / equal coefficients" | three Schur computations on already-certified branchings | **PASS** |
| `P1` | `Tr f(D_full/Λ)` with `∇^t` torsion | "the chiral-asymmetry/Holst sector is nonzero and odd in `t−½`, extremal at `t∈{0,1}`" | sign and extrema of the odd part of `a₄`/`a₆` | **PASS** |
| `P2` | ECSK torsion field equation on the frozen background | "the axial current of the `S⁶`-twisted zero modes is nonzero and the self-consistent torsion has `2t−1≠0`" | `⟨ψ̄γ₅γ^aψ⟩`; fixed-point solutions for `t`; **E8's 6 PASS criteria** | **PASS** |
| `P3` | `⟨χ̄Γ_{abc}χ⟩` in a condensing sector | "a condensate consistent with the frozen `S⁶` sources `H_{S³}∝(2t−1)vol₃` with `t∈{0,1}`" | induced `H` vs the frozen torsion normalization | **PASS (H)** |
| `P4` | `L(3,1)=S³/ℤ₃` (free, left) + triality `ℤ₃` | "`∇⁰` descends with trivial holonomy and `∇¹` does not" | holonomy rep on `π₁=ℤ₃`; `dim ker D^t` on the quotient | **PASS (H — modifies F1)** |
| `P5` | gauged `SO(4)×SO(4) ⊂ Spin(8)`, one factor `≡ Isom(S³)`'s `so(4)` | "block chirality `Γ_A` vs `Γ_B` maps `8_s`/`8_c` onto `t=1`/`t=0`" | induced assignment vs C38's `{(1,2),(2,1)}` | **PASS (H — V1)** |
| `P6` | 13D `C₆` with `G₇=vol₃∧ω∧ω` | "`∫C₆∧dC₆` is nonzero and odd in `t−½`" | reduced 4D coefficient's parity | **PASS (H)** |
| `P7` | 13D gauge field with a degree-7 invariant | "`∫CS₁₃(A)` exists and couples to `S³` torsion" | existence of a degree-7 Casimir (**already fails for `so(8)`**) | **PASS (H)** |
| `P8` | `S³`-bundle over `S⁶`, class in `π₅(SO(4))` | "a class nontrivial in exactly one `ℤ₂` summand distinguishes the `t`-sectors" | which summand; homogeneous representative (**shown trivial in §3**) | **PASS (H)** |
| `P9` | Holst / Nieh–Yan / `∫e∧T` **with `M₄` legs** | "at least one is nonzero on `M₄×S³` and odd in `t−½`" | degree count + explicit evaluation | **PASS** |
| `P10` | background `Φ` in `D_E→D_E+Φ` | "some Hermitian, Clifford-compatible `Φ` couples a triality label to a `t` label" | existence + independent motivation | **PASS (H — AOG-5)** |
| `P11` | Forgacs–Manton part (i) on `S³=SU(2)/{e}` | "the Scherk–Schwarz potential from `SU(2)`'s structure constants has extrema at `t∈{0,1}`" | the potential's extrema | **PASS** |
| `P12` | `log det D_full` as a function of `t` | "the one-loop `V(t)` has minima at `t∈{0,1}`, not `t=½`" | zeta-regularized `V(t)` extrema | **PASS** |
| `P13` | boundary/defect contribution on `∂M₁₃` | "the boundary term is odd under `S³`-orientation reversal and nonzero" | its parity and magnitude | **PASS (H)** |
| `P14` | joint constraint on `ε=ε₄⊗η₃⊗η₆` | "the joint equation admits a solution at `t=0` and not at `t=1` (or pairs channels asymmetrically)" | solution set of the decomposed constraint at each `t` | **PASS** |
| `N1`/`N2`/`N3` | — | — | — | **not proposed** |

**15 of 18 pass and are proposed.**

---

## 5. Step 4 — CDT ranking (single merged list)

`(differentiation + kill_power + rescue_power + reuse_value − circularity_risk) / cost`,
each 0–5, cost 1–5. `differentiation` is scored **against (P-II), the pairing** —
the round's actual question.

**The first draft used a two-tier split to keep a low-relevance item from
ranking second. The skeptic pass showed that was a correction applied at the
wrong layer: the real defect was that `differentiation` was not being applied as
declared.** Fixed at the source — channel-blind candidates now score
`differentiation` 0–1 — and the tiers are **removed**. The merged list below is
correctly ordered without them.

| Rank | # | diff | kill | rescue | reuse | circ | cost | CDT |
|---|---|---|---|---|---|---|---|---|
| **1** | **`P0`** symmetry ladder | 3 | 4 | 3 | 5 | 1 | **1** | **14.0** |
| **=2** | **`P2`** ECSK spin-current torsion | 4 | 4 | 3 | 4 | 2 | 2 | **6.5** |
| **=2** | **`P14`** joint 13D Killing-spinor constraint | 5 | 4 | 2 | 4 | 2 | 2 | **6.5** |
| **4** | **`P4`** diagonal `ℤ₃` orbifold | 5 | 4 | 3 | 3 | 3 | 2 | **6.0** |
| =5 | `P1` spectral action | 1 | 4 | 4 | 5 | 1 | 3 | 4.3 |
| =5 | `P5` gauged `Spin(8)`/`SO(4)²` | 5 | 3 | 4 | 4 | 3 | 3 | 4.3 |
| 7 | `P13` boundary / defect terms | 3 | 4 | 3 | 4 | 2 | 3 | 4.0 |
| =8 | `P8` `S³`-bundle over `S⁶` | 4 | 4 | 2 | 3 | 2 | 3 | 3.7 |
| =8 | `P12` Coleman–Weinberg `V(t)` | 1 | 3 | 4 | 4 | 1 | 3 | 3.7 |
| 10 | `P3` condensate | 4 | 3 | 4 | 3 | 2 | 4 | 3.0 |
| 11 | `P7` `CS₁₃(A)` via Sector III | 3 | 4 | 2 | 3 | 2 | 4 | 2.5 |
| 12 | `P6` 13D `p`-form CS | 3 | 3 | 3 | 3 | 3 | 4 | 2.3 |
| 13 | `P10` postulated `Φ` | 4 | 2 | 3 | 2 | 3 | 4 | 2.0 |
| — | `P9` Holst / Nieh–Yan (`M₄` legs) | 0 | 3 | 1 | 2 | 1 | 1 | **5.0** |
| — | `P11` CSDR narrow sub-question | 0 | 2 | 1 | 2 | 1 | 1 | **4.0** |

**The last two rows are deliberately unranked, and the reason is stated so it
can be undone in one step.** `P9` (5.0) and `P11` (4.0) score **0 on
differentiation** — by the survey's own declared convention they cannot bear on
the pairing question at all — yet they are cheap enough that raw CDT would place
`P9` at rank 5. Ranking a candidate that answers a different question above four
that answer this one would mislead the future round the ranking is written for.
They are therefore listed with their true scores, unranked, and given
same-round-rider slots in the Relaxation Map below rather than being deferred.
**Unlike the first draft's two-tier device (§7 finding 6), this changes no
score and hides nothing — a reader who disagrees simply reads the CDT column.**

**Prioritized Relaxation Map — the deliverable, not a single winner:**

```
run first, ~1 round, no new machinery :  P0   (+ P9, P11 as same-round riders)
then, one genuine mechanism each      :  P2  and  P14  (tied; P2 has a
                                          ready-made gate, P14 the better shape)
                                      →  P4
then, if a route-(c) postulate or a
  boundary is ever granted            :  P5  →  P13  →  P8  →  P3
low priority / postulate-heavy        :  P1, P12, P6, P7, P10
do not re-propose                     :  N1, N2, N3
never lost again                      :  checkpoint item 29 (Callias index on
                                          the cone over S6) — untried, and NOT
                                          covered by this survey either
```

---

## 5b. FL Step 4a — Floor–Ceiling Interval

**The honest answer is `NO_HEADROOM` for every candidate-count metric in this
round, including the substitute the first draft invented to escape the
problem.** The skeptic pass was right about both halves (§7 finding 7).

* **The round's own target** (`claim.md`: *"at least 8-15 genuinely distinct
  candidates, not padding"*). The first draft declared this `CRITERION_INVALID`
  by constructing a floor that **drops the words "genuinely distinct / not
  padding"** — i.e. by attacking a weakened restatement. Withdrawn: the
  criterion as actually written is not passed by a padding null model, and
  declaring it invalid cost nothing.
* **The substitute** ("candidates that pass the Zero-Signal Gate, are not
  mechanism-duplicates of a §1c row, and name a new ingredient"), floor
  asserted as 0–2. **Also wrong.** A registry-blind textbook enumeration of
  parent-action ingredients yields spectral action, Einstein–Cartan,
  condensates, orbifolds, `p`-form CS, gauge CS, warped/fibred backgrounds,
  postulated Yukawa, CSDR, Coleman–Weinberg — i.e. `P1, P2, P3, P4, P6, P7,
  P8, P10, P11, P12`, none of which is a §1c row. **Floor ≈ 10, observed 15
  → the substitute has the same floor≈observed defect it was introduced to
  escape.** No measurement of it was performed, and the 0–2 figure was an
  assertion.
* Internally, the first draft also printed `efficiency = (12−1)/(ceiling−1)
  ≥ 11/6 > 1` two lines after saying *"No scalar efficiency is reported"*, and
  silently used floor = 1 from a stated range of 0–2. Both withdrawn.

**Verdict for this section: `NO_HEADROOM`.** Per FL Step 4a's own rule this is
**not evidence against anything** — it means the count metric separates nothing
and should not be used to judge the round. What *can* be judged, item by item,
is the per-candidate prior-art mapping and pre-filter clearance — and that is
exactly what the skeptic pass did check, finding 2 stale filters (`O5`, `P2`'s
round72 quote), 2 missed classes (`P13`, `P14`), and `§1c` matching F4
item-for-item. **That per-item audit, not the count, is this round's evidence.**

---

## 6. Ready-to-run `claim.md` sketches for the top-ranked items

*(Sketches only. A future convergent round writes the real `claim.md` against
`experiments/_template/claim.md`, including the Prior Result Gate, estimand and
kill criterion. Do NOT execute in this round.)*

### Sketch A — `C133` (from `P0`): "Which symmetry assumption buys which reduction of the pairing-rule space?"

* **Mode:** convergent. **FL tier:** Full. **Question type:** descriptive.
* **Prior Result Gate:** grep `pairing`, `channel-symmetric`, `Hom_Spin(8)`,
  `triality-symmetric action`. **And re-run against the ~90-item
  goal-expansion list, which C132 could not read.**
* **Claim:** *On the frozen background, `G₂`-equivariance imposes no constraint
  on the channel dependence of a coupling; `Spin(8)`-equivariance forces block
  diagonality but permits independent per-channel coefficients; and only
  invariance under the triality `ℤ₃` forces equal coefficients, reducing the
  pairing-rule space to `{all→t=0, all→t=1, all→both}`.*
* **Kill criterion (can fire, three ways):** FALSE if a `G₂`-equivariant
  channel-mixing map does **not** exist (contradicting `pearl_registry` row 34);
  **or** if `Hom_{Spin(8)}(8_v,8_s) ≠ 0` (contradicting Schur on inequivalent
  irreps); **or** if the `ℤ₃` of `pearl_registry` row 33 does **not** conjugate
  the three blocks into one another.
* **Mandatory negative control:** run the identical three-rung argument on a
  case where the answer is known independently — e.g. three *equivalent* irreps,
  where even `Spin(8)` should permit mixing. If the machinery "proves"
  block-diagonality there too, it is not seeing inequivalence and the result is
  void.
* **What the round must NOT claim.** The anomaly step does not discriminate:
  the one-sector options fail for **every** `N_gen ≥ 1` (round95 §3's
  `n_L = n_R` with `n_L + n_R = N_gen`), so it restates "a one-sided `SU(4)`
  assignment is anomalous", and the survivor is the assumed Pati-Salam content.
  It must also not claim a 3→2 reduction "up to relabelling" — C125 says the
  opposite and leaves the orientation question `UNDECIDED` **gated on round95**.
* **Evidence discipline to pre-register:** round90's anomaly coefficients are
  `[WEAK]` (Wikipedia + an unverified modern-paper cluster, per round95's own
  assumptions section), not `[DOCS]`.
* **Cost:** one short round, no scripts beyond Schur bookkeeping.
* **Does NOT:** supply a parent action; change `N_gen=3`'s status.

### Sketch B — `C134` (from `P2`): "Does the ECSK torsion field equation, sourced by this project's own zero modes, have a self-consistent solution at `t∈{0,1}`?"

* **Mode:** convergent. **FL tier:** Full. **Question type:** descriptive
  (existence of a fixed point), explicitly **not** causal.
* **Prior Result Gate — corrected, and this is the step the survey got wrong:**
  the round must open against **round72's registered E8 gate**
  (`decision.md:89-121`) and its 6 PASS / 4 FAIL criteria, **not** against
  round72's superseded *"H2: not tested, out of scope"* row. It must
  explicitly address E8's adverse preliminary
  (`F'(t)=2(2t−1)[aA·t(t−1)+2bB]`; `t=½` always stationary; `t=0,1` stationary
  only if `b=0`) and state why an **algebraic, fermion-sourced auxiliary**
  torsion is a different question from extremizing a bosonic `F(t)` — or
  concede that it is not, and stop. Also check round111's Relaxation Map row 1,
  round75/E11 Q2, and C124's fermion-bilinear carve-out.
* **Claim:** *With an Einstein–Cartan action on `M₄×S³×S⁶`, the algebraic
  torsion equation evaluated on this project's `S⁶`-twisted zero modes admits a
  self-consistent solution with `2t−1 ≠ 0`, whose sign is fixed by L5's
  already-certified `sign(ind)=+1`.*
* **Kill criterion (two live branches; the third from the first draft is
  dropped because it cannot fire):** FALSE if the axial current vanishes
  identically on the homogeneous background (forcing `t=½` — which is also E8's
  own FAIL criterion firing); **or** if the self-consistency equation has a
  solution for **every** `t` (no selection content). ~~"or if it has no
  solution"~~ — **dropped: `t=½` with zero spin current is always a solution, so
  that branch is unreachable by construction.**
* **Mandatory positive control:** reproduce the standard flat-space ECSK
  four-fermion term's known sign and coefficient. If the machinery cannot
  recover that, it cannot be trusted here.
* **Mandatory negative control:** re-run with a **non-chiral** (vector-like)
  fermion content. The sourced torsion must vanish or lose its sign preference;
  if it does not, the computation is not seeing chirality at all.
* **Pre-filters to clear explicitly in `claim.md`:** `O1`, `O3` (quote C124's
  fermion-bilinear carve-out), `O5` (quote the torsion/soldering qualifier
  **and** C128's supersession of the `𝒜/𝒢` framing), `O6`, `O7`.
* **Gate fields:** **F6 for the first time with a named, derived EOM** (F6 is
  *"the single largest gap in the whole OB1 program"*), plus F4, F5.
* **Scoping discipline:** confine the computation to the `S³` torsion equation,
  with `S⁶` entering only through already-certified chirality and multiplicity.
  If that scoping is impossible, stop and say so rather than grow.

### Compressed spec — `P14` (ties `P2` at CDT 6.5, and has the better shape)

Not written out as a full sketch only because `P2` has a ready-made gate to open
against. **A future round may reasonably run `P14` first.** Minimum spec:
pose a generalized-Killing-spinor / gravitino-type constraint
`(∇_M + c·H_{MNP}Γ^{NP})ε = 0` on `M₄×S³×S⁶`, decompose `ε = ε₄⊗η₃⊗η₆`, and ask
whether the resulting coupled conditions pair an `S³` `t`-sector with an `S⁶`
channel asymmetrically. **Mandatory first move, and the screen the survey owes:
state that no standard Minkowskian supergravity exists at `D=13`, so the
constraint is posed geometrically and not imported.** Prior art to open against:
round86 (AHL2023 coexistence — does not transfer), round114 (FALSIFIED as a
calibration check), round98 (`INCONCLUSIVE`, genuinely open). Both Agricola PDFs
are already in-repo.

---

## 7. FL Step 8a — context-blind skeptic pass (ACTUALLY RUN)

**Disclosure.** The first draft of this document contained a §7 written by the
author *anticipating* skeptic concerns and labelled as a skeptic pass. **It was
not one.** A genuine context-blind pass was then run — `claim.md` +
`decision.md` only, no session history, no reasoning chain, with access to the
repository's own primary files as evidence — and it returned **`[FALSIFIED]` on
both items in scope**. The first draft's own §7 was itself flagged by that pass
(its finding 22) for exactly this reason: 5 of its 10 dispositions resolved to
"already stated", 0 changed a verdict, and it touched none of the errors below.

**Verdicts returned:** Novelty Check's completeness — **`[FALSIFIED]`**;
Ranking's reasoning — **`[FALSIFIED]`**.

### 7a. Findings, disposition, and independent re-verification

Per `~/.claude/rules/audit-verification-gate.md`, the two CRITICAL findings and
the two most consequential MAJOR ones were re-verified **by this session against
the primary files** before acceptance — an agent's `[VERIFIED]` is this
session's `[INFERRED]` until re-checked.

| # | Sev | Finding | Disposition |
|---|---|---|---|
| **1** | **CRITICAL** | `P0` step 2 ("any `G₂`-equivariant coupling is identical for all three channels") is **backwards**. `G₂` acts *trivially* on the channel label, so `G₂`-equivariance constrains nothing about it. | **ACCEPTED IN FULL. Re-verified independently:** `pearl_registry` row 34 states verbatim *"A `Φ` CAN be built at the `G₂`-only level (E-L3B's corollary gives one trivially, since the operators are literally identical)"* and that such a `Φ` exists *"BECAUSE `G₂` can't distinguish the channels"*, while a genuinely `Spin(8)`-equivariant one *"would be a nonzero element of `Hom_{Spin(8)}(8_v,8_s)`, which Schur's lemma forces to exactly 0."* **`P0` rewritten from scratch as the three-rung symmetry ladder; `O2` restated; §2 corrected; the verdict string and headline rewritten.** *(One sub-argument of the finding is itself unsound and is not adopted: the skeptic wrote "`SU(4)` is not a subgroup of `G₂` (dim 15 > 14), so an `SU(4)`-covariant coupling is `G₂`-equivariant" — a non-sequitur, since `G₂ ⊄ SU(4)` either. The finding's main claim does not depend on it.)* |
| **2** | **CRITICAL** | Sketch A's own mandatory negative control fires: the cubic anomaly excludes the one-sector options for **every** `N_gen ≥ 1`, not differentially, so by the sketch's own words the argument *"is content-free"*; and option (iii) is just the assumed Pati-Salam content. | **ACCEPTED.** Re-checked against round95 `decision.md:173`: `n_L(+2)+n_R(−2)=0 ⇒ n_L=n_R`; with `n_L+n_R=N_gen`, `{0,N}` fails for all `N≥1`. The parity-sensitive condition is Witten's, not the cubic one. **`P0`'s anomaly step demoted to a consistency filter; Sketch A's control replaced with a real one (an equivalent-irreps case) and a "what the round must NOT claim" section added.** |
| **3** | MAJOR | `P0`'s "3 → 2 up to `t↔1−t` relabelling" **inverts C125**, whose verdict is *"`t=0` vs `t=1` remains a genuine physical choice"*, and whose Family C is `UNDECIDED` and **gated on round95** — the question being surveyed. | **ACCEPTED, reduction withdrawn.** Traceable to §1a's disclosure 1 (C125 read second-hand). |
| **4** | MAJOR | `3×(2+2)=12` double-counts: `(4,2,1)⊕(4̄,1,2)` is **one** generation, so both sectors give `3×2=6` — C64's already-recorded number. | **ACCEPTED.** The "new prediction" is withdrawn; it is a restatement of C64. |
| **5** | MAJOR | The first draft's §7 claimed a repair in §0 that was not made. | **ACCEPTED** — moot, §0 and §7 both rewritten. |
| **6** | MAJOR | `differentiation` was not applied as declared; re-scored, `P9`→7.0 and `P11`→6.0 land inside Tier 1, so the two-tier split was *"a correction applied at the wrong layer."* CDT arithmetic itself verified correct in all 13 rows. | **ACCEPTED.** Fixed at the source: channel-blind candidates now score 0–1 on differentiation, **and the tiers are removed**. `P5`(4.3) vs `P12`(4.0) mis-ordering also fixed. |
| **7** | MAJOR | §5b's `CRITERION_INVALID` attacks a strawman (drops "genuinely distinct / not padding"), and the substituted floor of 0–2 is asserted, not measured — a textbook enumeration plausibly yields ~10 of the candidates. | **ACCEPTED IN FULL.** §5b rewritten to `NO_HEADROOM` for the whole count family, with the skeptic's own ~10 figure adopted. |
| **8** | MAJOR | Sketch B's "no solution" kill branch cannot fire — `t=½` with zero spin current is always a solution. | **ACCEPTED, branch dropped.** |
| **9** | MAJOR | `P2` quotes round72's H2 row from a table round72 marks **superseded**, hiding the registered **E8 gate** and its adverse preliminary. | **ACCEPTED. Re-verified independently** by reading round72 `decision.md:60-130` this session: line 123 *"supersedes the earlier one above"*; line 85 *"OPEN, now sharpened … BLOCKED/UNDERDETERMINED"*; lines 89–121 the E8 gate with `F'(t)=2(2t−1)[aA·t(t−1)+2bB]`, *"`t=1/2` is **always** stationary. `t=0,1` are stationary **only** if `b=0`"*, re-derived in sympy by round72 itself. **`P2` rewritten; §1c gains an E8 row; Sketch B's Prior Result Gate rebuilt around it.** This is the most consequential single repair in the document. |
| **10** | MAJOR | `O5` is stated from `pearl_registry` row 118 without row 122, which **overturns its `𝒜/𝒢` framing**; and C125/C128/C129/C131 were never read directly. | **ACCEPTED.** `O5` restated with the C128 supersession; §1a discloses the second-hand citations. |
| **11** | MAJOR | Boundary/defect terms were excluded from generation via **`claim.md`'s own mis-numbering** of C124's Relaxation Map. C124's V5 is *mismatched-index contractions*; boundary/defect terms are in the **not-closed** list. | **ACCEPTED. Re-verified** against C124 `decision.md:546-550` and `PARENT_ACTION_GATE.md` F4's *"Nor does C124 close … boundary/defect terms."* **New candidate `P13` added.** `P6`'s "V3" mislabel also fixed. |
| **12** | MAJOR | A joint 13D generalized-Killing-spinor / gravitino-variation constraint is missing — and round72's own five-item list names *"a supersymmetry equation"* and *"a boundary condition"* among what could break `t↔1−t`. | **ACCEPTED. Re-verified** at round72 `decision.md:62-65`, and round98's `INCONCLUSIVE` verdict confirms the adjacent literature is open, not closed. **New candidate `P14` added — it ties `P2` for the top mechanism slot.** |
| **13** | MINOR→MAJOR | `P10`'s AOG-5 exposure is partly removable by Dolan–Szabo arXiv:1208.1006, cited in the H-19 card the round says it read in full. | **ACCEPTED**, added to `P10`; `circ` lowered 4→3. |
| **14** | MINOR | §1a cross-references item 29 to a §4 that does not mention it. | **ACCEPTED** — item 29 (Callias index on the cone over `S⁶`) now recorded in §1a and in the Relaxation Map as untried and **not covered by this survey**. |
| **15** | MINOR | Counts do not add up (15/12 vs 16/13) and `P0` is excluded from one and included in the other. | **ACCEPTED** — renumbered: 18 generated (`P0`–`P14` + `N1`–`N3`), 15 proposed, consistently. |
| **16** | MINOR | §1a's "rows" are line counts, tagged `[VERIFIED-tool]`, wrong in the same direction three times. | **ACCEPTED**, corrected to line counts with data-row counts alongside. |
| **17** | MINOR | The H-19 file read is not the one `OPEN_BLOCKERS.md` cites, and its "quotes" are unmarked translations. | **ACCEPTED**, both disclosed in §1a. |
| **18** | MINOR | `P11` conflates the two Forgacs–Manton conditions; only (ii) is vacuous at `H={e}`, and (i) survives as a non-vacuous Scherk–Schwarz reduction. Its headline also restates the H-19 card's own conclusion. | **ACCEPTED**, `P11` rewritten. |
| **19** | MINOR | `P9`'s deliverable is a triviality (every 4-form vanishes on a 3-manifold), and C120's actual gap is a 13D F6 question. | **ACCEPTED**, `P9` deflated to `differentiation` 0 and re-pointed at the `M₄`-legs case. |
| **20** | MINOR | Evidence-marker laundering: round90's anomaly coefficients are round95-flagged as Wikipedia-sourced and `[WEAK]`, not `[DOCS]`. Also, "diffeomorphism invariance plus a homogeneous background ⇒ `G₂`-equivariant coupling" is a non-sequitur (that is what spontaneous breaking is) and was untagged. | **ACCEPTED both.** The `[WEAK]` provenance is now stated in `P0` and in Sketch A; the non-sequitur is deleted along with the argument it supported. |
| **21** | MINOR | C64's `3t·I₂` gives `dim ker=2` at `t=0` only; `t=1` comes from the `3t−3` branch. | **ACCEPTED**, corrected in `P0`. |
| **22** | MINOR | The first draft's §7 was not a real skeptic pass. | **ACCEPTED** — this section replaces it, with the disclosure above. |

**Nothing was dismissed. One sub-argument inside finding 1 was rejected as
unsound (recorded in-row, not silently), and it does not affect that finding's
main claim.** Per `claim.md`'s divergent-mode scope a second pass is not
required; the first is internally consistent (no finding contradicts another,
and its "where I found nothing wrong" section is specific rather than blanket).

### 7b. What the skeptic pass confirmed rather than broke

Recorded because a review that only lists defects is not calibrated: the pass
recomputed **all 13 CDT rows and found the arithmetic correct**; verified
`P7`'s C124 quotation verbatim at `decision.md:546`; verified `P1`'s three
arXiv IDs and the F6 pass-criterion quote at `PARENT_ACTION_GATE.md:434-437`,
calling `P1`'s `t`-parity screen *"the sharpest single screen in the survey"*;
verified `P4`'s core left/right holonomy asymmetry as *"structurally right"*
against round72:197 and confirmed `π₅(SO(4))=ℤ₂⊕ℤ₂`; confirmed `N1`/`N2`/`N3`
are correctly identified as not-new; and confirmed **§1c matches
`PARENT_ACTION_GATE.md` F4 item-for-item with no F4 mechanism omitted.**

### 7c. What would make this whole survey wrong

1. If the `ℤ₃` of `pearl_registry` row 33 does not actually conjugate the three
   channel blocks into one another, `P0`'s top rung fails and the pairing-rule
   space is never reduced at all.
2. If the unread ~90-item goal-expansion list already contains `P2`, `P14` or
   `P4` with a recorded verdict, the top-ranked mechanisms are duplicates and
   the ranking is void.
3. If `D_full²`'s exact decoupling (`O1`) is not actually exact — round95 lists
   it as a presupposed ansatz, not proven — then `O1` is not a filter and
   several candidates were priced too expensively.
4. If `claim.md`'s framing into (P-I)/(P-II) is not what round95 meant, the
   `differentiation` column measures the wrong thing throughout.
5. If round72's E8 gate is broader than read here — i.e. if it already covers
   auxiliary fermion-sourced torsion and not only bosonic `F(t)` — then `P2`
   dies inside an existing gate and drops out of the top slot entirely.

---

## 8. Pearl-registry candidates (proposed, NOT written)

| observation | falsifiable prediction | impact | trigger | next_check |
|---|---|---|---|---|
| **`G₂`-equivariance imposes NO constraint on the triality-channel label** (it acts trivially on it — `pearl_registry` row 34 exhibits a `G₂`-level channel-mixing `Φ`); `Spin(8)` forces block-diagonality by Schur on inequivalent irreps; only the triality `ℤ₃` forces equal per-channel coefficients | Any future claim of the form *"`G₂`-equivariance forces the pairing/coupling to be channel-symmetric"* is wrong with no computation — and any round wanting the 3-element pairing-rule space must **assume triality symmetry of the parent action and say so**, which draws on the same un-derived fiber-`Spin(8)`/triality credit line `N_gen=3` already rests on (G102) | 8 | any future H1c / round95 / OB1 pairing proposal, or any argument invoking `G₂`-equivariance to constrain channel dependence | at the next OB1 F4 or H1c attempt |
| A round72-style **superseded table inside a still-cited `decision.md`** produced a wrong prior-art status in C132's first draft: the quoted H2 row (*"not tested, out of scope"*) is marked superseded 100 lines later by a table giving `BLOCKED/UNDERDETERMINED` plus a **registered E8 gate with an adverse preliminary computation** | Any prior-art quote taken from a `decision.md` must be checked for a later *"supersedes the earlier one above"* marker **in the same file** before it is relied on; predicted to catch ≥1 further stale citation across this project's own cross-referencing | 6 | any round quoting a prior round's status table | at the next round that cites a prior `decision.md`'s status |
| `PARENT_ACTION_GATE.md` F6 names the Chamseddine–Connes spectral action in its own pass criterion, and the literature for exactly this project's object (a **twisted** Dirac operator with totally antisymmetric torsion) exists and yields a Holst term (Pfäffle–Stephan arXiv:1203.5898, arXiv:1101.1424; Hanisch–Pfäffle–Stephan arXiv:0911.5074) — yet no torsionful spectral action has ever been computed in this repo | The heat kernel of `D_full²` factorizes, so its Seeley–DeWitt coefficients are **products** across `S³` and `S⁶` — a genuine cross-factor coupling from frozen content with no new field, which is what `O1`/GAP-4 says every candidate needs; and any such functional of `D²` alone is even in `t−½`, so all odd content must live in the chiral-asymmetry/Holst sector | 7 | any future OB1 F6 attempt | before any further F4 candidate lacking an action principle |
| round95's Witten-`SU(2)`-anomaly pearl-candidate (*"`n_L=3` is odd"*) appears to count generations where Witten counts `SU(2)_L` **doublets**; a Pati-Salam `(4,2,1)` is 4 doublets, so 3 generations give 12 (even) | If confirmed, round95 §5's *"stronger and more immediate"* second consequence does not fire, and only the cubic-anomaly half of its contingency survives | 4 | whenever round95 §5's contingency is invoked | before any round cites round95's Witten argument as a constraint |
| `claim.md`'s own restatement of C124's Relaxation Map mis-numbered it (*"V5: boundary/defect terms — closed"*; C124's V5 is mismatched-index contractions, and boundary/defect terms are in the **not-closed** list), and that single wrong label **excluded a whole candidate class from generation** | A pre-registration document that paraphrases another round's Relaxation Map must cite item labels **from that round's own file**, not from memory; predicted to prevent ≥1 further class-exclusion of this kind | 5 | any `claim.md` that paraphrases a prior round's Relaxation Map | at the next pre-registration citing an external Relaxation Map |

---

## 9. What this round does NOT mean

1. Does NOT establish that any candidate is correct, or that a parent action exists.
2. Does NOT close OB1 or H1c — OB1 stays `PARKED`; no reopen condition is claimed met.
3. Does NOT change `N_gen=3`'s CONDITIONAL status, `lambda=FREE_COUPLING_PARAMETER`,
   or `safe_for_runtime=False`.
4. The Novelty Check is **`PARTIAL`**: the ~90-item goal-expansion list was unread;
   C125/C128/C129/C131 were read second-hand; and the first draft missed two whole
   candidate classes, both found by the skeptic pass, not by the survey.
5. `P0` does **not** say `G₂` forces channel symmetry — it says the opposite, and
   the first draft of this document said the wrong thing. The 3-element reduction
   holds **only** under an assumed triality-`ℤ₃` symmetry of the parent action.
6. `P0`'s anomaly step is **not** a differentiating test: it excludes the
   one-sector options for every `N_gen ≥ 1` and its survivor is the assumed
   Pati-Salam content.
7. `P2` is **not** an untouched question: round72's registered **E8 gate**
   already covers the bosonic curvature-plus-torsion version and its preliminary
   is adverse (`t=½` always stationary). `P2` survives only if the
   fermion-sourced *auxiliary* torsion reading is genuinely a different question,
   which is `[SPECULATIVE]` and is the first thing a future round must establish.
8. No candidate-count metric in this round has a healthy floor–ceiling interval
   (§5b, `NO_HEADROOM`) — the round's evidence is the per-item prior-art mapping,
   not the count.
9. Does NOT re-litigate C123–C131, and does NOT touch round95's own
   `TENSION_DISSOLVES` verdict — §8's fourth pearl candidate concerns one
   *pearl-candidate* paragraph of round95, not its verdict.
10. Does NOT solicit Tom Lawrence's Part 5.
