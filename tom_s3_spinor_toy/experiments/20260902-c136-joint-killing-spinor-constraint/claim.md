# C136 claim -- does a joint 13D generalized-Killing-spinor constraint,
# decomposed across M4 x S3 x S6, pair an S3 t-sector with an S6 triality
# channel asymmetrically? (C132's top-ranked-tied candidate P14)

## Mode declaration

**Convergent-mode round.** Tests ONE specific, pre-registered claim to
completion -- promote, weaken, or kill it. This is the LAST of C132's
top-tier candidates to be tested (P0 -> C133, confirmed with scope
narrowing; P2 -> C134, killed cleanly; this is P14, tied with P2 at
CDT rank 2, "the better shape" per C132's own assessment).

## Question type (EstimandOps L0)

**Descriptive** -- existence of a solution to a specific decomposed
constraint equation. Explicitly NOT causal, NOT predictive.

## MANDATORY FIRST MOVE, stated before anything else (per C132's own
## screen for this exact candidate -- do not skip this)

**No standard Minkowskian supergravity exists at D=13.** Standard
supergravity theories cap at D=11 (Nahm's theorem: a graviton
supermultiplet with spins <=2 cannot exist above 11 dimensions). This
project's own file `SPIN13_TO_SPIN4_DECOMPOSITION.md` (already quoted
in C134 Section 6, item 1) states this explicitly and adds that the
project does NOT claim a consistent 13D parent theory -- it treats the
4 x S3 x S6 split as independent factors from the start, not a unified
higher-dimensional spacetime. **Therefore any "generalized-Killing-
spinor" or "gravitino-type" constraint posed here is NOT an imported
piece of 13D supergravity** (no such theory exists to import from) --
it must be explicitly constructed as a GEOMETRIC constraint (e.g. by
analogy with generalized/Bismut/torsionful Killing-spinor equations
used in flux compactifications, which are well-defined on any Riemannian
manifold with torsion independent of supersymmetry), with the
non-standard nature of this move stated plainly in the round's own
`decision.md`, not glossed over. If this geometric construction cannot
be made precise without silently importing an assumption equivalent to
a 13D SUSY algebra, this round should say so explicitly and treat that
as a genuine, informative obstruction -- not route around it quietly.

## Background, stated honestly before any computation

Read, in full, before doing anything else:
- `experiments/20260902-c132-13d-parent-action-survey/decision.md`,
  especially the `P14` entry (search "P14") and its "Compressed spec"
  in Section 6 (this claim.md is built from that spec).
- `experiments/20260902-c134-ecsk-torsion-auxiliary/decision.md`
  Section 8 "What this round does NOT kill" -- confirms `P14` is
  untouched by C134's chirality-flip kill mechanism, because "a
  gravitino-type constraint is linear in psi, so route 2 does not
  transfer" -- verify this claim directly rather than assuming it, and
  state explicitly whether your own construction is linear or bilinear
  in the spinor, since that determines whether C134's mechanism could
  apply here too.
- `SPIN13_TO_SPIN4_DECOMPOSITION.md` in full -- the project's own
  authoritative statement on what 13D structure is and is not claimed.
- `experiments/20260717-round86-*/decision.md` (find via Glob,
  AHL2023 coexistence attempt) -- prior art that does NOT transfer,
  cited so you do not repeat it.
