"""
NOTE (label only, 2026-08-10): "Cl(7,0)" throughout this file should read
Cl(0,7) -- the generators it refers to square to -1. Naming inversion only,
no result affected. See docs/clifford_convention_registry.md.

Round 32 (2026-07-11): eliminate the LAST remaining 8x8 Clifford-matrix
construction Round 31 left untouched -- `build_curvature_h_table()`'s
own Cl(7,0)-side machinery (`RHO`/`NU` matrix products, `bracket_e`
matrix commutator, `decompose_g2`'s `Tr(nu_k.T*M)` trace-projection,
g2su3_appendix_a_construction.py, unchanged since Round 13).

Motivation: Round 31 closed the `build_quartic_matrix`+trace-projection
pattern for `Ch_tilde`/`degree4_term` (given `curv_h` as an input), but
both FL Step 8a skeptics independently found that `curv_h` ITSELF is
still built via 8x8 matrices upstream (`build_curvature_h_table()`,
called in STEP A) -- flagged in round31_claim.md's "What this does NOT
mean" as unaddressed. This round addresses it directly, by user request
("Довести build_curvature_h_table до комбинаторики").

KEY OBSERVATION: `e(p) := E_SIGN[p]*nu(8+p)` and `nu(k)` (k=1..14) are
ALREADY, by construction (g2su3_appendix_a_construction.py's own NU
dict), LINEAR COMBINATIONS of Cl(7,0) BIVECTORS `rho(a)*rho(b)` (a<b)
with EXPLICIT rational coefficients -- e.g. `nu_1 = (1/4)*(rho1*rho2 -
rho5*rho6)`. This is EXACTLY the same type of object Round 29's
Clifford-word reducer (`g2su3_round29_clifford_reduce.py`) was built to
manipulate combinatorially, just for a DIFFERENT Clifford algebra (7
generators here, Cl(7,0), vs 6 generators for Sigma=Lambda*(C^3) there).
`reduce_clifford_word` is fully generic (works for any number of
generators, using only Z_i^2=-1 and Z_iZ_j=-Z_jZ_i) -- reused UNCHANGED.

Two combinatorial primitives replace the matrix operations:
  1. COMMUTATOR: [X,Y] for two bivector-combinations X=sum c_a e_a,
     Y=sum c_b e_b, computed via `reduce_clifford_word` on each 4-index
     product e_a*e_b (both orders), entirely index-based -- replaces
     `bracket_e(p,q) = e(p)*e(q)-e(q)*e(p)` (an 8x8 matrix commutator).
  2. TRACE-PROJECTION AS A DOT PRODUCT: since {e_S}_{|S|=2} (bivector
     basis elements) satisfy Tr(e_S^T e_T) = 8 if S=T, else 0 (VERIFIED
     below, STEP A, against direct 8x8 matrix computation on all 21
     bivector pairs of Cl(7,0) -- a genuinely checkable fact, not
     assumed), `Tr(nu_k^T * M)` for M a bivector-combination reduces to
     `8 * sum_{(a,b)} [nu_k's coeff on (a,b)] * [M's coeff on (a,b)]` --
     a pure combinatorial dot product over EXPLICIT coefficient lists,
     zero matrix trace needed. Replaces `decompose_g2`.

Structure:
  STEP A: verify the trace primitive `Tr(e_S^T e_S)=8`, `Tr(e_S^T
          e_T)=0` (S!=S) directly against 8x8 matrices (RHO-built) --
          this IS a matrix computation, but it is a ONE-TIME, GENERAL
          primitive-verification step, not part of the per-(p,q,k)
          derivation loop itself.
  STEP B: transcribe e(p)/nu(k) (k=1..14) as {(a,b):coeff} bivector
          dicts DIRECTLY from the NU dict's own literal source (verbatim
          transcription, self-tested against the matrix e(p)/nu(k) for
          exact agreement).
  STEP C: compute [e(p),e(q)] combinatorially (STEP A's reducer, zero
          matrix ops) for all 15 (p,q) pairs; verify the commutator
          collapses to PURE bivector terms (no scalar/quartic residual)
          -- a genuine structural check, not assumed.
  STEP D: extract curv_h(p,q,k) for k=1..8 via the combinatorial dot-
          product formula (STEP A's primitive), for all (p,q,k) -- zero
          matrix construction anywhere in this step.
  STEP E: cross-check the FULL combinatorially-rebuilt curv_h table
          against the existing matrix-based `build_curvature_h_table()`
          -- exact match required, all entries.
  STEP F: feed the combinatorially-rebuilt curv_h into Round 31's own
          downstream pipeline (jach_coeff/degree4_coeff -> symbolic
          Diff assembly) to re-derive (1,-1/2,-7/4) -- now with curv_h
          ITSELF also matrix-free, closing Round 31's own flagged gap.
"""

