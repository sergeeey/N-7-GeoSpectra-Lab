# C178 — Claim

**Experiment ID:** `20260906-c178-ob11-degenerate-perturbation-theory-full-kernel`
**Parent:** OB11 (matter-generation tensor factorization / the "non-product
D" door C78/C79/C174 have been probing). Direct follow-up to C174, whose
own Relaxation Map named the correctly-scoped next step and explicitly
did NOT attempt it: **proper (not naive) degenerate perturbation theory
within the FULL 36-dim raw kernel of round59's `D`** (⊗ the 2-dim S³
factor, a 72-dim degenerate subspace), rather than tracking a single
ad hoc eigenvector's overlap through an `eps`-sweep (C174's own two
attempts, both self-diagnosed as artifact-dominated / not trustworthy).
Built per user's direction ("другое направление по OPEN_BLOCKERS" +
this project's own established next-step scoping).

## Step -5: Zero-Signal Gate

- **Entity:** the 72-dimensional degenerate eigenspace `V_0 = C²⊗ker(D)`
  of `D_joint_base` (`D`=round59's twisted `D_S6` operator on `Σ⊗Σ`,
  `ker(D)` established as 36-dimensional in C79/C172 — re-verified
  numerically here, not assumed), and the projected coupling operator
  `T_0 = P_{V0}† T P_{V0}` for each of the three triality channels
  (`v`,`s`,`c`), where `T` is C79/C174's own non-product coupling
  (`S³` Clifford generators `Z_i` tensored with a channel-bridged
  `so(4)_1` self-dual triple, reused via `importlib`, not rebuilt).
- **Falsifiable predicate:** is the eigenvalue SPECTRUM of `T_0` (the
  standard degenerate-perturbation-theory zeroth-order Hamiltonian, whose
  eigenvalues ARE the first-order-in-`eps` energy corrections) IDENTICAL
  across channels `v`,`s`,`c` — extending C173's own G44/G102 finding
  ("the three channels are identical `su(3)`-modules, not just
  isomorphic") to this non-invariant-generator, non-product construction
  — or does it genuinely differ?
- **Measurable outcome:** (a) verify the numeric `D_S6` build
  (`C73.build_numeric_dirac`, used for `D_joint_base` in C79/C174) agrees
  with round59's own symbolic `D` (`mod.build_dirac`) to numerical
  precision — a substrate check this project's own discipline requires
  BEFORE trusting anything built on top of either; (b) compute `ker(D)`
  via SVD, report its actual dimension (not assume 36); (c) build the
  72-dim degenerate subspace basis; (d) for each channel, project `T`,
  diagonalize the resulting 72×72 Hermitian `T_0`, get its sorted
  eigenvalue spectrum; (e) compare spectra pairwise across channels; (f)
  cross-check degenerate PT's own validity directly: at small `eps`, do
  the actual eigenvalues of the FULL 128×128 `D_joint(eps)` near
  `d_s3_scalar` shift linearly with slope matching `T_0`'s eigenvalues?
  (g) identify which corrected zeroth-order eigenvector has the largest
  overlap with round59's own specific physical direction (`v_round59`),
  connecting back to C174's original question.

## Step -2/-1 (EstimandOps L0)

**Question type: Descriptive.** Does a specific, exactly-constructed
72×72 Hermitian operator (built from already-established project objects)
have an eigenvalue spectrum that depends on a specific discrete choice
(which channel bridge) — not causal, no estimand canvas beyond the
falsifiable predicate above.

## Honest scope limitation, stated BEFORE computing

1. This is a NUMERIC (not symbolic) computation — `D`, `ker(D)`, and `T`
   are all built and diagonalized as complex `numpy` matrices, not exact
   `sympy` objects. Precision is finite; all comparisons use an explicit
   numerical tolerance, stated before any result is seen (see
   kill-criterion table).
2. This tests ONE specific non-product coupling `T` (C79/C174's own
   construction) — not every conceivable non-product coupling. A
   `CHANNEL-INDEPENDENT` verdict here would not prove no non-product
   construction could ever distinguish channels, only that this one,
   properly analyzed, does not.
3. Degenerate perturbation theory itself is standard, well-established
   linear algebra (not a novel method) — the novelty here is applying it
   correctly to a construction C174 already showed breaks naive analysis
   methods, not inventing new mathematics.

## Kill-criterion table (frozen before running the script)

| Verdict | Condition |
|---|---|
| `SUBSTRATE-MISMATCH` | The numeric `D_S6` build does not match round59's own symbolic `D` to acceptable tolerance (`>1e-6`), OR the numerically-found `dim(ker(D))` differs from the established `36` — signals the downstream construction rests on an unverified/incorrect substrate; STOP, do not report a channel-(in)dependence verdict until reconciled. |
| `PT-INVALID` | The small-`eps` numerical eigenvalue shifts of the FULL `D_joint(eps)` do NOT match `T_0`'s own eigenvalues (to leading order in `eps`) — signals a bug in the projection/diagonalization method itself, not a physics finding; must be fixed before trusting the channel comparison. |
| `CHANNEL-INDEPENDENT-SPECTRUM-CONFIRMED` | Sorted `T_0` eigenvalue spectra agree across `v`,`s`,`c` to within `1e-6` (pairwise max abs difference) — extends C173's own G44/G102 finding to this construction. |
| `CHANNEL-DEPENDENT-GENUINE-DISCOVERY` | Spectra genuinely differ beyond `1e-6` — a real, surprising discovery contradicting the established G44 pattern; would require independent skeptic scrutiny before trusting, per this project's own repeated "forced not discovered" caution (C144/C153/C154/C156/C158/C168 — six prior instances this session alone of an apparent finding later shown to be forced/artifactual). |

**Pre-registered expectation (written BEFORE running the script):** given
C173's own established result (all three triality channels are IDENTICAL
`su(3)`-modules under G44/G102, not merely isomorphic) and given that the
channel bridge `U_channel` is specifically constructed to intertwine each
channel's own generators to a COMMON reference basis (`gens_r59`) — i.e.
built FOR the purpose of making cross-channel comparison meaningful in a
common frame — the a priori expectation is
`CHANNEL-INDEPENDENT-SPECTRUM-CONFIRMED`, the "boring" outcome extending
this project's dominant pattern. This is written down now specifically so
a later "it worked" (in either direction) cannot be suspected of being
reverse-engineered from the answer.

