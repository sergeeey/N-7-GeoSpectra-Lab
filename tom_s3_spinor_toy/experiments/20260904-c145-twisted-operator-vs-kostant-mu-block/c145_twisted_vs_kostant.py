r"""
C145 -- does C139/C141's physicist-style twisted Dirac operator D' (Leibniz
rule, BOTH factors -- Sigma AND the twist bundle W -- carry their OWN
Levi-Civita/Nomizu covariant derivative) coincide with Kostant/Landweber's
algebraic twisted operator D_mu, restricted to the trivial G2-representation
block (lambda=0) that is exactly what these rounds compute (the SU(3)-
invariant sector of Sigma (x) W)?

STRUCTURAL PREDICTION, derived from Landweber's own equations (same argument
as C144): D_mu|_{V_0} = c(v) (x) Id_W EXACTLY -- Kostant's r(X_i) term
vanishes identically on the trivial G-rep REGARDLESS of which H-representation
mu=W is being twisted by, because r(X_i) differentiates the L^2(G) factor
only and a constant function's Lie derivative is always zero. So Kostant's
own twisted operator, at lambda=0, is a PURE algebraic operator that gives W
NO connection/dynamics of its own at all -- it enters only as a passive
identity factor.

C139's own D' = Sum_i E_i.NAB_Sigma[i] (x) Id_W  +  Sum_i E_i (x) conn_W[i],
with conn_W[i] = rho_vector(NOMIZU[i]) -- W's OWN, explicitly nonzero,
Levi-Civita Nomizu connection (same NOMIZU data as Sigma, different
representation of so(6)). By C144 (already verified, reused unmodified here):
Sum_i E_i.NAB_Sigma[i] = D_Sigma = (sqrt(3)/4) c(v) EXACTLY. So:

    D' = (sqrt(3)/4) c(v) (x) Id_W  +  Sum_i E_i (x) conn_W[i]

This script tests, directly and symbolically, whether the SECOND term
(the part Kostant's own operator does NOT have) is zero or not. If zero,
C139/C141's D' literally IS an instance of Kostant/Landweber's D_mu, and
Slebarski's closed-form kernel theorem applies directly. If nonzero, D' is
a GENUINELY MORE GENERAL construction than Kostant's -- an honest, testable
negative result, not previously distinguishable from "just twisted Dirac
operator, presumably Kostant's" without this computation.

Reuses round59_route_a_independent.py's build_clifford/spin_lift/NOMIZU
unmodified (same objects C139 itself imports and uses), and C139's own
bivec_to_6x6_sympy/rho_vector_sympy formula (transcribed here, credited,
not re-derived independently -- this round's OWN contribution is the
comparison against c(v), not a new W-connection construction).

Run:  python c145_twisted_vs_kostant.py
"""

import importlib.util
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
R59_PATH = (
    HERE.parent / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py"
)
C73B_PATH = (
    HERE.parent
    / "20260811-c73b-torsion-family-genuine-deformation-and-twist-control"
    / "c73b_torsion_family.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


R59 = load_module("round59_route_a_independent", R59_PATH)

sqrt3 = sp.sqrt(3)

# ---------------------------------------------------------------------------
# STEP 1 -- round59's own Clifford algebra + Levi-Civita Nomizu operators
# (imported directly, byte-identical to what C139 itself imports and uses).
# ---------------------------------------------------------------------------
E = R59.build_clifford(conj=False)
NAB_SIGMA = {i: R59.spin_lift(R59.NOMIZU[i], E) for i in range(1, 7)}

calib_ok, _ = R59.run_calibration(E, R59.NOMIZU)
assert calib_ok, "round59's own Killing-spinor calibration failed on import -- STOP"
print("STEP 1  round59's own Clifford + Nomizu machinery imported, calibration re-verified  [OK]")

D_SIGMA = sp.simplify(sum((E[i] * NAB_SIGMA[i] for i in range(1, 7)), sp.zeros(8, 8)))

# ---------------------------------------------------------------------------
# STEP 2 -- C144's own already-verified c(v) (Chevalley-quantized cubic
# Clifford term), rebuilt here from the SAME raw Lam data (verbatim from
# C144's own script) so this file is self-contained and independently
# re-checks C144's D_Sigma = (sqrt(3)/4) c(v) identity as a regression gate
# before using it in the twisted comparison below.
# ---------------------------------------------------------------------------
Lam = {
    1: [(sp.Rational(1, 1), 3, 6), (sp.Rational(1, 1), 4, 5)],
    2: [(sp.Rational(1, 1), 3, 5), (sp.Rational(-1, 1), 4, 6)],
    3: [(sp.Rational(-1, 1), 1, 6), (sp.Rational(-1, 1), 2, 5)],
    4: [(sp.Rational(-1, 1), 1, 5), (sp.Rational(1, 1), 2, 6)],
    5: [(sp.Rational(1, 1), 1, 4), (sp.Rational(1, 1), 2, 3)],
    6: [(sp.Rational(1, 1), 1, 3), (sp.Rational(-1, 1), 2, 4)],
}
C_ijk = {(i, j, k): sp.Integer(0) for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)}
for i in range(1, 7):
    for coeff, a, b in Lam[i]:
        C_ijk[(i, a, b)] = coeff
        C_ijk[(i, b, a)] = -coeff

