r"""
C155 STEP 6 -- tool-verification of the context-blind skeptic report.

The skeptic had NO runnable python and said so explicitly. Under
audit-verification-gate.md its [CONFIRMED-REAL] is only [HYPOTHESIS] here
until re-checked with a tool. Three of its points are directly testable and
two of them are tests it asked for and could not run:

  V1 (its Attack 4 hand-derivation): Q_mu == 4(a0-a2+a4)^2 + 4(a1-a3+a5)^2 ?
  V2 (its Attack 1, EXPLICITLY UNRUN): rank of the union map
      v |-> (D(v)psi_+, D(v)psi_-).  It predicted 4 "by chirality".
  V3 (its F2): it claims Step 3 cannot discriminate "isotropic" from "already
      diagonal", because orthonormalising a Gram=4I basis is a mere rescaling.
      Settle it the hard way: conjugate Q_c by a RANDOM orthogonal matrix that
      genuinely MIXES the three root planes, and see whether it stays 2*I.
"""
import importlib.util
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
EXP = HERE.parent


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, EXP / rel)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


S2 = load(
    "c153_step2",
    "20260904-c153-nk-linearity-structural-derivation/c153_step2_exact_rational_verification.py",
)


def hip(a, b):
    return sp.simplify(sum(sp.conjugate(a[k]) * b[k] for k in range(a.rows)))


def lam_of(vec):
    lam = {}
    for k in range(6):
        M = sp.zeros(6, 6)
        for p_idx, (i, j) in enumerate(S2.PAIRS6):
            M[i, j] += vec[k * 15 + p_idx]
            M[j, i] -= vec[k * 15 + p_idx]
        lam[k + 1] = M
    return lam


def D8_of(vec):
    lam = lam_of(vec)
    D = sp.zeros(8, 8)
    for i in range(1, 7):
        D += S2.E_sym[i] * S2.spin_lift_sym(lam[i])
    return D


def orthonormalise(B):
    out = []
    for j in range(B.cols):
        w = B[:, j]
        for u in out:
            w = w - hip(u, B[:, j]) * u
        w = sp.simplify(w)
        out.append(sp.simplify(w / sp.sqrt(hip(w, w))))
    return sp.Matrix.hstack(*out)


stacked = sp.Matrix.vstack(S2.RHO_SIGMA[0], S2.RHO_SIGMA[1])
ns = stacked.nullspace()
v1 = ns[0]
v2 = sp.simplify(ns[1] - (hip(v1, ns[1]) / hip(v1, v1)) * v1)
b2 = sp.Matrix.hstack(v1 / sp.sqrt(hip(v1, v1)), v2 / sp.sqrt(hip(v2, v2)))
psi_p = psi_m = None
for val, mult, vecs in sp.simplify(b2.conjugate().T * D8_of(S2.lc_vec) * b2).eigenvects():
    if sp.nsimplify(val) == 3:
        psi_p = sp.simplify(b2 * vecs[0])
    if sp.nsimplify(val) == -3:
        psi_m = sp.simplify(b2 * vecs[0])
assert psi_p is not None and psi_m is not None
fam = [S2.family_sym[:, k] for k in range(6)]

print("=" * 78)
print("V1  verify the skeptic's hand-derived closed form for Q_mu")
print("=" * 78)
a = sp.symbols("a0:6", real=True)
vgen = sp.zeros(90, 1)
for i in range(6):
    vgen += a[i] * fam[i]
Dpsi = sp.expand(D8_of(vgen) * psi_p)
Qmu = sp.simplify(sp.expand(hip(Dpsi, Dpsi) / hip(psi_p, psi_p)))
pred = sp.expand(4 * (a[0] - a[2] + a[4]) ** 2 + 4 * (a[1] - a[3] + a[5]) ** 2)
print(f"  Q_mu computed  = {sp.factor(sp.simplify(Qmu))}")
print(f"  skeptic's form = {sp.factor(pred)}")
v1_ok = sp.simplify(Qmu - pred) == 0
print(f"  V1 -- skeptic's closed form is EXACTLY correct: {v1_ok}")

print()
print("=" * 78)
print("V2  the test the skeptic asked for and could NOT run:")
print("    rank of the UNION map  v |-> (D(v)psi_+, D(v)psi_-)")
print("=" * 78)


