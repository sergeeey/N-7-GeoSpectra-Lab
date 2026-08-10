# OB10 Claim — geometric S³×S⁶ spinor bundle's reality/Majorana structure

**Date:** 2026-08-03
**FL tier:** [x] Standard (mathematical/structural claim, single self-contained computation)
**Question type:** [x] descriptive (algebraic classification of an existing construction, not causal)

---

## Prior Result Gate

1. Exact claim: does the geometric S³×S⁶ Clifford module (built from this
   repo's own already-established Cl(0,3) S³ generators and Cl(6,0) S⁶
   generators) admit a charge-conjugation-type reality structure, and if so
   which KO-type (real/pseudo-real/complex)?
2. `decision.md` grep (KO-dim, Majorana, reality condition, real structure):
   [x] done — hits reviewed: `experiments/20260619-g18-ncg-dirac-df/`,
   `g20-yukawa-intertwiner/`, `g23-chirality/`, `g26-ccm-comparison/` all
   concern **KO-dim 6 postulated for the FINITE algebra A_F only**
   (`J_F²=+1,{J_F,γ_F}=0,[D_F,J_F]=0` [sign corrected 2026-08-10, C36 — this
   line said `-1`], preprint.tex:354-355) — a different
   object from the GEOMETRIC bundle this claim is about. Non-transfer
   noted explicitly (Gate 1, artifact-provenance-gates.md): G18's verdict
   does not extend to this claim.
3. `round*_claim.md` + scripts grep: [x] done — `g89a-majorana-...` is
   about gauge-invariance of a Majorana MASS TERM (B-L selection rules),
   an unrelated question; no hits for the geometric-bundle reality
   question itself.
4. `null_results/` + `parked/` grep: [x] done, 0 hits for this exact
   question (pre-check on submit also matched G38-S2/G102/R45-Leibniz/
   S-T-cand/Round114-AHL2023 — all confirmed unrelated topics, see below).
5. `git log -S`/`-G` pickaxe: [x] done (via grep across full repo for
   "KO-dim", "Majorana", "quaternionic" etc.) — only hit is OB10's own
   entry in `OPEN_BLOCKERS.md`/`SPIN13_TO_SPIN4_DECOMPOSITION.md`/
   `CLAIM_LEDGER.yaml`, which explicitly states the gap, not a result.
