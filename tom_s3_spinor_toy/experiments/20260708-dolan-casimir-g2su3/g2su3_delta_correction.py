"""
KEY SIMPLIFICATION FOUND (2026-07-09): Agricola 2002 Section 2 (p.5-6)
proves Jac_h(X,Y,Z) = -Jac_m(X,Y,Z) IDENTICALLY for naturally reductive
spaces (both are m-valued; their sum has zero inner product with all of m
by the g2 Jacobi identity, hence vanishes since m's inner product is
positive definite). This lets the FULL Theorem 3.2 correction (cubic +
quartic terms) be expressed ENTIRELY via H and H^2 (already computed and
cross-validated against AHL2023's independently-published torsion) --
NO new curvature/Jac_h data needed, abandoning the failed V_7/octonion
route for THIS specific piece.

SIGN CORRECTION (2026-07-09, continuation session): re-read Agricola
2002 Theorem 3.2 directly via PyMuPDF (not doc_bridge OCR, which is what
an earlier round used when first transcribing this formula into
decision.md). The PDF's ACTUAL quartic-term bracket is
"<Zi, Jac_h(Zj,Zk,Zl) + 9t^2 Jac_m(Zj,Zk,Zl)>" -- Jac_h carries NO t
factor, Jac_m carries the 9t^2 factor. An earlier round's decision.md
transcription had these SWAPPED ("Jac_m(...) + 9t^2 Jac_h(...)"), which
silently flipped the sign of the quartic_term formula below. Caught and
INDEPENDENTLY confirmed via a completely separate data path: built
(Ctilde_h)_4 directly from curvature_h (Round 13/14's g2 curvature data,
built from AHL2023 Appendix A -- unrelated to H/torsion) and verified
numerically Ctilde_h_4 == -(1/9)*H2_4 EXACTLY (sympy, zero residual) --
this identity only holds with the corrected sign, confirming the fix.
The t=1/3 sanity check below CANNOT catch this bug (the quartic
coefficient (1-9t^2) is itself exactly zero at t=1/3, so the check passes
identically regardless of the sign in front of it) -- a real example of
a calibration point being insensitive to the exact bug it was meant to
guard against; only the independent curvature_h cross-check catches it.

Derivation:
  cubic term(t)  = 2(1-3t) H                              [already known]
  quartic term(t) = -(1-9t^2) * (1/9) (H^2)_4 = (9t^2-1)*(1/9)*(H^2)_4
    [CORRECTED SIGN, see above] since Jac_h=-Jac_m => quartic bracket =
                        Jac_h + 9t^2 Jac_m = -Jac_m + 9t^2 Jac_m
                        = Jac_m(9t^2-1), and the Jac_m-alone
                        contribution equals (1/9)(H^2)_4 by matching
                        Prop 3.2's coefficient (-9/2) against Thm 3.2's
                        quartic coefficient (-1/2): ratio = 1/9.
  scalar term(t) = (1/8) sum Q_h(...)  +  (3/8) t^2 sum Q_m(...)
    the Q_h piece is t-INDEPENDENT -> cancels in any t-vs-t' difference.
    sum Q_m([Zi,Zj],[Zi,Zj]) = sum_ijk T(i,j,k)^2 = 8 (already known,
    from (H^2)_0 = (3/8)*8 = 3).

Sanity check built in: at t=1/3, BOTH the cubic and quartic terms must
vanish exactly (Agricola's Theorem 3.3) -- this is checked numerically
below, but per the note above it does NOT validate the quartic term's
SIGN (only that its magnitude-determining prefactor is correctly zero
at t=1/3); the sign is validated separately via the curvature_h
cross-check in g2su3_delta_correction_sign_check.py.

Define Delta(t) := (D^t)^2 - (D^{1/3})^2 (difference from the Kostant
cubic Dirac operator, for which (D^{1/3})^2 restricted to a (rho,sigma)
isotypic piece is EXACTLY the naive Casimir-difference formula the
preprint already uses -- Kostant-Parthasarathy proper). This isolates
PRECISELY the correction the skeptic flagged as missing.

Delta(t) = 2(1-3t)H + (9t^2-1)*(1/9)*(H^2 - 3*Id) + [scalar(t)-scalar(1/3)]
scalar(t)-scalar(1/3) = (3/8)*(t^2-1/9)*8 = 3*(t^2-1/9)

At t=1/2: Delta(1/2) = -H + (5/36)*(H^2-3I) + 3*(1/4-1/9)
                      = -H + (5/36)H^2 - (5/12)I + (5/12)I
                      = -H + (5/36)H^2
"""

