# C74 -- full product lowest sector: groundwork rigorous, channel-transport step explicitly heuristic

**Experiment id:** `20260811-c74-full-product-lowest-sector`
**Date:** 2026-08-11 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C73/C73b (round59's real twisted `D_S6`, kernel=1 in the
SU(3)-invariant sector, robust across the full admissible torsion family,
chirality purely left-handed); C70-C72 (round59<->G102 triality-channel
bridge, verified intertwiners `U_v`, `U_s`, `U_c`); KT-8/C3 (full 9D product
kernel is NULL, `dim ker D_{S3xS6}=0`); C64 (`dim ker D_S3=0` at
Levi-Civita); C52 (t=0/1 torsion-crossing multiplicity trick shown to never
give a clean factor of 3)

---

## Why this round is scoped the way it is

`predictions_before_data.md`'s P5 (ledger-C74) asks for "the full product
lowest-sector computation -- properly framed as `ker D_S6 (x) (lowest S3 KK
level)`, NOT `ker D_full`... yields three physically distinguishable
sectors without using `t=0/1` as a multiplicity factor" plus "unified
Clifford convention asserted in-script both sides before tensoring (OB10
lesson)." An Explore-agent scoping pass (before any code was written) found:

- The S3 lowest KK level (n=0, Levi-Civita) is already established in
  round67's own closed-form spectrum -- reusable by citation.
- OB10's documented Clifford-convention trap (S3's `Cl(0,3)` vs an EARLIER
  S6 construction's opposite-sign `Cl(6,0)`) does NOT automatically apply to
  round59's specific S6 construction -- this exact pairing (round59 x
  round67) has never been checked in this codebase and must be verified,
  not assumed.
- `predictions_before_data.md`'s own correction note already warns that
  naively using `U_v`/`U_s`/`U_c` to build "three copies" is precisely what
  C71's tautological monodromy attempted and failed at -- this round must
  use each intertwiner independently (once), not chain them.
- "Three PHYSICALLY distinguishable sectors" is a harder question than this
  round alone can answer -- the round table's own division of labor assigns
  the adversarial distinguishability test to C75, not C74.

## The claim under test

> **C74 (working).** The groundwork for the full product's lowest sector is
> rigorous: no Clifford-sign mismatch between round59's S6 construction and
> round67's S3 construction; the S3 n=0 level is confirmed (eigenvalues
> `+-3/2`, multiplicity 2 each); round59's S6 kernel vector is explicitly
> constructed. Transporting this kernel content into each of the three
> triality channels (via C70/C71's own independently-verified intertwiners,
> each used once) gives a nonzero result in all three channels. **This last
> step relies on a heuristic (not rigorously derived) choice of how to
> extract a transportable vector from a genuinely entangled SU(3)-invariant
> kernel state -- flagged explicitly, not smoothed into a stronger claim
> than it supports.**

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1 (Clifford sign check)** | round59's `E_k` and round67's `Z_i` share the same anticommutator sign (`X^2=-I`) | pending |
| **P2 (S3 level)** | `n=0` level reproduces `+-3/2`, multiplicity 2 each, matching round67's own closed form | pending |
| **P3 (kernel construction)** | round59's kernel vector is explicit, normalized, and genuinely in `ker(D+)` (residual near machine precision) | pending |
| **P4 (channel transport)** | transporting the kernel content through `U_v`, `U_s`, `U_c` (each independently) gives a nonzero result in all three channels | pending -- explicitly NOT claimed as evidence of physical distinguishability regardless of outcome |

## kill_criterion

P1 fails if the signs disagree (would mean this specific pairing hits the
SAME trap OB10 already documented for a different S6 construction). P2/P3
fail if they disagree with already-established results (round67, C73). P4's
outcome (nonzero or zero) is recorded either way, but explicitly does NOT by
itself establish or refute "three distinguishable generations" -- that
determination requires the physical-observable test deferred to C75.

## What this cannot show

- Does **not** establish that the three constructed channel-transported
  vectors are PHYSICALLY distinguishable (not merely three labeled vector
  spaces, formally distinct by construction but potentially physically
  redundant) -- explicitly deferred to C75.
- Does **not** rigorously justify the "marginal projection" used to extract
  a transportable vector from the entangled kernel state -- flagged as
  heuristic, not derived from first principles.
- Does **not** re-test KT-8's already-NULL full-kernel result, nor use the
  already-refuted `t=0/1` multiplicity mechanism.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
