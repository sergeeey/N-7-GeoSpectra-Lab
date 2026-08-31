"""C119: is the Bismut-Ricci-flat condition  Rc(g) = (1/4) H_g^2  (with H
closed and g-harmonic) applicable to this project's FROZEN S^3 x S^6
background?  PARENT_ACTION_GATE.md field F1 only.

Definition tested, quoted verbatim from Lauret-Will arXiv:2301.02335
(abstract, tool-verified 2026-08-31) and Gutierrez arXiv:2401.03332:

    "A generalized metric on a manifold M, i.e. a pair (g,H), where g is a
     Riemannian metric and H a CLOSED 3-form, is a fixed point of the
     generalized Ricci flow if and only if (g,H) is Bismut Ricci flat:
     H is g-harmonic and ric(g) = (1/4) H_g^2."

Here  (H^2)_{ab} := sum_{c,d} H_{acd} H_{bcd}  in an orthonormal frame.

Everything below is exact (sympy Rationals / sqrt(3)); no floating point
enters any verdict-bearing quantity.

PART 0  S^3 factor, re-derived from scratch, cross-checked against
        round111's own certified Ric^t = 8t(1-t) delta.
PART 1  S^6 factor, using THIS PROJECT'S OWN certified torsion table
        (g2su3_H_element.build_T_table) and its own certified Ric = 5/3.
PART 2  identification of the project's S^6 torsion with the standard
        SU(3)-structure form psi^- (independent structural check).
PART 3  dT_{S^6}: two independent routes (Chevalley-Eilenberg differential
        for invariant forms on a reductive homogeneous space, from the
        project's own structure constants; and the algebraic sigma_T
        identity for parallel torsion).
PART 4  the PRODUCT: explicit 9-dimensional index sums for (H_tot^2),
        including the cross blocks (verified, not assumed).
PART 5  Bianchi / harmonicity of H_tot on the product.
PART 6  rescue attempts: (a) exhaustion over ALL G2-invariant 3-forms on the
        frozen S^6; (b) a topological (Hodge + Kunneth) no-go independent of
        the torsion, of t, and of both radii.
PART 7  one named, scoped relaxation (constant-lambda / "soliton-shaped"),
        recorded because it is the first thing a reader will propose.

Run:  python c119_bismut_ricci_flat_product_check.py
"""

from __future__ import annotations

import itertools
import json
import os
import platform
import sys
from pathlib import Path

import sympy as sp

# --- import the project's OWN certified S^6 torsion table (Gate 1: the
# --- object tested is provably the frozen one, not a re-typed textbook
# --- copy). sys.path.insert before the import is required here, not
# --- stylistic: g2su3_H_element.py itself does sibling top-level imports
# --- (e.g. `from g2su3_explicit_clifford import ...`) that only resolve
# --- if its own directory is on sys.path -- an importlib.util file-path
# --- load (tried first, reverted after ModuleNotFoundError) bypasses
# --- sys.path and breaks those.
_G2SU3 = Path(__file__).resolve().parents[1] / "20260708-dolan-casimir-g2su3"
sys.path.insert(0, str(_G2SU3))
from g2su3_H_element import build_T_table  # noqa: E402

RESULTS: dict[str, object] = {}
SEP = "=" * 92


# ----------------------------------------------------------------------
# generic exact multilinear-form helpers (dense dicts on index tuples)
# ----------------------------------------------------------------------
def basis_form(indices, n):
    """The decomposable p-form e^{i1} ^ ... ^ e^{ip} as a dict on p-tuples.

    Determinant convention: value on (j1..jp) is sgn of the permutation
    taking (i1..ip) to (j1..jp), or 0 if not a permutation.
    """
    p = len(indices)
    out = {}
    for perm in itertools.permutations(range(p)):
        key = tuple(indices[perm[k]] for k in range(p))
        out[key] = sp.Integer(perm_sign(perm))
    del n
    return out


def perm_sign(perm):
    """Sign of a permutation given as a tuple of images."""
    perm = list(perm)
    sign = 1
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                sign = -sign
    return sign


def add_forms(*forms):
    out: dict = {}
    for f in forms:
        for k, v in f.items():
            out[k] = sp.expand(out.get(k, 0) + v)
    return {k: v for k, v in out.items() if v != 0}


def scale_form(f, c):
    return {k: sp.expand(c * v) for k, v in f.items() if sp.expand(c * v) != 0}


def form_get(f, key):
    return f.get(tuple(key), sp.Integer(0))


def square_tensor(H, n, degree=3):
    """(H^2)_{ab} = sum over the last (degree-1) indices of H_{a...} H_{b...}."""
    M = sp.zeros(n, n)
    rest = list(itertools.product(range(n), repeat=degree - 1))
    for a in range(n):
        for b in range(n):
            s = sp.Integer(0)
            for r in rest:
                va = form_get(H, (a,) + r)
                if va == 0:
                    continue
                vb = form_get(H, (b,) + r)
                if vb == 0:
                    continue
                s += va * vb
            M[a, b] = sp.simplify(s)
    return M


def wedge22(beta, gamma, n):
    """Wedge of two 2-forms, (1/(2!2!)) sum_{sigma in S_4} sgn(sigma) ..."""
    out = {}
    perms = list(itertools.permutations(range(4)))
    for idx in itertools.product(range(n), repeat=4):
        s = sp.Integer(0)
        for perm in perms:
            sg = perm_sign(perm)
            b = form_get(beta, (idx[perm[0]], idx[perm[1]]))
            if b == 0:
                continue
            g = form_get(gamma, (idx[perm[2]], idx[perm[3]]))
            if g == 0:
                continue
            s += sg * b * g
        s = sp.expand(s / 4)
        if s != 0:
            out[idx] = s
    return out


