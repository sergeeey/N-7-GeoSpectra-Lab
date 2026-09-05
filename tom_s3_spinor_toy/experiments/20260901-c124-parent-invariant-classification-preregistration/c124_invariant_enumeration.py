"""C124 -- bottom-up enumeration of admissible 13D-covariant local invariants.

Executes claim.md's MANDATORY search order, steps (a)-(c):
  (a) enumerate all admissible 13D Lorentz-invariant local monomials in (e, T, R)
  (b) restrict to top-degree (13-form)
  (c) reduce on the frozen product background M13 = M4 x S3 x S6

Deliberately does NOT start from the target CS3(omega)^ch3(E)^vol4 expression.
Step (d) -- inspecting the reduced output for a CS3-shaped term -- is done in
decision.md AFTER this script's output is fixed.

Field content used (PARENT_ACTION_GATE.md F1/F2/F3/F5, frozen):
  e^A  : vielbein 1-form,  1 Lorentz index, form-degree 1
  T^A  : torsion 2-form,   1 Lorentz index, form-degree 2   (T = De)
  R^AB : curvature 2-form, 2 Lorentz indices, form-degree 2
  invariant tensors: eta_AB (symmetric), eps_{A1..A13}
  NO independent 13D gauge field is in the frozen content (verified separately).

Run:  python c124_invariant_enumeration.py
"""

from __future__ import annotations

import json
from itertools import combinations_with_replacement

import sympy as sp

D = 13
RESULTS: dict[str, object] = {}


# ---------------------------------------------------------------------------
# PART 1 -- epsilon sector (one eps_{A1..A13}, all 13 indices carried by fields)
# ---------------------------------------------------------------------------
# A monomial is  eps_{A1..A13} * (fields carrying those 13 indices)
#                             * (optional extra fields, eta-contracted among
#                                themselves).
# Let the eps-carried part have n_R curvatures, n_T torsions, n_e vielbeins.
#   index count : 2*n_R + 1*n_T + 1*n_e = 13
#   form degree : 2*n_R + 2*n_T + 1*n_e = 13 - deg_extra
# Subtracting:    n_T = -deg_extra  =>  n_T = 0 and deg_extra = 0
# (deg_extra >= 0 because every field has non-negative form degree).


def epsilon_sector() -> list[dict]:
    out = []
    for n_R in range(D + 1):
        for n_T in range(D + 1):
            for n_e in range(D + 1):
                idx = 2 * n_R + n_T + n_e
                deg = 2 * n_R + 2 * n_T + n_e
                if idx == D and deg == D:
                    out.append({"n_R": n_R, "n_T": n_T, "n_e": n_e})
    return out


eps_terms = epsilon_sector()
RESULTS["epsilon_sector_terms"] = eps_terms
RESULTS["epsilon_sector_count"] = len(eps_terms)
RESULTS["epsilon_sector_all_torsion_free"] = all(t["n_T"] == 0 for t in eps_terms)


# ---------------------------------------------------------------------------
# PART 2 -- non-epsilon sector (all indices eta-contracted pairwise)
# ---------------------------------------------------------------------------
# Parity lemma: index count must be EVEN (pairwise eta contractions).
#   deg - idx = n_T  =>  n_T = 13 - even = ODD.
# So every non-eps 13-form carries an odd number of torsion 2-forms.


def noneps_parity() -> dict:
    ok = True
    witnesses = []
    for n_R in range(D + 1):
        for n_T in range(D + 1):
            for n_e in range(D + 1):
                idx = 2 * n_R + n_T + n_e
                deg = 2 * n_R + 2 * n_T + n_e
                if deg == D and idx % 2 == 0:
                    witnesses.append({"n_R": n_R, "n_T": n_T, "n_e": n_e})
                    if n_T % 2 == 0:
                        ok = False
    return {"all_have_odd_torsion_count": ok, "n_solutions": len(witnesses)}


RESULTS["noneps_parity"] = noneps_parity()

