# C78 -- exhaustive so(8) commutant of round59's physical D (genuinely new construction)

**Experiment id:** `20260811-c78-exhaustive-so8-commutant-of-physical-D`
**Date:** 2026-08-11 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C75 (Gate 2, round124's su(3)+u(1)+u(1) candidate: NO);
C77 (Gate 2, round119's SO(4)+SO(4) candidate: NO, all 12/12); C70
(verified intertwiner `U_v`); `L3B_SPIN8_INTERFACE_SPEC.md` §1.5 (the
2026-07-15 F4/octonion-triality investigation, read in full before
designing this round -- its own "Dynamics" open item, point 2 of its
"what remains completely open" list, is exactly what this round closes)

---

## Why this is a genuinely new construction, not another candidate test

C75 and C77 each tested ONE hand-picked candidate symmetry (round124's
10-dim `su(3)+u(1)+u(1)`, round119's 12-dim `SO(4)+SO(4)`) against the
physical `D`. Both failed. But "two candidates failed" is not the same as
"no candidate can succeed" -- the guess-and-check methodology can never
produce that stronger, exhaustive statement no matter how many candidates
are tried.

**This round changes the method, not just the candidate.** Instead of
proposing a specific subalgebra and testing it, this round computes
**the full commutant of `D` within all of `so(8)`** directly: transport
G102's complete 28-generator `so8_basis()` (the standard antisymmetric
basis, not restricted to any subalgebra) to `Sigma` via C70's verified
`U_v`, then solve for the linear subspace of `so(8)` coefficients whose
transported generator commutes with `D` -- via a single SVD null-space
computation, not per-generator guessing.

This is the natural generalization the L3B document's own investigation
(read in full before starting) never had the tools to run: it required
BOTH a real physical `D` (only available since C73, this session) AND a
verified bridge into its representation space (C70, this session)
simultaneously -- a combination that did not exist before 2026-08-11.

**What this closes, if the result is `dim=8` (`=su(3)` exactly):** not
"this candidate fails" but **"no subalgebra of `so(8)`, of any dimension
or structure, commutes with the physical `D` except `su(3)` itself"** --
directly and completely closing `L3B_SPIN8_INTERFACE_SPEC.md` §1.5's own
"Dynamics" open item ("No argument shows the actual physical Dirac
operator, once `G2` is broken this way, remains consistent... this needs
independent verification, not assumption"). This would be an exhaustive
theorem-level statement, not one more data point alongside C75/C77.

**What this does NOT close, whatever the result:** the L3B document's own
final, sharper kill criterion -- a genuinely entangling structure "can
only come from a construction that is non-product AND `G2`-symmetry-
breaking... mixing the `S3` frame index with the `S6` triality index at
the level of the Dirac operator itself" -- requires leaving the
product-manifold framework entirely (a structurally different `D`, not
just a different symmetry group acting on the current one). This round
stays entirely within the current product-structure `D`; it cannot speak
to that door either way.

## The claim under test

> **C78 (working).** The commutant of round59's real physical `D` within
> `so(8)` (transported to `Sigma` via `U_v`) is computed exhaustively via
> null-space SVD, not guessed. Prediction, based on C75's and C77's
> results (every tested generator beyond `su(3)` failed, with no partial
> successes): the commutant equals `su(3)` exactly, dimension 8 -- no
> larger symmetry exists. If the result differs from this prediction, that
> is itself the more important finding and must not be downgraded to fit
> the expected narrative.

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1 (basis sanity)** | `so8_basis()` returns exactly 28 generators, and the known 8 `su(3)` generators (already verified elsewhere) lie exactly inside their span | pending |
| **P2 (bridge sanity)** | `U_v` reproduces its own already-verified intertwining property (residual near machine precision), reused not re-solved | pending |
| **P3 (positive control)** | `su(3)`'s own 8 generators lie inside the computed commutant null space -- i.e. the null-space computation, applied to the KNOWN-good su(3) subspace, correctly reports zero commutator (sanity-checks the method before trusting a negative result elsewhere) | pending |
| **P4 (exhaustive commutant)** | `dim(commutant) = 8`, exactly matching `su(3)` -- no element of `so(8)` outside `su(3)` commutes with `D` | pending |

## kill_criterion

P1/P2 fail if they disagree with already-established results (G102's own
28-generator basis, C70's `U_v`) -- would indicate a bug in this round's
reuse of prior machinery. P3 fails if the null-space computation does not
correctly recover `su(3)` as commuting -- would mean the method itself is
broken and P4's result cannot be trusted regardless of its value. **P4's
outcome is recorded exactly as found, in either direction**: `dim=8`
closes the question exhaustively as described above; `dim>8` is a
genuine, unexpected discovery requiring immediate, careful follow-up
(identify the extra generators explicitly, check their Lie-bracket
closure, compare against known physically-relevant algebras) rather than
being treated as a nuisance result to explain away.

## What this cannot show

- Does **not** address the L3B document's own final, sharper kill
  criterion (a non-product, `G2`-breaking `D`) -- explicitly out of reach
  within the current product-manifold construction, stated above.
- Does **not** resolve the channel-redundancy/permutation question by
  itself, even if `dim=8` -- an exhaustive "no extra symmetry" result
  closes one entire class of candidate mechanisms but does not by itself
  rule out a channel-permuting operator built by some other means (e.g.
  a genuinely non-tautological construction not expressible as an so(8)
  Lie-algebra element at all).
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** independently re-verify `L3B_SPIN8_INTERFACE_SPEC.md`'s own
  Hopf/Liouville "`G2`-invariant class closure" argument -- cited, not
  re-run; this round is a different, complementary computation (algebraic
  commutant of `D`, not a PDE argument about flux sourcing).
