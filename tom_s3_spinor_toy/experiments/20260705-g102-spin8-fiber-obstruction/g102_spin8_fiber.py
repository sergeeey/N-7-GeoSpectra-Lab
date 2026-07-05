"""G102: hidden Spin(8) in the S3xS6 fiber sector — Path A internal realizability test.

E-L3B killed Path B (G2-equivariant bundles are pairwise isomorphic). G101 killed
the naive G2-padding construction of 8_v. The ONE untested escape: a fiber-level
continuous symmetry larger than the geometric G2, acting on the octonion fiber
O = R^8 and commuting with the geometric structure — which would let Spin(8)-Schur
(Path A) distinguish the three triality channels internally, without a new postulate.

That is a centralizer question, answerable by finite linear algebra:

  S1: Der(O) computed as the FULL Leibniz kernel (not a formula) -> dim 14 = g2,
      and every element is antisymmetric (g2 c so(8)).
  S2: stabilizer of e1 in Der(O) -> dim 8 = su(3) (holonomy of G2/SU(3)).
  S3: centralizer c_so(8)(g2)    -> dim 0  (NO hidden continuous symmetry).
  S4: centralizer c_so(8)(su(3)) -> dim 2, abelian (inner u(1)^2 — cannot permute
      triality labels; triality is OUTER).
  S5: the genuine triality triple built from Cl(0,8): vector rho_v, half-spins
      rho_s, rho_c (chirality split of the 16-dim Cl(0,8) module) — this IS the
      construction G101 called for. Hom_so(8) off-diagonal = 0 (negative control),
      diagonal = 1 (Schur positive control).
  S6: restricted to g2 (which DOES act): Hom_g2(rho_a, rho_b) = 2 for ALL pairs
      -> channels are g2-isomorphic (E-L3B reconfirmed at the so(8) level).
  S7: restricted to su(3) (holonomy): Hom = 6 for ALL pairs -> ditto.

Conclusion if all pass: only so(8) — which does not act on the geometric fiber —
distinguishes the channels; nothing that acts can. Path A needs an INDEPENDENT
fiber Spin(8) postulate. G67-C3's remaining 1/3 is model-building input.

Reuses the verified octonion multiplication table and L/R matrices from G68.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g102.json"

# --- load G68 (verified octonion machinery) by path ------------------------------
G68_PATH = HERE.parent / "20260621-g68-octonion-channels" / "g68_channels.py"
_spec = importlib.util.spec_from_file_location("g68_channels", G68_PATH)
assert _spec and _spec.loader
G68 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G68)

OCT = G68.OCT_TABLE  # 8x8x8: OCT[a,b,c] = coeff of e_c in e_a*e_b
N = 8
TOL = 1e-9


def mult(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Octonion product via the verified G68 table."""
    return np.einsum("abc,a,b->c", OCT, u, v)


# --- S1: Der(O) as the Leibniz kernel --------------------------------------------


def leibniz_operator() -> np.ndarray:
    """Rows: constraints D(e_a e_b) - D(e_a) e_b - e_a D(e_b) = 0, unknowns vec(D).

    D is 8x8, vec by D[c, c'] -> index 8*c + c'. For each (a, b, c):
      sum_{c'} OCT[a,b,c'] D[c,c'] - sum_{a'} OCT[a',b,c] D[a',a] - sum_{b'} OCT[a,b',c] D[b',b] = 0
    """
    rows = []
    for a in range(N):
        for b in range(N):
            for c in range(N):
                row = np.zeros((N, N))
                row[c, :] += OCT[a, b, :]
                row[:, a] -= OCT[:, b, c]
                row[:, b] -= OCT[a, :, c]
                rows.append(row.ravel())
    return np.array(rows)


def nullspace(mat: np.ndarray, tol: float = 1e-8) -> np.ndarray:
    """Orthonormal basis of the nullspace via SVD; rows are basis vectors."""
    _, s, vt = np.linalg.svd(mat, full_matrices=True)
    rank = int(np.sum(s > tol * max(mat.shape) * (s[0] if len(s) else 1.0)))
    return vt[rank:]


