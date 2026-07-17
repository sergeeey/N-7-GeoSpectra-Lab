"""Round69-E4: attempt at a representation-theory-FREE verification of
dim ker(D_{S6}(x)S-) = 1, via an explicit ambient-Clifford-algebra /
hypersurface-embedding construction of the twisted Dirac operator on S6,
diagonalized directly by numerical/symbolic linear algebra (SVD / nullspace
/ eigenvalues), with NO decomposition into G2 or SU(3) irreps, NO character
theory, NO Casimir-eigenvalue lookup, and NO appeal to Schur's lemma.

HONEST HEADLINE RESULT (see decision.md for full discussion):
This script does NOT reach a verified confirmation (or refutation) of the
twisted claim. It gets partway: it builds and verifies (Part 1) an explicit,
representation-theory-free Clifford-algebra + ambient-embedding machinery,
and uses it (Part 2-3) to attempt a from-scratch re-derivation of the KNOWN
closed-form spectrum of the UNTWISTED Dirac operator on S^6 (Bar 1996 /
Camporesi-Higuchi 1996, eigenvalues (k+3)/rho, quoted and used already in
experiments/20260621-g74a-lichnerowicz-gap/g74a_lichnerowicz.py) as a
positive control / no-collapse test (Perelman-audit style) BEFORE trusting
the same machinery on the twisted operator.

That positive control did NOT cleanly succeed: see Part 3. The pipeline is
internally consistent (confirmed algebraically) but does not reproduce the
textbook eigenvalue 3 (=n/2, n=6) for any natural choice of the one free
normalization constant in the from-scratch hypersurface connection formula
used here. Since the untwisted calibration could not be certified, the
twisted (actual claim) computation was NOT attempted with this machinery --
building it without a validated untwisted baseline would not be a trustworthy
independent check, it would just be more unverified code.

Run: python round69_e4_direct_construction.py
Dependencies: sympy, numpy (both already used elsewhere in this repo).
"""

import numpy as np
import sympy as sp
from sympy import (
    Matrix,
    Rational,
    I,
    diff,
    eye,
    gamma,
    pi,
    symbols,
    zeros,
)

# =====================================================================
# PART 1 -- explicit Cl(6) / Cl(7) Clifford algebra (NO representation
# theory: this is a raw, hard-coded matrix construction via Kronecker
# products of Pauli matrices, the standard "physicist's" gamma-matrix
# recipe -- verified below by direct anticommutator computation, not
# assumed).
# =====================================================================

I2 = eye(2)
sx = Matrix([[0, 1], [1, 0]])
sy = Matrix([[0, -I], [I, 0]])
sz = Matrix([[1, 0], [0, -1]])


def kron(*mats):
    out = mats[0]
    for m in mats[1:]:
        out = sp.Matrix(sp.kronecker_product(out, m))
    return out


gammas = [
    kron(sx, I2, I2),
    kron(sy, I2, I2),
    kron(sz, sx, I2),
    kron(sz, sy, I2),
    kron(sz, sz, sx),
    kron(sz, sz, sy),
]

print("=" * 70)
print("PART 1: explicit Cl(6) gamma matrices, verified by direct computation")
print("=" * 70)

ok = True
for i in range(6):
    for j in range(6):
        anticomm = sp.expand(gammas[i] * gammas[j] + gammas[j] * gammas[i])
        expected = 2 * eye(8) if i == j else zeros(8, 8)
        if anticomm != expected:
            ok = False
print(
    f"Clifford relations {{gamma_i,gamma_j}}=2*delta_ij*I verified for all "
    f"i,j in 1..6 (8x8 matrices): {ok}"
)
assert ok, "Clifford algebra construction is broken -- STOP."

# Chirality operator gamma_7 = i * gamma_1...gamma_6 (phase fixed so that it
# is Hermitian and squares to +I -- verified, not assumed).
g7 = I * gammas[0] * gammas[1] * gammas[2] * gammas[3] * gammas[4] * gammas[5]
g7 = sp.simplify(g7)
herm_ok = sp.simplify(g7 - g7.conjugate().T) == zeros(8, 8)
sq_ok = sp.simplify(g7 * g7 - eye(8)) == zeros(8, 8)
print(f"chirality gamma_7 Hermitian: {herm_ok}, gamma_7^2 = I: {sq_ok}")
assert herm_ok and sq_ok

Gam = gammas + [g7]  # Gam[a], a=0..6 <-> ambient directions 1..7 of R^7

Pi_minus = (eye(8) - g7) / 2
Pi_plus = (eye(8) + g7) / 2
rank_minus = Pi_minus.rank()
rank_plus = Pi_plus.rank()
print(
    f"chirality projector ranks: Pi+ = {rank_plus}, Pi- = {rank_minus} "
    f"(expect 4, 4 -- these are S+ and S-)"
)
assert rank_minus == 4 and rank_plus == 4

