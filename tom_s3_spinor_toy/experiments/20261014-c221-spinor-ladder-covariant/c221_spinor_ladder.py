"""C221: ladder operators and the spin-1/2 multiplet of SO(3) on S^2 (unit sphere).

Part A: the literal orbital route (McMurry p.144 operators, spin weight s = 0).
Part B: spin-weighted operators L+- = e^{+-i phi}(+-d_theta + i cot(theta) d_phi - s/sin(theta)).
Exact sympy; analytic norms. Run: python c221_spinor_ladder.py  (writes results_c221.json).
"""

import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
TH = sp.symbols("theta", positive=True)
PH = sp.symbols("phi", real=True)
IU = sp.I
PI = sp.pi
HALF = sp.Rational(1, 2)
CHECKS: list[dict] = []
VALUES: dict[str, str] = {}
SAMPLE_THETAS = [sp.Rational(3, 10), sp.Rational(9, 10), sp.Rational(17, 10), sp.Rational(26, 10)]


def check(cid: str, text: str, ok: bool, kind: str = "main") -> None:
    CHECKS.append({"id": cid, "text": text, "ok": bool(ok), "kind": kind})
    tag = {"main": "PASS", "control": "CTRL", "restatement": "REST"}[kind]
    print(f"{tag if ok else 'FAIL'}  [{cid}] {text}")


def zero(expr) -> bool:
    """Exact zero test; falls back to a 1e-12 numeric test at four angles only if simplify is inconclusive."""
    e = sp.simplify(expr)
    if e == 0:
        return True
    extra = {
        sym: sp.Rational(7, 10) + sp.Rational(k, 10)
        for k, sym in enumerate(sorted(e.free_symbols - {TH, PH}, key=str))
    }
    pts = [
        abs(complex(e.subs({TH: t, PH: sp.Rational(7, 10), **extra}).evalf(30)))
        for t in SAMPLE_THETAS
    ]
    return max(pts) < 1e-12


def const_ratio(num, den):
    """(is_constant, value or ratio expression) for num/den as a function of theta (phi stripped)."""
    r = sp.simplify(num / den)
    if sp.simplify(sp.diff(r, TH)) == 0:
        return True, r
    vals = [complex(r.subs(TH, t).evalf(30)) for t in SAMPLE_THETAS]
    spread = max(abs(v - vals[0]) for v in vals)
    return spread < 1e-12, r


def lz(f):
    return -IU * sp.diff(f, PH)


def lp(f, s=0):
    return sp.exp(IU * PH) * (
        sp.diff(f, TH) + IU * sp.cot(TH) * sp.diff(f, PH) - s / sp.sin(TH) * f
    )


def lm(f, s=0):
    return sp.exp(-IU * PH) * (
        -sp.diff(f, TH) + IU * sp.cot(TH) * sp.diff(f, PH) - s / sp.sin(TH) * f
    )


def mode(chi, m):
    return chi * sp.exp(IU * m * PH)


def strip(expr, m_out):
    """Remove e^{i m_out phi}; returns the theta-function (asserts nothing of phi is left)."""
    out = sp.simplify(expr * sp.exp(-IU * m_out * PH))
    assert PH not in out.free_symbols, out
    return out


def act_p(chi, m, s=0):
    return strip(lp(mode(chi, m), s), m + 1)


def act_m(chi, m, s=0):
    return strip(lm(mode(chi, m), s), m - 1)


def norm2(chi):
    """Unit-sphere norm^2 of chi(theta) e^{i m phi} for real chi: 2 pi * int chi^2 sin(theta) dtheta."""
    e = sp.expand(sp.simplify(chi**2 * sp.sin(TH)))
    e = e.subs(
        {sp.sin(TH / 2) ** 2: (1 - sp.cos(TH)) / 2, sp.cos(TH / 2) ** 2: (1 + sp.cos(TH)) / 2}
    )
    return sp.simplify(2 * PI * sp.integrate(sp.expand(e), (TH, 0, PI)))


def chi_action_p(chi, m, s):
    return sp.diff(chi, TH) - m * sp.cot(TH) * chi - s * chi / sp.sin(TH)


def chi_action_m(chi, m, s):
    return -sp.diff(chi, TH) - m * sp.cot(TH) * chi - s * chi / sp.sin(TH)


def numeric_ratio(num, den):
    """(constant at 30 digits?, list of ratios) for num/den at the sample angles; no symbolic simplify."""
    vals = [complex(sp.N((num / den).subs(TH, th), 30)) for th in SAMPLE_THETAS]
    return max(abs(v - vals[0]) for v in vals) < 1e-20, vals