def d_invariant(alpha, p, C, n):
    """Exterior derivative of a G-invariant p-form on a reductive
    homogeneous space G/H, evaluated at the base point:

        d alpha(X_0..X_p) = sum_{i<j} (-1)^{i+j}
                            alpha([X_i,X_j]_m, X_0..^X_i..^X_j..X_p)

    C[i][j][k] = coefficient of Z_k in [Z_i,Z_j]_m.  (Valid for
    Ad(H)-invariant alpha; d^2 = 0 on such alpha is used below as the
    validity test, since [.,.]_m alone does NOT satisfy Jacobi.)
    """
    out = {}
    for idx in itertools.product(range(n), repeat=p + 1):
        val = sp.Integer(0)
        for i in range(p + 1):
            for j in range(i + 1, p + 1):
                rest = tuple(idx[k] for k in range(p + 1) if k not in (i, j))
                sg = (-1) ** (i + j)
                inner = sp.Integer(0)
                for k in range(n):
                    c = C[idx[i]][idx[j]][k]
                    if c == 0:
                        continue
                    a = form_get(alpha, (k,) + rest)
                    if a == 0:
                        continue
                    inner += c * a
                if inner != 0:
                    val += sg * inner
        val = sp.expand(val)
        if val != 0:
            out[idx] = val
    return out


def hodge_star_3form_6d(alpha):
    """Hodge star on 3-forms in 6d with vol = e^{123456} (0-indexed 0..5)."""
    out: dict = {}
    for triple in itertools.combinations(range(6), 3):
        coeff = form_get(alpha, triple)
        if coeff == 0:
            continue
        comp = tuple(i for i in range(6) if i not in triple)
        sg = perm_sign_of_sequence(list(triple) + list(comp))
        out = add_forms(out, scale_form(basis_form(comp, 6), sg * coeff))
    return out


def perm_sign_of_sequence(seq):
    """Sign of the permutation sorting seq (a permutation of 0..len-1)."""
    order = sorted(range(len(seq)), key=lambda i: seq[i])
    return perm_sign(tuple(order))


def nonzero_sorted(f, p):
    return {k: v for k, v in f.items() if list(k) == sorted(k) and len(set(k)) == p}


# ======================================================================
print(SEP)
print("PART 0 -- S^3 factor, re-derived from scratch (NOT inherited)")
print(SEP)

t = sp.symbols("t", real=True)


def pauli():
    return [
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        sp.Matrix([[1, 0], [0, -1]]),
    ]


Z3 = [sp.I * s for s in pauli()]  # same generators as round111's e34 script


def br(A, B):
    return sp.simplify(A * B - B * A)


def inner3(X, Y):
    return sp.simplify(-sp.Rational(1, 2) * sp.trace(X * Y))


met3 = sp.Matrix(3, 3, lambda i, j: inner3(Z3[i], Z3[j]))
print(f"  metric <Z_i,Z_j> == I (orthonormal frame)? {met3 == sp.eye(3)}")

# structure constants  [Z_i,Z_j] = c_ijk Z_k
C3 = [[[inner3(br(Z3[i], Z3[j]), Z3[k]) for k in range(3)] for j in range(3)] for i in range(3)]
c0 = C3[0][1][2]
print(f"  [Z_1,Z_2] = c0 * Z_3 with c0 = {c0}   (project convention c0 = -2)")

# Cartan-Schouten torsion  T^t(X,Y) = (2t-1)[X,Y];  H_{ijk} = <T(Z_i,Z_j),Z_k>
H3 = {}
for i, j, k in itertools.product(range(3), repeat=3):
    v = sp.expand((2 * t - 1) * C3[i][j][k])
    if v != 0:
        H3[(i, j, k)] = v
print(f"  H_{{S3}}(0,1,2) = {H3[(0, 1, 2)]}   (= (2t-1)*c0 = -2(2t-1))")

H3sq = square_tensor(H3, 3)
print(
    f"  (H_S3^2)_ab = {sp.simplify(H3sq[0, 0])} * delta   (off-diag zero: "
    f"{all(H3sq[a, b] == 0 for a in range(3) for b in range(3) if a != b)})"
)


# Levi-Civita Ricci from the Killing form (round111's own independent route)
def ad3(X):
    M = sp.zeros(3, 3)
    for b in range(3):
        comm = br(X, Z3[b])
        for a in range(3):
            M[a, b] = inner3(Z3[a], comm)
    return M


ad = [ad3(Z3[i]) for i in range(3)]
Killing3 = sp.Matrix(3, 3, lambda a, b: sp.simplify(sp.trace(ad[a] * ad[b])))
Ric3 = sp.simplify(-sp.Rational(1, 4) * Killing3)
print(
    f"  Ric_LC(S^3) = {Ric3[0, 0]} * delta ,  Scal_LC = {sp.trace(Ric3)}  (round111: Scal_LC = 6)"
)

bismut_defect_S3 = sp.simplify(Ric3[0, 0] - sp.Rational(1, 4) * H3sq[0, 0])
print(f"  Rc - (1/4)H^2  on S^3  =  {sp.factor(bismut_defect_S3)} * delta")


# MANDATORY cross-check against round111's own certified Ric^t = 8t(1-t) delta,
# recomputed here from round99's R^t (a genuinely different route).
def R_t(X, Y, W):
    return sp.expand(t * (t - 1) * br(br(X, Y), W))


