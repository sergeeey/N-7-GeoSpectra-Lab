---
# Round70-E5-Universality-CP3-S3xS3 Claim — corrected CP3 re-test + NEW S3xS3 test
# using the frozen "Route C" protocol shared by Round 59 (S6) and Round 65 (SU(3)/T2)

**Date:** 2026-07-17
**FL tier:** [x] Standard (two independent probes, one session, explicit escape route)
**Question type:** [x] descriptive

---

## Prior Result Gate (MANDATORY — filled BEFORE computing anything)

1. Exact claim: (A) was Round 64's CP3 "ILL-POSED" verdict a genuine structural
   fact about CP3=Sp(2)/(Sp(1)xU(1)), or a fixable setup error (wrong source /
   wrong bundle choice)? (B) does the SAME rank-forcing mechanism Round 59
   (S6) and Round 65 (SU(3)/T2) used generalize to S3xS3=SU(2)^3/SU(2), with a
   correctly-specified fermion bundle?
2. `decision.md` grep: done.
   - `experiments/20260715-round64-universality-cp3-probe/decision.md` —
     ILL-POSED, reason given: CH2016's instanton-deformation machinery only
     ever twists by the ADJOINT bundle, never the fundamental/tangent
     representation this project's S^- needs, and "the twisting bundle E
     CH2016 would need to supply is never instantiated anywhere in the paper."
   - `experiments/20260715-round65-su3t2-killing-spinor-test/decision.md` —
     PROMOTE, establishing the actual re-usable mechanism (Round 59's
     "Route C": Killing-eigenvalue nonzero + Term2-analog vanishes because
     Lambda^2(m^{1,0})(x)Lambda^2(m^{1,0}) has no isotropy-trivial component)
     on a SECOND space, with an explicit warning that CP3's ILL-POSED
     verdict came from a DIFFERENT route (L4A/CH2016-instanton-deformation)
     than Route C, so CP3 is NOT thereby excluded from Route C specifically.
     This round executes that exact unclaimed follow-up.
   - `reports/PROJECT_360_ROUND3_SYNTHESIS.md`, `reports/100_DIRECTIONS_BRAINSTORM_2026-07-17.md`
     item 87 correction: both read, both state S3xS3 "remains to be checked
     with a correctly-specified fermion bundle and operator" — this round's
     Part B target.
3. `round*_claim.md` + scripts grep: done. No script anywhere in this repo
   touches `Sp(1)`, `sp1u1`, `SU(2)^3`, or `S3xS3` isotropy representation
   theory before this round.
4. `null_results/` + `parked/` grep: done, 0 hits for CP3/S3xS3/universality
   beyond Round 51/64/65's own scoping (already read in full above).
5. `git log -S`/`-G` pickaxe: done, 0 hits outside the cited rounds.
6. Primary source re-read: **done, directly from the PDF via `pymupdf`, by
   this session** (not from Round 51/64/65's summaries) —
   `Charbonneau_Harland_2016_NK_instantons.pdf`, pages 11-22 (Section 4,
   "Instantons on homogeneous nearly Kahler manifolds", Proposition 7 /
   Theorem 3). Full isotropy-representation data for ALL FOUR Butruille
   spaces transcribed directly (page/equation citations in decision.md).
7. **Status:** [x] NEW for both sub-claims.

---

## Explicit risk flagged BEFORE starting (learned from Round 64 AND Round 65,
## same lineage)

Round 64's failure mode: assumed a "clean, reusable" formula transferred
across spaces without checking whether it answers the SAME QUESTION on the
new space. Round 65 (same session, immediately after) built in an explicit
safeguard against repeating this and found a DIFFERENT, genuinely-portable
mechanism (Route C) that DOES generalize, re-derived (not copy-pasted) for
`SU(3)/T^2`'s own isotropy representation theory.

**This round's OWN risk to guard against:** conflating "the isotropy
representation data exists in CH2016" (true — CH2016 §4 states m*_C for ALL
four spaces, verified independently below) with "therefore Round 64's
ILL-POSED finding was simply wrong." These are DIFFERENT claims. This round's
Part A explicitly separates: (i) is CH2016's INSTANTON-deformation machinery
(what Round 64 tested) reusable — re-confirmed NO, for an additional reason
found this round (see decision.md); (ii) is the RAW representation data
(m*_C decomposition) usable as an INGREDIENT for a DIFFERENT, correctly-posed
mechanism (Route C) — YES, and this round computes it.

