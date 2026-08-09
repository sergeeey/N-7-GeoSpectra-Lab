"""
Round 34 (2026-07-11): derive Round 13's `RHO`/`NU` (AHL2023 Appendix A's
g2 construction, used unchanged throughout Rounds 13-33) from the STANDARD,
citable octonion multiplication table (Baez 2002, "The Octonions"), via an
EXPLICIT orthogonal intertwiner matrix -- not an abstract uniqueness
argument (that pattern was already flagged too weak, Round 30's first
correction round). Closes the gap flagged since Round 32: "RHO/NU's own
construction is NOT independently re-derived from octonion multiplication
rules ... `NU_BIVEC_SOURCE` is a direct transcription of Round 13's
already-established data."

REUSES, does not rebuild, Round 68's already-validated octonion machinery
(`g2su3_round34...` below reimplements it locally in exact sympy rather
than importing across experiment folders -- this experiment's own
convention, matching every prior round -- but the Fano-plane table and
the L_i/R_i Clifford-relation/pseudoscalar results are UNCHANGED from
Round 68, which already cites the primary source: Baez, "The Octonions",
Bull. AMS 39 (2002), 145-205, arXiv:math/0105155 -- the canonical
reference for the Fano-plane octonion multiplication table used here).

CORE ARGUMENT:

  [LABEL CORRECTION 2026-08-10, repo-wide Clifford convention audit: every
   "Cl(7,0)" in this file should read Cl(0,7). Note that item (1) below is
   self-contradictory as written -- it names Cl(7,0) and then defines it as
   "generators squaring to -1", which is Cl(0,7) under the convention round67
   and s6-harm-g0 use. The DEFINITION in the parenthesis is right and the code
   below matches it (-2*sp.eye); only the name is inverted. No result changes.
   See docs/clifford_convention_registry.md.]

  (1) Cl(7,0) (7 anticommuting generators squaring to -1) is, as an
      ungraded real algebra, isomorphic to M_8(R) (+) M_8(R) -- exactly
      TWO inequivalent real 8-dimensional irreducible Clifford modules,
      distinguished by the sign of the pseudoscalar Omega_7 := product of
      all 7 generators (Omega_7^2=+I for this signature, so Omega_7 = +-I
      on each irreducible summand).

  (2) [VERIFIED below, STEP A] Octonion LEFT multiplication by the 7
      imaginary Fano-plane basis units, L_1..L_7 (Baez's canonical
      table, reused from Round 68), satisfies the exact Cl(7,0) relations
      and has pseudoscalar Omega_L = -Id exactly.

  (3) [VERIFIED below, STEP B] Round 13's RHO[1]..RHO[7] (AHL2023
      Appendix A, ALREADY calibrated against the paper's own trusted
      Remark 5.2 su(3)-action, independent of this round) ALSO has
      pseudoscalar Omega_RHO = -Id exactly -- the SAME chirality as L,
      not R (octonion RIGHT multiplication, Omega_R=+Id, Round 68).
      Since conjugation by any invertible matrix fixes a scalar matrix
      +-Id exactly, this is a RIGOROUS proof (not a numerical hint) that
      RHO can only possibly be equivalent to L, never to R.

  (4) [VERIFIED below, STEP C] Solving the linear intertwiner system
      `P*L_i = RHO_i*P` for i=1..7 SIMULTANEOUSLY (448 equations = 7
      generators x 64 entries, 64 unknown P entries) gives a UNIQUE
      solution up to overall scale (1-dimensional nullspace, matching
      Schur's lemma for this irreducible 7-generator system) -- an
      explicit matrix P with every entry in {+1,-1} and P^T P = 8*Id (a
      genuine order-8 HADAMARD matrix). `P*L_i - RHO_i*P == 0` holds
      EXACTLY (sympy Integer arithmetic) for ALL 7 generators
      simultaneously -- this is the SAME system used to solve for P
      (not an independent 2-then-5 split), so the exact-match re-check
      below is a genuine self-consistency verification of `linsolve`'s
      own output, not a fresh Schur-uniqueness test on held-out
      generators (see claim.md's Skeptic Verdict for this distinction).

  (5) [VERIFIED below, STEP D] Since `NU_k` (all 14 g2 generators,
      Round 13/AHL2023 Remark A.2) are explicit LINEAR COMBINATIONS of
      products RHO(a)*RHO(b), and conjugation by P is an algebra
      homomorphism (P^-1(AB)P = (P^-1 A P)(P^-1 B P)), the SAME formula
      applied to L(a)*L(b) instead of RHO(a)*RHO(b) is AUTOMATICALLY
      P-conjugate to NU_k. Verified directly (not merely asserted from
      the homomorphism argument) for all 14 generators exactly.

  (6) CONCLUSION: Round 13's ENTIRE g2 construction (RHO + all 14 NU_k,
      hence the whole Phase 2 derivation chain built on it since Rounds
      13-33) is, after this single EXPLICIT change of basis P, literally
      the canonical octonion-triality construction of g2 = Der(O) via
      left-multiplication bivectors on the Fano-plane octonion table --
      not an unrelated ad hoc Clifford-generator recipe. This closes the
      "not independently re-derived from octonion multiplication rules"
      gap with a concrete, verified matrix, not an abstract isomorphism
      argument (the exact failure mode Round 30 already caught once).

HONEST SCOPE: this does NOT prove that AHL2023's own literal "E_{a,b}"
notation (Appendix A's page, still UNVERIFIED against the source PDF's
actual definition, per Round 13's own caveat) means Baez's SPECIFIC
Fano-plane sign convention -- that notational question is untouched,
unaffected, and irrelevant to this round's claim. This round instead
shows that Round 13's ALREADY-CALIBRATED `RHO` (validated independently
via Remark 5.2, not via the E_{a,b} guess) is, regardless of that
open notational question, octonion-multiplication-EQUIVALENT to the
standard canonical construction -- i.e. whatever AHL2023 intended
concretely, the physics it produces (Clifford module, g2 Lie algebra,
downstream T-table/curv_h/Casimir data) is the same as literally using
octonion multiplication from the start. Does NOT change any previously
established numeric value (P is an orthogonal change of basis; all
downstream traces/inner-products are P-invariant) -- purely explanatory.
"""

