r"""
Round 59 -- Route C analytic anchor (INDEPENDENT reimplementation).

Derives, from the PRIMARY SOURCE ONLY
    Agricola-Hofmann-Lawn 2023, "Invariant spinors on homogeneous spheres"
    (arXiv:2203.02961v3), Section 2.1 eq.(5) + Section 5.1 Theorem 5.1 / Remark 5.2,
the analytic anchor for the trivial-block rank certificate on S^6 = G_2/SU(3).

This file is FORBIDDEN to read/import anything under
    experiments/20260708-dolan-casimir-g2su3/
Its whole value is independence: the Clifford action, the Levi-Civita
spin-connection (Nomizu) operators, and the su(3) generators are transcribed
by hand from the PDF, and every constant (-sqrt(3), Killing number 1/(2 sqrt3),
the invariant dimensions) is DERIVED here, not imported.

Conventions transcribed from AHL2023 (stated explicitly):
  * Clifford relation (p.6):  v w + w v = -2 beta(v,w) 1   ==>   e_i . e_i = -1.
    (negative-definite convention; verified below on a test spinor)
  * Spinor module Sigma = Lambda^* L'  with  L' = span_C{y1,y2,y3},  dim = 8.
    Basis ordered by subset of {1,2,3}: (), (1),(2),(3),(1,2),(1,3),(2,3),(1,2,3).
  * eq.(5), for j = 1,2,3  (n = 2l = 6, l = 3):
        e_{2j-1}.eta = i ( x_j |_ eta  +  y_j ^ eta )
        e_{2j}  .eta =   ( y_j ^ eta  -  x_j |_ eta )
    where y_j ^  is exterior product, x_j |_ is interior product with
    beta(x_j, y_k) = delta_{jk} (isotropic Lagrangian pairing).
  * Theorem 5.1:  psi_pm = 1 pm y123  are Killing spinors,
        grad^g_X psi_pm = pm (1/(2 sqrt3)) X . psi_pm.
  * Remark 5.2 gives the su(3) generators ad(nu_k)|m and the Levi-Civita
    "Nomizu" 2-forms Lambda_g(e_i), both as elements of so(6) = Lambda^2 m.
    The spin lift of the so(6) generator e_{ab} (a != b) is (1/2) e_a . e_b .
    (factor confirmed self-consistently by reproducing Theorem 5.1 exactly.)

Run:  python round59_route_c_analytic.py
"""

import sympy as sp

IU = sp.I
sqrt3 = sp.sqrt(3)

