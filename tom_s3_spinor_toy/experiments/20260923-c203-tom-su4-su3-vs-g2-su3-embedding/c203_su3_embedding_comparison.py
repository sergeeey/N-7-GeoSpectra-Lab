r"""C203: does Tom Lawrence's SU(3)<->SU(4)~SO(6) embedding coincide with
this project's own G2/SU(3)-on-S6 embedding, as a real 6-dim orthogonal
representation of su(3), up to conjugation?

Side A (ours): reuse `g96_g2_su3.py` (VERIFIED, 2026-06-26) unmodified --
G2 as derivations of the octonion algebra, SU(3) = stabilizer of e6 in
Im(O), restricted to its action on the 6-dim tangent space {v : v.e6=0}.

Side B (Tom's): build SU(4)~Spin(6) explicitly via a Cl(6) gamma-matrix
representation (8x8, tensor products of Pauli matrices, anticommutation
verified numerically before use), project to one 4-dim chirality to get
the su(4) fundamental, invert the standard so(6)<->su(4) Lie-algebra
isomorphism M_ab <-> (i/4)[Gamma_a,Gamma_b]|_chiral to express the
block-embedded su(3)~su(4) generators (upper-left 3x3, i.e. su(3)+u(1)
inside su(4)) as elements of so(6).

Then: search for an orthogonal intertwiner between Side A's and Side B's
8 generators (both 6x6 real antisymmetric); independently cross-check via
the eigenvalue spectrum of a generic Cartan element (basis-free, does not
depend on finding the intertwiner first); run a negative control against
G10-B's DIFFERENT, already-known su(3)-in-so(6) embedding.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parent.parent
G96_PATH = PROJECT_ROOT / "experiments" / "20260626-g96-s6-g2-su3" / "g96_g2_su3.py"
G10B_PATH = PROJECT_ROOT / "experiments" / "20260618-g10b-su3-in-so6" / "g10b_su3_explicit.py"


def _import_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


# --- Side A: reuse G96 unmodified, restrict su(3) generators to the 6-dim
# tangent space at e6 (the orthogonal complement of e6 in R^7).


def side_a_g2_su3_on_tangent_space() -> dict:
    g96 = _import_module(G96_PATH, "g96_reused")

    phi = g96.build_phi()
    gens = g96.find_g2_generators(phi)
    assert len(gens) == 14, f"G96 reuse broken: expected dim(G2)=14, got {len(gens)}"

    e6 = np.zeros(7)
    e6[6] = 1.0

    a_stab = np.column_stack([g @ e6 for g in gens])
    _, sv_stab, vt_stab = np.linalg.svd(a_stab, full_matrices=True)
    rank_stab = int(np.sum(sv_stab > 1e-10))
    null_coeffs = vt_stab[rank_stab:]

    gen_matrix = np.array([g.flatten() for g in gens])
    su3_gens_flat = null_coeffs @ gen_matrix
    su3_gens = [row.reshape(7, 7) for row in su3_gens_flat]
    assert len(su3_gens) == 8, f"G96 reuse broken: expected dim(su3)=8, got {len(su3_gens)}"

    stab_err = max(float(np.max(np.abs(g @ e6))) for g in su3_gens)
    assert stab_err < 1e-8, f"G96 reuse broken: su3 generators do not stabilize e6, err={stab_err}"

    # Orthonormal basis of the 6-dim tangent space V = {v in R^7 : v . e6 = 0}.
    basis7 = np.eye(7)
    v_basis = basis7[:, :6]  # standard e1..e6 already spans e6^perp since e6=(0,...,0,1)

    su3_on_v = []
    for g in su3_gens:
        restricted = v_basis.T @ g @ v_basis  # 6x6
        # sanity: g must map V into V (antisymmetric g stabilizing e6 does)
        leak = float(np.max(np.abs(g @ v_basis - v_basis @ restricted)))
        assert leak < 1e-8, f"su3 generator does not preserve tangent space, leak={leak}"
        su3_on_v.append(restricted)

    return {
        "su3_on_v": su3_on_v,
        "dim_g2": len(gens),
        "dim_su3": len(su3_gens),
        "stab_err": stab_err,
    }


# --- Side B: build su(3) block-embedded in su(4), map to so(6) via the
# Cl(6) gamma-matrix isomorphism.

PAULI = {
    "0": np.eye(2, dtype=complex),
    "1": np.array([[0, 1], [1, 0]], dtype=complex),
    "2": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "3": np.array([[1, 0], [0, -1]], dtype=complex),
}


def kron3(a: str, b: str, c: str) -> np.ndarray:
    return np.kron(np.kron(PAULI[a], PAULI[b]), PAULI[c])


def build_cl6_gammas() -> list[np.ndarray]:
    """Six mutually anticommuting 8x8 Hermitian gamma matrices, Cl(6)."""
    gammas = [
        kron3("1", "0", "0"),
        kron3("2", "0", "0"),
        kron3("3", "1", "0"),
        kron3("3", "2", "0"),
        kron3("3", "3", "1"),
        kron3("3", "3", "2"),
    ]
    return gammas


def verify_clifford_algebra(gammas: list[np.ndarray]) -> float:
    max_err = 0.0
    n = len(gammas)
    for a in range(n):
        for b in range(n):
            anticomm = gammas[a] @ gammas[b] + gammas[b] @ gammas[a]
            target = 2 * np.eye(8) if a == b else np.zeros((8, 8))
            max_err = max(max_err, float(np.max(np.abs(anticomm - target))))
        herm_err = float(np.max(np.abs(gammas[a] - gammas[a].conj().T)))
        max_err = max(max_err, herm_err)
    return max_err


def build_chirality_projector(gammas: list[np.ndarray]) -> np.ndarray:
    g7 = 1j * gammas[0] @ gammas[1] @ gammas[2] @ gammas[3] @ gammas[4] @ gammas[5]
    return g7


def side_b_su4_su3_via_gammas() -> dict:
    gammas = build_cl6_gammas()
    clifford_err = verify_clifford_algebra(gammas)
    assert clifford_err < 1e-10, f"Cl(6) construction broken, err={clifford_err}"

    chirality = build_chirality_projector(gammas)
    chirality_sq_err = float(np.max(np.abs(chirality @ chirality - np.eye(8))))
    assert chirality_sq_err < 1e-10, f"chirality^2 != 1, err={chirality_sq_err}"
    # chirality must anticommute with every gamma (else the projection is not chiral)
    anticomm_err = max(float(np.max(np.abs(chirality @ g + g @ chirality))) for g in gammas)
    assert anticomm_err < 1e-10, f"chirality does not anticommute with gammas, err={anticomm_err}"

    eigvals, eigvecs = np.linalg.eigh(chirality)
    plus_indices = np.where(eigvals > 0)[0]
    assert len(plus_indices) == 4, f"expected 4-dim chiral subspace, got {len(plus_indices)}"
    p_basis = eigvecs[:, plus_indices]  # 8x4, orthonormal columns spanning P+ subspace

    def restrict_to_chiral(mat8: np.ndarray) -> np.ndarray:
        return p_basis.conj().T @ mat8 @ p_basis

    # so(6) <-> su(4) dictionary: for each pair a<b, M_ab (1/4)[Gamma_a,Gamma_b]|_P+.
    # [Gamma_a,Gamma_b] is itself anti-Hermitian (Hermitian Gammas), so NO extra
    # factor of i here -- an earlier draft used (i/4)[.] (Hermitian, "physics
    # generator" convention) which does not land in su(4)'s anti-Hermitian
    # convention; caught immediately by the herm_err assertion below.
    pairs = [(a, b) for a in range(6) for b in range(a + 1, 6)]
    su4_basis_from_so6 = []
    for a, b in pairs:
        comm = gammas[a] @ gammas[b] - gammas[b] @ gammas[a]
        su4_elem = restrict_to_chiral(comm / 4)
        su4_basis_from_so6.append(su4_elem)

    # each su4_elem must be anti-Hermitian (element of u(4), and traceless -> su(4))
    for elem in su4_basis_from_so6:
        herm_err = float(np.max(np.abs(elem + elem.conj().T)))
        trace_err = float(np.abs(np.trace(elem)))
        assert herm_err < 1e-8 and trace_err < 1e-8, "so(6)->su(4) map does not land in su(4)"

    # Gell-Mann matrices (standard su(3) generators, normalized lambda_a, a=1..8)
    gell_mann = [
        np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex),
        np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex),
        np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex),
        np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex),
        np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex),
        np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex),
        np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex),
        (1 / np.sqrt(3)) * np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex),
    ]

    # su(3) block-embedded in su(4): X_a = i * diag_block(lambda_a/2, 0)
    su3_in_su4 = []
    for lam in gell_mann:
        block = 1j * (lam / 2)
        embedded = np.zeros((4, 4), dtype=complex)
        embedded[:3, :3] = block
        su3_in_su4.append(embedded)
        herm_err = float(np.max(np.abs(embedded + embedded.conj().T)))
        assert herm_err < 1e-10

    # Solve each su3_in_su4[a] as a REAL linear combination of the 15
    # su4_basis_from_so6 elements -> gives the so(6) coefficients directly.
    basis_flat = np.column_stack([m.flatten() for m in su4_basis_from_so6])  # 16 x 15, complex
    su3_so6_gens = []
    max_recon_err = 0.0
    max_imag_coeff = 0.0
    for target in su3_in_su4:
        coeffs, *_ = np.linalg.lstsq(basis_flat, target.flatten(), rcond=None)
        recon = (basis_flat @ coeffs).reshape(4, 4)
        recon_err = float(np.max(np.abs(recon - target)))
        max_recon_err = max(max_recon_err, recon_err)
        max_imag_coeff = max(max_imag_coeff, float(np.max(np.abs(coeffs.imag))))

        so6_mat = np.zeros((6, 6))
        for (a, b), c in zip(pairs, coeffs.real, strict=True):
            so6_mat[a, b] = c
            so6_mat[b, a] = -c
        su3_so6_gens.append(so6_mat)

    return {
        "su3_so6_gens": su3_so6_gens,
        "clifford_err": clifford_err,
        "chirality_sq_err": chirality_sq_err,
        "anticomm_err": anticomm_err,
        "max_recon_err": max_recon_err,
        "max_imag_coeff": max_imag_coeff,
    }


# --- Comparison: orthogonal intertwiner search + Cartan-spectrum cross-check.


def commutator(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def verify_closure(gens: list[np.ndarray], label: str) -> float:
    basis_flat = np.column_stack([g.flatten() for g in gens])
    max_err = 0.0
    for gi in gens:
        for gj in gens:
            c = commutator(gi, gj)
            coeffs, *_ = np.linalg.lstsq(basis_flat, c.flatten(), rcond=None)
            recon = (basis_flat @ coeffs).reshape(gi.shape)
            max_err = max(max_err, float(np.max(np.abs(c - recon))))
    return max_err


def cartan_spectrum(gens: list[np.ndarray], seed: int) -> np.ndarray:
    """Eigenvalues (as |imaginary parts|, sorted) of a GENERIC real linear
    combination of generators. NOTE (added after the first run): this is
    NOT basis-independent by itself -- comparing raw spectra from two
    INDEPENDENTLY-drawn random combinations in two unrelated generator bases
    is meaningless without matching normalization/direction first. Kept as
    an illustrative secondary check only; `casimir_ratio` below is the
    actual rigorous, basis-independent invariant used for the verdict."""
    rng = np.random.default_rng(seed)
    coeffs = rng.normal(size=len(gens))
    combo = sum(c * g for c, g in zip(coeffs, gens, strict=True))
    eigvals = np.linalg.eigvals(combo)
    return np.sort(np.abs(eigvals.imag))


def structure_constants(gens: list[np.ndarray]) -> np.ndarray:
    """f_ijk with [T_i,T_j] = sum_k f_ijk T_k, solved by least squares
    against the (assumed already-verified-closed) generator basis."""
    n = len(gens)
    basis_flat = np.column_stack([g.flatten() for g in gens])
    f = np.zeros((n, n, n))
    for i in range(n):
        for j in range(n):
            c = commutator(gens[i], gens[j])
            coeffs, *_ = np.linalg.lstsq(basis_flat, c.flatten(), rcond=None)
            f[i, j, :] = coeffs
    return f


def casimir_ratio(gens: list[np.ndarray]) -> dict:
    """Basis- and normalization-INDEPENDENT invariant: ratio of the quadratic
    Casimir's eigenvalue on the given (`gens`-carried) representation to its
    eigenvalue on the adjoint representation, built from the SAME structure
    constants. For su(3), the fundamental representation "3" (and its
    conjugate "3bar") has ratio C2(3)/C2(adjoint) = (4/3)/3 = 4/9 in the
    standard normalization -- but this function never assumes that value; it
    only requires that the Casimir be scalar (checked explicitly) on the
    representation carried by `gens`, then reports the ratio. Because both
    Casimirs are built from the IDENTICAL structure constants and the IDENTICAL
    (arbitrary) Killing-form normalization, that normalization cancels exactly
    in the ratio -- this is what makes the ratio comparable across two
    completely unrelated generator bases, unlike a raw spectrum."""
    n = len(gens)
    f = structure_constants(gens)
    # ad(T_i)_{jk} = f_{ijk}
    ad = [f[i] for i in range(n)]  # each n x n
    killing = np.array([[np.trace(ad[i] @ ad[j]) for j in range(n)] for i in range(n)])
    killing_inv = np.linalg.inv(killing)

    dim_rep = gens[0].shape[0]
    casimir_rep = np.zeros((dim_rep, dim_rep))
    for i in range(n):
        for j in range(n):
            casimir_rep += killing_inv[i, j] * (gens[i] @ gens[j])

    casimir_adj = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            casimir_adj += killing_inv[i, j] * (ad[i] @ ad[j])

    rep_eigs = np.linalg.eigvalsh((casimir_rep + casimir_rep.T) / 2)
    adj_eigs = np.linalg.eigvalsh((casimir_adj + casimir_adj.T) / 2)
    rep_scalar_defect = float(np.max(rep_eigs) - np.min(rep_eigs))
    adj_scalar_defect = float(np.max(adj_eigs) - np.min(adj_eigs))
    lambda_rep = float(np.mean(rep_eigs))
    lambda_adj = float(np.mean(adj_eigs))

    return {
        "lambda_rep": lambda_rep,
        "lambda_adj": lambda_adj,
        "ratio": lambda_rep / lambda_adj if abs(lambda_adj) > 1e-12 else None,
        "rep_scalar_defect": rep_scalar_defect,
        "adj_scalar_defect": adj_scalar_defect,
        "killing_det": float(np.linalg.det(killing)),
    }


def solve_intertwiner_nullspace(gens_a: list[np.ndarray], gens_b: list[np.ndarray]) -> np.ndarray:
    """Solve the LINEAR system A_i U = U B_i (i=1..8) for U (n x n real),
    via SVD null space -- same linear-algebra approach as C201/C202's
    intertwiner search, not a heuristic optimizer (which could report a
    false NO_INTERTWINER from getting stuck, not from genuine inequivalence).
    Returns an orthonormal basis (columns) for the solution space, as
    length-n^2 vectors."""
    n = gens_a[0].shape[0]
    rows = []
    for a, b in zip(gens_a, gens_b, strict=True):
        # (A U - U B)_{ij} = sum_k A_ik U_kj - sum_k U_ik B_kj = 0
        # as a linear map on vec(U) (row-major flatten, U_{ij} at index i*n+j).
        m = np.kron(a, np.eye(n)) - np.kron(np.eye(n), b.T)
        rows.append(m)
    big_m = np.vstack(rows)
    _, s, vt = np.linalg.svd(big_m)
    tol = 1e-8 * s[0] if len(s) and s[0] > 0 else 1e-8
    rank = int(np.sum(s > tol))
    null_basis = vt[rank:]  # (n^2 - rank) x n^2
    return null_basis


def search_orthogonal_intertwiner(gens_a: list[np.ndarray], gens_b: list[np.ndarray]) -> dict:
    """Find the intertwiner solution space exactly (linear algebra), then
    search WITHIN that space (not over all orthogonal matrices blindly) for
    a member that is orthogonal up to real scale -- i.e. U^T U proportional
    to the identity. Handles both a 1-dim solution space (real-type
    commutant) and a 2-dim one (complex-type commutant, expected here since
    3+3bar admits an invariant complex structure) via a fine angular scan."""
    n = gens_a[0].shape[0]
    null_basis = solve_intertwiner_nullspace(gens_a, gens_b)
    n_free = null_basis.shape[0]

    if n_free == 0:
        return {
            "n_free": 0,
            "best_err": np.inf,
            "best_u": None,
            "orthogonal_found": False,
            "best_conformality_defect": np.inf,
        }

    def matrix_from_coeffs(coeffs: np.ndarray) -> np.ndarray:
        vec = coeffs @ null_basis
        return vec.reshape(n, n)

    def conformality_defect(u: np.ndarray) -> float:
        gram = u.T @ u
        scale = np.trace(gram) / n
        if scale <= 1e-12:
            return np.inf
        return float(np.max(np.abs(gram - scale * np.eye(n)))) / scale

    best_defect = np.inf
    best_u = None
    if n_free == 1:
        candidates = [np.array([1.0])]
    else:
        angles = np.linspace(0, np.pi, 361)
        candidates = [np.array([np.cos(t), np.sin(t)] + [0.0] * (n_free - 2)) for t in angles]
        # also scan pairing across all free-dimension pairs, not just first two
        for i in range(n_free):
            for j in range(i + 1, n_free):
                for t in np.linspace(0, np.pi, 91):
                    c = np.zeros(n_free)
                    c[i], c[j] = np.cos(t), np.sin(t)
                    candidates.append(c)

    for coeffs in candidates:
        u_raw = matrix_from_coeffs(coeffs)
        defect = conformality_defect(u_raw)
        if defect < best_defect:
            best_defect = defect
            best_u = u_raw

    orthogonal_found = best_defect < 1e-6
    err = np.inf
    u_ortho = None
    if orthogonal_found and best_u is not None:
        scale = np.sqrt(np.trace(best_u.T @ best_u) / n)
        u_ortho = best_u / scale
        err = max(
            float(np.max(np.abs(u_ortho.T @ a @ u_ortho - b)))
            for a, b in zip(gens_a, gens_b, strict=True)
        )

    return {
        "n_free": n_free,
        "best_conformality_defect": best_defect,
        "orthogonal_found": orthogonal_found,
        "best_err": err,
        "best_u": u_ortho.tolist() if u_ortho is not None else None,
    }


def main() -> None:
    results: dict = {}

    side_a = side_a_g2_su3_on_tangent_space()
    results["side_a"] = {
        "dim_g2": side_a["dim_g2"],
        "dim_su3": side_a["dim_su3"],
        "stab_err": side_a["stab_err"],
    }
    su3_a = side_a["su3_on_v"]
    closure_a = verify_closure(su3_a, "side_a")
    results["side_a"]["closure_err"] = closure_a

    side_b = side_b_su4_su3_via_gammas()
    results["side_b"] = {
        "clifford_err": side_b["clifford_err"],
        "chirality_sq_err": side_b["chirality_sq_err"],
        "anticomm_err": side_b["anticomm_err"],
        "max_recon_err": side_b["max_recon_err"],
        "max_imag_coeff": side_b["max_imag_coeff"],
    }
    su3_b = side_b["su3_so6_gens"]
    closure_b = verify_closure(su3_b, "side_b")
    results["side_b"]["closure_err"] = closure_b

    # Negative control: G10-B's DIFFERENT su(3)-in-so(6) embedding, reused
    # directly via its own `su3_generators()` function (not reimplemented).
    g10b = _import_module(G10B_PATH, "g10b_reused")
    su3_c_sympy = g10b.su3_generators()
    su3_c = [np.array(g.tolist(), dtype=float) for g in su3_c_sympy]
    assert len(su3_c) == 8, f"G10-B reuse broken: expected 8 generators, got {len(su3_c)}"
    closure_c = verify_closure(su3_c, "g10b_control")
    results["g10b_negative_control"] = {"dim": len(su3_c), "closure_err": closure_c}

    intertwiner_ab = search_orthogonal_intertwiner(su3_a, su3_b)
    results["intertwiner_a_vs_b"] = intertwiner_ab

    intertwiner_a_vs_c = search_orthogonal_intertwiner(su3_a, su3_c)
    results["intertwiner_a_vs_c_NEGATIVE_CONTROL"] = intertwiner_a_vs_c

    spectrum_a = cartan_spectrum(su3_a, seed=42)
    spectrum_b = cartan_spectrum(su3_b, seed=42)
    spectrum_c = cartan_spectrum(su3_c, seed=42)
    results["cartan_spectrum_ILLUSTRATIVE_ONLY"] = {
        "spectrum_a": spectrum_a.tolist(),
        "spectrum_b": spectrum_b.tolist(),
        "spectrum_c_g10b": spectrum_c.tolist(),
        "max_diff_a_vs_b": float(np.max(np.abs(spectrum_a - spectrum_b))),
        "max_diff_a_vs_c": float(np.max(np.abs(spectrum_a - spectrum_c))),
    }

    # The actual rigorous, basis-independent verdict test.
    casimir_a = casimir_ratio(su3_a)
    casimir_b = casimir_ratio(su3_b)
    casimir_c = casimir_ratio(su3_c)
    results["casimir_ratio"] = {"A": casimir_a, "B": casimir_b, "C_g10b": casimir_c}

    out_path = HERE / "results_c203.json"
    out_path.write_text(json.dumps(results, indent=2, default=str))

    print("=== Side A (G96 reuse: G2/SU(3) on S6 tangent space) ===")
    print(f"  dim(G2)={results['side_a']['dim_g2']}, dim(su3)={results['side_a']['dim_su3']}")
    print(f"  stabilizer err={results['side_a']['stab_err']:.2e}, closure err={closure_a:.2e}")

    print("\n=== Side B (Tom's SU(3) subset SU(4) ~ SO(6) via Cl(6) gammas) ===")
    print(f"  Clifford err={side_b['clifford_err']:.2e}")
    print(
        f"  chirality^2 err={side_b['chirality_sq_err']:.2e}, anticomm err={side_b['anticomm_err']:.2e}"
    )
    print(
        f"  reconstruction err={side_b['max_recon_err']:.2e}, max imag coeff={side_b['max_imag_coeff']:.2e}"
    )
    print(f"  closure err={closure_b:.2e}")

    print("\n=== G10-B negative control (different, known su(3)-in-so(6) embedding) ===")
    print(f"  dim={results['g10b_negative_control']['dim']}, closure err={closure_c:.2e}")

    print(
        "\n=== Naive index-matched intertwiner search (NOT conclusive alone --"
        " no known generator correspondence between A and B/C bases) ==="
    )
    print(
        f"  A vs B: n_free={intertwiner_ab['n_free']}, orthogonal_found={intertwiner_ab['orthogonal_found']}"
    )
    print(
        f"  A vs C: n_free={intertwiner_a_vs_c['n_free']}, orthogonal_found={intertwiner_a_vs_c['orthogonal_found']}"
    )

    print("\n=== Rigorous, basis-independent verdict test: Casimir(rep)/Casimir(adjoint) ratio ===")
    for label, cr in (
        ("A (ours, G96)", casimir_a),
        ("B (Tom's, SU(4))", casimir_b),
        ("C (G10-B, control)", casimir_c),
    ):
        print(
            f"  {label}: ratio={cr['ratio']:.6f}  "
            f"(rep scalar defect={cr['rep_scalar_defect']:.2e}, "
            f"adj scalar defect={cr['adj_scalar_defect']:.2e})"
        )
    print(f"  Theoretical value for su(3) fundamental 3(+3bar): 4/9 = {4 / 9:.6f}")
    print(f"  |ratio_A - ratio_B| = {abs(casimir_a['ratio'] - casimir_b['ratio']):.2e}")
    print(f"  |ratio_A - ratio_C| = {abs(casimir_a['ratio'] - casimir_c['ratio']):.2e}")


if __name__ == "__main__":
    main()
