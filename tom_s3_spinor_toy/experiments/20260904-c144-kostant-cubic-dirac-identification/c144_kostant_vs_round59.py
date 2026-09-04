r"""
Independent check: is round59's Levi-Civita untwisted Dirac operator D
(on S6 = G2/SU(3), from AHL2023 Remark 5.2 Nomizu operators) an instance
of Kostant's algebraic cubic Dirac operator
    D_kostant := sum_i X_i (x) X_i^* + 1 (x) v
(Kostant 1999 / Landweber math/0005056 eq. (kostantdirac))?

STRUCTURAL FACT (derived directly from Landweber's eqs, not assumed):
  Restricted to the trivial G2-representation V_0 (i.e. acting purely on
  Sigma, no V_lambda tensor factor -- exactly round59's setup, since
  psi_+ = 1+y123, psi_- = 1-y123 in Sigma alone), the r(X_i) term of
  Kostant's operator vanishes identically (Lie derivative of a constant
  function is 0, independent of any connection choice). So
      D_kostant |_{V_0} = c(v)   exactly,
  a PURE algebraic Clifford-cubic operator with no connection-dependence
  at all in Kostant's own (canonical-connection-based) construction.

THE QUESTION this script actually tests: does round59's D (built from the
ACTUAL Levi-Civita spin connection, NOT the canonical/torsion connection)
equal c(v) up to a single overall real scalar?  This is a decisive,
symbol-exact test, reusing round59's own verified Clifford/Nomizu code
so nothing here is re-derived from a different, unverified convention.

v is built from AHL2023's own Remark-5.2 Nomizu 2-form DATA (the Lam[i]
table already transcribed and verified in round59_route_c_analytic.py --
its Killing-spinor calibration in round59 already PASSED), used as data
PROPORTIONAL to the g2 structure constants restricted to m = p: each raw
Lam[i] coefficient equals -(1/2) times the true structure constant
c_{i,a,b} = <e_i,[e_a,e_b]>, per the standard naturally-reductive-space
Nomizu formula grad^LC = (1/2)[.,.]_m.  Since only PROPORTIONALITY to
omega is tested below (not an exact normalization match), this -1/2
factor does not affect the test -- it is absorbed into the fitted alpha.

SKEPTIC CORRECTION (2026-09-04, context-blind pass, see decision.md):
the STEP 4 "proportional on all 64 entries" result below is ALGEBRAICALLY
FORCED by STEP 2 (total antisymmetry of C_ijk) plus the absence of any
Lam[i] entry with i in {a,b} -- it is NOT independent per-geometry
evidence beyond what STEP 1's Killing-spinor calibration already tests.
Total antisymmetry of the m-bracket is itself a GENERIC consequence of
building a naturally-reductive metric from any Ad-invariant form on g,
not a G2/SU(3)-specific surprise.  Kept in the record as still-correct
and still useful (it confirms Kostant/Slebarski's FRAMEWORK genuinely
applies here), but the interpretive weight originally given to STEP 4 in
isolation was overstated -- see claim.md caveat 5 for the full correction.

Run:  python kostant_vs_round59.py
"""

import sympy as sp

IU = sp.I
sqrt3 = sp.sqrt(3)

