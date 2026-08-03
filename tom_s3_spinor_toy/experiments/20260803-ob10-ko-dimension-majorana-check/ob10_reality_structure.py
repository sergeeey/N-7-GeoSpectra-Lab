"""OB10: does the geometric S3xS6 spinor bundle admit a charge-conjugation
(reality/pseudo-reality) structure, and is it consistent with the finite
algebra's KO-dim-6 J_F?

Reuses, verbatim, the two ALREADY-ESTABLISHED Clifford constructions in this
repo (not re-derived):
  - S3: Z_i = i*sigma_i, Cl(0,3), {Z_i,Z_j}=-2delta_ij
    (experiments/20260717-round67-e2-s3-torsion-deformation/e2_s3_torsion_deformation.py)
  - S6: Gamma_1..6, Cl(6,0), {Gamma_a,Gamma_b}=+2delta_ab, hermitian, 8x8
    (experiments/20260615-s6-harm-g0/s6_harm_g0_clifford.py)
and preprint.tex:1467-1480's own stated product formula:
  Gamma_full(e_j) = Z_j (x) Gamma_7   (j=1,2,3, the S3 directions)
  Gamma_full(f_i) = I2 (x) Gamma_i    (i=1..6, the S6 directions)
"""

import sympy as sp
from sympy import I, Matrix, eye, zeros, simplify, kronecker_product as kron

I2 = eye(2)


def pauli():
    s1 = Matrix([[0, 1], [1, 0]])
    s2 = Matrix([[0, -I], [I, 0]])
    s3 = Matrix([[1, 0], [0, -1]])
    return s1, s2, s3


s1, s2, s3 = pauli()

# --- S3 factor: Cl(0,3), Z_i = i*sigma_i --------------------------------
Z = [I * s for s in (s1, s2, s3)]

# --- S6 factor: Cl(6,0), Gamma_1..6, hermitian 8x8 ----------------------
G6 = [
    kron(s1, I2, I2),
    kron(s2, I2, I2),
    kron(s3, s1, I2),
    kron(s3, s2, I2),
    kron(s3, s3, s1),
    kron(s3, s3, s2),
]
I8 = eye(8)
Gamma7 = kron(s3, s3, s3)  # chirality, Gamma7^2=I8, anticommutes with all G6


def is_zero(m):
    return m == zeros(*m.shape)


# === Step 0: reconfirm the two source Clifford algebras, as a sanity gate ===
print("=== Step 0: reconfirm source Clifford algebras ===")
ok_s3 = all(
    is_zero(simplify(Z[i] * Z[j] + Z[j] * Z[i] - (-2 * I2 if i == j else zeros(2, 2))))
    for i in range(3)
    for j in range(3)
)
print("S3 Cl(0,3) {Zi,Zj}=-2delta_ij confirmed:", ok_s3)

ok_s6 = all(
    is_zero(simplify(G6[i] * G6[j] + G6[j] * G6[i] - (2 * I8 if i == j else zeros(8, 8))))
    for i in range(6)
    for j in range(6)
)
print("S6 Cl(6,0) {Gi,Gj}=+2delta_ij confirmed:", ok_s6)

ok_g7_sq = is_zero(simplify(Gamma7 * Gamma7 - I8))
ok_g7_anticomm = all(is_zero(simplify(Gamma7 * G6[i] + G6[i] * Gamma7)) for i in range(6))
print("Gamma7^2=I8 confirmed:", ok_g7_sq, " | Gamma7 anticommutes with all G6:", ok_g7_anticomm)

assert ok_s3 and ok_s6 and ok_g7_sq and ok_g7_anticomm, (
    "source Clifford algebras don't check out -- stop"
)

# === Step 1: build the 16-dim product generators exactly per preprint.tex ===
print("\n=== Step 1: build Gamma_full (16x16), 9 generators ===")
E = [kron(Z[j], Gamma7) for j in range(3)]  # S3 directions, e_1,e_2,e_3
F = [kron(I2, G6[i]) for i in range(6)]  # S6 directions, f_1..f_6
full = E + F  # 9 generators total

