# Checkpointing Enhancement Plan — Gate 4B Batched Execution

**Date:** 2026-06-01  
**Purpose:** Memory-safe resumability for interrupted batched runs  
**Scope:** Plan only — no code changes  

---

## Executive Summary

**Current state:** Batch-level checkpointing exists. Per-case checkpointing does NOT exist.

**Gap:** If rerun interrupted mid-batch → entire batch (24 cases, ~16 min) lost.

**Solution:** Per-case checkpointing with atomic writes + manifest tracking.

**Estimated effort:** 3 files changed, ~2 hours implementation + 1 hour testing.

---

## Current State (What Exists)

### Batch-Level Checkpointing ✅

**Evidence:** [VERIFIED-REAL] `scripts/run_gate4_batched.py:424-435`

```python
# Check if batch already completed (resume logic)
status_file = batch_dir / "status.json"
if status_file.exists() and not force:
    with open(status_file, "r") as f:
        status_data = json.load(f)
    if status_data["status"] in ["completed", "completed_with_missing_r_stat"]:
        print(f"Batch {batch_id:2d} already completed. Skipping.")
        return status_data
```

**What it does:**
- Tracks batch completion via `status.json`
- `--resume` flag skips completed batches (line 529)
- `--force` flag overwrites existing batch results (line 532)

**Granularity:** Batch = 24 cases = ~16 min runtime (v0.1.20 estimate, v0.1.24 TBD)

**Limitation:** If batch interrupted mid-execution → all 24 cases must re-run.

### Save Points

**Batch-level artifacts** (saved AFTER batch completes):
- `batch_config.json` — grid parameters (line 327)
- `results.json` — per-case results array (line 331)
- `timing.json` — runtime breakdown (line 350)
- `status.json` — completion status (line 371)
- `summary.md` — human-readable summary (line 401)

**Atomicity:** Results written ONCE after all 24 cases complete (line 475).

**Crash scenario:**
```
Batch 3 starts → 18/24 cases complete → OOM crash
→ NO checkpoint → batch marked incomplete → all 24 cases re-run on --resume
```

---

## What's Missing

### 1. Per-Case Checkpointing ❌

**Problem:** No incremental save during batch execution.

**Current behavior:**
```python
for i, case in enumerate(batch["cases"]):
    result = run_single_case(case)  # 40 sec per case (v0.1.24 OOM indicates ~40s average)
    results.append(result)          # In-memory only
    # ❌ NO save here
```

**Impact:**
- 24 cases × 40 sec = 16 min batch runtime
- Crash at case 23 → 15.3 min lost
- On 32 GiB server with OOM risk → high probability of mid-batch crash

### 2. Resume from Last Completed Case ❌

**Problem:** Cannot detect partial batch progress.

**Current logic:**
- Batch status: `completed` | `completed_with_failures` | (not exists = not started)
- No status: `in_progress_N_of_24`

**Needed:**
- Track completed case IDs: `[0, 1, 2, ..., 17]` (cases 0-17 done, 18-23 pending)
- Skip already-completed cases on resume

### 3. Corrupted Checkpoint Handling ❌

**Problem:** No validation that saved case data is complete.

**Risk scenarios:**
- Disk full → truncated JSON write
- OOM during `json.dump()` → partial file
- SIGKILL mid-write → corrupted file

**Current behavior:** No detection. Next run may crash loading invalid JSON.

### 4. Temp File Cleanup ❌

**Problem:** No intermediate files created → nothing to clean up.

**But:** If per-case checkpoints added → need cleanup protocol for `.tmp` files.

---

## Minimal Viable Checkpoint Design

### Objective

Enable per-case resume without excessive I/O overhead.

**Constraints:**
- Add <5% runtime overhead (target: <1 sec per case write)
- Work on OOM-prone environments (32 GiB server)
- No dependencies beyond stdlib (json, pathlib)
- Atomic writes (no partial files)

### Architecture

```
reports/RUNS/gate4_fss_v0.1.24/batches/batch_03/
├── batch_config.json       # Existing: batch metadata
├── manifest.json           # NEW: completed case tracker
├── case_000.json           # NEW: per-case result
├── case_001.json
├── ...
├── case_023.json
├── results.json            # Existing: merged at batch end (backward compat)
├── status.json             # Existing: batch status
└── summary.md              # Existing: human summary
```

