# Decision: G85B — Spectral Saddle / Worldline Resummation

**Date:** 2026-06-22
**Verdict:** NULL — saddle exists, bridge missing (same conclusion as G85A via different language)

---

## Claim

Spectral saddle point in proper-time integral ∫₀^∞ dt K(t,ρ₆) gives
the final bridge to A·exp(−λ_np/ρ₆²).

**Falsifier:** find t* where ∂K/∂t=0 at ρ₆≈1.090.
PASS: t* exists and K(t*)>0. FAIL: integrand monotonic.

---

## Gate Results (4/4 gates run)

| Gate | Test | Result |
|------|------|--------|
| G1 | K(t) monotonicity | NOT monotonic (1 sign change from zero modes → IR plateau) |
| G2 | Poisson-resummed saddle | t* = ρ₆²/3 = 0.3960 EXISTS, f(t*)=1.34>0 ✓ |
| G3 | ρ₆-dependence at saddle | f(t*) ~ ρ₆⁰·exp(−3) = **CONSTANT** (λ_fit = 0.0000) |
| G4 | K(t)/t effective action integrand | Monotonically decreasing — no interior saddle |

**Technical PASS / Physical NULL:**
- Falsifier condition (t* exists, K(t*)>0): **PASS** ✓
- Bridge to exp(−λ/ρ₆²): **MISSING** ✗

---

## What Happened

The Poisson-resummed heat kernel f(t) = (ρ₆²/t)³·exp(−ρ₆²/t) has a saddle at:

```
t* = ρ₆²/3  [analytically exact: df/dt = 0 ⟹ -3 + ρ₆²/t = 0]
```

At the saddle, the exponential factor evaluates to:
```
exp(−ρ₆²/t*) = exp(−ρ₆²/(ρ₆²/3)) = exp(−3) ≈ 0.0498 = CONSTANT
```

The ρ₆-dependence at t* is polynomial (ρ₆⁰), not exponential. Specifically:
```
f(t*) = (ρ₆²/(ρ₆²/3))³ · exp(−3) = 27·exp(−3) ≈ 1.34  [ρ₆-independent!]
```

The required form exp(−λ/ρ₆²) would need the exponential to grow as 1/ρ₆² → ∞ as ρ₆→0.
The saddle gives a constant instead.

**Root cause:** At t*=ρ₆²/3, the combination ρ₆²/t* = 3 always, regardless of ρ₆.
The saddle tracks ρ₆ exactly — the exponential factor is locked at exp(−3).

---

## Kill Analysis

**Killed:** "spectral/worldline saddle mechanism produces exp(−λ/ρ₆²)"

Two independent routes checked:
1. Direct heat kernel K(t): no saddle in K(t)/t (G4 — monotone)
2. Poisson-resummed: saddle exists but evaluates to a ρ₆-independent constant (G3)

**G85B = G85A restated:** G85A found the Poisson/theta form exists, bridge missing.
G85B found the saddle exists, bridge still missing. Different method, same barrier.

**What was NOT killed:**
1. **t* = ρ₆²/3 is real** — a genuine characteristic timescale of S⁶ ("modular temperature")
2. **G86A route** (dual-modulus: T(ρ₆) ∝ ρ₆^α with α≠6) — different mechanism, untested
3. **G86B route** (warp factor Ω(y)) — different mechanism, untested
4. **The non-perturbative factor itself** — exp(−λ/ρ₆²) may still arise from a non-spectral mechanism (brane instantons, gaugino condensation)

---

## Pearl [CANDIDATE]

**Observation:** t* = ρ₆²/3 is a ρ₆-covariant saddle — it scales with the internal geometry.

**Falsifiable prediction:** If S⁶ has a "modular temperature" T_mod = 1/(2πt*) = 3/(2πρ₆²),
this could fix a thermal contribution to the Casimir effective potential.

**Trigger:** Revival if G86A/B also fail → then modular temperature becomes the only
remaining geometric scale in the problem.

**next_check:** 2026-07-22 (after G86A/B verdict)

---

## Impact on λ-map

```
CLOSED routes:
  G85A: Poisson/theta resummation — form exists, bridge missing
  G85B: Spectral saddle — saddle exists, bridge missing (this gate)

OPEN routes:
  G86A: Dual-modulus T(ρ₆)∝ρ₆^α
  G86B: Warp factor Ω(y) compensation
```
