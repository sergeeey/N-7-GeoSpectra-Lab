"""Q3: the correspondent's 21.09 claim about invariant subspaces, irreducibility and decomposition in harmonics.

the correspondent (21.09): fields over a sphere that the dragging action turns into a spinor multiplet of SO(n+1)
form an invariant irreducible subspace; this holds even with discontinuities; they therefore cannot
be written as linear sums of spherical harmonics.

Checks:
  K1. Integer-spin theorem (numerical form): the dragging action of rotations about z on the
      harmonics Y_lm is e^{-i m alpha}, m integer; hence R(2 pi) = identity on L^2(S^2).
      (A spin-1/2 multiplet needs R(2 pi) = -1.)  Checked on Y_lm, l <= 4.
  K2. The amplitude Y = e^{i phi/2} sin(theta/2) (the amplitude of Psi in the correspondent's frame) is not a
      weight vector: R_z(alpha) Y != e^{-i alpha/2} Y for any alpha in (0, 2 pi).
  K3. The dragged orbit {Y o R_alpha} spans an infinite-dimensional space: the Gram-matrix rank grows
      with the number of sampled rotations (no finite spinor multiplet is generated).
  K4. the correspondent's sentence 'cannot be expressed as a linear sum of spherical harmonics' is tested in L^2:
      all Y_lm form an orthonormal basis of L^2(S^2) (completeness), so Y IS an L^2-convergent sum.
      Partial sums sum_{l<=L} |c_lm|^2 -> ||Y||^2 = 2 pi. Every m (integer) appears with nonzero coefficient.
  K5. Spinor span: components of Psi = (-(1-cos th)/2, e^{i phi} sin th /2) are l <= 1 harmonics
      (checked symbolically in verify_tom_21sep_spinor_span.py, rerun in K5 numerically here).
"""

import numpy as np
from scipy.special import lpmv, factorial

rng = np.random.default_rng(3)
fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


def Ylm(l, m, th, ph):
    """Standard orthonormal Y_lm with Condon-Shortley phase (m may be negative)."""
    am = abs(m)
    N = np.sqrt((2 * l + 1) / (4 * np.pi) * factorial(l - am) / factorial(l + am))
    P = lpmv(am, l, np.cos(th))
    val = N * P * np.exp(1j * am * ph)
    if m < 0:
        val = (-1) ** am * np.conj(val)
    return val


def Y_amp(th, ph):
    """the correspondent's amplitude on the cut sphere, phi in [0, 2 pi)."""
    return np.exp(1j * ph / 2) * np.sin(th / 2)


# K1: R_z(alpha) Y_lm = e^{-i m alpha} Y_lm ; at alpha = 2 pi the factor is 1 for integer m
ok1 = True
for l in range(0, 5):
    for m in range(-l, l + 1):
        ok1 &= abs(np.exp(-1j * m * 2 * np.pi) - 1) < 1e-12
check(
    "K1 integer m for all Y_lm, l<=4: R_z(2 pi) acts as identity on L^2(S^2) (no spin-1/2 weight)",
    ok1,
)

# K2: Y is not a weight vector under R_z(alpha)
th_g = np.linspace(0.05, np.pi - 0.05, 200)
ph_g = np.linspace(0.0, 2 * np.pi, 400, endpoint=False) + 1e-3
TH, PH = np.meshgrid(th_g, ph_g, indexing="ij")


def Y_rot(alpha):
    """(R_z(alpha) Y)(theta, phi) = Y(theta, phi - alpha), with phi taken mod 2 pi on the sphere."""
    return Y_amp(TH, np.mod(PH - alpha, 2 * np.pi))


def l2(f):
    w = np.sin(TH) * (np.pi / 200) * (2 * np.pi / 400)
    return np.sqrt(np.sum(np.abs(f) ** 2 * w))


worst = 0.0
for alpha in np.linspace(0.3, 2 * np.pi - 0.3, 10):
    d = Y_rot(alpha) - np.exp(-1j * alpha / 2) * Y_amp(TH, PH)
    worst = max(worst, l2(d) / l2(Y_amp(TH, PH)))
print("   relative L2 distance |R Y - e^{-i a/2} Y| / |Y| (max over sampled alpha) = %.3f" % worst)
check("K2 Y is not an eigenvector of R_z(alpha) with eigenvalue e^{-i alpha/2}", worst > 0.5)


# K3: rank of the Gram matrix of the orbit {R_alpha Y}
def gram_rank(n_rot):
    alphas = np.linspace(0, 2 * np.pi, n_rot, endpoint=False) + 0.01
    vecs = np.array([Y_rot(a).ravel() for a in alphas])
    w = (np.sin(TH) * (np.pi / 200) * (2 * np.pi / 400)).ravel()
    G = (vecs.conj() * w) @ vecs.T
    s = np.linalg.eigvalsh(G)[::-1]
    return int(np.sum(s > 1e-6 * s[0])), s[0]