Ricci_t = sp.zeros(3, 3)
for a in range(3):
    for b in range(3):
        Ricci_t[a, b] = sp.simplify(sum(inner3(R_t(Z3[c], Z3[a], Z3[b]), Z3[c]) for c in range(3)))
round111_match = sp.simplify(Ricci_t[0, 0] - bismut_defect_S3) == 0
print(f"  round111's Ric^t (from R^t route) = {sp.factor(Ricci_t[0, 0])} * delta")
print(
    f"  *** Rc - (1/4)H^2  ==  Ric^t  EXACTLY?  {round111_match}   "
    f"(cross-check; FALSE => substrate failure, not a finding)"
)

t_roots = sp.solve(sp.Eq(bismut_defect_S3, 0), t)
print(f"  Bismut-Ricci-flat on S^3 alone  <=>  t in {t_roots}")
rho_S3 = sp.simplify(Ric3[0, 0] / (sp.Rational(1, 4) * H3sq[0, 0]))
print(f"  rho_S3 = Rc / ((1/4)H^2) = {sp.simplify(rho_S3)}   (= 1 iff (2t-1)^2 = 1)")
print()

RESULTS["S3"] = {
    "c0": str(c0),
    "H_012": str(H3[(0, 1, 2)]),
    "H_squared_diag": str(sp.simplify(H3sq[0, 0])),
    "Ric_LC_diag": str(Ric3[0, 0]),
    "Scal_LC": str(sp.trace(Ric3)),
    "bismut_defect": str(sp.factor(bismut_defect_S3)),
    "equals_round111_Ric_t": bool(round111_match),
    "roots_t": [str(r) for r in t_roots],
    "rho": str(sp.simplify(rho_S3)),
}

# ======================================================================
print(SEP)
print("PART 1 -- S^6 factor, from THIS PROJECT'S OWN certified data")
print(SEP)

Traw = build_T_table()  # 1-indexed dict {(i,j,k): value}
T6 = {}
for (i, j, k), v in Traw.items():
    T6[(i - 1, j - 1, k - 1)] = sp.nsimplify(v)

antisym_ok = True
for (i, j, k), v in T6.items():
    if sp.simplify(form_get(T6, (j, i, k)) + v) != 0:
        antisym_ok = False
    if sp.simplify(form_get(T6, (i, k, j)) + v) != 0:
        antisym_ok = False
print(f"  imported {len(T6)} nonzero components; totally antisymmetric? {antisym_ok}")
print("  nonzero i<j<k components:")
for k_, v in sorted(nonzero_sorted(T6, 3).items()):
    print(f"    T{tuple(x + 1 for x in k_)} = {v}")

sumsq_all = sp.simplify(sum(v**2 for v in T6.values()))
sumsq_ijk = sp.simplify(sum(v**2 for v in nonzero_sorted(T6, 3).values()))
print(f"  sum_{{i,j,k}} T^2 = {sumsq_all} ;  sum_{{i<j<k}} T^2 = ||T||^2 = {sumsq_ijk}")

T6sq = square_tensor(T6, 6)
offdiag_zero = all(T6sq[a, b] == 0 for a in range(6) for b in range(6) if a != b)
diag_const = len({sp.simplify(T6sq[a, a]) for a in range(6)}) == 1
print(
    f"  (T_S6^2)_ab = {sp.simplify(T6sq[0, 0])} * delta   "
    f"(off-diag zero: {offdiag_zero}; diagonal constant: {diag_const})"
)

# The project's OWN certified Ricci for the SAME normalization:
#   experiments/20260708-dolan-casimir-g2su3/decision.md  ~lines 1926-1929
#   "Ric(e_p,e_p)=5/3 (off-diagonal zero) for all tested p ... Scal=10 (trace)"
RIC_S6 = sp.Rational(5, 3)
SCAL_S6 = sp.Integer(10)
assert sp.simplify(6 * RIC_S6 - SCAL_S6) == 0
print(
    f"  Ric(S^6) = {RIC_S6} * delta ,  Scal = {SCAL_S6}   "
    f"[project's own, triple-verified Round 16, SAME normalization as the T table]"
)

# INDEPENDENT literature cross-check of the normalisation:
# for a strict nearly-Kaehler 6-manifold, ||T||^2 = (2/15) Scal^g.
nk_identity_lhs = sumsq_ijk
nk_identity_rhs = sp.Rational(2, 15) * SCAL_S6
nk_identity_ok = sp.simplify(nk_identity_lhs - nk_identity_rhs) == 0
print(
    f"  NK literature identity  ||T||^2 = (2/15) Scal^g :  "
    f"{nk_identity_lhs} vs {nk_identity_rhs}  -> {nk_identity_ok}"
)

bismut_defect_S6 = sp.simplify(RIC_S6 - sp.Rational(1, 4) * T6sq[0, 0])
rho_S6 = sp.simplify(RIC_S6 / (sp.Rational(1, 4) * T6sq[0, 0]))
print(f"  Rc - (1/4)T^2  on S^6  =  {bismut_defect_S6} * delta")
print(f"  rho_S6 = Rc / ((1/4)T^2) = {rho_S6}      <-- must equal 1 for Bismut-Ricci-flat")
scale_needed = sp.sqrt(rho_S6)
print(
    f"  torsion rescaling that WOULD satisfy it: T -> {scale_needed} * T "
    f"(NOT the characteristic connection)"
)