def derivation_basis() -> list[np.ndarray]:
    """Basis of Der(O) as 8x8 matrices."""
    basis = nullspace(leibniz_operator())
    return [b.reshape(N, N) for b in basis]


def check_leibniz(mats: list[np.ndarray], n_checks: int = 20, seed: int = 0) -> float:
    """Max residual of D(uv) - D(u)v - u D(v) over random u, v and all D."""
    rng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(n_checks):
        u, v = rng.normal(size=N), rng.normal(size=N)
        uv = mult(u, v)
        for d in mats:
            r = d @ uv - mult(d @ u, v) - mult(u, d @ v)
            worst = max(worst, float(np.max(np.abs(r))))
    return worst


def max_asymmetry(mats: list[np.ndarray]) -> float:
    """Max |D + D^T| over the basis — derivations of O must be antisymmetric."""
    return max(float(np.max(np.abs(d + d.T))) for d in mats)


# --- S2: su(3) = stabilizer of e1 in Der(O) ---------------------------------------


def stabilizer_basis(der: list[np.ndarray], point_index: int = 1) -> list[np.ndarray]:
    """Elements of span(der) annihilating e_{point_index}."""
    e_pt = np.zeros(N)
    e_pt[point_index] = 1.0
    cols = np.array([d @ e_pt for d in der]).T  # 8 x len(der)
    coeffs = nullspace(cols)
    return [sum(c * d for c, d in zip(row, der)) for row in coeffs]


# --- S3/S4: centralizers in so(8) --------------------------------------------------


def so8_basis() -> list[np.ndarray]:
    """Standard antisymmetric basis F_ab = E_ab - E_ba, a<b (28 elements)."""
    basis = []
    for a in range(N):
        for b in range(a + 1, N):
            f = np.zeros((N, N))
            f[a, b] = 1.0
            f[b, a] = -1.0
            basis.append(f)
    return basis


def centralizer_dim(target: list[np.ndarray]) -> tuple[int, list[np.ndarray]]:
    """dim and basis of {A in so(8) : [A, T] = 0 for all T in target}."""
    so8 = so8_basis()
    rows = []
    for t in target:
        for a_basis in so8:
            rows.append((a_basis @ t - t @ a_basis).ravel())
    # unknowns: coefficients over the 28-dim so(8) basis
    mat = np.array(rows).reshape(len(target), len(so8), N * N)
    mat = np.transpose(mat, (0, 2, 1)).reshape(len(target) * N * N, len(so8))
    coeffs = nullspace(mat)
    cent = [sum(c * f for c, f in zip(row, so8_basis())) for row in coeffs]
    return len(cent), cent


def is_abelian(mats: list[np.ndarray]) -> bool:
    return all(float(np.max(np.abs(x @ y - y @ x))) < TOL for x in mats for y in mats)


# --- S5: the genuine triality triple from Cl(0,8) ---------------------------------


def cl8_gammas() -> list[np.ndarray]:
    """16x16 generators of Cl(0,8) ({G_a, G_b} = -2 delta I), doubled from G68's L_i."""
    gammas = []
    zero = np.zeros((N, N))
    for li in G68.L:  # L_1..L_7 satisfy {L_i, L_j} = -2 delta I (G68-D2)
        gammas.append(np.block([[zero, li], [li, zero]]))
    i8 = np.eye(N)
    gammas.append(np.block([[zero, -i8], [i8, zero]]))
    return gammas


def check_clifford(gammas: list[np.ndarray]) -> float:
    """Max |{G_a,G_b} + 2 delta_ab I| over all pairs."""
    ident = np.eye(2 * N)
    worst = 0.0
    for i, gi in enumerate(gammas):
        for j, gj in enumerate(gammas):
            ac = gi @ gj + gj @ gi + 2.0 * (1.0 if i == j else 0.0) * ident
            worst = max(worst, float(np.max(np.abs(ac))))
    return worst


