# Experiment: [TODO: Short descriptive name]

**ID:** `[TODO: YYYYMMDD-short-slug]`  
**Date:** [TODO: YYYY-MM-DD]  
**Status:** [TODO: planned | running | completed | failed | archived]  

---

## 1. Goal

[TODO: What are we testing? 1-2 sentences describing the primary question or objective.]

<!-- Example:
Test whether confidence-based deduplication reduces false positives in Gold-2026 
spectral anomaly detection without degrading true positive rate.
-->

---

## 2. Hypothesis

[TODO: Falsifiable claim that experiment will test.]

<!-- Example:
Confidence threshold ≥0.7 + spatial clustering (50m radius) will reduce FP rate 
from baseline 15% to ≤5% while maintaining TP rate ≥85% on Kyzylorda validation set.
-->

---

## 3. Success Criterion

[TODO: Quantitative threshold that defines success. Must be measurable.]

<!-- Example:
- False positive rate ≤ 5% (vs baseline 15%)
- True positive rate ≥ 85% (vs baseline 89%)
- Total detections reduced by ≥30%
- Runtime ≤ 2× baseline (acceptable overhead)
-->

---

## 4. Failure Condition

[TODO: What result means experiment failed? When to stop and reassess.]

<!-- Example:
- TP rate drops below 80% (unacceptable recall loss)
- Runtime exceeds 3× baseline (too expensive)
- OOM crash on target hardware (32GB)
- Zero detections after filtering (over-aggressive)
-->

---

## 5. Compute Requirements

**Hardware:**
- [TODO: RAM requirement, e.g., "32 GB minimum, 64 GB recommended"]
- [TODO: CPU cores, e.g., "8 cores"]
- [TODO: GPU if needed, e.g., "None" or "CUDA-capable GPU with 8GB VRAM"]

**Storage:**
- [TODO: Disk space for inputs + outputs, e.g., "150 GB for Sentinel-2 tiles + 5 GB outputs"]

**Runtime estimate:**
- [TODO: Expected duration, e.g., "4-6 hours for full Kyzylorda region"]

**Cost estimate (if cloud):**
- [TODO: e.g., "€12-15 for Hetzner CPX51 (16 vCPU, 32 GB, 6 hours)"]

<!-- Example:
**Hardware:**
- RAM: 32 GB minimum (peak usage ~28 GB observed in Gate 4B v0.1.24)
- CPU: 8 cores (parallelizes well)
- GPU: None

**Storage:**
- Input: 120 GB Sentinel-2 L2A tiles (Kyzylorda 2023-2024)
- Output: 3 GB GeoJSON + 2 GB confidence maps
- Total: 125 GB

**Runtime estimate:**
- 5-7 hours for full region (based on v0.1.21 baseline: 4.2 hours)

**Cost estimate:**
- Hetzner CPX51: €2.50/hr × 7hr = €17.50
-->

---

## 6. Safety Checks

### Pre-flight checks (before starting):
- [TODO: Smoke test to verify setup, e.g., "Run on 1 tile, expect output in <5 min"]
- [TODO: Disk space check, e.g., "df -h | grep /data — ensure ≥150 GB free"]
- [TODO: Dependency verification, e.g., "rasterio, geopandas, scipy installed"]

### During execution:
- [TODO: Monitoring strategy, e.g., "Check logs every 30 min, watch for OOM warnings"]
- [TODO: Checkpoint interval, e.g., "Save intermediate results every 50 tiles"]
- [TODO: Kill switch, e.g., "If RAM >90% for >10 min, abort gracefully"]

### Post-execution:
- [TODO: Output validation, e.g., "Verify GeoJSON has ≥100 features, no empty geometries"]
- [TODO: Sanity check, e.g., "Plot detections on map, visual inspection for obvious errors"]

<!-- Example:
### Pre-flight:
- Smoke test: `python run_gate4b.py --tiles 1 --region test_small`
- Disk: `df -h /mnt/data` → confirm ≥150 GB free
- Deps: `python -c "import rasterio, geopandas, scipy; print('OK')"`

### During:
- Monitor: `watch -n 300 'tail -20 logs/gate4b.log'` (every 5 min)
- Checkpoint: Save to `checkpoints/gate4b_tile_{N}.geojson` every 50 tiles
- Kill switch: If `free -h` shows <2 GB available for >10 min → graceful shutdown

### Post:
- Validate: `python validate_output.py output/detections.geojson`
- Sanity: Load in QGIS, overlay on Sentinel-2 RGB, check 10 random detections
-->

---

## 7. Data Outputs

[TODO: List all files/artifacts created by experiment and their storage locations.]

| Artifact | Path | Size (est.) | Description |
|----------|------|-------------|-------------|
| [TODO: name] | [TODO: path] | [TODO: size] | [TODO: what it contains] |

<!-- Example:
| Artifact | Path | Size (est.) | Description |
|----------|------|-------------|-------------|
| Detections (full) | `outputs/kyzylorda_detections_20260601.geojson` | 2.5 GB | All anomaly polygons with confidence scores |
| Detections (filtered) | `outputs/kyzylorda_filtered_conf07.geojson` | 800 MB | After confidence + spatial dedup |
| Confidence rasters | `outputs/confidence_maps/*.tif` | 1.2 GB | Per-tile confidence heatmaps (debugging) |
| Metrics summary | `outputs/metrics_summary.json` | 5 KB | TP/FP/FN counts, precision, recall, F1 |
| Experiment log | `logs/gate4b_20260601.log` | 50 MB | Full execution trace |
| Checkpoint (if crash) | `checkpoints/gate4b_tile_NNN.geojson` | varies | Resume point |
-->

---

## 8. Rollback Plan

[TODO: What to do if experiment breaks something or produces invalid results.]

### If experiment crashes mid-run:
- [TODO: Recovery steps, e.g., "Resume from last checkpoint in checkpoints/ dir"]

### If results are invalid:
- [TODO: Validation failure handling, e.g., "Archive to experiments/failed/, document why"]

### If compute environment corrupted:
- [TODO: Restoration steps, e.g., "Rebuild from Docker image geospectra:v0.1.24"]

### If blocking production work:
- [TODO: Abort protocol, e.g., "Kill process, restore baseline config, notify user"]

<!-- Example:
### If crash mid-run:
1. Check last checkpoint: `ls -lth checkpoints/ | head -1`
2. Resume: `python run_gate4b.py --resume checkpoints/gate4b_tile_250.geojson`
3. If checkpoint corrupted → restart from previous milestone (every 100 tiles)

### If results invalid:
1. Run `python validate_output.py` → capture error
2. Move to `experiments/failed/20260601-confidence-dedup/`
3. Document failure in `experiments/failed/INDEX.md`
4. Do NOT retry without hypothesis revision

### If environment corrupted:
1. Stop all processes: `pkill -f run_gate4b`
2. Restore Docker: `docker run geospectra:v0.1.24`
3. Verify smoke test passes before resuming

### If blocking production:
1. Immediate abort: `pkill -9 -f run_gate4b`
2. Restore baseline config: `git checkout configs/gate4b_baseline.yaml`
3. Notify via Telegram: "Experiment aborted, production priority"
-->

---

## Notes

[TODO: Any additional context, assumptions, or references.]

<!-- Example:
- Based on Gate 4B v0.1.24 OOM postmortem (docs/OUTCOMES.md)
- Uses memory-safe streaming (no full-array loads)
- Validation set: 50 known gold deposits in Kyzylorda (ground truth from Ерғали)
- Related experiments: 20260520-baseline-gate4b, 20260525-spatial-clustering
-->
