"""Q6 critical check: which superposition statements are actually proved, and which are only special cases.

Definitions. On S^3: even = f(-xi) = f(xi), odd = f(-xi) = -f(xi). z = -1 in SU(2) acts as xi -> -xi.

  M1. Constant-coefficient superpositions: for even functions e_k and constants c_k, sum_k c_k e_k is even.
      So no constant-coefficient superposition of even functions is odd. (Identity.)
  M2. L^2-closure: P_even is the orthogonal projection onto even functions; for odd o, P_even(o) = 0.
      So o is not in the L^2-closure of even functions. (Projection argument; numerical check with a test function.)
  M3. Function coefficients break M1: xi_1 = xi_1 * 1 with 1 even and coefficient xi_1 odd. Hence the theorem
      requires CONSTANT coefficients (the correspondent's 'superposition' in ket language). This is an explicit premise.
  M4. Products: pointwise product of two odd functions is even; of three odd functions is odd.
      So composites of two fermions are bosons (even), composites of three are fermions (odd).
  M5. Antisymmetric pairing of ONE doublet with itself: eps_{ab} xi^a xi^b = 0 (commuting, same field).
  M6. Antisymmetric pairing of two DIFFERENT doublets: eps_{ab} xi^a (eps xibar)^b = -|xi|^2 = -1 (constant,
      SU(2)-singlet). So a pair (xi, eps xibar) produces a spin-0 composite, which is the constant -1.
      This is the non-transfer warning of Q6: M5 does not imply that no spin-0 composite exists.
  M7. The spin-0 composite of M6 is a constant function, i.e. it carries no spin-1/2 data; the spin-1/2
      content is lost in the composite.
"""

import numpy as np

rng = np.random.default_rng(53)
fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


eps = np.array([[0, 1], [-1, 0]], dtype=complex)


def rand_s3(n):
    v = rng.normal(size=(n, 4))
    v /= np.linalg.norm(v, axis=1)[:, None]
    return np.column_stack([v[:, 0] + 1j * v[:, 1], v[:, 2] + 1j * v[:, 3]])


def even_fn(X):
    return (
        np.abs(X[:, 0]) ** 2 + 0.3 * np.abs(X[:, 1]) ** 2 + 0.2 * (X[:, 0] * np.conj(X[:, 1])).real
    )


def odd_fn(X):
    return X[:, 0] + 0.5j * X[:, 1]


X = rand_s3(20000)
# M1 constant-coefficient superpositions of even functions stay even
Xm = -X
e1, e2 = even_fn(X), even_fn(X) ** 2
c1, c2 = 1.3 - 0.4j, -0.7 + 0.2j
s = c1 * e1 + c2 * e2
s_neg = c1 * even_fn(Xm) + c2 * even_fn(Xm) ** 2
check("M1 constant-coefficient superposition of even functions is even", np.allclose(s, s_neg))

# M2 L^2 projection onto even part kills odd functions (Monte Carlo quadrature with symmetric sampling)
o = odd_fn(X)
Pe = 0.5 * (o + odd_fn(-X))  # projection of o onto even functions: (o(x)+o(-x))/2
check(
    "M2 projection of an odd function onto the even subspace vanishes pointwise",
    np.max(np.abs(Pe)) < 1e-12,
)

# M3 function coefficients: xi_1 = xi_1 * 1 (1 even, xi_1 odd) -- the constant-coefficient premise is essential
ones = np.ones(len(X))
check(
    "M3b xi_1 = xi_1 * 1 holds identically (coefficient is odd, the basis function is even)",
    np.allclose(X[:, 0], X[:, 0] * ones),
)

# M4 parity of products
check(
    "M4a product of two odd functions is even",
    np.allclose(odd_fn(X) * odd_fn(X), odd_fn(-X) * odd_fn(-X)),
)
check(
    "M4b product of three odd functions is odd",
    np.allclose(odd_fn(X) * odd_fn(X) * odd_fn(X), -(odd_fn(-X) * odd_fn(-X) * odd_fn(-X))),
)

# M5 self-pairing vanishes
check(
    "M5 eps_{ab} xi^a xi^b = 0 for one doublet",
    np.max(np.abs(X[:, 0] * X[:, 1] - X[:, 1] * X[:, 0])) < 1e-15,
)

# M6 pairing of xi and eps xibar
Xb = np.conj(X)
eps_xibar = (eps @ Xb.T).T
pair = X[:, 0] * eps_xibar[:, 1] - X[:, 1] * eps_xibar[:, 0]
check(
    "M6a eps_{ab} xi^a (eps xibar)^b = -|xi|^2 = -1 (constant)", np.allclose(pair, -np.ones(len(X)))
)
check("M6b the spin-0 composite of two different doublets is nonzero", np.max(np.abs(pair)) > 0.5)

# M7 spin-0 composite is constant: no spin-1/2 dependence
check("M7 the spin-0 composite has zero variance (constant function)", np.var(pair) < 1e-20)

print("\nFAILS:", fails if fails else "none")
