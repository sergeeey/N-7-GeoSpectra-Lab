---
experiment_id: 20260708-dolan-casimir-g2su3
round: 25
date: 2026-07-11
tier: Full-Ladder
status: skeptic_reviewed_C1-C3+C5_confirmed_C4_downgraded_to_inconclusive
parent: round24 (nabla*nabla isolation, C1-C3 confirmed, merged main@ea943ad)
---

# claim.md — Round 25: deriving Round 24's residual K from Nomizu/torsion algebra

## Background

Round 24 found `Delta := D64^2 - nabla*nabla - F_Sminus` on the 2-dim
SU(3)-invariant subspace equals `[[5/2,4/3],[4,5/2]]` — scalar part exactly
5/2 (matching the preprint's nominal Scal/4), with a trace-free residual
`K := [[0,4/3],[4,0]]` of unknown origin. Round 24's C4 (skeptic-weakened,
rewritten) left this genuinely unresolved between (i) a frame/Leibniz
correction term and (ii) an incomplete `F_{S^-}`, naming as the concrete
next differentiating test: derive a candidate for the residual directly
from invariant-frame/Nomizu/torsion algebra, BLIND (not fitted to the
target), then compare.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — algebraic decomposition and hypothesis test.
NOT empirical, NOT causal.

## Construction under test (code: `g2su3_round25_K_derivation.py`)

Round 24's `TERM1_sq := Dslash_mat^2 (x) Id_8` (the LEFT tensor factor's own
Dirac-squared, part of `D64^2`'s Round 23 exact decomposition) and `T12+T21`
(the `TERM1.TERM2+TERM2.TERM1` cross pieces) were both used as OPAQUE,
undecomposed blocks through Rounds 23-24. This round decomposes `TERM1_sq`
using `g2su3_H_element.py`'s ALREADY-BUILT, ALREADY-VALIDATED Kostant cubic
element `H` (built purely from the torsion 3-form `T(i,j,k)=<[Z_i,Z_j]_m,Z_k>`,
pure Nomizu/torsion algebra). Per that file's own docstring (citing
Agricola 2002 Theorem 3.2), at `t=1/2` (this project's Levi-Civita
convention) the cubic-Clifford torsion correction in `(D^{1/2})^2` is
exactly `-H`.

**Exact algebraic identity** (every piece defined by direct subtraction of
already-verified ground-truth matrices, asserted step-by-step in code,
NOT assumed):

```
Delta = kron(-H,Id8)                          [piece_H: pure Nomizu/torsion cubic term]
      + kron(cubic_and_curvature_L - (-H), Id8)  [piece_step2_rem: leftover after Casimir+H]
      + (T12+T21)                              [piece_T12T21: previously opaque cross terms]
      + TORSION_E                              [piece_torsion_E: Round 22/23's known term]
      + 2*sum_p kron(Ms[p],Ms[p])               [piece_cross_casimir: from N_p^2 Leibniz expansion]
```

