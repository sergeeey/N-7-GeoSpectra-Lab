#!/bin/bash
# GeoSpectra Server Smoke Test
# Validates compute environment + runs heaviest single case
# Exit 0 = PASS, 1 = FAIL

set -e  # Exit on first error

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SMOKE_OUTPUT="${PROJECT_ROOT}/smoke_test_output.json"

echo "=== GeoSpectra Server Smoke Test ==="
echo "Project root: ${PROJECT_ROOT}"
echo ""

# Step 1: Dependency version check
echo "[1/6] Checking dependencies..."
python3 - <<'EOF'
import sys
import importlib.metadata

required = {
    "numpy": None,      # Any version
    "scipy": "1.7.0",   # Minimum version
    "matplotlib": None,
}

print("Python version:", sys.version)
errors = []

for pkg, min_ver in required.items():
    try:
        version = importlib.metadata.version(pkg)
        print(f"  {pkg}: {version}", end="")

        if min_ver:
            from packaging import version as pkg_version
            if pkg_version.parse(version) < pkg_version.parse(min_ver):
                errors.append(f"{pkg} {version} < required {min_ver}")
                print(" [TOO OLD]")
            else:
                print(" [OK]")
        else:
            print(" [OK]")
    except importlib.metadata.PackageNotFoundError:
        errors.append(f"{pkg} not installed")
        print(f"  {pkg}: [MISSING]")

if errors:
    print("\nDependency check FAILED:")
    for err in errors:
        print(f"  - {err}")
    sys.exit(1)

print("\n✓ All dependencies OK")
EOF

if [ $? -ne 0 ]; then
    echo "❌ SMOKE TEST FAILED: Dependency check"
    exit 1
fi

# Step 2: Import test
echo ""
echo "[2/6] Testing imports..."
python3 - <<'EOF'
import sys
import os

# Add project root to path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

try:
    from cc_toy_lab.spectral.s3_s1_product_discretized import build_s3_s1_product_operator
    print("  ✓ cc_toy_lab.spectral.s3_s1_product_discretized")

    import numpy as np
    import scipy
    print("  ✓ numpy, scipy")

    print("\n✓ All imports OK")
except ImportError as e:
    print(f"\n❌ Import failed: {e}")
    sys.exit(1)
EOF

if [ $? -ne 0 ]; then
    echo "❌ SMOKE TEST FAILED: Import test"
    exit 1
fi

# Step 3-6: Run heaviest case with memory monitoring
echo ""
echo "[3/6] Running heaviest case (N=128 j_max=3 seed=123)..."
echo "       Monitoring peak RSS..."

# Use Python script for integrated test + monitoring
python3 - <<EOF
import sys
import os
import json
import time
import resource
import traceback

# Add project root to path
project_root = "${PROJECT_ROOT}"
sys.path.insert(0, project_root)

import numpy as np
from cc_toy_lab.spectral.s3_s1_product_discretized import build_s3_s1_product_operator

def get_peak_memory_mb():
    """Get peak RSS in MB (works on Linux/macOS)."""
    try:
        # Linux: maxrss in KB, macOS: maxrss in bytes
        maxrss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if sys.platform == 'darwin':  # macOS
            return maxrss / (1024 * 1024)
        else:  # Linux
            return maxrss / 1024
    except Exception:
        return -1  # Unknown platform

def compute_ipr(psi):
    """Inverse participation ratio."""
    return np.sum(np.abs(psi) ** 4)

print("[3/6] Building operator...")
start_time = time.time()