### File Specifications

#### `manifest.json` (NEW)

**Purpose:** Track which cases completed successfully.

**Format:**
```json
{
  "batch_id": 3,
  "total_cases": 24,
  "completed_cases": [0, 1, 2, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17],
  "failed_cases": [3, 4, 6, 9, 14],
  "pending_cases": [18, 19, 20, 21, 22, 23],
  "last_updated": "2026-06-01T08:27:34Z"
}
```

**Atomic write protocol:**
1. Write to `manifest.json.tmp`
2. `os.fsync()` to flush buffer
3. `os.replace(manifest.json.tmp, manifest.json)` (atomic on POSIX + Windows)

**Update frequency:** After each case completes (24 writes per batch).

#### `case_NNN.json` (NEW)

**Purpose:** Store single-case result.

**Format:** Same as current `results.json` entry (line 276-298):
```json
{
  "case_id": 17,
  "family": "spectral_circle",
  "disorder_strength": 20,
  "s1_size": 128,
  "j_max": 3,
  "seed": 789,
  "runtime_sec": 42.7,
  "true_ipr_mean": 0.0234,
  "uses_eigenvectors": true,
  "mean_low_eigenvalue": -12.45,
  "ipr_metric_version": "v0.1.24_true_eigenvector_ipr",
  "r_stat": 0.386,
  "r_stat_available": true,
  "r_stat_reason": null,
  "error": null
}
```

**Naming:** `case_{case_id:03d}.json` (e.g., `case_000.json`, `case_017.json`)

**Atomic write:** Same protocol as `manifest.json` (write `.tmp`, fsync, replace).

---

## Resume Logic (Pseudocode)

### On Batch Start

```python
def run_batch(batch, output_base, force=False):
    batch_dir = output_base / "batches" / f"batch_{batch_id:02d}"
    manifest_file = batch_dir / "manifest.json"
    
    # Load existing progress (if any)
    if manifest_file.exists() and not force:
        with open(manifest_file, "r") as f:
            manifest = json.load(f)
        completed_ids = set(manifest["completed_cases"])
    else:
        completed_ids = set()
        manifest = {
            "batch_id": batch["batch_id"],
            "total_cases": len(batch["cases"]),
            "completed_cases": [],
            "failed_cases": [],
            "pending_cases": list(range(len(batch["cases"]))),
            "last_updated": None,
        }
    
    # Run only pending cases
    for case in batch["cases"]:
        if case["id"] in completed_ids:
            print(f"Case {case['id']:3d} already completed. Skipping.")
            continue
        
        # Run case
        result = run_single_case(case)
        
        # Save per-case checkpoint
        save_case_checkpoint(batch_dir, result)
        
        # Update manifest
        if result["error"] is None:
            manifest["completed_cases"].append(case["id"])
        else:
            manifest["failed_cases"].append(case["id"])
        manifest["pending_cases"].remove(case["id"])
        manifest["last_updated"] = datetime.utcnow().isoformat() + "Z"
        
        save_manifest(batch_dir, manifest)
    
    # Merge per-case files → results.json (backward compat)
    merge_case_results(batch_dir, batch["cases"])
    
    # Save batch-level status.json (existing logic)
    save_batch_status(batch_dir, manifest)
```

### Atomic Save Helpers

```python
def save_case_checkpoint(batch_dir, result):
    """Save single case result atomically."""
    case_id = result["case_id"]
    case_file = batch_dir / f"case_{case_id:03d}.json"
    tmp_file = batch_dir / f"case_{case_id:03d}.json.tmp"
    
    # Write to temp file
    with open(tmp_file, "w") as f:
        json.dump(result, f, indent=2)
        f.flush()
        os.fsync(f.fileno())  # Force write to disk
    
    # Atomic replace
    os.replace(tmp_file, case_file)

def save_manifest(batch_dir, manifest):
    """Save manifest atomically."""
    manifest_file = batch_dir / "manifest.json"
    tmp_file = batch_dir / "manifest.json.tmp"
    
    with open(tmp_file, "w") as f:
        json.dump(manifest, f, indent=2)
        f.flush()
        os.fsync(f.fileno())
    
    os.replace(tmp_file, manifest_file)
```

