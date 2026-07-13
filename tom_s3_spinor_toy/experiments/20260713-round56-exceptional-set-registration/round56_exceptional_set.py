"""Round 56 (2026-07-13): formal registration/closure of the finite
exceptional set for the L4B higher-representation growing-gap program.

Per the reviewer's own explicit 6-step scope (a mechanical closure
round, not a search round, following Round 55/55a/55a.1's certification
chain):
  1. Record both equivalent forms: K_N*sqrt(C_N) = K_B*sqrt(C_B).
  2. Fix the final Bourbaki formula.
  3. Symbolically derive C_* (the positivity threshold).
  4. Enumerate all Dynkin labels with C_B <= C_*.
  5. Register the nontrivial exceptional set.
  6. Regression assertions: f(4)<0, f(8)>0.

Also confirms and annotates the rejected {7,14,27,64} branch (the
reviewer's own prior message) as a double-conversion error -- the
native-to-Bourbaki factor was applied twice: once correctly inside
K_cert=K_native/sqrt(2) (Round 55), and again, incorrectly, when
re-deriving the threshold on C_B.
"""

from __future__ import annotations

import sympy as sp

C2 = sp.Symbol("C2", positive=True)


def main() -> None:
    print("=" * 70)
    print("STEP 1: both equivalent forms of the bound")
    print("=" * 70)
    K_native = sp.Rational(4) * sp.sqrt(3) / 3  # from Round 55, K_L=K_R=sqrt(16/3)
    rescale = sp.sqrt(2)
    K_cert = sp.simplify(K_native / rescale)  # Bourbaki-units K
    print(f"  K_native = {K_native}  (native rho7_ep basis, Round 55 STEP 3)")
    print(f"  K_cert   = K_native / sqrt(2) = {K_cert}  (Bourbaki units, Round 55 STEP 3)")

    C_N, C_B = sp.symbols("C_N C_B", positive=True)
    lhs = K_native * sp.sqrt(C_N)
    rhs = K_cert * sp.sqrt(C_B)
    # C_N = C_B/2 (Round 55a, confirmed at rho=7 and rho=14)
    rhs_sub = rhs.subs(C_B, 2 * C_N)
    equal = sp.simplify(lhs - rhs_sub) == 0
    print(f"  Identity check: K_native*sqrt(C_N) == K_cert*sqrt(2*C_N)? {equal}")
    assert equal, "the two equivalent forms do not match -- STOP, re-derive"
    print("  CONFIRMED: K_N*sqrt(C_N) = K_B*sqrt(C_B) -- both forms of the bound")
    print("  are the SAME quantity, just parametrized in different units.")

    print()
    print("=" * 70)
    print("STEP 2: final Bourbaki-units formula")
    print("=" * 70)
    max_fibre_c2_bourbaki = sp.Integer(3)  # Round 52 + Round 55a.1 (SU3 side confirmed no rescale)
    f = C2 - max_fibre_c2_bourbaki - K_cert * sp.sqrt(C2)
    print(f"  lambda^2_min(rho) >= C_B(rho) - {max_fibre_c2_bourbaki} - {K_cert}*sqrt(C_B(rho))")
    print(f"  f(C_B) = {f}")

    print()
    print("=" * 70)
    print("STEP 3: symbolic threshold C_*")
    print("=" * 70)
    x = sp.Symbol("x", positive=True)  # x = sqrt(C_B)
    quad = x**2 - K_cert * x - max_fibre_c2_bourbaki
    roots = sp.solve(sp.Eq(quad, 0), x)
    x_star = max(r for r in roots if r.is_real and r > 0)
    x_star = sp.radsimp(sp.nsimplify(x_star))
    C_star = sp.simplify(x_star**2)
    C_star_exact = sp.nsimplify(sp.expand(C_star))
    print(f"  x* (positive root of x^2 - K_cert*x - 3 = 0) = {x_star}")
    print(f"  C_* = x*^2 = {C_star_exact}  ~ {float(C_star_exact):.6f}")
    expected_C_star = sp.Rational(13, 3) + 2 * sp.sqrt(22) / 3
    matches_reviewer = sp.simplify(C_star_exact - expected_C_star) == 0
    print(f"  Matches reviewer's own C_* = (13+2*sqrt(22))/3? {matches_reviewer}")
    assert matches_reviewer, "C_* does not match the reviewer's own closed form -- STOP"

    print()
    print("=" * 70)
    print("STEP 4: enumerate Dynkin labels (m,n) with C_B(m,n) <= C_*")
    print("=" * 70)

    def g2_casimir(m, n):
        return sp.Rational(2 * m * m + 6 * m * n + 6 * n * n + 10 * m + 18 * n, 3)

    def g2_dim(m, n):
        return (
            (m + 1)
            * (n + 1)
            * (m + n + 2)
            * (m + 2 * n + 3)
            * (m + 3 * n + 4)
            * (2 * m + 3 * n + 5)
        ) // 120

    below_threshold = []
    for m in range(7):
        for n in range(7 - m):
            c = g2_casimir(m, n)
            if c <= C_star:
                below_threshold.append((m, n, c, g2_dim(m, n)))
    for m, n, c, d in below_threshold:
        print(f"  (m,n)=({m},{n})  C_B={c}={float(c):.4f}  dim={d}")

    print()
    print("=" * 70)
    print("STEP 5: register the exceptional set")
    print("=" * 70)
    nontrivial_exceptional = [(m, n, d) for m, n, c, d in below_threshold if (m, n) != (0, 0)]
    print(f"  With trivial rep: {[(m, n) for m, n, c, d in below_threshold]}")
    print(
        f"  Nontrivial exceptional set E_nontrivial: {[(m, n) for m, n, d in nontrivial_exceptional]}"
    )
    assert nontrivial_exceptional == [(1, 0, 7)], (
        f"exceptional set does not match the expected {{(1,0)}} -- got {nontrivial_exceptional}, STOP"
    )
    print("  CONFIRMED: E_nontrivial = {(1,0)} = {rho=7} -- the ONLY nontrivial G2")
    print("  representation not certified positive by this general bound.")

    print()
    print("=" * 70)
    print("STEP 6: regression assertions f(4)<0, f(8)>0")
    print("=" * 70)
    f4 = f.subs(C2, 4)
    f8 = f.subs(C2, 8)
    print(f"  f(4) = {sp.nsimplify(f4)} = {float(f4):.6f}  (rho=7, expect <0, i.e. exceptional)")
    print(f"  f(8) = {sp.nsimplify(f8)} = {float(f8):.6f}  (rho=14, expect >0, i.e. safe)")
    assert f4 < 0, "REGRESSION FAILURE: f(4) is not negative -- rho=7 should be exceptional, STOP"
    assert f8 > 0, "REGRESSION FAILURE: f(8) is not positive -- rho=14 should be safe, STOP"
    print("  PASS: f(4)<0 (rho=7 exceptional, correctly not certified), f(8)>0 (rho=14")
    print("  safe, correctly certified positive) -- matches the registered exceptional set.")

    print()
    print("=" * 70)
    print("Monotonicity check (why no further representation needs checking)")
    print("=" * 70)
    vertex = sp.simplify(K_cert**2 / 4)
    print(
        f"  f(C) = C - 3 - K_cert*sqrt(C) is increasing for C > K_cert^2/4 = {vertex} ~ {float(vertex):.4f}"
    )
    print(f"  All nontrivial G2 representations have C_B >= 4 > {float(vertex):.4f} (Round 52),")
    print("  so f is monotonically increasing across the ENTIRE nontrivial spectrum --")
    print("  once positive at rho=14 (the next representation after rho=7), it stays")
    print("  positive for every larger representation. No further enumeration needed.")

    print()
    print("=" * 70)
    print("REJECTED BRANCH (annotated, not deleted, per this project's discipline)")
    print("=" * 70)
    print("""
  The larger set {7,14,27,64} (from an earlier message in this same
  review chain) resulted from applying the native-to-Bourbaki conversion
  factor TWICE: once correctly inside K_cert=K_native/sqrt(2) (Round 55),
  and again, incorrectly, when re-deriving the threshold directly on
  C_B. The positive control passing did NOT by itself distinguish
  between the two candidate normalizations (a bound need not be tight
  to pass a positive control) -- the decisive evidence was the explicit
  K_cert=K_native/sqrt(2) definition line in Round 55's own script,
  confirmed here via the STEP 1 identity check.
""")


if __name__ == "__main__":
    main()
