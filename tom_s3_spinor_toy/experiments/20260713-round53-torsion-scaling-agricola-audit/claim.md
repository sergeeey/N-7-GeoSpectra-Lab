# Round53-TorsionScaling Claim — does Agricola 2002 give a general torsion bound?

**Date:** 2026-07-13
**FL tier:** [x] Standard (structural/literature analysis, no new matrices per explicit user scope)
**Question type:** [x] descriptive

---

## Prior Result Gate (MANDATORY — fill BEFORE writing anything below)

1. Exact claim: does I. Agricola's 2002 general Kostant-Parthasarathy
   theorem (already cited in this project's own bibliography,
   `\bibitem{Agricola2002}`) provide a general, structural bound or
   formula showing the torsion-correction term in the L4B mechanism
   grows slower than the G₂ Casimir gap as ρ→∞ — the direct revival
   attempt for `L4B-HIGHER-REPS` (`parked/INDEX.md:9`), per the user's
   own frozen claim and explicit constraint: derive a scaling law from
   the operator's structure, do not build per-representation matrices.
2. `decision.md` grep: done — confirmed this is the literal, same-day
   revival attempt of the item Round 52 parked (`parked/INDEX.md:9`).
3. `round*_claim.md` + scripts grep: done via Round 52's own gate — 0
   hits for any prior torsion-scaling attempt.
4. `null_results/` + `parked/` grep: done — confirmed NOT a duplicate
   of `null_results/20260713-round45-leibniz-correction-blind-
   derivation.md` (that entry concerns interpreting an already-computed
   ρ=7-only residual matrix K; this round concerns a general ρ-scaling
   law across all representations — different mathematical questions,
   verified by reading both in full).
5. `git log -S`/`-G` pickaxe: done via Round 52's gate.
6. Primary source re-read: done — `Agricola_2002_Dirac_naturally_
   reductive.pdf` (the correct file; `Agricola_2002_naturally_reductive_
   Dirac.pdf` is MISLABELED and actually contains an unrelated Okounkov-
   Pandharipande paper on Gromov-Witten theory — flagged as a repo
   cleanup item, not fixed in this round, out of scope), read in full
   (pages 6-20), Theorem 3.2 and 3.3 quoted exactly. Also re-read
   `preprint.tex:668-747` (the L4B section itself) and
   `experiments/20260708-dolan-casimir-g2su3/decision.md:3317-3416`
   (Round 22's own construction) directly, not paraphrased.
7. **Status:** [x] OPEN → this round.

---

## Estimand

**Population:** the torsion-correction term in this project's L4B
mechanism, specifically the two pieces Round 22 identified for ρ=7:
TORSION-CROSS-TERM (built from the fixed torsion table T(p,q,r)) and
MIXED-A-B-CROSS-TERM (built from an anticommutator {e_p,D64} contracted
against ρ_7(e_p), the representation matrix on V_7).
**Intervention:** check whether Agricola's general Theorem 3.2 (proven
for the BARE, untwisted Dirac operator on any naturally reductive G/H)
structurally covers this project's actual TWISTED operator D_{S^6}⊗S^-.
**Comparator:** the "no data, no scaling law" state Round 52 established.
**Endpoint:** whether each of the two pieces (TORSION-CROSS-TERM,
MIXED-A-B-CROSS-TERM) is representation-independent (bounded), and
whether this is provable from existing theory or remains open.
**Summary measure:** per-piece verdict (structurally-grounded-bounded /
genuinely-open), not a single number.
**MCID:** N/A — descriptive structural analysis.

---

## Claim

Agricola's Theorem 3.2 gives real theoretical grounding — not merely
intuition — for representation-independence of the pure TORSION-CROSS-
TERM piece specifically, because its general formula shows all torsion-
dependent pieces act via Clifford multiplication by FIXED elements
(built from the structure constants of the fixed n=6-dimensional space
𝔪) on the FIXED spinor fiber Δ_𝔪, tensored with identity on the growing
Peter-Weyl multiplicity space — a genuine `‖A⊗I‖=‖A‖` argument. This
does NOT extend to the MIXED-A-B-CROSS-TERM, because that piece is
specific to this project's TWISTED operator (absent from Agricola's
bare, untwisted setup) and explicitly contracts against ρ_ρ(e_p) — a
representation-dependent quantity whose own operator-norm scaling with
ρ is a separate, unaddressed question.

---

## Kill criterion (MANDATORY — fill BEFORE running)

| Kill condition | Threshold |
|---|---|
| Agricola's Theorem 3.2 turns out to already cover twisted/auxiliary-bundle operators directly (not just the bare tangent-space spinor bundle) | if found, re-examine whether MIXED-A-B is also covered — would strengthen this round's claim |
| Round 22's MIXED-A-B-CROSS-TERM turns out NOT to actually depend on ρ_7(e_p) in a way that could scale with ρ (e.g. if it's secretly also expressible as fixed⊗identity) | if found, this round's "genuinely open" conclusion for that piece would be wrong — re-examine |

If FAIL (either condition triggers) → kills this round's split verdict,
re-open in whichever direction the finding points.
If PASS (neither triggers, both re-confirmed) → the split verdict
(TORSION piece: theoretically grounded; MIXED-A-B piece: open) stands.

**Verification performed**: re-read `preprint.tex:668-747` directly —
confirms Agricola's setup (§3 of his paper) is for the operator D^t on
the bare G/H homogeneous space (no auxiliary twisting bundle mentioned
anywhere in the extracted Theorem 3.2/3.3 statements); confirms Round
22's own decision.md text (`:3342-3343`) explicitly states MIXED-A-B is
"an anticommutator {e_p,D64} contracted against rho_7(e_p)" — the
ρ-dependence is in the primary source's own stated construction, not
inferred. Both kill conditions checked: neither triggers. PASS.

---

## Checks planned

- T1: read Agricola 2002's Theorem 3.2 in full, extract exact formula.
- T2: check whether the formula's structure implies a tensor-product
  (fixed-Clifford-operator ⊗ identity) form.
- T3 (adversarial): explicitly check whether this project's own twisted
  operator's cross-terms (Round 22, TORSION and MIXED-A-B) match that
  clean structure, or diverge from it — found: TORSION matches
  (built purely from the fixed T(p,q,r) table), MIXED-A-B diverges
  (explicitly contracts against ρ-dependent ρ_7(e_p)).

---

## What this does NOT mean

1. Does NOT prove sub-claim (B) from Round 52 (torsion-correction
   boundedness) — only PART of it, for one of two relevant pieces.
2. Does NOT mean the MIXED-A-B-CROSS-TERM actually grows unboundedly
   with ρ — only that its scaling is genuinely unknown, not that it's
   bad news confirmed.
3. Does NOT license computing ρ=27/64/77 spectra — the identified next
   question (operator-norm scaling of ρ_ρ(e_p) with ρ) is a different,
   more targeted question than building full Dirac operator matrices,
   and is not attempted in this round either.
4. Does NOT change any preprint.tex claim — the preprint's own L4B
   caveat language already correctly hedges this as "formally open."

---

## Fence (do not change without postmortem)

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

See `decision.md`.
