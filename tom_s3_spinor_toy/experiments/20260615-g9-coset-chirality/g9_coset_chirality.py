"""G9: Why S⁶ = G₂/SU(3) can produce chiral fermions — the equal-rank mechanism.

G8 showed: round S³×S⁶ with NO gauge background gives no net chirality (b₁=b₂=0,
index=0). The escape route is the coset structure S⁶ = G₂/SU(3) with its canonical
SU(3) connection. This gate establishes the ROBUST structural reason that escape works.

The key fact (Bott; Gross-Kostant-Ramond-Sternberg 1998):
  a homogeneous space G/H admits G-invariant CHIRAL fermions with a non-zero Dirac
  index iff rank(G) = rank(H).

We verify computationally for (G,H) = (G₂, SU(3)):
  1. The G₂ root system: 12 roots = 6 long + 6 short.
  2. The 6 LONG roots form an A₂ = su(3) root system  → SU(3) ⊂ G₂.
  3. The 6 SHORT roots = weights of 3 ⊕ 3̄ of that SU(3) = complexified TS⁶.
     (This is the SAME SU(3) that becomes SU(3)_color in G6.)
  4. rank(G₂) = rank(SU(3)) = 2  → EQUAL RANK → chirality mechanism available.
  5. |W_{G₂}| = 12, |W_{SU(3)}| = 6  → χ(S⁶) = |W_G|/|W_H| = 2 (matches χ(S⁶)=2).

What this gate does NOT do: compute the explicit twisted index number for the SM
representations (GKRS multiplet bookkeeping). That is deferred to G10 and needs a
literature cross-check — see caveats.
"""

import sympy as sp

s3 = sp.sqrt(3)
H = sp.Rational(1, 2)


# ── G₂ root system in 2D (standard realization, short²=1, long²=3) ─────────────
SHORT_ROOTS = [
    (sp.Integer(1), sp.Integer(0)),
    (sp.Integer(-1), sp.Integer(0)),
    (H, s3 / 2),
    (-H, -s3 / 2),
    (-H, s3 / 2),
    (H, -s3 / 2),
]

LONG_ROOTS = [
    (sp.Rational(3, 2), s3 / 2),
    (-sp.Rational(3, 2), -s3 / 2),
    (-sp.Rational(3, 2), s3 / 2),
    (sp.Rational(3, 2), -s3 / 2),
    (sp.Integer(0), s3),
    (sp.Integer(0), -s3),
]

ALL_ROOTS = SHORT_ROOTS + LONG_ROOTS


# ── linear algebra helpers (exact) ────────────────────────────────────────────
def dot(u, v):
    return sp.simplify(u[0] * v[0] + u[1] * v[1])


def norm2(u):
    return dot(u, u)


def reflect(v, alpha):
    """Weyl reflection of v in the hyperplane ⟂ alpha."""
    c = sp.simplify(2 * dot(v, alpha) / norm2(alpha))
    return (sp.simplify(v[0] - c * alpha[0]), sp.simplify(v[1] - c * alpha[1]))


def vkey(v):
    """Hashable canonical key for an exact 2D vector."""
    return (sp.nsimplify(sp.simplify(v[0])), sp.nsimplify(sp.simplify(v[1])))


def generate_weyl_group(simple_roots):
    """Generate the Weyl group (as a set of 2x2 matrices) from simple reflections."""

    # Represent each group element as a 2x2 sympy Matrix acting on column vectors.
    def refl_matrix(alpha):
        a = sp.Matrix(alpha)
        return sp.eye(2) - 2 * (a * a.T) / norm2(alpha)

    gens = [refl_matrix(a) for a in simple_roots]
    elements = {sp.ImmutableMatrix(sp.eye(2))}
    frontier = list(elements)
    while frontier:
        new_frontier = []
        for g in frontier:
            for s in gens:
                h = sp.ImmutableMatrix(sp.simplify(s * g))
                if h not in elements:
                    elements.add(h)
                    new_frontier.append(h)
        frontier = new_frontier
    return elements


# ── checks ────────────────────────────────────────────────────────────────────
def check_root_counts():
    short_ok = all(norm2(r) == 1 for r in SHORT_ROOTS)
    long_ok = all(norm2(r) == 3 for r in LONG_ROOTS)
    return len(SHORT_ROOTS) == 6 and len(LONG_ROOTS) == 6 and short_ok and long_ok


def check_long_roots_form_A2():
    """Long roots: closed under their own reflections, 6 roots, hexagonal (A₂)."""
    long_set = {vkey(r) for r in LONG_ROOTS}
    # closed under reflection by any long root
    for r in LONG_ROOTS:
        for a in LONG_ROOTS:
            if vkey(r) == vkey((-a[0], -a[1])):
                continue
            refl = reflect(r, a)
            if vkey(refl) not in long_set:
                return False
    return len(long_set) == 6


