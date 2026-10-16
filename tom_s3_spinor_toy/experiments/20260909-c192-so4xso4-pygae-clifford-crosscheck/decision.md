# C192 Decision — PROMOTE, with `[WEAK]` marker. C191's `P10` reproduces at the `Γ_i`-realization layer via an independently-written third-party Clifford-algebra library; the layer above `Γ_i` (subgroup embedding, `Γ_9` sign) is shared with C191, not independently re-derived — Medium rung, not Strong.

**Date:** 2026-09-09
**Verdict:** **PROMOTE (WEAKENED)** — `17 of 17` checks pass. C191's `P10`
(`8_s`/`8_c` identical `(j_L,j_R)` content under `so(4)_1`'s isometry alone)
is reproduced through an independently-written Cl(8) construction
(`pygae/clifford`'s left-regular representation) — but only at the layer
where the two rounds actually use different code. Everything above the raw
`Γ_i` generators is reused from C191 verbatim, not independently derived —
found and corrected via context-blind skeptic review before this claim was
trusted at its original (overclaimed) framing.

All numbers trace to `c192_pygae_clifford_crosscheck.py` and `run_output.txt`.

---

## 0. What was tested

User request, verbatim intent: "возьми C191's branching и прогони через
pygae/clifford" — take C191's `SO(4)×SO(4)` branching (its central finding,
`P10`: `8_s` and `8_c` have identical `(j_L,j_R)` content under `so(4)_1`'s
isometry alone) and re-derive it using the third-party `pygae/clifford`
library instead of the project's own hand-rolled numpy Kronecker-product
gamma matrices.

## 1. Method (summary — full detail in `claim.md`)

Built Cl(8,0)'s left-regular representation (256×256, real) via `clifford`'s
own geometric-product structure constants (`(e_i * blade).value` for every
basis blade — mechanically generated, not typed by hand). Verified
`{Γ_i,Γ_j}=2δ_ij` on all 256 matrices (`Q1`, real positive control). Built
`Γ_A`, `Γ_B`, `Γ_9`, `so(4)_1`'s `L_a`/`R_a` generators using the SAME
algebraic formulas as `so4xso4_branching.py`/C191. Calibrated the Casimir
scale empirically against the known `j=1/2` value (`Q13`) before trusting
any content comparison — same "positive control before the negative"
discipline as C191's own `P8`/`P9`.

## 2. What was found

`8_s`-block and `8_c`-block content, both `64×(1/2,0) + 64×(0,1/2)` —
identical (`Q16`), matching C191's `P10` exactly (scaled ×16, per
`Cl(8,0)≅Mat(16,ℝ)`). `17/17` checks pass.

## 3. Skeptic Concerns (Step 8a, Context Asymmetry — agent read ONLY
`claim.md` and the script, no reasoning chain, no session history)

**Verdict: WEAKENED.** Six concerns, addressed individually per the
Skeptic Response Matrix (`FALSIFIED ≠ KILLED` does not even apply here —
none were `FALSIFIED`; all were framing/scope corrections):

| # | Concern | Severity | Response |
|---|---|---|---|
| 1 | Everything downstream of `Γ_i` (`so(4)_1` embedding, `Γ_A`/`Γ_B`/`Γ_9`, `L_a`/`R_a` formulas) is copy-pasted from C191, not independently derived — a shared bug would be inherited and reproduced identically, not caught. Advertised "Strong" rung is an overclaim of ~one rung; actual rung is "different matrix realization of the same formulas" = Medium. | **HIGH** | **Fixed.** `claim.md` § Why this round exists, § Kill criterion, and Kill Analysis all rewritten to state the Medium rung explicitly and name exactly what is/isn't independently tested. |
| 2 | `k=−2` "empirical discovery" (`Q8`/`Q9`) is a direct 3-line algebraic consequence of the round's own `M=Γ_iΓ_j` normalization (`[Γ_1Γ_2,Γ_1Γ_3]=−2Γ_2Γ_3`, shown by direct computation), not a subtle trap in C186's sense. Framing it as "diagnosed via probe" overstated a derivable convention as a discovery — the shape of the `[Repaired check repeats tautology]` pattern (relax a failed check to "any consistent constant," pass, declare victory without naming that the relaxation IS the story). | **MEDIUM** | **Fixed.** `claim.md` § Method step 6 and § What was found rewritten: marked `[INFERRED]` with the actual 3-line derivation, explicitly states it was found empirically first and only derived after, and explicitly retracts the "diagnosed via probe... genuine surprise" framing. |
| 3 | `Cl(8,0)≅Mat(16,ℝ)` (Bott periodicity, `8 mod 8=0`) is used at every stage (the "16 copies" reading of `Q7`/`Q14`) but never cited or independently verified within the round — a Gate-1-style provenance miss for a load-bearing external fact. | **MEDIUM** | **Accepted limitation, marked.** `claim.md` § Method step 6 now carries `[DOCS, standard, not independently re-derived in this round]`. Re-deriving irreducibility of the regular representation is out of scope for a cross-check round — the fact is textbook-standard (real Clifford algebra classification), not a novel claim needing its own verification here. |
| 4 | The "16×" scaling in `Q14`/`Q15` is nearly forced by construction once `Cl(8,0)≅Mat(16,ℝ)` is accepted — arithmetic, not evidence. The actually informative content (only 2 of 4 possible `(j_L,j_R)` types appear; the 64:64 split) was obscured by framing the check as "matches 16× C191." | **MEDIUM** | **Fixed.** `claim.md` § What was found rewritten to lead with the two-types/64:64-split framing and explicitly name the scaling itself as non-evidentiary. |
| 5 | "Convention artifact vs. fact about the abstract algebra" (original `claim.md` § Kill criterion) conflates two different failure modes — since the round reuses C191's own formulas above `Γ_i`, a mismatch would mean a BUG in one of the two `Γ_i` realizations, not a convention-vs-reality distinction (any faithful rep of the same algebra with the same formulas on top must agree, by definition). | **LOW** | **Fixed.** `claim.md` § Kill criterion rewritten to state the bug-vs-bug framing correctly. |
| 6 | `Q2` (each `Γ_i` symmetric) is a forced structural consequence (orthogonal + involutive), not independent verification content — framing it as "a check C191's construction could not even pose" is check-count inflation, not evidence about correctness. | **LOW** | **Fixed.** `claim.md` § Method step 3 rewritten: `Q2` noted for completeness, explicitly NOT counted as adding epistemic weight. |

