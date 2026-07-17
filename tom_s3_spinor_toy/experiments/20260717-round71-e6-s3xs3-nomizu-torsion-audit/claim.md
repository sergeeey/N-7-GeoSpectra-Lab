---
# Round71-E6-S3xS3-Nomizu-Torsion-Audit Claim
# Explicit canonical-connection (Nomizu map) computation of Term2 on S3xS3 = SU(2)^3/SU(2)_diag,
# closing the gap E5 (20260717-round70) explicitly flagged as needing a NEW derivation step.
---

**Date:** 2026-07-17
**FL tier:** [x] Full (new derivation step, explicit connection/torsion construction, not a
substitution into an already-proven general formula)
**Question type:** [x] descriptive (does a specific representation-theoretic coefficient vanish
or not, for a specific explicit connection — not a causal or predictive claim)

---

## Prior Result Gate (MANDATORY — filled BEFORE computing anything)

1. Exact claim: does the Levi-Civita canonical (Nomizu-map) connection on S3xS3, built
   explicitly from CH2016's own stated basis/structure constants (page 18), force the
   isotropy-trivial slot inside `Lambda^2(m^{1,0})(x)Lambda^2(m^{1,0})` (found present by
   Round 70/E5, unlike S6/SU(3)-T2/CP3) to carry a ZERO or a NONZERO `Term2` coefficient?