def casimir(chi, m, s=0):
    f = mode(chi, m)
    return strip(lm(lp(f, s), s) + lz(lz(f)) + lz(f), m)


print("=== PART A: literal orbital route (s = 0) ===")
f = sp.Function("f")
CHI = sp.sqrt(sp.sin(TH))
UP, DN = CHI, CHI  # chi for m = +1/2 and m = -1/2

# A1: L_z eigenfunctions
gen = f(TH)
check(
    "A1",
    "L_z (chi(theta) e^{i m phi}) = m (chi e^{i m phi}) for m = +-1/2",
    all(zero(lz(mode(gen, m)) - m * mode(gen, m)) for m in (HALF, -HALF)),
)

# A2/A3: highest- and lowest-weight equations, solved
ode_up = act_p(f(TH), HALF, 0)
ode_dn = act_m(f(TH), -HALF, 0)
sol_up = sp.dsolve(ode_up, f(TH)).rhs
sol_dn = sp.dsolve(ode_dn, f(TH)).rhs
check(
    "A2",
    "L+ [chi e^{i phi/2}] = 0 is chi' - (1/2) cot(theta) chi = 0; dsolve gives chi = C sin^{1/2}(theta)",
    zero(ode_up - (sp.diff(f(TH), TH) - HALF * sp.cot(TH) * f(TH)))
    and const_ratio(sol_up.subs(sp.Symbol("C1"), 1), CHI)[0],
)
check(
    "A3",
    "L- [chi e^{-i phi/2}] = 0 gives chi = C' sin^{1/2}(theta)",
    const_ratio(sol_dn.subs(sp.Symbol("C1"), 1), CHI)[0],
)
check(
    "A2b",
    "the solution of a first-order linear homogeneous ODE is unique up to a constant (so no other chi)",
    True,
    "restatement",
)
check(
    "A2c",
    "psi_up = sqrt(sin) e^{i phi/2} is annihilated by L+ ; psi_dn = sqrt(sin) e^{-i phi/2} by L-",
    zero(act_p(UP, HALF)) and zero(act_m(DN, -HALF)),
)
chi_vec = sp.sin(TH)
check(
    "D5",
    "literal step 3 (m = -1, s = 0): L- [chi e^{-i phi}] = 0 gives chi = C sin(theta): the VECTOR m=-1 function, not a spinor",
    zero(act_m(chi_vec, -1)),
)

# A4: step 4 with the orbital operators
down_from_up = act_m(UP, HALF)
up_from_down = act_p(DN, -HALF)
ok1, r1 = const_ratio(down_from_up, DN)
ok2, r2 = const_ratio(up_from_down, UP)
VALUES["A4_L-psi_up_over_psi_dn"] = str(r1)
VALUES["A4_L+psi_dn_over_psi_up"] = str(r2)
check(
    "A4a",
    f"L- psi_up = ({r1}) psi_dn ; L+ psi_dn = ({r2}) psi_up (ratios, exact)",
    sp.simplify(r1 + sp.cot(TH)) == 0 and sp.simplify(r2 - sp.cot(TH)) == 0,
)
check(
    "A4b",
    "step 4 FAILS with a constant coefficient: the ratios depend on theta",
    (not ok1) and (not ok2),
)
two = act_m(down_from_up, HALF - 1)
c_two, r_two = const_ratio(two, sp.sin(TH) ** sp.Rational(-3, 2))
VALUES["A5_L-^2_psi_up"] = str(sp.simplify(two))
eps = sp.symbols("epsilon", positive=True)
div = sp.integrate(1 / sp.sin(TH) ** 2, (TH, eps, PI - eps))
check(
    "A5a",
    "L-^2 psi_up = -sin^{-3/2}(theta) e^{-3 i phi/2}: the lowering chain does not terminate",
    c_two and sp.simplify(r_two + 1) == 0,
)
check(
    "A5b",
    "int |L-^2 psi_up|^2 dOmega = 2 pi int sin^{-2} dtheta diverges (2 pi * 2 cot(eps) -> infinity)",
    sp.limit(sp.simplify(div), eps, 0, "+") == sp.oo,
)
check(
    "A6",
    "Casimir L^2 = L-L+ + Lz^2 + Lz = 3/4 on psi_up and psi_dn",
    sp.simplify(casimir(UP, HALF) - sp.Rational(3, 4) * UP) == 0
    and sp.simplify(casimir(DN, -HALF) - sp.Rational(3, 4) * DN) == 0,
)
n_up = norm2(UP)
n_lm = norm2(down_from_up)
VALUES["A7_norm2_psi_up"] = str(n_up)
check(
    "A7a",
    "<psi_up, psi_up> = pi^2 (so N = 1/pi) and the same for psi_dn",
    sp.simplify(n_up - PI**2) == 0 and sp.simplify(norm2(DN) - PI**2) == 0,
)
check(
    "A7b",
    "<L- psi_up, L- psi_up> = pi^2 (the algebra identity j(j+1) - m(m-1) = 1 times the norm)",
    sp.simplify(n_lm - PI**2) == 0,
)
phi_int = sp.integrate(sp.conjugate(sp.exp(IU * PH / 2)) * sp.exp(-IU * PH / 2), (PH, 0, 2 * PI))
check(
    "A7c",
    "psi_up and psi_dn are orthogonal (the phi integral of e^{-i phi} over [0, 2 pi] is 0)",
    sp.simplify(phi_int) == 0,
)
check(
    "A8",
    "psi(phi + 2 pi) = -psi(phi) for psi_up and psi_dn (double-valued, consistent with C179)",
    zero(mode(UP, HALF).subs(PH, PH + 2 * PI) + mode(UP, HALF))
    and zero(mode(DN, -HALF).subs(PH, PH + 2 * PI) + mode(DN, -HALF)),
)

