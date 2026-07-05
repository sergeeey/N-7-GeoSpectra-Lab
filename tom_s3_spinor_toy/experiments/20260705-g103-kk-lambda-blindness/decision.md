# G103 Decision — KK-Spectrum Lambda-Blindness + Closure of the λ-UV-Derivation Branch

**Verdict: PROMOTE (G103 consistency PASS 5/5) + REJECT the branch "derive λ_np from standard 10D mechanisms" (→ null_results) + PARK the R⁴-saddle loophole (→ parked)**

## G103 results [VERIFIED — results_g103.json, `python g103_kk_lambda_blindness.py`]

| Check | Result | Threshold | Status |
|---|---|---|---|
| (S) symbolic λ-blindness of KK tower | no λ_np in free_symbols | exact | ✅ |
| (I) indirect KK spread over λ∈[0.15,0.60] | **0.4076%** | ≤ 0.5% (kill > 1%) | ✅ |
| (M) modulus exponent d ln m_mod/d ln λ | **0.4928** | ∈ [0.40,0.60] (kill ∉ [0.30,0.70]) | ✅ |
| (P) positive control (GA1 ref at λ=1/3) | ρ₆_min=1.1791, ratio=0.1978% | ±0.002 / ±0.02 | ✅ |
| (N) negative control (fake λ-tower) | 17.47% — caught | must violate (I) | ✅ |

**Observable split established:** the geometric sector (KK tower) cannot fix λ_np —
its total λ-sensitivity is ≤0.41% over a 4× range; λ_np is nonetheless measurable,
in exactly one place: the modulus sector (m_mod ∝ λ^0.493, V_min ∝ λ per H1).

## Kill Analysis — branch "λ_np derived from standard 10D non-perturbative sources"

**What was killed** (mechanism sweep, session 2026-07-05; scalings verified by inspection):

| Source class | Instanton action scaling | Killer |
|---|---|---|
| Euclidean branes wrapping cycles of S⁶ | only Vol(S⁶) ~ ρ₆⁶ available | H_p(S⁶)=0 for 0<p<6 (χ-lemma G50 + standard) |
| Gaugino condensation / 4D gauge instantons | 1/g₄² ∝ ∫√g₆ ~ ρ₆⁶ → exp(−c·ρ₆⁶) | positive power (note: external draft's `exp(−c/ρ₆⁶)` was a typo — corrected here) |
| Worldline instantons | S ~ m·L ~ ρ₆ → exp(−c·ρ₆) | positive power |
| Borel/resurgence of α′-series | exp(−c·ρ₆²/α′) — opposite sign; small-radius series diverges at ρ_min (α′ρ₆²≈1.39>1) | wrong sign + wrong expansion regime |
| Non-geometric fluxes (Q,R,P) | polynomial in moduli | no NP exponential at all |

Plus five numerology attempts rejected during the session (π/9, 1/3 dim-split, K-theory n/3,
λ=3W₀ direct KKLT, \|V_AdS\|=4/(N(N+2))): each fitted to the target, none derived; the last
also contradicts G62 scale by ×10⁵ [VERIFIED-python].

**What was NOT killed:**
1. **R⁴ gravitational saddle**: ∫√g·R⁴ ~ ρ₆⁻² [VERIFIED-arithmetic] — the only candidate with
   the correct power law → **parked** with explicit revival condition (see parked/).
2. **Two-modulus emergent form** (T_eff ∝ 1/ρ₆² after integrating out X): with unconstrained
   B(T,X) this is unfalsifiable (AOG-2); revivable only with B constrained by SU(3) torsion classes.
3. **Non-standard UV** (nonlocal/resummed determinant sectors beyond the 10D class) — outside
   the class by construction; the no-go is conditional on the class.

**Relaxation Map:** the only single-assumption relaxations that reopen the branch are
(i) admit R⁴ as a genuine Euclidean saddle [parked, cheapest test defined],
(ii) admit a second light modulus with torsion-constrained coupling [needs Tom-framework input].

## Relation to prior internal results
- G83–G86B: λ-map EXHAUSTED (internal 4D scan) — today's sweep is the independent UV-side closure.
- META-C1 (dimensional obstruction) is recorded PROMOTE in null_results/INDEX but was
  **falsified by the 2026-06-23 audit** (mislabeled trajectory ρ₃=κρ₆ vs canonical ρ₃=ρ₆²);
  the standing closure therefore rests on G83–G86B + this sweep, NOT on C1.
- GA1: ρ₆_min ultra-stability (<0.3%) — G103 (I) is its observable-level corollary, now with
  controls and a pre-registered kill criterion.

## Skeptic (FL Step 8a) — [SKEPTIC-PRE-ANSWERED]
1. *Circularity: a_np(λ) is anchored at ρ\* by construction, so isn't blindness built in?*
   → No: (I) measures the dynamic ρ₆_min drift, not the anchor; the negative control shows the
   criterion CAN fail (17.47% ≫ 0.5%). Blindness is a measured property, not an assumption.
2. *Thresholds arbitrary?* → Pre-registered in claim.md before the run; PASS=0.5% is tied to the
   GA1-measured drift (≈2×0.2% via ρ₃=ρ₆²); KILL=1% is the falsification bound.
3. *m_mod ∝ √λ an artifact of PATH_K normalization?* → PATH_K is a λ-independent constant and
   cancels in the log-log slope.
4. *Sweep range too narrow?* → [0.15, 0.60] covers all candidate values proposed to date
   (1/3, π/9≈0.349, 0.337); outside-range behavior explicitly out of scope (claim.md).

## Caveats
- All numbers are per the canonical G91 path (ρ₃=ρ₆², C_SM=0.986); other trajectories require re-run.
- The no-go is **conditional**: class = standard 10D NP sources. It does NOT claim λ_np is
  underivable in every conceivable UV completion.
- `lambda_np = FREE_COUPLING_PARAMETER` remains the project hard constraint — G103 localizes
  where it is observable (m_mod, V_min), which is a falsifiable statement about FUTURE proposals:
  any λ-fixing mechanism that leaves the modulus sector untouched is inconsistent with this model.

## Pearl Gate
→ observable-split pearl added to pearl_registry/INDEX.md (next_check 2026-08-05).
