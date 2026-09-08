# C184 Decision — the five deliverables, and two bugs I found on the way

**Date:** 2026-09-08
**Verdict:** **PROMOTE** — all six pre-registered predictions held, every
injected-error control flipped, the `S^2` doublet is derived rather than written
down, and all three of the adversarial pass's real findings are closed by
computation rather than by argument.

| script | checks | what it settles |
|---|---|---|
| `c184_two_questions.py` | 33/33 | the six pre-registered predictions |
| `c184b_descent_derivation.py` | 18/18 | the `S^2` doublet, derived by descent, with the weight-`0` sector as its negative control |
| `c184c_skeptic_followups.py` | 8/8 | the spinors actually in Hopf coordinates; controls for `P1`/`P2`/`P3`; the `C180` sign question |

Exact symbolic arithmetic throughout; no floating point in any verdict. All
numbers trace to `run_output.txt`, `run_output_b.txt`, `run_output_c.txt`.

---

## 1. The answers, in his labels

### Question 1 — `S^2`

**No, they cannot be written as functions of the angular coordinates. They are
complex, two-component, and double-valued.** The explicit pair, *derived* by
descent and not supplied:

```
    chi_{+1/2}(theta, phi) = e^{-i phi/2} cos(theta/2)
    chi_{-1/2}(theta, phi) = e^{+i phi/2} sin(theta/2)
```

Route (`c184b`, no step assumed): take the `k=1` scalar harmonics on `S^3`,
`span{x_0,x_1,x_2,x_3}` — no spinor anywhere yet; diagonalise the `U(1)` fibre
generator; the eigenspace is 2-dimensional, so split it further with the second
generator, whose eigenvalue **is** the label `m`; substitute Hopf coordinates;
observe `psi` enters only as `e^{-i psi/2}`; strip it. What survives is a
function of `(theta, phi)` alone, and it is the pair above up to a constant
unitary (see §3).

Why it is not a function: `chi(phi + 2pi) = -chi(phi)` **exactly** — the same
point of `S^2`, the opposite sign.

**Negative control, same machinery, opposite answer:** run the identical
procedure on the weight-`0` sector at `k=2`. Those come out `psi`-independent
with no phase to strip, and single-valued in `phi` — genuine functions on `S^2`.
The half-integer case is a result, not an assertion, because the integer case
run through the same code gives the other answer.

### The sting in the tail — how a bilinear can be a function when its factors are not

This is the part of his question that is easy to read past, and it was answered
nowhere in the correspondence before now.

```
    chi -> -chi   under a 2pi circuit in phi
    chi_a chi_b^*  ->  (-1)(-1)^* chi_a chi_b^*  =  + chi_a chi_b^*
```

The sign appears twice and cancels. Verified, not argued: all four bilinears
`chi_a chi_b^*` are single-valued in `phi` (`P5a`, `D7`), and

```
    chi^dag sigma chi = (sin th cos ph,  sin th sin ph,  cos th)
```

**exactly, all three components** (`P5b`), with unit length identically
(`P5c`). So the outer product really does project out the vector — and the
vector is an honest function on `S^2` — while neither factor is. There is no
tension: the obstruction is a sign, and a bilinear is quadratic in it.

### Question 2 — `S^3`

**Yes — and in the group trivialization they are constants.** They are complex
(two components per chirality); equivalently one quaternion per chirality, but
only in the quaternionic basis (see §2).

Two things make this precise, both computed:

- **As scalar functions they do not exist.** `L^2(S^3)` decomposes under
  `SU(2)_L x SU(2)_R` as exactly `(j,j)` and nothing else — verified level by
  level for `k=0,1,2,3` (`P1`). `(1/2,0)` is simply not in the list. This is a
  **second, independent proof of the no-go**, by decomposition rather than by
  the `2pi` argument, and it does not rely on it.
- **As sections they do.** Tensoring with the fibre gives `⊕_j (j, j±1/2)`, and
  at `j=0` that is `(0,1/2)` — dimension 2, `D_0 = 0` (`P2`). Those are his
  `psi_{(0,±1/2)}`; the other chirality supplies `psi_{(±1/2,0)}`.

**Caveat that must travel with the answer:** "they are constants" is true *in
the group trivialization* and false in a coordinate frame, where they pick up
the frame's rotation. The sentence is not true without the frame attached.

---

## 2. Complex or quaternionic

`x^mu = (1/2) Tr(sigma_mu^† U)` returns the four real coordinates
`(x_0,x_1,x_2,x_3)` **only** in the quaternionic basis
`sigma_mu = (I, i s_1, i s_2, i s_3)` (`P6a`). In the plain Pauli basis the same
formula returns `(x_0, i x_1, i x_2, i x_3)` (`P6b`) — the unwelcome factor of
`i` on the spatial components, confirmed rather than warned about.