import itertools

import sympy as sp

from g2su3_appendix_a_construction import RHO, build_curvature_h_table
from g2su3_H_element import build_T_table
from g2su3_round28_coefficient_uniqueness import build_diff_noncircular
from g2su3_round29_clifford_reduce import reduce_clifford_word
from g2su3_round29_phase2_derivation import (
    expand_H_squared_from_T,
    expand_quartic_sum_from_T,
)
from g2su3_round31_full_combinatorial_derivation import (
    PAIR_PARTITION_QUADS,
    degree4_coeff,
    jach_coeff,
)
from g2su3_twisted_kernel import su3_action
from g2su3_explicit_clifford import DIM

sqrt = sp.sqrt
BRACKET_SIGN = -1  # matches g2su3_appendix_a_construction.py's own established convention

# NU dict, transcribed VERBATIM from g2su3_appendix_a_construction.py's own
# NU={...} literal (k: (overall_coeff, [(sign,a,b), ...])). Re-derived here
# independently as a {(a,b):coeff} representation for combinatorial use --
# self-tested (STEP B) against the matrix nu(k)/e(p) for exact agreement.
NU_BIVEC_SOURCE = {
    1: (sp.Rational(1, 4), [(1, 1, 2), (-1, 5, 6)]),
    2: (sp.Rational(1, 4), [(1, 3, 5), (1, 4, 6)]),
    3: (sp.Rational(1, 4), [(1, 3, 6), (-1, 4, 5)]),
    4: (sp.Rational(1, 4), [(1, 1, 3), (1, 2, 4)]),
    5: (sp.Rational(1, 4), [(1, 1, 4), (-1, 2, 3)]),
    6: (sp.Rational(1, 4), [(1, 1, 5), (1, 2, 6)]),
    7: (sp.Rational(1, 4), [(1, 1, 6), (-1, 2, 5)]),
    8: (sp.Rational(1, 4) / sqrt(3), [(-1, 1, 2), (2, 3, 4), (-1, 5, 6)]),
    9: (sp.Rational(1, 4) / sqrt(3), [(2, 1, 7), (-1, 3, 6), (-1, 4, 5)]),
    10: (sp.Rational(1, 4) / sqrt(3), [(2, 2, 7), (-1, 3, 5), (1, 4, 6)]),
    11: (sp.Rational(1, 4) / sqrt(3), [(1, 1, 3), (-1, 2, 4), (-2, 6, 7)]),
    12: (sp.Rational(1, 4) / sqrt(3), [(1, 1, 4), (1, 2, 3), (-2, 5, 7)]),
    13: (sp.Rational(1, 4) / sqrt(3), [(1, 1, 5), (-1, 2, 6), (2, 4, 7)]),
    14: (sp.Rational(1, 4) / sqrt(3), [(1, 1, 6), (1, 2, 5), (2, 3, 7)]),
}
E_SIGN = {1: 1, 2: 1, 3: -1, 4: 1, 5: -1, 6: 1}


def nu_bivec_dict(k):
    """{(a,b): coeff} for nu_k, a<b, built from NU_BIVEC_SOURCE alone."""
    coeff0, terms = NU_BIVEC_SOURCE[k]
    d = {}
    for sign, a, b in terms:
        key = (a, b) if a < b else (b, a)
        val = sign * coeff0 if a < b else -sign * coeff0
        d[key] = d.get(key, 0) + val
    return d


