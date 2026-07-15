# Round61-BLCommutantAudit Decision — FAIL (B-L is a member, not unique)

**Date:** 2026-07-14
**Verdict: FAIL**, per claim.md's own pre-registered kill criteria (dim
$V \geq 2$). Both independent routes agree qualitatively; the skeptic layer
found and corrected a real quantitative error in Route B and an honest
convention ambiguity in Route A, neither of which changes the verdict.

This is a genuine, informative, pre-registered outcome — not a failed round.
Per the frozen claim.md: *"All three non-PASS outcomes are pre-registered as
informative... each is a specific, falsifiable, reportable structural fact."*

---

## Headline result

$B{-}L$ is **not** uniquely selected by (1) commuting with
$\mathrm{SU}(3)_c\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$, (2) chirality
compatibility, (3) real-structure compatibility ($J_F T J_F = -T$), and (4)
the five standard anomaly-cancellation conditions, applied to this project's
own already-geometrically-derived 32-dimensional fermion representation
content. It is one member of a family of admissible generators — confirmed
robustly $\dim V \geq 3$ (multiply independently verified), possibly larger.

**$B{-}L$ IS confirmed to be a genuine member of the surviving family**
(independently re-verified by Skeptic 2 via direct 32-entry charge-pattern
reconstruction, not just trusted from either route) — this is not "B-L is
wrong," it is "B-L is under-determined by these constraints alone."

## Corrected numbers (post-skeptic)

| Quantity | Route B's original claim | Corrected / verified value |
|---|---|---|
| Diagonal-only anomaly-free family (4 block parameters $t_A,t_B,t_C,t_D$, literal all-32-state convention) | 2-dim, via "$t_C=-t_B$, $t_D=-t_A$" | **[FALSIFIED-tool-verified] → 3-dim**, single constraint $t_A+3t_B+3t_C+t_D=0$. Skeptic 2 exhibited an explicit counter-example $(t_A,t_B,t_C,t_D)=(0,1,0,-3)$ satisfying all 5 anomaly conditions exactly while violating Route B's claimed relations — independently matches Route A's own diagonal coordinates without having read Route A's code. |
| Full commutant incl. off-diagonal "flavor-mixing" directions | not considered (diagonal ansatz only) | Route A: **5-dim** (literal all-32 convention) or **4-dim** (chirality-weighted, one-sector-per-condition convention). The 2 extra off-diagonal dimensions are **[HYPOTHESIS-STRONG, not independently re-verified]** — Skeptic 2 could not check them (lacked access to the S³ generator matrices) and flagged them "UNVERIFIED-HERE, not disproved," not confirmed either. |
| Which convention does claim.md actually specify | ambiguous in claim.md's literal wording | Skeptic 1: claim.md's own pointer ("matching the preprint's existing hypercharge check style, eq. 286-291") refers to `g12_anomaly_check.py`'s chirality-weighted 16-Weyl-component convention — i.e. the **chirality-weighted / one-sector reading is the procedurally correct one**, not Route A's self-declared "primary" literal-all-32 reading. Route A's own honestly-reported cross-check number (4) is the more faithful one under this finding. |

**Bottom line, robust across every correction and every convention checked:**
$\dim V \geq 3$. The FAIL threshold is $\dim V \geq 2$. No correction found by
any skeptic moves the verdict toward PASS; if anything, every correction
found the true family was *larger* than first reported, never smaller.

## Kill Analysis (Anti-Overfitting Gate, mandatory for non-PASS)

**What was killed:** the specific hope, as framed in claim.md, that gauge
commutant + chirality + real structure + standard anomaly-freedom, applied
to this project's own geometrically-derived fermion content, is *by itself*
strong enough to single out $B{-}L$ (up to normalization) as the unique
admissible $\mathrm{U}(1)$. This hope is killed for this exact constraint
set on this exact representation content.

**What was NOT killed:**
- $B{-}L$'s status as a valid, anomaly-free choice — unaffected; it remains
  a fully consistent member of the surviving family.
- The already-published finding (gate G97) that $B{-}L$ cannot be embedded
  as an isometry generator — independent question, untouched.
- The preprint's own existing framing that $B{-}L$ is "identified from
  fermion charge content... geometric origin left open" — this round's
  result is *consistent with, and adds precision to*, that existing honest
  caveat; it does not contradict anything currently in `preprint.tex`.

**Relaxation map (what additional principle could still promote $B{-}L$ to
unique, if a future round wanted to pursue this further):**
| Relax/add | Effect |
|---|---|
| Require $T$ to extend to a full $\mathrm{SU}(4)_{\mathrm{PS}}$ (Pati-Salam) generator | Already shown impossible as an isometry (gate G97) — this route is closed, not open |
| Require $T$ diagonal (no flavor mixing) AND minimal charge quantization beyond the 5 anomalies checked | Would need to independently verify Route A's 2 off-diagonal directions first (currently unverified) — could shrink the family from 5→3, still not to 1 |
| Add a UV-completion constraint (e.g. proton stability, embedding in a specific simple group) | Genuinely new physical input, out of scope for a pure representation-theory search |
| Accept $B{-}L$ as the anomaly-free member singled out by matching known low-energy phenomenology, not by derivation | This is exactly the preprint's current, honest framing — no change needed |

