"""G98: B-L isotropy vs coset — with skeptic-required control.

Skeptic blockers addressed:
1. T4 (so(7) closure) runs BEFORE T5/T6.
2. Control: compare BmL's coset commutators against a genuine so(6) Cartan
   generator's coset commutators. If the Cartan generator behaves the same
   as BmL, the raw PASS is uninformative (diagonal-vs-off-diagonal artifact,
   not a B-L-specific finding).
"""

import json
import os

import sympy as sp
from sympy import zeros, eye, kronecker_product as kron, Rational as Rat

_EXP_DIR = os.path.dirname(__file__)

I8 = eye(8)
s0 = eye(2)
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])

G = [
    kron(s1, s0, s0),
    kron(s2, s0, s0),
    kron(s3, s1, s0),
    kron(s3, s2, s0),
    kron(s3, s3, s1),
    kron(s3, s3, s2),
]  # Gamma_1..Gamma_6, identical to G11/G15
G7 = kron(s3, s3, s3)

sigma3_1 = kron(s3, s0, s0)
sigma3_2 = kron(s0, s3, s0)
sigma3_3 = kron(s0, s0, s3)
BmL = -Rat(1, 3) * (sigma3_1 + sigma3_2 + sigma3_3)


def comm(A, B):
    return A * B - B * A


def frob(M):
    return sp.sqrt(sum(abs(M[i, j]) ** 2 for i in range(M.rows) for j in range(M.cols)))


