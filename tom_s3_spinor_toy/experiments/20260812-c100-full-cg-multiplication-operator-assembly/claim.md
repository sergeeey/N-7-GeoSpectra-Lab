# C100 -- assemble the full (q,p)-only multiplication operator matrix, level k -> level k+1

**Experiment id:** `20260812-c100-full-cg-multiplication-operator-assembly`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C90 (verified the mathematical basis for a
multiplication-type coupling operator via ONE extremal-weight
Clebsch-Gordan coefficient, `m1=j1`, per level; explicitly named "full
set of Clebsch-Gordan coefficients" as the next-step gap). C99
(extracted and verified the magnetic-number labeling `m_q(k,q)`,
`m_p(k,p)` directly from the certified `L_i`/`R_i` generators;
identified the literal extremal `p`-index at each `k`, correcting a
naive `p=k` assumption specifically at `k=1`).

---

## Why this is needed

C90's own decision.md scoped the actual multiplication-operator build
as: "construct the multiplication-type coupling operator properly in
the certified `(p,q,r)` basis... verify it against the full set of
Clebsch-Gordan coefficients (not just the one representative checked
here)." C90 itself checked exactly ONE `(q,p)` pair (the extremal
state) per level. This round builds the FULL matrix -- every `(q,p)`
pair at level `k` mapped to every `(Q,P)` pair at level `k+1` -- using
C99's now-verified magnetic-number labeling to correctly convert
between literal basis indices and the physical `(m_q,m_p)` values the
Clebsch-Gordan formula needs.

**Explicitly scoped OUT of this round:** the Clifford/spinor index `r`
-- `D^1_{ab}(g)` is scalar-valued and this round only builds the
`(q,p)`-only operator, matching the exact scope C90 itself worked in.
How `r` enters (if at all) remains a separate, open question.

## Method

For the level-`k` basis `|q,p⟩` (`q,p=0..k`, ignoring `r`) and
level-`(k+1)` basis `|Q,P⟩` (`Q,P=0..k+1`), the standard SU(2)
product-of-matrix-elements identity gives:

```
D^k_{q,p}(g) * D^{1}_{a,b}(g) = sum_J CG(j1,m_q; 1/2,a | J,m_q+a)
                                     * CG(j1,m_p; 1/2,b | J,m_p+b)
                                     * D^J_{m_q+a, m_p+b}(g)
```

with `j1=k/2`. Fixing `a=b=1/2` (matching C90's own choice, the
"top-top" matrix element of `D^1`) and `J=(k+1)/2` (the level-up
branch), this defines a `(k+2)^2 x (k+1)^2` matrix `M_k[(Q,P),(q,p)]`
whose entries are the product of two Clebsch-Gordan coefficients,
nonzero only when `Q,P` are the literal level-`(k+1)` indices whose
`m_Q=m_q+1/2`, `m_P=m_p+1/2` (via C99's own verified labeling tables,
inverted to look up literal index from physical `m`).

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P0 (structure)** | `M_k` has the correct dimensions `(k+2)^2 x (k+1)^2` for `k=1,2,3` | pending |
| **P1 (entries)** | every nonzero entry of `M_k` equals a directly-computed sympy `CG` product, exact symbolic value | pending |
| **P2 (cross-check vs C90)** | `M_k[(k+1,k+1),(k,k)] = 1` exactly, reproducing C90's own extremal-weight result as one entry of the now-fully-assembled matrix | pending |
| **P3 (non-degeneracy)** | `M_k` is not the zero matrix and not merely diagonal -- genuinely couples multiple `(q,p)` pairs to multiple `(Q,P)` pairs, unlike the block-diagonal translation-generator operators C79-C89 | pending |

## kill_criterion

If P0 or P1 fails, the assembly itself has a bug (indexing mismatch
between literal and physical labels, most likely) -- stop, debug
before drawing any conclusion. If P0/P1 hold but P2 fails, there is a
convention mismatch between this round's assembly and C90's own
extremal check that must be resolved before trusting the matrix. If
P0-P2 hold but P3 fails (matrix is trivial/diagonal), the
multiplication operator does NOT actually provide richer inter-level
structure than the already-excluded translation-generator family --
a real, informative null result that would require revisiting whether
this construction is worth pursuing further for task #59.

## What this cannot show

- Does **not** address `r`'s role -- the operator built here acts only
  on `(q,p)`, matching C90's own scope, not the full `(p,q,r)` basis
  the eventual physical operator needs.
- Does **not** build the full block-tridiagonal `D_PW` or run any
  truncation-convergence test -- those remain later steps.
- Does **not** verify the other three `D^1_{ab}` components
  (`a,b` other than `1/2,1/2`) -- only the one C90 itself used.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
