# C211 Claim — CSDR gravity-moduli potential for S6=G2/SU(3)

**Date:** 2026-10-02
**FL tier:** [ ] Micro  [ ] Standard  [x] Full
**Question type:** [x] descriptive  [ ] predictive  [ ] causal

---

## Prior Result Gate (MANDATORY)

1. Exact claim: the CSDR gravity-moduli potential's structure-constant
   terms (eq. 4.27 of Chatzistavrakidis-Manousselis-Prezas-Zoupanos,
   arXiv:0712.2717), evaluated on this project's own already-certified
   G96/C210 G2/SU(3) generators, give a specific finite number.
2. `decision.md` grep (`csdr`, `coset space dimensional`): [x] done —
   5 hits: g21-extended-schur, g26-ccm-comparison, **g69-csdr-coset**,
   clifford-convention-repo-audit, **c132-13d-parent-action-survey**.
3. `round*_claim.md` + scripts grep: n/a (no round-numbered duplicate found).
4. `null_results/` + `parked/` grep: [x] done, 0 hits for
   `csdr`/`coset-coset`/`moduli potential`.
5. `git log -S`/`-G` pickaxe: not run (new, externally-sourced formula,
   first use of eq. 4.27's specific terms in this repo).
6. Primary source re-read: [x] done — full text (not abstract) fetched via
   `mcp__arxiv__download_paper(0712.2717)`, eq. 2.1-2.27, 4.1-4.27 read directly.
7. **Status:** [x] NEW (related-but-distinct prior work found, see below)

**Two related hits, both read in full, neither a duplicate — Mechanism
Transfer Gate (FORMULA/OBJECT/SECTOR all differ):**

- **G69** (`experiments/20260621-g69-csdr-coset/decision.md`, 2026-06-21):
  used CSDR on G2/SU(3) to derive FERMION CONTENT (Spin(6)->SU(3) spinor
  branching, 3+3bar+1+1), explicitly disclaiming "does NOT claim CSDR is
  the physical mechanism — it is a computational verification tool."
  C211 uses a DIFFERENT CSDR formula (the metric-moduli SCALAR POTENTIAL
  from structure constants, eq. 4.27) for a DIFFERENT object (the
  gravitational background, not fermion representation content).
- **C132 P11** (`experiments/20260902-c132-13d-parent-action-survey/
  decision.md:715`): used Forgacs-Manton's PURE-GAUGE CSDR potential
  ("part (i)") on **S3=SU(2)/{e}** (trivial isotropy, group manifold),
  scored `PASS` on the Zero-Signal screen but ranked 0/unranked on CDT
  **specifically against C132's own t-selection question (P-II pairing)**.
  C211 is a different SECTOR (S6=G2/SU(3), nontrivial isotropy, non-symmetric
  coset) using a different, gravity-aware formula (eq. 4.27, not Forgacs-
  Manton's pure-gauge "part (i)") for a different question (F6's background-
  EOM gap, not t-selection) — P11's low CDT rank for C132's question does
  NOT transfer to this question (verdict-non-transfer, per
  `artifact-provenance-gates.md` Gate 1's hard rule, generalized).

---

## Estimand

**Population:** the single already-certified G2/SU(3) coset structure this
project uses for S6 (G96's 14 generators, SU(3) stabilizer of e6, 6-dim
complement verified as 3+3bar under SU(3) — C210 independently confirmed
the same object's root system matches standard G2).
**Intervention:** evaluate eq. (4.27)'s first two (gravity-only, non-
symmetric-coset) terms using this coset's own [complement,complement]
structure constants, in the complement's own Frobenius-orthonormal basis
(gamma_ab = delta_ab convention).
**Comparator:** none internal to this project yet — S6's own background
EOM has never been derived here (F6's own stated gap); this is a new,
externally-sourced input, not a cross-check against an existing S6 result.
**Endpoint:** Term1 = sum(f^a_bc)^2, Term2 = 2*sum f^c_da f^d_ca (both
dimensionless, basis/normalization-dependent in absolute value; their
RATIO is normalization-invariant).
**Summary measure:** the two term values and their ratio.
**MCID:** n/a — this is a single deterministic computation, not a
statistical estimate; "practically important" here means "nonzero",
confirming G2/SU(3)'s non-symmetric character has a real effect on V.

---

## Claim

The CSDR gravity-moduli potential (eq. 4.27, Chatzistavrakidis et al. 2007),
evaluated on G96/C210's own certified G2/SU(3) structure constants, gives
Term1 and Term2 that are BOTH nonzero (confirming non-symmetric-coset
character) and whose ratio Term2/Term1 is an exact, normalization-
independent number.

Supporting sub-claims:
1. The complement (3+3bar, 6-dim) together with su(3) (8-dim) fully spans
   g2 (sanity check: [complement,complement] has zero residual outside
   su3+complement — tests that G96's own basis-splitting is complete,
   independent of whether C211's specific contraction is interesting).
2. Term1, Term2 are computable directly from G96's generators with no new
   assumption beyond the gamma=delta (unit-radius) normalization choice.

---

## Kill criterion (MANDATORY)

| Kill condition | Threshold |
|---|---|
| [complement,complement] not fully spanned by su3+complement | residual > 1e-9 (would mean G96's own basis split is incomplete — kills the SETUP, not just this claim) |
| Term1 = 0 | would mean G2/SU(3) behaves as symmetric for this contraction — contradicts the paper's own stated remark and the known non-symmetric/nearly-Kahler character of G2/SU(3) |

If FAIL (residual check) → kills: trust in G96's su3/complement split itself,
a much bigger problem than this round — would need re-opening G96/C210.
If FAIL (Term1=0) → kills: this specific claim only; would mean the paper's
"non-zero only for non-symmetric cosets" remark does not apply here, which
would itself be a notable (if surprising) finding worth a skeptic pass.
If PASS → survives: a new, externally-anchored numeric input for F6 — does
NOT by itself close F6 (see "What this does NOT mean").

---

## Checks planned

| # | Check | Negative control |
|---|---|---|
| T1 | su3+complement spans [complement,complement] (residual ~0) | n/a — this IS the control: if G96's basis were wrong, residual would be large |
| T2 | Term1 != 0 | if comp_gens were accidentally built from a SYMMETRIC coset's generators (e.g. S6=SO(7)/SO(6), round sphere), Term1 would vanish identically — not run here, but named as the theoretical negative case |
| T3 | dim checks (g2=14, su3=8, complement=6) match G96/C210 exactly | any mismatch would mean the reused generators diverged from the certified object |

---

## What this does NOT mean

1. Does NOT close F6 — this is ONE term of the CSDR effective Lagrangian's
   potential (eq. 4.26), for the GRAVITY-only, non-symmetric-coset piece;
   the gauge-sector terms (third term of 4.27, needs an explicit embedding
   of SU(3) into a higher-D gauge group this project has not fixed) and
   the kinetic/torsion structure (C134/C207's ECSK formalism) are NOT
   included and are NOT shown consistent or inconsistent with this result.
2. Does NOT claim CSDR is THE physical mechanism for this project's
   background (same disclaimer G69 already made for its own, different,
   CSDR use) — it is evaluated here as a candidate, externally-sourced
   formula against already-certified algebra, nothing more.
3. Does NOT establish the ABSOLUTE values (8, -16, -8) as physical — they
   are gauge/normalization-dependent (scale as 1/rho_6^2 type factors the
   paper itself keeps separate via e^{...phi} prefactors). Only the RATIO
   Term2/Term1 is normalization-invariant and worth quoting as a number.
4. Does NOT cross-check against round111's S3 Ricci scalar or C134/C207's
   torsion EOM — those are S3-sector, metric/torsion results; this is an
   S6-sector, pure-coset-structure-constant result. No claim of agreement
   or disagreement between them is made.

---

## Fence (do not change without postmortem)

- lambda = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

**PASS** — both kill conditions cleared (residual 8.74e-16 < 1e-9; Term1=8 != 0).

**Evidence:** [VERIFIED-sympy/numpy 3/3] — residual check, Term1 != 0, dims
match G96/C210 exactly (14/8/6).

**Status:** CLOSED PASS_NEW_INPUT — see `decision.md` for full numbers and scope.
