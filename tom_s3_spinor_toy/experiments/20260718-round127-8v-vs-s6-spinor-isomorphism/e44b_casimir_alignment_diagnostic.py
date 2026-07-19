"""Round127 follow-up diagnostic: confirms the Layer 2/3 findings from
decision.md as a reproducible script (originally run ad hoc via Bash).

Checks:
1. su3_v (G102, octonion vector rep) has an already-orthonormal Gram
   matrix (Tr(Ai^dagger Aj) = delta_ij) -- confirms G102's SVD-based
   nullspace already orthonormalizes.
2. su3_sigma (G15's su(3) on the S6 spinor Sigma) does NOT have an
   orthonormal Gram matrix -- confirms G10-B's plain sympy .nullspace()
   does not orthonormalize, explaining why a naive Casimir sum Xi^dagger Xi
   gives a spurious, non-scalar spectrum for su3_sigma.
3. The PROPERLY-normalized Casimir (using the inverse Gram matrix as
   metric, C2 = sum_ij Ginv_ij Xi^dagger Xj) gives the SAME spectrum for
   both representations, confirming they share the identical abstract
   su(3)-module decomposition (1+1+3+3bar) once computed correctly.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent

G102_PATH = HERE.parent / "20260705-g102-spin8-fiber-obstruction" / "g102_spin8_fiber.py"
_spec_g102 = importlib.util.spec_from_file_location("g102_spin8_fiber", G102_PATH)
assert _spec_g102 and _spec_g102.loader
G102 = importlib.util.module_from_spec(_spec_g102)
_spec_g102.loader.exec_module(G102)

G15_DIR = HERE.parent / "20260619-g15-hypercharge"
sys.path.insert(0, str(G15_DIR))
_spec_g15 = importlib.util.spec_from_file_location(
    "g15_hypercharge", G15_DIR / "g15_hypercharge.py"
)
assert _spec_g15 and _spec_g15.loader
G15 = importlib.util.module_from_spec(_spec_g15)
_spec_g15.loader.exec_module(G15)


def gram_matrix(reps: list[np.ndarray]) -> np.ndarray:
    return np.array([[np.trace(A.conj().T @ B) for B in reps] for A in reps])


def casimir_proper(reps: list[np.ndarray]) -> np.ndarray:
    """C2 = sum_ij (G^-1)_ij Xi^dagger Xj -- the invariant Casimir for a
    possibly-non-orthonormal generator basis."""
    dim = reps[0].shape[0]
    gram = gram_matrix(reps)
    ginv = np.linalg.inv(gram)
    n = len(reps)
    C2 = np.zeros((dim, dim), dtype=complex)
    for i in range(n):
        for j in range(n):
            C2 += ginv[i, j] * reps[i].conj().T @ reps[j]
    return C2


def main() -> None:
    der = G102.derivation_basis()
    su3_v = [A.astype(complex) for A in G102.stabilizer_basis(der)]
    su3_sigma = [np.array(M.evalf(), dtype=complex) for M in G15.su3_spin]

    gram_v = gram_matrix(su3_v).real
    gram_s = gram_matrix(su3_sigma).real

    v_orthonormal = np.allclose(gram_v, gram_v[0, 0] * np.eye(8), atol=1e-6)
    s_orthonormal = np.allclose(gram_s, gram_s[0, 0] * np.eye(8), atol=1e-6)

    print("=" * 92)
    print("Round127 diagnostic -- Gram matrices and properly-normalized Casimir")
    print("=" * 92)
    print(f"su3_v (G102) Gram proportional to identity?     {v_orthonormal}")
    print(f"su3_sigma (G15) Gram proportional to identity?   {s_orthonormal}")
    print()
    print("su3_sigma Gram matrix (expect off-diagonal coupling if non-orthonormal):")
    print(np.round(gram_s, 4))
    print()

    C2v = casimir_proper(su3_v)
    C2s = casimir_proper(su3_sigma)
    ev_v = np.sort(np.linalg.eigvalsh(0.5 * (C2v + C2v.conj().T)).real)
    ev_s = np.sort(np.linalg.eigvalsh(0.5 * (C2s + C2s.conj().T)).real)

    print(f"Properly-normalized Casimir eigenvalues on 8_v   : {np.round(ev_v, 6)}")
    print(f"Properly-normalized Casimir eigenvalues on Sigma : {np.round(ev_s, 6)}")
    spectra_match = np.allclose(ev_v, ev_s, atol=1e-6)
    print(f"\nSpectra match exactly: {spectra_match}")
    print(f"VERDICT: {'SAME_ABSTRACT_SU3_MODULE_TYPE' if spectra_match else 'GENUINE_MISMATCH'}")


if __name__ == "__main__":
    main()
