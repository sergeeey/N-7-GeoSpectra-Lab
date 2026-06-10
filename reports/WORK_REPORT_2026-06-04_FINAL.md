# Отчёт о проделанной работе — сессия 2026-06-03 → 04

**Проект:** GeoSpectra Lab (Covariant Compactification Toy Lab)
**Диапазон commit'ов:** ead66d7 (git init) → 22fd9fe (HEAD, запушено)
**Расширяет:** `SESSION_REPORT_2026-06-03_04.md` (этот — финальная полная версия)

---

## 0. Резюме одной строкой

Закрыли negative-controls кампанию (**DISCRETIZATION_SENSITIVE / GEOMETRY_AGNOSTIC**),
поймали и исправили ошибку размерности (N≤896 → 13824), заменили нерабочий eigsh
на **точный block-solver (88×)** с committed-тестом, прогнали локально **W-sweep**
и **cross-geometry S²×S¹**, tool-проверили **карту Тома**, смягчили overclaim-wording,
и дали честную **оценку теории Тома** с диагнозом совместимости.

---

## 1. Хронология (по блокам, с commit'ами)

| # | Блок | Commit | Результат |
|---|------|--------|-----------|
| 1 | Ориентация + FL-постановка | — | S³×S¹ harness, задача: проверить специфичность Gate 4B |
| 2 | Skeptic-аудит Gate 4B | — | 3 FT: r(W=0) аномалия, spectral_circle, FSS |
| 3 | FL-артефакты (до расчётов) | ead66d7 | ESTIMAND, CLAIM, BATCH_DESIGN, SKEPTIC_AUDIT |
| 4 | Control D + 72-case batch | ead66d7 | C1 CONFIRMED, C2 INDETERMINATE |
| 5 | git init + push (363 файла) | ead66d7→907cf49 | merge серверной v0.1.24 работы |
| 6 | C2 закрытие (s1=128, 6 кейсов) | 66f2690 | scrambled 0.20× → вердикт уточнён (см. §5) |
| 7 | Пре-регистрация Gate5/W-sweep/cross-geom | b8a0f25 | 3 протокола + скрипты |
| 8 | **Ошибка размерности** (/tracy) | 92c7fe6 | N≤896 неверно → 13824; исправлено в forward-доках |
| 9 | **Block-solver** (eigsh отвергнут) | f7b98b1 | точно == dense, 88×, s1=256 разблокирован |
| 10 | Карта Тома (dimensional consistency) | 49c4d25 | λ₁(S^d)=d ✓, изометрия SO(d+1) нюанс |
| 11 | Cross-geometry fix (артефакт убран) | fa55fdc | hand-rolled → established builder; TRANSFER |
| 12 | W-sweep локально (block-solver) | 026bc61 | онсет W=5, насыщение с W≈10 |
| 13 | Verification-тест + wording fix | 22fd9fe | pytest 8/8; «GEOMETRY-SPECIFIC» смягчён |
| 14 | Оценка теории Тома | — (анализ) | research programme 5.5/10, см. §7 |

---

## 2. Научные результаты (все достоверны)

1. **Negative controls — DISCRETIZATION_SENSITIVE / GEOMETRY_AGNOSTIC.**
   Контроли A/B/C (random_hermitian, scrambled_geometry, broken_wilson) корректно
   отклонены (IPR(W=20) < 16% от ring-эталона). Харнесс различает метод дискретизации
   (FFT vs lattice), но НЕ детали геометрии внутри lattice-семейства.

2. **C2 spectral_circle — SCRAMBLING-SENSITIVE / STRUCTURE-SENSITIVE** (смягчено с
   «GEOMETRY-SPECIFIC»). Scrambled spectral_circle при s1=128 даёт IPR 0.014 vs S³×S¹
   0.070 (5× ниже) → чувствительность к структуре spectral_circle, НЕ S³×S¹-специфичность.

3. **Cross-geometry S²×S¹ — TRANSFER** (transfer_ratio≈1.0). После замены самодельного
   оператора на established builder: S²×S¹ ring контраст ≈ S³×S¹ ring (3.9/7.5/14.3 vs
   4.1/7.4/14.2). Подтверждает GEOMETRY_AGNOSTIC: сигнал несёт общий S¹-disorder.

4. **W-sweep — насыщение, не пик.** Онсет на W=5 (IPR 0.02→0.23, ~10×), плато с W≈10
   (ring 0.30–0.34). W=20 НЕ cherry-picked — сидит в насыщенной зоне. Укрепляет Gate 4B.
   Cross-check: ring W=20 s1=64 = 0.321 совпало с Gate 4B ref 0.320.

5. **Карта Тома — размерности стыкуются.** λ₁(S^d)=d: U(1)→S²(λ₁=2), SU(2)→S³(λ₁=3),
   SU(3)→S⁶(λ₁=6). Нюанс: изометрия S^d = SO(d+1) ≠ SO(d) маршрута Тома.

