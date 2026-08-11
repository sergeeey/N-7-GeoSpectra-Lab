"""C87 -- extends C86's joint-level coupling test to k=2 (physical n=1
<-> n=2), a second, independent data point on whether C79-C83's coupling
operator ever produces inter-Peter-Weyl-level mixing.

C86 built level k=1's full Hilbert space (containing physical n=0's
sigma=+1 branch and n=1's sigma=-1 branch simultaneously) and found a
clean NULL for round119's so(4)_1 triples. This round asks the same
question one level up: level k=2's own full Hilbert space (dimension
2*(k+1)^2=18) simultaneously contains physical n=2's sigma=-1 branch
(D-bar=-2, D=-3.5, multiplicity (2+1)(2+2)=12) and physical n=1's
sigma=+1 branch (D-bar=4, D=2.5, multiplicity (1+1)(1+2)=6) -- testing
the n=1<->n=2 pair, genuinely different from C86's n=0<->n=1 pair (k=2's
own space does not contain n=0 at all -- n=0 lives at k=0 and k=1 only).

Reuses C86's own build_full_level_d_s3/check_d_s3_full_matches_target/
build_coupling_on_full_level/run_full_level_test functions directly
(parametrized by K=2), not copy-pasted -- and C85's certified substrate,
C79's coupling construction, C73's build_numeric_dirac, all unmodified.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c87.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C86 = load_module(
    "c86_full_k1_coupling",
    HERE.parent / "20260812-c86-full-k1-level-coupling-test" / "c86_full_k1_coupling.py",
)
C79 = C86.C79


def main() -> None:
    K = 2
    print(f"=== Step 1: build FULL level k={K} D_S3 (certified substrate) ===")
    d_s3_full, d_s3_info = C86.build_full_level_d_s3(K)
    print(d_s3_info)

    print(f"\n=== Step 2: verify D_S3 reproduces BOTH physical n's living in k={K} ===")
    target_check = C86.check_d_s3_full_matches_target(d_s3_full, K)
    print(target_check)
    assert target_check["both_match"], (
        "D_S3 full-level construction does not match round67's own target -- stop"
    )

    print("\n=== Step 3: build T_2 (C79's coupling, embedded via identity on p,q) ===")
    so4_all = C79.SO4MOD.build_so4xso4_basis()
    so4_1 = so4_all[0:6]
    self_dual, anti_self_dual = C79.self_dual_anti_self_dual_triples(so4_1)
    dim_pr = d_s3_info["dim_pr"]
    t_self = C86.build_coupling_on_full_level(K, self_dual, dim_pr)
    t_anti = C86.build_coupling_on_full_level(K, anti_self_dual, dim_pr)
    print(f"T_2 (self-dual) shape: {t_self.shape}, T_2 (anti-self-dual) shape: {t_anti.shape}")

    print(
        f"\n=== Step 4: build D_S6, run raw-kernel-excluded test on the FULL {d_s3_full.shape[0] * 64}-dim joint space ==="
    )
    R59 = C79.R59
    C73 = C79.C73
    E = R59.build_clifford(conj=False)
    d_s6 = C73.build_numeric_dirac(E, R59.NOMIZU)

    results = {}
    for label, t_gen in (("self_dual", t_self), ("anti_self_dual", t_anti)):
        r = C86.run_full_level_test(d_s3_full, t_gen, d_s6)
        results[label] = r
        print(
            f"  {label}: compressed_n_crossings={r['compressed_n_crossings']}, "
            f"nonartifact_full_crossings={len(r['full_spectrum_nonartifact_crossings'])}, "
            f"global_min={r['compressed_global_min']:.6f} at eps={r['compressed_global_min_at_eps']:.3f}"
        )

    no_genuine_signal = all(
        r["compressed_n_crossings"] == 0 and len(r["full_spectrum_nonartifact_crossings"]) == 0
        for r in results.values()
    )
    print(f"\nno_genuine_signal_found (n=1<->n=2 coupling, this specific T): {no_genuine_signal}")

    out = {
        "k": K,
        "d_s3_full_info": d_s3_info,
        "target_crosscheck": target_check,
        "results": results,
        "no_genuine_signal_found": no_genuine_signal,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
