# TOM-CERT-01 Decision -- W = span{g_ab} in L^2(S^3) carries the exact (1/2, 1/2) structure of SU(2)_L x SU(2)_R

**Date:** 2026-11-03 (decision record written 2026-11-23, from the existing folder; no computation was re-run for the decision; the run logs were read and the SHA256 manifest verified)

## Result

On S^3 = SU(2), with x = (x0, x1) and g(x) = [[x0, -conj x1], [x1, conj x0]], the four matrix-element functions g_ab span a 4-dimensional space W of degree-1 functions. Exact Gaussian-rational arithmetic (verifier.py, stdlib fractions) establishes:

- W is invariant under SU(2)_L (f -> f(h^-1 x)) and SU(2)_R (f -> f(x k)).
- W splits into two left doublets (fixed column b of g) and two right doublets (fixed row a of g). The two left doublets are isomorphic, as are the two right doublets (their generator matrices coincide).
- The commutant of the full L x R action on W has dimension 1, so W is irreducible of type (1/2, 1/2). Commutants of L alone and R alone have dimension 4.
- Casimirs J_L^2 = J_R^2 = 3/4 times the identity.
- Joint weights (J_3L, J_3R) are (-1/2, +1/2), (-1/2, -1/2), (+1/2, +1/2), (+1/2, -1/2) on g00, g01, g10, g11: each combination (+-1/2, +-1/2) occurs exactly once.
- The uniform-measure Gram matrix is <g_ab, g_cd> = (1/2) delta, and all six generators are skew-Hermitian with respect to it (unitary action).
- Conjugate equivalence: eps T_a eps^-1 = conj(T_a) with eps = [[0,1],[-1,0]]; the left block is conj(T_a), the right block is T_a.

## Evidence

| item | value | source |
|---|---|---|
| verifier run on the valid certificate | ACCEPT, 18 checks passed, 0 skipped, exit 0 | `logs/verify_valid.txt` |
| negative controls (35) | all behaved as declared | `logs/negative_controls.txt`, `logs/run_all.txt` |
| fresh rebuild vs stored certificate | identical SHA256 (b35dc928...c2) | `logs/run_all.txt`, step S5 |
| file integrity | 9 files matched SHA256SUMS.txt | checked 2026-11-23 |
| independent check | context-blind skeptic agent, same model family (2026-11-03): mathematics confirmed by its own derivation; its verifier-weakness findings fixed and covered by new controls | `REPORT_RU.md` section 7a |

Old verifier on the 35 controls: 22 failures detected (including a homomorphic-convention mutant N8 that was accepted). New verifier: all controls pass.

## Status

- Mathematics: PROVED by exact arithmetic within the stated conventions (INTERNALLY_CERTIFIED).
- Not independently reviewed by a human. Builder and verifier share the author and the conventions, not the code.
- The folder is not an independent reproduction: the builder and verifier are one author's pair.

## What this decision does NOT establish

- Which SU(2) is spin (R05). W is a statement about SU(2)_L x SU(2)_R on S^3, not about spin.
- That W is the correspondent's multiplet or that any physical fermion exists.
- Any field equation; nothing about D_0 or the Dirac operator.
- Anything for functions of degree > 1 (W is the degree-1 block only).
- That the (1/2, 1/2) structure is new: it is the classical Peter-Weyl decomposition of the defining representation, here written as an exact certificate.

## Consequences for the ledger

- Ledger row added as `TOM_CERT_01_SPAN_GAB_SU2LR_HALFHALF_EXACT` (PROVED, PASS, INTERNALLY_CERTIFIED, ACTIVE, finding ESTABLISHED).
- Existing references: C232 (weight dictionary), C233 (mutation scan), C243 (addendum) cite this result without a ledger row of their own. They remain unchanged.
- Standalone novelty: not claimed. The result is classical and is recorded as a reproducible certificate.

## Relation to an earlier packet (found 2026-11-23)

A packet of 2026-08-09 (experiments/20260809-tom-s3-harmonics-solution-packet, present only on the unmerged branch b2-independent-reimplementation; private copy in `correspondence/branch_recovery_2026-11-23/`, git-ignored) computes the same j = 1/2 Peter-Weyl block (matrix elements of the fundamental SU(2) representation on S^3) in a different coordinate chart. Re-run in a scratch copy on 2026-11-23: the stored results json is reproduced exactly (verdict ALL_CHECKS_PASS). The two records overlap; the weight labelling (which g_ab carries which (J_3L, J_3R)) differs by chart and sign convention and is not reconciled here. TOM-CERT-01 therefore adds an exact rational certificate and negative controls, not a new object.

## Scripts and outputs

| script | output | outcome |
|---|---|---|
| `build_certificate.py` | `certificate.json` (SHA256 b35dc928...) | certificate built |
| `verifier.py` | `logs/verify_valid.txt` | ACCEPT, 18 checks |
| `negative_controls.py` | `logs/negative_controls.txt` | ALL BEHAVED AS DECLARED |
| `run_all.py` | `logs/run_all.txt` | ALL STEPS AS DECLARED, exit 0 |

Ledger: TOM_CERT_01_SPAN_GAB_SU2LR_HALFHALF_EXACT
