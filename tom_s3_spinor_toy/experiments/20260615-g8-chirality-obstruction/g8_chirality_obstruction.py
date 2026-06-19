"""G8: The chirality obstruction on S³×S⁶ (Witten 1981 problem), quantified.

Central question: does round S³×S⁶ give CHIRAL 4D fermions (the SM is chiral)?

G6 showed the 32 spinor components carry SM quantum numbers (representation level).
G7 showed there are NO zero modes (Lichnerowicz) → all KK modes are massive.

This gate confronts the deeper issue: even setting masses aside, getting a NET
chirality (more left than right) from a compactification is topologically
obstructed unless extra structure is present (Witten, "Search for a realistic
Kaluza-Klein theory", 1981).

Three computable facts establish the obstruction for the ROUND product:

  A. Cohomology (Künneth): H¹(S³×S⁶) = H²(S³×S⁶) = 0
     → no Wilson lines (Hosotani needs H¹≠0), no abelian flux (needs H²≠0).
  B. Dirac spectrum on each factor is ±-symmetric → index = 0 → zero NET chirality.
  C. π₁(S³×S⁶) = 0 (simply connected) → confirms no Hosotani (unlike S³×S¹ / BG-H1).

The escape route (structural insight, marked [DOCS]/[INFERRED], NOT computed here):
  S⁶ = G₂/SU(3) is a coset (nearly-Kähler). The canonical SU(3) connection on
  this coset IS a non-trivial gauge background — exactly the extra structure
  Witten requires. And that SU(3) is naturally the SU(3)_color of G6.
"""

import sympy as sp

t = sp.symbols("t", nonnegative=True)


# ── A. Künneth cohomology of S³×S⁶ ────────────────────────────────────────────
def poincare_sphere(n):
    """Poincaré polynomial of Sⁿ: 1 + tⁿ  (b₀ = bₙ = 1, else 0)."""
    return 1 + t**n


def poincare_product(*ns):
    """Poincaré polynomial of a product of spheres = product of P-polynomials."""
    p = sp.Integer(1)
    for n in ns:
        p *= poincare_sphere(n)
    return sp.expand(p)


def betti_numbers(poincare_poly, k_max=12):
    """Extract Betti numbers b_k = coefficient of t^k."""
    poly = sp.Poly(poincare_poly, t)
    return {k: int(poly.coeff_monomial(t**k)) for k in range(k_max + 1)}


# ── B. Dirac spectrum symmetry → index ────────────────────────────────────────
def dirac_eigenvalues_s6(n_max, rho=1):
    """S⁶ Dirac eigenvalues ±(n+3)/ρ, n=0..n_max  (from G4)."""
    vals = []
    for n in range(n_max + 1):
        vals.append(sp.Integer(n + 3) / rho)  # positive branch
        vals.append(-sp.Integer(n + 3) / rho)  # negative branch
    return vals


def dirac_eigenvalues_s3(m_max, rho=1):
    """S³ Dirac eigenvalues ±(m+3/2)/ρ, m=0..m_max."""
    vals = []
    for m in range(m_max + 1):
        vals.append(sp.Rational(2 * m + 3, 2) / rho)
        vals.append(-sp.Rational(2 * m + 3, 2) / rho)
    return vals


def chirality_index(eigenvalues):
    """
    Index proxy = (# positive) - (# negative) eigenvalues among nonzero modes,
    plus dim(kernel). For a ±-symmetric spectrum with no zero modes this is 0.
    """
    n_pos = sum(1 for e in eigenvalues if e > 0)
    n_neg = sum(1 for e in eigenvalues if e < 0)
    n_zero = sum(1 for e in eigenvalues if e == 0)
    return n_pos - n_neg, n_zero


