# SEALED — Expected Output

## ⚠️ DO NOT OPEN THIS FILE UNTIL YOU HAVE COMMITTED YOUR OWN RESULT

**If you are the external reviewer performing this verification: stop
reading now if you have not yet finished your own independent computation
and recorded your own answer (in writing, timestamped, before reading past
this line).** Reading this file first defeats the entire purpose of the
packet — this project's own internal certification of the same claim used
three *independently written* routes specifically because re-running
a known answer is the weakest possible form of verification (see
`verification_protocol.md`, "Verification Strength Ladder"). Your value to
this project is exactly the value of a genuinely blind, independent
computation — do not spend it by peeking early.

---

## This project's own internal result (2026-07-14, round59)

**Domain invariant subspace:** dimension 2.
**Target invariant subspace:** dimension 1.

**With orthonormal bases `u₁, u₂` (domain) and `ŵ` (target):**
`D⁺u₁ = a·ŵ`, `D⁺u₂ = b·ŵ`, with (orthonormal-basis normalization)
`a = -1`, `b = -√3`.

**Certificate:** `s := |a|² + |b|² = 1 + 3 = 4 > 0`.

**Rank verdict: `rank(D⁺|₁) = 1`** (since `s > 0` and the target is
1-dimensional, `b ≠ 0` alone already forces rank 1, independent of the
`a`-channel).

**Consequence (combined with separately-certified non-trivial-sector
results, out of scope for this packet):** `dim ker(D⁺_{S⁻}) = 1`,
`dim ker(D⁻_{S⁻}) = 0`, per channel.

## Internal mechanism (why this project believes the answer takes this
form — for your comparison AFTER your own derivation, not before)

This project's own internal finding (not itself part of what you were
asked to verify, but offered as context for comparing derivation
strategies once you have your own): the trivial-block amplitude `b`
coincides with the Killing-spinor Dirac eigenvalue from `AHL2023` Theorem
5.1 (the same one your calibration gate in `conventions.md` required you
to reproduce). The internal account for why this coincidence is a genuine
mechanism, not a coincidence: the "twisting correction" term vanishes by a
representation-theoretic fact about `SU(3)` tensor products having no
common invariant in the relevant piece — if your own derivation found an
equivalent structural reason (by any route), that is a meaningful
independent confirmation of the mechanism, not just the number.

## Convention robustness (internal finding)

This project's internal work found `s > 0` (hence rank 1) is stable across
every calibration-consistent convention variant it tried, and found
exactly one plausible-looking convention flip (a global sign flip of the
Nomizu tensor) that would have zeroed out the result — but that specific
flip fails the calibration gate itself (does not reproduce Theorem 5.1),
so it is excluded on those grounds, not because it gives an inconvenient
answer.

## Verification Strength Ladder position

Before your result: this claim sat at
`[VERIFIED-INDEPENDENT-INTERNAL]` — three internally-authored routes
(one blind to the others' code) plus an analytic anchor, but all
ultimately authored within this project. **Your result is the first entry
at the "external human review" rung** — the one rung this project's own
record explicitly named as still missing.

## How to report disagreement

If your independently-derived rank, dimensions, or stability finding
differs from the above, that is a valuable and reportable outcome in its
own right — do not discard or "fix" a discrepancy to match this file.
Report exactly what you found, with your own derivation, and let the
discrepancy stand as data. See `verification_protocol.md` for how to
submit either an agreement or a disagreement.
