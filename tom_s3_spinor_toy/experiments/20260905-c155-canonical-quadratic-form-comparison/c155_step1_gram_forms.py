r"""
C155 STEP 1 -- the canonical, norm-choice-free comparison.

Instead of picking a matrix norm post hoc until 2/3 appears (the C154 trap),
compare the two CANONICAL Hermitian Gram matrices of the two LINEAR maps

    C : V -> Hom(dom, tgt)     C(v) = c(v)
    M : V -> Sigma             M(v) = D_Sigma(v) psi_+ / ||psi_+||

    G_c[a][b]  = tr( C(v_a)^H C(v_b) )      (Hilbert-Schmidt / trace pairing)
    G_mu[a][b] = < M(v_a), M(v_b) >         (spinor inner product)

on the SAME family basis. Proportionality G_c = k*G_mu is then a basis-free,
falsifiable statement (20 conditions on the SU(3)/T^2 6-dim family), not a
norm choice. See PREREGISTRATION.md for predictions P1/P2/P3 written first.

The normalisation gap found in C154 (flagged against C153) is closed here:
dom/tgt are Gram-Schmidt orthonormalised BEFORE any HS trace is taken, and
the raw-vs-corrected factor is printed, not assumed.

Run:  python c155_step1_gram_forms.py
"""

import importlib.util
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
EXP = HERE.parent


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, EXP / rel)
    assert spec and spec.loader
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


print("=" * 78)
print("C155 STEP 1  canonical Gram forms  G_c vs G_mu")
print("=" * 78)

S2 = load(
    "c153_step2",
    "20260904-c153-nk-linearity-structural-derivation/c153_step2_exact_rational_verification.py",
)
C147B = load(
    "c147b",
    "20260904-c147-connection-coefficient-zero-locus/c147b_exact_and_complex_structure.py",
)
R59 = C147B.R59
E6_sym = C147B.E_sym


def hip(a, b):
    return sp.simplify(sum(sp.conjugate(a[k]) * b[k] for k in range(a.rows)))


# ===========================================================================
# PART A -- S^6 POSITIVE CONTROL (pre-registered as VACUOUS; must pass)
# ===========================================================================
print()
print("=" * 78)
print("PART A  S^6 positive control -- P3.  Pre-registered as VACUOUS")
print("        (1-complex-dim family, so any two C-linear maps are")
print("        proportional). It must pass; passing is NOT evidence.")
print("=" * 78)

NOM_A, NOM_B = C147B.NOMIZU_A, C147B.NOMIZU_B
psi_p = R59.psi_plus()
psi_n2 = sp.simplify(R59.hip(psi_p, psi_p))


def C_s6(nd):
    """1x1 case: return the scalar, via C147b own exact machinery."""
    return C147B.c_exact_for(nd)


def M_s6(nd):
    """D_Sigma(nabla) psi_+ / ||psi_+||, the FULL vector (nothing discarded)."""
    D = sp.zeros(8, 1)
    for i in range(1, 7):
        nab_i = R59.spin_lift(nd[i], E6_sym)
        D += E6_sym[i] * (nab_i * psi_p)
    return sp.simplify(D / sp.sqrt(psi_n2))


s6_basis = [NOM_A, NOM_B]
Cs6 = [C_s6(nd) for nd in s6_basis]
Ms6 = [M_s6(nd) for nd in s6_basis]

Gc_s6 = sp.Matrix(2, 2, lambda a, b: sp.simplify(sp.conjugate(Cs6[a]) * Cs6[b]))
Gm_s6 = sp.Matrix(2, 2, lambda a, b: hip(Ms6[a], Ms6[b]))
print(f"  G_c  (S^6) = {Gc_s6.tolist()}")
print(f"  G_mu (S^6) = {Gm_s6.tolist()}")


# --- CORRECTION found BY this positive control (kept, not hidden) ----------
# First formalisation compared the FULL Hermitian Gram matrices and the
# control failed:  G_c had off-diagonal +-4i/3 while G_mu had 0.  That is a
# defect of the TEST, not of the geometry: the admissible family is a REAL
# vector space, so the quadratic form on it is  Q(v) = sum conj(v_a) G[a][b] v_b
# with REAL v, and the purely imaginary antisymmetric part of a Hermitian G
# cancels identically in that sum.  The canonical object to compare is
# therefore Re(G); Im(G) is a SEPARATE (symplectic) invariant, reported below
# on its own rather than silently dropped.
def re_part(G):
    return sp.Matrix(G.rows, G.cols, lambda a, b: sp.simplify(sp.re(G[a, b])))


def im_part(G):
    return sp.Matrix(G.rows, G.cols, lambda a, b: sp.simplify(sp.im(G[a, b])))


