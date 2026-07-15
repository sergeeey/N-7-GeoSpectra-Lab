"""Independent sympy verification of two claims relayed from an unverified
external analysis, re-derived from scratch per this project's
audit-verification-gate discipline (agent's VERIFIED != our VERIFIED).

H1: ind(D (x) (S^- (x) T^{1,0}S^6)) = 7, not 3, using only this project's own
    established facts (c_3(T)=chi(S^6)=2 from G33, A-hat(S^6)=1 from G73).
H2: I(p,q) = (p-q)(p+1)(q+1)(p+q+2)(p+2q+3)(2p+q+3)/120 gives I(3)=1,
    I(3bar)=-1, I(6)=7.
"""

import sympy as sp

x, y = sp.symbols("x y")
z_sub = -x - y  # Chern roots of T^{1,0}S^6, x+y+z=0 forced by H^2(S^6)=0 (established)

roots_T = [x, y, z_sub]


def ch_exact(bundle_roots, deg):
    total = sp.Integer(0)
    for r in bundle_roots:
        total += r**deg / sp.factorial(deg)
    return sp.expand(total)


ch3_T = ch_exact(roots_T, 3)
c3_T = sp.expand(x * y * z_sub)
assert sp.simplify(ch3_T / c3_T) == sp.Rational(1, 2), "ch3(T)/c3(T) must be 1/2"

roots_TT = [ri + rj for ri in roots_T for rj in roots_T]
assert len(roots_TT) == 9
ch3_TT = ch_exact(roots_TT, 3)
assert sp.simplify(ch3_TT / c3_T) == 3, "ch3(TxT)/c3(T) must be 3"

ch3_E = sp.expand(ch3_T + ch3_TT)  # E = S^-(x)T = T (+) (TxT)
ratio = sp.simplify(ch3_E / ch3_T)
assert ratio == 7, f"expected ch3(E)/ch3(T) = 7, got {ratio}"

# integrate: int ch3(T) = c3(T)/2 integrated = chi(S6)/2 = 2/2 = 1 (G33 result)
int_ch3_T = sp.Rational(1, 1)
index_E = ratio * int_ch3_T  # A-hat(S6)=1 exact (G73), so ind = int ch3(E)
assert index_E == 7

print("H1 CONFIRMED: ch3(E)/ch3(T) =", ratio, "=> ind(D(x)E) =", index_E, "(not 3)")

p, q = sp.symbols("p q")
I_pq = (p - q) * (p + 1) * (q + 1) * (p + q + 2) * (p + 2 * q + 3) * (2 * p + q + 3) / 120

vals = {}
for pq, label in [((1, 0), "3"), ((0, 1), "3bar"), ((2, 0), "6")]:
    v = I_pq.subs({p: pq[0], q: pq[1]})
    vals[label] = v
    print(f"H2: I({label}) at (p,q)={pq} = {v}")

assert vals["3"] == 1
assert vals["3bar"] == -1
assert vals["6"] == 7
print("H2 CONFIRMED: I(3)=1, I(3bar)=-1, I(6)=7 -- matches claimed formula exactly")

# H3 sanity: net index of 6 (+) 3bar^4
net = vals["6"] + 4 * vals["3bar"]
assert net == 3
print(f"H3 sanity: net index of 6(+)3bar^4 = {net} (matches claimed 'net index 3')")
print(
    "but dim ker D+ >= I(6) =", vals["6"], "and dim ker D- >= 4*|I(3bar)| =", 4 * abs(vals["3bar"])
)
print(
    "=> at least", vals["6"] + 4 * abs(vals["3bar"]), "total zero modes, not an exact (3,0) kernel"
)