## AI-Hypothesis Pre-Gates (Steps -4/-3)

- **Source Trace:** `D`, `T`, and the channel bridges are all this
  project's own already-`[VERIFIED-tool]` objects (round59, C68/C70/C71,
  C79), reused via `importlib`, not re-derived. No new external literature
  dependency this round.
- **Novelty Check:** `grep`-confirmed no prior round has projected `T`
  onto the FULL 36-dim (72-dim with the S³ factor) degenerate subspace —
  C79 swept the raw 128-dim space (found the 36-dim degeneracy as an
  ARTIFACT, did not properly handle it); C174 tried a 2-dim compression
  (vacuous) and single-eigenvector overlap-tracking (collapsed under
  perturbation) — neither is proper degenerate PT. This round is
  genuinely the next, previously-unattempted step both prior rounds
  explicitly named and declined to build.

## What this does NOT mean (pre-registered)

1. Does NOT, under `CHANNEL-INDEPENDENT-SPECTRUM-CONFIRMED`, prove NO
   non-product construction could ever distinguish channels — only that
   this one, properly analyzed via degenerate PT, does not.
2. Does NOT, under `CHANNEL-DEPENDENT-GENUINE-DISCOVERY`, immediately
   establish a new generation-counting mechanism — a genuine spectral
   difference would need substantial further work (physical
   interpretation, stability under basis/gauge choices, independent
   skeptic pass) before being promoted to anything stronger than "worth
   investigating further."
3. Does NOT change `N_gen=3`'s CONDITIONAL status under any outcome.
4. Does NOT resolve OB11's STRONG reading (already separately BLOCKED by
   G97) — this concerns only the WEAK reading, the live candidate.
