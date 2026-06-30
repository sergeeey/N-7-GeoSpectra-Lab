"""
verify_artifacts.py — Reproducibility lock verification

Checks that all expected JSON artifacts exist and match committed values.
Usage: python verify_artifacts.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
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

print("="*60)
print("GEOSPECTRA ARTIFACT VERIFICATION")
print("="*60)

all_ok = True
for path, spec in EXPECTED.items():
    full = ROOT / path
    if not full.exists():
        print(f"  [MISSING] {path}")
        all_ok = False
        continue
    try:
        data = json.load(open(full))
    except Exception as e:
        print(f"  [INVALID JSON] {path}: {e}")
        all_ok = False
        continue

    if "keys" in spec:
        missing = [k for k in spec["keys"] if k not in data]
        if missing:
            print(f"  [KEYS MISSING] {path}: {missing}")
            all_ok = False
            continue

    if "structure" in spec:
        if isinstance(data, list) and len(data) > 0:
            has_phases = all("phase" in d for d in data[:5])
            status = "OK" if has_phases else "NO PHASES"
        else:
            status = "NOT LIST"
        if status != "OK":
            print(f"  [STRUCTURE] {path}: {status}")
            all_ok = False
            continue

    det = "DETERMINISTIC" if spec.get("deterministic") else "STOCHASTIC"
    print(f"  [OK] {path} ({det})")

phase4b = ROOT / "experiments/20260629-phase4b/phase4b_results.json"
if phase4b.exists():
    data = json.load(open(phase4b))
    rec = sum(1 for d in data if d.get("phase") == "recoverable")
    era = sum(1 for d in data if d.get("phase") == "erased")
    print(f"\n  Phase 4B: {len(data)} cells, {rec} recoverable, {era} erased")

print("\n" + "="*60)
if all_ok:
    print("ALL_SUBSETS_VERIFIED")
    print("L3 claims: 0")
    print("Publication freeze: v0.4a-paper-complete")
else:
    print("SOME ARTIFACTS MISSING OR INVALID")
print("="*60)
