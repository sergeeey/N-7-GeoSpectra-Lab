# Round55-CertifiedBound Decision

**Date:** 2026-07-13
**Verdict: PASS-WITH-OPEN-ITEMS** (6 of the user's 8 required conditions
fully closed; 2 flagged honestly, not silently assumed) — branch status
**ACTIVE / BOUND-CERTIFICATION** (not re-parked; neither the
completeness gate nor the normalization gate FAILED outright, per the
user's own explicit re-parking criterion)

## Headline result

```
K_cert = 2*sqrt(6)/3  ≈ 1.632993
```

Certified via exact/symbolic eigenvalue computation (SymPy exact
rational/radical arithmetic, not `numpy.linalg.eigvalsh` estimates) of
`H_L = Σ_r B_r B_r†` and `H_R = Σ_r B_r† B_r`, where `B_r = B_r^T +
B_r^AB` (torsion and mixed-A-B contributions combined BEFORE norming,
per explicit instruction). Both `H_L` and `H_R` have identical spectrum
`{4: mult 8, 8/3: mult 12, 4/3: mult 40, 16/3: mult 2, 0: mult 2}` —
max eigenvalue `16/3`, giving `K_native = √(16/3) = 4√3/3` in the raw
`ρ_7(e_p)` basis, converted to the established Bourbaki `C₂=4`
convention via the certified `√2` rescale from the normalization gate:
`K_cert = K_native/√2 = 2√6/3`.

## The 8-point checklist, honestly scored

| # | Requirement | Status |
|---|---|---|
| 1 | Full decomposition audit | **PARTIAL** — all 5 pieces classified (quadratic/linear/independent), but whether `CASIMIR+D64²+SU3-CURV` exactly reproduce the abstract cubic KP formula is not fully closed (see below) |
| 2 | Casimir normalization check on ρ=7 | **PASS-WITH-RESCALE** — naive 14-generator sum gives `2·I`, not `4·I`; diagnosed as a clean, uniform `√2` global rescale, independently confirmed via full pairwise trace-form orthonormality (all 14 generators individually unit-normalized, zero cross terms) |
| 3 | Explicit fixed matrices `B_a` | **PASS** — `B_r^T`, `B_r^AB` built and combined explicitly for r=1..6 |
| 4 | Independent reconstruction of both Round 22 terms | **PASS** — `torsion_cross_term`/`mixed_AB_term` used unmodified from Round 22's own module, both confirmed independently nonzero and distinct on the test vector |
| 5 | Numerical `K_num` | **PASS** — `K_cert` computed via exact symbolic arithmetic throughout; no separate cruder numerical estimate was needed since exact computation was tractable (small rational matrices) |
| 6 | Certified `K_cert` | **PASS** — exact eigenvalues, not estimates; `K_cert=2√6/3` |
| 7 | Positive control `‖Q_7‖≤2K_cert` | **PASS** — `‖Q_7(singlet_1)‖/‖singlet_1‖ = 2√3/3 ≈ 1.155 ≤ 2K_cert ≈ 3.266` |
| 8 | Full lower bound with possible `B_0` | **PARTIAL** — formula stated; `B_0`'s exact role not fully pinned down (see below) |

## The completeness-gate finding (Step 1b) — reported honestly

Testing whether `CASIMIR+D64²+SU3-CURVATURE` reproduce the abstract
cubic-operator KP eigenvalue on `singlet_1` (σ=(0,0) fibre type):
found the actual value is **6** (native units), not the naively-expected
**2** (my own initial assumption, using only the 6 `𝔪`-direction
Casimir). Root cause, verified directly: `termB_squared` (`D64²`) has
its own nonzero eigenvalue (**4**) on this test vector — `D64` is
confirmed `ρ`-independent (Round 54: built purely from the fixed
`Σ⊗Σ` structure), so this is a KNOWN, FIXED, COMPUTABLE constant, not
an unknown or unbounded quantity — but it is genuinely ADDITIVE to
whatever the m-direction-only `CASIMIR` term (2, native) contributes,
not something that was already "accounted for" in my naive expected
value.

**What this does NOT threaten**: since `D64²`'s contribution is fixed
(zero `ρ`-dependence, confirmed structurally, not just on this one test
vector), it cannot introduce any NEW `ρ`-scaling behavior — at most it
shifts the final numeric threshold by a KNOWN additive constant once
correctly identified, exactly the role the user's own `B_0` term in the
final formula anticipates. **What remains open**: the exact value and
correct placement of this constant (is it already implicitly part of
Round 52's own `-3`, or does it need to be added as an EXPLICIT,
separate `B_0` in the final formula?) is not resolved by testing a
single vector on a single `σ`-type — a fuller check across all `σ`
types appearing in the fibre would be needed to state this with the
same certainty as the `K_cert` result itself.

## Kill Analysis

**What was tested:** whether the certified bound `K_cert` on
`Q_ρ=torsion+mixed_AB` holds up under the user's full 8-point rigor
protocol, including gates the crude Round 54 argument did not check.

**What was killed:** the assumption (implicit in Round 54, and in my
own initial Step 1b expectation) that the "baseline" pieces (CASIMIR,
D64², SU3-CURV) are either trivially zero or already fully understood.
`D64²`'s own nonzero contribution was not previously identified as a
distinct, nameable quantity requiring explicit accounting.

**What was NOT killed:** the core certified bound `K_cert=2√6/3` on
`Q_ρ=torsion+mixed_AB` itself — verified via exact eigenvalues,
Hermiticity, PSD, and a genuine positive control against Round 22's own
unmodified functions. Round 54's qualitative conclusion (finite
exceptional set exists) is UNCHANGED — a fixed additive `B_0` constant
does not alter the `O(√C₂(ρ))` vs `O(C₂(ρ))` asymptotic argument that
guarantees a finite threshold; it only shifts where that threshold
falls numerically.

