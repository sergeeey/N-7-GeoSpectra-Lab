# Round71-E6-S3xS3-Nomizu-Torsion-Audit Decision — ILL-POSED (two independent repair attempts, both fail to give a forced construction)

**Date:** 2026-07-17

**Verdict: ILL-POSED**, per claim.md's pre-registered kill-criteria table, row 4. Building the
explicit Levi-Civita canonical (Nomizu-map) connection for `S^3xS^3 = SU(2)^3/SU(2)_diag`
directly from CH2016's own stated page-18 data (`X_i,Y_i` basis + `B` normalization + stated
almost-complex-structure action) requires an additional, non-forced convention choice that has
NO canonical resolution from the primary source text available (CH2016 pages 2-6, 13-20). Two
independent repair attempts were made (per the claim.md escape route requiring >=2 attempts
before settling on BLOCKED/ILL-POSED rather than continuing indefinitely); both are tool-verified
to fail to reconcile the source's own stated data, and they disagree with each other, confirming
the obstruction is genuine rather than a single computational slip.

**This means the `Term2` value E5 flagged as the concrete open question (does the isotropy-trivial
slot in `Lambda^2(m^{1,0})(x)Lambda^2(m^{1,0})` carry a zero or nonzero coefficient) was NOT
reached — the calibration substrate needed to compute it exactly could not be certified as
trustworthy, per the Falsification Ladder's Verification Substrate Gate (Step 2a): an
uncalibrated/inconsistent connection construction is a substrate problem, not evidence about
the claim. E5's Schur bound (`dim ker <= 1`, independent of Route C) is UNCHANGED and remains
the strongest currently-certified fact about S3xS3's trivial block.**

All numbers below trace to `round71_s3xs3_nomizu.py` and its saved output `run_output.txt` —
none hand-typed independently of that file.

---

## Which Dirac operator convention this concerns (explicit, per task constraint)

This experiment used, and only used, the **Levi-Civita connection** (`nabla^0` in CH2016's own
family `nabla^t`, CH2016 eq. 7: `g(nabla^t_X Y,Z) = g(nabla^{LC}_X Y,Z) + (t/2)P(X,Y,Z)`, `t=0`
gives literally `nabla^{LC}`) — the SAME convention Round 59/65 used for S6/SU(3)-T2, and the
one `preprint.tex` uses as its physically-relevant operator. It does **NOT** use, and does not
touch, CH2016's canonical/characteristic connection `nabla^1` (their `D^{1/3,A}`, the operator
their own Prop 7/8 Kostant-Parthasarathy-style Casimir machinery is proved for, page 16, Prop 8:
`(D^{1/3,A})^2` built from `nabla^{t/3}` at `t=1`). This experiment therefore does **not**
resolve, inherit, or depend on the project's own already-open S6 tension
(`experiments/20260708-dolan-casimir-g2su3/`: Kostant-Parthasarathy proved only at `t=1/3`,
not `t=1/2`/Levi-Civita, plus the `8/45` vs `~1.03` norm-bound discrepancy) — that tension
concerns a DIFFERENT connection (`nabla^1`) than the one attempted here (`nabla^0`). The failure
found in this experiment is a **new, independent** obstruction, specific to transporting the
`nabla^0` (Levi-Civita) Nomizu-map construction to `SU(2)_diag` isotropy using CH2016's own
stated `su(2)^3` basis.

---

## Step 0 — transcription and structural checks (all `[VERIFIED-external-source]` + `[VERIFIED-tool]`)

Primary-source data transcribed directly from the PDF (`pymupdf`, this session):
- `g = su(2)(+)su(2)(+)su(2)`, basis `I_i^(a)` (CH2016 p.14/18), bracket
  `[I_i^(a),I_j^(b)] = delta_ab eps_ijk I_k^(a)`.
