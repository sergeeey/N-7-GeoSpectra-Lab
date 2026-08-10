"""W1-lift: is ASSUMPTION A1-lift an assumption, or a theorem?

WHAT WAS FLAGGED. C55 derived A1 (iota flips D) from the bare Peter-Weyl pullback and
flagged: "ASSUMPTION A1-lift, not discharged: the geometric spinor lift may differ from
the bare pullback by a unitary. The conclusion survives any such factor that preserves
the isotypic decomposition -- a much weaker input than A1 itself, but it IS an input."
This is the same shape as W1 (C50): there the worry was a non-factorizing J; here it is a
non-block-preserving lift of U_iota.

THE ARGUMENT, in prose (Structure-Bias Guard: reason first, serialize the conclusion).
iota(ag) = g^-1 a^-1 means iota intertwines LEFT translation by a with RIGHT translation
by a^-1 -- pure group associativity, no convention anywhere. Define the TWISTED action of
(a,b) in SU(2)xSU(2) on the (j,k) block (V_j under left, V_k* under right) as the PLAIN
action of the swapped pair (b,a). Because V_j (x) V_k* is one irrep per factor of a
product group, twisted-(j,k) is, as an abstract SU(2)xSU(2)-module, IDENTICAL to
plain-(k,j) -- a relabelling. So "U intertwines twisted-(j,k) with plain-(j',k')" is
exactly "U is a plain-equivariant self-map of (k,j) if (j',k')=(k,j), else a map between
INEQUIVALENT irreps." Two standard facts finish it: (1) such tensor irreps are
inequivalent unless both labels match; (2) Schur's lemma -- equivariant maps between
inequivalent irreps are ZERO, equivariant self-maps of an irrep (compact group, over C)
are SCALARS.

WHY THIS IS CHECKED COMPUTATIONALLY, not just cited. The Lie-algebra bookkeeping for a
TWISTED tensor action is easy to get subtly wrong by hand (which generator pairs with
which slot, conjugate vs transpose for the dual). Rather than trust a by-hand derivation,
the equivariance condition is built explicitly from su(2) generator matrices and solved as
a linear system (SVD null space) -- exactly the same discipline as every other round this
session that reached for a lemma name: verify the specific instance, don't just cite it.

Predictions S1-S5 are recorded in claim.md BEFORE this ran. S3 is the load-bearing negative
control: SAME total dimension, WRONG label (not swapped) -- if dimension alone forced
vanishing, S3 would be uninformative; it must be the LABEL match specifically.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_a1lift.json"
results: dict = {}


def spin_generators(j: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Standard Hermitian angular-momentum matrices Jx,Jy,Jz for spin j, basis m=j..-j."""
    dim = round(2 * j + 1)
    ms = [j - i for i in range(dim)]  # m = j, j-1, ..., -j
    jz = np.diag(ms).astype(complex)
    jp = np.zeros((dim, dim), dtype=complex)
    for i in range(1, dim):
        m = ms[i]  # target state (after raising) has m+1 = ms[i-1]
        jp[i - 1, i] = np.sqrt(j * (j + 1) - m * (m + 1))
    jm = jp.conj().T  # J- = (J+)^dagger for Hermitian Jx,Jy and real J+ built this way
    jx = (jp + jm) / 2
    jy = (jp - jm) / (2 * 1j)
    return jx, jy, jz


def dual_generators(gens: tuple[np.ndarray, ...]) -> tuple[np.ndarray, ...]:
    """Generators of the dual (contragredient) rep on V*: dpi*(X) = -dpi(X)^T = conj(dpi(X))
    for the ANTI-Hermitian Lie-algebra generator dpi(X) = -i*J. In terms of the physics
    Hermitian J, that works out to J* = -conj(J), not conj(J) -- confirmed by hand-check:
    conj(J) alone flips the su(2) commutator's overall sign ([conj(Jx),conj(Jy)] = -i*conj(Jz)
    instead of +i*conj(Jz)), so it is not even a valid representation on its own; the extra
    minus sign restores [J*x,J*y] = i*J*z. First version of this function used bare conj(g)
    and every equivariance test (S2) returned null-dim 0 where Schur's lemma requires 1 --
    caught by hand-verifying the simplest (j,k)=(0,1/2) case against explicit Pauli matrices
    before accepting the numeric result.
    """
    return tuple(-g.conj() for g in gens)


def vec_constraint(a_src: np.ndarray, b_tgt: np.ndarray) -> np.ndarray:
    """Rows encoding U @ a_src = b_tgt @ U as a linear constraint on vec(U) (col-major)."""
    dim_src = a_src.shape[0]
    dim_tgt = b_tgt.shape[0]
    return np.kron(a_src.T, np.eye(dim_tgt)) - np.kron(np.eye(dim_src), b_tgt)