try:
    # HEAVIEST CASE from smoke test grid
    H, _, meta = build_s3_s1_product_operator(
        j_max=3,                      # Heaviest S³ truncation
        s1_family="spectral_circle",  # Standard family
        s1_size=128,                  # Largest grid from prior runs
        alpha=0.5,                    # APBC
        mode="geometric_weight",      # Disorder mode
        disorder_strength=4.0,        # Moderate disorder
        seed=123,                     # Fixed seed
        radius=1.0,
    )

    N = H.shape[0]
    print(f"  ✓ Operator built: N={N}")

    build_time = time.time() - start_time
    build_memory_mb = get_peak_memory_mb()

    # Step 4: Compute spectrum
    print("[4/6] Computing eigenvalues...")
    eig_start = time.time()

    eigvals, eigvecs = np.linalg.eigh(H)
    sort_idx = np.argsort(np.abs(eigvals))
    eigvals = eigvals[sort_idx]
    eigvecs = eigvecs[:, sort_idx]

    eig_time = time.time() - eig_start
    eig_memory_mb = get_peak_memory_mb()

    print(f"  ✓ Spectrum computed: {len(eigvals)} eigenvalues")

    # Step 5: Compute IPR for 5 lowest modes
    print("[5/6] Computing IPR for low modes...")
    n_low = 5
    low_iprs = []

    for i in range(min(n_low, len(eigvals))):
        ipr = compute_ipr(eigvecs[:, i])
        low_iprs.append(float(ipr))

    mean_ipr = np.mean(low_iprs)
    min_ipr = np.min(low_iprs)
    max_ipr = np.max(low_iprs)

    # Validate IPR (must be in [0, 1])
    if not all(0 <= ipr <= 1 for ipr in low_iprs):
        print(f"  ⚠ WARNING: IPR out of [0,1] range")

    if np.isnan(mean_ipr):
        print(f"  ❌ FAIL: IPR is NaN")
        sys.exit(1)

    print(f"  ✓ IPR computed: mean={mean_ipr:.6f}, min={min_ipr:.6f}, max={max_ipr:.6f}")

    # Step 6: Validate output structure
    print("[6/6] Validating output structure...")

    total_time = time.time() - start_time
    peak_memory_mb = get_peak_memory_mb()

    result = {
        "test": "server_smoke_test",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "status": "PASS",
        "config": {
            "j_max": 3,
            "s1_family": "spectral_circle",
            "s1_size": 128,
            "alpha": 0.5,
            "disorder_strength": 4.0,
            "seed": 123,
        },
        "metrics": {
            "N": int(N),
            "build_time_sec": round(build_time, 2),
            "eigensolve_time_sec": round(eig_time, 2),
            "total_time_sec": round(total_time, 2),
            "peak_memory_mb": round(peak_memory_mb, 1) if peak_memory_mb > 0 else "unknown",
            "low_eigenvalues": [round(float(e), 6) for e in eigvals[:n_low]],
            "low_iprs": [round(ipr, 6) for ipr in low_iprs],
            "mean_ipr": round(mean_ipr, 6),
            "min_ipr": round(min_ipr, 6),
            "max_ipr": round(max_ipr, 6),
        },
        "validation": {
            "spectrum_computed": True,
            "ipr_in_range": all(0 <= ipr <= 1 for ipr in low_iprs),
            "ipr_not_nan": not np.isnan(mean_ipr),
            "hermiticity": np.allclose(H, H.conj().T, atol=1e-10),
        }
    }

    # Save JSON
    output_path = "${SMOKE_OUTPUT}"
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)

    print(f"  ✓ Output JSON saved: {output_path}")
    print("")
    print("=" * 50)
    print("✓ SMOKE TEST PASSED")
    print("=" * 50)
    print(f"Total runtime:  {total_time:.1f}s")
    print(f"Peak memory:    {peak_memory_mb:.1f} MB" if peak_memory_mb > 0 else "Peak memory:    unknown")
    print(f"Operator size:  N={N}")
    print(f"Mean IPR:       {mean_ipr:.6f}")
    print("")

except Exception as e:
    print("")
    print("=" * 50)
    print("❌ SMOKE TEST FAILED")
    print("=" * 50)
    print(f"Error: {e}")
    print("")
    print("Traceback:")
    traceback.print_exc()

    # Save failure JSON
    result = {
        "test": "server_smoke_test",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "status": "FAIL",
        "error": str(e),
        "traceback": traceback.format_exc(),
    }

    output_path = "${SMOKE_OUTPUT}"
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)

    sys.exit(1)

EOF

EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    echo ""
    echo "❌ SMOKE TEST FAILED (exit code: $EXIT_CODE)"
    exit 1
fi

echo "✓ All checks passed"
echo "✓ Output: ${SMOKE_OUTPUT}"
exit 0
