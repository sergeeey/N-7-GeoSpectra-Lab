"""
Round 47B (2026-07-13): literal AHL2023 notation audit -- what does
"E_{a,b}" mean, as printed in the primary source, and does Round 13's
45-round-old RHO/NU construction (g2su3_appendix_a_construction.py)
actually match the paper's own verbatim Appendix A formulas?

WHY THIS ROUND. Round 13's own code carries this caveat, unresolved
since 2026-07-09: 'E_{a,b}" convention: NOT verified in the paper's
text (OCR gives no explicit definition on this page) -- assumed to be
the standard ANTISYMMETRIC elementary matrix... THIS ASSUMPTION IS
CALIBRATED BELOW before being trusted'. The downstream calibration
(against Remark 5.2's trusted ad(nu_i)(e_p) action) passed for all 48
(i,p) pairs, giving indirect confidence, but the paper's own literal
definition of E_{a,b} was never directly read. Per the user's own
PRIOR RESULT GATE (see PRIOR_RESULT_GATE.md) and this round's own
acceptance criteria: exact pages/formulas of the primary source, a
paper-symbol -> project-object table, checking all 14 generators (not
one block), no calibration-only closure, doc update not a new theorem
if this is purely notational.

PRIMARY SOURCE FINDING (two targeted research-agent PDF reads,
Agricola-Hofmann-Lawn 2023 "invariant spinors", independently
cross-checked against this file's own code below -- not trusted
without verification, per this project's audit-verification-gate.md):

  Page 8 (Section 2.2, general notational conventions -- NOT local to
  Appendix A, used "throughout the paper"): the paper DOES explicitly
  define E^(n)_{i,j} as the elementary SKEW-SYMMETRIC n x n matrix with
  -1 at position (i,j) and +1 at position (j,i). Round 13's own
  docstring claim ("OCR gives no explicit definition on this page") was
  a FALSE NEGATIVE caused by looking only within Appendix A itself --
  the definition is in Section 2.2, applied throughout including in
  Appendix A's own E^(8)_{i,j} instances.

  Page 49 (Remark A.2): rho(eps_1)..rho(eps_7) are defined as EXPLICIT,
  verbatim linear combinations of E^(8)_{i,j} terms (transcribed exactly
  below, STEP 1).

  Page 49 (Proposition A.3): nu_1..nu_14 (nu_1..nu_8 = su(3),
  nu_9..nu_14 = m) are defined as EXPLICIT, verbatim combinations of
  rho(eps_i)*rho(eps_j) PRODUCTS (transcribed exactly below, STEP 2).

THE SIGN QUESTION, RESOLVED: the paper's own E^(n)_{i,j} (-1 at (i,j),
+1 at (j,i)) is the OPPOSITE overall sign from Round 13's own `Emat`
function (+1 at (a,b), -1 at (b,a)). This means, term-by-term,
code_rho(i) = -paper_rho(i) for every i (each rho(eps_i) is a SUM of
E-terms with a FIXED structure; flipping the sign of every E flips the
whole sum). Since nu_k is built ENTIRELY from PRODUCTS rho(eps_i)*
rho(eps_j) (never a bare rho(eps_i) alone), and (-A)*(-B) = A*B, this
sign convention difference is STRUCTURALLY INVISIBLE to every nu_k --
not a lucky coincidence, a provable consequence of nu_k's own quadratic
form. Verified directly below (STEP 3), not just argued.

ANTI-CIRCULARITY: the paper's own E-convention and nu_k formulas are
built FRESH in this script (PAPER_E, PAPER_RHO, PAPER_NU below), not
imported from g2su3_appendix_a_construction.py, so the comparison in
STEP 4 is a genuine independent check, not a self-consistency tautology.

Evidence markers: every claim is re-computed and asserted in main()
below ([VERIFIED-tool] on run).
"""

import sympy as sp

from g2su3_appendix_a_construction import RHO as CODE_RHO
from g2su3_appendix_a_construction import NU as CODE_NU

N = 8


def paper_E(i, j):
    """AHL2023's own E^(n)_{i,j} (page 8): -1 at (i,j), +1 at (j,i).
    OPPOSITE sign from g2su3_appendix_a_construction.py's own Emat."""
    M = sp.zeros(N, N)
    M[i - 1, j - 1] = -1
    M[j - 1, i - 1] = 1
    return M


# STEP 1: rho(eps_i), i=1..7, verbatim from AHL2023 Remark A.2 (page 49),
# built from PAPER_E (this script's own fresh construction, not imported).
PAPER_RHO = {
    1: paper_E(1, 8) + paper_E(2, 7) - paper_E(3, 6) - paper_E(4, 5),
    2: -paper_E(1, 7) + paper_E(2, 8) + paper_E(3, 5) - paper_E(4, 6),
    3: -paper_E(1, 6) + paper_E(2, 5) - paper_E(3, 8) + paper_E(4, 7),
    4: -paper_E(1, 5) - paper_E(2, 6) - paper_E(3, 7) - paper_E(4, 8),
    5: -paper_E(1, 3) - paper_E(2, 4) + paper_E(5, 7) + paper_E(6, 8),
    6: paper_E(1, 4) - paper_E(2, 3) - paper_E(5, 8) + paper_E(6, 7),
    7: paper_E(1, 2) - paper_E(3, 4) - paper_E(5, 6) + paper_E(7, 8),
}


def prho(i):
    return PAPER_RHO[i]


def pprod(i, j):
    return prho(i) * prho(j)


