"""
Round 17 (2026-07-09): build the twisted Dirac operator DIRECTLY on
rho=7 matrix-coefficient sections, from first principles -- no recalled
formula, no naive substitution into Agricola's UNTWISTED closed-form
Theorem 3.2 (the trap Round 15 hit), no "generic Lichnerowicz formula"
assumption (the trap Round 16 hit, later found genuinely inconsistent
with Agricola's own machinery via a tool-verified 1/6 discrepancy).

THE CONSTRUCTION

For a homogeneous vector bundle G x_H F and an H-intertwiner
w: V_rho -> F, sections in the rho-isotypic piece are realized as
matrix-coefficient sections psi_{v,w}(g) := w(rho_V(g^{-1})v) for
v in V_rho. This round's key structural fact (re-derived from Agricola's
equation 3, "grad_Z psi = Z(psi) + Lambda_tilde_m(Z)psi", and INDEPENDENTLY
verified TWICE by adversarial review this session -- both the sign of
the raw-derivative piece via a from-scratch group-theory hand derivation,
and its consistency with D_on_simple_tensor's own established formula):

  D(psi_{v,w})|_e = -sum_p e_p . w(rho_V(e_p) v)  +  D_on_simple_tensor(w(v))

The FIRST term is genuinely new this round (V_7's own m-action,
Round 14, contracted through w and Clifford-multiplied). The SECOND term
is EXACTLY D_on_simple_tensor (already validated, calibrated against
AHL2023 throughout this whole experiment) applied to w(v) -- i.e. this
formula does NOT invent any new twisted-connection machinery; it
correctly identifies which ALREADY-TRUSTED piece plays which role.

By G2-equivariance (Schur's lemma), D acts on the rho=7-isotypic
component as Id_{V_7} (x) D_7 for a linear operator D_7 on the
intertwiner space w. Crucially, the FORMULA ABOVE, applied for v ranging
over ALL of V_7 (not just one vector), DEFINES D_7(w) as a NEW
intertwiner w' -- this is directly computable and composable (apply
twice for D^2_7), WITHOUT needing D to act on "sections at general g",
only at the identity, for varying v -- this sidesteps the entire
"apply D to a section, then differentiate the RESULT" subtlety that
tripped up earlier attempts.

THE "1"-PIECE, WITHOUT SOLVING FOR THE "3"/"3bar" INTERTWINERS

phi_2 (V_7's SU(3)-singlet, already established) is COMPLETELY ISOLATED
under the su(3) action restricted to V_7 (row AND column 0 exactly zero
for all 8 su(3) generators, VERIFIED this round) -- this means "project
v onto its phi_2-component" is ITSELF an SU(3)-equivariant map V_7 -> C,
with NO need to explicitly identify V_7's "3"/"3bar" pieces. Composing
with embedding into F's two singlets (v_a, v_b, the SAME vectors from
L4B) gives two intertwiners w_a, w_b supported ONLY on phi_2:
  w_a(v) := v[phi_2-component] * v_a,   w_b(v) := v[phi_2-component] * v_b
VERIFIED this round (symbolically, all 7 directions, all 8 generators
simultaneously): w_a is EXACTLY SU(3)-equivariant.

RESULT (see main()): apply D_7 TWICE to w_a and w_b (via the formula
above, evaluated on ALL of V_7 -- not just phi_2, since D_7(w_a) is
generally supported on more than just phi_2), extract the "1"-block
(coefficients of v_a, v_b in D^2_7(w_a)(phi_2), D^2_7(w_b)(phi_2)), and
report the eigenvalues -- a genuinely first-principles, from-scratch
computation of the rho=7 danger-zone answer for this piece, independent
of every formula that failed adversarial review in Rounds 15-16.
"""

import sympy as sp

from g2su3_appendix_a_construction import NU
from g2su3_equivariance_check import build_D_matrix64, build_su3_matrix64
from g2su3_explicit_clifford import DIM, IDX, SUBSETS, e_action, vec_from_subsets

N64 = DIM * DIM
E_SIGN = {1: 1, 2: 1, 3: -1, 4: 1, 5: -1, 6: 1}


def idx64(a, b):
    return DIM * a + b


def rho7_ep(p):
    full = E_SIGN[p] * NU[8 + p]
    return full[1:8, 1:8]


def rho7_nuk(k):
    return NU[k][1:8, 1:8]


