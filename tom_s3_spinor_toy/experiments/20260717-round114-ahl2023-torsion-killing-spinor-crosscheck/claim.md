# Round114 — Claim

**OB1 mechanism search.** `PARENT_ACTION_GATE.md` item 24 (Bismut torsion
Dirac operator) and item 25 (compare the whole one-parameter connection
family, check ker/spec/index stability in `t`) from the
`100_DIRECTIONS_BRAINSTORM_2026-07-17.md` document, both flagged by that
document's own adversarial critique as among the highest-priority items
("Наиболее ценные пункты: 21, 25...").

**Source found this round:** `Agricola_Hofmann_Lawn_2023_invariant_spinors.pdf`
(arXiv:2203.02961v3, "Invariant Spinors on Homogeneous Spheres", Agricola/
Hofmann/Lawn, 2023) — already downloaded in this repo but never read in
any of rounds 67-113. Read directly via pymupdf this round, not from
memory. This paper independently classifies invariant/Killing spinors on
`S^{2n+1}=SU(n+1)/SU(n)` for general `n`; for `n=1` this is `S³=SU(2)/{e}`,
**the exact presentation round67/preprint.tex use** for the KT-8 torsion
escape route.

Key results read directly from the PDF, verified present (not paraphrased
from memory):
- **Theorem 3.7**: for any metric parameters `a,b>0`, the invariant-spinor
  space is exactly 2-dimensional — for `n=1` specifically, the isotropy
  group is trivial (`SU(1)={e}`), so *every* spinor is invariant (matches
  round67's own finding that Kostant's torsion element `H` acts as a pure
  scalar on the whole 2-dim spinor space for `S³` specifically, via an
  independent, general classification-theoretic route, not the same
  argument).
- **Theorem 3.13** + **Corollary 3.14**: at the round metric
  (`a=n/(n+1)`, `b=1/2`), the invariant spinors `ψ±` are genuine Killing
  spinors with eigenvalue `1/2` (for `n=1`).
- **Remark 3.16 + Proposition 3.17**: a **1-parameter family of invariant
  connections with skew torsion**, `∇^s = ∇^{g_ε} - εs·Φ∧η`, `s∈ℝ`,
  with an **explicit closed-form generalized-Killing-spinor endomorphism**
  `A^s_±` as a function of `s` — for `n≠2,3` (so `n=1` is covered).

## L0 gate (EstimandOps)

**Question type: Descriptive.** Computing a Dirac-operator eigenvalue from
an already-published closed-form endomorphism formula, and comparing the
result to this project's own already-established value, is arithmetic on
established definitions — not causal or predictive.

## Falsifiable claim

Using `Proposition 3.17`'s own `A^s_+` endomorphism (`n=1`, round metric
`ε=-1`) and this paper's own stated Clifford relation
(`vw+wv=-2β(v,w)·1`, §2.1, matching round67/round99/round113's own
`{Z_i,Z_j}=-2δ_ij` convention exactly), build the actual Dirac operator
`D^s(ψ_+) := Σᵢ eᵢ·A^s_+(eᵢ)·ψ_+` explicitly via sympy (not by hand), using
the paper's own stated Clifford-representation formulas (§2.1, eq. 4-6),
and:
1. Verify the resulting `2×2` matrices for `e1,e2,e3` satisfy
   `{eᵢ,eⱼ}=-2δᵢⱼ` exactly (sanity check on the hand-transcription from the
   PDF before trusting anything downstream).
2. Compute `D^0` (Levi-Civita, `s=0`) and check it matches round67's own
   cited eigenvalue `±3/2` (up to sign/branch convention — the two papers'
   sign conventions for the Dirac operator itself have not been shown
   identical, only the Clifford relation has).
3. Find the zero-crossing(s) in `s`, if any exist.

## Kill criterion (pre-registered)

- If step 1's sanity check **fails** (transcribed matrices don't satisfy
  the Clifford relation) → this round's own construction has an error;
  STOP, do not trust steps 2-3, report `BLOCKED-BY-TRANSCRIPTION-ERROR`.
- If step 1 passes and step 2's magnitude **matches** `3/2` (regardless of
  overall sign) → genuine, independent cross-check of round67's own
  `h_H=3` calibration via a completely different, independently-published
  2023 paper — a real, if modest, new piece of evidence (Independent
  Verification Strength Ladder: "independently-written source," per
  `falsification-ladder.md`).
- If step 2's magnitude does **not** match `3/2` → either a genuine
  discrepancy between the two constructions (worth flagging precisely,
  since they claim to describe the same underlying object — `S³=SU(2)/{e}`
  with the round metric), or this round's own construction of `D` from
  `A` (`D:=Σeᵢ·A(eᵢ)`, an assumption not explicitly stated as such in the
  paper for this specific case) is not the right way to build the Dirac
  operator from this paper's own data — report honestly as `INCONCLUSIVE`,
  not as a refutation of round67.
- If a zero-crossing in `s` exists → report its value; do **not** claim
  this by itself supplies a parent action (a value of `s` where `D=0` is
  the SAME kind of "mathematically available crossing, no known selection
  principle" situation round67 already found for `t` — this round's
  contribution, if positive, is an independent cross-check of the
  mechanism's mathematical soundness, not a resolution of the selection
  question).

## What this does NOT mean (pre-registered)

1. Does NOT itself supply a parent action or resolve OB1's central
   question (why `t=0,1` specifically) — even a successful cross-check
   only strengthens confidence in the MATHEMATICS of the torsion-Dirac
   construction, not the PHYSICS of why nature would select any specific
   crossing.
2. Does NOT establish that this paper's `s`-parameter and round67's
   `t`-parameter (or round99/round111/round113's `t`) are the same
   parameterization — that would require its own explicit reparameterization
   check, not attempted here unless the magnitude cross-check in step 2
   succeeds first.
3. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.
4. Does NOT constitute re-deriving this paper's own theorems — Theorem 3.7,
   3.13, Corollary 3.14, Proposition 3.17 are cited/reused, not
   re-proven; only the NEW combination (building `D` from `A` and finding
   its zero-crossings) is this round's own computation.
