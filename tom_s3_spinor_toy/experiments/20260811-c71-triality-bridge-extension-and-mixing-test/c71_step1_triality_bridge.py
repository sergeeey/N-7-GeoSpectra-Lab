"""C71 step 1 -- extend C70's round59<->G102 bridge to all three triality
channels. C70 found the intertwiner U_v: Sigma_r59 -> channel_v only. Before
any mixing-matrix test is meaningful, U_s and U_c (Sigma_r59 -> channel_s,
channel_c) must be found and verified the SAME independent way -- not assumed
from triality symmetry, since no explicit triality operator relating
v_out/s_out/c_out exists in this codebase (checked: they are genuinely
distinct matrices, not related by an already-known map).

Reuses C70's run_direct_solve / test_representation_intertwiner /
compute_structure_tensor unmodified (imported, not copied) and G102's
restrict_to_subalgebra (also unmodified) for the s/c channel generator sets.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c71_step1.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C70 = load_module(
    "c70_bridge_diagnostics",
    HERE.parent
    / "20260811-c70-independent-bridge-fingerprint-and-direct-solve"
    / "c70_bridge_diagnostics.py",
)
C68 = C70.C68  # already-loaded ob11ii_complexification_bridge module
G102 = C68.G102


def su3_g102_on_channel_s() -> list[np.ndarray]:
    der = G102.derivation_basis()
    su3 = G102.stabilizer_basis(der)
    _v_out, s_out, _c_out = G102.restrict_to_subalgebra(su3)
    return [g.astype(complex) for g in s_out]


def su3_g102_on_channel_c() -> list[np.ndarray]:
    der = G102.derivation_basis()
    su3 = G102.stabilizer_basis(der)
    _v_out, _s_out, c_out = G102.restrict_to_subalgebra(su3)
    return [g.astype(complex) for g in c_out]


def bridge_one_channel(
    gens_r59: list[np.ndarray], gens_channel: list[np.ndarray], seed: int
) -> dict:
    """Exactly C70's pipeline: direct solve for Phi, positive/negative
    controls, then the representation-space intertwiner U given Phi."""
    solve = C70.run_direct_solve(gens_r59, gens_channel, n_trials=15, norm_weight=5.0, seed=seed)
    pos = C70.test_positive_control(gens_channel)
    neg = C70.test_negative_control(gens_r59, seed=seed + 1000)
    rep = C70.test_representation_intertwiner(gens_r59, gens_channel, solve["best"]["phi"])

    def strip_phi(d: dict) -> dict:
        out = dict(d)
        out["best"] = {k: v for k, v in d["best"].items() if k != "phi"}
        return out

    return {
        "solve": strip_phi(solve),
        "positive_control": strip_phi(pos),
        "negative_control": strip_phi(neg),
        "representation_intertwiner": rep,
    }


def main() -> None:
    gens_r59 = C68.to_numpy_su3_r59()
    gens_s = su3_g102_on_channel_s()
    gens_c = su3_g102_on_channel_c()

    print("=== Bridge to channel_s ===")
    result_s = bridge_one_channel(gens_r59, gens_s, seed=201)
    print(result_s["solve"]["best"])
    print(result_s["representation_intertwiner"])

    print("\n=== Bridge to channel_c ===")
    result_c = bridge_one_channel(gens_r59, gens_c, seed=301)
    print(result_c["solve"]["best"])
    print(result_c["representation_intertwiner"])

    results = {
        "channel_s": result_s,
        "channel_c": result_c,
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