antisym_ok = all(
    sp.simplify(C_ijk[(i, j, k)] - C_ijk[(j, k, i)]) == 0
    and sp.simplify(C_ijk[(i, j, k)] + C_ijk[(j, i, k)]) == 0
    for i in range(1, 7)
    for j in range(1, 7)
    for k in range(1, 7)
)
assert antisym_ok, "C144 regression: total antisymmetry check failed on import -- STOP"

c_v = sp.zeros(8, 8)
for i in range(1, 7):
    for j in range(i + 1, 7):
        for k in range(j + 1, 7):
            coeff = C_ijk[(i, j, k)]
            if coeff != 0:
                c_v += coeff * (E[i] * E[j] * E[k])
c_v = sp.simplify(c_v)

alpha = sp.Rational(1, 1)
for r in range(8):
    for cc in range(8):
        if sp.simplify(c_v[r, cc]) != 0:
            alpha = sp.simplify(D_SIGMA[r, cc] / c_v[r, cc])
            break
    else:
        continue
    break

regression_ok = sp.simplify(D_SIGMA - alpha * c_v) == sp.zeros(8, 8)
print(f"STEP 2  C144 regression: D_Sigma == alpha*c(v) exactly, alpha={alpha}: {regression_ok}")
assert regression_ok, "C144 regression FAILED -- STOP, do not proceed to twisted comparison"
assert sp.simplify(alpha - sqrt3 / 4) == 0, f"alpha changed from C144's sqrt(3)/4: got {alpha}"

# ---------------------------------------------------------------------------
# STEP 3 -- W = m_C (6-dim vector/tangent rep of so(6)), C139's own
# construction (bivec_to_6x6 + sign-corrected rho_vector), rebuilt here in
# exact sympy arithmetic from the SAME NOMIZU data, transcribed from C139's
# own bivec_to_6x6_sympy/rho_vector_sympy (formula credited, not altered).
# ---------------------------------------------------------------------------


def bivec_to_6x6_sympy(terms):
    mat = sp.zeros(6, 6)
    for coeff, a, b in terms:
        i, j = a - 1, b - 1
        mat[i, j] += coeff
        mat[j, i] -= coeff
    return mat


def rho_vector_sympy(terms):
    """C139's own sign-corrected vector-rep lift (decision.md Sec 3d)."""
    return -bivec_to_6x6_sympy(terms)


CONN_W = {i: rho_vector_sympy(R59.NOMIZU[i]) for i in range(1, 7)}
print("STEP 3  W = m_C (6-dim) Nomizu connection built from the same NOMIZU data  [done]")

nonzero_conn = any(CONN_W[i] != sp.zeros(6, 6) for i in range(1, 7))
print(f"STEP 3  sanity: at least one conn_W[i] is nonzero: {nonzero_conn}")