## Pearl (registered in pearl_registry/INDEX.md)

Route A's discovery, invisible to the (natural, and originally
user-specified) diagonal-block ansatz: the lepton doublet block
$\{\nu_L,e_L\}$ and antilepton doublet block $\{\bar e_L,\bar\nu_L\}$ (and
their CPT/R-sector images) are isomorphic as bare
$(\mathrm{SU}(3),\mathrm{SU}(2)_L)$ representations (both are color-singlet
doublets), so Schur's lemma does *not* force a commuting Hermitian operator
to be scalar-diagonal there — a genuine off-diagonal Hermitian mixing block
between these two multiplets is allowed by the gauge symmetry alone, and
critically, *invisible to every one of the 5 standard anomaly conditions*
(all are sums of diagonal entries only). This is a structural point with
reach beyond this one round: any future "is generator X uniquely forced by
anomaly cancellation" search on this fermion content (or similar SM-like
content with isomorphic same-chirality color-singlet multiplets) must check
for such directions explicitly, not assume a diagonal ansatz. Impact 5/10
(local to this representation content and this class of question, but a real
methodological trap for future gates).

## Skeptic response matrix (Step 8a)

| Skeptic | Verdict | Finding | Response |
|---|---|---|---|
| 0 — anomaly completeness | no issue, no verdict change | Mixed grav-$\mathrm{SU}(2)$/$\mathrm{SU}(3)$ anomalies vanish identically (non-abelian generators traceless); Witten $\mathrm{SU}(2)$ global anomaly is $T$-independent (doublet counts even, satisfied regardless); $\mathrm{SU}(2)_L$-$\mathrm{SU}(2)_R$ mixed anomaly vanishes (no state charged under both). Anomaly list is complete for this gauge group. | No action needed |
| 1 — independence | issue found, no verdict change | (Clean) No numeric $B{-}L$/$Y$ leak in either script before their labeled comparison steps. (Cosmetic leak) The human-readable state *names* Route B read (`u_L`, `e_Lbar`, etc.) were originally assigned in `g17_electric_charge.py` to match already-known SM charges — but the block *partition* was independently re-verified against the real generator matrices (V2-V5 checks), not asserted from names, so the numeric result is uncontaminated. **Key additional finding**: Route A's "primary" convention (dim=5) is not what claim.md's own eq-286-291 pointer specifies; the chirality-weighted convention (dim=4) is the procedurally correct reading. | Accepted: documented in the corrected-numbers table above; does not change FAIL verdict |
| 2 — mathematical referee | issue found (in Route B), no verdict change | Independently rebuilt $J_F$ from `g18_ncg.py`'s `CPT_PAIRS` and confirmed real-structure/Hermiticity/chirality relations exactly. **Falsified Route B's specific claimed relations** ($t_C=-t_B$, $t_D=-t_A$) with an explicit counter-example satisfying all 5 anomalies while violating them — correct diagonal-only family is 3-dim (one constraint), not 2-dim. Independently matched Route A's diagonal coordinates without reading Route A's code. Could not verify Route A's off-diagonal claim (access-limited) — flagged unverified, not disproved. Confirmed the $B{-}L$ charge pattern is exact and consistent across all 32 entries. | Accepted: Route B's specific relation formula corrected in this decision.md; underlying FAIL logic confirmed sound |

## Recommendation

1. No `preprint.tex` change is *required* — the existing Open Problems
   $\mathrm{U}(1)_{B-L}$ entry already correctly says the geometric origin is
   open; this round is consistent with, not contradictory to, that text.
2. **Optional strengthening** (not applied here, needs separate
   confirmation): add one sentence to that Open Problems entry citing this
   experiment, e.g. "*an internal search (gate/experiment
   `20260714-round61-bl-commutant-audit`, this work) confirms $B{-}L$ is one
   member of a family of anomaly-free $\mathrm{U}(1)$ generators consistent
   with the geometrically-derived gauge action, chirality, and real
   structure on this fermion content — not uniquely selected by these
   constraints alone.*" This would be a genuine, citable negative result
   strengthening the existing caveat with precision, not just repeating it.
3. If a future round wants to push further: independently re-verify Route
   A's 2 off-diagonal directions (the one piece no skeptic could confirm),
   using the actual S³ $\mathrm{SU}(2)_L/\mathrm{SU}(2)_R$ generator
   matrices from `g11_block_generators.py`.

## Files

- `claim.md` — frozen before running
- `round61_route_a_commutant.py`, `round61_route_b_blocks.py` — the two routes
- `route_a_run_output.txt`, `results_round61_route_a.json` — captured output
- Workflow transcripts: `wmpajal0a` (failed, all 5 agents hit session limit,
  0 completions — see `wf_3a370503-560/journal.jsonl`), retried as
  `wfy76s8zr` (same script, `resumeFromRunId`, all 5 completed)