def main():
    results = {}
    passed = 0
    total = 0

    def check(name, ok):
        nonlocal passed, total
        total += 1
        passed += int(bool(ok))
        results[name] = bool(ok)
        print(f"{name}: {'PASS' if ok else 'FAIL'}")

    # T1: Gamma_7 Clifford checks
    t1a = all(
        comm(G[a], G7) == -2 * G[a] * G7 for a in range(6)
    )  # anticommute check via {}=AB+BA=0
    anticomm_ok = all((G[a] * G7 + G7 * G[a]) == zeros(8, 8) for a in range(6))
    herm_ok = G7.H == G7
    sq_ok = G7 * G7 == I8
    check("T1_gamma7_anticommutes", anticomm_ok)
    check("T1_gamma7_hermitian", herm_ok)
    check("T1_gamma7_squares_to_I", sq_ok)

    # T2: coset generators K_a = [Gamma_a, Gamma_7]/4
    K = [comm(G[a], G7) / 4 for a in range(6)]
    check("T2_coset_built", len(K) == 6)

    # T3: so(6) generators J_ab
    J = {}
    for a in range(6):
        for b in range(a + 1, 6):
            J[(a, b)] = comm(G[a], G[b]) / 4
    check("T3_so6_gens_built", len(J) == 15)

    # T4: 21 generators close into so(7) -- structure-constant sanity check.
    # Sufficient proxy (not full structure-constant table): every commutator of
    # two generators from {J_ab} U {K_a} must itself be expressible as a real
    # linear combination of the same 21 generators (closure), verified by
    # checking each such commutator lies in the span (rank test).
    all_gens = list(J.values()) + K
    n_gens = len(all_gens)

    def to_vec(M):
        return sp.Matrix([M[i, j] for i in range(8) for j in range(8)])

    basis_mat = sp.Matrix.hstack(*[to_vec(m) for m in all_gens])
    basis_rank = basis_mat.rank()
    check("T4a_21_generators_independent", basis_rank == 21)

    closure_ok = True
    for i in range(n_gens):
        for jx in range(i + 1, n_gens):
            c = comm(all_gens[i], all_gens[jx])
            if c == zeros(8, 8):
                continue
            aug = sp.Matrix.hstack(basis_mat, to_vec(c))
            if aug.rank() != basis_rank:
                closure_ok = False
                break
        if not closure_ok:
            break
    check("T4b_closes_under_commutation", closure_ok)

    if not closure_ok or basis_rank != 21:
        print("\nT4 FAILED -- so(7) framing invalid, aborting T5/T6/control.")
        result = {"gate": "G98", "verdict": "FAIL_T4_STRUCTURE", "gates": results}
        with open(os.path.join(_EXP_DIR, "results_g98.json"), "w") as f:
            json.dump(result, f, indent=2)
        return False

    # T5: [BmL, J_ab] = 0 for all 15 so(6) generators
    so6_comms = [comm(BmL, Jab) for Jab in J.values()]
    t5_ok = all(c == zeros(8, 8) for c in so6_comms)
    check("T5_BmL_commutes_with_so6", t5_ok)

    # T6: [BmL, K_a] for all 6 coset generators
    bml_coset_comms = [comm(BmL, Ka) for Ka in K]
    bml_coset_nonzero = [c != zeros(8, 8) for c in bml_coset_comms]
    t6_count = sum(bml_coset_nonzero)
    check("T6_BmL_fails_coset_at_least_one", t6_count >= 1)
    print(f"   BmL vs coset: {t6_count}/6 nonzero")

    # CONTROL (skeptic-required): so(6) Cartan generator (rank 3), e.g. J_01
    # (proportional to sigma3_1, same qubit-pairing pattern as BmL's building
    # blocks) -- check whether a GENERIC diagonal isotropy Cartan direction
    # ALSO fails to commute with the coset, which would make T6 uninformative.
    cartan_candidates = {"J_01": J[(0, 1)], "J_23": J[(2, 3)], "J_45": J[(4, 5)]}
    control_report = {}
    for name, Cgen in cartan_candidates.items():
        c_coset = [comm(Cgen, Ka) for Ka in K]
        n_nonzero = sum(1 for c in c_coset if c != zeros(8, 8))
        control_report[name] = n_nonzero
        print(f"   CONTROL {name} vs coset: {n_nonzero}/6 nonzero")

    all_cartan_also_fail = all(v >= 1 for v in control_report.values())
    check("CONTROL_cartan_gens_also_fail_coset", all_cartan_also_fail)

    # Differential: is BmL distinguishable from a generic so(6) Cartan generator?
    # BmL = -(1/3)(sigma3_1+sigma3_2+sigma3_3) is itself a linear combination of
    # the 3 Cartan directions tested above (each sigma3_k prop to J_(2k,2k+1)).
    # So BmL failing to commute with the coset is NOT independent evidence --
    # it is a direct consequence of each Cartan piece failing individually.
    is_uninformative = all_cartan_also_fail
    results["differential_informative"] = not is_uninformative

    # T7: alternative BmL construction (Hamming weight formula) -- consistency,
    # not a fix for the informativeness issue (both are diagonal by definition).
    Hamming = Rat(3, 2) * I8 - Rat(1, 2) * (sigma3_1 + sigma3_2 + sigma3_3)
    BmL_alt = (2 * Hamming - 3 * I8) * Rat(1, 3)
    t7_ok = BmL_alt == BmL
    check("T7_alt_construction_identical", t7_ok)

    print(f"\n{'=' * 60}")
    print(f"G98: {passed}/{total} gates PASS")

    if is_uninformative:
        verdict = "WEAK_UNINFORMATIVE_DIAGONAL_ARTIFACT"
        print("\nVERDICT: WEAK.")
        print("BmL's failure to commute with the coset generators is NOT")
        print("B-L-specific -- ALL tested so(6) Cartan directions (J_01,")
        print("J_23, J_45) ALSO fail to commute with the coset, in the same")
        print("pattern. This is a generic feature of so(7)/so(6) as a curved")
        print("(non-product) coset space, not evidence that B-L specifically")
        print("is a 'holonomy charge' distinct from a generic isometry-Cartan")
        print("direction. The reconciliation hypothesis in claim.md is NOT")
        print("confirmed by this test as originally scoped.")
    else:
        verdict = "PASS_HOLONOMY_CONFIRMED"
        print("\nVERDICT: PASS -- BmL is distinguishable from generic so(6)")
        print("Cartan directions in its relation to the coset.")

    result = {
        "gate": "G98",
        "verdict": verdict,
        "gates": results,
        "bml_coset_nonzero_count": t6_count,
        "control_cartan_coset_nonzero": control_report,
    }
    with open(os.path.join(_EXP_DIR, "results_g98.json"), "w") as f:
        json.dump(result, f, indent=2)

    return verdict == "PASS_HOLONOMY_CONFIRMED"


if __name__ == "__main__":
    main()
