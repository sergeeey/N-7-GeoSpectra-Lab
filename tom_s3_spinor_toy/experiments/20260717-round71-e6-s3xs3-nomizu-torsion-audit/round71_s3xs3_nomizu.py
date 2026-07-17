r"""
Round 71 (E6) -- explicit Levi-Civita Nomizu-connection / Term2 audit for
S^3 x S^3 = SU(2)^3/SU(2)_diag.

Closes the gap Round 70/E5 explicitly flagged: does the isotropy-trivial slot
inside Lambda^2(m^{1,0})(x)Lambda^2(m^{1,0}) (present for S3xS3, absent for
S6/SU(3)-T2/CP3) carry a zero or nonzero Term2 coefficient under the actual
canonical (Levi-Civita) connection?

Primary source: Charbonneau-Harland 2016 (CH2016), arXiv:1510.07720v2,
  - Section 2 (pages 2-6): general nearly-Kahler spinorial geometry, Killing
    spinor equation (eq 1), connection family nabla^t (eq 7-8), Lemma 2 (P,Q
    eigenvalues on Lambda^0/Lambda^1/Lambda^6).
  - Section 4 (pages 13-19): SU(2)^3/SU(2) case. Basis I_i^(a) (page 14),
    B(I_i^(a),I_j^(b)) = (1/6) delta_ij delta_ab (page 14/18), diagonal
    isotropy H_i = I_i^(1)+I_i^(2)+I_i^(3) (page 14), orthogonal-complement
    basis X_i = ((1+sqrt2)J_i,(1-sqrt2)J_i,-2J_i), Y_i = sqrt6(J_i,-J_i,0)
    (page 18), "the almost complex structure sends X_i to Y_i and Y_i to
    -X_i" (page 18), ad(I_i)(X_j) = eps_ijk X_k (page 18).

Method transported from experiments/20260714-round59-trivial-rank-certification
(round59_route_c_analytic.py), which built the SAME kind of explicit
Levi-Civita Nomizu-map + Clifford-module + calibration construction for
S^6 = G2/SU(3), following Agricola-Hofmann-Lawn 2023 (AHL2023). This script
does NOT import or copy-paste from that file (independence, same discipline
as Round 65) -- it rebuilds the analogous objects from scratch for
SU(2)_diag, using CH2016's own stated su(2)^3 data instead of AHL2023's
G2/SU(3) data.

Run:  python round71_s3xs3_nomizu.py
"""

import sympy as sp

sqrt2 = sp.sqrt(2)
sqrt3 = sp.sqrt(3)
sqrt6 = sp.sqrt(6)
IU = sp.I

# ----------------------------------------------------------------------------
# STEP 0: g = su(2) (+) su(2) (+) su(2).  Elements represented as 3x3 sympy
# Matrices M with M[a,i] = coefficient of I_i^{(a)}  (a = copy 0,1,2 ; i = su(2)
# vector index 0,1,2, i.e. 1-indexed i=1,2,3 in CH2016's own notation).
# Bracket: [I_i^(a), I_j^(b)] = delta_ab * eps_ijk * I_k^(a)   (CH2016 p.18,
# "Ii = (Ji,0,0)" etc. with [Ji,Jj]=eps_ijk Jk within each copy; copies commute).
# ----------------------------------------------------------------------------


def eps(i, j, k):
    """Levi-Civita symbol, 1-indexed i,j,k in {1,2,3}."""
    p = [i, j, k]
    if len(set(p)) < 3:
        return 0
    sign = 1
    n = 3
    for x in range(n):
        for y in range(n - 1 - x):
            if p[y] > p[y + 1]:
                p[y], p[y + 1] = p[y + 1], p[y]
                sign = -sign
    return sign


def bracket_g(Mx, My):
    out = sp.zeros(3, 3)
    for a in range(3):
        for i in range(3):
            cxi = Mx[a, i]
            if cxi == 0:
                continue
            for j in range(3):
                cyj = My[a, j]
                c = cxi * cyj
                if c == 0:
                    continue
                for k in range(3):
                    e = eps(i + 1, j + 1, k + 1)
                    if e:
                        out[a, k] += c * e
    return out