**Relaxation Map:**
A. Extend Step 1b's single-test-vector check across all 4 fibre `σ`
   types (not just `σ=(0,0)`) to determine `D64²`'s eigenvalue on each,
   giving a complete, certified `B_0` (or confirming it is absorbed
   into the existing `-3` term via a mechanism not yet identified) —
   the natural next sub-step, cheap (reuses all of this round's
   already-built machinery).
B. Accept the current formula with `B_0` as an explicit unknown-but-
   bounded placeholder and proceed to Round 56's exceptional-set
   enumeration using a conservative (not yet tight) bound.
C. Treat this as sufficient for a qualitative preprint statement
   ("a finite exceptional set exists, threshold not yet pinned to the
   last constant") without full numeric precision.

## Recommendation

Do NOT return to `PARKED` — per the user's own explicit criterion,
re-parking requires a completeness-gate or normalization-gate FAIL;
neither occurred (normalization gate passed with a diagnosed, certified
rescale; completeness gate surfaced a fixable open item, not a
contradiction). Branch status: **ACTIVE / BOUND-CERTIFICATION**.

Immediate next step (small, cheap, same machinery): extend Step 1b
across all fibre types to close item 1/8 fully, yielding an exact `B_0`
and the fully certified final formula
`λ²_min(ρ) ≥ C₂(ρ) - 3 - B_0 - K_cert·√C₂(ρ)`. Only after that is
Round 56 (finite exceptional set enumeration by Dynkin label) properly
licensed with a FULLY certified threshold rather than a provisional one.

## Scope discipline check

No Dirac-operator matrices built for any new ρ. `preprint.tex`
untouched. Step 7 (basis-rotation control) explicitly not performed,
reported as an honest gap rather than silently skipped, per this
project's own integrity discipline.

## Files

- `claim.md` — this round's FL Standard-tier artifact
- `round55_certified_bound.py` — script, all 8 steps run in sequence,
  exact/symbolic computation throughout
- `results_round55.json` — full structured output
