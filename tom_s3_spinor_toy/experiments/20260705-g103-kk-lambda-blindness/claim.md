# G103 Claim — KK-Spectrum Lambda-Blindness (final consistency brick of the lambda no-go)

**Question type:** descriptive (structural/computational; domain = mathematical per sci-evidence Domain Gate)

**Entity:** the canonical G91-path potential V(ρ₆) = (V_FLUX − A_np·exp(−λ_np/ρ₆²))/Vol(ρ₆) on S³×S⁶
with its KK tower (S³: m=1.5/ρ₃, S⁶: m=3/ρ₆; ρ₃=ρ₆²) and radial-modulus mass m_mod.

**Falsifiable predicate:** the geometric KK tower is λ_np-blind (direct symbolic dependence = 0;
indirect dependence via ρ₆_min drift ≤ 0.5% over λ_np ∈ [0.15, 0.60]), while the modulus sector
carries λ_np with exponent p = d ln m_mod / d ln λ_np ∈ [0.40, 0.60] (H1 √λ scaling).

**Measurable outcome:** PASS/FAIL per five checks (S/I/M + positive/negative control) in
`results_g103.json`, reproducible via `python g103_kk_lambda_blindness.py`.

**Claim:** λ_np is orthogonal to the geometric sector: no observable built from the KK tower
can fix λ_np (spread ≤ 0.5%), and λ_np is nonetheless observable in exactly one place —
the modulus sector (m_mod ∝ √λ_np, V_min ∝ λ_np). This is the observable-level content of
"λ_np = FREE_COUPLING_PARAMETER" (LAMBDA-B5-G4) and closes the UV-derivation branch swept
in session 2026-07-05 (5 mechanism classes, all giving positive powers of ρ₆ in instanton actions).

**Natural language statement:**
We estimate the spread of the lightest KK mass and the scaling exponent of m_mod
for the S³×S⁶ compactification, comparing λ_np = 0.15 vs 0.60 under the same GA1/G91
canonical-radion formalism, to verify that geometry is λ-blind while dynamics is λ-sensitive.

**Kill criterion:**
- If KK spread over λ_np ∈ [0.15, 0.60] exceeds 1% → geometry secretly depends on λ_np →
  the free-parameter picture AND the no-go closure are BLOCKED (this experiment REJECTs itself).
- If p ∉ [0.30, 0.70] → H1 √λ scaling is wrong → modulus-sector observability claim falls.
- If the negative control (injected fake λ-dependent tower) is NOT caught → the test has no
  discriminating power → result void regardless of other checks.

**Controls:**
- Positive: reproduce GA1 reference at λ_np = 1/3: ρ₆_min = 1.1791 ± 0.002, ratio = 0.198% ± 0.02.
- Negative: inject m_KK_fake = m_KK·√(1+λ_np); blindness criterion must FAIL on it.

**What this does NOT mean:**
1. Does NOT prove λ_np is underivable in every UV completion — only that no standard 10D
   mechanism produces exp(−λ/ρ₆²) (R⁴ Euclidean-saddle loophole remains open → parked).
2. Does NOT fix λ_np — it remains free; it only localizes where λ_np is measurable (m_mod, V_min).
3. Does NOT apply outside λ_np ∈ [0.15, 0.60] without a separate check.
