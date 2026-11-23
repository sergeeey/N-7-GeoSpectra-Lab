"""Check for the follow-up to Tom (m-values): with m = -1/2 as the intended value, does the scalar ladder close?

Candidates (scalar, half-integer phase):
  Y_up   = e^{i phi/2} sin^{1/2}(theta)   (L_+ Y_up = 0)
  Y_down = e^{-i phi/2} sin^{1/2}(theta)  (L_- Y_down = 0)
Checks:
  Q1. L_+ Y_up = 0.
  Q2. L_- Y_down = 0.
  Q3. L_+ Y_down is NOT a constant multiple of Y_up (so the pair does not close under L_+).
  Q4. L_- Y_up is NOT a constant multiple of Y_down.
Operators (polar, verified in q1_normalisation_numeric.py B):
  L_+ = e^{i phi}(d_theta + i cot(theta) d_phi),  L_- = e^{-i phi}(-d_theta + i cot(theta) d_phi).
"""

import sympy as sp

th, ph = sp.symbols("theta phi", real=True)
I = sp.I


def Lp(f):
    return sp.exp(I * ph) * (sp.diff(f, th) + I * sp.cos(th) / sp.sin(th) * sp.diff(f, ph))


def Lm(f):
    return sp.exp(-I * ph) * (-sp.diff(f, th) + I * sp.cos(th) / sp.sin(th) * sp.diff(f, ph))


Y_up = sp.exp(I * ph / 2) * sp.sqrt(sp.sin(th))
Y_down = sp.exp(-I * ph / 2) * sp.sqrt(sp.sin(th))

fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


def ratio_is_const(a, b):
    r = sp.simplify(a / b)
    return sp.simplify(sp.diff(r, th)) == 0 and sp.simplify(sp.diff(r, ph)) == 0


check("Q1 L_+ Y_up = 0", sp.simplify(Lp(Y_up)) == 0)
check("Q2 L_- Y_down = 0", sp.simplify(Lm(Y_down)) == 0)
lp_down = sp.simplify(Lp(Y_down))
print("   L_+ Y_down =", lp_down)
check("Q3 L_+ Y_down is not a constant multiple of Y_up", not ratio_is_const(lp_down, Y_up))
lm_up = sp.simplify(Lm(Y_up))
print("   L_- Y_up   =", lm_up)
check("Q4 L_- Y_up is not a constant multiple of Y_down", not ratio_is_const(lm_up, Y_down))

print("\nFAILS:", fails if fails else "none")