def spin_rep_blocks() -> tuple[list[np.ndarray], list[np.ndarray], list[np.ndarray]]:
    """(vector, spin+, spin-) so(8) generator triples, aligned to the F_ab basis.

    sigma(F_ab) = -1/2 G_a G_b on the 16-dim module. WHY the minus sign: with the
    Cl(0,7)-doubled gammas ({G_a,G_b} = -2 delta), the naive +1/2 G_a G_b satisfies
    [sigma_ab, sigma_bc] = -sigma_ac while [F_ab, F_bc] = +F_ac — an ANTI-homomorphism
    (caught by the bracket-residual control on the first run, residual 9.4). Since
    X -> -X^T = X on antisymmetric X, flipping the sign of every generator yields the
    genuine homomorphism. Chirality Omega_8 = G_1...G_8 (Omega^2 = +I) block-splits
    the module into the two half-spin 8's.
    """
    gammas = cl8_gammas()
    omega = np.eye(2 * N)
    for g in gammas:
        omega = omega @ g
    evals, evecs = np.linalg.eigh(omega)
    minus = evecs[:, evals < 0]
    plus = evecs[:, evals > 0]

    vec, sp, sm = [], [], []
    for a in range(N):
        for b in range(a + 1, N):
            f = np.zeros((N, N))
            f[a, b] = 1.0
            f[b, a] = -1.0
            vec.append(f)
            sigma = -0.5 * gammas[a] @ gammas[b]
            sp.append(plus.T @ sigma @ plus)
            sm.append(minus.T @ sigma @ minus)
    return vec, sp, sm


def check_bracket_homomorphism(seed: int = 1) -> float:
    """sigma([X,Y]) = [sigma(X), sigma(Y)] for random so(8) X, Y (convention gate)."""
    vec, sp, _ = spin_rep_blocks()
    rng = np.random.default_rng(seed)
    x_c, y_c = rng.normal(size=len(vec)), rng.normal(size=len(vec))
    x_v = sum(c * f for c, f in zip(x_c, vec))
    y_v = sum(c * f for c, f in zip(y_c, vec))
    x_s = sum(c * s for c, s in zip(x_c, sp))
    y_s = sum(c * s for c, s in zip(y_c, sp))
    bracket_v = x_v @ y_v - y_v @ x_v
    # decompose bracket_v back onto F_ab basis (orthogonal, norm^2 = 2)
    coeffs = [float(np.sum(bracket_v * f)) / 2.0 for f in vec]
    lhs = sum(c * s for c, s in zip(coeffs, sp))
    rhs = x_s @ y_s - y_s @ x_s
    return float(np.max(np.abs(lhs - rhs)))


def hom_dim(rep_a: list[np.ndarray], rep_b: list[np.ndarray]) -> int:
    """dim of {S : S A_k = B_k S for all k} via the stacked Sylvester kernel."""
    n_a = rep_a[0].shape[0]
    n_b = rep_b[0].shape[0]
    rows = []
    for a_k, b_k in zip(rep_a, rep_b):
        op = np.kron(a_k.T, np.eye(n_b)) - np.kron(np.eye(n_a), b_k)
        rows.append(op)
    return len(nullspace(np.vstack(rows)))


def restrict_to_subalgebra(sub: list[np.ndarray]) -> tuple[list, list, list]:
    """Images of a g c so(8) (given as antisym 8x8 matrices) in the three reps."""
    vec, sp, sm = spin_rep_blocks()
    v_out, s_out, c_out = [], [], []
    for x in sub:
        coeffs = [float(np.sum(x * f)) / 2.0 for f in vec]
        v_out.append(sum(cf * f for cf, f in zip(coeffs, vec)))
        s_out.append(sum(cf * s for cf, s in zip(coeffs, sp)))
        c_out.append(sum(cf * s for cf, s in zip(coeffs, sm)))
    return v_out, s_out, c_out


# --- main -------------------------------------------------------------------------


