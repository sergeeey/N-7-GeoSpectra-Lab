# Session Report — 2026-06-03 → 2026-06-04

**Project:** GeoSpectra Lab (Covariant Compactification Toy Lab)
**Scope:** v0.1.22 Negative Controls → v0.1.25 (dimension fix, block solver, Tom mapping)
**Commits:** ead66d7 (init) → 49c4d25 (latest)

---

## TL;DR (одной строкой)

Закрыли negative-controls кампанию (вердикт **DISCRETIZATION_SENSITIVE /
GEOMETRY_AGNOSTIC**), поймали и исправили **ошибку размерности N≤896** в публичных
доках, заменили нерабочий sparse eigsh на **точный block-solver (88× быстрее)**, и
tool-проверили **карту Тома** (размерности стыкуются, изометрия — нюанс).

---

## Хронология (что делали по порядку)

### 1. Ориентация + постановка
- `/orient`: проект — finite-lattice spectral falsification harness. Git отсутствовал.
- Поставили задачу через FL Full-Ladder + EstimandOps: проверить специфичность
  Gate 4B сигнала перед движением дальше.

### 2. Skeptic-аудит Gate 4B (context-asymmetric)
Сгенерировали 3 falsification-теста, проверили по сырым JSON (`merged/*.json`):
- **FT-1:** агрегатный r(W=0)=0.606 — аномалия, оказалась от spectral_circle r=1.000
  (вырожденный спектр, структурная особенность).
- **FT-2:** spectral_circle IPR(W=20) **убывает** с N (0.175→0.087), тогда как
  ring/wilson_ring дают **плато** (~0.32, ~0.25). [OPEN]
- **FT-3:** FSS-усиление реально для ring/wilson_ring [CLOSED], под вопросом для
  spectral_circle.

### 3. FL-артефакты (написаны ДО расчётов)
`SKEPTIC_AUDIT`, `ESTIMAND_v0.1.22`, `CLAIM_v0.1.22` (C1+C2), `BATCH_DESIGN_v0.1.22`.

### 4. Код + прогон
- Реализовали Control D (`spectral_circle_scrambled`), исправили broken_wilson
  (`disabled`→`scrambled`: disabled = чистый ring, не контроль).
- Dry run (4 контроля) → **72-case batch** (s1=16,32,64).
- Результат: **C1 CONFIRMED** (контроли A/B/C отклонены, IPR <16% от ring),
  **C2 INDETERMINATE** (spectral_circle — crossover).

### 5. Git + публикация
- `git init`, коммит 363 файла, remote, push. Merge принёс серверную работу v0.1.24.
- Обновили ROADMAP, CLAIMS_AND_CAVEATS. Zenodo-архив готов (блокер: токен).

### 6. Пре-регистрация будущего (3 протокола)
`GATE5_FSS`, `W_SWEEP`, `CROSS_GEOMETRY_S2S1` + скрипты, все dry-run проверены.

### 7. Закрытие C2 (точечный прогон)
- 6 кейсов spectral_circle_scrambled s1=128 (~48 мин).
- Результат: scrambled IPR(W=20)=0.014 vs S³×S¹ ref 0.070 = **0.20×**.
- Вердикт **C2 → GEOMETRY-SPECIFIC** (геометрия держит локализацию при большом N,
  не структурный артефакт). Artifact audit: **RUN_VALID_READY_FOR_REVIEW**.

### 8. /tracy → ВСКРЫТА ОШИБКА РАЗМЕРНОСТИ
Перед планированием Gate 5 нашли: заявленное **«N≤896» неверно**.
- [VERIFIED-git f7eff32] Gate 4B реально использовал s3_dimension(3)=108 →
  **N=13824** при s1=128, не 896. «896» = 7×s1 = одна SU(2)-оболочка (mislabel).
- [VERIFIED-run] Negative controls тоже 108×s1 → **сравнения ВАЛИДНЫ** (dimension-matched).
- Изначальная паника («comparison invalid») **опровергнута** git-проверкой.
- Исправили N во всех forward-доках (.zenodo, CITATION, README, CLAIMS×6, ROADMAP×3).
- Зафиксировали в `DIMENSION_DISCREPANCY_AUDIT_v0.1.25`.

### 9. Sparse eigsh → отвергнут, block-solver
- Пользователь попросил sparse eigsh для Gate 5 s1≥256.
- **eigsh провалился:** IPR=0.036 (неверно, не сошёлся) + 399s (в 6× медленнее dense).
- Нашли: оператор **точно блочно-диагонален** (110 независимых S¹-цепочек, 3 ненулевых/строку).
- Написали `block_ipr_solver.py`: **совпадение с dense до 1e-14** (IPR+r_stat,
  6/6 проверок), **88× быстрее**. Gate 5 расширен до s1=256.