- `B(I_i^(a),I_j^(b)) = (1/6) delta_ij delta_ab` (CH2016 p.14 and p.18, restated identically in
  both places — this is CH2016's OWN normalization, used by them for their Prop 7/8 Casimir
  bookkeeping AND stated, in Section 4's opening paragraph, to be "the nearly Kahler metric ...
  induced from a multiple of the Cartan-Killing form" for **all four** homogeneous spaces).
- `H_i = I_i^(1)+I_i^(2)+I_i^(3)` (isotropy `su(2)_diag`, p.14).
- `X_i = (1+sqrt2)I_i^(1) + (1-sqrt2)I_i^(2) - 2I_i^(3)`, `Y_i = sqrt6(I_i^(1)-I_i^(2))` (p.18,
  EXACT transcription, verified against the PDF text directly this session).
- "The almost complex structure sends `X_i` to `Y_i` and `Y_i` to `-X_i`" (p.18, literal quote).

`[VERIFIED-tool]` checks (script STEP 0):
- `B(H_i,X_j)=0`, `B(H_i,Y_j)=0` for all `i=j` (orthogonality of `m` to `h`): **True**.
- `[H_i,H_j] = eps_ijk H_k`: **True** (isotropy genuinely closes as `su(2)`).
- `ad(H_i)(X_j) = eps_ijk X_k`: **True** — independently re-derived from the raw bracket table,
  matching CH2016's own stated fact (p.18) exactly. This cross-check confirms the `su(2)^3`
  bracket-table code itself is correct (it reproduces a fact CH2016 states independently).

---

## Step 1 — metric-compatibility check of the literal `(X_i,Y_i,J)` data (`[VERIFIED-tool]`)

For `J` to be Hermitian-compatible with a metric `g` (`g(JX,JY)=g(X,Y)`, required for `(g,J)` to
form a genuine almost-Hermitian/nearly-Kahler structure — this is definitional, not a choice),
`J(X_i)=Y_i` forces `g(Y_i,Y_i)=g(X_i,X_i)` and, separately, `g(JX,JY)=g(X,Y)` with `X=X_i,Y=Y_i`
forces `g(Y_i,-X_i) = g(X_i,Y_i)`, i.e. `g(X_i,Y_i)=0`.

Computed directly from CH2016's own stated `B` and basis (script STEP 1):
```
B(X_1,X_1) = 5/3
B(Y_1,Y_1) = 2
B(X_1,Y_1) = 2*sqrt(3)/3
```
**Neither required condition holds**: `5/3 != 2`, and `2*sqrt(3)/3 != 0`. CH2016's own literal
page-18 data — the SAME `B` used for their Prop 7/8 Casimir bookkeeping, combined with their own
literal statement of `J`'s action — is **not internally Hermitian-consistent** as stated.

This is reported as `[VERIFIED-tool]`, not a transcription error: STEP 0 already cross-checked
the transcription of `X_i,Y_i,B` against CH2016's OWN independently-stated facts (the `ad(H_i)`
action, the `-4` Casimir eigenvalue on `m*_C` already checked in Round 70/E5) and both matched
exactly. The inconsistency is between two DIFFERENT pieces of CH2016's own stated data (the `B`
normalization and the literal `J`-action sentence), not an error in reading either piece alone.

---

## Repair attempt 1 — Hermitize the metric, keep the literal `J` (`[INFERRED]` construction, `[VERIFIED-tool]` outcome)

Standard, general fact for any `(bilinear form, almost complex structure J)` pair with `J^2=-1`:
`g_H(V,W) := (1/2)[B(V,W)+B(JV,JW)]` is automatically Hermitian-compatible with `J`
(`g_H(JV,JV)=g_H(V,V)` and `g_H(V,JV)=0` both hold identically, by direct algebra — this is not
specific to S3xS3, it is a general linear-algebra fact). This is the FORCED, canonical way to
repair metric-compatibility for a FIXED `J` — not an arbitrary choice of which vector to rescale.

Computed (script STEP 1, continued): `g_H` is diagonal in the `(X_1,Y_1,X_2,Y_2,X_3,Y_3)` basis,
with all six diagonal entries equal to `kappa = 11/6` — confirms `g_H(X_i,X_i)=g_H(Y_i,Y_i)` and
`g_H(X_i,Y_i)=0` as the general theory predicts, and additionally confirms `g_H` is "isotropic"
(proportional to identity on the 2-dim multiplicity space), which is what a naturally-reductive
metric on a multiplicity-2 isotropy type would need to be.

