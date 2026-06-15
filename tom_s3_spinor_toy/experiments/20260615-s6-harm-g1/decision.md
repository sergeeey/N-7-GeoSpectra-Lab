# S6-HARM-G1 — Decision

**Date:** 2026-06-15
**Verdict:** PROMOTE
**Status:** PASS_S6_COORDINATES_CARTAN_PHASES_CONFIRMED

## Evidence
- T1: Σ(xⁱ)² = ρ² — координатный constraint PASS [VERIFIED-sympy]
- T2: Метрика диагональна, все 6 компонент правильны PASS [VERIFIED-sympy]
- T2c: det(g) = ρ¹² sin²β₁ cos⁸β₁ sin²β₂ cos⁴β₂ sin²β₃ PASS [VERIFIED-sympy]
- T3: Vol(S⁶) = 16π³/15 × ρ⁶ (I₁=1/5, I₂=1/3, I₃=2) PASS [VERIFIED-sympy]
- T4: −i∂_{φ_k} e^{im_kφ_k} = m_k,  m_k = ±½ PASS [VERIFIED-sympy]
- T5: 8 весовых векторов (4⊕4̄ из G0) — все ±½, правильная чётность, нет дублей PASS
- 10/10 pytest тестов зелёных [VERIFIED-pytest 2026-06-15, 1.95s]
- Полный тест-сьют: 453 passed, 2 skipped [VERIFIED-pytest 2026-06-15]

## Coordinate system (pinned)
```
x¹ = ρ sinβ₁ cosφ₁          H₁=J₁₂ ↔ φ₁
x² = ρ sinβ₁ sinφ₁
x³ = ρ cosβ₁ sinβ₂ cosφ₂    H₂=J₃₄ ↔ φ₂
x⁴ = ρ cosβ₁ sinβ₂ sinφ₂
x⁵ = ρ cosβ₁ cosβ₂ sinβ₃ cosφ₃   H₃=J₅₆ ↔ φ₃
x⁶ = ρ cosβ₁ cosβ₂ sinβ₃ sinφ₃
x⁷ = ρ cosβ₁ cosβ₂ cosβ₃

β₁,β₂ ∈ [0,π/2]   β₃ ∈ [0,π]   φ₁,φ₂,φ₃ ∈ [0,2π]
√det(g) = ρ⁶ sinβ₁ cos⁴β₁ sinβ₂ cos²β₂ sinβ₃
```

## Cartan phase structure (S⁶ analog of Tom row 14)
Spinor на S⁶ в Картановом секторе:
  ψⱼ(β,φ) = Aⱼ(β₁,β₂,β₃) × exp(i(m₁ʲφ₁ + m₂ʲφ₂ + m₃ʲφ₃))

4-rep веса (m₁,m₂,m₃):
  (+½,+½,+½),  (+½,−½,−½),  (−½,+½,−½),  (−½,−½,+½)

4̄-rep веса:
  (−½,−½,−½),  (−½,+½,+½),  (+½,−½,+½),  (+½,+½,−½)

Аналог Tom row 14: e^{i(m₁φ₁+m₂φ₂+m₃φ₃)} ← exp(i[i_L(θ+θ̃)+i_R(θ-θ̃)])

Ключевая деталь β₃ ∈ [0,π]: innermost сфера = S², полярный угол.
β₁,β₂ ∈ [0,π/2]: внешние "половинки" (как α Тома на S³).

## What this does NOT mean
- Не доказывает существование радиальной части Aⱼ(β)
- Не решает уравнение Дирака на S⁶
- Не соединяет S³ и S⁶

## Next gate: G2
Действие операторов вращения SO(6) на азимутальных фазах:
аналог ∂_θ + ∂_θ̃ = Î_{3L} (Tom row 13) — что происходит при
действии корневых генераторов (лестничные операторы) на Картановы фазы?
Структурное предсказание: появятся члены с cotβ_k — аналог cot(2α) из G2.