# DECISIVE INDEPENDENT LITERATURE CROSS-CHECK of exactly this number.
# Agricola, "The Srni lectures on non-integrable geometries with torsion",
# arXiv:math/0606705, nearly-Kaehler section (tool-verified 2026-08-31):
#   "any 6-dimensional nearly Kaehler manifold is also nabla-bar-Einstein
#    with  Ric^{nabla-bar} = 2 (scal^g / 15) g"
# Ric^{nabla-bar} is precisely the (symmetric) Ricci of the characteristic
# = Bismut connection, i.e. Rc(g) - (1/4)T^2 (the skew part -(1/2)delta T
# vanishes here because T is parallel/co-closed, verified in PART 3).
# So the literature says outright that the Bismut-Ricci of ANY nearly-Kaehler
# 6-manifold is 2 Scal/15 * g, which is NONZERO whenever Scal > 0 -- i.e.
# no strict nearly-Kaehler 6-manifold is Bismut-Ricci-FLAT.
AGRICOLA_RIC_BISMUT = sp.Rational(2, 15) * SCAL_S6
agricola_match = sp.simplify(AGRICOLA_RIC_BISMUT - bismut_defect_S6) == 0
print(
    f"  literature cross-check (Agricola arXiv:math/0606705): "
    f"Ric^{{nabla-bar}} = 2 Scal/15 = {AGRICOLA_RIC_BISMUT} ; "
    f"computed defect = {bismut_defect_S6}  -> agree? {agricola_match}"
)
print(
    "  => the Bismut-Ricci of a nearly-Kaehler 6-manifold is 2 Scal/15 * g, NEVER zero for Scal > 0"
)
print()

RESULTS["S6"] = {
    "n_nonzero_components": len(T6),
    "agricola_Ric_bismut_2Scal_over_15": str(AGRICOLA_RIC_BISMUT),
    "agricola_matches_computed_defect": bool(agricola_match),
    "totally_antisymmetric": bool(antisym_ok),
    "sum_ijk_T_squared": str(sumsq_all),
    "norm_T_squared_i_lt_j_lt_k": str(sumsq_ijk),
    "T_squared_diag": str(sp.simplify(T6sq[0, 0])),
    "T_squared_offdiag_zero": bool(offdiag_zero),
    "Ric_diag_project_certified": str(RIC_S6),
    "Scal_project_certified": str(SCAL_S6),
    "nk_literature_identity_normT2_eq_2over15_Scal": bool(nk_identity_ok),
    "bismut_defect": str(bismut_defect_S6),
    "rho": str(rho_S6),
    "torsion_rescale_that_would_work": str(scale_needed),
}

# ======================================================================
print(SEP)
print("PART 2 -- structural identification: is the project's S^6 torsion the")
print("standard SU(3)-structure form psi^- ?  (independent check of PART 1)")
print(SEP)

# standard SU(3) structure on R^6 (0-indexed e_0..e_5):
#   omega  = e^{01} + e^{23} + e^{45}
#   Psi    = (e^0 + i e^1) ^ (e^2 + i e^3) ^ (e^4 + i e^5)
#   psi^+  = Re Psi = e^{024} - e^{035} - e^{125} - e^{134}
#   psi^-  = Im Psi = e^{025} + e^{034} + e^{124} - e^{135}
omega = add_forms(basis_form((0, 1), 6), basis_form((2, 3), 6), basis_form((4, 5), 6))
psi_p = add_forms(
    basis_form((0, 2, 4), 6),
    scale_form(basis_form((0, 3, 5), 6), -1),
    scale_form(basis_form((1, 2, 5), 6), -1),
    scale_form(basis_form((1, 3, 4), 6), -1),
)
psi_m = add_forms(
    basis_form((0, 2, 5), 6),
    basis_form((0, 3, 4), 6),
    basis_form((1, 2, 4), 6),
    scale_form(basis_form((1, 3, 5), 6), -1),
)

lam = sp.Rational(1, 1) / sp.sqrt(3)
T_pred = scale_form(psi_m, -lam)
keys = set(T6) | set(T_pred)
identification_ok = all(sp.simplify(form_get(T6, k) - form_get(T_pred, k)) == 0 for k in keys)
print(f"  lambda := 1/sqrt(3) = {sp.nsimplify(lam)}")
print(f"  project's T_S6  ==  -lambda * psi^-  component-by-component?  {identification_ok}")

psq_p = square_tensor(psi_p, 6)
psq_m = square_tensor(psi_m, 6)
print(
    f"  (psi^+ ^2)_ab = {sp.simplify(psq_p[0, 0])} * delta ;  "
    f"(psi^- ^2)_ab = {sp.simplify(psq_m[0, 0])} * delta"
)
print(
    f"  => (T^2) = lambda^2 * 4 * delta = {sp.simplify(lam**2 * 4)} * delta "
    f"(matches PART 1: {sp.simplify(lam**2 * 4 - T6sq[0, 0]) == 0})"
)
print(
    f"  NK theory: Ric = 5 lambda^2 g = {sp.simplify(5 * lam**2)} * delta  "
    f"(matches project's certified 5/3: "
    f"{sp.simplify(5 * lam**2 - RIC_S6) == 0})"
)
print("  => rho_S6 = 5 lambda^2 / lambda^2 = 5, independent of lambda (i.e. of the S^6 radius)")

star_psi_m = hodge_star_3form_6d(psi_m)
star_is_minus_psi_p = all(
    sp.simplify(form_get(star_psi_m, k) + form_get(psi_p, k)) == 0
    for k in set(star_psi_m) | set(psi_p)
)
star_is_plus_psi_p = all(
    sp.simplify(form_get(star_psi_m, k) - form_get(psi_p, k)) == 0
    for k in set(star_psi_m) | set(psi_p)
)
print(
    f"  Hodge:  *psi^- = +psi^+ ? {star_is_plus_psi_p} ;  *psi^- = -psi^+ ? {star_is_minus_psi_p}"
)
print()

