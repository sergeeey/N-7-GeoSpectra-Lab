"""C193 -- is round59's `spin_lift` a genuine Lie-algebra homomorphism
so(6) -> spin(6)?  Closes OB11(ii)'s flagged "J remains unchecked"
prerequisite (C149) WITHOUT constructing J explicitly.

Reuses round59_route_a_independent.py's E (Clifford generators), spin_lift,
NOMIZU, ADNU directly (import, not retyped) -- same loading pattern as
C149's own script.

Run:  python c193_spin_lift_homomorphism.py
"""

from __future__ import annotations

import importlib.util
import random
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
R59_PATH = (
    HERE.parent
    / "20260714-round59-trivial-rank-certification"
    / "round59_route_a_independent.py"
)

PASS, FAIL = [], []


def check(label, condition, detail=""):
    (PASS if condition else FAIL).append(label)
    print(f"  [{'PASS' if condition else 'FAIL'}] {label}")
    if detail:
        print(f"         {detail}")


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


print("=" * 78)
print("0  load round59's own machinery (E, spin_lift, NOMIZU, ADNU) -- reused,")
print("   not retyped")
print("=" * 78)

R59 = load_module("round59_route_a_independent", R59_PATH)
E = R59.build_clifford(conj=False)

calib_ok, _ = R59.run_calibration(E, R59.NOMIZU)
check("Q0 round59 calibration re-verified on import", calib_ok)

RHO = {a: R59.spin_lift(R59.ADNU[a], E) for a in range(1, 9)}
NAB = {i: R59.spin_lift(R59.NOMIZU[i], E) for i in range(1, 7)}

# ---------------------------------------------------------------------------
# so(6) <-> term-list conversion, matching spin_lift's OWN convention exactly
# (verified by derivation in claim.md: (1/4) sum_{all c,d} X_cd E_c E_d
#  = (1/2) sum_{c<d} X_cd E_c E_d, i.e. one term per (a,b), a<b, coeff=X_ab)
# ---------------------------------------------------------------------------


def matrix_to_terms(X: sp.Matrix) -> list[tuple]:
    """6x6 antisymmetric sympy Matrix (1-indexed convention: entry X[a-1,b-1])
    -> spin_lift-compatible term list [(coeff, a, b), ...], a<b, a,b in 1..6."""
    terms = []
    for a in range(1, 7):
        for b in range(a + 1, 7):
            coeff = X[a - 1, b - 1]
            if sp.simplify(coeff) != 0:
                terms.append((coeff, a, b))
    return terms


def terms_to_matrix(terms) -> sp.Matrix:
    """Inverse of matrix_to_terms: term list -> antisymmetric 6x6 Matrix."""
    M = sp.zeros(6, 6)
    for coeff, a, b in terms:
        M[a - 1, b - 1] += coeff
        M[b - 1, a - 1] -= coeff
    return M


print()
print("=" * 78)
print("1  sanity: matrix_to_terms / terms_to_matrix round-trip on NOMIZU/ADNU")
print("=" * 78)

for i in range(1, 7):
    M = terms_to_matrix(R59.NOMIZU[i])
    back = matrix_to_terms(M)
    check(
        f"Q1.{i} NOMIZU[{i}] round-trips through matrix<->terms",
        sorted(back, key=lambda t: (t[1], t[2]))
        == sorted(R59.NOMIZU[i], key=lambda t: (t[1], t[2])),
    )

print()
print("=" * 78)
print("2  THE MAIN TEST: [spin_lift(X),spin_lift(Y)] == -spin_lift([X,Y]_so6)")
print("   (the '-1' was found empirically, not assumed -- see diag_scale.py and")
print("   claim.md's Correction section; the pre-registered claim used +1 and")
print("   failed on every generic pair before this correction)")
print("   for GENERIC random antisymmetric X, Y (not NOMIZU/ADNU -- those come")
print("   after, as a positive control, not the substantive test)")
print("=" * 78)

random.seed(20260909)


def random_antisym_6x6(scale=3) -> sp.Matrix:
    M = sp.zeros(6, 6)
    for a in range(6):
        for b in range(a + 1, 6):
            v = sp.Rational(random.randint(-scale, scale), 1)
            M[a, b] = v
            M[b, a] = -v
    return M


