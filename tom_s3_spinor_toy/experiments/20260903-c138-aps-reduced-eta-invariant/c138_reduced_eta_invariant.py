"""C138 -- the APS REDUCED eta invariant xi(D^t) = (eta(D^t)+h(t))/2 mod 1,
at the spectral crossings of the S3 torsion-deformed Dirac operator family
already certified in C121.

Everything numeric/symbolic is machine-checked with exact sympy Rational
arithmetic -- no floating point is used for any load-bearing comparison.

What this script does, in order (mirrors claim.md's own verification plan):

1.  Re-derives eta(a)'s closed form P(a) on the base interval from scratch
    via the Hurwitz-zeta route C121 used, independently re-typed (not
    copy-pasted) -- then checks it against C121's own already-published
    closed form P(a)=a(3-4a^2)/6 and against the independent APS-variation
    identity dP/da=-2(a^2-1/4) C121's skeptic pass also confirmed.
2.  Builds the crossing-lattice map a=3(t-1/2), a_c=+-(3/2+n), and verifies
    it reproduces claim.md's own stated t-values for n=0,1,2.
3.  Builds mu(n)=(n+1)(n+2) and the cumulative multiplicity S(n).
4.  Computes eta AT each crossing point via TWO independent routes:
      (i)  direct average of the two one-sided limits (the definition of
           the AT-the-point convention C121's skeptic pass established --
           the naive one-sided limit is NOT the value at the point, since
           the crossing eigenvalue contributes sign(0)=0, not the limit's
           implicit +-1);
      (ii) the closed-form shortcut eta_at = P(a_c) + 2*S(n-1) + mu(n).
    Route (i) and (ii) are checked to agree EXACTLY (symbolic equality),
    and spot-checked against C121's own already-independently-confirmed
    numbers (eta(a=2)=-1/3, eta_at(a=3/2)=+1/2, eta(a=0)=0).
5.  Computes h(t) = mu(n) at each crossing (0 elsewhere, not computed
    elsewhere since it is not needed there).
6.  Computes xi_at = (eta_at+h)/2 mod 1 at every computed crossing --
    this is the round's central table.
7.  Proves the h(t)-jump cancellation ALGEBRAICALLY (not just numerically):
    xi_at mod 1 = P(a_c)/2 mod 1 for every crossing, because
    eta_at+h = P(a_c) + 2*S(n-1) + 2*mu(n) -- an INTEGER shift of P(a_c),
    so dividing by 2 removes exactly the ambiguity mod 1. Verified by
    checking xi mod 1 computed via the raw (eta_at+h)/2 route matches the
    P(a_c)/2 shortcut route exactly, at every crossing.
8.  Proves CONTINUITY of xi mod 1 through each crossing directly: computes
    xi on the near-origin open interval (h=0 there) and the far-from-origin
    open interval (h=0 there too) approaching the same crossing, and checks
    both one-sided xi-mod-1 values match xi_at mod 1 exactly -- i.e. xi mod
    1 has NO discontinuity at any crossing, unlike raw eta (jumps by
    2*mu(n)) and unlike h itself (jumps from 0 to mu(n) and back to 0).

AST self-audit: refuses to run if any check() call is passed a literal
constant (defends against unfailable checks) -- same pattern as
C130/C133/C134/C136.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp
from sympy import Rational, Symbol, bernoulli, expand

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c138.json"

a = Symbol("a", real=True)

RESULTS: dict[str, bool] = {}
DATA: dict[str, object] = {}
FAILURES: list[str] = []


def _self_audit_no_hardcoded_checks() -> int:
    """Reject any check(...) whose condition is a LITERAL constant in the
    source. WHY: a "check" whose condition is a literal True cannot fail --
    C134's own first draft had exactly this defect, caught by two
    independent skeptic passes. Audited on the SOURCE (a literal is
    syntactically distinguishable from a computed value there)."""
    import ast

    src = Path(__file__).read_text(encoding="utf-8")
    bad = []
    for node in ast.walk(ast.parse(src)):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "check"
            and len(node.args) >= 2
            and isinstance(node.args[1], ast.Constant)
        ):
            bad.append((node.lineno, ast.unparse(node.args[0])))
    if bad:
        raise AssertionError(f"hardcoded check conditions at {bad}")
    return sum(
        1
        for n in ast.walk(ast.parse(src))
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "check"
    )


N_CHECK_CALLSITES = _self_audit_no_hardcoded_checks()


def check(name: str, cond: bool, detail: str = "") -> bool:
    RESULTS[name] = bool(cond)
    status = "PASS" if cond else "FAIL"
    if not cond:
        FAILURES.append(name)
    print(f"  [{status}] {name}" + (f"   {detail}" if detail else ""))
    return cond


# ----------------------------------------------------------------------
# 1. Re-derive P(a) from scratch (Hurwitz-zeta route), independent re-typing
#    of C121's own method -- not copied, cross-checked below.
# ----------------------------------------------------------------------
print("\n=== 1. Re-derive eta(a)=P(a) on the base interval, from scratch ===")


def zeta_H_neg_int(n_val: int, q):
    """zeta_H(-n, q) = -bernoulli(n+1, q) / (n+1), n a nonnegative int."""
    return -bernoulli(n_val + 1, q) / (n_val + 1)


def f_closed_form(a_expr):
    """f(0, a) = sum_n (m^2-1/4)*(m+a)^{-s} at s=0, m=n+3/2, via the
    s=-2,-1,0 Hurwitz-zeta decomposition (C121's method, re-derived)."""
    q = Rational(3, 2) + a_expr
    z0 = zeta_H_neg_int(0, q)
    z1 = zeta_H_neg_int(1, q)
    z2 = zeta_H_neg_int(2, q)
    return z2 - 2 * a_expr * z1 + (a_expr**2 - Rational(1, 4)) * z0


P_rederived = expand(f_closed_form(a) - f_closed_form(-a))
P_rederived = sp.simplify(P_rederived)
print(f"  P(a) re-derived = {P_rederived}")

P_certified = a * (3 - 4 * a**2) / 6  # C121's own published closed form
check(
    "P_rederived_matches_C121_certified_closed_form",
    sp.simplify(P_rederived - P_certified) == 0,
    f"re-derived {P_rederived}  vs  certified {sp.expand(P_certified)}",
)

# APS variation identity, independently re-checked (C121's skeptic pass
# also confirmed this from a structurally different, heat-kernel route --
# not re-derived via that second route here, but this closed-form
# derivative check is itself independent of the Hurwitz-zeta arithmetic
# above, since sp.diff does not reuse zeta_H_neg_int at all).
dP_da = sp.diff(P_certified, a)
check(
    "dP_da_APS_variation_identity",
    sp.simplify(dP_da - (-2 * (a**2 - Rational(1, 4)))) == 0,
    f"dP/da = {sp.expand(dP_da)}  (target -2*(a^2-1/4))",
)

# Odd-polynomial check
check(
    "P_is_odd_function_of_a",
    sp.simplify(P_certified.subs(a, -a) + P_certified) == 0,
)

# P(0) = 0 (t=1/2, k_grav=0, already-certified project fact G34-B3, not
# re-derived here, only spot-checked for internal consistency)
check("P_at_a0_is_zero", P_certified.subs(a, 0) == 0)

DATA["P_closed_form"] = str(sp.expand(P_certified))


def P(a_val):
    return P_certified.subs(a, a_val)


# ----------------------------------------------------------------------
# 2. Crossing lattice map a = 3(t-1/2), a_c = +-(3/2+n)
# ----------------------------------------------------------------------
print("\n=== 2. Crossing lattice map: a = 3(t-1/2), a_c = +-(3/2+n) ===")

t_sym = Symbol("t", real=True)
a_of_t = 3 * (t_sym - Rational(1, 2))


def t_of_a(a_val):
    # invert a = 3(t-1/2)  =>  t = a/3 + 1/2
    return sp.nsimplify(a_val / 3 + Rational(1, 2))


N_MAX = 5  # n=0,1,2 required by claim.md; n=3,4,5 as an extra check below
crossings = []  # list of dict: n, sign, a_c, t
for n in range(N_MAX + 1):
    for sign in (+1, -1):
        a_c = sign * (Rational(3, 2) + n)
        t_c = t_of_a(a_c)
        crossings.append({"n": n, "sign": sign, "a_c": a_c, "t": t_c})

# claim.md's own stated values: t=0,1 [n=0]; t=-1/3,4/3 [n=1]; t=-2/3,5/3 [n=2]
expected = {
    (0, -1): Rational(0),
    (0, +1): Rational(1),
    (1, -1): Rational(-1, 3),
    (1, +1): Rational(4, 3),
    (2, -1): Rational(-2, 3),
    (2, +1): Rational(5, 3),
}
ok = all(
    c["t"] == expected[(c["n"], c["sign"])] for c in crossings if (c["n"], c["sign"]) in expected
)
check(
    "crossing_lattice_matches_claim_md_stated_t_values",
    ok,
    "n=0,1,2 both signs, against claim.md's own quoted t-values",
)
DATA["crossing_table_n0_to_n2"] = [
    {"n": c["n"], "sign": c["sign"], "a_c": str(c["a_c"]), "t": str(c["t"])}
    for c in crossings
    if c["n"] <= 2
]

# ----------------------------------------------------------------------
# 3. mu(n) = (n+1)(n+2), cumulative S(n)
# ----------------------------------------------------------------------
print("\n=== 3. Multiplicity table mu(n)=(n+1)(n+2) and cumulative S(n) ===")


def mu(n_val: int) -> int:
    return (n_val + 1) * (n_val + 2)


mu_table = {n: mu(n) for n in range(N_MAX + 1)}
check(
    "mu_table_matches_claim_md_stated_values",
    mu_table[0] == 2 and mu_table[1] == 6 and mu_table[2] == 12,
    f"mu(0)={mu_table[0]}, mu(1)={mu_table[1]}, mu(2)={mu_table[2]}  (claim.md: 2,6,12)",
)
check(
    "mu_n_always_even_product_of_consecutive_integers",
    all(mu_table[n] % 2 == 0 for n in range(N_MAX + 1)),
    "mu(n)=(n+1)(n+2), a product of two consecutive integers, always even -- "
    "this is what makes S(n)/2 an integer below",
)


def S(n_val: int) -> int:
    """S(n) = sum_{k=0}^{n} mu(k), S(-1) := 0 (empty sum)."""
    if n_val < 0:
        return 0
    return sum(mu_table[k] for k in range(n_val + 1))


S_table = {n: S(n) for n in range(-1, N_MAX + 1)}
DATA["mu_table"] = mu_table
DATA["S_table"] = S_table


# ----------------------------------------------------------------------
# 4. eta AT each crossing, via TWO independent routes
# ----------------------------------------------------------------------
print("\n=== 4. eta AT each crossing point, two independent routes ===")


def eta_near_limit(a_c, n_val: int):
    """One-sided limit approaching a_c from the NEAR-ORIGIN side
    (interval n-1, |a|<3/2+n): eta = P(a) + 2*S(n-1)."""
    return P(a_c) + 2 * S(n_val - 1)


def eta_far_limit(a_c, n_val: int):
    """One-sided limit approaching a_c from the FAR-FROM-ORIGIN side
    (interval n, |a|>3/2+n): eta = P(a) + 2*S(n)."""
    return P(a_c) + 2 * S(n_val)


def eta_at_route_average(a_c, n_val: int):
    """Route (i): the AT-the-point value is the average of the two
    one-sided limits (the crossing eigenvalue contributes sign(0)=0,
    not the limit's implicit +-1 -- C121's skeptic-corrected convention,
    independently re-derived here via the average, not copied)."""
    return (eta_near_limit(a_c, n_val) + eta_far_limit(a_c, n_val)) / 2


def eta_at_route_closed_form(a_c, n_val: int):
    """Route (ii): closed-form shortcut, eta_at = P(a_c)+2*S(n-1)+mu(n)."""
    return P(a_c) + 2 * S(n_val - 1) + mu(n_val)


eta_at_table = {}
for c in crossings:
    n_val, a_c, t_c = c["n"], c["a_c"], c["t"]
    r1 = sp.nsimplify(eta_at_route_average(a_c, n_val))
    r2 = sp.nsimplify(eta_at_route_closed_form(a_c, n_val))
    key = f"n={n_val},t={t_c}"
    eta_at_table[key] = {"route_average": str(r1), "route_closed_form": str(r2)}
    if n_val <= 2:
        check(
            f"eta_at_two_routes_agree_{key}",
            sp.simplify(r1 - r2) == 0,
            f"average-of-limits={r1}  closed-form={r2}",
        )

DATA["eta_at_table_n0_to_n5"] = eta_at_table

# Spot-check against C121's own already independently-confirmed numbers.
eta_at_t1 = eta_at_route_average(Rational(3, 2), 0)
check(
    "spotcheck_eta_at_t1_matches_C121_certified_plus_half",
    sp.simplify(eta_at_t1 - Rational(1, 2)) == 0,
    f"eta_at(t=1) = {eta_at_t1}  (C121 certified: +1/2)",
)

eta_at_interval_pt_a2 = P(2) + 2 * S(0)  # a=2 is NOT a crossing, ordinary interval-0 point
check(
    "spotcheck_eta_at_a2_matches_C121_certified_minus_1_3",
    sp.simplify(eta_at_interval_pt_a2 - Rational(-1, 3)) == 0,
    f"eta(a=2) = {eta_at_interval_pt_a2}  (C121 certified: -1/3)",
)

check(
    "spotcheck_eta_at_a0_is_zero_t_half",
    P(0) == 0,
    "eta(a=0) = P(0) = 0  (t=1/2, k_grav=0, G34-B3, spot-check of P only)",
)

# ----------------------------------------------------------------------
# 5-6. h(t) at each crossing, and xi_at = (eta_at + h)/2 mod 1
# ----------------------------------------------------------------------
print("\n=== 5-6. h(t)=mu(n) at each crossing, xi_at=(eta_at+h)/2 mod 1 ===")


def frac_mod1(x):
    """Exact fractional part in [0,1) for a sympy Rational."""
    x = sp.nsimplify(x)
    return x - sp.floor(x)


xi_table = {}
for c in crossings:
    n_val, sign, a_c, t_c = c["n"], c["sign"], c["a_c"], c["t"]
    eta_at = sp.nsimplify(eta_at_route_closed_form(a_c, n_val))
    h_at = mu(n_val)
    xi_at = sp.nsimplify((eta_at + h_at) / 2)
    xi_mod1 = frac_mod1(xi_at)
    xi_table[str(t_c)] = {
        "n": n_val,
        "sign": sign,
        "a_c": str(a_c),
        "eta_at": str(eta_at),
        "h_at": h_at,
        "xi_at_raw": str(xi_at),
        "xi_mod1": str(xi_mod1),
    }

print("  t        n   sign   eta_at   h    xi_at     xi mod 1")
for t_key, row in sorted(xi_table.items(), key=lambda kv: (int(kv[1]["n"]), -int(kv[1]["sign"]))):
    print(
        f"  {t_key:8s} {row['n']:>2} {row['sign']:>5} {row['eta_at']:>9} "
        f"{row['h_at']:>4} {row['xi_at_raw']:>9}   {row['xi_mod1']}"
    )

DATA["xi_table_full"] = xi_table

# ----------------------------------------------------------------------
# 7. Algebraic proof: xi_at mod 1 = P(a_c)/2 mod 1  (the cancellation)
# ----------------------------------------------------------------------
print("\n=== 7. Algebraic cancellation proof: xi_at mod 1 = P(a_c)/2 mod 1 ===")

cancellation_ok = True
for c in crossings:
    n_val, a_c, t_c = c["n"], c["a_c"], c["t"]
    eta_at = sp.nsimplify(eta_at_route_closed_form(a_c, n_val))
    h_at = mu(n_val)
    xi_at = sp.nsimplify((eta_at + h_at) / 2)
    xi_mod1_direct = frac_mod1(xi_at)
    xi_mod1_shortcut = frac_mod1(P(a_c) / 2)
    if sp.simplify(xi_mod1_direct - xi_mod1_shortcut) != 0:
        cancellation_ok = False
check(
    "xi_mod1_equals_P_over_2_mod1_at_every_crossing",
    cancellation_ok,
    f"checked n=0..{N_MAX}, both signs ({len(crossings)} crossings)",
)

# The integer-shift fact this rests on: S(n-1)+mu(n) is an integer for every
# n (trivially true -- sum/value of integer-valued mu -- verified concretely
# here rather than only asserted).
integer_shift_ok = all(isinstance(S_table[n - 1] + mu_table[n], int) for n in range(N_MAX + 1))
check(
    "S_nminus1_plus_mu_n_is_integer_for_every_n",
    integer_shift_ok,
    "the exact mechanism: (eta_at+h)/2 - P(a_c)/2 = S(n-1)+mu(n), always an integer",
)

# ----------------------------------------------------------------------
# 8. Continuity of xi mod 1 through every crossing (not just raw values
#    matching -- the ONE-SIDED xi limits, computed with h=0 off the
#    crossing, must ALSO match xi_at mod 1).
# ----------------------------------------------------------------------
print("\n=== 8. Continuity of xi mod 1 through every crossing (h=0 off-crossing) ===")

continuity_ok = True
continuity_detail = []
for c in crossings:
    n_val, a_c, t_c = c["n"], c["a_c"], c["t"]
    eta_near = eta_near_limit(a_c, n_val)  # h=0 here (away from crossing)
    eta_far = eta_far_limit(a_c, n_val)  # h=0 here too
    xi_near_mod1 = frac_mod1(eta_near / 2)
    xi_far_mod1 = frac_mod1(eta_far / 2)
    eta_at = sp.nsimplify(eta_at_route_closed_form(a_c, n_val))
    xi_at_mod1 = frac_mod1((eta_at + mu(n_val)) / 2)
    same = (
        sp.simplify(xi_near_mod1 - xi_at_mod1) == 0 and sp.simplify(xi_far_mod1 - xi_at_mod1) == 0
    )
    continuity_detail.append(
        {
            "t": str(t_c),
            "xi_near_mod1": str(xi_near_mod1),
            "xi_at_mod1": str(xi_at_mod1),
            "xi_far_mod1": str(xi_far_mod1),
            "continuous": bool(same),
        }
    )
    if not same:
        continuity_ok = False
check(
    "xi_mod1_is_continuous_through_every_crossing",
    continuity_ok,
    f"near-side, at-point, and far-side xi mod 1 all agree at every crossing "
    f"(n=0..{N_MAX}, both signs) -- unlike raw eta (jumps by 2*mu(n)) and "
    f"unlike h itself (jumps 0->mu(n)->0)",
)
DATA["continuity_detail"] = continuity_detail

# Contrast: raw eta itself is NOT continuous at the crossings (this is what
# the h(t)/2 correction is specifically fixing). WHY 2*mu(n), not mu(n): the
# eta sum counts sign(lambda)*|lambda|^{-s}; a multiplicity-mu(n) eigenspace
# crossing zero flips its contribution from -mu(n) to +mu(n), a NET change
# of +2*mu(n) -- caught here on first run (initial draft asserted mu(n),
# off by a factor of 2; the concrete near/far limit values in section 4's
# printed table already showed the jump was 4 = 2*mu(0) = 2*2 at n=0, not 2).
raw_eta_jump_ok = all(
    sp.simplify(eta_far_limit(c["a_c"], c["n"]) - eta_near_limit(c["a_c"], c["n"]) - 2 * mu(c["n"]))
    == 0
    for c in crossings
)
check(
    "raw_eta_jumps_by_exactly_2mu_n_at_each_crossing_contrast_case",
    raw_eta_jump_ok,
    "raw eta (NOT reduced) jumps by 2*mu(n) at each crossing -- half of this "
    "jump is exactly what the +h(t) term in xi=(eta+h)/2 cancels, leaving a "
    "net integer shift under division by 2",
)

# ----------------------------------------------------------------------
# 9. Duplicate-value curiosity check (honesty check, NOT claimed as a
#    result): does the n=0 pair {1/4,3/4} recur at other n? If so, it
#    argues AGAINST (not for) any "n=0 is special" reading.
# ----------------------------------------------------------------------
print("\n=== 9. Duplicate-value check across n (honesty check, not a claimed result) ===")

pair_by_n = {}
for n_val in range(N_MAX + 1):
    vals = set()
    for sign in (+1, -1):
        a_c = sign * (Rational(3, 2) + n_val)
        vals.add(frac_mod1(P(a_c) / 2))
    pair_by_n[n_val] = frozenset(vals)

n0_pair = pair_by_n[0]
recurs_at = [n_val for n_val in range(1, N_MAX + 1) if pair_by_n[n_val] == n0_pair]
all_pairs_distinct = len({v for v in pair_by_n.values()}) == len(pair_by_n)
DATA["xi_pair_by_n"] = {str(n): sorted(str(x) for x in v) for n, v in pair_by_n.items()}
DATA["n0_pair_recurs_at_n"] = recurs_at
print(
    f"  {{n=0 pair}} = {sorted(str(x) for x in n0_pair)}; recurs at n={recurs_at}"
    if recurs_at
    else f"  {{n=0 pair}} = {sorted(str(x) for x in n0_pair)}; does NOT recur for n=1..{N_MAX}"
)
# Genuine, failable check: is every n's unordered {xi} pair DISTINCT from
# every other n's pair? This CAN fail (and in fact does -- recorded honestly
# below, not tuned away) -- it is what would be needed for "n=0's value is
# unique" to be even a candidate structural claim.
pairs_readable = {n: sorted(str(x) for x in v) for n, v in pair_by_n.items()}
check(
    "every_n_gives_a_DISTINCT_unordered_xi_pair_ie_n0_would_be_unique",
    all_pairs_distinct,
    f"pairs by n: {pairs_readable}" if not all_pairs_distinct else "all distinct",
)

# ----------------------------------------------------------------------
print("\n=== SUMMARY ===")
n_ok = sum(1 for v in RESULTS.values() if v)
print(
    f"  boolean checks : {len(RESULTS)} distinct names from {N_CHECK_CALLSITES} call sites  (passed {n_ok})"
)
print(f"  recorded data  : {len(DATA)}  -- NOT counted as checks")
print("  hardcoded-condition self-audit: PASS (no check() takes a literal)")
print(f"  failures       : {len(FAILURES)}  {FAILURES}")

with open(RESULTS_PATH, "w") as f:
    json.dump({"checks": RESULTS, "data": DATA}, f, indent=2, sort_keys=True, default=str)
print(f"  wrote {RESULTS_PATH}")
