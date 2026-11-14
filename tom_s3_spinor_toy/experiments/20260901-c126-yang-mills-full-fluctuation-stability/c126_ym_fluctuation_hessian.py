"""C126: full second variation of S_YM[nabla] = int_{S^3} |R^nabla|^2 dvol
around the flat Cartan-Schouten connections nabla^0 and nabla^1, for a
GENERAL su(2)-valued 1-form perturbation (not restricted to the
1-parameter family direction).

Conventions (bridged explicitly to round99, PART 0):
  round99 uses Z_i = i*sigma_i with [Z_1,Z_2] = -2 Z_3 (c0 = -2).
  This round uses T_a := -Z_a/2, giving [T_i,T_j] = eps_ijk T_k (c0 = +1),
  i.e. the SAME Lie algebra in a rescaled basis.  The rescaling is a
  rescaling of the S^3 radius; it changes the overall positive constant
  in front of S_YM and nothing else (no sign, no critical point).

  X_i  : left-invariant frame on S^3 = SU(2), [X_i,X_j] = eps_ijk X_k,
         declared orthonormal (radius fixed by that declaration).
  e^i  : dual coframe, de^k = -(1/2) eps_ijk e^i ^ e^j.
  A    : connection 1-form, su(2)-valued, components A_i^b := A(X_i)^b.
  a    : fluctuation, same type.  a_i^b(x), x in S^3.

  The Cartan-Schouten family nabla^t_X Y = t[X,Y] has, in this frame,
         A^t(X_i)^b = t * delta_i^b        (PART 1 verifies this gives
                                            F^t = t(t-1) * (const)).

Component formulas used throughout (all verified symbolically in PART 1):
  F_{ij}^b   = X_i A_j^b - X_j A_i^b - eps_ijk A_k^b + eps_bcd A_i^c A_j^d
  (d_A a)_{ij}^b = X_i a_j^b - X_j a_i^b - eps_ijk a_k^b
                   + eps_bcd (A_i^c a_j^d - A_j^c a_i^d)
  (d_A phi)_i^b  = X_i phi^b + eps_bcd A_i^c phi^d
  S_YM[A]    = int sum_{i<j} sum_b (F_{ij}^b)^2   (positive-definite: a
               sum of squares, Riemannian signature -- load-bearing)

Peter-Weyl: L^2(SU(2)) = sum_j V_j (x) V_j^*.  A left-invariant field X_k
acts on the RIGHT index only, as the representation matrix rho_j(T_k) =
-i J_k^{(j)}; the left index is a spectator of multiplicity (2j+1).  So
the whole fluctuation operator is block diagonal in j, and each block acts
on  C^3 (frame) (x) C^3 (internal) (x) C^{2j+1},  dim 9(2j+1).

Run:  python c126_ym_fluctuation_hessian.py
"""

from __future__ import annotations

import importlib.util
import json
import pathlib
from collections import Counter
from itertools import product

import numpy as np
import sympy as sp
from scipy.optimize import root

np.set_printoptions(precision=6, suppress=True)

TOL = 1e-9
RESULTS: dict = {}

EPS = np.zeros((3, 3, 3))
for _i, _j, _k in product(range(3), repeat=3):
    EPS[_i, _j, _k] = (
        0
        if len({_i, _j, _k}) < 3
        else (1 if (_i, _j, _k) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)] else -1)
    )

PAIRS = [(0, 1), (0, 2), (1, 2)]  # i<j


def hr(title: str) -> None:
    print("=" * 92)
    print(title)
    print("=" * 92)


# ---------------------------------------------------------------------------
# PART 0 -- convention bridge to round99 (tool-verified, not assumed)
# ---------------------------------------------------------------------------
hr("PART 0 -- convention bridge:  round99's Z_i = i*sigma_i  ->  T_a := -Z_a/2")


def _pauli():
    return [
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        sp.Matrix([[1, 0], [0, -1]]),
    ]


Z = [sp.I * s for s in _pauli()]  # round99 generators, verbatim
T = [sp.simplify(-Zi / 2) for Zi in Z]


def _br(A, B):
    return sp.simplify(A * B - B * A)


round99_c0_minus2 = all(
    _br(Z[i], Z[j]) == -2 * Z[k] for (i, j, k) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
)
T_structure_plus1 = all(_br(T[i], T[j]) == T[k] for (i, j, k) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)])
print(f"  round99 convention [Z1,Z2] = -2 Z3 reproduced?            {round99_c0_minus2}")
print(f"  rescaled T_a = -Z_a/2 obeys [T_i,T_j] = eps_ijk T_k?      {T_structure_plus1}")
print("  -> same Lie algebra, rescaled basis.  NAMED EXPLICITLY (FL Step 8a")
print("     skeptic finding E9): T_a = -Z_a/2 is a scaling by 1/2 COMPOSED WITH")
print("     a sign flip of all three generators, and X_i -> -X_i has det = -1 on")
print("     the frame, i.e. it REVERSES ORIENTATION relative to round99's basis.")
print("     The minus sign is forced (with +Z_a/2 the structure constant would")
print("     be -1, not +1).  Nothing load-bearing here depends on it: S_YM is")
print("     even under orientation reversal, and |n|=1 in PART 6b is not")
print("     affected (only the SIGN of the winding number is convention-")
print("     dependent).  Flagged because this repo does use orientation")
print("     elsewhere (iota is orientation-reversing, C37-C39) and CS is")
print("     orientation-odd -- do not reuse this bridge in an orientation-")
print("     sensitive round without re-checking round99's own frame handedness,")
print("     which round99 never fixes (it works with matrices, not a frame).")
print()
RESULTS["part0_round99_convention_reproduced"] = bool(round99_c0_minus2)
RESULTS["part0_rescaled_basis_structure_constant_plus1"] = bool(T_structure_plus1)


# ---------------------------------------------------------------------------
# PART 1 -- exact expansion of the curvature and of S_YM (symbolic)
# ---------------------------------------------------------------------------
hr("PART 1 -- EXACT expansion  F(A+a) = F(A) + d_A a + [a,a]   (symbolic, no truncation)")

# symbols: A_i^b, a_i^b, and their frame-derivatives X_i A_j^b, X_i a_j^b
As = sp.symbols("A0:3_0:3", real=True)
as_ = sp.symbols("a0:3_0:3", real=True)
dAs = sp.symbols("dA0:3_0:3_0:3", real=True)  # dA[i][j][b] = X_i A_j^b
das = sp.symbols("da0:3_0:3_0:3", real=True)

Asym = [[As[3 * i + b] for b in range(3)] for i in range(3)]
asym = [[as_[3 * i + b] for b in range(3)] for i in range(3)]
dAsym = [[[dAs[9 * i + 3 * j + b] for b in range(3)] for j in range(3)] for i in range(3)]
dasym = [[[das[9 * i + 3 * j + b] for b in range(3)] for j in range(3)] for i in range(3)]


def F_sym(Amat, dA, i, j, b):
    out = dA[i][j][b] - dA[j][i][b]
    out -= sum(EPS[i, j, k] * Amat[k][b] for k in range(3))
    out += sum(EPS[b, c, d] * Amat[i][c] * Amat[j][d] for c in range(3) for d in range(3))
    return sp.expand(out)


def dA_a_sym(Amat, amat, da, i, j, b):
    out = da[i][j][b] - da[j][i][b]
    out -= sum(EPS[i, j, k] * amat[k][b] for k in range(3))
    out += sum(
        EPS[b, c, d] * (Amat[i][c] * amat[j][d] - Amat[j][c] * amat[i][d])
        for c in range(3)
        for d in range(3)
    )
    return sp.expand(out)


def bracket_sym(amat, i, j, b):
    return sp.expand(
        sum(EPS[b, c, d] * amat[i][c] * amat[j][d] for c in range(3) for d in range(3))
    )


ApA = [[Asym[i][b] + asym[i][b] for b in range(3)] for i in range(3)]
dApA = [[[dAsym[i][j][b] + dasym[i][j][b] for b in range(3)] for j in range(3)] for i in range(3)]

expansion_exact = True
for i, j in PAIRS:
    for b in range(3):
        lhs = F_sym(ApA, dApA, i, j, b)
        rhs = (
            F_sym(Asym, dAsym, i, j, b)
            + dA_a_sym(Asym, asym, dasym, i, j, b)
            + bracket_sym(asym, i, j, b)
        )
        if sp.simplify(lhs - rhs) != 0:
            expansion_exact = False
print(f"  F(A+a) = F(A) + d_A a + [a,a] holds for all 9 (i<j,b) components?  {expansion_exact}")
print("  (exact -- Yang-Mills is quartic, the expansion TERMINATES at O(a^2)")
print("   inside |.|^2, so the 'Hessian' below is not a truncation.)")
RESULTS["part1_exact_expansion_verified"] = bool(expansion_exact)

# curvature of the Cartan-Schouten family: A_i^b = t delta_i^b
t = sp.symbols("t", real=True)
A_t = [[t * (1 if i == b else 0) for b in range(3)] for i in range(3)]
dA_t = [[[sp.Integer(0)] * 3 for _ in range(3)] for _ in range(3)]  # constant coefficients
F_t = {}
for i, j in PAIRS:
    for b in range(3):
        F_t[(i, j, b)] = sp.expand(F_sym(A_t, dA_t, i, j, b))
F_family_ok = all(
    sp.simplify(F_t[(i, j, b)] - (t**2 - t) * EPS[b, i, j]) == 0 for i, j in PAIRS for b in range(3)
)
print(f"  F^t_{{ij}}^b = (t^2-t) eps_bij for the family A_i^b = t delta_i^b?  {F_family_ok}")
S_family = sp.expand(sum(F_t[(i, j, b)] ** 2 for i, j in PAIRS for b in range(3)))
print(f"  S_YM(t)/Vol = {sp.factor(S_family)}      (round99/C123 shape [t(t-1)]^2 x 3)")
E2 = sp.expand(sp.diff(S_family, t, 2))
print(f"  d2/dt2 S_YM(t)/Vol = {E2} = 3*(2 - 12t + 12t^2)   -> C = 3 in C123's E(t)=C t^2(1-t)^2")
print(
    f"  E''(0)={E2.subs(t, 0)}, E''(1)={E2.subs(t, 1)}, "
    f"E''(1/2)={E2.subs(t, sp.Rational(1, 2))}   [C123: 2C, 2C, -C with C=3]"
)
print()
RESULTS["part1_family_curvature_formula_verified"] = bool(F_family_ok)
RESULTS["part1_S_YM_of_t_over_Vol"] = str(sp.factor(S_family))
RESULTS["part1_C123_C_constant"] = 3
RESULTS["part1_Epp_0"] = int(E2.subs(t, 0))
RESULTS["part1_Epp_1"] = int(E2.subs(t, 1))
RESULTS["part1_Epp_half"] = int(E2.subs(t, sp.Rational(1, 2)))