RESULTS["S6_identification"] = {
    "T_equals_minus_lambda_psi_minus": bool(identification_ok),
    "lambda": "1/sqrt(3)",
    "psi_plus_squared_diag": str(sp.simplify(psq_p[0, 0])),
    "psi_minus_squared_diag": str(sp.simplify(psq_m[0, 0])),
    "star_psi_minus_is_plus_psi_plus": bool(star_is_plus_psi_p),
    "star_psi_minus_is_minus_psi_plus": bool(star_is_minus_psi_p),
}

# ======================================================================
print(SEP)
print("PART 3 -- is dT_{S^6} = 0 ?   TWO INDEPENDENT ROUTES")
print(SEP)

# structure constants of the reductive complement m:  [Z_i,Z_j]_m = T(i,j,k) Z_k
Cm = [[[form_get(T6, (i, j, k)) for k in range(6)] for j in range(6)] for i in range(6)]

print("  Route A -- Chevalley-Eilenberg differential for invariant forms on a")
print("             reductive homogeneous space, from the project's own")
print("             structure constants [Z_i,Z_j]_m = T(i,j,.)")

d_omega = d_invariant(omega, 2, Cm, 6)
ratio_domega = None
if d_omega:
    k0 = next(iter(sorted(d_omega)))
    if form_get(psi_p, k0) != 0:
        ratio_domega = sp.simplify(d_omega[k0] / form_get(psi_p, k0))
    d_omega_matches = (
        all(
            sp.simplify(form_get(d_omega, k) - ratio_domega * form_get(psi_p, k)) == 0
            for k in set(d_omega) | set(psi_p)
        )
        if ratio_domega is not None
        else False
    )
else:
    d_omega_matches = False
print(
    f"    d(omega) = {ratio_domega} * psi^+  ?  {d_omega_matches}   "
    f"[NK structure equation d omega = 3 lambda psi^+ ; "
    f"3*lambda = {sp.nsimplify(3 * lam)}]"
)

# validity test of the formula on THESE forms: d^2 = 0 (nontrivial -- [.,.]_m
# alone does NOT satisfy Jacobi, so this only holds for Ad(H)-invariant forms)
dd_omega = d_invariant(d_omega, 3, Cm, 6)
print(f"    validity test  d(d omega) == 0 ?  {len(dd_omega) == 0}")

d_psip = d_invariant(psi_p, 3, Cm, 6)
d_psim = d_invariant(psi_m, 3, Cm, 6)
print(f"    d(psi^+) == 0 ?  {len(d_psip) == 0}   (nonzero components: {len(d_psip)})")
print(f"    d(psi^-) == 0 ?  {len(d_psim) == 0}   (nonzero components: {len(d_psim)})")

om_wedge_om = wedge22(omega, omega, 6)
ratio_dpsim = None
dpsim_is_omega2 = False
if d_psim:
    k0 = next(iter(sorted(d_psim)))
    if form_get(om_wedge_om, k0) != 0:
        ratio_dpsim = sp.simplify(d_psim[k0] / form_get(om_wedge_om, k0))
        dpsim_is_omega2 = all(
            sp.simplify(form_get(d_psim, k) - ratio_dpsim * form_get(om_wedge_om, k)) == 0
            for k in set(d_psim) | set(om_wedge_om)
        )
print(
    f"    d(psi^-) = {ratio_dpsim} * (omega ^ omega) ?  {dpsim_is_omega2}   "
    f"[NK structure equation d psi^- = -2 lambda omega^omega ; "
    f"-2*lambda = {sp.nsimplify(-2 * lam)}]"
)

dT_A = d_invariant(T6, 3, Cm, 6)
print(f"    ==> d(T_S6) : {len(dT_A)} nonzero components  -> dT = 0 ?  {len(dT_A) == 0}")

print()
print("  Route B -- algebraic identity for PARALLEL skew torsion (Kirichenko:")
print("             the characteristic torsion of a nearly-Kaehler manifold IS")
print("             parallel):   dT = 2 sigma_T ,  sigma_T = 1/2 sum_i (e_i _| T) ^ (e_i _| T)")
sigma_T: dict = {}
for i in range(6):
    contracted = {}
    for (a, b, c), v in T6.items():
        if a == i:
            contracted[(b, c)] = v
    if contracted:
        sigma_T = add_forms(sigma_T, wedge22(contracted, contracted, 6))
sigma_T = scale_form(sigma_T, sp.Rational(1, 2))
print(f"    sigma_T : {len(sigma_T)} nonzero components -> sigma_T = 0 ? {len(sigma_T) == 0}")

routes_agree = None
ratio_AB = None
if dT_A and sigma_T:
    k0 = next(iter(sorted(dT_A)))
    if form_get(sigma_T, k0) != 0:
        ratio_AB = sp.simplify(dT_A[k0] / form_get(sigma_T, k0))
        routes_agree = all(
            sp.simplify(form_get(dT_A, k) - ratio_AB * form_get(sigma_T, k)) == 0
            for k in set(dT_A) | set(sigma_T)
        )
elif not dT_A and not sigma_T:
    routes_agree = True
    ratio_AB = sp.Integer(0)
print(
    f"    dT (route A) = {ratio_AB} * sigma_T (route B) ?  {routes_agree}   "
    f"[identity predicts the constant 2]"
)

# co-closedness:  delta T = 0  <=>  d(*T) = 0
star_T = hodge_star_3form_6d(T6)
d_star_T = d_invariant(star_T, 3, Cm, 6)
print(
    f"    d(*T) : {len(d_star_T)} nonzero components -> T co-closed "
    f"(delta T = 0) ?  {len(d_star_T) == 0}"
)
print()

