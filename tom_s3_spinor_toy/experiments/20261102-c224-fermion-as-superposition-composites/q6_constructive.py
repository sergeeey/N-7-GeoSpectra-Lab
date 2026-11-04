"""Q6 constructive test: can a fermion (odd function) be a constant-coefficient superposition of composites?

Fermion f^a := xi^a (odd under xi -> -xi). Identity on S^3: |xi|^2 = 1, hence
    xi^a = sum_b xi^a * xi^b * conj(xi^b)        (cubic composite of three odd factors: odd).
Checks:
  C1. Identity xi^a = sum_b xi^a xi^b conj(xi^b) holds on S^3 (uses |xi|=1; a geometric fact, not a fit).
  C2. Each cubic term xi^a xi^b conj(xi^b) is odd (parity of three odd factors).
  C3. Quadratic composites (two odd factors) are even: no constant combination of them equals xi^a.
      Test: the projection of xi^a onto the even subspace is zero (xi^a is orthogonal to all even functions),
      checked by averaging over antipodal pairs.
  C4. Control: the symmetric quadratic composite xi^a xi^b is spin-1 (3-dim span), not spin-1/2.
"""
import numpy as np

rng = np.random.default_rng(79)
fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


def rand_s3(n):
    v = rng.normal(size=(n, 4))
    v /= np.linalg.norm(v, axis=1)[:, None]
    return np.column_stack([v[:, 0] + 1j * v[:, 1], v[:, 2] + 1j * v[:, 3]])


X = rand_s3(5000)
C = np.conj(X)
ok1 = True
ok2 = True
for a in range(2):
    rhs = sum(X[:, a] * X[:, b] * C[:, b] for b in range(2))
    ok1 &= np.allclose(rhs, X[:, a])
    for b in range(2):
        term = X[:, a] * X[:, b] * C[:, b]
        ok2 &= np.allclose((-X[:, a]) * (-X[:, b]) * (-C[:, b]), -term)  # odd: f(-x) = -f(x)
check("C1 xi^a = sum_b xi^a xi^b conj(xi^b) on S^3 (|xi|^2 = 1)", ok1)
check("C2 each cubic composite xi^a xi^b conj(xi^b) is odd", ok2)

# C3: projection onto even functions of xi^a is zero
ok3 = True
for a in range(2):
    f = X[:, a]
    fneg = (-X)[:, a]
    proj_even = 0.5 * (f + fneg)
    ok3 &= np.max(np.abs(proj_even)) < 1e-12
check("C3 the even part of each fermion xi^a vanishes: no composite of two fermions reproduces it", ok3)

# C4: symmetric quadratic composites span 3 dims (spin 1)
comp = np.column_stack([X[:, 0] ** 2, X[:, 0] * X[:, 1], X[:, 1] ** 2])
check("C4 quadratic composites xi^a xi^b span a 3-dim space (spin 1, integer)",
      np.linalg.matrix_rank(comp, tol=1e-9) == 3)

print("\nFAILS:", fails if fails else "none")
