"""C219 -- computed Dirac Casimir zeta_FP(rho3, rho6) on S^3 x S^6 inside the G92 2D landscape.

Independent re-implementation (nothing imported from G54, whose code lives only inside tests):
  zeta(s) = sum W3(n) W6(m) (a_n^2/rho3^2 + m^2/rho6^2)^(-s),  a_n = n+3/2, W3 = 2(n+1)(n+2),
  W6(m) = 16*C(m+2,5) = (2/15)(m^5 - 5 m^3 + 4 m)  (m = k+3 >= 3; vanishes at m=1,2).
  Mellin split at tau=T: asymptotic part (K3 Poisson-exact, K6 exact Euler-Maclaurin/Mellin series)
  integrated analytically, the tail by quadrature of the exact sums.
  zeta_FP(-1/2) = (1/Gamma(-1/2)) * (F_reg - c * psi(-1/2))   [with-psi]   or without the psi term.
claim.md has the pre-registered claims and amendment A1.
"""

from __future__ import annotations

import importlib.util
import json
import math
from itertools import pairwise
from pathlib import Path

import numpy as np
from scipy.special import digamma, gamma
from sympy import bernoulli, factorial

HERE = Path(__file__).resolve().parent
G92_PATH = HERE.parent / "20260626-g92-s3-casimir-stabilization" / "g92_s3_casimir.py"

PASS: list[str] = []
FAIL: list[str] = []
RESULTS: dict = {}


def check(name: str, ok: bool, detail: str = "") -> None:
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"         {detail}")


# ---------------------------------------------------------------- exact S^6 / S^3 asymptotics
SQPI = math.sqrt(math.pi)
A0_S3, A2_S3 = SQPI / 2, -SQPI / 4  # K3(x) = A0 x^-3/2 + A2 x^-1/2 + O(exp(-pi^2/x))
JMAX = 20


def zeta_neg_odd(n: int) -> float:
    """zeta(-n) for odd n >= 1:  -B_{n+1}/(n+1)."""
    return float(-bernoulli(n + 1) / (n + 1))


def k6_coeffs(jmax: int = JMAX) -> dict[int, float]:
    """K6(y) ~ sum_p b_p y^p, exact.  W6 = (2/15)(m^5 - 5 m^3 + 4 m).
    sum_m m^(2k+1) e^{-y m^2} ~ (1/2) k! y^(-k-1) + sum_j (-y)^j / j! * zeta(-2k-1-2j)."""
    pref = 2.0 / 15.0
    wts = {2: 1.0, 1: -5.0, 0: 4.0}  # k -> coefficient of m^(2k+1)
    b: dict[int, float] = {}
    for k, wk in wts.items():
        b[-k - 1] = b.get(-k - 1, 0.0) + pref * wk * 0.5 * float(factorial(k))
        for j in range(jmax + 1):
            term = (
                pref
                * wk
                * ((-1) ** j)
                / float(factorial(j))
                * zeta_neg_odd(2 * k + 1 + 2 * j)
            )
            b[j] = b.get(j, 0.0) + term
    return b


B6 = k6_coeffs()
# G54's own fitted values (tests/test_g54c_effective_potential.py docstring / decision.md), for comparison
B8_G54_FIT, B10_G54_FIT = -0.0076, -0.0033  # 6-param fit; 7-param gave B10=-0.0029


def c_half(
    rho3: float, rho6: float, b8: float | None = None, b10: float | None = None
) -> float:
    """t^{1/2} coefficient of K(t;rho3,rho6) = K3(t/rho3^2) K6(t/rho6^2)."""
    b8 = B6[1] if b8 is None else b8
    b10 = B6[2] if b10 is None else b10
    return A2_S3 * b8 * rho3 / rho6**2 + A0_S3 * b10 * rho3**3 / rho6**4


# ---------------------------------------------------------------- direct (exact) heat kernels
def k3_direct(x: np.ndarray, nmax: int | None = None) -> np.ndarray:
    xmin = float(np.min(x))
    nmax = nmax or int(math.sqrt(45.0 / xmin)) + 3
    n = np.arange(0, nmax)
    return 2.0 * np.sum(
        (n + 1) * (n + 2) * np.exp(-np.outer(x, (n + 1.5) ** 2)), axis=1
    )


