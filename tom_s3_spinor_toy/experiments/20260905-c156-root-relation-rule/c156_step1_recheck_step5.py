r"""
C156 STEP 1 -- re-examine C155 Step 5's own falsification.

C155 Step 5 declared the root-relation hypothesis FALSIFIED because:
    weights of the 3 planes : (-2,1), (1,1), (1,-2)
    the vanishing relation among THOSE oriented weights : (1,1,1)
    mu's per-plane coefficient functional               : (1,-1,1)
    -> mismatch, hypothesis dead.

Suspicion: that compared the wrong objects. The oriented weight of a plane
is orientation-DEPENDENT (flip the plane, the weight negates), whereas the
canonical root-theoretic datum attached to a plane is its POSITIVE root,
which is orientation-INDEPENDENT (a plane spans the root space of a pair
+-beta; the positive one is beta either way).

So redo it properly:
  1. From the Cartan generators actually used, identify the simple roots.
  2. Assign to each plane its POSITIVE root (computed, not assumed).
  3. Compute the unique linear relation among those three positive roots.
  4. Compare with mu's functional.

This step CANNOT by itself establish a rule -- one space, one relation, n=1.
It can only establish whether C155 Step 5's falsification was sound.
"""

import sympy as sp

print("=" * 78)
print("C156 STEP 1  re-examining C155 Step 5")
print("=" * 78)

# Cartan generators used throughout C153/C155: cartan_on_m((1,-1,0)), ((0,1,-1)).
# These are the standard simple COROOTS H_1, H_2 of su(3).
# The measured plane weights (C155 Step 5 output, reproduced here as data):
W = {"A": sp.Matrix([-2, 1]), "B": sp.Matrix([1, 1]), "C": sp.Matrix([1, -2])}
print("  measured plane weights (values on the two Cartan generators):")
for k, v in W.items():
    print(f"    plane {k}: {tuple(v)}")

# Standard A_2 simple roots, in the SAME pairing basis: <alpha_i, H_j> is the
# Cartan matrix [[2,-1],[-1,2]].  This is not a choice made to fit anything --
# it is what "simple roots of su(3) paired against the standard simple coroots"
# means.
a1 = sp.Matrix([2, -1])
a2 = sp.Matrix([-1, 2])
theta = a1 + a2  # highest root
print()
print(f"  standard simple roots (rows of the A_2 Cartan matrix): a1={tuple(a1)}, a2={tuple(a2)}")
print(f"  highest root a1+a2 = {tuple(theta)}")

POS = {"a1": a1, "a2": a2, "a1+a2": theta}
print()
print("  assign each plane its POSITIVE root (orientation-independent):")
assign = {}
for k, w in W.items():
    hit = None
    for name, b in POS.items():
        if sp.simplify(w - b) == sp.zeros(2, 1):
            hit = (name, +1)
        if sp.simplify(w + b) == sp.zeros(2, 1):
            hit = (name, -1)
    assert hit is not None, f"plane {k} weight {tuple(w)} is not +-(a positive root)"
    assign[k] = hit
    sign = "+" if hit[1] == 1 else "-"
    print(f"    plane {k}: weight = {sign}({hit[0]})  ->  positive root = {hit[0]}")

print()
print("  the unique linear relation among the three POSITIVE roots:")
c1, c2, c3 = sp.symbols("c1 c2 c3")
bA = POS[assign["A"][0]]
bB = POS[assign["B"][0]]
bC = POS[assign["C"][0]]
sol = sp.solve([(c1 * bA + c2 * bB + c3 * bC)[i] for i in range(2)], [c1, c2, c3], dict=True)
print(f"    solving c1*{assign['A'][0]} + c2*{assign['B'][0]} + c3*{assign['C'][0]} = 0")
print(f"    solution space: {sol}")
# normalise so c1 = 1
s = sol[0]
rho = sp.Matrix([1, s[c2].subs(c3, 1) if c2 in s else 1, 1])
# do it robustly: substitute a free parameter
free = [v for v in (c1, c2, c3) if v not in s]
subsmap = {free[0]: 1}
rho = sp.Matrix([sp.simplify((s.get(v, v)).subs(subsmap)) for v in (c1, c2, c3)])
print(f"    relation coefficients (A,B,C), normalised: {tuple(rho)}")
chk = sp.simplify(rho[0] * bA + rho[1] * bB + rho[2] * bC)
print(f"    check it really vanishes: {tuple(chk)} -> {chk == sp.zeros(2, 1)}")

m = sp.Matrix([1, -1, 1])  # mu's functional, measured in C155 Steps 1/4/6
print()
print("=" * 78)
print("  COMPARISON")
print("=" * 78)
print(f"    mu's per-plane functional (measured, C155)     : {tuple(m)}")
print("    relation among the ORIENTED weights (C155 St5) : (1, 1, 1)")
print(f"    relation among the POSITIVE roots (this step)  : {tuple(rho)}")
prop = sp.simplify(rho.cross(m)) == sp.zeros(3, 1) if rho.rows == 3 else None
print(f"    mu functional PROPORTIONAL to positive-root relation: {prop}")
print()
if prop:
    print("  => C155 Step 5's falsification compared mu against the relation among")
    print("     the ORIENTED weights, which is orientation-dependent. Against the")
    print("     canonical POSITIVE-root relation the two agree exactly.")
    print("     C155 Step 5's verdict was UNSOUND and must be corrected.")
    print("     This does NOT yet establish a rule: n=1, and A_2 has exactly one")
    print("     relation, so agreement here is a 1-in-4 sign coincidence a priori.")
else:
    print("  => C155 Step 5's falsification stands even against positive roots.")
