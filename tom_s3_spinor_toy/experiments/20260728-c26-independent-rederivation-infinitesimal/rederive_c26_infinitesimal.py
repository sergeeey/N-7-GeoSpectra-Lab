r"""Independent second derivation of C26 (round77's SU(2)_L x SU(2)_R
representation pattern), via a genuinely DIFFERENT technique: differentiate
round77's own finite-transformation actions ACTION_L(h,psi)(G):=psi(h^-1 G),
ACTION_R(h,psi)(G):=h.psi(Gh) at h=identity to get INFINITESIMAL (Lie
algebra) generators as actual differential operators, then check directly
whether psi^(0), psi^(1) are annihilated (singlet) or transform as the full
fundamental representation (doublet) under these generators -- structurally
the same TYPE of check Tom Lawrence's PDF did (compare a differential
operator's action to an abstract Lie-algebra generator), applied honestly
here rather than by re-testing finite group elements (round77's own method).

Key correspondence (round76 Part 1, already tool-verified): X_i^L's FLOW is
RIGHT translation (g -> g.exp(sX_i)); X_i^R's FLOW is LEFT translation
(g -> exp(sX_i).g). Differentiating:
  ACTION_L(exp(eps*Y),psi)(G) = psi(exp(-eps*Y)G)
    -> infinitesimal generator = -X_Y^R(psi)  [LEFT translation flow = X^R]
  ACTION_R(exp(eps*Y),psi)(G) = exp(eps*Y).psi(G.exp(eps*Y))
    -> infinitesimal generator = Y.psi + X_Y^L(psi)  [RIGHT translation flow = X^L]

Reuses round76's own verified XL, XR vector fields and psi^(1)=gbar(x)*psi_0
construction directly (sys.path import), not re-derived from scratch.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROUND76 = HERE.parent / "20260717-round76-e9followup-right-invariant-frame" / "e10_right_invariant_frame.py"
spec = importlib.util.spec_from_file_location("round76", ROUND76)
assert spec and spec.loader
R76 = importlib.util.module_from_spec(spec)
sys.modules["round76"] = R76
spec.loader.exec_module(R76)

I = sp.I  # noqa: E741
x0, x1, x2, x3 = R76.x0, R76.x1, R76.x2, R76.x3
XS = R76.XS

Z = R76.clifford_generators()
Binv = R76.basis_inverse(Z)
XL, XR = R76.build_invariant_frames(Z, Binv)  # round76's own verified vector fields


def directional_derivative_of_matrix(M: sp.Matrix, vf: list[sp.Expr]) -> sp.Matrix:
    """Apply a vector field (4 components in x0..x3) to each entry of a matrix M."""
    out = sp.zeros(*M.shape)
    for r in range(M.shape[0]):
        for c in range(M.shape[1]):
            term = sp.Integer(0)
            for mu in range(4):
                term += vf[mu] * sp.diff(M[r, c], XS[mu])
            out[r, c] = sp.expand(term)
    return out


def infinitesimal_L_generator(psi: sp.Matrix, i: int) -> sp.Matrix:
    """Y=Z_i infinitesimal SU(2)_L generator on psi: -X_i^R(psi)."""
    return sp.simplify(-directional_derivative_of_matrix(psi, XR[i]))


def infinitesimal_R_generator(psi: sp.Matrix, i: int) -> sp.Matrix:
    """Y=Z_i infinitesimal SU(2)_R generator on psi: Z_i*psi + X_i^L(psi)."""
    return sp.simplify(Z[i] * psi + directional_derivative_of_matrix(psi, XL[i]))


def main() -> None:
    a, b = sp.symbols("a b")
    psi0 = sp.Matrix([a, b])  # t=0: genuine constant (x-independent)

    print("=" * 90)
    print("t=0 (psi^(0) = constant (a,b)): infinitesimal generator check")
    print("=" * 90)
    su2L_on_psi0 = [infinitesimal_L_generator(psi0, i) for i in range(3)]
    su2R_on_psi0 = [infinitesimal_R_generator(psi0, i) for i in range(3)]
    su2L_all_zero = all(g == sp.zeros(2, 1) for g in su2L_on_psi0)
    print("SU(2)_L generators on psi^(0) (expect all ZERO -> singlet):")
    for i, g in enumerate(su2L_on_psi0):
        print(f"  Y=Z_{i+1}: {list(g)}")
    print("ALL ZERO (exact singlet)?", su2L_all_zero)
    print()
    print("SU(2)_R generators on psi^(0) (expect = Z_i*(a,b) exactly -> doublet):")
    doublet_match = []
    for i, g in enumerate(su2R_on_psi0):
        expected = sp.simplify(Z[i] * psi0)
        match = sp.simplify(g - expected) == sp.zeros(2, 1)
        doublet_match.append(match)
        print(f"  Y=Z_{i+1}: generator={list(g)}  matches Z_{i+1}*(a,b)? {match}")
    print("ALL match fundamental (genuine doublet, not degenerate)?", all(doublet_match))

    print()
    print("=" * 90)
    print("t=1 (psi^(1) = gbar(x)*psi_0, c0=-2 right-invariant profile)")
    print("=" * 90)
    a_, b_ = sp.symbols("a_ b_")
    psi0_1 = sp.Matrix([a_, b_])
    gbar = R76.group_conjugate(Z)
    psi1 = sp.expand(gbar * psi0_1)

    su2L_on_psi1 = [infinitesimal_L_generator(psi1, i) for i in range(3)]
    su2R_on_psi1 = [infinitesimal_R_generator(psi1, i) for i in range(3)]

    print("SU(2)_R generators on psi^(1) (expect all ZERO -> singlet):")
    su2R_all_zero = True
    for i, g in enumerate(su2R_on_psi1):
        is_zero = sp.expand(g) == sp.zeros(2, 1)
        su2R_all_zero &= is_zero
        print(f"  Y=Z_{i+1}: is_zero={is_zero}  (residual: {list(sp.simplify(g))})")
    print("ALL ZERO (exact singlet)?", su2R_all_zero)
    print()
    print("SU(2)_L generators on psi^(1) (expect nonzero, genuine doublet-type action):")
    su2L_nontrivial = []
    for i, g in enumerate(su2L_on_psi1):
        is_nonzero = sp.expand(g) != sp.zeros(2, 1)
        su2L_nontrivial.append(is_nonzero)
        print(f"  Y=Z_{i+1}: nonzero={is_nonzero}")
    print("At least one nonzero (genuinely charged, not singlet)?", any(su2L_nontrivial))

    print()
    print("=" * 90)
    print("VERDICT")
    print("=" * 90)
    print(f"psi^(0) exact SU(2)_L singlet: {su2L_all_zero}")
    print(f"psi^(0) genuine SU(2)_R doublet (matches Z_i exactly): {all(doublet_match)}")
    print(f"psi^(1) exact SU(2)_R singlet: {su2R_all_zero}")
    print(f"psi^(1) nontrivially SU(2)_L-charged: {any(su2L_nontrivial)}")


if __name__ == "__main__":
    main()
