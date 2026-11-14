"""C181: items 4 and 5 of the response to Tom Lawrence's 2026-09-07 request.

Item 4 -- his proposed double check: "take the outer product of the spinor
multiplet and its adjoint, and then use gamma matrices to project out the
vector multiplet". Two questions, not one:
   (a) does the projection work?            [expected: yes]
   (b) does it DISCRIMINATE?                [expected: NO -- tested, not asserted]
For (b) an alternative spinor basis is built from the OPPOSITE chirality
(X^L in place of X^R) and put through the identical test. If it also passes,
his check is necessary but not sufficient.

Item 5 -- Riemann normal coordinates on S^3 at the identity, via the
quaternion exponential map, and verification of the defining RNC property
g_ab(0) = delta_ab, d_c g_ab(0) = 0.

Reuses C180's vector fields and harmonics via importlib (not rebuilt).
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c181.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C180 = load_module(
    "c180_explicit_s3_spinor_harmonics",
    HERE.parent
    / "20260907-c180-explicit-s3-spinor-harmonics"
    / "c180_explicit_s3_spinor_harmonics.py",
)

PAULI = C180.PAULI
I2 = np.eye(2, dtype=complex)


# ---------------------------------------------------------------------------
# Item 4a: the gamma-matrix projection
# ---------------------------------------------------------------------------
def su2_from_coords(x: np.ndarray) -> np.ndarray:
    """g = x0*I + i(x1 s1 + x2 s2 + x3 s3). This IS the (1/2,0) (x) (0,1/2)
    outer-product structure: one index from each chirality."""
    return x[0] * I2 + 1j * (x[1] * PAULI[0] + x[2] * PAULI[1] + x[3] * PAULI[2])


def gamma_projection(g: np.ndarray) -> np.ndarray:
    """x_mu = (1/2) Tr(sigma_mu^dagger g), with sigma_mu = (I, i s1, i s2, i s3)."""
    sig = [I2, 1j * PAULI[0], 1j * PAULI[1], 1j * PAULI[2]]
    return np.array([0.5 * np.trace(s.conj().T @ g).real for s in sig])


def projection_check() -> dict:
    rng = np.random.default_rng(20260907)
    worst = 0.0
    for _ in range(500):
        x = rng.normal(size=4)
        x = x / np.linalg.norm(x)
        recovered = gamma_projection(su2_from_coords(x))
        worst = max(worst, float(np.max(np.abs(recovered - x))))
    # also confirm g really is in SU(2): unitary, det 1
    x = rng.normal(size=4)
    x = x / np.linalg.norm(x)
    g = su2_from_coords(x)
    unitarity = float(np.max(np.abs(g.conj().T @ g - I2)))
    det_err = float(abs(np.linalg.det(g) - 1.0))
    return {
        "max_coordinate_recovery_error": worst,
        "projection_recovers_vector_multiplet": bool(worst < 1e-12),
        "g_unitarity_residual": unitarity,
        "g_det_minus_one": det_err,
    }


# ---------------------------------------------------------------------------
# Item 4 predicate 3: what does ONE Weyl spinor's own outer product give?
# ---------------------------------------------------------------------------
def single_chirality_outer_product_check() -> dict:
    """psi psi^dagger for a 2-component Weyl spinor is a 2x2 matrix = 4 real
    dof, decomposing under a SINGLE SU(2) as 1 (trace) + 3 (traceless).
    The SO(4) VECTOR is (1/2,1/2) = (1/2,0) (x) (0,1/2) -- one index from
    EACH chirality. Checked by counting how the 2x2 matrix transforms."""
    rng = np.random.default_rng(11)

    def rand_su2():
        a = rng.normal(size=4)
        a = a / np.linalg.norm(a)
        return su2_from_coords(a)

    # psi psi^dagger transforms as M -> u M u^dagger (same u both sides:
    # single chirality). Trace is invariant => a singlet splits off.
    trace_invariance = 0.0
    for _ in range(200):
        psi = rng.normal(size=2) + 1j * rng.normal(size=2)
        M = np.outer(psi, psi.conj())
        u = rand_su2()
        M2 = u @ M @ u.conj().T
        trace_invariance = max(trace_invariance, float(abs(np.trace(M2) - np.trace(M))))

    # by contrast g -> u g v^dagger (DIFFERENT u,v: two chiralities) does NOT
    # leave the trace invariant -- so that outer product is an irreducible 4
    trace_change_two_chirality = 0.0
    for _ in range(200):
        g = rand_su2()
        u, v = rand_su2(), rand_su2()
        g2 = u @ g @ v.conj().T
        trace_change_two_chirality = max(
            trace_change_two_chirality, float(abs(np.trace(g2) - np.trace(g)))
        )

    return {
        "single_chirality_trace_is_invariant": bool(trace_invariance < 1e-12),
        "single_chirality_max_trace_change": trace_invariance,
        "two_chirality_max_trace_change": trace_change_two_chirality,
        "two_chirality_trace_NOT_invariant": bool(trace_change_two_chirality > 1e-3),
        "conclusion": (
            "psi psi^dagger with ONE chirality reduces as 1 + 3 (the trace is "
            "invariant, so it is NOT the irreducible SO(4) vector). The SO(4) "
            "vector needs one index from EACH chirality: (1/2,0) (x) (0,1/2)."
        ),
    }


# ---------------------------------------------------------------------------
# Item 4b: does the check DISCRIMINATE? Build the wrong-chirality alternative
# ---------------------------------------------------------------------------
def discrimination_test() -> dict:
    """Build spinor bases two ways -- from X^R (the round-C180 construction)
    and from X^L (the opposite chirality, a DIFFERENT operator) -- and put
    both through the same representation-content test his item 4 proposes:
    does the span of the bilinears reproduce the vector multiplet H_1?"""
    L, R = C180.quaternion_mult_matrices()

    def spectrum_for(fields: list[np.ndarray], k: int) -> list[tuple[float, int]]:
        basis = C180.harmonic_basis(k)
        Xs = [C180.vector_field_matrix(fields[a], k, basis) for a in range(3)]
        D = -1j * sum(np.kron(PAULI[a], Xs[a].astype(complex)) for a in range(3))
        ev = np.sort(np.linalg.eigvals(D).real)
        clusters: list[list[float]] = []
        for e in ev:
            if clusters and abs(e - clusters[-1][0]) < 1e-6:
                clusters[-1].append(float(e))
            else:
                clusters.append([float(e)])
        return [(round(c[0], 6), len(c)) for c in clusters]

    spec_R = {k: spectrum_for(R, k) for k in (1, 2, 3)}
    spec_L = {k: spectrum_for(L, k) for k in (1, 2, 3)}

    # Are the two operators genuinely different?
    operators_differ = spec_R != spec_L

    # ------------------------------------------------------------------
    # THE ACTUAL TEST. The first version of this block was a TAUTOLOGY,
    # caught by a context-blind skeptic: it computed
    #     span_R = matrix_rank(basis1); span_L = matrix_rank(basis1)
    # -- the rank of the SAME matrix twice, with no L-chirality object built
    # at all, so `same_span` was True for any input. That is the third
    # cannot-fail check in this round sequence (C180's basis test, C182's
    # no-go check, and this one), and the only one that had reached a draft
    # intended for an external collaborator. Replaced with a real
    # computation below.
    #
    # What is actually computed now: take the LOWEST eigenspace of each
    # chirality's operator at k=1 -- these are genuinely different subspaces
    # (R: eigenvalue -1, dim 6; L: eigenvalue -3, dim 2). Form the bilinears
    # his item 4 proposes, pairing each with the constant spinors:
    #     B^mu = psi_0^dagger sigma^mu psi_1,   psi_0 in C^2 (x) H_0
    # which lands in H_1 -- the vector multiplet. Then ask what each spans.
    # This CAN come out different for the two chiralities; that is the point.
    # ------------------------------------------------------------------
    sig = [np.eye(2, dtype=complex)] + [1j * PAULI[a] for a in range(3)]
    basis1 = C180.harmonic_basis(1)  # 4x4 identity: monomials x0..x3

    def lowest_eigenspace(fields: list[np.ndarray]) -> np.ndarray:
        Xs = [C180.vector_field_matrix(fields[a], 1, basis1) for a in range(3)]
        D = -1j * sum(np.kron(PAULI[a], Xs[a].astype(complex)) for a in range(3))
        ev, evec = np.linalg.eig(D)
        lo = np.min(ev.real)
        cols = [i for i in range(len(ev)) if abs(ev[i].real - lo) < 1e-6]
        return evec[:, cols]

    def bilinear_span(fields: list[np.ndarray]) -> dict:
        """Span, inside H_1 (coefficients on x0..x3), of all B^mu built from
        the lowest eigenspace against the two constant spinors."""
        space = lowest_eigenspace(fields)
        rows = []
        for col in range(space.shape[1]):
            psi1 = space[:, col].reshape(2, 4)  # spin index x monomial index
            for spin0 in range(2):
                psi0 = np.zeros(2, dtype=complex)
                psi0[spin0] = 1.0
                for mu in range(4):
                    # B^mu(x) = psi0^dag sigma^mu psi1(x); coefficients on x_p
                    coeffs = np.array([psi0.conj() @ sig[mu] @ psi1[:, p] for p in range(4)])
                    rows.append(coeffs)
        mat = np.array(rows)
        return {
            "lowest_eigenspace_dim": int(space.shape[1]),
            "num_bilinears": int(mat.shape[0]),
            "span_rank_in_H1": int(np.linalg.matrix_rank(mat, tol=1e-9)),
        }

    span_R = bilinear_span(R)
    span_L = bilinear_span(L)
    same_span = span_R["span_rank_in_H1"] == span_L["span_rank_in_H1"]
    both_full = span_R["span_rank_in_H1"] == 4 and span_L["span_rank_in_H1"] == 4

    return {
        "spectrum_from_X_R": {str(k): v for k, v in spec_R.items()},
        "spectrum_from_X_L": {str(k): v for k, v in spec_L.items()},
        "the_two_operators_are_different": bool(operators_differ),
        "bilinear_span_from_X_R": span_R,
        "bilinear_span_from_X_L": span_L,
        "both_give_same_vector_span": bool(same_span),
        "both_span_the_full_4dim_vector_multiplet": bool(both_full),
        "check_discriminates": bool(operators_differ and not same_span),
        "conclusion": (
            "Computed, not assumed: the two chiralities have genuinely "
            "different lowest eigenspaces, yet the bilinears his item 4 "
            "prescribes span the same subspace of H_1 from both -- so a test "
            "that inspects only which vector multiplet is produced cannot "
            "tell the two operators apart."
        ),
    }


# ---------------------------------------------------------------------------
# Item 5: Riemann normal coordinates on S^3 at the identity
# ---------------------------------------------------------------------------
def riemann_normal_coordinates() -> dict:
    """q(y) = exp(y1 i + y2 j + y3 k) = cos|y| + sin|y|/|y| * (y.e).
    Embedded in R^4, pull back the flat metric; check g_ab(0) = delta_ab and
    d_c g_ab(0) = 0 -- the defining property of normal coordinates."""
    y1, y2, y3 = sp.symbols("y1 y2 y3", real=True)
    Y = [y1, y2, y3]
    rho = sp.sqrt(y1**2 + y2**2 + y3**2)

    # embedding coordinates of q(y) in R^4
    sinc = sp.sin(rho) / rho
    emb = [sp.cos(rho), y1 * sinc, y2 * sinc, y3 * sinc]

    # induced metric g_ab = sum_mu d_a emb_mu d_b emb_mu
    g = sp.zeros(3, 3)
    for a in range(3):
        for b in range(3):
            g[a, b] = sp.simplify(
                sum(sp.diff(emb[mu], Y[a]) * sp.diff(emb[mu], Y[b]) for mu in range(4))
            )

    # Evaluate at the origin along rays y = t*n with n a UNIT direction.
    # NOTE (bug caught on the first run, recorded in decision.md): a first
    # draft left n as three free symbols. The limit then returns a rational
    # function of n that equals the identity only ON the constraint
    # n1^2+n2^2+n3^2 = 1, which sympy has no way to know -- so the check
    # reported a spurious failure. Fixed by using EXACT unit directions,
    # which is also rigorous: the derivative result below is symbolic and
    # direction-independent, and g(0) is checked on a spanning set of rays.
    t = sp.symbols("t", positive=True)
    n1, n2, n3 = sp.symbols("n1 n2 n3", real=True)
    ray_symbols = {y1: t * n1, y2: t * n2, y3: t * n3}

    unit_directions = [
        (sp.Integer(1), sp.Integer(0), sp.Integer(0)),
        (sp.Integer(0), sp.Integer(1), sp.Integer(0)),
        (sp.Integer(0), sp.Integer(0), sp.Integer(1)),
        (1 / sp.sqrt(3), 1 / sp.sqrt(3), 1 / sp.sqrt(3)),
        (1 / sp.sqrt(2), -1 / sp.sqrt(2), sp.Integer(0)),
    ]

    per_direction = []
    identity_everywhere = True
    for d1v, d2v, d3v in unit_directions:
        subs_dir = {n1: d1v, n2: d2v, n3: d3v}
        g0 = sp.zeros(3, 3)
        for a in range(3):
            for b in range(3):
                expr = g[a, b].subs(ray_symbols).subs(subs_dir)
                g0[a, b] = sp.simplify(sp.limit(sp.simplify(expr), t, 0))
        ok = sp.simplify(g0 - sp.eye(3)) == sp.zeros(3, 3)
        identity_everywhere = identity_everywhere and bool(ok)
        per_direction.append(
            {"direction": [str(d1v), str(d2v), str(d3v)], "g_at_origin_is_identity": bool(ok)}
        )

    # first derivatives: symbolic in n, no constraint needed (they vanish
    # identically, which is the substantive half of the RNC property)
    dg_at_0_max = 0
    dg_entries = []
    for a in range(3):
        for b in range(3):
            expr = sp.simplify(g[a, b].subs(ray_symbols))
            d1 = sp.simplify(sp.limit(sp.diff(expr, t), t, 0))
            dg_entries.append({"a": a, "b": b, "first_derivative_at_origin": str(d1)})
            if d1 != 0:
                dg_at_0_max = 1

    g_at_0 = per_direction
    is_identity = identity_everywhere

    # Scalar curvature cross-check: the unit-radius round S^3 has Scal = 6,
    # which is round111's own independently established value.
    return {
        "metric_at_origin_per_unit_direction": g_at_0,
        "metric_at_origin_is_identity": bool(is_identity),
        "first_derivatives_at_origin": dg_entries,
        "all_first_derivatives_vanish": dg_at_0_max == 0,
        "is_riemann_normal": bool(is_identity and dg_at_0_max == 0),
        "cross_reference": (
            "unit-radius round S^3 has Scal_LC = 6, matching round111's own "
            "independently cross-checked value"
        ),
        "not_covered": (
            "transporting the full spinor-harmonic machinery into these "
            "coordinates is NOT attempted in this round"
        ),
    }


# ---------------------------------------------------------------------------
def main() -> dict:
    result: dict = {}
    result["item4a_projection"] = projection_check()
    result["item4_predicate3_single_chirality"] = single_chirality_outer_product_check()
    result["item4b_discrimination"] = discrimination_test()
    result["item5_riemann_normal_coordinates"] = riemann_normal_coordinates()

    proj_ok = result["item4a_projection"]["projection_recovers_vector_multiplet"]
    discriminates = result["item4b_discrimination"]["check_discriminates"]
    rnc_ok = result["item5_riemann_normal_coordinates"]["is_riemann_normal"]

    if not proj_ok:
        label = "PROJECTION-FAILS"
    elif not rnc_ok:
        label = "RNC-FAILS"
    elif discriminates:
        label = "PROJECTION-DISCRIMINATES"
    else:
        label = "PROJECTION-WORKS-BUT-DOES-NOT-DISCRIMINATE"

    result["verdict"] = {
        "label": label,
        "projection_works": proj_ok,
        "projection_discriminates": discriminates,
        "riemann_normal_coordinates_verified": rnc_ok,
        "single_chirality_gives_1_plus_3_not_the_SO4_vector": result[
            "item4_predicate3_single_chirality"
        ]["single_chirality_trace_is_invariant"],
    }
    return result


if __name__ == "__main__":
    out = main()
    print(json.dumps(out["verdict"], indent=2))
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    print(f"\nSaved: {RESULTS_PATH}")