def B_form(Mx, My):
    """B(Mx,My) = (1/6) sum_{a,i} Mx[a,i]*My[a,i]   (CH2016 p.18)."""
    s = 0
    for a in range(3):
        for i in range(3):
            s += Mx[a, i] * My[a, i]
    return sp.nsimplify(sp.Rational(1, 6) * s)


def e_ai(a, i):
    M = sp.zeros(3, 3)
    M[a, i] = 1
    return M


# I_i^(a) basis
Ivec = [[e_ai(a, i) for i in range(3)] for a in range(3)]

# H_i = I_i^(1)+I_i^(2)+I_i^(3)   (page 14, "Ii = (Ji,Ji,Ji)")
H = [Ivec[0][i] + Ivec[1][i] + Ivec[2][i] for i in range(3)]

# X_i, Y_i  (page 18, EXACT transcription)
X = [(1 + sqrt2) * Ivec[0][i] + (1 - sqrt2) * Ivec[1][i] + (-2) * Ivec[2][i] for i in range(3)]
Y = [sqrt6 * Ivec[0][i] + (-sqrt6) * Ivec[1][i] for i in range(3)]

print("=" * 78)
print("STEP 0  Transcription + orthogonality checks (CH2016 p.14, p.18)")
print("=" * 78)
for i in range(3):
    bhx = sp.simplify(B_form(H[i], X[i]))
    bhy = sp.simplify(B_form(H[i], Y[i]))
    print(f"  B(H_{i + 1}, X_{i + 1}) = {bhx}   B(H_{i + 1}, Y_{i + 1}) = {bhy}")
    assert bhx == 0 and bhy == 0, "X_i or Y_i not orthogonal to isotropy H_i"
print("  m = span{X_i,Y_i} is B-orthogonal to h = span{H_i}: CONFIRMED")

# cross-check: [H_i,H_j] = eps_ijk H_k   (su(2) bracket on isotropy, general fact)
ok = True
for i in range(3):
    for j in range(3):
        lhs = bracket_g(H[i], H[j])
        rhs = sp.zeros(3, 3)
        for k in range(3):
            e = eps(i + 1, j + 1, k + 1)
            if e:
                rhs += e * H[k]
        ok &= sp.simplify(lhs - rhs) == sp.zeros(3, 3)
print(f"  [H_i,H_j] = eps_ijk H_k (isotropy is genuinely su(2)): {ok}")
assert ok

# cross-check: ad(H_i)(X_j) = eps_ijk X_k   (CH2016 p.18, independent re-derivation)
ok2 = True
for i in range(3):
    for j in range(3):
        lhs = bracket_g(H[i], X[j])
        rhs = sp.zeros(3, 3)
        for k in range(3):
            e = eps(i + 1, j + 1, k + 1)
            if e:
                rhs += e * X[k]
        ok2 &= sp.simplify(lhs - rhs) == sp.zeros(3, 3)
print(f"  ad(H_i)(X_j) = eps_ijk X_k, re-derived from bracket_g (matches CH2016 p.18): {ok2}")
assert ok2

# ----------------------------------------------------------------------------
# STEP 1: metric-compatibility check.  B(X_i,X_i) vs B(Y_i,Y_i) -- Risk 2.
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("STEP 1  Metric-compatibility check of CH2016's literal (X_i,Y_i) basis")
print("=" * 78)
bxx = sp.simplify(B_form(X[0], X[0]))
byy = sp.simplify(B_form(Y[0], Y[0]))
bxy = sp.simplify(B_form(X[0], Y[0]))
print(f"  B(X_1,X_1) = {bxx}")
print(f"  B(Y_1,Y_1) = {byy}")
print(f"  B(X_1,Y_1) = {bxy}")
compat = sp.simplify(bxx - byy) == 0
print(f"  B(X,X) == B(Y,Y) (required for J to be B-Hermitian)?  {compat}")
if not compat:
    print("  => CONFIRMED INCONSISTENCY: raw B is NOT Hermitian w.r.t. J(X_i)=Y_i.")
    print("     Repairing via the FORCED (not arbitrary) Hermitization")
    print("     g_H(V,W) := (1/2)[B(V,W) + B(JV,JW)]  (general fact for any (form,J) pair).")