print("=== PART B: spin-weighted operators ===")
S = sp.symbols("s", real=True)
F = sp.Function("F")(TH, PH)
comm = sp.simplify(sp.expand(lp(lm(F, S), S) - lm(lp(F, S), S) - 2 * lz(F)))
check("B1a", "[L+,L-] F - 2 Lz F = 0 for generic F and generic s", comm == 0)
check(
    "B1b",
    "[Lz,L+] F - L+ F = 0 and [Lz,L-] F + L- F = 0 for generic F and generic s",
    sp.simplify(sp.expand(lz(lp(F, S)) - lp(lz(F), S) - lp(F, S))) == 0
    and sp.simplify(sp.expand(lz(lm(F, S)) - lm(lz(F), S) + lm(F, S))) == 0,
)

# general highest / lowest weight solutions (derived by integrating f'/f)
m_sym = sp.symbols("m", real=True)
logder_up = m_sym * sp.cot(TH) + S / sp.sin(TH)
chi_hw = sp.sin(TH) ** m_sym * sp.tan(TH / 2) ** S
chi_lw = sp.sin(TH) ** (-m_sym) * sp.tan(TH / 2) ** (-S)
check(
    "B2a",
    "f'/f = m cot(theta) + s/sin(theta) integrates to f = sin^m(theta) tan^s(theta/2) (d/dtheta ln tan(theta/2) = 1/sin(theta))",
    zero(sp.diff(sp.log(sp.tan(TH / 2)), TH) - 1 / sp.sin(TH))
    and zero(sp.diff(m_sym * sp.log(sp.sin(TH)) + S * sp.log(sp.tan(TH / 2)), TH) - logder_up),
)
check(
    "B2b",
    "L+ [sin^m tan^s(theta/2) e^{i m phi}] = 0 and L- [sin^{-m} tan^{-s}(theta/2) e^{i m phi}] = 0 for symbolic m, s",
    zero(act_p(chi_hw, m_sym, S)) and zero(act_m(chi_lw, m_sym, S)),
)
sA = sp.Symbol("C1")
chk_dsolve = []
for sv in (HALF,):
    o_up = act_p(f(TH), HALF, sv)
    solv = sp.dsolve(o_up, f(TH)).rhs.subs(sA, 1)
    cand = chi_hw.subs({m_sym: HALF, S: sv})
    vals = [complex((solv / cand).subs(TH, t).evalf(30)) for t in SAMPLE_THETAS]
    chk_dsolve.append(max(abs(v - vals[0]) for v in vals) < 1e-12)
check(
    "B2c",
    "independent dsolve of the s = 1/2 highest-weight ODE agrees with the integrated form (ratio constant at 4 angles)",
    all(chk_dsolve),
)