ReGc_s6, ReGm_s6 = re_part(Gc_s6), re_part(Gm_s6)
k_s6 = sp.simplify(ReGc_s6[0, 0] / ReGm_s6[0, 0])
prop_s6 = sp.simplify(ReGc_s6 - k_s6 * ReGm_s6) == sp.zeros(2, 2)
print(f"  Re(G_c)  = {ReGc_s6.tolist()}")
print(f"  Re(G_mu) = {ReGm_s6.tolist()}")
print(f"  Im(G_c)  = {im_part(Gc_s6).tolist()}   <- separate symplectic invariant")
print(f"  Im(G_mu) = {im_part(Gm_s6).tolist()}")
print(f"  k (from entry 0,0)            = {sp.nsimplify(k_s6)}")
print(f"  Re(G_c) == k * Re(G_mu)       : {prop_s6}")
print(f"  k == 4/9                      : {sp.simplify(k_s6 - sp.Rational(4, 9)) == 0}")
P3 = prop_s6 and sp.simplify(k_s6 - sp.Rational(4, 9)) == 0
print(f"  P3 (positive control) PASSES  : {P3}")
assert P3, "positive control failed -- BLOCKED-INFRASTRUCTURE, not evidence"

# ===========================================================================
# PART B -- SU(3)/T^2 : close the normalisation gap FIRST
# ===========================================================================
print()
print("=" * 78)
print("PART B  SU(3)/T^2 -- close the C153 Gram-Schmidt gap before any HS trace")
print("=" * 78)

dom_raw, tgt_raw = S2.dom_sym, S2.tgt_sym
Gd = sp.simplify(dom_raw.conjugate().T * dom_raw)
Gt = sp.simplify(tgt_raw.conjugate().T * tgt_raw)
print(f"  Gram(dom_raw) = {Gd.tolist()}")
print(f"  Gram(tgt_raw) = {Gt.tolist()}")
off_d = sp.simplify(Gd - sp.diag(*[Gd[i, i] for i in range(3)]))
print(f"  dom_raw already ORTHOGONAL (off-diagonal zero): {off_d == sp.zeros(3, 3)}")


def orthonormalise(B):
    out = []
    for j in range(B.cols):
        w = B[:, j]
        for u in out:
            w = w - (hip(u, B[:, j])) * u
        w = sp.simplify(w)
        out.append(sp.simplify(w / sp.sqrt(hip(w, w))))
    return sp.Matrix.hstack(*out)


dom_on = orthonormalise(dom_raw)
tgt_on = orthonormalise(tgt_raw)
ok_d = sp.simplify(dom_on.conjugate().T * dom_on - sp.eye(3)) == sp.zeros(3, 3)
ok_t = sp.simplify(tgt_on.conjugate().T * tgt_on - sp.eye(3)) == sp.zeros(3, 3)
print(f"  Gram(dom_on) == I : {ok_d}")
print(f"  Gram(tgt_on) == I : {ok_t}")
assert ok_d and ok_t

# ===========================================================================
# PART C -- psi_+ on SU(3)/T^2 (reuse the C154 Step B certified construction)
# ===========================================================================
print()
print("=" * 78)
print("PART C  psi_+ on SU(3)/T^2 (gate: must reproduce Stage 2a eigenvalue 3)")
print("=" * 78)

stacked = sp.Matrix.vstack(S2.RHO_SIGMA[0], S2.RHO_SIGMA[1])
inv_ns = stacked.nullspace()
assert len(inv_ns) == 2


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


v1 = inv_ns[0]
v2 = sp.simplify(inv_ns[1] - (hip(v1, inv_ns[1]) / hip(v1, v1)) * v1)
b2 = sp.Matrix.hstack(v1 / sp.sqrt(hip(v1, v1)), v2 / sp.sqrt(hip(v2, v2)))
D_LC_2 = sp.simplify(b2.conjugate().T * D8_of(S2.lc_vec) * b2)
psi_su3 = None
for val, mult, vecs in D_LC_2.eigenvects():
    if sp.nsimplify(val) == 3:
        psi_su3 = sp.simplify(b2 * vecs[0])
assert psi_su3 is not None
psi_su3_n2 = sp.simplify(hip(psi_su3, psi_su3))
_d = D8_of(S2.lc_vec) * psi_su3
mu_lc_check = sp.simplify(sp.sqrt(hip(_d, _d)) / sp.sqrt(psi_su3_n2))
print(f"  ||psi_+||^2 = {psi_su3_n2},  mu(LC) = {sp.nsimplify(mu_lc_check)}  (gate: 3)")
assert sp.simplify(mu_lc_check - 3) == 0

# ===========================================================================
# PART D -- the two canonical linear maps, and their Gram forms
# ===========================================================================
print()
print("=" * 78)
print("PART D  G_c and G_mu on the 6-dim family (the falsifiable comparison)")
print("=" * 78)

I6s = sp.eye(6)


def C_su3(vec):
    lam = lam_of(vec)
    D = sp.zeros(48, 48)
    for i in range(1, 7):
        D += S2.kron_sym(S2.E_sym[i] * S2.spin_lift_sym(lam[i]), I6s)
        D += S2.kron_sym(S2.E_sym[i], -lam[i])
    return sp.simplify(tgt_on.conjugate().T * D * dom_on)


