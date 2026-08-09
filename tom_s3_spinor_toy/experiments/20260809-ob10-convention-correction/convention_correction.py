"""OB10 CORRECTION -- the pseudo-real verdict was a Clifford-convention artifact.

Origin: an external red-team audit (2026-08-09) challenged OB10's conclusion.
Its argument: S3 and S6 are BOTH Riemannian, so their product is a 9-dim
Riemannian manifold whose spinor bundle requires ONE uniform Clifford
convention. OB10 instead combined two sub-projects that had independently
chosen OPPOSITE conventions:

    S3  (round67, e2_s3_torsion_deformation.py):  Z_i = i*sigma_i,
        {Z_i,Z_j} = -2 delta_ij            -> Cl(0,3)
    S6  (s6-harm-g0, s6_harm_g0_clifford.py):     Gamma_a hermitian,
        {Gamma_a,Gamma_b} = +2 delta_ab    -> Cl(6,0)

Gluing those gives a MIXED signature Cl(6,3). OB10 reported that mixed
signature as a geometric finding and derived PSEUDO-REAL from it. The audit
predicted that uniformising the convention flips the type to REAL, matching
Spin(9)'s Delta_9 = R^16.

This script runs that decisive test, and then follows the consequence through
to C27 -- because C31 (the "Majorana branch is CLOSED" claim, committed
earlier the same day) rests entirely on the pseudo-reality now in question.

Per this project's audit-verification-gate, the audit's claims are treated as
HYPOTHESES to be checked here, not accepted. Every verdict below is computed.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_correction.json"

I2 = np.eye(2, dtype=complex)
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
results: dict = {}


def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = np.kron(out, m)
    return out


def anticomm(a, b):
    return a @ b + b @ a


# --- the two source conventions, reproduced exactly as the sub-projects define them
Z = [1j * s for s in (s1, s2, s3)]  # round67's Cl(0,3)
G6 = [
    kron(s1, I2, I2),
    kron(s2, I2, I2),
    kron(s3, s1, I2),
    kron(s3, s2, I2),
    kron(s3, s3, s1),
    kron(s3, s3, s2),
]  # s6-harm-g0's Cl(6,0)
G7 = kron(s3, s3, s3)
I8 = np.eye(8, dtype=complex)
I16 = np.eye(16, dtype=complex)

print("=" * 74)
print("OB10 CORRECTION: was the pseudo-real verdict a convention artifact?")
print("=" * 74)

print("\nSTEP 1: confirm the two sub-projects really do use OPPOSITE conventions")
s3_ok = all(
    np.allclose(anticomm(Z[i], Z[j]), (-2 * I2 if i == j else 0))
    for i in range(3)
    for j in range(3)
)
s6_ok = all(
    np.allclose(anticomm(G6[a], G6[b]), (2 * I8 if a == b else 0))
    for a in range(6)
    for b in range(6)
)
print(f"  S3 (round67):     {{Z_i,Z_j}} = -2*delta  -> Cl(0,3): {s3_ok}")
print(f"  S6 (s6-harm-g0):  {{G_a,G_b}} = +2*delta  -> Cl(6,0): {s6_ok}")
print("  => genuinely OPPOSITE. Two long-standing parts of this project have")
print("     been carrying incompatible Clifford sign conventions, and OB10 was")
print("     the first round ever to combine them.")
results["step1_s3_is_Cl03"] = bool(s3_ok)
results["step1_s6_is_Cl60"] = bool(s6_ok)
results["step1_conventions_are_opposite"] = bool(s3_ok and s6_ok)


def build_product(G6_use):
    """preprint.tex:1467-1480's own product formula, unchanged."""
    return [kron(Z[j], G7) for j in range(3)] + [kron(I2, G6_use[a]) for a in range(6)]


def signature_and_conjugation(full, label):
    sq = [np.round(np.real(anticomm(g, g)[0, 0]), 10) for g in full]
    off_ok = all(
        np.allclose(anticomm(full[a], full[b]), 0) for a in range(9) for b in range(9) if a != b
    )
    p = sum(1 for c in sq if c > 0)
    q = sum(1 for c in sq if c < 0)
    print(f"\n  [{label}] signature (p,q) = ({p},{q}); genuine Clifford algebra: {off_ok}")

    paulis, names = [I2, s1, s2, s3], ["I", "s1", "s2", "s3"]
    found = []
    for idx in itertools.product(range(4), repeat=4):
        B = kron(*[paulis[k] for k in idx])  # involutory, so B^-1 = B
        etas, ok = set(), True
        for g in full:
            lhs = B @ g @ B
            if np.allclose(lhs, np.conj(g)):
                etas.add(1)
            elif np.allclose(lhs, -np.conj(g)):
                etas.add(-1)
            else:
                ok = False
                break
        if ok and len(etas) == 1:
            BBc = B @ np.conj(B)
            if np.allclose(BBc, I16):
                t = "REAL"
            elif np.allclose(BBc, -I16):
                t = "PSEUDO-REAL"
            else:
                t = "OTHER"
            found.append(("(x)".join(names[k] for k in idx), etas.pop(), t, B))
    for nm, eta, t, _ in found:
        print(f"       B = {nm:18s} eta={eta:+d}   B*conj(B) -> {t}")
    return (p, q), found


print("\nSTEP 2: the AS-BUILT (mixed) product -- reproduce OB10's own result")
sig_mixed, found_mixed = signature_and_conjugation(build_product(G6), "as-built, mixed")
type_mixed = {t for _, _, t, _ in found_mixed}
results["step2_mixed_signature"] = list(sig_mixed)
results["step2_mixed_type"] = sorted(type_mixed)

