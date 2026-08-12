"""C89 -- extends C86's joint-level coupling test (n=0<->n=1, level k=1's
full certified Hilbert space) to round119's so(4)_2 (BLOCK2=[4,5,6,7],
so4_all[6:12]), the second octonion block, previously only tested at
n=0's scalar approximation (C82).

Per C88's own finding: the S3-side coupling channel (Z_i's matrix
elements between D-bar's adjacent-n eigenspaces) is candidate-
INDEPENDENT -- it depends only on round67's own Z_i, not on which S6-side
generator triple is paired with it. So the necessary condition for a
crossing (nonzero S3-side channel) is already known to hold for ANY
candidate using this T=sum Z_i(x)Leibniz(g_i) construction; what remains
genuinely candidate-specific is whether THIS candidate's own Leibniz(g_i)
combines with that channel to produce an actual joint-operator crossing.
This round tests that for so(4)_2, on the genuinely richer k=1 joint
space, for the first time (C82 only tested it at n=0's scalar
approximation, unable to probe n=0<->n=1 mixing at all).

Reuses C86's build_full_level_d_s3/build_coupling_on_full_level/
run_full_level_test directly (K=1, so4_all[6:12] instead of so4_all[0:6]),
and C79/C73's underlying machinery, all unmodified.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c89.json"


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
    K = 1
    print(f"=== Step 1: build FULL level k={K} D_S3 (certified substrate, reused) ===")
    d_s3_full, d_s3_info = C86.build_full_level_d_s3(K)
    print(d_s3_info)

    print(f"\n=== Step 2: verify D_S3 reproduces BOTH physical n's living in k={K} ===")
    target_check = C86.check_d_s3_full_matches_target(d_s3_full, K)
    print(target_check)
    assert target_check["both_match"], (
        "D_S3 full-level construction does not match round67's own target -- stop"
    )

    print("\n=== Step 3: build T (so(4)_2, embedded via identity on p,q) ===")
    so4_all = C79.SO4MOD.build_so4xso4_basis()
    so4_2 = so4_all[6:12]
    self_dual, anti_self_dual = C79.self_dual_anti_self_dual_triples(so4_2)

    print("=== su(2) closure sanity (same check C82 ran) ===")
    sd_closure = C79.check_su2_closure(self_dual)
    asd_closure = C79.check_su2_closure(anti_self_dual)
    print("self-dual closure:", sd_closure)
    print("anti-self-dual closure:", asd_closure)

    dim_pr = d_s3_info["dim_pr"]
    t_self = C86.build_coupling_on_full_level(K, self_dual, dim_pr)
    t_anti = C86.build_coupling_on_full_level(K, anti_self_dual, dim_pr)
    print(f"T (self-dual) shape: {t_self.shape}, T (anti-self-dual) shape: {t_anti.shape}")

    print("\n=== Step 4: build D_S6, run raw-kernel-excluded test on the FULL joint space ===")
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
            f"base_is_hermitian={r['base_is_hermitian']}, "
            f"max_imag_seen={r['max_imaginary_part_seen']:.2e}, "
            f"nonartifact_full_crossings={len(r['full_spectrum_nonartifact_crossings'])}, "
            f"global_min={r['compressed_global_min']:.6f} at eps={r['compressed_global_min_at_eps']:.3f}"
        )

    no_genuine_signal = all(
        r["compressed_n_crossings"] == 0 and len(r["full_spectrum_nonartifact_crossings"]) == 0
        for r in results.values()
    )
    print(f"\nno_genuine_signal_found (n=0<->n=1 coupling, so(4)_2): {no_genuine_signal}")

    out = {
        "k": K,
        "candidate": "so(4)_2 (round119 BLOCK2, so4_all[6:12])",
        "d_s3_full_info": d_s3_info,
        "target_crosscheck": target_check,
        "su2_closure_self_dual": sd_closure,
        "su2_closure_anti_self_dual": asd_closure,
        "results": results,
        "no_genuine_signal_found": no_genuine_signal,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