def e_bivec_dict(p):
    """{(a,b): coeff} for e(p) := E_SIGN[p]*nu(8+p), p=1..6."""
    d0 = nu_bivec_dict(8 + p)
    s = E_SIGN[p]
    return {k: s * v for k, v in d0.items()}


def bivec_product_combinatorial(dict_a, dict_b):
    """(sum c_a e_a)(sum c_b e_b) via the Clifford-word reducer -- pure
    index combinatorics, zero matrix operations."""
    out = {}
    for (a1, a2), ca in dict_a.items():
        for (b1, b2), cb in dict_b.items():
            sign, key = reduce_clifford_word([a1, a2, b1, b2])
            out[key] = out.get(key, 0) + sign * ca * cb
    return out


def commutator_combinatorial(dict_a, dict_b):
    ab = bivec_product_combinatorial(dict_a, dict_b)
    ba = bivec_product_combinatorial(dict_b, dict_a)
    out = {}
    for key in set(ab) | set(ba):
        v = sp.simplify(ab.get(key, 0) - ba.get(key, 0))
        if v != 0:
            out[key] = v
    return out


def dot_product_trace(dict_m, dict_n):
    """Tr(M^T N) for bivector-combinations M,N, via the combinatorial
    primitive Tr(e_S^T e_T) = 8*delta_ST (STEP A) -- zero matrix trace."""
    keys = set(dict_m) & set(dict_n)
    return 8 * sum(dict_m[k] * dict_n[k] for k in keys)


def build_curv_h_combinatorial():
    """Rebuild {(p,q,k): coeff} (k=1..8, the h=su(3) part) entirely via
    combinatorics -- zero calls to RHO/NU matrices, bracket_e, or
    decompose_g2 anywhere in this function."""
    table = {}
    for p in range(1, 7):
        for q in range(p + 1, 7):
            comm = commutator_combinatorial(e_bivec_dict(p), e_bivec_dict(q))
            for key in comm:
                assert len(key) == 2, (
                    f"p={p},q={q}: commutator has a non-bivector residual at {key} "
                    "-- structural premise (STEP C) fails"
                )
            bracket_pq = {k: BRACKET_SIGN * v for k, v in comm.items()}
            for k in range(1, 9):
                val = sp.simplify(dot_product_trace(nu_bivec_dict(k), bracket_pq))
                if val != 0:
                    table[(p, q, k)] = val
    return table