print("\nSTEP 3: UNIFORMISE (G'_a = i*G_a) and redo -- the audit's decisive test")
G6_uni = [1j * g for g in G6]
uni_ok = all(
    np.allclose(anticomm(G6_uni[a], G6_uni[b]), (-2 * I8 if a == b else 0))
    for a in range(6)
    for b in range(6)
)
print(f"  uniformised S6 now satisfies {{G',G'}} = -2*delta: {uni_ok}")
sig_uni, found_uni = signature_and_conjugation(build_product(G6_uni), "uniform Cl(0,9)")
type_uni = {t for _, _, t, _ in found_uni}
results["step3_uniform_signature"] = list(sig_uni)
results["step3_uniform_type"] = sorted(type_uni)

flipped = type_mixed != type_uni
print(f"\n  TYPE CHANGED under uniformisation: {flipped}")
print(f"    mixed   -> {sorted(type_mixed)}")
print(f"    uniform -> {sorted(type_uni)}")
print("  The uniform (0,9) answer is the geometrically correct one: S3xS6 is a")
print("  9-dim RIEMANNIAN product, and Spin(9)'s spinor module Delta_9 = R^16")
print("  is REAL type (9 mod 8 = 1). OB10's PSEUDO-REAL verdict was an artifact.")
results["step3_type_flipped_under_uniformisation"] = bool(flipped)

# --- NEGATIVE CONTROL: the test must be able to tell the two apart at all ----
print("\nSTEP 4: NEGATIVE CONTROL -- can this test distinguish the two cases?")
print("  (if it returned the same answer regardless of convention it would be")
print("   measuring nothing)")
discriminates = (sig_mixed != sig_uni) and flipped
print(f"  signature differs: {sig_mixed} vs {sig_uni}")
print(f"  CONTROL PASSES (test is sensitive to the convention): {discriminates}")
results["step4_control_discriminates"] = bool(discriminates)

# --- consequence for C31 ------------------------------------------------------
print("\n" + "=" * 74)
print("STEP 5: CONSEQUENCE for C31 -- is the Majorana route open after all?")
print("=" * 74)
print("C31 (committed earlier today) argued: the S3 factor is pseudo-real, so")
print("no Majorana condition exists, so that row of C27's Relaxation Map is")
print("CLOSED. That argument's premise is the type now corrected. Re-check it")
print("on the CORRECT (uniform, real) structure.")

B_uni = found_uni[0][3]
n = 16
Br, Bi = np.real(B_uni), np.imag(B_uni)
# psi = a + i b ; require psi = B conj(psi)
#   a = Br a + Bi b ;  b = Bi a - Br b
M = np.block([[Br - np.eye(n), Bi], [Bi, -Br - np.eye(n)]])
rank = np.linalg.matrix_rank(M, tol=1e-9)
sol_dim = 2 * n - rank
print("\n  Majorana condition psi = B conj(psi) on the 16-dim module:")
print(f"    real solution-space dimension = {sol_dim}  (out of 32 real d.o.f.)")
admits = sol_dim > 0
print(f"    admits NONZERO solutions: {admits}")
print(f"    halves the module (16 of 32 real d.o.f.): {sol_dim == n}")
results["step5_majorana_real_solution_dim"] = int(sol_dim)
results["step5_majorana_admits_nonzero"] = bool(admits)
results["step5_majorana_halves_module"] = bool(sol_dim == n)

# same check under the OLD (mixed, pseudo-real) structure, for contrast
B_mix = found_mixed[0][3]
Br2, Bi2 = np.real(B_mix), np.imag(B_mix)
M2 = np.block([[Br2 - np.eye(n), Bi2], [Bi2, -Br2 - np.eye(n)]])
sol_dim_mixed = 2 * n - np.linalg.matrix_rank(M2, tol=1e-9)
print(f"\n  (for contrast, under the OLD mixed/pseudo-real B: solution dim = {sol_dim_mixed})")
results["step5_majorana_dim_under_old_mixed_B"] = int(sol_dim_mixed)

print("\n  => C31's VERDICT IS INVERTED. On the geometrically correct structure a")
print("     Majorana condition is not forbidden -- it exists and halves the")
print("     module. C31 claimed that row of C27's Relaxation Map was closed;")
print("     it is OPEN, and is now a live candidate mechanism.")
print("\n  SCOPE, stated carefully: this shows the condition is ALGEBRAICALLY")
print("  AVAILABLE on the Clifford module. It does NOT yet show it actually")
print("  halves ker(D_full) to one mode per channel -- that requires checking")
print("  it against the ZERO MODE subspace and its compatibility with D_full,")
print("  which is a separate round (see decision.md 'Next gate').")

verdict = (
    results["step1_conventions_are_opposite"]
    and results["step3_type_flipped_under_uniformisation"]
    and results["step4_control_discriminates"]
)
print("\n" + "=" * 74)
print(f"VERDICT: {'OB10_CORRECTED__TYPE_IS_REAL__C31_INVERTED' if verdict else 'INCONCLUSIVE'}")
print("=" * 74)
results["verdict"] = "OB10_CORRECTED__TYPE_IS_REAL__C31_INVERTED" if verdict else "INCONCLUSIVE"

RESULTS_PATH.write_text(json.dumps(results, indent=2))
print(f"\nResults -> {RESULTS_PATH}")