# J acting on the 6 real basis vectors (X1,Y1,X2,Y2,X3,Y3), as a list of images
basis6 = [X[0], Y[0], X[1], Y[1], X[2], Y[2]]
Jimg6 = [Y[0], -X[0], Y[1], -X[1], Y[2], -X[2]]

Braw = sp.Matrix(6, 6, lambda r, c: B_form(basis6[r], basis6[c]))
BJJ = sp.Matrix(6, 6, lambda r, c: B_form(Jimg6[r], Jimg6[c]))
gH = sp.simplify((Braw + BJJ) / 2)
print()
print("  g_H matrix (basis X1,Y1,X2,Y2,X3,Y3):")
sp.pprint(gH)
off_diag_zero = all(gH[r, c] == 0 for r in range(6) for c in range(6) if r != c)
diag_vals = {gH[r, r] for r in range(6)}
print(f"  g_H is diagonal: {off_diag_zero}")
print(f"  g_H diagonal values (should be a single constant kappa): {diag_vals}")
assert off_diag_zero and len(diag_vals) == 1, "g_H is not a clean isotropic form -- unexpected"
kappa = diag_vals.pop()
print(f"  kappa = {kappa}")

# ----------------------------------------------------------------------------
# STEP 2: natural-reductivity check of g_H on m (decisive gate for the Nomizu
# map formula Lambda(V)(W) = (1/2)[V,W]_m to BE the Levi-Civita connection).
# Condition: g_H([U,V]_m, W) + g_H(V, [U,W]_m) = 0  for all U,V,W in m.
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("STEP 2  Natural-reductivity check of g_H  (decisive gate)")
print("=" * 78)

# P matrix: columns = (H-direction, X-direction, Y-direction) coefficients in
# "copy space" (same for every vector-index i, by construction).
P = sp.Matrix([[1, 1 + sqrt2, sqrt6], [1, 1 - sqrt2, -sqrt6], [1, -2, 0]])
Pinv = P.inv()


def decompose(Gmat):
    """Gmat: 3x3 (copy x vector-index).  Returns (h_part, m_part) as g-elements
    (3x3 matrices), by solving, for EACH column i, P*(h_i,x_i,y_i)^T = Gmat[:,i]."""
    h_part = sp.zeros(3, 3)
    m_part = sp.zeros(3, 3)
    for i in range(3):
        col = Gmat[:, i]
        coeffs = sp.simplify(Pinv * col)
        h_i, x_i, y_i = coeffs[0], coeffs[1], coeffs[2]
        h_part += h_i * H[i]
        m_part += x_i * X[i] + y_i * Y[i]
    return sp.simplify(h_part), sp.simplify(m_part)


def m_coeffs(Gmat):
    """Return the 6 coefficients (c_X1,c_Y1,c_X2,c_Y2,c_X3,c_Y3) of proj_m(Gmat)."""
    out = []
    for i in range(3):
        col = Gmat[:, i]
        coeffs = sp.simplify(Pinv * col)
        out.append(coeffs[1])  # x_i
        out.append(coeffs[2])  # y_i
    return out  # ordered (x1,y1,x2,y2,x3,y3) matching basis6 order


def metric_of_vectors(metric_diag, coeffsA, coeffsB):
    return sp.simplify(sum(coeffsA[k] * coeffsB[k] * metric_diag[k] for k in range(6)))


def check_natural_reductivity(metric_diag, label):
    ok = True
    for a in range(6):
        for b in range(6):
            for c in range(6):
                U, V, W = basis6[a], basis6[b], basis6[c]
                UV_coeffs = m_coeffs(bracket_g(U, V))
                UW_coeffs = m_coeffs(bracket_g(U, W))
                e_c_coeffs = [1 if k == c else 0 for k in range(6)]
                e_b_coeffs = [1 if k == b else 0 for k in range(6)]
                term1 = metric_of_vectors(metric_diag, UV_coeffs, e_c_coeffs)
                term2 = metric_of_vectors(metric_diag, e_b_coeffs, UW_coeffs)
                if sp.simplify(term1 + term2) != 0:
                    ok = False
    print(f"  [{label}] g([U,V]_m,W) + g(V,[U,W]_m) = 0 for all U,V,W in m-basis: {ok}")
    return ok


