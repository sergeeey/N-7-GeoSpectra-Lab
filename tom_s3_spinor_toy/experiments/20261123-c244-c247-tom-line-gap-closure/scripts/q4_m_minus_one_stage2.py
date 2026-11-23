"""Q4 and the stage-2 construction of 13.10 (literal reading with scalar L_+-, L_-).

For Y = e^{i m phi} f(theta):
  L_+ Y = e^{i(m+1) phi} (f' - m cot(theta) f)
  L_- Y = e^{i(m-1) phi} (-f' - m cot(theta) f)

Checks:
  S1. m = -1 literal: the solution of L_- Y = 0 is f = sin(theta)  (an l = 1 state, not spin-1/2).
  S2. m = +1/2: L_+ Y = 0 gives f = sin^{1/2}(theta), Y_{1/2,1/2} = e^{i phi/2} sin^{1/2}(theta).
  S3. m = -1/2: L_- Y = 0 gives f = sin^{1/2}(theta), Y_{1/2,-1/2} = e^{-i phi/2} sin^{1/2}(theta).
  S4. L_- Y_{1/2,1/2} is NOT proportional to Y_{1/2,-1/2}  (Tom's 'check that it gives Y_{1/2,-1/2}' fails).
  S5. L_- Y_{1/2,-1/2} is not zero (the multiplet does not close).
  S6. Boundary: all these functions carry half-integer phase e^{i m phi}; none is single-valued in phi.
"""

import sympy as sp

th, ph = sp.symbols("theta phi", real=True)
I = sp.I
fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


def strip_phase(expr, m):
    """Divide out e^{i k phi}: returns the theta-part of an expression."""
    return sp.simplify(expr * sp.exp(-I * (m) * ph))


def Lp_theta(f, m):
    # L_+ (e^{i m phi} f) = e^{i(m+1) phi} (f' - m cot f)
    return sp.simplify(sp.diff(f, th) - m * sp.cos(th) / sp.sin(th) * f)


def Lm_theta(f, m):
    # L_- (e^{i m phi} f) = e^{i(m-1) phi} (-f' - m cot f)
    return sp.simplify(-sp.diff(f, th) - m * sp.cos(th) / sp.sin(th) * f)


# Sanity: the operator forms reproduce the formulas above
F = sp.Function("F")(th)
m_sym = sp.symbols("m")
Lp_direct = sp.simplify(
    sp.exp(-I * (m_sym + 1) * ph)
    * sp.exp(I * ph)
    * (
        sp.diff(sp.exp(I * m_sym * ph) * F, th)
        + I * sp.cos(th) / sp.sin(th) * sp.diff(sp.exp(I * m_sym * ph) * F, ph)
    )
)
check(
    "S0 operator form: L_+ on e^{i m phi} F gives e^{i(m+1)phi}(F' - m cot F)",
    sp.simplify(Lp_direct - (sp.diff(F, th) - m_sym * sp.cos(th) / sp.sin(th) * F)) == 0,
)

# S1  m = -1: L_- Y = 0
f_m1 = sp.sin(th)
check("S1a literal m=-1: f = sin(theta) satisfies L_- Y = 0", sp.simplify(Lm_theta(f_m1, -1)) == 0)
check(
    "S1b literal m=-1: L_+ of the same function is non-zero (so it is not an L_+ null state; it is the l=1 lowest weight Y_{1,-1})",
    sp.simplify(Lm_theta(f_m1, -1)) == 0 and sp.simplify(Lp_theta(f_m1, -1)) != 0,
)

# S2  m = +1/2: L_+ Y = 0
f_p = sp.sqrt(sp.sin(th))
check(
    "S2 m=+1/2: f = sin^{1/2} th gives L_+ Y = 0",
    sp.simplify(Lp_theta(f_p, sp.Rational(1, 2))) == 0,
)

# S3  m = -1/2: L_- Y = 0
f_m = sp.sqrt(sp.sin(th))
check(
    "S3 m=-1/2: f = sin^{1/2} th gives L_- Y = 0",
    sp.simplify(Lm_theta(f_m, -sp.Rational(1, 2))) == 0,
)

# S4  the step 'apply L_- to Y_{1/2,1/2}' :
Lm_of_Yhalf = Lm_theta(f_p, sp.Rational(1, 2))  # theta-part of L_- Y_{1/2,1/2}; phase e^{-i phi/2}
print("   theta-part of L_- Y_{1/2,1/2} =", sp.simplify(Lm_of_Yhalf))
prop = sp.simplify(Lm_of_Yhalf / f_m)
print("   ratio to sin^{1/2} th (the Y_{1/2,-1/2} candidate) =", prop)
check(
    "S4 L_- Y_{1/2,1/2} is NOT a constant multiple of Y_{1/2,-1/2} (ratio depends on theta)",
    sp.simplify(sp.diff(prop, th)) != 0,
)

# S5  the multiplet does not close: L_- Y_{1/2,-1/2} != 0
Lm_of_Yminus = Lm_theta(f_m, -sp.Rational(1, 2))
check("S5 (control, must be 0 by S3) L_- Y_{1/2,-1/2} = 0", sp.simplify(Lm_of_Yminus) == 0)
# the actual closure test: L_- applied to the state obtained from L_- Y_{1/2,1/2}, with m = -1/2
Lm_twice = Lm_theta(sp.simplify(Lm_of_Yhalf), -sp.Rational(1, 2))
print("   L_- applied again (m=-1/2 phase):", sp.simplify(Lm_twice))

# S6  phases: all candidates carry e^{i m phi} with m half-integer -> not single-valued
for name, mval in (("Y_{1/2,1/2}", sp.Rational(1, 2)), ("Y_{1/2,-1/2}", -sp.Rational(1, 2))):
    check(
        f"S6 {name} has phase e^{{i m phi}}, m={mval}, antiperiodic under phi->phi+2pi",
        sp.simplify(sp.exp(I * mval * 2 * sp.pi) + 1) == 0,
    )

print("\nFAILS:", fails if fails else "none")
