# C135 — FL Step 8a skeptic record

**Passes run:** 1 (context-blind: `claim.md` + `decision.md` +
`c135_triality_vs_gamma_signs.py` + `results_c135.json`, plus the cited primary
sources for a citation audit. No session history, no reasoning chain.)

**Verdict: `[WEAKENED]`**

**Second (paraphrased) pass: NOT run — justification.** `claim.md`'s own scope
note requires a Paraphrase-Sensitivity Probe only if the first pass finds
something that changes the verdict's *direction*. It did not. The pass states:
*"The central mathematical statement survives every attack I could mount"* and
*"Every component of the central conclusion is mathematically correct."* What it
weakened is the round's evidentiary framing, not its answer. Running a second
pass would cost 2x for a disagreement that the first pass explicitly rules out.

---

## What the pass attacked, and what happened

| # | Attack | Outcome |
|---|---|---|
| T1 | Is the decisive `eps`-triple measured, or definitional? | **LANDS.** Two of the three values are fixed by construction (`8_s`, `8_c` are *defined* as the `Gamma_9` eigenspaces); the third follows from `Gamma_9 Gamma_a Gamma_9 = -Gamma_a`. The run contributes ~zero bits to the negative half. Recorded in `decision.md` §8a. |
| T2 | Is `rho_v(Gamma_A) = -D_A` a sign-convention artifact (twisted vs untwisted adjoint)? | **FAILS — the result holds.** `Gamma_A, Gamma_B, Gamma_9` are all even, so the grade involution is trivial on them and twisted/untwisted conjugation coincide; `Gamma_A^2 = I` makes `g x g^-1 = g^-1 x g`. Reordering `Gamma_A`'s four factors flips all three `eps` together, leaving `n_distinct = 2` and the stabiliser unchanged. |
| T3 | Is "every nontrivial central element is `+1` on exactly one of the three `8`s" asserted or computed? | **FAILS — genuinely computed** (step 2, 4 pass / 4 fail by `O(1)`) and convention-free. Minor: `Gamma_9`'s commutation with the 28 bivectors is inferred, not directly checked → tier lowered to `[INFERRED]` in §5b. |
| T4 | Does `summand_pairing` have any control? | **LANDS — it had none.** The `0.903` cited beside it belongs to step 5. Two tests specified. |
| T5 | Is C133's actual `sigma` shown to be one of the 8 label 3-cycles? | **LANDS.** It is an inference chain, not a measurement. `decision.md` §5d/§8a now says so. |
| T6 | Citation audit — are the quotes verbatim, and does round119 really contain no `(Gamma_A, Gamma_B)` construction? | **FAILS — §2 and §2a are accurate.** All quotations verified verbatim against `pearl_registry/INDEX.md` row 40, `L3B_SPIN8_INTERFACE_SPEC.md` lines 451-456 / 505-511 / 586-589, and round119's `decision.md`. Round119 mentions `Gamma_A/Gamma_B` once, as a citation. |

---

## Response Matrix (FL Step 8a) — 14 concerns, 0 dismissed

Every concern was **Fixed** or **Accepted-with-documentation**. None was
dismissed. Two required re-running the script; one of those exposed a real bug.

| Concern | Response |
|---|---|
| 1. Stale residual range `13.8–15.9` vs JSON `14.34–21.43` [HIGH] | **Fixed** — re-read `results_c135.json`, corrected §5b. |
| 2. Top-line verdict inverted: the caveat's *letter* says "sectors", which ARE permuted [HIGH] | **Fixed** — header rewritten, new §2c isolates the `sectors` vs `sign patterns` substitution *inside row 40's own two columns* as the hinge of the whole result. This is the pass's most valuable catch. |
| 3. One-sidedness disclosed for the losing half only; the positive half is equally entailed and uncontrolled [HIGH] | **Fixed by running the missing control** rather than conceding — see below. §8a rewritten to cover both halves; the first draft's repair is withdrawn. |
| 4. `{6,3,3}` replication placed at "independently-written code" | **Accepted** — same equation, same algebra, same nullspace method. Downgraded to "Same model, isolated context" (Weak–Medium) in §13. |
| 5. "Stabiliser of the fixed *pair*" ≠ what was measured (stabiliser of the *pattern*) | **Fixed** — header, §5c and §6 now say "pattern"; the pair-level claim is routed through §6a as `[INFERRED]`. |
| 6. §6.1 stacks two uncomputed steps: the `Spin` lift of `Gamma_B`, and the octonion-index ↔ gamma-index bridge | **Accepted, documented** — new §6a states both explicitly, notes this project's own registry warned about exactly this and fixed it with `P, Q` intertwiners that C135 does not rebuild. Marked `[INFERRED]`, with V4 in the Relaxation Map as the repair. |
| 7. `predicted_fixed_subalgebra_dim` is hard-coded arithmetic under a corroboration-sounding key | **Fixed** — JSON key renamed, flagged in §5d. |
| 8. `conj_by_U` scalarity / `U24.T` orthogonality unchecked | **Accepted** — rescued by the independent `max\|a∓b\| = 0.0` checks; recorded in §8.14, not repaired. |
| 9. Ordinal slip: the `P, Q` row is two rows later, not the next one | **Fixed** §2b — and the row actually in between is the superseded "never-reconciled realizations" warning, now cited in §6a where it belongs. |
| 10. §5a (7 Fano splits, one `G2`-orbit) not reconciled with §6's "convenient basis: REFUTED" | **Fixed** — §6b downgraded to **PARTLY REFUTED**; canonicity named as open and added to the proposed Caveat-Gate entries. |
| 11. §7.3 corrects an impression the record does not contain | **Accepted** — §7.3 reworded as a sharpening, not a correction. |
| 12–14. Misc. (contradiction between §2b/§9 and §7.7 on "resolves L3b's open item"; disclosure completeness) | **Fixed** — §2b and §7.7 reconciled: this round answers the *question*, does not execute the relabelling programme, never touches the covariance equation, and neither finds nor excludes the conjectured twist. |

### The one place the pass was tested and turned out wrong about the code

The pass predicted step 8's degeneracy control would show the counter *can*
fail, and that a non-quaternionic split would still give three distinct
pairings. Both were run (new `step8b`).

* **T4a:** `n_distinct = 2` — the counter can fail. ✔ as predicted.
* **T4b:** first run returned `2`, appearing to *refute* the prediction. That
  was **my bug, not the pass's error**: `summand_pairing` took `np.real()` of a
  complex Hermitian compression before diagonalising, which silently emptied the
  control's eigenspaces. Harmless on the quaternionic path (that compression
  happens to be real), fatal on the control. **Fixed → `n_distinct = 3`,
  confirming the prediction exactly.**

Had this not been run, `decision.md` would have reported "the non-quaternionic
split has no pairing structure" as a finding. It is an artifact. Recorded as
self-caught defect 15 in §8.

**Net effect of that control:** distinctness of the three pairings is **generic
to any `4+4` split** and carries no octonionic information. The round's single
discriminating measurement is the `0.903` triality-covariance control, which
replicates a 2026-07-15 result.

---

## Standing lesson

*A control quoted next to a claim is not a control **for** that claim.* The
`0.903` residual is a real, failable control — for step 5. It sat one paragraph
away from step 8 and read as if it covered it. Proximity is not coverage: check
which computation a control's input actually enters.

Secondary: *a registry row's own columns can disagree.* Row 40's caveat column
says "sectors" and its `next_check` column says "sign patterns"; they get
opposite answers. The narrowing was never flagged when the row was written, and
a round that quoted only one column would have reached a confidently wrong
headline — as this one's first draft did.