# ---------------------------------------------------------------------------
# PART 1b -- |R^nabla|^2 (Riemann-tensor norm) vs the Yang-Mills norm used here
# ---------------------------------------------------------------------------
hr("PART 1b -- the two readings of |R^nabla|^2 differ by a POSITIVE constant (4)")
print("  claim.md writes S_YM = Int |R^nabla|^2.  Two readings:")
print("    (a) affine:  |R|^2 = R_{ijkl} R^{ijkl}, all four indices contracted")
print("        with the (positive-definite) metric in the orthonormal frame;")
print("    (b) Yang-Mills: |F|^2 = sum_{i<j} sum_b (F_{ij}^b)^2, internal index")
print("        contracted with the Killing form of so(3).")
print("  For a METRIC connection, R_{ijkl} = eps_{ijb} F_{kl}^b (the curvature")
print("  2-form valued in so(3) = Lambda^2 R^3), so the two differ by a fixed")
print("  positive factor.  Determined numerically here, not asserted:")
rngq = np.random.default_rng(31415)
ratios = []
for _ in range(200):
    Fc = rngq.normal(size=(3, 3, 3))  # F[k,l,b] arbitrary, antisymmetrised in k,l
    Fc = 0.5 * (Fc - np.transpose(Fc, (1, 0, 2)))
    Riem = np.einsum(
        "ijb,klb->ijkl",
        np.array([[[EPS[i, j_, b] for b in range(3)] for j_ in range(3)] for i in range(3)]),
        Fc,
    )
    affine = float(np.sum(Riem**2))
    ym = float(
        sum(Fc[k, l_, b] ** 2 for k in range(3) for l_ in range(3) for b in range(3) if k < l_)
    )
    ratios.append(affine / ym)
ratio = float(np.mean(ratios))
ratio_const = bool(np.allclose(ratios, ratios[0], atol=1e-10))
print(f"  |R|^2_affine / |F|^2_YM = {ratio:.12f}  (constant over 200 random F? {ratio_const})")
print("  A positive constant cannot move a critical point, change the sign of a")
print("  second variation, or alter a kernel.  Everything below is therefore")
print("  stated for the Yang-Mills normalisation and holds verbatim for the")
print("  affine one.  [This is the same 'positive constant cannot move a")
print("  stationary point' step C123 used for the round99 comparison.]")
RESULTS["part1b_affine_to_ym_ratio"] = ratio
RESULTS["part1b_ratio_is_constant"] = ratio_const
print()
# ---------------------------------------------------------------------------
# PART 2 -- the linear term: which t are genuine critical points?
# ---------------------------------------------------------------------------
hr("PART 2 -- linear term  delta S = 2 sum_{i<j} <F_{ij}, (d_A a)_{ij}>  (symbolic)")

# For a GENERAL a (including x-dependence), the linear functional is
#   L(a) = 2 sum_{i<j} int F^t_{ij}.(d_A a)_{ij}.
# F^t is CONSTANT, so the derivative terms integrate to zero
# (int X_i f = 0 on a compact group: X_i is divergence-free / Haar-invariant).
# What survives is the algebraic part, evaluated on the zero-mode (constant)
# part of a only.  Compute that surviving 9-component covector.
Lvec = [[sp.Integer(0)] * 3 for _ in range(3)]  # coefficient of a_k^c
for i, j in PAIRS:
    for b in range(3):
        Fij = (t**2 - t) * EPS[b, i, j]
        alg = -sum(EPS[i, j, k] * asym[k][b] for k in range(3)) + sum(
            EPS[b, c, d] * (A_t[i][c] * asym[j][d] - A_t[j][c] * asym[i][d])
            for c in range(3)
            for d in range(3)
        )
        for k in range(3):
            for c in range(3):
                Lvec[k][c] += sp.expand(2 * Fij * sp.diff(alg, asym[k][c]))
Lvec = [[sp.factor(sp.expand(Lvec[k][c])) for c in range(3)] for k in range(3)]
print("  linear functional coefficients L_k^c (coefficient of the constant mode a_k^c):")
for k in range(3):
    print(f"    k={k}: {[str(Lvec[k][c]) for c in range(3)]}")
zero_ts = sorted(
    set().union(
        *[
            set(sp.solve(sp.Eq(Lvec[k][c], 0), t))
            for k in range(3)
            for c in range(3)
            if Lvec[k][c] != 0
        ]
    ),
    key=str,
)
all_zero_t = [
    tv
    for tv in [sp.Integer(0), sp.Integer(1), sp.Rational(1, 2)]
    if all(Lvec[k][c].subs(t, tv) == 0 for k in range(3) for c in range(3))
]
print(f"  L == 0 identically at t in {[str(v) for v in all_zero_t]}   (critical points of S_YM)")
print("  -> t=0 and t=1 ARE genuine critical points w.r.t. the FULL fluctuation")
print("     space, not merely along the 1-parameter family. (t=1/2 too: it is")
print("     the barrier top, a critical point of index >= 1, see PART 5.)")
print()
RESULTS["part2_critical_t_values"] = [str(v) for v in all_zero_t]
RESULTS["part2_linear_term_roots_raw"] = [str(v) for v in zero_ts]


# ---------------------------------------------------------------------------
# PART 3 -- the KEY structural argument (stated, then checked numerically)
# ---------------------------------------------------------------------------
hr("PART 3 -- structural argument: t=0,1 are flat, S_YM >= 0, so they are GLOBAL minima")
print("  S_YM[A] = int sum_{i<j,b} (F_{ij}^b)^2 >= 0 with equality iff F = 0.")
print("  F^t = (t^2-t) x const  =>  F^0 = F^1 = 0  =>  S_YM[A^0] = S_YM[A^1] = 0.")
print("  Hence A^0 and A^1 attain the ABSOLUTE minimum of S_YM.  For a")
print("  non-negative functional, a zero is automatically a global minimum, so")
print("  the second variation there CANNOT have a negative direction.")
print("  Explicitly, with F(A)=0 the exact expansion of PART 1 gives")
print("      S_YM[A + a] = int sum_{i<j} | (d_A a)_{ij} + [a_i,a_j] |^2 ,")
print("  whose quadratic part is   Q[a] = int sum_{i<j} |(d_A a)_{ij}|^2  >= 0,")
print("  i.e. the Hessian is exactly  2 d_A^dagger d_A  -- manifestly PSD.")
print("  The only question left is the KERNEL, computed numerically below.")
print("  Load-bearing assumption, named: Riemannian (positive-definite) metric")
print("  on S^3, so |.|^2 is a sum of squares.  In Lorentzian signature this")
print("  argument fails; on S^3 it does not.")
print()


# ---------------------------------------------------------------------------
# PART 4 -- explicit Peter-Weyl mode operator, numerically diagonalised
# ---------------------------------------------------------------------------
hr("PART 4 -- explicit Peter-Weyl fluctuation operator, block by block")


def spin_matrices(two_j: int):
    """rho_j(T_k) = -i J_k for spin j = two_j/2, as (d x d) complex matrices."""
    j = two_j / 2.0
    d = two_j + 1
    ms = np.array([j - n for n in range(d)])  # m = j, j-1, ..., -j
    Jz = np.diag(ms).astype(complex)
    Jp = np.zeros((d, d), dtype=complex)
    for n in range(1, d):
        m = ms[n]
        Jp[n - 1, n] = np.sqrt(j * (j + 1) - m * (m + 1))
    Jm = Jp.conj().T
    Jx = (Jp + Jm) / 2.0
    Jy = (Jp - Jm) / (2.0j)
    return [-1j * Jx, -1j * Jy, -1j * Jz]


def _check_rep(two_j: int) -> bool:
    rho = spin_matrices(two_j)
    ok = True
    for i, j_, k in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        c = rho[i] @ rho[j_] - rho[j_] @ rho[i]
        ok = ok and np.allclose(c, rho[k], atol=1e-10)
    # anti-hermitian (so X_k is a real vector field / skew operator on L^2)
    for r in rho:
        ok = ok and np.allclose(r.conj().T, -r, atol=1e-10)
    return ok


rep_ok = all(_check_rep(tj) for tj in range(9))
print(
    f"  rho_j(T_k) satisfy [rho_i,rho_j]=eps_ijk rho_k and are anti-hermitian, 2j=0..8?  {rep_ok}"
)
RESULTS["part4_representation_matrices_verified"] = bool(rep_ok)


def idx1(i: int, b: int, n: int, d: int) -> int:
    """index into the 1-form space  C^3(frame) (x) C^3(internal) (x) C^d."""
    return (i * 3 + b) * d + n


def idx2(p: int, b: int, n: int, d: int) -> int:
    """index into the 2-form space  C^3(pairs) (x) C^3(internal) (x) C^d."""
    return (p * 3 + b) * d + n


def build_dA_1form(tval: float, two_j: int) -> np.ndarray:
    """matrix of  d_A : Omega^1(su2) -> Omega^2(su2)  on Peter-Weyl block j."""
    d = two_j + 1
    rho = spin_matrices(two_j)
    D = np.zeros((3 * 3 * d, 3 * 3 * d), dtype=complex)
    for p, (i, j_) in enumerate(PAIRS):
        for b in range(3):
            for n in range(d):
                row = idx2(p, b, n, d)
                # X_i a_j^b - X_j a_i^b
                for m in range(d):
                    D[row, idx1(j_, b, m, d)] += rho[i][n, m]
                    D[row, idx1(i, b, m, d)] -= rho[j_][n, m]
                # - eps_{ij k} a_k^b
                for k in range(3):
                    if EPS[i, j_, k]:
                        D[row, idx1(k, b, n, d)] -= EPS[i, j_, k]
                # + eps_{bcd}(A_i^c a_j^d - A_j^c a_i^d),  A_i^c = t delta_i^c
                for dd in range(3):
                    if EPS[b, i, dd]:
                        D[row, idx1(j_, dd, n, d)] += tval * EPS[b, i, dd]
                    if EPS[b, j_, dd]:
                        D[row, idx1(i, dd, n, d)] -= tval * EPS[b, j_, dd]
    return D


def build_dA_0form(tval: float, two_j: int) -> np.ndarray:
    """matrix of  d_A : Omega^0(su2) -> Omega^1(su2)  (the gauge directions)."""
    d = two_j + 1
    rho = spin_matrices(two_j)
    G = np.zeros((3 * 3 * d, 3 * d), dtype=complex)
    for i in range(3):
        for b in range(3):
            for n in range(d):
                row = idx1(i, b, n, d)
                for m in range(d):
                    G[row, b * d + m] += rho[i][n, m]  # X_i phi^b
                for c in range(3):
                    if EPS[b, i, c]:
                        G[row, c * d + n] += tval * EPS[b, i, c]  # eps_bcd A_i^c phi^d
    return G


def build_F_term(tval: float, two_j: int) -> np.ndarray:
    """2 sum_{i<j} <F_{ij},[a_i,a_j]>  as a hermitian matrix.

    Derived in closed form (checked against the family direction below):
        2 sum_{i<j} F.[a,a] = (t^2-t) [ (tr a)^2 - tr(a a) ],
    with a the 3x3 matrix a_i^b (frame index i, internal index b).
    """
    d = two_j + 1
    M = np.zeros((9, 9))
    for i in range(3):
        for c in range(3):
            for j_ in range(3):
                for dd in range(3):
                    r, s = i * 3 + c, j_ * 3 + dd
                    val = 0.0
                    if i == c and j_ == dd:
                        val += 1.0  # (tr a)^2
                    if i == dd and j_ == c:
                        val -= 1.0  # - tr(a a)
                    M[r, s] += val
    M = (tval**2 - tval) * 0.5 * (M + M.T)
    return np.kron(M, np.eye(d)).astype(complex)


def hessian_block(tval: float, two_j: int) -> np.ndarray:
    """quadratic form Q = (1/2) delta^2 S_YM restricted to Peter-Weyl block j."""
    D = build_dA_1form(tval, two_j)
    H = D.conj().T @ D + build_F_term(tval, two_j)
    return 0.5 * (H + H.conj().T)


