"""Q6 (after Q5): central element, rotations on S^3, spinor transformation, exchange statistics. Four separate facts.

Setting: G = SU(2) acts on S^3 = SU(2) (by left multiplication on the point xi in C^2) and on scalar functions by
dragging: (g.f)(xi) = f(g^{-1} xi). The central element z = -1 in SU(2) acts on S^3 as xi -> -xi.

  P1. Central element: z = -1 acts on functions as f(xi) -> f(-xi). Its eigenvalues are +1 (even f) and -1 (odd f).
      Odd functions carry half-integer SU(2)_L spin, even functions integer spin. (Identity; checked on xi, |xi|^2.)
  P2. Orthogonality: L^2(S^3) = L^2_even (+) L^2_odd, orthogonal. Hence an odd function is NOT an L^2-superposition
      of even functions. PROVED (antipodal symmetry of the measure). Numeric check below.
  P3. Products: odd x odd = even. So two identical odd (spin-1/2) functions compose into an even (integer spin) product.
      Checked symbolically: xi^1 xi^2 - xi^2 xi^1 = 0 identically (commuting functions).
  P4. Exchange (statistics) of two identical composites: for COMMUTING functions the antisymmetric combination
      eps_{ab} xi^a xi^b vanishes, so only the symmetric spin-1 part survives: {xi1^2, xi1 xi2, xi2^2} is a 3-dim
      SU(2)_L-invariant space (spin 1). Commutation vs anticommutation is an algebra choice; it is NOT derived
      from the representation.
  P5. On S^2 = S^3/U(1) (rotations SO(3)): the central element acts TRIVIALLY on the Bloch point. So the parity
      distinguishing spin-1/2 from spin-1 is not available on S^2. This is why the S^2 amplitude e^{i ph/2} (Q5, Q6)
      does not carry a fermion-parity invariant.
  P6. Spin-1/2 transformation of the spinor state: the action of 2 pi-rotation (central element) on xi is -1; on
      functions of n (S^2) it is +1. The -1 lives in the fibre/on S^3, not in the Bloch data.
"""

import numpy as np

rng = np.random.default_rng(23)
fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


def rand_s3(n):
    v = rng.normal(size=(n, 4))
    v /= np.linalg.norm(v, axis=1)[:, None]
    return np.column_stack([v[:, 0] + 1j * v[:, 1], v[:, 2] + 1j * v[:, 3]])


# P1: parity of simple functions under xi -> -xi
X = rand_s3(4000)
f_even = np.abs(X[:, 0]) ** 2
f_odd = X[:, 0]
check(
    "P1a |xi_1|^2 is even under the central element", np.allclose(f_even, np.abs((-X)[:, 0]) ** 2)
)
check("P1b xi_1 is odd under the central element", np.allclose(f_odd, -((-X)[:, 0])))

# P2 orthogonality of even and odd (Monte Carlo on S^3, uniform measure)
Xs = rand_s3(400000)
even = np.abs(Xs[:, 0]) ** 2 + np.abs(Xs[:, 1]) ** 2 * 0.3 + (Xs[:, 0] * np.conj(Xs[:, 1])).real
odd = Xs[:, 0] + 0.2 * Xs[:, 1]
ip = np.mean(np.conj(even) * odd)
norm = np.sqrt(np.mean(np.abs(even) ** 2) * np.mean(np.abs(odd) ** 2))
print("   |<even,odd>| / (norms) = %.3e  (Monte Carlo, 4e5 points)" % (abs(ip) / norm))
check(
    "P2 even and odd functions are L^2-orthogonal (normalised overlap below 1e-2)",
    abs(ip) / norm < 1e-2,
)

# P3 composites: xi^a xi^b symmetric
ok3 = True
for _ in range(50):
    x = rand_s3(1)[0]
    ok3 &= abs(x[0] * x[1] - x[1] * x[0]) < 1e-15
check(
    "P3 eps_{ab} xi^a xi^b = 0 identically for commuting functions (antisymmetric composite vanishes)",
    ok3,
)

# P3b: the symmetric composites span a 3-dim space (spin 1) and the product of two odd functions is even
Xc = rand_s3(200)
comp = np.column_stack([Xc[:, 0] ** 2, Xc[:, 0] * Xc[:, 1], Xc[:, 1] ** 2])
rank = np.linalg.matrix_rank(comp, tol=1e-9)
check(
    "P4 symmetric composites {xi1^2, xi1 xi2, xi2^2} span a 3-dim space (spin 1 in L^2(S^3))",
    rank == 3,
)
prod_even = np.allclose((Xc[:, 0] ** 2), (-Xc)[:, 0] ** 2)
check("P3c odd x odd is even (xi_1 * xi_1 is invariant under xi -> -xi)", prod_even)

# P5 the central element acts trivially on the Bloch point n(xi) = xi^dag sigma xi
sig = [
    np.array([[0, 1], [1, 0]], complex),
    np.array([[0, -1j], [1j, 0]], complex),
    np.array([[1, 0], [0, -1]], complex),
]
ok5 = True
for x in Xc[:50]:
    nb = np.array([np.vdot(x, s @ x).real for s in sig])
    nb2 = np.array([np.vdot(-x, s @ (-x)).real for s in sig])
    ok5 &= np.linalg.norm(nb - nb2) < 1e-12
check("P5 the central element leaves the Bloch point invariant (it is trivial on S^2)", ok5)

print("\nFAILS:", fails if fails else "none")