# Index-contraction graph decomposition: a monomial in e (valence 1),
# T (valence 1), R (valence 2) with all indices eta-contracted decomposes into
#   - closed cycles of R's                      -> Pontryagin  P_{2n}
#   - open chains with both ends on e's         -> A_{2n}
#   - open chains with one end e, one end T     -> B_{2n+1}
#   - open chains with both ends on T's         -> C_{2n+2}
# Symmetry constraints (antisymmetry of R^{ab}; e^a 1-forms anticommute, T^a
# 2-forms commute) kill half of each family -- reproduced here independently
# and cross-checked against Zanelli hep-th/0502193 eqs. (65)-(68).


def building_blocks(max_deg: int) -> dict[str, int]:
    """name -> form degree, for every non-eps Lorentz-invariant chain block."""
    blocks: dict[str, int] = {}
    for n in range(1, max_deg + 2):
        # A_{2n}: e ... e with (n-1) R's ; nonzero only for n even, n >= 2
        if n >= 2 and n % 2 == 0 and 2 * n <= max_deg:
            blocks[f"A_{2 * n}"] = 2 * n
        # B_{2n+1}: T ... e with (n-1) R's ; any n >= 1
        if n >= 1 and 2 * n + 1 <= max_deg:
            blocks[f"B_{2 * n + 1}"] = 2 * n + 1
        # C_{2n+2}: T ... T with (n-1) R's ; nonzero only for n odd, n >= 1
        if n >= 1 and n % 2 == 1 and 2 * n + 2 <= max_deg:
            blocks[f"C_{2 * n + 2}"] = 2 * n + 2
        # P_{2n}: closed R-cycle ; tr(R^odd) = 0, so n even
        if n >= 2 and n % 2 == 0 and 2 * n <= max_deg:
            blocks[f"P_{2 * n}"] = 2 * n
    return blocks


BLOCKS = building_blocks(13)
RESULTS["noneps_building_blocks"] = BLOCKS
RESULTS["noneps_block_degrees_available"] = sorted(set(BLOCKS.values()))


def products_of_degree(target: int) -> list[tuple[str, ...]]:
    """All multisets of blocks whose degrees sum to `target`, dropping any
    multiset that repeats an ODD-degree block (alpha ^ alpha = 0 for odd alpha).
    """
    names = sorted(BLOCKS)
    found = []
    for size in range(1, 5):
        for combo in combinations_with_replacement(names, size):
            if sum(BLOCKS[c] for c in combo) != target:
                continue
            odd_repeat = any(combo.count(c) > 1 and BLOCKS[c] % 2 == 1 for c in set(combo))
            if odd_repeat:
                continue
            found.append(combo)
    return found


# Block-diagonal (product) background: eta and R are block diagonal, so every
# chain block lives entirely inside ONE factor. Hence the 13-form must split as
#   (degree 4 on M4) ^ (degree 3 on S3) ^ (degree 6 on S6).
factor_degrees = {"M4": 4, "S3": 3, "S6": 6}
RESULTS["noneps_factor_content"] = {
    f: [list(p) for p in products_of_degree(d)] for f, d in factor_degrees.items()
}
RESULTS["noneps_S6_leg_empty"] = len(products_of_degree(6)) == 0


# ---------------------------------------------------------------------------
# PART 3 -- degree-14 closed invariant (would-be parent of a 13D CS form)
# ---------------------------------------------------------------------------
# Closed Lorentz invariants in the (e, T, R) algebra are the Pontryagin forms
# P_{4k} and the Nieh-Yan form N_4 (and products thereof). All have degree = 0
# mod 4. A 13D Chern-Simons Lagrangian requires a closed invariant 14-form.
closed_generator_degrees = [4, 8, 12]  # P_4, N_4 (4), P_8, P_12, ...


def reachable_by(gens: list[int], target: int, max_factors: int = 6) -> bool:
    def rec(rem: int, k: int) -> bool:
        if rem == 0:
            return True
        if k == 0 or rem < 0:
            return False
        return any(rec(rem - g, k - 1) for g in gens)

    return rec(target, max_factors)


