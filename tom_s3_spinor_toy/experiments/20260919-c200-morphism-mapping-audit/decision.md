# C200 Decision — the 5-outcome morphism-mapping audit, run on every target

**Date:** 2026-09-19
**Verdict: PARTIALLY_SUPPORTED — PROMOTE, narrow scope.** The instrument is valid
where it can be checked against known answers (19/19 controls), the amended
protocol is worth keeping for COMPUTED pairs, the raw prompt as written is NOT
adopted as a standalone gate, and the hand-encoded targets are NOT findings.
Independent skeptic pass (context-blind): **WEAKENED** — every finding is answered in
the table at the end; the fixes were checked by a brute-force oracle (0 mismatches,
same author), not by a second skeptic pass.

---

## Bottom line

1. **Signature decides the verdict.** The same three 8-dimensional modules
   `{8_v, 8_s, 8_c}` are EXACT under `g2`/`su(3)`, split 1+2 under each `so(7)`
   copy, NO_BRIDGE under `so(8)`, and QUOTIENT-related under `so(8)` up to the
   outer automorphism S3. A prompt that asks for ONE verdict without a declared
   signature is ill-posed; the amended prompt must output `signature -> verdict`.
2. **The prompt is a good tool for COMPUTED pairs and an unreliable one for prose
   analogies.** On explicit matrices and weight diagrams it reproduces known
   answers and is checkable. On hand-encoded targets the verdict is largely my
   encoding (two of four such targets turned out to be tautological or
   convention-dependent, see below).
3. **Two of the five outcomes are weak as written:** the literal PARTIAL
   threshold fires on chance graphs at rate 1.000 (n=8), and QUOTIENT_RELATION
   silently covers two different relations.
4. **No new physics.** The triality-vs-generations pair re-expresses closed
   results (C72, C63, G102, C173, THEOREM.md); nothing here changes OB1/H1c or
   N_gen=3 status.

## 1. Instrument validity (T0) [VERIFIED-tool: `run_output.txt`, `results_c200.json`]

19 of 19 controls pass. The pre-registered kill criteria (any of PC-M1/M2/M3,
PC-G1, PC-G2 failing, or NC-G2 EXACT-or-QUOTIENT rate > 1%) did not fire.

| Control | Result |
|---|---|
| `g2` `8_v/8_s/8_c` pairwise | EXACT, `dim Hom = 2`, residual `1e-15` to `8e-15` |
| `su(3)` same triple | EXACT, `dim Hom = 6`, residual `2e-15` to `3e-15` |
| random basis change of `8_v|g2` | EXACT, residual `1e-13` |
| `so(8)` `8_v` vs `8_s` | NO_BRIDGE, `Hom = 0`, strict Cauchy-Schwarz non-isomorphic (the C199-verified direction) |
| weight graph `8_v` vs node-shuffled copy | EXACT |
| weight graphs `8_v,8_s,8_c` pairwise | not EXACT; found only after permuting Dynkin labels `{1,3,4}` |
| one edge moved (non-isomorphism proved by an independent 1-WL invariant) | not EXACT |
| 300 random same-size graphs | EXACT-or-QUOTIENT rate 0.0000 |
| PARTIAL, HOMOMORPHISM positive/negative controls (added post hoc, hand-derived answers) | PASS x3 |

**Deviations, stated plainly.**
- **NC-M2 failed as pre-registered, and the CHECK was wrong, not the instrument.**
  I pre-registered `Hom = 0` for `8_v|g2` against itself with the generator
  correspondence shifted. Result: `hom = 1`. Cause: `8_v|g2 = 7 + 1` and the trivial
  summand is annihilated by every generator, so any correspondence shares it.
  Independent confirmation (not from the classifier): the number of `g2`-invariant
  vectors in `8_v` is 1 = `hom` = `rank`. The classifier's verdict (shared proper
  submodule) was right. This control was **replaced after seeing the failure**
  (PC-M4, plus NC-M2a on the irreducible `so(8)` `8_v`, which is a weak check
  because a random shift of 28 generators is near-unfailable). The pre-registered
  clause "audit the check first" authorised the escape, not the replacement
  threshold; treat PC-M4/NC-M2a as post hoc.
- NC-G1's first generator (double edge swap) could not produce a provably
  non-isomorphic graph under a 2-path invariant; replaced by an edge relocation
  checked with 1-WL (code issue, not a classification failure).
- **Coverage.** The controls validate EXACT, QUOTIENT (twisted-isomorphism kind)
  and NO_BRIDGE at module and weight-graph level, and PARTIAL/HOMOMORPHISM only on
  three hand-built graphs. `instrument valid` does not mean every level is calibrated:
  see finding F1 below.