# CONTROL: raw B (unmodified) must be naturally reductive automatically -- B is
# the literal restriction of an Ad(g)-invariant form on the WHOLE Lie algebra g,
# and this is a completely general fact (e.g. Besse, "Einstein Manifolds", 7.44)
# independent of anything specific to S3xS3.  If this control FAILS, the checker
# code itself is broken, not the geometry -- must be fixed before trusting the
# g_H result below.
Braw_diag = [Braw[k, k] for k in range(6)]


# raw B is NOT diagonal in general off the (X_i,Y_i)-index-i block-diagonal
# structure already confirmed (B(X_i,X_j)=B(Y_i,Y_j)=B(X_i,Y_j)=0 for i!=j) but
# B(X_i,Y_i) != 0 -- so use the FULL Braw matrix, not just its diagonal.
def metric_of_vectors_full(metric_mat, coeffsA, coeffsB):
    v = sp.Matrix(coeffsA)
    w = sp.Matrix(coeffsB)
    return sp.simplify((v.T * metric_mat * w)[0])


def check_natural_reductivity_full(metric_mat, label):
    ok = True
    for a in range(6):
        for b in range(6):
            for c in range(6):
                U, V, W = basis6[a], basis6[b], basis6[c]
                UV_coeffs = m_coeffs(bracket_g(U, V))
                UW_coeffs = m_coeffs(bracket_g(U, W))
                e_c_coeffs = [1 if k == c else 0 for k in range(6)]
                e_b_coeffs = [1 if k == b else 0 for k in range(6)]
                term1 = metric_of_vectors_full(metric_mat, UV_coeffs, e_c_coeffs)
                term2 = metric_of_vectors_full(metric_mat, e_b_coeffs, UW_coeffs)
                if sp.simplify(term1 + term2) != 0:
                    ok = False
    print(f"  [{label}] g([U,V]_m,W) + g(V,[U,W]_m) = 0 for all U,V,W in m-basis: {ok}")
    return ok


print()
print("  CONTROL: is raw B (unmodified, no Hermitization) naturally reductive?")
print("  (general theorem predicts YES automatically -- sanity-checks the CODE)")
control_ok = check_natural_reductivity_full(Braw, "raw B")
assert control_ok, (
    "CONTROL FAILED: raw B is not naturally reductive -- this violates a general "
    "theorem (Ad(g)-invariant form restricted via reductive decomposition is ALWAYS "
    "naturally reductive), so the natural-reductivity CHECKER CODE itself must have "
    "a bug -- fix before trusting any g_H result"
)
print("  CONTROL PASSED: checker code is correct (raw B is naturally reductive, as it must be).")

print()
print("  ACTUAL TEST: is the Hermitized g_H naturally reductive?")
nat_red_ok = check_natural_reductivity_full(gH, "Hermitized g_H")
if not nat_red_ok:
    print()
    print("  => g_H (the FORCED Hermitization needed to repair CH2016's literal")
    print("     J-vs-B incompatibility) is NOT naturally reductive w.r.t. m.")
    print("     Consequence: the standard naturally-reductive Levi-Civita Nomizu")
    print("     formula Lambda(V)(W)=(1/2)[V,W]_m is NOT valid for g_H, because g_H")
    print("     is only Ad(H)-invariant (built from J, which only H preserves), NOT")
    print("     the restriction of an Ad(g)-invariant form on the WHOLE Lie algebra")
    print("     g (which is what the general naturally-reductive theorem requires).")
    print("     Raw B (control, above) IS naturally reductive -- but raw B is NOT")
    print("     Hermitian w.r.t. CH2016's own literal stated J (Step 1). There is NO")
    print("     forced, canonical way to have BOTH properties simultaneously from")
    print("     CH2016's own stated page-18 data alone: fixing metric-compatibility")
    print("     (Hermitization) breaks natural reductivity; keeping natural")
    print("     reductivity (raw B) breaks metric-compatibility with the stated J.")
    print("     This is a GENUINE, VERIFIED OBSTRUCTION, not a computational slip.")