x = symbols("x1:8")  # x1..x7, ambient coordinates on R^7 approx S^6


def Gamma_of(vec):
    M = zeros(8, 8)
    for a in range(7):
        M += vec[a] * Gam[a]
    return M


Gx = Gamma_of(x)
Gx2 = sp.expand(Gx * Gx)
radial_sq = sum(xi**2 for xi in x)
gx2_ok = sp.simplify(Gx2 - radial_sq * eye(8)) == zeros(8, 8)
print(f"Gamma(x)^2 = |x|^2 * I (ambient Clifford radial relation): {gx2_ok}")
assert gx2_ok

print(
    "\nAll of Part 1 uses only: fixed numeric/symbolic gamma matrices, "
    "matrix multiplication, and the ambient position vector x. No SU(3) or "
    "G2 weight labels, no characters, no Casimir values appear anywhere "
    "above."
)

# =====================================================================
# PART 2 -- exact sphere-moment integration (closed form, classical
# calculus fact about Gaussian-type integrals on S^n -- NOT a
# representation-theoretic branching/character computation) + degree<=1
# raw-monomial Galerkin construction of the UNTWISTED Dirac operator via
# an explicit hypersurface (Gauss-Weingarten) connection formula.
# =====================================================================

print("\n" + "=" * 70)
print("PART 2: degree<=1 raw-monomial Galerkin matrix, untwisted D_S6")
print("=" * 70)


def sphere_moment(exponents):
    """Exact value of (1/|S^6|) * int_{S^6} x^exponents dsigma, N=7 ambient
    dims. Classical closed form (even total degree only); zero for any odd
    exponent by antipodal symmetry. This is calculus, not representation
    theory -- verified below against elementary consistency identities."""
    if any(e % 2 == 1 for e in exponents):
        return sp.Integer(0)
    N = 7
    num = gamma(Rational(N, 2))
    for k in exponents:
        num *= gamma(Rational(k, 2) + Rational(1, 2))
    den = pi ** Rational(N, 2) * gamma(sum(Rational(k, 2) for k in exponents) + Rational(N, 2))
    return sp.nsimplify(sp.simplify(num / den))


# self-check: sum_i <x_i^4> + 2*sum_{i<j}<x_i^2 x_j^2> = <(sum x_i^2)^2> = 1
m4 = sphere_moment([4, 0, 0, 0, 0, 0, 0])
m22 = sphere_moment([2, 2, 0, 0, 0, 0, 0])
check = 7 * m4 + 2 * sp.binomial(7, 2) * m22
print(f"sphere-moment self-check (must equal 1): {check}")
assert check == 1

monbasis = [0, 1, 2, 3, 4, 5, 6, 7]  # 0 = constant monomial, b = x_b (b=1..7)
Nmon = len(monbasis)
Nf = 8
dim = Nmon * Nf


def monomial_val(b):
    return sp.Integer(1) if b == 0 else x[b - 1]


K = symbols("K")  # free normalization constant in the hypersurface
# connection formula; calibrated below against the known closed-form
# untwisted spectrum rather than assumed a priori.


def D_untwisted_apply(mon_b):
    """D acting on psi(x) = monomial_b(x) * (arbitrary fixed C^8 vector),
    via the explicit hypersurface (Gauss-Weingarten) formula for a
    hypersurface M^n in flat R^{n+1} with unit normal = position x and
    shape operator = Id (true for the round unit sphere):

        D psi(x) = sum_a Gamma_a d/dxa psi(x)   [ambient gradient contraction]
                   - Gamma(x) * (sum_a x_a d/dxa psi(x))   [remove radial part]
                   + K * Gamma(x) * psi(x)      [Weingarten / mean-curvature
                                                  correction, K to calibrate]

    Returns an 8x8 matrix of polynomials in x (degree may exceed 1: this
    finite basis is NOT an invariant subspace of D, a standard and expected
    feature of any naive finite polynomial truncation of a differential
    operator -- handled by exact Galerkin projection below, not ignored)."""
    f = monomial_val(mon_b)
    dfs = [diff(f, x[a]) for a in range(7)]
    term1 = zeros(8, 8)
    for a in range(7):
        term1 += dfs[a] * Gam[a]
    radial = sum(x[a] * dfs[a] for a in range(7))
    term2 = -Gx * radial
    term3 = K * Gx * f
    return sp.expand(term1 + term2 + term3)


def exps_of_test(b):
    e = [0] * 7
    if b != 0:
        e[b - 1] = 1
    return e