**What the skeptic confirmed as genuinely solid** (quoted, not paraphrased
away): *"`joint_s == joint_c` is a dict-equality on outputs of the SAME
extraction procedure applied to two orthogonal subspaces. The calibration
`SCALE = 0.25` is fixed from `V_S` alone and reused unchanged on `V_C`. A
genuine asymmetry between the two blocks... would show up in `Q15`/`Q16`
and could not be papered over by the single scale factor. This part of the
check is honest and cannot be forced by post-hoc scaling."* This is the
part of `Q16` that survives at full strength — the reproduction of `P10`
at the `Γ_i`-realization layer, not the inflated "Strong rung" framing
around it.

## 4. Kill Analysis

**What this round killed:** the possibility that C191's `P10` was an
artifact of the SPECIFIC 16×16 Kronecker-product `Γ_i` realization
`so4xso4_branching.py` uses (as opposed to the shared algebraic formulas on
top of it, which this round does not independently test).
**What survives:** C191's own `P10` — reproduced at the `Γ_i` layer through
independently-written code, Medium rung on the Independent Verification
Strength Ladder (corrected down from an initially overclaimed "Strong").
**Not killed, unaffected:** C191's own REJECT verdict on claim (a), the
steelman, role-swap, and split-identification sections — none re-derived
here.

**Revival condition:** not applicable — confirmatory round, not a killed
claim.

## 5. What this establishes for the Independent Verification Strength Ladder

This is the first round in this project's Cl(8)/Spin(8) line to use
genuinely independently-written code for ANY layer of the construction.
Prior "independent" checks were the same hand-rolled construction re-run.
**Honest characterization, per skeptic review:** this round occupies Medium
(different code realizing the same shared formulas), not Strong. Reaching
Strong for this specific claim would require independently re-deriving at
least one of: the `so(4)_1` embedding formula, the `Γ_9` sign convention, or
the `L_a`/`R_a` generator conventions — not just the raw `Γ_i` matrices.
Recorded honestly as a partial, not full, ascent — the overclaim was caught
before commit, not after.

## 5.5 Floor–Ceiling (Step 4a)

Discrete metric, not continuous (does the independently-realized content
match C191's, after calibration: yes/no) — same shape as C191's own
Floor-Ceiling note (`experiments/20260909-c191-*/decision.md` § 5). **Floor
= 0**: the calibration step (`Q13`) itself failing to reproduce the ALREADY
KNOWN `j=1/2` value, or `Q14` failing to reproduce the known row-58 content
— either would make the construction untrustworthy before any comparison to
`C191` is even attempted (a construction with a broken mechanism could not
land here by accident, same logic as C191's own `P8`/`P9` positive control).
**Ceiling = 1**: exact match to C191's content, scaled by the
`Cl(8,0)≅Mat(16,ℝ)`-forced multiplicity factor. **Observed = 1** (`Q14`,
`Q15`, `Q16` all exact). **Efficiency = (observed−floor)/(ceiling−floor) =
1.0** — lands exactly on the ceiling. Per § 3 above, this efficiency score
applies ONLY to the `Γ_i`-realization layer (Medium rung) — it says nothing
about the shared formulas above `Γ_i`, which this round does not measure at
all (no floor/ceiling defined for a layer that was not independently
varied).

## 6. What this does NOT establish

See `claim.md` § What this does NOT establish (updated post-skeptic-review)
for the full list, including the HIGH-severity scope limitation (shared
formulas above `Γ_i` not independently tested).

## 7. Reproduction

```
cd experiments/20260909-c192-so4xso4-pygae-clifford-crosscheck
pip install clifford   # pygae/clifford 1.5.1, BSD-3
python c192_pygae_clifford_crosscheck.py
```

`17/17`. `ruff check` and `ruff format`: clean.