def null_dim(rows: list[np.ndarray], tol: float = 1e-9) -> int:
    m = np.vstack(rows)
    sv = np.linalg.svd(m, compute_uv=False)
    max_sv = sv.max() if sv.size else 0.0
    return int(np.sum(sv < tol * max(max_sv, 1.0) + tol))


def plain_block_gens(j: float, k: float) -> dict[str, np.ndarray]:
    """Plain action of (X,Y) on V_j (x) V_k* : X on first slot, Y (conjugated) on second."""
    jxj, jyj, jzj = spin_generators(j)
    jxk, jyk, jzk = dual_generators(spin_generators(k))
    ij, ik = np.eye(round(2 * j + 1)), np.eye(round(2 * k + 1))
    return {
        "X=Jx,Y=0": np.kron(jxj, ik),
        "X=Jy,Y=0": np.kron(jyj, ik),
        "X=Jz,Y=0": np.kron(jzj, ik),
        "X=0,Y=Jx": np.kron(ij, jxk),
        "X=0,Y=Jy": np.kron(ij, jyk),
        "X=0,Y=Jz": np.kron(ij, jzk),
    }


def twisted_block_gens(j: float, k: float) -> dict[str, np.ndarray]:
    """Twisted action of (X,Y): plain action of the SWAPPED pair (Y,X)."""
    jxj, jyj, jzj = spin_generators(j)
    jxk, jyk, jzk = dual_generators(spin_generators(k))
    ij, ik = np.eye(round(2 * j + 1)), np.eye(round(2 * k + 1))
    # twisted(X,Y) = plain(Y,X) = [Y acting via j-slot generator] + [X acting via k*-slot generator]
    return {
        "X=Jx,Y=0": np.kron(ij, jxk),  # plain(Y=0,X=Jx) -> X goes to the k*-slot
        "X=Jy,Y=0": np.kron(ij, jyk),
        "X=Jz,Y=0": np.kron(ij, jzk),
        "X=0,Y=Jx": np.kron(jxj, ik),  # plain(Y=Jx,X=0) -> Y goes to the j-slot
        "X=0,Y=Jy": np.kron(jyj, ik),
        "X=0,Y=Jz": np.kron(jzj, ik),
    }


def equivariance_null_dim(src_jk: tuple[float, float], tgt_jk: tuple[float, float]) -> int:
    twisted = twisted_block_gens(*src_jk)
    plain = plain_block_gens(*tgt_jk)
    rows = [vec_constraint(twisted[key], plain[key]) for key in twisted]
    return null_dim(rows)


print("=" * 78)
print("W1-lift -- is A1-lift forced by equivariance (Schur), or merely assumed?")
print("=" * 78)

# --- sanity: generators are correct spin-j representations -------------------
print("\nSanity -- generator commutators [Jx,Jy]=i*Jz etc, for j=0,1/2,1,3/2")
comm_ok = True
for j in (0.0, 0.5, 1.0, 1.5):
    jx, jy, jz = spin_generators(j)
    comm_ok &= bool(np.allclose(jx @ jy - jy @ jx, 1j * jz))
    comm_ok &= bool(np.allclose(jy @ jz - jz @ jy, 1j * jx))
    comm_ok &= bool(np.allclose(jz @ jx - jx @ jz, 1j * jy))
    herm_ok = all(np.allclose(g, g.conj().T) for g in (jx, jy, jz))
    print(f"    j={j:4.1f}  dim={round(2 * j + 1)}  su(2) algebra: {comm_ok}  Hermitian: {herm_ok}")
print(f"  generators verified: {comm_ok}")
results["sanity_generators_ok"] = bool(comm_ok)

# --- S2: the matching pair -- existence AND uniqueness -----------------------
print("\nS2 -- matching pair: twisted-(j,k) vs plain-(k,j).  Expect null dim EXACTLY 1.")
s2_cases = [(0.0, 0.5), (0.5, 1.0), (1.0, 0.5), (1.5, 1.0), (1.0, 1.0)]
s2 = {}
for j, k in s2_cases:
    d = equivariance_null_dim((j, k), (k, j))
    s2[f"({j},{k})->({k},{j})"] = d
    print(
        f"    twisted-({j},{k}) -> plain-({k},{j})   [dims {round(2 * j + 1) * round(2 * k + 1)}]"
        f"   null dim = {d}   (expect 1)"
    )
s2_ok = all(v == 1 for v in s2.values())
print(f"  S2: every matching pair gives EXACTLY 1-dim solution (existence+uniqueness): {s2_ok}")
results["s2_matching_pairs"] = s2
results["s2_all_unique"] = bool(s2_ok)

