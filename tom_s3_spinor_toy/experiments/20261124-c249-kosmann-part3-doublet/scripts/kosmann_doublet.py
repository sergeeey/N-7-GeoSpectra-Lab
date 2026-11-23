"""C249 P3-P5: the (0, 1/2) doublet as a spinor field in the Hopf frame, versus the scalar ansatz.

Generators J_a = -i L_{N_a} (from [N1, N2] = -N3, so [J1, J2] = i J3). N^+ is SU(2)_R
(N3^+ = (d_theta - d_thetat)/2), N^- is SU(2)_L. Kosmann sign fixed by kosmann_checks.py.
WHY this layout: the first version simplified whole expressions and timed out after 15 min; here the
frame-rotation matrix C_N is simplified once per field, and angle dependence is removed by evaluating
the conditions at exact angle pairs instead of a Fourier expansion.
"""

import json
import random
import sys

import sympy as sp

# WHY: python -I (used by tom_line_check --run) drops the script folder from sys.path
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from kosmann_geometry import NM, NP, I, Q, T, a, kos_matrix, omega, t

S_CONN, S_KOS = +1, +1
A, B, Ap, Bp = sp.symbols("A B Ap Bp")
C = {id(N): sp.simplify(S_CONN * omega(N) + S_KOS * kos_matrix(N)) for N in NP + NM}
out, ok = {}, True


def J(N, psi, spinor=True):
    d = sp.Matrix(
        [sum(N[j] * sp.diff(psi[r], Q[j]) for j in range(3)) for r in range(2)]
    )
    return -I * (d + C[id(N)] * psi) if spinor else -I * d


def ladder(Ns, sign, psi, spinor=True):
    return J(Ns[0], psi, spinor) + sign * I * J(Ns[1], psi, spinor)


phase = sp.exp(I * (t - T) / 2)
fA, fB = sp.Function("fA")(a), sp.Function("fB")(a)
sub = {sp.Derivative(fA, a): Ap, sp.Derivative(fB, a): Bp}
# WHY: after dividing by the phase every condition is c0 + c1 cos(d) + s1 sin(d) + c2 cos(s) + s2 sin(s)
# with d = theta - thetat, s = theta + thetat (generators and frame term are first harmonics). Five
# (d, s) samples with an invertible 5x5 design make "zero at the samples" equal to "zero for all angles".
# Angles with simple exact trig values (the third run used pi/21-type angles that sympy could not cancel).
DS = [
    (0, 0),
    (sp.pi / 2, sp.pi / 2),
    (-sp.pi / 2, sp.pi / 2),
    (0, sp.pi / 2),
    (sp.pi / 3, sp.pi / 3),
]
DESIGN = sp.Matrix([[1, sp.cos(d), sp.sin(d), sp.cos(s), sp.sin(s)] for d, s in DS])
assert DESIGN.det() != 0
ANGLES = [((s + d) / 2, (s - d) / 2) for d, s in DS]


def conditions(psi, spinor):
    eqs = []
    for Ns, sgn in ((NM, +1), (NM, -1), (NP, +1)):
        expr = (ladder(Ns, sgn, psi, spinor) / phase).subs(sub).subs({fA: A, fB: B})
        for th, tt in ANGLES:
            for comp in expr:
                e = sp.expand(sp.simplify(comp.subs({t: th, T: tt})))
                if e != 0:
                    eqs.append(e)
    return eqs


# ---------- spinor ansatz psi = e^{i(t - T)/2} (A(a), B(a)) ----------
# WHY: sp.solve on the 30 symbolic conditions returned [] (first run 2026-11-24), although the numeric
# null space at fixed alpha is one-dimensional (kosmann_rank_scan.py). The closed form below was read off
# the numeric null vectors (B/A = -i tan(alpha/2), A'/A = -tan(alpha/2)/2 at four alphas) and is now
# checked exactly: every condition must vanish identically.
Asol, Bsol = sp.cos(a / 2), -I * sp.sin(a / 2)
eqs = conditions(phase * sp.Matrix([fA, fB]), True)
# WHY: plain simplify left half-angle residues (second run); substitute alpha = 2h and expand_trig.
hh = sp.Symbol("h", positive=True)
tw = sp.Symbol(
    "tw", positive=True
)  # Weierstrass variable tan(h/2) makes every residual rational