**Decisive gate (script STEP 2): is `g_H` naturally reductive w.r.t. `m`?**
`g_H([U,V]_m,W) + g_H(V,[U,W]_m) = 0` for all `U,V,W` in the 6-dim `m`-basis — this is the
EXACT condition required for the standard formula `Lambda(V)(W) := (1/2)[V,W]_m` to actually BE
the Levi-Civita connection's Nomizu map (Besse, *Einstein Manifolds*, 7.44; Kobayashi-Nomizu vol.
2 ch. X — general fact, not S3xS3-specific).

**Control check (built into the same code path, run FIRST):** is the RAW, unmodified `B` (before
any Hermitization) naturally reductive? **General theorem predicts YES automatically** — `B` is
literally the restriction, via the reductive decomposition `g=h(+)m`, of an `Ad(g)`-invariant
form on the WHOLE Lie algebra `g` (a scalar multiple of the Killing form), and this ALWAYS
satisfies the natural-reductivity identity, for any homogeneous space, by a completely general
argument. Result: **`[raw B] ... True`** — the control passes, confirming the natural-reductivity
CHECKER CODE ITSELF IS CORRECT (it is not a bug that later produces a false negative).

**Actual test result: `[Hermitized g_H] ... False`.** `g_H` is **NOT** naturally reductive w.r.t.
`m`. Reason (structural, not just "the computer said so"): `g_H` is built using `J`, and `J` is
only preserved by `Ad(H)` (the isotropy group), not by the full `Ad(g)` action — so `g_H` is only
an `Ad(H)`-invariant form on `m`, not the restriction of an `Ad(g)`-invariant form on all of `g`,
which is exactly the hypothesis the general natural-reductivity theorem requires. Repairing
metric-compatibility (Step 1's Hermitization) silently broke a DIFFERENT property (natural
reductivity) that the original, unmodified `B` already had for free.

**Consequence:** the standard formula `Lambda(V)(W)=(1/2)[V,W]_m` is NOT valid for `g_H` — using
it anyway would silently compute the Nomizu map of a DIFFERENT (non-metric, or at least
non-Levi-Civita) connection, not the actual Levi-Civita connection of any genuine Riemannian
metric compatible with the stated `J`.

---

## Repair attempt 2 — keep `B` fixed, solve for the `B`-compatible `J_B` instead (`[VERIFIED-tool]`)

Per claim.md's escape route (>=2 independent attempts before settling on BLOCKED/ILL-POSED), a
SECOND, structurally different repair was tried: instead of modifying the metric to fit the
stated `J`, keep the metric `B` untouched (guaranteed naturally reductive by the control above)
and solve directly for the almost complex structure `J_B` that IS compatible with `B`
(`J_B^2=-1`, `B(J_B v,J_B w)=B(v,w)`). In a 2-real-dimensional space (the `{X_i,Y_i}` plane for
fixed `i`) this compatible `J_B` is unique up to the standard `+/-` orientation ambiguity present
in any complex-structure identification — NOT a genuine extra free parameter, so if `J_B` matches
CH2016's literal `J` up to that standard sign, the two repair paths would agree and there would
be no real obstruction.

Computed (script STEP 3), using `Mxy` = `B` restricted to `span{X_i,Y_i}` and the standard
"square-root-and-rotate" construction `J_B = M^{-1/2} R M^{1/2}` (`R` = 90-degree rotation):

```
J_B (acting on (X,Y)-coefficient vectors) =
[ -sqrt(6)/3     -sqrt(2)   ]
[  5*sqrt(2)/6    sqrt(6)/3 ]
```
verified `J_B^2 = -I` (**True**) and `J_B^T . Mxy . J_B = Mxy` (**True**) — `J_B` is a genuine,
correctly-computed `B`-compatible almost complex structure.

