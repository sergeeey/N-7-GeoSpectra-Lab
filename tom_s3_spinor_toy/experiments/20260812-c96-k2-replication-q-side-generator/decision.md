# C96 decision — k=2 replication DIVERGES from k=1: C95's formula is k=1-specific

**Verdict:** `K2_REPLICATION_DIVERGES_FROM_K1__C95_FORMULA_IS_K_SPECIFIC`
**Status:** RESOLVED (two genuine bugs found+fixed in this round's own construction,
then a clean, bracket-consistent, informative result obtained)

---

## Summary

C95 found, at `k=1` (the defining/self-conjugate representation): `L_i =
+l_{e_i}(1)` directly, `R_i = -l_{e_i}(1)^T`. This round tested whether
that exact formula generalizes to `k=2` (spin-1), as the reviewer's own
original proposal required before trusting it.

**It does not, in the specific form found at k=1.** After fixing two
genuine bugs in this round's own script (both self-caught, both fixed
before drawing any conclusion, per this round's own kill_criterion),
the clean result is:

```
k=1 (C95):  L_i = +l_{e_i}(1)         R_i = -l_{e_i}(1)^T
k=2 (C96):  L_i = -l_{e_i}(2)^T       R_i = +l_{e_i}(2)
```

**The L/R roles are exactly swapped between k=1 and k=2** — both are
individually valid, bracket-consistent generators (`[L1,L2]=2L3` and
`[R1,R2]=2R3` both hold exactly, verified symbolically), and the
calibration (P0: does R match a certified `l_{e_i}(2)` candidate
uniformly, with the bracket holding) cleanly succeeds — just not to the
specific candidate label (`-lT`) predicted in `claim.md`, matching
`+l` instead.

## Predictions vs outcome

| # | Prediction (claim.md) | Outcome |
|---|---|---|
| P0 (calibration) | `R_i(k=2)` matches `-l_{e_i}(2)^T` uniformly | **Miss on the specific label** — matches `+l` uniformly instead. Calibration criterion itself (uniform match to ONE candidate + bracket holds) **PASSES**. |
| P1 | `L_i(k=2)` matches `+l_{e_i}(2)` directly | **FAILS** — matches `-l_{e_i}(2)^T` instead (the role R held at k=1). |
| P2 | both brackets hold exactly at k=2 | **HOLDS** — `[L1,L2]=2L3` and `[R1,R2]=2R3` both verified symbolically. |

Per this round's own pre-registered kill_criterion: *"If P0 holds but
P1 fails, C95's `L_i=+l_{e_i}` formula is k=1-specific... would mean
the multiplication-operator build needs a k-dependent formula, not a
single fixed rule."* — this is exactly the outcome. A real, useful,
narrowing finding, not a null result.

## Two genuine bugs found and fixed in THIS round's own script (not C95's)

### Bug 1 — abstract-vs-concrete symbol conflation (all-zero generators)

First full run produced all-zero `L_op`/`R_op` for every unit, with
`[L1,L2]==2L3` trivially `True` (0=0) — a textbook case of a bracket
check passing vacuously. Root cause: `coefficient_space_generator_general`
was called with `D2_generic` (an explicit polynomial function of `a,b`)
as the "abstract D matrix," instead of a set of independent free
symbols matching C95's own `g00,g01,g10,g11` convention. After
`sp.expand`, the compound polynomial entries of `D2_generic` no longer
appear as recognizable generators, so `Poly.coeff_monomial` silently
returned 0 for every coefficient. **Fixed** by introducing `D_sym`, a
genuinely abstract `3x3` matrix of free symbols, and passing that (not
`D2_generic`) into the coefficient-extraction step — the group-action
generator `X3x3` (correctly computed by differentiating the real,
nonlinear `D2_h(a(eps),b(eps))`) still acts on `D_sym` via ordinary
matrix multiplication, exactly mirroring C95's `g`/`X` split.

### Bug 2 — `build_d2_matrix` was an anti-homomorphism (more serious)

After fixing Bug 1, P0 uniformly matched `-l` (not `-lT`) and P2's
brackets failed for BOTH `L` and `R`. Traced this via a pure
Lie-algebra argument (verified by direct computation, not assumed):
given any `l_i` satisfying `[l1,l2]=2l3`, only the candidates `+l_i`
and `-l_i^T` can ever satisfy `[R1,R2]=2R3` — `-l_i` and `+l_i^T` are
**algebraically guaranteed to fail** that bracket (a basis-independent
fact, not specific to this construction). Since my computed `L_op`,
`R_op` matched exactly `+l^T` and `-l` (both in the "guaranteed-fail"
class), and this was an *exact* symbolic match (not a numerical
near-miss), the bug had to be upstream of the coefficient extraction —
in `build_d2_matrix` itself.

Directly tested `build_d2_matrix` for the group-homomorphism property
`D(g1)*D(g2) =? D(g1*g2)` using two independent symbolic `SU(2)`
elements: **it failed** — instead `D(g1)*D(g2) = D(g2*g1)`, an
**anti-homomorphism** (composition order reversed). This is the classic
pullback-vs-pushforward trap: literally substituting the transformed
variables `v0->a*v0+b*v1` into a monomial and reading off coefficients
in the *original* `v0,v1` computes the **pullback/dual** action, which
composes in reverse order by construction, not the ordinary (pushforward)
representation.