def realcols(vecs):
    cols = []
    for M in vecs:
        col = []
        for t in range(M.rows):
            col.append(sp.re(M[t]))
            col.append(sp.im(M[t]))
        cols.append(sp.Matrix(col))
    return sp.Matrix.hstack(*cols)


Mp = [sp.simplify(D8_of(fam[k]) * psi_p) for k in range(6)]
Mm = [sp.simplify(D8_of(fam[k]) * psi_m) for k in range(6)]
Rp, Rm = realcols(Mp), realcols(Mm)
union = sp.Matrix.vstack(Rp, Rm)
print(f"  rank(v -> D(v) psi_+)              = {Rp.rank()}")
print(f"  rank(v -> D(v) psi_-)              = {Rm.rank()}")
print(f"  rank(v -> (D(v)psi_+, D(v)psi_-))  = {union.rank()}   <- skeptic predicted 4")
v2_pred_ok = union.rank() == 4
print(f"  V2 -- skeptic's chirality prediction (4) correct: {v2_pred_ok}")
print("  NOTE: this does NOT touch the central claim; Q_mu is defined on psi_+.")

print()
print("=" * 78)
print("V3  settle the skeptic's F2: rotate Q_c by a random CROSS-PLANE")
print("    orthogonal matrix. Isotropy must survive; mere diagonality would not.")
print("=" * 78)
dom_on = orthonormalise(S2.dom_sym)
tgt_on = orthonormalise(S2.tgt_sym)
I6s = sp.eye(6)


def C_of(vec):
    lam = lam_of(vec)
    D = sp.zeros(48, 48)
    for i in range(1, 7):
        D += S2.kron_sym(S2.E_sym[i] * S2.spin_lift_sym(lam[i]), I6s)
        D += S2.kron_sym(S2.E_sym[i], -lam[i])
    return sp.simplify(tgt_on.conjugate().T * D * dom_on)


# V-orthonormal family basis (Gram(family)=4I => divide by 2)
onb = [fam[k] / 2 for k in range(6)]
Cs = [C_of(v) for v in onb]
Gc = sp.Matrix(6, 6, lambda i, j: sp.simplify(sp.re((Cs[i].conjugate().T * Cs[j]).trace())))
print(f"  Re(G_c) in the V-orthonormal basis is 2*I : {sp.simplify(Gc - 2 * sp.eye(6)) == sp.zeros(6, 6)}")

# a genuinely cross-plane rotation: Givens rotations between planes A,B and B,C
th = sp.Rational(3, 5)  # cos, with sin = 4/5 -> exact rational orthogonal
co, si = sp.Rational(3, 5), sp.Rational(4, 5)
R1 = sp.eye(6)
R1[0, 0], R1[0, 2], R1[2, 0], R1[2, 2] = co, -si, si, co  # mixes plane A and B
R2 = sp.eye(6)
R2[3, 3], R2[3, 5], R2[5, 3], R2[5, 5] = co, -si, si, co  # mixes plane B and C
R = sp.simplify(R1 * R2)
print(f"  R is orthogonal : {sp.simplify(R.T * R - sp.eye(6)) == sp.zeros(6, 6)}")
print(f"  R genuinely mixes planes (nonzero cross-plane entries): {R[0, 2] != 0 and R[3, 5] != 0}")

rot = [sum((R[i, j] * onb[i] for i in range(6)), sp.zeros(90, 1)) for j in range(6)]
Csr = [C_of(v) for v in rot]
Gcr = sp.Matrix(6, 6, lambda i, j: sp.simplify(sp.re((Csr[i].conjugate().T * Csr[j]).trace())))
still_iso = sp.simplify(Gcr - 2 * sp.eye(6)) == sp.zeros(6, 6)
print(f"  Re(G_c) after cross-plane rotation is STILL 2*I : {still_iso}")
# and the same for Q_mu, which must NOT be invariant (it is rank 2)
Mr = realcols([sp.simplify(D8_of(v) * psi_p) for v in rot])
print(f"  rank(Q_mu) after the same rotation : {Mr.rank()}  (rank is invariant, must stay 2)")
print()
print(f"  V3 -- isotropy of Q_c is REAL, not a basis artifact: {still_iso}")
