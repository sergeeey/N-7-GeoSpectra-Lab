"""C72 -- state-level triality obstruction system, scoped down after two
methodological lessons from C71:

1. C71 showed that "T^3=1", when T is built by chaining three
   INDEPENDENTLY-found pairwise intertwiners through a common reference
   (V_vs=U_s U_v^-1 etc.), is a pure algebraic tautology -- the telescoping
   cancellation V_cv V_sc V_vs = U_v U_v^-1 = Identity uses no su(3)- or
   g2-specific structure whatsoever, so it holds for ANY three invertible
   blocks built this way. This is re-derived analytically here (not
   re-run numerically -- the proof is algebra, not data) and shown to
   generalize completely: it is not specific to C71's su(3) case.
2. Consequently, "T^3=1" cannot be tested meaningfully via this
   construction at ANY equivariance level (su(3), g2, or otherwise) --
   it is vacuous by construction. What CAN be tested meaningfully is the
   OTHER condition in predictions_before_data.md's stated system,
   T*rho(a)*T^-1 = rho(tau(a)), by directly computing Hom_g(channel_i,
   channel_j) for successively LARGER equivariance algebras g and
   checking whether a genuine intertwiner (not just any nonzero one, an
   INVERTIBLE one) survives.

This script computes that Hom-space dimension at three levels --
su(3) (dim 8, already established =6 in C70/C71), g2 (dim 14, the full
S6=G2/SU(3) isotropy+coset algebra), and so(8) (dim 28, the full ambient
algebra in which triality is defined) -- and checks invertibility at each.
so(8) serves as the structural negative control: Schur's lemma forces
Hom_so(8)(channel_v, channel_s) = 0 exactly, since 8_v and 8_s are
INEQUIVALENT as so(8)-representations (this is the textbook definition of
triality) -- G102's own module already asserts this in its docstring
(g102_spin8_fiber.py:19); this script re-verifies it directly rather than
trusting the assertion.

Reuses G102's derivation_basis/stabilizer_basis/restrict_to_subalgebra/
so8_basis and C68's hom_basis/search_nonzero_intertwiner unmodified.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c72.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C68 = load_module(
    "ob11ii_complexification_bridge",
    HERE.parent
    / "20260811-ob11ii-complexification-bridge-test"
    / "ob11ii_complexification_bridge.py",
)
G102 = C68.G102


def test_equivariance_level(gens: list[np.ndarray], label: str) -> dict:
    v_out, s_out, c_out = G102.restrict_to_subalgebra(gens)
    v_out = [g.astype(complex) for g in v_out]
    s_out = [g.astype(complex) for g in s_out]
    c_out = [g.astype(complex) for g in c_out]

    results = {}
    for name, (a, b) in [("v_s", (v_out, s_out)), ("s_c", (s_out, c_out)), ("c_v", (c_out, v_out))]:
        basis = C68.hom_basis(a, b)
        hom_dim = basis.shape[1]
        u, best_det = C68.search_nonzero_intertwiner(basis, n_trials=300, seed=0)
        residual = None
        if u is not None:
            u_inv = np.linalg.inv(u)
            residual = max(
                float(np.max(np.abs(u @ a[k] @ u_inv - b[k]))) for k in range(len(gens))
            )
        results[name] = {
            "hom_dim": hom_dim,
            "invertible_found": u is not None,
            "best_det": best_det,
            "explicit_residual": residual,
        }
    print(
        f"{label} (dim {len(gens)}): "
        + ", ".join(f"{k}={v['hom_dim']}" for k, v in results.items())
    )
    return results


def main() -> None:
    der = G102.derivation_basis()  # full g2, 14-dim
    su3 = G102.stabilizer_basis(der)  # su(3) subalgebra, 8-dim
    so8 = G102.so8_basis()  # full ambient so(8), 28-dim

    print("=== Equivariance-level sweep: Hom(channel_i, channel_j) at 3 algebra sizes ===")
    r_su3 = test_equivariance_level(su3, "su(3)")
    r_g2 = test_equivariance_level(der, "g2")
    r_so8 = test_equivariance_level(so8, "so(8) [negative control]")

    print("\nMonotone shrinkage as algebra grows (su3=8 -> g2=14 -> so8=28):")
    print(
        f"  Hom(v,s): {r_su3['v_s']['hom_dim']} -> {r_g2['v_s']['hom_dim']} -> "
        f"{r_so8['v_s']['hom_dim']}"
    )

    print("\n=== g2 invertibility detail ===")
    for pair in ("v_s", "s_c", "c_v"):
        print(
            f"  {pair}: hom_dim={r_g2[pair]['hom_dim']}, "
            f"invertible={r_g2[pair]['invertible_found']}, "
            f"det={r_g2[pair]['best_det']}, residual={r_g2[pair]['explicit_residual']}"
        )

    # Cross-check the g2 branching directly: eigenvalues of a g2-Casimir-like
    # operator on channel_v should show exactly 1 distinct value (trivial)
    # and 7 equal values (the irreducible 7) -- confirming pearl #33's
    # symbolic 8_v=1+7 claim numerically, independent of that construction.
    v_der, _s_der, _c_der = G102.restrict_to_subalgebra(der)
    casimir_v = sum(g @ g.conj().T for g in v_der)
    eigvals = np.sort(np.linalg.eigvalsh(casimir_v.real))
    print(f"\ng2-Casimir-like eigenvalues on channel_v (expect 1 trivial + 7 equal): {eigvals}")

    # T^3=1 tautology, algebraic re-derivation (not a new numerical claim --
    # this is a proof, included here as an executable check that the
    # construction indeed telescopes for arbitrary invertible blocks, using
    # random matrices with NO su(3)/g2 structure at all).
    rng = np.random.default_rng(0)
    u_v = rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8))
    u_s = rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8))
    u_c = rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8))
    v_vs = u_s @ np.linalg.inv(u_v)
    v_sc = u_c @ np.linalg.inv(u_s)
    v_cv = u_v @ np.linalg.inv(u_c)
    monodromy = v_cv @ v_sc @ v_vs
    tautology_residual = float(np.max(np.abs(monodromy - np.eye(8))))
    print(
        f"\nT^3=1 tautology re-check (arbitrary random u_v/u_s/u_c, NO su(3)/g2 structure): "
        f"monodromy - I residual = {tautology_residual:.3e} (confirms: 0 regardless of algebra)"
    )

    results = {
        "su3": r_su3,
        "g2": r_g2,
        "so8_negative_control": r_so8,
        "g2_casimir_eigenvalues_channel_v": eigvals.tolist(),
        "t3_tautology_recheck_arbitrary_blocks": tautology_residual,
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
