# CLAUDE.md — N-7-GeoSpectra-Lab (project-level)

## Project type
**RESEARCH** — falsification-first numerical/algebraic physics harness.
Resolves dispatcher ambiguity (was: research=6, production=5, tie).
README + activeContext.md use VERIFIED/KILLED/PASS/FAIL evidence markers,
ACH falsification matrices, kill_criterion gates — this is not production code,
methodology = **FL Full + EstimandOps** for every experiment (per global dispatcher rule).

## Two tracks (do not conflate)
| | Track A — Numerical | Track B — Algebraic |
|---|---|---|
| Dir | `cc_toy_lab/`, `scripts/`, `tests/` | `tom_s3_spinor_toy/` |
| Verdict | `DISCRETIZATION_SENSITIVE` | N_gen=3 via Atiyah-Singer |
| Entry | `reports/GATE4B_SPECIFICITY_VERDICT_v0.1.24.md` | `tom_s3_spinor_toy/RESEARCH_STATUS_REPORT.md` |

Third, independent track (frozen 2026-06-30): `paper/WHEN_GEOMETRY_BECOMES_UNRECOVERABLE.md`
— spectral-recoverability-vs-physics null result (H0 wins, H1-H4 killed). See `CLAIMS_REGISTRY.md`.

## Hard constraints (do not violate — carried from activeContext.md)
- Tom Lawrence: **DO NOT INITIATE CONTACT** — he reaches out when Part 4/5 ready
- `lambda = FREE_COUPLING_PARAMETER` — never claim derived/fixed (LAMBDA-B5-G4 theorem)
- `sm_derivation_claimed = False`; "tom_ansatz solved" phrasing FORBIDDEN
- `safe_for_runtime = False`, `runtime = research_only`
- DO NOT merge `preserve/*` → main without explicit audit/cherry-pick decision
- New code: bare `lambda` FORBIDDEN — use `lambda_v`/`lambda_v_operator` or `lambda_np` explicitly
  (lambda_v_operator vs lambda_np — see `tom_s3_spinor_toy/experiments/20260622-g79a-lambda-identity-audit/lambda_separation_plan.md`)

## Письма Тому Лоуренсу (единственное место правил; читать перед каждым черновиком)
Источники и случаи: `tom_s3_spinor_toy/correspondence/LETTER_CHECKLIST_TOM.md`.
Перед отправкой: `python tom_s3_spinor_toy/correspondence/presend_check.py <файл>` (FAIL = не отправлять).
1. Первыми не пишем; отвечаем на его просьбы. Отправляет пользователь, не Claude.
2. Выписать все его вопросы из последнего письма и прежние открытые; ответить на каждый.
3. К нашему вопросу объяснить, зачем он нужен (причина → следствие), без тона поправки. Не говорить, что прошлый ответ был неверным. Один вопрос в конце.
4. Атрибуция: «Claude identified, I checked». Наружу только «Tom + Sergey», рабочее название проекта наружу не выносить.
5. Не опережать: его теория и наша работа — два слоя. N_gen=3, триальность, G₂ только по его вопросу. Непроверенное — вопросом, с оговоркой.
6. Его слова и ровный тон: брать его термины; не использовать bundle, fibre, pullback, ambient, trivialization; без слов про «честность» и «ошибку»; не пересказывать ему его же текст; не описывать его намерения.
7. Выкладки формулами (LaTeX или уравнения Word, не ASCII), простой английский, короткие абзацы.
8. «Проверено» = строка в скрипте; писать, что проверка не покрыла. Формулы и числа брать из сохранённого результата, не по памяти; число с функцией и мерой.
9. О его документе и о нашем прошлом письме говорить только с самим документом в руках (PDF как изображение). Конвенцию закрепить до слова «неверно».
10. Тривиальное не подавать как результат. Зависящее от выбора (калибровка, конвенция) называть конвенцией.
11. Гейт: независимый контекстно-слепой разбор (до 3 раундов, каждое замечание проверять инструментом) и перечитывание письма целиком после паузы. После любой правки проверять заново. Самопроверка разбор не заменяет.
12. Репозиторий публичный: письма и всё с цитатами только в `correspondence/`, никогда `git add -A`. В файле перед отправкой нет `**`, `$`, `[4pt]`.
13. Пользователю по-русски; сообщения Тома переводить полностью и сразу; к английскому черновику давать русский перевод.
14. Даты и цитаты Тома сверять с экспортом `docs/perepiska`, не с памятью.

## Methodology activation (per global ~/.claude/CLAUDE.md dispatcher)
Every new experiment/claim in this repo goes through, in order:
1. `~/.claude/rules/estimand-ops.md` — L0 gate (descriptive/predictive/causal) before design
2. `~/.claude/rules/falsification-ladder.md` — Full tier: claim.md + estimand.md + kill_criterion
   → use `tom_s3_spinor_toy/experiments/_template/claim.md` (has mandatory kill_criterion section)
3. `~/.claude/rules/doubt-driven-development.md` — skeptic red-team before non-trivial builds
4. `~/.claude/rules/audit-verification-gate.md` — tool-verify any HIGH/MEDIUM finding before reporting
5. `~/.claude/rules/integrity.md` evidence markers on every numeric/factual claim

## Experiment naming
`experiments/YYYYMMDD-<gN>-<slug>/` with `claim.md` + `decision.md` (+ script + `results_gN.json`).
Rejected → `null_results/<id>.md` + INDEX. Deprioritized → `parked/<id>.md` + INDEX.

## Memory
`.claude/memory/activeContext.md` — current focus, updated after each commit (auto-logged).