def clifford_left_64(p, vec64):
    """e_p . (eta (x) xi) := (e_p.eta) (x) xi -- Clifford mult on the LEFT
    tensor factor only, matching the SAME convention D_on_simple_tensor
    itself uses throughout this experiment (established since Round 10)."""
    out = sp.zeros(N64, 1)
    for row in range(N64):
        c = vec64[row]
        if c == 0:
            continue
        sL = SUBSETS[row // DIM]
        eta = vec_from_subsets({sL: 1})
        e_eta = e_action(p, eta)
        for r2 in range(DIM):
            v = e_eta[r2]
            if v != 0:
                out[DIM * r2 + (row % DIM)] += c * v
    return out


def d7_apply(w_cols, D64):
    """w_cols: list of 7 vectors in F (64-dim), w_cols[i] = w(basis vector
    i of V_7). Returns w'_cols = D_7(w) applied the SAME way, using
    D(psi_{v,w})|_e = -sum_p e_p.w(rho_7(e_p)v) + D_on_simple_tensor(w(v)).
    """
    new_cols = []
    for i in range(7):
        v = sp.zeros(7, 1)
        v[i] = 1
        term2 = sp.simplify(D64 * w_cols[i])
        term1 = sp.zeros(N64, 1)
        for p in range(1, 7):
            Mp = rho7_ep(p)
            rho_ep_v = Mp * v  # rho_7(e_p) applied to basis vector i
            # w(rho_7(e_p) v): rho_ep_v is a LINEAR COMBINATION of V_7 basis
            # vectors -- apply w linearly using w_cols.
            w_of_that = sp.zeros(N64, 1)
            for j in range(7):
                if rho_ep_v[j] != 0:
                    w_of_that += rho_ep_v[j] * w_cols[j]
            term1 += clifford_left_64(p, w_of_that)
        new_cols.append(sp.simplify(-term1 + term2))
    return new_cols


def main():
    print("=" * 70)
    print("SETUP: w_a, w_b (V_7 -> F, supported only on phi_2)")
    print("=" * 70)
    y1, y2, y3 = IDX[(1,)], IDX[(2,)], IDX[(3,)]
    y12, y13, y23 = IDX[(1, 2)], IDX[(1, 3)], IDX[(2, 3)]
    one, y123 = IDX[()], IDX[(1, 2, 3)]

    v_a = sp.zeros(N64, 1)
    v_a[idx64(y1, y23)] = 1
    v_a[idx64(y2, y13)] = -1
    v_a[idx64(y3, y12)] = 1
    v_b = sp.zeros(N64, 1)
    v_b[idx64(y123, one)] = 1

    # w_a_cols[i] = w_a(basis vector i of V_7) = (1 if i==0 else 0)*v_a
    w_a_cols = [v_a if i == 0 else sp.zeros(N64, 1) for i in range(7)]
    w_b_cols = [v_b if i == 0 else sp.zeros(N64, 1) for i in range(7)]

    print("\n" + "=" * 70)
    print("VERIFY: w_a is SU(3)-equivariant (symbolic, all directions/generators)")
    print("=" * 70)
    c = sp.symbols("c0:7")
    v_generic = sp.Matrix(c)
    equivariant = True
    for k in range(1, 9):
        Mk = rho7_nuk(k)
        rho_v = Mk * v_generic
        w_of_rho_v = sp.zeros(N64, 1)
        for j in range(7):
            if rho_v[j] != 0:
                w_of_rho_v += rho_v[j] * w_a_cols[j]
        Sk = build_su3_matrix64(k)
        w_v = sp.zeros(N64, 1)
        for j in range(7):
            if v_generic[j] != 0:
                w_v += v_generic[j] * w_a_cols[j]
        rhs = Sk * w_v
        if sp.simplify(w_of_rho_v - rhs) != sp.zeros(N64, 1):
            equivariant = False
    print(f"  w_a SU(3)-equivariant for all 8 generators, symbolic? {equivariant}")

    print("\n" + "=" * 70)
    print("STEP 1: D_7(w_a), D_7(w_b) -- apply the from-scratch formula once")
    print("=" * 70)
    D64 = build_D_matrix64()
    w_a_prime = d7_apply(w_a_cols, D64)
    w_b_prime = d7_apply(w_b_cols, D64)
    print(
        f"  D_7(w_a)(phi_2) nonzero entries: "
        f"{[(SUBSETS[i // DIM], SUBSETS[i % DIM], w_a_prime[0][i]) for i in range(N64) if w_a_prime[0][i] != 0]}"
    )
    print("  (sanity: should equal D_on_simple_tensor(v_a) = -sqrt(3)*w, matching L4B,")
    print("   since w_a(rho_7(e_p)phi_2)=0 -- phi_2's own e_p-derivative has no phi_2-component)")

    print("\n" + "=" * 70)
    print("STEP 2: D^2_7(w_a), D^2_7(w_b) -- apply the SAME formula again")
    print("=" * 70)
    w_a_double = d7_apply(w_a_prime, D64)
    w_b_double = d7_apply(w_b_prime, D64)

    print("  D^2_7(w_a)(phi_2) nonzero entries:")
    for i in range(N64):
        if w_a_double[0][i] != 0:
            print(f"    {SUBSETS[i // DIM]},{SUBSETS[i % DIM]}: {w_a_double[0][i]}")
    print("  D^2_7(w_b)(phi_2) nonzero entries:")
    for i in range(N64):
        if w_b_double[0][i] != 0:
            print(f"    {SUBSETS[i // DIM]},{SUBSETS[i % DIM]}: {w_b_double[0][i]}")

    print("\n" + "=" * 70)
    print("STEP 3: extract the '1'-block of D^2_7 and its eigenvalues")
    print("=" * 70)
    va_idx, vb_idx = idx64(y1, y23), idx64(y123, one)
    M11 = w_a_double[0][va_idx]
    M21 = w_a_double[0][vb_idx]
    M12 = w_b_double[0][va_idx]
    M22 = w_b_double[0][vb_idx]
    # also check: does D^2_7(w_a)(phi_2) stay PURELY within span{v_a,v_b},
    # or does it leak into other SU(3)-types (would indicate a construction error)?
    leak_a = sp.simplify(w_a_double[0] - M11 * v_a - M21 * v_b)
    leak_b = sp.simplify(w_b_double[0] - M12 * v_a - M22 * v_b)
    print(
        f"  D^2_7(w_a)(phi_2) stays purely in span(v_a,v_b) (no leakage)? "
        f"{leak_a == sp.zeros(N64, 1)}"
    )
    print(
        f"  D^2_7(w_b)(phi_2) stays purely in span(v_a,v_b) (no leakage)? "
        f"{leak_b == sp.zeros(N64, 1)}"
    )

    M = sp.Matrix([[M11, M12], [M21, M22]])
    print("\n  D^2_7 restricted to the '1'-block (basis v_a,v_b):")
    sp.pprint(M)
    print(f"\n  Eigenvalues: {M.eigenvals()}")


if __name__ == "__main__":
    main()
