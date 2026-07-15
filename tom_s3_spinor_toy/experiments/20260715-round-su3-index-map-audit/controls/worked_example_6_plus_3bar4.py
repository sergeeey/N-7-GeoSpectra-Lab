"""Positive control for Claim C: reproduces the E=6(+)3bar^4 worked example
kernel-dimension bound, using I(p,q) values conditional on Claim A.
"""

import sympy as sp

p, q = sp.symbols("p q", integer=True)
I_pq = (p - q) * (p + 1) * (q + 1) * (p + q + 2) * (p + 2 * q + 3) * (2 * p + q + 3) / 120

ind_6 = I_pq.subs({p: 2, q: 0})
ind_3bar = I_pq.subs({p: 0, q: 1})
assert ind_6 == 7
assert ind_3bar == -1

ker_plus_min = ind_6  # dim ker D_6^+ >= ind(D_6) when ind>0
ker_minus_min = 4 * abs(ind_3bar)  # dim ker D_3bar^-^{x4} >= 4*|ind(D_3bar)|
net_index = ind_6 + 4 * ind_3bar

assert net_index == 3, f"expected net index 3, got {net_index}"
assert ker_plus_min == 7
assert ker_minus_min == 4
total_modes = ker_plus_min + ker_minus_min
assert total_modes == 11

print(f"net index = {net_index} (matches naive target 3)")
print(f"dim ker D_E+ >= {ker_plus_min}, dim ker D_E- >= {ker_minus_min}")
print(f"=> at least {total_modes} total zero modes, NOT exact (3,0)")
print("CONFIRMS Claim C worked example (standard block-diagonal operator class)")
