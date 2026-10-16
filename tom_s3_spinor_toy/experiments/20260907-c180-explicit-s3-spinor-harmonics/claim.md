# C180 — Claim

**Experiment ID:** `20260907-c180-explicit-s3-spinor-harmonics`
**Parent:** items 2+3 of the 5-item plan responding to Tom Lawrence's
2026-09-07 request (§3.3 italic: *"harmonics of S³ that form a basis for a
four-component spinor"*). Direct successor to C179, which established that
this cannot be done with a multiplet of ordinary functions carrying an
`SO(4)` representation, and named the route that does work: `S³` is
parallelizable, so in the group (left-invariant) trivialization spinor
fields ARE `C⁴`-valued functions — carrying a `Spin(4)` representation,
not an `SO(4)` one.

## Step -5: Zero-Signal Gate

- **Entity:** (a) the four vector harmonics `|φ_i⟩ = x_i/r` on `S³ ⊂ ℝ⁴`;
  (b) the operator `D₀ = −i Σ_a σ_a X_a^R` acting on `C²`-valued functions
  on `S³ = SU(2)`, where `X_a^R` are the explicit right-invariant vector
  fields of the quaternion group structure; (c) its eigenspaces at each
  harmonic level `k`.
- **Falsifiable predicate:** (i) does Tom's eq (77) hold for the `S³`
  VECTOR multiplet with his own convention `Γ_d = −T` (the `n=3`
  extension of the `S²` case he verified himself in his §3.2)? (ii) does
  `D₀` split each level-`k` space into exactly two eigenspaces with
  multiplicities `(k+1)(k+2)` and `k(k+1)`, matching this project's own
  already-established `S³` Dirac degeneracy `(n+1)(n+2)` (round67,
  `reference_spinor_harmonics.py`, `c85_certification.py`)?
- **Measurable outcome:** symbolic verification of eq (77) for (i);
  explicit construction and numerical diagonalization for (ii), with
  eigenvalues and multiplicities reported per level `k = 0,1,2,3`; plus
  the explicit lowest harmonics written out as formulas.

## Step -2/-1 (EstimandOps L0)

**Question type: Descriptive.** Do explicitly-constructed objects have
specific, pre-stated algebraic properties (satisfying an equation;
having a specific eigenvalue-multiplicity pattern) — not causal.

## Honest scope, stated BEFORE computing

1. **The `S³` Dirac spectrum is already established in this project**
   (round67: `σ(n+3/2)`, multiplicity `(n+1)(n+2)`; independently in
   `c85_certification.py` via Peter–Weyl). This round does NOT re-derive
   it as a new result; it uses it as the **reference the new explicit
   construction must reproduce**. If the construction reproduces it, that
   is a consistency check, not a discovery — stated up front per this
   project's own "forced not discovered" discipline.
2. **The overall additive constant is a connection convention.** `D₀` as
   defined here contains no spin-connection constant; the physical Dirac
   operator differs by an additive shift. This round therefore tests the
   **convention-independent** content — the two-branch structure and the
   multiplicities — and reports the raw computed eigenvalues without
   tuning any constant to match a target.
3. This round covers items 2–3 only. Item 4 (his `ψψ†` → gamma → vector
   check) and item 5 (Riemann normal coordinates) are a separate round.

## Kill-criterion table (frozen before running the script)

| Verdict | Condition |
|---|---|
| `BOTH-CONFIRMED` | (i) eq (77) verifies exactly for the `S³` vector multiplet under his stated convention and FAILS under the transpose/sign variants (same discrimination as C179's control A), AND (ii) `D₀` gives exactly two eigenvalues per level with multiplicities `(k+1)(k+2)` and `k(k+1)` for all `k` tested. |
| `VECTOR-OK-SPINOR-FAILS` | (i) passes but (ii) does not reproduce the established multiplicities — the trivialization construction is wrong somewhere and must be fixed before anything is claimed. |
| `VECTOR-FAILS` | (i) fails — our reading of Tom's conventions does not extend from `n=2` to `n=3`, which would undermine C179's transferability too and must be resolved first. |
| `SUBSTRATE-MISMATCH` | The quaternion vector fields do not close into `su(2)⊕su(2)`, or do not span the same `so(4)` as the coordinate rotations `x_i∂_j − x_j∂_i`, or `D₀` is not Hermitian — construction untrustworthy, no verdict. |

**Pre-registered expectation:** `BOTH-CONFIRMED`. Reasoning stated in
advance: eq (77) is dimension-agnostic in its derivation (Tom's §1.4 is
written for general `n`), so (i) should extend; and the coupling
`k/2 ⊗ ½ = (k+1)/2 ⊕ (k−1)/2` predicts exactly two branches with
multiplicities `(k+1)(k+2)` and `k(k+1)`, which is where round67's own
`(n+1)(n+2)` comes from. **A `VECTOR-OK-SPINOR-FAILS` outcome would mean
the explicit trivialization construction is wrong**, which matters more
than the eigenvalues themselves — it is the object Tom actually asked for.

## AI-Hypothesis Pre-Gates (Steps -4/-3)

- **Source Trace:** Tom's PDF (§1.4 eq 77, §2.1 eq 83/89, §3.2) read
  directly. Reference spectrum from this project's own round67
  (`[VERIFIED-tool]`) and `reference_spinor_harmonics.py:22-44`
  (Camporesi–Higuchi 1996 eq 3.25, marked VERIFIED_FROM_PDF).
- **Novelty Check:** the repo inventory run this session found **no file
  constructing explicit `S³` spinor harmonics as a multiplet** —
  `reference_spinor_harmonics.py` has the radial factor only,
  `c85_certification.py` has the operator at Peter–Weyl level but not
  assembled kets, round67 has the spectrum. Assembling them explicitly
  and checking eq (77) on them is new to this repo.

## What this does NOT mean (pre-registered)

1. Reproducing the known multiplicities is a CONSISTENCY CHECK on the new
   construction, not independent confirmation of the spectrum.
2. Does NOT address `S²` spinor harmonics (C179's Relaxation Map argues
   `S²` should be obtained by descent from `S³`, not independently).
3. Does NOT change `N_gen=3`'s CONDITIONAL status or any open blocker.
4. Does NOT constitute a submission to Tom (Submission Gate separate).