# --- positive control: the 1-parameter family direction must reproduce C123 ---
print()
print("  POSITIVE CONTROL (known answer from round99/C123): plug the family")
print("  direction  a = d/dt A^t  (a_i^b = delta_i^b, a constant/j=0 mode) into")
print("  the general operator and compare with (1/2) E''(t) = 3(6t^2-6t+1).")
ctrl_rows = []
v0 = np.zeros(9, dtype=complex)
for i in range(3):
    v0[idx1(i, i, 0, 1)] = 1.0
ctrl_ok = True
for tv in [0.0, 0.25, 0.5, 0.75, 1.0, 1.7]:
    H = hessian_block(tv, 0)
    q = float(np.real(v0.conj() @ H @ v0))
    exact = 3.0 * (6 * tv**2 - 6 * tv + 1)
    ok = abs(q - exact) < 1e-10
    ctrl_ok = ctrl_ok and ok
    ctrl_rows.append({"t": tv, "Q_operator": q, "half_Epp_expected": exact, "match": bool(ok)})
    print(f"    t={tv:<5} Q[family dir] = {q:>10.6f}   (1/2)E''(t) = {exact:>10.6f}   match={ok}")
print(f"  POSITIVE CONTROL PASSED (all t)?  {ctrl_ok}")
print("  -> at t=0 and t=1 this is +3 = (1/2)(2C) with C=3: C123's E''(0)=E''(1)=2C.")
print("  -> at t=1/2 this is -1.5 = (1/2)(-C): C123's E''(1/2)=-C.  The general")
print("     operator reproduces the 1D-slice numbers it must reproduce.")
print()
RESULTS["part4_positive_control_family_direction"] = ctrl_rows
RESULTS["part4_positive_control_passed"] = bool(ctrl_ok)

# --- the actual spectra at t=0 and t=1 ---
TWO_J_MAX = 8  # j = 0, 1/2, ..., 4
spec_table = []
print(f"  Spectrum of Q, block by block, 2j = 0..{TWO_J_MAX}")
print("  (dim = 9(2j+1) per block; each block occurs with multiplicity 2j+1)")
print()
print(
    f"  {'2j':>3} {'dim':>5} | {'t=0: min eig':>13} {'ker dim':>8} {'rk d_A':>7}"
    f" | {'t=1: min eig':>13} {'ker dim':>8} {'rk d_A':>7}"
)
psd_all = True
kernel_matches_gauge = True
for two_j in range(TWO_J_MAX + 1):
    d = two_j + 1
    row = {"two_j": two_j, "dim": 9 * d, "multiplicity": d}
    for tv, tag in [(0.0, "t0"), (1.0, "t1")]:
        H = hessian_block(tv, two_j)
        ev = np.linalg.eigvalsh(H)
        G = build_dA_0form(tv, two_j)
        rk = int(np.linalg.matrix_rank(G, tol=1e-9))
        kdim = int(np.sum(np.abs(ev) < 1e-9))
        row[f"{tag}_min_eig"] = float(ev[0])
        row[f"{tag}_max_eig"] = float(ev[-1])
        row[f"{tag}_kernel_dim"] = kdim
        row[f"{tag}_gauge_rank"] = rk
        row[f"{tag}_n_negative"] = int(np.sum(ev < -1e-9))
        row[f"{tag}_eigs"] = [round(float(x), 8) for x in ev]
        if ev[0] < -1e-9:
            psd_all = False
        if kdim != rk:
            kernel_matches_gauge = False
    spec_table.append(row)
    print(
        f"  {two_j:>3} {9 * d:>5} | {row['t0_min_eig']:>13.9f} {row['t0_kernel_dim']:>8}"
        f" {row['t0_gauge_rank']:>7} | {row['t1_min_eig']:>13.9f} {row['t1_kernel_dim']:>8}"
        f" {row['t1_gauge_rank']:>7}"
    )
print()
print(f"  ALL blocks positive semi-definite at t=0 and t=1?          {psd_all}")
print(f"  kernel(Q) dimension == rank(d_A: Omega^0 -> Omega^1)?      {kernel_matches_gauge}")
print("  -> the kernel is EXACTLY the gauge-orbit tangent space; there is no")
print("     extra flat direction, i.e. the twisted cohomology H^1_{d_A} = 0,")
print("     as it must be for a flat connection on the simply-connected S^3.")
print("  -> modulo gauge, the Hessian is strictly POSITIVE DEFINITE.")
RESULTS["part4_spectra"] = spec_table
RESULTS["part4_psd_at_t0_and_t1"] = bool(psd_all)
RESULTS["part4_kernel_equals_gauge_orbit"] = bool(kernel_matches_gauge)

# spectral gap modulo gauge
gaps = {}
for tv, tag in [(0.0, "t0"), (1.0, "t1")]:
    nz = []
    for two_j in range(TWO_J_MAX + 1):
        ev = np.linalg.eigvalsh(hessian_block(tv, two_j))
        nz.extend([x for x in ev if x > 1e-9])
    gaps[tag] = float(min(nz))
print(
    f"  spectral gap (lowest NONZERO eigenvalue) : t=0 -> {gaps['t0']:.9f},"
    f"  t=1 -> {gaps['t1']:.9f}"
)
RESULTS["part4_spectral_gap"] = gaps
print()


# ---------------------------------------------------------------------------
# PART 4b -- truncation-robustness of the t=0,1 PSD result
# ---------------------------------------------------------------------------
hr("PART 4b -- truncation robustness: push the mode cutoff up and re-check")
TWO_J_HIGH = 14  # j up to 7; block dim 9*15 = 135
rob = {}
for tv, tag in [(0.0, "t0"), (1.0, "t1")]:
    mn, kmatch = 1e9, True
    for two_j in range(TWO_J_HIGH + 1):
        H = hessian_block(tv, two_j)
        ev = np.linalg.eigvalsh(H)
        mn = min(mn, float(ev[0]))
        kdim = int(np.sum(np.abs(ev) < 1e-9))
        rk = int(np.linalg.matrix_rank(build_dA_0form(tv, two_j), tol=1e-9))
        kmatch = kmatch and (kdim == rk)
    rob[tag] = {
        "two_j_max": TWO_J_HIGH,
        "global_min_eig": mn,
        "kernel_equals_gauge": bool(kmatch),
    }
    print(
        f"  {tag}: 2j <= {TWO_J_HIGH}, min eigenvalue over ALL blocks = {mn:.12f},"
        f"  kernel==gauge in every block: {kmatch}"
    )
print("  -> the PSD + kernel-is-gauge result is NOT an artifact of the cutoff.")
print("     (It cannot be: PART 3's argument is cutoff-free.  This only checks")
print("      that the numerics agree with it.)")
RESULTS["part4b_robustness"] = rob
print()


# ---------------------------------------------------------------------------
# PART 4c -- EXTERNAL cross-check of the whole apparatus against Hodge theory
# ---------------------------------------------------------------------------
hr("PART 4c -- external check: the t=0 spectrum must be the known S^3 Hodge spectrum")
print("  At t=0 the operator is exactly d^dagger d on Omega^1(S^3, su(2)).  Its")
print("  kernel is the exact 1-forms and its NONZERO spectrum is the Hodge")
print("  Laplacian spectrum on COEXACT 1-forms of the round S^3, which has a")
print("  closed form.  PART 6b derives the radius R = 2 independently (from the")
print("  sectional curvature K = 1/4 of the Levi-Civita member), so the")
print("  prediction below has NO free parameter:")
print("      lambda_k = (k+1)^2 / R^2 = (k+1)^2/4,   k >= 1,")
print("      multiplicity 2k(k+2), times 3 for the su(2) internal index.")
print("  [CITED: the coexact-1-form spectrum of the round S^3 is a standard")
print("   result of spectral geometry; the formula is used here as an external")
print("   prediction and is NOT re-derived in this project.]")
_counts: Counter = Counter()
for _tj in range(TWO_J_HIGH + 1):
    for _x in np.linalg.eigvalsh(hessian_block(0.0, _tj)):
        if _x > 1e-9:
            _counts[round(float(_x), 6)] += _tj + 1
hodge_rows, hodge_ok = [], True
print()
print(
    f"  {'k':>2} {'predicted lambda':>17} {'computed lambda':>16} {'pred mult':>10} {'computed mult':>14} {'match':>6}"
)
for _k in range(1, 8):
    lam_pred = (_k + 1) ** 2 / 4.0
    mult_pred = 3 * 2 * _k * (_k + 2)
    lam_key = round(lam_pred, 6)
    mult_got = _counts.get(lam_key, 0)
    ok = mult_got == mult_pred
    hodge_ok = hodge_ok and ok
    hodge_rows.append(
        {
            "k": _k,
            "lambda": lam_pred,
            "mult_predicted": mult_pred,
            "mult_computed": mult_got,
            "match": bool(ok),
        }
    )
    print(f"  {_k:>2} {lam_pred:>17.6f} {lam_key:>16.6f} {mult_pred:>10} {mult_got:>14} {ok!s:>6}")
print()
print(f"  ALL 7 levels match in BOTH eigenvalue and multiplicity?         {hodge_ok}")
print("  This is the strongest available check on the Peter-Weyl normalisation,")
print("  the frame formulas, and the claim that the computed numbers really are")
print("  L^2 eigenvalues: a wrong inner-product normalisation, a wrong coframe")
print("  term, or a wrong action of X_i would break the multiplicities, which")
print("  are integers and cannot be fudged by a rescaling.")
RESULTS["part4c_hodge_cross_check"] = hodge_rows
RESULTS["part4c_hodge_cross_check_passed"] = bool(hodge_ok)
print()
# ---------------------------------------------------------------------------
# PART 4d -- the assembled matrices vs a DIRECT component-by-component rebuild
# ---------------------------------------------------------------------------
hr("PART 4d -- verify  2 sum_{i<j} <F_ij,[a_i,a_j]> = (t^2-t)[(tr a)^2 - tr(a a)]")
print("  build_F_term() uses a closed form.  The positive control in PART 4 only")
print("  exercises it on ONE vector (the family direction), which is not enough.")
print("  Check it against a DIRECT index-by-index evaluation on random a:")
rngf = np.random.default_rng(20260902)
max_dev = 0.0
for _ in range(500):
    amat = rngf.normal(size=(3, 3))  # a_i^b, constant (j=0) so no derivatives
    tv = float(rngf.uniform(-2, 3))
    direct = 0.0
    for i, j_ in PAIRS:
        for b in range(3):
            Fij = (tv**2 - tv) * EPS[b, i, j_]
            brk = sum(
                EPS[b, c, dd] * amat[i, c] * amat[j_, dd] for c in range(3) for dd in range(3)
            )
            direct += 2.0 * Fij * brk
    vec = np.zeros(9, dtype=complex)
    for i in range(3):
        for b in range(3):
            vec[idx1(i, b, 0, 1)] = amat[i, b]
    closed = float(np.real(vec.conj() @ build_F_term(tv, 0) @ vec))
    max_dev = max(max_dev, abs(direct - closed))
fterm_ok = max_dev < 1e-10
print(f"  max |direct - closed form| over 500 random (a, t):  {max_dev:.3e}   -> {fterm_ok}")