import sympy as sp
from g2su3_explicit_clifford import DIM, SUBSETS
from g2su3_H_element import build_T_table, build_H_matrix

sqrt = sp.sqrt


def cubic_term(t, H):
    return 2 * (1 - 3 * t) * H


def quartic_term(t, H2, H2_0):
    H2_4 = H2 - H2_0 * sp.eye(DIM)
    # SIGN CORRECTED 2026-07-09 (was (1-9t^2), see module docstring for the
    # Theorem 3.2 Jac_h/Jac_m transcription error this fixes, independently
    # confirmed via curvature_h): correct prefactor is (9t^2-1).
    return (9 * t**2 - 1) * sp.Rational(1, 9) * H2_4


def scalar_diff(t, sum_Qm):
    # scalar(t) - scalar(1/3), Q_h piece cancels (t-independent)
    return sp.Rational(3, 8) * (t**2 - sp.Rational(1, 9)) * sum_Qm


def delta(t, H, H2, H2_0, sum_Qm):
    return cubic_term(t, H) + quartic_term(t, H2, H2_0) + scalar_diff(t, sum_Qm) * sp.eye(DIM)


def main():
    print("=" * 70)
    print("Computing H, H^2 (reusing validated data)")
    print("=" * 70)
    T = build_T_table()
    H = build_H_matrix(T)
    H2 = sp.simplify(H * H)
    diag_vals = sorted(set(sp.simplify(H2[r, r]) for r in range(DIM)), key=str)
    print(f"H^2 diagonal values found: {diag_vals}")
    H2_0 = sp.Rational(3, 8) * sum(
        sp.simplify(T.get((i, j, k), 0)) ** 2
        for i in range(1, 7)
        for j in range(1, 7)
        for k in range(1, 7)
    )
    sum_Qm = sum(
        sp.simplify(T.get((i, j, k), 0)) ** 2
        for i in range(1, 7)
        for j in range(1, 7)
        for k in range(1, 7)
    )
    print(f"(H^2)_0 = {H2_0}, sum_Qm = sum T^2 = {sum_Qm}")

    print("\n" + "=" * 70)
    print("SANITY CHECK: Delta(1/3) must be EXACTLY ZERO (Theorem 3.3)")
    print("=" * 70)
    d13 = sp.simplify(delta(sp.Rational(1, 3), H, H2, H2_0, sum_Qm))
    is_zero = d13 == sp.zeros(DIM, DIM)
    print(f"Delta(1/3) == 0 (8x8 zero matrix)? {is_zero}")
    if not is_zero:
        print("NONZERO ENTRIES (should be none if the derivation is correct):")
        for r in range(DIM):
            for c in range(DIM):
                if sp.simplify(d13[r, c]) != 0:
                    print(f"  [{SUBSETS[r]},{SUBSETS[c]}] = {d13[r, c]}")

    print("\n" + "=" * 70)
    print("Delta(1/2) = (D^{1/2})^2 - (D^{1/3})^2, the correction beyond the")
    print("naive/cubic-Dirac Casimir formula the preprint currently uses")
    print("=" * 70)
    d12 = sp.simplify(delta(sp.Rational(1, 2), H, H2, H2_0, sum_Qm))
    print("Delta(1/2) matrix (nonzero entries):")
    for r in range(DIM):
        for c in range(DIM):
            v = sp.simplify(d12[r, c])
            if v != 0:
                print(f"  [{SUBSETS[r]},{SUBSETS[c]}] = {v}")
    diag12 = sorted(set(sp.simplify(d12[r, r]) for r in range(DIM)), key=str)
    print(f"\nDiagonal values of Delta(1/2): {diag12}")
    print("(if block-scalar per Schur as expected: one value on trivial-mult-2")
    print(" piece {1,y123}, another on the 3+3bar piece {y1,y2,y3,y12,y13,y23})")


if __name__ == "__main__":
    main()