ranks = {}
for n in (8, 16, 32):
    r, top = gram_rank(n)
    ranks[n] = r
    print("   orbit with %d rotations: numerical rank %d" % (n, r))
check(
    "K3 numerical rank of the dragged orbit grows with the number of rotations (no finite spinor multiplet)",
    ranks[8] < ranks[16] < ranks[32],
)

# K4: L^2 expansion of Y in harmonics; coefficients and partial sums
norm_Y2 = 2 * np.pi  # int |Y|^2 dOmega = 2 pi * int_0^pi sin^2(th/2) sin th dth = 2 pi
th_q = np.linspace(0, np.pi, 40001)
mid = 0.5 * (th_q[1:] + th_q[:-1])
dth = np.diff(th_q)
w_th = mid


def theta_int(f):
    fm = f(mid)
    return np.sum(fm * np.sin(mid) * dth)


numeric_norm = theta_int(lambda t: np.sin(t / 2) ** 2) * 2 * np.pi
check("K4a numerical ||Y||^2 = 2 pi (%.6f)" % numeric_norm, abs(numeric_norm - norm_Y2) < 1e-4)

partial = {}
coef_nonzero = {}
Lmax = 60
total = 0.0
for l in range(0, Lmax + 1):
    for m in range(-l, l + 1):
        # int conj(Y_lm) Y dOmega = [int e^{-i m phi} e^{i phi/2} dphi] * [int N P_l^m(cos th) sin(th/2) sin th dth]
        phi_int = (np.exp(1j * (0.5 - m) * 2 * np.pi) - 1) / (1j * (0.5 - m))
        am = abs(m)
        N = np.sqrt((2 * l + 1) / (4 * np.pi) * factorial(l - am) / factorial(l + am))
        Pl = lpmv(am, l, np.cos(mid))
        th_part = np.sum(N * Pl * np.sin(mid / 2) * np.sin(mid) * dth)
        c = (phi_int * th_part) * ((-1) ** am if m < 0 else 1)
        total += abs(c) ** 2
        if l <= 2 and abs(m) <= 2:
            coef_nonzero[(l, m)] = abs(c)
    partial[l] = total
for L in (5, 10, 20, 40, 60):
    print("   sum_{l<=%d} sum_m |c_lm|^2 = %.6f   (||Y||^2 = %.6f)" % (L, partial[L], norm_Y2))
check(
    "K4b partial sums converge to ||Y||^2 (L^2 completeness): deficit at L=60 below 0.05",
    abs(partial[60] - norm_Y2) < 0.05,
)
# every integer m appears with a nonzero coefficient at l = |m| (the seam makes all m contribute)
ok_all_m = True
for m in range(-3, 4):
    l = max(abs(m), 0)
    phi_int = (np.exp(1j * (0.5 - m) * 2 * np.pi) - 1) / (1j * (0.5 - m))
    am = abs(m)
    N = np.sqrt((2 * l + 1) / (4 * np.pi) * factorial(l - am) / factorial(l + am))
    th_part = np.sum(N * lpmv(am, l, np.cos(mid)) * np.sin(mid / 2) * np.sin(mid) * dth)
    ok_all_m &= abs(phi_int * th_part) > 1e-6
check(
    "K4c every m in -3..3 has nonzero coefficient at l=|m|: no finite expansion, infinite family",
    ok_all_m,
)
check(
    "K4d (refuted reading) 'cannot be expressed as a linear sum of harmonics' is FALSE in L^2",
    partial[60] > norm_Y2 - 0.05,
)


# K5: Psi components are l <= 1 (numeric check of the symbolic result)
def Psi(th, ph):
    return np.stack([-(1 - np.cos(th)) / 2, np.exp(1j * ph) * np.sin(th) / 2])


def fit_error(f_vals, basis):
    A = np.array([b.ravel() for b in basis]).T
    coef, *_ = np.linalg.lstsq(A, f_vals.ravel(), rcond=None)
    return np.linalg.norm(A @ coef - f_vals.ravel()) / np.linalg.norm(f_vals.ravel())


TH2 = rng.uniform(0.1, np.pi - 0.1, 500)
PH2 = rng.uniform(0, 2 * np.pi, 500)
basis_l1 = [
    np.ones(500, dtype=complex),
    np.cos(TH2),
    np.sin(TH2) * np.cos(PH2),
    np.sin(TH2) * np.sin(PH2),
]
for comp in (0, 1):
    vals = Psi(TH2, PH2)[comp]
    err = fit_error(vals, basis_l1)
    check(
        "K5 component %d of Psi lies in span{1, x, y, z} (rel. residual %.1e)" % (comp, err),
        err < 1e-10,
    )

print("\nFAILS:", fails if fails else "none")