import sympy as sp

from g2su3_appendix_a_construction import NU, RHO

N = 8
sqrt = sp.sqrt

# Fano-plane octonion multiplication table (Baez 2002, "The Octonions",
# Table 1 convention -- IDENTICAL data already used and tested in Round
# 68, g2su3_round34 reimplements it locally in exact sympy rather than
# importing across experiment-folder boundaries, matching this whole
# experiment's own established convention).
FANO_TRIPLES = [
    (1, 2, 4),
    (2, 3, 5),
    (3, 4, 6),
    (4, 5, 7),
    (5, 6, 1),
    (6, 7, 2),
    (7, 1, 3),
]


def build_mult_table():
    """{(a,b,c): coeff of e_c in e_a*e_b}, e_0=1 (real unit), e_1..e_7 imaginary."""
    M = {}
    for i in range(N):
        M[(0, i, i)] = sp.Integer(1)
        M[(i, 0, i)] = sp.Integer(1)
    for i in range(1, N):
        M[(i, i, 0)] = sp.Integer(-1)
    for a, b, c in FANO_TRIPLES:
        M[(a, b, c)] = sp.Integer(1)
        M[(b, c, a)] = sp.Integer(1)
        M[(c, a, b)] = sp.Integer(1)
        M[(b, a, c)] = sp.Integer(-1)
        M[(c, b, a)] = sp.Integer(-1)
        M[(a, c, b)] = sp.Integer(-1)
    return M


MT = build_mult_table()


def left_matrix(a):
    """8x8 matrix for x -> e_a * x."""
    Lm = sp.zeros(N, N)
    for b in range(N):
        for c in range(N):
            v = MT.get((a, b, c), 0)
            if v != 0:
                Lm[c, b] = v
    return Lm


def right_matrix(a):
    """8x8 matrix for x -> x * e_a."""
    Rm = sp.zeros(N, N)
    for b in range(N):
        for c in range(N):
            v = MT.get((b, a, c), 0)
            if v != 0:
                Rm[c, b] = v
    return Rm