6. Primary source re-read: [x] done — both `Agricola_2002_Dirac_naturally_
   reductive.pdf` (zero hits, doesn't treat S⁶/G₂ at all) and `Agricola_
   Hofmann_Lawn_2023_invariant_spinors.pdf` (§5.1 gives the Killing-spinor
   Theorem 5.1 for S⁶=G₂/SU(3) but states nothing about reality/KO-type;
   the only adjacent fact is Lemma A.1, Spin(7)'s real Δ7=R⁸, used for an
   unrelated Lie-algebra-chain purpose) read via Explore agent,
   `pdftotext -layout` full-text grep, see grounding report.
7. **Status:** [x] NEW — confirmed by direct search, not merely absence of
   a keyword match. `GLOBAL_RECOMPOSITION_AUDIT.md:60-69` (its own C19
   audit) already independently confirmed OB10 is genuinely new and does
   **not** feed into the `D2` zero-mode-counting argument either way.

**Null-results pre-check on submit matched 5 entries — all confirmed
unrelated on inspection:** `G38-S2` (spectral action minimum, energy
language), `G102` (SO(8) fiber-symmetry obstruction), `R45-Leibniz`
(structural-tautology index check), `S-T-cand` (index formula for a
different bundle E), `Round114-AHL2023` (Killing-constant cross-check,
already-falsified — cautionary precedent for not accepting a "cross-check"
that reduces to restating the source's own stated theorem; heeded here by
doing a from-scratch computation instead of citing a table).

---

## Estimand

**Population:** the 16-dimensional Clifford module carrying the product
Dirac operator's gamma matrices on S³×S⁶, as already constructed in this
project's own code (not a new bundle).
**Intervention:** none (descriptive/structural, not an intervention study).
**Comparator:** the finite NCG algebra A_F's own already-established real
structure J_F (KO-dim 6, J_F²=+1 [corrected 2026-08-10, C36 — said -1]).
**Endpoint:** existence and type (real / pseudo-real / complex, i.e.
B·conj(B) = +I / −I / no consistent B) of a charge-conjugation matrix B
satisfying B·Γ_a·B⁻¹ = η·conj(Γ_a) for all 9 generators simultaneously,
one shared sign η.
**Summary measure:** categorical classification (REAL / PSEUDOREAL /
COMPLEX), not a continuous statistic.
**MCID:** not applicable — this is an exact algebraic classification, not
a statistical estimate with a practical-significance threshold.

---

## Claim

The product Clifford module built from this repo's own established S³
(Cl(0,3)) and S⁶ (Cl(6,0)) gamma-matrix conventions and preprint.tex's own
stated tensor-product formula admits a genuine charge-conjugation
structure, and it is of **pseudo-real (quaternionic) type**, matching —
not contradicting — the finite algebra's own pseudo-real J_F²=−1.
   [VOID 2026-08-10, C36 + C32: this corroboration fails twice over. J_F² is
   **+1**, not −1, so the finite algebra is NOT pseudo-real in the sense claimed;
   and OB10's own pseudo-real verdict was itself a Clifford-convention artifact
   (C32). Two independent reasons this sentence supports nothing.]

Supporting sub-claims:
1. The naturally-constructed 9-generator product Clifford algebra has
   MIXED signature Cl(6,3), not the uniform Cl(9,0)/Cl(0,9) that OB10's
   own proposed "3+6=9≡1 mod 8" resolution path implicitly assumed.
2. Despite the signature mismatch with the naive proposal, a consistent,
   unique (within a natural {I,σ₁,σ₂,σ₃}⁴ factorized ansatz, 256
   candidates checked) charge-conjugation operator B exists, is Hermitian
   and unitary, and gives B·conj(B) = −I (pseudo-real).
3. This pseudo-real verdict is stable under an independent, equally valid
   re-ordering of the S⁶ Clifford factors (no-collapse check).

---

## Kill criterion

| Kill condition | Threshold |
|---|---|
| No consistent B found across the full {I,σ₁,σ₂,σ₃}⁴ ansatz (256 candidates) | 0 candidates satisfy B·Γ_a·B⁻¹=η·conj(Γ_a) for all 9 generators with one shared η |
| B found but B·conj(B) is neither +I nor −I | residual ≠ 0 for both eye(16) and −eye(16) tests |
| Re-ordering check gives a DIFFERENT type (REAL vs PSEUDOREAL) | contradicts basis-independence, would mean a construction bug, not a real result |

If FAIL → kills: the claim that this specific, already-established
Clifford construction carries a compatible reality structure at all;
would leave OB10 open with a stronger negative (no naive factorized reality
structure exists), not just "not yet checked."
If PASS → survives: OB10's core question answered — geometric bundle IS
of a definite, pseudo-real type, consistent with the finite algebra's own
type.

---

## Checks planned

- T1: reconfirm the two source Clifford algebras exactly as coded upstream
  (Cl(0,3) for S³, Cl(6,0) for S⁶, Γ₇ chirality) — sanity gate before
  building anything new.
- T2: build the 16×16 product generators per preprint.tex:1467-1480's own
  stated formula; verify the full 9-generator Clifford algebra and extract
  actual signature (p,q).
- T3 (adversarial/edge case): exhaustive search over all 256
  {I,σ₁,σ₂,σ₃}⁴ factorized candidates for B (not just the minimal
  {I,σ₂}⁴=16-candidate guess) — the wider search is the adversarial check
  against a false negative from too narrow an ansatz.
- T4 (no-collapse): rebuild the S⁶ factor with reversed Kronecker-factor
  ordering (an independent, equally legitimate representative of the same
  abstract Cl(6,0) algebra) and re-run the full search — reality TYPE must
  be basis-independent; a mismatch would indicate a bug, not a new result.

---

## What this does NOT mean

1. Does NOT establish that this B satisfies any commutation/anticommutation
   relation with the actual (differential, not just algebraic) product
   Dirac operator `D_full` — that is a further, unchecked condition
   (standard NCG real-structure axioms require `[D,J]=0` or `{D,J}=0`
   depending on KO-dimension); this claim only concerns the Clifford
   MODULE's own algebraic reality type.
2. Does NOT construct or verify any explicit combined reality structure
   `J = B⊗J_F` linking the geometric and finite parts — "same qualitative
   type (pseudo-real)" is confirmed; an actual combined operator and its
   own consistency (J²=?, {J,Γ}=?) is not attempted here.
3. Does NOT resolve OB1 (no zero mode for the full operator), OB2 (D4
   product-ansatz fork), or any other open blocker — this is a
   free-standing algebraic classification, per `GLOBAL_RECOMPOSITION_
   AUDIT.md`'s own confirmation that OB10 doesn't feed `D2`'s counting
   argument.
4. Does NOT mean the "3+6=9≡1 mod 8" arithmetic in OPEN_BLOCKERS.md's own
   OB10 text is meaningless — it correctly flags that dimension 9 sits in
   a KO-periodicity window associated with non-real behavior; it is
   incomplete because it omits that the two established sub-algebras have
   DIFFERENT signature conventions (Cl(0,3) vs Cl(6,0)), so the naive
   p+q=9 arithmetic is not the quantity that actually governs the type —
   the direct construction here is what settles it, not a corrected
   mod-8 formula.

---

## Fence (do not change without postmortem)

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

**PASS_PSEUDOREAL_CONSISTENT_WITH_JF**

**Evidence:** [VERIFIED-sympy 4/4] (T1-T4 all pass, see
`ob10_reality_structure.py` output, `decision.md`).

**Status:** CLOSED PASS_PSEUDOREAL_CONSISTENT_WITH_JF
