# C158 Steps 3-4 — Pin(m) lift of the Weyl action, and the true equivariance of M

**Question type (EstimandOps L0): DESCRIPTIVE.** Tier: FL Full.
**Mandate (standing):** autonomy over computation, NOT over declaring
"discovery". This file reports the DIRECT USER REQUEST ("подними действие
Вейля на спиноры и проверь эквивариантность M") to completion.

## Result, stated first

> **`S . M_+(v) = i * M_-(R.v)`, exactly, verified on all 6 family basis
> directions, for both Weyl generators `R01` and `R12`.**

`M_+(v) := D_Sigma(v) psi_+` (C158's original `M`), and `M_-(v) := D_Sigma(v)
psi_-` (the analogous map built from the OTHER `T`-invariant spinor). `S` is
the genuine Pin(m) lift of the Weyl reflection `R` (constructed and verified
below), acting on `Sigma` by LEFT Clifford multiplication.

**`M` is not equivariant on its own** — because `psi_+` itself is not
Weyl-fixed (`S . psi_+ = -i * psi_-`, verified exactly): the Weyl group swaps
the two `T`-invariant spinors. The genuinely equivariant object is the PAIR
`(M_+, M_-)`, on which `W(A_2)` acts by swapping (with phase), matching the
swap of `psi_+`/`psi_-`. This is a complete, clean answer, not a partial one —
finding that the naive question was ill-posed (holding `psi_+` fixed) IS the
answer, not a failure to answer it.

## Three self-caught corrections in reaching this (kept, not hidden)

1. **The original "integrate a path through SU(3)" strategy was
   misconceived.** `A_pq` (a ROOT generator, i.e. an element of `m`, not of
   the Cartan `t`) does not generate a path that stays inside `N(T)` for
   generic `theta`, and `ad(A_pq)` does not preserve `m` — checked directly:
   `[A01, M_BASIS[0]] = 2*h1`, a PURE Cartan direction, which `to_m` silently
   discards. Confirmed the resulting damage numerically: `R01_theta(pi/7)` is
   not orthogonal (residual 0.61, det 0.62 instead of `+-1`). The `theta=0`
   derivative regression had still matched, masking the problem (leakage is
   higher-order there).
2. **The deeper, root cause: `det(R01) = det(R12) = -1`.** Both simple Weyl
   reflections are ORIENTATION-REVERSING elements of `O(m)`. A bivector
   exponential (`spin_lift(L)` exponentiated) is always EVEN-graded and can
   only ever cover `SO(m)` — structurally incapable of reproducing a
   `det=-1` map, regardless of any theta or indexing fix. Genuine odd Pin(m)
   elements are required.
3. **`[spin_lift(L), v] = -L(v)` exactly**, in this project's specific
   Clifford convention (`E_a^2=-1`) — the opposite sign from what this session
   initially assumed by analogy with generic geometric-algebra references.
   Verified directly via the Lie bracket (cheaper, more diagnostic than
   guessing at the group level): conjugation by `exp(theta*spin_lift(L))`
   reproduces `R(-theta)`, not `R(+theta)`. Fixed by inverting the built
   rotor for the even/rotation part.

## Construction that survived verification

`R01 = Refl_{e0} . Rot`, `R12` similarly (each Weyl reflection factored as a
single-axis reflection composed with a genuine `SO(m)` rotation in the
remaining two 2-planes — found automatically, not assumed). Lifts:

- `Rot` (even, det +1): `S_rot := exp((pi/2)*spin_lift(L_rot))^{-1}` (the `^-1`
  is correction 3). Verified: conjugation by `S_rot` reproduces `Rot` exactly
  on all 6 Clifford vector generators.
- `Refl_{e0}` (odd, det -1): `n := E_{e0+1}` (a single Clifford vector), with
  the TWISTED adjoint `v |-> -n v n^-1` (standard Pin(n) formula for odd
  elements). Verified exactly against `Refl_{e0}` on all 6 generators
  (untwisted `n v n^-1` does NOT match; twisted does).
- Combined: `S := S_rot * n` (odd, since even*odd=odd). Verified: the twisted
  adjoint `v |-> -S v S^-1` reproduces the FULL `R01`/`R12` exactly on all 6
  generators.

## Q1-Q4, answered

| # | question | answer |
|---|---|---|
| Q1 | order of `S01`, `S12` on `Sigma` | Neither `+I` nor `-I`; `S01^2 = diag(1,1,-1,-1,-1,-1,1,1)` — a genuine mixed pattern (order 4, matching the same "torus-element" shape found for `R01^2` back in Step 1's ambient action on `m`) |
| Q2 | how does `psi_+` transform | `S01 . psi_+ = S12 . psi_+ = -i * psi_-` exactly — BOTH Weyl generators swap the two `T`-invariant spinors identically |
| Q3 | is `D_Sigma(v)` equivariant | **YES, exactly**: `-S D_Sigma(v) S^-1 = D_Sigma(R.v)` for all 6 family directions, both generators — the "should follow automatically from Clifford covariance" expectation is CONFIRMED, not just assumed |
| Q4 | is `M` equivariant | Naive form FALSE (neither `+` nor `-` sign works) — because it presupposes `psi_+` fixed, which Q2 shows is false. The TRUE equivariant statement is `S.M_+(v) = i * M_-(R.v)`, verified exactly |

## What this does NOT establish

1. Nothing about `N_gen=3`, `lambda`, triality, or any physical claim.
2. Not novelty-audited: Pin/Spin lifts of Weyl group actions on isotropy
   modules of flag manifolds, and their swap-action on invariant spinor pairs,
   are very likely standard material in the equivariant-Dirac-operator
   literature (the same literature C156/C157's novelty checks already found
   this project's whole `D_Sigma` construction sits inside). Not checked here.
3. Not skeptic-reviewed.
4. One homogeneous space (`SU(3)/T^2`), fixed conventions — not a general
   theorem.
5. The isotypic decomposition from C158 Step 2 (`ker(M)=2*standard`,
   `quotient=trivial+sign`) was computed using ONLY the ORTHOGONAL action on
   `V_conn`'s 6-dim COORDINATES (`W01`, `W12`, real matrices) — that
   decomposition is UNAFFECTED by anything found in Steps 3-4 (which concern
   the SEPARATE question of lifting the action to `Sigma`, not to `V_conn`
   itself). The two results are complementary, not in tension.

## Reproduce

```
python c158_step3_spin_lift.py        # ORIGINAL (flawed) attempt -- kept for
                                       # the record, documents errors 1 above
python c158_step3b_pin_lift.py        # intermediate debugging (error 3 found)
python c158_step3c_pin_lift_final.py  # FINAL correct Pin(m) lift, all verified
python c158_step4_equivariance.py     # Q1-Q3 (Q4's correct sign fixed by
                                       # hand after this script; see above)
```