L = {i: left_matrix(i) for i in range(1, 8)}
R = {i: right_matrix(i) for i in range(1, 8)}


def pseudoscalar(mats):
    out = sp.eye(N)
    for i in range(1, 8):
        out = out * mats[i]
    return sp.simplify(out)


def main():
    print("=" * 70)
    print("STEP A: verify octonion left-multiplication L_1..L_7 (Baez's")
    print("canonical Fano-plane table) satisfies exact Cl(7,0) relations")
    print("=" * 70)
    clifford_ok = True
    for i in range(1, 8):
        for j in range(1, 8):
            ac = sp.simplify(L[i] * L[j] + L[j] * L[i])
            expected = -2 * sp.eye(N) if i == j else sp.zeros(N, N)
            if ac != expected:
                clifford_ok = False
    print(f"  {{L_i,L_j}} = -2*delta_ij*Id exactly, all 49 pairs? {clifford_ok}")
    assert clifford_ok, "octonion left-multiplication does not satisfy Cl(7,0)"

    Omega_L = pseudoscalar(L)
    omega_l_ok = Omega_L == -sp.eye(N)
    print(f"  pseudoscalar Omega_L == -Id exactly? {omega_l_ok}")
    assert omega_l_ok, "Omega_L chirality unexpected -- Round 68's own finding not reproduced"

    print("\n" + "=" * 70)
    print("STEP B: Round 13's RHO[1..7] pseudoscalar -- which chirality?")
    print("=" * 70)
    Omega_RHO = pseudoscalar(RHO)
    omega_rho_matches_L = Omega_RHO == -sp.eye(N)
    print(f"  Omega_RHO == -Id (same chirality as L, not R)? {omega_rho_matches_L}")
    assert omega_rho_matches_L, "RHO chirality does not match L -- cannot be equivalent to L"

    Omega_R = pseudoscalar(R)
    omega_r_ok = Omega_R == sp.eye(N)
    print(f"  (negative control) Omega_R == +Id exactly? {omega_r_ok}")
    assert omega_r_ok, "Omega_R chirality unexpected"
    print("  => since conjugation by ANY invertible matrix fixes a central")
    print("  scalar matrix +-Id exactly, RHO (Omega=-Id) can RIGOROUSLY")
    print("  NEVER be equivalent to R (Omega=+Id) -- a proof, not a")
    print("  numerical coincidence. RHO can only possibly match L.")

    print("\n" + "=" * 70)
    print("STEP C: solve for the EXPLICIT intertwiner P: P*L_i = RHO_i*P")
    print("for all i=1..7 simultaneously (448 equations = 7x64, 64 unknowns)")
    print("=" * 70)
    Psyms = sp.symbols("p0:64")
    Pmat = sp.Matrix(N, N, Psyms)
    eqs = []
    for i in range(1, 8):
        eqs += list(Pmat * L[i] - RHO[i] * Pmat)
    sol = sp.linsolve(eqs, Psyms)
    sol_list = list(sol)[0]
    free_syms = set()
    for expr in sol_list:
        free_syms |= expr.free_symbols
    print(f"  intertwiner solution space dimension (free params): {len(free_syms)}")
    assert len(free_syms) == 1, (
        f"expected a 1-dim intertwiner space (Schur's lemma for this "
        f"irreducible system), got {len(free_syms)} free params"
    )
    (free_sym,) = free_syms
    P = sp.Matrix(N, N, [sp.simplify(e.subs({free_sym: 1})) for e in sol_list])
    print("  P (normalized, one free scale fixed to 1):")
    print(f"  {P.tolist()}")

    entries_pm1 = all(v in (1, -1) for v in P)
    print(f"  every entry of P is +1 or -1 (Hadamard-type)? {entries_pm1}")
    gram = sp.simplify(P.T * P)
    is_hadamard = gram == N * sp.eye(N)
    print(f"  P^T P == {N}*Id exactly (order-{N} Hadamard matrix)? {is_hadamard}")
    assert entries_pm1 and is_hadamard, "P is not the expected Hadamard-type intertwiner"

    intertwines_all_7 = True
    for i in range(1, 8):
        diff = sp.simplify(P * L[i] - RHO[i] * P)
        if diff != sp.zeros(N, N):
            intertwines_all_7 = False
    print(f"  P*L_i == RHO_i*P exactly, verified for ALL 7 generators? {intertwines_all_7}")
    assert intertwines_all_7, "P fails to intertwine all 7 generators"
    print("  => RHO_i = P*L_i*P^-1 EXACTLY: RHO is octonion left-multiplication")
    print("  after an explicit, concrete, verified change of basis P.")

    print("\n" + "=" * 70)
    print("STEP D: the SAME P also intertwines all 14 g2 generators NU_k")
    print("(automatic from P intertwining RHO/L via the algebra-homomorphism")
    print("property of conjugation, but VERIFIED directly here, not merely")
    print("asserted from that argument)")
    print("=" * 70)

    def Lprod(a, b):
        return L[a] * L[b]

    NU_OCT_FORMULA = {
        1: sp.Rational(1, 4) * (Lprod(1, 2) - Lprod(5, 6)),
        2: sp.Rational(1, 4) * (Lprod(3, 5) + Lprod(4, 6)),
        3: sp.Rational(1, 4) * (Lprod(3, 6) - Lprod(4, 5)),
        4: sp.Rational(1, 4) * (Lprod(1, 3) + Lprod(2, 4)),
        5: sp.Rational(1, 4) * (Lprod(1, 4) - Lprod(2, 3)),
        6: sp.Rational(1, 4) * (Lprod(1, 5) + Lprod(2, 6)),
        7: sp.Rational(1, 4) * (Lprod(1, 6) - Lprod(2, 5)),
        8: (sp.Rational(1, 4) / sqrt(3)) * (-Lprod(1, 2) + 2 * Lprod(3, 4) - Lprod(5, 6)),
        9: (sp.Rational(1, 4) / sqrt(3)) * (2 * Lprod(1, 7) - Lprod(3, 6) - Lprod(4, 5)),
        10: (sp.Rational(1, 4) / sqrt(3)) * (2 * Lprod(2, 7) - Lprod(3, 5) + Lprod(4, 6)),
        11: (sp.Rational(1, 4) / sqrt(3)) * (Lprod(1, 3) - Lprod(2, 4) - 2 * Lprod(6, 7)),
        12: (sp.Rational(1, 4) / sqrt(3)) * (Lprod(1, 4) + Lprod(2, 3) - 2 * Lprod(5, 7)),
        13: (sp.Rational(1, 4) / sqrt(3)) * (Lprod(1, 5) - Lprod(2, 6) + 2 * Lprod(4, 7)),
        14: (sp.Rational(1, 4) / sqrt(3)) * (Lprod(1, 6) + Lprod(2, 5) + 2 * Lprod(3, 7)),
    }

    nu_all_match = True
    for k in range(1, 15):
        diff = sp.simplify(P * NU_OCT_FORMULA[k] - NU[k] * P)
        if diff != sp.zeros(N, N):
            nu_all_match = False
            print(f"  MISMATCH at nu_{k}")
    print(f"  P*NU_OCT_k == NU_k*P exactly, ALL 14 generators? {nu_all_match}")
    assert nu_all_match, "P fails to intertwine the full 14-dim g2 basis"

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("  Round 13's RHO/NU (used unchanged throughout Rounds 13-33) is,")
    print("  after the single explicit Hadamard-type intertwiner P found")
    print("  above, EXACTLY the canonical octonion-triality construction of")
    print("  g2 = Der(O) via left-multiplication bivectors on Baez's")
    print("  standard Fano-plane octonion table -- not an unrelated ad hoc")
    print("  Clifford-generator recipe. Closes the gap flagged since Round")
    print("  32: 'RHO/NU's own construction not independently re-derived")
    print("  from octonion multiplication rules'.")
    print()
    print("  HONEST LIMIT: does NOT resolve whether AHL2023's own literal")
    print("  E_{a,b} notation means this SPECIFIC Fano sign convention --")
    print("  that separate notational question (Round 13's own caveat)")
    print("  remains open, untouched, and irrelevant to this round's claim.")


if __name__ == "__main__":
    main()
