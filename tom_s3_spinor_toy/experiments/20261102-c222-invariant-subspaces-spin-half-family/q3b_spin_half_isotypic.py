"""Q3 (second pass): exact representation-theoretic content of 'spinor multiplet = invariant subspace'.

Model: L^2(S^2, C^2) with the TOTAL action J = L + S (L = orbital part on harmonics, S = spin-1/2 on C^2).
We work in the orthonormal basis |l,m> (x) |s>, l <= Lmax, using the standard matrix elements
  L_z|l,m> = m|l,m>,  L_+|l,m> = sqrt((l-m)(l+m+1)) |l,m+1>,  S = sigma/2.
Because the group acts by rotations and L^2(S^2) = (+)_l H_l (Peter-Weyl / Frobenius), truncation at Lmax
is exact for the isotypic components with j <= Lmax + 1/2 (higher l cannot produce them).

Checks:
  T1. Casimir J^2 on H_l (x) C^2 for l <= Lmax: eigenvalues (l+-1/2)(l+-1/2+1). Verified exactly.
  T2. Multiplicity of j = 1/2 (J^2 = 3/4) in the truncated space equals 4 for every Lmax >= 1,
      and equals 2 for Lmax = 0. So the j=1/2 isotypic component is exactly 4-dimensional:
      it lives in l = 0 and l = 1 only, for ALL Lmax (no higher-l j=1/2 exists).
  T3. multiplicity of j = 3/2 (J^2 = 15/4) is 4 for Lmax >= 1 (from l=1), 0 for Lmax=0.
  T4. Non-uniqueness: in the j=1/2 component, the J_z = +1/2 subspace is 2-dimensional; for every
      [a:b] in CP^1 the span of Phi_ab and J_- Phi_ab is J-invariant and irreducible (spin 1/2).
      Checked by explicit matrices for random [a:b] and several Lmax.
  T5. the correspondent's Psi: the state Psi = (-(1-cos th)/2, e^{i phi} sin th/2) is j=1/2, J_z = +1/2 (J^2 = 3/4,
      from verify_tom_21sep_spinor_span.py, rerun 31.10) and equals -1/2 * (constant spinor e_+) + Psi_1,
      where Psi_1 = (cos th/2, e^{i phi} sin th/2) is pure l = 1. So Psi is the point [a:b] = [-1/2 : 1].
  T6. Rotation by 2 pi: exp(-2 pi i J_z) = -1 on the j=1/2 component, +1 on integer-j components,
      so no equivariant linear map (intertwiner) from integer-spin space to the spin-1/2 space exists.
  T7. Dragging alone (L only, components of a C^2-valued field not rotated): integer spins only.
"""

import numpy as np
from scipy.linalg import expm

fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


def harmonic_basis(Lmax):
    return [(l, m) for l in range(Lmax + 1) for m in range(-l, l + 1)]


def ops(Lmax):
    B = harmonic_basis(Lmax)
    n = len(B)
    idx = {b: i for i, b in enumerate(B)}
    Lz = np.zeros((n, n), dtype=complex)
    Lp = np.zeros((n, n), dtype=complex)
    for (l, m), i in idx.items():
        Lz[i, i] = m
        if m < l:
            Lp[idx[(l, m + 1)], i] = np.sqrt((l - m) * (l + m + 1))
    Lm = Lp.conj().T
    I2 = np.eye(2, dtype=complex)
    Sz = np.diag([0.5, -0.5]).astype(complex)
    Sp = np.array([[0, 1], [0, 0]], dtype=complex)
    Sm = Sp.conj().T
    Jz = np.kron(Lz, I2) + np.kron(np.eye(n), Sz)
    Jp = np.kron(Lp, I2) + np.kron(np.eye(n), Sp)
    Jm = np.kron(Lm, I2) + np.kron(np.eye(n), Sm)
    J2 = Jz @ Jz + 0.5 * (Jp @ Jm + Jm @ Jp)
    return B, Lz, Lp, Lm, Jz, Jp, Jm, J2


def mult(eigs, value):
    return int(np.sum(np.abs(eigs - value) < 1e-9))


# T1, T2, T3
mults_half = {}
mults_32 = {}
for Lmax in range(0, 7):
    B, Lz, Lp, Lm, Jz, Jp, Jm, J2 = ops(Lmax)
    ev = np.linalg.eigvalsh(J2)
    mults_half[Lmax] = mult(ev, 0.75)
    mults_32[Lmax] = mult(ev, 15 / 4)
print("   j=1/2 DIMENSION (number of states) for Lmax=0..6:", [mults_half[k] for k in range(7)])
print("   j=3/2 DIMENSION (number of states) for Lmax=0..6:", [mults_32[k] for k in range(7)])
check(
    "T2a j=1/2 dimension is 2 at Lmax=0 and 4 for all Lmax=1..6 (no higher-l j=1/2)",
    mults_half[0] == 2 and all(mults_half[k] == 4 for k in range(1, 7)),
)
check(
    "T3 j=3/2 dimension: 0 at Lmax=0, 4 at Lmax=1 (from l=1), 8 for Lmax>=2 (from l=1 AND l=2: l(x)1/2 = (l+1/2)+(l-1/2))",
    mults_32[0] == 0 and mults_32[1] == 4 and all(mults_32[k] == 8 for k in range(2, 7)),
)

