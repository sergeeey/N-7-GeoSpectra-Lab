# G91 Decision — Full 4D Reduced Action

**Date:** 2026-06-24
**Verdict:** `CONSTRAINED_PHYSICAL_RATIO`
**Gates:** 6/6 PASS

---

## What was computed

Full 2D moduli-space analysis of V(ρ₃, ρ₆) for S³×S⁶ compactification,
closing three of four gaps from G88F.

---

## Key results

### 1. σ₃ (S³ radius) is a runaway direction [VERIFIED-bash]

```
V(ρ₃, ρ₆) = g(ρ₆) / (ω₃ ω₆ ρ₃³ ρ₆⁶)
=> ∂V/∂(ln ρ₃) = −3V
```

At the AdS minimum (V < 0): ∂V/∂(ln ρ₃) = +7.58×10⁻⁶ > 0
→ V increases as ρ₃ grows → ρ₃ runs to infinity.
**The S³ radius has no minimum in the current potential.**
Numerical agreement: analytic = 7.580592296×10⁻⁶, FD = 7.580592299×10⁻⁶ ✓

### 2. Frame independence: Ω² cancels exactly [VERIFIED-bash]

```
Ω² = ρ₃^N₃ · ρ₆^N₆ = ρ₆^12  (along path ρ₃ = ρ₆²)
m²_mod^E = m²_mod^s / Ω²
m²_KK^E  = m²_KK^s  / Ω²
```

Ratio string frame = 0.001978025700522417
Ratio Einstein frame = 0.001978025700522417
Relative difference = 0.0 (machine precision)
**The mass ratio is exactly frame-independent.**

### 3. Corrected ratio using verified KK spectra [VERIFIED-pytest, G4, G73]

At ρ₆_min = 1.1791 (same minimum as G62/G88A):

| KK source | m_KK | ratio |
|-----------|------|-------|
| G88A proxy (1/ρ₆) | 0.848 | 0.252% |
| S⁶ spectrum [G73] λ₀ = 3/ρ₆ | 2.544 | 0.084% |
| **S³ spectrum [G4] λ₀ = 3/(2ρ₃)** | **1.079** | **0.198%** |

**Lightest KK is from S³** (since ρ₃ = ρ₆² > ρ₆ at ρ₆ > 1).
Physical ratio: **m_mod/m_KK = 0.198%** (G88A was 0.252%, off by factor 0.786).

### 4. Modulus is well below KK threshold [VERIFIED-bash]

```
m_mod (string)  = 0.002134  (string units)
m_KK (S³, lightest) = 1.079
EFT hierarchy: m_mod/m_KK = 198:1
```

EFT is self-consistent (modulus ~500× below KK threshold in mass).

---

## What G88F said was missing → status

| G88F missing item | G91 status |
|---|---|
| Closed reduced 4D action chain | ✅ CLOSED: V(ρ₃,ρ₆) written, Ω explicit |
| Same-frame KK scale map | ✅ CLOSED: Ω cancels, ratio frame-independent |
| Normalization stack for physical ratio | ✅ CLOSED: verified KK eigenvalues from G4/G73 |
| Path constraint derivation | 🔴 OPEN: ρ₃=ρ₆² is still an assumption |

---

## Remaining open

**The path constraint ρ₃ = ρ₆² is an assumption, not derived.**

In the full 2D potential, σ₃ is a runaway direction. The constraint must come
from an external mechanism:
- Flux quantization on S³ (e.g., H₃ flux fixing ρ₃)
- Geometric coupling between spheres (UV completion)
- Tom's framework (his action may fix the ratio differently)

Until ρ₃ is independently stabilized, the verdict is CONSTRAINED (not UNCONDITIONAL).

---

## What this does NOT mean

- Does NOT identify M_s/M_Pl (physical units still require this map)
- Does NOT prove the path is a mass eigenstate of the full 2D Hessian
- Does NOT close the S³ stabilization problem
- The 0.198% ratio is within the current ansatz only

---

## Verdict interpretation

`CONSTRAINED_PHYSICAL_RATIO`: the ratio is physically meaningful and
frame-independent given the path constraint. It improves on G88A (proxy)
in two ways: (1) frame independence proved, (2) correct KK eigenvalue used.
The single remaining assumption is external stabilization of ρ₃.
