"""L3b: does triality act as a genuine order-3 automorphism on SO(4)xSO(4)?

Context: L3B_SPIN8_INTERFACE_SPEC.md SS1.5, "Attempted 2026-07-15, continued
further" (point 3 of the "what remains open" list after the SO(4)xSO(4)
candidate was found in ../20260715-l3b-so4xso4-candidate/). Checks whether
that SO(4)xSO(4) subalgebra of so(8) is genuinely triality-compatible
(mapped to itself by the triality automorphism), or merely a convenient
basis with no such symmetry.

Fully self-contained: builds the octonion multiplication table from scratch
via Cayley-Dickson doubling of the quaternions, and the 14-dim g2=Der(O)
basis via the derivation equation, rather than depending on any external
scratch files.

Construction: Baez, "The Octonions," arXiv:math/0105155, SS2.4 "Spinors and
Trialities" -- for n=8 the normed triality trilinear map is realized by
octonion multiplication itself. Differentiating the group-level covariance
relation gives, for a,b,c in so(8) acting on V=S+=S-=O:

    a(x).y + x.b(y) = c(x.y)      for all x,y in O
"""

import numpy as np

# ---------------------------------------------------------------------------
# Quaternion multiplication table (basis 1, i, j, k)
# ---------------------------------------------------------------------------

_Q = np.zeros((4, 4, 4))
_QUAT_MULT = {
    (0, 0): (1, 0),
    (0, 1): (1, 1),
    (0, 2): (1, 2),
    (0, 3): (1, 3),
    (1, 0): (1, 1),
    (1, 1): (-1, 0),
    (1, 2): (1, 3),
    (1, 3): (-1, 2),
    (2, 0): (1, 2),
    (2, 1): (-1, 3),
    (2, 2): (-1, 0),
    (2, 3): (1, 1),
    (3, 0): (1, 3),
    (3, 1): (1, 2),
    (3, 2): (-1, 1),
    (3, 3): (-1, 0),
}
for (_a, _b), (_sign, _c) in _QUAT_MULT.items():
    _Q[_a, _b, _c] = _sign


def _qmul(x, y):
    return np.einsum("...a,...b,abc->...c", x, y, _Q)


def _qconj(x):
    out = x.copy()
    out[..., 1:] *= -1
    return out


def _cd_mul(pair1, pair2):
    """Cayley-Dickson doubling: (a,b)*(c,d) = (ac - dbar*b, d*a + b*cbar)."""
    a, b = pair1
    c, d = pair2
    return _qmul(a, c) - _qmul(_qconj(d), b), _qmul(d, a) + _qmul(b, _qconj(c))


def build_octonion_table():
    """C8[i,j,k]: e_i * e_j = sum_k C8[i,j,k] e_k, via Cayley-Dickson doubling."""
    qbasis = [np.eye(4)[i] for i in range(4)]
    zero4 = np.zeros(4)

    def octonion_basis(i):
        if i < 4:
            return (qbasis[i].copy(), zero4.copy())
        return (zero4.copy(), qbasis[i - 4].copy())

    c8 = np.zeros((8, 8, 8))
    for i in range(8):
        for j in range(8):
            a, b = _cd_mul(octonion_basis(i), octonion_basis(j))
            c8[i, j] = np.concatenate([a, b])
    return c8


C8 = build_octonion_table()


def octonion_table_is_division_algebra(n_trials=50, seed=0):
    """Spot-check |xy| = |x||y| for random vectors (division algebra property)."""
    rng = np.random.default_rng(seed)
    for _ in range(n_trials):
        x = rng.standard_normal(8)
        y = rng.standard_normal(8)
        xy = np.einsum("i,j,ijk->k", x, y, C8)
        if not np.isclose(np.linalg.norm(xy), np.linalg.norm(x) * np.linalg.norm(y), rtol=1e-6):
            return False
    return True


# ---------------------------------------------------------------------------
# g2 = Der(O): 14-dim null space of the derivation equation D(xy)=D(x)y+xD(y)
# ---------------------------------------------------------------------------


def build_g2_basis():
    """Solve for the null space of the derivation-equation linear map, returns (14,8,8)."""
    n = 8
    # Unknowns: D (8x8, 64 entries). Equation: D(e_i e_j) = D(e_i)e_j + e_i D(e_j)
    # for all basis pairs i,j -> linear constraints on the 64 entries of D.
    constraints = []
    for i in range(n):
        for j in range(n):
            # constraint vector over the 64 unknowns D[a,b], for one output component
            # D(e_i*e_j)_k - (D(e_i)*e_j)_k - (e_i*D(e_j))_k = 0  for each k
            for k in range(n):
                vec = np.zeros((n, n))
                # D(e_i*e_j)_k = sum_b D[k,b] * C8[i,j,b]
                vec[k, :] += C8[i, j, :]
                # (D(e_i)*e_j)_k = sum_b D(e_i)_b * C8[b,j,k] = sum_{a} D[a,i]... careful:
                # D(e_i) has components (D(e_i))_b = sum_c D[b,c] * (e_i)_c = D[b,i]
                # (D(e_i)*e_j)_k = sum_b (D(e_i))_b * C8[b,j,k] = sum_b D[b,i]*C8[b,j,k]
                for b in range(n):
                    vec[b, i] -= C8[b, j, k]
                # (e_i*D(e_j))_k = sum_b (e_i)_b_contribution... e_i*D(e_j) means
                # multiply e_i by the vector D(e_j); (e_i * w)_k = sum_c C8[i,c,k]*w_c
                # here w = D(e_j), w_c = D[c,j]
                for c in range(n):
                    vec[c, j] -= C8[i, c, k]
                constraints.append(vec.reshape(-1))
    constraints = np.array(constraints)  # (8*8*8, 64)
    _u, s, vt = np.linalg.svd(constraints)
    tol = 1e-9
    n_null = 64 - int(np.sum(s > tol))
    null_basis = vt[64 - n_null :]
    return null_basis.reshape(-1, n, n)


