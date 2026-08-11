"""C82 -- so(4)_2's two halves, using C81's corrected (raw-kernel-excluded)
non-product coupling test.

C81 fixed the test design (compress D_joint onto Delta_m (x) D_S6's
gapped 28-dim non-kernel eigenspace before sweeping eps, so the
deterministic raw-kernel-crossing mechanism cannot occur by construction)
and reconfirmed so(4)_1's two halves are a clean NULL. This round applies
the IDENTICAL, unmodified pipeline to so(4)_2 (round119's other octonion
block, BLOCK2=[4,5,6,7], generators so4_all[6:12]) -- never before tested
with this corrected methodology (C77's own Gate-2 test of so(4)_2 used
the simple commutator-with-D_S6 test, a different question).

Reuses C81's run_for_triple unmodified (which itself reuses C79's
get_bridge_to_sigma/leibniz_matrix/check_su2_closure and all of C79's own
module-level reuses).
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c82.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C81 = load_module(
    "c81_raw_kernel_excluded_retest",
    HERE.parent / "20260811-c81-raw-kernel-excluded-retest" / "c81_raw_kernel_excluded_retest.py",
)
C79 = C81.C79


def main() -> None:
    C73 = C79.C73
    R59 = C79.R59

    E = R59.build_clifford(conj=False)
    d_s6 = C73.build_numeric_dirac(E, R59.NOMIZU)
    d_s3_scalar = float(C79.sp.Rational(1, 2) * C79.ROUND67.calibrate_h_H())

    so4_all = C79.SO4MOD.build_so4xso4_basis()
    so4_2 = so4_all[6:12]
    self_dual, anti_self_dual = C79.self_dual_anti_self_dual_triples(so4_2)

    print("=== P1: so(4)_2 su(2) closure sanity ===")
    sd_closure = C79.check_su2_closure(self_dual)
    asd_closure = C79.check_su2_closure(anti_self_dual)
    print("self-dual closure:", sd_closure)
    print("anti-self-dual closure:", asd_closure)

    print("\n=== P2: self-dual triple, raw-kernel-excluded ===")
    self_result = C81.run_for_triple(self_dual, "so4_2_self_dual", d_s6, d_s3_scalar)
    print(
        f"compressed: eps0_min={self_result['compressed_eps0_min_abs_eigval']:.4f}, "
        f"n_crossings={self_result['compressed_n_crossings']}, "
        f"global_min={self_result['compressed_global_min']:.6f} "
        f"at eps={self_result['compressed_global_min_at_eps']:.3f}"
    )
    print(
        f"full-spectrum: {len(self_result['full_spectrum_all_crossings'])} total near-zero, "
        f"{len(self_result['full_spectrum_nonartifact_crossings'])} non-artifact"
    )

    print("\n=== P3: anti-self-dual triple, raw-kernel-excluded ===")
    anti_result = C81.run_for_triple(anti_self_dual, "so4_2_anti_self_dual", d_s6, d_s3_scalar)
    print(
        f"compressed: eps0_min={anti_result['compressed_eps0_min_abs_eigval']:.4f}, "
        f"n_crossings={anti_result['compressed_n_crossings']}, "
        f"global_min={anti_result['compressed_global_min']:.6f} "
        f"at eps={anti_result['compressed_global_min_at_eps']:.3f}"
    )
    print(
        f"full-spectrum: {len(anti_result['full_spectrum_all_crossings'])} total near-zero, "
        f"{len(anti_result['full_spectrum_nonartifact_crossings'])} non-artifact"
    )

    no_genuine_signal = (
        self_result["compressed_n_crossings"] == 0
        and anti_result["compressed_n_crossings"] == 0
        and len(self_result["full_spectrum_nonartifact_crossings"]) == 0
        and len(anti_result["full_spectrum_nonartifact_crossings"]) == 0
    )

    results = {
        "su2_closure_self_dual": sd_closure,
        "su2_closure_anti_self_dual": asd_closure,
        "self_dual": self_result,
        "anti_self_dual": anti_result,
        "no_genuine_signal_found": bool(no_genuine_signal),
        "conclusion": (
            "so(4)_2, tested with C81's corrected (raw-kernel-excluded) "
            "methodology: "
            + (
                "NEITHER half produces any crossing outside the raw-kernel "
                "artifact mechanism, matching so(4)_1's own C81 result exactly. "
                "Both octonion blocks of round119's SO(4)xSO(4) candidate are "
                "now clean, rigorously-confirmed NULLs under the corrected test."
                if no_genuine_signal
                else "at least one crossing survives raw-kernel exclusion -- a "
                "genuinely new finding, the first candidate to survive the "
                "corrected test, requiring the same extra scrutiny as any "
                "unexpectedly positive result in this arc before being trusted."
            )
        ),
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
