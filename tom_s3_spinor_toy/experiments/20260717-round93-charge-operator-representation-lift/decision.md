# E23 (round93) — Decision

**Date:** 2026-07-17
**Verdict:** `BLOCKED__OPERATORS_DEFINED_AND_K3_EQUALS_T3R_PROVEN__Y_FORMULA_AMBIGUITY_WAS_A_DOCUMENTATION_ARTIFACT_NOT_A_PHYSICAL_ONE__BUT_FIELD_CENSUS_FOR_SYSTEM_A_STILL_UNFILLABLE_ON_BL_Y__SU4_LIFT_EXISTS_BUT_IS_NOT_THE_ANOMALY_RELEVANT_ONE`

**Go/no-go:** This is a genuine, tool-verified PARTIAL resolution, not a
forced PASS/FAIL/BLOCKED pick. Part A (operator provenance) and Part B (the
`K_3`/`T_{3R}` reconciliation) reach a clean, positive result: `K_3` and
`T_{3R}` are literally the same 32×32 operator in every piece of this
project's own tool-verified code that actually computes with it (G11, G16,
G17, KT-6) — the "two distinct, unreconciled `Y`-formulas" round92 flagged
is real as a **documentation-level** mismatch (`preprint.tex`'s own prose,
and G16's own `decision.md` summary, mis-describe `K_3`'s geometric origin
as S⁶-side when the code that computes it is unambiguously S³-side) but is
**not** a physical ambiguity in this project's actual constructions —
Part B outcome **(1)** holds, proven by direct matrix computation, not
argued from prose. Part C (the field census) and Part D (`SU(4)` lift) do
**not** reach PASS: Part C is fillable for System A's `SU(3)_c`/`SU(2)_L`/
`SU(2)_R` content but not for `B-L`/`Y` (the same gap round83/91/92 already
flagged, untouched by Part B's resolution — this is a *different* gap:
locating the twisted kernel in a weight-labeled space, not a formula
ambiguity), and Part D exhibits an explicit `SU(4)` action that closes into
complete `4⊕4̄` representations but is confirmed (by this project's own
G97 and, independently re-verified this round, G98) to be neither an
isometry nor a symmetry that preserves this project's own `B-L` charge
assignment — so `SU4_ANOMALY_ROUTE: NOT_APPLICABLE`, and `[SU(4)]^3` is
correctly NOT computed. **Overall: BLOCKED**, per the pre-registered
criterion's own wording ("the gauge provenance... cannot be established
from what this project has already written down") — but a narrower,
sharper BLOCKED than round92's, with one of its two original blocking
causes now closed.

---

## Bottom line, stated plainly first