2. `decision.md` grep: done.
   - `experiments/20260717-round70-e5-universality-cp3-s3xs3/decision.md` — Part B verdict
     `INCONCLUSIVE-BY-ROUTE-C`, explicit unclaimed follow-up: "Deciding the actual sign/value
     of Term2 on S3xS3 would require the explicit torsion 3-form / Nomizu-connection structure
     constants for this specific coset ... a genuinely NEW, non-trivial derivation step."
     THIS experiment executes exactly that follow-up.
   - `experiments/20260708-dolan-casimir-g2su3/decision.md` (21 rounds, S6/G2-SU3): confirms the
     project's OWN open tension — the Kostant-Parthasarathy Casimir-difference theorem is proved
     only for CH2016's `D^{1/3,A}` operator (built from the connection family `nabla^t`,
     `t=1` = canonical/characteristic connection, evaluated at parameter `t/3=1/3` — CH2016 p.5-6,
     eq 7-8), NOT for the Levi-Civita operator (`t=0` in CH2016's own family) used throughout
     `preprint.tex`.
   - `experiments/20260714-round59-trivial-rank-certification/decision.md` +
     `round59_route_c_analytic.py`: the S6 precedent this round's method is transported from —
     builds the LEVI-CIVITA (not canonical/characteristic) Nomizu 2-forms explicitly from
     Agricola-Hofmann-Lawn 2023 (AHL2023), spin-lifts them, calibrates against the known Killing
     equation, then computes `Term1`/`Term2` exactly.
   - `experiments/20260715-round65-su3t2-killing-spinor-test/decision.md`: T^2 analog, uses only
     representation-theoretic (weight) arguments, no explicit connection built — NOT reused here
     because for S3xS3 the representation-theoretic shortcut is exactly what fails (E5's finding).
3. `round*_claim.md` + scripts grep: done. No script anywhere in this repo builds a Nomizu map,
   torsion, or explicit spin connection for `su(2)^3`/`su(2)_diag` isotropy before this round.
4. `null_results/` + `parked/` grep: done, 0 hits for "S3xS3 Nomizu" or "SU(2)_diag torsion".
5. Primary source re-read: **done, directly from the PDF via `pymupdf`, this session** —
   `Charbonneau_Harland_2016_NK_instantons.pdf`, pages 2-6 (Section 2, general NK spinorial
   geometry, Killing spinor equation eq.(1), connection family `nabla^t` eq.(7)-(8), Lemma 2 P/Q
   eigenvalues) and pages 13-19 (Section 4, explicit `su(2)^3` basis, Casimir normalization
   `B(I_i^(a),I_j^(b))=(1/6)delta_ij delta_ab`, `X_i=((1+sqrt2)J_i,(1-sqrt2)J_i,-2J_i)`,
   `Y_i=sqrt6(J_i,-J_i,0)`, "the almost complex structure sends X_i to Y_i and Y_i to -X_i",
   `ad(I_i)(X_j)=eps_ijk X_k`). Full page/equation citations recorded in `decision.md`.
6. **Status:** [x] NEW.

---

## Explicit risk flagged BEFORE starting

**Risk 1 (which Dirac operator convention):** Per the task constraint and the project's own
`dolan-casimir-g2su3` audit, this experiment uses the **Levi-Civita connection** (CH2016's
`nabla^0`, i.e. `t=0` in their family — matching Round 59/65's own convention and `preprint.tex`'s
physically-relevant operator), **NOT** CH2016's canonical/characteristic connection `nabla^1`
(their `D^{1/3,A}`, the one their own Prop 7/8 Casimir machinery is proved for). This experiment
does NOT touch or resolve the project's own open Kostant-Parthasarathy `t=1/3` vs `t=1/2`
tension for S6 — that remains open, unrelated to this computation.

**Risk 2 (metric normalization is NOT free — checked, not assumed):** CH2016's own stated basis
`X_i, Y_i` (page 18) is NOT literally metric-compatible with its own stated complex structure
under the naive "equal per-copy weight" bilinear form `B` also stated on page 18
(`B(I_i^(a),I_j^(b))=(1/6)delta_ij delta_ab`): direct computation (see decision.md) gives
`B(X_i,X_i)=5/3` but `B(Y_i,Y_i)=2` — NOT equal, contradicting the general fact that any
almost-Hermitian pair `(g,J)` must satisfy `g(JX,JX)=g(X,X)`. This is flagged and resolved via
the STANDARD, FORCED (not arbitrary) Hermitization `g_H(V,W) := (1/2)[B(V,W)+B(JV,JW)]` — this
construction is a general fact about any (invariant form, compatible almost-complex-structure)
pair, not a choice invented for this experiment. Marked `[INFERRED]`, not `[ASSUMED]`, and its
validity is CHECKED (not merely asserted) via the calibration gate in Step 1a below — exactly the
same "can this fail" discipline Round 59 used for AHL2023's own transcription.

**Risk 3 (target dimension is NOT 1 for S3xS3 — a new structural fact, established by
elementary Clebsch-Gordan BEFORE running any Nomizu-map code, not dependent on the outcome):**
For S6/SU(3)-T2/CP3, Route C's "target" (`H`-invariants of `Sigma_even (x) Sigma_even`) is
1-dimensional, so ANY nonzero component of `D+(v_b)` forces `rank=1` outright. For S3xS3,
`Sigma_even = Lambda^0(+)Lambda^2(m^{1,0}) ~= V0 (+) V2` (dim 4), and
`Sigma_even (x) Sigma_even ~= (V0+V2)(x)(V0+V2) = V0 (+) V2 (+) V2 (+) (V0+V2+V4)`, which has
**TWO** `SU(2)_diag`-trivial (`V0`) components: one from `Lambda^0(x)Lambda^0` (call it `w`,
the SAME object Round 59/65 used) and a SECOND one from `Lambda^2(x)Lambda^2`'s singlet (call it
`w'` — this is EXACTLY the "isotropy-trivial slot" E5 found and flagged). **Target dimension is
2, not 1.** This is established by pure representation theory (Clebsch-Gordan `V2(x)V2 = V0+V2+V4`,
already computed in E5) and does NOT depend on anything computed in this round — it is recorded
here, before running, as a genuine refinement of E5's finding: the "Route C" mechanism's target
space itself has a qualitatively different structure for S3xS3, not merely an "available slot"
in an otherwise-unchanged target.

**Consequence for what "PASS"/"FAIL" must mean here:** Because target is 2-dimensional, the
clean "(1,0)"-kernel/cokernel outcome that automatically followed from a 1-dimensional target
for the other three spaces does NOT directly transfer. This experiment's kill criteria (below)
are stated in terms of the SPECIFIC, well-defined quantity E5 flagged as undetermined — the
`w'`-component of `Term2(v_b)` — rather than force-fitting a literal "(1,0)" label onto a
structurally different target space. `Term1` is a GENERAL Killing-spinor fact (independent of
isotropy) that lands ENTIRELY in the `w` direction (never `w'`), so the `w`-channel result
(`rank >= 1` via `Term1 != 0`, exactly as Round 59/65 already showed generalizes) is NOT
re-litigated here — this experiment targets ONLY the previously-undetermined `w'`-channel.

---

## Estimand

**Population:** `S^3 x S^3 = SU(2)^3/SU(2)_diag`, the one Butruille nearly-Kahler 6-manifold
where Round 70/E5 found the Route-C representation-theoretic shortcut does not apply.

**Intervention:** Build the explicit Levi-Civita canonical (Nomizu-map) connection on `m` from
CH2016's own page-18 structure constants; spin-lift it via the AHL2023-style Clifford module
`Sigma = Lambda^*(m^{1,0})`; calibrate against the general Killing-spinor equation; compute
`Term2(v_b) = sum_i (e_i . topwedge) (x) (nabla_i(1))` exactly; project onto the `w'` singlet
inside `Lambda^2(m^{1,0})(x)Lambda^2(m^{1,0})` found present by E5.

**Comparator:** S6's own Round 59 result (`Term2`'s only available target direction is absent
entirely, so the question does not arise there) and the general "no isotropy-trivial slot exists"
structural difference E5 established for the other three spaces.

**Endpoint:** Is `<w', Term2(v_b)>` exactly zero or exactly nonzero (symbolic, sympy-exact, not
a numerical/floating-point question)?

**Summary measure:** A PASS/FAIL/ILL-POSED/BLOCKED verdict (defined below), plus the exact
symbolic value of `<w', Term2(v_b)>`.

**MCID:** Not applicable — binary (zero vs nonzero) structural/algebraic question, exact
arithmetic, no measurement noise.

---

## Claim

