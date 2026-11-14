---
# C192 — independent cross-check of C191's SO(4)×SO(4) branching via pygae/clifford

**Date:** 2026-09-09
**FL tier:** [x] Full (research claim touching OB1/H1c via C191, per project CLAUDE.md)
**Question type:** [x] descriptive (does C191's P10 result reproduce under an
independently-written Cl(8) construction — not a causal or predictive claim)

---

## Why this round exists

`falsification-ladder.md`'s own Independent Verification Strength Ladder
ranks "same model, isolated context" as Weak-Medium and "independently-written
code" as Strong. This round independently rebuilds the `Γ_i` generators
(`so4xso4_branching.py`'s numpy Kronecker products of Pauli matrices, 16×16)
via `pygae/clifford`'s own geometric-product engine (256×256, the left-regular
representation of Cl(8,0) on itself).

**Corrected after skeptic review (Step 8a), before this claim was trusted at
its original framing — see `decision.md` § Skeptic Concerns for the full
response matrix:** everything downstream of the `Γ_i` — the `so(4)_1`
embedding formulas, `Γ_A=Γ_1Γ_2Γ_3Γ_4`/`Γ_B=Γ_5Γ_6Γ_7Γ_8`/`Γ_9=Γ_AΓ_B`, the
`L_a`/`R_a` self-dual/anti-self-dual combinations — reuses C191's own
algebraic formulas verbatim, not independently re-derived. **The rung this
round actually occupies is Medium** ("different matrix realization of the
same anticommutation relations, same algebraic formulas layered on top"),
**not Strong.** A bug in the shared formulas (wrong subgroup, wrong `Γ_9`
sign) would be inherited and reproduced identically here, not caught. What
IS independent, and cannot be forced by shared formulas alone: the raw
`Γ_i` matrices themselves, and the fact that the SAME calibration scale
(fixed from `V_S` alone, § Method step 6) reproduces the identical content
on `V_C` without being re-fitted per sector (`decision.md` § What Q16
Actually Shows).

User request, verbatim intent: "возьми C191's branching и прогони через
pygae/clifford."

## Prior Result Gate

1. `so4xso4_branching.py` (2026-07-15, pearl_registry): the reused 16×16
   Cl(8) construction, `Γ_A`, `Γ_B`, `Γ_9`. Cited, not rebuilt in the original
   sense — this round rebuilds it independently on purpose.
2. `C191` (`experiments/20260909-c191-*`): `P8`–`P10` — restricting the known
   `SU(2)^4` branching to the first `so(4)` factor gives `8_s` and `8_c`
   IDENTICAL `(j_L,j_R)` content, `4×(1/2,0)+4×(0,1/2)` each. This is the
   specific result under test.
3. **Novelty check:** `grep -rl "pygae\|clifford" experiments/` — 0 hits
   before this round. No prior round in this project used a third-party
   Clifford-algebra library; all Cl(8)/Spin(8) work has been hand-rolled.
4. **Status:** [x] NEW (the cross-check method; the underlying algebraic
   claim under test — P10 — is C191's, not new here).

## Falsifiable claim

Building Cl(8,0)'s left-regular representation via `pygae/clifford`
(256-dim, 16 independently-constructed copies of the 16-dim Dirac spinor
rep), restricting to the first `so(4)` factor's `su(2)_L×su(2)_R`, the joint
`(j_L,j_R)` content of the `Γ_9=+1` block (`8_s`-type) and `Γ_9=−1` block
(`8_c`-type) is **identical**, matching C191's `P10` up to the expected
factor of 16 (16 copies of the same 8-dim content).

## Kill criterion

**REJECTED** if the `pygae/clifford`-derived content for `8_s` and `8_c`
DIFFERS after calibration — i.e. if C191's `P10` (identical content) does
NOT reproduce under this independently-written construction.
**[Corrected after skeptic review — the original wording here conflated two
different failure modes, per `decision.md` § Skeptic Concerns:]** since this
round reuses C191's own `so(4)_1` embedding and `Γ_9` sign formulas (§ Why
this round exists), a mismatch would NOT distinguish "convention artifact"
from "fact about the abstract algebra" — any faithful representation of the
same algebra with the same formulas on top of it must agree, by definition
of "same abstract algebra." A mismatch would instead mean a **bug** in one
of the two `Γ_i` realizations (this round's left-regular construction, or
C191's Kronecker-product one) — a real, checkable finding either way, just
not the "convention vs. reality" framing originally written.

## Method

1. `clifford.Cl(8)` — signature `[1]*8` (Euclidean, matches the project's
   `{Γ_i,Γ_j}=2δ_ij` convention exactly).
2. `Γ_i` = matrix of left multiplication by basis vector `e_i` on the full
   256-dim multivector space (extracted column-by-column via `(e_i * blade)`
   for every one of the 256 basis blades) — mechanically generated from
   `clifford`'s own geometric-product structure constants, not typed by hand.
3. Positive control on the construction itself: `{Γ_i,Γ_j}=2δ_ij` on all 256
   matrices (`Q1`, the real evidence this is a valid Cl(8) representation).
   `Q2` (each `Γ_i` symmetric) is a forced structural consequence of
   orthogonal+involutive on a real signed-permutation representation, not an
   independent verification of anything — **[corrected per skeptic review]**
   noted for completeness, not counted as adding epistemic weight.
4. `Γ_A`, `Γ_B`, `Γ_9` built the same way as `so4xso4_branching.py`;
   `Γ_9=±1` eigenspaces extracted via projector + `eigh` (mirrors the
   original script's `_proj` approach, more numerically stable than a raw
   `eig` on a matrix not guaranteed diagonalizable by an orthogonal basis).
5. `so(4)_1`'s `su(2)_L×su(2)_R` generators built the REAL way (no `i`
   factor — `Γ_i` here is real-symmetric, not complex-Hermitian, so
   `Γ_i@Γ_j` for `i≠j` is already the natural real antisymmetric generator).
6. **Calibration, not assumption:** the raw commutator closure was checked
   for a SINGLE consistent scale factor (found: `k=−2` exactly, `std=0`
   across every nonzero entry). **[INFERRED, corrected after skeptic
   review]** this is not an empirical surprise — it is a direct, 3-line
   algebraic consequence of the `M(i,j)=0.5·(Γ_iΓ_j−Γ_jΓ_i)=Γ_iΓ_j`
   (for `i≠j`, since `{Γ_i,Γ_j}=2δ_ij`) normalization chosen in this round:
   `[Γ_1Γ_2,Γ_1Γ_3] = Γ_1Γ_2Γ_1Γ_3 − Γ_1Γ_3Γ_1Γ_2 = −Γ_2Γ_3−Γ_2Γ_3 =
   −2·Γ_2Γ_3`. It was found empirically first (`diag_q8.py`) and only
   derived afterward — the original framing overstated this as a "diagnosed
   via probe" discovery in the C186 sense (a wrong relative sign that a
   commutator catches and a Casimir hides); it is instead a known
   consequence of the normalization choice, catchable by inspection. The
   commutator check itself is still real (it verifies closure holds AT ALL,
   with a SINGLE consistent constant, not that the constant is surprising).
   The Casimir spectrum was then independently calibrated against the KNOWN
   `j=1/2` value (`j(j+1)=0.75`) before any new content was trusted — same
   "positive control before the negative" discipline as C191's own `P8/P9`.
   `Cl(8,0)≅Mat(16,ℝ)` (Bott periodicity / ACC classification, `8 mod 8=0`)
   `[DOCS, standard, not independently re-derived in this round]` — the
   "256=16×8, 16 copies" reading of `Q7`/`Q14` relies on this cited fact
   rather than an internal irreducibility check.