# --- S3: the load-bearing negative control -- same dim, WRONG label ----------
print("\nS3 -- NEGATIVE CONTROL: twisted-(j,k) vs plain-(j,k) itself (same dim, NOT swapped)")
s3_cases = [(1.0, 0.0), (0.5, 1.5), (1.0, 1.0), (0.5, 0.5)]
s3 = {}
for j, k in s3_cases:
    d = equivariance_null_dim((j, k), (j, k))
    s3[f"({j},{k})->({j},{k})"] = d
    same_label = j == k
    print(
        f"    twisted-({j},{k}) -> plain-({j},{k})   "
        f"[same dim, {'labels EQUAL by chance' if same_label else 'wrong label'}]"
        f"   null dim = {d}   (expect 0 unless j==k)"
    )
s3_ok = all(
    (v == 0) or (j == k and v == 1) for (j, k), v in zip(s3_cases, s3.values(), strict=False)
)
print("  (when j==k, plain-(j,k) IS the correct target (k,j)=(j,j), so dim=1 there is CORRECT,")
print(
    "   not a control failure -- included to show the machinery is consistent, not cherry-picked)"
)
print("  S3: same-dimension MISMATCHED labels give null dim 0 -- dimension alone does")
print(f"      NOT force vanishing, only the label match does: {s3_ok}")
results["s3_mismatched_same_dim"] = s3
results["s3_discriminates"] = bool(s3_ok)

# --- S4: basic sanity -- different-dimension pairs give 0 --------------------
print("\nS4 -- sanity: different-dimension pairs")
s4_cases = [((0.5, 0.0), (1.0, 0.5)), ((1.0, 1.0), (0.5, 0.0))]
s4 = {}
for src, tgt in s4_cases:
    d = equivariance_null_dim(src, tgt)
    s4[f"{src}->{tgt}"] = d
    print(f"    twisted-{src} -> plain-{tgt}   null dim = {d}   (expect 0)")
s4_ok = all(v == 0 for v in s4.values())
print(f"  S4: {s4_ok}")
results["s4_different_dim"] = s4
results["s4_ok"] = bool(s4_ok)

# --- S5: connect back to C55/C56/C57's own (j,k) example ---------------------
print("\nS5 -- connect to C55's own example: (j,k) = (0, 1/2), the n=0 level")
d55 = equivariance_null_dim((0.0, 0.5), (0.5, 0.0))
print(f"    twisted-(0,1/2) -> plain-(1/2,0)  [C55's own n=0 pair]   null dim = {d55}")
print("    This is the SAME (j,k) pair C55/C56 used for U_iota's block. The phase freedom")
print("    C56 exploited (c = +-1 or +-i) IS this null-dim-1 freedom -- Schur's scalar,")
print("    nothing more. C56/C57 are corroborated, not contradicted.")
results["s5_c55_pair_null_dim"] = d55
results["s5_matches_c56_freedom"] = bool(d55 == 1)

# --- VERDICT -----------------------------------------------------------------
print("\n" + "=" * 78)
ok = comm_ok and s2_ok and s3_ok and s4_ok and (d55 == 1)
verdict = (
    "A1_LIFT_IS_A_THEOREM_NOT_AN_ASSUMPTION__SCHUR_FORCES_BLOCK_PRESERVATION"
    if ok
    else "INCONCLUSIVE"
)
print(f"VERDICT: {verdict}")
print("=" * 78)
if ok:
    print("  C59 STANDS. ASSUMPTION A1-lift is DISCHARGED -- it was never a free choice.")
    print()
    print("  Any unitary implementing iota EQUIVARIANTLY (intertwining L_a with R_{a^-1},")
    print("  which is what 'a lift of the isometry iota' MEANS -- pure group associativity,")
    print("  no Clifford sign, no metric convention) is FORCED by Schur's lemma to map the")
    print("  (j,k) isotypic block ONLY to (k,j), and is unique there up to a PHASE.")
    print()
    print("  The negative control (S3) shows this is not a dimension-counting accident:")
    print("  same-dimension, wrong-label pairs give EXACTLY ZERO solutions. Only the label")
    print("  match (forced by the twisted-(j,k) = plain-(k,j) relabelling) produces a")
    print("  nonzero, and then unique-up-to-phase, intertwiner.")
    print()
    print("  CONSEQUENCE. The 'much weaker input' C55 flagged as ASSUMPTION A1-lift is not")
    print("  an input at all -- it is what ANY genuine geometric/Pin-group lift of iota is")
    print("  forced to do. The remaining freedom (S5) is exactly the phase C56 already used,")
    print("  nothing more and nothing less. C55-C58 now rest on ZERO named assumptions about")
    print("  the lift -- only on the definition of 'lift of an isometry' itself.")
results["verdict"] = verdict
RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
print(f"\nResults -> {RESULTS_PATH}")
