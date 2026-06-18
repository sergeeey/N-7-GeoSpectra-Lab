# HAI-OS v0.3 — Human-AI Operating System

**Статус:** `hypothesis` | **Роль:** `daily_operating_standard` | **Справка:** [CEVA_REFERENCE.md](CEVA_REFERENCE.md)

## Быстрый цикл

```
Task Passport → Context Map → Strategy Card → Work Log
     → Verification Report → Decision Record
```

**5 gates:** Task | Context | Strategy | Verification | Decision

## Файлы

| Путь | Назначение |
|------|------------|
| [HAI-OS_v0.3.yaml](HAI-OS_v0.3.yaml) | Каноническая спецификация |
| [templates/](templates/) | Пустые шаблоны артефактов |
| [instances/](instances/) | Заполненные примеры (GeoSpectra) |
| [CAP_MAPPING.md](CAP_MAPPING.md) | Связь с `docs/cap/` |
| [CEVA_REFERENCE.md](CEVA_REFERENCE.md) | Роль CEVA (reference, не SOP) |

## Как начать задачу

1. Скопируй `templates/task_passport.yaml` → `instances/<task_id>/`
2. Заполни Task Passport, пройди Task Gate
3. Добавь `context_map.yaml`, `strategy_card.yaml`
4. Веди `work_log.yaml` по ходу работы
5. Закрой `verification_report.yaml` + `decision_record.yaml`
6. Optional: `pearl_card.yaml` / `method_delta.yaml` только при сигнале

## GeoSpectra примеры

- [instances/p13h_gate/instance.yaml](instances/p13h_gate/instance.yaml) — P13H (hd_mavp + agentic)
- [instances/exp_cap_001/instance.yaml](instances/exp_cap_001/instance.yaml) — golden set CAP

## Принципы (коротко)

1. Fluency ≠ truth  
2. Confidence ≠ evidence  
3. Human owns intent, judgment, accountability  
4. Risk → depth процесса  
5. Context ceiling — не перегружать  
6. Unsupported claims → помечать  
7. Extensions only by need  

## Связь с CAP

CAP (`docs/cap/`) — развёрнутый прототип и audit trail.  
HAI-OS v0.3 — **ежедневный** компактный стандарт. Не заменяют друг друга.

## Validation

```yaml
validation_status: hypothesis
next_required_action: test_on_5_real_tasks
do_not_do: expand_core_back_to_12_layers
```
