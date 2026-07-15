"""L3b: does K=Spin(4)xSpin(4) have an invariant vector in the fiber (8_v,8_s,8_c)?

Context: L3B_SPIN8_INTERFACE_SPEC.md SS1.5, "Attempted 2026-07-15, continued"
(the K-equivariant Lemma B attempt). G74A's Lemma B upper-bounds dim ker <= 1
per channel via: G2 acts TRANSITIVELY on the base S6=G2/SU(3), so Frobenius
reciprocity gives {G2-invariant sections} = {SU(3)-invariant fiber vectors} --
counting G2-singlets in the fiber directly counts possible zero modes.

This module checks the analogous fiber-invariant count for K=Spin(4)xSpin(4)
(the candidate from ../20260715-l3b-so4xso4-candidate/). Result: zero in all
three channels -- but (see decision.md / spec) this number does NOT license
an upper bound on dim ker the way it did for G2, because K (as constructed)
acts only on the fiber, not on the base -- the Frobenius reciprocity step
Lemma B relies on has no analogue here. This script computes the fiber fact
honestly; it does NOT claim a kernel bound.
"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "20260715-l3b-so4xso4-candidate"))
sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..", "20260715-l3b-triality-so4xso4-invariance"),
)

from so4xso4_branching import GAMMA, GAMMA_9  # noqa: E402
from triality_so4xso4_invariance import build_so4xso4_basis  # noqa: E402


def spin_lift(a):
    """so(8) generator a (8x8 antisymmetric) -> spin representation (16x16)."""
    mat = np.zeros((16, 16), dtype=complex)
    for i in range(8):
        for j in range(8):
            if a[i, j] != 0:
                mat += a[i, j] * (GAMMA[i + 1] @ GAMMA[j + 1]) / 4
    return mat


def chirality_eigenbasis():
    evals, evecs = np.linalg.eigh(GAMMA_9)
    return evecs[:, evals > 0], evecs[:, evals < 0]


def k_invariant_dim_8v(tol=1e-8):
    """Joint kernel dimension of all 12 so(4)+so(4) generators on 8_v (vector rep)."""
    basis = build_so4xso4_basis()
    stacked = np.vstack(list(basis))
    _u, s, _vt = np.linalg.svd(stacked)
    return int(np.sum(s < tol))


def k_invariant_dim_spinor(v_chirality, tol=1e-8):
    """Joint kernel dimension of all 12 so(4)+so(4) generators on 8_s or 8_c,
    via the spin-lift restricted to the given chirality eigenbasis.
    """
    basis = build_so4xso4_basis()
    restricted = [v_chirality.conj().T @ spin_lift(a) @ v_chirality for a in basis]
    stacked = np.vstack(restricted)
    _u, s, _vt = np.linalg.svd(stacked)
    return int(np.sum(s < tol))


if __name__ == "__main__":
    v_s, v_c = chirality_eigenbasis()

    dim_8v = k_invariant_dim_8v()
    dim_8s = k_invariant_dim_spinor(v_s)
    dim_8c = k_invariant_dim_spinor(v_c)

    print("K=Spin(4)xSpin(4)-invariant subspace dimension:")
    print(f"  8_v: {dim_8v}  (expect 0 -- each SO(4) block's vector rep is nontrivial)")
    print(f"  8_s: {dim_8s}  (expect 0 -- matches branching, no (1,1;1,1) piece)")
    print(f"  8_c: {dim_8c}  (expect 0 -- matches branching, no (1,1;1,1) piece)")
    print()
    print("IMPORTANT: this fiber fact does NOT license a kernel upper bound the")
    print("way the G2-singlet count did in G74A's Lemma B -- that argument used")
    print("Frobenius reciprocity for G2 acting transitively on the BASE S6.")
    print("K here acts only on the fiber -- no such correspondence is available.")
    print("See L3B_SPIN8_INTERFACE_SPEC.md SS1.5 for the full reasoning.")
