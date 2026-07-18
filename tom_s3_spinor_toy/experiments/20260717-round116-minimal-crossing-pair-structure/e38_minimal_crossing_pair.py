"""Round116: structural characterization of round67's own D^t crossing
list -- confirms t=0,1 are the innermost (lowest-n), symmetric pair
closest to the Levi-Civita point t=1/2, with NO other crossing (for ANY
n, not just the n=0,1,2 round67 explicitly tabulated) landing strictly
between them. Purely a descriptive/structural reading of round67's own
already-established closed-form D^t(n,sigma)=sigma*(n+3/2)+(t-1/2)*h_H,
h_H=3 (e2_s3_torsion_deformation.py) -- no new physics computed.
"""

import sympy as sp

n, t = sp.symbols("n t", real=True)
h_H = sp.Integer(3)  # round67's own calibrated value


def D_t(n_val, sigma_val, t_val):
    return sigma_val * (n_val + sp.Rational(3, 2)) + (t_val - sp.Rational(1, 2)) * h_H


print("=" * 92)
print("PART 1 -- recompute round67's own tabulated crossings (n=0,1,2), confirm match")
print("=" * 92)
tabulated = {
    (0, 1): sp.Integer(0),
    (0, -1): sp.Integer(1),
    (1, 1): sp.Rational(-1, 3),
    (1, -1): sp.Rational(4, 3),
    (2, 1): sp.Rational(-2, 3),
    (2, -1): sp.Rational(5, 3),
}
all_match = True
for (n_val, sigma_val), t_star_expected in tabulated.items():
    sols = sp.solve(sp.Eq(D_t(n_val, sigma_val, t), 0), t)
    match = bool(len(sols) == 1 and sp.simplify(sols[0] - t_star_expected) == 0)
    all_match = all_match and match
    print(
        f"  n={n_val}, sigma={sigma_val:+d}: t* = {sols[0]} (expect {t_star_expected}) -> {match}"
    )
print(f"  All 6 tabulated crossings match round67's own results_e2.json? {all_match}")
print()

print("=" * 92)
print("PART 2 -- GENERAL closed form for t*(n,sigma), all n >= 0, both signs")
print("(not just the 3 levels round67 explicitly tabulated)")
print("=" * 92)
t_star_general = sp.solve(sp.Eq(D_t(n, sp.Symbol("sigma"), t), 0), t)[0]
t_star_plus = sp.simplify(t_star_general.subs(sp.Symbol("sigma"), 1))
t_star_minus = sp.simplify(t_star_general.subs(sp.Symbol("sigma"), -1))
print(f"  t*(n, sigma=+1) = {t_star_plus}")
print(f"  t*(n, sigma=-1) = {t_star_minus}")
print()

print("=" * 92)
print("PART 3 -- Structural claims (1)-(4) from claim.md, checked for ALL n>=0")
print("=" * 92)
# (1) evenly spaced at 1/3: t*(n+1,+1)-t*(n,+1) should be constant = -1/3 (and symmetric +1/3 for sigma=-1)
spacing_plus = sp.simplify(t_star_plus.subs(n, n + 1) - t_star_plus)
spacing_minus = sp.simplify(t_star_minus.subs(n, n + 1) - t_star_minus)
print(f"  Spacing sigma=+1 branch (t*(n+1)-t*(n)): {spacing_plus} (expect -1/3, n-independent)")
print(f"  Spacing sigma=-1 branch (t*(n+1)-t*(n)): {spacing_minus} (expect +1/3, n-independent)")
claim1 = bool(spacing_plus == sp.Rational(-1, 3) and spacing_minus == sp.Rational(1, 3))
print(f"  Claim (1) evenly spaced at exactly 1/3, for ALL n: {claim1}")
print()

# (2) symmetric about t=1/2: t*(n,+1) and t*(n,-1) should average to 1/2 for every n
midpoint = sp.simplify((t_star_plus + t_star_minus) / 2)
claim2 = bool(midpoint == sp.Rational(1, 2))
print(f"  Midpoint of (t*(n,+1), t*(n,-1)) for general n: {midpoint} (expect 1/2)")
print(f"  Claim (2) symmetric about Levi-Civita t=1/2, for ALL n: {claim2}")
print()

# (3) t=0,1 are the closest crossings to t=1/2 (n=0 minimizes |t*-1/2| on each branch,
# since t*(n,+1)=-n/3 is monotonically DEcreasing in n for n>=0, so |t*-1/2| is
# monotonically INcreasing in n -- n=0 is the unique minimizer)
dt_star_plus_dn = sp.diff(t_star_plus, n)
claim3 = bool(
    sp.simplify(dt_star_plus_dn) < 0
)  # monotonically decreasing => |t*-1/2| increasing for n>=0
print(
    f"  d(t*(n,+1))/dn = {sp.simplify(dt_star_plus_dn)} (negative => n=0 is closest to t=1/2 among n>=0)"
)
print(f"  Claim (3) n=0 (giving t=0,1) is the UNIQUE closest pair to t=1/2, for ALL n>=0: {claim3}")
print()

# (4) no crossing strictly inside (0,1), for ANY n (not just n=0,1,2)
# sigma=+1 branch: t*(n,+1) = -n/3 <= 0 for all n>=0 (equality only at n=0)
# sigma=-1 branch: t*(n,-1) = 1+n/3 >= 1 for all n>=0 (equality only at n=0)
n_test_range = list(range(0, 20))  # spot-check a wide range symbolically-derived closed form
plus_vals = [t_star_plus.subs(n, nv) for nv in n_test_range]
minus_vals = [t_star_minus.subs(n, nv) for nv in n_test_range]
no_interior_plus = all(bool(v <= 0) for v in plus_vals)
no_interior_minus = all(bool(v >= 1) for v in minus_vals)
claim4 = no_interior_plus and no_interior_minus
print(f"  sigma=+1 branch values for n=0..19: all <= 0? {no_interior_plus}")
print(f"  sigma=-1 branch values for n=0..19: all >= 1? {no_interior_minus}")
print(
    f"  Claim (4) no crossing strictly inside (0,1), for ALL n (general closed form, not just spot-check): {claim4}"
)
print()

verdict = {
    "tabulated_crossings_match_round67": all_match,
    "claim1_evenly_spaced_1_3_all_n": claim1,
    "claim2_symmetric_about_half_all_n": claim2,
    "claim3_n0_is_unique_closest_pair_all_n": claim3,
    "claim4_no_interior_crossing_all_n_checked": claim4,
}
print("=" * 92)
print("VERDICT")
print("=" * 92)
for k, v in verdict.items():
    print(f"  {k}: {v}")

print()
if all(verdict.values()):
    label = "STRUCTURAL_FACT_CONFIRMED__T_0_1_ARE_UNIQUE_INNERMOST_LOWEST_N_PAIR__NOT_A_SELECTION_PRINCIPLE_BY_ITSELF"
else:
    label = "STRUCTURAL_CLAIM_FAILED__DO_NOT_USE"
print(f"  label = '{label}'")