1. **`K_3 = T_{3R}` — PROVEN**, not merely argued. `experiments/20260618-
   g11-block-generators/g11_block_generators.py:104-108` defines `K_i`
   ("SU(2)_R") as `block_diag(0₂, σ_i/2)` on the 4-dim S³ spinor, **trivial
   on S⁶** (line 6-8: "K_i: SU(2)_R — S³ spinor sector, trivial on S⁶").
   `experiments/20260619-g16-t3r-from-k3/g16_t3r_k3.py:70-71` builds
   `K3_32 = kron(K_S3[2], I8)` and its own inline comment reads "T3R on
   32-dim S³×S⁶ spinor (K₃ acts on S³, trivial on S⁶)". This script's own
   direct computation (`e23_charge_operator_provenance.py`, Part A.2)
   confirms `K3_32` (built exactly as G16 builds it) is **identical**,
   entry-for-entry, to the 32×32 diagonal operator obtained by tensoring
   `g6_spinor_decomposition.py`'s own per-state `T3R` value with the S⁶
   identity, in G6's own product ordering — `K3_equals_T3R_as_32x32_operator
   = True`. `K_3` and `T_{3R}` are not merely numerically coincident; they
   are **the same matrix**, used identically throughout G11→G16→G17→G19→
   G21-G24→KT-6.

2. **The "two distinct `Y`-formulas" finding (round92 Section 3b(ii)) is a
   documentation-level mismatch, traced to its exact origin.**
   `preprint.tex:304-305` describes `K_3` in prose as "a `U(1)` quantum
   number from the `SU(3)`-harmonic decomposition of `S^6`" — an S⁶-side
   description. But grepping this project's own CODE for any S⁶-side
   construction actually named or used as `K_3` finds **none** — every
   single occurrence of `K_3`/`K3_32` in this project's Python (G11, G12,
   G16, G17, G19, G21, G22, G23, G24, KT-6 — 10 files) builds it from
   `K_S3`, the S³-side `SU(2)_R` generator. Traced to its exact source:
   **G16's own `decision.md`** (`experiments/20260619-g16-t3r-from-k3/
   decision.md:9`) itself states "`K₃` is the Cartan generator of
   `SO(6)⊃SU(3)` on `S⁶`" — directly contradicting its OWN script's code
   and its OWN script's inline docstring ("S³ sector (`K₃`): right-handed
   `SU(2)_R` generator (G11)", `g16_t3r_k3.py:31`). This wrong description
   then propagated into `preprint_draft.md:125-126` ("`K₃` is a `U(1)`
   quantum number from the `SU(3)`-harmonic decomposition of `S⁶`") and
   `preprint.tex:304-305` verbatim. **The formula `Y=K_3+(B-L)/2`
   (`preprint.tex:302,309`, used in the paper's own verified anomaly
   computation) and `Y=T_{3R}+(B-L)/2` (`preprint.tex:408`, Weinberg
   section) are, by direct code inspection, THE SAME FORMULA** — confirmed
   by `experiments/20260618-g12-anomaly/g12_anomaly_check.py`'s own
   docstring (line 22: "`Y = T3R + (B−L)/2` (Pati-Salam decomposition)")
   computing exactly the anomaly-cancellation result `preprint.tex:309-320`
   cites as "K₃"-based, and by `g16_t3r_k3.py` itself using both names for
   the same object throughout. There is no second, competing `K_3`
   operator anywhere in this project's actual constructions.

3. **This does NOT unblock round92's E22.** Round92 found TWO separate
   blocking causes for the mixed anomaly conditions: (i) no numeric `B-L`
   value ever assigned to the twisted S⁶-kernel specifically, and (ii) the
   `Y`-formula ambiguity. This experiment resolves (ii) but leaves (i)
   completely untouched — `B-L` (G15's `BmL`) is constructed on the
   UNTWISTED 8-state S⁶ weight space, and this project has never
   constructed `B-L`, or any operator, on the twisted kernel's own ambient
   space (the 1-dim `G₂`-singlet subspace of a 2-dim ambient space,
   `preprint.tex:806-831`). Part A.7 below marks this `[B-L, D_{S6,
   twisted}]` check explicitly NOT COMPUTABLE, exactly as round83/91/92
   already found — this is a genuinely different, still-open gap.

4. **Part D: `SU(4)` acts and closes, but is not the anomaly-relevant
   `SU(4)`.** `SO(6)≅SU(4)`'s 15 generators (`g10_s6_so6_gauge.py:
   so6_generators()`, spinor-lifted per G11's own `lift_to_spinor`) DO act
   explicitly on the 8-dim S⁶ spinor and DO close it into complete `4⊕4̄`
   chirality sectors (`S+`/`S-`, 4 states each, this round's Part D
   computation: `chirality_split_is_4_plus_4bar = True`,
   `full_so6_preserves_chirality_split = True`). But this `SU(4)` is (a)
   confirmed NOT an isometry of `S^6=G_2/SU(3)` (`preprint.tex:282-284`,
   gate G97, reused) and (b) confirmed, independently re-verified this
   round, to NOT preserve this project's own `B-L` charge assignment for
   the raw generator directions outside the `su(3)⊕u(1)` subalgebra (gate
   G98, re-verified: `BmL_commutes_with_full_so6_su4 = False`) — gauging
   the full `SU(4)` would mix the quark and lepton sectors `B-L` is built
   to keep distinct. `SU4_ANOMALY_ROUTE: NOT_APPLICABLE` — `[SU(4)]^3` is
   correctly not computed.

---

## Part A — Operator provenance table

| Generator | Acts on which factor | Explicit operator (cited) | Spectrum on the torsion-endpoint kernel |
|---|---|---|---|
| `T_{3L}` | `S³` | `J_3 = J_S3[2] = block_diag(σ_3/2, 0₂)`, 4×4 (`g11_block_generators.py:98-102`) | `t=0`: `0` (S³ kernel is an `SU(2)_L` singlet, round85/E17 Section 1); `t=1`: `±1/2` (S³ kernel is an `SU(2)_L` doublet, under Convention A) |
| `T_{3R}` | `S³` | `K_3 = K_S3[2] = block_diag(0₂, σ_3/2)`, 4×4 (`g11_block_generators.py:104-108`) | `t=0`: `±1/2` (doublet); `t=1`: `0` (singlet) |
| `K_3` | `S³` (identical to `T_{3R}` — see Bottom Line item 1) | `K3_32 = kron(K_S3[2], I8)` (`g16_t3r_k3.py:70-71`) | Same as `T_{3R}` row — literally the same operator |
| `B-L` | `S⁶`, **untwisted** weight space only | `BmL = -(1/3)(σ₃^{(1)}+σ₃^{(2)}+σ₃^{(3)})`, 8×8 (`g15_hypercharge.py:69-71`) | On G6's untwisted 8-state basis: `-1` (lepton singlet), `+1/3`×3 (quarks), `-1/3`×3 (antiquarks), `+1` (anti-lepton). **On the actual twisted kernel (the specific `dim ker=1` `G₂`-singlet vector, `preprint.tex:806-831`): UNDEFINED — no map from that vector into this weight basis exists anywhere in this project** (round83/91/92, reused) |
| `Y` | Full Hilbert space (`S³⊗S⁶`) | `Y_32 = K3_32 + BmL_32/2` (`g16_t3r_k3.py:83`), proven `= T3R_32 + BmL_32/2` this round | On System B's 32-state bookkeeping: the standard SM hypercharge values (`g16_t3r_k3.py` T6/T7/T8, PASS). On System A's `t=0`/`t=1` torsion-endpoint content: **NOT COMPUTABLE** — inherits the `B-L` gap above |

### Commutator checks (this round's `e23_charge_operator_provenance.py`, all re-verified, not merely cited)

| Check | Relevant `D` | Result | Source |
|---|---|---|---|
| `[T_{3L}, T_{3R}] = 0` | — (algebra closure, not a Dirac-operator check) | **True** | G11 T3, re-verified |
| `[K_3/T_{3R}, C_i]=0` (all 8 `SU(3)_c` generators) | — | **True** | G16 T4 / KT-6, re-verified |
| `[B-L, C_i]=0` (all 8 `SU(3)_c` generators) | — | **True** | G15 T4, re-verified |
| `[B-L, \Gamma_7]=0` (S⁶ chirality) | `\Gamma_7` (chirality operator, proxy for commuting with the untwisted `D_{S6}`'s grading) | **True** | G15 T3, re-verified |
| `[B-L, so(6)=su(4)]` — full 15-dim algebra | — | **False** for the raw 15-generator basis (3/15 commute individually); **True** for the 9-dim `su(3)⊕u(1)` SUBALGEBRA (8 `su(3)` generators + the `U(1)` center, which commutes with `B-L` trivially since they are proportional, G15 T8: `lift_to_spinor(J) = -(3i/2)·BmL`) | G98, re-verified this round with the basis-dependence made explicit (G98's own `decision.md` phrase "9 of 15" refers to subalgebra DIMENSION, not a count of individually-commuting raw basis generators — reconciled this round, not previously stated this precisely anywhere in the project) |
| `[B-L, D_{S6,twisted}]=0` | `D_{S6,twisted}` (the actual physical operator whose kernel is System A's S⁶-side content) | **NOT COMPUTABLE** | `B-L` has never been constructed as an operator on the twisted kernel's ambient space (round83 "Assumptions carried, unresolved" item 3; round91 Section 3; round92 Section 3b(i) — all reused, unchanged) |
| `[T_{3L}/T_{3R}, D_{S3,t}]=0` | `D_{S3,t}` | **Not independently re-verified as a raw commutator this round** — but this is exactly what round77/E11's own construction already establishes implicitly: the surviving `SU(2)` factor's Cartan generator is well-defined and gives a consistent `T_3=±1/2` eigenvalue split on `ker(D_{S3,t})` (round77, reused by round83/85/92) — a conserved quantum number on the kernel is precisely what "commutes with `D` restricted to its own kernel" means operationally; the OTHER `SU(2)` factor is explicitly NOT a symmetry of `D_{S3,t}` at generic `t` (this is exactly why `t=0` is an `SU(2)_L` singlet, not doublet — round77/round85 Section 1, reused) |

**Honest gap named explicitly, per the task's own instruction:** `B-L` is
never defined anywhere in this project as an operator on a Hilbert space
that includes the twisted kernel — it is defined only on G6's untwisted,
per-KK-level 8-state weight space (`g15_hypercharge.py`), and then used as
a **post-hoc LABEL** assigned to already-classified states in that
DIFFERENT space (`bl_charge(weight)` in `g6_spinor_decomposition.py:40-69`
takes an S⁶ weight vector, never a twisted-kernel vector, confirmed by
direct `Read` this round and by round83/92's own prior finding). This is
exactly the distinction the task asked to check: `B-L` is a LABEL on
System B, not (yet) an OPERATOR on System A's Hilbert space.

---

## Part B — Resolving the two `Y` formulas: outcome (1), proven

**Outcome (1) holds: `K_3 = T_{3R}` is provably true as an operator
identity on the physical subspace.** This is established by direct code
inspection and direct matrix computation (`e23_charge_operator_provenance.
py`, verdict key `K3_equals_T3R_as_32x32_operator = True`), not by
argument from prose. The full citation trail:

1. `experiments/20260618-g11-block-generators/g11_block_generators.py`
   (2026-06-18) defines `K_i` ("SU(2)_R generators") as block-diagonal
   `4×4` matrices acting on the S³ spinor sector alone, "trivial on S⁶"
   (lines 6-8, 22, 104-108).
2. `experiments/20260619-g16-t3r-from-k3/g16_t3r_k3.py` (2026-06-19)
   builds `K3_32 = kron(K_S3[2], I8)` (line 71) and its own docstring
   states the question it answers is "Do `K₃` eigenvalues give `T3R = ±1/2`
   for right-handed SM fermions" (line 6) and its own conclusion states
   "`T3R = K₃` eigenvalue on S³ right-handed block" (line 227) — i.e. this
   experiment's OWN framing already treats `K_3` and `T3R` as names for the
   same eigenvalue, not as two operators being compared.
3. `experiments/20260619-g17-electric-charge/g17_electric_charge.py`
   (docstring lines 5-6) states plainly: "G11: `T3L = J₃^{32}`... G16:
   `Y_32 = K₃^{32} + BmL_32/2`" — treating `K_3` as the established
   quantity from G16, used identically to `T3R` throughout G19 (Higgs
   bidoublet, `g19_higgs_bidoublet.py:33`: "`J₃ = G11, K₃ = G16, B−L = G15,
   Y = G16`"), G21-G24 (extended Schur/first-order/chirality/blind-spectrum,
   all import `K_32` from G21's own construction, itself built the same
   way), and `experiments/20260715-kt6-su2r-anomaly-no-bl/
   kt6_su2r_anomaly_check.py:80` ("`K32 = [kron(K_S3[a], I8) for a in
   range(3)]  # SU(2)_R, trivial on S3-orthogonal`" — the exact same
   construction, used in a LATER (2026-07-15), independently-scoped
   anomaly check).