# ── Main report ───────────────────────────────────────────────────────────────
def main():
    print("=" * 78)
    print("G8: Chirality obstruction on round S³×S⁶  (Witten 1981)")
    print("=" * 78)

    # --- Part A: cohomology ---
    print("\n── A. Künneth cohomology — which gauge backgrounds are possible? ──")
    P = poincare_product(3, 6)
    print(f"Poincaré polynomial P(S³×S⁶) = (1+t³)(1+t⁶) = {P}")
    b = betti_numbers(P)
    print("Betti numbers: " + ", ".join(f"b{k}={v}" for k, v in b.items() if v != 0))

    print(
        f"\n  b₁ (Wilson lines / Hosotani) = {b[1]}  →  "
        f"{'POSSIBLE' if b[1] else 'IMPOSSIBLE — no non-contractible 1-cycle'}"
    )
    print(
        f"  b₂ (abelian magnetic flux)   = {b[2]}  →  "
        f"{'POSSIBLE' if b[2] else 'IMPOSSIBLE — no 2-cohomology'}"
    )
    print(f"  b₃ (3-form / S³ volume)      = {b[3]}")
    print(f"  b₆ (6-form / S⁶ volume)      = {b[6]}")

    obstruction_A = b[1] == 0 and b[2] == 0
    print(
        f"\n  → Round S³×S⁶ admits NO Wilson line and NO abelian flux. "
        f"[{'OBSTRUCTED' if obstruction_A else 'open'}]"
    )

    # --- Part B: spectrum symmetry → index ---
    print("\n── B. Dirac spectrum symmetry → net chirality (index) ──")
    s6 = dirac_eigenvalues_s6(n_max=4)
    s3 = dirac_eigenvalues_s3(m_max=4)
    idx6, zero6 = chirality_index(s6)
    idx3, zero3 = chirality_index(s3)
    print(f"  S⁶ spectrum ±(n+3)/ρ : index = {idx6}, zero modes = {zero6}")
    print(f"  S³ spectrum ±(m+3/2)/ρ: index = {idx3}, zero modes = {zero3}")
    print("\n  → Both spectra are ±-symmetric: every left-type mode has a right-type partner.")
    print("  → NET chirality (index) = 0. No chiral asymmetry from the round metric alone.")

    # --- Part C: the escape route (marked) ---
    print("\n── C. Escape route — where chirality CAN come from [DOCS/INFERRED] ──")
    print("  [DOCS]     S⁶ = G₂/SU(3) is a coset space (nearly-Kähler).")
    print("  [DOCS]     KK reduction on a coset G/H carries a canonical H-connection")
    print("             = a non-trivial gauge background (Salam-Strathdee; Witten 1981).")
    print("  [INFERRED] That SU(3) coset connection is the 'extra structure' that")
    print("             evades the Künneth obstruction → can give index ≠ 0.")
    print("  [INFERRED] The coset SU(3) is naturally identified with SU(3)_color (G6).")
    print("             → chirality mechanism and color group share one geometric origin.")
    print("  [UNKNOWN]  Whether this yields exactly 3 generations — not addressed.")

    # --- Comparison with BG-H1 (S³×S¹) ---
    print("\n── Comparison: why BG-H1 used S³×S¹, not S³×S⁶ ──")
    P_circle = poincare_product(3, 1)
    b_circle = betti_numbers(P_circle)
    print(f"  P(S³×S¹) = (1+t³)(1+t¹) = {P_circle}")
    print(
        f"  b₁(S³×S¹) = {b_circle[1]}  →  Wilson line POSSIBLE → Hosotani works "
        f"→ BG-H1 found zero mode at λ=0."
    )
    print(
        f"  b₁(S³×S⁶) = {b[1]}  →  Wilson line IMPOSSIBLE → Hosotani needs the "
        f"coset SU(3) connection instead."
    )

    verdict = obstruction_A and idx6 == 0 and idx3 == 0
    print("\n" + "=" * 78)
    print(f"VERDICT: {'PASS_G8_CHIRALITY_OBSTRUCTION_QUANTIFIED' if verdict else 'FAIL'}")
    print("  Round S³×S⁶: no Wilson line (b₁=0), no flux (b₂=0), index=0 → no chiral")
    print("  fermions from the metric alone. Chirality needs SOME extra structure;")
    print("  the natural candidate is the G₂/SU(3) coset connection (other routes:")
    print("  warping, SUGRA form-flux, torsion). This is the central open mechanism.")
    print("=" * 78)
    return verdict


if __name__ == "__main__":
    main()
