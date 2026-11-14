# C155 — the `|c| = (2/3) mu` coincidence is a dimensional artifact

**Question type (EstimandOps L0): DESCRIPTIVE.** Tier: FL Full.

## Setting (all objects pre-existing in this repo, not introduced here)

For a homogeneous nearly-Kahler 6-space `G/H` with an invariant spinor `psi_+`
and an admissible family `V` of `H`-equivariant connections, two quantities have
been used across C139–C154:

    c(nabla)  = <w_hat, D_twisted(nabla) u_hat>     (twist / Term2 coefficient,
                                                     a matrix in Hom(dom,tgt))
    mu(nabla) = || D_Sigma(nabla) psi_+ || / ||psi_+||   (untwisted Dirac norm)

At the Levi-Civita point `|c|/mu = 2/3` on `S^6`, and the same value was believed
to recur on `SU(3)/T^2`. C154 rejected the "family-wide law" framing on `S^6` but
left `SU(3)/T^2` INCONCLUSIVE.

## Claim

**The `2/3` relation exists only because the `S^6` admissible family is
1-complex-dimensional. It is not a law, and on a genuinely multi-plane
nearly-Kahler coset the two quantities are structurally incomparable.**

Concretely, with `Q_c(v) = ||c(v)||^2_HS` and `Q_mu(v) = ||D_Sigma(v) psi_+||^2 /
||psi_+||^2` — two canonical real quadratic forms on the SAME real vector space
`V`, no norm chosen post hoc — computed exactly (sympy, no floats):

| | `S^6` | `SU(3)/T^2` |
|---|---|---|
| `dim_R V` | 2 | 6 |
| `Q_c` | `(4/9) Q_mu`, rank 2 | `2 * ||v||^2` — **isotropic, rank 6** |
| `Q_mu` | rank 2 | **rank 2** |
| proportional? | yes (**forced**: 1 complex dim) | **NO — different ranks** |

Two forms of different rank cannot be proportional under any normalisation, so
**no universal identity between `|c|` and `mu` exists.** The `S^6` agreement is
the degenerate case `dim_C V = 1`, where any two `C`-linear maps are
automatically proportional.

## Mechanism (why the ranks differ) — directly tested, one part withdrawn

The mechanism was NOT asserted from the two rank numbers; each half was made
falsifiable and run separately (Steps 4 / 4b). The 3 root planes contribute

* **incoherently to `c`** — the three blocks land in mutually **HS-orthogonal**
  subspaces of `Hom(dom,tgt)`: all cross-block pairings are **exactly 0**
  (`A-B`, `A-C`, `B-C`, four pairings each). Within a block the pairing is purely
  imaginary (`-8i`, so `Re = 0`). Hence `Re(G_c)` is diagonal — isotropic, rank 6.
  **[CONFIRMED]**
* **coherently to `mu`** — all six images lie in **one and the same real
  2-dimensional subspace** of `Sigma`; the three planes differ only by the signs
  `(+, -, +)`, verified separately for the even directions `(0,2,4)` and the odd
  ones `(1,3,5)`. Hence rank 2, kernel 4. **[CONFIRMED]**

**Withdrawn sub-claim:** an earlier version of this file said that shared
subspace was a *complex line* and that `M` is `C`-linear per block. Step 4
falsified both: `M(dir1)` is not a complex multiple of `M(dir0)`, and
`rank([M0 M1 | i*M0]) = 3`, so the 2-plane is **not** closed under multiplication
by `i`. The rank-2 conclusion does not depend on the withdrawn part; only the
"complex line" wording did.

`S^6` has effectively one plane, so coherent and incoherent are indistinguishable
there — which is exactly why the artifact looked like a law.

## Closed forms (verified exactly on a symbolic 6-parameter connection)

    Q_mu(v) = 4 (a_0 - a_2 + a_4)^2 + 4 (a_1 - a_3 + a_5)^2      rank 2
    Q_c(v)  = 8 (a_0^2 + a_1^2 + a_2^2 + a_3^2 + a_4^2 + a_5^2)  rank 6

(raw family basis; `Gram(family) = 4 I`). The rank gap is visible by inspection.
The `Q_mu` form was first hand-derived by a context-blind skeptic from the
printed Gram matrix and then verified symbolically here.