G2_BASIS = build_g2_basis()

BLOCK1 = [0, 1, 2, 3]  # H
BLOCK2 = [4, 5, 6, 7]  # Hl


def solve_triality_partners(a):
    """Given a (8x8), solve for b,c satisfying a(x).y + x.b(y) = c(x.y) for all x,y.

    Returns (b, c, max_residual) via least squares on the linear system.
    """
    n = 8
    term1 = np.einsum("ip,iqk->kpq", a, C8)
    lhs_matrix = np.zeros((n * n * n, 2 * n * n))
    rhs_known = -term1.reshape(-1)

    idx = 0
    for k in range(n):
        for p in range(n):
            for q in range(n):
                row = np.zeros(2 * n * n)
                for j in range(n):
                    row[j * n + q] += C8[p, j, k]
                for ell in range(n):
                    row[n * n + k * n + ell] -= C8[p, q, ell]
                lhs_matrix[idx] = row
                idx += 1

    sol, _, _, _ = np.linalg.lstsq(lhs_matrix, rhs_known, rcond=None)
    residual = np.max(np.abs(lhs_matrix @ sol - rhs_known))
    b = sol[: n * n].reshape(n, n)
    c = sol[n * n :].reshape(n, n)
    return b, c, residual


def build_so4xso4_basis():
    """12 antisymmetric matrices: block-diagonal rotations of block1 and block2 separately."""
    basis = []
    for blk in (BLOCK1, BLOCK2):
        for ii in range(4):
            for jj in range(ii + 1, 4):
                mat = np.zeros((8, 8))
                mat[blk[ii], blk[jj]] = 1
                mat[blk[jj], blk[ii]] = -1
                basis.append(mat)
    return np.array(basis)


def coords_in_basis(mat, basis_flat):
    coeffs, _, _, _ = np.linalg.lstsq(basis_flat.T, mat.reshape(64), rcond=None)
    return coeffs


def residual_in_span(mat, basis_flat):
    coeffs = coords_in_basis(mat, basis_flat)
    recon = basis_flat.T @ coeffs
    return np.max(np.abs(recon - mat.reshape(64)))


def g2_sanity_check_residual():
    """For a known g2 derivation, solving the covariance eq. must give b=c=a."""
    a = G2_BASIS[0]
    b, c, _ = solve_triality_partners(a)
    return max(np.max(np.abs(b - a)), np.max(np.abs(c - a)))


def build_triality_matrix_T():
    """12x12 matrix representing a -> b restricted to so(4)_1 (+) so(4)_2."""
    basis = build_so4xso4_basis()
    basis_flat = basis.reshape(12, 64)
    t_matrix = np.zeros((12, 12))
    max_partner_residual = 0.0
    for i, a in enumerate(basis):
        b, _, _ = solve_triality_partners(a)
        max_partner_residual = max(max_partner_residual, residual_in_span(b, basis_flat))
        t_matrix[:, i] = coords_in_basis(b, basis_flat)
    return t_matrix, max_partner_residual


if __name__ == "__main__":
    print(
        "Octonion table is a division algebra (|xy|=|x||y| spot check):",
        octonion_table_is_division_algebra(),
    )
    print("dim(g2) =", G2_BASIS.shape[0], "(expect 14)")
    print("G2 sanity check (b=c=a for a known g2 element):", g2_sanity_check_residual())

    T, max_partner_residual = build_triality_matrix_T()
    print(
        "Max residual of b staying inside so(4)+so(4) span (all 12 generators):",
        max_partner_residual,
    )

    evals = np.linalg.eigvals(T)
    print("\nEigenvalues of T (a -> b restricted to so(4)+so(4)):")
    for ev in sorted(evals, key=lambda z: (round(z.real, 4), round(z.imag, 4))):
        print(f"  {ev.real:+.4f} {ev.imag:+.4f}j")

    T3 = T @ T @ T
    print("\nT^3 == I:", np.allclose(T3, np.eye(12), atol=1e-6))
    n_plus1 = int(round(sum(1 for ev in evals if abs(ev.real - 1) < 1e-6 and abs(ev.imag) < 1e-6)))
    print("Number of +1 eigenvalues:", n_plus1, "(expect 6, matching dim Stab_G2(H))")