# ---------------------------------------------------------------------------
# STEP 0 -- verbatim reproduction of round59_route_c_analytic.py's Clifford
# algebra construction (AHL2023 Section 2.1 eq.(5)), so E[i] here is BYTE-
# IDENTICAL in construction to the already-independently-verified round59
# operators.  (Transcribed by hand from the same primary source, same
# convention e_i.e_i = -1.)
# ---------------------------------------------------------------------------
BASIS = [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
IDX = {s: k for k, s in enumerate(BASIS)}


def _sort_sign(seq):
    seq = list(seq)
    sign = 1
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
    out = {}
    for subset, c in form.items():
        s, sign = _sort_sign((j,) + subset)
        if s is None:
            continue
        out[s] = out.get(s, 0) + sign * c
    return {k: v for k, v in out.items() if v != 0}


def contract_x(j, form):
    out = {}
    for subset, c in form.items():
        for pos, elt in enumerate(subset):
            if elt == j:
                sign = (-1) ** pos
                rest = subset[:pos] + subset[pos + 1 :]
                out[rest] = out.get(rest, 0) + sign * c
    return {k: v for k, v in out.items() if v != 0}


def clifford(i, form):
    j = (i + 1) // 2
    xj = contract_x(j, form)
    yj = wedge_y(j, form)
    if i % 2 == 1:
        return _add(_scale(IU, xj), _scale(IU, yj))
    else:
        return _add(yj, _scale(-1, xj))


def _scale(a, form):
    return {k: a * v for k, v in form.items() if a * v != 0}


def _add(*forms):
    out = {}
    for f in forms:
        for k, v in f.items():
            out[k] = out.get(k, 0) + v
    return {k: sp.simplify(v) for k, v in out.items() if sp.simplify(v) != 0}


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
PSI_P = ONE + Y123
PSI_M = ONE - Y123

for i in range(1, 7):
    assert sp.simplify(E[i] * E[i] + sp.eye(8)) == sp.zeros(8, 8)
print("STEP 0  Clifford convention e_i.e_i=-1 reproduced (8x8, verbatim round59)  [OK]")

# ---------------------------------------------------------------------------
# STEP 1 -- round59's own Levi-Civita Nomizu operators (Remark 5.2), verbatim.
# ---------------------------------------------------------------------------


def so6_lift(pairs):
    M = sp.zeros(8, 8)
    for coeff, a, b in pairs:
        M += coeff * sp.Rational(1, 2) * (E[a] * E[b])
    return M


Lam = {
    1: [(sp.Rational(1, 1), 3, 6), (sp.Rational(1, 1), 4, 5)],
    2: [(sp.Rational(1, 1), 3, 5), (sp.Rational(-1, 1), 4, 6)],
    3: [(sp.Rational(-1, 1), 1, 6), (sp.Rational(-1, 1), 2, 5)],
    4: [(sp.Rational(-1, 1), 1, 5), (sp.Rational(1, 1), 2, 6)],
    5: [(sp.Rational(1, 1), 1, 4), (sp.Rational(1, 1), 2, 3)],
    6: [(sp.Rational(1, 1), 1, 3), (sp.Rational(-1, 1), 2, 4)],
}
NAB = {i: so6_lift([(c / (2 * sqrt3), a, b) for (c, a, b) in Lam[i]]) for i in range(1, 7)}


def nab(i, v):
    return sp.simplify(NAB[i] * v)


kill_ok = True
for i in range(1, 7):
    lhs_p = nab(i, PSI_P)
    rhs_p = sp.simplify(sp.Rational(1, 1) / (2 * sqrt3) * (E[i] * PSI_P))
    kill_ok &= sp.simplify(lhs_p - rhs_p) == sp.zeros(8, 1)
assert kill_ok
print("STEP 1  Levi-Civita Nomizu operators reproduce Thm 5.1 Killing eqn (verbatim round59)  [OK]")

D = sp.simplify(sum((E[i] * NAB[i] for i in range(1, 7)), sp.zeros(8, 8)))
Dp = sp.simplify(D * PSI_P)
lam_p = sp.simplify(Dp[IDX[()]] / PSI_P[IDX[()]])
assert sp.simplify(lam_p + sqrt3) == 0
print(f"STEP 1  round59's own D psi_+ = ({lam_p}) psi_+   [OK, matches -sqrt3]")

# ---------------------------------------------------------------------------
# STEP 2 -- extract structure constants c_{ijk} = <e_i,[e_j,e_k]> from Lam,
# using the RAW (unscaled, +-1) coefficients only -- i.e. treat Lam[i] as
# encoding the m-component of ad(e_i) as an so(6) 2-form, PRIOR to any of
# round59's own 1/(2 sqrt3) metric/connection normalization.
# ---------------------------------------------------------------------------
C = {(i, j, k): sp.Integer(0) for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)}
for i in range(1, 7):
    for coeff, a, b in Lam[i]:
        C[(i, a, b)] = coeff
        C[(i, b, a)] = -coeff