## What was found

**All 17 checks pass** (`Q0`–`Q16`, `run_output.txt`). The calibration step
(`Q13`) found exactly one nonzero Casimir eigenvalue on `V_S` (`3.0`), giving
scale `0.25`. Under that calibration, `8_s`-block content = `8_c`-block
content = `64×(1/2,0) + 64×(0,1/2)` (`Q14`/`Q15`), and the two sectors are
**identical** (`Q16`), reproducing C191's `P10` through an independently
constructed set of `Γ_i` generators (§ Why this round exists — the layer
above `Γ_i` is shared with C191, not independently re-derived).

**[Corrected framing, per skeptic review]** the informative content of
`Q14`/`Q15` is NOT the factor of 16 (that follows from `Cl(8,0)≅Mat(16,ℝ)`
almost by arithmetic once the construction is trusted at all — see § Method
step 6) — it is that only TWO of the four possible `(j_L,j_R)` types appear
(`(1/2,0)` and `(0,1/2)`, not `(1/2,1/2)` or `(0,0)`), and the split is
exactly `64:64`, not some other ratio. That is the actual reproduction of
C191's specific content, not the scaling itself.

`Q8`/`Q9` failed on the first run against an assumed `±1` structure
constant, then passed once corrected to test for any single consistent
scale (found: `comm(L1,L2) = −2·L3` exactly). **[Corrected, per skeptic
review]** this is not a subtle discovery in C186's sense (a wrong relative
sign a Casimir would hide and only a commutator catches) — it is a direct,
three-line algebraic consequence of this round's own `M=Γ_iΓ_j`
normalization (§ Method step 6). It was found empirically before being
derived, which is a legitimate order of operations, but the original write-up
overstated its significance; recorded honestly here rather than left as
originally framed.

