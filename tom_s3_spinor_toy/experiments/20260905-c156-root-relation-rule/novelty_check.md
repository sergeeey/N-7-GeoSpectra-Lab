# C156 — Novelty check (FL Step -3), run before the verdict

## What is definitely NOT new (found, and used as background, not claimed)

| fact used here | published source |
|---|---|
| existence/dimension of invariant spinors on maximal flag manifolds is governed by combinatorics of the positive roots | Artacho–Semmelmann, *Invariant Spinors on Flag Manifolds*, arXiv:2407.08493 (Thm 6(1) gives `2^floor(n/2)` as an `A_n`, `n` even bound; matches the `dim_C Sigma^T = 2` computed here for `A_2`) |
| invariant spinors on a homogeneous space are exactly the ones parallel for the **canonical** connection | standard; restated in the same literature. Consistent with the setup here: the canonical connection is `Lambda = 0`, and `M(0) = 0` trivially |
| the one-parameter family of connections joining canonical to Levi-Civita, and the cubic Dirac operator at parameter 1/3 | Agricola, *Connections on naturally reductive spaces…*, arXiv:math/0202094; Kostant | 
| `Sigma` is a Clifford module; `omega` anticommutes with `e_a`, so the Dirac operator is odd | textbook |

**The `+-1`-in-`R` criterion for existence of an invariant spinor was
re-derived here from scratch** (a spinor weight is `(1/2) sum eps_k beta_k`), and
used to disqualify `C_2`, `A_3` and `B_3` before wasting a build on them. That
re-derivation reproduces published results — it is a consistency check on this
round's machinery, **not** a new result.

## What was searched for and NOT found

Searches run: equivariant Dirac operators + invariant spinors + flag manifolds +
image/surjectivity/isotropy; cubic Dirac operator + flag manifold + invariant
connections + kernel/image dimension. Nearest hits were the papers above plus
Huang–Pandžić (*Dirac Operators in Representation Theory*) and the
Freed–Hopkins–Teleman/Landweber line — none of which, in what was retrieved,
states the specific quantity studied here: **the rank of the map from the space
of `T`-equivariant connections to `Sigma`, given by the Dirac response of a
fixed invariant spinor.**

**This is `[WEAK]` evidence at best.** The area (equivariant Dirac operators on
homogeneous spaces) is classical and heavily worked; "not in the handful of
papers a web search surfaced" is a statement about the search, not about the
literature. No claim of novelty is made on this basis.

## The stronger reason to doubt novelty/importance, stated by this round itself

The containment half of HYPOTHESIS S is **forced** by chirality; the remaining
content is surjectivity of a map whose source (`dim V` = 6, 30, 12) is much
larger than its target (2, 4, 4). A generic linear map with such dimensions is
surjective with probability 1. **If a null model shows surjectivity here is
generic, the hypothesis is near-vacuous** — forced part plus generic part, with
nothing left over. That test was explicitly handed to an independent
context-blind reviewer with shell access as its highest-priority attack, and its
verdict is recorded in `decision.md`.
