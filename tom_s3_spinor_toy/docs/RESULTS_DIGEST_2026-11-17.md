# Сводка результатов проекта (на 2026-11-17)

Рабочий документ для владельца. Собран из `CLAIM_LEDGER.yaml` (223 записи, разобраны скриптом),
`null_results/INDEX.md`, `parked/INDEX.md`, `OPEN_BLOCKERS.md`, `THEOREM_PACK.md`,
`SUPERSEDED_RESULTS.md`, корневого `CLAIMS_REGISTRY.md` и списка папок `experiments/`.
Сами утверждения я заново не проверял: ниже пересказ записей реестра. Метки: [VERIFIED] означает,
что число получено разбором файла инструментом в этой сессии; остальное пересказ записей.

## 1. Как читать цифры (сначала про надёжность)

| Что | Значение [VERIFIED, разбор CLAIM_LEDGER.yaml] |
|---|---|
| Записей в журнале | 223 |
| Папок экспериментов в `experiments/` | 449 (июнь 124, июль 100, август 99, сентябрь 89, октябрь 12, ноябрь 23) |
| truth_status | SUPPORTED 155, PROVED 38, REFUTED 15, OPEN 7, CONDITIONAL 4, PARTIALLY_SUPPORTED 4 |
| test_outcome | PASS 160, FAIL 37, PARTIAL 14, INCONCLUSIVE 6, NOT_RUN 4, CONFLICTING 2 |
| evidence_status | INTERNALLY_CERTIFIED 208, PARTIAL 6, VERIFIED_EXTERNAL_SOURCE 4, FORMALLY_CHECKED 3, CONTESTED 1, INDEPENDENTLY_REPRODUCED 1 |
| Записей по месяцам (по дате папки-доказательства) | июнь 1, июль 19, август 93, сентябрь 67, октябрь 12, ноябрь 22, без даты 9 |

Что из этого следует:

- 208 из 223 записей «внутренне сертифицированы», то есть проверены нашими же скриптами и
  проверками той же семьи моделей. Независимо воспроизведена одна запись, формально проверены
  (Lean) три, сверены с внешним первоисточником четыре.
- 37 записей с исходом FAIL это в основном полезные отрицательные результаты (убитые гипотезы,
  закрытые пути), а не поломки.
- Журнал покрывает меньше половины папок: 449 папок против 223 записей. Результаты июня и июля
  (цепочка G6–G106) в основном живут в `null_results/INDEX.md`, `THEOREM_PACK.md` и
  `docs/gates_tracker.md`, а не в журнале.

## 2. Три трека проекта (из CLAUDE.md и README)

1. **Трек A, численный** (`cc_toy_lab/`, `scripts/`, `tests/`): вердикт `DISCRETIZATION_SENSITIVE`.
   Корневой `CLAIMS_REGISTRY.md` (26 утверждений, версия 2026-06-30) содержит уровни L1–L4.
2. **Трек B, алгебраический** (`tom_s3_spinor_toy/`): механизм числа поколений на S³×S⁶ через
   индекс Атьи–Зингера. Это основная масса этого документа.
3. **Третий, независимый трек** (заморожен 2026-06-30, `paper/WHEN_GEOMETRY_BECOMES_UNRECOVERABLE.md`):
   спектральная восстановимость геометрии против физики. Итог: нулевая гипотеза H0 побеждает,
   H1–H4 убиты (в корневом реестре: пункт 23 «S³×S⁶ → СМ» помечен KILLED; H1 калибровочное
   расслоение Â=0, H2 поток H²(S⁶)=0, H3 орбифолд χ=0, H4 NCG KO-dim=1).

## 3. Главный вердикт по Треку B [пересказ OPEN_BLOCKERS / RESEARCH_STATUS_REPORT / ledger]

- **N_gen = 3: CONDITIONAL** (C4). Условия: C1 (индекс = 1 на канал триальности, PROVED),
  C2 (dim ker D_{S6,twisted} = 1, PROVED, 2026-07-14), C3 (KT-8, SUPPORTED с исходом FAIL:
  у полного оператора на S³×S⁶ с обычной связностью на S³ нет нулевой моды, то есть
  физической безмассовой фермионной моды нет) и C_G67C3 (третий канал триальности, OPEN).
  Статус не менялся с сентября, ни одна из четырёх зависимостей не закрыта.
- **λ (константа подавления) свободный параметр** (C14, PROVED): стандартного 10D/геометрического
  происхождения нет, путь исчерпан.
- **Главный открытый блок OB1** (механизм выбора родительского действия / выбор t=0 или t=1)
  припаркован 2026-07-17 после серии закрытых путей (см. раздел 5).
- Полный список блокеров: OB1 PARKED; OB2 отвечен «нет» (2026-08-10); OB3 исправлен; OB4 разделён;
  OB5, OB7–OB10, OB12 решены; OB11 частично; OB13 «селектор t не найден»; OB14 заблокирован.

## 4. Хронология по периодам

### 4.1 Июнь–июль 2026: фундамент и массовое закрытие путей (цепочка G6–G106)

Записей в журнале мало, основное в `null_results/INDEX.md` (62 строк) и `THEOREM_PACK.md`.

Что установлено:
- **Теорема-пакет из пяти лемм**: S⁶ = G₂/SU(3), c₃(S⁻) = χ(S⁶) = 2, индекс = 1 на канал
  триальности, хиральность (C21: знак индекса +1, единственное решение dim ker D⁺=1, D⁻=0).
  Ограничение, записанное самим пакетом: это результат на факторе S⁶, не на полном S³×S⁶.
- **Теорема T1 «исчерпание» (G47/G48)**: категории 1–5 закрыты (14 отрицательных результатов),
  категория 6 закрыта чтением первоисточника Harland–Nölle (в S⁶ нет c₃=6).

Что убито (REJECT/NULL), по смыслу:
- свободное ℤ₃-действие на S⁶ (χ=2 не делится на 3), G₂-инстантон на три поколения (индекс 0),
  Рарита–Швингер на S³, Эйлеров класс, квантование потока, WZW уровня S³, кобордизмы,
  K-теория, тадпол струны, минимум спектрального действия, SU(4) Пати–Салам по классу c₃,
  G₂→SU(3) нарушение, браны, аномалия Грина–Шварца, стабильные расслоения, триальность на S³×S⁶
  (G₂ не имеет 8-мерного неприводимого представления, 8_v≅8_s≅8_c, орбита триальности схлопывается).
- λ-происхождение: 5 классов непертурбативных источников (G103), «dual-modulus» (G86A),
  warp-фактор (G86B), волновая линия (G85B), модулярная симметрия вкусов: ни один не даёт
  exp(−λ/ρ₆²).
- Исправления по пути: META-C1 был PROMOTE, затем помечен SUPERSEDED (траектория ρ₃=κρ₆ была
  ошибочно принята за физическую); G34-D1 и G40-B2 помечены WEAK.

### 4.2 17 июля 2026: серия «раундов» (C5–C27 в журнале)

- **C7 PROVED**: в рамках произведения многообразий Iso(S³×S⁶)=SO(4)×SO(7) нельзя реализовать
  калибровочную алгебру SU(4) ни одним вложением (ворота G97 закрыты). Оговорка записана
  2026-11-14: скрученный/непроизведённый вариант остаётся открытым.
- **C10, C16 REFUTED**: все условия аномалии смешанной гиперзаряд-цепочки обращаются в ноль на обоих
  концах t=0,1 (проверены все три и оставшиеся два канала).
- **C6**: правильный механизм аномалии кубическая SU(4)³ (A(4,2,1)=+2, A(4̄,1,2)=−2), а не Виттена.
- **C13 PROVED**: Scal(t) = Scal_LC − 6(2t−1)².
- **C17 PROVED**: соглашения по t согласованы между preprint.tex и раундами 99/111.
- **C22 REFUTED**: обычное уравнение Киллинговых спиноров не выбирает t=0,1.
- **C23 PROVED**: плоскостность связности Картана–Шоутена при t∈{0,1} даёт глобально параллельный спинор.
- **C27 REFUTED**: размерность ядра D_{S³,t=0} равна 2, а не 1 (двумя независимыми методами).
- **C25 OPEN**: какое из t=0, t=1 реализовано физически — остаётся открытым.
- **C26**: t=0 это SU(2)_L-синглет и SU(2)_R-дублет; t=1 наоборот (при c₀=−2, см. C24).
- Отрицательные результаты того же дня: AHL2023-кросс-проверка (FALSIFIED), сильное чтение
  «H_matter ⊗ H_generation» (REJECT), согласование L5 (FALSIFIED), отсутствие градуирующего оператора.

### 4.3 Август 2026: цепочка C28–C121 (93 записи)

Три больших линии.

1. **C11 (два оператора D для t=0 и t=1)**, C38–C57. Итог: ядра при t=0,1 это две хиральные половины
   одного 4-мерного Spin(4)-спинора (C38). Однооператорный выход закрыт (C42). Блок D⁰⊕D¹ даёт
   градуировку, но она общая по t, а не специфичная для t=0,1 (C43, C44). Дублирование, если принять,
   это дублирование чётности (C46). Четырёхмерное ядро изолированная точка семейства (C47). Индексное
   спаривание равно нулю, двойственность Пуанкаре не выполняется (C49), ориентируемость не
   восстанавливается ни одним способом (C50–C54). Сигнатура ошибок: C28 (псевдореальный тип)
   отозван, C32 исправил на реальный; C31 рассуждение отозвано, вывод восстановлен (C33).
   C55 (A1: инверсия переворачивает оператор Дирака) выведена после десяти раундов как унаследованное
   допущение; C56 «флаг U_ι²» оказался ложной тревогой.
2. **OB11 (триальность, SU(3) на каналах)**, C61–C85. Три канала доказуемо не сводятся к одному (C63).
   Мост round59↔G102 найден (C70), расширен на три канала (C71), эквивариантность по G₂ сохраняется
   до G₂ и исчезает на нём (C72). Поиск непроизведённой связи: серия чистых нулей C79–C91. Пробел с
   цитатой «Sire & Xu» закрыт заменой на Meier (C85). C94 → C95: исправление знака обобщённого генератора.
3. **Оператор D_PW (Пётер–Вейль)**, C86–C106 и позже. Сборка блочно-трёхдиагонального оператора,
   обнаружен реальный спектр без объяснения (C101–C103), эксперименты по смешиванию (C104–C106),
   «исключительные точки» (C111), асимметричное правило n=4,5 (C114–C117). Часть линии закончена
   ретракциями: C118 (гипотеза плотности) отозвана, C122 (негативный контроль) припаркован после
   трёх раундов (каждый нашёл настоящий дефект предыдущего).

Закрытия: C107 «наивный мост Meier–Kostant» FALSIFIED (29 августа); C119 Бисмут-Риччи-плоский
кандидат убит; C121 эта-инвариант не зависит от интервала (REFUTED).

