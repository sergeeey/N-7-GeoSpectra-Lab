# ALIVE_BRANCHES — живые маршруты исследования

**Обновлён:** 2026-08-12
**Дополняет:** `null_results/INDEX.md` (закрытые маршруты)

> **Разрыв 2026-06-22 → 2026-08-12 (52 дня, ~250 раундов, G67 → C102) закрыт
> boyko-project-radar скана: файл не отражал ни triality-closure (G109-128),
> ни decisive-experiment программу (C70-C90), ни multiplication-operator
> цепочку (C91-C102). Ниже добавлены только реально ОТКРЫТЫЕ ветки из
> самого свежего слоя (C99-C102); полная хронология — см.
> `experiments/20260811-ngen3-decisive-program/predictions_before_data.md`
> и `reports/SESSION_REPORT_2026-08-12_C91-C102_MULTIPLICATION_OPERATOR.md`.

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
| ~~G85B~~ | ~~Spectral saddle даёт мост к exp(−λ/ρ₆²)~~ | **NULL** | — | Closed 2026-06-22: t*=ρ₆²/3 exists, K(t*)>0, but exp factor = exp(−3)=const → no bridge | — | G85A, G85B |
| ~~G86A~~ | ~~Dual-modulus T∝ρ₆^α → exp(−λ/ρ₆²)~~ | **NULL** | — | Closed 2026-06-22: I=Γ(3)/T³~ρ₆^{−3α} for ALL α; structural theorem, 0/25 alpha give exp | — | G84A, G86A |
| ~~G86B~~ | ~~Warp factor Ω(y) → exp(−λ/ρ₆²)~~ | **NULL** | — | Closed 2026-06-22: uniform flux→trivial A=const; localized→polynomial+free Q; postulated→circular; ALL fail PASS | — | G84A, G86B |
| G72 | Geometric realization of 8_v triality bundle on S⁶ | PAUSED | 8_v construction требует explicit Tom input | — | TOM-BRIDGE PROMOTE → тогда открываем | — |
| C99-R-ROLE | Multiplication-operator "r не затрагивается" (M_k⊗I_r) — постулат, не выведен | OPEN | `D^1_{ab}(g)` скалярна, не касается индекса r напрямую — нет естественной точки старта | Найти/опровергнуть альтернативную гипотезу (D^1 действует на r как на копии того же представления) | — | — |
| C100-MULTI-COMPONENT | Даёт ли сумма по всем 4 компонентам D^1_{a,b} настоящее смешивание состояний (вместо инъективного вложения C100)? | OPEN | Не запускалось — C100 проверил только a=b=1/2 | Собрать все 4 M_k^{(a,b)}, сложить, перепроверить P0-P3 из C100 | — | — |
| C102-3LEVEL | Настоящий truncation-convergence тест (3+ уровня), не только пара k,k+1 | OPEN | Построен только 2-уровневый D_PW (C101/C102) | k=1,2,3 D_PW, code reused verbatim из C101/C102 | — | — |
| C102-REAL-SPECTRUM-S | Механизм точной вещественности связанного спектра D_PW (кандидат: D-bar подобен эрмитовой матрице через фикс. S) | OPEN | Численная replication (k=1,2 и k=2,3) есть, аналитический вывод S — нет | Построить/опровергнуть явное S для D-bar; см. pearl_registry/INDEX.md 2026-08-12 запись | — | — |

---

## Карта покрытия λ-маршрутов

```
exp(−λ/ρ₆²) происхождение — что проверено:

ЗАКРЫТО:
  ├── Стандартная калибровочная редукция (G83-G84A) → +12/+6, не 1/ρ₆²
  ├── Spectral proper-time (G84B) → только внутри интеграла
  ├── Poisson/theta resummation (G85A) → форма есть, мост нет
  ├── Spectral saddle/worldline (G85B) → t*=ρ₆²/3, exp(−3)=const, не 1/ρ₆²
  ├── Dual-modulus T∝ρ₆^α ALL α (G86A) → STRUCTURAL: I~ρ₆^{−3α}, ВСЕГДА степенная
  ├── Warp factor Ω(y) на S⁶ (G86B) → тривиальный A=const; λ~ρ₆² + свободный Q; circular
  └── Minkowski uplift через λ_geom (G60) → λ_geom < 0

ОТКРЫТО:
  *** ВЕСЬ ГЕОМЕТРИЧЕСКИЙ/СПЕКТРАЛЬНЫЙ КЛАСС ИСЧЕРПАН (G83–G86B) ***
  Brane instantons / gaugino condensation — вне scope этого проекта
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
