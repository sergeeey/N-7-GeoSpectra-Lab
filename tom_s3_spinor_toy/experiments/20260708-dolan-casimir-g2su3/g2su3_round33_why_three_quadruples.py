"""
Round 33 (2026-07-11): explain STRUCTURALLY (not just verify
computationally) why `jach_coeff`/`degree4_coeff` (Round 26/29/31/32) are
nonzero on EXACTLY the 3 "pair-partition" quadruples `(1,2,3,4)`,
`(1,2,5,6)`, `(3,4,5,6)` out of all `C(6,4)=15` possible ordered
index-quadruples in `1..6` -- an observation Round 31 explicitly flagged
as "verified but not explained from a deeper principle", plausibly
connected to Round 28's proven 3-dimensional SU(3)-equivariant,
Swap-symmetric operator space.

CORE ARGUMENT (a genuine corollary of Round 28's own theorem, not a new
independent proof from scratch):

  (1) Round 28 PROVED: any SU(3)-equivariant (commutes with all 8
      su3_action generators) AND Swap-symmetric (commutes with the
      `Swap` involution) Hermitian operator on Sigma lies EXACTLY in the
      3-dimensional space spanned by {Id, Casimir_su3, H}.

  (2) [VERIFIED below, STEP A] `Ch_4` (Round 26's degree-4 piece of
      C~h, Prop 3.3) and `degree4_term` (Round 26's degree-4 piece of
      Omega_g's own cubic-term expansion) are BOTH SU(3)-equivariant,
      Swap-symmetric, AND Hermitian (real symmetric) -- so (1) applies
      to them DIRECTLY: each MUST be expressible as `a*H + b*Id +
      c*Casimir_su3` for SOME (a,b,c).

  (3) STRUCTURAL FACT (automatic from their own construction, not
      assumed): `Ch_4`/`degree4_term` are built ENTIRELY as
      `sum_{i<j<k<l} coeff(i,j,k,l) * Z_i.Z_j.Z_k.Z_l` (4 DISTINCT
      frame-vector indices) -- this is ALWAYS a genuine degree-4
      Clifford-algebra element (never collapses to a lower degree),
      hence has ZERO degree-0 (scalar/trace) component and ZERO degree-3
      component, BY CONSTRUCTION, not by computation.

  (4) COMBINING (2)+(3) via degree-counting in the {Id,Casimir_su3,H}
      basis itself: `H` is PURELY degree-3 (Kostant's cubic torsion
      element, by ITS OWN construction, established since Round 25/26)
      -- the ONLY source of a degree-3 component in the span. `Id` is
      purely degree-0. `Casimir_su3` (Round 29/30) decomposes as
      `Id + X/3` -- i.e. ONLY degree-0 (coefficient 1) and degree-4
      (coefficient 1/3 on `X:=Z1234+Z1256+Z3456`) parts, ZERO degree-3.
      So in `M = a*H + b*Id + c*Casimir_su3`:
        - the degree-3 component is `a*H` alone -- for `M` to have ZERO
          degree-3 component (STEP 3), we NEED `a=0`.
        - with `a=0`, the degree-0 component is `b + c` (Id contributes
          b, Casimir_su3 contributes c*1) -- for `M` to have ZERO
          degree-0 component (STEP 3), we NEED `b=-c`.
      Hence `M = c*(Casimir_su3 - Id) = (c/3)*X` for a UNIQUE scalar `c`
      determined by `M`'s own normalization -- FORCED, not assumed.

  (5) [VERIFIED below, STEP B] Solving Round 28's own 3x3 linear system
      for `Ch_4` and `degree4_term` gives EXACTLY `a=0` for BOTH,
      confirming step (4)'s prediction directly (not merely consistent
      with it -- the actual solve reproduces a=0 to the letter).

  (6) CONCLUSION: since `Ch_4`/`degree4_term` MUST be proportional to
      `Casimir_su3 - Id = X/3`, and `X`'s own support (Round 29) is
      EXACTLY the 3 pair-partition quadruples with EQUAL coefficient
      across all three -- `Ch_4`/`degree4_term` are FORCED to share
      this SAME support and this SAME "equal across the 3 quadruples"
      property. This is WHY only 3 of 15 quadruples are ever nonzero:
      it is not a coincidence of Jacobiator index gymnastics, it is a
      NECESSARY CONSEQUENCE of (a) Round 28's 3-dim-space theorem and
      (b) the elementary fact that a genuine degree-4 Clifford element
      cannot carry a degree-0 or degree-3 component.

BONUS: this ALSO re-explains Round 30's `Ch_tilde=Casimir_su3` finding
via a cleaner route -- but NOTE this bonus route is only PARTIALLY
structural: the general theorem above (steps 1-6) only forces
`Ch_4 = c*(Casimir_su3-Id)` for SOME scalar `c`; it does NOT by itself
pin down `c=1`. The bonus route additionally PLUGS IN `c=1`, the value
Ch_4 actually SOLVES to in STEP B (a directly-computed fact, not a
structural derivation of why `c` must equal 1) -- giving
`Ch_4 = Casimir_su3 - Id` for THIS specific object. Combined with
`Ch_0=1` (established, Round 26/29): `Ch_tilde = Ch_0*Id + Ch_4 =
Id + (Casimir_su3-Id) = Casimir_su3`. So Round 30's finding is a SPECIAL
CASE of this round's general "purely-degree-4 + SU(3)-equivariant +
Swap-symmetric implies proportional to Casimir_su3-Id" theorem PLUS two
separately-established numeric facts (`Ch_0=1` and `Ch_4`'s own solved
`c=1`) -- not a purely structural re-derivation of `Ch_tilde=Casimir_su3`
from scratch.

HONEST SCOPE: this explains WHY the SUPPORT is confined to the 3
pair-partition quadruples and WHY the coefficient is automatically EQUAL
across all three -- it does NOT explain the SPECIFIC numeric value of
the proportionality constant `c` (e.g. why `Ch_4`'s own `c=1` rather than
some other number) -- that still requires the direct combinatorial
computation (Rounds 26/29/31/32), unchanged by this round.
"""