## 2. Computed targets (independent ground truth exists)

### T1a — signature ladder on `{8_v, 8_s, 8_c}` (module level, explicit matrices)

Pre-registered predictions all met. `hom / End_A / End_B` per pair:

| Signature `h` | dim | `v-s` | `s-c` | `c-v` | reading |
|---|---|---|---|---|---|
| `su(3)` | 8 | EXACT (6/6/6) | EXACT | EXACT | no channel distinguished |
| `g2` | 14 | EXACT (2/2/2) | EXACT | EXACT | no channel distinguished |
| `so(7)_v` | 21 | NO (0/2/1) | EXACT (1/1/1) | NO (0/1/2) | `v` singled out, `s≅c` |
| `so(7)_s` | 21 | NO (0/1/2) | NO (0/2/1) | EXACT (1/1/1) | `s` singled out, `v≅c` |
| `so(7)_c` | 21 | EXACT (1/1/1) | NO (0/1/2) | NO (0/2/1) | `c` singled out, `v≅s` |
| `so(8)` | 28 | NO (0/1/1) | NO | NO | all three distinguished |

Every NO is accounted for by strict Cauchy-Schwarz `hom^2 < End_A * End_B` (the
direction Lean-verified in C199). **Consequence for `E1`:** among these signatures
only `so(8)` makes all three pairs non-isomorphic; each `so(7)` copy leaves exactly
one pair isomorphic. This is the computed form of the mechanism behind the rev 6
to rev 7 counterexample in THEOREM.md §0g. I did not search whether an earlier
round already computed the three `so(7)` Hom tables directly `[UNKNOWN]`; treat this
as consistent with, not as new to, the analytic argument.

### T1b — the same three channels as `so(8)` weight graphs

Edges labelled by the four simple roots of D4. All three pairs: not EXACT,
related after a permutation of labels `{1,3,4}`; random same-size graphs reproduce
that in 0 of 300. **Naming caveat (skeptic, accepted):** the graphs have equal size
(8 nodes, 8 edges each); neither is a quotient of the other. What is found is an
isomorphism twisted by the outer automorphism of the acting algebra. The output now
carries `quotient_kind = "twisted isomorphism ... NOT a quotient map"`.

## 3. Hand-encoded targets — what they do and do not show

All are `[ENCODING-CHOICE]`; I authored both sides. None is evidence about the world.