# and the FULL quadratic form against a direct evaluation, derivatives included:
# use a single Peter-Weyl block and compare Q built from the matrices against a
# term-by-term rebuild of  sum_{i<j}|d_A a|^2 + 2 sum_{i<j}<F,[a,a]>.
print("  Same for the FULL quadratic form Q on a nontrivial Peter-Weyl block")
print("  (2j=3), rebuilt term by term from the component formula:")
two_j_chk = 3
d_chk = two_j_chk + 1
rho_chk = spin_matrices(two_j_chk)
max_dev2 = 0.0
for _ in range(50):
    tv = float(rngf.uniform(-1.5, 2.5))
    cvec = rngf.normal(size=9 * d_chk) + 1j * rngf.normal(size=9 * d_chk)
    a_arr = np.zeros((3, 3, d_chk), dtype=complex)
    for i in range(3):
        for b in range(3):
            for n in range(d_chk):
                a_arr[i, b, n] = cvec[idx1(i, b, n, d_chk)]
    # direct: |d_A a|^2 term by term
    direct = 0.0
    for i, j_ in PAIRS:
        for b in range(3):
            comp = rho_chk[i] @ a_arr[j_, b, :] - rho_chk[j_] @ a_arr[i, b, :]
            for k in range(3):
                comp = comp - EPS[i, j_, k] * a_arr[k, b, :]
            for dd in range(3):
                comp = comp + tv * EPS[b, i, dd] * a_arr[j_, dd, :]
                comp = comp - tv * EPS[b, j_, dd] * a_arr[i, dd, :]
            direct += float(np.real(np.vdot(comp, comp)))
    # direct: F-term, hermitian-symmetrised (real quadratic form on real fields)
    fpart = 0.0
    for i, j_ in PAIRS:
        for b in range(3):
            Fij = (tv**2 - tv) * EPS[b, i, j_]
            for c in range(3):
                for dd in range(3):
                    if EPS[b, c, dd]:
                        fpart += (
                            2.0
                            * Fij
                            * EPS[b, c, dd]
                            * float(np.real(np.vdot(a_arr[i, c, :], a_arr[j_, dd, :])))
                        )
    direct += fpart
    closed = float(np.real(cvec.conj() @ hessian_block(tv, two_j_chk) @ cvec))
    max_dev2 = max(max_dev2, abs(direct - closed))
full_ok = max_dev2 < 1e-8
print(f"  max |direct - assembled Q| over 50 random (a, t) at 2j=3:  {max_dev2:.3e}  -> {full_ok}")
print("  -> the assembled matrices reproduce the component formula they claim to")
print("     implement, on generic input, not just on the one control vector.")
RESULTS["part4d_F_term_closed_form_max_deviation"] = max_dev
RESULTS["part4d_F_term_closed_form_ok"] = bool(fterm_ok)
RESULTS["part4d_full_quadratic_form_max_deviation"] = max_dev2
RESULTS["part4d_full_quadratic_form_ok"] = bool(full_ok)
print()
# ---------------------------------------------------------------------------
# PART 4e -- cross-check the rep matrices against the project's CERTIFIED
#            C85 Peter-Weyl module (claim.md's "reuse rather than rebuild")
# ---------------------------------------------------------------------------
hr("PART 4e -- cross-check rho_j(T_i) against C85's certified build_l_matrices")
print("  claim.md asks to reuse this project's certified Peter-Weyl apparatus")
print("  rather than rebuild.  Honest position: C85's module builds `D-bar_k`,")
print("  a Dirac-type operator (quaternion right-multiplication x su(2)")
print("  L-matrices) -- and C107 already established D-bar_k is NOT the same")
print("  object as the torsion family D^t.  It contains NO 1-form/2-form")
print("  complex, no d_A, no Yang-Mills F-term, so the fluctuation operator")
print("  here HAD to be built.  But its `build_l_matrices` IS the same su(2)")
print("  representation this round needs, so that piece is cross-checked")
print("  against the certified module instead of merely re-derived.")

_c85_path = (
    pathlib.Path(__file__).resolve().parent.parent
    / "20260812-c85-peter-weyl-representation-certification"
    / "c85_certification.py"
)
c85_available = _c85_path.exists()
print(f"  C85 module found at {_c85_path.name}?                            {c85_available}")
c85_rows, c85_ok = [], True
if c85_available:
    _spec = importlib.util.spec_from_file_location("c85_certification", _c85_path)
    _c85 = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_c85)
    for k in range(7):  # k = 2j
        lmats = _c85.build_l_matrices(k, "repaired")
        brk = _c85.bracket_residuals(*lmats)
        cas = _c85.casimir_residual(k, *lmats)
        # C85 convention: [l_1,l_2] = 2 l_3  and  -(sum l_i^2) = k(k+2) Id.
        # This round: [rho_i,rho_j] = eps_ijk rho_k  and  sum rho_i^2 = -j(j+1).
        # So l_i must equal 2*rho_i up to a similarity transformation.
        rho = spin_matrices(k)
        cas_mine = sum(r @ r for r in rho)
        j = k / 2.0
        cas_mine_ok = np.allclose(cas_mine, -j * (j + 1) * np.eye(k + 1), atol=1e-10)
        # rescaled Casimirs must agree exactly:  -(sum (2 rho_i)^2) = k(k+2) Id
        rescaled = -4.0 * cas_mine
        casimir_agree = np.allclose(rescaled, k * (k + 2) * np.eye(k + 1), atol=1e-10)
        # spectra of the diagonal generator must agree up to sign/conjugation
        l1_eigs = np.sort_complex(
            np.array([complex(z) for z in sp.Matrix(lmats[0]).eigenvals(multiple=True)]) / 2.0
        )
        rho_eigs = np.sort_complex(np.linalg.eigvals(rho[2]))
        spec_agree = np.allclose(
            np.sort(np.abs(l1_eigs.imag)), np.sort(np.abs(rho_eigs.imag)), atol=1e-9
        )
        ok = bool(
            brk["all_brackets_hold"]
            and cas["casimir_holds_exactly"]
            and cas_mine_ok
            and casimir_agree
            and spec_agree
        )
        c85_ok = c85_ok and ok
        c85_rows.append(
            {
                "k_equals_2j": k,
                "c85_brackets_hold": bool(brk["all_brackets_hold"]),
                "c85_casimir_holds": bool(cas["casimir_holds_exactly"]),
                "this_round_casimir_is_minus_j_jplus1": bool(cas_mine_ok),
                "rescaled_casimirs_agree": bool(casimir_agree),
                "generator_spectra_agree": bool(spec_agree),
                "all": ok,
            }
        )
        print(
            f"    k=2j={k}: C85 brackets={brk['all_brackets_hold']}, C85 Casimir="
            f"{cas['casimir_holds_exactly']}, mine=-j(j+1)={cas_mine_ok}, "
            f"rescaled Casimirs agree={casimir_agree}, spectra agree={spec_agree}"
        )
    print()
    print("  rho_j(T_i) agrees with C85's certified l-matrices (l_i = 2 rho_i, up")
    print(f"  to similarity) for k = 0..6?                                   {c85_ok}")
else:
    print("  SKIPPED -- module not found; the rep matrices remain validated by")
    print("  PART 4 (brackets + anti-hermiticity) and PART 4c (Hodge spectrum).")
RESULTS["part4e_c85_module_available"] = bool(c85_available)
RESULTS["part4e_c85_cross_check"] = c85_rows
RESULTS["part4e_c85_cross_check_passed"] = bool(c85_ok and c85_available)
print()
# ---------------------------------------------------------------------------
# PART 5 -- negative control at the OTHER critical point, t=1/2
# ---------------------------------------------------------------------------
hr("PART 5 -- NEGATIVE CONTROL: the operator must find the known instability at t=1/2")
print("  Counting negative modes is only meaningful AT a critical point (where")
print("  the gradient vanishes).  PART 2 found exactly three: t = 0, 1/2, 1.")
print("  t=1/2 is the one C123 already knows to be unstable in the 1D slice.")
print()
crit_index: dict = {}
for tv, tag in [(0.0, "t=0"), (0.5, "t=1/2"), (1.0, "t=1")]:
    nneg = 0
    negvals = []
    for two_j in range(TWO_J_MAX + 1):
        ev = np.linalg.eigvalsh(hessian_block(tv, two_j))
        k = int(np.sum(ev < -1e-9))
        nneg += k * (two_j + 1)
        negvals.extend([float(x) for x in ev if x < -1e-9])
    crit_index[tag] = {
        "morse_index_with_multiplicity": nneg,
        "negative_eigenvalues": negvals,
    }
    print(
        f"    {tag:<6}  Morse index (negative modes, with multiplicity) = {nneg}"
        f"   negative eigenvalues = {[round(v, 8) for v in negvals]}"
    )
neg_ctrl_ok = crit_index["t=1/2"]["morse_index_with_multiplicity"] > 0
print()
print(f"  NEGATIVE CONTROL PASSED (instability detected at t=1/2)?   {neg_ctrl_ok}")

H_half = hessian_block(0.5, 0)
evals, evecs = np.linalg.eigh(H_half)
u = evecs[:, 0]
fam = v0 / np.linalg.norm(v0)
overlap = float(abs(np.vdot(fam, u)))
print(f"  |<family direction | lowest eigenvector at t=1/2>| = {overlap:.12f}")
print(
    f"  lowest eigenvalue at t=1/2 = {evals[0]:.12f}  "
    f"( = Q[family]/||family||^2 = {-1.5 / 3.0:.12f} )"
)
print("  -> the unique unstable direction at Levi-Civita IS the Cartan-Schouten")
print("     family direction.  The full operator neither adds nor removes")
print("     unstable directions there: Morse index exactly 1, modulo gauge.")
RESULTS["part5_critical_point_morse_indices"] = crit_index
RESULTS["part5_negative_control_passed"] = bool(neg_ctrl_ok)
RESULTS["part5_t_half_unstable_direction_overlap_with_family"] = overlap

print()
print("  Scan of the smallest eigenvalue along t (NOT a Morse index away from")
print("  the three critical points -- at non-critical t the gauge directions")
print("  acquire nonzero eigenvalues of either sign, because")
print("  delta^2 S[d_A phi, d_A phi] = -delta S[second-order orbit term] != 0.")
print("  Reported for shape only):")
neg_scan = []
for tv in [0.0, 0.1, 0.2113, 0.25, 0.4, 0.5, 0.6, 0.75, 0.7887, 0.9, 1.0]:
    mins = [float(np.linalg.eigvalsh(hessian_block(tv, tj))[0]) for tj in range(TWO_J_MAX + 1)]
    neg_scan.append({"t": tv, "min_eig": min(mins)})
    print(f"    t={tv:<7} min eig = {min(mins):>12.6f}")
roots = sp.solve(sp.Eq(6 * t**2 - 6 * t + 1, 0), t)
print(
    f"  (1D slice) family direction is negative on t in "
    f"({float(min(roots)):.6f}, {float(max(roots)):.6f})."
)
print("  CORRECTED (FL Step 8a skeptic finding E4 -- an earlier draft of this")
print("  line claimed the min-eig curve 'tracks it exactly', which the table")
print("  above refutes: at t=0.1 the minimum is -0.1056 while the family")
print("  direction is +0.46, and at t=0.25 the minimum -0.1553 is BELOW the")
print("  family value -0.125).  The minimum is dominated by near-gauge modes")
print("  away from the critical points and coincides with the family direction")
print("  ONLY at t=1/2, where the gauge modes are exact zeros.")
RESULTS["part5_t_scan_min_eig"] = neg_scan
RESULTS["part5_family_direction_negative_interval"] = [
    float(min(roots)),
    float(max(roots)),
]
print()