def exact_zero(e):
    e = sp.expand_trig(e.subs(a, 2 * hh))
    e = e.subs({sp.tan(hh): sp.sin(hh) / sp.cos(hh)})
    e = e.subs(
        {sp.sin(hh): 2 * tw / (1 + tw**2), sp.cos(hh): (1 - tw**2) / (1 + tw**2)}
    )
    return sp.cancel(sp.together(sp.expand(e)))


resid = [
    exact_zero(e.subs({Ap: sp.diff(Asol, a), Bp: sp.diff(Bsol, a), A: Asol, B: Bsol}))
    for e in eqs
]
exact = all(r == 0 for r in resid)
out["nonzero_residuals"] = [str(r) for r in resid if r != 0]
ok &= exact
out["spinor_conditions"] = len(eqs)
out["closed_form_conditions_vanish_exactly"] = exact
print(
    ("PASS " if exact else "FAIL ")
    + f"closed form satisfies all {len(eqs)} conditions exactly"
)
if True:
    print("A(alpha) =", Asol, "  B(alpha) =", Bsol)
    out["A"], out["B"] = str(Asol), str(Bsol)
    plus = phase * sp.Matrix([Asol, Bsol])
    minus = ladder(NP, -1, plus)
    random.seed(7)
    pts = [
        {
            a: random.uniform(0.15, 1.4),
            t: random.uniform(0, 6.2),
            T: random.uniform(0, 6.2),
        }
        for _ in range(5)
    ]

    def num(M):
        return max(abs(complex(sp.N(c.subs(p)))) for p in pts for c in M)

    checks = {
        "JR3_plus_is_half": (J(NP[2], plus) - plus / 2, True),
        "JL_annihilate_plus": (sp.Matrix.vstack(*[J(N, plus) for N in NM]), True),
        "JR_plus_annihilates_plus": (ladder(NP, +1, plus), True),
        "minus_nonzero": (minus, False),
        "JR3_minus_is_minus_half": (J(NP[2], minus) + minus / 2, True),
        "JR_plus_on_minus_returns_plus": (ladder(NP, +1, minus) - plus, True),
        "JR_minus_annihilates_minus": (ladder(NP, -1, minus), True),
        "JL_annihilate_minus": (sp.Matrix.vstack(*[J(N, minus) for N in NM]), True),
        "control_scalar_action_on_plus_not_closed": (
            ladder(NP, +1, plus, spinor=False),
            False,
        ),
    }
    for k, (M, want_zero) in checks.items():
        v = num(M)
        good = v < 1e-12 if want_zero else v > 1e-6
        ok &= good
        out[k] = {
            "value": v,
            "expected": "zero" if want_zero else "nonzero",
            "pass": good,
        }
        print(("PASS " if good else "FAIL ") + f"{k}: {v:.3e}")
    out["partner_minus"] = str(sp.simplify(minus))
    print("partner m_R = -1/2:", out["partner_minus"])
    out["plus_theta_2pi_ratio"] = str(
        sp.simplify(plus.subs(t, t + 2 * sp.pi)[0] / plus[0])
    )
    out["pointwise_norm2_plus"] = str(sp.simplify((plus.H * plus)[0]))
    print(
        "antiperiodic factor:",
        out["plus_theta_2pi_ratio"],
        " |plus|^2 =",
        out["pointwise_norm2_plus"],
    )

# ---------- scalar control: psi = e^{i(t - T)/2} (A(a), 0), no frame term ----------
seqs = conditions(phase * sp.Matrix([fA, 0]), False)
ssol = sp.solve(seqs, [Ap, A], dict=True)
only_zero = len(ssol) > 0 and all(s.get(A) == 0 for s in ssol)
out["scalar_solutions"], out["scalar_only_zero"] = [str(s) for s in ssol], only_zero
print(
    ("PASS " if only_zero else "FAIL ")
    + f"scalar highest-weight (0,1/2) only A = 0: {ssol}"
)
ok &= only_zero
with open("results_doublet.json", "w") as fh:
    json.dump(out, fh, indent=1)
print("ALL_PASS" if ok else "SOME_FAIL")
sys.exit(0 if ok else 1)
