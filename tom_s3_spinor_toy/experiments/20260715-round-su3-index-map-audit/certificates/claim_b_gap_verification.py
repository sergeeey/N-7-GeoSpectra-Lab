"""Numerical certificate supporting (not replacing) Claim B's analytic proof.

Checks, via sympy, the specific sub-claims the proof relies on:
1. I(p,0) matches the claimed closed form and is strictly increasing for p=1..9.
2. The q>=1, p>=q+1 branch has its minimum at (p,q)=(2,1)=14 over a wide scan.
3. Sign structure: I(p,q) > 0 iff p > q, over (p,q) in [0,15]^2.

This is a control, not a proof: it cannot cover all (p,q). The proof itself
rests on the algebraic monotonicity of a product of strictly increasing
positive factors, verified symbolically here only for the closed q=0 form.
"""

import sympy as sp

p, q = sp.symbols("p q", integer=True)
I_pq = (p - q) * (p + 1) * (q + 1) * (p + q + 2) * (p + 2 * q + 3) * (2 * p + q + 3) / 120

# 1. q=0 branch
Iq0 = I_pq.subs(q, 0)
formula_q0 = p * (p + 1) * (p + 2) * (p + 3) * (2 * p + 3) / 120
assert sp.simplify(Iq0 - formula_q0) == 0, "I(p,0) closed form mismatch"

vals_q0 = [Iq0.subs(p, pv) for pv in range(1, 10)]
assert all(vals_q0[i] < vals_q0[i + 1] for i in range(len(vals_q0) - 1)), "not monotone"
assert vals_q0[0] == 1 and vals_q0[1] == 7
print("Claim B check 1/3: I(p,0) closed form + monotone increase p=1..9 CONFIRMED:", vals_q0)

# 2. q>=1, p>=q+1 branch minimum search
candidates = []
for qv in range(1, 15):
    for pv in range(qv + 1, qv + 15):
        candidates.append((pv, qv, I_pq.subs({p: pv, q: qv})))
min_val = min(candidates, key=lambda t: t[2])
assert min_val == (2, 1, 14), f"expected min (2,1,14), got {min_val}"
below_14 = [c for c in candidates if c[2] < 14]
assert not below_14, f"found values below 14: {below_14}"
print("Claim B check 2/3: q>=1 branch minimum CONFIRMED at (2,1)=14, no counterexample in scan")

# 3. sign structure over [0,15]^2
mismatches = []
for pv in range(0, 16):
    for qv in range(0, 16):
        v = I_pq.subs({p: pv, q: qv})
        if pv > qv and not v > 0:
            mismatches.append((pv, qv, v, "expected>0"))
        if pv <= qv and not v <= 0:
            mismatches.append((pv, qv, v, "expected<=0"))
assert not mismatches, f"sign mismatches: {mismatches}"
print("Claim B check 3/3: sign structure I(p,q)>0 <=> p>q CONFIRMED, zero exceptions in [0,15]^2")

print()
print("All three sub-checks pass. This SUPPORTS the analytic gap proof; it does")
print("NOT replace it (finite scan, not exhaustive over all p,q).")
