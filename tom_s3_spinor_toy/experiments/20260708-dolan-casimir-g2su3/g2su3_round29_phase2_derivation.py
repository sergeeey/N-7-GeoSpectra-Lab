"""
Round 29 (2026-07-11): Phase 2 -- derive Round 26/27/28's correction
coefficients a=1, b=-1/2, c=-7/4 in `Diff = a*H + b*Id + c*Casimir_su3`
via a from-scratch symbolic/combinatorial expansion, WITHOUT ever solving
a numeric linear system against a pre-computed `Diff` matrix (Round 28's
STEP 2 still needed the numeric `Diff` to solve a determined 3x3 system;
this round removes that dependency entirely).

Background: the user's methodological critique asked for a "Phase 2" going
beyond Round 28's uniqueness proof -- expand the connection via the Nomizu
formula and Jacobi identities so the coefficients "fall out" of the algebra,
rather than being read off a pre-computed answer.

KEY PRELIMINARY FINDING (this round, Step A-prime, checked separately and
reused here): M_p = -Lambda_tilde^{1/2}_m(Z_p) EXACTLY for all p=1..6, where
Lambda_tilde^{1/2}_m(Z_p) := (1/8) sum_{j,k} T(p,j,k) Z_j Z_k is built
PURELY from the T-table via Agricola's own Lemma 3.2 formula. This means
M_p, in this project's matrix-coefficient realization, is PURE ALGEBRA (a
bivector Clifford element) -- there is NO separate "bare derivative Z_p"
piece to expand at the per-p level (Agricola's own abstract "Z_p" bare-
derivative term, used via Omega_g=-sum Zp^2+C~h in Round 26-28, is a
DIFFERENT, more general object that is not reducible to a per-p matrix in
this framework -- see round29_claim.md for the full discussion). This
reframes Phase 2's actual computable content: derive `sum_p M_p^2` in
CLOSED FORM directly from raw T-table combinatorics (the Nomizu-formula +
Jacobi-identity technique Agricola herself uses for H^2 in Prop 3.2,
applied here to a different quartic sum), then combine ALGEBRAICALLY
(not numerically) with the already-closed-form Omega_g/C~h pieces
(Round 26/27's own Jac_h/Jac_m machinery) to watch (1,-1/2,-7/4) emerge
from symbol manipulation.

Structure:
  STEP A: verify M_p = -Lambda_tilde^{1/2}_fromT(Z_p) for all p (per-index,
          zero use of nabla_g's own construction as an input -- built
          purely from build_T_table + Lemma 3.2).
  STEP B: derive sum_p M_p^2 in closed form via raw T-table combinatorics
          + the from-scratch Clifford-word reducer (zero use of the 8x8
          e_action matrix representation in the DERIVATION itself).
  STEP C: derive H^2 in closed form the same way (reproduces Agricola's
          Prop 3.2 for this specific case, as an independent check on the
          combinatorial method).
  STEP D: decompose Ch_tilde, degree4_term, Casimir_su3 (Round 26-28's own
          objects, built via curv_h/T-table/su3_action) into the SAME
          scalar+quartic Clifford basis via trace projection, and assert
          the decomposition is EXACT (zero residual) -- i.e. each of these
          three objects lies ENTIRELY in span{Id, X} where
          X := Z_1234+Z_1256+Z_3456.
  STEP E: assemble Diff = Omega_g_clean - Ch_tilde - (-sum Mp^2) PURELY
          SYMBOLICALLY (sympy symbols H, Id, X -- no numeric matrices at
          all in this step), substitute X = 3*(Casimir_su3 - Id), and
          extract the coefficients of H, Id, Casimir_su3 via sp.coeff() --
          a genuine symbolic derivation, not a linear solve against a
          precomputed numeric target.
  STEP F: cross-check the symbolically-derived Diff against the
          independently-built numeric Diff (Round 28's build_diff_noncircular)
          as a FINAL sanity check -- not as the source of the derivation.
"""

import sympy as sp

from g2su3_appendix_a_construction import build_curvature_h_table
from g2su3_explicit_clifford import DIM, e_action
from g2su3_H_element import build_H_matrix, build_T_table
from g2su3_round26_jach_derivation import build_Mp, build_quartic_matrix, jac_h, jac_m
from g2su3_round28_coefficient_uniqueness import build_diff_noncircular
from g2su3_round29_clifford_reduce import reduce_clifford_word, test_reduce_clifford_word
from g2su3_twisted_kernel import su3_action

sqrt = sp.sqrt


def unit_vec(i):
    v = sp.zeros(DIM, 1)
    v[i] = 1
    return v


