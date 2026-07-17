# Convention Reconciliation Table — S³ torsion-connection family

**Compiled:** 2026-07-17, Round 84 (see `claim.md` for the naming note — this is
not the project's own `E13`, which is `experiments/20260717-round79-multiplicity-reconciliation-attempt/`).
**Purpose:** one citable reference for the sign/orientation/labeling conventions
used throughout E2/E7/E9/E10/E11/E12/E14/E15/E16, so future rounds (starting with
E17) do not have to re-derive or re-litigate them. Every entry below traces to an
existing file:line — no new convention is introduced here.

---

## 1. Orientation of S³

| Field | Content |
|---|---|
| **Current convention** | The tangent space at each point is spanned by the fixed frame `{Z_1,Z_2,Z_3}` built from `Z_i=i·σ_i` in that fixed order, reused byte-identically in every experiment (see row 3). This fixes a definite orientation implicitly — "positively oriented" means "oriented so that `[X_i^L,X_j^L]=c0·ε_{ijk}X_k^L` with `c0=-2`" (round76 Part 1) — but no experiment or `preprint.tex` ever attaches an explicit "right-handed" / "left-handed" LABEL to this choice. The project's gauge-group construction restricts to the **connected** component `SO(4)` of the full isometry group `O(4)` (equivalently, restricts to orientation-PRESERVING isometries only). |
| **Source** | `preprint.tex:274,279` — `Iso(S³×S⁶)=SO(4)×SO(7)` (connected component only, `SO`, not `O`); `experiments/20260717-round80-z2-left-right-symmetry-search/e14_z2_left_right_symmetry.py` `run_part_a`, reported in `decision.md:53-58` (`det(J)=-1` for the antipodal/inversion map `ι:g↦g⁻¹`, confirming `ι` is orientation-REVERSING and therefore lies in `O(4)∖SO(4)`, i.e. genuinely outside the gauge group). |
| **Status** | **FIXED (implicitly, by reuse) — but never explicitly named.** Every downstream experiment inherits the SAME concrete frame, so there is no internal inconsistency; the gap is purely one of an unstated label, not a substantive ambiguity. |
| **What would resolve the gap (if ever needed)** | A one-line addition to `preprint.tex` or a future decision.md stating explicitly: "the frame `{Z_i=i·σ_i}` in this fixed order is defined to be positively/right-handed oriented on S³." Not currently needed for any existing result — flagged here purely so a future experiment does not have to reconstruct this from round80's `det(J)=-1` fact. |

---

## 2. Sign of `[e_i,e_j]` — abstract `c=+2` vs concrete `c0=-2`

| Field | Content |
|---|---|
| **Current convention** | TWO distinct, both-legitimate quantities coexist and must not be silently conflated: <br>**(a) Abstract `c` (physics-calibrated, `c=+2`)** — a free symbolic bookkeeping parameter in `∇^t_XY=t[X,Y]_m`, fixed to `c=2` only via an INDEPENDENT physics fact (Kostant cubic element `H=(3c/2)ω` calibrated against this project's own established n=0 eigenvalue `3/2`, giving `h_H=3 ⟺ c=2`). Used for scalar/algebraic bookkeeping (eigenvalue spectrum, `H` calibration). <br>**(b) Concrete `c0` (literal, `c0=-2`)** — the LITERAL structure constant obtained by directly computing `[X_i^L,X_j^L]` via ordinary vector-field brackets on the concrete Pauli/quaternion realization `g(x)=x0·I+Σx_i Z_i`. Found, not assumed, in round76 Part 1. |
| **Source** | Abstract `c=2`: `experiments/20260717-round73-e9-explicit-parallel-spinor/claim.md:21-24` ("Kostant cubic element `H=(3c/2)·ω`... calibrated `h_H=3` (⟺ `c=2`..)"), reusing `experiments/20260717-round67-e2-s3-torsion-deformation/claim.md:48-51`. Concrete `c0=-2`: `experiments/20260717-round76-e9followup-right-invariant-frame/decision.md:26-37` (`[X_i^L,X_j^L]=c0·ε_{ijk}X_k^L, c0=-2` — "found, not assumed"; `c0_right_equals_minus_c0_left = true`). |
| **Status** | **CONVENTION CHOICE — both valid, NOT interchangeable; a rule is needed for which to use when.** Round76 Part 1 tool-verified these differ ONLY in sign, not otherwise. |
| **Recommendation (definitive, going forward)** | Use **`c0=-2`** (the concrete, literal sign) whenever a computation requires an actual concrete vector field / directional derivative on the manifold realization (spin connections `Ω_i(t)` evaluated at a specific `t`, parallel-transport checks, anything that differentiates along `Z_i` or `X_i^{L/R}`) — round76 Part 3 explicitly found that "the abstract, symbolic `c` cannot substitute here because directional derivatives require an actual, concrete vector field" (`decision.md:99-101`). Reserve the abstract **`c=+2`** strictly for purely scalar/algebraic statements tied to the ORIGINAL Kostant-element physics calibration (e.g., citing `H=3·I₂`, the eigenvalue-spectrum bookkeeping of E2). **Do not substitute `c=+2` into any formula that is about to be differentiated or evaluated on concrete matrices** — this is exactly the mistake that made round76 Part 4's `c=+2` spinor candidate fail while the `c0=-2` one succeeded (`decision.md:146-168`). |

---

## 3. Clifford algebra convention

| Field | Content |
|---|---|
| **Current convention** | `Z_i = i·σ_i` (Pauli matrices), giving `{Z_i,Z_j} = -2δ_ij·Id` exactly. |
| **Source** | First stated `experiments/20260717-round67-e2-s3-torsion-deformation/e2_s3_torsion_deformation.py:100-107` (`clifford_generators()`, docstring: "`Z_i = i*sigma_i`, giving `{Z_i,Z_j} = -2 delta_ij` (Cl(0,3) convention...)"), verified exactly at lines 110-120 (`verify_clifford_relations`, all 6 pairs checked). |
| **Confirmation this round** | Grepped `pauli_matrices`/`clifford_generators`/`Z_i = i*sigma_i` across every script in `experiments/20260717-round6[7-9]*`, `round7*`, `round8*` this round (not merely cited from a prior report): **byte-identical** convention found in ALL of — `round67/e2_s3_torsion_deformation.py:100-107`, `round73/e9_explicit_parallel_spinor.py:97-98`, `round76/e10_right_invariant_frame.py:94-95`, `round77/e11_su2lr_representation_check.py:74-75`, `round78/e12_multiplicity_gate.py:83` (+ comment line 69), `round80/e14_z2_left_right_symmetry.py:79-80`, `round81/e15_chirality_grading_check.py:116-117`, `round83/e16_joint_representation_check.py:79`. **Zero divergent instances found.** (`experiments/20260615-g6-s3xs6-spinor-content/g6_spinor_decomposition.py`, the earlier bookkeeping-only script cited in round83, defines no Clifford matrices at all — it operates purely on `(T3L,T3R,chir_s3)` labels, so there is no competing convention there either, just a different layer of abstraction.) |
| **Status** | **FIXED — single convention, no exceptions found.** |

---

## 4. Spin lift

| Field | Content |
|---|---|
| **Current convention** | `Ω_i(t) = -(tc/2)·Z_i` — the standard spin lift of the `so(3)`-valued frame connection `Γ^k_{ij}(t)=t·c·ε_{ijk}` (via `Ω_i(t)=(1/4)Σ_{j,k}Γ^k_{ij}(t)·Z_j·Z_k`), applied to this project's own `∇^t`. |
| **Source** | Derived and verified `experiments/20260717-round73-e9-explicit-parallel-spinor/decision.md:13-30` (§1, exact result `Ω_i(t)=-(tc/2)Z_i`), reused unchanged in `experiments/20260717-round76-e9followup-right-invariant-frame/decision.md:50-51` (right-invariant mirror, `Ω_i^right(t)=+(tc/2)Z_i`) and cited throughout E11/E12. |
| **Does the c=+2 vs c0=-2 ambiguity (item 2) propagate into this formula's numerical use?** | **YES, directly and consequentially.** Round76 built `Ω_i^right(1)` under BOTH values: under `c=2` (E9's abstract calibration), solving `Ω_i^right(1)ψ=0` gives ONLY the trivial solution (`decision.md:60-68`, "t1_only_trivial_via_solve = true"); under `c0=-2` (the concrete realization), the explicit candidate spinor `ψ=ḡ(x)ψ₀` is EXACTLY `∇¹`-parallel (`decision.md:129-145`). These are genuinely different numerical outcomes for the literal same formula `Ω_i(t)=-(tc/2)Z_i`, depending purely on which value of `c` is substituted — this is the concrete demonstration of why item 2's resolution rule matters operationally, not just formally. |
| **Status** | **FIXED formula; numeric substitution governed by item 2's rule.** Any future use of `Ω_i(t)` in a concrete (as opposed to purely symbolic-in-`c`) computation MUST state explicitly which value of `c` was substituted and why, per item 2's recommendation. |

---

## 5. Correspondence `t=0` / `t=1` ↔ left-invariant / right-invariant frame

| Field | Content |
|---|---|
| **Current convention** | `t=0` is parallelized by the **left-invariant** frame **unconditionally** (holds for ANY sign/value of the structure constant — `Ω_i(0)=0` identically regardless of `c`). `t=1` is parallelized by the **right-invariant** frame, but this has been constructed and verified **only under `c0=-2`** — the identical candidate spinor demonstrably FAILS under the project's own abstractly-calibrated `c=+2` (see item 2/4). |
| **Source** | `t=0` unconditional: `experiments/20260717-round73-e9-explicit-parallel-spinor/decision.md:44-62` (§3, "any constant left-invariant spinor... `D^0ψ=0` exactly"; §"Bonus generalization," `t=0` is the UNIQUE root of `det(Ω_1(t))=(tc/2)²` for any nonzero `c`). `t=1` under `c0=-2` only: `experiments/20260717-round76-e9followup-right-invariant-frame/decision.md:129-168` (§Part 4, explicit spinor `ψ=ḡ(x)ψ₀` found parallel under `c0=-2`, fails under `c=+2`). |
| **Status** | **FIXED for `t=0` (unconditional). CONVENTION-DEPENDENT / partially open for `t=1`** — the `t=1` ↔ right-invariant correspondence is established ONLY in the `c0=-2` convention; whether an (as-yet-unconstructed) DIFFERENT candidate spinor realizes it under the project's own `c=+2` calibration remains open (round76's own "Recommended next action," not attempted anywhere in this project to date). |
| **Definitive single-entry statement (for citation)** | "`t=0` ↔ left-invariant frame (unconditional, any sign of `c`); `t=1` ↔ right-invariant frame (established only under `c0=-2`; NOT yet shown, and by the one candidate tried, demonstrably fails, under this project's own physics-calibrated `c=+2`)." Cite this exact sentence rather than the shorter, caveat-free "t=0↔left, t=1↔right" — the shorter form has already caused one near-overclaim (round77 had to re-flag it, `decision.md:130-136`). |