### 4.4 Сентябрь 2026: C122–C198 (67 записей)

- **Закрытие маршрутов к OB1.** C124 (классификация родительских инвариантов) STRUCTURAL_NO_GO;
  C125 полная калибровочная эквивалентность отвергнута; C134 ECSK-кручение (REJECT); C136 совместное
  уравнение Киллинга (REJECT); C137 конденсат фермионов (REJECT); C138 приведённая эта-инвариант (NULL);
  C167–C173: диагональный ℤ_p-орбифолд, итог C173: триальность это внешний автоморфизм Spin(8), чисто
  геометрическая конструкция из G₂/SU(3)+S³ внешней быть не может, весь маршрут P4 закрыт; C176/C177
  спектральное действие имеет единственный минимум при t=½, а не при t=0,1 (то есть против нужного
  результата); C191 постулат P5 (калибруемый слой Spin(8)) не разделяет 8_s и 8_c; C198 ядро
  зафиксировано по всему семейству кручения (REJECT).
- **Kostant–Landweber / твист-расслоение**, C139–C160: нулевая мода для другого твиста (C139),
  ядро как «пол градуированного ветвления» (C141), пропорциональность оператора кубическому члену
  Костанта (C144), но физический скрученный оператор Костанту не равен (C145, REFUTED), доказано,
  что исчезновение члена вынуждено теоремой Шура (C146), анализ коэффициента связности (C147, C151–C156,
  часть REFUTED/артефакт), сбалансированность хиральности доказана, но классически, не открытие
  (C157), соответствие знаковой тройки KO-размерности 6 найдено в первоисточнике (C160).
- **Спиноры на S³ и S²**, C179–C198 (начало линии, которую ведёт переписка): функции-мультиплеты на
  сфере не несут спинорного представления (C179 PROVED); явный спектр Дирака на S³ (C180) и на S² (C185,
  ±(n+1)); спинорные секторы S² по спуску Хопфа (C182, C184); эйлеровы углы (C187 → C188: векторная
  версия не совпала, версия «из кватернионов» воспроизвела спектр); сдвиг спиновой связности −3/2
  выведен (C189), пара ±3/2 для левого/правого действия (C190); кандидат кадра Хопфа воспроизводит k=1,
  но не нулевую моду k=0 (C194, REJECT только для этого кандидата).

### 4.5 Октябрь 2026: C199–C221 (12 записей)

- **Lean 4 (C199 PROVED, FORMALLY_CHECKED)**: эквивариантный изоморфизм вынуждает равенство размерностей Hom.
- **Линия «ладдеров» и кандидата Тома**: C201 (калибровка теста лестницы l=1, √2 точно), C202
  (матрицы l=1 корреспондента эквивалентны C201 через U), C205/C206 (соглашения строка/столбец,
  √2-форма), C220 (норма гармоник), C221 (шаг 4 спинорной лестницы не проходит: котангенс отношения
  спин-весов).
- **CSDR / S⁶ (gravity-only)**: C210–C217 (корневая система G₂, потенциал, кручение, Риччи по Кастеллани,
  Фридрих–Иванов); C214 «расхождение формулы мостика» была отозвана C217 (формула была верна,
  «аномалия» это соглашение Кастеллани без стандартной 1/2); C219: точное значение теплового ядра
  S⁶ даёт точку стабилизации ρ₆; нет допустимой области минимума для H8 (PARTIALLY_SUPPORTED).
- C203/C218: три конструкции su(3) в so(6) одного типа представления; явная вещественная структура J.

### 4.6 Ноябрь 2026: C222–C243 (линия по запросам корреспондента)

С 2 ноября работа идёт по прямым запросам Тома Лоуренса (все записи SUPPORTED/PASS, кроме двух FAIL,
которые отрицательные результаты):

- **C222–C226**: инвариантные подпространства спина ½ на S² образуют семейство CP¹; слои Хопфа
  окружности, кадр g_ab; фермион не является суперпозицией двух функций с постоянными коэффициентами
  (C224, исход FAIL); генераторы D₁,D₂,D₃ выведены из определений (C225); проекция вектора Хопфа
  и нормировка SO(3) (C226).
- **C227–C232**: спектр D₀ для всех s по Пётеру–Вейлю (C227); дублет H₂ не инвариантен под D₀ (C228,
  исход FAIL: остаток один, ядро одно); три чтения действия SU(2): A и C представления, B
  антипредставление (C229); H₂ сохраняется эквивариантным оператором первого порядка тогда и только
  тогда, когда выполнено условие на коэффициент B (C230); ядро CR на S³ (C231); J₃R на правом индексе
  равно половине хопфова заряда (C232).
- **C233**: проверка мутациями, 40 мутантов, 27 убиты проверкой, 9 упали громко, 4 выжили (все
  эквивалентны).
- **C234–C241**: плотность √det g как скалярная плотность; гармонические секторы S³ (C235); четвёртая
  гармоника это диагональный синглет (C236); стабилизатор вакуумной точки это диагональный SU(2)
  (C237); алгебра препринта корреспондента проверена (C238: несовпадение знаков уравнений 3 и 5, лишний
  генератор); 32 состояния постера согласованы по бухгалтерии (C239); на C² нет оператора хиральности
  (C240); стандартный гиперзаряд, добавленный к 32 состояниям, даёт стандартные заряды (C241).
- **C242 (16.11)**: вторая компонента дублета e^{iφ} sin(θ/2) однозначно определяется вектором V и совпадает
  с результатом через u при двух заявленных допущениях; вариант с другим знаком это элемент u-транспонированной,
  определитель −1.
- **C243 (17.11)**: u^T = σ₂ u⁻¹ σ₂ в SU(2); инверсия на S³ переворачивает ориентацию и меняет левые трансляции
  на правые; чтение C из C229 равно чтению A в переменных σ₂ξ (численно, 300 испытаний). Связь с вопросом
  «какая SU(2) это спин» остаётся гипотезой. Коммит `d5e387a`, не отправлен в origin.

## 5. Сильнейшие результаты (PROVED, 38 записей, избранное)

| Запись | Что доказано |
|---|---|
| C1, C2, C21 | индекс S⁶ = 1 на канал, dim ker = 1, знак хиральности +1 |
| C7 | SU(4) не реализуется в Iso(S³×S⁶) (в рамках произведения) |
| C8, C13, C17 | K3 ≡ T3R; Scal(t) = Scal_LC − 6(2t−1)²; соглашения по t согласованы |
| C14 | λ свободный параметр |
| C23, C39, C42, C44, C46–C57, C59, C60 | цепочка по C11: плоскость при t=0,1, ι это чётность, дублирование это дублирование чётности, ориентируемость не восстанавливается, KO-кортеж не зависит от выбора Pin |
| C113, C167, C179, C195 | нулевая модель j₂=0 не ломает вещественность; ℤ_p-орбифолд асимметрия; функции-мультиплеты не несут спинор |
| C199 | Lean-доказательство: эквивариантный изоморфизм вынуждает равенство Hom-размерностей |
| C201, C202, C205, C206, C220, C221 | серия точных sympy-проверок по лестничным операторам и спинорным шагам |

## 6. Что убито (REFUTED, 15 записей) и главные отрицательные итоги

C10, C16 (аномалии смешанного гиперзаряда), C22 (Киллингов спинор не выбирает t), C27 (кратность 2),
C28/C31 (отозваны и исправлены), C45 (алгебра не оправдывает дублирование), C107 (наивный мост Meier–Kostant),
C110 (гипотеза ковариантности), C119 (Бисмут-Риччи-плоский кандидат), C121 (эта-инвариант), C145
(скрученный оператор ≠ Костант), C151, C154, C156 (формулировки про коэффициент связности/отношение).

Кроме журнала: 62 строк `null_results/INDEX.md`; 7 припаркованных направлений в
`parked/INDEX.md` (R4-SADDLE, L4A-FORK, L4B-HIGHER-REPS закрыт Round 56, PW-ASYMMETRIC-RULE-MECHANISM,
C122-NEGATIVE-CONTROL, OB1-PARENT-ACTION, C204-EXPLICIT-CONJUGACY).

## 7. Что осталось открытым

- OB1: нет механизма, выбирающего t=0 или t=1 (C25 OPEN); все проверенные кандидаты закрыты.
- OB14: почему Σ, а не m или другое расслоение, является физическим твистом (заблокировано).
- Третий канал триальности 8_v: постулат модели, не выведен (C_G67C3 OPEN).
- C11: «два оператора» остаётся вопросом о пределах рамки произведения (C11 OPEN).
- Линия корреспондента: какая SU(2) является спином (R05), какой n в явном u, оператор поля Тома (у нас его нет).
- C118 и C122: гипотеза плотности отозвана, негативный контроль припаркован.

## 8. Ограничения этой сводки

- Пересказ записей реестра, не независимая проверка: утверждения я не пересчитывал.
- Ранние результаты (июнь–июль) взяты из индексов и пакетов теорем, а не из журнала, поэтому там
  детализация беднее.
- Корневой реестр Трека A (26 утверждений) и третий трек отражены кратко; полные таблицы в
  `../CLAIMS_REGISTRY.md` и `../paper/`.
- Журнал и индексы могли разойтись: `ALIVE_BRANCHES.md` сам помечен как не перепроверенный с 2026-09-09.

## Приложение A. Все 223 записи журнала (компактно)

Столбцы: идентификатор (обрезан), truth_status, test_outcome, дата папки-доказательства, начало формулировки.
Полные тексты: `CLAIM_LEDGER.yaml`.

