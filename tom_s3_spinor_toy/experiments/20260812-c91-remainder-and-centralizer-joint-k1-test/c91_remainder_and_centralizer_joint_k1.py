"""C91 -- extends C86's joint k=1 coupling test to (P1) C83's 9-dim
so(8) remainder (3 groups of 3, SVD-derived) and (P2) C75's 2-dim
centralizer (u1_a, u1_b, adapted with a zero-padded 3rd generator).
Both were previously tested only at n=0's scalar approximation (C83) or
against round59's S6-only D directly (C75, a different question --
symmetry commutation, not spectral crossing on the joint level).

See claim.md for the same-day correction to C89's own "C75's 10-dim
centralizer" phrasing (should be "2-dim centralizer, from a 10-dim
ambient space" -- the 10 refers to v_out_10, not the centralizer itself).

Reuses C86's build_full_level_d_s3/check_d_s3_full_matches_target/
build_coupling_on_full_level/run_full_level_test, C83's
find_su3_overlap_direction/build_remaining_complement_basis/
build_complement_basis (to regenerate the SAME 9-dim remainder,
deterministic), and C75's get_centralizer_generators_on_channel_v, all
unmodified.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c91.json"


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
C83 = load_module(
    "c83_remaining_complement",
    HERE.parent / "20260811-c83-remaining-complement-test" / "c83_remaining_complement.py",
)
C75 = load_module(
    "c75_gate2_symmetry_check",
    HERE.parent
    / "20260811-c75-gate2-physical-d-vs-extended-symmetry"
    / "c75_gate2_symmetry_check.py",
)


def build_c83_remainder_groups() -> dict:
    """Regenerates C83's own 9-dim remainder basis (deterministic SVD),
    reshaped into the same 3 groups of 3 C83 itself tested."""
    so4_all = C79.SO4MOD.build_so4xso4_basis()
    so4_flat = np.array([g.reshape(-1) for g in so4_all]).astype(complex)

    u_v, _ = C79.get_bridge_to_sigma()
    u_v_inv = np.linalg.inv(u_v)
    R59 = C79.R59
    C73 = C79.C73
    E = R59.build_clifford(conj=False)
    d_mat = C73.build_numeric_dirac(E, R59.NOMIZU)

    complement_basis, complement_rank = C83.build_complement_basis(u_v_inv, u_v, d_mat)
    assert complement_rank == 20, f"expected complement_rank=20, got {complement_rank}"
    remaining_generators, remaining_info = C83.build_remaining_complement_basis(
        so4_flat, complement_basis
    )
    assert remaining_info["remaining_dim"] == 9, (
        f"expected 9-dim remainder, got {remaining_info['remaining_dim']}"
    )
    groups = {
        "group_0_1_2": remaining_generators[0:3].reshape(3, 8, 8),
        "group_3_4_5": remaining_generators[3:6].reshape(3, 8, 8),
        "group_6_7_8": remaining_generators[6:9].reshape(3, 8, 8),
    }
    return {"groups": groups, "remaining_info": remaining_info, "d_mat": d_mat}


def run_group(label: str, triple, K: int, d_s3_full, dim_pr: int, d_s6) -> dict:
    t_gen = C86.build_coupling_on_full_level(K, triple, dim_pr)
    r = C86.run_full_level_test(d_s3_full, t_gen, d_s6)
    print(
        f"  {label}: compressed_n_crossings={r['compressed_n_crossings']}, "
        f"base_is_hermitian={r['base_is_hermitian']}, "
        f"max_imag_seen={r['max_imaginary_part_seen']:.2e}, "
        f"nonartifact_full_crossings={len(r['full_spectrum_nonartifact_crossings'])}, "
        f"global_min={r['compressed_global_min']:.6f} at eps={r['compressed_global_min_at_eps']:.3f}"
    )
    return r


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
    dim_pr = d_s3_info["dim_pr"]

    R59 = C79.R59
    C73 = C79.C73
    E = R59.build_clifford(conj=False)
    d_s6 = C73.build_numeric_dirac(E, R59.NOMIZU)

    print("\n=== P1: regenerate C83's own 9-dim remainder, 3 groups of 3 ===")
    remainder = build_c83_remainder_groups()
    print("remaining_info:", remainder["remaining_info"])

    p1_results = {}
    for label, triple in remainder["groups"].items():
        print(f"\n--- P1 group {label} ---")
        p1_results[label] = run_group(label, triple, K, d_s3_full, dim_pr, d_s6)

    p1_no_signal = all(
        r["compressed_n_crossings"] == 0 and len(r["full_spectrum_nonartifact_crossings"]) == 0
        for r in p1_results.values()
    )
    print(f"\nP1 no_genuine_signal_found (all 3 remainder groups): {p1_no_signal}")

    print("\n=== P2: C75's 2-dim centralizer (u1_a, u1_b), zero-padded to a triple ===")
    u1_a, u1_b, cent_sanity = C75.get_centralizer_generators_on_channel_v()
    print("centralizer sanity (reused from C75, unmodified):", cent_sanity)
    zero_gen = np.zeros((8, 8), dtype=complex)
    centralizer_triple = np.array([u1_a, u1_b, zero_gen])
    p2_result = run_group("centralizer_padded", centralizer_triple, K, d_s3_full, dim_pr, d_s6)
    p2_no_signal = (
        p2_result["compressed_n_crossings"] == 0
        and len(p2_result["full_spectrum_nonartifact_crossings"]) == 0
    )
    print(f"\nP2 no_genuine_signal_found (centralizer, adapted): {p2_no_signal}")

    out = {
        "k": K,
        "d_s3_full_info": d_s3_info,
        "target_crosscheck": target_check,
        "p1_remainder_info": remainder["remaining_info"],
        "p1_results": p1_results,
        "p1_no_genuine_signal_found": p1_no_signal,
        "p2_centralizer_sanity": cent_sanity,
        "p2_result": p2_result,
        "p2_no_genuine_signal_found": p2_no_signal,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
