r"""
C155 STEP 4b -- addendum forced by Step 4.

Step 4 falsified one sub-hypothesis of the mechanism story: M is NOT
C-linear per block (M(dir1) is not a complex multiple of M(dir0)), so the
image is NOT "one complex line" as claim.md first said. Two repairs to test:

  H-coh-odd : do the ODD directions (1,3,5) also map onto one common line,
              the way Step 4 showed the EVEN ones (0,2,4) do?
  H-plane   : is the TOTAL image exactly the real span of M(dir0), M(dir1),
              i.e. one 2-REAL-dimensional subspace shared by all 3 blocks?

If both hold, the corrected mechanism is: all three root planes map onto the
SAME real 2-plane (coherence), which is what forces rank 2 -- with no claim
that the 2-plane is a complex line.
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


S2 = load("c153_step2", "20260904-c153-nk-linearity-structural-derivation/c153_step2_exact_rational_verification.py")


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


stacked = sp.Matrix.vstack(S2.RHO_SIGMA[0], S2.RHO_SIGMA[1])
ns = stacked.nullspace()
v1 = ns[0]
v2 = sp.simplify(ns[1] - (hip(v1, ns[1]) / hip(v1, v1)) * v1)
b2 = sp.Matrix.hstack(v1 / sp.sqrt(hip(v1, v1)), v2 / sp.sqrt(hip(v2, v2)))
psi_p = None
for val, mult, vecs in sp.simplify(b2.conjugate().T * D8_of(S2.lc_vec) * b2).eigenvects():
    if sp.nsimplify(val) == 3:
        psi_p = sp.simplify(b2 * vecs[0])

fam = [S2.family_sym[:, k] for k in range(6)]
Ms = {k: sp.simplify(D8_of(fam[k]) * psi_p) for k in range(6)}

print("=" * 78)
print("H-coh-odd : do odd directions 1,3,5 share one line, as 0,2,4 do?")
print("-" * 78)
ref = Ms[1]
nz = [t for t in range(8) if sp.simplify(ref[t]) != 0]
ok_odd = True
for k in (3, 5):
    r = sp.simplify(Ms[k][nz[0]] / ref[nz[0]])
    same = sp.simplify(Ms[k] - r * ref) == sp.zeros(8, 1)
    print(f"  dir {k} vs dir 1: ratio = {sp.nsimplify(r)}   same line: {same}")
    ok_odd = ok_odd and same
print(f"  H-coh-odd holds: {ok_odd}")

print()
print("=" * 78)
print("H-plane : is the whole image the REAL span of M(dir0), M(dir1)?")
print("-" * 78)


def realvec(M):
    out = []
    for t in range(8):
        out.append(sp.re(M[t]))
        out.append(sp.im(M[t]))
    return sp.Matrix(out)


span2 = sp.Matrix.hstack(realvec(Ms[0]), realvec(Ms[1]))
print(f"  rank of span(M(dir0), M(dir1)) over R = {span2.rank()}")
full = sp.Matrix.hstack(*[realvec(Ms[k]) for k in range(6)])
print(f"  rank of span of ALL SIX images  over R = {full.rank()}")
same_space = full.rank() == span2.rank() == 2
print(f"  H-plane holds (all six live in that same real 2-plane): {same_space}")

print()
print("  is that 2-plane closed under multiplication by i (a complex line)?")
mult_i = sp.Matrix([[0, -1], [1, 0]])
iM0 = sp.zeros(16, 1)
for t in range(8):
    a, b = sp.re(Ms[0][t]), sp.im(Ms[0][t])
    ab = mult_i * sp.Matrix([a, b])
    iM0[2 * t], iM0[2 * t + 1] = ab[0], ab[1]
aug = sp.Matrix.hstack(span2, iM0)
print(f"  rank([M0 M1 | i*M0]) = {aug.rank()}  (2 => complex line, 3 => NOT)")
print(f"  the 2-plane IS a complex line: {aug.rank() == 2}")
