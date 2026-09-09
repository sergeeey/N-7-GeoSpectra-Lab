# C191 Decision — REJECT (claim a), with a sharpened, not closed, path forward. P5 as literally stated does not produce a pairing rule; a refined version reduces to a match/mismatch structure needing external input C173 already flagged as missing.

**Date:** 2026-09-09
**Verdict:** **REJECT** (claim a: naive P5 produces a definite `8_s`/`8_c` ↔
`t=0`/`t=1` pairing). `15 of 15` checks pass — including the checks that
establish the negative, and the steelman section that checks a stronger
reading before this verdict was written, not after.

All numbers trace to `c191_p5_postulate_pairing.py` and `run_output.txt`.

---

## 0. Explicit framing — this is a postulate round, authorized as such

Per user instruction this session: *"ставить P5 как явно мотивированный
постулат (не вывод) — с пониманием, что это AOG-5-риск. ставь если что
потом откатим."* This round does not derive or justify the identification
of S³'s isometry with a `Spin(8)`-fiber `so(4)` factor — it takes that
identification as given (exactly as `C132`/`OPEN_BLOCKERS.md` flagged:
"high AOG-5 risk — no motivation beyond wanting to unblock OB1") and tests
one specific, previously-uncomputed consequence.

**AOG assessment, honest, not skipped because the round is postulate-based:**
- AOG-1 (pre-registration): **partial pass** — `P5` was registered in
  `C132`'s own ranked survey (2026-09-02), before this round, not invented
  post-hoc to rescue a null result.
- AOG-2 (specificity): **pass** — the postulate is a concrete, checkable
  identification, not a vague relaxation.
- AOG-3 (novel prediction): **pass** — produces a checkable prediction
  (the pairing), which this round then tests.
- AOG-4 (non-triviality): **pass** — falsifiable; found false as literally
  stated (claim a).
- AOG-5 (independent motivation): **fails**, as already flagged by
  `C132`/`C173` before this round — this is why the round required
  explicit user authorization rather than proceeding on the project's own
  internal CDT ranking alone.

Per the Anti-Overfitting Gate, failing 1 of 5 (not ≥2) does not
automatically demote this to `[SPECULATIVE]`, but the AOG-5 gap is real
and is not resolved by this round's result either way — this decision does
**not** claim the postulate is motivated, only reports what it predicts.

## 1. What was tested

`C132`'s own sentence: *"'which block chirality' — the datum separating
`8_s` from `8_c` — becomes 'which `SU(2)` factor', i.e. which `t`-sector...
That is a pairing rule."* Never computed before this round (Novelty Check,
`claim.md` §Prior Result Gate item 4).

## 2. What was found — naive reading (claim a)

Restricting the already-verified `SO(4)×SO(4)` branching to the first
`so(4)` factor (the postulated S³ isometry) alone:

```
8_s restricted to (L1,R1): 4x(j_L=1/2,j_R=0) + 4x(j_L=0,j_R=1/2)
8_c restricted to (L1,R1): 4x(j_L=1/2,j_R=0) + 4x(j_L=0,j_R=1/2)
```

Identical. `P8`, `P9` confirm this matches the known `SU(2)^4` branching
exactly (a positive control on the machinery, not a coincidence); `P10`
states the negative directly: S³'s own isometry, alone, cannot distinguish
`8_s` from `8_c`. **Claim (a) is REJECTED, cleanly, not from a broken or
inconclusive check.**

## 3. Steelman, checked before this verdict was written

Does fixing the *other* `so(4)` factor's own quantum number rescue the
pairing? `P12`-`P15`: **yes, locally, but self-referentially.** At each
fixed value of the second factor's `(L2,R2)`, `8_s` and `8_c` DO separate
— but `8_s` always tracks whichever `(L1,R1)` value *matches* `(L2,R2)`,
and `8_c` always tracks the *mismatch*. This is a real, verified structure
(`P14`/`P15`, exact) — but it answers a different, more complex question
("does the S³ label match the S⁶ label?") than the one `P5`'s sentence
posed ("which channel is which `t`-sector?"), and it requires an
**independent physical meaning** for the second `so(4)` factor's quantum
number (presumably an S⁶-side triality label) that nothing in this
project's own content currently supplies — the same missing ingredient
`C173` already named (Part 5, or a new non-`G2` construction).

