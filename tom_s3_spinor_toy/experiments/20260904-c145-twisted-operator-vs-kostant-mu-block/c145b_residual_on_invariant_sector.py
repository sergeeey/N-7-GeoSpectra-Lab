r"""
C145b -- follow-up check (self-raised, not from the skeptic): C145's main
script found D' != alpha*c(v)(x)Id_W on the FULL 48-dim space (residual
nonzero at 192/2304 entries). But round59/C139's own physics interest is
ONLY the su(3)-invariant domain/target sectors (each 1-dimensional here,
per C139's own Section 4: domain = (Sigma_odd (x) m)^su3, target =
(Sigma_even (x) m)^su3). If the residual vanishes when restricted to THOSE
specific 1-dim subspaces, C145's literal 48x48 REJECT would still be
correct as stated, but its PRACTICAL import for the kernel computation
C139/C141 actually care about would be much weaker than claimed.

This uses C139's own su(3)-invariant-sector construction (su3_ops_np,
rho_m_adnu_np, block_global_gen, invariant_basis_gen) unmodified, applied
to the SAME residual matrix C145 already computed.

Run:  python c145b_residual_on_invariant_sector.py
"""

import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
R59_PATH = (
    HERE.parent / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py"
)
C139_PATH = (
    HERE.parent
    / "20260904-c139-twisted-s6-alternate-representation-negative-control"
    / "c139_twisted_s6_alternate_representation.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


R59 = load_module("round59_route_a_independent", R59_PATH)
C139 = load_module("c139_twisted_s6_alternate_representation", C139_PATH)

E_sym = R59.build_clifford(conj=False)
E_np = {i: np.array(E_sym[i].evalf(), dtype=complex) for i in range(1, 7)}
NAB_sym = {i: R59.spin_lift(R59.NOMIZU[i], E_sym) for i in range(1, 7)}
NAB_np = {i: np.array(NAB_sym[i].evalf(), dtype=complex) for i in range(1, 7)}
su3_ops_sym = {a: R59.spin_lift(R59.ADNU[a], E_sym) for a in range(1, 9)}
su3_ops_np = {a: np.array(su3_ops_sym[a].evalf(), dtype=complex) for a in range(1, 9)}

rho_m_nomizu_np = {i: C139.rho_vector(R59.NOMIZU[i]) for i in range(1, 7)}
rho_m_adnu_np = {a: C139.rho_vector(R59.ADNU[a]) for a in range(1, 9)}

I8 = np.eye(8, dtype=complex)
I6 = np.eye(6, dtype=complex)

# D_Sigma (untwisted, round59's own) and c(v) (C144's own, rebuilt in numpy
# here from the same raw Lam data for a self-contained cross-check).
D_SIGMA = sum((E_np[i] @ NAB_np[i] for i in range(1, 7)), np.zeros((8, 8), dtype=complex))

Lam_raw = {
    1: [(1, 3, 6), (1, 4, 5)],
    2: [(1, 3, 5), (-1, 4, 6)],
    3: [(-1, 1, 6), (-1, 2, 5)],
    4: [(-1, 1, 5), (1, 2, 6)],
    5: [(1, 1, 4), (1, 2, 3)],
    6: [(1, 1, 3), (-1, 2, 4)],
}
C_ijk = np.zeros((7, 7, 7), dtype=complex)
for i in range(1, 7):
    for coeff, a, b in Lam_raw[i]:
        C_ijk[i, a, b] = coeff
        C_ijk[i, b, a] = -coeff

c_v_np = np.zeros((8, 8), dtype=complex)
for i in range(1, 7):
    for j in range(i + 1, 7):
        for k in range(j + 1, 7):
            coeff = C_ijk[i, j, k]
            if coeff != 0:
                c_v_np += coeff * (E_np[i] @ E_np[j] @ E_np[k])

alpha = np.sqrt(3) / 4
regression_ok = np.max(np.abs(D_SIGMA - alpha * c_v_np)) < 1e-10
print(
    f"regression: D_Sigma == alpha*c(v) numerically: {regression_ok}  "
    f"(max diff = {np.max(np.abs(D_SIGMA - alpha * c_v_np)):.3e})"
)
assert regression_ok

# D' (C139's own construction, W=m) and the Kostant candidate.
D_PRIME = C139.build_twisted_dirac_np(E_np, NAB_np, 6, rho_m_nomizu_np)
KOSTANT_CAND = alpha * np.kron(c_v_np, I6)
RESIDUAL = D_PRIME - KOSTANT_CAND
print(
    f"full 48x48 residual max|entry| = {np.max(np.abs(RESIDUAL)):.3e}  "
    f"(nonzero -- matches C145's symbolic finding)"
)

# su(3)-invariant domain/target sectors, C139's own construction, unmodified.
gens_leibniz_48 = [np.kron(su3_ops_np[a], I6) + np.kron(I8, rho_m_adnu_np[a]) for a in range(1, 9)]
domain_block = C139.block_global_gen(R59.ODD_IDX, list(range(6)), 6)
target_block = C139.block_global_gen(R59.EVEN_IDX, list(range(6)), 6)
domain_inv = C139.invariant_basis_gen(gens_leibniz_48, domain_block, 48)
target_inv = C139.invariant_basis_gen(gens_leibniz_48, target_block, 48)
print(f"domain_inv shape: {domain_inv.shape}, target_inv shape: {target_inv.shape}")

# Project the RESIDUAL (not D' or Kostant separately -- the actual quantity
# that matters for "does the mismatch survive on the physics sector") onto
# target_inv^dagger . RESIDUAL . domain_inv.
residual_on_sector = target_inv.conj().T @ RESIDUAL @ domain_inv
print()
print("=" * 78)
print("DECISIVE CHECK: does the residual survive on the su(3)-invariant")
print("domain -> target sector C139/C141 actually use for the kernel test?")
print("=" * 78)
print(f"  target_inv^dagger . RESIDUAL . domain_inv = {residual_on_sector}")
print(f"  |value| = {np.abs(residual_on_sector[0, 0]):.6f}")
survives = np.abs(residual_on_sector[0, 0]) > 1e-8
print(f"  residual survives on the physics-relevant sector: {survives}")

# Also project D' and Kostant candidate separately onto the sector, for
# context (what value does each actually predict for the kernel test).
d_prime_on_sector = complex((target_inv.conj().T @ D_PRIME @ domain_inv)[0, 0])
kostant_on_sector = complex((target_inv.conj().T @ KOSTANT_CAND @ domain_inv)[0, 0])
print()
print(
    f"  D'(actual, C139's own)      on sector = {d_prime_on_sector}  |.|={abs(d_prime_on_sector):.6f}"
)
print(
    f"  alpha*c(v)(x)Id_W(Kostant)  on sector = {kostant_on_sector}  |.|={abs(kostant_on_sector):.6f}"
)