**Compared against CH2016's literal stated `J` (matrix `[[0,-1],[1,0]]` in the same `(X,Y)`
coordinates): `J_B == +/- J_literal`? False.** `J_B` has NONZERO diagonal entries; `J_literal`'s
diagonal is identically zero. This is not a rescaling, not a sign flip, not a basis-ordering
artifact — it is a **structurally different linear map**. The two repair strategies (fix-the-
metric vs. fix-the-complex-structure) give two DIFFERENT, mutually incompatible resolutions of
the Step-1 inconsistency, and CH2016's own stated text (pages 13-20, the only pages consulted
this session for the `SU(2)^3/SU(2)` case) gives no basis for preferring one over the other.

---

## Verdict classification (per claim.md's frozen kill-criteria table)

| Criterion | This round's finding |
|---|---|
| Calibration/substrate check reachable before attempting `Term2`? | **No** — the prerequisite Levi-Civita Nomizu-map construction itself could not be certified consistent (Steps 1-3), so the calibration gate (reproducing the general Killing-spinor equation, the actual decisive "can this fail" check Round 59 used) was never reached — there is no trustworthy connection to calibrate. |
| Extra, non-forced choice required, with no canonical resolution from the primary source? | **Yes**, confirmed by 2 independent, tool-verified repair attempts that disagree with each other. |

**=> ILL-POSED**, per claim.md row 4 exactly ("Building the Levi-Civita Nomizu map from CH2016's
stated basis requires an extra, non-forced normalization choice with NO canonical resolution from
the primary source"). This is NOT the BLOCKED outcome (that would require the choice to be
well-defined but the resulting computation intractable — that is not what happened; the choice
itself has no forced answer) and NOT a forced PASS or FAIL on `Term2` (no trustworthy computation
of `Term2` was ever performed, so no claim about its zero/nonzero value is made).

---

## Kill Analysis (OSA — required for a non-PASS verdict)

**What was killed:** The hope that CH2016's own page-18 `(X_i,Y_i,J)` data could be used
directly, as literally stated, to build an AHL2023/Round-59-style explicit Nomizu-map + Clifford
module construction for S3xS3 in one session. This is killed with two independent, structurally
different repair attempts (metric-side and complex-structure-side), both tool-verified, both
disagreeing with each other — not a single failed heuristic, and not attributable to a
transcription error (Step 0's independent cross-checks against CH2016's own stated facts both
passed exactly).

**What was NOT killed:**
- E5's own two established facts remain fully intact and unaffected: the isotropy-Schur bound
  `dim ker <= 1` for `S^- = m^{1,0}(+)1` (independent of Route C or any connection construction),
  and the Route-C crux finding itself (`Lambda^2(m^{1,0})(x)Lambda^2(m^{1,0})` DOES contain an
  isotropy-trivial component for S3xS3, unlike the other three spaces) — both survive this round
  untouched, since neither depends on the Nomizu-map construction attempted here.
- The POSSIBILITY that `Term2`'s coefficient on the isotropy-trivial slot is zero, nonzero, or
  requires a case-by-case resolution remains fully OPEN — this round neither confirms nor refutes
  any of the three; it only shows that ONE specific, natural attempt to settle it (reusing
  CH2016's own page-18 basis literally) does not go through without an extra choice.
- CH2016's own explicit `su(2)^3` bracket structure, `B` normalization, and the general Levi-
  Civita-Nomizu-map theory itself (all confirmed correct and internally consistent in Steps 0-2's
  control check) remain fully reusable in a future round — the obstruction is narrowly located in
  how the page-18 `X_i,Y_i,J` triple combines, not in the surrounding machinery.
- The general theorem "an `Ad(g)`-invariant form restricted via a reductive decomposition is
  automatically naturally reductive" — independently re-confirmed here as a control (not merely
  assumed) — remains available and correct for any future attempt using `B` directly.

**Relaxation Map (Minimal Relaxation Rule — one assumption changed at a time):**