---

## Error Recovery Protocol

### Corrupted Checkpoint Detection

**On manifest load:**
```python
try:
    with open(manifest_file, "r") as f:
        manifest = json.load(f)
    
    # Validate schema
    required_keys = ["batch_id", "total_cases", "completed_cases", "pending_cases"]
    if not all(k in manifest for k in required_keys):
        raise ValueError("Manifest missing required keys")
    
    # Validate consistency
    n_completed = len(manifest["completed_cases"])
    n_failed = len(manifest.get("failed_cases", []))
    n_pending = len(manifest["pending_cases"])
    if n_completed + n_failed + n_pending != manifest["total_cases"]:
        raise ValueError("Manifest case count mismatch")

except (json.JSONDecodeError, ValueError) as e:
    print(f"⚠️ WARNING: Corrupted manifest.json: {e}")
    print("Reconstructing from case_*.json files...")
    
    # Fallback: scan case_*.json files
    completed_ids = []
    for case_file in sorted(batch_dir.glob("case_*.json")):
        try:
            with open(case_file, "r") as f:
                result = json.load(f)
            if result["error"] is None:
                completed_ids.append(result["case_id"])
        except (json.JSONDecodeError, KeyError):
            print(f"⚠️ WARNING: Corrupted {case_file.name}. Skipping.")
    
    # Rebuild manifest from scratch
    manifest = rebuild_manifest(batch, completed_ids)
```

**On per-case file load:**
```python
def load_case_result(batch_dir, case_id):
    """Load case result with corruption handling."""
    case_file = batch_dir / f"case_{case_id:03d}.json"
    
    if not case_file.exists():
        return None  # Not yet run
    
    try:
        with open(case_file, "r") as f:
            result = json.load(f)
        
        # Validate required fields
        required = ["case_id", "runtime_sec", "true_ipr_mean", "error"]
        if not all(k in result for k in required):
            raise ValueError("Missing required fields")
        
        return result
    
    except (json.JSONDecodeError, ValueError) as e:
        print(f"⚠️ WARNING: Corrupted case_{case_id:03d}.json: {e}")
        print("Marking case for re-run.")
        return None  # Treat as not completed
```

### Temp File Cleanup

**On batch completion:**
```python
# Clean up .tmp files (if any remain from interrupted writes)
for tmp_file in batch_dir.glob("*.tmp"):
    tmp_file.unlink()
```

**On startup:**
```python
# Before batch execution, clean stale .tmp files from previous crash
batch_dir.mkdir(parents=True, exist_ok=True)
for tmp_file in batch_dir.glob("*.tmp"):
    print(f"Removing stale temp file: {tmp_file.name}")
    tmp_file.unlink()
```

---

## Implementation Plan

### Files to Change

| File | Change Type | LOC Estimate |
|------|-------------|--------------|
| `scripts/run_gate4_batched.py` | Modify `run_batch()`, add helpers | +80 lines |
| `scripts/run_gate4_batched.py` | Add `save_case_checkpoint()`, `save_manifest()` | +40 lines |
| `scripts/run_gate4_batched.py` | Add `load_case_result()`, `rebuild_manifest()` | +50 lines |
| **Total** | | **+170 lines** |

### Testing Requirements

#### Unit Tests (NEW)

**File:** `tests/test_checkpointing.py`

**Cases:**
1. **test_save_case_checkpoint_atomic** — verify `.tmp` → `.json` atomic replace
2. **test_manifest_update** — verify manifest updates correctly after each case
3. **test_resume_from_partial** — simulate crash at case 18/24, verify resume skips 0-17
4. **test_corrupted_manifest_recovery** — corrupt manifest, verify rebuild from `case_*.json`
5. **test_corrupted_case_file** — corrupt `case_017.json`, verify re-run triggers
6. **test_cleanup_tmp_files** — verify stale `.tmp` files removed on startup

**Estimated effort:** 6 tests × 20 min = 2 hours

#### Integration Test (CRITICAL)

**Scenario:** Simulate OOM crash mid-batch on dev machine.

**Protocol:**
1. Run batch 1 (24 cases)
2. Kill process at case 18 (SIGKILL or manual interrupt)
3. Verify manifest shows 18 completed, 6 pending
4. Resume with `--resume`
5. Verify cases 0-17 skipped, cases 18-23 run
6. Verify final `results.json` contains all 24 cases

