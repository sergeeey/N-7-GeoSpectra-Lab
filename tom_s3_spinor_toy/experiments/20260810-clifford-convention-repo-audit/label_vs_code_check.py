"""Does each sub-project's Clifford LABEL match the sign its CODE asserts?

The scan (clifford_convention_scan.py) flagged three files carrying both signs.
Two turned out to be label/code disagreements rather than math errors, so this
script settles the question the only way that counts: build the generators,
square them, and compute the discriminating invariant. No periodicity table
recited from memory -- every claim below is computed here.

THE QUESTION. This repo names its Clifford algebras two different ways:

    round67 (S3):        Z_i = i*sigma_i,  Z_i^2 = -1,  labeled  Cl(0,3)
    s6-harm-g0 (S6):     Gamma_a hermitian, Gamma_a^2 = +1, labeled Cl(6,0)
    g68/round34 (oct):   L_i^2 = -1,                      labeled  Cl(7,0)   <-- ?

The first two are consistent with each other: Cl(0,n) means squares to -1,
Cl(n,0) means squares to +1. The third uses Cl(n,0) for squares to -1, which
is the OPPOSITE. If that is right, the SAME label `Cl(n,0)` means two
different algebras in two different corners of this repo -- and a future round
that reads a label instead of the code walks straight into OB10's trap.

THE DISCRIMINATOR (computed, not asserted). For n=7 the pseudoscalar
omega = e_1...e_7 is central, and

    omega^2 = eps^7 * (-1)^(7*6/2)    where eps = e_i^2

so eps=-1 gives omega^2 = +1 (omega = +-I on each of TWO irreducible real
summands -> the algebra SPLITS as M_8(R) (+) M_8(R)), while eps=+1 gives
omega^2 = -1 (omega acts as a complex structure -> M_8(C), NO split).

g68 and round34 both claim the SPLIT (Omega_L = +I, Omega_R = -I, "two
inequivalent 8-dim REAL modules"). That claim is only available for eps = -1.
So their own mathematical content identifies the algebra as the eps=-1 one --
and their label says Cl(7,0), which under this repo's other convention means
eps=+1. The label is what is wrong, not the math.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_label_vs_code.json"
results: dict = {}

s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
s0 = np.eye(2, dtype=complex)


def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = np.kron(out, m)
    return out


def square_sign(gens: list[np.ndarray]) -> int | None:
    """+1 if every g^2 = +I, -1 if every g^2 = -I, None if inconsistent."""
    n = gens[0].shape[0]
    ident = np.eye(n, dtype=complex)
    if all(np.allclose(g @ g, ident) for g in gens):
        return +1
    if all(np.allclose(g @ g, -ident) for g in gens):
        return -1
    return None


def pseudoscalar(gens: list[np.ndarray]) -> np.ndarray:
    out = gens[0]
    for g in gens[1:]:
        out = out @ g
    return out


print("=" * 78)
print("Clifford LABEL vs CODE -- computed, not recited")
print("=" * 78)

# --- 1. S3 side, round67's actual generators ---------------------------------
Z = [1j * s1, 1j * s2, 1j * s3]
eps_s3 = square_sign(Z)
print(f"\nS3  round67  Z_i = i*sigma_i        -> Z_i^2 = {eps_s3:+d}   labeled Cl(0,3)")
results["s3_round67_square_sign"] = eps_s3

# --- 2. S6 side, s6-harm-g0's actual generators ------------------------------
G6 = [
    kron(s1, s0, s0),
    kron(s2, s0, s0),
    kron(s3, s1, s0),
    kron(s3, s2, s0),
    kron(s3, s3, s1),
    kron(s3, s3, s2),
]
eps_s6 = square_sign(G6)
print(f"S6  s6-harm-g0  Gamma_a hermitian   -> G_a^2   = {eps_s6:+d}   labeled Cl(6,0)")
results["s6_harm_g0_square_sign"] = eps_s6

# --- 3. octonion side, g68's actual generators -------------------------------
# WHY rebuilt here rather than imported: g68 builds them from the Fano table at
# import time and prints a full report; the audit only needs the 7 matrices, and
# rebuilding from the SAME published table (Baez 2002, Fano triples) keeps this
# file self-contained. Cross-checked against g68's own assertion below.
FANO = [(1, 2, 3), (1, 4, 5), (1, 7, 6), (2, 4, 6), (2, 5, 7), (3, 4, 7), (3, 6, 5)]


def octonion_left_mult() -> list[np.ndarray]:
    """L_i = left multiplication by imaginary unit e_i, as 8x8 real matrices."""
    table = np.zeros((8, 8, 8))  # table[i,j,k]: e_i e_j = sum_k table[i,j,k] e_k
    for i in range(8):
        table[0, i, i] = 1.0
        table[i, 0, i] = 1.0
    for i in range(1, 8):
        table[i, i, 0] = -1.0
    for a, b, c in FANO:
        for x, y, z in ((a, b, c), (b, c, a), (c, a, b)):
            table[x, y, z] = 1.0
            table[y, x, z] = -1.0
    return [table[i].T.astype(complex) for i in range(1, 8)]


L = octonion_left_mult()
eps_oct = square_sign(L)
anticomm_ok = all(
    np.allclose(L[i] @ L[j] + L[j] @ L[i], np.zeros((8, 8)))
    for i in range(7)
    for j in range(7)
    if i != j
)
print(f"OCT g68/round34  L_i (Fano table)   -> L_i^2   = {eps_oct:+d}   labeled Cl(7,0)  <-- ")
print(f"     (all 21 off-diagonal pairs anticommute: {anticomm_ok})")
results["octonion_g68_square_sign"] = eps_oct
results["octonion_anticommute_ok"] = bool(anticomm_ok)

# --- 4. the discriminator: does the algebra SPLIT? ---------------------------
print("\nDISCRIMINATOR -- omega = e_1...e_7 is central; omega^2 = +1 <=> the")
print("algebra splits as M_8(R) (+) M_8(R) (two inequivalent REAL 8-dim modules),")
print("which is exactly what g68-D4 and round34 claim.")
om = pseudoscalar(L)
om_sq_plus = bool(np.allclose(om @ om, np.eye(8)))
om_is_pm_id = bool(np.allclose(om, np.eye(8))) or bool(np.allclose(om, -np.eye(8)))
print(f"  computed omega^2 = +I : {om_sq_plus}")
print(f"  computed omega = +-I  : {om_is_pm_id}  (so the module IS one summand)")
results["octonion_pseudoscalar_sq_is_plus_I"] = om_sq_plus
results["octonion_pseudoscalar_is_pm_identity"] = om_is_pm_id

# Now the same invariant for a genuinely eps=+1 seven-generator algebra, to show
# the split is NOT available there. Build one by multiplying each L_i by i.
Lpos = [1j * m for m in L]
eps_pos = square_sign(Lpos)
om_pos = pseudoscalar(Lpos)
om_pos_sq_plus = bool(np.allclose(om_pos @ om_pos, np.eye(8)))
print(f"\n  CONTRAST: same 7 generators scaled by i -> e_i^2 = {eps_pos:+d} (a true Cl(7,0))")
print(f"            omega^2 = +I : {om_pos_sq_plus}   (expect False -> no real split)")
results["true_pos_definite_square_sign"] = eps_pos
results["true_pos_definite_pseudoscalar_sq_is_plus_I"] = om_pos_sq_plus

# --- 4b. the n=6 case: g69's documentary constant `Cl(6,0) = M8(R)` -----------
# g69_csdr.py:121-124 hardcodes CL6_IS_MATRIX = "M8(R)" with the comment
# "Cl(6,0) ~ M8(R) (unique 8-dim real rep)". Same question as above, one
# dimension down, and the n=6 pseudoscalar does NOT discriminate (omega^2 = -1
# for both signs when n=6), so use the commutant instead: the real algebra
# generated by the six matrices is M_8(R) iff it commutes with an antilinear J
# with J^2=+1, and M_4(H) iff J^2=-1. Search the same factorized ansatz OB10
# used, over both signs, and report what is actually found.
print("\nn=6 CASE -- g69 hardcodes Cl(6,0) = M8(R); the pseudoscalar cannot")
print("decide here (omega^2 = -1 for both signs), so use the commutant.")

PAULIS = {"I": s0, "s1": s1, "s2": s2, "s3": s3}


def commuting_real_structures(gens: list[np.ndarray]) -> dict[str, int]:
    """Antilinear J = M.conj commuting with every generator; report J^2 signs."""
    found: dict[str, int] = {}
    n = gens[0].shape[0]
    ident = np.eye(n, dtype=complex)
    for na, a in PAULIS.items():
        for nb, b in PAULIS.items():
            for nc, c in PAULIS.items():
                M = kron(a, b, c)
                # antilinear J(x) = M conj(x) commutes with linear g iff M conj(g) = g M
                if not all(np.allclose(M @ np.conj(g), g @ M) for g in gens):
                    continue
                sq = M @ np.conj(M)
                if np.allclose(sq, ident):
                    found[f"{na}(x){nb}(x){nc}"] = +1
                elif np.allclose(sq, -ident):
                    found[f"{na}(x){nb}(x){nc}"] = -1
    return found


for label, gens in (("eps=+1 (a true Cl(6,0))", G6), ("eps=-1 (Cl(0,6))", [1j * g for g in G6])):
    js = commuting_real_structures(gens)
    signs = sorted(set(js.values()))
    algebra = (
        "M8(R) (real)" if signs == [+1] else "M4(H) (quaternionic)" if signs == [-1] else str(signs)
    )
    print(f"  {label:24s} -> commuting J found: {len(js):2d}, J^2 signs {signs} -> {algebra}")
    results[f"n6_commutant_{'pos' if gens is G6 else 'neg'}"] = {
        "n_found": len(js),
        "squares": signs,
    }

_pos_signs = sorted(set(commuting_real_structures(G6).values()))
_neg_signs = sorted(set(commuting_real_structures([1j * g for g in G6]).values()))
g69_constant_ok = _pos_signs == [+1]
print(f"  g69's 'Cl(6,0) = M8(R)' matches the eps=+1 commutant: {g69_constant_ok}")
results["g69_cl6_equals_M8R_verified"] = bool(g69_constant_ok)
results["n6_pos_signs"] = _pos_signs
results["n6_neg_signs"] = _neg_signs

# --- 5. verdict ---------------------------------------------------------------
label_bug = (eps_oct == -1) and om_sq_plus and (not om_pos_sq_plus)
conventions_differ = eps_s3 != eps_s6
print("\n" + "=" * 78)
print("FINDINGS")
print("=" * 78)
print(
    f"1. S3 and S6 genuinely use OPPOSITE signs ({eps_s3:+d} vs {eps_s6:+d}): {conventions_differ}"
)
print("   -> C32's diagnosis confirmed independently. Both labels are correct.")
print(f"2. The octonion sub-project's code is eps={eps_oct:+d} but it is labeled Cl(7,0),")
print("   which under this repo's OTHER convention (round67, s6-harm-g0) means eps=+1.")
print(f"   Its own M_8(R)(+)M_8(R) split claim is only available at eps=-1: {label_bug}")
print("   -> LABEL BUG, not a math bug. The matrices and every result are fine.")
results["s3_s6_conventions_genuinely_differ"] = bool(conventions_differ)
results["octonion_label_is_wrong"] = bool(label_bug)
results["octonion_math_is_correct"] = bool(eps_oct == -1 and anticomm_ok and om_is_pm_id)

verdict = "THREE_NAMING_STATES_FOUND__ONE_LABEL_BUG__NO_NEW_MATH_ERROR"
if not (conventions_differ and label_bug):
    verdict = "INCONCLUSIVE"
print(f"\nVERDICT: {verdict}")
results["verdict"] = verdict

RESULTS_PATH.write_text(json.dumps(results, indent=2))
print(f"\nResults -> {RESULTS_PATH}")
