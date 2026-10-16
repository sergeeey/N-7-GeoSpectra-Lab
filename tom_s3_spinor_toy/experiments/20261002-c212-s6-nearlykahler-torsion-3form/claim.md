# C212 Claim — explicit nearly-Kahler torsion 3-form on S6=G2/SU(3)

**Date:** 2026-10-02
**FL tier:** [ ] Micro  [ ] Standard  [x] Full
**Question type:** [x] descriptive  [ ] predictive  [ ] causal

---

## Prior Result Gate (MANDATORY)

1. Exact claim: the torsion 3-form of S6's characteristic connection
   (Agricola-Borowka-Friedrich, arXiv:1707.08591, Prop 4.2), evaluated
   explicitly on G96's own certified complement basis, gives a specific,
   TOTALLY ANTISYMMETRIC tensor T_abc.
2. `decision.md`/`null_results` grep (`torsion`, `naturally reductive`,
   `characteristic connection`): [x] done -- hits are all about a
   DIFFERENT object (the L4B Dirac-operator's own torsion-cross-term,
   Agricola 2002's Theorem 3.2 on D^t, Dolan-Casimir) -- none compute
   the octonion-cross-product torsion 3-form of S6 itself. See
   `round53-torsion-scaling-agricola-audit/decision.md` for the nearest
   prior (different object: operator-norm bound, not this 3-form).
3. `null_results/` + `parked/`: 0 hits for this specific object.
4. Primary source re-read: [x] done -- full text (not abstract) fetched
   via `mcp__arxiv__download_paper(1707.08591)`, Proposition 4.2's proof
   read directly, not paraphrased from memory.
5. **Status:** [x] NEW

---

## Estimand

**Population:** G96's own already-certified G2/SU(3) construction
(14 g2 generators, 8-dim su(3) stabilizer of the point N=e6, 6-dim
complement verified as an SU(3) representation 3+3bar).
**Intervention:** evaluate T^c(X,Y,Z)=-<N,(XxY)xZ> (Agricola et al.
Prop 4.2) at the base point N, with X,Y,Z ranging over the tangent
basis v_a = K_a@N (K_a the complement generators).
**Comparator:** none internal yet -- this is the FIRST explicit
computation of S6's own nearly-Kahler torsion in this project (F6's
own stated gap: "S6's own curvature -- never certified" applies
equally to its torsion before this round).
**Endpoint:** T_abc (6x6x6 tensor), |T|^2=sum(T_abc^2), max|T_abc|.
**Summary measure:** |T|^2 (basis/radius-dependent in absolute value,
same normalization-dependence caveat as C211's Term1/Term2).
**MCID:** n/a -- deterministic computation, not a statistical estimate.

---

## Claim

The octonion-cross-product torsion 3-form of S6=G2/SU(3)'s
characteristic connection, evaluated on G96's own certified basis, is
(a) totally antisymmetric (Gray's theorem, used here as the MANDATORY
positive control before trusting the magnitude) and (b) has a specific,
exactly-rational magnitude |T|^2=8/9 in the Frobenius-orthonormal
(unit-radius) convention.

---

## Kill criterion (MANDATORY)

| Kill condition | Threshold |
|---|---|
| Total antisymmetry fails | max asymmetry error > 1e-9 -- would mean the cross-product/formula transcription has a bug; magnitude MUST NOT be trusted if this fails |
| Cross product sanity fails (antisymmetry, orthogonality to both factors) | error > 1e-10 -- would mean `octonion_cross` itself is wrong, independent of the torsion formula |
| Tangent vectors degenerate | rank < 6 -- would mean the complement does not act freely at N, a problem with the reused G96 basis itself |

If FAIL (antisymmetry) -> kills: trust in this specific transcription of
Prop 4.2; does NOT kill Gray's theorem itself (independently published,
cited not re-derived) -- would mean MY implementation is wrong.
If PASS (all three) -> survives: a new, calibrated number for F6's own
S6-side gap, explicitly scoped (see below).

---

## Checks planned

| # | Check | Negative control |
|---|---|---|
| T1 | Cross product antisymmetric, orthogonal to both factors | n/a -- algebraic identity of any cross product; failure would be a pure code bug |
| T2 | Tangent vectors rank 6 | n/a -- would fail if complement generators were accidentally degenerate |
| T3 [MANDATORY POSITIVE CONTROL] | T_abc totally antisymmetric (Gray's theorem) | the theorem's own claim IS the control: a buggy transcription would generically NOT be antisymmetric, so passing this to machine precision (1.53e-16) is strong evidence the transcription is correct |

---

## What this does NOT mean

1. Does NOT give S6's Ricci tensor or Einstein constant -- this is the
   TORSION of the characteristic connection, a related but distinct
   object; no Ricci/scalar-curvature computation was attempted here.
2. Does NOT relate to C134/C207's ECSK torsion -- that torsion is
   sourced ALGEBRAICALLY by fermion zero-mode bilinears on the FULL 13D
   background (a physical equation of motion); THIS torsion is the
   INTRINSIC geometric torsion of the S6 factor's own nearly-Kahler
   structure (a fixed, a priori geometric fact, independent of any
   matter content). Same vocabulary ("torsion"), different objects --
   no claim of agreement, disagreement, or even comparability is made
   without first establishing a shared normalization/embedding, which
   this round does not attempt.
3. Does NOT establish the absolute value 8/9 as physical -- same
   normalization-dependence caveat as C211: it is tied to G96's
   Frobenius-orthonormal complement basis and unit-radius N. Only
   ratios/dimensionless combinations built consistently from this same
   convention are safe to quote.
4. Does NOT claim novelty of the MATHEMATICAL fact (Gray's theorem,
   Prop 4.2's formula are both already published, cited) -- the new
   content is evaluating them EXPLICITLY on this project's own already-
   certified G2/SU(3) data, which had not been done.

---

## Fence (do not change without postmortem)

- lambda = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

**PASS_CALIBRATED** — all three checks passed; positive control
(Gray's theorem) reproduced to machine precision (1.53e-16).

**Evidence:** [VERIFIED-numpy 3/3].

**Status:** CLOSED PASS_CALIBRATED — see `decision.md`.