**Estimated effort:** 1 hour

---

## Backward Compatibility

### Existing Runs

**No breaking changes:**
- Existing `results.json` format unchanged
- New `manifest.json` and `case_*.json` are ADDITIONS
- Existing scripts reading `results.json` work as-is

### Migration Path

**Old runs (no checkpointing):**
- Missing `manifest.json` → treated as "not started"
- Missing `case_*.json` → all cases run from scratch

**New runs:**
- `manifest.json` + `case_*.json` created incrementally
- `results.json` merged at batch end for backward compat

---

## Performance Impact

### I/O Overhead

**Per-case writes:**
- `case_NNN.json` write: ~1 KB per file, ~0.1 sec (SSD)
- `manifest.json` update: ~0.5 KB, ~0.05 sec
- **Total per case:** ~0.15 sec

**Batch overhead:**
- 24 cases × 0.15 sec = 3.6 sec per batch
- Batch runtime: ~16 min (960 sec)
- **Overhead: 3.6 / 960 = 0.4%** (negligible)

### Memory Impact

**No change:**
- Per-case checkpoints write to disk immediately
- No additional in-memory accumulation
- Memory usage: same as current (dominated by `np.linalg.eigh()`)

---

## Alternative Approaches Considered (And Rejected)

### Alternative 1: SQLite Database

**Pros:**
- Transactional safety (ACID guarantees)
- Single file (no `case_*.json` clutter)

**Cons:**
- Dependency (sqlite3 is stdlib, but adds complexity)
- Lock contention (single-threaded writes only)
- Harder to inspect (need SQL client, not just `cat`)

**Verdict:** Rejected. JSON files easier to debug, inspect, version-control.

### Alternative 2: HDF5 Checkpointing

**Pros:**
- Efficient for large numerical arrays
- Structured hierarchical storage

**Cons:**
- Dependency (`h5py` not stdlib)
- Overkill for ~1 KB per case
- Harder to inspect (need `h5dump` or Python)

**Verdict:** Rejected. JSON sufficient for current scale (216 cases).

### Alternative 3: Single `progress.json` (All Cases)

**Format:**
```json
{
  "completed": [
    {"case_id": 0, "true_ipr_mean": 0.023, ...},
    {"case_id": 1, "true_ipr_mean": 0.045, ...}
  ]
}
```

**Pros:**
- Single file (less clutter)

**Cons:**
- Must rewrite ENTIRE file on each case (not atomic)
- File grows large (24 cases × 1 KB = 24 KB per batch)
- Corrupted write loses ALL progress

**Verdict:** Rejected. Per-case files safer (atomic, isolated corruption).

---

## Risk Assessment

### Risk 1: Atomic Write Failure

**Scenario:** `os.replace()` interrupted by SIGKILL.

**Mitigation:**
- POSIX/Windows guarantee `os.replace()` is atomic (kernel-level)
- Worst case: old file remains, no corruption
- Recovery: Retry case (idempotent)

**Residual risk:** Low (OS-level guarantee)

### Risk 2: Disk Full During Write

**Scenario:** SSD full, `json.dump()` truncates file.

**Mitigation:**
- Write to `.tmp` first (failure leaves original intact)
- Manifest validation detects truncated JSON (raises `JSONDecodeError`)
- Recovery: Re-run case

**Residual risk:** Medium (depends on disk monitoring)

**Recommendation:** Add disk space check at batch start:
```python
import shutil
free_gb = shutil.disk_usage(batch_dir).free / (1024**3)
if free_gb < 1.0:
    raise RuntimeError(f"Insufficient disk space: {free_gb:.2f} GB free")
```

### Risk 3: Manifest Rebuild from Corrupted Files

**Scenario:** Both `manifest.json` AND multiple `case_*.json` corrupted.

**Mitigation:**
- Rebuild skips corrupted case files (logged as warning)
- User manually inspects warnings, decides to re-run or accept partial

**Residual risk:** Low (requires simultaneous multi-file corruption, unlikely)

---

## Next Steps (Implementation)

### Step 1: Design Review (This Document)

**Action:** Review this plan with user.  
**Decision:** Approve / revise / reject.  
**Duration:** 30 min