s_half = HALF
UPB = sp.sin(TH / 2) / sp.sqrt(2 * PI)
DNB = -sp.cos(TH / 2) / sp.sqrt(2 * PI)  # Condon-Shortley sign chosen so that L- psi_up = + psi_dn
check(
    "B3a",
    "s=1/2: sin(theta/2) e^{i phi/2} is highest weight (L+ = 0); cos(theta/2) e^{-i phi/2} is lowest weight (L- = 0)",
    zero(act_p(UPB, HALF, s_half)) and zero(act_m(DNB, -HALF, s_half)),
)
check(
    "B3b",
    "s=1/2 closure: L- psi_up = + psi_dn and L+ psi_dn = + psi_up (modulus-1 constants, Condon-Shortley sign on psi_dn)",
    zero(act_m(UPB, HALF, s_half) - DNB) and zero(act_p(DNB, -HALF, s_half) - UPB),
)
check(
    "B3c",
    "s=1/2: Casimir L^2 = 3/4 on both",
    sp.simplify(casimir(UPB, HALF, s_half) - sp.Rational(3, 4) * UPB) == 0
    and sp.simplify(casimir(DNB, -HALF, s_half) - sp.Rational(3, 4) * DNB) == 0,
)
n1, n2 = norm2(UPB), norm2(DNB)
VALUES["B3_norms"] = f"{n1}, {n2}"
check(
    "B3d",
    "s=1/2: both unit-normalised with N = 1/sqrt(2 pi); with B3b, |L- psi_up| = |psi_dn| = 1 = |psi_up| (the norm forced by step 4 agrees with the sphere integral)",
    sp.simplify(n1 - 1) == 0 and sp.simplify(n2 - 1) == 0,
)
check(
    "B3e",
    "s=1/2 pair is anti-periodic: psi(phi + 2 pi) = -psi(phi)",
    zero(mode(UPB, HALF).subs(PH, PH + 2 * PI) + mode(UPB, HALF))
    and zero(mode(DNB, -HALF).subs(PH, PH + 2 * PI) + mode(DNB, -HALF)),
)
c184_minus = sp.sin(TH / 2)  # C184b chi_{-1/2} = e^{i phi/2} sin(theta/2): L_z = +1/2
c184_plus = sp.cos(TH / 2)  # C184b chi_{+1/2} = e^{-i phi/2} cos(theta/2): L_z = -1/2
check(
    "B4",
    "s=1/2 pair = C184b doublet up to normalisation and sign, labels reversed: C184b chi_{+1/2} has Lz = -1/2",
    zero(lz(mode(c184_plus, -HALF)) + HALF * mode(c184_plus, -HALF))
    and sp.simplify(UPB * sp.sqrt(2 * PI) - c184_minus) == 0
    and sp.simplify(DNB * sp.sqrt(2 * PI) + c184_plus) == 0,
)

# closure scan over s
print("--- closure scan ---")
gen_f = sp.Function("f")(TH)
check(
    "B5c",
    "the closed-form action on chi(theta) equals the full operator action for generic chi, m, s (so the scan below is exact in form)",
    zero(act_p(gen_f, m_sym, S) - chi_action_p(gen_f, m_sym, S))
    and zero(act_m(gen_f, m_sym, S) - chi_action_m(gen_f, m_sym, S)),
)
scan = {}
for sv in (0, HALF, -HALF, 1, -1, sp.Rational(3, 2), -sp.Rational(3, 2)):
    up_s = chi_hw.subs({m_sym: HALF, S: sv})
    dn_s = chi_lw.subs({m_sym: -HALF, S: sv})
    ok_a, va = numeric_ratio(chi_action_m(up_s, HALF, sv), dn_s)
    ok_b, vb = numeric_ratio(chi_action_p(dn_s, -HALF, sv), up_s)
    closes = bool(ok_a and ok_b)
    fmt = lambda vals, ok: (
        f"{complex(vals[0]).real:.12g}"
        if ok
        else "theta-dependent: " + ", ".join(f"{complex(v).real:.4g}" for v in vals)
    )
    scan[str(sv)] = {"closes": closes, "L-up/dn": fmt(va, ok_a), "L+dn/up": fmt(vb, ok_b)}
    print(
        f"   s = {sv}: closes = {closes}; L- up / dn = {scan[str(sv)]['L-up/dn']}; L+ dn / up = {scan[str(sv)]['L+dn/up']}"
    )
VALUES["B5_scan"] = json.dumps(scan)
check(
    "B6",
    "s=-1/2 mirror pair closes exactly: cos(theta/2) e^{i phi/2} -> L- -> sin(theta/2) e^{-i phi/2} with constant +1 (and back)",
    zero(act_m(sp.cos(TH / 2), HALF, -HALF) - sp.sin(TH / 2))
    and zero(act_p(sp.sin(TH / 2), -HALF, -HALF) - sp.cos(TH / 2)),
)
check(
    "B5a",
    "closure holds for s = +1/2 and s = -1/2 (mirror images under theta -> pi - theta)",
    scan["1/2"]["closes"] and scan["-1/2"]["closes"],
)
check(
    "B5b",
    "closure FAILS for s = 0 (the closure test can say no)",
    not scan["0"]["closes"],
    "control",
)
VALUES["B5_other_s_exploratory"] = ", ".join(
    f"s={k}: {v['closes']}" for k, v in scan.items() if k not in ("0", "1/2", "-1/2")
)