| Relax this assumption | What it would take | Cost estimate |
|---|---|---|
| "CH2016's page-18 basis alone (pp.13-20) is sufficient" | Read CH2016's earlier general setup (Section 2, already partly read here, pp.2-6) AND any earlier pages (7-12, not read this session) that might define the SPECIFIC 3-symmetric-space eigenbasis construction (e.g. an order-3 automorphism `sigma` of `g`, whose `omega`/`omega^2` eigenspaces on `m_C` would be AUTOMATICALLY `B`-compatible, unlike the ad hoc basis used here) | Cheap-to-moderate: a few more pages of the SAME PDF, already in the repo |
| "Use CH2016's literal `J`-action as stated" | Use `J_B` (Repair attempt 2) instead, accepting it is NOT literally "sends `X_i` to `Y_i`" but IS `B`-compatible and naturally reductive by construction, then redo the whole Clifford/calibration/Term2 chain with `J_B` | Moderate: the full Clifford-module + calibration construction (not yet built) would need to be built once, using `J_B` in place of `J` |
| "Levi-Civita connection specifically" | N/A — already the correct choice per the task's explicit convention constraint; not a relaxation candidate |
| "One session only" | Allow a second session with a literature check for the standard `Z_3`-symmetric-space construction of `S^3xS^3`'s NK structure (a well-known construction in the broader 3-symmetric-space literature, e.g. via cube-root-of-unity eigenspaces of the cyclic factor-permutation automorphism) that would likely resolve the ambiguity by CONSTRUCTION rather than by picking between two ad hoc repairs | Moderate — this is the most promising single next step |

---

## Pearl Gate scan (mandatory, per Falsification Ladder)

**Unexpected but testable insight:** CH2016's own page-18 data exhibits an internal tension
between its stated bilinear form `B` (used for their OWN Casimir/Prop-7-8 bookkeeping and,
per their Section 4 opening paragraph, claimed to be literally the nearly-Kahler metric for
ALL FOUR homogeneous spaces) and its stated almost-complex-structure action on the SAME basis.
This is recorded as a `[CANDIDATE]` pearl (impact_score 3/10 — narrow: it affects only how a
future round should approach S3xS3's specific basis, not this project's core `N_gen=3` claim or
any of the other three Butruille spaces, whose own page-14/15/21-22 basis data was already
independently verified consistent in Round 70/E5 and Round 65) rather than promoted: the most
likely resolution (per the Relaxation Map above) is that CH2016's page-18 basis is adapted for a
DIFFERENT purpose (describing the `su(2)->su(3)` gauge-embedding structure for their instanton-
deformation problem, Prop 7/8's "gauge group SU(3)" case) rather than for directly supplying an
orthonormal-adapted Hermitian basis for the tangent-space Clifford module — a hypothesis that a
future round could check cheaply by reading CH2016's remaining un-consulted pages (7-12) for an
explicit `Z_3`/cyclic-automorphism-based construction of the actual NK complex structure.
`next_check`: if a future round attempts this same S3xS3 Nomizu-map construction again, first
check CH2016 pp.7-12 (not consulted this session) for a direct `sigma`-eigenspace definition of
`m^{1,0}`, which would sidestep this round's entire obstruction by construction.

---

## What this does NOT mean (carried from claim.md, unchanged)

- Does NOT mean S3xS3 fails "Universality" — only that this SPECIFIC attempt to certify the
  `Term2` coefficient, within one session, using CH2016's page 13-20 data literally, could not be
  completed with a trustworthy substrate.
- Does NOT touch, weaken, or overturn S6's own established `N_gen=3` result (G73, G74A) or
  `preprint.tex`'s own open Levi-Civita-vs-cubic-Dirac caveat for S6.
- Does NOT resolve or inherit the project's own open Kostant-Parthasarathy `t=1/3` vs `t=1/2`
  tension (`dolan-casimir-g2su3`) — this experiment concerns a different connection (`nabla^0`)
  than that tension (`nabla^1`), as stated explicitly above.
- Does NOT close the door on a future attempt — the Relaxation Map above gives concrete,
  reasonably cheap next steps (reading CH2016 pp.7-12, or building the full construction with
  `J_B` instead of the literal `J`), neither of which was itself ruled out by this round.

---

## Independent cross-validation (external audit pass, added post-hoc, same day)

Per this project's own `audit-verification-gate.md` ("agent's [VERIFIED] != your [VERIFIED]"),
this experiment's core findings were re-derived from scratch by an independent reviewing pass,
using a **structurally different route** than `round71_s3xs3_nomizu.py`, before that script was
read in full: CH2016's **Appendix C** basis (`K_i=(J_i,-J_i,0)`, `L_i=(J_i,J_i,-2J_i)`, page 25)
instead of the script's page-18 `(X_i,Y_i)` basis, plus a general `(a,b,c)`-parametrized
`Ad(H)`-invariant metric on `m=V2(+)V2` swept exhaustively over all `6x6x6` basis-triple
combinations (`sympy`, exact), rather than the script's direct 6-vector Hermitization route.

**Result 1 (metric-incompatibility numbers): exact match.** Converting the independent `K,L`-basis
result to the script's own `X,Y` basis (`X_i=L_i+sqrt(2)K_i`, `Y_i=sqrt(6)K_i`, matching page 18's
stated coefficients exactly) reproduces `B(X,X)=5/3`, `B(Y,Y)=2`, `B(X,Y)=2*sqrt(3)/3` bit-for-bit
— the identical numbers `round71_s3xs3_nomizu.py` Step 1 reports, obtained independently.