where `cubic_and_curvature_L := Dslash_mat^2 - (-sum_p Ms[p]^2)` (exact
subtraction). Each of the five pieces is independently compressed onto
`span(w_a,w_b)` (Round 23/24's 2-dim SU(3)-invariant subspace) via a
Gram-corrected linear projection (`compress_2x2`) and summed.

## Falsifiable Claims

**C1:** `H` (imported from `g2su3_H_element.py`) re-verifies against its own
established closed-form check (`Tr(H^2)/8 = (3/8)*sum T(i,j,k)^2`).

RESULT: `[VERIFIED-tool]` — both sides equal exactly `3`.

**C2:** The five-piece decomposition of `Delta` is an EXACT algebraic
identity (verified by re-summing and comparing to `D64^2 - nabla*nabla -
F_Sminus` computed directly, entrywise over the full 64x64 matrices, not
just the 2-dim restriction).

RESULT: `[VERIFIED-tool]` — exact match, all 64x64 entries (sympy exact
equality after simplify).

**C3:** Individual pieces of this decomposition are NOT each required to
preserve `span(w_a,w_b)` (i.e. may "leak" outside it under matrix action);
only the FULL SUM (`= Delta`, itself a genuinely SU(3)-equivariant
quantity by construction) is guaranteed to. The `compress_2x2` helper
performs a Gram-corrected LINEAR projection (not a strict endomorphism
restriction) precisely to allow summing such pieces validly — linearity of
the projection guarantees `sum(compress(piece_i)) = compress(sum(piece_i))
= compress(Delta)` regardless of individual leaks.

RESULT: `[VERIFIED-tool]` — `kron(-H,Id8)` and `kron(step2_remainder,Id8)`
both DO leak outside `span(w_a,w_b)` (confirmed via the strict
`project_2x2` helper raising an assertion on first attempt, before
`compress_2x2` was introduced as the correct tool). The five compressed
pieces sum EXACTLY to the known `Delta_2x2=[[5/2,4/3],[4,5/2]]`.

**C4 (REWRITTEN post-skeptic — see "Skeptic Verdict" below; this is NO
LONGER framed as an informative hypothesis test of H specifically):**
`kron(-H,Id8)` alone, compressed onto `span(w_a,w_b)`, is EXACTLY
`[[0,0],[0,0]]` — `[VERIFIED-tool]`, re-confirmed independently (author
execution, not just skeptic code-inspection).

**This result carries LESS information about Kostant's H than originally
claimed.** Two independent skeptics traced the SAME underlying mechanism
(H is chirality-odd on the left factor; `w_a,w_b`'s left-tensor support
lies entirely in the even/S+ sector, so `kron(-H,Id8)` maps that support
into the odd/S- sector, disjoint from `span(w_a,w_b)`'s own sector) but
diverged on how to read it: Skeptic 1 treated the zero as a valid (if
structurally-forced) hypothesis-test result; Skeptic 2 called it a
**chirality-grading tautology carrying no information specific to H** —
*any* chirality-odd left-only operator would give the identical zero.

Author's OWN follow-up verification (independent of both skeptics, run
directly, `[VERIFIED-tool]`) went further and found Skeptic 2's specific
mechanism is itself INCOMPLETE, not merely correct-but-uninformative:
- `kron(e_1,Id8)` (a single Clifford generator, chirality-odd, structurally
  unrelated to torsion) compresses to `[[0,0],[0,0]]` — matches Skeptic
  2's substitution test, confirms chirality-flip alone is *sufficient*
  for the off-diagonal to vanish (a genuine tautology, confirmed
  structurally: the RIGHT tensor index cannot change under `kron(X,Id8)`
  for ANY `X`, and `w_a`'s RIGHT-support `{1,2,3}` is disjoint from
  `w_b`'s RIGHT-support `{7}` — this alone forces both off-diagonal
  entries to zero for literally any `X`).
- `kron(M_1,Id8)` (a single bivector/connection operator, CHIRALITY-
  PRESERVING, i.e. NOT of the type Skeptic 2's mechanism covers) ALSO
  compresses to `[[0,0],[0,0]]` — this is NOT explained by chirality-flip
  at all, since M_1 preserves left chirality.
- A literal random 8x8 matrix `X` compresses to a NONZERO diagonal
  `[[2/3,0],[0,5]]` (off-diagonal still zero, confirming the universal
  off-diagonal tautology above) — so the FULL zero (diagonal included)
  is NOT a universal fact about `kron(X,Id8)` for arbitrary `X`; H, e_1,
  and M_1 share some real structural property that a generic matrix does
  not, and this project has NOT identified what that property precisely
  is (candidate: each is built from a single antisymmetric structure-
  constant source acting alone, vs. the correlated multi-index SUMS that
  `F_Sminus`/`TORSION_E`/`cross_casimir` are — untested, flagged for a
  future round, NOT claimed here).

**Bottom line (both skeptics' conclusion CONFIRMED and further
strengthened by the author's own additional controls, though the precise
mechanism remains only partially understood):** `kron(-H,Id8)` compressing
to zero on this subspace is NOT decisive evidence that Kostant's H
(specifically, i.e. its being built from THIS project's torsion data) is
irrelevant to K — the test as constructed cannot distinguish "H is right,"
"H is wrong," or "any of several structurally-unrelated single-source
operators" from one another. This claim is DOWNGRADED from "the actual
hypothesis test" to "an inconclusive probe with an interesting but
incompletely-understood null."

**C5 (the genuinely informative finding of this round — PROMOTED to
headline per skeptic consensus):** the traceless residual `K` is
distributed across the four NON-`kron(-H,Id8)` pieces: `step2_remainder`
compressed = `[[-1/6,0],[0,5/2]]`; `T12+T21` compressed = `[[0,1],[3,0]]`;
`TORSION_E` compressed = `[[8/3,2/3],[2,0]]`; `2*sum kron(Ms[p],Ms[p])`
compressed = `[[0,-1/3],[-1,0]]`. Most notable: **`step2_remainder`'s
compressed value is a NON-SCALAR diagonal** (`-1/6` vs `5/2`, not equal).
Since `step2_remainder := cubic_and_curvature_L - (-H)` is, by STEP 2's
own construction, exactly the piece Agricola's Theorem 3.2 would assign to
a `t^2`-weighted "Jac_h curvature-Jacobi" term — and `g2su3_H_element.py`'s
own docstring explicitly flagged that piece as "NOT computed here...
requires full g2 structure constants beyond what's been built so far" —
this non-scalar result is empirical evidence that the Jac_h/curvature-
Jacobi piece is a REAL, nonzero presence in `cubic_and_curvature_L`, not
merely a theoretical possibility. This is the concrete, actionable lead
this round produced, independent of C4's inconclusive H-test.

## Kill Conditions

- C1/C2 killed if: skeptic finds an arithmetic/sign error in re-deriving H
  or in the five-piece identity (e.g. `curvature_R`/`nabla_bracket`'s sign
  convention misapplied relative to how `g2su3_Sminus_weitzenbock.py`
  itself uses them — this script rebuilds `nabla_bracket`/`curvature_R`
  locally rather than importing them; skeptic should verify the local
  rebuild is faithful to the original).
- C3 killed if: skeptic finds `compress_2x2`'s linear-projection argument
  is actually invalid (e.g. finds a case where summing non-endomorphism-
  preserving compressions does NOT equal the compression of the sum —
  this would be a real mathematical error in the compress_2x2 reasoning,
  not just a code bug).
- C4/C5 are NEGATIVE results already, not subject to "kill" in the usual
  sense — but the skeptic should check whether the negative result on C4
  is itself an artifact of a construction error (e.g. is `H` embedded with
  the correct sign/normalization relative to `-H` as Agricola's formula
  requires? Getting the OVERALL SIGN of piece_H wrong would not change
  "compresses to zero" if H's compression truly is zero regardless of
  sign — but it's worth an independent sign check).

## What this does NOT mean

- Does NOT establish that Round 24's "unresolved (i) vs (ii)" question is
  now resolved in favor of either reading. C4's null result is inconclusive
  (see above), not a falsification of "(i) frame correction" as a category
  — only of the single specific candidate "H alone, isolated via
  kron(-H,Id8)."
- Does NOT mean no clean geometric account of K exists — only that this
  round's specific probe (H alone, via this particular kron embedding)
  cannot distinguish candidates. A DIFFERENT decomposition or a proper
  derivation of the Jac_h/curvature-Jacobi term (flagged as the concrete
  next step, see C5) might still isolate something clean.
- Does NOT resolve the preprint's `8/45 vs ~1.03` norm-ratio tension.
- Does NOT establish any mechanistic link beyond the exact algebraic
  identities themselves — each compressed piece's numeric value is exact
  arithmetic, not evidence of a physical/geometric "meaning" for that
  specific number beyond what is directly derived.
- Does NOT claim to have identified the precise structural reason H, e_1,
  and M_1 all compress to zero while a random matrix does not — this is
  observed and reported, not explained. Any future claim about "why"
  requires a proper derivation, not an inference from three data points.

## Skeptic Verdict (FL Step 8a, 2026-07-11, two independent context-blind
skeptics + author's own follow-up tool-verification of the disagreement)

| Claim | Verdict | Note |
|---|---|---|
| C1 | CONFIRMED-REAL (both skeptics) | H re-verification exact |
| C2 | CONFIRMED-REAL (both skeptics) | five-piece identity exact, traced by hand + 3 independent 64x64 asserts |
| C3 | CONFIRMED-REAL (both skeptics) | compress_2x2 linearity is trivial matrix distributivity, no flaw found — this round's core methodology is sound |
| C4 | DISAGREEMENT (Skeptic 1: CONFIRMED-REAL: Skeptic 2: WEAKENED) → resolved WEAKENED, then further refined by author's own additional controls (E1/M1/random) showing the mechanism is broader/less understood than either skeptic stated | see rewritten C4 above |
| C5 | CONFIRMED-REAL (both skeptics), PROMOTED to headline finding | non-scalar step2_remainder diagonal is the actionable lead |

Durability note (Skeptic 1): C4/C5 per-piece values were only printed, not
asserted in the original script — hard asserts added below to prevent
silent breakage under future primitive refactors.