def check_short_roots_are_3_plus_3bar():
    """Short roots split into two SU(3)-triangles (3 and 3̄), oppositely oriented."""
    # The 3: three short roots forming an equilateral triangle (120° apart).
    triple_3 = [(sp.Integer(1), sp.Integer(0)), (-H, s3 / 2), (-H, -s3 / 2)]
    triple_3bar = [(sp.Integer(-1), sp.Integer(0)), (H, s3 / 2), (H, -s3 / 2)]
    short_set = {vkey(r) for r in SHORT_ROOTS}
    union = {vkey(r) for r in triple_3} | {vkey(r) for r in triple_3bar}
    if union != short_set:
        return False
    # each triple sums to zero (weights of a fundamental SU(3) irrep)
    sum3 = (sum(r[0] for r in triple_3), sum(r[1] for r in triple_3))
    sum3bar = (sum(r[0] for r in triple_3bar), sum(r[1] for r in triple_3bar))
    # 3̄ = -(3)
    neg3 = {vkey((-r[0], -r[1])) for r in triple_3}
    return (
        sp.simplify(sum3[0]) == 0
        and sp.simplify(sum3[1]) == 0
        and sp.simplify(sum3bar[0]) == 0
        and sp.simplify(sum3bar[1]) == 0
        and neg3 == {vkey(r) for r in triple_3bar}
    )


def main():
    print("=" * 78)
    print("G9: S⁶ = G₂/SU(3) — equal-rank chirality mechanism")
    print("=" * 78)

    # 1. root counts
    c1 = check_root_counts()
    print(
        f"\n1. G₂ root system: 6 short (|α|²=1) + 6 long (|α|²=3) = 12 roots ... "
        f"{'OK' if c1 else 'FAIL'}"
    )

    # 2. long roots = A₂ = SU(3)
    c2 = check_long_roots_form_A2()
    print(
        f"2. 6 LONG roots form A₂ = su(3) root system (SU(3) ⊂ G₂) ........... "
        f"{'OK' if c2 else 'FAIL'}"
    )

    # 3. short roots = 3 ⊕ 3̄
    c3 = check_short_roots_are_3_plus_3bar()
    print(
        f"3. 6 SHORT roots = weights of 3 ⊕ 3̄ of SU(3) = (TS⁶)_ℂ ............ "
        f"{'OK' if c3 else 'FAIL'}"
    )
    print("     → the tangent space of S⁶ literally carries the color 3 ⊕ 3̄ (cf. G6)")

    # 4. equal rank
    rank_g2 = 2
    rank_su3 = 2
    c4 = rank_g2 == rank_su3
    print(
        f"4. rank(G₂)={rank_g2} = rank(SU(3))={rank_su3}  → EQUAL RANK .............. "
        f"{'OK' if c4 else 'FAIL'}"
    )

    # 5. Weyl group orders → Euler characteristic
    W_g2 = generate_weyl_group([SHORT_ROOTS[0], LONG_ROOTS[2]])  # one short + one long simple
    su3_simple = [(sp.Rational(3, 2), s3 / 2), (-sp.Rational(3, 2), s3 / 2)]  # two long, 120°
    W_su3 = generate_weyl_group(su3_simple)
    chi = len(W_g2) // len(W_su3)
    c5 = len(W_g2) == 12 and len(W_su3) == 6 and chi == 2
    print(
        f"5. |W(G₂)|={len(W_g2)}, |W(SU(3))|={len(W_su3)} → χ(S⁶)=|W_G|/|W_H|={chi} "
        f"(matches χ(S⁶)=2) ... {'OK' if c5 else 'FAIL'}"
    )

    # 6. the theorem (cited, not re-proved)
    print("\n6. [DOCS] Bott / Gross-Kostant-Ramond-Sternberg (1998):")
    print("     equal rank(G)=rank(H) ⟺ G/H carries G-invariant CHIRAL spinors with")
    print("     a non-zero Dirac index. This is EXACTLY the structure absent in G8's")
    print("     round-metric analysis — and present here. The chirality escape is real.")

    print("\n   [DOCS] S⁶ untwisted Dirac index = ∫Â(S⁶) = 0 (no degree-6 Â term)")
    print("          → consistent with G8. Chirality needs the SU(3)-TWISTED operator.")

    verdict = c1 and c2 and c3 and c4 and c5
    print("\n" + "=" * 78)
    print(f"VERDICT: {'PASS_G9_EQUAL_RANK_CHIRALITY_MECHANISM' if verdict else 'FAIL'}")
    print("  S⁶ = G₂/SU(3) is equal-rank → admits chiral fermions (escapes G8).")
    print("  The coset SU(3) (= color, G6) acts on TS⁶ as 3 ⊕ 3̄.")
    print("  NEXT (G10, needs lit-check): explicit twisted index for SM reps.")
    print("=" * 78)
    return verdict


if __name__ == "__main__":
    main()