dT_is_zero = len(dT_A) == 0
RESULTS["S6_dT"] = {
    "route_A_dT_nonzero_components": len(dT_A),
    "route_A_dT_is_zero": bool(dT_is_zero),
    "route_B_sigma_T_nonzero_components": len(sigma_T),
    "routes_proportional": None if routes_agree is None else bool(routes_agree),
    "route_A_over_route_B_ratio": str(ratio_AB),
    "d_omega_over_psi_plus": str(ratio_domega),
    "d_omega_is_multiple_of_psi_plus": bool(d_omega_matches),
    "dd_omega_is_zero_validity_test": bool(len(dd_omega) == 0),
    "d_psi_plus_is_zero": bool(len(d_psip) == 0),
    "d_psi_minus_over_omega_wedge_omega": str(ratio_dpsim),
    "d_psi_minus_is_multiple_of_omega2": bool(dpsim_is_omega2),
    "d_star_T_nonzero_components": len(d_star_T),
    "T_is_co_closed": bool(len(d_star_T) == 0),
}

# ======================================================================
print(SEP)
print("PART 4 -- the PRODUCT S^3 x S^6: explicit 9-dimensional index sums")
print(SEP)

c3, c6 = sp.symbols("c3 c6", positive=True)  # independent radius scalings
# ON frame of the product: indices 0,1,2 = S^3 ; 3..8 = S^6.
Htot: dict = {}
for (i, j, k), v in H3.items():
    Htot[(i, j, k)] = sp.expand(v / c3)
for (i, j, k), v in T6.items():
    Htot[(i + 3, j + 3, k + 3)] = sp.expand(v / c6)
print(
    f"  H_tot built on 9 indices: {len(Htot)} nonzero components "
    f"({len(H3)} from S^3, {len(T6)} from S^6, 0 cross)"
)

Htot_sq = square_tensor(Htot, 9)
cross_zero = all(Htot_sq[A, B] == 0 for A in range(9) for B in range(9) if (A < 3) != (B < 3))
block3_ok = all(
    sp.simplify(Htot_sq[a, b] - H3sq[a, b] / c3**2) == 0 for a in range(3) for b in range(3)
)
block6_ok = all(
    sp.simplify(Htot_sq[a + 3, b + 3] - T6sq[a, b] / c6**2) == 0 for a in range(6) for b in range(6)
)
print(
    f"  (H_tot^2) cross blocks (S^3 x S^6) all zero -- VERIFIED by explicit "
    f"index sum, not assumed:  {cross_zero}"
)
print(f"  (H_tot^2) S^3 block == (H_S3^2)/c3^2 ? {block3_ok}")
print(f"  (H_tot^2) S^6 block == (T_S6^2)/c6^2 ? {block6_ok}")

# Ricci of a Riemannian product is block diagonal, Ric(M x N) = Ric(M) + Ric(N)
Ric_tot = sp.zeros(9, 9)
for a in range(3):
    Ric_tot[a, a] = Ric3[0, 0] / c3**2
for a in range(6):
    Ric_tot[a + 3, a + 3] = RIC_S6 / c6**2

defect = sp.simplify(Ric_tot - sp.Rational(1, 4) * Htot_sq)
d3 = sp.simplify(defect[0, 0])
d6 = sp.simplify(defect[3, 3])
print(f"  [Rc - (1/4)H^2]  S^3 block = {sp.factor(d3)} * delta_3")
print(f"  [Rc - (1/4)H^2]  S^6 block = {sp.factor(d6)} * delta_6")
print("  cross blocks:  Rc = 0 and (1/4)H^2 = 0 -> satisfied trivially")

sol3 = sp.solve(sp.Eq(d3, 0), t)
sol6 = sp.solve(sp.Eq(d6, 0), [c6])
print(f"  S^3 block = 0  <=>  t in {sol3}   (independent of c3 -- the radius cancels)")
print(f"  S^6 block = 0  <=>  {sol6}   (EMPTY = no radius c6 satisfies it)")
product_pass = (len(sol3) > 0) and (len(sol6) > 0)
print(f"  ==> product Bismut-Ricci-flat achievable ?  {product_pass}")
print()

RESULTS["product"] = {
    "n_nonzero_H_tot": len(Htot),
    "cross_block_of_H_squared_is_zero_VERIFIED": bool(cross_zero),
    "S3_block_matches_isolated_S3": bool(block3_ok),
    "S6_block_matches_isolated_S6": bool(block6_ok),
    "defect_S3_block": str(sp.factor(d3)),
    "defect_S6_block": str(sp.factor(d6)),
    "S3_block_roots_t": [str(x) for x in sol3],
    "S6_block_roots_c6": [str(x) for x in sol6],
    "product_condition_satisfiable": bool(product_pass),
}

# ======================================================================
print(SEP)
print("PART 5 -- Bianchi / harmonicity of H_tot on the product")
print(SEP)

print("  H_{S^3}: top-degree on the 3-dimensional factor and constant in the")
print("           product ON coframe, so d_{S^3}H = 0 (degree) and d_{S^6}H = 0")
print("           (no S^6 dependence)  =>  dH_{S^3} = 0.")
print("           *_9 H_{S^3} = (const) vol_{S^6}, also closed  =>  delta H_{S^3} = 0.")
print(f"  H_{{S^6}}: dT computed above -> dT = 0 ?  {dT_is_zero}")
dH_tot_zero = dT_is_zero
print(f"  ==> dH_tot = 0 ?  {dH_tot_zero}    (the definition REQUIRES H closed)")
print()

