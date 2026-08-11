# C75 -- Gate 2 of TRIALITY_DISTINGUISHABILITY_GATE.md tested directly on round59's real physical D

**Experiment id:** `20260811-c75-gate2-physical-d-vs-extended-symmetry`
**Date:** 2026-08-11 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** `TRIALITY_DISTINGUISHABILITY_GATE.md` (round119, Gate 1 done two
independent ways, Gate 2 "Undetermined... the source's own tooling says it
cannot be checked this way at all"); round124 (su(3)-centralizer construction,
`G102.centralizer_dim`); C70 (round59<->G102 bridge, verified intertwiner
`U_v`); C73/C73b (round59's real `D_S6`, extensively characterized this
session); G74A Lemma B (abstract prediction that breaking G2 "does not
degrade gradually with perturbation size; it simply no longer applies, at any
nonzero perturbation")

---

## Why this round is scoped the way it is (read before trusting the result)

`predictions_before_data.md`'s own C75 concretization ("The C75 adversarial
round, made concrete") asks for a **different, harder** test than this round
runs: "compute the commutant of the full physical operator algebra {gauge
generators, D, gamma, J, B-L} on the three-channel space. If the channel
PERMUTATIONS lie inside that commutant... the redundancy reading is LIVE."
That test needs a genuine channel-PERMUTING operator (something that maps
`channel_v -> channel_s -> channel_c`). **No such operator exists in this
codebase and none is constructed here** -- C71 already showed the natural
construction (composing `U_v`, `U_s`, `U_c` around a cycle) is a pure
matrix-algebra tautology (`I=I` for any three invertible matrices built this
way), reconfirmed fully general in C72. This round does **not** repeat that
mistake.

What this round tests instead: `TRIALITY_DISTINGUISHABILITY_GATE.md`'s own
**Gate 2** ("does the physical Dirac operator commute with the extended,
channel-DISTINGUISHING symmetry Gate 1 already constructed") -- a genuinely
open, previously-untestable question, now testable for the first time because
this project finally has both pieces: a real physical `D` (round59, via
C73/C73b) and a verified bridge into its representation space (C70's `U_v`).
This closes Gate 2 for the specific `su(3)+u(1)+u(1)` candidate (round124),
**not** the full redundancy/permutation question `predictions_before_data.md`
asked C75 to attack. That question remains open -- see "What this does NOT
show" below and the correction note added to `predictions_before_data.md`.

## The claim under test

> **C75 (working).** round124's `su(3)+u(1)+u(1)` extended symmetry (the
> centralizer construction that gives Gate 1 of `TRIALITY_DISTINGUISHABILITY_
> GATE.md` its algebraic channel-distinguishing power) does NOT commute with
> round59's real physical Dirac operator `D`, transported to `Sigma` via
> C70's own verified intertwiner `U_v`. The violation is large and
> unambiguous (O(1) relative to `|D|`), not a numerical-noise-level effect,
> and a positive control (genuine su(3) generators, which ARE known to
> commute with `D`) confirms the commutator machinery itself is sound.

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1 (centralizer sanity)** | round124's 2 extra generators are abelian and centralize su(3) on `channel_v`, matching round124's own already-established result | pending |
| **P2 (bridge sanity)** | C70's `U_v` reproduces its own already-verified intertwining property (residual near machine precision) | pending |
| **P3 (positive control)** | `[D, Leibniz(M_k)]=0` for all 8 genuine su(3) generators (D's su(3)-equivariance is already established elsewhere; this just confirms the commutator test machinery itself works) | pending |
| **P4 (Gate 2 test)** | `[D, Leibniz(u1_a)]` and `[D, Leibniz(u1_b)]` are nonzero -- per G74A's Lemma B ("does not degrade gradually... simply no longer applies") this is expected to be a clean, large violation, not a small one | pending |

## kill_criterion

P1/P2/P3 fail if they disagree with already-established results (round124,
C70, D's own su(3)-equivariance) -- would indicate a bug in this round's
reuse of prior machinery, not a new physics finding. P4's outcome is recorded
either way: if the commutator turned out to vanish (or be small/comparable to
P3's positive-control noise floor), that would be a genuine surprise
contradicting G74A's Lemma B and would need immediate re-examination before
trusting it; a large, clean nonzero result confirms the Lemma B prediction
computationally for the first time.

## What this cannot show

- Does **not** attack `predictions_before_data.md`'s own C75 concretization
  (the channel-permutation/redundancy commutant test) -- that needs a
  genuine channel-permuting operator, which does not exist in this codebase
  and is not constructed here.
- Does **not** resolve whether the three triality channels are physically
  redundant (gauge copies of one degree of freedom) or genuinely distinct --
  orthogonal to what this round tests, not answered either way.
- Does **not** test `u1_b`'s or `u1_a`'s individual physical meaning beyond
  "part of round124's centralizer construction" -- no claim is made about
  what breaks the commutation, only that it breaks.
- Does **not** change `N_gen=3`'s CONDITIONAL status (C75 carries no
  pre-commitment in `predictions_before_data.md`'s P1-P5 table -- it is a
  separate adversarial round, not one of the five pre-committed predictions).