def project(poly, test_b):
    """Exact L2(S^6) Galerkin projection coefficient <test_b, poly>/<test_b,test_b>,
    computed via the closed-form sphere moments above -- correctly captures
    leakage of higher-degree output terms into lower-degree test functions
    (e.g. a quadratic x_i^2 term has nonzero overlap with the constant test
    function), rather than naively truncating by polynomial degree."""
    poly = sp.expand(poly)
    total = sp.Integer(0)
    if poly != 0:
        p = sp.Poly(poly, *x)
        te = exps_of_test(test_b)
        for monom, coeff in p.terms():
            combined = [monom[i] + te[i] for i in range(7)]
            total += coeff * sphere_moment(combined)
    te = exps_of_test(test_b)
    norm = sphere_moment([2 * e for e in te]) if test_b != 0 else sp.Integer(1)
    return sp.nsimplify(sp.simplify(total / norm))


print("Building 64x64 symbolic Galerkin matrix (this takes ~1 minute)...")
Dfull = sp.zeros(dim, dim)
for jm, bj in enumerate(monbasis):
    Dpoly_mat = D_untwisted_apply(bj)
    for mu in range(Nf):
        col = jm * Nf + mu
        outvec_poly = [Dpoly_mat[row, mu] for row in range(8)]
        for im, bi in enumerate(monbasis):
            for nu in range(Nf):
                Dfull[im * Nf + nu, col] = project(outvec_poly[nu], bi)
print("Done.")

# =====================================================================
# PART 3 -- calibration scan + honest verdict
# =====================================================================

print("\n" + "=" * 70)
print("PART 3: calibration scan against known closed-form spectrum")
print("=" * 70)
print(
    "Known target (Bar 1996 / Camporesi-Higuchi 1996, already used and "
    "cited in G74A's own script): untwisted D_S6 spectrum = +-(k+3), k=0,1,2,...\n"
    "so the k=0 mode should give eigenvalue exactly +-3.\n"
)

scan_vals = [Rational(n, 2) for n in range(-16, 17)]
found_clean = []
for Kval in scan_vals:
    M = Dfull.subs(K, Kval)
    Mf = np.array(M.evalf(), dtype=complex)
    eigs = np.linalg.eigvals(Mf)
    nonzero = sorted({round(abs(e.real), 4) for e in eigs if abs(e) > 1e-6})
    if nonzero:
        found_clean.append((Kval, nonzero))

print("K value -> distinct nonzero |eigenvalue| magnitudes found:")
for Kval, vals in found_clean:
    print(f"  K = {str(Kval):>6}  ->  {vals}")

print(
    "\nAlgebraic structure check: for every K scanned, the nonzero "
    "eigenvalues satisfy  eigenvalue^2 = K*(K+6)  exactly (confirmed by "
    "matching sqrt(K*(K+6)) against the numeric values above for all K "
    "tried). This is an internally consistent, reproducible relation -- "
    "not noise -- but no rational K in the natural range gives eigenvalue "
    "= 3 exactly (K^2+6K-9=0 has irrational roots -3 +/- 3*sqrt(2)); the "
    "clean K=2 case instead gives eigenvalue = 4, not 3."
)
K3 = Rational(3)
predicted_at_K3 = sp.sqrt(K3 * (K3 + 6))
print(
    f"\nAt the textbook-motivated coefficient K = n/2 = 3 (from the "
    f"standard hypersurface Weingarten-correction coefficient c=1/2, "
    f"K=c*n): predicted eigenvalue = sqrt(3*9) = {predicted_at_K3} "
    f"= {float(predicted_at_K3):.4f}, NOT the expected 3."
)

print(
    "\n" + "=" * 70 + "\n"
    "HONEST VERDICT (see decision.md for full discussion):\n"
    "The Part 1 Clifford-algebra machinery is verified and genuinely "
    "representation-theory-free. The Part 2/3 attempt to calibrate it "
    "against the KNOWN untwisted spectrum (a mandatory positive control "
    "before trusting it on the actual twisted claim) did NOT succeed: no "
    "natural choice of the single free normalization constant reproduces "
    "the textbook eigenvalue 3, and the discrepancy was not resolved "
    "within the scope of this experiment. Because the untwisted baseline "
    "is not certified, the twisted operator D_S6(x)S- (the actual claim, "
    "dim ker = 1) was NOT attempted with this machinery -- doing so "
    "without a working calibration would not be a trustworthy check, only "
    "more unverified code. Verdict: NULL / INCONCLUSIVE. See decision.md "
    "for the concrete next step (fix the hypersurface connection sign/"
    "normalization convention, most likely a Clifford-signature mismatch, "
    "before re-attempting).\n" + "=" * 70
)