4. **Direct grep audit, this round:** every occurrence of `K_3`/`K3_32` in
   this project's Python source (10 files: G11, G12, G16, G17, G19, G21,
   G22, G23, G24, KT-6) builds it from `K_S3` (S³-side). **Zero**
   occurrences build an S⁶-side "SU(3)-harmonic" `K_3`.
5. **Where the wrong description originates, traced this round:**
   `experiments/20260619-g16-t3r-from-k3/decision.md:9` (G16's own
   official verdict summary, written the same day as the script) states
   "`K₃` is the Cartan generator of `SO(6)⊃SU(3)` on `S⁶`; `B−L` from `K₃`
   via Pati-Salam" — this is the **opposite** of what `g16_t3r_k3.py`
   itself builds and states inline ("K₃ acts on S³, trivial on S⁶",
   line 70). `preprint_draft.md:125-126` repeats the S⁶-side description
   almost verbatim ("`K₃` is a `U(1)` quantum number from the `SU(3)`-
   harmonic decomposition of `S⁶`"), and this exact phrasing was then
   copied into `preprint.tex:304-305`. **This is a documentation
   propagation error, not a physics ambiguity**: a wrong one-line summary
   in a `decision.md`, written the same day as (and evidently not checked
   against) its own script, propagated first into a draft and then into
   the arXiv-bound `preprint.tex`, surviving three independent citations
   (round90, round91, round92) that read `preprint.tex`'s prose without
   tracing back to the underlying G11/G16/KT-6 code.

**Does the paper's own already-verified anomaly computation
(`preprint.tex:309-320`) use `K_3` consistently, or does it implicitly need
`T_{3R}` somewhere (per the task's specific instruction to check this)?**
**It already uses `T_{3R}` — under the name `K_3`.** `g12_anomaly_check.py`
(the script whose PASS underlies `preprint.tex:309-320`'s "verified
symbolically" claim) states in its own docstring (line 22): "`Y = T3R +
(B−L)/2` (Pati-Salam decomposition; B−L not yet geometric)" — `g12` never
uses the symbol `K_3` at all; it uses `T3R` directly, and its `FERMIONS`
table's `Y` values (`R(1,6), R(2,3), R(-1,3), R(-1,2), R(-1,1), R(0,1)`)
are exactly the values `g16_t3r_k3.py`'s `K3_32`-based computation
reproduces for the same physical states (T6/T7/T8, PASS). **There is no
internal inconsistency in the paper's own published anomaly computation**
— it was already, correctly, using `T_{3R}` (the S³-side operator) the
whole time; only the PROSE label `K_3` attached to that same computation
in the "Standard Model fermion content" section carries a wrong
geometric-origin description.

**Outcomes (2) and (3) are both ruled out:** (2) does not apply — neither
formula is "simply wrong"; they are the same formula, just named
differently in two different sections of the same document. (3) does not
apply — they are not "genuinely different `U(1)` generators"; direct
matrix computation (not mere non-contradiction) shows they are identical.

---

## Part C — All-left-handed census, per `t`-sector

### System A (torsion endpoints, E9-E17) — per triality channel, per `t`-sector

| Field | `SU(3)_c` rep | `SU(2)_L` rep | `SU(2)_R` rep | `K_3`/`T_{3R}` | `B-L` | `Y` | CPT status |
|---|---|---|---|---|---|---|---|
| `t=0`, channel `i∈{1,2,3}`, component `↑` | **singlet** (round92 Section 3a) | **singlet** (round85/E17 Section 1) | doublet, `T_{3R}=+1/2` | `+1/2` (Part A, above) | **NOT ESTABLISHED** | **NOT ESTABLISHED** | NOT the CPT-conjugate of the `↓` component in the same channel (round83/E13 Section D, reused: the two `T_3` components of one doublet are not CPT partners) |
| `t=0`, channel `i`, component `↓` | singlet | singlet | doublet, `T_{3R}=-1/2` | `-1/2` | NOT ESTABLISHED | NOT ESTABLISHED | not the CPT-conjugate of `↑` (same reasoning) |
| `t=1`, channel `i`, component `↑` | singlet | doublet, `T_{3L}=+1/2` | singlet | `T_{3R}=0` | NOT ESTABLISHED | NOT ESTABLISHED | not the CPT-conjugate of `↓` in the same channel (same reasoning, mirrored) |
| `t=1`, channel `i`, component `↓` | singlet | doublet, `T_{3L}=-1/2` | singlet | `T_{3R}=0` | NOT ESTABLISHED | NOT ESTABLISHED | not the CPT-conjugate of `↑` |

Per-channel count: 2 states at `t=0`, 2 at `t=1`; ×3 triality channels
(G67, reused) ⇒ 6 states per sector, 12 if (and only if, per round85/E17's
own unresolved coexistence question) both sectors are simultaneously
physically realized.

**Cells honestly flagged as currently unfillable, and why:** `B-L` and `Y`
for every row. This is NOT the Part B ambiguity (resolved above) — it is
the separate, still-open gap Part A.7 names: `B-L` has never been
constructed as an operator on the twisted kernel's ambient space at all,
so there is no computation to perform, correct or otherwise, for these
cells. Filling them would require the same missing ingredient round83/91/
92 already identified: a stated map from the specific `G₂`-singlet kernel
vector (`preprint.tex:806-831`) into a weight-labeled basis where
`bl_charge()`-style assignment is meaningful.

**CPT-conjugate exclusion, per the task's explicit instruction:** the two
`T_3`-components listed per sector/channel above are the FULL kernel
content per round83/E16's own PASS finding (one weak-isospin doublet, not
two copies) — there is no additional "CPT-conjugate duplicate" to exclude
WITHIN a single `t`-sector/channel, because `B-L` (the axis that carries
CPT-conjugation in this project's bookkeeping, per E13/round79) is not
even established for these states. The census above IS the complete,
non-duplicated content per sector/channel — it is simply narrower in what
it can report (no `B-L`/`Y`, hence no external CPT-partner identification)
than System B's census below.

### System B (`g6_spinor_decomposition.py`, full one-generation bookkeeping) — for comparison, fully fillable but NOT established as System A's target

| Field (representative) | `SU(3)_c` | `SU(2)_L` | `SU(2)_R` | `T_{3R}`(`=K_3`) | `B-L` | `Y` | CPT status |
|---|---|---|---|---|---|---|---|
| `Q_L=(u_L,d_L)` | `3` | doublet | singlet | `0` | `+1/3` | `+1/6` | CPT partner: `(ū_L,d̄_L)` (`B-L=-1/3`) |
| `u_R` | `3` | singlet | doublet, `+1/2` | `+1/2` | `+1/3` | `+2/3` | CPT partner: `ū_R` |
| `d_R` | `3` | singlet | doublet, `-1/2` | `-1/2` | `+1/3` | `-1/3` | CPT partner: `d̄_R` |
| `L_L=(\nu_L,e_L)` | `1` | doublet | singlet | `0` | `-1` | `-1/2` | CPT partner: `(\bar\nu_L,\bar e_L)` |
| `e_R` | `1` | singlet | doublet, `-1/2` | `-1/2` | `-1` | `-1` | CPT partner: `\bar e_R` |
| `\nu_R` | `1` | singlet | doublet, `+1/2` | `+1/2` | `-1` | `0` | CPT partner: `\bar\nu_R` |

16 independent left-handed Weyl states (all-left-handed convention, right-
handed fields written as CPT conjugates of left-handed anti-fields, per
`preprint.tex:296-298`'s own "32 = one generation... plus their CPT
conjugates" and G6/G12's own bookkeeping) — fully established, tool-
verified (G6, G11, G12, G15, G16, G17, KT-6, all PASS). **This table is
NOT established as the target for System A's torsion-zero-mode content**
(round91's core finding, unaffected by anything in this experiment) — it
is reproduced here only to make the fillable/unfillable contrast in the
System A table above concrete, per the task's own instruction to be
"honest and explicit about which cells... are currently unfillable."

---

## Part D — `SU(4)` lift: exhibited, but not the anomaly-relevant route

**Explicit action exhibited (route (a), literally satisfied for the
untwisted S⁶ spinor):** `so6_generators()` (`g10_s6_so6_gauge.py:35-44`,
15 antisymmetric `6×6` generators) spinor-lifted via G11's own
`lift_to_spinor` gives 15 explicit `8×8` operators. This round's script
confirms (`full_so6_preserves_chirality_split = True`) all 15 commute with
the S⁶ chirality operator `\Gamma_7`, so they preserve the `S+`/`S-` split
— and `chirality_split_is_4_plus_4bar = True` confirms this split is
exactly `4⊕4̄` (4 states each, `n_minus` even/odd), matching
`g6_spinor_decomposition.py`'s own docstring framing ("S⁶ Dirac spinor: 8
components... `S+` (positive chirality, `4` of `SU(4)`)... `S-` (negative
chirality, `4̄` of `SU(4)`)"). **This closure is real and tool-verified.**

**Why this is NOT the anomaly-relevant `SU(4)`, per the task's own
instruction to check honestly:**

1. **Not an isometry.** `preprint.tex:282-284` (gate G97, reused): "an
   internal check... finds no `SU(4)` subgroup in `Iso(S^3×S^6)`" — the
   `SU(4)` exhibited above acts on the SPINOR FIBER (the structure group
   of the frame/Clifford bundle, per `g10_s6_so6_gauge.py`'s own framing:
   "the SO(6) GAUGE FIELD... Whether the SO(6) gauge field actually
   reduces to the SU(3) preserving J... is the orthogonal→unitary gap"),
   not on the base manifold `S^6=G_2/SU(3)` itself. Only the `SU(3)⊂G_2`
   subgroup is realized as an actual isometry generating a gauge field via
   this project's own KK spin-connection mechanism.
2. **Does not preserve `B-L`.** Gate G98 (`experiments/20260701-g98-bl-
   isometry-holonomy/decision.md`, re-verified this round with the basis-
   dependence made explicit, see Part A table): `B-L` commutes with the
   9-dimensional `su(3)⊕u(1)` subalgebra of `so(6)`, but not with the full
   15-dimensional algebra — 6 of the (basis-dependent) raw generator
   directions mix the quark (`3`) and lepton (`1`) sectors that `B-L` is
   specifically built to distinguish (`BmL_commutes_with_full_so6_su4 =
   False`, this round). **Gauging the full `SU(4)` would erase the very
   `B-L` distinction the entire hypercharge program (Part B) depends on.**

**Verdict:** `su4_anomaly_route = "NOT_APPLICABLE"` (this round's script
verdict dict). Per the task's own instruction, `[SU(4)]^3` is **correctly
not computed** — Part D does not reach a "genuine PASS" (an `SU(4)` action
that both closes AND is gauge-relevant to the anomaly question motivating
round90-92's whole line of inquiry). Separately and independent of the
gauging question: this `SU(4)` structure, even taken at face value,
applies to System B's untwisted S⁶ spinor — it says nothing about System
A's twisted-kernel torsion-endpoint content specifically, for the same
System-A/System-B reconciliation reason Part C's census is incomplete.

---

## Applying the pre-registered criteria

| Criterion | Finding |
|---|---|
| Are operators defined (Part A)? | **Mostly YES** — `T_{3L}`, `T_{3R}`/`K_3` fully defined with explicit matrices and cited spectra; `B-L` defined ONLY on the untwisted System B space, not on the twisted System A kernel (honest gap, not a definition failure of the operator itself) |
| Are the two `Y` formulas reconciled (Part B)? | **YES, cleanly** — proven identical by direct matrix computation, tracing the apparent ambiguity to a documented prose/decision.md propagation error, not a physics ambiguity |
| Is the field table unambiguous (Part C)? | **NO** — `SU(3)_c`/`SU(2)_L`/`SU(2)_R`/`T_3` cells are fillable and unambiguous for System A; `B-L`/`Y` cells are honestly unfillable (a different, deeper, still-open gap than Part B's) |
| Is `SU(4)`-completion explicitly constructed or honestly excluded (Part D)? | **Honestly excluded from the anomaly-relevant role** — an `SU(4)` action IS explicitly constructed and closes, but is shown, not merely asserted, to be neither an isometry nor `B-L`-preserving, so `SU4_ANOMALY_ROUTE: NOT_APPLICABLE` is the correct, non-dangling registration |

**PASS is not supported:** PASS requires ALL FOUR parts to close cleanly.
Parts A/B/D close (D closes via honest exclusion, which the pre-registered
PASS wording explicitly allows: "explicitly constructed OR honestly,
cleanly excluded"); Part C does not — the `B-L`/`Y` census cells for
System A remain genuinely unfillable from this project's own text.

**FAIL is not supported:** none of FAIL's three disjuncts hold. `K_3` and
`T_{3R}` do NOT give genuinely different charges (the opposite was
proven). The anomaly-free table (`preprint.tex:309-320`, `g12_anomaly_
check.py`) was NOT assembled by manually assigning SM charges without
derivation — `g16_t3r_k3.py`'s own T6/T7/T8 gates derive those exact
values from the geometric `K3_32`/`BmL_32` construction, tool-verified.
`B-L` is not shown to be a post-hoc fit for System B — if anything the
chronology argues against fitting: `g12_anomaly_check.py`
(`experiments/20260618-g12-anomaly`, 2026-06-18) runs the anomaly check
using an ASSUMED `Y` table and its own docstring states plainly "B−L not
yet geometric" at that point; `g15_hypercharge.py`
(`experiments/20260619-g15-hypercharge`, one day LATER, 2026-06-19) then
derives `B-L` independently from the `SO(6)⊃SU(3)×U(1)` embedding — and
reproduces the SAME numeric values G12 had already assumed the day before
(`g15_hypercharge.py` T10, PASS). A later geometric derivation landing
exactly on values an earlier, ungeometrized anomaly check had assumed is a
nontrivial cross-check, not a fit (a fit would require the anomaly
condition to have been used to CHOOSE `B-L`'s value, which is chronologically
impossible here) — though for System A specifically, `B-L` is not FITTED
either, since it is simply ABSENT (no value has ever been proposed for it
at all, fitted or derived).

**BLOCKED is the honest verdict**, per the pre-registered criterion's own
wording: "the gauge provenance... cannot be established from what this
project has already written down" applies precisely to `B-L`'s status on
System A's twisted kernel (Part A.7, Part C). This is a **narrower**
BLOCKED than round92's: round92 was blocked by BOTH the `B-L`-value gap
AND an apparent formula ambiguity; this experiment closes the formula
ambiguity cleanly (Part B) and leaves only the `B-L`-value gap, now
stated in its sharpest form yet: not "no numeric value has been assigned"
(vague) but "no OPERATOR has ever been constructed relating the twisted
kernel's Hilbert space to ANY weight-labeled basis where a `B-L` charge
would even be well-defined" (Part A.7).

---

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result kills:** the reading, implicit in round92's framing
  and in the user's own cautious "register as UNRECONCILED, not assumed
  resolved" instruction, that `K_3` and `T_{3R}` might be genuinely
  different physical quantities requiring a nontrivial reconciliation
  argument. Direct matrix computation shows they are the identical
  operator; there is nothing to reconcile beyond correcting a
  documentation description. It also kills the possibility that this
  project's anomaly-cancellation computation (`preprint.tex:309-320`) is
  internally inconsistent about which hypercharge generator it uses — it
  is not; it consistently uses `T_{3R}` (under the label `K_3`) throughout.
- **What this result does NOT kill:** round83/91/92's own finding that no
  numeric `B-L` value has ever been assigned to the twisted S⁶-kernel —
  this experiment SHARPENS that finding (Part A.7: not just "no value,"
  but "no operator, on the relevant Hilbert space, exists at all") but does
  not resolve it. It also does not kill round85/E17's own `BLOCKED` on
  `t=0`/`t=1` coexistence, round91's System-A/System-B non-reconciliation,
  or G97/G98's own findings (both reused and, for G98, independently
  re-verified with a genuine basis-dependence clarification added).
- **What survives, confirmed stronger than before:** the project's own
  `T_{3R}`-based anomaly-cancellation computation (`g12_anomaly_check.py`,
  underlying `preprint.tex:309-320`) is now shown to be free of the
  internal-inconsistency risk round92 flagged as a live possibility — a
  genuine strengthening, achieved by code-level verification rather than
  prose-level argument, exactly the kind of check `audit-verification-
  gate.md`'s "agent's [VERIFIED] = your [INFERRED]" rule exists to force.

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Fix `preprint.tex:304-305`'s prose (and G16's own `decision.md:9`) to say `K_3` is the S³-side `SU(2)_R` generator, not an S⁶-side "SU(3)-harmonic" quantity | **DONE (2026-07-17, same day, follow-up commit):** `preprint.tex:304-305` corrected directly (formula unchanged, only the prose description of `K_3` fixed); G16's own `decision.md:9` left unchanged with an additive superseding note added above it (history preserved, matching this project's G74A-correction precedent) |
| Construct `B-L` (or ANY charge operator) on the twisted kernel's ambient space | Locate the specific `dim ker(D_{S6,twisted})=1` `G₂`-singlet vector (`dolan-casimir-g2su3`/round59) within a weight-labeled basis, exactly as round92's own Relaxation Map already specified — this experiment does not narrow that requirement further, only confirms it is the SOLE remaining blocker for the `U(1)_Y` side of Part C's census |
| Resolve `t=0`/`t=1` coexistence (round85/E17) | Still requires a stated 13D parent action (KT-1/E18), unaffected by this experiment |
| Reconcile System A and System B (round91) | Still open; this experiment's System B table (Part C) is reproduced only for contrast, not as a proposed resolution |

## Assumptions carried, unresolved

- `D_full²=D_{S3,t}²⊗I+I⊗D_{S6,twisted}²` (E2/E12) — presupposed throughout.
- `SU(2)_L`=left-translation (Convention A) — the qualitative findings
  (representation content, `K_3=T_{3R}` identity) are convention-
  independent; only which name (`L`/`R`) attaches to which sector depends
  on this choice.
- `t=1`'s kernel exists only under `c0=-2` — carried forward unchanged.
- The `dolan-casimir-g2su3`/round59 `dim ker=1` computation itself was NOT
  independently re-verified this round (reused by citation, exactly as
  round90-92 also did not re-open it).
- G98's own T1-T4/T7 gates (Clifford/so(7) closure sanity checks) were
  reused by citation, not independently re-derived this round; only T5
  (the `B-L`/`so(6)` commutator count) was directly re-run, with the
  basis-dependence clarification added.

## What this does NOT mean

1. Does **not** unblock round92 (E22)'s own endpoint-anomaly-audit
   `BLOCKED` verdict — one of its two blocking causes is closed here, the
   other (numeric `B-L` for the twisted kernel) is untouched and,
   independently, re-confirmed as the sole remaining blocker.
2. Does **not** claim `preprint.tex` is free of documentation errors — the
   opposite: it identifies and traces a specific, real prose error (K_3's
   stated geometric origin) to its exact source (G16's own `decision.md`),
   which this project should correct in a future documentation-only round
   (flagged in the Relaxation Map, not fixed here per this task's
   constraints).
3. Does **not** resolve round85 (E17)'s `t=0`/`t=1` coexistence `BLOCKED`,
   or round91's System-A/System-B non-reconciliation finding — both
   untouched, reused by citation.
4. Does **not** claim the `SU(4)` structure exhibited in Part D is
   physically irrelevant to this project in general — it is the same
   structure G6/G14/G15's own "4 of SU(4)" framing already uses to
   organize the untwisted S⁶ spinor's color/lepton content; what is new
   here is the explicit, tool-verified demonstration that this SAME
   structure cannot be promoted to a GAUGED symmetry without contradicting
   `B-L` (G98) or the project's own G97 isometry finding.
5. Does **not** affect this project's `N_gen=3` headline claim (the
   independently-established G73/G74A/G74B S⁶-only triality/index/
   chirality chain) — this experiment concerns only the separate,
   already-non-load-bearing S³-side torsion-escape-route program and its
   hypercharge/anomaly bookkeeping.
6. Does **not** re-derive or challenge any of G6/G11/G12/G15/G16/G17/G97/
   G98/E9-E22's own tool-verified results — all reused here purely by
   citation, except G98's T5 (re-run directly, with a basis-dependence
   clarification, not a correction of its PASS/FAIL content).
7. Nothing in this experiment was submitted, posted, or sent anywhere
   external; this project's standing rules (no arXiv submission, no
   contact with Tom Lawrence, `lambda=FREE_COUPLING_PARAMETER`,
   `safe_for_runtime=False`) are unaffected and were not approached. No
   existing file was modified — only this new folder was created.

## Pearl-registry candidate

**Observation, concrete enough to flag:** a `decision.md` summary written
the same day as its own script, describing that script's own result in
PROSE, directly contradicted the script's code and the script's own
inline comments (`g16_t3r_k3.py` vs `g16_t3r_k3/decision.md:9`) — and this
contradiction survived, undetected, through THREE later rounds (round90,
91, 92) that each cited `preprint.tex`'s prose (itself downstream of the
wrong `decision.md` summary) without tracing back to the underlying code.
**Falsifiable prediction, if pursued:** any future round that encounters an
apparent physical ambiguity or inconsistency stated in `preprint.tex`'s
PROSE should, before accepting it as a genuine physics gap, grep the
actual Python source for the object in question and check whether the
code's own construction agrees with the prose description — a fast, cheap
check (this round: ~15 minutes) that here overturned what three prior
rounds had treated as an open physical question. **Impact score ~6** (this
pattern — decision.md prose drifting from its own script, then propagating
into preprint.tex, then surviving multiple citation-only rounds — could
recur anywhere else in this project's ~90 rounds of decision.md files;
worth a general documentation-consistency sweep, not just this one
instance). `next_check`: before promoting any future "unreconciled formula"
or "apparent inconsistency" finding that is based on reading `preprint.tex`
prose alone, grep the underlying experiment's own script for the actual
construction, exactly as this round did.

## Check (reproduces this decision)

```
cd experiments/20260717-round93-charge-operator-representation-lift
python e23_charge_operator_provenance.py
```

Expect (from the script's own `verdict` dict, printed at the end):
`T3L_G11_matches_G6_on_shared_basis=True`,
`T3R_G11_matches_G6_on_shared_basis=True`,
`K3_equals_T3R_as_32x32_operator=True`,
`no_s6_side_k3_construction_found_in_code=True`, `J3_K3_commute=True`,
`K3_commutes_with_all_8_su3_generators=True`,
`BmL_commutes_with_all_8_su3_generators=True`,
`BmL_commutes_with_S6_chirality=True`,
`BmL_commutes_with_n_of_15_raw_so6_basis_generators=3`,
`BmL_commutes_with_su3_plus_u1_subalgebra_dim9=True`,
`BmL_commutes_with_full_so6_su4=False`,
`BL_commutator_with_D_S6_twisted_computable=False`, `s_plus_dim=4`,
`s_minus_dim=4`, `chirality_split_is_4_plus_4bar=True`,
`full_so6_preserves_chirality_split=True`, `su4_is_isometry_of_s6=False`,
`su4_preserves_bl_charge_fully=False`, `su4_anomaly_route='NOT_APPLICABLE'`.
Every source number and citation is given in a comment immediately above
its assignment, tracing to a specific prior experiment's file (G6, G10,
G10-B, G11, G12, G15, G16, G17, G97, G98, KT-6), each independently `Read`
this round (not from memory or paraphrase) at the exact line ranges cited
in Parts A-D above.
