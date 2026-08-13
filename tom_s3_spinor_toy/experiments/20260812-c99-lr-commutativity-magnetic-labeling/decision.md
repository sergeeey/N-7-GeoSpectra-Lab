# C99 decision — P0 was a category error (self-corrected before running); P1-P3 verified, k=1 magnetic-labeling anomaly found

**Verdict:** `ALL_VERIFIED__LABELING_READY_FOR_FULL_CG_ASSEMBLY`
**Status:** RESOLVED — one design flaw self-corrected mid-round, substantive result obtained

---

## Same-day correction: P0 as originally pre-registered was ill-posed

`claim.md`'s own P0 asked whether the raw `(k+1)x(k+1)` matrix
commutator `[L_i(k), R_j(k)]` vanishes for all `i,j` and `k=1,2,3,4`.
**This is the wrong question, and running it first (before catching
the error) produced a misleading result:** it failed for every
off-diagonal `(i,j)` pair, at every `k` (e.g. `[L1,R2](k=2) =
[[0,2I,0],[4I,0,4I],[0,2I,0]]`, nonzero).

**Why this is not informative, and not a real physics finding:** `L_i`
and `R_i` act on DIFFERENT tensor factors (`q` and `p` respectively)
of the `(k+1)^2`-dimensional matrix-coefficient space
`D^k_{q,p}(g)` — they are not two operators on the same `(k+1)`-dim
space, so there is no reason their raw `(k+1)x(k+1)` matrix forms
should commute as ordinary matrix multiplication, and asking them to
is a category error (comparable to asking whether a row-operation
matrix and a column-operation matrix "commute" when compared as if
they acted on the same space). Caught by re-deriving, from first
principles, what the CORRECTLY posed question is: does the
tensor-embedded action `(L_i ⊗ I)` (left-multiplication on the full
`D^k` matrix) commute with `(I ⊗ R_j^T)` (right-multiplication, via
the standard `vec(AXB) = (B^T⊗A)vec(X)` identity)? This is
**guaranteed by plain matrix associativity** (`A(XB) = (AX)B` for ANY
matrices `A,X,B`) — it needs no symbolic/empirical verification at
all, for ANY choice of `L_i`, `R_j`, correct or not. Verified this
directly for one representative case (`k=2`, `[L1⊗I, I⊗R2^T]`) as an
implementation sanity-anchor, not as a criterion the round's own
verdict depends on — confirmed zero.

**Consequence:** the original P0 has been dropped from this round's
own pass/fail logic entirely (see script docstring for the full
correction). This is recorded here explicitly rather than silently
edited out, per this project's own same-day-correction discipline —
the mistaken premise ("independence needs checking, and might be
false") was itself the thing worth catching before it propagated into
a false "STOP, the whole construction is broken" verdict, which is
what the flawed P0 would have produced.

## P1/P2 — magnetic-number labeling, extracted directly (not assumed)

For each `k=1,2,3,4`, `m_q(k,q) := L_1(k)[q,q]/i` and `m_p(k,p) :=
R_1(k)[p,p]/i` (both well-defined since `l_{e1}(k)` is diagonal, and
`L_1`, `R_1` are each `+-l_{e1}(k)` or `+-l_{e1}(k)^T`, unaffected by
the transpose). Converted to standard physical spin units (`j1=k/2`,
`m` ranging `-j1..j1` in integer steps):

```
k=1: m_q = [-1/2, +1/2]      m_p = [+1/2, -1/2]
k=2: m_q = [+1, 0, -1]       m_p = [-1, 0, +1]
k=3: m_q = [+3/2,+1/2,-1/2,-3/2]   m_p = [-3/2,-1/2,+1/2,+3/2]
k=4: m_q = [+2,+1,0,-1,-2]   m_p = [-2,-1,0,+1,+2]
```

Both `m_q` and `m_p` form evenly-spaced sequences at every `k` (P1,
P2 both PASS) — confirming the labeling is a genuine, clean magnetic
number in every case, not an artifact.

**Note the k=1 vs k>=2 sign pattern**: `m_q` decreases with increasing
index `q` for `k=1` but increases with `q` for `k>=2`; `m_p` does the
opposite. This is the direct numerical manifestation of C96-C98's own
"L/R roles swap between k=1 and k>=2" finding, now expressed as an
explicit, usable magnetic-number table rather than an abstract
matrix-candidate label.

## P3 — extremal-index identification, and the k=1 anomaly

For each `k`, identified which literal `p` has `m_p(k,p) = j1` (the
extremal/top state, `m1=j1`, that C90's own single-representative
Clebsch-Gordan check used):

| k | extremal p (m_p = j1) | naive "p=k" assumption holds? |
|---|---|---|
| 1 | **p=0** | **NO** |
| 2 | p=2 | yes |
| 3 | p=3 | yes |
| 4 | p=4 | yes |

**At k=1, the extremal state is p=0, not p=k=1 as one might naively
assume by analogy with `l_{e1}`'s own raw index ordering.** This is a
direct, concrete consequence of C95's own finding that `R_i(1) =
-l_{e_i}(1)^T` is SIGN-FLIPPED relative to `l_{e1}(1)` itself (whereas
`R_i(k>=2) = +l_{e_i}(k)` directly, matching `l_{e1}`'s own convention
with no flip). Recomputing the Clebsch-Gordan coefficient at the
CORRECTLY identified extremal index (`p=0` at k=1, `p=k` at k=2,3)
reproduces C90's own abstract result (coefficient `1`, exact) in every
case (P3 PASSES) — the abstract CG value doesn't depend on which
literal index we call "extremal", but knowing WHICH literal index that
is, correctly, is exactly the new information this round adds and
C90's own check never determined (it worked in pure `(j,m)` language,
never naming a literal `p`).

## Practical consequence for task #59 (multiplication-operator build)

The full `(q,p) -> (Q,P)` Clebsch-Gordan assembly for the
multiplication operator can now use the CORRECT, verified magnetic
labeling tables above, instead of a naive `m = 2\cdot\text{index} - k`
assumption that would have been silently wrong at k=1 specifically
(off by an index-reversal on the p-side, and would need care on the
q-side too given `m_q`'s own k-dependent sign pattern). This closes
the specific "unstated condition" gap the explore-agent's own
context-gathering pass flagged before this round started.

**Still open, explicitly deferred:** the FULL CG-coefficient assembly
for all `(q,p)` pairs (not just the extremal one) -- the actual
operator-matrix build. And `r`'s role in the multiplication operator
(the Clifford/spinor index `build_dbar` uses) remains completely
unaddressed -- `D^1_{ab}(g)` is scalar-valued and does not obviously
touch `r`; how the two combine, if at all, is a genuinely open
question this round does not attempt to resolve.

## What this cannot show

- Does not build the multiplication operator itself, nor verify the
  full set of CG coefficients across all `(q,p)` pairs.
- Does not resolve `r`'s role in the construction.
- Does not change `N_gen=3`'s CONDITIONAL status.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## Verification

- `ruff check experiments/20260812-c99-lr-commutativity-magnetic-labeling/`
  — clean, 0 errors.
- The tensor-embedded sanity-anchor was verified directly via sympy's
  own Kronecker product (`sp.kronecker_product`), not merely asserted
  from the associativity argument.
- All magnetic-number extractions use `sp.nsimplify` on exact matrix
  entries (`L_1(k)[q,q]/i`, `R_1(k)[p,p]/i`), not floating-point
  approximation.