**Fixed** via the standard remedy: a genuine order-preserving
representation is recovered as `D_correct(g) := D_raw(g^{-1})`. For
`g=[[a,b],[-conj(b),conj(a)]]` in `SU(2)`, `g^{-1}` has `(A,B) =
(conj(a), -b)` in the same parametrization. Verified directly: `D_raw(
conj(a1),-b1) * D_raw(conj(a2),-b2) = D_raw(conj(a1*a2's own g-product
entries))` matches `D(g1*g2)` exactly for two independent symbolic
`SU(2)` elements (both composition orders checked). Confirmed that
`X1,X2,X3` (3x3) built from the corrected `D` now satisfy their own
`[X1,X2]=2X3` (previously failed: residual
`[[0,-4I,0],[-8I,0,-8I],[0,-4I,0]]`, nonzero).

**Why this bug did not, and could not, occur in C95's own k=1
construction:** at `k=1`, `D^{(1)}(g):=g` is used directly (the
identity map on the defining representation), which is trivially a
genuine homomorphism (`D(g1)D(g2)=g1g2=D(g1g2)` by definition — no
substitution trick, no possibility of a pullback/pushforward sign
error). The anti-homomorphism bug is specific to the polynomial/
monomial-substitution construction needed to build `D^{(2)}`, which
simply did not exist as a code path at `k=1`. This is exactly the kind
of `k=1`-degenerate blind spot this round's own `claim.md` flagged as
the reason `k=2` replication was needed in the first place.

### Basis-normalization note (a third, smaller correction, en route)

An intermediate draft of `build_d2_matrix` also applied a
`S=diag(1,1/sqrt(2),1)` similarity transform to force unitarity
(`D^dagger @ D == I`), on an unstated assumption that "unitary" was
the right convention. Checking C85's own `l_{e_i}(2)` matrices directly
showed they are **not** anti-Hermitian in their own `|p>` basis (e.g.
`l2[0,1]=1` but `l2[1,0]=-2`) — i.e. C85 already uses the RAW,
non-unitary monomial basis. The `S`-transform was removed so this
round's basis matches C85's own convention (a Lie-algebra
representation need not be unitary, only bracket-consistent).

## What survives, what doesn't

- **Survives:** C85's own `l_{e_i}(2)` matrices are unaffected — this
  round found bugs in C96's own new construction, not in C85 or C95.
- **Survives:** C95's k=1 result (`L=+l`, `R=-l^T`) is unaffected —
  verified to be structurally impossible for the anti-homomorphism bug
  to have occurred there (see above).
- **Does NOT survive:** the assumption that C95's exact formula
  (`L_i=+l_{e_i}(k)` directly, for any `k`) is a single fixed rule.
  It is **k=1-specific**. At k=2 the roles swap: `L_i=-l_{e_i}(2)^T`,
  `R_i=+l_{e_i}(2)`.
- **Open, not resolved by this round:** WHY do the roles swap between
  k=1 and k=2? Is there a clean k-dependent rule (e.g. alternating by
  parity of k, or governed by a specific normalization/orientation
  fact about the symmetric-power construction), or is k=2 itself just
  another data point requiring a k=3 check before any pattern can be
  trusted? This round deliberately does not speculate further — the
  next-cheapest test (per this round's own `kill_criterion`) would be
  a k=3 replication using the SAME (now-debugged) construction.

## kill_criterion (from claim.md, evaluated)

> "If P0 holds but P1 fails, C95's `L_i=+l_{e_i}` formula is
> `k=1`-specific (a real, useful, narrowing finding -- would mean the
> multiplication-operator build needs a `k`-dependent formula, not a
> single fixed rule)."

This is exactly what happened. **The multiplication-operator build
(task #59, C90's reviewer-proposed next step) must NOT assume a single
fixed q-side generator formula across Peter-Weyl levels** — it needs
either a k-dependent rule (not yet known) or per-level certification.

## What this cannot show

- Does not test `k>=3` — a genuine open question, not implied by this
  result either way.
- Does not build the multiplication operator itself.
- Does not change `N_gen=3`'s CONDITIONAL status.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## Verification

- `ruff check experiments/20260812-c96-k2-replication-q-side-generator/`
  — clean, 0 errors.
- Full suite: `python -m pytest tests/ -q --tb=short` — 2512 passed,
  4 skipped, 0 failed.
- `build_d2_matrix`'s homomorphism property verified directly
  (`D(g1)*D(g2) == D(g1*g2)` for two independent symbolic SU(2)
  elements, both orders), not merely assumed from the bracket check
  passing downstream.
- `[X1,X2]=2X3` verified directly for the 3x3 group-action generators
  themselves (not just the derived L_op/R_op), confirming the fix
  operates at the correct layer.
- All candidate matches (`L_match`, `R_match` per unit) are EXACT
  symbolic equalities (`sp.simplify(...) == sp.zeros(3,3)`), not
  numerical near-matches.
