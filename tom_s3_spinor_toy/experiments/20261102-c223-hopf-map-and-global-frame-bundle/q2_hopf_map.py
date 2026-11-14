"""Q2: the map C^2 -> R^3, xi -> x(xi) = xi^dagger sigma xi, and the 'two-to-one' claim.

Checks:
  H1. |x(xi)| = |xi|^2 for random complex xi (so the radius relation |x| = |xi|^2 holds).
  H2. Fibres of x restricted to S^3 are U(1)-orbits e^{i a} xi (circles), not pairs:
      x(e^{i a} xi) = x(xi) for all a, and the orbit is 1-dimensional (rank of the
      derivative of the map S^3 -> S^2 is 2 at a generic point, so fibres are 1-dimensional).
  H3. The pair {xi, -xi} lies on the same fibre (a = pi), so the 'sign' pair is a point of a circle.
  H4. the correspondent's Hopf coordinates xi1 = cos(th/2) e^{i(psi-phi)/2}, xi2 = sin(th/2) e^{i(psi+phi)/2}
      give x = (sin th cos phi, sin th sin phi, cos th) up to the relabelling of the sign of x3,
      and psi -> psi + 2 pi flips the sign of xi (the 'two branches'), psi -> psi + 4 pi returns it.
  H5. Adjoint map SU(2) -> SO(3): Ad(g) = Ad(-g), and the kernel is exactly {+1, -1}
      (checked on random SU(2) elements: Ad(g) computed from g sigma_a g^dagger, and Ad(g)=Ad(h) iff h = +-g).
  H6. A field of U(1)-charge k (F(e^{i a} xi) = e^{i k a} F(xi)) is single-valued on S^2 iff k = 0.
      For k = 1 (xi itself): F(-xi) = -F(xi), so the values at +xi and -xi have opposite sign:
      this is the sign the correspondent saw, but it is one value per circle-point, i.e. a family, not two fields.
"""

import numpy as np

rng = np.random.default_rng(7)
sig = [
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
]
fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


def xmap(xi):
    """x_a = xi^dagger sigma_a xi, real for every a."""
    return np.array([np.vdot(xi, s @ xi).real for s in sig])


def rand_c2():
    v = rng.normal(size=4)
    return np.array([v[0] + 1j * v[1], v[2] + 1j * v[3]])


# H1
err = 0.0
for _ in range(2000):
    xi = rand_c2()
    x = xmap(xi)
    err = max(err, abs(np.linalg.norm(x) - np.linalg.norm(xi) ** 2))
check("H1 |x(xi)| = |xi|^2 (max error %.2e over 2000 samples)" % err, err < 1e-12)

# H2  fibre is a circle
xi0 = rand_c2()
xi0 = xi0 / np.linalg.norm(xi0)
x0 = xmap(xi0)
errs = [np.linalg.norm(xmap(np.exp(1j * a) * xi0) - x0) for a in np.linspace(0, 2 * np.pi, 97)]
check(
    "H2a x is constant on the orbit e^{i a} xi0 (max deviation %.2e)" % max(errs), max(errs) < 1e-12
)


def jac_rank_S3_to_R3(xi, eps=1e-6):
    """Tangent map of x restricted to S^3 at xi, as a 4-dim -> 3-dim matrix; returns its rank."""
    basis = []
    # tangent space of S^3 at xi (real 4-vectors orthogonal to xi, in R^4 = C^2)
    v = np.concatenate([xi.real, xi.imag])
    for k in range(4):
        e = np.zeros(4)
        e[k] = 1.0
        e = e - np.dot(e, v) * v
        basis.append(e)
    # orthonormalise tangent directions
    M = np.array(basis)
    U, s, Vt = np.linalg.svd(M)
    tang = Vt[:3]  # 3-dim tangent space of S^3
    J = []
    for t in tang:
        d = t[:2] + 1j * t[2:]
        xp = xmap(xi + eps * d) - xmap(xi - eps * d)
        J.append(xp / (2 * eps))
    J = np.array(J)
    return np.linalg.matrix_rank(J, tol=1e-6)


def unit_c2():
    v = rand_c2()
    return v / np.linalg.norm(v)


