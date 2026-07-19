# Verification Protocol — Round59 External Verification Packet

## Why this packet exists

This project's own internal certification of the claim below (round59,
2026-07-14) reached `[VERIFIED-INDEPENDENT-INTERNAL]` status using three
independently-authored computational routes plus a literature-anchored
analytic derivation — but all three routes were authored within the same
project, by the same author/AI system, in the same session. The project's
own record explicitly names "external human review" as the one remaining
rung above this status, on its own **Verification Strength Ladder**:

| Rung | Independence |
|---|---|
| Same model, new prompt | Weak |
| Same model, isolated context | Weak-Medium |
| Different model | Medium |
| Independently-written code | Strong |
| Symbolic solver / Lean / Coq | Strong (formal claims) |
| **Blind replication by another group** | **Very strong** ← this packet |
| New physical/empirical experiment | Strongest (empirical claims) |

Completing this packet moves the claim to the "blind replication by
another group" rung, regardless of whether your result agrees or
disagrees with this project's own.

## File reading order (strict)

1. `problem_statement.md` — what you are being asked to compute.
2. `bundle_definition.md` — the geometric/representation-theoretic setup.
3. `conventions.md` — which conventions are pinned vs. free.
4. `critical_blocks.md` — known methodological pitfalls to watch for.
5. `environment_manifest.md` — record your own environment now (before
   computing), and note the sealed file's hash for later verification.
6. **Do your own independent computation now.** Do not proceed to step 7
   until you have a written, timestamped record of your own result:
   domain and target dimensions, the explicit matrix (or its rank at
   minimum), and your assessment of convention-robustness.
7. Only after step 6: verify `expected_output_sealed.md`'s SHA-256 hash
   against `environment_manifest.md`'s recorded value, THEN open it,
   compare, and write up the comparison per "Reporting" below.

## Hard rules

- **Do not read `expected_output_sealed.md` before completing your own
  computation.** This is the single most important rule in this packet —
  violating it converts your result from "blind replication" (Very
  strong) back to "same known answer, re-derived" (Weak), defeating the
  purpose entirely.
- **Do not consult this project's own code, scripts, or `decision.md`
  files for round59** (or any experiment referencing it) before or during
  your own computation. Reading the primary source
  (`Agricola_Hofmann_Lawn_2023_invariant_spinors.pdf`) directly is
  required and encouraged; reading this project's transcription of it is
  not, and defeats the independence this packet is designed to provide.
- **Record your calibration gate result** (whether you reproduced
  Theorem 5.1's Killing equation exactly) before proceeding to the novel
  computation — if calibration fails, stop and report that, rather than
  adjusting conventions until it passes (adjusting until it passes is a
  legitimate part of transcription debugging, but the FINAL passing
  configuration and the path to it should both be reported).

## What to submit (regardless of agreement or disagreement)

1. Your calibration result (pass/fail, and if fail, what you adjusted and
   why).
2. Domain and target invariant-subspace dimensions you found.
3. The explicit matrix of `D⁺` in your chosen orthonormal bases.
4. The rank you computed.
5. Your convention-sweep findings (which variants you tried, whether the
   verdict was stable).
6. Your own derivation/reasoning, in enough detail that a third party
   could follow it independently of both this project's account and your
   specific code (if any).
7. Explicit comparison against `expected_output_sealed.md`, written AFTER
   you have recorded items 1-6, not interleaved with your derivation.

## If your result disagrees

This is a legitimate, valuable, and fully anticipated possible outcome —
`critical_blocks.md` documents that this project's own history includes a
prior near-miss (an incomplete invariant search) that was only caught by
a completeness audit. A disagreement here would be exactly the kind of
finding an external-verification rung exists to catch. Report:
- The exact point where your derivation diverges from
  `expected_output_sealed.md`'s account.
- Whether you can identify which side (yours or this project's) contains
  the more likely error, with reasoning — or state explicitly that you
  cannot determine this without further discussion.
- Do **not** silently adjust your computation to match the sealed
  expectation once you have seen it — if you go back and change something
  after opening the sealed file, that change is no longer part of your
  "blind" result and should be reported as a separate, labeled follow-up,
  not merged into your original submission.

## Scope reminder

This packet concerns ONLY the `S⁶`-only trivial-sector rank computation
described in `problem_statement.md`. It does not ask you to evaluate this
project's separate triality-distinguishability line
(`paper/P1_FROZEN_VERDICTS_TABLE.md`), its `N_gen=3` headline claim as a
whole, its free coupling parameter `λ`, or any runtime/safety claim.