# ---------------------------------------------------------------------------
# PART 6 -- A^0 and A^1 lie on ONE gauge orbit (verified, not asserted)
# ---------------------------------------------------------------------------
hr("PART 6 -- A^0 and A^1 are on ONE gauge orbit of the SO(3) bundle over id_{S^3}")
print("  Claim to check numerically:  A^1 = G^{-1} dG  with  G = Ad : SU(2) -> SO(3),")
print("  i.e. A^1 is PURE GAUGE and A^0 = 0 is the trivial connection, related by a")
print("  bundle automorphism over the IDENTITY diffeomorphism (no orientation flip).")

_SX = np.array([[0, 1], [1, 0]], dtype=complex)
_SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
_SZ = np.array([[1, 0], [0, -1]], dtype=complex)
TM = [
    -0.5j * _SX,
    -0.5j * _SY,
    -0.5j * _SZ,
]  # T_a = -i sigma_a/2, [T_i,T_j]=eps_ijk T_k


def su2_exp(v: np.ndarray) -> np.ndarray:
    Xm = sum(v[a] * TM[a] for a in range(3))
    w, U = np.linalg.eigh(1j * Xm)
    return U @ np.diag(np.exp(-1j * w)) @ U.conj().T


def Ad_matrix(x: np.ndarray) -> np.ndarray:
    """R_{ab} defined by  x T_b x^{-1} = sum_a T_a R_{ab}  (<T_a,T_c> = -2 tr = delta)."""
    R = np.zeros((3, 3))
    xi = np.linalg.inv(x)
    for b in range(3):
        Y = x @ TM[b] @ xi
        for a in range(3):
            R[a, b] = float(np.real(-2.0 * np.trace(TM[a] @ Y)))
    return R


adT = [np.array([[-EPS[i, a, b] for b in range(3)] for a in range(3)]) for i in range(3)]
adT_ok = all(
    np.allclose(adT[i] @ adT[j_] - adT[j_] @ adT[i], adT[k], atol=1e-12)
    for i, j_, k in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
)
print(f"    ad(T_i) matrices reproduce [ad T_i, ad T_j] = eps_ijk ad T_k?   {adT_ok}")

rng0 = np.random.default_rng(126126)
hstep = 1e-6
max_err, is_orth_all = 0.0, True
for _ in range(50):
    x = su2_exp(rng0.normal(scale=1.3, size=3))
    R = Ad_matrix(x)
    is_orth_all = (
        is_orth_all and np.allclose(R @ R.T, np.eye(3), atol=1e-9) and np.linalg.det(R) > 0
    )
    Rinv = np.linalg.inv(R)
    for i in range(3):
        e = np.zeros(3)
        e[i] = hstep
        XiR = (Ad_matrix(x @ su2_exp(e)) - Ad_matrix(x @ su2_exp(-e))) / (2 * hstep)
        max_err = max(max_err, float(np.max(np.abs(Rinv @ XiR - adT[i]))))
gauge_ok = max_err < 1e-6
print(f"    Ad(x) is in SO(3) at all 50 sampled points?                    {is_orth_all}")
print(f"    max over x,i of | R^-1 (X_i R) - ad(T_i) | = {max_err:.3e}  (ad(T_i) == A^1_i)")
print(f"    -> A^1 is pure gauge, G^-1 dG with G = Ad:                     {gauge_ok}")
print("    [tool-verified by finite differences on the group, not asserted]")
RESULTS["part6_adT_bracket_ok"] = bool(adT_ok)
RESULTS["part6_Ad_is_SO3"] = bool(is_orth_all)
RESULTS["part6_pure_gauge_max_error"] = max_err
RESULTS["part6_pure_gauge_verified"] = bool(gauge_ok)

flat_ok = all(
    abs(float((tv**2 - tv) * EPS[b, i, j])) < TOL
    for tv in (0.0, 1.0)
    for i, j in PAIRS
    for b in range(3)
)
print(f"    consequence (i)  F(A^0) = F(A^1) = 0                           {flat_ok}")


def total_spectrum(tv: float, two_j_max: int) -> np.ndarray:
    out: list = []
    for two_j in range(two_j_max + 1):
        ev = np.linalg.eigvalsh(hessian_block(tv, two_j))
        out.extend(list(np.repeat(ev, two_j + 1)))
    return np.sort(np.array(out))


LAM_CUT = 6.0
s0 = total_spectrum(0.0, TWO_J_HIGH)
s1 = total_spectrum(1.0, TWO_J_HIGH)
s0c, s1c = s0[s0 < LAM_CUT], s1[s1 < LAM_CUT]
iso_ok = len(s0c) == len(s1c) and np.allclose(s0c, s1c, atol=1e-7)
print(f"    consequence (ii) total spectra below lambda={LAM_CUT} identical?      {iso_ok}")
print(
    f"                     counts t=0 -> {len(s0c)}, t=1 -> {len(s1c)}, "
    f"max|diff| = {(np.max(np.abs(s0c - s1c)) if iso_ok else float('nan')):.2e}"
)
print("    Direct evidence of the promised block mixing: the covariantly-constant")
print("    adjoint sections (3 of them) sit in the 2j=0 block at t=0 and in the")
print("    2j=2 block at t=1 -- see PART 4's 'rk d_A' column (0 vs 3 at 2j=0).")
RESULTS["part6_both_flat"] = bool(flat_ok)
RESULTS["part6_isospectral_below_cut"] = bool(iso_ok)
RESULTS["part6_lambda_cut"] = LAM_CUT
print()
print("  SCOPE, stated because it is easy to overread (and because a sibling")
print("  round, C125, owns the neighbouring question):  this is gauge")
print("  equivalence of the SO(3) CONNECTION alone, i.e. after FORGETTING the")
print("  soldering form.  As AFFINE connections on TS^3 the two are NOT")
print("  equivalent -- their torsions have opposite sign (checked below) -- and")
print("  relating THOSE still needs the orientation-reversing iota of")
print("  C37-C39/OB13.  Nothing here settles the full 13D configuration")
print("  question (vielbein + twist bundle + fermions) that C125 is about.")
tor0 = np.array([[float((2 * 0.0 - 1) * EPS[i, j, k]) for k in range(3)] for i, j in PAIRS])
tor1 = np.array([[float((2 * 1.0 - 1) * EPS[i, j, k]) for k in range(3)] for i, j in PAIRS])
tor_opposite = bool(np.allclose(tor0, -tor1, atol=TOL) and not np.allclose(tor0, tor1))
print(f"    torsion T^t(X_i,X_j) = (2t-1)[X_i,X_j]:  T^0 = -T^1 and T^0 != T^1 ?  {tor_opposite}")
RESULTS["part6_torsion_opposite_sign"] = tor_opposite
print()


# ---------------------------------------------------------------------------
# PART 6b -- is that gauge transformation SMALL or LARGE?
# ---------------------------------------------------------------------------
hr("PART 6b -- winding number of G = Ad : the gauge transformation is LARGE")
print("  PART 6 showed A^1 = G^-1 dG.  A gauge transformation connected to the")
print("  identity would make A^0 and A^1 indistinguishable by EVERY functional")
print("  invariant under the identity component alone -- Chern-Simons included.")
print("  A prior round found CS(0) != CS(1), so G had better be LARGE.  Check it")
print("  by computing the winding number, exactly.")

# radius of S^3 in this normalisation, from the sectional curvature of the
# Levi-Civita member t=1/2:  R^{1/2}(X,Y)Z = -(1/4)[[X,Y],Z]
# K(X_1,X_2) = <R(X_1,X_2)X_2, X_1> = -(1/4)<[[X_1,X_2],X_2], X_1> = 1/4
Zt = [sp.Matrix(Ti) for Ti in T]  # T_a = -Z_a/2 from PART 0


def _brm(P, Q):
    return sp.simplify(P * Q - Q * P)


sec_num = _brm(_brm(Zt[0], Zt[1]), Zt[1])  # [[X1,X2],X2]


# express in the basis: <A,B> := -2 tr(A B) makes T_a orthonormal
def _ip(P, Q):
    return sp.simplify(-2 * sp.trace(P * Q))


orthonormal_ok = all(_ip(Zt[a], Zt[b]) == (1 if a == b else 0) for a in range(3) for b in range(3))
K = sp.simplify(sp.Rational(-1, 4) * _ip(sec_num, Zt[0]))
Rsphere = sp.simplify(1 / sp.sqrt(K))
VolS3 = sp.simplify(2 * sp.pi**2 * Rsphere**3)
print(f"  T_a orthonormal under <A,B> = -2 tr(AB)?                      {orthonormal_ok}")
print(f"  sectional curvature K(X_1,X_2) of the Levi-Civita member       K = {K}")
print(f"  => S^3 radius R = 1/sqrt(K) = {Rsphere},  Vol(S^3) = 2 pi^2 R^3 = {VolS3}")

# theta = sum_i e^i T_i is the Maurer-Cartan form (c0 = +1, PART 0), so
#   tr(theta ^ theta ^ theta) = [ sum_{ijk} eps_ijk tr(T_i T_j T_k) ] e^1^e^2^e^3
Wcoef = sp.simplify(
    sum(
        sp.Integer(int(EPS[i, j_, k])) * sp.trace(Zt[i] * Zt[j_] * Zt[k])
        for i in range(3)
        for j_ in range(3)
        for k in range(3)
    )
)
winding = sp.simplify(Wcoef * VolS3 / (24 * sp.pi**2))
print(f"  sum_ijk eps_ijk tr(T_i T_j T_k) = {Wcoef}")
print(f"  n = (1/24 pi^2) * Int_S3 tr((g^-1 dg)^3) = {Wcoef} * {VolS3} / (24 pi^2) = {winding}")
print(f"  |n| = {sp.Abs(winding)}  -> G is a GENERATOR of pi_3(SU(2)) = pi_3(SO(3)) = Z.")
print("  (the SU(2) lift is used: Ad induces an isomorphism on pi_3, so the")
print("   winding of G = Ad in pi_3(SO(3)) equals that of its lift, the identity")
print("   map SU(2) -> SU(2).)  [CITED for the pi_3 isomorphism; the integral")
print("   itself is computed here.]")
large_gauge = bool(abs(abs(complex(sp.N(winding))) - 1.0) < 1e-12)
print(f"  => the gauge transformation relating A^0 to A^1 is LARGE, not small:  {large_gauge}")
print()
print("  CONSEQUENCE, and it is the sharp statement this round contributes to")
print("  the t-selection question:")
print("    * any functional invariant under the FULL gauge group (large")
print("      transformations included) -- S_YM, and every curvature-norm")
print("      invariant of omega alone -- is STRUCTURALLY blind to t=0 vs t=1,")
print("      because they are the same point of the quotient space;")
print("    * a functional invariant only under the IDENTITY COMPONENT can")
print("      distinguish them, and must shift by the winding number -- which is")
print("      exactly what a Chern-Simons functional does, and exactly why a")
print("      prior round measured CS(0) != CS(1).")
RESULTS["part6b_orthonormal_basis_ok"] = bool(orthonormal_ok)
RESULTS["part6b_sectional_curvature"] = str(K)
RESULTS["part6b_S3_radius"] = str(Rsphere)
RESULTS["part6b_S3_volume"] = str(VolS3)
RESULTS["part6b_trace_coefficient"] = str(Wcoef)
RESULTS["part6b_winding_number"] = str(winding)
RESULTS["part6b_gauge_transformation_is_large"] = large_gauge
print()
# ---------------------------------------------------------------------------
# PART 7 -- ALL homogeneous (left-invariant) connections: 9-parameter scan
# ---------------------------------------------------------------------------
hr("PART 7 -- ALL homogeneous (left-invariant) connections: full 9-parameter scan")
print("  A general left-invariant connection is a 3x3 real matrix M (M_i^b), of")
print("  which the family A^t = t*Id is a single line.  This addresses claim.md's")
print("  secondary clause: do new stable homogeneous vacua appear outside {0,1}?")