def main() -> None:
    # S1
    der = derivation_basis()
    p1 = len(der)
    leib = check_leibniz(der)
    asym = max_asymmetry(der)

    # S2
    su3 = stabilizer_basis(der)
    p2 = len(su3)

    # S3 / S4
    p3, _ = centralizer_dim(der)
    p4, cent_su3 = centralizer_dim(su3)
    p4_abelian = is_abelian(cent_su3) if cent_su3 else True

    # S5
    cliff_res = check_clifford(cl8_gammas())
    bracket_res = check_bracket_homomorphism()
    vec, sp, sm = spin_rep_blocks()
    p5 = (hom_dim(vec, sp), hom_dim(vec, sm), hom_dim(sp, sm))
    p6 = (hom_dim(vec, vec), hom_dim(sp, sp), hom_dim(sm, sm))

    # S6 / S7
    reps_g2 = restrict_to_subalgebra(der)
    reps_su3 = restrict_to_subalgebra(su3)
    labels = ("v", "s", "c")
    p7 = {
        f"{la}-{lb}": hom_dim(reps_g2[i], reps_g2[j])
        for i, la in enumerate(labels)
        for j, lb in enumerate(labels)
    }
    p8 = {
        f"{la}-{lb}": hom_dim(reps_su3[i], reps_su3[j])
        for i, la in enumerate(labels)
        for j, lb in enumerate(labels)
    }

    checks = {
        "S1_dim_der": p1,
        "S1_leibniz_residual": leib,
        "S1_max_asymmetry": asym,
        "S2_dim_su3": p2,
        "S3_centralizer_g2": p3,
        "S4_centralizer_su3": p4,
        "S4_abelian": p4_abelian,
        "S5_clifford_residual": cliff_res,
        "S5_bracket_residual": bracket_res,
        "S5_hom_so8_offdiag": p5,
        "S5_hom_so8_diag": p6,
        "S6_hom_g2_pairs": p7,
        "S7_hom_su3_pairs": p8,
    }

    controls_ok = (
        leib < TOL
        and asym < TOL
        and cliff_res < TOL
        and bracket_res < 1e-7
        and p6 == (1, 1, 1)
        and p5 == (0, 0, 0)
    )
    predictions_ok = (
        p1 == 14
        and p2 == 8
        and p3 == 0
        and p4 == 2
        and p4_abelian
        and all(v == 2 for v in p7.values())
        and all(v == 6 for v in p8.values())
    )
    killed_discovery = p3 > 0  # a hidden symmetry would flip the experiment
    killed_inconsistency = any(v == 0 for v in p7.values()) or any(v == 0 for v in p8.values())

    if controls_ok and predictions_ok:
        verdict = "PASS"
    elif killed_discovery:
        verdict = "KILLED_DISCOVERY"
    elif killed_inconsistency:
        verdict = "KILLED_INCONSISTENT_WITH_L3B"
    else:
        verdict = "FAIL"

    results = {
        "gate": "G102",
        "checks": checks,
        "verdict": verdict,
        "interpretation": (
            "No continuous fiber symmetry beyond the geometric g2 exists on the octonion "
            f"fiber (centralizer of g2 in so(8) has dim {p3}); the holonomy centralizer is "
            f"a dim-{p4} abelian (inner) algebra that cannot permute triality labels. The "
            "three genuine so(8) channels (built here explicitly from Cl(0,8), as G101 "
            "required) are distinguished ONLY by so(8) itself, which does not act on the "
            "geometric fiber: restricted to g2 or su(3), all pairs are isomorphic. Path A "
            "(Spin(8)-Schur) therefore requires an INDEPENDENT fiber Spin(8) postulate — "
            "the remaining 1/3 of G67-C3 is model-building input, not derivable from S3xS6."
        ),
    }

    print(f"S1 dim Der(O) = {p1} (predict 14), Leibniz res {leib:.2e}, asym {asym:.2e}")
    print(f"S2 dim stab(e1) = {p2} (predict 8)")
    print(f"S3 dim c_so8(g2) = {p3} (predict 0)")
    print(f"S4 dim c_so8(su3) = {p4} (predict 2), abelian = {p4_abelian}")
    print(f"S5 Cl(0,8) res {cliff_res:.2e}, bracket res {bracket_res:.2e}")
    print(f"S5 Hom_so8 offdiag = {p5} (predict 0,0,0), diag = {p6} (predict 1,1,1)")
    print(f"S6 Hom_g2 pairs  = {sorted(set(p7.values()))} (predict all 2)")
    print(f"S7 Hom_su3 pairs = {sorted(set(p8.values()))} (predict all 6)")
    print(f"\nVERDICT: {verdict}")

    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"Results -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