def k6_direct(y: np.ndarray, mmax: int | None = None) -> np.ndarray:
    ymin = float(np.min(y))
    mmax = mmax or int(math.sqrt(45.0 / ymin)) + 3
    m = np.arange(1, mmax, dtype=float)
    w = (2.0 / 15.0) * (m**5 - 5 * m**3 + 4 * m)
    return np.exp(-np.outer(y, m**2)) @ w


# ---------------------------------------------------------------- Mellin-split zeta
_GL_X, _GL_W = np.polynomial.legendre.leggauss(40)


def _tail_integral(
    rho3: float, rho6: float, T: float, s: float, panels: int = 14
) -> float:
    """integral_T^inf tau^(s-1) K(tau) dtau, via u=ln tau on composite Gauss-Legendre."""
    lam2_min = (1.5 / rho3) ** 2 + 9.0 / rho6**2
    umax = math.log(max(60.0 / lam2_min, 4 * T))
    edges = np.linspace(math.log(T), umax, panels + 1)
    total = 0.0
    for a, b in pairwise(edges):
        u = 0.5 * (b - a) * _GL_X + 0.5 * (b + a)
        tau = np.exp(u)
        kk = k3_direct(tau / rho3**2) * k6_direct(tau / rho6**2)
        total += 0.5 * (b - a) * float(np.sum(_GL_W * np.exp(s * u) * kk))
    return total


def asym_terms(rho3: float, rho6: float) -> dict[float, float]:
    """c_alpha of K(t) ~ sum c_alpha t^alpha (exact product of the two asymptotic series)."""
    out: dict[float, float] = {}
    for q, aq in ((-1.5, A0_S3), (-0.5, A2_S3)):
        for p, bp in B6.items():
            alpha = p + q
            out[alpha] = out.get(alpha, 0.0) + aq * rho3 ** (-2 * q) * bp * rho6 ** (
                -2 * p
            )
    return out


def zeta_fp(
    rho3: float,
    rho6: float,
    T: float | None = None,
    with_psi: bool = True,
    mu: float = 1.0,
):
    """Constant term of the Laurent expansion of zeta(s) at s=-1/2; also returns (c_half, residue)."""
    T = T if T is not None else 0.12 * min(rho3, rho6) ** 2
    s = -0.5
    terms = asym_terms(rho3, rho6)
    f_reg = 0.0
    c_pole = 0.0
    for alpha, c in terms.items():
        if abs(alpha - 0.5) < 1e-12:
            c_pole = c
            f_reg += c * math.log(T)
        else:
            f_reg += c * T ** (alpha + s) / (alpha + s)
    f_reg += _tail_integral(rho3, rho6, T, s)
    g0 = 1.0 / gamma(-0.5)
    z = g0 * (f_reg - (c_pole * digamma(-0.5) if with_psi else 0.0))
    res = c_pole * g0  # residue of zeta at s=-1/2
    # mu convention E(s)=mu^(2s+1) zeta(s)/2: at s=-1/2 only the log shift survives (A2: the earlier extra 1/mu was wrong, never used)
    z = z + 2.0 * res * math.log(mu)
    return z, c_pole, res


def zeta_mellin_general_s(
    rho3: float, rho6: float, s: float, T: float | None = None
) -> float:
    """zeta(s) for Re s large enough to converge, by the same split (control for the machinery)."""
    T = T if T is not None else 0.12 * min(rho3, rho6) ** 2
    terms = asym_terms(rho3, rho6)
    f = sum(c * T ** (alpha + s) / (alpha + s) for alpha, c in terms.items())
    f += _tail_integral(rho3, rho6, T, s)
    return f / gamma(s)


def zeta_brute(
    rho3: float, rho6: float, s: float, nmax: int = 220, mmax: int = 220
) -> float:
    n = np.arange(0, nmax)
    m = np.arange(1, mmax, dtype=float)
    w3 = 2.0 * (n + 1) * (n + 2)
    w6 = (2.0 / 15.0) * (m**5 - 5 * m**3 + 4 * m)
    lam2 = ((n + 1.5) ** 2 / rho3**2)[:, None] + (m**2 / rho6**2)[None, :]
    return float(np.sum(w3[:, None] * w6[None, :] * lam2 ** (-s)))


