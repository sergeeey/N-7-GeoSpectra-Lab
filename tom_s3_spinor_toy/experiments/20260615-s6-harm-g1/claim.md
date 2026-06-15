# S6-HARM-G1: S⁶ Coordinates and Cartan Phase Structure

**Date:** 2026-06-15
**Gate:** G1 — координаты на S⁶ и фазовая структура (аналог Tom rows 11-14)
**Depends on:** G0 PASS (SO(6) Clifford + Cartan generators H₁,H₂,H₃ + weights ±½)

## Question type
Descriptive — зафиксировать координатную систему, проверить объём, идентифицировать
Картановы фазы.

## Physical motivation
Tom rows 11-14 на S³:
- Row 11: координаты x¹=ρsinαcosθ, x²=ρsinαsinθ, x³=ρcosαsinθ̃, x⁴=ρcosαcosθ̃  → мера sin(2α)dα
- Row 13: ∂_θ + ∂_θ̃ = Î_{3L},  ∂_θ - ∂_θ̃ = Î_{3R}
- Row 14: спинор имеет фазу exp(i[i_L(θ+θ̃)+i_R(θ-θ̃)])

Аналог на S⁶ с SO(6) rang=3 → 3 азимутальных угла (φ₁,φ₂,φ₃),
каждый соответствует одному Картанову генератору H_k = J_{2k-1,2k}.

## Parameterization (nested sphere)
S⁶ ⊂ ℝ⁷:

x¹ = ρ sinβ₁ cosφ₁          ⟩ пара для H₁=J₁₂
x² = ρ sinβ₁ sinφ₁          ⟩

x³ = ρ cosβ₁ sinβ₂ cosφ₂    ⟩ пара для H₂=J₃₄
x⁴ = ρ cosβ₁ sinβ₂ sinφ₂    ⟩

x⁵ = ρ cosβ₁ cosβ₂ sinβ₃ cosφ₃   ⟩ пара для H₃=J₅₆
x⁶ = ρ cosβ₁ cosβ₂ sinβ₃ sinφ₃   ⟩

x⁷ = ρ cosβ₁ cosβ₂ cosβ₃

Диапазоны: β₁,β₂ ∈ [0,π/2],  β₃ ∈ [0,π],  φ₁,φ₂,φ₃ ∈ [0,2π]

## Claim
1. Σᵢ(xⁱ)² = ρ² [constraint]
2. Индуцированная метрика на S⁶ диагональна:
   g_{β₁β₁}=ρ², g_{φ₁φ₁}=ρ²sin²β₁,
   g_{β₂β₂}=ρ²cos²β₁, g_{φ₂φ₂}=ρ²cos²β₁sin²β₂,
   g_{β₃β₃}=ρ²cos²β₁cos²β₂, g_{φ₃φ₃}=ρ²cos²β₁cos²β₂sin²β₃
3. Объём ∫√g dβ₁dφ₁dβ₂dφ₂dβ₃dφ₃ = (16π³/15)ρ⁶ = Vol(S⁶)
4. Карtan фазы: H_k действует на e^{im_kφ_k} → m_k ∈ {±½} (из G0)
5. 8 весовых векторов G0 реализуются как фазы e^{i(m₁φ₁+m₂φ₂+m₃φ₃)}

## What this does NOT mean
- Не доказывает что радиальная часть A(β₁,β₂,β₃) существует (это G2+)
- Не утверждает связь S³×S⁶ (не смешивать с Tom's S³ framework)
- Не фиксирует λ
- Не решает уравнение Дирака на S⁶

## Falsification
- Σ(xⁱ)² ≠ ρ² → FAIL
- Vol(S⁶) ≠ 16π³/15 ρ⁶ → FAIL
- m_k ∉ {±½} → FAIL (несогласованность с G0)