---

## 3. Инженерные результаты

- **`block_ipr_solver.py`** — точная по-блочная диагонализация (оператор блочно-диагонален
  по S³, 110 независимых S¹-цепочек). Совпадение с dense до 1e-14 (IPR + r_stat), 88×
  быстрее, снимает OOM до s1=256.
- **`tests/test_block_ipr_solver.py`** — committed pytest, 8/8 за 22.6s, |Δ|<1e-10.
- **eigsh отвергнут** (задокументировано): давал неверный IPR (0.036 vs 0.296) + 6× медленнее.
- Block-solver побочно ускорил W-sweep (43 мин → 1.7 мин) — стал локально-запускаемым.

---

## 4. Integrity-находки (что поймали и исправили)

| Находка | Серьёзность | Исход |
|---------|-------------|-------|
| **N≤896 неверно** (реально 108×s1=13824) | 🔴 шло в Zenodo | Исправлено во всех forward-доках; git-доказательство f7eff32 |
| **eigsh даёт неверный IPR** | 🔴 ложный FSS-тренд | Отвергнут, заменён block-solver'ом |
| **Самодельный S²×S¹ → IPR 0.83** | 🟠 артефакт построения | Заменён established builder'ом |
| **«GEOMETRY-SPECIFIC» overclaim** | 🟡 против GEOMETRY_AGNOSTIC | Смягчён → scrambling-sensitive |
| **Block-solver без committed-теста** | 🟡 verification-gap | Добавлен pytest |

Все три поймал принцип verify-before-claim: первая паника («comparison invalid»)
была опровергнута git-проверкой; eigsh и S²×S¹ артефакт пойманы correctness-gate
на области перекрытия (s1=64).

---

## 5. Оценка теории Тома (S³×S⁶ unification)

Независимая скептическая оценка (не peer-review полной статьи):

| Слой | Оценка | Комментарий |
|------|--------|-------------|
| Геометрическая идея | 8/10 | красивое ядро |
| Групповая структура | 7/10 | группы достижимы «бесплатно» (mirage-риск) |
| Связь с физикой СМ | 5/10 | хиральность+массы — пропасть |
| Завершённость | 3/10 | Dirac-bridge + alpha-проблема открыты |
| Проверяемость сейчас | 3/10 | нет предсказаний, отличающих от СМ/GR |
| **Witten no-go (хиральность)** | не доказано | центральный нерешённый враг программы |

- Как research programme: **5.5/10**
- Как завершённая теория: **3/10**
- Как поле для твоего вклада: **7/10** (узкое место: S³ spinor harmonics + alpha-проблема)

**Главный вывод о совместимости:** наш `GEOMETRY_AGNOSTIC` вердикт означает, что
**текущий harness структурно НЕ способен тестировать теорию Тома** (вся она про
различение геометрий, а харнесс к геометрии слеп). Чтобы помочь — нужна **новая
geometry/spinor-sensitive ветка**, начиная с узкой alpha-проблемы S³, а не полной теории.

---

## 6. Текущий статус

| Блок | Статус |
|------|--------|
| Negative controls (v0.1.22) | ✅ COMPLETE |
| C2 spectral_circle | ✅ scrambling-sensitive (s1=128) |
| Cross-geometry S²×S¹ | ✅ TRANSFER (geometry-agnostic) |
| W-sweep | ✅ насыщение, W=20 robust |
| Размерность | ✅ исправлена (13824) |
| Block-solver + тест | ✅ verified, 8/8 |
| Карта Тома | ✅ проверена |
| Wording | ✅ смягчён, audit-gaps закрыты |
| Git | ✅ HEAD=22fd9fe запушено, working tree чист |

---

## 7. Дальнейший план

**Заблокировано (дома/сервер):**
- Gate 5 s1≥256 (RAM ~13GB или сервер) — скрипт готов, block-solver
- Zenodo релиз (токен) — архив + инструкция готовы, N исправлен

**Опционально / отложено:**
- Sparse СБОРКА оператора → разблокирует s1=512
- **Новая S³ spinor-toy ветка** (Hopf-координаты, Kosmann generator) — для помощи Тому
  по alpha-проблеме. НЕ смешивать с v0.1.22.
- Ответ Тому: короткое сообщение «что есть S³/S¹ в моей модели», не отчёт

**Коммуникация:**
- Письмо Тому (черновик в TOM_MAPPING doc) — ждём ответа на прошлые

---

## 8. Остаточные заметки (для решения, не трогалось)

- `CLAIM_v0.1.22.md` и `SESSION_REPORT` ещё содержат «geometry-specific» (не в audit
  add-списке; CLAIM легитимен как pre-run гипотеза).
- upstream tracking для `main` не настроен (push явный `git push origin main`).
- Репо переехало: старый URL → `github.com/sergeeey/N-7-GeoSpectra-Lab.git`.

---

**Дата отчёта:** 2026-06-04
**HEAD:** 22fd9fe