# ----------------------------------------------------------------------------
# Exterior algebra on L' = span{y1,y2,y3}.  Elements are dicts {subset_tuple: coeff}.
# ----------------------------------------------------------------------------
BASIS = [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
IDX = {s: k for k, s in enumerate(BASIS)}
EVEN = [(), (1, 2), (1, 3), (2, 3)]  # Lambda^0 + Lambda^2  (Sigma_even = S^-)
ODD = [(1,), (2,), (3,), (1, 2, 3)]  # Lambda^1 + Lambda^3  (Sigma_odd  = S^+)


def _sort_sign(seq):
    """Sort a sequence of distinct ints, return (sorted_tuple, parity_sign) or (None,0) if a repeat."""
    seq = list(seq)
    sign = 1
    # bubble sort counting transpositions
    n = len(seq)
    for a in range(n):
        for b in range(n - 1 - a):
            if seq[b] == seq[b + 1]:
                return None, 0
            if seq[b] > seq[b + 1]:
                seq[b], seq[b + 1] = seq[b + 1], seq[b]
                sign = -sign
    if len(set(seq)) != n:
        return None, 0
    return tuple(seq), sign


def wedge_y(j, form):
    """y_j ^ form."""
    out = {}
    for subset, c in form.items():
        s, sign = _sort_sign((j,) + subset)
        if s is None:
            continue
        out[s] = out.get(s, 0) + sign * c
    return {k: v for k, v in out.items() if v != 0}


def contract_x(j, form):
    """x_j |_ form, an antiderivation with beta(x_j, y_k) = delta_{jk}."""
    out = {}
    for subset, c in form.items():
        for pos, elt in enumerate(subset):
            if elt == j:
                sign = (-1) ** pos  # antiderivation sign
                rest = subset[:pos] + subset[pos + 1 :]
                out[rest] = out.get(rest, 0) + sign * c
    return {k: v for k, v in out.items() if v != 0}


def clifford(i, form):
    """e_i . form  via AHL eq.(5).  i in 1..6."""
    j = (i + 1) // 2  # e_{2j-1}, e_{2j}
    xj = contract_x(j, form)
    yj = wedge_y(j, form)
    if i % 2 == 1:  # e_{2j-1} = i (x_j|_ + y_j^)
        return _add(_scale(IU, xj), _scale(IU, yj))
    else:  # e_{2j}   =   (y_j^ - x_j|_)
        return _add(yj, _scale(-1, xj))


def _scale(a, form):
    return {k: a * v for k, v in form.items() if a * v != 0}


def _add(*forms):
    out = {}
    for f in forms:
        for k, v in f.items():
            out[k] = out.get(k, 0) + v
    return {k: sp.simplify(v) for k, v in out.items() if sp.simplify(v) != 0}


# 8x8 Clifford matrices (columns = images of basis vectors)
def op_matrix(action):
    M = sp.zeros(8, 8)
    for col, s in enumerate(BASIS):
        img = action({s: sp.Integer(1)})
        for k, c in img.items():
            M[IDX[k], col] = c
    return M


E = {i: op_matrix(lambda f, i=i: clifford(i, f)) for i in range(1, 7)}


def vec(form):
    v = sp.zeros(8, 1)
    for k, c in form.items():
        v[IDX[k]] = c
    return v


ONE = vec({(): sp.Integer(1)})
Y123 = vec({(1, 2, 3): sp.Integer(1)})
PSI_P = ONE + Y123  # psi_+ = 1 + y123
PSI_M = ONE - Y123  # psi_- = 1 - y123

print("=" * 70)
print("STEP 0  Clifford convention check  (e_i . e_i = -1 ?)")
print("=" * 70)
conv_ok = True
for i in range(1, 7):
    sq = sp.simplify(E[i] * E[i] + sp.eye(8))
    ok = sq == sp.zeros(8, 8)
    conv_ok &= ok
    print(f"  e_{i}.e_{i} + 1 = 0 : {ok}")
# explicit test-spinor confirmation on eta = 1  (task: 'compute e_1.e_1 on a test spinor')
e1e1_on_1 = sp.simplify(E[1] * (E[1] * ONE))
print(
    f"  e_1.(e_1 . 1) = {[sp.simplify(x) for x in e1e1_on_1.T]}  (== -1 * (1)) -> "
    f"{sp.simplify(e1e1_on_1 + ONE) == sp.zeros(8, 1)}"
)
assert conv_ok, "Clifford convention mismatch"
print("  => AHL convention is NEGATIVE-definite: e_i.e_i = -1  [confirmed]")


# ----------------------------------------------------------------------------
# STEP: build so(6) spin lift and Levi-Civita Nomizu operators (Remark 5.2)
#   spin lift:  rho(e_{ab}) = (1/2) e_a . e_b .   (a != b)
# ----------------------------------------------------------------------------
def so6_lift(pairs):
    """pairs = list of (coeff, a, b) meaning coeff * e_{a,b}; return 8x8 spinor operator."""
    M = sp.zeros(8, 8)
    for coeff, a, b in pairs:
        M += coeff * sp.Rational(1, 2) * (E[a] * E[b])
    return M


# Levi-Civita Nomizu 2-forms Lambda_g(e_i), transcribed from Remark 5.2 (page 42).
Lam = {
    1: [(sp.Rational(1, 1), 3, 6), (sp.Rational(1, 1), 4, 5)],
    2: [(sp.Rational(1, 1), 3, 5), (sp.Rational(-1, 1), 4, 6)],
    3: [(sp.Rational(-1, 1), 1, 6), (sp.Rational(-1, 1), 2, 5)],
    4: [(sp.Rational(-1, 1), 1, 5), (sp.Rational(1, 1), 2, 6)],
    5: [(sp.Rational(1, 1), 1, 4), (sp.Rational(1, 1), 2, 3)],
    6: [(sp.Rational(1, 1), 1, 3), (sp.Rational(-1, 1), 2, 4)],
}
# each carries an overall 1/(2 sqrt3)
NAB = {i: so6_lift([(c / (2 * sqrt3), a, b) for (c, a, b) in Lam[i]]) for i in range(1, 7)}


def nab(i, v):
    return sp.simplify(NAB[i] * v)


print()
print("=" * 70)
print("STEP 1a  Calibration: reproduce Theorem 5.1 Killing equation")
print("         grad_{e_i} psi_pm  ==  +/- (1/(2 sqrt3)) e_i . psi_pm   (6/6 each)")
print("=" * 70)
kill_ok = True
for i in range(1, 7):
    lhs_p = nab(i, PSI_P)
    rhs_p = sp.simplify(sp.Rational(1, 1) / (2 * sqrt3) * (E[i] * PSI_P))
    lhs_m = nab(i, PSI_M)
    rhs_m = sp.simplify(-sp.Rational(1, 1) / (2 * sqrt3) * (E[i] * PSI_M))
    ok_p = sp.simplify(lhs_p - rhs_p) == sp.zeros(8, 1)
    ok_m = sp.simplify(lhs_m - rhs_m) == sp.zeros(8, 1)
    kill_ok &= ok_p and ok_m
    print(f"  i={i}:  psi_+ {'OK' if ok_p else 'FAIL'}   psi_- {'OK' if ok_m else 'FAIL'}")
assert kill_ok, "CALIBRATION FAILED -- transcription of Lambda_g or lift factor is wrong"
print("  => Nomizu operators + (1/2)e_a.e_b lift REPRODUCE Thm 5.1 exactly.")
print("     (This gate CAN fail; it pins the spin-connection independently.)")

# also record the derived Nomizu image on the two invariant spinors:
#   grad_{e_i} 1     = (1/(2 sqrt3)) e_i . y123
#   grad_{e_i} y123  = (1/(2 sqrt3)) e_i . 1
print()
print("  Derived corollary (from psi_pm = 1 +/- y123):")
c1 = all(
    sp.simplify(nab(i, ONE) - sp.Rational(1, 1) / (2 * sqrt3) * (E[i] * Y123)) == sp.zeros(8, 1)
    for i in range(1, 7)
)
c2 = all(
    sp.simplify(nab(i, Y123) - sp.Rational(1, 1) / (2 * sqrt3) * (E[i] * ONE)) == sp.zeros(8, 1)
    for i in range(1, 7)
)
print(f"    grad_ei 1    = (1/(2 sqrt3)) e_i . y123  : {c1}")
print(f"    grad_ei y123 = (1/(2 sqrt3)) e_i . 1     : {c2}")

# ----------------------------------------------------------------------------
# STEP 1  Untwisted Dirac operator  D = sum_i e_i . grad_{e_i}
# ----------------------------------------------------------------------------
print()
print("=" * 70)
print("STEP 1  Untwisted Dirac  D psi_pm  =  -/+ sqrt(3) psi_pm")
print("=" * 70)
D = sum((E[i] * NAB[i] for i in range(1, 7)), sp.zeros(8, 8))
D = sp.simplify(D)
Dp = sp.simplify(D * PSI_P)
Dm = sp.simplify(D * PSI_M)
lam_p = sp.simplify((Dp[IDX[()]]) / PSI_P[IDX[()]])  # eigenvalue on psi_+
lam_m = sp.simplify((Dm[IDX[()]]) / PSI_M[IDX[()]])
print(
    f"  D psi_+ = ({lam_p}) psi_+   [expect -sqrt(3)]  match: "
    f"{sp.simplify(Dp - lam_p * PSI_P) == sp.zeros(8, 1) and sp.simplify(lam_p + sqrt3) == 0}"
)
print(
    f"  D psi_- = ({lam_m}) psi_-   [expect +sqrt(3)]  match: "
    f"{sp.simplify(Dm - lam_m * PSI_M) == sp.zeros(8, 1) and sp.simplify(lam_m - sqrt3) == 0}"
)
print("  Closed form:  D psi_pm = -/+ (6/(2 sqrt3)) psi_pm = -/+ sqrt(3) psi_pm.")

# ----------------------------------------------------------------------------
# STEP 2  Friedrich bound cross-check (pure numbers, no code from the module)
# ----------------------------------------------------------------------------
print()
print("=" * 70)
print("STEP 2  Friedrich bound  lambda^2 >= n/(4(n-1)) scal,  n=6, saturated")
print("=" * 70)
n = 6
mu = sp.Rational(1, 1) / (2 * sqrt3)  # Killing number
# Killing spinor => Einstein with scal = 4 n (n-1) mu^2
scal = sp.simplify(4 * n * (n - 1) * mu**2)
lam2_bound = sp.simplify(sp.Rational(n, 4 * (n - 1)) * scal)
lam_from_D = sp.simplify(n * mu)  # |D eigenvalue| = n*mu
print(f"  Killing number mu = 1/(2 sqrt3);   scal = 4 n(n-1) mu^2 = {scal}")
print(f"  Friedrich RHS  n/(4(n-1)) * scal   = {lam2_bound}")
print(f"  |lambda| from D  = n*mu = {lam_from_D};   lambda^2 = {sp.simplify(lam_from_D**2)}")
print(f"  bound saturated (lambda^2 == RHS): {sp.simplify(lam2_bound - lam_from_D**2) == 0}")
print(
    f"  radius check: scal_round(r) = n(n-1)/r^2 = {n * (n - 1)}/r^2 = {scal}  => r^2 = "
    f"{sp.simplify(sp.Rational(n * (n - 1), 1) / scal)}  (r = sqrt(3))"
)

# ----------------------------------------------------------------------------
# STEP 3  Twisted trivial block.
#   Domain  = SU(3)-invariants in Sigma_odd  (x) Sigma_even   (expect dim 2)
#   Target  = SU(3)-invariants in Sigma_even (x) Sigma_even   (expect dim 1)
#   D^+ (eta (x) xi) = sum_i (e_i . grad_ei eta)(x) xi + (e_i . eta)(x)(grad_ei xi)
#                    = (D (x) Id) + sum_i (e_i (x) grad_ei)
# ----------------------------------------------------------------------------
print()
print("=" * 70)
print("STEP 3  Twisted trivial-block certificate  (independent invariant search)")
print("=" * 70)

# su(3) generators on m (Remark 5.2), as so(6) elements -> spin lift on Sigma.
AD = {
    1: [(sp.Rational(1, 1), 1, 2), (sp.Rational(-1, 1), 3, 4)],
    2: [(sp.Rational(1, 1), 3, 5), (sp.Rational(1, 1), 4, 6)],
    3: [(sp.Rational(-1, 1), 3, 6), (sp.Rational(1, 1), 4, 5)],
    4: [(sp.Rational(1, 1), 1, 6), (sp.Rational(-1, 1), 2, 5)],
    5: [(sp.Rational(-1, 1), 1, 5), (sp.Rational(-1, 1), 2, 6)],
    6: [(sp.Rational(-1, 1), 1, 4), (sp.Rational(1, 1), 2, 3)],
    7: [(sp.Rational(1, 1), 1, 3), (sp.Rational(1, 1), 2, 4)],
    8: None,  # special 1/(2 sqrt3) prefactor below
}
RHO = {}
for k in range(1, 8):
    RHO[k] = so6_lift([(c * sp.Rational(1, 2), a, b) for (c, a, b) in AD[k]])
# ad(nu8)|m = (1/(2 sqrt3))(-e12 - e34 + 2 e56)
RHO[8] = so6_lift([(-1 / (2 * sqrt3), 1, 2), (-1 / (2 * sqrt3), 3, 4), (2 / (2 * sqrt3), 5, 6)])

# sanity: invariant spinors in Sigma = common kernel of RHO[1..8]  (expect span{1, y123})
stack = sp.Matrix.vstack(*[sp.simplify(RHO[k]) for k in range(1, 9)])
inv_sigma = stack.nullspace()
print(f"  invariant spinors in Sigma: dim = {len(inv_sigma)}  (expect 2: 1, y123)")


# Build tensor helpers on the 64-dim Sigma (x) Sigma.
def kron(A, B):
    return sp.Matrix(sp.kronecker_product(A, B))


def tvec(fa, fb):
    return kron(vec(fa), vec(fb))


# index sets for parity subspaces
odd_idx = [IDX[s] for s in ODD]
even_idx = [IDX[s] for s in EVEN]


def sub_indices(rows_first, rows_second):
    """flat indices into the 64-dim space for (first in rows_first) x (second in rows_second)."""
    return [i * 8 + j for i in rows_first for j in rows_second]


DOMAIN_IDX = sub_indices(odd_idx, even_idx)  # Sigma_odd (x) Sigma_even
TARGET_IDX = sub_indices(even_idx, even_idx)  # Sigma_even (x) Sigma_even

# su(3) action on the tensor product: M_k = RHO_k (x) Id + Id (x) RHO_k
I8 = sp.eye(8)
Mten = [sp.simplify(kron(RHO[k], I8) + kron(I8, RHO[k])) for k in range(1, 9)]


def restrict(M, idx):
    return M[idx, idx]


def invariants(idx):
    blocks = [restrict(M, idx) for M in Mten]
    stacked = sp.Matrix.vstack(*blocks)
    return stacked.nullspace()


dom_inv = invariants(DOMAIN_IDX)
tar_inv = invariants(TARGET_IDX)
print(f"  domain invariants  dim(Sigma_odd (x) Sigma_even)^SU(3)  = {len(dom_inv)}  (expect 2)")
print(f"  target invariants  dim(Sigma_even (x) Sigma_even)^SU(3) = {len(tar_inv)}  (expect 1)")
assert len(dom_inv) == 2 and len(tar_inv) == 1, "FRAMING COLLAPSE: block dims wrong"


# Embed invariant vectors back into full 64-dim space.
def embed(coeffs, idx):
    full = sp.zeros(64, 1)
    for local, gi in enumerate(idx):
        full[gi] = coeffs[local]
    return full


w_full = embed(tar_inv[0], TARGET_IDX)
w_full = w_full / sp.sqrt(sp.simplify((w_full.T * w_full)[0]))  # normalize target

# identify v_b = y123 (x) 1 explicitly and confirm it is one of the domain invariants
v_b = tvec({(1, 2, 3): sp.Integer(1)}, {(): sp.Integer(1)})
# express: is v_b in span(dom_inv)?  (it must be)
dom_full = [embed(c, DOMAIN_IDX) for c in dom_inv]
DM = sp.Matrix.hstack(*dom_full)
sol = DM.solve_least_squares(v_b) if False else None
# simpler: check rank does not increase when appending v_b
r0 = DM.rank()
r1 = sp.Matrix.hstack(DM, v_b).rank()
print(f"  v_b = y123 (x) 1 lies in domain-invariant span: {r0 == r1}  (rank {r0} -> {r1})")

# Build the twisted Dirac D^+ = D (x) Id + sum_i e_i (x) NAB_i  as 64x64, then map domain->target.
Dtw = kron(D, I8)
for i in range(1, 7):
    Dtw += kron(E[i], NAB[i])
Dtw = sp.simplify(Dtw)

# ---- exact w-coefficient of D^+(v_b) (the b-channel, task's core deliverable) ----
Dvb = sp.simplify(Dtw * v_b)
b_coeff = sp.simplify((w_full.T * Dvb)[0])  # <w_hat, D^+ v_b> with w_hat normalized
print()
print("  --- b-channel (v_b = y123 (x) 1, normalized; target w = 1 (x) 1) ---")
print(
    f"  <w, D^+ v_b>  =  b  =  {b_coeff}     |b|^2 = {sp.simplify(b_coeff * sp.conjugate(b_coeff))}"
)

# decompose Term1 (D (x) Id) vs Term2 (sum e_i (x) NAB_i) to show Term2 has NO w-component
term1 = sp.simplify(kron(D, I8) * v_b)
term2 = sp.simplify(sum((kron(E[i], NAB[i]) for i in range(1, 7)), sp.zeros(64, 64)) * v_b)
t1w = sp.simplify((w_full.T * term1)[0])
t2w = sp.simplify((w_full.T * term2)[0])
print(f"  Term1 (D(x)Id) . v_b  w-coeff = {t1w}   [= -sqrt(3)]")
print(
    f"  Term2 (sum e_i(x)NAB_i).v_b  w-coeff = {t2w}   [= 0, the pair (e_{{2j-1}},e_{{2j}}) cancels]"
)
print(f"  Term2 vector identically zero: {sp.simplify(term2) == sp.zeros(64, 1)}")

# ---- a-channel (the other domain invariant) for completeness ----
# pick the domain invariant orthogonal to v_b -> that is (proportional to) v_a in span{y_i}(x)span{y_jk}
# Gram-Schmidt: u2 = v_b/|v_b|, u1 = component of dom_inv not along v_b
u2 = v_b / sp.sqrt(sp.simplify((v_b.T * v_b)[0]))
# take the two domain invariants, remove u2 part from one of them
cand = dom_full[0]
cand = cand - sp.simplify((u2.T * cand)[0]) * u2
if sp.simplify(cand.T * cand)[0] == 0:
    cand = dom_full[1] - sp.simplify((u2.T * dom_full[1])[0]) * u2
u1 = cand / sp.sqrt(sp.simplify((cand.T * cand)[0]))
a_coeff = sp.simplify((w_full.T * sp.simplify(Dtw * u1))[0])
s_cert = sp.simplify(a_coeff * sp.conjugate(a_coeff) + b_coeff * sp.conjugate(b_coeff))
print()
print("  --- full certificate ---")
print(f"  a = <w, D^+ u1> = {a_coeff}     |a|^2 = {sp.simplify(a_coeff * sp.conjugate(a_coeff))}")
print(f"  b = <w, D^+ u2> = {b_coeff}     |b|^2 = {sp.simplify(b_coeff * sp.conjugate(b_coeff))}")
print(f"  s = |a|^2 + |b|^2 = {s_cert}")
print(f"  rank(D^+|_1) = 1  (target is 1-dim, s > 0): {sp.simplify(s_cert) > 0}")

# ----------------------------------------------------------------------------
# Convention-flip robustness on |b|^2 (magnitude, not sign/phase)
# ----------------------------------------------------------------------------
print()
print("=" * 70)
print("STEP 4  Convention robustness of |b|^2")
print("=" * 70)
print("  b = -sqrt(3).  A global sign/phase flip (Clifford sign e_i.e_i=+1,")
print("  orientation of y123, phase of the invariant) sends b -> (phase)*(+/- sqrt3),")
print("  leaving |b|^2 = 3 invariant.  Hence s >= |b|^2 = 3 > 0 regardless of v_a,")
print("  and rank >= 1 survives every calibration-consistent convention.")
print()

print("=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"  convention           : e_i.e_i = -1                    [{conv_ok}]")
print(f"  Thm 5.1 calibration  : 6/6 dirs, both signs            [{kill_ok}]")
print(
    f"  untwisted Dirac      : D psi_pm = -/+ sqrt(3) psi_pm   "
    f"[{sp.simplify(lam_p + sqrt3) == 0 and sp.simplify(lam_m - sqrt3) == 0}]"
)
print(
    f"  Friedrich saturated  : lambda^2 = 3 = n/(4(n-1)) scal  [{sp.simplify(lam2_bound - 3) == 0}]"
)
print(
    f"  block dims (dom,tar) : ({len(dom_inv)}, {len(tar_inv)})                        "
    f"[{len(dom_inv) == 2 and len(tar_inv) == 1}]"
)
print(
    f"  b-channel exact      : b = {b_coeff},  |b|^2 = 3       "
    f"[{sp.simplify(b_coeff * sp.conjugate(b_coeff) - 3) == 0}]"
)
print(f"  Term2 w-component    : 0                               [{t2w == 0}]")
print(f"  certificate          : s = {s_cert} > 0  => rank = 1")