**Result 2 (natural-reductivity condition): exact match, plus a conceptual explanation of Step 2's
control check.** The independent full symbolic sweep (`T(u,v,w)+T(u,w,v)=0` for all
`u,v,w in {K_i,L_i}`) gives the natural-reductivity condition `b = 3a, c = 0` (up to overall
scale) on the `K,L`-basis metric `(a,b,c)`. Raw `B` in this basis is `(a,b,c)=(1/6*2, 1/6*6, 0) =
(1/3, 1, 0)`, and `1 - 3*(1/3) = 0` **exactly** — raw `B` sits precisely on the unique
natural-reductivity ray. This independently confirms, via a different computational path, WHY
`round71_s3xs3_nomizu.py`'s Step 2 control check (`raw B is naturally reductive: True`) must hold
(not merely that it empirically does) — and, by the SAME uniqueness (the ray is 1-dimensional up
to scale), why the Hermitized `g_H` (which is provably NOT proportional to raw `B`, since raw `B`
already fails `J`-compatibility per Result 1) CANNOT also be naturally reductive: natural
reductivity pins the metric ray uniquely, `g_H` is off that ray by construction.

**Conclusion of the cross-check:** two independent routes — different basis (page-18 `X,Y` vs
Appendix-C `K,L`), different method (direct 6-vector Hermitization + pairwise check vs general
3-parameter sweep over all basis triples) — converge on the identical numeric and structural
result. This upgrades the ILL-POSED verdict from `[VERIFIED-tool]` (single script, single basis)
to independently-reproduced (still internal to this session/repo; external human or cross-model
review remains the next rung up per the Verification Strength Ladder, `falsification-ladder.md`).
No discrepancy was found between the two routes.

---

## Files

- `claim.md` — frozen before this round's computation, including the pre-registered kill-criteria
  table and the explicit escape route requiring >=2 independent repair attempts before a
  BLOCKED/ILL-POSED verdict.
- `round71_s3xs3_nomizu.py` — from-scratch verification script: `su(2)^3` bracket table
  (cross-checked against 2 independent CH2016-stated facts), metric-compatibility check (Step 1),
  natural-reductivity check with a built-in control (Step 2), and the second independent repair
  attempt via the `B`-compatible complex structure `J_B` (Step 3).
- `run_output.txt` — actual run output (exit code 0); every number in this decision traces to
  this file, none hand-typed independently of it.
- Independent cross-validation (this addendum) — computed in a scratch file outside the repo
  (`Appendix-C K,L basis + full (a,b,c) symbolic sweep`), not committed as a separate script since
  it reproduces (not extends) `round71_s3xs3_nomizu.py`'s findings via a different route; the exact
  commands are reproducible from CH2016 Appendix C (page 25-26) plus the general natural-
  reductivity identity `g([U,V]_m,W)+g(V,[U,W]_m)=0` stated in Step 2 of the script.