print("=== CONTROLS ===")
c_ = sp.sqrt(3 / (8 * PI))
y11 = -c_ * sp.sin(TH)  # chi of Y(1,1) (times e^{i phi})
y10 = sp.sqrt(3 / (4 * PI)) * sp.cos(TH)
check(
    "D1",
    "integer positive control, s = 0: L+ [sin e^{i phi}] = 0 and L- Y(1,1) = sqrt(2) Y(1,0) (the C220 result)",
    zero(act_p(sp.sin(TH), 1)) and zero(act_m(y11, 1) - sp.sqrt(2) * y10),
    "control",
)
ok_d2, r_d2 = const_ratio(act_m(y11, 1, HALF), y10)
check(
    "D2",
    "s = 1/2 operators on the integer harmonics Y(1,m) do NOT close (L- Y(1,1)/Y(1,0) depends on theta)",
    not ok_d2,
    "control",
)
const_a, const_b = sp.symbols("a b", real=True)
comm_bad = sp.simplify(
    sp.expand(lp(lm(F, const_b), const_a) - lm(lp(F, const_a), const_b) - 2 * lz(F))
)
comm_half = sp.simplify(sp.expand(lp(lm(F, -HALF), HALF) - lm(lp(F, HALF), -HALF) - 2 * lz(F)))
check(
    "D3a",
    "the commutator test alone is BLIND to unequal constants: [L+_a, L-_b] F = 2 Lz F holds for symbolic a, b (so also for a = 1/2, b = -1/2); the pre-registered D3 predicted a failure and was wrong",
    comm_bad == 0 and comm_half == 0,
)
up_half = chi_hw.subs({m_sym: HALF, S: HALF})
ok_d3b, vals_d3b = numeric_ratio(
    chi_action_m(up_half, HALF, -HALF), chi_lw.subs({m_sym: -HALF, S: -HALF})
)
check(
    "D3b",
    "unequal constants (L+ with s = 1/2, L- with s = -1/2): the closure ratio L- psi_up / psi_dn is theta-dependent (does not close)",
    not ok_d3b,
    "control",
)


def adjoint_gap(a, b):
    """|<G, L+_a F> - <L-_b G, F>| for real chi_F e^{i m phi}, chi_G e^{i (m+1) phi} vanishing at the poles."""
    chi_f = sp.sin(TH) ** 2
    chi_g = sp.sin(TH) ** 3 * (1 + sp.cos(TH))
    m_f = HALF
    lhs = chi_g * chi_action_p(chi_f, m_f, a) * sp.sin(TH)
    rhs = chi_action_m(chi_g, m_f + 1, b) * chi_f * sp.sin(TH)
    val = sp.Integral(lhs - rhs, (TH, 0, PI)).evalf(25)
    return abs(2 * PI * val)


gaps = {(a, b): adjoint_gap(a, b) for a, b in ((0, 0), (HALF, HALF), (HALF, -HALF), (0, HALF))}
VALUES["D3c_adjoint_gaps"] = {str(k): float(v) for k, v in gaps.items()}
check(
    "D3c",
    "adjointness <G, L+_a F> = <L-_b G, F> holds for a = b (gap < 1e-15) and fails for a != b (gap > 0.1)",
    gaps[(0, 0)] < 1e-15
    and gaps[(HALF, HALF)] < 1e-15
    and gaps[(HALF, -HALF)] > 0.1
    and gaps[(0, HALF)] > 0.1,
    "control",
)

failed = [c for c in CHECKS if not c["ok"]]
main = [c for c in CHECKS if c["kind"] == "main"]
ctrl = [c for c in CHECKS if c["kind"] == "control"]
print(
    f"\nmain checks: {sum(c['ok'] for c in main)}/{len(main)} | controls: {sum(c['ok'] for c in ctrl)}/{len(ctrl)} "
    f"| restatements (not counted): {sum(1 for c in CHECKS if c['kind'] == 'restatement')}"
)
(HERE / "results_c221.json").write_text(
    json.dumps({"checks": CHECKS, "values": VALUES}, indent=1, ensure_ascii=False), encoding="utf-8"
)
sys.exit(1 if failed else 0)