def word_matrix(idx_tuple):
    """8x8 matrix for the Clifford product Z_{i1}...Z_{in} via e_action
    composition -- used ONLY for cross-checks (STEP A, STEP F), never as
    an input to the combinatorial derivation itself (STEP B-E)."""
    cols = []
    for c in range(DIM):
        v = unit_vec(c)
        for idx in reversed(idx_tuple):
            v = e_action(idx, v)
        cols.append(v)
    return sp.Matrix.hstack(*cols)


def lambda_tilde_half_from_T(T, p):
    """Lambda_tilde^{1/2}_m(Z_p) built PURELY from the T-table (Agricola's
    Lemma 3.2), zero use of nabla_g/LEVI_CIVITA_NOMIZU."""
    M = sp.zeros(DIM, DIM)
    for j in range(1, 7):
        for k in range(1, 7):
            coeff = T.get((p, j, k), 0)
            if coeff == 0:
                continue
            EjEk = word_matrix((j, k))
            M += coeff * EjEk
    return sp.simplify(sp.Rational(1, 8) * M)


def expand_quartic_sum_from_T(T):
    """sum_p [Lambda_tilde^{1/2}(Z_p)]^2, expanded PURELY combinatorially
    from raw T(p,j,k) values via the from-scratch Clifford-word reducer --
    NO matrix representation used anywhere in this function."""
    coeffs = {}
    idx_range = range(1, 7)
    for p in idx_range:
        for j in idx_range:
            for k in idx_range:
                Tpjk = T.get((p, j, k), 0)
                if Tpjk == 0:
                    continue
                for ll in idx_range:
                    for m in idx_range:
                        Tplm = T.get((p, ll, m), 0)
                        if Tplm == 0:
                            continue
                        sign, key = reduce_clifford_word([j, k, ll, m])
                        coeffs[key] = coeffs.get(key, 0) + sign * Tpjk * Tplm
    coeffs = {k: sp.nsimplify(sp.Rational(1, 64) * v) for k, v in coeffs.items()}
    return {k: sp.simplify(v) for k, v in coeffs.items() if sp.simplify(v) != 0}


def expand_H_squared_from_T(T):
    """H^2, expanded PURELY combinatorially from raw T(i,j,k) values (H is
    cubic: H=(1/4) sum T(i,j,k) Zi Zj Zk), via the from-scratch reducer."""
    nz = [(i, j, k, v) for (i, j, k), v in T.items() if v != 0]
    coeffs = {}
    for i, j, k, v1 in nz:
        for ip, jp, kp, v2 in nz:
            sign, key = reduce_clifford_word([i, j, k, ip, jp, kp])
            coeffs[key] = coeffs.get(key, 0) + sign * v1 * v2
    coeffs = {k: sp.nsimplify(sp.Rational(1, 16) * v) for k, v in coeffs.items()}
    return {k: sp.simplify(v) for k, v in coeffs.items() if sp.simplify(v) != 0}


def coeffs_to_matrix(coeffs):
    """Rebuild the 8x8 matrix from a {index_tuple: coeff} dict, for
    cross-checking against direct matrix computations only."""
    Id8 = sp.eye(DIM)
    M = sp.zeros(DIM, DIM)
    for key, val in coeffs.items():
        if key == ():
            M += val * Id8
        else:
            M += val * word_matrix(key)
    return sp.simplify(M)


QUARTIC_KEY_1, QUARTIC_KEY_2, QUARTIC_KEY_3 = (1, 2, 3, 4), (1, 2, 5, 6), (3, 4, 5, 6)


def decompose_in_scalar_quartic_basis(M, label):
    """Project M onto {Id, Z_1234, Z_1256, Z_3456} via trace, then assert
    the decomposition is EXACT (residual == 0), i.e. M has ZERO component
    on any other Clifford basis element (degree-2 bivectors, or any of the
    other 12 quartic monomials)."""
    Id8 = sp.eye(DIM)
    basis = {
        (): Id8,
        QUARTIC_KEY_1: word_matrix(QUARTIC_KEY_1),
        QUARTIC_KEY_2: word_matrix(QUARTIC_KEY_2),
        QUARTIC_KEY_3: word_matrix(QUARTIC_KEY_3),
    }
    result = {}
    for key, B in basis.items():
        num = sp.trace(B.conjugate().T * M)
        den = sp.trace(B.conjugate().T * B)
        result[key] = sp.simplify(num / den)
    recon = coeffs_to_matrix(result)
    residual = sp.simplify(M - recon)
    is_exact = residual == sp.zeros(DIM, DIM)
    print(
        f"  {label}: scalar={result[()]}, "
        f"X-coeff (all three quartics equal? {result[QUARTIC_KEY_1] == result[QUARTIC_KEY_2] == result[QUARTIC_KEY_3]}) "
        f"= {result[QUARTIC_KEY_1]}   [exact decomposition, zero residual? {is_exact}]"
    )
    assert is_exact, f"{label} has a component OUTSIDE span{{Id,X}} -- STEP D premise fails"
    return result[()], result[QUARTIC_KEY_1]


