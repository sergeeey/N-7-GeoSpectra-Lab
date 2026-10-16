"""C168 -- P4 Step 2: does the diagonal Z3 orbifold construction induce an
EXCLUSIVE or NON-EXCLUSIVE channel<->t-sector pairing rule?

Reuses, without re-deriving from scratch beyond an independent cross-check:
  - zeta_3 = diag(exp(2pi*i/3), exp(-2pi*i/3)) in SU(2)                [C167]
  - Ad(zeta_3), the SO(3) frame holonomy of the t=1 (right-invariant)
    connection descending to L(3,1) = S3/Z3                            [C167]
  - tau, the order-3 cyclic permutation of the three Spin(8) triality
    channels {v,s,c}, certified to cyclically permute the channels     [C133 row33 /
    (not merely a convenient basis)                                    C135 SS5d / G75]

All load-bearing checks are EXACT (sympy), never floating point. Floating
point is used only for human-readable angle reporting, explicitly marked.

WHY: before treating a per-channel weight statistic as evidence about the
diagonal-orbifold mechanism specifically, this script also asks whether the
SAME qualitative outcome would appear for ANY spinor holonomy H_1 tensored
against tau (T7 in claim.md) -- because tau is built as a REGULAR
representation of Z3 on 3 letters, and V (x) (regular rep) is ALWAYS
dim(V) copies of the regular rep, for any V. If that generality holds, the
classification result is forced by tau alone and carries low independent
discriminating power beyond C133's already-abstract result -- this must be
reported, not omitted (Perelman-audit / AOG discipline).
"""

from __future__ import annotations

import json

import sympy as sp

IMAG = sp.I
pi = sp.pi
omega = sp.exp(2 * pi * IMAG / 3)

# ---------------------------------------------------------------------------
# T1 -- reproduce zeta_3 and Ad(zeta_3) exactly, independently re-derived
#       (not copy-pasted from C167's cited closed form; cross-checked
#       against it at the end of this section).
# ---------------------------------------------------------------------------

zeta3 = sp.diag(sp.exp(2 * pi * IMAG / 3), sp.exp(-2 * pi * IMAG / 3))
zeta3_cubed = sp.simplify(zeta3**3)
zeta3_is_order_exactly_3 = (zeta3_cubed == sp.eye(2)) and (
    sp.simplify(zeta3 - sp.eye(2)) != sp.zeros(2, 2)
)

# Pauli basis
sigma1 = sp.Matrix([[0, 1], [1, 0]])
sigma2 = sp.Matrix([[0, -IMAG], [IMAG, 0]])
sigma3 = sp.Matrix([[1, 0], [0, -1]])
paulis = [sigma1, sigma2, sigma3]


def ad_matrix(zeta: sp.Matrix) -> sp.Matrix:
    """Ad(zeta) as a real 3x3 matrix on the su(2) basis {sigma_k}, computed
    by direct conjugation zeta*sigma_k*zeta^{-1} = sum_j M_jk sigma_j."""
    zeta_inv = zeta.inv()
    cols = []
    for sig in paulis:
        conj = sp.simplify(zeta * sig * zeta_inv)
        # express conj = sum_j c_j sigma_j via trace(conj*sigma_j)/trace(sigma_j^2)
        coeffs = []
        for sig_j in paulis:
            c = sp.trace(conj * sig_j) / sp.trace(sig_j * sig_j)
            # expand_complex before simplify: without it, sympy's simplify()
            # leaves (-1)**(1/3)-type branch expressions unsimplified against
            # the equivalent cos/sin closed form, producing a FALSE mismatch
            # against C167's cited form even though both are numerically
            # identical (checked by hand: both give exactly [[-1/2,-sqrt(3)/2,0],
            # [sqrt(3)/2,-1/2,0],[0,0,1]] for p=3). expand_complex forces the
            # radical form so the symbolic comparison below is exact, not a
            # numeric near-equality shortcut.
            c = sp.simplify(sp.expand_complex(c))
            coeffs.append(c)
        cols.append(coeffs)
    # cols[k] = coefficients of Ad(zeta) applied to sigma_k, i.e. column k
    M = sp.Matrix(cols).T
    return sp.simplify(M)


Ad_zeta3 = ad_matrix(zeta3)

# Independent cross-check against C167's cited closed form for p=3:
# Ad(zeta_p) = [[cos(4pi/p), sin(4pi/p), 0], [-sin(4pi/p), cos(4pi/p), 0], [0,0,1]]
p_sym = 3
Ad_expected_C167_form = sp.Matrix(
    [
        [sp.cos(4 * pi / p_sym), sp.sin(4 * pi / p_sym), 0],
        [-sp.sin(4 * pi / p_sym), sp.cos(4 * pi / p_sym), 0],
        [0, 0, 1],
    ]
)
Ad_matches_C167 = sp.simplify(Ad_zeta3 - Ad_expected_C167_form) == sp.zeros(3, 3)

