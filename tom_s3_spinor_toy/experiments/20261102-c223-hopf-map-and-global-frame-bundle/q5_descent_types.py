"""Q5 critical: two frames, two equivariance types, and which one descends to a frame of E_rho over S^2.

E_rho = (S^3 x C^2) / ~ with [t xi, rho(t) v] ~ [xi, v], rho(t) = diag(t, conj t). A canonical vector of E_rho
over the point [xi] is the class [xi, v]. A frame F(xi) = (f_1, f_2) of E_rho is well defined over S^2 iff
[t xi, f_j(t xi)] = [xi, f_j(xi)] for all t, i.e. f_j(t xi) = rho(t) f_j(xi).

  F  (SU(2)-covariant on S^3):   columns f_j = F e_j with F = [xi | eps conj xi].
  Phi (sigma-free):              columns Phi e_j with Phi = [[xi1, xi2],[conj xi2, -conj xi1]].

Checks:
  T1. Phi descends: Phi(t xi) e_j = rho(t) Phi(xi) e_j  -> canonical vectors of E_rho.
  T2. F does NOT descend as a frame of E_rho: F(t xi) e_1 = t F(xi) e_1 (scalar multiple), but rho(t) != t*1.
      So the descended vector changes: [xi, rho(t)^{-1} t xi] != [xi, xi] for generic xi and t.
  T3. SU(2)_L acts on E_rho by [xi, v] -> [h xi, v] (well defined; fibre coordinates unchanged).
      Phi is NOT covariant under this action: M(h, xi) = Phi(h xi)^{-1} Phi(xi) is NOT diagonal in general.
      So Phi is a global frame of E_rho without SU(2)-covariance (consistent with the sigma-forced form, K-4).
"""
import numpy as np

rng = np.random.default_rng(67)
fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


def rand_s3():
    v = rng.normal(size=4)
    v /= np.linalg.norm(v)
    return np.array([v[0] + 1j * v[1], v[2] + 1j * v[3]])


def rand_su2():
    v = rng.normal(size=4)
    v /= np.linalg.norm(v)
    a, b, c, d = v
    return np.array([[a + 1j * b, c + 1j * d], [-c + 1j * d, a - 1j * b]])


eps = np.array([[0, 1], [-1, 0]], dtype=complex)


def Phi(x):
    return np.array([[x[0], x[1]], [np.conj(x[1]), -np.conj(x[0])]])


def F(x):
    return np.column_stack([x, eps @ np.conj(x)])


def rho(t):
    return np.diag([t, np.conj(t)])


def rho_inv(t):
    return np.diag([np.conj(t), t])


# T1
ok1 = True
for _ in range(200):
    x = rand_s3()
    t = np.exp(1j * rng.uniform(0, 2 * np.pi))
    for j in range(2):
        ok1 &= np.linalg.norm(Phi(t * x)[:, j] - rho(t) @ Phi(x)[:, j]) < 1e-12
check("T1 Phi descends: Phi(t xi) e_j = rho(t) Phi(xi) e_j", ok1)

# T2 F does not descend: the class [xi, v] with v = rho(t)^{-1} F(t xi) e_1
ok2 = True
gap = []
for _ in range(200):
    x = rand_s3()
    t = np.exp(1j * rng.uniform(0, 2 * np.pi))
    v = rho_inv(t) @ F(t * x)[:, 0]  # the vector representing [t xi, F(t xi)e_1] in the chart over xi
    gap.append(np.linalg.norm(v - F(x)[:, 0]))
check("T2 F does not descend: rho(t)^{-1}F(t xi)e_1 differs from F(xi)e_1 (median gap %.2f)" % np.median(gap),
      np.median(gap) > 0.1)

# T3 SU(2)_L covariance of the frame Phi on E_rho
offdiag = []
for _ in range(100):
    x = rand_s3()
    h = rand_su2()
    M = np.linalg.inv(Phi(h @ x)) @ Phi(x)
    offdiag.append(max(abs(M[0, 1]), abs(M[1, 0])))
check("T3 Phi is not SU(2)_L-covariant: frame change M(h,xi) has nonzero off-diagonal part (median %.2f)"
      % np.median(offdiag), np.median(offdiag) > 0.1)

print("\nFAILS:", fails if fails else "none")
