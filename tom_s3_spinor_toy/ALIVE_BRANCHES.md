# ALIVE_BRANCHES — живые маршруты исследования

**Обновлён:** 2026-06-22
**Дополняет:** `null_results/INDEX.md` (закрытые маршруты)

> Canonical source: этот репо. Claude/ChatGPT контексты = производные.
> Перед новым экспериментом: grep `null_results/INDEX.md` + проверить этот файл.

---

## Статусы

| Статус | Значение |
|--------|---------|
| `OPEN` | Активный, не убит, следующий тест определён |
| `PAUSED` | Жив, но ждёт внешнего события |
| `PROMOTE_CANDIDATE` | Прошёл gates, ждёт скептик-проверки |
| `BLOCKED` | Жив, но конкретная техническая проблема мешает тесту |

---

## Живые маршруты

| ID | Claim (1 строка) | Статус | Изменённое предположение | Kill condition | Revival condition | Последняя проверка | Связанный null |
|----|-----------------|--------|--------------------------|---------------|------------------|-------------------|----------------|
| TOM-BRIDGE | S³ spin connection → локальные SU(2)×SU(2) трансформации совпадают с операторами Тома на гармониках | PAUSED | Явная форма diff. операторов Тома | Тест покажет несовпадение при подстановке | Tom Lawrence Part 5 или Part 6 | 2026-06-22 | — |
| G85B | Spectral saddle / worldline resummation даёт финальный мост к A·exp(−λ_np/ρ₆²) | OPEN | Метод ресуммирования (Bessel/saddle, не Poisson/theta) | Вычисление показывает расходимость или отсутствие седловой точки | — | 2026-06-22 | G85A (Poisson/theta — форма есть, моста нет) |
| G86A | Dual-modulus или inverse-modulus route к exp(−λ/ρ₆²) | OPEN | Нестандартное определение модуля (не T∝ρ⁶) | Показывает те же +6/+12 что G84A | — | 2026-06-22 | G84A (стандартный ansatz → +12) |
| G86B | Dilaton / warp compensation route к exp(−λ/ρ₆²) | OPEN | Warp factor ≠ 1 в размерной редукции | Вводит новые свободные параметры без предсказательной силы | — | 2026-06-22 | G84A, G84B |
| G72 | Geometric realization of 8_v triality bundle on S⁶ | PAUSED | Требует explicit construction от Тома | 8_v не поддаётся G₂-equivariant construction | Tom подтверждает operator bridge (TOM-BRIDGE) | 2026-06-22 | — |

---

## Карта покрытия λ-маршрутов

```
exp(−λ/ρ₆²) происхождение — что проверено:

ЗАКРЫТО:
  ├── Стандартная калибровочная редукция (G83-G84A) → +12/+6, не 1/ρ₆²
  ├── Spectral proper-time (G84B) → только внутри интеграла
  ├── Poisson/theta resummation (G85A) → форма есть, мост нет
  └── Minkowski uplift через λ_geom (G60) → λ_geom < 0

ОТКРЫТО:
  ├── Spectral saddle/worldline (G85B) ← следующий внутренний gate
  ├── Dual-modulus route (G86A)
  └── Warp/dilaton compensation (G86B)
```

---

## Правила работы с этим файлом

1. **Перед новым экспериментом** — проверить этот файл + `null_results/INDEX.md`
2. **При REJECT** → строка переходит в `null_results/INDEX.md`, из этого файла удаляется
3. **При PAUSED** → revival condition должен быть конкретным и измеримым (не "когда-нибудь")
4. **Minimal Relaxation Rule** — новый маршрут меняет ОДНО предположение от ближайшего null result
5. **Revival condition без даты next_check** → статус деградирует до PARKED через 4 недели

---

*Паттерн: оригинальный (нет публичных аналогов с revival_condition + kill_condition + null pointer).
Ближайший аналог: Arbor (arXiv 2606.11926) — но без revival_condition и без parked/killed разделения.*