def F_hom(M: np.ndarray) -> np.ndarray:
    return -np.einsum("ijk,kb->ijb", EPS, M) + np.einsum("bcd,ic,jd->ijb", EPS, M, M)


def V_hom(M: np.ndarray) -> float:
    return 0.5 * float(np.sum(F_hom(M) ** 2))


def grad_V(M: np.ndarray) -> np.ndarray:
    F = F_hom(M)
    g = -np.einsum("ijq,ijp->pq", F, EPS)
    g += np.einsum("pjb,bqd,jd->pq", F, EPS, M)
    g += np.einsum("ipb,bcq,ic->pq", F, EPS, M)
    return g


Mtest = np.random.default_rng(7).normal(size=(3, 3))
gfd = np.zeros((3, 3))
for i in range(3):
    for b in range(3):
        Mp, Mm = Mtest.copy(), Mtest.copy()
        Mp[i, b] += 1e-6
        Mm[i, b] -= 1e-6
        gfd[i, b] = (V_hom(Mp) - V_hom(Mm)) / 2e-6
grad_ok = bool(np.allclose(grad_V(Mtest), gfd, atol=1e-5))
print(f"  analytic grad V matches finite differences?                    {grad_ok}")
print(f"    (max abs difference = {float(np.max(np.abs(grad_V(Mtest) - gfd))):.2e})")
RESULTS["part7_gradient_verified"] = grad_ok

rng = np.random.default_rng(20260901)
crit = []
for _ in range(800):
    M0 = rng.normal(scale=1.0, size=(3, 3))
    sol = root(lambda v: grad_V(v.reshape(3, 3)).ravel(), M0.ravel(), method="hybr", tol=1e-13)
    M = sol.x.reshape(3, 3)
    if float(np.max(np.abs(grad_V(M)))) < 1e-9:
        crit.append(M)
print(f"  critical points located (800 random starts, |grad V|_inf < 1e-9):  {len(crit)}")

classes: dict = {}
for M in crit:
    v = V_hom(M)
    if np.allclose(M, 0, atol=1e-7):
        key = "M = 0                                (this IS t=0)"
    elif np.allclose(M @ M.T, np.eye(3), atol=1e-6):
        key = f"M orthogonal, det={np.sign(np.linalg.det(M)):+.0f}          (det=+1 contains t=1)"
    elif np.allclose(4 * (M @ M.T), np.eye(3), atol=1e-6):
        key = (
            f"M = (1/2) x orthogonal, det={np.sign(np.linalg.det(M)):+.0f}  (det=+1 contains t=1/2)"
        )
    else:
        key = f"OTHER  V={v:.6f}  singular values {np.round(np.linalg.svd(M)[1], 4)}"
    classes.setdefault(key, []).append(v)
for k in sorted(classes):
    vs = np.array(classes[k])
    print(f"    n={len(vs):>4}  V in [{vs.min():.9f}, {vs.max():.9f}]   {k}")


def is_flat_hom(M: np.ndarray) -> bool:
    return V_hom(M) < 1e-12


rand_orth_flat = True
for _ in range(300):
    Q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    if np.linalg.det(Q) < 0:
        Q[:, 0] *= -1.0
    rand_orth_flat = rand_orth_flat and is_flat_hom(Q)
det_minus_flat = is_flat_hom(np.diag([1.0, 1.0, -1.0]))
non_orth_flat = any(
    is_flat_hom(M) and not np.allclose(M @ M.T, np.eye(3), atol=1e-6) and not np.allclose(M, 0)
    for M in crit
)
print()
print(f"  every SO(3) matrix M is a flat (V=0) connection?               {rand_orth_flat}")
print(f"  a det=-1 orthogonal M (diag(1,1,-1)) also flat?                {det_minus_flat}")
print(f"  any flat critical M outside 0 u SO(3) among those found?       {non_orth_flat}")
print("  NOTE the det=-1 answer is False and that is CORRECT, not a defect:")
print("  Aut(su(2)) = SO(3), NOT O(3) -- a det=-1 orthogonal map reverses the")
print("  cross product, so it is an ANTI-automorphism and is not flat.")
print("  algebraic reason (not just numerics): F=0 <=> [M_i,M_j]=eps_ijk M_k,")
print("  i.e. T_i -> M_i is a Lie algebra homomorphism su(2)->su(2).  su(2) is")
print("  simple, so the kernel is 0 or everything: M = 0, or M is an")
print("  automorphism, i.e. an element of Aut(su(2)) = SO(3).")
aut_check = True
for _ in range(200):
    Q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    if np.linalg.det(Q) < 0:
        Q[:, 0] *= -1.0
    for i, j_, k in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        aut_check = aut_check and np.allclose(np.cross(Q[i], Q[j_]), Q[k], atol=1e-9)
print(f"  SO(3) rows satisfy [M_i,M_j] = eps_ijk M_k (cross product)?     {aut_check}")
RESULTS["part7_n_critical_points"] = len(crit)
RESULTS["part7_classes"] = {
    k: {"count": len(v), "V_min": float(min(v)), "V_max": float(max(v))} for k, v in classes.items()
}
RESULTS["part7_every_SO3_is_flat"] = bool(rand_orth_flat)
RESULTS["part7_det_minus_one_orthogonal_flat"] = bool(det_minus_flat)
RESULTS["part7_non_orthogonal_flat_found"] = bool(non_orth_flat)
RESULTS["part7_SO3_is_automorphism_group"] = bool(aut_check)
print()
print("  CONSEQUENCE for claim.md's secondary clause: the homogeneous vacuum")
print("  set is {0} u SO(3), NOT just {t=0, t=1}.  Every one of these has")
print("  S_YM = 0, the same absolute minimum, and SO(3) is a single gauge orbit")
print("  (PART 6 -- the identity of SO(3) is t=1, and it is gauge-equivalent to")
print("  M=0 which is t=0).  So no new vacuum appears that S_YM ITSELF could use")
print("  to break the t=0 vs t=1 degeneracy -- there are MORE exactly degenerate")
print("  minima than the 1-parameter family sees, not fewer, which makes the")
print("  selection problem strictly HARDER for S_YM, not easier.")
print()
print("  CORRECTED (FL Step 8a skeptic finding E8 -- an earlier draft said 'no")
print("  NEW vacua in ANY sense', which is false and self-undermining).  There")
print("  IS another sense, and it is exactly the one that matters: {0} and SO(3)")
print("  are two DIFFERENT connected components of the flat set, sitting in")
print("  different small-gauge winding sectors (PART 6b).  The full flat set has")
print("  one component per winding number -- the standard theta-vacuum ladder.")
print("  S_YM cannot see that label; a Chern-Simons-type functional can.  So the")
print("  correct statement is scoped to S_YM, not universal.")
print()


# ---------------------------------------------------------------------------
# PART 7b -- EXACT symbolic classification of the homogeneous critical set
# ---------------------------------------------------------------------------
hr("PART 7b -- exact symbolic classification of ALL homogeneous critical points")
print("  V(M) is invariant under  M -> h M R^T  for h,R in SO(3)  (h = global")
print("  internal gauge rotation; R = a right translation of S^3, which acts on")
print("  the left-invariant frame by a rotation).  Both invariances are verified")
print("  numerically first, then USED: every orbit has a DIAGONAL representative")
print("  (SVD, signs absorbed), so scanning diagonal M finds a representative of")
print("  EVERY critical orbit.  That turns a 9-parameter search into an exactly")
print("  solvable 3-variable polynomial system.")

rng2 = np.random.default_rng(4242)


def _rand_so3(rg) -> np.ndarray:
    Q, _ = np.linalg.qr(rg.normal(size=(3, 3)))
    if np.linalg.det(Q) < 0:
        Q[:, 0] *= -1.0
    return Q


inv_h_ok = inv_R_ok = True
for _ in range(200):
    M = rng2.normal(size=(3, 3))
    inv_h_ok = inv_h_ok and abs(V_hom(M @ _rand_so3(rng2).T) - V_hom(M)) < 1e-9
    inv_R_ok = inv_R_ok and abs(V_hom(_rand_so3(rng2) @ M) - V_hom(M)) < 1e-9
print(f"  V invariant under internal SO(3) rotation of the b index?      {inv_h_ok}")
print(f"  V invariant under frame SO(3) rotation of the i index?         {inv_R_ok}")
RESULTS["part7b_internal_so3_invariance"] = bool(inv_h_ok)
RESULTS["part7b_frame_so3_invariance"] = bool(inv_R_ok)

m1, m2, m3 = sp.symbols("m1 m2 m3", real=True)
Vdiag = (m1 * m2 - m3) ** 2 + (m1 * m3 - m2) ** 2 + (m2 * m3 - m1) ** 2
diag_ok = True
for _ in range(50):
    vv = rng2.normal(size=3)
    diag_ok = (
        diag_ok
        and abs(float(Vdiag.subs({m1: vv[0], m2: vv[1], m3: vv[2]})) - V_hom(np.diag(vv))) < 1e-10
    )
print(f"  closed form V(diag) = (m1m2-m3)^2+(m1m3-m2)^2+(m2m3-m1)^2 ?     {diag_ok}")
eqs = [sp.expand(sp.diff(Vdiag, v) / 2) for v in (m1, m2, m3)]
print("  stationarity equations (grad V / 2 = 0):")
for e in eqs:
    print(f"    {sp.factor(e)} = 0")
sols = sp.solve(eqs, [m1, m2, m3], dict=True)
uniq = []
for s_ in sols:
    vals = [s_.get(v, v) for v in (m1, m2, m3)]
    if any(getattr(val, "free_symbols", set()) for val in vals):
        continue
    nv = [complex(sp.N(val)) for val in vals]
    if any(abs(z.imag) > 1e-12 for z in nv):
        continue
    key = tuple(round(z.real, 10) for z in nv)
    if key not in [tuple(round(float(y), 10) for y in u) for u in uniq]:
        uniq.append([sp.nsimplify(sp.Rational(round(z.real * 2), 2)) for z in nv])
print(f"  sympy solve() returned {len(sols)} branches -> {len(uniq)} distinct REAL points")


def hom_hessian(Mv: np.ndarray) -> np.ndarray:
    hh = 1e-4
    H = np.zeros((9, 9))
    for aa in range(9):
        for bb in range(9):
            ea = np.zeros(9)
            ea[aa] = hh
            eb = np.zeros(9)
            eb[bb] = hh
            H[aa, bb] = (
                V_hom(Mv + (ea + eb).reshape(3, 3))
                - V_hom(Mv + (ea - eb).reshape(3, 3))
                - V_hom(Mv + (eb - ea).reshape(3, 3))
                + V_hom(Mv - (ea + eb).reshape(3, 3))
            ) / (4 * hh * hh)
    return 0.5 * (H + H.T)