# ---------------------------------------------------------------------------
# STEP 4 -- the decisive test.  D' = D_Sigma (x) Id_W + Sum_i E_i (x) conn_W[i]
# (C139's own construction, Leibniz rule).  Kostant/Landweber's candidate is
# D_mu|_{V_0} = alpha * c(v) (x) Id_W  (NO connection term on W at all, per
# the structural argument in this file's own docstring).  Compare.
# ---------------------------------------------------------------------------
I6 = sp.eye(6)


def kron(a, b):
    return sp.Matrix(sp.kronecker_product(a, b))


D_PRIME = kron(D_SIGMA, I6)
for i in range(1, 7):
    D_PRIME += kron(E[i], CONN_W[i])
D_PRIME = sp.simplify(D_PRIME)

KOSTANT_CANDIDATE = sp.simplify(alpha * kron(c_v, I6))

RESIDUAL = sp.simplify(D_PRIME - KOSTANT_CANDIDATE)
residual_is_zero = RESIDUAL == sp.zeros(48, 48)
print()
print("=" * 78)
print("STEP 4  DECISIVE TEST")
print("=" * 78)
print(
    f"  D'  ==  alpha * c(v) (x) Id_W   (i.e. D' is literally Kostant's D_mu|_V0): "
    f"{residual_is_zero}"
)

# The residual should, by construction, equal EXACTLY the extra term
# Sum_i E_i (x) conn_W[i] (since D_Sigma (x) Id_W == alpha*c(v)(x)Id_W by
# STEP 2's own regression check) -- verify this identification directly,
# not just assert it.
EXTRA_TERM = sp.zeros(48, 48)
for i in range(1, 7):
    EXTRA_TERM += kron(E[i], CONN_W[i])
EXTRA_TERM = sp.simplify(EXTRA_TERM)
extra_matches_residual = sp.simplify(EXTRA_TERM - RESIDUAL) == sp.zeros(48, 48)
print(f"  residual EXACTLY equals Sum_i E_i (x) conn_W[i] (as predicted): {extra_matches_residual}")

n_nonzero_residual = sum(
    1 for r in range(48) for cc in range(48) if sp.simplify(RESIDUAL[r, cc]) != 0
)
print(f"  nonzero entries in residual (out of 48x48=2304): {n_nonzero_residual}")

# Rough size comparison: is the extra term "small" relative to the matched
# part, or comparable in size?  (Frobenius-norm-squared, exact rational/
# radical arithmetic, no floating point.)
frob_kostant_sq = sp.simplify(
    sum(
        KOSTANT_CANDIDATE[r, cc] * sp.conjugate(KOSTANT_CANDIDATE[r, cc])
        for r in range(48)
        for cc in range(48)
    )
)
frob_extra_sq = sp.simplify(
    sum(EXTRA_TERM[r, cc] * sp.conjugate(EXTRA_TERM[r, cc]) for r in range(48) for cc in range(48))
)
print(f"  ||alpha*c(v)(x)Id_W||_F^2 = {frob_kostant_sq}")
print(f"  ||extra term||_F^2       = {frob_extra_sq}")
print(
    f"  ratio extra/kostant (size comparison, not a proof of anything): "
    f"{sp.simplify(frob_extra_sq / frob_kostant_sq) if frob_kostant_sq != 0 else 'N/A'}"
)

print()
print("=" * 78)
print("SUMMARY")
print("=" * 78)
if residual_is_zero:
    print("  C139/C141's twisted operator D' IS an instance of Kostant/Landweber's")
    print("  D_mu|_{V_0} -- Slebarski's closed-form kernel theorem applies directly.")
else:
    print("  C139/C141's twisted operator D' is NOT literally Kostant/Landweber's")
    print("  D_mu|_{V_0} -- it carries a genuinely EXTRA term (the twist bundle's own")
    print("  Levi-Civita connection, which Kostant's own construction does not have")
    print("  at lambda=0, since r(X_i) kills it there regardless of the H-rep chosen).")
    print("  Slebarski's theorem does NOT directly resolve C142's W_cand question via")
    print("  this route; C139/C141's construction is a more general 'physicist-style'")
    print("  twisted Dirac operator (own connection on W), not Kostant's group-theoretic")
    print("  one (W as a passive label with no connection at lambda=0).")