---

## 6. Representation labels `SU(2)_L` / `SU(2)_R` — physical identification

| Field | Content |
|---|---|
| **Current convention** | `preprint.tex` uses `\mathrm{SU}(2)_L` / `\mathrm{SU}(2)_R` **only as representation-content labels** (standard Pati–Salam/SM convention: `SU(2)_L` doublet = weak-isospin-charged, left-handed content; `SU(2)_L` singlet = right-handed content, e.g. `ν_R`). `preprint.tex` never states which of the two candidate GEOMETRIC actions on `S³=SU(2)` — left translation `g↦hg` or right translation `g↦gh⁻¹` — IS the physical `SU(2)_L`. |
| **Source — representation-content usage** | `preprint.tex:273-279` (`SO(4)≅SU(2)_L×SU(2)_R` from the bi-invariant round metric on S³, gauge algebra `SU(3)_c×SU(2)_L×SU(2)_R` from `Iso(S³×S⁶)=SO(4)×SO(7)`); `preprint.tex:300-304` (electric charge `Q=T_{3L}+Y`); `preprint.tex:331-334` (`ν_R` = neutral singlet, `SU(2)_L` singlet); `preprint.tex:884-912` (Lemma L5, "Matching the `S⁶` orientation convention to the SM convention for `SU(2)_L`, the left-handed Dirac zero mode corresponds to the left-handed SM fermion doublet"). |
| **Verification this round (re-grep, not cited from memory)** | `grep -c "SU}(2)_L" preprint.tex` → **12**; `grep -c "SU}(2)_R" preprint.tex` → **9**; `grep -n "left-invariant\|right-invariant\|left translation\|right translation\|acts on the left\|acts on the right" preprint.tex` → **0 hits, confirmed this round independently of round74/round77's own prior counts.** Also checked `preprint.tex:273-287` (the `Iso(S³×S⁶)` passage itself) and `:884-912` (Lemma L5) directly for any left/right-translation language — none found in either; both state representation-content pairings only. |
| **The one candidate anchor found (project-wide)** | `preprint.tex:331-334` + Lemma L5 (`:906-908`): IF one additionally *assumes* the imported (not paper-derived) convention `SU(2)_L`=left-translation, THEN the project's own already-constructed spinors give a clean match: `ψ⁽¹⁾` (the `t=1`, right-invariant-frame candidate) is an exact `SU(2)_L` doublet — matching S⁶'s independently-fixed "left-handed" label (Lemma L5) — while `ψ⁽⁰⁾` (`t=0`) is an `SU(2)_L` singlet, matching the `ν_R` ("right-handed") label. Source: `experiments/20260717-round77-su2lr-correspondence-test/decision.md:93-153` (§Part 3), reconfirmed independently in `experiments/20260717-round83-joint-representation-decomposition/decision.md:91-99`. |
| **Status** | **AMBIGUOUS — genuinely unresolved from existing project text.** This is not merely an unstated label (contrast items 1 and 4): it is a substantive fork that flips every downstream label in the table above (round77 `decision.md:122-129`: "if the convention is reversed... every label in the table above flips... nothing in `preprint.tex` or in this experiment's own computation can distinguish these two possibilities"). Three independent, stacked reasons block resolution (round77 `decision.md:112-153`, reconfirmed round83 `decision.md:271-275`): <br>(1) `SU(2)_L`=left-translation is an imported convention, not a stated or derivable one — `preprint.tex` grep-confirmed to contain zero occurrences of the relevant geometric language (see above); <br>(2) the candidate spinor `ψ⁽¹⁾` for which the match is checked exists ONLY under `c0=-2` (item 2/5), NOT under this project's own physics-calibrated `c=+2` — so the very object being labeled is not currently known to exist under the project's own calibration; <br>(3) no physical principle anywhere in this project requires the S³-factor zero mode to match S⁶'s left-handed label in the first place, and moreover `preprint.tex:1421-1495` (KT-8) establishes that **no zero mode of the full untwisted 9D operator currently exists at all** — so the entire question is, at present, about representation content of spinors in a connection family not yet tied to any actual physical zero mode of the operator the paper's physics depends on. |
| **What would resolve this (exactly)** | Any ONE of: (a) an explicit statement added to `preprint.tex` (or a new, independently-motivated derivation) fixing which of {left-translation, right-translation} is `SU(2)_L`, geometrically, on `S³`; (b) construction of a DIFFERENT candidate `t=1` spinor that survives under the project's own `c=+2` (closing gap (2) above, per round76's own "Recommended next action" — not attempted anywhere in this project); (c) an explicit physical principle, stated and justified, for why the S³-factor zero mode must carry the same chirality label as the S⁶ factor (closing gap (3)); (d) resolution of KT-8's blocking gap (whether any zero mode of the full operator exists at all), without which (a)-(c) address a construction that is not yet known to be physically realized. None of (a)-(d) is attempted in this round, per the task's constraint that this is a reconciliation task, not a new-derivation task — except that (a) was actively searched for (see "Verification this round" above) and confirmed absent. |

---

## Summary

| # | Topic | Status |
|---|---|---|
| 1 | S³ orientation | FIXED (implicit, by reuse; never explicitly labeled) |
| 2 | Structure-constant sign (`c=+2` vs `c0=-2`) | CONVENTION CHOICE — both valid, explicit conversion rule given |
| 3 | Clifford algebra convention | FIXED — single convention, zero exceptions found |
| 4 | Spin lift `Ω_i(t)` | FIXED formula; numeric substitution governed by item 2's rule |
| 5 | `t=0`/`t=1` ↔ left/right-invariant correspondence | FIXED for `t=0` (unconditional); CONVENTION-DEPENDENT for `t=1` (only under `c0=-2`) |
| 6 | `SU(2)_L`/`SU(2)_R` physical (geometric) identification | **AMBIGUOUS — genuinely unresolved**, three independent blocking reasons, all stated above |

5 of 6 topics reconcile cleanly into a single, citable statement (with item 5
carrying one explicit caveat, and item 2 carrying one explicit usage rule). Item 6
is the one genuine, currently-unresolvable-from-existing-text ambiguity — see
`decision.md` for how E17 should proceed given this.