crit_exact = []
for r in sorted(
    uniq,
    key=lambda z: (float(V_hom(np.diag([float(x) for x in z]))), [float(x) for x in z]),
):
    mv = np.diag([float(x) for x in r])
    v = V_hom(mv)
    evh = np.linalg.eigvalsh(hom_hessian(mv))
    nneg = int(np.sum(evh < -1e-5))
    nzero = int(np.sum(np.abs(evh) <= 1e-5))
    crit_exact.append(
        {
            "m": [str(x) for x in r],
            "V": float(v),
            "flat": bool(v < 1e-12),
            "det_sign": int(np.sign(round(np.linalg.det(mv), 9)))
            if abs(np.linalg.det(mv)) > 1e-12
            else 0,
            "hom_hessian_signature_neg_zero_pos": [nneg, nzero, 9 - nneg - nzero],
        }
    )
    print(
        f"    m = ({', '.join(str(x) for x in r):<16})  V = {float(v):<9.6f} flat={v < 1e-12!s:<5}"
        f" hom-Hessian signature (-,0,+) = ({nneg},{nzero},{9 - nneg - nzero})"
    )
n_flat = sum(1 for c in crit_exact if c["flat"])
n_saddle = sum(
    1 for c in crit_exact if (not c["flat"]) and c["hom_hessian_signature_neg_zero_pos"][0] > 0
)
n_nonflat_min = sum(
    1 for c in crit_exact if (not c["flat"]) and c["hom_hessian_signature_neg_zero_pos"][0] == 0
)
print()
print(f"  distinct critical points on the diagonal slice (exact):   {len(crit_exact)}")
print(f"    flat (V=0, hence GLOBAL minima):                        {n_flat}")
print(f"    non-flat with >=1 negative direction (saddles):         {n_saddle}")
print("    non-flat with NO negative direction  ->  a NEW stable")
print(f"    homogeneous vacuum, claim.md's secondary clause:        {n_nonflat_min}")
print()
print("  EXHAUSTIVE up to the SO(3)xSO(3) symmetry verified above: every")
print("  homogeneous critical point has a diagonal representative in its orbit,")
print("  and every diagonal critical point appears in this list.")
RESULTS["part7b_exact_critical_points"] = crit_exact
RESULTS["part7b_n_flat"] = n_flat
RESULTS["part7b_n_nonflat_saddle"] = n_saddle
RESULTS["part7b_n_nonflat_minimum"] = n_nonflat_min
RESULTS["part7b_closed_form_verified"] = bool(diag_ok)
print()
# ---------------------------------------------------------------------------
# PART 4f -- d_A o d_A = 0 at the flat points  (skeptic finding E5)
# ---------------------------------------------------------------------------
hr("PART 4f -- operator-level check  d_A o d_A = 0  (E5: kernel claim needs it)")
print("  PART 4 concludes 'kernel = gauge orbit' from a DIMENSION COUNT")
print("  (dim ker Q == rank d_A).  That licenses the conclusion only via")
print("  im d_A subset ker d_A, i.e. d_A o d_A = 0 -- the one identity tying the")
print("  two independently-built matrices together, and it was never checked.")
print("  Checked now, at the operator level, with its own negative control:")
print("  d_A o d_A = [F, .], so it must VANISH at t=0,1 and NOT vanish at t=1/2.")
dd_rows = []
dd_ok = True
for tv, tag in [(0.0, "t=0"), (0.5, "t=1/2"), (1.0, "t=1")]:
    norms = []
    for two_j in range(TWO_J_MAX + 1):
        prod = build_dA_1form(tv, two_j) @ build_dA_0form(tv, two_j)
        norms.append(float(np.linalg.norm(prod)))
    mx = max(norms)
    should_vanish = tag in ("t=0", "t=1")
    ok = (mx < 1e-10) if should_vanish else (mx > 1e-3)
    dd_ok = dd_ok and ok
    dd_rows.append({"t": tv, "max_norm_dA_dA": mx, "expected_zero": should_vanish, "ok": bool(ok)})
    print(
        f"    {tag:<6}  max_j ||d_A o d_A|| = {mx:<22.12g}"
        f" expected {'ZERO' if should_vanish else 'NONZERO'}   ok={ok}"
    )
print(f"  d_A o d_A = 0 exactly at the flat points, nonzero at t=1/2?     {dd_ok}")
print("  -> the two matrices really are consecutive maps of one complex, so the")
print("     dimension count in PART 4 does license 'kernel = gauge orbit'.")
RESULTS["part4f_dA_squared_rows"] = dd_rows
RESULTS["part4f_dA_squared_ok"] = bool(dd_ok)
print()


# ---------------------------------------------------------------------------
# PART 5b -- Morse index at t=1/2 at the HIGH cutoff  (skeptic finding E7)
# ---------------------------------------------------------------------------
hr("PART 5b -- t=1/2 Morse index re-run at 2j <= 14 (E7: it was only checked at 8)")
print("  PART 4b pushed the cutoff only at t=0 and t=1 -- exactly the two points")
print("  where PART 3 already settles the answer without any cutoff.  The one")
print("  place a truncation could actually bite is t=1/2, and it was computed")
print("  only at 2j<=8.  Re-run here.  Note the concern is not idle: at a")
print("  critical point the gauge directions are EXACT zero modes, and on them")
print("  D^dag D is O(1) rather than growing with j, so 'large j is safe' does")
print("  not follow from the naive j^2 argument.")
nneg_high, negvals_high, per_block = 0, [], []
for two_j in range(TWO_J_HIGH + 1):
    ev = np.linalg.eigvalsh(hessian_block(0.5, two_j))
    k = int(np.sum(ev < -1e-9))
    nneg_high += k * (two_j + 1)
    negvals_high.extend([float(x) for x in ev if x < -1e-9])
    per_block.append({"two_j": two_j, "n_negative_in_block": k, "min_eig": float(ev[0])})
    print(
        f"    2j={two_j:>2}  dim={9 * (two_j + 1):>4}  min eig = {float(ev[0]):>12.9f}"
        f"   negative modes in block = {k}"
    )
index_stable = (
    nneg_high
    == RESULTS["part5_critical_point_morse_indices"]["t=1/2"]["morse_index_with_multiplicity"]
)
print()
print(
    f"  Morse index at t=1/2, 2j<=8  : "
    f"{RESULTS['part5_critical_point_morse_indices']['t=1/2']['morse_index_with_multiplicity']}"
)
print(f"  Morse index at t=1/2, 2j<=14 : {nneg_high}     unchanged? {index_stable}")
print(f"  negative eigenvalues found: {[round(v, 9) for v in negvals_high]}")
print("  Analytic backstop, independent of ANY cutoff [own derivation, prompted")
print("  by the skeptic's own T9 observation]: the quadratic form")
print("  (tr a)^2 - tr(a a) on 3x3 real matrices has eigenvalues +2 (trace, x1),")
print("  +1 (antisymmetric, x3), -1 (symmetric-traceless, x5).  The F-term is")
print("  (t^2-t) times that form tensored with the identity on the mode index,")
print("  so its spectrum is the SAME in every Peter-Weyl block.  Since")
print("  H = D^dag D + F-term and D^dag D >= 0, we get H >= min(F-term) for")
print("  EVERY j at once.  Computed exactly rather than argued:")
Mform = build_F_term(0.5, 0)
fev = np.linalg.eigvalsh(Mform)
print(
    f"    spectrum of the F-term at t=1/2 (2j=0 block): {sorted(round(float(x), 6) for x in set(np.round(fev, 9)))}"
)
print(f"    => H = D^dag D + F-term >= 0 + min(F-term) = {float(fev[0]):.6f} for EVERY j,")
print("       so no eigenvalue below that bound can exist at any cutoff.  The")
print("       observed minimum saturates it, which is why raising the cutoff")
print("       cannot produce a deeper mode -- though it could in principle have")
print("       produced MORE modes at the same depth, which is what was checked.")
RESULTS["part5b_high_cutoff_morse_index"] = nneg_high
RESULTS["part5b_index_stable_under_cutoff"] = bool(index_stable)
RESULTS["part5b_per_block"] = per_block
RESULTS["part5b_F_term_lower_bound_at_t_half"] = float(fev[0])
print()


# ---------------------------------------------------------------------------
# PART 8 -- NON-METRIC (gl(3)-valued) perturbations  (skeptic finding E2)
# ---------------------------------------------------------------------------
hr("PART 8 -- non-metric gl(3)-valued perturbations: what survives, what does not")
print("  The whole analysis above lives in Omega^1(S^3, so(3)) -- METRIC")
print("  connections at fixed metric, which is what claim.md asks for and where")
print("  the Cartan-Schouten family lives.  A general AFFINE connection on TS^3")
print("  has 27 frame components, not 9.  Tested here rather than argued:")
print("  does the conclusion survive on Omega^1(S^3, gl(3))?")

L = [np.array([[-EPS[i, a, b] for b in range(3)] for a in range(3)], dtype=float) for i in range(3)]


def _gl_idx1(i: int, r: int, c: int, n: int, d: int) -> int:
    return ((i * 3 + r) * 3 + c) * d + n


def _gl_idx2(p: int, r: int, c: int, n: int, d: int) -> int:
    return ((p * 3 + r) * 3 + c) * d + n


def build_dA_1form_gl(tval: float, two_j: int) -> np.ndarray:
    """d_A on gl(3)-valued 1-forms; A_i = t*L_i acts by matrix commutator."""
    d = two_j + 1
    rho = spin_matrices(two_j)
    D = np.zeros((3 * 9 * d, 3 * 9 * d), dtype=complex)
    for p, (i, j_) in enumerate(PAIRS):
        for r in range(3):
            for c in range(3):
                for n in range(d):
                    row = _gl_idx2(p, r, c, n, d)
                    for m in range(d):
                        D[row, _gl_idx1(j_, r, c, m, d)] += rho[i][n, m]
                        D[row, _gl_idx1(i, r, c, m, d)] -= rho[j_][n, m]
                    for k in range(3):
                        if EPS[i, j_, k]:
                            D[row, _gl_idx1(k, r, c, n, d)] -= EPS[i, j_, k]
                    # [A_i, a_j] - [A_j, a_i], A_i = t L_i, matrix commutator
                    for s in range(3):
                        D[row, _gl_idx1(j_, s, c, n, d)] += tval * L[i][r, s]
                        D[row, _gl_idx1(j_, r, s, n, d)] -= tval * L[i][s, c]
                        D[row, _gl_idx1(i, s, c, n, d)] -= tval * L[j_][r, s]
                        D[row, _gl_idx1(i, r, s, n, d)] += tval * L[j_][s, c]
    return D


def build_dA_0form_gl(tval: float, two_j: int) -> np.ndarray:
    d = two_j + 1
    rho = spin_matrices(two_j)
    G = np.zeros((3 * 9 * d, 9 * d), dtype=complex)
    for i in range(3):
        for r in range(3):
            for c in range(3):
                for n in range(d):
                    row = _gl_idx1(i, r, c, n, d)
                    for m in range(d):
                        G[row, (r * 3 + c) * d + m] += rho[i][n, m]
                    for s in range(3):
                        G[row, (s * 3 + c) * d + n] += tval * L[i][r, s]
                        G[row, (r * 3 + s) * d + n] -= tval * L[i][s, c]
    return G