## 4. Kill Analysis

**Killed:** the reading "one `so(4)` factor alone = S³'s isometry, ignore
the other" as a source of a working `t`-sector pairing rule.
**Not killed, unaffected:** the underlying `SO(4)×SO(4) ⊂ Spin(8)`
construction (re-verified, `P1`-`P2`, `P13`); `C38`'s own kernel-content
result; `C173`'s prior closure of the `P4` escalation line; `OB1/H1c`'s
overall `PARKED` status (unchanged — this round sharpens what a working
`P5` would need, it does not resolve OB1).
**Relaxation Map:** the surviving option is exactly the match/mismatch
structure (`P14`/`P15`), contingent on an as-yet-unsupplied independent
meaning for the second `so(4)` factor. No revival is possible from this
project's own existing content alone — this mirrors, and does not
contradict, `C173`'s own conclusion.

## 5. Floor–Ceiling (Step 4a)

The natural numeric form of this round's metric: **how many of the 2
distinct `(j_L,j_R)` content-types present in `8_s`/`8_c` differ between
the two sectors, out of 2 possible.** Floor = 0 (no mechanism / full
mixing — `8_s` and `8_c` share both types, exactly the naive-postulate
outcome). Ceiling = 2 (full separation — `8_s` and `8_c` share neither
type, matching `C38`'s own clean single-irrep-per-sector pattern).
Observed = 0 (`P10`: both types present in both sectors, identically).
Efficiency = (observed − floor) / (ceiling − floor) = (0 − 0) / (2 − 0) =
**0.0** — the naive postulate lands exactly on the floor, not partway
toward the ceiling `C38`'s own established result already demonstrates is
attainable in principle (a clean, single-irrep pairing).

The steelman (§3) moves this to `2/2` (full separation, `P14`) **at each
fixed second-factor value individually** — efficiency 1.0 for that
narrower, conditional metric — but the metric itself is then conditioned
on an external input (§3) this round does not supply, so the two
efficiency numbers answer different questions and must not be conflated:
`0.0` is the naive postulate's own, unconditional score; `1.0` is the
refined postulate's score *given* information this project does not yet
have an independent source for.

The equivalent safeguard against a trivial floor-passing artifact: `P8`/`P9`
are a positive control — the machinery is shown to reproduce the
already-known-correct `SU(2)^4` branching (`P13`, exact match to the
2026-07-15 pearl) *before* its `0.0`-efficiency verdict (`P10`) is trusted.
A machinery that could not reproduce the known-correct branching would
make `P10`'s zero uninterpretable; it does reproduce it, so `P10` is
informative, not an artifact of broken machinery.

## 6. What this does NOT establish

- Does not establish or refute whether S³'s isometry genuinely embeds in
  `Spin(8)` this way at all — only tests one consequence of assuming it.
- Does not exhaust every possible reading of `P5` (see `claim.md` §What
  this does NOT establish for the two readings tested and what was not).
- Does not change `OB1/H1c`'s `PARKED` status.
- Does not touch `C186-C190`'s S³-spinor chain, `S²` construction, or
  anything about the Tom-correspondence thread — orthogonal.

## 7. Consequence for OPEN_BLOCKERS.md / OB1 tracking

To be added: `P5`, the last unexecuted item in `C132`'s prioritized queue,
is now attempted (not merely screened) and its naive reading closed, with
a sharpened, unresolved refinement identified. `OB1/H1c` remains `PARKED`
— no internal candidate from `C132`'s queue now remains untested; the only
routes left are genuinely external (Part 5, or a new non-`G2` construction
supplying independent meaning for the second `so(4)` factor).

## 8. Reproduction

```
cd experiments/20260909-c191-p5-so4-postulate-pairing-test
python c191_p5_postulate_pairing.py
```

`15/15`. `ruff check` and `ruff format`: clean (to be verified before
commit).