- `experiments/20260717-round114-ahl2023-torsion-killing-spinor-crosscheck/decision.md`
  -- **already FALSIFIED**, per `null_results/INDEX.md`. Read this
  file's actual failure mode carefully: the skeptic found that
  `D = Sigma e_i.A(e_i).psi` collapses ALGEBRAICALLY to `-tr(A)`
  regardless of Clifford-representation convention, so a computed
  magnitude there was just AHL2023's own already-stated Killing
  constant summed back out -- NOT independent evidence. **This round
  must not repeat that exact algebraic-collapse trap**: before treating
  any computed quantity as a genuine result, check whether it reduces
  to a trace identity or other tautology independent of the actual
  input data, exactly the species of error this project's own
  `audit-verification-gate.md` and this session's own repeated findings
  (C128/C129/C130/C133/C134's "checks that cannot fail") warn against.
- `experiments/20260717-round98-*/decision.md` (find via Glob,
  Friedrich-Ivanov characteristic-connection uniqueness) --
  `INCONCLUSIVE__SOURCE_ACCESS_INSUFFICIENT`, genuinely open, not
  closed. Check whether the specific source-access gap that blocked
  round98 also blocks this round, or whether this round's narrower
  question sidesteps it.
- C125's decision.md Section 0a/2a and Section 4 (the `Omega_3 * Omega_6
  = i*gamma_5` identity, and C125's own downgrade of it as "forced in
  every irrep of Cl(1,12), not a discovery about the split" -- if your
  construction uses this identity, carry that downgrade forward
  honestly, do not re-present it as a fresh finding).
- Both Agricola PDFs already in the repository root (search for them --
  `Agricola_2002_Dirac_naturally_reductive.pdf` and
  `Agricola_Hofmann_Lawn_2023_invariant_spinors.pdf`) -- these are the
  primary sources for torsion-Killing-spinor equations on S3-type
  spaces; consult them directly for the correct general form of a
  generalized/torsionful Killing spinor equation before constructing
  your own ad hoc version.

## The Zero-Signal Gate check, required before proceeding

Per `falsification-ladder.md` Step -5: `(exists entity) AND (exists
falsifiable predicate) AND (exists measurable outcome)`, all three
required.

- **Entity:** a precisely-stated generalized Killing-spinor constraint
  `(nabla_M + c * H_{MNP} * Gamma^{NP}) epsilon = 0` on `M4 x S3 x S6`
  (or the closest well-defined geometric analogue you can construct and
  justify -- state precisely what `c` and `H` are for THIS background,
  citing the Agricola-family literature for the standard form, not
  inventing coefficients ad hoc), with `epsilon = epsilon_4 (x)
  eta_3 (x) eta_6` the decomposition ansatz.
- **Falsifiable predicate:** the decomposed, coupled system of
  equations (one piece per factor) admits a solution for `eta_3`
  restricted to ONE specific S3 t-sector (t=0 or t=1, not both) paired
  with ONE specific S6 triality channel, asymmetrically -- i.e. NOT
  every channel pairs equally with every sector.
- **Measurable outcome:** the explicit solution set of the decomposed
  system, stated for all three S6 channels crossed with both S3
  sectors (a 3x2 table, filled in explicitly, not asserted).

**If the constraint cannot be posed precisely without either (a)
importing an unjustified 13D SUSY assumption this project does not
have, or (b) reducing to an algebraic tautology in the style of
round114's collapse, this round should return `BLOCKED` or explicit
`[UNKNOWN]` -- NOT force a positive result and NOT silently route
around the obstruction. This is explicitly permitted and is not a
failure of the round.**

## Falsifiable claim

The decomposed generalized-Killing-spinor system, evaluated on this
project's own certified content (the S3 connection family `nabla^t`,
the S6 twist bundle and its established chirality), has a solution set
that pairs a specific S3 `t`-sector with a specific S6 triality channel
asymmetrically -- not uniformly across all three channels, and not
identically for both `t=0` and `t=1`.

## Kill criterion

FALSE if: (a) the constraint cannot be posed without an unjustified
13D-SUSY import (report as BLOCKED, name the specific missing
ingredient); (b) the solution set is uniform across all three S6
channels (no channel-selectivity, hence no pairing information); (c)
the solution set is identical for `t=0` and `t=1` (no sector-
selectivity); (d) any computed "result" reduces to a trace identity or
other construction-independent tautology (round114's exact failure
mode -- actively check for this, do not just assert its absence).

## What this round does NOT show

- Does NOT claim this constraint is derived from an actual 13D
  supergravity theory -- none exists for this project, stated up front.
- Does NOT reopen C123-C135's verdicts.
- Does NOT change `N_gen=3`'s CONDITIONAL status, `lambda=
  FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.
- Does NOT close H1c, OB1, or round95's own diagnosed gap even if it
  succeeds -- it would supply one candidate mechanism, not resolve the
  program.
- Does NOT solicit Tom Lawrence's Part 5.

## Verification plan

- Read all cited files in full before any computation, especially
  round114's exact failure mode and round98's exact blocking gap.
- Consult the Agricola-family primary literature (already in-repo PDFs)
  for the standard form of a torsionful/generalized Killing-spinor
  equation before constructing an ad hoc version.
- Perform the decomposition and the coupled-system solve explicitly,
  shown not asserted, for all six (channel, sector) combinations.
- Actively test whether any computed quantity collapses to a
  representation-independent trace identity (round114's trap) --
  build this check into the verification script itself, not just as a
  narrative caveat.
- Cite `[VERIFIED]`/`[CITED]`/`[INFERRED]`/`[SPECULATIVE]` throughout.
- FL Step 8a skeptic pass (context-blind: only claim.md + decision.md +
  code, no session history). Given this round involves a genuinely
  novel geometric construction (no direct precedent in this project)
  and a documented prior trap (round114) in the exact same problem
  area, run a SECOND independent pass with a differently-worded prompt
  (Paraphrase-Sensitivity Probe) regardless of the first pass's
  verdict, unless the first pass returns a clean, unqualified
  confirmation with zero findings.
