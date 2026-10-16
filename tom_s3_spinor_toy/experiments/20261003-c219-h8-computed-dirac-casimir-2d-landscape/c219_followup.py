"""C219 follow-up (Amendment A2): mu axis, validity-cut sensitivity, exact rho6* in V_main, interior path extrema."""

from __future__ import annotations

import importlib.util
import json
from math import exp
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


c219 = load("c219", HERE / "c219_computed_casimir_landscape.py")
g92 = load(
    "g92", HERE.parent / "20260626-g92-s3-casimir-stabilization" / "g92_s3_casimir.py"
)
vol = g92.VOL_S3_UNIT * g92.VOL_S6_UNIT
OUT: dict = {}

grid = np.geomspace(0.35, 8.0, 64)  # wider box than the first run (upper edge 8)


def v_main_with(rho_star: float):
    a_np = g92.V_FLUX * exp(g92.LAM / rho_star**2)

    def vm(r3: float, r6: float) -> float:
        return (g92.V_FLUX - a_np * exp(-g92.LAM / r6**2)) / (vol * r3**3 * r6**6)

    return vm


# sanity: my re-parametrised v_main equals G92's at rho6*=1.090
vm_090 = v_main_with(1.090)
assert abs(vm_090(1.4, 1.2) / g92.v_main(1.4, 1.2) - 1) < 1e-12

print("A. interior extrema of zeta_FP along rho3=0.986 rho6^2")
rs = np.linspace(0.35, 2.2, 371)
zz = np.array([c219.zeta_fp(0.986 * r**2, r)[0] for r in rs])
d = np.diff(zz)
ext = [
    (float(rs[i + 1]), float(zz[i + 1]), "min" if d[i] < 0 < d[i + 1] else "max")
    for i in range(len(d) - 1)
    if d[i] * d[i + 1] < 0
]
print(
    "  interior extrema (rho6, zeta_FP, kind):", ext, "  G54-E: min at 0.953, -8.63e-4"
)
OUT["path_interior_extrema"] = ext

zeta_cache: dict = {}


def zgrid(with_psi: bool, mu: float) -> np.ndarray:
    key = (with_psi, mu)
    if key not in zeta_cache:
        zeta_cache[key] = np.array(
            [
                [c219.zeta_fp(a, b, with_psi=with_psi, mu=mu)[0] for b in grid]
                for a in grid
            ]
        )
    return zeta_cache[key]


VOLR = np.array([[vol * a**3 * b**6 for b in grid] for a in grid])


def minima(V: np.ndarray):
    out = []
    for i in range(1, V.shape[0] - 1):
        for j in range(1, V.shape[1] - 1):
            c = V[i, j]
            if all(
                c < V[i + di, j + dj]
                for di in (-1, 0, 1)
                for dj in (-1, 0, 1)
                if (di, dj) != (0, 0)
            ):
                out.append((float(grid[i]), float(grid[j]), float(c)))
    return out


def build(vm, kappa, with_psi, mu):
    VM = np.array([[vm(a, b) for b in grid] for a in grid])
    return VM + kappa * zgrid(with_psi, mu) / VOLR


print(
    "B. mu axis x sign x FP-definition, valid region rho3>1 & rho6>1.5 (G92 V_main, rho6*=1.090)"
)
any_valid = False
for with_psi in (True, False):
    for mu in (0.5, 1.0, 2.0):
        for k in (0.25, 0.5, 1.0, -0.25, -0.5, -1.0):
            mins = minima(build(vm_090, k, with_psi, mu))
            val = [m for m in mins if m[0] > 1.0 and m[1] > 1.5]
            any_valid |= bool(val)
            print(
                f"  psi={with_psi!s:5} mu={mu:3.1f} kappa={k:+.2f}: minima={[(round(m[0], 2), round(m[1], 2)) for m in mins]} valid={len(val)}"
            )
OUT["B_any_valid_min_for_abs_kappa_le_1_mu_axis"] = any_valid

print("C. cut sensitivity (kappa=-1, mu=1, psi): minima positions vs cuts")
mins = minima(build(vm_090, -1.0, True, 1.0))
print("  minima:", mins)

print(
    "D. V_main with the EXACT rho6*=1.1541: where is the kappa<0 minimum, and the valid-region threshold (bisection)"
)
vm_ex = v_main_with(1.1541)
for k in (-0.25, -1.0):
    print(f"  kappa={k}: minima={minima(build(vm_ex, k, True, 1.0))}")


def valid_min(vm, kappa):
    return any(m[0] > 1.0 and m[1] > 1.5 for m in minima(build(vm, kappa, True, 1.0)))


print(
    "E. mu changes the Casimir value at the kappa<0 minimum point (sanity: mu axis is live)"
)
for mu in (0.5, 1.0, 2.0):
    print(
        f"  mu={mu}: zeta_FP(0.64,1.27)={c219.zeta_fp(0.64, 1.27, mu=mu)[0]:+.4e}   zeta_FP(2.2185,1.5)={c219.zeta_fp(2.2185, 1.5, mu=mu)[0]:+.4e}"
    )

print(
    "F. kappa scan (existence is NOT monotone in kappa, so scan, not bisect): kappas with a valid-region minimum"
)
kap = np.geomspace(0.5, 400.0, 70)
for name, vm in (("rho6*=1.090", vm_090), ("rho6*=1.1541", vm_ex)):
    row = {}
    for sign in (-1, +1):
        hits = [round(float(k), 1) for k in kap if valid_min(vm, sign * k)]
        row[str(sign)] = (hits[0], hits[-1], len(hits)) if hits else "none in [0.5,400]"
    print(
        f"  {name}: (first, last, count) of |kappa| with a valid-region minimum: {row}"
    )
    OUT[f"valid_window_{name}"] = row

(HERE / "results_c219_followup.json").write_text(json.dumps(OUT, indent=2, default=str))