**Falsifiable statement:** The isotropy-trivial (`w'`) slot inside
`Lambda^2(m^{1,0})(x)Lambda^2(m^{1,0})` that E5 found present (unlike S6/SU(3)-T2/CP3) either
(a) carries an EXACTLY ZERO `Term2` coefficient under the explicit Levi-Civita canonical
connection built from CH2016's own stated `su(2)^3` structure constants — in which case the
Route-C-style rank-forcing argument extends to S3xS3 after all, matching the qualitative pattern
of the other three spaces (PASS) — or (b) carries a NONZERO coefficient, in which case the
isotropy-trivial slot genuinely obstructs the simple argument and an ADDITIONAL zero mode /
cokernel direction is forced for S3xS3 specifically, a genuine structural difference from the
other three spaces (FAIL) — or (c) the computation cannot be completed without an additional,
non-forced convention choice not resolvable from CH2016's own stated data (ILL-POSED) — or (d)
the computation is well-posed in principle but cannot be completed with reasonable effort in one
session, e.g. the calibration gate itself cannot be passed (BLOCKED).

---

## Kill criterion (MANDATORY — filled BEFORE running)

| Outcome | Verdict |
|---|---|
| Calibration gate (Levi-Civita connection reproduces the general Killing-spinor equation `nabla_X psi_pm = +/- mu X.psi_pm` for BOTH signs, all 6 directions, EXACTLY, for the SU(2)_diag-built connection) FAILS | **BLOCKED** — the substrate (connection/Clifford construction) cannot be trusted; do NOT report a PASS/FAIL verdict on `Term2` from an uncalibrated construction. |
| Calibration passes, AND `<w', Term2(v_b)>` computed **exactly zero** (symbolic) | **PASS** — Route-C-style mechanism extends: the available slot is not forced to cancel Term1's/kernel's clean structure; S3xS3's exact kernel picture is qualitatively the same as the other three spaces at the level E5's Schur bound already established (`dim ker <= 1`). |
| Calibration passes, AND `<w', Term2(v_b)>` computed **exactly nonzero** (symbolic) | **FAIL** — the isotropy-trivial slot genuinely carries signal: `Term2` does NOT vanish on it, a genuine, new, structural difference for S3xS3 (an ADDITIONAL zero mode/cokernel direction beyond the `w`-channel, i.e. the naive expectation `dim ker=1` for the FULL trivial block does NOT hold — the true answer needs the full domain-to-target rank, reported as a secondary finding, not overclaimed as "kernel=0"). |
| Building the Levi-Civita Nomizu map from CH2016's stated basis requires an extra, non-forced normalization choice with NO canonical resolution from the primary source (e.g. the metric-compatibility repair itself is ambiguous, not unique) | **ILL-POSED** |
| Metric-compatibility repair (Hermitization) is well-defined and unique, calibration is reachable in principle, but the resulting symbolic computation cannot be completed with reasonable one-session effort (e.g. genuinely intractable symbolic blow-up) | **BLOCKED** |

**Explicit escape route:** one session only. If the calibration gate fails after 2 independent
attempts to fix the connection/basis construction (per Stuck Detection Tier 1-2), the verdict is
BLOCKED, not a forced PASS or FAIL — an uncalibrated connection cannot certify anything about
`Term2`. This experiment does NOT attempt to resolve the project's own open Kostant-Parthasarathy
`t=1/3` vs `t=1/2` tension for S6 (out of scope, per the task's explicit constraint) — it uses
ONLY the Levi-Civita (`t=0`) connection, calibrated independently against the general Killing
equation, which is a SEPARATE, already-settled fact (Round 59) not entangled with that tension.

## What this does NOT mean

- A PASS verdict does NOT re-derive or re-certify the FULL Atiyah-Singer index / exact kernel
  count for S3xS3's physically-relevant twisted operator (that remains a separate, larger, still
  out-of-scope computation, exactly as E5 and Round 51 already scoped) — it settles ONLY the
  specific `w'`-component question E5 flagged as the concrete blocking unknown.
- A FAIL verdict does NOT mean S3xS3 fails "Universality" outright — it means the SPECIFIC
  Route-C-style two-line shortcut does not extend cleanly, and the target space for S3xS3's
  trivial block is genuinely 2-dimensional (not 1-dimensional as for the other three spaces),
  requiring a full rank computation (reported as a secondary, non-primary finding if reached)
  rather than a simple zero/nonzero scalar check, to determine the actual kernel dimension.
- Does NOT touch, weaken, or overturn S6's own established `N_gen=3` result (G73, G74A) or
  `preprint.tex`'s own open Levi-Civita-vs-cubic-Dirac caveat for S6 — this experiment's
  Levi-Civita construction is independently calibrated (Round 59's own precedent), not borrowed
  from the disputed norm-bound estimate.
- An ILL-POSED or BLOCKED verdict does NOT mean S3xS3's Universality question is permanently
  closed — only that THIS specific attempt, within one session, could not certify an answer;
  a future round with more budget (e.g. consulting CH2016's earlier pages on the specific
  3-symmetric-space eigenbasis derivation, currently opaque from pages 13-19 alone) could revisit.

---

## Fence (do not change without postmortem)

- lambda = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

See `decision.md`.
