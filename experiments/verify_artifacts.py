"""
verify_artifacts.py — Reproducibility lock verification

Checks that all expected JSON artifacts exist and match committed values.
Usage: python verify_artifacts.py

Audit note (2026-09-06): before this revision, the "keys" check only
verified that expected top-level keys were PRESENT, never that their
values were non-null or otherwise sane, and the "structure" check for
phase4b only sampled the first 5 rows for key presence, never checking
the actual row count or the validity of "phase" values across the whole
file. Reproduced directly: a copy of this file's own unmodified logic,
run against a copy of the real artifacts with every metric value set to
null, phase4b truncated from 36 rows to 1 with an invalid "phase" string,
still printed ALL_SUBSETS_VERIFIED. Fixed below by checking values, not
just keys, and the full file, not just a sample.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

# phase4b's own row count: the generator (phase4b_phase_diagram.py) defines
# the grid as len(W_VALUES)=12 x len(N_CURVED)=1 x len(PAIRS)=3 = 36 cells
# -- verified directly against that file, 2026-09-06. The original
# "structure" comment below said "35 dicts"; that number was never checked
# against the generator and was simply wrong.
PHASE4B_EXPECTED_ROWS = 36
# phase4b_phase_diagram.py's own classification (same file, ~line 166) has
# three outcomes -- recoverable (>=0.95 accuracy), degraded (>=0.70), erased
# (below both) -- "degraded" is a real, expected value, not an error state.
VALID_PHASES = {"recoverable", "degraded", "erased"}
VALID_VERDICTS = {"PASS", "FAIL"}

EXPECTED = {
    "experiments/20260629-hard-negatives/hard_negatives_results.json": {
        "keys": ["t1_same_acc", "t2_fp_rate", "t3_curved_boundary", "t4_ablation"],
        "deterministic": True,
    },
    "experiments/20260629-physics-rescue/physics_rescue_results.json": {
        "keys": ["H1_gauge_bundle", "H2_flux", "H3_orbifold", "H4_ncg", "summary"],
        "deterministic": True,
    },
    "experiments/20260629-phase4d/phase4d_results.json": {
        "keys": ["results", "distinct", "pairs_tested", "percent", "verdict"],
        "deterministic": True,
    },
    "experiments/20260629-phase4c/phase4c_results.json": {
        "keys": ["fingerprints", "comparisons", "baseline_stable", "verdict"],
        "deterministic": True,
    },
    "experiments/20260629-phase4b/phase4b_results.json": {
        "structure": "list of 35 dicts with keys [W,N,pair,sd_acc,phase]",
        "deterministic": False,
    },
}


def value_is_null(v):
    """True for None and for the common 'looks present but empty' shapes a
    poisoned/failed run could plausibly leave behind."""
    if v is None:
        return True
    return bool(isinstance(v, dict) and len(v) == 0)


print("=" * 60)
print("GEOSPECTRA ARTIFACT VERIFICATION")
print("=" * 60)

all_ok = True
for path, spec in EXPECTED.items():
    full = ROOT / path
    if not full.exists():
        print(f"  [MISSING] {path}")
        all_ok = False
        continue
    try:
        with open(full) as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"  [INVALID JSON] {path}: {e}")
        all_ok = False
        continue

    if "keys" in spec:
        missing = [k for k in spec["keys"] if k not in data]
        if missing:
            print(f"  [KEYS MISSING] {path}: {missing}")
            all_ok = False
            continue
        nulled = [k for k in spec["keys"] if value_is_null(data.get(k))]
        if nulled:
            print(f"  [NULL VALUES] {path}: {nulled}")
            all_ok = False
            continue

    if "structure" in spec:
        if isinstance(data, list) and len(data) > 0:
            has_phases = all("phase" in d for d in data)
            status = "OK" if has_phases else "NO PHASES"
        else:
            status = "NOT LIST"
        if status != "OK":
            print(f"  [STRUCTURE] {path}: {status}")
            all_ok = False
            continue
        bad_phases = sorted({d.get("phase") for d in data} - VALID_PHASES)
        if bad_phases:
            print(f"  [INVALID PHASE VALUES] {path}: {bad_phases}")
            all_ok = False
            continue
        if len(data) != PHASE4B_EXPECTED_ROWS:
            print(
                f"  [COUNT MISMATCH] {path}: expected {PHASE4B_EXPECTED_ROWS} "
                f"rows (per this file's own spec), found {len(data)} -- "
                f"pre-existing discrepancy, not fixed here, surfaced instead "
                f"of silently passing"
            )
            all_ok = False
            continue

    det = "DETERMINISTIC" if spec.get("deterministic") else "STOCHASTIC"
    print(f"  [OK] {path} ({det})")

phase4b = ROOT / "experiments/20260629-phase4b/phase4b_results.json"
if phase4b.exists():
    with open(phase4b) as f:
        data = json.load(f)
    rec = sum(1 for d in data if d.get("phase") == "recoverable")
    era = sum(1 for d in data if d.get("phase") == "erased")
    print(f"\n  Phase 4B: {len(data)} cells, {rec} recoverable, {era} erased")

print("\n" + "=" * 60)
if all_ok:
    print("ALL_SUBSETS_VERIFIED")
    print("L3 claims: 0")
    print("Publication freeze: v0.4a-paper-complete")
else:
    print("SOME ARTIFACTS MISSING OR INVALID")
print("=" * 60)

# Audit note (2026-09-06, second pass): a real run against real repo data
# printed [MISSING]/[COUNT MISMATCH] and still exited 0 -- the exact same
# class of bug this revision was meant to fix, one level up: any caller
# checking the process exit code rather than reading the printed text saw
# "success" regardless. Fixed here.
sys.exit(0 if all_ok else 1)