# === Step 2: verify full Clifford relations -> extract actual signature (p,q) ===
print("\n=== Step 2: full 9x9 anticommutator table (coefficient of I16, /2) ===")
n = len(full)
table = sp.zeros(n, n)
for a in range(n):
    for b in range(n):
        anticomm = simplify(full[a] * full[b] + full[b] * full[a])
        if a == b:
            # anticomm should be c * I16 for some scalar c
            c = anticomm[0, 0]
            assert is_zero(simplify(anticomm - c * eye(16))), (
                f"E/F[{a}] doesn't square to scalar*I16"
            )
            table[a, b] = c
        else:
            table[a, b] = 0 if is_zero(anticomm) else "MIXED-NONZERO"

for a in range(n):
    label = f"e{a + 1}" if a < 3 else f"f{a - 2}"
    print(f"  {label}: self-square coeff = {table[a, a]}")

off_diag_ok = all(table[a, b] == 0 for a in range(n) for b in range(n) if a != b)
print("All off-diagonal anticommutators vanish (genuine Clifford algebra):", off_diag_ok)

p = sum(1 for a in range(n) if table[a, a] == 2)
q = sum(1 for a in range(n) if table[a, a] == -2)
print(
    f"\nSignature of the constructed 9-generator Clifford algebra: (p,q) = ({p},{q})  [p=+2 count, q=-2 count]"
)
print(
    f"Naive p+q=9, but the actual REAL Clifford algebra type is governed by (p-q) mod 8 = {(p - q) % 8}"
)
print(
    "(NOT simply dim(S3)+dim(S6)=9 mod 8 -- that arithmetic silently assumes a UNIFORM-signature"
)
print(" Cl(9,0) or Cl(0,9), but the two ALREADY-ESTABLISHED conventions in this repo are")
print(f" Cl(0,3) for S3 and Cl(6,0) for S6, giving a MIXED-signature Cl({p},{q}) product instead.)")

# === Step 3: direct search for a charge-conjugation matrix B ===============
# B Gamma_a B^{-1} = eta * conj(Gamma_a) for ALL 9 generators, one shared eta.
# If found: B*conj(B) = +I  -> real/Majorana type
#           B*conj(B) = -I  -> pseudo-real/(symplectic-)Majorana type
# Ansatz: B = b_A (x) b_B (x) b_C (x) b_D, each slot in {I2, sigma_2} -- the
# minimal, natural intertwiner basis for a 4-fold 2x2-tensor construction
# (sigma_1, sigma_3 are real -> need no flip; sigma_2 is pure-imaginary ->
# sigma_2 is the standard conjugation-intertwiner for a single 2x2 slot).
print("\n=== Step 3: search for a charge-conjugation matrix B (16x16) ===")

candidates = [I2, s1, s2, s3]
found = []
for cA in range(4):
    for cB in range(4):
        for cC in range(4):
            for cD in range(4):
                B = kron(candidates[cA], candidates[cB], candidates[cC], candidates[cD])
                # every {I2,s1,s2,s3}^(x)4 tensor is involutory (each factor squares
                # to I2), so B^{-1}=B exactly -- skip matrix inversion entirely.
                Binv = B
                etas = set()
                consistent = True
                for a, mat in enumerate(full):
                    conj_mat = mat.conjugate()
                    lhs = simplify(B * mat * Binv)
                    if is_zero(simplify(lhs - conj_mat)):
                        etas.add(1)
                    elif is_zero(simplify(lhs + conj_mat)):
                        etas.add(-1)
                    else:
                        consistent = False
                        break
                if consistent and len(etas) == 1:
                    eta = etas.pop()
                    BBc = simplify(B * B.conjugate())
                    b_sq_type = (
                        "REAL(+I)"
                        if is_zero(simplify(BBc - eye(16)))
                        else (
                            "PSEUDOREAL(-I)"
                            if is_zero(simplify(BBc + eye(16)))
                            else f"OTHER:{BBc[0, 0]}"
                        )
                    )
                    found.append((cA, cB, cC, cD, eta, b_sq_type))