## Negative control

The construction's own internal positive control IS the calibration step:
`Q13`/`Q14` require the pygae/clifford-derived content to match the ALREADY
KNOWN row-58 branching (scaled ×16) before `Q15`/`Q16`'s negative-adjacent
comparison (identical `8_s`/`8_c`) is trusted at all. A machinery that could
not reproduce the known-correct branching would make `Q16` uninterpretable;
it does reproduce it exactly, so `Q16` is informative.

## Kill Analysis

**What this round killed:** the possibility that C191's `P10` finding
(`8_s`=`8_c` content under `so(4)_1` alone) was an artifact of the specific
16×16 Kronecker-product `Γ_i` REALIZATION `so4xso4_branching.py` uses (as
opposed to the shared algebraic formulas layered on top, § Why this round
exists — those were NOT independently tested).
**What survives:** C191's own `P10` — now independently reproduced at the
`Γ_i`-realization layer — stands strengthened, at a **Medium** rung on the
Independent Verification Strength Ladder (not Strong, corrected per skeptic
review — see `decision.md` § Skeptic Concerns for why).
**Not touched:** C191's own REJECT verdict on claim (a), the steelman
(`P14`/`P15`), role-swap (`P16`/`P17`), or split-identification (`P18`–`P22`)
sections — none of those were re-derived here; only the naive-reading
content comparison (`P8`–`P10`) was cross-checked, and only at the `Γ_i`
layer, not the algebraic formulas above it.

**Revival condition:** not applicable — this is a confirmatory round, not a
killed claim awaiting revival.

## What this does NOT establish

- **[HIGH, per skeptic review]** does not independently re-derive the
  `so(4)_1` embedding formulas, the `Γ_A`/`Γ_B`/`Γ_9` construction, or the
  `L_a`/`R_a` self-dual split — these are shared with C191 verbatim. A bug
  in any of THESE (wrong subgroup, wrong sign in `Γ_9`) would be inherited
  and reproduced identically by this round, not caught by it. Only the raw
  `Γ_i` matrices are independently constructed.
- Does not re-derive C191's steelman, role-swap, or split-identification
  sections (`P11`–`P22`) — only the naive-reading content comparison
  (`P8`–`P10`) was cross-checked via independent machinery.
- Does not touch whether the P5 postulate itself (identifying `S³`'s
  isometry with a `Spin(8)`-fiber `so(4)` factor) is physically motivated —
  orthogonal to this round, which only re-verifies a representation-theoretic
  computation.
- Does not change `OB1/H1c`'s `PARKED` status.
- The `k=−2` normalization difference is NOT derived from first principles
  here — only measured empirically and shown consistent across every
  generator pair checked. A full symbolic derivation of why this project's
  `0.25j` convention and this round's real-antisymmetric convention differ
  by exactly `−2` is not attempted (not needed for the cross-check to be
  valid — the empirical calibration in `Q13` is what licenses trust,
  independent of understanding the scale's origin).

## Floor–Ceiling (Step 4a)

Discrete metric (does the independently-derived content match C191's, after
calibration: yes/no), not a continuous statistic — same shape as C191's own
Floor-Ceiling note. Floor = the calibration itself failing to reproduce the
KNOWN row-58 result (would make the whole construction untrustworthy).
Ceiling = exact match, scaled by the known multiplicity factor (16). Observed
= exact match (`Q14`, `Q15`) — the construction lands on the ceiling, not
partway.

## Reproduction

```
cd experiments/20260909-c192-so4xso4-pygae-clifford-crosscheck
pip install clifford   # pygae/clifford 1.5.1, BSD-3
python c192_pygae_clifford_crosscheck.py
```

`17/17`. `ruff check` and `ruff format`: clean.
