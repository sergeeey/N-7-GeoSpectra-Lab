# S6-HARM-G2: Root Generators in Coordinates — cotβ_k Structure

**Date:** 2026-06-15
**Gate:** G2 — root generators SO(6) в координатах (аналог Tom row 13+15)
**Depends on:** G1 PASS (nested sphere, diagonal metric, g^{kk} known)

## Physical motivation
Tom rows 13, 15 на S³:
- Row 13: ∂_θ + ∂_θ̃ = Î_{3L} (Cartan = чистый азимутальный оператор)
- Row 15: "Sounds right" — cot(2α) = Hopf-frame артефакт, не физический

Вопрос для S⁶: какова форма корневых (лестничных) генераторов SO(6)
в координатах вложенной сферы? Предсказание: появятся члены с cotβ_k.

## Formula for Killing vectors
L_{ij} = x^i ∂_{x^j} - x^j ∂_{x^i} (Killing вектора SO(7) на S⁶)

В координатах (q^k = β₁,φ₁,β₂,φ₂,β₃,φ₃):

L_{ij} = Σ_k  c_k^{ij}  ∂_{q^k}

где коэффициент:
c_k^{ij} = g^{kk} × [ x^i × (∂x^j/∂q^k) − x^j × (∂x^i/∂q^k) ]

(используется диагональная метрика из G1: g^{kk} = 1/g_{kk})

## Claim

### Картановы генераторы (чистый азимутальный оператор)
- L₁₂ = ∂_{φ₁}   (all c_k = 0 except c_{φ₁} = 1)
- L₃₄ = ∂_{φ₂}
- L₅₆ = ∂_{φ₃}

### Корневые генераторы — cotβ_k структура
- L₁₃: c_{φ₁} = cotβ₁ × sinβ₂ cosφ₂ sinφ₁   [cotβ₁ артефакт фрейма]
- L₃₅: c_{φ₂} = cotβ₂ × sinβ₃ cosφ₃ sinφ₂   [cotβ₂ артефакт фрейма]
- L₁₅: c_{φ₁} = cotβ₁ × cosβ₂ sinβ₃ cosφ₃ sinφ₁  [cotβ₁ через β₂ уровень]

### Иерархия котангенсов
- L_{1j}, L_{2j} для j=3,...,6: cotβ₁ в φ₁-коэффициенте
- L_{3j}, L_{4j} для j=5,6: cotβ₂ в φ₂-коэффициенте
- Нет дальних связей: L₁₃ не содержит φ₃, β₃ членов

Аналог Tom row 15: cot(2α) на S³ → cotβ_k на S⁶
(координатный артефакт, не физический)

## What this does NOT mean
- Не доказывает что spinor harmonic equation решается
- Не фиксирует λ
- Не утверждает что котангенсы исчезают в физической наблюдаемой

## Falsification
- L₁₂ ≠ ∂_{φ₁} → FAIL
- c_{φ₁}^{13} ≠ cotβ₁ × sinβ₂ cosφ₂ sinφ₁ → FAIL