| id | truth | test | дата | формулировка |
|---|---|---|---|---|
| C1_S6_INDEX_1 | PROVED | PASS | - | ind(D_{S6} tensor S-) = 1 per Z3-triality channel (Atiyah-Singer, S6-only) |
| C2_ROUND59_KERNEL_DIM1 | PROVED | PASS | 20260714 | dim ker(D_{S6,twisted}) = 1 exactly (Lichnerowicz safety factor 8/45 + G2-Schur) |
| C3_KT8_NO_ZERO_MODE | SUPPORTED | FAIL | - | Full D on S3xS6 (untwisted, Levi-Civita S3) has NO zero mode -- blocks N_gen=3 as a physical (massless 4D fermion) statement |
| C4_NGEN3_HEADLINE | CONDITIONAL | CONFLICTING | - | N_gen = 3 (three Standard Model generations from S3xS6 geometry) |
| C_G67C3_THIRD_CHANNEL | OPEN | INCONCLUSIVE | 20260717 | Three geometrically distinct triality channels (8_v,8_s,8_c) all independently realized as physical Dirac zero-mode channels |
| C5_SU2R_GAUGED | SUPPORTED | PASS | 20260717 | SU(2)_R is genuinely gauged in preprint.tex (real KK boson + kinetic term + Higgs bidoublet, not just a label) |
| C6_CUBIC_SU4_ANOMALY_MECHANISM | SUPPORTED | PASS | - | Cubic SU(4)^3 anomaly (A(4,2,1)=+2, A(4bar,1,2)=-2, sum=0 only together) is the correct anomaly-forcing mechanism, not the Witten SU(2) anom |
| C7_GATE_G97_CLOSED | PROVED | PASS | 20260717 | No SU(4) gauge-algebra realization exists within Iso(S3xS6)=SO(4)xSO(7), for same-factor OR diagonal embeddings, within the standard product |
| C8_K3_EQUIV_T3R | PROVED | PASS | - | K3 (a previously separate charge) is identical to T3R |
| C9_BL_ZERO_TWISTED_KERNEL | SUPPORTED | PASS | 20260717 | B-L = 0 on the twisted kernel via Leibniz-lift |
| C10_MIXED_Y_ANOMALY_FAIL | REFUTED | FAIL | 20260717 | All three anomaly conditions ([SU(3)_c]^2 U(1)_Y, [U(1)_Y]^3, [grav]^2 U(1)_Y) computed for BOTH t=0,1 endpoints separately using Y=T3R+(B-L |
| C16_REMAINING_MIXED_Y_CHANNELS_FAIL | REFUTED | FAIL | 20260717 | [SU(2)_L]^2 U(1)_Y and [SU(2)_R]^2 U(1)_Y (the 2 mixed-Y channels round96/round92 never computed) also vanish for both t=0,1 endpoints and i |
| C17_T_CONVENTION_RECONCILED | PROVED | PASS | 20260717 | preprint.tex/round67-68's Kostant Dirac-operator shift D_S3(t)=D_LC+(t-1/2)h_H and round99/round111's Cartan-Schouten curvature R^t=t(t-1)[[ |
| C18_Z2_LEFT_RIGHT_ISOMETRY_CONFIRMED_ORBIFOLD_RO | SUPPORTED | PASS | 20260717 | iota(g):=g^-1 is a genuine, tool-verified isometry of S3=SU(2) that pulls back the WHOLE Cartan-Schouten connection family exactly: iota*(Na |
| C11_D4_PRODUCT_ANSATZ_FORK | OPEN | INCONCLUSIVE | 20260717 | t=0 and t=1 sector coexistence, as a product-ansatz spectral-triple question (does 'two D's' make sense at all) |
| C12_BLOCK_SPECTRAL_TRIPLE_NO_SWAP_SYMMETRY | SUPPORTED | PASS | 20260717 | Toy block spectral triple D_block=diag(0,0,3c/2,3c/2) has NO block-exchange symmetry (S D_block S^-1 != D_block) |
| C13_SCAL_T_EINSTEIN_CARTAN_SPLIT | PROVED | PASS | 20260717 | Scal(t) = Scal_LC - 6*(2t-1)^2 -- bare curvature scalar of the torsionful connection decomposes exactly into metric-curvature minus torsion- |
| C14_LAMBDA_FREE_PARAMETER | PROVED | FAIL | - | lambda (the exponential-suppression coupling) has no standard 10D/geometric/spectral origin -- FREE_COUPLING_PARAMETER, confirmed exhausted |
| C15_G74A_PROOF_ROUTE_SUPERSEDED | PROVED | PASS | - | G74A's dim ker=1 conclusion still holds, but its own original proof route was superseded by dolan-casimir-g2su3 + round59 |
| C19_SPINOR_DECOMPOSITION_AUDIT | CONDITIONAL | PASS | - | 32-component internal S3xS6 spinor per generation = 16 (particle content) + 16 (CPT conjugates), matching the standard CCM finite-triple con |
| C20_MATTER_GENERATION_FACTORIZATION_THREE_WAY | CONDITIONAL | CONFLICTING | 20260717 | User's H_physical=H_matter(x)H_generation hypothesis splits into a STRONG reading (genuine gauged SU(4) Pati-Salam H_matter) which is BLOCKE |
| C21_G74B_CHIRALITY_SIGN | PROVED | PASS | 20260621 | sign(ind(D+_{S6}(x)S-)) = sign(c3(S-)) = +1, and combined with C2's dim ker=1 per channel, gives the UNIQUE solution dim ker(D+)=1, dim ker( |
| C22_H1A_KILLING_SPINOR_REFUTED | REFUTED | FAIL | 20260717 | The ordinary Riemannian Killing-spinor equation (nabla^LC psi = kappa X.psi) does NOT select t=0/1 -- round S3 already has Killing spinors w |
| C23_H1B_FLATNESS_PARALLEL_SPINOR_PROVED | PROVED | PASS | 20260717 | R^t=0 (Cartan-Schouten flatness) at exactly t in {0,1}, on simply-connected S3, forces a globally nabla^t-parallel spinor which is automatic |
| C24_SIGN_CONVENTION_GAP | SUPPORTED | FAIL | 20260717 | This project's own physics-calibrated structure constant (c=+2, fixed via h_H=3) has the OPPOSITE sign from the literal geometric bracket co |
| C25_H1C_PHYSICAL_SELECTION_OPEN | OPEN | NOT_RUN | 20260717 | Which of t=0 or t=1 (not both, not neither) is physically realized remains completely OPEN. A later round (round80/E14) found a genuine isom |
| C26_SU2LR_REP_PATTERN_SPECULATIVE | SUPPORTED | PASS | 20260717 | The t=0 spinor is an exact SU(2)_L singlet / genuine SU(2)_R doublet; the t=1 spinor (existing only under c0=-2, see C24) is an exact SU(2)_ |
| C27_MULTIPLICITY_2_FAIL | REFUTED | FAIL | 20260717 | dim_C ker(D_{S3,t=0}) = 2, not 1 -- confirmed by two independent methods (Peter-Weyl representation theory; direct symbolic construction). T |
| C28_OB10_GEOMETRIC_BUNDLE_PSEUDOREAL | REFUTED | FAIL | 20260803 | [RETRACTED 2026-08-09 -- SEE C32.] Original claim: the 16-dim geometric S3xS6 Clifford module is PSEUDOREAL (B*conj(B)=-I), with mixed signa |
| C29_OB11_CONDITION_I_SU3_BLOCK_STRUCTURE | SUPPORTED | PASS | 20260803 | OB11 condition (i) [SU(3)_c part -- the only non-trivial part, since SU(2)_L x SU(2)_R lives on S3 only and never acts on the S6-side 8_v/8_ |
| C30_OB2_MATRIX_T_Z2_EXCHANGE_PARTIAL | SUPPORTED | PASS | 20260803 | Codex item 5 (OB2/OB6): promoting t from a discrete label to a general rank-1 Hermitian projector T (Bloch-sphere parametrized) admits the i |
| C31_C27_MAJORANA_BRANCH_CLOSED | REFUTED | FAIL | 20260806 | [REASONING RETRACTED 2026-08-09 (C32); CONCLUSION REINSTATED 2026-08-10 (C33).] Original claim: the 'new reality/Majorana condition' row of  |
| C32_OB10_CORRECTED_TYPE_IS_REAL | SUPPORTED | PASS | 20260809 | CORRECTION of C28 and C31. The geometric S3xS6 spinor module's reality type is REAL, not pseudo-real. C28's mixed Cl(6,3) signature was an a |
| C33_MAJORANA_DOES_NOT_RESOLVE_MULTIPLICITY_2 | SUPPORTED | PASS | 20260810 | The Majorana condition does NOT resolve C27's multiplicity-2, and C32's inference that the corresponding Relaxation Map row is OPEN was an o |
| C34_CLIFFORD_CONVENTION_REPO_AUDIT | SUPPORTED | PASS | 20260810 | Repo-wide audit for the convention mixing OB10 hit: NO SECOND INSTANCE EXISTS, but a distinct systematic LABEL inversion does. Scanned 370 . |
| C35_THETA_IS_NOT_A_REAL_STRUCTURE | SUPPORTED | PASS | 20260810 | C30's antiunitary Theta = i*sigma_2*K does NOT fill the NCG real-structure slot, and structurally cannot. Theta was built to satisfy Theta T |
| C36_JF_SQUARE_IS_PLUS_ONE_NOT_MINUS_ONE | SUPPORTED | PASS | 20260810 | The project's recorded value J_F^2 = -1 for G18's finite spectral triple is WRONG in prose and RIGHT in code; the correct value is J_F^2 = + |
| C37_T_SELECTION_REQUIRES_TORSION_ODD_TERM | SUPPORTED | PASS | 20260810 | Any t-dependent quantity that is an EVEN function of (t-1/2) is identically blind to the t=0 vs t=1 question, because t -> 1-t is exactly (t |
| C38_T_KERNELS_ARE_THE_TWO_SPIN4_HALVES | SUPPORTED | PASS | 20260810 | ker(D_S3, t=0) and ker(D_S3, t=1) are the two chiral halves of ONE 4-dimensional Spin(4) spinor, not two competing 2-dimensional kernels. [V |
| C39_IOTA_IS_PARITY_NOT_GAUGE | PROVED | PASS | 20260810 | iota(g) = g^-1 is an ORIENTATION-REVERSING isometry of S3, hence a parity-like discrete symmetry and NOT a gauge redundancy. [VERIFIED-numpy |
| C40_LEMMAB_DEGRADATION_IS_COMPUTABLE_AND_LOOSENS | SUPPORTED | PASS | 20260810 | G74A's Lemma B degrades DISCRETELY and COMPUTABLY under G2-breaking, and the degradation LOOSENS the bound rather than preserving it. Lemma  |
| C41_S6_FACTOR8_WAS_A_WRONG_PAIRING | SUPPORTED | PASS | 20260810 | The 'S6-side factor 8' I reported earlier the same day does not exist -- it was a wrong pairing, and the unified rule holds on BOTH factors. |
| C42_C11_FORCED_ONTO_TWO_OPERATOR_READING | PROVED | PASS | 20260810 | The one-operator escape from C11 is closed: NO member of the Cartan-Schouten family has a 4-dimensional kernel, so 'both t are realized' can |
| C43_BLOCK_SUPPLIES_THE_GRADING | SUPPORTED | PASS | 20260810 | The block D^0 (+) D^1 supplies the grading that C35 proved impossible for a single operator, and it does so because the two sectors are a pa |
| C44_C43_GRADING_IS_GENERIC_IN_T | PROVED | PASS | 20260810 | C43's grading is GENERIC, not specific to t=0,1, so it may not be cited as evidence that the t=0/t=1 doubling is structurally motivated. [VE |
| C45_ALGEBRA_DOES_NOT_EARN_THE_DOUBLING | REFUTED | FAIL | 20260810 | REFUTED AS WORDED. The proposed C45 was: 'there is a natural algebra A on (H, D_block, gamma) satisfying the axioms available at this stage, |
| C46_DOUBLING_IF_TAKEN_IS_A_PARITY_DOUBLING | PROVED | PASS | 20260810 | If the doubling is taken, it is a PARITY doubling: the second sector necessarily carries f o iota, not a free second copy and not a duplicat |
| C47_FOUR_DIM_KERNEL_IS_AN_ISOLATED_POINT | PROVED | PASS | 20260810 | The 4-dim kernel matching C38's Spin(4) spinor is an ISOLATED POINT of the admissible off-diagonal deformation family, not a stable feature  |
| C48_J_FORCES_ALPHA_BETA_ZERO_BUT_KILLS_THE_MAXIM | PROVED | PASS | 20260810 | TWO results pulling in opposite directions, both recorded. (1) THE DEFORMATION IS KILLED. [VERIFIED-numpy] beta = 0 by BOUNDEDNESS: [beta D^ |
| C49_EVEN_INDEX_PAIRING_VANISHES_PD_FAILS | PROVED | PASS | 20260810 | The doubled even triple's index pairing vanishes IDENTICALLY, so a NECESSARY condition for Poincare duality FAILS: the fundamental class it  |
| C50_NO_J_ADMITS_A_SECTOR_MIXING_ALGEBRA | PROVED | PASS | 20260810 | REFUTES the proposed C50 ('a non-factorizing J readmits a sector-mixing algebra') and thereby UPGRADES C48's result 2 and C49 from ANSATZ-LI |
| C51_MIXING_WITHOUT_A_UNITARY_IS_ALSO_EXCLUDED | PROVED | PASS | 20260810 | REFUTES the proposed C51 ('a sector-mixing algebra containing no sector-swap unitary admits a J') and SUBSUMES C50 as its f == 1 special cas |
| C52_ORIENTABILITY_FAILS_BY_LOCALITY | PROVED | PASS | 20260810 | REFUTES the proposed C52 and closes Y2 by a route that owes NOTHING to the C48-C51 J-chain. Y2 IS a real escape from that chain, as predicte |
| C53_A_TENSOR_AOP_DOES_NOT_REPAIR_ORIENTABILITY | PROVED | PASS | 20260810 | REFUTES the proposed C53 and closes CAVEAT O, the sub-point C52 explicitly left open. The A (x) A^op formulation of orientability puts J b*  |
| C54_CAVEAT_O_PRIME_DISSOLVED_SPAN_NOT_DECOMPOSIT | PROVED | PASS | 20260810 | REFUTES the proposed C54 and closes CAVEAT O' -- the LAST technically open door in the C11 line. THE WORRY WAS NOT EMPTY: cancellation is re |
| C55_A1_VERIFIED_IOTA_FLIPS_THE_DIRAC_OPERATOR | PROVED | PASS | 20260810 | A1 is DERIVED, after ten rounds of being carried as an inherited assumption. On S^3 = SU(2) with the bi-invariant metric, Peter-Weyl gives L |
| C56_UIOTA_SQUARED_SIGN_IS_A_CHOICE_NOT_AN_OBSTRU | PROVED | PASS | 20260810 | THE C45 FLAG WAS A FALSE ALARM, carried for ten rounds. C45 recorded U_iota^2 = +-1 as OPEN and 'needed for gamma^dag = gamma'; after C55 di |
| C57_KO_TUPLE_IS_PIN_INDEPENDENT_KO_2_OR_4 | PROVED | PASS | 20260810 | REFUTES the proposed C57 as worded and CORRECTS my own C56. C56's U5 said the eps'' sign of the KO tuple FLIPS with the Pin+/Pin- choice; it |
| C58_OB1_NOT_REOPENED_BY_C11_CHAIN | SUPPORTED | PASS | 20260810 | Step 7 of the day's agreed C11 portfolio was N_gen=3, deferred throughout C41-C57. Checked honestly per the Adaptive Iteration Branch Rule ( |
| C59_A1LIFT_DISCHARGED_BY_SCHUR | PROVED | PASS | 20260810 | ASSUMPTION A1-lift (flagged in C55: 'the geometric spinor lift may differ from the bare pullback by a unitary... a much weaker input than A1 |
| C60_KO_SPLIT_IS_REAL_NOT_GAUGE | PROVED | PASS | 20260810 | REFUTES the proposed C60 ('a sector-only automorphism relates k=I and k=s3, making the KO-2/KO-4 split of C57 a gauge artifact') and thereby |
| C61_OB11II_MIXING_NOT_EXCLUDED_BY_SU3_NECESSARY_ | SUPPORTED | PASS | 20260810 | OB11(ii) (no channel-mixing terms in the Dirac operator) tested at the cheapest tractable level -- the S6-restricted, pointwise SU(3)-equiva |
| C62_OB11III_SU3_TRIALITY_FIXED_INDEPENDENT_CONST | SUPPORTED | PASS | 20260810 | OB11(iii) (triality acting purely as 1(x)t, no admixture on the matter factor), attacked at the cheapest tractable level -- a cross-construc |
| C63_THREE_CHANNELS_PROVABLY_NOT_REDUNDANT | SUPPORTED | PASS | 20260810 | Step-4 red-team (user-posed): can a change of basis reduce the three triality channels to one physical degree of freedom -- is N_gen=3 secre |
| C64_S3_TORSION_MECHANISM_NEVER_MULTIPLICITY_SAFE | SUPPORTED | PASS | 20260810 | Step-5 (scoped, user-agreed): does the one candidate mechanism this project has on record for giving the full S3xS6 Dirac operator a nonzero |
| C65_ROUND59_SIGMA_SAME_SU3_MODULE_AS_TRIALITY_CH | SUPPORTED | PASS | 20260810 | OB11(ii) hard half, step 1 of a multi-step bridge: does round59's real, already-PROVED (dim ker(D_S6,twisted)=1) curvature-twisted Clifford  |
| C67_MCRAE_2025_CONFIRMED_STATE_LEVEL_TRIALITY_GE | SUPPORTED | PASS | 20260810 | OB11(iii) hard half: is the state-level triality operator (mapping an actual vector in 8_v to a vector in 8_s) genuinely open in the literat |
| C68_COMPLEXIFICATION_BRIDGE_LOCALIZED_NOT_RESOLV | SUPPORTED | PARTIAL | 20260811 | OB11(ii) hard half, directed follow-up to an external review of this project's own session: does dropping the real-coefficient constraint fr |
| C69_GROUND_TRUTH_REFUTES_C68_HYPOTHESIS_OBSTRUCT | SUPPORTED | PASS | 20260811 | OB11(ii) follow-up, same arc as C68: ground-truthed the entire correspondence pipeline on a known case (G102's su(3) matched against ITSELF  |
| C70_ROUND59_G102_INTERTWINER_FOUND_OB11II_HARD_H | SUPPORTED | PASS | 20260811 | OB11(ii) follow-up, superseding the C68/C69 Cartan-Weyl root-matching pipeline with an independent, pipeline-free method: a direct global no |
| C71_TRIALITY_BRIDGE_EXTENDED_MONODROMY_TEST_TAUT | SUPPORTED | PARTIAL | 20260811 | OB11(ii) follow-up, C70 continuation: extended the round59<->G102 su(3) bridge from channel_v alone to all three triality channels [VERIFIED |
| C72_G2_EQUIVARIANCE_SWEEP_BRIDGE_SURVIVES_TO_G2_ | SUPPORTED | PASS | 20260811 | OB11(iii) follow-up, state-level triality obstruction scoped as an equivariance-algebra sweep after C71 proved T^3=1 (via chaining independe |
| C73_ROUND59_DIRAC_BATTERY_CHIRALITY_DIRECT_DEFOR | SUPPORTED | PARTIAL | 20260811 | Full battery on round59's real twisted D_S6 (the only non-surrogate curvature-twisted Dirac operator in this project). Precise-target correc |
| C73B_GENUINE_2PARAM_TORSION_FAMILY_KERNEL_PROTEC | SUPPORTED | PARTIAL | 20260811 | C73 follow-up, per user direction after reviewing C73 (rated 9.4/10): built a genuine multi-parameter admissible-connection test rather than |
| C74_PRODUCT_LOWEST_SECTOR_GROUNDWORK_RIGOROUS_TR | SUPPORTED | PARTIAL | 20260811 | Full product lowest-sector round, framed per predictions_before_data.md's own P5 (NOT re-testing KT-8's already-NULL full-kernel result, NOT |
| C75_GATE2_PHYSICAL_D_VS_EXTENDED_SYMMETRY_NO_RED | SUPPORTED | PASS | 20260811 | TRIALITY_DISTINGUISHABILITY_GATE.md's Gate 2 (does the physical Dirac operator commute with the extended, channel-distinguishing symmetry Ga |
| C76_STATUS_SYNTHESIS_PRECOMMITMENT_NOT_TRIGGERED | SUPPORTED | PASS | 20260811 | Status-synthesis round closing the C70-C75 decisive-experiment program (predictions_before_data.md), re-grading N_gen=3 against the frozen P |
| C77_SO4XSO4_GATE2_ALSO_NO_ALL_12_T_BRIDGE_SCOPED | SUPPORTED | PASS | 20260811 | Follow-up to C76's own named next lead: attempted to bridge round119's SO(4)+SO(4) triality-automorphism matrix T into round59's real D. [VE |
| C78_EXHAUSTIVE_SO8_COMMUTANT_OF_D_EQUALS_SU3_EXA | SUPPORTED | PASS | 20260811 | Genuinely new construction (per user direction, after C77 found the T-bridge needs infrastructure that doesn't exist): instead of testing ha |
| C79_NONPRODUCT_COUPLING_ATTEMPT_NULL_UV_NONUNITA | SUPPORTED | PARTIAL | 20260811 | Genuinely new construction, per user direction ('go for the non-product construction'): every prior round (C70-C78) tested symmetries of rou |
| C80_ANTISELFDUAL_COMPLETION_METHODOLOGY_FLAW_IDE | SUPPORTED | PASS | 20260811 | Self-directed round (user left C80's scope open): completes C79's self-dual/anti-self-dual pair and re-synthesizes C76-C79. [VERIFIED-numpy] |
| C81_RAW_KERNEL_EXCLUDED_RETEST_CLEAN_NULL_BOTH_H | SUPPORTED | PASS | 20260811 | Implements C80's own named fix (per user direction: 'Fix the test design and re-run so(4)_1 both halves'). D_S6's spectrum read directly: ex |
| C82_SO4_2_RAW_KERNEL_EXCLUDED_CLEAN_NULL_BOTH_HA | SUPPORTED | PASS | 20260811 | Per user direction ('Continue with C82 -- test so(4)_2'): applies C81's corrected (raw-kernel-excluded) non-product coupling test to round11 |
| C83_SU3_OVERLAP_FOUND_9DIM_REMAINDER_TESTED_FULL | SUPPORTED | PASS | 20260811 | Per user direction ('test the remaining complement elements'): a NEW finding made while scoping, computed not guessed: round119's so(4)_1+so |
| C84_SIGMA_MINUS_BRANCH_CLEAN_NULL_N1_NAIVE_ANSAT | SUPPORTED | PASS | 20260812 | Per user direction ('try the full Peter-Weyl tower'): scoping (re-reading Agricola 2002 directly, tracing C74/C79-C83's own WORKING CODE not |
| C85_MEIER_EQ63_REPAIRED_SUBSTRATE_CERTIFIED_INDE | SUPPORTED | PASS | 20260812 | Following C84's own provenance gap (the 'Sire & Xu' citation attached to round67's S3 Dirac multiplicity formula does not actually contain i |
| C86_FULL_K1_N0_N1_JOINT_COUPLING_TEST_CLEAN_NULL | SUPPORTED | PASS | 20260812 | Per the external reviewer's C84B proposal (compute selection-rule matrix elements to determine whether C79-C83's coupling operator T is diag |
| C87_FULL_K2_N1_N2_JOINT_COUPLING_TEST_CLEAN_NULL | SUPPORTED | PASS | 20260812 | Extends C86's joint-level coupling test one level deeper: level k=2's own full 18-dim S3 Hilbert space was [VERIFIED-numpy] confirmed to con |
| C88_Z_I_HAS_NONZERO_MATRIX_ELEMENTS_BETWEEN_ADJA | SUPPORTED | PASS | 20260812 | Found while scoping the round after C87, then investigated properly (not smoothed over): C87's own d_joint_base was genuinely non-Hermitian  |
| C89_SO4_2_FULL_K1_JOINT_TEST_CLEAN_NULL | SUPPORTED | PASS | 20260812 | Extends C86's n=0<->n=1 joint coupling test (level k=1's full certified Hilbert space) to round119's so(4)_2 (BLOCK2=[4,5,6,7], so4_all[6:12 |
| C90_STRUCTURAL_NOGO_TRANSLATION_GENERATOR_COUPLI | SUPPORTED | PASS | 20260812 | An external reviewer proposed assembling C86/C87/C89's per-level tests into one block-tridiagonal Peter-Weyl Dirac matrix D_PW and testing t |
| C91_REMAINDER_AND_CENTRALIZER_JOINT_K1_CLEAN_NUL | SUPPORTED | PASS | 20260812 | Extends C86/C89's joint k=1 coupling test to the two remaining untested so(8)-adjacent candidates named as next steps in C89's own decision. |
| C92_LEFT_REGULAR_GENERATOR_NAIVE_ANALOG_BLOCKED_ | SUPPORTED | PASS | 20260812 | First concrete step toward building the q-side ('left-regular-representation') generator needed for task #59's multiplication-operator const |
| C93_DUAL_REPRESENTATION_Q_SIDE_GENERATOR_VALID_S | SUPPORTED | PASS | 20260812 | Continues task #59's q-side generator scoping after C92. Scoping clarified WHY C92's quaternion left-multiplication approach hit an obstruct |
| C94_GROUP_ACTION_CERTIFICATION_SIGN_CORRECTED_BU | PARTIALLY_SUPPORTED | PARTIAL | 20260812 | Directed by an external reviewer's proposal: stop hand-deriving the q-side generator sign (C92/C93 showed real risk -- +l_{e_i}^T and -l_{e_ |
| C95_COEFFICIENT_SPACE_BRACKET_RESOLVED | SUPPORTED | PASS | 20260812 | Resolves C94's own P3 bracket-consistency contradiction. Root cause: C94 computed 'how g0's own raw matrix entries transform' under h(eps)^- |
| C96_K2_REPLICATION_DIVERGES_L_R_ROLES_SWAP | SUPPORTED | PASS | 20260812 | Tests whether C95's k=1 q-side generator formula (L_i=+l_{e_i}(1) directly, R_i=-l_{e_i}(1)^T) generalizes to k=2 (spin-1), per the reviewer |
| C97_K3_MATCHES_K2_PARITY_HYPOTHESIS_FALSIFIED | SUPPORTED | PASS | 20260812 | Tests whether the L/R role-swap found between C95 (k=1: L_i=+l_{e_i}(1), R_i=-l_{e_i}(1)^T) and C96 (k=2: L_i=-l_{e_i}(2)^T, R_i=+l_{e_i}(2) |
| C98_K4_CONFIRMS_K2_K3_STABILITY_HYPOTHESIS_3_POI | SUPPORTED | PASS | 20260812 | Tests whether the tentative 'k=1 is a distinct base case, k>=2 follows one fixed rule' picture (proposed in C97's decision.md after the pari |
| C99_MAGNETIC_LABELING_VERIFIED_K1_EXTREMAL_INDEX | SUPPORTED | PASS | 20260812 | Prerequisite check before building the actual multiplication-type coupling operator (task #59, C90's own explicit next step): extracts the m |
| C100_FULL_CG_MULTIPLICATION_OPERATOR_ASSEMBLED_I | SUPPORTED | PASS | 20260812 | Builds the FULL (q,p)-only multiplication-type coupling operator matrix M_k, level k -> level k+1, for k=1,2,3, using the standard D^k_{q,p} |
| C101_TWO_LEVEL_DPW_SPECTRAL_SHIFT_FOUND_REAL_SPE | SUPPORTED | PASS | 20260812 | Builds the smallest possible instance of the truncation-convergence/spectral-flow test C90's own decision.md scoped as the final endpoint of |
| C102_REAL_SPECTRUM_REPLICATES_AT_K2K3_STRUCTURAL | SUPPORTED | PASS | 20260812 | Repeats C101's exact 2-level D_PW construction at k=2,3 (instead of k=1,2), code reused verbatim (only level arguments changed), to test whe |
| C103_BLOCK_TRIDIAGONAL_DPW_BUILT_TRUNCATION_APPE | SUPPORTED | PASS | 20260812 | Builds the first genuinely block-tridiagonal D_PW (k=1,2,3, BOTH M_1 and M_2 simultaneously as adjacent-level off-diagonal couplings), the l |
| C104_SUMMED_COMPONENTS_PRODUCE_CLEAN_FOURFOLD_MI | SUPPORTED | PASS | 20260812 | Tests whether summing all four D^1_{a,b} components (a,b in {+1/2,-1/2}) produces genuine mixing, instead of C100's own single-component (a= |
| C105_BLOCK_DIAGONAL_S_RULED_OUT_LEVEL_LOCAL_FORM | SUPPORTED | PASS | 20260812 | Searches for the candidate similarity transform S (C101's own pearl-registry open question) explaining why the coupled D_PW spectrum is exac |
| C106_R_COUPLED_CLIFFORD_ALTERNATIVE_ALSO_REAL_R_ | SUPPORTED | PASS | 20260813 | Tests whether the 'r-untouched' ansatz (B_1=M_1(x)I_r, used throughout C101-C103/C105, flagged as a postulated/unverified simplification in  |
| C107_NAIVE_MEIER_KOSTANT_BRIDGE_FALSIFIED_EXACTL | REFUTED | FAIL | 20260829 | Following boyko-project-radar (full-project scan, 2026-08-29) and /tracy's converged recommendation -- the C90-C106 Peter-Weyl multiplicatio |
| C108_SUMMED_MIXING_BREAKS_REALITY_AT_K1_ONLY_HOL | SUPPORTED | PASS | 20260830 | Returns to the pure C90-C106 numerical track (after the C107 OB1-bridge detour) and runs the test C104's own decision.md flagged as a natura |
| C109_K1_ANOMALY_REQUIRES_FULL_4COMPONENT_INTERFE | SUPPORTED | PASS | 20260830 | Diagnoses C108's own open pearl (why is k=1 anomalous under M_k^sum?) via targeted structural/symbolic diagnosis, not another numeric sweep. |
| C110_COVARIANCE_HYPOTHESIS_REFUTED_NO_SINGLE_CRI | REFUTED | FAIL | 20260830 | Tests C109's own pearl (does covariance -- a coupling corresponding to a genuine real quaternion coordinate function, zero symbolic imaginar |
| C111_EXCEPTIONAL_POINT_MECHANISM_CONFIRMED_FOUR_ | SUPPORTED | PASS | 20260830 | Follows up on C110's own pearl (a full 4-complex-parameter symbolic sweep) via the single most natural 1-parameter slice: D_PW(t) with off-d |
| C112_J1_EQ_J2_INSUFFICIENT_AT_TESTED_POINTS_TARG | CONDITIONAL | PASS | 20260830 | Follows up on C109's own pearl (does an analogous resonance recur at higher spin under a matching auxiliary representation, j2=k/2). DDD des |
| C113_J2_ZERO_ALGEBRAICALLY_INCAPABLE_OF_BREAKING | PROVED | PASS | 20260830 | C112's artifact review named j2=0 (trivial/singlet auxiliary) as the one way to reach target_level=2 with j1!=j2 inside the tested construct |
| C114_SUBSET_BREAKS_REALITY_CONFIRMED_NOT_TRIVIAL | SUPPORTED | PASS | 20260830 | Surfaced by narrow-discovery-engines Engine 2 (Constraint Relaxation Search) run against the C90-C113 construction family's own unquestioned |
| C115_ASYMMETRIC_RULE_CONFIRMED_AT_J2_GEQ_3HALVES | SUPPORTED | PASS | 20260830 | Third matched-diagonal cell (j1=j2=2, 25 components) built as a third data point for C114's own open mechanism question. Full sum real (P0), |
| C116_REALITY_PRESERVING_WINDOW_NARROW_J2_1_AND_J | SUPPORTED | PASS | 20260830 | Decisive test named by C115's own FL Step 8a skeptic review: does the asymmetric rule's own prediction for a=0 removals hold at j2=3 (49 com |
| C117_ASYMMETRIC_RULE_VERIFIED_SUPPORT_IS_N4_N5_O | SUPPORTED | PASS | 20260831 | User-requested resolution of the j2=5/2 (n=6) gap the C116-addendum skeptic pass had named. Built the matched-diagonal cell j1=j2=5/2 (k_sou |
| C118_DENSITY_HYPOTHESIS_TEST_RETRACTED_NOT_SUPPO | OPEN | FAIL | 20260831 | User requested the cheap eigenvalue-density check named by C117's own skeptic pass. v1 (global minimum eigenvalue gap vs component norm): su |
| C119_BISMUT_RICCI_FLAT_CANDIDATE_KILLED_ON_F1_S6 | REFUTED | FAIL | 20260831 | PARENT_ACTION_GATE.md field F1 test of a candidate OB1 t-selection mechanism (Bismut-Ricci-flat condition Rc(g)=(1/4)H^2, from the generaliz |
| C120_I9_GATE_CHECK_REFERENT_RECONSTRUCTED_TO_ROU | OPEN | FAIL | 20260831 | User-requested gate-fill check (no computation) of an externally-proposed OB1 F4 candidate, 'I9 ∝ (2t-1)*Vol(S3)*Vol(S6)', described in a si |
| C121_ETA_INVARIANT_NULL_MOD2_IDENTICAL_ACROSS_IN | REFUTED | FAIL | 20260901 | Computed eta(D^t) (eta-invariant / gravitational Chern-Simons level of the torsion-deformed S3 Dirac operator), the candidate C120's own ske |
| C122_NEGATIVE_CONTROL_PARKED_THREE_ROUNDS_EACH_F | OPEN | FAIL | 20260901 | Attempted the random-matrix negative control C118's own skeptic pass named for the density hypothesis. Three rounds within this one experime |
| C139_ALTERNATE_TWIST_M_KERNEL_ZERO | SUPPORTED | PASS | 20260904 | Twisting D_S6 by W'=m_C (complexified tangent/isotropy rep, module type 3+3bar, dim 6, ZERO su(3) singlets) instead of Sigma (module type 1+ |
| C141_KERNEL_IS_GRADED_BRANCHING_FLOOR_NOT_DYNAMI | SUPPORTED | FAIL | 20260904 | Testing whether D_S6 discriminates Sigma from a twist bundle W''=m(+)2*1 (dim 8, module type 3+3bar+1+1, matching Sigma's own two-singlet CO |
| C144_ROUND59_UNTWISTED_DIRAC_PROPORTIONAL_TO_KOS | SUPPORTED | PASS | 20260904 | Triggered by the user citing two specific arXiv papers (math/0005056 Landweber, math/0005057-referenced Kostant 1999) while critiquing C143' |
| C145_TWISTED_DIRAC_NOT_KOSTANT_LANDWEBER_MU_BLOC | REFUTED | FAIL | - | User-authorized follow-up to C144 ('го C145'): does C139/C141's own physicist-style twisted Dirac operator D' (Leibniz rule, both Sigma AND  |
| C146_TERM1_VANISHING_IS_SCHUR_FORCED_NOT_M_SPECI | SUPPORTED | PASS | 20260904 | User proposed (post-C145) deriving E_W=D'-D_Kostant analytically and its SU(3)-equivariance as new low-hanging fruit; novelty check found mo |
| C147_CONNECTION_COEFFICIENT_VANISHES_ONLY_AT_ZER | SUPPORTED | PASS | 20260904 | User (consortium message) named this the single highest-value next round: for the invariant-connection class C139 already used, WHEN does th |
| C148_DELTA_GEO_IS_ZERO_IN_EVERY_KERNEL_THIS_PROJ | SUPPORTED | NOT_RUN | 20260904 | Accounting round (NO new computation -- every number read from already-committed results_c139.json and results_c141.json, cell-by-cell skept |
| C149_OB11II_TRANSPORT_STEP_IS_WELLPOSED_FOR_D_SI | SUPPORTED | PASS | 20260904 | Autonomous-session debt audit found a step NAMED but NEVER attempted: OB11(ii) (OPEN_BLOCKERS.md:1782-1791) specifies transporting D, J, gam |
| C150_G44_INFORMATION_RETENTION_GATE_SYNTHESIS_NO | SUPPORTED | NOT_RUN | 20260904 | User proposed (consortium message, 2026-09-04) proving a functorial G44 information-loss theorem: if R: Rep(Spin(8))->Rep(G2) is restriction |
| C151_SU3T2_CARRIES_NO_CONNECTION_COEFFICIENT_PRE | REFUTED | FAIL | 20260904 | Executed the pre-registered blind test of whether C147's holomorphy (c(J.nabla) = i c(nabla)) is a nearly-Kahler universality or a G2/SU(3)  |
| C152_NK_HOLOMORPHY_CONFIRMED_ON_SU3T2_AFTER_SECT | SUPPORTED | PASS | 20260904 | C152 set out to explain WHY Term2 annihilates the T^2-invariant sector on SU(3)/T^2 (C151's unexplained residue; Term1's vanishing was alrea |
| C153_TWIST_CONNECTION_FACTORS_PER_ROOT_PLANE | SUPPORTED | PASS | 20260904 | Explains WHY C152's residual question (why does c(J.grad)=i*c(grad) hold, and why for exactly 2 of the 8 invariant almost-complex structures |
| C154_S6_RATIO_LAW_FORCED_NOT_DISCOVERED_SU3T2_OP | REFUTED | FAIL | 20260904 | Set out to test the real open question C153's novelty check left standing: why does /c(nabla_LC)///mu(nabla_LC)/ = 2/3 exactly on both nearl |
| C155_RATIO_IS_DIMENSIONAL_ARTIFACT_RANK_MISMATCH | SUPPORTED | PASS | 20260905 | Settles, structurally rather than numerically, the /c/-vs-mu question C147 opened and C154 left INCONCLUSIVE. Method chosen specifically to  |
| C156_ROOT_RELATION_RULE_FALSIFIED_AND_REPLACEMEN | REFUTED | FAIL | 20260905 | Attempted, under an explicit user mandate to pursue a discovery autonomously, to turn C155s A_2 observation into a general rule about full f |
| C157_CHIRALITY_BALANCE_PROVEN_CLASSICAL_NOT_DISC | SUPPORTED | PASS | 20260905 | Under an explicit user mandate requiring theorem + out-of-sample test + null model + literature novelty audit + independent skeptic pass ALL |
| C158_WEYL_KERNEL_INVARIANCE_AND_PIN_LIFT_FULLY_F | SUPPORTED | PASS | 20260905 | Under the user's own five-gate discovery mandate (theorem+out-of-sample+null-model+novelty-audit+skeptic ALL FIVE required): built the genui |
| C159_PARITY_OBSTRUCTION_HOLDS_ONLY_FOR_EXCLUSIVE | SUPPORTED | FAIL | 20260905 | Round95's anomaly condition n_L=n_R combined with n_L+n_R=N_gen=3 gives 2n_L=3 with no integer solution, but this is NOT a general impossibi |
| C160_SIGN_TRIPLE_PLUS_PLUS_MINUS_IS_KO_DIM_6_PER | SUPPORTED | PASS | 20260905 | A fetched primary source states the sign-triple <-> KO-dimension correspondence in the same slot order this project uses, and identifies the |
| C161_LAMBDA_ALPHA_RECOMBINATION_UNDERDETERMINED_ | SUPPORTED | INCONCLUSIVE | 20260905 | Mapping C133's coupling Phi = 1_F (x) (lambda_0 w_0 + lambda_1 w_1) onto C136's per-channel, per-(t,frame) alpha data does not yield an answ |
| C162_DELTA_DYN_ZERO_FORCED_FOR_M_PLUS_DECOUPLED_ | SUPPORTED | PASS | 20260906 | For W_cand = 3+3bar+3bar built as m (+) a decoupled extra 3bar (the only instantiation buildable from this project's existing content), the  |
| C163_NO_LICENSE_FOUND_FOR_LAMBDA_ALPHA_IDENTIFIC | SUPPORTED | PARTIAL | 20260906 | No license was found, in the rounds actually checked (C133 decision.md, C132 decision.md, and C38 via C125), for identifying C133's lambda_0 |
| C164_OB14_SUBPATH_SCOPING_INCONCLUSIVE_ONE_CANDI | OPEN | INCONCLUSIVE | 20260906 | Scoping OB14's two sub-paths ((i') avoid m entirely, (ii') couple a new summand to m's tangent bundle) ends INCONCLUSIVE, not with the first |
| C165_CANONICAL_CURVATURE_VANISHES_ON_FUNDAMENTAL | SUPPORTED | PASS | 20260906 | The curvature 2-form R^c of the canonical (Nomizu/Ambrose-Singer) connection of S^6 = G2/SU(3), R^c(X,Y) = -[X,Y]_h, restricted to the funda |
| C166_AHL2023_HAS_NO_SU3_COUPLING_DATA_ON_S6_ISOT | SUPPORTED | FAIL | 20260906 | Reading the primary source (arXiv:2203.02961v3, Agricola-Hofmann-Lawn; LaTeX sections 2.3, 2.4, 4.1.1, 5.1 by the round, plus 4.2-4.4 and 5. |
| C167_DIAGONAL_Z_P_ORBIFOLD_HOLONOMY_ASYMMETRY_FO | PROVED | PASS | 20260906 | For the free left-translation action of Z_p (zeta_p = diag(e^{2 pi i/p}, e^{-2 pi i/p})) on S^3=SU(2), giving the lens space L(p,1): the lef |
| C168_DIAGONAL_Z3_PAIRING_NON_EXCLUSIVE_BUT_FORCE | SUPPORTED | PASS | 20260906 | At the representation-theory / classification level only, with explicit modeling assumptions (spin-level holonomies H_0=I_2 and H_1=zeta_3,  |
| C169_ROUND59_KERNEL_HAS_NO_T_OR_CHANNEL_INDEX_ST | SUPPORTED | NOT_RUN | 20260906 | Round59's certified zero-mode vector (kernel of the su(3)-invariant-sector twisted Dirac operator on S^6, dim ker=1) carries no t-index and  |
| C170_T0_KERNEL_EXPLICIT_T1_CANDIDATE_HOLONOMY_ZE | SUPPORTED | PARTIAL | 20260906 | Item 1 of C169's escalation, attempted in isolation: ker(D_S3(t)) as explicit vectors. At t=0 the spin-connection matrices vanish, M_i(0)=0, |
| C171_ZETA_INVERSE_HOLONOMY_RECONCILES_WITH_C168_ | SUPPORTED | PASS | 20260906 | Substituting H_1'=zeta_p^{-1} (p=3; the holonomy C170 derived for its t=1 candidate psi_1(g)=g^{-1}.psi_0) for H_1=zeta_p in C168's own inva |
| C172_REAL_TWISTED_DS6_KERNEL_IS_36_DIM_CL9_CHECK | SUPPORTED | FAIL | 20260906 | Plugging round59's real twisted D_S6 (64x64 on Sigma (x) Sigma, reused unmodified) into the Cl(9) product framework of round68/E3 with D_S3( |
| C173_ITEM3_TRIALITY_BRIDGE_IMPOSSIBLE_BY_G44_ITE | SUPPORTED | FAIL | 20260906 | C169's escalation item 3 -- a basis bridge from round59's SU(3)-indexed zero-mode space Sigma to the {v,s,c} Spin(8) triality-channel index  |
| C174_NONPRODUCT_COUPLING_CHANNEL_TEST_BLOCKED_BY | SUPPORTED | INCONCLUSIVE | 20260906 | Extending C79's non-product coupling test (S3 Clifford generators Z_i with a so(4)_1 self-dual triple, bridged to round59's Sigma by channel |
| C175_CHARBONNEAU_HARLAND_THM3_GIVES_ZERO_DEFORMA | SUPPORTED | FAIL | 20260906 | Reading Charbonneau and Harland, 'Deformations of nearly Kaehler instantons' (arXiv:1510.07720v2, Commun. Math. Phys. 2016, DOI 10.1007/s002 |
| C176_TORSION_SPECTRAL_ACTION_A2_PREFERS_T_HALF_N | SUPPORTED | FAIL | 20260906 | For S3's Cartan-Schouten torsion family D_S3(t), the leading Seeley-DeWitt term of the spectral action, built from the torsion-corrected for |
| C177_EXACT_S3_SPECTRAL_ACTION_MINIMUM_AT_T_HALF_ | SUPPORTED | FAIL | 20260906 | Computed directly from D^t's exact closed-form spectrum on S3 (D^t(n,sigma) = sigma(n+3/2) + 3(t-1/2), multiplicity (n+1)(n+2) per sign, reu |
| C178_NONPRODUCT_T0_SPECTRUM_SPREAD_ATTRIBUTED_TO | SUPPORTED | INCONCLUSIVE | 20260906 | Degenerate perturbation theory was built inside the 72-dim degenerate subspace C^2(x)ker(D) (dim ker(D)=36 re-verified; v_round59 lies in it |
| C179_MULTIPLET_OF_FUNCTIONS_ON_SPHERE_CANNOT_CAR | PROVED | FAIL | 20260907 | A multiplet of single-valued complex functions on S^n, with the isometry group acting by the induced pullback action on functions, cannot ca |
| C180_S3_SPINOR_HARMONICS_EXPLICIT_DIRAC_SPECTRUM | SUPPORTED | PASS | 20260907 | In the left-invariant (group) trivialization of S^3 = SU(2), spinor fields are C^2-valued functions, and D0 = -i sum_a sigma_a (x) X_a^R, bu |
| C181_GAMMA_PROJECTION_NECESSARY_NOT_SUFFICIENT_A | PARTIALLY_SUPPORTED | PASS | 20260907 | On S^3 with the C180 construction: (a) the gamma projection x_mu = (1/2) Tr(sigma_mu^dag g), g = x0 I + i(x1 s1 + x2 s2 + x3 s3), recovers t |
| C182_S2_SPINOR_SECTORS_BY_HOPF_DESCENT_WEIGHT_LA | SUPPORTED | PASS | 20260907 | Hopf descent S^2 = S^3/U(1): diagonalizing the U(1) fibre generator, weight = -(i/2) X3^R, on the harmonic spaces H_k of S^3 for k = 0..5 gi |
| C183_TERM2_STEP_FAILS_ONLY_ON_S3XS3_ALL_REPS_ISO | SUPPORTED | PASS | 20260908 | For the four homogeneous nearly-Kahler 6-manifolds (S^6 = G_2/SU(3), SU(3)/T^2, CP^3 = Sp(2)/(Sp(1)xU(1)), S^3xS^3 = SU(2)^3/SU(2)_diag), th |
| C184_S2_DOUBLET_DERIVED_DOUBLE_VALUED_BILINEAR_S | SUPPORTED | PASS | 20260908 | Exact symbolic arithmetic (sympy over Q and Q(i), no floats in any verdict; 33/33 + 18/18 + 8/8 checks). (1) The lowest S^2 spinor doublet,  |
| C185_S2_DIRAC_OPERATOR_BUILT_SPECTRUM_PLUS_MINUS | SUPPORTED | PASS | 20260908 | The Dirac operator on the round unit S^2 was built from the metric rather than quoted (frame; Cartan's first structure equation solved and c |
| C186_S3_EIGENSPINORS_K2_K3_EXACT_CANONICAL_WEIGH | SUPPORTED | PASS | 20260909 | Exact arithmetic over Q(i), no floats in any verdict (34/34 checks): for k = 2 and k = 3 on S^3, D0 = -i sum_a sigma_a X_a^R satisfies (D0 + |
| C187_EULER_ANGLE_REDUCTION_FAST_BUT_VIELBEIN_D_F | SUPPORTED | PARTIAL | 20260909 | For the S^3 Dirac operator in Euler angles (theta,phi,psi) built from a vielbein and a Cartan-solved spin connection, the half-angle substit |
| C188_QUATERNION_NATIVE_EULER_ANGLE_DIRAC_REPRODU | SUPPORTED | PASS | 20260909 | Building the S^3 Dirac operator in Euler angles directly as D = -i sum_a sigma_a X_a^R, with X_a^R the quaternion right-multiplication gener |
| C189_DERIVED_SPIN_CONNECTION_SHIFT_IS_MINUS_3_2_ | SUPPORTED | PASS | 20260909 | On the unit S^3 with the orthonormal frame {X_a^R} (g(X_a^R,X_b^R)=delta_ab exactly), the Levi-Civita spin connection was solved from Cartan |
| C190_LEFT_ACTING_SHIFT_PLUS_3_2_RIGHT_MINUS_3_2_ | SUPPORTED | PASS | 20260909 | For the left-acting S^3 Dirac operator D_0^L = -i sum_a sigma_a X_a^L, the Levi-Civita spin connection in the orthonormal frame {X_a^L} was  |
| C191_P5_POSTULATE_ALONE_CANNOT_SEPARATE_8S_FROM_ | SUPPORTED | FAIL | 20260909 | Under the explicit postulate that one so(4) summand of the SO(4)xSO(4) in Spin(8) block-chirality construction is S^3's own SU(2)_L x SU(2)_ |
| C192_P10_REPRODUCES_UNDER_PYGAE_CLIFFORD_GAMMA_R | SUPPORTED | PASS | 20260909 | C191's P10 (8_s and 8_c have identical (j_L,j_R) content under so(4)_1 alone) reproduces when the Cl(8,0) generators Gamma_i are rebuilt ind |
| C193_SPIN_LIFT_IS_EXACT_ANTI_HOMOMORPHISM_AND_J_ | SUPPORTED | PARTIAL | 20260909 | The function spin_lift of round59_route_a_independent.py (so(6) -> spin(6) on the 8-dim Lambda-L' presentation of Sigma) satisfies [spin_lif |
| C194_SINGLE_HOPF_FRAME_CANDIDATE_REPRODUCES_K1_N | SUPPORTED | FAIL | 20260910 | The candidate frame map psi = U(theta,phi,psi)*v (U = the Euler/Hopf SU(2) matrix of C184, v a constant 2-vector) does NOT give the four k=0 |
| C195_CHI_DIFFERENCE_JUMP_VANISHES_ONLY_AT_EQUATO | PROVED | PASS | 20260910 | For the S^2 doublet of C184, chi_{+1/2} = e^{-i phi/2} cos(theta/2) and chi_{-1/2} = e^{i phi/2} sin(theta/2), both anti-periodic under phi  |
| C196_K3_DESCENT_GIVES_GENUINE_SPIN_WEIGHT_3_2_S2 | SUPPORTED | PASS | 20260910 | Applying the C184b fibre-descent recipe (diagonalise the fibre generator, split the weight degeneracy with the second generator, substitute  |
| C197_K3_DESCENT_GIVES_SECOND_GENUINE_SPIN_WEIGHT | SUPPORTED | PASS | 20260910 | At k=3, fibre weight -1/2, m_R=-1/2, after Hopf substitution and stripping the psi-phase, the descent method gives q = e^{-i phi/2} cos(thet |
| C198_KERNEL_LINE_EXACTLY_FIXED_ACROSS_C73B_TORSI | SUPPORTED | FAIL | 20260917 | Across the 13-angle torsion family of C73b (kernel_dim = 1 at all 13 angles, matching C73b's saved results) the unit kernel line of D(theta) |
| C199_LEAN_PROVES_EQUIVARIANT_ISO_FORCES_EQUAL_HO | PROVED | PASS | 20260918 | A complete Lean 4 proof (Lean v4.34.0, mathlib v4.34.0; lake build succeeds, 1589 jobs, zero errors, zero sorry/admit in Homschwarz/Basic.le |
| C200_MORPHISM_AUDIT_VERDICT_DEPENDS_ON_SIGNATURE | PARTIALLY_SUPPORTED | PARTIAL | 20260919 | Instrument-validation round for a 5-outcome 'morphism mapping audit' (EXACT / PARTIAL / HOMOMORPHISM / QUOTIENT / NO_BRIDGE) run on nine obj |
| C201_L1_LADDER_SQRT2_EXACT_INTERTWINER_TEST_CALI | PROVED | PASS | 20260922 | Using only McMurry's stated polar-form L+/- and l=1 spherical harmonics, exact sympy computation gives L+Y(1,-1)=sqrt(2)Y(1,0), L+Y(1,0)=sqr |
| C202_CORRESPONDENT_L1_MATRICES_EQUIVALENT_TO_C20 | PROVED | PASS | 20260923 | The correspondent's 3x3 l=1 so(3) generator matrices (T_12, T_23, T_31 in a complex basis), reconstructed here exactly from defining-represe |
| C203_SU3_IN_SO6_THREE_CONSTRUCTIONS_SAME_REP_TYP | SUPPORTED | PARTIAL | 20260923 | Three independently built real 6-dimensional orthogonal su(3) representations -- A: the project's G2/SU(3)-on-S6 construction (G96: stabiliz |
| C205_CARTESIAN_L1_ROTATION_GENERATORS_ROW_INPUT_ | PROVED | PASS | 20260923 | Exact sympy differentiation of the Cartesian rotation generators Lx=i(z d/dy - y d/dz), Ly=i(x d/dz - z d/dx), Lz=i(y d/dx - x d/dy) on the  |
| C206_LADDER_OPERATORS_POLAR_AND_CARTESIAN_SQRT2_ | PROVED | PASS | 20260923 | Exact sympy: (A) McMurry's polar-form ladder operators give on the l=1 harmonics L+y(1,0)=sqrt(2)y(1,1), L+y(1,-1)=sqrt(2)y(1,0), L-y(1,0)=s |
| C207_ECSK_C134_VACUUM_EINSTEIN_VIOLATED_AT_T_HAL | SUPPORTED | FAIL | 20260924 | At t=1/2 -- the one point where C134's torsion equation of motion is self-consistent and where KT-8 (no zero modes) makes the fermion stress |
| C210_G96_G2_BASIS_REPRODUCES_STANDARD_ROOT_SYSTE | SUPPORTED | PASS | 20260927 | Extracting a Cartan subalgebra and root system from G96's own 14-generator octonion-derivation basis of g2 (7x7 real antisymmetric matrices) |
| C211_CSDR_GRAVITY_MODULI_POTENTIAL_TERMS_ON_S6_G | SUPPORTED | PASS | 20261002 | The gravity-only terms of the CSDR metric-moduli potential (Chatzistavrakidis-Manousselis-Prezas-Zoupanos arXiv:0712.2717 eq. 4.27) were eva |
| C212_NEARLY_KAHLER_TORSION_3FORM_ON_S6_G2_SU3_NO | SUPPORTED | PASS | 20261002 | The characteristic-connection torsion 3-form of S6=G2/SU(3), T^c(X,Y,Z) = -<N,(XxY)xZ> (Agricola-Borowka-Friedrich arXiv:1707.08591 Prop. 4. |
| C213_S6_RICCI_VIA_CASTELLANI_FORMULA_EINSTEIN_IS | SUPPORTED | PASS | 20261002 | S6=G2/SU(3)'s Ricci tensor was computed with Castellani's rescaled-coset curvature formula (arXiv:hep-th/9912277 eq. 3.35-3.36), structure c |
| C214_TORSION_RICCI_BASIS_MISMATCH_FOUND_BRIDGE_R | SUPPORTED | PASS | 20261002 | Established: C212 (torsion) and C213 (Ricci) were computed in different metric normalizations (tangent Gram = I/3, rescale factor sqrt(3));  |
| C215_FRIEDRICH_IVANOV_RELATION_ON_S6_COMPONENTWI | SUPPORTED | PASS | 20261002 | Friedrich-Ivanov's relation for a metric connection with skew torsion (arXiv:math/0102142 sec. 2), Ric^g = Ric^grad - (1/4) sum g(T(e_i,X),T |
| C216_KOBAYASHI_NOMIZU_ROUTE_GIVES_RIC_C_4_ON_S6_ | SUPPORTED | FAIL | 20261002 | The Kobayashi-Nomizu canonical-connection route (R^c(X,Y)Z = -[[X,Y]_h,Z], T^c = -[X,Y]_m, pure Lie bracket, no octonions) was calibrated on |
| C217_CASTELLANI_CURVATURE_IS_HALF_STANDARD_CONVE | SUPPORTED | PASS | 20261003 | C213's Castellani-formula curvature is exactly 1/2 of the standard curvature: eq. (3.34) defines R^a_b = R^a_{b de} V^d ^ V^e without the st |
| C218_EXPLICIT_REAL_STRUCTURE_J_ON_ROUND59_SIGMA_ | SUPPORTED | PASS | 20261003 | An explicit antiunitary J = B o K on round59's 8-dim Sigma exists for both signs eps = +-1 of J E_k J^-1 = eps E_k (solution space 1-dim eac |
| C219_EXACT_S6_HEAT_KERNEL_B10_MINUS_0_0029521_GI | SUPPORTED | PASS | 20261003 | The tau^2 coefficient of the S^6 spinor heat kernel is exactly B10 = -0.0029521 (Mellin / Euler-Maclaurin closed form with W6 = (2/15)(m^5-5 |
| C219_H8_COMPUTED_DIRAC_CASIMIR_NO_VALID_REGION_M | PARTIALLY_SUPPORTED | PARTIAL | 20261003 | With the computed Dirac zeta_FP(rho3,rho6) on S^3 x S^6 (kappa times zeta_FP over Vol3 Vol6 rho3^3 rho6^6 added to G92's V_main) there is no |
| C220_L1_HARMONICS_R4_NORM_SQRT2_FORCED_BY_NORM_P | PROVED | PASS | 20261012 | Exact sympy plus a numeric cross-check, l=1 harmonics on S^2 of radius r. (1) int x^2 dS = int y^2 dS = int z^2 dS = 4 pi r^4/3, mixed integ |
| C221_SPINOR_LADDER_ORBITAL_STEP4_FAILS_COT_RATIO | PROVED | PASS | 20261014 | Sympy exact (closure scan and D3c numeric at 4 angles), unit S^2, the five ladder steps for m=+-1/2. (1) With McMurry p.144 operators (s=0): |
| C222_SPIN_HALF_INVARIANT_SUBSPACES_ON_S2_FORM_A_ | SUPPORTED | PASS | 20261102 | Exact sympy plus numeric checks, 39 checks in four scripts. (1) Scalar functions on S^2 under the dragging action (pullback by rotations) de |
| C223_HOPF_MAP_FIBRES_ARE_CIRCLES_G_AB_FRAME_CONS | SUPPORTED | PASS | 20261102 | Exact sympy plus numeric checks, 39 checks in five scripts. (1) For the Hopf map x_i = xi^dagger sigma_i xi: /x/ = /xi/^2; the fibres over S |
| C224_FERMION_NOT_A_CONSTANT_COEFFICIENT_SUPERPOS | SUPPORTED | FAIL | 20261102 | Exact sympy plus numeric checks, 34 checks in five scripts, two defined models. (1) Cut sphere, phi in (0, 2 pi): e^{i phi/2} equals an L^2  |
| C225_SU2_DIFFERENTIAL_GENERATORS_D1_D2_D3_DERIVE | SUPPORTED | PASS | 20261102 | Exact sympy, 11 checks, xi and conj(xi) treated as independent symbols (Wirtinger calculus). With the action (U(g) f)(xi, conj xi) = f(g^-1  |
| C226_HOPF_VECTOR_PROJECTION_SO3_NORMALISATION_AN | SUPPORTED | PASS | 20261102 | Exact sympy plus numeric checks, 30 checks. (1) For F = xi xi^dagger and V^i = (1/2) tr(F sigma^i) = (1/2) xi^dagger sigma^i xi: F = (1/2)/x |
| C227_D0_SPECTRUM_MULTIPLICITIES_FOR_ALL_S_FROM_P | SUPPORTED | PASS | 20261102 | D0 = -i sum_a sigma_a X_a^R on L^2(S^3, C^2), with C = -1 (T_a = -i sigma_a), has eigenvalue -2s with multiplicity (2s+1)(2s+2) and eigenval |
| C228_H2_DOUBLET_NOT_INVARIANT_UNDER_D0_RESIDUAL_ | SUPPORTED | FAIL | 20261102 | With A = D0 - I, Gamma = sigma.n, Psi = (-(1-cos theta)/2, e^{i phi} sin theta/2), Phi = J_- Psi and H2 = span{Psi, Phi}: (1) numerically (s |
| C229_THREE_READINGS_OF_SU2_ACTION_A_AND_C_ARE_RE | SUPPORTED | PASS | 20261103 | Exact sympy, 29 asserted checks and 5 self-controls, derived from the definitions with g_a(t) = cos(t/2) + i sin(t/2) sigma_a. Reading A: (U |
| C230_H2_PRESERVED_BY_EQUIVARIANT_FIRST_ORDER_OPE | SUPPORTED | PASS | 20261103 | Exact sympy, 19 asserted checks. The operators 1, sigma.L, Gamma, Gamma sigma.L commute with J; on the j = 1/2 multiplicity space (basis chi |
| C231_CR_KERNEL_ON_S3_AT_CHARGE_N_HAS_DIMENSION_N | SUPPORTED | PASS | 20261103 | Exact sympy. For charge n = 0..4 the kernel of the CR operator Lbar on S^3 (polynomials of degree <= n+3 modulo the sphere relation) has dim |
| C232_J3R_ON_RIGHT_INDEX_IS_HALF_HOPF_CHARGE_AND_ | SUPPORTED | PASS | 20261103 | Exact sympy. (J3L, J3R) on (g00, g01, g10, g11) = ((-1/2,+1/2), (-1/2,-1/2), (+1/2,+1/2), (+1/2,-1/2)), reproducing the TOM-CERT-01 table in |
| C233_MUTATION_SCAN_40_MUTANTS_4_SURVIVORS_ALL_EQ | SUPPORTED | PASS | 20261103 | mutation_scan.py, 40 mutants: 27 KILLED by a check, 9 CRASHED (loud failure), 4 SURVIVED; excluding crashes 27 of 31 were caught. All 4 surv |
| C234_SQRT_DET_G_IS_A_SCALAR_DENSITY_THE_RATIO_TO | SUPPORTED | PASS | 20261103 | Exact sympy at three regular points, 24 asserted checks and 3 self-controls. sqrt(det g) of the round S^3 is sin(eta)cos(eta) in Hopf coordi |
| C235_S3_HARMONIC_SECTORS_SCALARS_S_S_C2_FIELDS_J | SUPPORTED | PASS | 20261103 | Exact sympy (rank and nullity of joint Casimir systems), 13 asserted checks and 3 self-controls, degrees 0..3. Scalars: sectors (j_L,j_R) =  |
| C236_FOURTH_HARMONIC_IS_THE_DIAGONAL_SINGLET_A_C | SUPPORTED | PASS | 20261104 | Exact sympy, 37 checks. The four degree-1 harmonics split under the diagonal SU(2) (conjugation g -> h g h^-1, generators X_k + Y_k) as 1 +  |
| C237_VACUUM_POINT_STABILIZER_IS_DIAGONAL_SU2_ACT | SUPPORTED | PASS | 20261104 | Exact sympy, 39 checks. Under g -> h g k^-1 on S^3 = SU(2) the action is transitive; at four sampled points the stabilizer algebra is 3-dime |
| C238_PREPRINT_ALGEBRA_CHECKED_EQ3_EQ5_SIGN_MISMA | SUPPORTED | PASS | 20261104 | Exact sympy, 26 checks, on the equations of the correspondent's preprint (Preprints.org 202510.2222.v2, 21 pages): eq (14) d/d theta = x d_y |
| C239_POSTER_32_STATE_GENERATORS_CONSISTENT_BOOKK | SUPPORTED | PASS | 20261104 | Numerical linear algebra (tolerance 1e-12), 23 checks, on the explicit generators printed on the correspondent's conference poster (IOCSYM 2 |
| C240_NO_CHIRALITY_OPERATOR_ON_C2_AND_SECTOR_TABL | SUPPORTED | PASS | 20261104 | Exact sympy, degrees 0..1. The only 2x2 matrices commuting with sigma_1, sigma_2, sigma_3 are the scalars (Schur). The C^2-valued sectors of |
| C241_STANDARD_HYPERCHARGE_ADDED_TO_POSTER_32_STA | SUPPORTED | PASS | 20261104 | Numerical linear algebra (tolerance 1e-12), 11 checks. On the 32 states of the poster's generators (C239) with T3R = (1/2)(1 x P_R x sigma_3 |
| C242_SECOND_COMPONENT_E_I_PHI_SIN_HALF_THETA_FIX | SUPPORTED | PASS | 20261116 | Exact sympy plus numeric checks, 23 checks (22 exact, 1 numeric with 500 random points, worst residual 4e-15). For V^i = (1/2) xi^dagger sig |
| C243_TRANSPOSE_OF_SU2_ELEMENT_IS_SIGMA2_INVERSE_ | SUPPORTED | PASS | 20261117 | Exact sympy plus numeric checks, 13 checks. For u in SU(2) written u = [[a, -conj b], [b, conj a]] (a, b, conj a, conj b independent symbols |