| Target | Result | Honest reading |
|---|---|---|
| **T2a** triality `{v,s,c}` vs SM generations | S1, S2 (symmetric relations): raw EXACT, calibrated **VACUOUS** (chance-EXACT-rate 1.000). S3 (cyclic triality action vs transitive mass order): NO_BRIDGE. S4 (union): NO_BRIDGE. Throwing away direction makes S3 EXACT. | A directed 3-cycle and a transitive tournament are not isomorphic; that is an exhaustive fact about the two encodings. Direction is the only thing separating S3 from a match. On 3 nodes chance alone gives an exact match at 0.083 (S3) to 1.000 (S1/S2), so no POSITIVE bridge on these encodings can be calibrated at alpha = 0.05. Physically this is the known statement: the only surviving correspondence is "three mutually identical things". |
| **T2b** C198 pipeline | attribute level NO_BRIDGE (`core = 0`) | **Not a test.** Both graphs were written from one edge list, so coarsening to role gives identical graphs by construction (skeptic, verified). The only content is the attribute table in `run_output.txt` (where the circulant/Lovasz analogy stops: abelian vs non-abelian group, 1x1 vs matrix blocks, proved inequality vs fixed line, numeric bound vs diagnostic). That table is consistent with C198 but is my restatement of it. |
| **T2c** round89 Killing constants | strict labels: NO_BRIDGE; with `opp<->same` twisted: QUOTIENT_RELATION; magnitude layer alone: EXACT | The verdict flips on an encoding convention. Round89's own verdict (`PARTIAL_OPPOSITE_SIGN_STRUCTURAL`) is a LAYERED statement the taxonomy cannot express. Pre-registered prediction "single-graph PARTIAL" was **NOT met**. Kept only as an expressiveness demonstration. |
| **T2d** MethodOps vs `meta-loop.md` | raw PARTIAL, core 13 of 15; null search budget exhausted in 8/8 trials | **UNCALIBRATED and CIRCULAR** (`G_B` was authored from `G_A`'s vocabulary). It checks my reading of the source's braces, nothing else. |

**Skipped, with reason:** Tom Lawrence's vocabulary — settled by direct reading
2026-09-07/08; three terms carry no structure to test; contact must not be initiated.

## 4. Findings about the prompt itself

- **F1. The literal PARTIAL rule (core >= max(3, 50%)) is vacuous at small n.** 300
  random 8-node graphs with the same per-label edge counts have common-core sizes
  `{4: 23, 5: 258, 6: 19}`; the threshold is 4, so raw PARTIAL fires on chance graphs
  at rate **1.000**. NC-G1's one-edge-moved graph scores core 6, top ~6% of chance.
  The 50% rule has no justification; a threshold must come from a null.
- **F2. QUOTIENT_RELATION conflates two relations:** (a) twisted isomorphism by an
  automorphism of the alphabet (same size, lossless), (b) coarsening of attributes
  (lossy). Only (b) is a quotient in the usual sense, and only (b) needs a "what was
  forgotten" list.
- **F3. HOMOMORPHISM is unavailable for equal-size pairs** (a surjective non-injective
  map needs `|A| > |B|`); the output now prints `n/a`, not a false `False`. No target
  in this run exercised graph-level HOMOMORPHISM on real data, so its usefulness is
  untested here (only PC-H1/NC-H1 on constructed graphs).
- **F4. For semisimple modules PARTIAL and HOMOMORPHISM coincide** (a non-zero
  non-invertible intertwiner exhibits a shared proper submodule). Argued, not
  separately tested.
- **F5. No layered verdicts.** A pair can be EXACT on one layer (magnitude) and
  NO_BRIDGE on another (sign); one graph, one word cannot say that (T2c).
- **F6. Blind to circularity.** Nothing in the taxonomy detects that `G_B` was built
  from `G_A`'s vocabulary (T2d, T2b).
- **F7. Vacuous exactness.** Small symmetric structures match by chance at rate 1.0
  and would be reported EXACT (T2a S1/S2).

## 5. What it gives us

1. **A reusable, controlled classifier** (`c200_morphism_audit.py`: labelled-graph
   isomorphism / induced-core / surjective-homomorphism search, module-level `Hom`
   classifier, same-size null, 19 controls) for questions of the form "are these two
   explicit representations/graphs the same?" — e.g. comparing multiplicity blocks or
   spectra across rounds.
2. **A complete computed signature ladder for `E1`** (table above): among `su(3), g2,
   so(7)_{v,s,c}, so(8)`, only `so(8)` separates all three channels; each `so(7)` copy
   separates exactly one. Compact, checkable, consistent with THEOREM.md.
3. **A verdict on the prompt:** adopt the AMENDED protocol (appendix) as an optional
   pre-check for cross-domain bridge claims, only when both sides are computed
   objects. Do not adopt the raw five-word prompt as a gate.
4. **A sharper statement for the generation question:** every non-vacuous signature
   we could encode leaves triality's cyclic structure without an image in the
   observed hierarchy; only the vacuous "three identical things" survives. It does not
   change any project status.
5. **Where the C198 analogy stops** (attribute table) — a restatement, useful as a
   checklist, not evidence.
6. **A control-design lesson:** a permuted-generator negative control on a
   representation with a trivial summand cannot have `Hom = 0`; check the invariant
   count before pre-registering it.

## 6. Adoption rule (fixed before results) — outcome

| Condition | Met? |
|---|---|
| (i) instrument valid | yes, for the levels controlled (see §1 coverage note) |
| (ii) H_main: some verdict changes with signature or calibration | **yes** (T1a: EXACT / 1+2 / NO by `h`; T2a: raw EXACT becomes VACUOUS; T2c: convention flip) |
| (iii) taxonomy separates something the Mechanism Transfer Gate collapses | **partially.** The signature declaration and the null (vacuity) do; the five-word vocabulary alone does not, and F2 shows it conflates two relations. |

Decision: adopt the amended protocol for computed pairs; archive the raw prompt as
vocabulary; do not cite T2 targets as evidence.

## Appendix — amended Phase 2 (proposed, ready to paste)

```
ФАЗА 2 (v2, по итогам C200). АУДИТ СТРУКТУРНОГО СООТВЕТСТВИЯ
0. СИГНАТУРА до классификации: какие узлы, какие типы рёбер/операций, какая группа симметрий
   допускается для отождествления. Вердикт — функция сигнатуры; при неоднозначности выдай таблицу
   «сигнатура -> вердикт», а не одно слово.
1. ПРОВЕНАНС: G_A и G_B построены независимо? Если G_B выведен из словаря G_A — пометь [CIRCULAR];
   вердикт узлового соответствия недействителен.
2. СЛОИ: классифицируй каждый слой (величина / знак / структура) отдельно; итог — набор вердиктов.
3. ИСХОДЫ: EXACT; TWISTED_ISOMORPHISM (после автоморфизма алфавита/алгебры, без потери);
   QUOTIENT_COARSENING (после огрубления атрибутов — ОБЯЗАТЕЛЬНО список потерянного);
   PARTIAL (порог ядра из нуль-модели, не «50%»); HOMOMORPHISM (только при |A|>|B|, иначе n/a);
   NO_STRUCTURAL_BRIDGE; UNCALIBRATED.
4. НУЛЬ: для каждого положительного вердикта — доля случайных графов того же размера и числа рёбер
   по типам, дающих тот же уровень. >= 5% или мало прогонов -> VACUOUS / UNCALIBRATED.
   На <= 4 узлах положительный мост откалибровать нельзя.
5. КОНТРОЛИ на объектах с известным ответом до запуска на целевой паре; негативный — тоже.
6. Где объекты вычислимы (модули, матрицы, спектры) — считать (Hom, инварианты, WL-сигнатуры),
   а не кодировать прозой.
```

## Skeptic Concerns (context-blind pass; the agent could not execute code and traced by hand — I verified findings 1, 2, 4, 5 against `results_c200.json` / the code)

| # | Skeptic finding | Response |
|---|---|---|
| 1 | T2d calibrated verdict rests on a null where 8/8 trials aborted | **Fixed.** `calibrate` now returns `UNCALIBRATED` when the null hits its budget or `n * alpha < 3`; T2d reports `PARTIAL(UNCALIBRATED)`. |
| 2 | T2b QUOTIENT is an identity by construction | **Accepted.** Removed the quotient claim and the null; T2b reduced to the attribute table, labelled "NOT a test". |
| 3 | Controls cover 3 of 5 levels; raw PARTIAL fires 300/300 on chance; threshold unjustified | **Fixed partly / accepted.** Added PC-P1, PC-H1, NC-H1; PARTIAL vacuity now printed as F1; the 50% rule has no justification and is replaced by a null-derived threshold in the amended protocol. |
| 4 | T2a null degenerate for S1/S2 and the measured null for S3/S4 (0.083, 0.103) suppressed | **Accepted.** Chance-EXACT-rate now printed for every signature; on 3 nodes no positive bridge is calibratable. |
| 5 | T2c flips on an undeclared label convention | **Fixed.** Both conventions printed; T2c downgraded to an expressiveness demonstration. |
| 6 | QUOTIENT is the wrong name for the twisted isomorphism | **Accepted** as F2; `quotient_kind` recorded. |
| 7 | Minor: `hom` "False" where "not tested"; `core_size=1` when none found; `None` calibration treated as failure; hard-coded conclusions; NC-M2 replacement post hoc; one fixed-seed generic Hom element | **Fixed** (n/a, core size, calibration branches, conditional printing); **accepted** (post-hoc controls flagged; single seed for a generic element is a minor residual). |

**Fix verification (added after the first write-up):** `verify_c200_bruteforce.py` /
`verify_output.txt` compare `find_iso`, `max_common_induced` and `find_surj_hom` against
exhaustive enumeration on 400 random labelled digraphs (<= 5 nodes): **0 mismatches**; and
check the post-review fixes on known answers (`hom` reported `n/a` for equal-size pairs,
`core_size = 0` with disjoint node labels, label-twist QUOTIENT, all `UNCALIBRATED`
branches of `calibrate`). This is same-author verification, not a second skeptic pass; no
second skeptic pass was run. Dismissed: nothing.

**Adopted:** the amended protocol lives in `docs/morphism_audit_protocol.md` (optional
pre-check, computed pairs only).

## Pre-registered predictions — scoreboard

Met: PC-M1/M2/M3, PC-G1, PC-G2, NC-M1, NC-G1, NC-G2, T1a (all rows), T1b, T2a S1-S4,
T2d (core 13/15). **Not met:** NC-M2 (`Hom = 0`; check malformed, see §1), T2b ("non-vacuous
role-level QUOTIENT"; tautological), T2c ("single-graph PARTIAL reproducing round89"; the
classifier returns NO_BRIDGE). Not computed: "no homomorphism either way" for S3 (equal size,
`n/a`; true by hand).

## What this does NOT mean

1. No new physics verdict on triality/generations; no status of OB1, N_gen=3, or any existing verdict changes.
2. Not evidence that prose analogies can be classified reliably.
3. Not validated beyond these pairs.
4. The amended protocol is proposed, not yet used by any other round.

## Reproduction

```bash
cd tom_s3_spinor_toy/experiments/20260919-c200-morphism-mapping-audit
python -u c200_morphism_audit.py > run_output.txt     # ~10 min (null trials dominate)
```
Seed 200, `N_NULL = 300`, `ALPHA = 0.05`. Depends on
`../20260705-g102-spin8-fiber-obstruction/g102_spin8_fiber.py`.