### 10. Карта Тома (dimensional consistency)
- [VERIFIED-tool] λ₁(S^d)=d: U(1)→2→S²(λ₁=2), SU(2)→3→S³(λ₁=3), SU(3)→6→S⁶(λ₁=6) —
  **размерности стыкуются точно**.
- [VERIFIED-tool] Нюанс: изометрия S^d = SO(d+1) ≠ SO(d) маршрута Тома.
- Документ + черновик ответа Тому. Научное подтверждение: 0/10 (коммуникация/roadmap).

---

## Текущий результат / статус

| Блок | Статус |
|------|--------|
| Gate 4B сигнал | ✅ SIGNAL_PRESERVED (7.07×, v0.1.24) |
| Negative controls | ✅ COMPLETE: **DISCRETIZATION_SENSITIVE / GEOMETRY_AGNOSTIC** |
| C1 (харнесс-дискриминация) | ✅ CONFIRMED — random/scrambled/broken отклонены |
| C2 (spectral_circle) | ✅ GEOMETRY-SPECIFIC (s1=128 закрыл) |
| Ошибка N≤896 | ✅ FIXED во всех forward-доках (real N=13824) |
| Gate 5 feasibility | ✅ block-solver → s1=256 доступен (был OOM) |
| Карта Тома | ✅ dimensional consistency проверена |
| Тесты | ✅ block-solver 6/6 совпадений с dense |

**Главный научный вывод:** ring и wilson_ring — единственные семейства с настоящим
плато локализации, специфичным к S³×S¹. Все плохие контроли отклонены. Харнесс
различает дискретизацию (FFT vs lattice), но НЕ детали геометрии внутри lattice.

**Главный инженерный вывод:** реальная размерность 108×s1 (не 896); block-solver
снял OOM-барьер до s1=256 точно и в 88× быстрее.

---

## Что НЕ сделано (заблокировано)

| Задача | Блокер |
|--------|--------|
| Zenodo релиз | токен (дома) |
| Gate 5 / W-sweep / cross-geom запуск | сервер (пользователь запустит дома) |
| s1≥320 | нужна sparse СБОРКА оператора (op всё ещё dense) |
| Письмо Тому | черновик готов, ждём прошлый ответ |

---

## Дальнейший план

**Дома (пользователь):**
1. Запустить `run_gate5_fss_v0.1.25.py --run` (block-solver, s1=160/192/256)
2. Запустить W-sweep + cross-geometry S²×S¹
3. Zenodo: загрузить архив с исправленным N (инструкция готова)

**Следующая сессия (после серверных данных):**
4. Проанализировать Gate 5 (SATURATION / CONTINUING / REVERSAL)
5. W-sweep: найти онсет/пик disorder (валидирован ли W=20)
6. cross-geometry: переносится ли сигнал на S²×S¹

**Опционально / отложено:**
7. Sparse сборка оператора → разблокирует s1=512
8. Geometry-sensitivity харнесса → предусловие для Tom-aligned лестницы (S²/S³/S⁶)
9. Отправить ответ Тому (с нюансом SO(d+1))

---

## Ключевые файлы сессии

```
reports/SKEPTIC_AUDIT_GATE4B_v0.1.22.md
reports/ESTIMAND_v0.1.22.md
reports/CLAIM_v0.1.22.md
reports/BATCH_DESIGN_v0.1.22.md
reports/S3_S1_NEGATIVE_CONTROLS_RESULTS_v0.1.22.md
reports/DIMENSION_DISCREPANCY_AUDIT_v0.1.25.md
reports/GATE5_FSS_PREREGISTRATION_v0.1.25.md
reports/W_SWEEP_PREREGISTRATION_v0.1.25.md
reports/CROSS_GEOMETRY_S2S1_PREREGISTRATION_v0.1.25.md
reports/TOM_MAPPING_DIMENSIONAL_CONSISTENCY_v0.1.25.md
cc_toy_lab/spectral/block_ipr_solver.py
cc_toy_lab/controls/negative_controls.py  (Control D added)
scripts/run_gate5_fss_v0.1.25.py  (block solver)
scripts/run_w_sweep_v0.1.25.py
scripts/run_cross_geometry_s2s1_v0.1.25.py
```

---

**Report date:** 2026-06-04
**Latest commit:** 49c4d25
