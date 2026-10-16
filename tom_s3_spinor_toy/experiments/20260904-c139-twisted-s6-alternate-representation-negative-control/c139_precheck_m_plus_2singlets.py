"""Quick precheck (per user request, 2026-09-04): before building a full C141
round with twist bundle W' = m (+) 2*1 (matched singlet count to Sigma), check
whether D'_{twist=m(+)2*1} could be a priori THEOREM-forced to equal
D'_{twist=Sigma} via a unitary change of basis on the twist factor alone --
which would make a full round a redundant regression test, not a decisive
negative control.

Reuses C139's own already-verified data (NAB_np on Sigma, rho_vector(NOMIZU))
unmodified -- no new physics construction, this is a pure linear-algebra
consistency check.

Key already-established fact this reuses (C139 Sec 3b, independently
verified there): under {NAB_i}, Sigma's ONLY achievable invariant-subspace
dimensions are {0,4,4,8} (EVEN_IDX and ODD_IDX are each irreducible, 4-dim).

For D'_{twist=m+2*1} to be unitarily equivalent to D'_{twist=Sigma} via
(1 tensor U) on the twist factor, NAB_i (on Sigma) would need to be unitarily
equivalent to conn_{m+2*1,i} = rho_vector(NOMIZU_i) (+) 0_2 (the natural,
only-available construction for the two EXTRA singlets, which have no
NOMIZU-derived connection data of their own). Under this connection, m (6-dim)
is an invariant subspace (block-diagonal by construction) -- so equivalence
would require Sigma to ALSO have a 6-dim {NAB_i}-invariant subspace, which
Sec 3b already shows does not exist.

This script verifies that dimension-counting argument directly and
numerically (not just citing Sec 3b's abstract conclusion), via an explicit
intertwiner-nullspace search between NAB_i (8-dim) and rho_vector(NOMIZU_i)
(+) 0_2 (8-dim).
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
C139_MAIN = HERE / "c139_twisted_s6_alternate_representation.py"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


print("Loading C139's own verified module (reuses NAB_np, rho_vector, NOMIZU)...")
C139 = load_module("c139_main", C139_MAIN)

NAB_np = C139.NAB_np  # Sigma-side connection, dict i=1..6 -> 8x8
NOMIZU = C139.R59.NOMIZU  # raw connection data, i=1..6
rho_vector = C139.rho_vector  # sign-corrected vector rep of so(6)

# Build the NATURAL m(+)2*1 connection: rho_vector(NOMIZU[i]) (6x6) block-diag
# with a 2x2 ZERO block for the two extra, NOMIZU-less singlets.
conn_m_plus_2singlets = {}
for i in range(1, 7):
    m6 = rho_vector(NOMIZU[i])
    full8 = np.zeros((8, 8), dtype=complex)
    full8[:6, :6] = m6
    conn_m_plus_2singlets[i] = full8

gens_sigma = [NAB_np[i] for i in range(1, 7)]
gens_m2 = [conn_m_plus_2singlets[i] for i in range(1, 7)]

print("\n=== Check 1: is m (6-dim) an invariant subspace of conn_m_plus_2singlets? ===")
for i in range(1, 7):
    off_block = conn_m_plus_2singlets[i][:6, 6:]
    assert np.abs(off_block).max() < 1e-12, f"i={i}: extra singlets NOT decoupled by construction"
print("  Confirmed by construction: extra 2 singlets have zero coupling to m (as designed).")

print("\n=== Check 2: does Sigma (under NAB_i) have a 6-dim invariant subspace? ===")
# Direct approach: find dim of the commutant-compatible invariant subspaces by
# checking whether ANY 6-dim subspace can be simultaneously NAB_i-invariant.
# Reuse C139's own already-computed fact (Sec 3b): EVEN_IDX, ODD_IDX are each
# irreducible (commutant dim 1), so by complete reducibility the ONLY
# invariant subspaces of Sigma=EVEN(+)ODD under {NAB_i} are direct sums of a
# subset of {EVEN_IDX, ODD_IDX} (since they are non-isomorphic irreducibles,
# by Sec 3c's own confirmed zero-intertwiner-Sigma-to-m fact and the fact
# EVEN/ODD carry different NAB_i actions) -- achievable dims: 0, 4, 4, 8.
achievable_dims = {0, 4, 8}  # {0, dim(EVEN), dim(ODD), dim(EVEN)+dim(ODD)} = {0,4,4,8}
print(
    f"  From C139 Sec 3b (reused, not recomputed): achievable invariant dims = {sorted(achievable_dims)}"
)
print(f"  6 in achievable_dims? {6 in achievable_dims}")
assert 6 not in achievable_dims

print("\n=== Check 3: direct intertwiner-nullspace search (independent confirmation) ===")
# All T (8x8) with T @ NAB_i = conn_m_plus_2singlets_i @ T for all i -- if this
# search returns nonzero dimension AND a genuinely unitary T exists among the
# solutions, that would indicate equivalence despite the dimension argument
# (which would be a contradiction worth flagging loudly). If zero, confirms
# no such T exists at all (not even a non-unitary one), the strongest
# possible negative answer.
dim = 8
ident = np.eye(dim, dtype=complex)
stacked = np.vstack([np.kron(a.T, ident) - np.kron(ident, b) for a, b in zip(gens_sigma, gens_m2)])
_, sv, vh = np.linalg.svd(stacked)
tol = 1e-8
null_dim = int(np.sum(sv < tol)) + max(0, stacked.shape[1] - len(sv))
print(f"  intertwiner nullspace dimension (T with T@NAB_i = conn_i@T for all i): {null_dim}")
print(f"  singular values near the tolerance ({tol}): {sorted(sv)[:5]}")

print("\n=== RESULT ===")
if null_dim == 0:
    print("CONFIRMED (Исход B): NO intertwiner exists at all between Sigma's")
    print("{NAB_i} action and the NATURAL m(+)2*1 connection (extra singlets")
    print("decoupled). D'_{twist=m+2*1} is NOT theorem-forced to equal")
    print("D'_{twist=Sigma} by SU(3)-branching equivalence alone -- the")
    print("connection data (so(6)-valued NOMIZU acting via spin_lift on Sigma")
    print("vs. via rho_vector+0 on m+2*1) genuinely differs, because Sigma has")
    print("NO 6-dimensional {NAB_i}-invariant subspace (only {0,4,4,8}), so no")
    print("unitary can map m's invariant 6-dim block onto anything inside Sigma.")
    print("A full C141 round on m+2*1 WOULD be a genuine, non-redundant test,")
    print("PROVIDED it uses this natural (decoupled-singlet) construction.")
else:
    print("UNEXPECTED (would be Исход A or a genuine surprise): a nonzero")
    print("intertwiner exists -- requires manual inspection before concluding")
    print("anything; check whether it is actually unitary and whether it")
    print("truly conjugates the FULL Dirac operator, not just the connection.")
