"""C249 add-on: is the (0, 1/2) doublet a Dirac eigenspinor, and a Killing spinor? Exact (Weierstrass)."""

import json
import sys

import sympy as sp

# WHY: python -I (used by tom_line_check --run) drops the script folder from sys.path
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from kosmann_geometry import E, I, T, a, cliff, dirac, nabla_spin, t

h, tw = sp.symbols("h tw", positive=True)


def zero(e):
    e = sp.expand_trig(
        sp.expand(e / sp.exp(I * (t - T) / 2) * sp.exp(I * (t - T) / 2)).subs(a, 2 * h)
    )
    e = e.subs({sp.tan(h): sp.sin(h) / sp.cos(h)})
    e = e.subs({sp.sin(h): 2 * tw / (1 + tw**2), sp.cos(h): (1 - tw**2) / (1 + tw**2)})
    return sp.cancel(sp.together(sp.expand(e))) == 0


ph = sp.exp(I * (t - T) / 2)
plus = ph * sp.Matrix([sp.cos(a / 2), -I * sp.sin(a / 2)])
minus = sp.conjugate(ph) * sp.Matrix([-I * sp.sin(a / 2), sp.cos(a / 2)])
out, ok = {}, True
for name, psi in (("plus", plus), ("minus", minus)):
    Dpsi = dirac(psi, +1)
    ratio = sp.N((Dpsi[0] / psi[0]).subs({a: 0.7, t: 0.3, T: 1.2}))
    # WHY: with Hermitian sigma the operator sum sigma_a nabla_a is anti-self-adjoint, so lambda is imaginary
    lam = sp.nsimplify(sp.re(ratio), rational=True, tolerance=1e-10) + I * sp.nsimplify(
        sp.im(ratio), rational=True, tolerance=1e-10
    )
    eig = all(
        zero((Dpsi - lam * psi)[k] / (ph if name == "plus" else sp.conjugate(ph)))
        for k in range(2)
    )
    # Killing spinor equation nabla_X psi = mu X.psi; then D psi = sum sigma_a mu sigma_a psi = 3 mu psi
    mu = lam / 3
    kil = all(
        zero(
            (nabla_spin(E[j], psi, +1) - mu * cliff(E[j], psi))[k]
            / (ph if name == "plus" else sp.conjugate(ph))
        )
        for j in range(3)
        for k in range(2)
    )
    out[name] = {
        "eigenvalue": str(lam),
        "dirac_eigen_exact": eig,
        "killing_mu": str(mu),
        "killing_exact": kil,
    }
    ok &= eig and kil
    print(
        f"{name}: D psi = {lam} psi exact={eig}; Killing nabla_X psi = {mu} X.psi exact={kil}"
    )
# control: a wrong eigenvalue must fail
bad = all(zero((dirac(plus, +1) - (lam + 1) * plus)[k] / ph) for k in range(2))
out["control_wrong_eigenvalue_passes"] = bad
print(("PASS " if not bad else "FAIL ") + "control: lambda+1 is not an eigenvalue")
ok &= not bad
with open("results_dirac_eigen.json", "w") as fh:
    json.dump(out, fh, indent=1)
print("ALL_PASS" if ok else "SOME_FAIL")
sys.exit(0 if ok else 1)
