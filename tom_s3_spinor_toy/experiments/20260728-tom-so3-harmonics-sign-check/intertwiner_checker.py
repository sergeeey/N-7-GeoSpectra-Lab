r"""Reusable helper: honestly build the matrix representation of a
differential operator in a given function basis, via bra-ket (inner-product)
projection -- the THIRD independent method verified in
verify_via_inner_product.py to agree exactly with the two other methods used
in this round (linear-system solving; exp(i*phi)-coefficient decomposition).

Motivation (see decision.md): comparing a differential operator's action to
an abstract Lie-algebra generator matrix via "matrix times a combined vector
of several DIFFERENT basis functions" (the pattern used in Tom Lawrence's
2026-07-28 PDF) silently produces the TRANSPOSE of the honest matrix
representation for off-diagonal generators. Any future round in this
project that needs to compare a differential/geometric operator against an
abstract matrix representation should use this function (or one of its
sibling methods) directly, rather than re-deriving the comparison ad hoc.

Usage:
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..",
                     "20260728-tom-so3-harmonics-sign-check"))
    from intertwiner_checker import build_matrix_via_bra_ket, compare_to_abstract_matrix

    basis = {"p1": sin(theta)*exp(I*phi), "p0": cos(theta), "pm1": sin(theta)*exp(-I*phi)}
    order = ["p1", "p0", "pm1"]
    M = build_matrix_via_bra_ket(basis, order, Lx, theta, phi,
                                  measure=sp.sin(theta), phi_range=(0, 2*sp.pi),
                                  theta_range=(0, sp.pi))
    compare_to_abstract_matrix(M, T_prime_x)  # reports match / transpose-match / neither
"""

from __future__ import annotations

import sympy as sp


def build_matrix_via_bra_ket(
    basis: dict[str, sp.Expr],
    order: list[str],
    operator,
    theta: sp.Symbol,
    phi: sp.Symbol,
    measure: sp.Expr,
    theta_range: tuple,
    phi_range: tuple,
) -> sp.Matrix:
    """Build the matrix of `operator` in `basis`, ordered by `order`, via
    genuine bra-ket projection: M[row,col] = <basis[order[row]] | operator |
    basis[order[col]]> / <basis[order[row]] | basis[order[row]]>, with the
    inner product <f|g> := integral conj(f)*g*measure over the given ranges.

    This is the HONEST matrix representation -- unlike "operator applied to a
    combined vector of all basis functions at once" (which silently produces
    a transpose for non-symmetric operators, see decision.md), this builds
    each matrix element independently via its own defining integral, exactly
    matching standard quantum-mechanics matrix-element bookkeeping.
    """
    n = len(order)
    M = sp.zeros(n, n)

    def inner_product(f: sp.Expr, g: sp.Expr) -> sp.Expr:
        integrand = sp.conjugate(f) * g * measure
        inner_theta = sp.integrate(integrand, (theta, theta_range[0], theta_range[1]))
        return sp.simplify(sp.integrate(inner_theta, (phi, phi_range[0], phi_range[1])))

    for col, ket_name in enumerate(order):
        ket = basis[ket_name]
        op_ket = operator(ket)
        for row, bra_name in enumerate(order):
            bra = basis[bra_name]
            norm_bra = inner_product(bra, bra)
            raw = inner_product(bra, op_ket)
            M[row, col] = sp.simplify(raw / norm_bra)
    return M


def compare_to_abstract_matrix(honest_matrix: sp.Matrix, abstract_matrix: sp.Matrix) -> str:
    """Classify the relationship between an honestly-built operator matrix and
    a candidate abstract matrix: EQUAL, TRANSPOSE, NEGATIVE, NEGATIVE_TRANSPOSE,
    or NO_SIMPLE_RELATION. Use this before trusting any "L=T" or "L=-T" claim
    that was derived via a combined-vector comparison instead of this honest
    per-basis-element construction."""
    n = honest_matrix.shape[0]
    zero = sp.zeros(n, n)
    if sp.simplify(honest_matrix - abstract_matrix) == zero:
        return "EQUAL"
    if sp.simplify(honest_matrix - abstract_matrix.T) == zero:
        return "TRANSPOSE"
    if sp.simplify(honest_matrix + abstract_matrix) == zero:
        return "NEGATIVE"
    if sp.simplify(honest_matrix + abstract_matrix.T) == zero:
        return "NEGATIVE_TRANSPOSE"
    return "NO_SIMPLE_RELATION"
