# CEVA — Reference Architecture (не SOP)

**Роль в HAI-OS v0.3:** `reference_whitepaper` — объяснение и обоснование, **не** ежедневная пошаговая инструкция.

## Что такое CEVA в этой схеме

CEVA (Context–Evidence–Verification–Agency architecture) — **справочная** модель того, как устроена осознанная работа человека с LLM:

- где ломается доверие к ответам (**Verification Gap**);
- где ломается качество из-за объёма (**Context Ceiling**);
- кто принимает решение (**Human Agency**);
- какие расширения оправданы (Pearl, MethodOps, HD-MAVP).

HAI-OS **не копирует** CEVA целиком как обязательные 12 слоёв.

## Что взято в ядро HAI-OS v0.3

| CEVA element | HAI-OS v0.3 |
|--------------|-------------|
| Verification Gap | core principle + Verification Gate |
| Context Ceiling | core principle + Context Map field |
| Human Agency | core principle + Decision Record |
| Pearl Registry | **optional** module |
| MethodOps | **optional** module |
| Human Development | **optional** extension |
| HD-MAVP | **activated** for complex/high-risk |

## Что сознательно не взято

- mandatory 12-layer core as daily SOP
- full whitepaper structure on every task
- mandatory Pearl on every turn
- heavy MethodOps by default

## Когда читать CEVA

- проектирование новой версии HAI-OS;
- обоснование optional module перед активацией;
- обучение нового участника (после HAI-OS quick start).

## Когда не читать CEVA

- рутинная задача low-risk → `strategy: minimal`
- нужен только чеклист → `HAI-OS_v0.3.yaml` + templates

## GeoSpectra mapping

| CEVA idea | GeoSpectra example |
|-----------|-------------------|
| Verification Gap | P13H: ответ «NO_GO» потребовал pytest, не только слов |
| Context Ceiling | Исключили `.venv`, session spec без grep |
| Human Agency | promote P13 forbidden без human gate |
| Pearl | PEARL-001 bootstrap, PEARL-002 pytest smoke |
| HD-MAVP | P13 chain decomposition |

Полный whitepaper CEVA — вне этого репозитория; здесь только **роль reference**.