def main() -> None:
    global B6
    print("=" * 78)
    print("P0  exact S^6 coefficients (Mellin) vs G54's least-squares fits")
    print("=" * 78)
    check("P0a B0 = 2/15 exactly", abs(B6[-3] - 2 / 15) < 1e-15, f"B0={B6[-3]:.15f}")
    print(f"  exact: B6={B6[0]:.6f}  B8={B6[1]:.7f}  B10={B6[2]:.7f}")
    print(
        f"  G54 6-param fit: B8={B8_G54_FIT}  B10={B10_G54_FIT}  (7-param B10 was -0.0029)"
    )
    rel8 = abs(B6[1] - B8_G54_FIT) / abs(B6[1])
    rel10 = abs(B6[2] - B10_G54_FIT) / abs(B6[2])
    check(
        "P0b exact B8, B10 within 25% of G54's 6-param fits",
        rel8 < 0.25 and rel10 < 0.25,
        f"rel diff B8={rel8:.3f}, B10={rel10:.3f}",
    )
    RESULTS.update(
        {
            "B6_exact": B6[0],
            "B8_exact": B6[1],
            "B10_exact": B6[2],
            "rel_diff_B8_vs_G54": rel8,
            "rel_diff_B10_vs_G54": rel10,
        }
    )

    print()
    print("=" * 78)
    print("P1  instrument checks")
    print("=" * 78)
    r3, r6 = 1.3, 1.1
    worst = 0.0
    for T in (0.03, 0.06, 0.12, 0.2):
        z, _, _ = zeta_fp(r3, r6, T=T * min(r3, r6) ** 2)
        worst = max(worst, abs(z))  # placeholder, replaced below
    zs = [zeta_fp(r3, r6, T=T * min(r3, r6) ** 2)[0] for T in (0.03, 0.06, 0.12, 0.2)]
    spread = (max(zs) - min(zs)) / abs(np.mean(zs))
    check(
        "P1a zeta_FP independent of split point T (rel spread < 1e-8)",
        spread < 1e-8,
        f"zeta_FP={zs[0]:.10e}, spread={spread:.2e}",
    )
    for s in (6.3, 8.1):
        zm = zeta_mellin_general_s(r3, r6, s)
        zb = zeta_brute(r3, r6, s)
        check(
            f"P1b split-Mellin equals brute double sum at s={s}",
            abs(zm - zb) / abs(zb) < 1e-8,
            f"Mellin={zm:.10e}, brute={zb:.10e}",
        )
    # (c) feed G54's fitted B8,B10 into c_half: rho6* along rho3 = 0.986 rho6^2
    C_SM = 0.986

    def root_c(b8, b10):
        lo, hi = 0.5, 3.0
        f = lambda r: c_half(C_SM * r**2, r, b8, b10)
        for _ in range(100):
            mid = 0.5 * (lo + hi)
            if f(lo) * f(mid) <= 0:
                hi = mid
            else:
                lo = mid
        return 0.5 * (lo + hi)

    r_star_fit = root_c(B8_G54_FIT, B10_G54_FIT)
    r_star_exact = root_c(None, None)
    check(
        "P1c G54's fitted B8,B10 in my c_half give rho6* = 1.090 +- 0.01",
        abs(r_star_fit - 1.090) < 0.01,
        f"rho6*(fit)={r_star_fit:.4f}",
    )
    print(f"  rho6*(exact B8,B10) = {r_star_exact:.4f}   [A1 predicted ~1.15]")
    RESULTS.update(
        {"rho6_star_G54_fit_inputs": r_star_fit, "rho6_star_exact": r_star_exact}
    )
    # (d) negative control: W6 with the 4m term dropped must break P1b
    saved = dict(B6)
    wrong = k6_coeffs()
    # drop the k=0 weight contribution: subtract its part
    pref = 2.0 / 15.0
    wrong[-1] -= pref * 4.0 * 0.5
    for j in range(JMAX + 1):
        wrong[j] -= (
            pref * 4.0 * ((-1) ** j) / float(factorial(j)) * zeta_neg_odd(1 + 2 * j)
        )
    B6 = wrong
    zm_bad = zeta_mellin_general_s(r3, r6, 6.3)
    B6 = saved
    zb = zeta_brute(r3, r6, 6.3)
    check(
        "P1d negative control: dropping a W6 term breaks the Mellin-vs-brute match",
        abs(zm_bad - zb) / abs(zb) > 1e-3,
        f"rel diff = {abs(zm_bad - zb) / abs(zb):.3e}",
    )

    print()
    print("=" * 78)
    print(
        "P1'  radii along rho3 = 0.986 rho6^2 (reported difference vs G54-E, not pass/fail)"
    )
    print("=" * 78)
    rs = np.linspace(0.6, 2.0, 141)
    for with_psi in (True, False):
        zz = np.array([zeta_fp(C_SM * r**2, r, with_psi=with_psi)[0] for r in rs])
        i_min = int(np.argmin(zz))
        sign = np.where(np.diff(np.sign(zz)) != 0)[0]
        zeros = [
            float(rs[i] - zz[i] * (rs[i + 1] - rs[i]) / (zz[i + 1] - zz[i]))
            for i in sign
        ]
        print(
            f"  with_psi={with_psi}: min at rho6={rs[i_min]:.3f} (zeta_FP={zz[i_min]:.3e}); zeros at {np.round(zeros, 4).tolist()}"
        )
        RESULTS[f"path_min_rho6_psi_{with_psi}"] = float(rs[i_min])
        RESULTS[f"path_zeros_psi_{with_psi}"] = zeros
        RESULTS[f"path_zeta_at_min_psi_{with_psi}"] = float(zz[i_min])
    print("  G54-E: rho6_min=0.953 (zeta_FP=-8.63e-4), rho6*=1.090, rho6**=1.4469")

    print()
    print("=" * 78)
    print("P2/P3  2D landscape with the COMPUTED Casimir (G92's V_main)")
    print("=" * 78)
    spec = importlib.util.spec_from_file_location("g92", G92_PATH)
    g92 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g92)
    vol = g92.VOL_S3_UNIT * g92.VOL_S6_UNIT

    grid3 = np.geomspace(0.35, 6.0, 56)
    grid6 = np.geomspace(0.35, 6.0, 56)
    Z = {}
    for with_psi in (True, False):
        Z[with_psi] = np.array(
            [[zeta_fp(a, b, with_psi=with_psi)[0] for b in grid6] for a in grid3]
        )
    RESULTS["zeta_grid_range"] = [float(Z[True].min()), float(Z[True].max())]
    VM = np.array([[g92.v_main(a, b) for b in grid6] for a in grid3])
    VOLR = np.array([[vol * a**3 * b**6 for b in grid6] for a in grid3])

    def local_minima(V: np.ndarray):
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
                    out.append((float(grid3[i]), float(grid6[j]), float(c)))
        return out

    def valid(r3, r6):
        return r3 > 1.0 and r6 > 1.5

    kappas = [0.25, 0.5, 1.0, -0.25, -0.5, -1.0]
    any_valid = False
    for with_psi in (True, False):
        for k in kappas:
            V = VM + k * Z[with_psi] / VOLR
            mins = local_minima(V)
            inval = [m for m in mins if valid(m[0], m[1])]
            any_valid |= bool(inval)
            print(
                f"  psi={with_psi!s:5} kappa={k:+.2f}: grid-local minima={len(mins)}, in valid region={len(inval)}"
                + (
                    f"  e.g. {inval[0]}"
                    if inval
                    else (f"  (at {mins[0][:2]})" if mins else "")
                )
            )
            RESULTS[f"kappa_{k:+.2f}_psi_{with_psi}_n_min"] = len(mins)
            RESULTS[f"kappa_{k:+.2f}_psi_{with_psi}_n_valid_min"] = len(inval)
    check(
        "P2 no local minimum in the valid region (rho3>1, rho6>1.5) for |kappa|<=1, both FP definitions",
        not any_valid,
    )

    # P3: minimal |kappa| at which ANY grid-local minimum appears; and the biggest one in the valid region
    for with_psi in (True, False):
        found = {}
        for sign in (+1, -1):
            for k in np.geomspace(0.05, 200.0, 60):
                V = VM + sign * k * Z[with_psi] / VOLR
                mins = local_minima(V)
                if mins and "any" not in found.setdefault(sign, {}):
                    found[sign]["any"] = (float(k), mins[0])
                if any(
                    valid(m[0], m[1]) for m in mins
                ) and "valid" not in found.setdefault(sign, {}):
                    found[sign]["valid"] = (
                        float(k),
                        next(m for m in mins if valid(m[0], m[1])),
                    )
        print(
            f"  P3 psi={with_psi}: minimal |kappa| for any local min / for one in the valid region: {found}"
        )
        RESULTS[f"P3_psi_{with_psi}"] = {str(k): v for k, v in found.items()}

    print()
    print("=" * 78)
    print(f"C219: {len(PASS)} passed, {len(FAIL)} failed")
    for f in FAIL:
        print(f"  FAILED: {f}")
    print("=" * 78)
    (HERE / "results_c219.json").write_text(json.dumps(RESULTS, indent=2, default=str))


if __name__ == "__main__":
    main()
