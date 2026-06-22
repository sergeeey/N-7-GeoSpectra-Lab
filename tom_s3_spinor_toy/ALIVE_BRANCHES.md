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

| ID | Claim (1 строка) | Статус | Limited by | Next falsifier | Revival condition | Связанный null |
|----|-----------------|--------|------------|----------------|------------------|----------------|
| TOM-BRIDGE | S³ spin connection → локальные SU(2)×SU(2) трансформации совпадают с операторами Тома на гармониках | PAUSED | Явная форма diff. операторов Тома неизвестна | Прямое сравнение с его ур. (84) TSSv9 | Tom Part 5/6 — он сам придёт с вопросами | — |
| G85B | Spectral saddle / worldline resummation даёт финальный мост к A·exp(−λ_np/ρ₆²) | OPEN | G85A показал: Poisson/theta форма есть, моста нет | Найти седловую точку в proper-time интеграле или доказать отсутствие | — | G85A |
| G86A | Dual-modulus / inverse-modulus route к exp(−λ/ρ₆²) | OPEN | G84A убил стандартный T∝ρ⁶ ansatz | Показать T(ρ₆) с другим определением модуля → проверить степень | — | G84A |
| G86B | Dilaton / warp compensation route к exp(−λ/ρ₆²) | OPEN | G84A/G84B убили стандартную редукцию | Показать warp factor ≠ 1 не вводит новых свободных параметров | — | G84A, G84B |
| G72 | Geometric realization of 8_v triality bundle on S⁶ | PAUSED | 8_v construction требует explicit Tom input | — | TOM-BRIDGE PROMOTE → тогда открываем | — |

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

*Паттерн: оригинальный — сочетание null_results/ + parked/ + ALIVE_BRANCHES с revival_condition не найдено в публичных репо.*

*Внешний аналог: [UNVERIFIED] Возможная параллель с branch-status системами для hypothesis tracking — не верифицировано инструментом. Не цитировать внешне до подтверждения.*
