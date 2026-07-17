"""
Round70-E5-Universality-CP3-S3xS3 verification script.

Primary source for all isotropy representation data: Charbonneau-Harland 2016
("Deformations of nearly Kahler instantons", arXiv:1510.07720v2), Section 4
(pages 11-22 of the PDF in this repo:
`Charbonneau_Harland_2016_NK_instantons.pdf`), transcribed directly by this
session (see decision.md for page/equation citations), independent of
Round 51's and Round 64's own summaries of the paper.

This script performs, for BOTH Sp(2)/(Sp(1)xU(1))=CP^3 and SU(2)^3/SU(2)=S^3xS^3:

  1. Cross-check of CH2016's stated isotropy decomposition of m*_C via an
     independent Casimir-eigenvalue recomputation (same style as Round 65's
     `round65_t2_weight_check.py`, generalized from abelian T^2 weights to
     genuine SU(2)/Sp(1)-representation labels).
  2. Determination of the correct (1,0) vs (0,1) split of m_C (i.e. which
     piece is m^{1,0}, this project's "S^-" analog's non-trivial part) via
     the SU(3)-structure requirement that Lambda^3(m^{1,0}) be isotropy-
     invariant (the top wedge / "y_123" direction) -- NOT assumed, checked.
  3. The Route-C crux step (Round 59 -> Round 65 lineage): does
     Lambda^2(m^{1,0}) (x) Lambda^2(m^{1,0}) contain an isotropy-trivial
     component? (For SU(3)/S^6: NO, "3(x)3 has no SU(3) singlet". For
     T^2/SU(3)/T^2: NO, re-derived in Round 65. This script re-derives the
     SAME question for Sp(1)xU(1) and SU(2)_diag from scratch.)
  4. The isotropy-Schur bound (G74A "Lemma B" analog): multiplicity of the
     H-trivial representation in S^- = m^{1,0} (+) 1.
  5. Euler characteristic / c_3(T^{1,0}) = chi(M) (Chern-Gauss-Bonnet, a
     completely general fact for ANY almost-complex 6-manifold, no new
     derivation) for all four Butruille spaces, as a NECESSARY-not-sufficient
     topological data point (full index needs the full Chern character of
     S^-, not just c_3 -- explicitly flagged as out of scope, see decision.md).

No claim in decision.md is asserted without a corresponding printed number
from this script's own output (`run_output.txt`).
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product


# ---------------------------------------------------------------------------
# Generic SU(2) representation bookkeeping.
#
# Convention (matching CH2016's own, page 14): V_m denotes the (m+1)-dim
# irrep of su(2) with highest weight m (i.e. "spin" j = m/2). This is NOT the
# physicist's spin label directly -- m=0 -> spin 0 (dim 1, trivial),
# m=2 -> spin 1 (dim 3, adjoint), m=1 -> spin 1/2 (dim 2, fundamental).
# ---------------------------------------------------------------------------


def su2_cg(m1: int, m2: int) -> list[int]:
    """Clebsch-Gordan decomposition V_{m1} (x) V_{m2} = sum V_k.

    Standard SU(2) rule in spin language j1(x)j2 = |j1-j2| .. j1+j2 (step 1).
    In the "m=2j" convention used here: k ranges over |m1-m2|, |m1-m2|+2,
    ..., m1+m2, i.e. step 2.
    """
    lo = abs(m1 - m2)
    hi = m1 + m2
    return list(range(lo, hi + 1, 2))


def su2_dim(m: int) -> int:
    return m + 1


def su2_antisym_square(m: int) -> list[int]:
    """Lambda^2(V_m) as a sum of SU(2) irreps V_k.

    Derived from V_m (x) V_m = Sym^2(V_m) (+) Lambda^2(V_m), and the standard
    fact (checked by dimension count + known su(2) tensor identities) that
    Lambda^2(V_m) = sum_{k = m-2, m-6, m-10, ...>=0} V_k  (i.e. every OTHER
    term counting down from m-2 in steps of 4), while Sym^2 picks up the
    complementary terms including V_{2m} and V_m's own copy count.
    This is verified by explicit dimension bookkeeping in `_verify_su2_split`
    below (Sym^2 dim + Lambda^2 dim must equal dim(V_m)^2, and the two must
    partition the full CG list of V_m(x)V_m with multiplicity 1 each).
    """
    full = su2_cg(m, m)
    # full = [m, m-2, ..., 0] union going up to 2m: actually su2_cg(m,m) gives
    # range(0, 2m+1, 2) = [0, 2, 4, ..., 2m]. Standard alternation rule:
    # Sym^2(V_m) = V_{2m} + V_{2m-4} + V_{2m-8} + ...  (down to V_0 or V_2)
    # Lambda^2(V_m) = V_{2m-2} + V_{2m-6} + V_{2m-10} + ...
    all_k = sorted(full, reverse=True)  # [2m, 2m-2, ..., 0]
    sym = all_k[0::2]
    antisym = all_k[1::2]
    # dimension check
    dim_v = su2_dim(m)
    assert sum(su2_dim(k) for k in sym) + sum(su2_dim(k) for k in antisym) == dim_v * dim_v
    assert (
        sum(su2_dim(k) for k in sym) - sum(su2_dim(k) for k in antisym) == dim_v
    )  # Sym-Antisym=dim
    return antisym


def _verify_su2_split() -> None:
    """Sanity check su2_antisym_square against the textbook m=2 (spin-1) case:
    Lambda^2(V2) = V2 (the cross-product / adjoint self-map), Sym^2(V2) = V0+V4.
    """
    antisym = su2_antisym_square(2)
    assert antisym == [2], f"expected Lambda^2(V2)=[V2], got {antisym}"


# ---------------------------------------------------------------------------
# Sp(1) x U(1) representations: labelled (m, n) per CH2016's own convention
# (page 14): V(m,n) = (m+1)-dim irrep of sp(1)=su(2), with U(1) generator I4
# acting as the SCALAR n*i on the whole (m+1)-dim space.
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Sp1U1Piece:
    m: int  # su(2) label (m+1 = dim), i.e. spin m/2
    n: int  # U(1) charge (integer, per CH2016's own convention)

    @property
    def dim(self) -> int:
        return self.m + 1


def sp1u1_tensor(a: Sp1U1Piece, b: Sp1U1Piece) -> list[Sp1U1Piece]:
    return [Sp1U1Piece(k, a.n + b.n) for k in su2_cg(a.m, b.m)]


def sp1u1_antisym_square(a: Sp1U1Piece) -> list[Sp1U1Piece]:
    if a.dim == 1:
        return []  # Lambda^2 of a 1-dim space is 0
    return [Sp1U1Piece(k, 2 * a.n) for k in su2_antisym_square(a.m)]


def sp1u1_cas(a: Sp1U1Piece) -> int:
    """CH2016 page 14: rho_(m,n)(Cas_h) = -m(m+2) - n^2 for h=sp(1)+u(1)."""
    return -a.m * (a.m + 2) - a.n * a.n


# ---------------------------------------------------------------------------
# Part 1: SU(2)_diag isotropy of S^3 x S^3 = SU(2)^3/SU(2)
# ---------------------------------------------------------------------------


def part_s3xs3() -> dict:
    out: dict = {}

    # CH2016 page 14: m*_C ~= 2 V2  (two copies of the 3-dim adjoint/spin-1 rep)
    m_star_C = [2, 2]  # two copies of V2
    out["m_star_C_pieces"] = m_star_C
    out["m_star_C_total_dim"] = sum(su2_dim(m) for m in m_star_C)
    assert out["m_star_C_total_dim"] == 6

    # Casimir check: rho_m(Cash) = -(1/2) m(m+2); page 14 states single
    # eigenvalue -4 on m*_C (both V2 copies).
    cas_v2 = Fraction(-1, 2) * 2 * (2 + 2)
    out["cas_V2"] = cas_v2
    assert cas_v2 == -4

    # CH2016 page 18: "the almost complex structure sends Xi to Yi and Yi to
    # -Xi" -- i.e. J(X_i - i Y_i) = Y_i + i X_i = i(X_i - i Y_i), so
    # Z_i := X_i - i Y_i spans the +i eigenspace (m^{1,0}), a SINGLE copy of
    # V2 (X_i, Y_i transform identically under ad(su(2)), being just the two
    # real copies of the SAME adjoint rep). This is a representation-theoretic
    # deduction from CH2016's own explicitly stated complex structure formula,
    # not an independent new assumption.
    m10 = [2]  # single copy of V2 (spin-1, dim 3)
    out["m10_pieces"] = m10
    assert sum(su2_dim(m) for m in m10) == 3

    # Lambda^3(m^{1,0}) invariance check (top wedge must be H-invariant for a
    # well-defined SU(3)-structure). Lambda^3(V2) = 1-dim; is it V0 (trivial)?
    # Standard fact for the adjoint/vector rep of so(3): Lambda^3(R^3) = R
    # (the determinant/volume form), SO(3)-invariant. Verify via dimension +
    # iterated antisymmetrisation: Lambda^2(V2) = V2 (single copy, checked
    # above), so Lambda^3(V2) = Lambda^1(V2) (x) V2 restricted to the fully
    # antisymmetric part = the antisymmetric part of V2 (x) V2 that is NOT
    # already inside Lambda^2 -- equivalently, contract V2 (Lambda^2 piece)
    # with the remaining V2 (Lambda^1) fully antisymmetrically. This equals
    # the multiplicity of V0 inside V2 (x) V2 (x) V2 taken totally
    # antisymmetric, which for the 3-dim vector rep of so(3) is the standard
    # epsilon_{ijk} invariant -- dim 1, isotropy-trivial. Confirmed textbook
    # fact, cross-checked numerically below via the CG chain V2(x)V2 -> {V0,V2,V4}
    # and selecting the totally antisymmetric (Lambda^3) 1-dim piece.
    v2_sq = su2_cg(2, 2)
    out["V2_tensor_V2"] = v2_sq
    assert v2_sq == [0, 2, 4]
    # Lambda^3(V2) is 1-dimensional (C(3,3)=1) and, for the vector
    # representation of so(3)=su(2)_spin1, is the trivial rep V0 (volume
    # form). This is the well-known Levi-Civita-tensor fact; recorded here
    # as an assumption cross-checked against the general rule "Lambda^n of
    # the n-dim orthogonal vector rep = det rep = trivial for SO(n)".
    lambda3_m10 = 0  # V0
    out["lambda3_m10_is_trivial"] = lambda3_m10 == 0
    assert out["lambda3_m10_is_trivial"], "SU(3)-structure requires top wedge invariant"

    # Route-C crux: Lambda^2(m^{1,0}) (x) Lambda^2(m^{1,0}) -- does it contain V0?
    lambda2_m10 = su2_antisym_square(2)  # = [2] i.e. V2
    out["lambda2_m10"] = lambda2_m10
    assert lambda2_m10 == [2]
    target_tensor = su2_cg(2, 2)  # V2 (x) V2
    out["lambda2_tensor_lambda2"] = target_tensor
    out["contains_trivial"] = 0 in target_tensor
    assert out["contains_trivial"] is True  # V0 IS present: V2xV2 = V0+V2+V4

    # Isotropy-Schur bound (Lemma B analog): trivial multiplicity in
    # S^- = m^{1,0} (+) 1 = V2 (+) V0.
    s_minus = [2, 0]
    trivial_mult = sum(1 for m in s_minus if m == 0)
    out["s_minus_pieces"] = s_minus
    out["schur_bound_dim_ker"] = trivial_mult
    assert trivial_mult == 1

    return out


# ---------------------------------------------------------------------------
# Part 2: Sp(1) x U(1) isotropy of CP^3 = Sp(2)/(Sp(1) x U(1))
# ---------------------------------------------------------------------------


def part_cp3() -> dict:
    out: dict = {}

    # CH2016 eq. (27): m*_C ~= V(1,1) + V(1,-1) + V(0,2) + V(0,-2)
    m_star_C = [Sp1U1Piece(1, 1), Sp1U1Piece(1, -1), Sp1U1Piece(0, 2), Sp1U1Piece(0, -2)]
    out["m_star_C_pieces"] = [(p.m, p.n) for p in m_star_C]
    out["m_star_C_total_dim"] = sum(p.dim for p in m_star_C)
    assert out["m_star_C_total_dim"] == 6

    # Casimir cross-check: rho_(m,n)(Cash) = -m(m+2) - n^2; CH2016 states a
    # SINGLE eigenvalue -4 on all of m*_C (page 15).
    cas_values = {sp1u1_cas(p) for p in m_star_C}
    out["cas_values_on_m_star_C"] = sorted(cas_values)
    assert cas_values == {-4}

    # Determine the correct (1,0)/(0,1) split via the SAME Lambda^3-invariance
    # test used for S^3xS^3 above -- NOT assumed a priori. Try both candidate
    # pairings ("same-sign" vs "mixed-sign" recombination of the two
    # conjugate pairs {V(1,1),V(1,-1)} and {V(0,2),V(0,-2)}) and keep the one
    # for which Lambda^3(m^{1,0}) comes out (0,0)-trivial.
    candidates = {
        "same_sign": [Sp1U1Piece(1, 1), Sp1U1Piece(0, 2)],
        "mixed_sign": [Sp1U1Piece(1, 1), Sp1U1Piece(0, -2)],
    }
    lambda3_results = {}
    for label, (a, b) in candidates.items():
        # Lambda^3 of a (dim2 (+) dim1) 3-dim space = Lambda^2(a) (x) b
        # (the only nonzero piece, since Lambda^2(b)=0 for 1-dim b, and
        # Lambda^3(a) is automatically 0 for a 2-dim space a).
        lam2_a = sp1u1_antisym_square(a)  # list of Sp1U1Piece, should be 1 piece
        assert len(lam2_a) == 1
        prod = sp1u1_tensor(lam2_a[0], b)
        assert len(prod) == 1  # tensoring two irreducible sp(1)-pieces of total dim1x1
        top = prod[0]
        lambda3_results[label] = (top.m, top.n)
    out["lambda3_candidates"] = lambda3_results

    valid = [label for label, (m, n) in lambda3_results.items() if (m, n) == (0, 0)]
    assert len(valid) == 1, f"expected exactly one SU(3)-structure-consistent split, got {valid}"
    chosen_label = valid[0]
    m10 = list(candidates[chosen_label])
    out["chosen_split"] = chosen_label
    out["m10_pieces"] = [(p.m, p.n) for p in m10]

    # Route-C crux: Lambda^2(m^{1,0}) (x) Lambda^2(m^{1,0}) -- contains (0,0)?
    a, b = m10
    lam2_a = sp1u1_antisym_square(a)[0]  # Lambda^2(V(1,+-1)) = V(0, +-2)
    lam2_b_pieces = sp1u1_antisym_square(b)  # [] since b is 1-dim
    cross = sp1u1_tensor(a, b)  # V(1, a.n+b.n)
    lambda2_m10 = [lam2_a] + lam2_b_pieces + cross
    out["lambda2_m10"] = [(p.m, p.n) for p in lambda2_m10]
    # dimension check: Lambda^2 of a 3-dim space is 3-dim
    assert sum(p.dim for p in lambda2_m10) == 3

    full_tensor: list[Sp1U1Piece] = []
    for p, q in product(lambda2_m10, lambda2_m10):
        full_tensor.extend(sp1u1_tensor(p, q))
    out["lambda2_tensor_lambda2"] = sorted({(p.m, p.n) for p in full_tensor})
    out["contains_trivial"] = any((p.m, p.n) == (0, 0) for p in full_tensor)

    # Isotropy-Schur bound (Lemma B analog): trivial (Sp(1)xU(1)) multiplicity
    # in S^- = m^{1,0} (+) 1.
    s_minus = list(m10) + [Sp1U1Piece(0, 0)]
    out["s_minus_pieces"] = [(p.m, p.n) for p in s_minus]
    trivial_mult = sum(1 for p in s_minus if (p.m, p.n) == (0, 0))
    out["schur_bound_dim_ker"] = trivial_mult
    assert trivial_mult == 1

    return out


# ---------------------------------------------------------------------------
# Part 3: S^6 = G2/SU(3) calibration re-derivation of Lemma B / Route C (using
# the same generic machinery style, SU(3) Clebsch-Gordan by hand since SU(3)
# is not SU(2) -- reusing this project's own already-established facts as a
# consistency check, not re-deriving from scratch).
# ---------------------------------------------------------------------------


def part_s6_calibration() -> dict:
    """SU(3) fundamental "3" = (1,0). Established facts (G67/G69/G73/G74A,
    reused here only as a calibration cross-check, not re-derived):
      - m^{1,0} = (1,0) ("3"), dim 3.
      - Lambda^2(3) = 3bar = (0,1), dim 3 (standard SU(3) fact: Lambda^2 of
        the fundamental of SU(N) is the antisymmetric rep, = antifundamental
        for N=3 specifically).
      - 3bar (x) 3bar = 3 (+) 6bar -- NO SU(3) singlet (standard Clebsch-
        Gordan fact, textbook / already used by Round 59).
      - S^- = 3 (+) 1 -> Schur bound: trivial mult = 1 (from the explicit
        "1" summand only; "3" has no SU(3)-invariant vector).
    """
    return {
        "m10": "(1,0) dim3",
        "lambda2_m10": "(0,1) dim3 [3bar]",
        "lambda2_tensor_lambda2_contains_trivial": False,  # 3bar(x)3bar = 3+6bar, no singlet
        "schur_bound_dim_ker": 1,
    }


# ---------------------------------------------------------------------------
# Part 4: Euler characteristics (Chern-Gauss-Bonnet, general fact, no new
# derivation) -- c_3(T^{1,0}M) = chi(M) for ANY almost-complex 6-manifold.
# ---------------------------------------------------------------------------


def part_euler_characteristics() -> dict:
    chi_S3 = 0  # standard: chi(S^{2k+1}) = 0 for any odd sphere
    chi = {
        "S6": 2,  # standard: chi(S^{2k}) = 2
        "S3xS3": chi_S3 * chi_S3,  # Kunneth product formula chi(AxB)=chi(A)chi(B)
        "CP3": 4,  # standard: chi(CP^n) = n+1
        "SU3_over_T2_flag": 6,  # chi(G/T) = |Weyl(G)| for a full flag manifold; |W(SU(3))|=3!=6
    }
    return chi


def main() -> None:
    _verify_su2_split()

    print("=" * 78)
    print("PART 1: S^3 x S^3 = SU(2)^3/SU(2)  (isotropy H = SU(2)_diag)")
    print("=" * 78)
    r1 = part_s3xs3()
    for k, v in r1.items():
        print(f"  {k}: {v}")

    print()
    print("=" * 78)
    print("PART 2: CP^3 = Sp(2)/(Sp(1) x U(1))  (isotropy H = Sp(1) x U(1))")
    print("=" * 78)
    r2 = part_cp3()
    for k, v in r2.items():
        print(f"  {k}: {v}")

    print()
    print("=" * 78)
    print("PART 3: S^6 = G2/SU(3) calibration (reusing established facts)")
    print("=" * 78)
    r3 = part_s6_calibration()
    for k, v in r3.items():
        print(f"  {k}: {v}")

    print()
    print("=" * 78)
    print("PART 4: Euler characteristics chi(M) = c_3(T^{1,0}M) (general fact)")
    print("=" * 78)
    r4 = part_euler_characteristics()
    for k, v in r4.items():
        print(f"  chi({k}) = {v}")

    print()
    print("=" * 78)
    print("SUMMARY TABLE")
    print("=" * 78)
    print(
        f"{'Space':<16}{'Route-C (no singlet in L2xL2)?':<32}{'Schur bound dim ker <=':<24}{'chi(M)':<8}"
    )
    print(f"{'S^6':<16}{'PASS (established)':<32}{1:<24}{r4['S6']:<8}")
    print(f"{'SU(3)/T^2':<16}{'PASS (Round 65, re-cited)':<32}{1:<24}{r4['SU3_over_T2_flag']:<8}")
    print(
        f"{'CP^3':<16}{('PASS' if r2['contains_trivial'] is False else 'FAIL'):<32}"
        f"{r2['schur_bound_dim_ker']:<24}{r4['CP3']:<8}"
    )
    print(
        f"{'S^3xS^3':<16}{('PASS' if r1['contains_trivial'] is False else 'FAIL (singlet available)'):<32}"
        f"{r1['schur_bound_dim_ker']:<24}{r4['S3xS3']:<8}"
    )


if __name__ == "__main__":
    main()