# STEP 2: nu_1..nu_14, verbatim from AHL2023 Proposition A.3 (page 49),
# built from PAPER_RHO (this script's own fresh construction).
PAPER_NU = {
    1: sp.Rational(1, 4) * (pprod(1, 2) - pprod(5, 6)),
    2: sp.Rational(1, 4) * (pprod(3, 5) + pprod(4, 6)),
    3: sp.Rational(1, 4) * (pprod(3, 6) - pprod(4, 5)),
    4: sp.Rational(1, 4) * (pprod(1, 3) + pprod(2, 4)),
    5: sp.Rational(1, 4) * (pprod(1, 4) - pprod(2, 3)),
    6: sp.Rational(1, 4) * (pprod(1, 5) + pprod(2, 6)),
    7: sp.Rational(1, 4) * (pprod(1, 6) - pprod(2, 5)),
    8: -(sp.Rational(1, 4) / sp.sqrt(3)) * (pprod(1, 2) - 2 * pprod(3, 4) + pprod(5, 6)),
    9: (sp.Rational(1, 4) / sp.sqrt(3)) * (2 * pprod(1, 7) - pprod(3, 6) - pprod(4, 5)),
    10: (sp.Rational(1, 4) / sp.sqrt(3)) * (2 * pprod(2, 7) - pprod(3, 5) + pprod(4, 6)),
    11: (sp.Rational(1, 4) / sp.sqrt(3)) * (pprod(1, 3) - pprod(2, 4) - 2 * pprod(6, 7)),
    12: (sp.Rational(1, 4) / sp.sqrt(3)) * (pprod(1, 4) + pprod(2, 3) - 2 * pprod(5, 7)),
    13: (sp.Rational(1, 4) / sp.sqrt(3)) * (pprod(1, 5) - pprod(2, 6) + 2 * pprod(4, 7)),
    14: (sp.Rational(1, 4) / sp.sqrt(3)) * (pprod(1, 6) + pprod(2, 5) + 2 * pprod(3, 7)),
}


def main():
    print("=" * 70)
    print("STEP 1+3: is code_rho(i) == -paper_rho(i) for all i=1..7?")
    print("(the ONLY effect of the E-sign convention difference)")
    print("=" * 70)
    rho_all_flip = True
    for i in range(1, 8):
        diff = sp.simplify(CODE_RHO[i] - (-PAPER_RHO[i]))
        match = diff == sp.zeros(N, N)
        print(f"  code_rho({i}) == -paper_rho({i})? {match}")
        if not match:
            rho_all_flip = False
    assert rho_all_flip, "rho(eps_i) sign relationship broken -- E-convention analysis wrong"

    print("\n" + "=" * 70)
    print("STEP 4 (the actual test): does code's NU[k] match this script's own")
    print("independently-built PAPER_NU[k], for ALL 14 k, using the paper's OWN")
    print("literal E-sign convention (not imported, not calibrated to match)?")
    print("=" * 70)
    all_match = True
    for k in range(1, 15):
        diff = sp.simplify(CODE_NU[k] - PAPER_NU[k])
        match = diff == sp.zeros(N, N)
        print(f"  nu_{k}: code == paper (independent rebuild)? {match}")
        if not match:
            all_match = False
            print("    DIFFERENCE:")
            sp.pprint(diff)
    print(f"\n  ALL 14 GENERATORS MATCH: {all_match}")
    assert all_match, "at least one nu_k differs from the paper's own literal formula"

    print("\n" + "=" * 70)
    print("STEP 5 (negative control): confirm the check has discriminating power")
    print("-- deliberately corrupt ONE sign in a fresh nu_5 and confirm mismatch")
    print("=" * 70)
    corrupted_nu5 = sp.Rational(1, 4) * (pprod(1, 4) + pprod(2, 3))  # wrong sign
    corrupted_diff = sp.simplify(CODE_NU[5] - corrupted_nu5)
    corrupted_differs = corrupted_diff != sp.zeros(N, N)
    print(
        f"  Deliberately-wrong nu_5 (+prod(2,3)) correctly flagged as different? "
        f"{corrupted_differs}"
    )
    assert corrupted_differs, "negative control failed -- check has no discriminating power"

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("  PASS. AHL2023 (Agricola-Hofmann-Lawn 2023) DOES explicitly define")
    print("  E^(n)_{i,j} (page 8, Section 2.2, used throughout the paper) as the")
    print("  skew-symmetric elementary matrix with -1 at (i,j), +1 at (j,i) --")
    print("  Round 13's own 'OCR gives no explicit definition' claim was a false")
    print("  negative (the definition is in Section 2.2, not Appendix A itself).")
    print()
    print("  Round 13's own Emat(a,b) (+1 at (a,b), -1 at (b,a)) is the OPPOSITE")
    print("  sign from the paper's own E^(n)_{i,j}. This flips the sign of every")
    print("  individual rho(eps_i) (STEP 1+3, verified: code_rho(i)=-paper_rho(i)")
    print("  for all i=1..7) -- but since every nu_k (Proposition A.3) is built")
    print("  ENTIRELY from PRODUCTS rho(eps_i)*rho(eps_j), never a bare rho(eps_i)")
    print("  alone, (-A)(-B)=AB makes this sign convention PROVABLY INVISIBLE to")
    print("  every nu_k -- not a lucky coincidence, a structural consequence of")
    print("  nu_k's own quadratic form. Verified directly (STEP 4): all 14 nu_k")
    print("  match the paper's own literal Proposition A.3 formulas EXACTLY, using")
    print("  an INDEPENDENTLY rebuilt paper-convention E matrix (not imported from")
    print("  the code being checked, not calibrated to match).")
    print()
    print("  This is a NOTATIONAL CLEANUP, not a new theorem: Round 13's")
    print("  construction was already correct; what was missing was the literal")
    print("  primary-source citation proving it, replacing an indirect")
    print("  (calibration-only) justification with a direct one.")


if __name__ == "__main__":
    main()