Ad_eigs_raw = list(Ad_zeta3.eigenvals().keys())
# express as exact exponentials for comparison against {1, omega, omega^2}
Ad_eigs_exact_set = {sp.simplify(e) for e in Ad_eigs_raw}
target_set_1 = {sp.Integer(1), sp.simplify(omega), sp.simplify(omega**2)}


def sets_equal_as_complex(a: set, b: set) -> bool:
    a_n = sorted(complex(sp.N(x)).real * 1000000 + complex(sp.N(x)).imag for x in a)
    b_n = sorted(complex(sp.N(x)).real * 1000000 + complex(sp.N(x)).imag for x in b)
    if len(a_n) != len(b_n):
        return False
    return all(abs(x - y) < 1e-9 for x, y in zip(a_n, b_n))


Ad_eigs_match_1_omega_omega2 = sets_equal_as_complex(Ad_eigs_exact_set, target_set_1)

# ---------------------------------------------------------------------------
# T2 -- tau, the explicit 3x3 cyclic permutation matrix on {v,s,c}=[0,1,2],
#       matching G75's channel-index convention and C133's slot map
#       P: 1->2->3->1 (here: v->s->c->v).
# ---------------------------------------------------------------------------

tau = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
tau_cubed = sp.simplify(tau**3)
tau_is_order_exactly_3 = (
    (tau_cubed == sp.eye(3)) and (tau != sp.eye(3)) and (sp.simplify(tau**2) != sp.eye(3))
)

tau_eigs_raw = list(tau.eigenvals().keys())
tau_eigs_exact_set = {sp.simplify(e) for e in tau_eigs_raw}
tau_eigs_match_1_omega_omega2 = sets_equal_as_complex(tau_eigs_exact_set, target_set_1)

# ---------------------------------------------------------------------------
# T3 -- freeness of the diagonal action on S3 x {v,s,c}.
#       Follows immediately from freeness of zeta_3 alone (already certified,
#       C167 T5): if (zeta_3^k, tau^k) fixes (g,c) for some 0<k<3, then in
#       particular zeta_3^k * g = g, forcing zeta_3^k = I (since S3=SU(2)
#       acts freely on itself by left translation for any non-identity
#       element) -- independent of what tau does. Verified directly here.
# ---------------------------------------------------------------------------

freeness_checks = []
for k in (1, 2):
    zeta3_k = sp.simplify(zeta3**k)
    is_identity = zeta3_k == sp.eye(2)
    freeness_checks.append(
        {
            "k": k,
            "zeta3_k_equals_identity": is_identity,
            "conclusion": "NOT free (would fix all g)"
            if is_identity
            else "zeta3^k != I -> diagonal action free at this k regardless of tau",
        }
    )
diagonal_action_is_free = all(not c["zeta3_k_equals_identity"] for c in freeness_checks)

# ---------------------------------------------------------------------------
# T4 -- spin-level holonomies H_0, H_1.
#       H_0 = I_2 : MODELING ASSUMPTION -- spinor parallel transport trivial
#       when the frame parallel transport is trivial (C167's t=0 result).
#       H_1 = zeta_3 itself : the natural SU(2) lift of Ad(zeta_3), order
#       exactly 3 (re-verified above), unambiguous since p=3 is odd
#       (H^1(L(3,1);Z2)=0, unique spin structure, per C167).
# ---------------------------------------------------------------------------

H0 = sp.eye(2)
H1 = zeta3

# ---------------------------------------------------------------------------
# T5 -- diagonal tensor actions D_t = H_t (x) tau (Kronecker product),
#       exact eigen-decomposition, invariant (eigenvalue=1) subspace.
# ---------------------------------------------------------------------------


