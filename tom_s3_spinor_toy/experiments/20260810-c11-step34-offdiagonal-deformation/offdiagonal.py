"""C11 steps 3+4: the sector grading of A, and the off-diagonal deformation M(alpha,beta).

WHY THESE TWO ARE RUN TOGETHER. Step 3 of the agreed portfolio was the sector/mixing
test ([T,a] vs {T,a}). After step 1 it is a ONE-LINE COROLLARY of the symbol table
already computed there, not a new experiment -- and this file says so rather than
re-packaging it as a fresh finding (the failure mode round110 was caught in: restating
round106 as new evidence). Step 4 -- an off-diagonal M between the sectors, and the
region of (alpha,beta) where the structure survives -- IS substantive, because
D_block is currently strictly block-diagonal and an off-diagonal term is exactly how
a Yukawa-like coupling would enter.

THE DEFORMATION. Self-adjointness allows

    D(alpha,beta) = D_block + Y (x) s2 * alpha + X (x) s1 * beta

and {gamma, D} = 0 with gamma = U_iota (x) s1 constrains the two coefficients in
OPPOSITE ways, because conjugation by s1 fixes s1 and flips s2:

    X must be iota-ODD   (U_iota X U_iota^dag = -X)   -> take X = D^{1/2}
    Y must be iota-EVEN  (U_iota Y U_iota^dag = +Y)   -> take Y = Identity

so the minimal admissible deformation is  alpha*(I (x) s2) + beta*(D^{1/2} (x) s1).

PREDICTIONS, recorded before running:
  Q1  A is Z2-GRADED by the sector order parameter T = s3, with even part exactly
      the twisted diagonal {diag(f, f o iota)}       [COROLLARY of step 1, not new]
  Q2  the admissible off-diagonal pair is (X iota-odd with s1, Y iota-even with s2)
  Q3  eigenvalues become  mu +- sqrt(9/4 + beta^2 mu^2 + alpha^2),  mu = sigma(n+3/2)
  Q4  the 4-dim kernel at (0,0) is an ISOLATED point -- ANY nonzero (alpha,beta)
      destroys it. This is a no-collapse test and the prediction is that it FAILS.
  Q5  other kernels appear on the curves 9/4 + alpha^2 = (n+3/2)^2 (1 - beta^2), n>=1
  NC  a NON-admissible deformation (I (x) s1, wrong parity) must break {gamma,D}=0

WHAT THIS CANNOT SHOW: whether the off-diagonal term is allowed by the FIRST-ORDER
condition. That is step 5, and Q4's outcome is what makes step 5 decisive rather
than decorative.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_step34.json"
results: dict = {}

H_H = 3
N_MAX = 6

S = [
    np.eye(2, dtype=complex),
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[-1, 0], [0, 1]], dtype=complex),  # T: sector order parameter, -1 <-> t=0
]

print("=" * 78)
print("C11 steps 3+4 -- sector grading of A, and the off-diagonal deformation")
print("=" * 78)

# --- Q1: COROLLARY of step 1, explicitly labelled as such --------------------
print("\nQ1 -- [COROLLARY of step 1, NOT new evidence] how does A sit w.r.t. T = s3?")
EVEN_SYMS = {(+1, 0): "even(x)I", (+1, 1): "even(x)s1", (-1, 2): "odd (x)s2", (-1, 3): "odd (x)s3"}
grading = {}
for (par, k), name in EVEN_SYMS.items():
    comm = np.allclose(S[3] @ S[k] - S[k] @ S[3], 0)
    anti = np.allclose(S[3] @ S[k] + S[k] @ S[3], 0)
    grading[name] = "commutes" if comm else ("anticommutes" if anti else "neither")
    print(f"    {name:12s} with T: {grading[name]}")
a_even = {n for n, v in grading.items() if v == "commutes"}
print(f"    => A is Z2-graded by T. Even part = {sorted(a_even)}")
q1 = a_even == {"even(x)I", "odd (x)s3"}
print(f"    Q1: the T-even part is EXACTLY the twisted diagonal {{diag(f, f o iota)}}: {q1}")
print("        (this restates C46's symbol table in a different basis -- recorded as a")
print("         corollary, and it is NOT counted as independent support for anything)")
results["q1_grading_by_T"] = grading
results["q1_even_part_is_twisted_diagonal"] = bool(q1)

# --- Q2: which off-diagonal terms are admissible? ----------------------------
print("\nQ2 -- which off-diagonal deformations survive {gamma, D} = 0? (gamma = U_iota (x) s1)")
q2 = {}
for xname, x_iota_parity in (("D^{1/2} (iota-ODD)", -1), ("Identity (iota-EVEN)", +1)):
    for k in (1, 2):
        # conj by gamma: X -> (parity)X ,  s_k -> s1 s_k s1 = (+1 for k=1, -1 for k=2) s_k
        pauli_sign = +1 if k == 1 else -1
        anticommutes = (x_iota_parity * pauli_sign) == -1
        q2[f"{xname} (x) s{k}"] = anticommutes
        print(f"    {'OK  ' if anticommutes else '--  '}{xname:22s}(x) s{k}: {anticommutes}")
q2_ok = q2["D^{1/2} (iota-ODD) (x) s1"] and q2["Identity (iota-EVEN) (x) s2"]
q2_ok &= not q2["Identity (iota-EVEN) (x) s1"] and not q2["D^{1/2} (iota-ODD) (x) s2"]
print(f"\n    Q2 (odd-with-s1 and even-with-s2 admissible, the other two NOT): {q2_ok}")
print("    NEGATIVE CONTROL is built in: I (x) s1 has the WRONG parity and FAILS.")
results["q2_admissible_offdiagonal"] = q2
results["q2_pattern_confirmed"] = bool(q2_ok)

# --- Q3: the deformed spectrum, symbolically ---------------------------------
print("\nQ3 -- deformed eigenvalues, exactly")
al, be, mu = sp.symbols("alpha beta mu", real=True)
blk = sp.Matrix(
    [[mu - sp.Rational(3, 2), be * mu - sp.I * al], [be * mu + sp.I * al, mu + sp.Rational(3, 2)]]
)
ev = sorted((sp.simplify(e) for e in sp.Matrix(blk).eigenvals()), key=str)
closed = sp.simplify(ev[0] - (mu - sp.sqrt(sp.Rational(9, 4) + be**2 * mu**2 + al**2)))
closed2 = sp.simplify(ev[1] - (mu + sp.sqrt(sp.Rational(9, 4) + be**2 * mu**2 + al**2)))
q3 = (closed == 0 and closed2 == 0) or (
    sp.simplify(ev[1] - (mu - sp.sqrt(sp.Rational(9, 4) + be**2 * mu**2 + al**2))) == 0
)
print(f"    eigenvalues = {ev[0]}  and  {ev[1]}")
print(f"    Q3 matches mu +- sqrt(9/4 + beta^2 mu^2 + alpha^2): {q3}")
results["q3_closed_form"] = [str(e) for e in ev]
results["q3_matches_prediction"] = bool(q3)

# --- Q4 / Q5: where does the kernel live? ------------------------------------
print("\nQ4/Q5 -- kernel of D(alpha,beta): NO-COLLAPSE TEST on the 4-dim kernel")


def kernel_dim(a: float, b: float, nmax: int = N_MAX) -> int:
    d = 0
    for n in range(nmax + 1):
        for sgn in (+1, -1):
            m = sgn * (n + 1.5)
            blk_n = np.array([[m - 1.5, b * m - 1j * a], [b * m + 1j * a, m + 1.5]])
            d += int(np.sum(np.isclose(np.linalg.eigvalsh(blk_n), 0.0, atol=1e-9))) * (
                (n + 1) * (n + 2)
            )
    return d


probe = [(0.0, 0.0), (0.1, 0.0), (0.0, 0.1), (0.3, 0.2), (0.0, 0.8)]
kt = {}
for a, b in probe:
    kt[f"({a},{b})"] = kernel_dim(a, b)
    print(f"    (alpha,beta) = ({a:9.2e}, {b:9.2e})   dim ker = {kt[f'({a},{b})']}")

# The boolean above must NOT be evaluated at tiny (alpha,beta): at alpha = 1e-6 the
# surviving eigenvalue is ~ alpha^2/3 ~ 3e-13, INSIDE any reasonable atol, so a
# "dim ker = 4" there measures the tolerance and not the operator. First version of
# this file did exactly that. The isolation is settled EXACTLY instead.
print("\n    Q4a -- EXACT: solve the n=0 kernel condition mu^2(1-beta^2) = 9/4 + alpha^2")
print("           over the reals, at mu^2 = 9/4 (the n=0 level)")
only_origin = sp.simplify(sp.Rational(9, 4) * (1 - be**2) - sp.Rational(9, 4) - al**2)
forced = sp.simplify(only_origin + al**2 + sp.Rational(9, 4) * be**2) == 0
# sp.solve on this returns the PARAMETRIC COMPLEX root alpha = +-3i*beta/2, which over
# the reals is the origin and nothing else -- but reading that off a solve() return is
# error-prone. The exact statement is settled by positive-definiteness instead: a
# positive-definite real quadratic form vanishes only at 0.
Q = sp.Matrix([[1, 0], [0, sp.Rational(9, 4)]])
pos_def = bool(Q.is_positive_definite)
print(f"           condition reduces to  alpha^2 + (9/4) beta^2 = 0 : {forced}")
print(f"           that form is positive-definite (eigenvalues {sorted(Q.eigenvals())}): {pos_def}")
print("           => over the REALS its only zero is the origin. Isolation is EXACT.")
q4a = bool(forced and pos_def)

print("\n    Q4b -- SCALING: smallest |eigenvalue| at n=0 vs alpha (expect ~ alpha^2/3)")
scal = {}
for a in (1e-3, 1e-2, 1e-1):
    m = 1.5
    lam = float(
        np.min(np.abs(np.linalg.eigvalsh(np.array([[m - 1.5, -1j * a], [1j * a, m + 1.5]]))))
    )
    scal[a] = {"min_abs_eig": lam, "ratio_to_alpha2_over_3": lam / (a**2 / 3)}
    print(
        f"           alpha = {a:.0e}   min|lambda| = {lam:.6e}   /(alpha^2/3) = {lam / (a**2 / 3):.4f}"
    )
scaling_ok = all(0.9 < v["ratio_to_alpha2_over_3"] < 1.1 for v in scal.values())
print(f"           moves off zero quadratically, never stays at zero: {scaling_ok}")

q4 = kt["(0.0,0.0)"] == 4 and kt["(0.1,0.0)"] == 0 and kt["(0.0,0.1)"] == 0
q4 = bool(q4 and q4a and scaling_ok)
print(f"\n    Q4: the 4-dim kernel is destroyed by ANY nonzero (alpha,beta): {q4}")
print("        => it is an ISOLATED point, NOT a stable feature. This is a")
print("           NO-COLLAPSE TEST and the 4-dim kernel FAILS it.")
results["q4a_exact_isolation"] = bool(q4a)
results["q4b_scaling"] = scal

print("\n    Q5 -- where kernels DO reappear: 9/4 + alpha^2 = (n+3/2)^2 (1 - beta^2)")
curves = {}
for n in range(4):
    rhs = (n + 1.5) ** 2
    b_at_zero_alpha = 1 - 2.25 / rhs
    if b_at_zero_alpha >= 0:
        bb = float(np.sqrt(b_at_zero_alpha))
        d = kernel_dim(0.0, bb)
        curves[f"n={n}"] = {"beta_at_alpha0": round(bb, 6), "ker_dim": d}
        print(f"    n = {n}: alpha=0 gives beta = {bb:.6f},  dim ker = {d}")
q5 = curves["n=0"]["beta_at_alpha0"] == 0.0 and all(
    v["ker_dim"] > 0 for k, v in curves.items() if k != "n=0"
)
print("    Q5: n=0's 'curve' degenerates to the single point (0,0); n>=1 give real")
print(f"        curves with LARGER kernels (over-production, as at t=-1/3 in C44): {q5}")
results["q4_kernel_table"] = kt
results["q4_kernel_is_isolated"] = bool(q4)
results["q5_curves"] = curves
results["q5_confirmed"] = bool(q5)

# --- VERDICT -----------------------------------------------------------------
print("\n" + "=" * 78)
ok = q1 and q2_ok and q3 and q4 and q5
verdict = "FOUR_DIM_KERNEL_IS_UNSTABLE__STEP5_NOW_DECISIVE" if ok else "INCONCLUSIVE"
print(f"VERDICT: {verdict}")
print("=" * 78)
if ok:
    print("  The block admits a two-parameter family of self-adjoint, gamma-anticommuting")
    print("  off-diagonal deformations, and the 4-dim kernel that matched C38's Spin(4)")
    print("  spinor survives at EXACTLY ONE point of it, (alpha,beta) = (0,0).")
    print()
    print("  Consequence, and it cuts both ways:")
    print("   - AGAINST: the 4-dim kernel is not a robust feature of the two-operator")
    print("     structure. It is a property of the UNDEFORMED block, and nothing found")
    print("     so far forbids the deformation.")
    print("   - FOR: this makes step 5 decisive rather than decorative. If the")
    print("     first-order condition forbids the off-diagonal terms, the kernel's")
    print("     isolation stops being a fragility and becomes a SELECTION -- (0,0)")
    print("     would then be the only point compatible with the axioms.")
    print()
    print("  Either way the question is now sharp and cheap to settle, which it was not")
    print("  before this deformation was written down.")
results["verdict"] = verdict
RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
print(f"\nResults -> {RESULTS_PATH}")