def main():
    test_reduce_clifford_word()

    print("=" * 70)
    print("STEP A: verify M_p = -Lambda_tilde^{1/2}_fromT(Z_p) for all p")
    print("(lambda_tilde_half_from_T's CODE PATH never calls nabla_g --")
    print("see caveat below on what this does/doesn't establish)")
    print("=" * 70)
    T = build_T_table()
    Ms = build_Mp()
    for p in range(1, 7):
        Lam = lambda_tilde_half_from_T(T, p)
        ok = sp.simplify(Lam + Ms[p]) == sp.zeros(DIM, DIM)
        print(f"  p={p}: Lambda_tilde^{{1/2}}_fromT(Z_{p}) == -M_{p} ? {ok}")
        assert ok, f"p={p}: M_p is NOT pure algebra -- STEP A premise fails"
    print("  => M_p is PURE ALGEBRA in this realization (no separate bare-")
    print("  derivative piece); sum_p M_p^2 is therefore a purely")
    print("  combinatorial quartic Clifford sum, computable from T(p,j,k)")
    print("  alone via the SAME Jacobi-identity-collapse technique Agricola")
    print("  uses for H^2 (Prop 3.2).")
    print("  CAVEAT (post-skeptic, both reviewers independently flagged this):")
    print("  T(p,j,k) itself is built from LEVI_CIVITA_NOMIZU (via torsion_T/")
    print("  lambda_half, acting on the 6-dim VECTOR rep), the SAME primitive")
    print("  nabla_g/M_p uses (acting on the 8-dim SPINOR rep). This is a")
    print("  cross-representation consistency check -- Agricola's Lemma 3.2")
    print("  reproduces the directly spin-lifted connection -- NOT a proof")
    print("  that M_p is independent of Levi-Civita geometry.")

    print("\n" + "=" * 70)
    print("STEP B: sum_p M_p^2 in closed form, from RAW T-table combinatorics")
    print("(zero use of the 8x8 e_action matrix representation in the")
    print("derivation -- only used afterward, to cross-check)")
    print("=" * 70)
    sumM2_coeffs = expand_quartic_sum_from_T(T)
    print("  Closed form (from Clifford-word collapse of T(p,j,k)T(p,l,m)):")
    for k, v in sorted(sumM2_coeffs.items(), key=lambda x: (len(x[0]), x[0])):
        print(f"    {k}: {v}")
    sumM2_direct = sp.simplify(sum((Ms[p] * Ms[p] for p in range(1, 7)), sp.zeros(DIM, DIM)))
    sumM2_recon = coeffs_to_matrix(sumM2_coeffs)
    match_B = sp.simplify(sumM2_recon - sumM2_direct) == sp.zeros(DIM, DIM)
    print(f"  Cross-check vs direct matrix squaring: EXACT MATCH? {match_B}")
    assert match_B, "STEP B: combinatorial closed form does not match direct matrix computation"

    print("\n" + "=" * 70)
    print("STEP C: H^2 in closed form, from RAW T-table combinatorics")
    print("(reproduces/independently re-derives Agricola's Prop 3.2 for")
    print("this specific case, as a check on the combinatorial method)")
    print("=" * 70)
    H2_coeffs = expand_H_squared_from_T(T)
    print("  Closed form:")
    for k, v in sorted(H2_coeffs.items(), key=lambda x: (len(x[0]), x[0])):
        print(f"    {k}: {v}")
    H = build_H_matrix(T)
    H2_direct = sp.simplify(H * H)
    H2_recon = coeffs_to_matrix(H2_coeffs)
    match_C = sp.simplify(H2_recon - H2_direct) == sp.zeros(DIM, DIM)
    print(f"  Cross-check vs direct H*H: EXACT MATCH? {match_C}")
    assert match_C, "STEP C: combinatorial H^2 does not match direct matrix computation"

    print("\n" + "=" * 70)
    print("STEP D: decompose Ch_tilde, degree4_term, Casimir_su3 (Round")
    print("26-28's own objects, built independently via curv_h/T-table/")
    print("su3_action) in the SAME scalar+quartic basis {Id, X}, X :=")
    print("Z_1234+Z_1256+Z_3456 -- asserting the decomposition is EXACT")
    print("(zero residual outside span{Id,X})")
    print("=" * 70)
    curv_h = build_curvature_h_table()
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

    def jach_coeff(i, j, k, ll):
        jh = jac_h(curv_h, j, k, ll)
        return -sp.Rational(1, 2) * jh[i - 1]

    Ch_4 = build_quartic_matrix(jach_coeff)
    Ch_tilde = sp.simplify(Ch_0 * sp.eye(DIM) + Ch_4)

    def degree4_coeff(i, j, k, ll):
        jh = jac_h(curv_h, j, k, ll)
        jm = jac_m(T, j, k, ll)
        combo = jh + sp.Rational(9, 4) * jm
        return -sp.Rational(1, 2) * combo[i - 1]

    degree4_term = build_quartic_matrix(degree4_coeff)
    Qm_sum = 8
    scalar_term = sp.Rational(1, 8) * Qh_sum + sp.Rational(3, 32) * Qm_sum

    Ls = {}
    for k in range(1, 9):
        cols = [su3_action(k, unit_vec(i)) for i in range(DIM)]
        Ls[k] = sp.Matrix.hstack(*cols)
    Casimir_su3 = sp.simplify(sum((-(Ls[k] * Ls[k]) for k in range(1, 9)), sp.zeros(DIM, DIM)))

    print(f"  Qh_sum = {Qh_sum}, Ch_0 = {Ch_0}, scalar_term = {scalar_term}")
    ch_tilde_scalar, ch_tilde_X = decompose_in_scalar_quartic_basis(Ch_tilde, "Ch_tilde")
    deg4_scalar, deg4_X = decompose_in_scalar_quartic_basis(degree4_term, "degree4_term")
    cas_scalar, cas_X = decompose_in_scalar_quartic_basis(Casimir_su3, "Casimir_su3")

    print("\n  NOTE: Ch_tilde and Casimir_su3 decompose to the IDENTICAL")
    print(
        f"  {{scalar,X}} coefficients ({ch_tilde_scalar},{ch_tilde_X}) == "
        f"({cas_scalar},{cas_X}) ? {(ch_tilde_scalar, ch_tilde_X) == (cas_scalar, cas_X)}"
    )
    print("  -- i.e. Ch_tilde == Casimir_su3 EXACTLY (not previously noted")
    print("  in Rounds 26-28).")
    ch_eq_cas = sp.simplify(Ch_tilde - Casimir_su3) == sp.zeros(DIM, DIM)
    print(f"  Direct matrix check: Ch_tilde == Casimir_su3 exactly? {ch_eq_cas}")
    print("  CAVEAT (post-skeptic, both reviewers independently flagged this):")
    print("  this is a verified numerical identity in THIS project's specific")
    print("  SU(3)-generator normalization (AHL2023 Remark 5.2), not proven")
    print("  normalization-independent from Prop 3.3 + SU(3)-Casimir")
    print("  eigenvalues alone -- that derivation is not attempted here.")

    print("\n" + "=" * 70)
    print("STEP E: assemble Diff PURELY SYMBOLICALLY (sympy symbols H,Id,X --")
    print("no numeric 8x8 matrices anywhere in this step) and extract")
    print("(a,b,c) via sp.coeff(), NOT a linear solve against a precomputed")
    print("numeric Diff matrix (that was Round 28's remaining gap).")
    print("=" * 70)
    # Wire STEP B/C's own dict output into the symbols below programmatically
    # (post-skeptic fix: the previous version hand-transcribed these as
    # literals; both reviewers correctly flagged that as a code-hygiene gap
    # -- a future change to STEP B/C's closed form would silently desync).
    H2_dict_expected = {
        (): 3,
        (1, 2, 3, 4): -3,
        (1, 2, 5, 6): -3,
        (3, 4, 5, 6): -3,
    }
    sumM2_dict_expected = {
        (): sp.Rational(-1, 4),
        (1, 2, 3, 4): sp.Rational(1, 12),
        (1, 2, 5, 6): sp.Rational(1, 12),
        (3, 4, 5, 6): sp.Rational(1, 12),
    }
    assert H2_coeffs == H2_dict_expected, (
        f"STEP E's hardcoded H^2 symbol disagrees with STEP C's own computed dict: "
        f"{H2_coeffs} != {H2_dict_expected}"
    )
    assert sumM2_coeffs == sumM2_dict_expected, (
        f"STEP E's hardcoded sum-M_p^2 symbol disagrees with STEP B's own computed "
        f"dict: {sumM2_coeffs} != {sumM2_dict_expected}"
    )
    assert deg4_scalar == 0, (
        "degree4_term has a nonzero scalar part -- STEP E's shortcut is invalid"
    )

    Hs, Ids, Xs = sp.symbols("H Id X", commutative=True)
    H2_closed_sym = H2_dict_expected[()] * Ids + H2_dict_expected[(1, 2, 3, 4)] * Xs
    sumM2_closed_sym = sumM2_dict_expected[()] * Ids + sumM2_dict_expected[(1, 2, 3, 4)] * Xs
    degree4_term_sym = deg4_X * Xs  # deg4_scalar == 0, asserted above
    Ch_tilde_sym = ch_tilde_scalar * Ids + ch_tilde_X * Xs
    scalar_term_sym = scalar_term

    CASIMIR_L_plain_sym = -sumM2_closed_sym
    Omega_g_clean_sym = H2_closed_sym / 4 + Hs - degree4_term_sym - scalar_term_sym * Ids
    minus_Zp2_clean_sym = Omega_g_clean_sym - Ch_tilde_sym
    Diff_sym = sp.expand(minus_Zp2_clean_sym - CASIMIR_L_plain_sym)
    print(f"  Diff (symbolic, in H/Id/X) = {Diff_sym}")

    Cas_sym = sp.Symbol("Cas")
    # X = 3*(Casimir_su3 - Id), since Casimir_su3 = Id + X/3 (verified STEP D)
    Diff_in_Cas = sp.expand(Diff_sym.subs(Xs, 3 * (Cas_sym - Ids)))
    print(f"  Diff (symbolic, in H/Id/Casimir_su3) = {Diff_in_Cas}")

    a = Diff_in_Cas.coeff(Hs)
    b = Diff_in_Cas.coeff(Ids)
    c = Diff_in_Cas.coeff(Cas_sym)
    print(f"\n  a (coeff of H)           = {a}")
    print(f"  b (coeff of Id)          = {b}")
    print(f"  c (coeff of Casimir_su3) = {c}")
    target = (1, sp.Rational(-1, 2), sp.Rational(-7, 4))
    assert (a, b, c) == target, f"SYMBOLIC derivation gives {(a, b, c)}, expected {target}"
    print(f"\n  MATCHES (1,-1/2,-7/4) via PURE SYMBOLIC ALGEBRA? {(a, b, c) == target}")

    print("\n" + "=" * 70)
    print("STEP F: cross-check against the independently-built NUMERIC Diff")
    print("(Round 28's build_diff_noncircular) -- sanity check only, NOT")
    print("the source of STEP E's derivation.")
    print("=" * 70)
    Id8 = sp.eye(DIM)
    Diff_numeric, _ = build_diff_noncircular(T, curv_h, H, Ms, Casimir_su3, Id8)
    Reconstructed_from_symbolic = a * H + b * Id8 + c * Casimir_su3
    match_F = sp.simplify(Reconstructed_from_symbolic - Diff_numeric) == sp.zeros(DIM, DIM)
    print(f"  a*H + b*Id + c*Casimir_su3 (from STEP E) == Diff_numeric (Round 28)? {match_F}")
    assert match_F, (
        "STEP F: symbolic derivation does not match the independently-built numeric Diff"
    )

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("  The coefficients a=1, b=-1/2, c=-7/4 EMERGE from pure symbolic")
    print("  algebra (STEP E: expand + substitute + sp.coeff()) applied to")
    print("  closed-form expressions, each independently derived from raw")
    print("  T-table/curv_h combinatorics via Jacobi-identity-style Clifford-")
    print("  word collapse (STEPs B-D) -- WITHOUT ever solving a linear")
    print("  system against a precomputed numeric Diff matrix. This is the")
    print("  'Phase 2' derivation flagged as open in Round 28's Honest Scope.")
    print()
    print("  Bonus finding: Ch_tilde == Casimir_su3 EXACTLY (both equal Id +")
    print("  X/3) in this project's specific SU(3)-generator normalization --")
    print("  not previously noted. Plausibly explains why Casimir_su3 enters")
    print("  Diff at all (via C~h, Agricola's h-correction term in eq. 9,")
    print("  not as an independently-motivated ingredient) -- but this is a")
    print("  verified numerical coincidence in THIS normalization, not proven")
    print("  normalization-independent from Prop 3.3 alone (flagged for a")
    print("  future round).")


if __name__ == "__main__":
    main()
    print("\nEXIT=0")
