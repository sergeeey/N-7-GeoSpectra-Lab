# C154 — Decision. Verdict: **REJECT (family-wide-law framing) / OPEN (the underlying 2-point coincidence, both spaces)**

**Date:** 2026-09-04. **Tier:** FL Full. **L0:** descriptive.
**Two context-blind skeptic passes, both from source alone, could not
execute code in either session. Both hand-derivations independently
tool-verified by this session before being trusted (per
audit-verification-gate.md: agent's `[DERIVED]` = this session's
`[HYPOTHESIS]` until checked).**

## The arc, in full, kept rather than hidden

| version | claim | verdict | caught by |
|---|---|---|---|
| v1 | `μ:=⟨ψ₊,Dψ₊⟩/⟨ψ₊,ψ₊⟩`, ratio law on `S⁶` | FALSIFIED (`μ=0` at 2nd basis point) | self, via the pre-registered kill criterion |
| v2 | corrected `μ:=‖Dψ₊‖`, ratio law "confirmed, 3 independent points" | reported CONFIRMED, framed as new evidence | skeptic pass 1 (fixed v1's scalarisation) |
| v3 (final) | same numbers, correct framing: forced by already-known facts, not new evidence | **downgraded** | skeptic pass 2 (attacked v2's own "non-tautological" claim) |

Every number printed by both scripts is exact and correct throughout this
whole arc. What changed each time was never the arithmetic — it was
whether the arithmetic constitutes NEW evidence, which turned out, both
times, to be "less than it looked."

## Skeptic pass 1 — Response Matrix (recorded, superseded by pass 2 below)

| concern | verdict | response |
|---|---|---|
| v1's scalarisation discards `ψ₋`, arbitrary | CONFIRMED | Fixed: full-norm `μ` |
| "kernel-dimension mismatch" mechanism is dimension-counting only | CONFIRMED | Withdrawn |
| `claim.md` misquoted `PREREGISTRATION.md`'s Test B contingency | CONFIRMED | Fixed, Test B run |
| v1's CONFIRMED branch was structurally unreachable | CONFIRMED | Accepted |

## Skeptic pass 2 — Response Matrix (the one that stands)

| concern | verdict | independently tool-verified | response |
|---|---|---|---|
| the "structurally matched" full-norm `μ` might itself be forced conformal by `ψ₊⊥ψ₋`, not a real discovery | **CONFIRMED** | `<psi_+,psi_-> = 0` exact; cross-term in `Q_mu` forced to `0` by this alone | **Accepted, headline downgraded** |
| the "3rd point (A+B) is non-tautological" claim in v2 | **CONFIRMED FALSE** | cross-term in `Q_c` ALSO forced to `0`, by `c_B=i*c_A` (C147b, pre-existing); both forms conformal by construction, so A+B agreement is not independent information | **Withdrawn** |
| closed form `mu(a,b)=sqrt(3)*sqrt(a^2+b^2)` should hold EVERYWHERE if the mechanism is real, not just at 3 points | predicted by the skeptic | verified exactly at a random `(a,b)=(3/7,-2/5)` not among the 3 originally tested points; ratio `2/3` reproduced there too | confirms the forcing argument, not a new discovery |
| `SU(3)/T²`'s `dom_sym`/`tgt_sym` (C153) are built from raw `nullspace()` with no Gram-Schmidt — are the numbers even invariants? | partially confirmed, less severe than feared | Gram matrices computed directly: both exactly `2*I₃` (a fortunate accident, not by construction) — numbers ARE proportional to genuine invariants, but on an un-unit-normalised basis (factor of `2` in `‖c‖²` unaccounted) | **New finding, flagged as a correction to C153**, not itself a reason to distrust C153's existing ratio/sign conclusions (those are scale-invariant) |
| the `SU(3)/T²` 3 mismatched ratios (`2√2`, `2√6`, `2√6/3`) might hide a simple `√3`-scaling pattern the round missed | plausible, **not independently verified this session** — noted, not chased further (diminishing returns per Cheapest Differentiating Test discipline) | not run | left as an open observation, not asserted |
| `psi_+` on `SU(3)/T²` (`+3` eigenvalue) is the sign-opposite analogue of `S⁶`'s `psi_+` (`-3` eigenvalue) — untested whether this matters | correct as stated | not independently re-run with the `-3` branch | noted as an open gap, not resolved here |

**No concern dismissed either time.**

## Kill Analysis

**What was killed:** the claim that `|c(∇)|=(2/3)μ(∇)` on `S⁶`'s whole
family is independent, family-wide evidence for anything. It is a 2-line
algebraic consequence of `ψ₊⊥ψ₋` (visible by inspection) and C147b's own
already-registered `c_B=i·c_A` — **zero bits of new information beyond
the single ratio at the Levi-Civita point.**

**What was NOT killed:**
- The single-point coincidence itself: `|c(∇_LC)|/μ(∇_LC)=2/3` on `S⁶`,
  still true, still with no known mechanism.
- The analogous `SU(3)/T²` value, similarly unexplained (and now flagged
  as resting on an unnormalised basis — a real, separate, useful finding).
- `S⁶`'s own closed-form `c`/`μ` formulas — correct and now exact
  everywhere in the family, useful machinery even though the family-wide
  agreement itself is forced.

**Relaxation Map:** none proposed for "the family-wide law" — it was never
a real target; the underlying single-point coincidence is the only thing
left to explain, and remains exactly where C153's novelty check left the
whole `E_W`/connection-coefficient line: real, exact, cross-space, and
without a derivation.

## A pattern worth naming explicitly (third occurrence today)

Three rounds in one day (this project's own "algebraically forced" class,
first named for C144) each found a numeric pattern that read as a genuine
discovery and, on closer inspection by a context-blind skeptic, collapsed
to already-known structure:

1. **C153**: an "exact per-plane multiplicative law" — entailed by Schur's
   lemma plus a 1958 classical theorem, not new (post-hoc novelty check).
2. **C154 v1→v2**: a "3-point-confirmed family-wide ratio" — entailed by
   orthogonality plus an already-registered exact ratio, not new (this
   file, skeptic pass 2).

Both were caught the SAME way: a context-blind reviewer, unable to run any
code, asked "is this forced by something already on record?" and found
yes, in each case, from facts sitting in files this project had already
committed. Flagged as a pearl below — this is no longer an isolated
incident.

## Reproduce

```
python c154_stepA_s6_family_ratio.py     # S^6: closed form, forced by
                                          # already-known facts (see Step A3)
python c154_stepB_su3t2_family_ratio.py  # SU(3)/T^2: genuinely inconclusive
```