def main():
    print("=" * 70)
    print("STEP A: verify the trace primitive Tr(e_S^T e_S)=8, Tr(e_S^T")
    print("e_T)=0 (S!=T) directly against 8x8 RHO-built matrices, for all")
    print("C(7,2)=21 bivector pairs (a one-time primitive check, not part")
    print("of the per-(p,q,k) derivation loop)")
    print("=" * 70)

    def bivec_matrix(a, b):
        return RHO[a] * RHO[b]

    pairs = list(itertools.combinations(range(1, 8), 2))
    print(f"  Number of bivector pairs (C(7,2)): {len(pairs)}")
    assert len(pairs) == 21, "expected 21 bivector pairs for Cl(7,0)"
    diag_ok = True
    for a, b in pairs:
        s = bivec_matrix(a, b)
        tr_self = sp.trace(s.T * s)
        if tr_self != 8:
            diag_ok = False
            print(f"  FAIL: Tr(e_{{{a}{b}}}^T e_{{{a}{b}}}) = {tr_self}, expected 8")
    print(f"  All 21 diagonal traces == 8? {diag_ok}")
    assert diag_ok, "STEP A: diagonal trace primitive failed"

    offdiag_ok = True
    checked = 0
    for (a, b), (c, d) in itertools.combinations(pairs, 2):
        val = sp.trace(bivec_matrix(a, b).T * bivec_matrix(c, d))
        checked += 1
        if val != 0:
            offdiag_ok = False
            print(f"  FAIL: Tr(e_{{{a}{b}}}^T e_{{{c}{d}}}) = {val}, expected 0")
    print(f"  All C(21,2)={checked} off-diagonal traces == 0? {offdiag_ok}")
    assert offdiag_ok, "STEP A: off-diagonal trace primitive failed"

    print("\n" + "=" * 70)
    print("STEP B: transcribe e(p)/nu(k) as {(a,b):coeff} bivector dicts")
    print("from the NU dict's own literal source; self-test against the")
    print("matrix e(p)/nu(k) for exact agreement (all 6 p, all 14 k)")
    print("=" * 70)
    from g2su3_appendix_a_construction import e as e_matrix
    from g2su3_appendix_a_construction import nu as nu_matrix

    def dict_to_matrix(d):
        m = sp.zeros(8, 8)
        for (a, b), c in d.items():
            m += c * RHO[a] * RHO[b]
        return m

    all_e_match = True
    for p in range(1, 7):
        recon = dict_to_matrix(e_bivec_dict(p))
        ok = sp.simplify(recon - e_matrix(p)) == sp.zeros(8, 8)
        if not ok:
            all_e_match = False
        print(f"  e({p}) dict reconstructs matrix exactly? {ok}")
    assert all_e_match, "STEP B: e(p) bivector-dict transcription does not match e(p) matrix"

    all_nu_match = True
    for k in range(1, 15):
        recon = dict_to_matrix(nu_bivec_dict(k))
        ok = sp.simplify(recon - nu_matrix(k)) == sp.zeros(8, 8)
        if not ok:
            all_nu_match = False
    print(f"  ALL 14 nu(k) dicts reconstruct their matrices exactly? {all_nu_match}")
    assert all_nu_match, "STEP B: nu(k) bivector-dict transcription does not match nu(k) matrix"

    print("\n" + "=" * 70)
    print("STEP C+D: build curv_h(p,q,k) entirely combinatorially -- zero")
    print("calls to RHO/NU matrix products, bracket_e, or decompose_g2")
    print("anywhere in build_curv_h_combinatorial()")
    print("=" * 70)
    curv_h_comb = build_curv_h_combinatorial()
    print(f"  Combinatorial curv_h: {len(curv_h_comb)} nonzero entries")
    for key in sorted(curv_h_comb):
        print(f"    {key}: {curv_h_comb[key]}")

    print("\n" + "=" * 70)
    print("STEP E: cross-check against the existing MATRIX-based")
    print("build_curvature_h_table() -- exact match required, all entries")
    print("=" * 70)
    curv_h_matrix = build_curvature_h_table()
    print(f"  Matrix-based curv_h: {len(curv_h_matrix)} nonzero entries")
    all_keys = set(curv_h_comb) | set(curv_h_matrix)
    all_match = True
    for key in sorted(all_keys):
        v_comb = curv_h_comb.get(key, 0)
        v_mat = curv_h_matrix.get(key, 0)
        if sp.simplify(v_comb - v_mat) != 0:
            all_match = False
            print(f"  MISMATCH at {key}: combinatorial={v_comb}, matrix={v_mat}")
    print(f"  ALL {len(all_keys)} entries match exactly? {all_match}")
    assert all_match, "STEP E: combinatorial curv_h disagrees with the matrix-based version"

    print("\n" + "=" * 70)
    print("STEP F: feed the combinatorially-rebuilt curv_h into Round 31's")
    print("own downstream pipeline (jach_coeff/degree4_coeff -> symbolic")
    print("Diff assembly) -- re-derive (1,-1/2,-7/4) with curv_h ITSELF")
    print("also matrix-free, closing Round 31's own flagged gap")
    print("=" * 70)
    T = build_T_table()

    ch4_coeffs = {}
    deg4_coeffs = {}
    for i, j, k, ll in itertools.combinations(range(1, 7), 4):
        ch4_coeffs[(i, j, k, ll)] = sp.simplify(jach_coeff(curv_h_comb, i, j, k, ll))
        deg4_coeffs[(i, j, k, ll)] = sp.simplify(degree4_coeff(T, curv_h_comb, i, j, k, ll))

    nonzero_ch4 = {q: v for q, v in ch4_coeffs.items() if v != 0}
    nonzero_deg4 = {q: v for q, v in deg4_coeffs.items() if v != 0}
    assert set(nonzero_ch4.keys()) == set(PAIR_PARTITION_QUADS), (
        f"jach_coeff (via combinatorial curv_h) has support outside the pair-partition "
        f"quadruples: {nonzero_ch4.keys()}"
    )
    assert set(nonzero_deg4.keys()) == set(PAIR_PARTITION_QUADS), (
        f"degree4_coeff (via combinatorial curv_h) has support outside the pair-partition "
        f"quadruples: {nonzero_deg4.keys()}"
    )
    ch_tilde_X_values = {ch4_coeffs[q] for q in PAIR_PARTITION_QUADS}
    deg4_X_values = {deg4_coeffs[q] for q in PAIR_PARTITION_QUADS}
    assert len(ch_tilde_X_values) == 1, (
        f"jach_coeff (via combinatorial curv_h) not equal across the 3 quadruples: "
        f"{ch_tilde_X_values}"
    )
    assert len(deg4_X_values) == 1, (
        f"degree4_coeff (via combinatorial curv_h) not equal across the 3 quadruples: "
        f"{deg4_X_values}"
    )
    ch_tilde_X = ch_tilde_X_values.pop()
    deg4_X = deg4_X_values.pop()
    print(f"  ch_tilde_X (via combinatorial curv_h) = {ch_tilde_X}")
    print(f"  deg4_X (via combinatorial curv_h) = {deg4_X}")
    assert ch_tilde_X == sp.Rational(1, 3), f"ch_tilde_X={ch_tilde_X}, expected 1/3"
    assert deg4_X == sp.Rational(-5, 12), f"deg4_X={deg4_X}, expected -5/12"

    Qh_sum = sp.simplify(
        2
        * sum(
            curv_h_comb.get((i, j, k), 0) ** 2
            for i in range(1, 7)
            for j in range(i + 1, 7)
            for k in range(1, 9)
        )
    )
    Ch_0 = sp.Rational(1, 8) * Qh_sum
    Qm_sum = sp.simplify(
        sum(T.get((i, j, k), 0) ** 2 for i in range(1, 7) for j in range(1, 7) for k in range(1, 7))
    )
    assert Qm_sum == 8, (
        f"Qm_sum computed from T={Qm_sum}, expected 8 (Round 26's established value)"
    )
    scalar_term = sp.Rational(1, 8) * Qh_sum + sp.Rational(3, 32) * Qm_sum
    print(
        f"  Ch_0 = {Ch_0}, Qm_sum (from T, not hardcoded) = {Qm_sum}, scalar_term = {scalar_term}"
    )
    assert Ch_0 == 1, f"Ch_0={Ch_0}, expected 1"
    assert scalar_term == sp.Rational(7, 4), f"scalar_term={scalar_term}, expected 7/4"

    sumM2_coeffs = expand_quartic_sum_from_T(T)
    H2_coeffs = expand_H_squared_from_T(T)
    expected_sumM2 = {
        (): sp.Rational(-1, 4),
        (1, 2, 3, 4): sp.Rational(1, 12),
        (1, 2, 5, 6): sp.Rational(1, 12),
        (3, 4, 5, 6): sp.Rational(1, 12),
    }
    expected_H2 = {(): 3, (1, 2, 3, 4): -3, (1, 2, 5, 6): -3, (3, 4, 5, 6): -3}
    assert sumM2_coeffs == expected_sumM2, f"sum_p M_p^2 disagrees with Round 29/31: {sumM2_coeffs}"
    assert H2_coeffs == expected_H2, f"H^2 disagrees with Round 29/31: {H2_coeffs}"

    Hs, Ids, Xs = sp.symbols("H Id X", commutative=True)
    H2_closed_sym = H2_coeffs[()] * Ids + H2_coeffs[(1, 2, 3, 4)] * Xs
    sumM2_closed_sym = sumM2_coeffs[()] * Ids + sumM2_coeffs[(1, 2, 3, 4)] * Xs
    Ch_tilde_sym = Ch_0 * Ids + ch_tilde_X * Xs
    degree4_term_sym = deg4_X * Xs

    CASIMIR_L_plain_sym = -sumM2_closed_sym
    Omega_g_clean_sym = H2_closed_sym / 4 + Hs - degree4_term_sym - scalar_term * Ids
    minus_Zp2_clean_sym = Omega_g_clean_sym - Ch_tilde_sym
    Diff_sym = sp.expand(minus_Zp2_clean_sym - CASIMIR_L_plain_sym)

    Cas_sym = sp.Symbol("Cas")
    Diff_in_Cas = sp.expand(Diff_sym.subs(Xs, 3 * (Cas_sym - Ids)))
    a = Diff_in_Cas.coeff(Hs)
    b = Diff_in_Cas.coeff(Ids)
    c = Diff_in_Cas.coeff(Cas_sym)
    print(f"\n  a={a}, b={b}, c={c}")
    target = (1, sp.Rational(-1, 2), sp.Rational(-7, 4))
    assert (a, b, c) == target, (
        f"Re-derivation via combinatorial curv_h gives {(a, b, c)}, expected {target}"
    )
    print(f"  MATCHES (1,-1/2,-7/4) with curv_h ALSO matrix-free? {(a, b, c) == target}")

    print("\n" + "=" * 70)
    print("STEP G: final sanity cross-check against Round 28's numeric Diff")
    print("(the ONLY Sigma-side e_action-based 8x8 matrix construction in")
    print("this entire script -- Cl(7,0)-side RHO/NU matrices were used")
    print("ONLY in STEP A/B's one-time primitive verification/self-test,")
    print("not in the per-(p,q,k) derivation loop itself, STEP C-F)")
    print("=" * 70)
    from g2su3_H_element import build_H_matrix
    from g2su3_round26_jach_derivation import build_Mp

    H = build_H_matrix(T)
    Ms = build_Mp()
    Id8 = sp.eye(DIM)
    Ls = {}

    def unit_vec(i):
        v = sp.zeros(DIM, 1)
        v[i] = 1
        return v

    for k in range(1, 9):
        cols = [su3_action(k, unit_vec(i)) for i in range(DIM)]
        Ls[k] = sp.Matrix.hstack(*cols)
    Casimir_su3 = sp.simplify(sum((-(Ls[k] * Ls[k]) for k in range(1, 9)), sp.zeros(DIM, DIM)))
    Diff_numeric, _ = build_diff_noncircular(T, curv_h_comb, H, Ms, Casimir_su3, Id8)
    Reconstructed = a * H + b * Id8 + c * Casimir_su3
    match = sp.simplify(Reconstructed - Diff_numeric) == sp.zeros(DIM, DIM)
    print(f"  a*H+b*Id+c*Casimir_su3 == Diff_numeric (using combinatorial curv_h)? {match}")
    assert match, (
        "STEP G: fully-combinatorial (curv_h included) derivation disagrees with numeric Diff"
    )

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("  curv_h(p,q,k) -- the LAST piece of the derivation chain still")
    print("  built via 8x8 Clifford matrices after Round 31 -- is now ALSO")
    print("  rebuilt entirely combinatorially (STEPs C-F): the Cl(7,0)-side")
    print("  RHO/NU matrix products, bracket_e commutator, and decompose_g2")
    print("  trace-projection are replaced by the SAME Clifford-word-")
    print("  reduction technique Round 29 used for Sigma M_p^2/H^2, plus a")
    print("  combinatorial dot-product formula for the trace-projection")
    print("  (justified by a ONE-TIME, general primitive check, STEP A --")
    print("  not needed per (p,q,k), only once for the whole algebra).")
    print()
    print("  Combined with Rounds 29 and 31, the ENTIRE derivation chain")
    print("  from raw NU-dict/T-table data to (1,-1/2,-7/4) is now free of")
    print("  Clifford-matrix construction, except: STEP A/B's one-time")
    print("  primitive-verification/self-test (not part of the per-index")
    print("  derivation), and STEP G's final numeric sanity cross-check.")


if __name__ == "__main__":
    main()
    print("\nEXIT=0")