def M_su3(vec):
    return sp.simplify(D8_of(vec) * psi_su3 / sp.sqrt(psi_su3_n2))


fam = [S2.family_sym[:, k] for k in range(6)]
Cs = [C_su3(v) for v in fam]
Ms = [M_su3(v) for v in fam]
print("  6 family directions pushed through both linear maps.")

Gc = sp.Matrix(6, 6, lambda a, b: sp.simplify((Cs[a].conjugate().T * Cs[b]).trace()))
Gm = sp.Matrix(6, 6, lambda a, b: hip(Ms[a], Ms[b]))

ReGc, ReGm = re_part(Gc), re_part(Gm)
ImGc, ImGm = im_part(Gc), im_part(Gm)


def show(name, G):
    print(f"  {name} =")
    for r in range(6):
        print("    " + "  ".join(f"{sp.nsimplify(G[r, c])!s:>9}" for c in range(6)))


print()
show("Re(G_c) ", ReGc)
show("Re(G_mu)", ReGm)
show("Im(G_c) ", ImGc)
show("Im(G_mu)", ImGm)

print()
print("=" * 78)
print("P1  is  Re(G_c) == k * Re(G_mu)  for a single scalar k ?")
print("=" * 78)
nz = [(a, b) for a in range(6) for b in range(6) if sp.simplify(ReGm[a, b]) != 0]
ks = {sp.simplify(ReGc[a, b] / ReGm[a, b]) for (a, b) in nz}
print(f"  distinct ratios over nonzero Re(G_mu) entries: {[sp.nsimplify(x) for x in ks]}")
bad0 = [
    (a, b)
    for a in range(6)
    for b in range(6)
    if sp.simplify(ReGm[a, b]) == 0 and sp.simplify(ReGc[a, b]) != 0
]
print(f"  entries where Re(G_mu)==0 but Re(G_c)!=0 : {bad0}")
proportional = len(ks) == 1 and not bad0
print(f"  PROPORTIONAL: {proportional}")
if proportional:
    kk = next(iter(ks))
    print(f"  k = {sp.nsimplify(kk)}    (S^6 gave 4/9)")
    print(f"  k == 4/9 EXACTLY : {sp.simplify(kk - sp.Rational(4, 9)) == 0}")
print(f"  P1 (NOT proportional), as predicted: {not proportional}")

print()
print("  --- diagnostics that survive either outcome ---")
print(f"  rank Re(G_c)  = {ReGc.rank()},  rank Re(G_mu) = {ReGm.rank()}")
print(f"  Re(G_c) diagonal  : {[sp.nsimplify(ReGc[i, i]) for i in range(6)]}")
print(f"  Re(G_mu) diagonal : {[sp.nsimplify(ReGm[i, i]) for i in range(6)]}")
diag_ratios = [
    sp.simplify(ReGc[i, i] / ReGm[i, i]) for i in range(6) if sp.simplify(ReGm[i, i]) != 0
]
print(f"  per-direction diagonal ratios : {[sp.nsimplify(x) for x in diag_ratios]}")
offc = [(a, b) for a in range(6) for b in range(6) if a != b and sp.simplify(ReGc[a, b]) != 0]
offm = [(a, b) for a in range(6) for b in range(6) if a != b and sp.simplify(ReGm[a, b]) != 0]
print(f"  nonzero OFF-diagonal of Re(G_c)  : {offc}")
print(f"  nonzero OFF-diagonal of Re(G_mu) : {offm}")

print()
print("=" * 78)
print("RAW-vs-CORRECTED normalisation factor (the C153 gap, quantified)")
print("=" * 78)
c_raw = S2.c_of_exact(S2.lc_vec)
c_on = C_su3(S2.lc_vec)
fro_raw = sp.sqrt(sum(sp.Abs(c_raw[r, c]) ** 2 for r in range(3) for c in range(3)))
fro_on = sp.sqrt(sum(sp.Abs(c_on[r, c]) ** 2 for r in range(3) for c in range(3)))
print(f"  ||c(LC)||_F raw (C153 basis)     = {sp.nsimplify(fro_raw)}")
print(f"  ||c(LC)||_F orthonormalised      = {sp.nsimplify(fro_on)}")
print(f"  correction factor raw/orthonorm  = {sp.nsimplify(sp.simplify(fro_raw / fro_on))}")
print(
    f"  |c(LC)|_F / mu(LC), corrected    = {sp.nsimplify(sp.simplify(fro_on / mu_lc_check))}"
    f"   -- this is sqrt(6)/3 = 0.816.., NOT 2/3 = 0.666..; ratio of the"
    f" SQUARED forms is {sp.nsimplify(sp.simplify(fro_on**2 / mu_lc_check**2))},"
    f" a DIFFERENT quantity from S^6's 4/9 -- do not conflate the two"
)