# total antisymmetry check: C[i,j,k] should equal C[j,k,i] should equal -C[j,i,k]
antisym_ok = True
detail = []
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            a = C[(i, j, k)]
            b = C[(j, k, i)]
            c_ = C[(j, i, k)]
            ok1 = sp.simplify(a - b) == 0
            ok2 = sp.simplify(a + c_) == 0
            if not (ok1 and ok2):
                antisym_ok = False
                detail.append((i, j, k, a, b, c_))
print(f"STEP 2  total antisymmetry of C_ijk (cyclic + swap) over all (i,j,k): {antisym_ok}")
if not antisym_ok:
    print(f"         FIRST FAILURE (of {len(detail)}): {detail[0]}")

# ---------------------------------------------------------------------------
# STEP 3 -- quantize omega = sum_{i<j<k} C[i,j,k] e^i^e^j^e^k into Cl(m) via
# the Chevalley map (for DISTINCT indices, wedge = ordered Clifford product,
# no lower-order correction terms).
# ---------------------------------------------------------------------------
if antisym_ok:
    v_op = sp.zeros(8, 8)
    for i in range(1, 7):
        for j in range(i + 1, 7):
            for k in range(j + 1, 7):
                coeff = C[(i, j, k)]
                if coeff != 0:
                    v_op += coeff * (E[i] * E[j] * E[k])
    v_op = sp.simplify(v_op)
    print("STEP 3  built c(omega_raw) := quantization of raw structure-constant 3-form  [done]")

    # ------------------------------------------------------------------
    # STEP 4 -- is D proportional to v_op?  Solve for a single scalar alpha
    # such that D == alpha * v_op as exact 8x8 matrices (try componentwise
    # ratio of the first nonzero entry, then verify on ALL entries).
    # ------------------------------------------------------------------
    alpha = None
    for r in range(8):
        for cc in range(8):
            if sp.simplify(v_op[r, cc]) != 0:
                alpha = sp.simplify(D[r, cc] / v_op[r, cc])
                break
        if alpha is not None:
            break

    if alpha is None:
        print("STEP 4  v_op is identically ZERO -- cannot test proportionality this way")
    else:
        residual = sp.simplify(D - alpha * v_op)
        proportional = residual == sp.zeros(8, 8)
        print(f"STEP 4  candidate scalar alpha (from first nonzero entry) = {alpha}")
        print(f"STEP 4  D == alpha * c(omega_raw) EXACTLY on all 64 entries: {proportional}")
        if not proportional:
            nz = [
                (r, cc, sp.simplify(residual[r, cc]))
                for r in range(8)
                for cc in range(8)
                if sp.simplify(residual[r, cc]) != 0
            ]
            print(f"         residual nonzero at {len(nz)} / 64 entries; sample: {nz[:5]}")

    # ------------------------------------------------------------------
    # STEP 5 -- eigenvalue cross-check (independent of the STEP 4 result):
    # v_op psi_pm = ? * psi_pm
    # ------------------------------------------------------------------
    vp_P = sp.simplify(v_op * PSI_P)
    ratio_P = sp.simplify(vp_P[IDX[()]] / PSI_P[IDX[()]]) if PSI_P[IDX[()]] != 0 else None
    is_eigvec = sp.simplify(vp_P - ratio_P * PSI_P) == sp.zeros(8, 1)
    print(f"STEP 5  v_op psi_+ = ({ratio_P}) psi_+  (is exact eigenvector: {is_eigvec})")
else:
    print(
        "STEP 3-5 SKIPPED: raw Lam data is not a totally antisymmetric 3-tensor as-is;"
        " round59's Lam[i] table encodes the SPIN-CONNECTION 2-form per direction i,"
        " not directly the structure-constant 3-tensor -- these need not coincide"
        " index-for-index without also checking the su(3) part (AD[k]) or an"
        " independent primary-source g2 structure-constant table."
    )

print()
print("=" * 78)
print("SUMMARY")
print("=" * 78)
print("This checks ONLY the 'raw Lam as structure constants' hypothesis.")
print("It does NOT yet resolve whether Kostant's v needs additional su(3)-sector")
print("input (AD[k]) beyond the pure-m data in Lam.")