import sympy as sp

from g2su3_appendix_a_construction import build_curvature_h_table
from g2su3_H_element import build_H_matrix, build_T_table
from g2su3_round26_jach_derivation import build_quartic_matrix, jac_h, jac_m
from g2su3_round28_coefficient_uniqueness import build_swap
from g2su3_twisted_kernel import su3_action
from g2su3_explicit_clifford import DIM

sqrt = sp.sqrt


def unit_vec(i):
    v = sp.zeros(DIM, 1)
    v[i] = 1
    return v


def main():
    print("=" * 70)
    print("SETUP: rebuild Ch_4, degree4_term, H, Casimir_su3, Swap")
    print("(all via the ALREADY-established Rounds 26-29 constructions,")
    print("zero new numeric machinery this round)")
    print("=" * 70)
    T = build_T_table()
    curv_h = build_curvature_h_table()
    H = build_H_matrix(T)
    Id8 = sp.eye(DIM)

    def jach_coeff(i, j, k, ll):
        jh = jac_h(curv_h, j, k, ll)
        return -sp.Rational(1, 2) * jh[i - 1]

    Ch_4 = build_quartic_matrix(jach_coeff)

    def degree4_coeff(i, j, k, ll):
        jh = jac_h(curv_h, j, k, ll)
        jm = jac_m(T, j, k, ll)
        combo = jh + sp.Rational(9, 4) * jm
        return -sp.Rational(1, 2) * combo[i - 1]

    degree4_term = build_quartic_matrix(degree4_coeff)

    Ls = {}
    for k in range(1, 9):
        cols = [su3_action(k, unit_vec(i)) for i in range(DIM)]
        Ls[k] = sp.Matrix.hstack(*cols)
    Casimir_su3 = sp.simplify(sum((-(Ls[k] * Ls[k]) for k in range(1, 9)), sp.zeros(DIM, DIM)))
    Swap = build_swap()

    print("\n" + "=" * 70)
    print("STEP A: verify Ch_4 and degree4_term are SU(3)-equivariant,")
    print("Swap-symmetric, and Hermitian (real symmetric) -- Round 28's")
    print("theorem premise, checked DIRECTLY on these two objects")
    print("=" * 70)
    for name, M in [("Ch_4", Ch_4), ("degree4_term", degree4_term)]:
        su3_ok = all(sp.simplify(M * Ls[k] - Ls[k] * M) == sp.zeros(DIM, DIM) for k in range(1, 9))
        swap_ok = sp.simplify(M * Swap - Swap * M) == sp.zeros(DIM, DIM)
        # .H (conjugate-transpose), not .T -- genuine Hermiticity check, matching
        # the convention g2su3_round26_jach_derivation.py already uses (post-
        # skeptic fix: the original version here used .T, mathematically
        # equivalent for these specific REAL matrices but inconsistent labeling).
        herm_ok = sp.simplify(M.H - M) == sp.zeros(DIM, DIM)
        print(
            f"  {name}: SU(3)-equivariant={su3_ok}, Swap-symmetric={swap_ok}, Hermitian={herm_ok}"
        )
        assert su3_ok, f"{name} is NOT SU(3)-equivariant -- STEP A premise fails"
        assert swap_ok, f"{name} is NOT Swap-symmetric -- STEP A premise fails"
        assert herm_ok, f"{name} is NOT Hermitian -- STEP A premise fails"
    print("  => Round 28's 3-dim-space theorem applies DIRECTLY to both.")

    print("\n" + "=" * 70)
    print("STEP A': defense-in-depth -- re-verify Casimir_su3's own degree")
    print("decomposition (Id + X/3, Round 29/30) directly in THIS script,")
    print("not merely cited, closing a skeptic-recommended hardening gap")
    print("=" * 70)
    X1234 = sp.zeros(DIM, DIM)

    def unit_vec_local(i):
        v = sp.zeros(DIM, 1)
        v[i] = 1
        return v

    for a, b, c, d in [(1, 2, 3, 4), (1, 2, 5, 6), (3, 4, 5, 6)]:
        from g2su3_explicit_clifford import e_action

        cols = [
            e_action(a, e_action(b, e_action(c, e_action(d, unit_vec_local(i)))))
            for i in range(DIM)
        ]
        X1234 += sp.Matrix.hstack(*cols)
    cas_trace_part = sp.simplify(sp.trace(Casimir_su3) / DIM)
    cas_minus_scalar = sp.simplify(Casimir_su3 - cas_trace_part * Id8)
    x_over_3_matches = sp.simplify(cas_minus_scalar - X1234 / 3) == sp.zeros(DIM, DIM)
    print(f"  Casimir_su3's own trace/{DIM} (degree-0 coefficient) = {cas_trace_part}")
    print(
        f"  Casimir_su3 - (scalar part) == X/3 exactly (X:=Z1234+Z1256+Z3456)? {x_over_3_matches}"
    )
    assert cas_trace_part == 1, f"Casimir_su3's degree-0 coefficient={cas_trace_part}, expected 1"
    assert x_over_3_matches, (
        "Casimir_su3's non-scalar part is NOT exactly X/3 -- load-bearing premise fails"
    )
    print("  => Casimir_su3 = Id + X/3 independently re-confirmed HERE, not")
    print("  merely cited from Round 29/30.")

    print("\n" + "=" * 70)
    print("STEP B: solve Round 28's own 3x3 system for Ch_4/degree4_term's")
    print("own (a,b,c) coordinates in {H,Id,Casimir_su3}. Given STEP A/A'")
    print("(H purely degree-3, Ch_4/degree4_term purely degree-4, Casimir_su3")
    print("purely degree-{0,4}), a=0 and b=-c are STRUCTURALLY FORCED --")
    print("not merely 'predicted': a solve returning a!=0 or b+c!=0 would")
    print("DISPROVE one of these premises, not just miss a guess. Solve below")
    print("confirms the forced values, it does not merely check a guess.")
    print("=" * 70)
    coord_rows = [(0, 0), (0, 7), (1, 1)]
    Basis_mat = sp.Matrix([[H[r, c], Id8[r, c], Casimir_su3[r, c]] for (r, c) in coord_rows])
    det = Basis_mat.det()
    print(f"  (Basis determinant, re-confirming Round 28's {{Id,Casimir_su3,H}} basis: {det})")
    assert det != 0, "STEP B: {Id,Casimir_su3,H} is not a basis -- cannot solve uniquely"

    forced_values_confirmed = True
    for name, M in [("Ch_4", Ch_4), ("degree4_term", degree4_term)]:
        rhs = sp.Matrix([M[r, c] for (r, c) in coord_rows])
        a, b, c = Basis_mat.solve(rhs)
        recon = a * H + b * Id8 + c * Casimir_su3
        full_match = sp.simplify(recon - M) == sp.zeros(DIM, DIM)
        print(
            f"  {name}: a(H)={a}, b(Id)={b}, c(Casimir_su3)={c}  "
            f"[full 64-entry reconstruction exact? {full_match}]"
        )
        assert full_match, f"{name}: solved (a,b,c) does not reconstruct the full matrix"
        if a != 0 or sp.simplify(b + c) != 0:
            forced_values_confirmed = False
            print(f"    STRUCTURAL PREMISE VIOLATED for {name}: expected a=0, b=-c")
        else:
            print(f"    STRUCTURALLY-FORCED VALUES CONFIRMED: a=0 (no H component), b=-c={-c}")
    assert forced_values_confirmed, (
        "STEP B: the structurally-forced values (a=0, b=-c) failed for at least one object "
        "-- this would mean one of STEP A/A's premises (SU(3)-equivariance, Swap-symmetry, "
        "H's pure degree-3 nature, or Casimir_su3=Id+X/3) is actually false"
    )

    print("\n" + "=" * 70)
    print("STEP C: conclude Ch_4, degree4_term are FORCED proportional to")
    print("(Casimir_su3 - Id) = X/3 -- explaining WHY their support is")
    print("confined to X's own 3 pair-partition quadruples, with an")
    print("automatically EQUAL coefficient across all three")
    print("=" * 70)
    for name, M in [("Ch_4", Ch_4), ("degree4_term", degree4_term)]:
        rhs = sp.Matrix([M[r, c] for (r, c) in coord_rows])
        _, _, c = Basis_mat.solve(rhs)
        recon_via_X = sp.simplify(c * (Casimir_su3 - Id8))
        match = sp.simplify(recon_via_X - M) == sp.zeros(DIM, DIM)
        print(f"  {name} == {c}*(Casimir_su3 - Id) exactly? {match}")
        assert match, f"{name} is not exactly proportional to (Casimir_su3-Id)"

    print("\n" + "=" * 70)
    print("STEP D (bonus, PARTIALLY structural): re-derive Round 30's")
    print("Ch_tilde=Casimir_su3 via a cleaner route. CAVEAT: this plugs in")
    print("Ch_4's own SOLVED c=1 from STEP B (a computed fact, not derived")
    print("purely from degree-counting) -- Ch_0=1 (established) +")
    print("Ch_4=Casimir_su3-Id (c=1 plugged in) => Ch_tilde =")
    print("Id+(Casimir_su3-Id) = Casimir_su3. NOT a from-scratch structural")
    print("re-derivation of the constant -- see docstring BONUS section.")
    print("=" * 70)
    Qh_sum = sp.simplify(
        2
        * sum(
            curv_h.get((i, j, k), 0) ** 2
            for i in range(1, 7)
            for j in range(i + 1, 7)
            for k in range(1, 9)
        )
    )
    Ch_0 = sp.Rational(1, 8) * Qh_sum
    Ch_tilde = sp.simplify(Ch_0 * Id8 + Ch_4)
    print(f"  Ch_0 = {Ch_0}")
    ch_tilde_eq_cas = sp.simplify(Ch_tilde - Casimir_su3) == sp.zeros(DIM, DIM)
    print(f"  Ch_tilde == Casimir_su3 (Round 30's finding, re-derived here)? {ch_tilde_eq_cas}")
    assert ch_tilde_eq_cas, "STEP D: the bonus re-derivation of Round 30's finding failed"

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("  WHY only 3 of 15 index-quadruples are ever nonzero in")
    print("  jach_coeff/degree4_coeff: because Ch_4/degree4_term are")
    print("  SU(3)-equivariant + Swap-symmetric (STEP A) -- forcing them,")
    print("  by Round 28's OWN 3-dim-space theorem, into span{Id,")
    print("  Casimir_su3, H} -- AND purely degree-4 by construction (zero")
    print("  scalar/degree-3 component) -- forcing the H-coefficient to 0")
    print("  and the Id/Casimir_su3 coefficients to cancel at degree-0")
    print("  (STEP B, confirmed exactly for both objects). This leaves")
    print("  ONLY a multiple of (Casimir_su3-Id)=X/3 -- whose support IS")
    print("  exactly the 3 pair-partition quadruples (Round 29). This is")
    print("  a NECESSARY CONSEQUENCE, not a coincidence of index")
    print("  gymnastics -- closing Round 31's own flagged open question.")
    print()
    print("  HONEST LIMIT: this explains the SUPPORT (which 3 quadruples,")
    print("  why equal across them) but NOT the SPECIFIC proportionality")
    print("  constant (e.g. Ch_4's own c=1) -- that still requires the")
    print("  direct combinatorial computation from Rounds 26/29/31/32.")


if __name__ == "__main__":
    main()
    print("\nEXIT=0")
