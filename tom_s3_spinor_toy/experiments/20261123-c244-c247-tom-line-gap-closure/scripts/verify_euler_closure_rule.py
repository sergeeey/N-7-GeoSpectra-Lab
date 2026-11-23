"""Does the Euler-angle picture PREDICT which (j, s) pairs close the ladder (the exploratory rule of C221 section 5)?

Prediction written before the run (from two lines of algebra, not from the C221 table):
  J+ (e^{i m phi} e^{i k psi} f) = e^{i(m+1)phi} e^{i k psi} [ f' - m cot(theta) f + k f / sin(theta) ]
  highest weight m = j:  f_high = sin^{j-k}(theta/2) cos^{j+k}(theta/2)
  lowest  weight m = -j: f_low  = sin^{j+k}(theta/2) cos^{j-k}(theta/2)
  regular at both poles  <=>  |k| <= j.
  A function on SU(2) needs m - k in Z, i.e. j - k in Z (m runs over j, j-1, ..., -j).
  Prediction: J-^{2j} psi_high is a CONSTANT multiple of psi_low  <=>  |k| <= j and j - k in Z.
  With s = -k (C221 writes the extra term as -s/sin(theta); here it is k/sin(theta), k = -s).
The operators J+, J-, J_z are the ones verified in verify_euler_operators.py (derived from the group action).
Negative controls: pairs the rule excludes must show a NON-constant ratio (or a pole), otherwise the test cannot fail.
"""

import random

import sympy as sp

th, ph, ps = sp.symbols("theta phi psi", real=True)
I = sp.I
random.seed(3)
ths = [random.uniform(0.4, 2.7) for _ in range(5)]


def Jm(f):
    return sp.exp(-I * ph) * (
        -sp.diff(f, th) + I * sp.cot(th) * sp.diff(f, ph) - (I / sp.sin(th)) * sp.diff(f, ps)
    )


def Jp(f):
    return sp.exp(I * ph) * (
        sp.diff(f, th) + I * sp.cot(th) * sp.diff(f, ph) - (I / sp.sin(th)) * sp.diff(f, ps)
    )


def num(expr, t):
    return complex(sp.N(expr.subs({th: t, ph: 0.7, ps: 0.3}), 30))


def closes(j, k):
    """True if J-^{2j} psi_high / psi_low is the same number at all test angles (and finite)."""
    m = j
    hi = (
        sp.exp(I * m * ph)
        * sp.exp(I * k * ps)
        * sp.sin(th / 2) ** (j - k)
        * sp.cos(th / 2) ** (j + k)
    )
    lo = (
        sp.exp(-I * j * ph)
        * sp.exp(I * k * ps)
        * sp.sin(th / 2) ** (j + k)
        * sp.cos(th / 2) ** (j - k)
    )
    # highest weight really is annihilated by J+ (only meaningful where f_high is a legitimate function)
    f = hi
    for _ in range(int(round(2 * j))):  # noqa: RUF046 (j may be a sympy Rational, int() is needed)
        f = Jm(f)
    try:
        ratios = [num(f, t) / num(lo, t) for t in ths]
    except (ZeroDivisionError, ValueError, OverflowError):
        return False, None
    if any(abs(r) != abs(r) or abs(r) > 1e12 for r in ratios):
        return False, None
    spread = max(abs(r - ratios[0]) for r in ratios) / max(abs(ratios[0]), 1e-30)
    return spread < 1e-9 and abs(ratios[0]) > 1e-9, ratios[0]


def annihilated(j, k):
    hi = (
        sp.exp(I * j * ph)
        * sp.exp(I * k * ps)
        * sp.sin(th / 2) ** (j - k)
        * sp.cos(th / 2) ** (j + k)
    )
    return all(abs(num(Jp(hi), t)) < 1e-9 for t in ths)


R = sp.Rational
js = [R(1, 2), R(1), R(3, 2), R(2)]
ks = [R(0), R(1, 2), R(-1, 2), R(1), R(-1), R(3, 2), R(-3, 2), R(2), R(-2)]
ok = True
rows = []
for j in js:
    for k in ks:
        predicted = abs(k) <= j and (j - k).q == 1
        got, ratio = closes(j, k)
        agree = predicted == got
        ok &= agree
        rows.append((j, k, -k, predicted, got, ratio, annihilated(j, k)))
        print(
            f"j={j!s:>4} k={k!s:>5} (s={-k!s:>5}): predicted closes={predicted!s:5} measured closes={got!s:5} "
            f"{'agree' if agree else 'DISAGREE'}  ratio={'-' if ratio is None else f'{ratio.real:.4g}'}"
        )

pos = sum(1 for r in rows if r[3])
neg = sum(1 for r in rows if not r[3])
print(
    f"\npairs where the rule predicts closure: {pos}, predicts failure: {neg}  (both kinds present: {pos > 0 and neg > 0})"
)
print("annihilated by J+ in all rows:", all(r[6] for r in rows))

# the pairs of C221 section 5: j in {1/2, 1, 3/2}, s in {0, +-1/2, +-1, +-3/2}; its exploratory rule was 'j - |s| is a non-negative integer'
c221 = [
    (j, s)
    for j in (R(1, 2), R(1), R(3, 2))
    for s in (R(0), R(1, 2), R(-1, 2), R(1), R(-1), R(3, 2), R(-3, 2))
]
rule_c221 = {(j, s): (j - abs(s) >= 0 and (j - abs(s)).q == 1) for j, s in c221}
rule_euler = {(j, s): (abs(s) <= j and (j - (-s)).q == 1) for j, s in c221}
print(
    "C221 exploratory rule == Euler-angle rule on all 21 pairs:",
    rule_c221 == rule_euler,
    f"({len(c221)} pairs)",
)
ok &= rule_c221 == rule_euler
print("ALL AGREE" if ok else "SOME DISAGREE")
