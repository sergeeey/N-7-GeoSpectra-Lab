# Human-AI Work — CAP v1.0 (GeoSpectra Lab instance)

**Status:** `proceed_with_caution` | **v0.1.0-cap-geospectra** | **validation:** partially_validated

## Quick start

1. Read `MASTER_CONTEXT.md`
2. Run calls in order: `call01` → `call02` → `call03` → `call04`
3. For each gate task, copy `templates/cognitive_loop_log.yaml`

## Files

| Call | File | Output |
|------|------|--------|
| 1 Foundation | `call01_foundation.yaml` | Awareness, Environment, Intent + 3 gates |
| 2 Core Loop | `call02_core_loop.yaml` | Context, Strategy Router, Cognitive Loop |
| 3 Validation | `call03_validation.yaml` | HD-MAVP, Pearls, Evaluation (layers 1–6 only) |
| 4 Operations | `call04_operations.yaml` | MethodOps, Safety, MVP 7d, Risk Register |

## GeoSpectra anchors

- **Gate culture:** pre-reg, PASS_WITH_CAVEATS, `docs/CLAIMS_AND_CAVEATS.md`
- **Pearl #001:** bootstrap — P13H needs P13A-G on disk
- **Pearl #002:** pytest `test_gate_2_smoke` — use narrow bundle on Windows
- **Example blocked task:** `examples/p13h_cognitive_loop_log.yaml`

## Not claimed

- CAP is not "validated team standard" until golden set + human review
- `[hypothesis — expected quality improvement, requires testing]` for CAP vs megaprompt

## HAI-OS v0.3 (daily standard)

Ежедневный компактный стандарт: [`docs/hai-os/`](../hai-os/README.md)  
Маппинг CAP ↔ HAI-OS: [`docs/hai-os/CAP_MAPPING.md`](../hai-os/CAP_MAPPING.md)

## Operating algorithm (short)

Intent → Environment → Context → Strategy → Decompose → Evidence → Recompose → Pearl → Human Decision → MethodOps