RESULTS["degree14_closed_invariant_exists"] = reachable_by(closed_generator_degrees, 14)
RESULTS["degree14_mod4"] = 14 % 4
# so(N) invariant polynomials: Pontryagin (deg 4k) + Euler/Pfaffian (deg N, N even)
RESULTS["so_1_12_has_euler_class"] = 13 % 2 == 0
RESULTS["so_12_2_euler_class_degree"] = 14  # rank-14 orthogonal algebra -> Pfaffian
# "exotic" (Pontryagin-based) CS gravity needs D+1 = 0 mod 4, i.e. D = 4k-1
RESULTS["exotic_CS_gravity_exists_in_D13"] = (13 + 1) % 4 == 0


# ---------------------------------------------------------------------------
# PART 4 -- S3 torsion family: symbolic curvature / torsion / scalar curvature
# ---------------------------------------------------------------------------
# su(2) basis with [X_i, X_j] = 2 eps_{ijk} X_k, bi-invariant metric <X_i,X_j>=d_ij
# (unit S3 normalisation: Scal_LC = 6). Connection nabla^t_X Y = t [X, Y].
t = sp.symbols("t", real=True)
x = sp.symbols("x", real=True)  # x = t - 1/2

eps = sp.LeviCivita


def bracket(i: int, j: int) -> list[int]:
    return [2 * eps(i, j, k) for k in range(3)]


def nabla(i: int, j: int):
    return [t * c for c in bracket(i, j)]


def torsion(i: int, j: int):
    # T(X_i,X_j) = nabla_i X_j - nabla_j X_i - [X_i,X_j] = (2t-1)[X_i,X_j]
    return [sp.expand(nabla(i, j)[k] - nabla(j, i)[k] - bracket(i, j)[k]) for k in range(3)]


def curvature(i: int, j: int, k: int):
    # R(X_i,X_j)X_k = nab_i nab_j X_k - nab_j nab_i X_k - nab_{[X_i,X_j]} X_k
    out = [sp.Integer(0)] * 3
    for m in range(3):
        out[m] += t * sum(nabla(i, m)[0] * 0 for _ in [0])  # placeholder, unused
    # term 1: nabla_i (nabla_j X_k) = t * [X_i, t [X_j, X_k]]
    inner = nabla(j, k)
    term1 = [sp.Integer(0)] * 3
    for m in range(3):
        if inner[m] != 0:
            for n in range(3):
                term1[n] += inner[m] * nabla(i, m)[n]
    inner2 = nabla(i, k)
    term2 = [sp.Integer(0)] * 3
    for m in range(3):
        if inner2[m] != 0:
            for n in range(3):
                term2[n] += inner2[m] * nabla(j, m)[n]
    br = bracket(i, j)
    term3 = [sp.Integer(0)] * 3
    for m in range(3):
        if br[m] != 0:
            for n in range(3):
                term3[n] += br[m] * nabla(m, k)[n]
    for n in range(3):
        out[n] = sp.expand(term1[n] - term2[n] - term3[n])
    return out


# Scal = sum_{i,j} < R(X_i, X_j) X_j , X_i >
scal = sp.expand(sum(curvature(i, j, j)[i] for i in range(3) for j in range(3)))
scal = sp.simplify(scal)

# torsion is linear in t
T01 = torsion(0, 1)
RESULTS["S3_torsion_components_T01"] = [str(c) for c in T01]
RESULTS["S3_torsion_is_linear_odd_in_x"] = bool(
    sp.simplify(
        sp.expand(T01[2].subs(t, x + sp.Rational(1, 2)))
        + sp.expand(T01[2].subs(t, sp.Rational(1, 2) - x))
    )
    == 0
)

# curvature is t(t-1) times a t-independent tensor -- checked on ALL 27
# components, and the check is required to be NON-VACUOUS (some components,
# e.g. R(X0,X1)X2, vanish identically and would make an `all()` trivially true)
nonzero_ratios = []
all_components = {}
for i in range(3):
    for j in range(3):
        for k in range(3):
            comp = curvature(i, j, k)
            all_components[f"R_{i}{j}{k}"] = [str(c) for c in comp]
            for c in comp:
                if c != 0:
                    nonzero_ratios.append(sp.simplify(c / (t * (t - 1))))
