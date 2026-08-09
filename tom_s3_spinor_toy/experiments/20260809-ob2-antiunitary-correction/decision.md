# OB2 — C30's "Z2 symmetry" is orbit equivalence; the real symmetry is antiunitary

**Date:** 2026-08-09
**Verdict:** `C30_DEMOTED_TO_ORBIT_EQUIVALENCE__THETA_IS_THE_SYMMETRY`
**Corrects:** `experiments/20260803-ob2-t-matrix-order-parameter-z2/` (C30)

## The criticism, and it is correct

An external red-team audit made two claims about C30. Both checked here
rather than accepted, per `audit-verification-gate.md`.

**(a) C30 proved pointwise orbit equivalence, not a symmetry.** C30 built, for
each rank-one projector `T(n)`, a unitary `S_n = m̂·σ` with
`S_n T(n) S_n⁻¹ = 1−T(n)` — where **`m̂` depends on `n`**. That says the two
operators lie on a common unitary orbit. A *symmetry* needs **one fixed
operator** working for all `T` simultaneously. Reproduced C30's per-point
result here (it is correct as far as it goes); the criticism is about what it
licenses.

**(b) No single unitary can do it.** Verified two ways:
- exhaustive over the factorized Pauli set C30 itself searched — **0 candidates**
- random search over general 2×2 unitaries, 40 000 draws — **none found**

The reason is structural, not a search failure: `T(n) → 1−T(n) = T(−n)` is the
antipodal map `n → −n`, i.e. `R = −I₃` with `det = −1`. Unitary conjugation of
Pauli matrices induces only **proper** rotations (`SO(3)`, `det = +1`).
Confirmed: `det(−I₃) = −1`, not in `SO(3)`.

## The operator that does work — and it is an upgrade, not a demotion

```
Θ = i·σ₂·K          (K = complex conjugation)
```

| check | result |
|---|---|
| `Θ T(n) Θ⁻¹ = 1 − T(n)` at all 8 random Bloch points | **True** |
| `Θ² = −I` | **True** |
| `Θ σ_i Θ⁻¹ = −σ_i` for all three `i` (the structural reason) | **True** |

One fixed operator, no `n`-dependence. This is the genuine symmetry.

**Negative control** (a check that accepts everything proves nothing): the
wrong candidate `i·σ₁` — which flips only two of the three Paulis — is
**rejected**. The framework discriminates.

**Why this is an upgrade:** `PARENT_ACTION_GATE.md`'s OB2 checklist lists
**"real structure `J`" as NOT ATTEMPTED**, and C30 separately recorded that
its naive *linear* grading candidate **failed** `{γ,D} = 0`. An antiunitary
`Θ` with `Θ² = −1` is exactly the object that checklist field asks for — and
it **explains** the grading failure rather than leaving it as an unexplained
negative: the exchange is order-two on the projector space (`T → 1−T → T`)
but lifts *projectively* to the spinors (`Θ² = −1`). A linear `Z₂` grading was
the wrong object to look for.

## The topological point, checked concretely

The per-point construction needs an axis `m̂ ⊥ n̂` chosen for every `n̂ ∈ S²` —
a nonvanishing tangent vector field on the 2-sphere, which the hairy-ball
theorem forbids. C30's own code chose `m̂ = cross(n̂, ref)` with `ref` selected
by a **case split** on `|n_z| < 0.9`. It silently patched two charts. That is
what a global obstruction looks like when it is not named.

## Net effect on OB2

| | before (C30) | after |
|---|---|---|
| Exchange `T ↔ 1−T` | "internal Z₂ symmetry via SU(2) conjugation" | **pointwise orbit equivalence** |
| A single global unitary | implied | **proven not to exist** |
| The actual symmetry | — | **antiunitary `Θ = iσ₂K`, `Θ² = −I`** |
| `PARENT_ACTION_GATE` "real structure J" | NOT ATTEMPTED | **candidate supplied** |
| Why the grading failed | unexplained negative | **explained** (projective lift) |

## What this does NOT mean

1. Does **NOT** resolve OB2. The physical action (`F6`) remains entirely
   open — Codex's own item-5 text already said so, and nothing here changes it.
2. Does **NOT** verify `Θ` against the full NCG real-structure axioms. It is a
   candidate for the `J` field; `[D,Θ]`/`{D,Θ}` and the KO-dimension
   consistency conditions are unchecked.
3. Does **NOT** touch the finite algebra's own `J_F`. Different object.
4. Does **NOT** import the corrected OB10/C32 conclusion. The `Θ² = −1` found
   here is on the **internal 2-dim order-parameter space**, not the geometric
   S³×S⁶ bundle (which C32 establishes is REAL). The audit separately
   hypothesised these might have been conflated — that is a *plausible and
   untested* suggestion, recorded, not adopted.

## Next gate

1. Check `Θ` against the NCG real-structure axioms (`[D,Θ]` or `{D,Θ}`, plus
   the sign triple `(Θ², ΘDΘ⁻¹/D, ΘγΘ⁻¹/γ)`).
2. Test the audit's conflation hypothesis explicitly: is the quaternionicity
   the project has been chasing a property of the **internal** sector rather
   than the geometric one? C32 (geometry REAL) and this round (internal
   `Θ² = −1`) are consistent with that reading but do not establish it.

## Check

```
cd experiments/20260809-ob2-antiunitary-correction
python antiunitary_check.py
```
Expect `VERDICT: C30_DEMOTED_TO_ORBIT_EQUIVALENCE__THETA_IS_THE_SYMMETRY`;
0 single-unitary candidates from both searches; `Θ` valid at all points with
`Θ² = −I`; negative control rejects `i·σ₁`.