**A second risk, specific to the Lichnerowicz/Kostant-Parthasarathy (L4A/L4B)
mechanism this project ALSO uses for S6 (G74A):** `preprint.tex` itself
(\S\ref{sec:schur}) and `experiments/20260708-dolan-casimir-g2su3/decision.md`
(21-round investigation) both document an UNRESOLVED internal tension for
S6 itself — the Kostant-Parthasarathy Casimir-difference formula is a
theorem ONLY for Kostant's cubic Dirac operator (t=1/3), NOT proven for the
physically-relevant Levi-Civita operator (t=1/2), and a separate norm-bound
estimate (8/45) is in outright numerical tension with a later, more careful
computation (~1.03) on the SAME reference case. Given this, this round does
NOT attempt to reproduce an exact, calibrated Lichnerowicz/Kostant-Parthasarathy
NUMBER for CP3/S3xS3 — doing so honestly would first require resolving this
project's OWN already-open S6 tension, which is out of one-session scope
(matches Round 51's cost re-estimate). Route C is chosen as the PRIMARY
mechanism for exactly this reason: it does not depend on any disputed
norm-bound/normalization-conversion step.

---

## Estimand

**Population:** (A) `CP^3 = Sp(2)/(Sp(1)xU(1))`; (B) `S^3xS^3 = SU(2)^3/SU(2)`
— the two remaining unresolved Butruille nearly-Kahler homogeneous 6-manifolds
for this project's "Universality" open problem.

**Intervention:** Apply Round 59/65's Route C protocol (frozen, unchanged in
structure):
  1. Killing spinor with nonzero eigenvalue exists (general NK fact, reused
     unconditionally, not re-derived — CH2016 \S2, valid for all four spaces).
  2. Identify `m^{1,0}` (the holomorphic isotropy-representation piece of the
     complexified tangent space) via the SU(3)-structure requirement that
     `Lambda^3(m^{1,0})` be isotropy-invariant — checked explicitly per space,
     not assumed.
  3. Define this project's own `S^- = m^{1,0} (+) 1` convention (SAME as S6's
     `T^{1,0}S^6 (+) 1`).
  4. Route-C crux: does `Lambda^2(m^{1,0}) (x) Lambda^2(m^{1,0})` contain an
     isotropy-trivial component? (S6/SU(3): NO. `SU(3)/T^2`: NO, Round 65.)
  5. Isotropy-Schur bound (G74A "Lemma B" analog, independent of Route C):
     multiplicity of the H-trivial representation in `S^- = m^{1,0}(+)1`.

**Comparator:** S6's own established results (Route-C argument holds, no
singlet in `3bar (x) 3bar`; Schur bound `dim ker <= 1`) and `SU(3)/T^2`'s
Round 65 result (same qualitative outcome, independently re-derived for `T^2`
isotropy).

**Endpoint:** For each of CP3 and S3xS3: (i) does the Route-C crux step go
through (PASS) or not (FAIL/inconclusive)? (ii) what is the isotropy-Schur
bound on `dim ker`? (iii) what is `chi(M)` (Euler characteristic, a general,
always-computable necessary — not sufficient — ingredient for a full
Atiyah-Singer index, via `c_3(T^{1,0}M) = chi(M)`, Chern-Gauss-Bonnet)?

**Summary measure:** A PASS/FAIL verdict per space per mechanism, plus the
Schur-bound integer and the Euler characteristic integer.

**MCID:** Not applicable — procedural/structural probe, binary+integer
outcomes, not a numeric hypothesis test.

---

## Claim

