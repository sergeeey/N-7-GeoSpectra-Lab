"""C113 -- confirms j2=0 (trivial/singlet auxiliary) cannot break C112's
target_level=2 confound: the resulting [[D,tI],[tI,D]] construction is
similar, via u=x+y/v=x-y (independent of D), to diag(D+tI, D-tI). Since
every dbar_full(k) has an exactly real spectrum, this is algebraically
incapable of breaking reality for any k or t -- confirmed here, not
discovered.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c113.json"

T_SCALE = 1.0
TESTED_LEVELS = (1, 2, 3)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    c85 = load_module(
        "c85_certification",
        HERE.parent
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )
    rmult = [c85.right_mult_matrix_on_ab(u) for u in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))]

    def dbar_full(level: int) -> sp.Matrix:
        l1, l2, l3 = c85.build_l_matrices(level, "repaired")
        dbar = c85.build_dbar([l1, l2, l3], rmult)
        dim_q = level + 1
        return sp.Matrix(sp.kronecker_product(sp.eye(dim_q), dbar))

    per_level = {}
    all_ok = True

    for k in TESTED_LEVELS:
        print(f"\n=== k={k} ===")
        D = dbar_full(k)
        D_np = np.array(D.evalf().tolist(), dtype=np.float64)
        n = D_np.shape[0]

        eig_D = np.linalg.eigvals(D_np)
        max_im_D = float(np.max(np.abs(np.imag(eig_D))))
        p0_ok = max_im_D == 0.0
        print(f"  P0: max|Im(eig D)| = {max_im_D} (exactly zero: {p0_ok})")

        # j2=0 self-coupling: single (a,b)=(0,0) component, CG(j1,m,0,0,j1,m)=1
        # for every m -- the off-diagonal block is exactly t*I, not built via
        # the general CG machinery since it is trivially the identity.
        full = np.zeros((2 * n, 2 * n))
        full[:n, :n] = D_np
        full[n:, n:] = D_np
        full[:n, n:] = T_SCALE * np.eye(n)
        full[n:, :n] = T_SCALE * np.eye(n)

        eig_full = np.linalg.eigvals(full)
        max_im_full = float(np.max(np.abs(np.imag(eig_full))))
        p1_ok = max_im_full < 1e-9
        print(f"  P1: max|Im(self-coupled)| = {max_im_full} (real: {p1_ok})")

        predicted = np.sort_complex(np.concatenate([eig_D + T_SCALE, eig_D - T_SCALE]))
        actual = np.sort_complex(eig_full)
        p2_ok = bool(np.allclose(predicted, actual, atol=1e-9))
        print(f"  P2: matches eig(D+t) UNION eig(D-t): {p2_ok}")

        level_ok = p0_ok and p1_ok and p2_ok
        all_ok = all_ok and level_ok
        per_level[str(k)] = {
            "dim": n,
            "max_im_D": max_im_D,
            "p0_ok": p0_ok,
            "max_im_self_coupled": max_im_full,
            "p1_ok": p1_ok,
            "p2_ok": p2_ok,
        }

    verdict = (
        "J2_ZERO_ALGEBRAICALLY_INCAPABLE_OF_BREAKING_REALITY__CONFOUND_ROUTE_CLOSED"
        if all_ok
        else "UNEXPECTED_PATTERN__ALGEBRAIC_ARGUMENT_HAS_AN_ERROR__SEE_DETAILS"
    )

    out = {"per_level": per_level, "all_ok": all_ok, "verdict": verdict, "t_scale": T_SCALE}
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")

    assert all_ok, "algebraic argument failed to hold numerically -- see per_level detail"


if __name__ == "__main__":
    main()