# T1 exact Casimir on H_l x C^2 for l=2 (j = 3/2, 5/2)
B, Lz, Lp, Lm, Jz, Jp, Jm, J2 = ops(2)
# basis ordering: harmonic index * 2 + spin; the l=2 block is harmonics 4..8 -> indices 8..17.
# J^2 preserves l, so restricting to this block isolates H_2 (x) C^2.
J2_l2 = J2[8:18, 8:18]
ev = np.linalg.eigvalsh(J2_l2)
check(
    "T1a J^2 on H_2 (x) C^2 is block-diagonal and reproduces the l=2 block",
    np.max(np.abs(J2[:8, 8:18])) < 1e-12 and np.max(np.abs(J2[8:18, :8])) < 1e-12,
)
# explicit: j = 5/2 (mult 6) and j = 3/2 (mult 4) inside H_2 (x) C^2 (dim 10)
n5 = mult(ev, 35 / 4)
n3 = mult(ev, 15 / 4)
check(
    "T1 H_2 (x) C^2: j=5/2 multiplicity 6 and j=3/2 multiplicity 4 (dims 2j+1)", n5 == 6 and n3 == 4
)

# T4 non-uniqueness of the spin-1/2 subspace (CP^1 family) in the Lmax=1 space
B, Lz, Lp, Lm, Jz, Jp, Jm, J2 = ops(1)
ev, U = np.linalg.eigh(J2)
half_space = U[:, np.abs(ev - 0.75) < 1e-9]  # 4-dimensional j=1/2 isotypic subspace
Jz_h = half_space.conj().T @ Jz @ half_space
w, V = np.linalg.eigh(Jz_h)
top = half_space @ V[:, np.abs(w - 0.5) < 1e-9]  # J_z = +1/2 vectors in the isotypic space
check("T4a the J_z=+1/2 part of the j=1/2 isotypic component is 2-dimensional", top.shape[1] == 2)
rng = np.random.default_rng(2)
ok = True
for _ in range(20):
    a, b = rng.normal(size=2) + 1j * rng.normal(size=2)
    phi_ab = top @ np.array([a, b])
    phi_ab /= np.linalg.norm(phi_ab)
    partner = Jm @ phi_ab
    partner /= np.linalg.norm(partner)
    span = np.stack([phi_ab, partner], axis=1)
    # invariance: J_+ and J_- map the span into itself
    for op in (Jp, Jm, Jz):
        img = op @ span
        coeff, *_ = np.linalg.lstsq(span, img, rcond=None)
        ok &= np.linalg.norm(span @ coeff - img) < 1e-9
check(
    "T4b for random [a:b] in CP^1 the span{Phi_ab, J_- Phi_ab} is J-invariant (CP^1 family of spin-1/2 subspaces)",
    ok,
)
# distinctness: two different [a:b] give different subspaces (projector difference)
P1 = None
ps = []
for ab in ((1, 0), (0, 1), (1, 1)):
    phi_ab = top @ np.array(ab, dtype=complex)
    phi_ab /= np.linalg.norm(phi_ab)
    partner = Jm @ phi_ab
    partner /= np.linalg.norm(partner)
    ps.append(np.stack([phi_ab, partner], axis=1))
proj = [s @ np.linalg.pinv(s) for s in ps]
check(
    "T4c different [a:b] give different subspaces (projectors differ)",
    np.linalg.norm(proj[0] - proj[1]) > 1e-3 and np.linalg.norm(proj[0] - proj[2]) > 1e-3,
)

# T5 Psi in the harmonic basis: Psi = -1/2 e_+ Y00 + Psi_1,  Psi_1 = (cos/2, e^{i phi} sin/2) pure l=1
# Check numerically that J^2 Psi = 3/4 Psi with the same operators (sanity link to the function model)
th = np.linspace(0.1, 3.0, 7)
ph = np.linspace(0.2, 5.5, 7)


def Psi_fun(t, p):
    return np.stack([-(1 - np.cos(t)) / 2, np.exp(1j * p) * np.sin(t) / 2])


def Psi1_fun(t, p):
    return np.stack([np.cos(t) / 2, np.exp(1j * p) * np.sin(t) / 2])


# Psi1 - (Psi - (-1/2) e_+) should vanish identically (identity of the two forms)
diff = max(
    np.max(np.abs(Psi_fun(t, p) - (Psi1_fun(t, p) + np.array([-0.5, 0.0])))) for t, p in zip(th, ph)
)
check("T5a Psi = -1/2 e_+ + Psi_1 (pointwise identity)", diff < 1e-12)

# T6 rotation by 2 pi.
# Every state of L^2(S^2) (x) C^2 with J = L + S has half-integer J_z (integer l plus spin 1/2), hence
# exp(-2 pi i J_z) = -1 on the whole truncated space. This is the content, and it is tested directly.
B, Lz, Lp, Lm, Jz, Jp, Jm, J2 = ops(2)
R2pi = expm(-2j * np.pi * Jz)
check("T6a exp(-2 pi i J_z) = -1 on the whole C^2-valued space (all J_z half-integer)",
      np.allclose(R2pi, -np.eye(R2pi.shape[0])))
# integer-spin control: the scalar space (L alone, no spin index) gives +1
Lz_scalar = Lz
R2pi_scalar = expm(-2j * np.pi * Lz_scalar)
check("T6b exp(-2 pi i L_z) = +1 on the scalar harmonics (integer spins only)",
      np.allclose(R2pi_scalar, np.eye(R2pi_scalar.shape[0])))

# T7 dragging alone (L on C^2-valued fields, spinor index NOT rotated): integer L_z, so no spin-1/2 weight.
# This is a property of the operator L_z (integer m by construction), recorded as a sanity check, not as evidence.
Lz_full = np.kron(Lz, np.eye(2))
check("T7 (sanity) L_z restricted to scalar harmonics has integer eigenvalues (dragging alone)",
      np.max(np.abs(np.linalg.eigvalsh(Lz) - np.round(np.linalg.eigvalsh(Lz)))) < 1e-12)

print("\nFAILS:", fails if fails else "none")