RESULTS["bianchi"] = {
    "dH_S3_is_zero": True,
    "dH_S3_reason": "top-degree on the 3-dim factor; no S^6 dependence",
    "delta_H_S3_is_zero": True,
    "dH_S6_is_zero": bool(dT_is_zero),
    "dH_tot_is_zero": bool(dH_tot_zero),
}

# ======================================================================
print(SEP)
print("PART 6 -- can ANY choice of H rescue it?  (a) exhaustion over all")
print("G2-invariant 3-forms on the frozen S^6;  (b) the topological argument")
print(SEP)

al, be = sp.symbols("alpha beta", real=True)

# (a) the space of G2-invariant 3-forms on S^6 = G2/SU(3) is exactly the
# SU(3)-invariant part of Lambda^3 m*, i.e. span{psi^+, psi^-}.  Take the
# general element H = alpha psi^+ + beta psi^- and impose all three conditions.
Mcross = sp.zeros(6, 6)
for a in range(6):
    for b in range(6):
        s = sp.Integer(0)
        for c_, d_ in itertools.product(range(6), repeat=2):
            va = form_get(psi_p, (a, c_, d_))
            if va == 0:
                continue
            vb = form_get(psi_m, (b, c_, d_))
            if vb == 0:
                continue
            s += va * vb
        Mcross[a, b] = sp.simplify(s)
cross_is_zero = all(Mcross[a, b] == 0 for a in range(6) for b in range(6))
cross_sym_is_zero = all(
    sp.simplify(Mcross[a, b] + Mcross[b, a]) == 0 for a in range(6) for b in range(6)
)
print(f"  (psi^+ . psi^-)_ab := sum psi^+_acd psi^-_bcd  identically 0 ?  {cross_is_zero}")
print(
    f"  its SYMMETRIC part (the only part entering (H^2), which is symmetric) "
    f"is 0 ?  {cross_sym_is_zero}"
)

Hgen = add_forms(scale_form(psi_p, al), scale_form(psi_m, be))
Hgen_sq_diag = sp.simplify(square_tensor(Hgen, 6)[0, 0])
print(f"  (H^2)_aa for H = alpha psi^+ + beta psi^- :  {sp.factor(Hgen_sq_diag)}")
eq_ricci = sp.Eq(RIC_S6, sp.Rational(1, 4) * Hgen_sq_diag)
print(
    f"  condition Rc = (1/4)H^2  <=>  {sp.simplify(sp.Rational(1, 4) * Hgen_sq_diag)}"
    f" = {RIC_S6}   i.e. alpha^2 + beta^2 = {sp.simplify(RIC_S6)}"
)

# closedness:  d(alpha psi^+ + beta psi^-) = beta * d psi^-  (d psi^+ = 0)
# co-closedness: *H = alpha*psi^+ + beta*psi^- ; d(*H) = 0 needs the psi^-
# component of *H to vanish, i.e. alpha = 0.
dHgen = d_invariant(Hgen, 3, Cm, 6)
star_Hgen = hodge_star_3form_6d(Hgen)
dstar_Hgen = d_invariant(star_Hgen, 3, Cm, 6)
closed_constraint = sp.solve([sp.Eq(v, 0) for v in dHgen.values()], [al, be], dict=True)
coclosed_constraint = sp.solve([sp.Eq(v, 0) for v in dstar_Hgen.values()], [al, be], dict=True)
print(f"  dH = 0        <=>  {closed_constraint}")
print(f"  d(*H) = 0     <=>  {coclosed_constraint}")
both = sp.solve(
    [sp.Eq(v, 0) for v in dHgen.values()] + [sp.Eq(v, 0) for v in dstar_Hgen.values()],
    [al, be],
    dict=True,
)
print(f"  BOTH (H harmonic)  <=>  {both}  -> forces H = 0")
harmonic_forces_zero = both == [{al: 0, be: 0}] or both == [{be: 0, al: 0}]
rescue_exists = bool(
    sp.solve(
        [eq_ricci]
        + [sp.Eq(v, 0) for v in dHgen.values()]
        + [sp.Eq(v, 0) for v in dstar_Hgen.values()],
        [al, be],
        dict=True,
    )
)
print(f"  any (alpha,beta) satisfying Rc=(1/4)H^2 AND dH=0 AND d*H=0 ?  {rescue_exists}")
print()

print("  (b) TOPOLOGICAL argument -- independent of the invariance assumption,")
print("      independent of the torsion, independent of both radii:")
print("      The definition requires H CLOSED and g-HARMONIC, i.e. dH = 0 and")
print("      delta H = 0.  On a COMPACT oriented manifold, Hodge's theorem makes")
print("      the space of harmonic 3-forms isomorphic to H^3(M;R).")
print("      Kunneth:  H^3(S^3 x S^6; R) = H^3(S^3) (x) H^0(S^6)  = R ,")
print("      because H^1(S^3)=H^2(S^3)=0 and H^1..H^5(S^6)=0.")
print("      For a PRODUCT metric the harmonic representative is vol_{S^3}, so")
print("           H = h * vol_{S^3}   for some constant h,   H|_{S^6} = 0 .")
print("      Then the S^6 block of Rc = (1/4)H^2 reads  Ric(g_{S^6}) = 0 :")
print("      the S^6 factor would have to be RICCI-FLAT.")
print(f"      Frozen S^6: Ric = {RIC_S6} * delta  (Einstein, positive) -> CONTRADICTION.")
print("      No choice of t, of the S^6 torsion, or of either radius can repair")
print("      this: b_3(S^6) = 0 is a topological fact about the frozen background.")
print()

