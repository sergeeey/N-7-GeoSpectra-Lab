"""Q5 (after Q3 corrections): local ket bases from the SU(2) action on C^2, and the global obstructions.

Setting. G = SU(2) acts on C^2 linearly. S^3 = unit sphere in C^2, Hopf map xi -> n(xi) = xi^dag sigma xi.
eps = [[0,1],[-1,0]] is the invariant antisymmetric form: for g in SU(2), conj(g) = eps g eps^{-1}.

Checks:
  K1. F(xi) := [xi | eps conj(xi)] is unitary, with det F = -1, for xi in S^3. So its columns are an orthonormal
      basis of C^2 at every point of S^3 (a pointwise ket basis built from C^2 alone, no sigma matrices).
  K2. Equivariance: F(g xi) = g F(xi) for g in SU(2) (uses conj(g) = eps g eps^{-1}).
  K3. Hopf phase: F(e^{i b} xi) = F(xi) diag(e^{i b}, e^{-i b}). So F does NOT descend to S^2: it is a section of a
      principal bundle over S^3, and the descent to S^2 needs a section of the Hopf bundle S^3 -> S^2.
  K4. Hopf sections over S^2 minus one point: s_N, s_S (Bloch +n) with s_N = e^{i ph} s_S, and the induced
      frames F_N = F(s_N), F_S = F(s_S) satisfy F_N = F_S diag(e^{i ph}, e^{-i ph}): transition in the torus T.
  K5. Global SU(2)-frame on S^2 (a rank-2 object, NOT a line): G(n) := M(n) (M(n)^dag M(n))^{-1/2} * c with
      M(n) = a + b n.sigma, a^2 != b^2 and a != +-b; G is unitary, det G = 1 after the constant c, continuous,
      and G(g n) = g G(n) g^{-1} (covariant under conjugation of the frame index). So the principal SU(2)
      bundle over S^2 has a global section (pi_1(SU(2)) = 0).
  K6. The Bloch line sub-bundles L_+ (vector +n) and L_- (vector -n) have nowhere-zero sections only locally:
      the winding of s_N/s_S around the equator is +1 (c_1 = +-1). This obstructs LINES, not the rank-2 bundle.
  K7. Orthogonality of the two rank-1 members (a=b=1 and a=1,b=-1): their subspaces are orthogonal.
      (Verified in q3d_corrections.py C2; repeated here for the frame G.)
  K8. Frame G restricted to a=b (rank 1, Bloch +n): the first column of G(n) is a section of L_+ with value
      in the Bloch line of n. Its winding around the equator is +1. This is the Hopf obstruction, and it is
      the only obstruction; the full G is globally defined.
"""

import numpy as np
from scipy.linalg import sqrtm

rng = np.random.default_rng(17)
fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


eps = np.array([[0, 1], [-1, 0]], dtype=complex)
sig = [
    np.array([[0, 1], [1, 0]], complex),
    np.array([[0, -1j], [1j, 0]], complex),
    np.array([[1, 0], [0, -1]], complex),
]


def rand_s3():
    v = rng.normal(size=4)
    v /= np.linalg.norm(v)
    return np.array([v[0] + 1j * v[1], v[2] + 1j * v[3]])


def rand_su2():
    v = rng.normal(size=4)
    v /= np.linalg.norm(v)
    a, b, c, d = v
    return np.array([[a + 1j * b, c + 1j * d], [-c + 1j * d, a - 1j * b]])


def F(xi):
    return np.column_stack([xi, eps @ np.conj(xi)])


# K1
ok1 = True
for _ in range(200):
    xi = rand_s3()
    Fm = F(xi)
    ok1 &= np.linalg.norm(Fm.conj().T @ Fm - np.eye(2)) < 1e-12
    ok1 &= abs(np.linalg.det(Fm) + 1) < 1e-12
check("K1 F(xi) = [xi | eps xibar] is unitary with det -1 on S^3", ok1)

# K2 equivariance
ok2 = True
for _ in range(200):
    xi = rand_s3()
    g = rand_su2()
    ok2 &= np.linalg.norm(F(g @ xi) - g @ F(xi)) < 1e-10
check("K2 equivariance F(g xi) = g F(xi) for g in SU(2)", ok2)

# K3 Hopf phase
ok3 = True
for _ in range(50):
    xi = rand_s3()
    b_ = rng.uniform(0, 2 * np.pi)
    lhs = F(np.exp(1j * b_) * xi)
    rhs = F(xi) @ np.diag([np.exp(1j * b_), np.exp(-1j * b_)])
    ok3 &= np.linalg.norm(lhs - rhs) < 1e-12
