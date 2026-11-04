"""Q5 (second pass): local ket bases, transitions, global obstructions.

Setting: the spinor fibre C^2 over S^2 with the Bloch map psi -> psi^dagger sigma psi / |psi|^2.
A 'local spinor basis' at a point is a continuous unit section psi(n) with psi^dagger sigma psi = n
(a section of the Hopf bundle S^3 -> S^2, up to the U(1) phase ambiguity).

Two standard charts:  s_N = (cos(th/2), e^{i ph} sin(th/2)) regular on S^2 minus S
                      s_S = (e^{-i ph} cos(th/2), sin(th/2)) regular on S^2 minus N

Checks:
  G1. s_N and s_S are unit sections with Bloch vector +n.
  G2. On the overlap s_N = e^{i ph} s_S: transition winding +1 around the equator (c_1 = +-1).
  G3. the correspondent's eta (17.10) = e^{-i ph/2} chi with chi = (-sin(th/2), e^{i ph} cos(th/2)) single-valued on S^2 minus N,
      with Bloch vector -n. So the half-integer seam behaviour of eta is a gauge factor e^{-i ph/2}, not topology.
  G4. Global obstruction (elementary): a global section sigma = lambda_N s_N = lambda_S s_S. Each lambda is a
      continuous U(1)-valued function on a disc (contractible), so its winding on the equator is 0,
      but lambda_N / lambda_S = e^{-i ph} has winding -1. Contradiction => no global nowhere-zero section.
      Numerically: winding of s_N/s_S along the equator equals 1 (computed), so the obstruction is nonzero.
  G5. Equivariant obstruction: the stabiliser of the north pole in SU(2) is U(1) = {diag(e^{-i a/2}, e^{i a/2})}
      acting on the fibre C^2. A nonzero SU(2)-equivariant global section would have a nonzero value at N
      fixed by the whole stabiliser; there is none (weights -1/2, +1/2 do not vanish). So no nonzero
      equivariant global section exists: no global SU(2)-covariant spinor basis.
      Numerically: the fixed subspace of the stabiliser action is {0}.

"""

import numpy as np

fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


sig = [
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
]


def bloch(v):
    v = v / np.linalg.norm(v)
    return np.array([np.vdot(v, s @ v).real for s in sig])


def npt(th, ph):
    return np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])


def sN(th, ph):
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])


def sS(th, ph):
    return np.array([np.exp(-1j * ph) * np.cos(th / 2), np.sin(th / 2)])


def eta(th, ph):
    return np.array([-np.exp(-1j * ph / 2) * np.sin(th / 2), np.exp(1j * ph / 2) * np.cos(th / 2)])


def chi(th, ph):
    return np.array([-np.sin(th / 2), np.exp(1j * ph) * np.cos(th / 2)])


rng = np.random.default_rng(9)
pts = [(rng.uniform(0.05, np.pi - 0.05), rng.uniform(0, 2 * np.pi)) for _ in range(200)]

# G1
e1 = max(np.linalg.norm(bloch(sN(t, p)) - npt(t, p)) for t, p in pts)
e2 = max(np.linalg.norm(bloch(sS(t, p)) - npt(t, p)) for t, p in pts)
check("G1 s_N and s_S have Bloch vector +n (max errors %.1e, %.1e)" % (e1, e2), max(e1, e2) < 1e-12)

# G2 transition
e_tr = max(np.linalg.norm(sN(t, p) - np.exp(1j * p) * sS(t, p)) for t, p in pts)
check("G2 s_N = e^{i ph} s_S on the overlap (max error %.1e)" % e_tr, e_tr < 1e-12)
eq = np.linspace(0, 2 * np.pi, 4001)
ratio = np.array([sN(np.pi / 2, p)[1] / sS(np.pi / 2, p)[1] for p in eq])
wind = (np.unwrap(np.angle(ratio))[-1] - np.unwrap(np.angle(ratio))[0]) / (2 * np.pi)
print("   winding of s_N/s_S around the equator = %.6f" % wind)
check("G2b transition winding is +1 (c_1 = +-1, nonzero)", abs(wind - 1) < 1e-6)

# G3 the correspondent's eta = e^{-i ph/2} chi, chi single valued, Bloch -n
e3 = max(np.linalg.norm(eta(t, p) - np.exp(-1j * p / 2) * chi(t, p)) for t, p in pts)
check("G3a eta = e^{-i ph/2} chi (max error %.1e)" % e3, e3 < 1e-12)
e4 = max(np.linalg.norm(chi(t, p) - chi(t, p + 2 * np.pi)) for t, p in pts)
check("G3b chi is single valued in ph (period 2 pi)", e4 < 1e-12)
e5 = max(np.linalg.norm(eta(t, p) + eta(t, p + 2 * np.pi)) for t, p in pts)
check(
    "G3c eta is antiperiodic (eta(ph+2pi) = -eta(ph)) -- the gauge factor is responsible",
    e5 < 1e-12,
)
e6 = max(np.linalg.norm(bloch(chi(t, p)) + npt(t, p)) for t, p in pts)
check("G3d chi has Bloch vector -n (max error %.1e)" % e6, e6 < 1e-12)

# G5 stabiliser fixed vectors
def spin_rot(alpha):
    return np.diag([np.exp(-1j * alpha / 2), np.exp(1j * alpha / 2)])


# fixed vectors of the whole stabiliser {spin_rot(alpha)}: solve (R(alpha) - 1) v = 0 for several alpha
A = np.vstack([spin_rot(a) - np.eye(2) for a in np.linspace(0.1, 4 * np.pi - 0.1, 17)])
rank = np.linalg.matrix_rank(A, tol=1e-10)
check(
    "G5 the stabiliser of N has no nonzero fixed vector in the fibre C^2 (rank %d = 2)" % rank,
    rank == 2,
)


print("\nFAILS:", fails if fails else "none")