So: on `S^3`, complex two-component per chirality, and equivalently quaternionic
because `C^2 ≅ H` and the group acts by quaternion multiplication — in that
basis. On `S^2` the quaternionic option does not exist at all: the sphere is not
parallelizable, so there is no global expression of any kind, of either type.
Two different answers to one question, and conflating them would be an error.

---

## 3. Two bugs I found, both mine, both worth stating

**(a) A sign in the total angular momentum.** The first run failed `P3`. The
orbital operator was taken as `J = -(i/2)X` while the spin operator was
`S = +sigma/2`, so `J_tot = J_orb + S` had its two terms in opposite
conventions and the cross term came out `-2 J.S` instead of `+2 J.S`. Symptom:
`Casimir_R = {3:2, 1:6}` where `{0:2, 2:6}` was predicted.

Part C never caught it, and could not have: a Casimir is quadratic and blind to
the overall sign. Only the **sum** in `J_tot` is sensitive. The check that now
catches it on sight is in the file: a genuine total angular momentum must close
on `su(2)` with `[J_a,J_b] = i eps_abc J_c`, and the mis-signed one does not.
With the sign fixed, `P3` holds exactly as pre-registered: `j_R=0` is dim 2 with
`D_0 = +3`, `j_R=1` is dim 6 with `D_0 = -1` — reproducing `C180`'s
independently computed multiplicities.

**(b) The quaternion-to-Pauli map is an ANTI-isomorphism**, and I descended
along the wrong circle because of it. The map sending `(1,i,j,k)` to
`(I, i s_1, i s_2, i s_3)` has `(i s_1)(i s_2) = -i s_3` while `i·j = k` maps to
`+i s_3` (`H1`, `H2`). So quaternionic **right** multiplication is matrix
**left** multiplication. The `psi` fibre of the Euler parameterization is
generated by the quaternionic-**left** field `X_3^L`, not `X_3^R`.

The symptom was unmistakable once printed: two vectors of a single `X_3^R`
weight sector came out with **opposite** `psi` phases, which a genuine weight
sector cannot do.

This is worth flagging outside the code: it is the **same order-reversal
phenomenon** as the transpose / anti-homomorphism point currently under
discussion in the correspondence, surfacing a second time in a different guise.
That the two are the same effect is a point the reply can make.

**(c) A third, smaller one, recorded because it is the session's recurring
shape.** The first version of `D9` compared the derived bilinear to the radial
vector component by component. The derived doublet differs from the
hand-written one by a constant unitary that **swaps** the components, which is a
rotation — and a rotation must fail a component-wise comparison. The check was
not wrong about the mathematics; it was the wrong check. Replaced by: recover
the constant `M`, verify it is unitary, compute the induced `SO(3)` matrix
`R = (1/2)Tr(sigma_a M sigma_b M^†)`, verify `R` is a rotation, and verify the
bilinear equals `R` applied to the radial vector. It does, exactly:
`R = [[0,1,0],[1,0,0],[0,0,-1]]` and `chi^† sigma chi = (sin ph sin th,
sin th cos ph, -cos th)`.

---

## 4. Skeptic (FL Step 8a, context-asymmetric)

Returned **three CONFIRMED, one WEAKENED, none FALSIFIED**, with one important
self-declared limit: **the reviewer had no shell and could not execute the
script.** Its "no failure found" therefore means "not found by close reading and
hand algebra", which is weaker than a run. Recorded as the reviewer stated it,
not upgraded.

Four attacks it made and lost, worth keeping because each strengthens a claim:

- **Is `P5b` automatic for any normalised spinor?** No. Unit *length* is
  automatic (Bloch sphere — that is `P5c`, and it is indeed trivial). The
  *direction* is not: the reviewer's `chi_swap = (e^{-i phi/2} sin(th/2),
  e^{+i phi/2} cos(th/2))` passes `P4` and `P5a` and gives the **antipodal**
  vector, failing `P5b`. It further showed the general family
  `(e^{-i phi/2}f, e^{+i phi/2}g)` with `f^2+g^2=1` is pinned **uniquely** to
  `f=cos(th/2), g=sin(th/2)` by the two constraints. So `P5b` does real work.
- **Are `XL` and `XR` secretly the same?** No — and `B3` is the safeguard: had
  they been equal, `B3` would be testing `[X^R,X^R]=0`, which `B2` shows is
  false, so `B3` would fail.
- **Is `P.pinv() * D * P` a valid block restriction?** Yes, given `D` preserves
  the span — which `E1a` checks. The reviewer noted this is the same `pinv`
  question `C180` §7 had to fix, and that here it is used correctly.
- **Is labelling-by-dimension trivial at `k=1`?** The dimension label is, and
  `claim.md` says so. What is not trivial is that `D_0` sorts *by irrep*.

Three findings that were real. All three are now closed by computation in
`c184c_skeptic_followups.py` (8/8) rather than by argument:

| finding | resolution |
|---|---|
| **F — Part F never substitutes Hopf into any spinor**, so "the spinors in Hopf coordinates" was not delivered, only "Hopf parameterises `S^3`". | Closed. `c184c` solves the `k=1` eigenproblem (dimensions 6 and 2, matching), takes one eigenspinor from each block, substitutes, and verifies the eigenvalue survives identically. E.g. the `D_0=+3` spinor `(-x_0 - i x_3, -i x_1 + x_2)` becomes `(-(e^{i(ph+ps-th)/2}+e^{i(ph+ps+th)/2})e^{-i(ph+ps)}/2, i(e^{i th}-1)e^{-i(-ph+ps+th)/2}/2)`. |
| **G1 — `claim.md` said every prediction had an injected-error control; only four of six did.** `P1`, `P2`, `P3` had none. | Closed. `P1`: the same `(j,j)` test applied to the spinor space at `k=0`, which is genuinely `(0,1/2)`, **fails** — so it is not a test that passes on anything. `P2`: mis-normalising the spin operator to `sigma` instead of `sigma/2` gives `Casimir_R = 3` instead of `3/4`. `P3`: the deliberately mixed operator `-i sum sigma_a (x) X_a^L` does **not** commute with the `J^R` Casimir, so sorting by irrep is not something every operator passes. |
| **G3 — a sign conflict with `C180`**, which states `[X_a^R,X_b^R] = -2 eps X_c^R` where `C184` verified `+2`. | **Not a conflict — two different objects, and the reason is again order reversal.** `C180` takes the commutator of the 4x4 *matrices* `R[a]`; `C184` takes the Lie bracket of the *vector fields*. Since `R_a R_b (q) = q e_b e_a`, the map `a -> R_a` is an anti-homomorphism while `a -> X_a^R` is a homomorphism, so the two brackets **must** differ in sign. Computed both in `c184c`: matrix `-2 eps`, vector field `+2 eps`, and verified `R_a R_b = R_{e_b e_a}` directly. This is the **third** appearance of the same order-reversal effect in this round. |

Two findings accepted as standing caveats rather than closed:

- **`W1` — the `S^2` doublet is not verified to solve the `S^2` Dirac equation.**
  It is now *derived* (`c184b`) as the weight-`(-1/2)`, `m = ±1/2` sector rather
  than written down, which is stronger than the reviewer saw; but "lowest
  **Dirac** harmonic" remains a textbook identification, because the `S^2` Dirac
  operator is still not built. This is the same gap the sent letter already
  declares.
- **`G4` — which `SU(2)` factor is called "left" is a convention**, not
  something the script fixes. Swapping the names would relabel `k=0` as
  `(1/2,0)`. The reply must present the pair as `{(1/2,0), (0,1/2)}` without
  asserting which is which physically.

---

## 5. What this does NOT establish

- **The reading of his four `S^3` labels is an assumption.** `(m_L, m_R)` with
  one entry zero, i.e. the two states of `(1/2,0)` and of `(0,1/2)`. If he meant
  something else, the labelling half answers a different question. Flagged in
  the reply, not buried here.
- **No new mathematics.** Peter-Weyl, the `D^{1/2}` matrix elements and
  spin-weighted harmonics are textbook. The work was getting them into his
  labels and his coordinates without error — and two errors were found doing it.
- **The `S^2` Dirac operator is still not built**, so its eigenvalues `±(l+1)`
  are still not independently produced. Unchanged from what was already sent.
- **The harmonics are still not transported into normal coordinates.**
  Groundwork only, as already stated to him.
- **`P3` is not as sharp as a bare "2 of 2" would suggest.** Dimensions 2 and 6
  are the only ones available at `k=1`, so dimension-matching alone would score
  full marks. What carries the content is that the `D_0` eigenvalue **sorts by
  irrep**, which dimension-matching does not supply.

---

## 6. Reproduction

```
cd experiments/20260908-c184-tom-two-questions
python c184_two_questions.py        # 33/33, ~2 min
python c184b_descent_derivation.py  # 18/18, ~2 min
```

`ruff check` and `ruff format`: clean on both.