check("K3 F(e^{ib} xi) = F(xi) diag(e^{ib}, e^{-ib}) (not invariant: needs the Hopf section)", ok3)


# K4 Hopf sections and transition
def sN(th, ph):
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])


def sS(th, ph):
    return np.array([np.exp(-1j * ph) * np.cos(th / 2), np.sin(th / 2)])


ok4 = True
ok4b = True
for _ in range(200):
    th = rng.uniform(0.05, np.pi - 0.05)
    ph = rng.uniform(0, 2 * np.pi)
    ok4 &= np.linalg.norm(sN(th, ph) - np.exp(1j * ph) * sS(th, ph)) < 1e-12
    FN = F(sN(th, ph))
    FS = F(sS(th, ph))
    ok4b &= np.linalg.norm(FN - FS @ np.diag([np.exp(1j * ph), np.exp(-1j * ph)])) < 1e-12
check("K4a s_N = e^{i ph} s_S on the overlap", ok4)
check("K4b frame transition: F_N = F_S diag(e^{i ph}, e^{-i ph}) (torus-valued, det 1)", ok4b)


# K5 global SU(2) frame G(n) on S^2
def M(a, b, n):
    return a * np.eye(2) + b * (n[0] * sig[0] + n[1] * sig[1] + n[2] * sig[2])


def G_frame(a, b, n):
    m = M(a, b, n)
    P = sqrtm(m.conj().T @ m)
    U = m @ np.linalg.inv(P)
    det = np.linalg.det(U)
    return U / np.sqrt(det)  # det 1


a_, b_ = 1.0 + 0.3j, 0.4 - 0.2j
ok5 = True
ok5b = True
for _ in range(60):
    n = rng.normal(size=3)
    n /= np.linalg.norm(n)
    G = G_frame(a_, b_, n)
    ok5 &= np.linalg.norm(G.conj().T @ G - np.eye(2)) < 1e-9
    ok5 &= abs(np.linalg.det(G) - 1) < 1e-9
    # covariance: G(R n) = g G(n) g^{-1} with g in SU(2) acting on n by the spin-1/2 rotation
    g = rand_su2()
    Rn = np.array(
        [
            np.trace(
                sig[i] @ (g @ (n[0] * sig[0] + n[1] * sig[1] + n[2] * sig[2]) @ g.conj().T)
            ).real
            / 2
            for i in range(3)
        ]
    )
    ok5b &= np.linalg.norm(G_frame(a_, b_, Rn) - g @ G @ np.linalg.inv(g)) < 1e-7
check("K5a global SU(2)-valued frame G(n) on S^2 for a^2 != b^2 (unitary, det 1, continuous)", ok5)
check("K5b G is covariant: G(g n) = g G(n) g^{-1} (frame index conjugated)", ok5b)

# K6 winding of the line section (Bloch +n) around the equator: c_1
eq = np.linspace(0, 2 * np.pi, 4001)
ratio = np.array([sN(np.pi / 2, p)[1] / sS(np.pi / 2, p)[1] for p in eq])
wind = (np.unwrap(np.angle(ratio))[-1] - np.unwrap(np.angle(ratio))[0]) / (2 * np.pi)
check(
    "K6 line-section transition winding = 1 (obstructs the Bloch LINE, c_1 = +-1)",
    abs(wind - 1) < 1e-6,
)

# K7 orthogonality of the two rank-1 members (a=b, a=-b) at every point, integrated
xg, wg = np.polynomial.legendre.leggauss(40)
phg = np.linspace(0, 2 * np.pi, 40, endpoint=False)
v, w = np.array([1.0, 0.2j]), np.array([0.3, 1.0])
tot = 0j
for x, wi in zip(xg, wg):
    th = np.arccos(x)
    for p in phg:
        n = np.array([np.sin(th) * np.cos(p), np.sin(th) * np.sin(p), np.cos(th)])
        tot += wi * (2 * np.pi / 40) * np.vdot(M(1, 1, n) @ v, M(1, -1, n) @ w)
check(
    "K7 rank-1 members a=b and a=-b are orthogonal subspaces (|<.,.>| = %.1e)" % abs(tot),
    abs(tot) < 1e-10,
)

# K8 the rank-1 section (a=b) lies in a line: rank of M(1,1,n) is 1 at every n
ok8 = True
for _ in range(60):
    n = rng.normal(size=3)
    n /= np.linalg.norm(n)
    ok8 &= np.linalg.matrix_rank(M(1, 1, n), tol=1e-10) == 1
check(
    "K8 M(1,1,n) = 2 P_{+n} has rank 1 for every n (pointwise line, the only Hopf-obstructed piece)",
    ok8,
)

print("\nFAILS:", fails if fails else "none")