# ----------------------------------------------------------------------------
# STEP 3: SECOND independent attempt to resolve the Step-1/Step-2 obstruction
# (per claim.md's escape route -- BLOCKED/ILL-POSED requires >= 2 independent
# repair attempts, not just one).  Instead of fixing the metric (Step 1's
# Hermitization, which broke natural reductivity), try fixing the COMPLEX
# STRUCTURE instead: keep raw B untouched (guaranteed naturally reductive,
# confirmed by the control above), and find the B-COMPATIBLE almost complex
# structure J_B on the 2-plane span{X_i,Y_i} directly (J_B^2=-1,
# B(J_B v, J_B w)=B(v,w)).  In 2 real dimensions this is unique up to the
# standard +/- orientation ambiguity (not a genuine new free parameter) --
# check whether J_B agrees with CH2016's literal "sends X_i to Y_i" statement
# up to that standard ambiguity, or is a genuinely different map.
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("STEP 3  SECOND independent repair attempt: B-compatible J_B (keep B fixed,")
print("        solve for the compatible complex structure instead of Step 1's")
print("        'keep J fixed, repair the metric' direction)")
print("=" * 78)
Mxy = sp.Matrix([[bxx, bxy], [bxy, byy]])  # B restricted to span{X_i,Y_i}, any fixed i
print("  B restricted to span{X_i,Y_i} (basis order X,Y):")
sp.pprint(Mxy)

Pdiag, Ddiag = Mxy.diagonalize()
Dsqrt = Ddiag.applyfunc(sp.sqrt)
L = sp.simplify(Pdiag * Dsqrt * Pdiag.inv())  # Mxy^{1/2}, symmetric, L*L=Mxy
assert sp.simplify(L * L - Mxy) == sp.zeros(2, 2), "M^(1/2) construction failed"
Linv = L.inv()
Rot90 = sp.Matrix([[0, -1], [1, 0]])
J_B = sp.simplify(Linv * Rot90 * L)  # the (essentially unique, up to sign) B-compatible J
print("  J_B (matrix acting on (X,Y)-coefficient vectors) =")
sp.pprint(J_B)
print(f"  J_B^2 == -I:  {sp.simplify(J_B * J_B) == -sp.eye(2)}")
print(
    f"  J_B^T . Mxy . J_B == Mxy (B-compatibility):  {sp.simplify(J_B.T * Mxy * J_B - Mxy) == sp.zeros(2, 2)}"
)

J_literal = sp.Matrix([[0, -1], [1, 0]])  # CH2016's literal "X_i -> Y_i, Y_i -> -X_i"
print()
print("  CH2016's literal stated J (X->Y, Y->-X), same coordinate convention:")
sp.pprint(J_literal)
same_up_to_sign = (sp.simplify(J_B - J_literal) == sp.zeros(2, 2)) or (
    sp.simplify(J_B + J_literal) == sp.zeros(2, 2)
)
print(
    f"  J_B == +/- J_literal (i.e. same map, up to the standard orientation sign)?  {same_up_to_sign}"
)
print("  => J_B has NONZERO diagonal entries (J_literal's diagonal is identically zero) --")
print("     this is NOT a rescaling or orientation-flip of CH2016's literal J; it is a")
print("     GENUINELY DIFFERENT linear map on span{X_i,Y_i}. CONFIRMS: no forced,")
print("     canonical single resolution exists from CH2016's own stated page-18 data --")
print("     the 'repair-the-metric' path (Step 1-2) and the 'repair-the-complex-")
print("     structure' path (this step) give two DIFFERENT, mutually incompatible fixes,")
print("     neither preferred by the primary source text over the other.")
assert not same_up_to_sign, (
    "unexpected: J_B DOES match CH2016's literal J up to sign -- would change the verdict, "
    "re-examine before writing decision.md"
)

print()
print("=" * 78)
print("SUMMARY (2 independent repair attempts, both FAIL to give a forced,")
print("unique construction -- per claim.md's escape route, this now settles the")
print("verdict rather than continuing indefinitely)")
print("=" * 78)
print(f"  Attempt 1 (Hermitize metric, keep literal J): naturally reductive? {nat_red_ok}")
print(f"  Attempt 2 (keep raw B, solve for compatible J): matches literal J? {same_up_to_sign}")
print("  VERDICT: ILL-POSED for building the Levi-Civita Nomizu map / Clifford module")
print("  directly from CH2016's own stated page-18 (X_i,Y_i,J) data without an")
print("  additional, non-forced choice. See decision.md for full writeup.")