RESULTS["rescue_attempts"] = {
    "psi_plus_psi_minus_cross_contraction_is_zero": bool(cross_is_zero),
    "psi_plus_psi_minus_cross_symmetric_part_is_zero": bool(cross_sym_is_zero),
    "H_general_invariant_squared_diag": str(sp.factor(Hgen_sq_diag)),
    "Rc_eq_quarter_H2_requires": f"alpha^2 + beta^2 = {sp.simplify(RIC_S6)}",
    "dH_zero_solutions": str(closed_constraint),
    "dstarH_zero_solutions": str(coclosed_constraint),
    "harmonic_forces_H_zero": bool(harmonic_forces_zero),
    "any_invariant_H_satisfying_all_three": bool(rescue_exists),
    "topological_argument": {
        "b3_S6": 0,
        "H3_of_product_over_R": "R, generated by vol_{S^3} (Kunneth)",
        "harmonic_H_must_be": "h * vol_{S^3}, so H|_{S^6} = 0",
        "forces": "Ric(g_{S^6}) = 0, i.e. S^6 factor Ricci-flat",
        "frozen_S6_Ric": str(RIC_S6),
        "contradiction": True,
    },
}

# ======================================================================
print(SEP)
print("PART 7 -- ONE NAMED RELAXATION, scoped: the constant-lambda ('soliton-")
print("shaped') weakening  Rc - (1/4)H^2 = lambda g  instead of = 0.")
print(SEP)
print("  NOT a generalized-Ricci-soliton computation.  The full soliton system")
print("  also constrains H; this is only its NECESSARY metric equation, and only")
print("  for a homogeneous background where the potential is constant (grad^2 f")
print("  = 0).  Recorded because it is the first relaxation a reader will")
print("  propose, and it is 3 lines.")
print("  Eliminating the common lambda between the two blocks gives one equation, d3 = d6:")
soliton_rel = sp.simplify(sp.Eq(d3, d6))
print(f"    {soliton_rel}")
t_soliton = sp.solve(sp.Eq(sp.expand(d3 - d6), 0), t)
print("  => -8t(t-1)/c3^2 = 4/(3 c6^2)  =>  t(1-t) = c3^2/(6 c6^2) > 0")
print(f"     roots: t = {t_soliton}")
print("     Since c3, c6 > 0, t(1-t) > 0 STRICTLY, i.e. 0 < t < 1 and")
print("     t = 0, t = 1 are EXCLUDED -- the relaxation, if anything, selects")
print("     AGAINST the two values OB1 needs, and leaves a one-parameter curve")
print("     of solutions rather than a discrete selection.  It also does not")
print("     repair dH != 0.")
print()
RESULTS["relaxation_constant_lambda"] = {
    "scope": "necessary metric equation only, homogeneous background, "
    "NOT the full generalized-Ricci-soliton system",
    "matched_blocks_equation": str(soliton_rel),
    "t_roots_in_terms_of_radii": [str(x) for x in t_soliton],
    "endpoints_t_0_and_1_excluded": True,
    "reason": "t(1-t) = c3^2/(6 c6^2) > 0 for positive radii",
    "still_fails_dH_zero": True,
}

# ======================================================================
print(SEP)
print("VERDICT")
print(SEP)

f1_pass = bool(product_pass and dH_tot_zero)
if not round111_match:
    label = "BLOCKED_INFRASTRUCTURE__S3_CROSSCHECK_AGAINST_ROUND111_FAILED"
elif routes_agree is False:
    label = "BLOCKED_INFRASTRUCTURE__dT_ROUTES_DISAGREE"
elif f1_pass:
    label = "F1_PASS__BISMUT_RICCI_FLAT_APPLICABLE_TO_FROZEN_S3xS6"
else:
    label = (
        "F1_FAIL__S3_FACTOR_ADMITS_t_IN_0_1_BUT_S6_FACTOR_VIOLATES_"
        "Rc_EQ_QUARTER_H2_BY_FACTOR_5_AND_H_NOT_CLOSED__"
        "AND_TOPOLOGICALLY_UNRESCUABLE_SINCE_b3_S6_EQ_0"
    )
RESULTS["verdict"] = {
    "F1_pass": f1_pass,
    "label": label,
    "rho_S3_condition": "rho_S3 = 1 <=> (2t-1)^2 = 1 <=> t in {0,1}",
    "rho_S6": str(rho_S6),
    "dT_S6_is_zero": bool(dT_is_zero),
}
for k, v in RESULTS["verdict"].items():
    print(f"  {k}: {v}")

RESULTS["provenance"] = {
    "date": "2026-08-31",
    "python": platform.python_version(),
    "sympy": sp.__version__,
    "platform": platform.platform(),
    "S6_torsion_source": "experiments/20260708-dolan-casimir-g2su3/"
    "g2su3_H_element.py :: build_T_table()",
    "S6_Ricci_source": "experiments/20260708-dolan-casimir-g2su3/decision.md "
    "(Round 16, Ric(e_p,e_p)=5/3, Scal=10, triple-verified)",
    "S3_crosscheck_source": "experiments/20260717-round111-codex-item6-"
    "scalar-curvature-action/decision.md (Ric^t = "
    "8t(1-t) delta, Scal(t)=24t(1-t))",
    "definition_source": "arXiv:2301.02335 (Lauret-Will) abstract, verbatim; "
    "arXiv:2401.03332 (Gutierrez) abstract, verbatim",
    "exact_arithmetic_only": True,
}

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_c119.json")
with open(out_path, "w", encoding="utf-8") as fh:
    json.dump(RESULTS, fh, indent=2)
print(f"\n  written: {out_path}")