def homomorphism_holds(X_terms, Y_terms) -> tuple[bool, sp.Matrix]:
    """Check [spin_lift(X),spin_lift(Y)] == -spin_lift([X,Y]_so6). Returns
    (holds, residual_matrix).

    The '-1' here is not assumed -- it was FOUND (diag_scale.py) after the
    first version of this check (testing a +1 coefficient) failed on every
    generic pair (Q2) and 34/48 NOMIZU/ADNU pairs (Q3), exactly the shape of
    C192's k=-2 finding earlier this session: a clean, single, consistent
    sign/scale constant, not a structural break. Diagnosed by sampling the
    entrywise ratio lhs/rhs on nonzero entries -- exactly -1 across all
    sampled entries, sympy-exact, not a floating-point coincidence."""
    liftX = R59.spin_lift(X_terms, E)
    liftY = R59.spin_lift(Y_terms, E)
    lhs = liftX * liftY - liftY * liftX
    X_mat = terms_to_matrix(X_terms)
    Y_mat = terms_to_matrix(Y_terms)
    comm_mat = X_mat * Y_mat - Y_mat * X_mat
    comm_terms = matrix_to_terms(comm_mat)
    rhs = -R59.spin_lift(comm_terms, E)
    residual = sp.simplify(lhs - rhs)
    holds = all(sp.simplify(x) == 0 for x in residual)
    return holds, residual


N_GENERIC_PAIRS = 5
generic_results = []
for trial in range(N_GENERIC_PAIRS):
    X = random_antisym_6x6()
    Y = random_antisym_6x6()
    X_terms = matrix_to_terms(X)
    Y_terms = matrix_to_terms(Y)
    comm_nonzero = any(
        sp.simplify(c) != 0
        for c in terms_to_matrix(X_terms) * terms_to_matrix(Y_terms)
        - terms_to_matrix(Y_terms) * terms_to_matrix(X_terms)
    )
    holds, _residual = homomorphism_holds(X_terms, Y_terms)
    generic_results.append((trial, comm_nonzero, holds))
    check(
        f"Q2.{trial} generic random pair #{trial}: [X,Y]!=0={comm_nonzero}, homomorphism holds={holds}",
        holds,
    )

check(
    "Q2.all all 5 generic random (non-commuting) pairs satisfy the"
    " homomorphism identity EXACTLY -- the substantive test",
    all(r[2] for r in generic_results) and all(r[1] for r in generic_results),
    f"{generic_results}",
)

print()
print("=" * 78)
print("3  positive control: X=NOMIZU[i], Y=ADNU[a] (specific, geometrically")
print("   meaningful pairs -- should ALSO satisfy the identity, as a special case)")
print("=" * 78)

nomizu_adnu_results = []
for i in range(1, 7):
    for a in range(1, 9):
        holds, _ = homomorphism_holds(R59.NOMIZU[i], R59.ADNU[a])
        nomizu_adnu_results.append((i, a, holds))

n_pass = sum(1 for _, _, h in nomizu_adnu_results if h)
check(
    f"Q3 all {len(nomizu_adnu_results)} (NOMIZU[i], ADNU[a]) pairs satisfy the"
    " homomorphism identity",
    n_pass == len(nomizu_adnu_results),
    f"{n_pass}/{len(nomizu_adnu_results)} passed",
)

print()
print("=" * 78)
print("4  negative-control-style check: does [NAB[i], RHO[a]] actually relate")
print("   to how NOMIZU transforms as a vector under ad(nu_a) -- an")
print("   independent geometric cross-check, not just algebraic tautology")
print("=" * 78)

# ADNU[a] acting on NOMIZU[i] as a vector: NOMIZU transforms in the m-rep,
# so ad(nu_a) . NOMIZU_i = sum_j (ADNU_a)_{ij} NOMIZU_j  (standard adjoint
# action of an isotropy generator on a vector-valued object indexed by i).
ADNU_mat = {a: terms_to_matrix(R59.ADNU[a]) for a in range(1, 9)}