**Falsifiable statement (Part A, CP3):** Round 64's ILL-POSED verdict was
CORRECT for the specific mechanism it tested (CH2016's own instanton-
deformation machinery, which never twists by the fundamental/tangent
representation) but does NOT by itself preclude a DIFFERENT, correctly-posed
mechanism (Route C) from being computable and passing on CP3, using ONLY
already-published isotropy representation data (CH2016 eq. 27-28) and
already-proven general facts (SU(3)-structure top-wedge invariance,
Clebsch-Gordan decomposition) — no new derivation of machinery.

**Falsifiable statement (Part B, S3xS3):** The SAME Route-C mechanism,
re-derived (not copy-pasted) for `SU(2)_diag` isotropy using CH2016's own
stated `m*_C ~= 2*V2` data (page 14), either goes through unchanged (PASS,
third data point for the Round 59 pearl) or fails at an identifiable specific
step (the isotropy-dependent `Lambda^2(x)Lambda^2` singlet check).

---

## Kill criterion (MANDATORY — filled BEFORE running)

| Outcome (per space) | Verdict |
|---|---|
| `Lambda^3(m^{1,0})` invariance check fails for BOTH candidate splits of `m*_C` | ILL-POSED — no consistent SU(3)-structure `m^{1,0}` exists with the data at hand; matches Round 64's original finding, unfixable within this probe |
| `Lambda^3(m^{1,0})` invariance check succeeds for exactly one split, AND `Lambda^2(m^{1,0})(x)Lambda^2(m^{1,0})` has NO isotropy-trivial component | PASS (Route C mechanism holds — third/fourth data point for the universality pearl, still not a full L4A/L4B derivation) |
| `Lambda^3` check succeeds, but `Lambda^2(x)Lambda^2` DOES contain an isotropy-trivial component | INCONCLUSIVE-BY-THIS-ROUTE (NOT a hard structural NULL — an available trivial slot means the simple "no singlet forces vanishing" argument does not apply; whether the actual Term2 coefficient is zero or not would require the explicit torsion/Nomizu structure constants of that space, a further derivation step, out of scope here) |
| Isotropy-Schur bound (Lemma B) computation itself fails (e.g. `m^{1,0}` turns out to contain an isotropy-trivial summand, breaking the "exactly one from the `1`-summand" bound) | STRUCTURAL-NULL for the Schur bound specifically (independent of the Route-C verdict) |

**Explicit escape route:** one session only. The full Lichnerowicz-norm-bound
/ Kostant-Parthasarathy Casimir-difference NUMBER (the L4A/L4B mechanism,
distinct from Route C) is explicitly OUT OF SCOPE for an exact, calibrated
reproduction — see risk flag above. This round reports CH2016's own
internally-consistent Casimir data (`Cas_g` vs `Cas_h`) as a qualitative,
NOT normalization-calibrated, directional indicator only, and states plainly
that a full reproduction requires resolving this project's own already-open
S6 tension first (out of scope, matches Round 51's cost re-estimate of
~0.3-0.5 priority).

## What this does NOT mean

- A PASS verdict on Route C for CP3 or S3xS3 does NOT establish `dim ker=1`
  for the physically-relevant Levi-Civita twisted Dirac operator — Route C
  (like Round 59/65) only forces `rank(D+|trivial-block) = 1` for the SPECIFIC
  two-line Killing-spinor argument; it does not touch the L4A/L4B
  Lichnerowicz-norm-bound question, which remains open for S6 itself.
- Does NOT mean an INCONCLUSIVE-BY-THIS-ROUTE verdict (if it occurs) closes
  the door on that space for ALL mechanisms — only that this SPECIFIC,
  cheap, representation-theoretic shortcut does not decide it; an explicit
  torsion-tensor computation could still settle it in a future round.
- Does NOT commit to an exact Atiyah-Singer index computation for CP3/S3xS3
  — the Euler-characteristic data point (`c_3(T^{1,0})=chi(M)`) is reported
  as a NECESSARY, not sufficient, ingredient; the full index needs the
  complete Chern character of `S^-`, not just its top Chern class, which is
  explicitly flagged as future work, not attempted here.
- Does NOT re-open or edit Round 64's own decision.md — this round's
  correction to its framing is recorded here and in this folder's own
  decision.md only, per the task's explicit constraint.

---

## Fence (do not change without postmortem)

- lambda = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

See `decision.md`.