### Step 2: Implement Checkpointing Logic

**Tasks:**
1. Add `save_case_checkpoint()` helper (20 min)
2. Add `save_manifest()` helper (15 min)
3. Modify `run_batch()` to call helpers (30 min)
4. Add `load_case_result()` recovery logic (20 min)
5. Add stale `.tmp` cleanup on startup (10 min)

**Duration:** 1.5 hours

### Step 3: Write Unit Tests

**File:** `tests/test_checkpointing.py`  
**Tasks:** 6 test cases (see Testing Requirements)  
**Duration:** 2 hours

### Step 4: Integration Test

**Scenario:** Simulated OOM crash mid-batch  
**Duration:** 1 hour

### Step 5: Documentation Update

**Files to update:**
- `PRE_RERUN_CHECKLIST.md` — add checkpoint validation step
- `README.md` — document `--resume` with per-case granularity
- `scripts/run_gate4_batched.py` docstring — update resume behavior

**Duration:** 30 min

### Total Effort

| Phase | Duration |
|-------|----------|
| Design review | 30 min |
| Implementation | 1.5 hours |
| Unit tests | 2 hours |
| Integration test | 1 hour |
| Documentation | 30 min |
| **TOTAL** | **5.5 hours** |

---

## Open Questions

### Q1: Should we compress `case_*.json` files?

**Context:** 24 files × 1 KB = 24 KB per batch. 9 batches = 216 KB total.

**Options:**
- **Option A:** No compression (simplicity, inspectability)
- **Option B:** gzip per file (`case_000.json.gz`)
- **Option C:** tar.gz entire batch at completion

**Recommendation:** Option A (no compression). 216 KB is tiny, inspectability > space savings.

### Q2: What if user runs `--force` with partial checkpoint?

**Current behavior:** `--force` overwrites entire batch (line 532).

**With checkpointing:**
- Option A: `--force` deletes `manifest.json` + all `case_*.json` → clean slate
- Option B: `--force` re-runs all cases but keeps checkpoints (idempotent)

**Recommendation:** Option A (delete checkpoints). `--force` = "start fresh", user expects clean state.

### Q3: Should manifest track runtime per case?

**Context:** Currently only in per-case files.

**Pros:** Easier to compute batch ETA without loading all case files.

**Cons:** Duplicates data (already in `case_*.json`).

**Recommendation:** NO. Keep manifest minimal. Compute ETA on-demand from case files if needed.

---

## Appendix: File Structure Example

### Before Checkpointing (Current)

```
reports/RUNS/gate4_fss_v0.1.24/batches/batch_03/
├── batch_config.json       # Saved at batch END
├── results.json            # Saved at batch END (all 24 cases)
├── timing.json             # Saved at batch END
├── status.json             # Saved at batch END
└── summary.md              # Saved at batch END
```

**Crash at case 18/24:**  
→ NO files written → entire batch re-run

### After Checkpointing (Proposed)

```
reports/RUNS/gate4_fss_v0.1.24/batches/batch_03/
├── manifest.json           # Updated after EACH case
├── case_000.json           # Saved after case 0 completes
├── case_001.json
├── ...
├── case_017.json           # Last completed before crash
├── batch_config.json       # Saved at batch END
├── results.json            # Merged from case_*.json at batch END
├── timing.json
├── status.json
└── summary.md
```

**Crash at case 18/24:**  
→ `manifest.json` shows 18 completed  
→ `--resume` skips cases 0-17, runs 18-23  
→ Total wasted: 0 cases (vs 18 in current design)

---

## Success Criteria

### Checkpointing is successful if:

1. ✅ Batch interrupted at case N → resume skips cases 0..(N-1)
2. ✅ Corrupted `manifest.json` → rebuild from `case_*.json` without user intervention
3. ✅ Corrupted `case_017.json` → case 17 re-run, others skipped
4. ✅ Runtime overhead <1% (measured on batch 1 before/after)
5. ✅ All unit tests pass (6/6 green)
6. ✅ Integration test: kill at case 18 → resume completes remaining 6 cases
7. ✅ Backward compat: existing scripts reading `results.json` work unchanged

---

**Status:** PLAN ONLY — awaiting approval before implementation

**Next action:** User reviews this plan → approve / revise / reject