def adnu_action_on_nomizu(a: int) -> dict[int, sp.Matrix]:
    """Returns { i : sum_j ADNU_mat[a][i-1,j-1] * NOMIZU_matrix[j] } as a
    dict of 6x6 antisymmetric matrices -- ad(nu_a) acting on the vector
    index i of NOMIZU."""
    Mj = {j: terms_to_matrix(R59.NOMIZU[j]) for j in range(1, 7)}
    out = {}
    for i in range(1, 7):
        acc = sp.zeros(6, 6)
        for j in range(1, 7):
            acc += ADNU_mat[a][i - 1, j - 1] * Mj[j]
        out[i] = acc
    return out


cross_check_results = []
for a in range(1, 9):
    predicted = adnu_action_on_nomizu(a)
    for i in range(1, 7):
        # [ADNU[a], NOMIZU[i]]_so6 should equal -predicted[i] (or +, sign
        # convention checked directly, not assumed)
        lhs = (
            ADNU_mat[a] * terms_to_matrix(R59.NOMIZU[i])
            - terms_to_matrix(R59.NOMIZU[i]) * ADNU_mat[a]
        )
        match_plus = sp.simplify(lhs - predicted[i]) == sp.zeros(6, 6)
        match_minus = sp.simplify(lhs + predicted[i]) == sp.zeros(6, 6)
        cross_check_results.append((a, i, match_plus, match_minus))

n_plus = sum(1 for _, _, mp, _ in cross_check_results if mp)
n_minus = sum(1 for _, _, _, mm in cross_check_results if mm)
check(
    "Q4 [ADNU[a],NOMIZU[i]]_so6 matches ADNU's OWN adjoint action on"
    " NOMIZU's vector index, with a SINGLE consistent sign across all 48"
    " (a,i) pairs. [Corrected per skeptic Concern 5: this sign match is"
    " NOT fully independent of Q2's -1 -- both plausibly trace to the same"
    " underlying convention in round59's ADNU/NOMIZU indexing, not two"
    " separate confirmations.]",
    n_plus == 48 or n_minus == 48,
    f"plus_matches={n_plus}/48, minus_matches={n_minus}/48",
)

print()
print("=" * 78)
print("4b  [added after skeptic pass, Concern 2] does RHO=spin_lift(ADNU) itself")
print("    satisfy su(3)'s OWN structure constants, or the FLIPPED ones? Concrete,")
print("    not abstract -- 'spin_lift is a homomorphism up to sign' is imprecise:")
print("    the correct statement is spin_lift is an ANTI-homomorphism, and RHO")
print("    is therefore a rep of su(3) with FLIPPED structure constants, not the")
print("    standard ones. Checked directly here, not left as an inference.")
print("=" * 78)


def so6_bracket_terms(X_terms, Y_terms):
    X_mat = terms_to_matrix(X_terms)
    Y_mat = terms_to_matrix(Y_terms)
    return matrix_to_terms(X_mat * Y_mat - Y_mat * X_mat)


anti_hom_on_adnu = []
for a in range(1, 9):
    for b in range(a + 1, 9):
        lhs_spinor = RHO[a] * RHO[b] - RHO[b] * RHO[a]
        so6_comm_terms = so6_bracket_terms(R59.ADNU[a], R59.ADNU[b])
        standard_pred = R59.spin_lift(
            so6_comm_terms, E
        )  # what a TRUE homomorphism predicts
        anti_pred = -standard_pred  # what the verified ANTI-homomorphism predicts
        matches_standard = sp.simplify(lhs_spinor - standard_pred) == sp.zeros(8, 8)
        matches_anti = sp.simplify(lhs_spinor - anti_pred) == sp.zeros(8, 8)
        anti_hom_on_adnu.append((a, b, matches_standard, matches_anti))