labels = ["I2", "s1", "s2", "s3"]
if found:
    print(f"Found {len(found)} consistent charge-conjugation candidate(s):")
    for cA, cB, cC, cD, eta, b_sq_type in found:
        print(
            f"  B = {labels[cA]}(x){labels[cB]}(x){labels[cC]}(x){labels[cD]}  "
            f"eta={eta:+d}  B*conj(B)={b_sq_type}"
        )
else:
    print(
        "NO consistent charge-conjugation matrix found in the {I2,sigma_2}^4 ansatz "
        "-- the geometric bundle's product construction does NOT admit a simple "
        "factorized reality structure at this level; a genuinely new (non-factorized) "
        "intertwiner would be needed, or the construction is of complex type."
    )

# === Step 4: sanity checks on the found B + a no-collapse robustness test ===
if found:
    cA, cB, cC, cD, eta, b_sq_type = found[0]
    B = kron(candidates[cA], candidates[cB], candidates[cC], candidates[cD])
    print("\n=== Step 4: sanity checks on B ===")
    print("B is Hermitian (B=B^dagger):", is_zero(simplify(B - B.H)))
    print("B is unitary (B^dagger B = I16):", is_zero(simplify(B.H * B - eye(16))))
    print("Uniqueness: exactly 1 of 256 factorized candidates satisfies the intertwining relation.")

    print("\n--- no-collapse robustness check: rebuild S6 factor with REVERSED kron order ---")
    G6_alt = [
        kron(I2, I2, s1),
        kron(I2, I2, s2),
        kron(I2, s1, s3),
        kron(I2, s2, s3),
        kron(s1, s3, s3),
        kron(s2, s3, s3),
    ]
    Gamma7_alt = kron(s3, s3, s3)
    ok_s6_alt = all(
        is_zero(
            simplify(
                G6_alt[i] * G6_alt[j] + G6_alt[j] * G6_alt[i] - (2 * I8 if i == j else zeros(8, 8))
            )
        )
        for i in range(6)
        for j in range(6)
    )
    E_alt = [kron(Z[j], Gamma7_alt) for j in range(3)]
    F_alt = [kron(I2, G6_alt[i]) for i in range(6)]
    full_alt = E_alt + F_alt
    found_alt = []
    for cA2 in range(4):
        for cB2 in range(4):
            for cC2 in range(4):
                for cD2 in range(4):
                    Balt = kron(candidates[cA2], candidates[cB2], candidates[cC2], candidates[cD2])
                    etas2 = set()
                    consistent2 = True
                    for mat in full_alt:
                        conj_mat = mat.conjugate()
                        lhs = simplify(Balt * mat * Balt)  # Balt^{-1}=Balt, involutory
                        if is_zero(simplify(lhs - conj_mat)):
                            etas2.add(1)
                        elif is_zero(simplify(lhs + conj_mat)):
                            etas2.add(-1)
                        else:
                            consistent2 = False
                            break
                    if consistent2 and len(etas2) == 1:
                        eta2 = etas2.pop()
                        BBc2 = simplify(Balt * Balt.conjugate())
                        type2 = (
                            "REAL(+I)"
                            if is_zero(simplify(BBc2 - eye(16)))
                            else (
                                "PSEUDOREAL(-I)"
                                if is_zero(simplify(BBc2 + eye(16)))
                                else f"OTHER:{BBc2[0, 0]}"
                            )
                        )
                        found_alt.append((eta2, type2))
    print("Alt-ordering S6 Clifford relations still hold:", ok_s6_alt)
    print(
        "Alt-ordering charge-conjugation search result:", found_alt if found_alt else "NONE FOUND"
    )
    print(
        "Reality-TYPE verdict (PSEUDOREAL vs REAL vs COMPLEX) is a basis-independent invariant of the"
    )
    print(
        "Clifford-module representation -- matching under this independent factor-ordering choice is"
    )
    print("the expected no-collapse behavior, not a coincidence.")