## Exact consequences, verified as identities (not as rank numbers)

1. **A 4-dimensional space of admissible `T^2`-equivariant connections
   annihilates the invariant spinor**: `D_Sigma(v) psi_+ = 0` exactly, verified
   as an 8-component vector identity for a kernel basis
   `{(1,0,1,0,0,0), (0,1,0,1,0,0), (-1,0,0,0,1,0), (0,-1,0,0,0,1)}` **and** for a
   random rational combination outside that basis. The same connections have
   `||c||^2 != 0` — `c` survives exactly where `mu` dies.
2. **The same 4-dimensional family annihilates the ENTIRE space of
   `T^2`-invariant spinors**, not merely the chosen Killing eigenvector:
   `rank(v -> (D(v) psi_+, D(v) psi_-)) = 2`, the same as for `psi_+` alone. So
   the result does not depend on which invariant spinor is called `psi_+`.
   (A context-blind skeptic predicted this union rank would be **4** "by
   chirality independence"; running it gave **2** — its prediction was wrong and
   the claim came out stronger.)
3. **`c` is injective on `V`** (`Q_c` isotropic of full rank 6): the zero locus of
   the connection coefficient on `SU(3)/T^2` is exactly `{0}`. This answers, for
   this coset, the question C147 asked on `S^6`.
4. Per-direction magnitudes are equal across all 6 directions
   (`||c||^2 = 32`, `||D psi_+||^2 = 8` in the raw family basis) — the Weyl/Schur
   signature, consistent with both structures being symmetry-forced.

## Basis-independence (self-attack, Step 3)

"Isotropic" is a basis-dependent word. Checked: `Gram(family_sym) = 4*I_6` in the
natural metric on `V`, i.e. the basis was already orthonormal up to one common
scale; re-deriving both forms in a genuinely orthonormal basis gives
`Re(G_c) = 2*I_6` and `Re(G_mu)` of rank 2. The isotropy claim **survives**.
Ranks and `dim ker = 4` were basis-independent from the start.

## What this does NOT claim

1. **Not new mathematics.** Both structures look **symmetry-forced** (weight
   orthogonality + Weyl `S_3` + the `C`-linearity already registered in C153).
   The contribution is settling a question this project chased for three rounds,
   not discovering a new phenomenon. Stated explicitly to avoid the C153/C154
   failure mode ("forced != discovered").
2. Nothing about `N_gen = 3` or any physical claim.
3. Nothing about `lambda` (still `FREE_COUPLING_PARAMETER`).
4. Not a theorem about all nearly-Kahler 6-manifolds — two homogeneous examples
   with fixed conventions. The dimensional-artifact ARGUMENT is general; the
   computations are not a proof for arbitrary `G/H`.
5. The positive control on `S^6` is pre-registered as **vacuous** and its passing
   is not evidence for anything.
6. **Scope limitation raised by the skeptic (F3) and accepted:** "no universal
   identity" is a statement about the REAL quadratic forms `Re(G)`. The imaginary
   parts are not compared — `Im(G_c) != 0` (a genuine symplectic invariant) while
   `Im(G_mu) = 0` identically. An identity involving the full Hermitian data is
   not addressed here and is NOT ruled out. This scope is load-bearing; do not
   read "structurally incomparable" as broader than the real forms.
7. The `(+,-,+)` sign pattern is **unexplained**. The hypothesis that it is the
   `A_2` root relation was tested and FALSIFIED (Step 5): the weights
   `(-2,1), (1,1), (1,-2)` satisfy `wA + wB + wC = 0`, i.e. pattern `(1,1,1)`,
   whereas `Q_mu`'s coefficient functional is `(1,-1,1)`. A single plane
   re-orientation would reconcile them, which is exactly why no match is claimed.

## Correction made during this round (kept, not hidden)

The first formalisation compared full **Hermitian** Gram matrices and the `S^6`
positive control FAILED (`G_c` had off-diagonal `±4i/3`, `G_mu` had `0`). That was
a defect of the test, not the geometry: `V` is a REAL vector space, so the
quadratic form only sees `Re(G)`. Fixed; `Im(G)` is now reported separately as a
distinct symplectic invariant (nonzero for `c`, identically zero for `mu`) rather
than silently dropped.