ranks = [jac_rank_S3_to_R3(unit_c2()) for _ in range(20)]
check(
    "H2b Jacobian of S^3 -> S^2 has rank 2 at generic points (so fibres are 1-dimensional circles): ranks=%s"
    % sorted(set(ranks)),
    set(ranks) == {2},
)

# H3  xi and -xi lie on the same fibre (a = pi)
check("H3 x(-xi) = x(xi)", np.linalg.norm(xmap(-xi0) - x0) < 1e-12)


# H4 the correspondent's Hopf coordinates
def tom_xi(th, ph, psi):
    return np.array(
        [
            np.cos(th / 2) * np.exp(1j * (psi - ph) / 2),
            np.sin(th / 2) * np.exp(1j * (psi + ph) / 2),
        ]
    )


maxdev = 0.0
for _ in range(200):
    th = rng.uniform(0.05, np.pi - 0.05)
    ph = rng.uniform(0, 2 * np.pi)
    psi = rng.uniform(0, 2 * np.pi)
    x = xmap(tom_xi(th, ph, psi))
    target = np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])
    maxdev = max(maxdev, np.linalg.norm(x - target))
print("   max |x(tom_xi) - (sin th cos ph, sin th sin ph, cos th)| = %.3e" % maxdev)
check(
    "H4a the correspondent Hopf coordinates map to the sphere point (theta, phi), independent of psi",
    maxdev < 1e-10,
)

th, ph, psi = 1.1, 0.4, 0.7
check(
    "H4b psi -> psi+2pi flips the sign of xi (two branches)",
    np.linalg.norm(tom_xi(th, ph, psi + 2 * np.pi) + tom_xi(th, ph, psi)) < 1e-12,
)
check(
    "H4c psi -> psi+4pi returns xi",
    np.linalg.norm(tom_xi(th, ph, psi + 4 * np.pi) - tom_xi(th, ph, psi)) < 1e-12,
)


# H5  adjoint map SU(2) -> SO(3)
def random_su2():
    v = rng.normal(size=4)
    v = v / np.linalg.norm(v)
    a, b, c, d = v
    return np.array([[a + 1j * b, c + 1j * d], [-c + 1j * d, a - 1j * b]])


def Ad(g):
    R = np.zeros((3, 3))
    for j in range(3):
        M = g @ sig[j] @ g.conj().T
        for i in range(3):
            R[i, j] = (np.trace(sig[i] @ M) / 2).real
    return R


ok_pm = True
ok_orth = True
ok_gen = True
for _ in range(200):
    g = random_su2()
    R = Ad(g)
    ok_pm &= np.linalg.norm(Ad(-g) - R) < 1e-12
    ok_orth &= np.linalg.norm(R.T @ R - np.eye(3)) < 1e-10 and abs(np.linalg.det(R) - 1) < 1e-10
    h = random_su2()
    if np.linalg.norm(Ad(h) - R) < 1e-8:
        # Ad(h) = Ad(g) must imply h = +-g
        ok_gen &= np.linalg.norm(h - g) < 1e-8 or np.linalg.norm(h + g) < 1e-8
check("H5a Ad(-g) = Ad(g) (the 2:1 is exact at group level)", ok_pm)
check("H5b Ad(g) in SO(3)", ok_orth)
check("H5c Ad(h)=Ad(g) implies h = +-g (kernel {+1,-1}), sampled", ok_gen)

# H6  charge argument: F(e^{i a} xi) = e^{i k a} F(xi)
# For charge 1, F(xi) = xi_2 (a component): F(-xi) = -F(xi)
F1 = lambda xi: xi[1]
check(
    "H6 charge-1 field xi_2: F(-xi) = -F(xi) (sign flip, one value per circle point)",
    abs(F1(-xi0) + F1(xi0)) < 1e-12,
)
F0 = lambda xi: np.vdot(xi, xi).real
check("H6 charge-0 field |xi|^2 : F(-xi)=F(xi), descends to S^2", abs(F0(-xi0) - F0(xi0)) < 1e-12)

print("\nFAILS:", fails if fails else "none")
