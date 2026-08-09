# OB10 CORRECTION — the pseudo-real verdict was a convention artifact

**Date:** 2026-08-09
**Verdict:** `OB10_CORRECTED__TYPE_IS_REAL__C31_INVERTED`
**Supersedes:** `experiments/20260803-ob10-ko-dimension-majorana-check/` (C28)
and `experiments/20260806-ob10-c27-majorana-halving/` (C31), both committed
earlier the same week.

## What was wrong

OB10 concluded the geometric S³×S⁶ spinor bundle is **PSEUDO-REAL**, from a
mixed signature `Cl(6,3)` it reported as a genuine geometric finding. Both are
wrong, for one reason:

**Two long-standing parts of this project carry OPPOSITE Clifford sign
conventions, and OB10 was the first round ever to combine them.**

| source | convention | algebra |
|---|---|---|
| S³ — `round67/e2_s3_torsion_deformation.py` | `Z_i = i·σ_i`, `{Z_i,Z_j} = −2δ` | `Cl(0,3)` |
| S⁶ — `s6-harm-g0/s6_harm_g0_clifford.py` | `Γ_a` hermitian, `{Γ_a,Γ_b} = +2δ` | `Cl(6,0)` |

Gluing those without reconciling the signs produces `Cl(6,3)` — which OB10
then read as geometry. But S³ and S⁶ are **both Riemannian**; their product is
a 9-dimensional Riemannian manifold, whose spinor bundle requires **one**
uniform Clifford convention.

## The decisive test [VERIFIED-numpy]

Uniformise (`Γ'_a = i·Γ_a`, so all nine generators satisfy `{Γ,Γ} = −2δ`) and
re-run the identical exhaustive charge-conjugation search:

| | signature | unique `B` | `B·conj(B)` | type |
|---|---|---|---|---|
| as-built (mixed) | `(6,3)` | `σ₂⊗σ₂⊗σ₁⊗σ₂` | `−I` | PSEUDO-REAL |
| **uniform `Cl(0,9)`** | `(0,9)` | `σ₂⊗σ₁⊗σ₂⊗σ₁` | `+I` | **REAL** |

The uniform answer is the geometrically correct one and matches the standard
result independently: `Spin(9)`'s spinor module `Δ₉ = ℝ¹⁶` is **real** type
(`9 mod 8 = 1`).

**Negative control:** the test must be able to tell the two cases apart at all
— signature `(6,3)` vs `(0,9)`, type PSEUDO-REAL vs REAL. It discriminates.

## Consequence: C31's verdict is INVERTED, not merely weakened

C31 (committed 2026-08-06) argued: the relevant factor is pseudo-real ⇒ no
Majorana condition can exist ⇒ that row of C27's Relaxation Map is **CLOSED**.
Its premise is exactly the type now corrected. Re-checked on the correct
structure:

```
Majorana condition psi = B conj(psi) on the 16-dim module:
  under the OLD mixed/pseudo-real B : solution dimension 0   (forbidden)
  under the CORRECT uniform/real B  : solution dimension 16  (of 32 real d.o.f.)
```

It exists, and it halves the module exactly. **The Majorana row of C27's
Relaxation Map is OPEN, and is now a live candidate mechanism** — the opposite
of what C31 claimed.

## Scope — what is and is not established

**Established:** the reality type of the geometric Clifford module is REAL,
not pseudo-real; a Majorana condition is algebraically available on it; C31's
no-go argument fails at its premise.

**NOT established — stated carefully because this is exactly where an
over-read would be costly:** this does **not** yet show that the Majorana
condition resolves C27's multiplicity-2 problem. That requires checking it
(a) against the actual zero-mode subspace `ker(D_full)` rather than the whole
module, and (b) for compatibility with `D_full` itself (a reality condition
must commute appropriately with the operator to be imposable on its kernel).
Both are a separate round — see Next gate.

**Also NOT affected:** the sub-claim that the *S³ factor alone* is
quaternionic stands independently — `Spin(3) = SU(2)`'s fundamental is
pseudo-real for `3 mod 8 = 3`, a convention-independent fact, and C31's
exhaustive search over antilinear structures on that 2-dim module remains
valid *for that factor*. What was wrong was propagating it to the 9-dim
product across a signature mismatch.

## What OB10 did genuinely contribute

Not the conclusion — the discovery. OB10 surfaced a **real latent
inconsistency**: two sub-projects had been carrying incompatible Clifford
conventions for months, and nothing had combined them until now. That is a
genuine finding with real downstream consequences (any future round tensoring
S³ and S⁶ constructions hits the same trap). It was simply misread as a
statement about geometry rather than about the codebase.

## How this was found

An external red-team audit (2026-08-09) challenged the result. Per this
project's own `audit-verification-gate.md`, its claims were treated as
hypotheses and checked here rather than accepted — all three of its
substantive claims verified. **Worth recording plainly: this error survived
its own experiment's internal checks, a full ledger entry, a `decision.md`
with an explicit "what this does NOT mean" section, and a merge. It was
caught only from outside.** The same session's own pearl — that self-checks
find the bugs they were designed to find and miss the ones they were not —
applies to this correction as much as to what prompted it.

## Next gate (ordered by information value)

1. **Does the Majorana condition actually halve `ker(D_full)`?** Check it on
   the zero-mode subspace, not the whole module, and verify compatibility with
   `D_full`. If yes, this closes C27 — a multi-round blocker.
2. **Audit every other place the two conventions could have been mixed.**
   OB10 was the first round to combine them; it should not be the last one to
   notice. A repo-wide check is warranted.
3. Re-examine whether `preprint.tex`'s KO-dimension-6 statements carry the
   same convention ambiguity (the audit flagged that KO labels are
   convention-dependent and should be stored as the full invariant tuple
   `(J², JDJ⁻¹/D, JγJ⁻¹/γ)` plus the Clifford sign convention, not as a bare
   "KO-dim 6").

## Check (reproduces this correction)

```
cd experiments/20260809-ob10-convention-correction
python convention_correction.py
```
Expect `VERDICT: OB10_CORRECTED__TYPE_IS_REAL__C31_INVERTED`, signature
`(6,3)` → `(0,9)`, type PSEUDO-REAL → REAL, Majorana solution dimension
`0` → `16`.
