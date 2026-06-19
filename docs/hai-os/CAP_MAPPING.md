# HAI-OS v0.3 ↔ CAP v1.0 Mapping

CAP (`docs/cap/`) остаётся **детальным прототипом** и audit trail.  
HAI-OS v0.3 — **ежедневный** operating standard.

## Core mapping

| HAI-OS v0.3 | CAP v1.0 | GeoSpectra path |
|-------------|----------|-----------------|
| Task Passport | Intent Card + Environment Passport | `call01_foundation.yaml` |
| Context Map | Context Map | `call02_core_loop.yaml` |
| Strategy Card | Strategy Router | `call02_core_loop.yaml` |
| Work Log | Cognitive Loop (execution steps) | `templates/cognitive_loop_log.yaml` |
| Verification Report | HD-MAVP + Evaluation | `call03_validation.yaml` |
| Decision Record | Decision step in loop | `call04_operations.yaml` |

## Gates mapping

| HAI-OS Gate | CAP Gate |
|-------------|----------|
| Task Gate | Awareness + Intent Gate |
| Context Gate | Context Gate |
| Strategy Gate | Strategy Gate |
| Verification Gate | Evidence + Evaluation Gate |
| Decision Gate | Human Decision Boundary |

## Optional modules

| HAI-OS optional | CAP location |
|-----------------|--------------|
| Pearl Registry | `call03_validation.yaml` pearls |
| MethodOps | `call04_operations.yaml` method_version_card |
| HD-MAVP | `call03_validation.yaml` hd_mavp_protocol |
| Human Development | `call04_operations.yaml` human_development_layer |

## Version policy

- **HAI-OS** semver: `0.3.0` — daily standard
- **CAP** semver: `0.1.0-cap-geospectra` — research formalization archive
- Изменение HAI-OS → `templates/method_delta.yaml`
- Изменение CAP → `docs/cap/CHANGELOG.md`

## Rule

Не раздувать HAI-OS core обратно до 12 CAP layers.  
CAP читать когда нужна **глубина**; HAI-OS — когда нужна **скорость**.
