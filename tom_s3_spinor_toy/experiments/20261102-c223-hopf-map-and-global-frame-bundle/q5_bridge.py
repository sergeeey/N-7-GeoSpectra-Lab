"""Q5 bridge: global ket W = C^2_L (x) C^2_R (matrix entries g_ab on S^3 = SU(2)) -> local fibre E_rho over S^2.

Definitions. g(x) in SU(2) with first column x. SU(2)_L acts by left multiplication g -> h g (on S^3: x -> h x).
Right torus U(1)_R = {k_t = diag(t, conj t)} acts by g -> g k_t (Hopf fibre: x -> t x).
Local fibre: E_rho = S^3 x_{U(1)} C^2 with (t x, rho(t) v) ~ (x, v), rho(t) = diag(t, conj t).
Bridge: B_x(e_j) := [x, (row_j g(x))^T], i.e. the local vector is the j-th row of g(x) (evaluations of the ket functions).

Checks:
  B1. g(h x) = h g(x) for h in SU(2)  (left covariance of the matrix; the ket functions transform by left mult).
  B2. Covariance of B under SU(2)_L: B_{hx}(hbar e_j) = h . B_x(e_j), with h . [x,v] = [hx, v] (trivial fibre action),
      hbar = (h^T)^{-1}. Here M(h) = hbar is CONSTANT in x (this is the correct covariance test).
  B3. Descent: B_{t x}(e_j) = [x, rho(t)^{-1}...] -> the vector rho(t)*row_j(g) is the same class: well-definedness on S^2.
  B4. Full group over S^3: B_{xk}(e_j) = B_x(k^T e_j) for k in SU(2): fibre change by k^T (only the torus descends).
  B5. Sub-doublets: the subspace C^2_L (x) e (for a right line e) is U(1)_R-invariant iff e is an eigenline of diag(t,tbar),
      i.e. e in {e_1, e_2} (the Hopf poles of Q3). Checked on random e.
  B6. Earlier T3 test: M(h,x) = Phi(hx)^{-1} Phi(x) is NOT diagonal but constant in x. Check constancy.
"""
import numpy as np

rng = np.random.default_rng(83)
fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


def rand_su2():
    v = rng.normal(size=4)
    v /= np.linalg.norm(v)
    a, b, c, d = v
    return np.array([[a + 1j * b, c + 1j * d], [-c + 1j * d, a - 1j * b]])


def gx(x):
    return np.array([[x[0], -np.conj(x[1])], [x[1], np.conj(x[0])]])


def xof(g):
    return g[:, 0]


def rho(t):
    return np.diag([t, np.conj(t)])


# B1
ok1 = True
for _ in range(200):
    h = rand_su2()
    x = xof(rand_su2())
    ok1 &= np.linalg.norm(gx(h @ x) - h @ gx(x)) < 1e-10
check("B1 g(h x) = h g(x) (left covariance of the ket matrix)", ok1)

# B2 covariance with constant M(h) = (h^T)^{-1}
ok2 = True
for _ in range(200):
    h = rand_su2()
    g = rand_su2()
    x = xof(g)
    B_x = gx(x).T           # columns = frame vectors B_x(e_j) = row_j(g)
    B_hx = gx(h @ x).T
    M = np.linalg.inv(h.T)  # hbar
    # frame at hx applied to M e_j must equal the frame at x (trivial fibre action h.[x,v] = [hx,v])
    ok2 &= np.linalg.norm(B_hx @ M - B_x) < 1e-10
check("B2 B_{hx}(hbar e_j) = h . B_x(e_j): covariant with CONSTANT frame rep hbar (x-independent)", ok2)

# B3 descent: column vectors transform by rho under the torus
ok3 = True
for _ in range(200):
    g = rand_su2()
    t = np.exp(1j * rng.uniform(0, 2 * np.pi))
    g_t = gx(t * xof(g))
    ok3 &= np.linalg.norm(g_t.T - rho(t) @ g.T) < 1e-10
check("B3 B_{t x}(e_j) = rho(t) B_x(e_j): the class [x, B_x(e_j)] is well defined on S^2", ok3)

# B4 full-group action over S^3: right multiplication by k changes the fibre by k^T
ok4 = True
for _ in range(200):
    g = rand_su2()
    k = rand_su2()
    lhs = (g @ k).T
    rhs = k.T @ g.T
    ok4 &= np.linalg.norm(lhs - rhs) < 1e-10
check("B4 under right SU(2)_R: B -> k^T B (fibre change, descends only for the torus)", ok4)

# B5 sub-doublet invariance under the torus
ok5 = True
bad = 0
for _ in range(100):
    e = rng.normal(size=2) + 1j * rng.normal(size=2)
    e /= np.linalg.norm(e)
    t = np.exp(1j * 0.9)
    inv = np.linalg.norm(np.abs(rho(t) @ e) - np.abs(e)) < 1e-12 and np.linalg.norm(
        np.cross(rho(t) @ e, e)) < 1e-12 if False else None
    # invariance of the line C e under rho(t): rho(t) e parallel to e
    par = abs(np.vdot(e, rho(t) @ e)) / (np.linalg.norm(rho(t) @ e) * np.linalg.norm(e))
    if par < 1 - 1e-6:
        bad += 1
e1 = np.array([1, 0], dtype=complex)
e2 = np.array([0, 1], dtype=complex)
poles_ok = np.linalg.norm(rho(np.exp(0.9j)) @ e1 - np.exp(0.9j) * e1) < 1e-12 and np.linalg.norm(rho(np.exp(0.9j)) @ e2 - np.conj(np.exp(0.9j)) * e2) < 1e-12
check("B5 generic right lines are NOT torus-invariant (%d/100 not invariant); the poles e_1, e_2 are" % bad,
      bad > 90 and poles_ok)

# B6 constancy of M(h, x) = Phi(hx)^{-1} Phi(x) in x (Phi = gx^T)
ok6 = True
h = rand_su2()
Ms = []
for _ in range(20):
    x = xof(rand_su2())
    M = np.linalg.inv(gx(h @ x).T) @ gx(x).T
    Ms.append(M)
ok6 = all(np.linalg.norm(M - Ms[0]) < 1e-10 for M in Ms)
check("B6 M(h,x) = Phi(hx)^{-1} Phi(x) is constant in x (covariant); T3's off-diagonal test was the wrong criterion", ok6)

print("\nFAILS:", fails if fails else "none")