RESULTS["S3_curvature_R_0_1_0"] = [str(c) for c in curvature(0, 1, 0)]
RESULTS["S3_curvature_nonzero_components_checked"] = len(nonzero_ratios)
RESULTS["S3_curvature_factorises_as_t(t-1)"] = bool(
    len(nonzero_ratios) > 0 and all(sp.diff(r, t) == 0 for r in nonzero_ratios)
)

RESULTS["S3_scalar_curvature_of_nabla_t"] = str(sp.factor(scal))
RESULTS["S3_Scal_LC_at_t_half"] = str(sp.simplify(scal.subs(t, sp.Rational(1, 2))))
RESULTS["S3_Scal_at_t_0"] = str(sp.simplify(scal.subs(t, 0)))
RESULTS["S3_Scal_at_t_1"] = str(sp.simplify(scal.subs(t, 1)))
scal_x = sp.expand(scal.subs(t, x + sp.Rational(1, 2)))
RESULTS["S3_Scal_in_x"] = str(sp.expand(scal_x))
RESULTS["S3_Scal_is_even_in_x"] = bool(sp.simplify(scal_x - scal_x.subs(x, -x)) == 0)

# round111 cross-check:  Scal(t) = Scal_LC - 6*(2t-1)^2   with Scal_LC = 6
round111 = 6 - 6 * (2 * t - 1) ** 2
RESULTS["matches_round111_Scal_formula"] = bool(sp.simplify(scal - round111) == 0)


# ---------------------------------------------------------------------------
# PART 5 -- 4D effective potential from the epsilon sector on the frozen bg
# ---------------------------------------------------------------------------
# Terms contributing a bare vol_4 need all 4 M4 eps-indices carried by e's.
# S3 leg (3 eps-indices) is then either  eps_ijk R^ij e^k  or  eps_ijk e^i e^j e^k
# S6 leg (6 eps-indices) is t-independent in every case.
# Explicit enumeration rather than hand assertion: with n_T = 0 (Part 1), each
# factor F of dimension d_F carries n_R^F curvatures and n_e^F vielbeins with
# 2*n_R^F + n_e^F = d_F  (index count = form degree, because n_T = 0).
def leg_options(dim: int) -> list[dict]:
    return [{"n_R": n_R, "n_e": dim - 2 * n_R} for n_R in range(dim // 2 + 1)]


legs = {f: leg_options(d) for f, d in factor_degrees.items()}
RESULTS["epsilon_sector_leg_options"] = legs

# t enters ONLY through the S3 leg (M4 flat, S6 round Levi-Civita in the frozen
# background), and there only through R^t = t(t-1)*R_0 (Part 3, verified).
RESULTS["epsilon_sector_bare_vol4_leg"] = [o for o in legs["M4"] if o["n_R"] == 0]
RESULTS["epsilon_sector_S3_leg_t_dependence"] = [
    str(sp.expand((t * (t - 1)) ** o["n_R"])) for o in legs["S3"]
]

A, B = sp.symbols("A B", real=True)
V = A + B * t * (1 - t)  # A from the vol_3 leg, B from the eps_ijk R^ij e^k leg
RESULTS["epsilon_sector_4D_potential"] = str(V)
RESULTS["epsilon_sector_potential_stationary_points"] = [str(s) for s in sp.solve(sp.diff(V, t), t)]
V_x = sp.expand(V.subs(t, x + sp.Rational(1, 2)))
RESULTS["epsilon_sector_potential_even_in_x"] = bool(sp.simplify(V_x - V_x.subs(x, -x)) == 0)

# The target shape, for contrast (evaluated, NOT searched-for): the CS3 cubic
# recorded by C123 is odd in x with a nonzero cubic term.
RESULTS["target_shape_parity"] = "odd cubic in x (C123, cited)"


if __name__ == "__main__":
    print(json.dumps(RESULTS, indent=2, ensure_ascii=False))
    with open("results_c124.json", "w", encoding="utf-8") as fh:
        json.dump(RESULTS, fh, indent=2, ensure_ascii=False)