print()
print(
    f"  {'2j':>3} {'so(3) dim':>10} {'gl(3) dim':>10} | {'t':>4} "
    f"{'min eig (gl3)':>14} {'ker (gl3)':>10} {'rk d_A (gl3)':>13} {'ker (so3)':>10}"
)
gl_rows, gl_psd, gl_kernel_ok, gl_bigger = [], True, True, True
for two_j in range(5):
    d = two_j + 1
    for tv in (0.0, 1.0):
        Dg = build_dA_1form_gl(tv, two_j)
        Hg = Dg.conj().T @ Dg
        Hg = 0.5 * (Hg + Hg.conj().T)
        evg = np.linalg.eigvalsh(Hg)
        kg = int(np.sum(np.abs(evg) < 1e-9))
        rg = int(np.linalg.matrix_rank(build_dA_0form_gl(tv, two_j), tol=1e-9))
        ks = int(np.sum(np.abs(np.linalg.eigvalsh(hessian_block(tv, two_j))) < 1e-9))
        if evg[0] < -1e-9:
            gl_psd = False
        if kg != rg:
            gl_kernel_ok = False
        if not (kg >= ks):
            gl_bigger = False
        gl_rows.append(
            {
                "two_j": two_j,
                "t": tv,
                "min_eig": float(evg[0]),
                "kernel_gl3": kg,
                "rank_dA_gl3": rg,
                "kernel_so3": ks,
            }
        )
        print(
            f"  {two_j:>3} {9 * d:>10} {27 * d:>10} | {tv:>4} {float(evg[0]):>14.9f}"
            f" {kg:>10} {rg:>13} {ks:>10}"
        )
print()
print(f"  (i)  PSD survives on gl(3) at t=0 and t=1?                      {gl_psd}")
print(f"  (ii) kernel(Q_gl3) == rank(d_A on Omega^0(gl3))  (H^1 = 0 too)? {gl_kernel_ok}")
print(f"  (iii) kernel is LARGER than the so(3) one?                      {gl_bigger}")
print("  -> POSITIVITY survives -- it only ever used 'sum of squares, zero at a")
print("     flat connection', which is signature- and structure-group-blind.")
print("  -> 'NO extra zero modes' does NOT survive verbatim: the extra null")
print("     directions are gauge directions of the LARGER GL(3) group, which is")
print("     not a symmetry of a theory that has a metric.  So the correct scope")
print("     of the kernel statement is: kernel = the METRIC (so(3)) gauge orbit,")
print("     within metric connections.  Stated, not smoothed over.")
print("  -> Also NOT varied anywhere in this round: the metric g itself.  A full")
print("     stability statement about the GEOMETRY would need delta-g, and the")
print("     connection/metric split is exactly what S_YM cannot see.")
RESULTS["part8_gl3_rows"] = gl_rows
RESULTS["part8_gl3_psd_survives"] = bool(gl_psd)
RESULTS["part8_gl3_kernel_equals_gauge"] = bool(gl_kernel_ok)
RESULTS["part8_gl3_kernel_larger_than_so3"] = bool(gl_bigger)
print()


# ---------------------------------------------------------------------------
# PART 9 -- the barrier is TOPOLOGICALLY FORCED  (skeptic finding E1, adopted)
# ---------------------------------------------------------------------------
hr("PART 9 -- why the t=1/2 barrier EXISTS at all: it is topologically forced")
print("  PART 6b established winding(A^1 rel A^0) = -1.  Consequence, adopted")
print("  from the FL Step 8a skeptic pass and re-derived here:")
print("    * on S^3 (simply connected) EVERY flat connection is pure gauge, so")
print("      the flat set is the gauge orbit of 0, i.e. {G^-1 dG : G in Gauge};")
print("    * the Chern-Simons functional restricted to that set equals the")
print("      winding number (up to a fixed positive constant) -- an INTEGER-")
print("      valued continuous function, hence locally constant;")
print("    * CS(A^0) = 0 and CS(A^1) = -1, so A^0 and A^1 lie in DIFFERENT")
print("      connected components of the flat set;")
print("    * therefore ANY continuous path from A^0 to A^1 must leave the flat")
print("      set, i.e. S_YM > 0 somewhere along it.  THE BARRIER IS FORCED.")
print()
print("  Checked, not just asserted -- the family path is one such path and its")
print("  barrier is strictly positive on the open interval:")
tt = sp.symbols("tt", real=True)
Sfam = 3 * tt**2 * (tt - 1) ** 2
_zeros = sorted(sp.solve(sp.Eq(Sfam, 0), tt), key=lambda z: float(z))
pos_on_open = [sp.nsimplify(z) for z in _zeros] == [
    sp.Integer(0),
    sp.Integer(1),
] and all(float(Sfam.subs(tt, v)) > 0 for v in (0.05, 0.25, 0.5, 0.75, 0.95))
peak = sp.maximum(Sfam, tt, sp.Interval(0, 1))
print(
    f"    S_YM(t)/Vol = {sp.factor(Sfam)};  zeros exactly at t in {sorted(sp.solve(sp.Eq(Sfam, 0), tt), key=str)}"
)
print(f"    max on [0,1] = {peak} = 3/16 at t=1/2 (the family path's barrier height)")
print(f"    strictly positive on the OPEN interval (0,1)?                {pos_on_open}")
print()
print("  SCOPE, stated rather than glossed: this shows the family path's barrier")
print("  is 3/16 and that SOME barrier is unavoidable.  It does NOT show 3/16 is")
print("  the LEAST barrier over all paths (the true sphaleron energy) -- that is")
print("  a variational problem not attempted here.  PART 7b's index-1 saddle at")
print("  (1/2)SO(3) is CONSISTENT with it being the sphaleron; consistency is")
print("  not proof.  [UNKNOWN], named.")
RESULTS["part9_family_barrier_height"] = str(peak)
RESULTS["part9_barrier_strictly_positive_on_open_interval"] = bool(pos_on_open)
RESULTS["part9_least_barrier_is_unknown"] = True
print()
# ---------------------------------------------------------------------------
# VERDICT
# ---------------------------------------------------------------------------
hr("VERDICT INPUTS")
verdict_inputs = {
    "exact_expansion_verified": RESULTS["part1_exact_expansion_verified"],
    "assembled_matrices_match_component_formula": (
        RESULTS["part4d_F_term_closed_form_ok"] and RESULTS["part4d_full_quadratic_form_ok"]
    ),
    "t0_t1_are_full_critical_points": (
        "0" in RESULTS["part2_critical_t_values"] and "1" in RESULTS["part2_critical_t_values"]
    ),
    "hessian_PSD_at_t0_and_t1_all_blocks_2jmax8": RESULTS["part4_psd_at_t0_and_t1"],
    "hessian_PSD_still_holds_at_2jmax14": (
        RESULTS["part4b_robustness"]["t0"]["global_min_eig"] > -1e-9
        and RESULTS["part4b_robustness"]["t1"]["global_min_eig"] > -1e-9
    ),
    "kernel_is_exactly_gauge_orbit": RESULTS["part4_kernel_equals_gauge_orbit"],
    "positive_control_reproduces_C123_Epp": RESULTS["part4_positive_control_passed"],
    "external_control_matches_S3_Hodge_spectrum": RESULTS["part4c_hodge_cross_check_passed"],
    "rep_matrices_agree_with_certified_C85_module": RESULTS["part4e_c85_cross_check_passed"],
    "negative_control_finds_instability_at_t_half": RESULTS["part5_negative_control_passed"],
    "t_half_morse_index": RESULTS["part5_critical_point_morse_indices"]["t=1/2"][
        "morse_index_with_multiplicity"
    ],
    "t_half_unstable_direction_is_family_direction": (
        RESULTS["part5_t_half_unstable_direction_overlap_with_family"] > 1 - 1e-9
    ),
    "A0_A1_pure_gauge_verified": RESULTS["part6_pure_gauge_verified"],
    "A0_A1_isospectral": RESULTS["part6_isospectral_below_cut"],
    "A0_A1_related_by_LARGE_gauge_winding_1": RESULTS["part6b_gauge_transformation_is_large"],
    "winding_number": RESULTS["part6b_winding_number"],
    "torsion_still_distinguishes_them": RESULTS["part6_torsion_opposite_sign"],
    "homogeneous_flat_set_is_0_union_SO3": (
        RESULTS["part7_every_SO3_is_flat"]
        and not RESULTS["part7_non_orthogonal_flat_found"]
        and not RESULTS["part7_det_minus_one_orthogonal_flat"]
    ),
    "dA_squared_zero_at_flat_points_nonzero_at_t_half": RESULTS["part4f_dA_squared_ok"],
    "t_half_morse_index_stable_at_2jmax14": RESULTS["part5b_index_stable_under_cutoff"],
    "gl3_positivity_survives": RESULTS["part8_gl3_psd_survives"],
    "gl3_kernel_equals_larger_gauge_orbit": (
        RESULTS["part8_gl3_kernel_equals_gauge"] and RESULTS["part8_gl3_kernel_larger_than_so3"]
    ),
    "barrier_topologically_forced": RESULTS["part9_barrier_strictly_positive_on_open_interval"],
    "truncation_two_j_max_main": TWO_J_MAX,
    "truncation_two_j_max_robustness": TWO_J_HIGH,
}
for k, v in verdict_inputs.items():
    print(f"  {k}: {v}")
RESULTS["verdict_inputs"] = verdict_inputs

# Label REVISED after the FL Step 8a skeptic pass (finding E3): the previous
# label headlined GLOBAL_MINIMA and H1_ZERO, both of which are THEOREMS
# available before any code ran, not findings.  The genuinely new content is
# promoted instead, and the pre-registration defect is stated in the label.
label = (
    "WEAKENED_BY_FL_STEP_8A__MATH_CONFIRMED_FRAMING_CORRECTED__"
    "PSD_AND_H1_ZERO_AT_T0_T1_ARE_FORCED_THEOREMS_NOT_FINDINGS_AND_THE_"
    "PRE_REGISTERED_KILL_CRITERION_WAS_UNFALSIFIABLE_BY_CONSTRUCTION__"
    "SCOPE_IS_METRIC_SO3_PERTURBATIONS_AT_FIXED_METRIC_GL3_ADDS_NULL_"
    "DIRECTIONS_AND_THE_METRIC_ITSELF_WAS_NEVER_VARIED__"
    "NEW_CONTENT_IS_EXHAUSTIVE_HOMOGENEOUS_CRITICAL_SET_9_POINTS_PLUS_"
    "MORSE_INDEX_EXACTLY_1_AT_T_HALF_STABLE_TO_2J14_PLUS_WINDING_MINUS_1__"
    "T0_T1_ARE_ONE_POINT_OF_A_MOD_G_BUT_DISTINCT_IN_A_MOD_G0_SO_THE_BARRIER_"
    "IS_TOPOLOGICALLY_FORCED_AND_CHERN_SIMONS_DOES_DISTINGUISH_THEM__"
    "YANG_MILLS_WEAKENED_NOT_PROMOTED_AT_F4_AND_F6"
    if (
        verdict_inputs["hessian_PSD_at_t0_and_t1_all_blocks_2jmax8"]
        and verdict_inputs["hessian_PSD_still_holds_at_2jmax14"]
        and verdict_inputs["kernel_is_exactly_gauge_orbit"]
        and verdict_inputs["positive_control_reproduces_C123_Epp"]
        and verdict_inputs["negative_control_finds_instability_at_t_half"]
    )
    else "REFUTED_OR_INCONCLUSIVE"
)
print()
print(f"label = '{label}'")
RESULTS["label"] = label

with open("results_c126.json", "w", encoding="utf-8") as fh:
    json.dump(RESULTS, fh, indent=2)
print("\nwrote results_c126.json")
