"""Round125: are SO(4)xSO(4) (round119) and su(3)+centralizer (round124) the
SAME subalgebra of so(8) in different language, or genuinely different?

This is round124's own flagged open question (decision.md Relaxation Map,
row 3): "Cross-check against SO(4)xSO(4): are these two candidates the SAME
underlying structure in different language, or genuinely different?" -- not
attempted there, a natural next question given both are rank-4, both escape
SO(7)/fix-zero-vectors, both emerge from breaking G2.

Both candidates already live in the SAME 8-dim vector representation of
so(8) (8x8 antisymmetric matrices acting on 8_v):
  - round119's SO(4)xSO(4): experiments/20260715-l3b-triality-so4xso4-invariance
    /triality_so4xso4_invariance.py:build_so4xso4_basis() -- 12 generators
    (6+6, block-diagonal rotations of the two 4-dim octonion blocks H, Hl).
  - round124's su(3)+centralizer: reuses G102's derivation_basis() ->
    stabilizer_basis() (su(3), 8 generators) + centralizer_dim() (2 more
    generators) -- 10 generators total, all 8x8 antisymmetric so(8) elements.

Test: stack both generator sets as 64-dim vectors (flattened 8x8 matrices),
compute rank(A), rank(B), rank(A union B) via SVD. Then:
  dim(A ∩ B) = dim(A) + dim(B) - dim(A ∪ B)   (standard subspace-intersection identity)

This directly answers "same / one-contains-other / independent / partial
overlap" without needing to guess -- a genuinely cheap, differentiating test
(CDT protocol: differentiates between 4 mutually exclusive outcomes, no
circularity, reuses already-verified machinery from both source rounds).
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_round125.json"
TOL = 1e-8

SO4_MODULE_PATH = (
    HERE.parent / "20260715-l3b-triality-so4xso4-invariance" / "triality_so4xso4_invariance.py"
)
_spec_so4 = importlib.util.spec_from_file_location("triality_so4xso4_invariance", SO4_MODULE_PATH)
assert _spec_so4 and _spec_so4.loader
SO4MOD = importlib.util.module_from_spec(_spec_so4)
_spec_so4.loader.exec_module(SO4MOD)

G102_PATH = HERE.parent / "20260705-g102-spin8-fiber-obstruction" / "g102_spin8_fiber.py"
_spec_g102 = importlib.util.spec_from_file_location("g102_spin8_fiber", G102_PATH)
assert _spec_g102 and _spec_g102.loader
G102 = importlib.util.module_from_spec(_spec_g102)
_spec_g102.loader.exec_module(G102)


def subspace_rank(mats: list[np.ndarray]) -> int:
    if not mats:
        return 0
    flat = np.array([m.reshape(-1) for m in mats])
    s = np.linalg.svd(flat, compute_uv=False)
    return int(np.sum(s > TOL * max(1.0, s[0] if len(s) else 1.0)))


def main() -> None:
    # --- Candidate A: SO(4)xSO(4), round119 ---
    so4xso4 = SO4MOD.build_so4xso4_basis()  # (12, 8, 8)
    so4xso4_list = [so4xso4[i] for i in range(so4xso4.shape[0])]
    dim_a = subspace_rank(so4xso4_list)

    # --- Candidate B: su(3) + centralizer, round124 (reuse G102 machinery directly) ---
    der = G102.derivation_basis()
    su3 = G102.stabilizer_basis(der)
    _cent_dim, cent_su3 = G102.centralizer_dim(su3)
    combined_b = su3 + cent_su3
    dim_b = subspace_rank(combined_b)

    # --- Union rank ---
    union_list = so4xso4_list + combined_b
    dim_union = subspace_rank(union_list)

    dim_intersection = dim_a + dim_b - dim_union

    if dim_intersection == dim_a == dim_b:
        verdict = "IDENTICAL"
    elif dim_intersection == dim_b:
        verdict = "B_SUBALGEBRA_OF_A"
    elif dim_intersection == dim_a:
        verdict = "A_SUBALGEBRA_OF_B"
    elif dim_intersection == 0:
        verdict = "INDEPENDENT_NO_OVERLAP"
    else:
        verdict = "PARTIAL_OVERLAP"

    results = {
        "round": 125,
        "dim_A_so4xso4": dim_a,
        "dim_B_su3_plus_centralizer": dim_b,
        "dim_A_union_B": dim_union,
        "dim_A_intersect_B": dim_intersection,
        "verdict": verdict,
    }

    print("=" * 92)
    print("Round125 -- SO(4)xSO(4) (round119) vs su(3)+centralizer (round124): same or different?")
    print("=" * 92)
    print(f"dim(A) SO(4)xSO(4)            = {dim_a} (predict 12)")
    print(f"dim(B) su(3)+centralizer      = {dim_b} (predict 10)")
    print(f"dim(A union B)                = {dim_union}")
    print(f"dim(A intersect B)            = {dim_intersection}")
    print()
    print(f"VERDICT: {verdict}")

    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"\nResults -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