n_std = sum(1 for _, _, ms, _ in anti_hom_on_adnu if ms)
n_anti = sum(1 for _, _, _, ma in anti_hom_on_adnu if ma)
# A pair also matching "standard" is only informative if the two predictions
# actually differ (standard_pred != anti_pred, i.e. so6_comm != 0) --
# checked directly, not assumed, so a degenerate [ADNU[a],ADNU[b]]=0 case
# satisfying BOTH trivially does not get miscounted as a genuine conflict.
degenerate_pairs = [
    (a, b)
    for a in range(1, 9)
    for b in range(a + 1, 9)
    if terms_to_matrix(so6_bracket_terms(R59.ADNU[a], R59.ADNU[b])) == sp.zeros(6, 6)
]
n_genuinely_conflicting = sum(
    1 for a, b, ms, _ in anti_hom_on_adnu if ms and (a, b) not in degenerate_pairs
)
check(
    "Q4b RHO satisfies the FLIPPED su(3) structure constants"
    " ([RHO[a],RHO[b]] = -spin_lift([ADNU[a],ADNU[b]])), NOT the standard ones"
    " -- concrete confirmation of Concern 2, not left abstract. The 3 pairs"
    " also matching 'standard' are exactly the degenerate [ADNU[a],ADNU[b]]=0"
    " cases (both predictions trivially agree at 0), verified below, not"
    " a genuine standard-vs-anti conflict.",
    n_anti == 28 and n_genuinely_conflicting == 0,
    f"matches_standard={n_std}/28 (all {len(degenerate_pairs)} are degenerate"
    f" zero-commutator pairs: {degenerate_pairs}),"
    f" matches_anti-homomorphism={n_anti}/28,"
    f" genuinely_conflicting={n_genuinely_conflicting}",
)

print()
print("=" * 78)
print("5  THE COROLLARY, CORRECTED after skeptic pass (Concerns 1 and 4 --")
print("   verdict WEAKENED, both accepted, NOT presented as closing anything)")
print("=" * 78)

print("  Cited [DOCS]: SU(3) is defined as the isotropy subgroup stabilizing")
print("  the near-Kahler almost-complex structure J on S^6=G2/SU(3) -- i.e.")
print("  [J, ad(nu_a)|_m] = 0 for all a=1..8, at the so(6) (vector) level,")
print("  a standard structural fact, not new geometric content computed here.")
print("  NOTE: this is a coordinate-free statement about SOME J; it does not")
print("  identify which antisymmetric 6x6 matrix, in round59's OWN ADNU/NOMIZU")
print("  basis, represents J -- that identification is NOT made by this round.")
print()
homomorphism_confirmed = all(r[2] for r in generic_results) and n_pass == len(
    nomizu_adnu_results
)
if homomorphism_confirmed:
    print("  Given Q2/Q3 (spin_lift is a genuine ANTI-homomorphism so(6)->spin(6),")
    print("  verified computationally, not merely cited):")
    print("  [J,ad(nu_a)]_so6 = 0  ==>  [spin_lift(J), RHO[a]] = -spin_lift(0) = 0,")
    print("  for ALL a=1..8 -- the sign is irrelevant once the bracket itself is zero.")
    print()
    print("  CONCLUSION, CORRECTED after skeptic pass (WEAKENED, Concerns 1/4")
    print("  accepted): this is an EXISTENCE argument only. It shows SOME J-in-")
    print("  round59's-basis would have spin_lift(J) automatically commuting with")
    print("  RHO -- it does NOT construct that J explicitly, does NOT produce")
    print("  spin_lift(J) as a matrix, and does NOT verify a transport step could")
    print("  actually use it. C149's 'J remains unchecked' gap is NARROWED to")
    print("  'J's abstract equivariance is guaranteed once J is built' -- it is")
    print("  NOT closed operationally. Same non-substantive character as gamma's")
    print("  own 'forced by parity' finding in C149, and this round's own claim.md")
    print("  said so before the skeptic pass confirmed it, not after.")
else:
    print("  Homomorphism property NOT confirmed (see Q2/Q3 failures above) --")
    print("  the corollary about J does NOT follow. J's equivariance genuinely")
    print("  remains unchecked; this round would need to fall back to explicit")
    print("  octonion-based construction after all.")

print()
print("=" * 78)
print(f"C193: {len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    for f in FAIL:
        print(f"  FAILED: {f}")
print("=" * 78)