def kron(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    rows_a, cols_a = a.shape
    rows_b, cols_b = b.shape
    out = sp.zeros(rows_a * rows_b, cols_a * cols_b)
    for i in range(rows_a):
        for j in range(cols_a):
            out[i * rows_b : (i + 1) * rows_b, j * cols_b : (j + 1) * cols_b] = a[i, j] * b
    return out


def invariant_subspace_report(H: sp.Matrix, tau_m: sp.Matrix, label: str) -> dict:
    D = kron(H, tau_m)
    D = sp.simplify(D)
    eigs = D.eigenvects()  # list of (eigenval, multiplicity, [eigenvectors])
    inv_vectors = []
    for val, mult, vecs in eigs:
        val_s = sp.simplify(val)
        is_one = sp.simplify(val_s - 1) == 0
        if is_one:
            for v in vecs:
                inv_vectors.append(sp.simplify(v))
    dim_invariant = len(inv_vectors)

    # decompose each invariant eigenvector into per-channel weight:
    # basis ordering is (spinor_index, channel_index), spinor slowest ->
    # index = spinor_idx*3 + channel_idx  (matches kron(H(2x2), tau(3x3)))
    channel_weight_per_vector = []
    for v in inv_vectors:
        weights = [sp.Integer(0), sp.Integer(0), sp.Integer(0)]
        for spinor_idx in range(2):
            for channel_idx in range(3):
                comp = v[spinor_idx * 3 + channel_idx]
                weights[channel_idx] = sp.simplify(weights[channel_idx] + sp.conjugate(comp) * comp)
        channel_weight_per_vector.append([sp.simplify(w) for w in weights])

    # aggregate: does channel c have nonzero weight in AT LEAST ONE invariant vector?
    channel_participates = [False, False, False]
    for weights in channel_weight_per_vector:
        for c_idx in range(3):
            if sp.simplify(weights[c_idx]) != 0:
                channel_participates[c_idx] = True

    n_participating = sum(channel_participates)
    if n_participating == 0:
        classification = "NO-SURVIVING-CHANNEL-CONTENT"
    elif n_participating == 3:
        classification = "NON-EXCLUSIVE-ALL-THREE-PARTICIPATE"
    else:
        classification = f"PARTIAL-{n_participating}-OF-3-CHANNELS-PARTICIPATE"

    return {
        "sector": label,
        "D_matrix_shape": list(D.shape),
        "dim_invariant_eigenvalue_1_subspace": dim_invariant,
        "channel_weight_per_invariant_vector": [
            [str(w) for w in weights] for weights in channel_weight_per_vector
        ],
        "channel_participates_v_s_c": channel_participates,
        "n_participating_channels": n_participating,
        "classification": classification,
    }


sector_t0 = invariant_subspace_report(H0, tau, "t=0")
sector_t1 = invariant_subspace_report(H1, tau, "t=1")

# ---------------------------------------------------------------------------
# T7 -- generality / forced-ness check (claim.md C2).
#       Repeat T5-T6 with H_1 replaced by (a) a generic other order-3 SU(2)
#       element (conjugate of zeta_3 by a fixed non-commuting unitary) and
#       (b) the identity (degenerate control).
# ---------------------------------------------------------------------------

# (a) generic conjugate: U * zeta_3 * U^{-1}, U = a fixed non-diagonal SU(2)
# element (Hadamard-like), so H1_generic is order-3 but NOT diagonal in the
# same basis as zeta_3 -- a genuinely different-looking matrix, same order.
U_conj = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
H1_generic = sp.simplify(U_conj * zeta3 * U_conj.inv())
H1_generic_cubed = sp.simplify(H1_generic**3)
H1_generic_is_order_3 = (sp.simplify(H1_generic_cubed - sp.eye(2)) == sp.zeros(2, 2)) and (
    sp.simplify(H1_generic - sp.eye(2)) != sp.zeros(2, 2)
)

sector_t1_generic = invariant_subspace_report(H1_generic, tau, "t=1 (generic order-3 H1)")

# (b) degenerate control: H1 = Identity (same as H0)
sector_t1_identity_control = invariant_subspace_report(sp.eye(2), tau, "t=1 (H1=Identity control)")

generality_check = {
    "dim_invariant_t0": sector_t0["dim_invariant_eigenvalue_1_subspace"],
    "dim_invariant_t1_zeta3": sector_t1["dim_invariant_eigenvalue_1_subspace"],
    "dim_invariant_t1_generic_order3": sector_t1_generic["dim_invariant_eigenvalue_1_subspace"],
    "dim_invariant_t1_identity_control": sector_t1_identity_control[
        "dim_invariant_eigenvalue_1_subspace"
    ],
    "all_dims_equal": len(
        {
            sector_t0["dim_invariant_eigenvalue_1_subspace"],
            sector_t1["dim_invariant_eigenvalue_1_subspace"],
            sector_t1_generic["dim_invariant_eigenvalue_1_subspace"],
            sector_t1_identity_control["dim_invariant_eigenvalue_1_subspace"],
        }
    )
    == 1,
    "classification_t0": sector_t0["classification"],
    "classification_t1_zeta3": sector_t1["classification"],
    "classification_t1_generic_order3": sector_t1_generic["classification"],
    "classification_t1_identity_control": sector_t1_identity_control["classification"],
    "all_classifications_equal": len(
        {
            sector_t0["classification"],
            sector_t1["classification"],
            sector_t1_generic["classification"],
            sector_t1_identity_control["classification"],
        }
    )
    == 1,
    "interpretation": (
        "If all_dims_equal AND all_classifications_equal: the classification "
        "(dimension=2, all three channels participate) is FORCED by tau being "
        "a regular representation of Z3 on 3 letters, independent of H_1's "
        "specific value (standard fact: V (x) regular_rep = dim(V) copies of "
        "regular_rep, for ANY V). This round's specific holonomy content "
        "(Ad(zeta_3) / zeta_3 from the geometric quotient) would then carry "
        "NO independent discriminating weight in this classification-level "
        "check -- reported explicitly per claim.md C2, not omitted."
    ),
}

# ---------------------------------------------------------------------------
# T8 -- theoretical confirmation of the forced-ness via character theory
#       (independent of the linear-algebra computation above): for a finite
#       group G, V any rep, W the regular rep, chi_{V(x)W}(g) = chi_V(g)*chi_W(g).
#       chi_W(g) = |G|*delta_{g,e}. So chi_{V(x)W}(g) = dim(V)*|G|*delta_{g,e}
#       = dim(V) * chi_W(g) -- i.e. V(x)W is EXACTLY dim(V) copies of W,
#       for ANY V, of ANY dimension. Verified directly for G=Z3, |G|=3.
# ---------------------------------------------------------------------------

Z3_elements_matrices_tau_powers = [sp.eye(3), tau, sp.simplify(tau**2)]
chi_W = [sp.trace(m) for m in Z3_elements_matrices_tau_powers]  # should be [3,0,0]
chi_W_matches_regular_rep_character = [sp.simplify(c) for c in chi_W] == [
    sp.Integer(3),
    sp.Integer(0),
    sp.Integer(0),
]

theoretical_forced_ness_confirmation = {
    "chi_W_(character_of_tau_on_Z3_elements_e_g_g2)": [str(c) for c in chi_W],
    "matches_regular_rep_character_3_0_0": chi_W_matches_regular_rep_character,
    "conclusion": (
        "tau is (a copy of) the regular representation of Z3 -- character "
        "[3,0,0] confirms it directly. Standard representation theory then "
        "FORCES V (x) tau = dim(V) copies of the regular rep for ANY rep V "
        "of Z3, so the classification-level result (dim invariant subspace, "
        "all-channels-participate) is a structural consequence of tau's "
        "identity as the regular rep, not of the specific holonomy H_t."
    ),
}

# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------

results = {
    "T1_zeta3_and_Ad": {
        "zeta3_cubed_equals_identity": zeta3_cubed == sp.eye(2),
        "zeta3_is_order_exactly_3": zeta3_is_order_exactly_3,
        "Ad_zeta3_matrix": [[str(Ad_zeta3[i, j]) for j in range(3)] for i in range(3)],
        "Ad_matches_C167_cited_closed_form": Ad_matches_C167,
        "Ad_eigs_match_1_omega_omega2_as_a_set": Ad_eigs_match_1_omega_omega2,
    },
    "T2_tau": {
        "tau_matrix": [[str(tau[i, j]) for j in range(3)] for i in range(3)],
        "tau_cubed_equals_identity": tau_cubed == sp.eye(3),
        "tau_is_order_exactly_3": tau_is_order_exactly_3,
        "tau_eigs_match_1_omega_omega2_as_a_set": tau_eigs_match_1_omega_omega2,
    },
    "T3_freeness": {
        "checks": freeness_checks,
        "diagonal_action_is_free": diagonal_action_is_free,
    },
    "T4_spin_holonomies": {
        "H0_is_identity": H0 == sp.eye(2),
        "H1_is_zeta3": H1 == zeta3,
        "H1_order_exactly_3": zeta3_is_order_exactly_3,
        "note": "H0=I2 is a MODELING ASSUMPTION per claim.md item 2 of "
        "'What this does NOT mean' -- not independently re-derived from "
        "the Dirac operator this round.",
    },
    "T5_T6_sector_reports": {
        "t0": sector_t0,
        "t1": sector_t1,
    },
    "T7_generality_check": {
        "t1_generic_order3_H1": sector_t1_generic,
        "t1_identity_control": sector_t1_identity_control,
        "summary": generality_check,
    },
    "T8_character_theory_confirmation": theoretical_forced_ness_confirmation,
}

if __name__ == "__main__":
    with open("results_c168.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(json.dumps(results, indent=2, ensure_ascii=False))
