"""C181-B -- correction to C181's item-4 finding, forced by a verbatim re-read
of Tom's section 2.2 (p.13).

C181 concluded that his item 4 ("outer product of the spinor multiplet and its
adjoint, then project out the vector") needed a wording fix, because for ONE
Weyl chirality psi psi^dag has an invariant trace and is reducible as 1 + 3,
hence not the irreducible SO(4) vector.

The C181 skeptic flagged that this assumed "spinor multiplet" = one chirality,
and that if he meant a full Dirac bispinor his sentence stands.  His section 2.2
settles it in his own words: for n ODD the multiplet is "the direct sum of the
two (fundamental) spinor representations" -- n=3 is odd, so for S^3 his object
IS the 4-component bispinor.  And he already writes that the induced action is
"a reducible representation" that "include[s] the basis for a vector multiplet".

So: HIS SENTENCE IS CORRECT.  This script verifies the decomposition that makes
it correct, and locates exactly where in the 16 components the vector sits.
"""

import json

import numpy as np

rng = np.random.default_rng(20260907)
sigma = [
    np.eye(2, dtype=complex),
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
]


def rand_su2():
    a = rng.normal(size=4)
    a /= np.linalg.norm(a)
    return a[0] * sigma[0] + 1j * (a[1] * sigma[1] + a[2] * sigma[2] + a[3] * sigma[3])


res = {}

# ---- 1. block transformation laws under U = diag(u_L, u_R) --------------
worst = {"LL": 0.0, "LR": 0.0, "RL": 0.0, "RR": 0.0}
for _ in range(400):
    psiL, psiR = (
        rng.normal(size=2) + 1j * rng.normal(size=2),
        rng.normal(size=2) + 1j * rng.normal(size=2),
    )
    Psi = np.concatenate([psiL, psiR])
    M = np.outer(Psi, Psi.conj())
    uL, uR = rand_su2(), rand_su2()
    U = np.block([[uL, np.zeros((2, 2))], [np.zeros((2, 2)), uR]])
    Mp = U @ M @ U.conj().T
    blocks = {
        "LL": (slice(0, 2), slice(0, 2), uL, uL),
        "LR": (slice(0, 2), slice(2, 4), uL, uR),
        "RL": (slice(2, 4), slice(0, 2), uR, uL),
        "RR": (slice(2, 4), slice(2, 4), uR, uR),
    }
    for k, (r, c, a, b) in blocks.items():
        worst[k] = max(worst[k], float(np.max(np.abs(Mp[r, c] - a @ M[r, c] @ b.conj().T))))
res["block_transformation_max_error"] = worst

# ---- 2. the two invariant traces (the two singlets) ---------------------
tr_LL, tr_RR = 0.0, 0.0
for _ in range(400):
    psiL, psiR = (
        rng.normal(size=2) + 1j * rng.normal(size=2),
        rng.normal(size=2) + 1j * rng.normal(size=2),
    )
    Psi = np.concatenate([psiL, psiR])
    M = np.outer(Psi, Psi.conj())
    uL, uR = rand_su2(), rand_su2()
    U = np.block([[uL, np.zeros((2, 2))], [np.zeros((2, 2)), uR]])
    Mp = U @ M @ U.conj().T
    tr_LL = max(tr_LL, abs(np.trace(Mp[0:2, 0:2]) - np.trace(M[0:2, 0:2])))
    tr_RR = max(tr_RR, abs(np.trace(Mp[2:4, 2:4]) - np.trace(M[2:4, 2:4])))
res["invariant_trace_LL_max_change"] = float(tr_LL)
res["invariant_trace_RR_max_change"] = float(tr_RR)

# ---- 3. WHICH block is the IRREDUCIBLE vector -------------------------
# FIRST ATTEMPT (kept in the record, it FAILED as a test): compare the
# invariance of |x| built from each block.  Both came out invariant to 1e-15,
# because |x|^2 = 1/2 Tr(M^dag M) is the Frobenius norm, invariant under
# M -> u M v^dag for ANY unitaries u,v -- so it holds for every block and
# discriminates nothing.  Recorded, not deleted: it is the 4th
# cannot-discriminate check in this round sequence.
#
# REAL discriminator -- does a SINGLET split off?
#   diagonal block  M_LL -> u_L M_LL u_L^dag : Tr is invariant by itself,
#                   so 1 splits off  =>  REDUCIBLE (1 + 3)
#   off-diag block  M_LR -> u_L M_LR u_R^dag : Tr is NOT invariant,
#                   no component splits off  =>  IRREDUCIBLE (2,2)
#
# WHICH HALF ACTUALLY CARRIES INFORMATION -- corrected after an independent code
# review, and the correction is measured below rather than asserted here.
# The diagonal half is the identity Tr(u A u^dag) = Tr(A) (trace cyclicity plus
# unitarity), which holds for ANY 2x2 matrix conjugated by the same unitary on
# both sides -- whether or not it was built from Psi. It therefore says nothing
# about the construction being correct. `junk_control_diag_y0_max_drift` below
# proves this by running the identical test on an UNRELATED random matrix.
# ALL of the discriminator's falsifying power is in the OFF-DIAGONAL half:
# `offdiag_x0_drift > 1e-3` genuinely can come out False -- e.g. slice the
# diagonal block by mistake and it collapses to ~0 by the same identity.
offdiag_x0_drift, diag_y0_drift = 0.0, 0.0
offdiag_norm_drift = 0.0
junk_y0_drift = 0.0
for _ in range(400):
    psiL = rng.normal(size=2) + 1j * rng.normal(size=2)
    psiR = rng.normal(size=2) + 1j * rng.normal(size=2)
    Psi = np.concatenate([psiL, psiR])
    M = np.outer(Psi, Psi.conj())
    uL, uR = rand_su2(), rand_su2()
    U = np.block([[uL, np.zeros((2, 2))], [np.zeros((2, 2)), uR]])
    Mp = U @ M @ U.conj().T
    # component 0 (the would-be singlet) of each block
    x0, x0p = 0.5 * np.trace(M[0:2, 2:4]), 0.5 * np.trace(Mp[0:2, 2:4])
    y0, y0p = 0.5 * np.trace(M[0:2, 0:2]), 0.5 * np.trace(Mp[0:2, 0:2])
    offdiag_x0_drift = max(offdiag_x0_drift, abs(x0p - x0))
    diag_y0_drift = max(diag_y0_drift, abs(y0p - y0))

    # CONTROL ON THE CONTROL: the same diagonal-block test, run on a matrix with
    # no relation to Psi at all. If this drifts as little as the genuine block,
    # the diagonal half is an identity and carries no evidence whatsoever.
    junk = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    junk_p = uL @ junk @ uL.conj().T
    junk_y0_drift = max(junk_y0_drift, abs(0.5 * np.trace(junk_p) - 0.5 * np.trace(junk)))

    # Frobenius norm of the off-diagonal block. NOT evidence about representation
    # content -- see the withdrawal note below. Retained only as a sanity check
    # that the transformation actually applied was unitary.
    x = np.array([0.5 * np.trace(s.conj().T @ M[0:2, 2:4]) for s in sigma])
    xp = np.array([0.5 * np.trace(s.conj().T @ Mp[0:2, 2:4]) for s in sigma])
    offdiag_norm_drift = max(offdiag_norm_drift, abs(np.linalg.norm(xp) - np.linalg.norm(x)))

res["DISCRIMINATOR_offdiag_LR_singlet_x0_max_drift"] = float(offdiag_x0_drift)
res["diag_LL_singlet_y0_max_drift_IDENTITY_NOT_EVIDENCE"] = float(diag_y0_drift)
res["junk_control_diag_y0_max_drift"] = float(junk_y0_drift)
res["diag_half_is_an_identity"] = bool(junk_y0_drift < 1e-10)
res["discriminates"] = bool(offdiag_x0_drift > 1e-3 and diag_y0_drift < 1e-10)
res["falsifying_power_is_entirely_in"] = "offdiag_x0_drift > 1e-3"
res["UNITARITY_SANITY_ONLY_offdiag_norm_max_drift"] = float(offdiag_norm_drift)
res["WITHDRAWN_frobenius_norm_test"] = (
    "Both blocks gave ~1e-15. The Frobenius norm is invariant under "
    "M -> u M v^dag for ANY unitaries and ANY matrix, so it discriminates "
    "nothing and is withdrawn as evidence. The value above is retained ONLY as "
    "a check that the transformation applied was unitary, and must not be "
    "quoted in support of the (2,2) identification."
)

# ---- 4. dimension bookkeeping ------------------------------------------
res["decomposition"] = {
    "Psi": "S+ (+) S-  =  (2,1) (+) (1,2),  dim 4   [his n odd case]",
    "Psi Psi^dag": "dim 16",
    "LL = S+ x S+*": "(1,1) (+) (3,1)   dim 1+3",
    "RR = S- x S-*": "(1,1) (+) (1,3)   dim 1+3",
    "LR = S+ x S-*": "(2,2)             dim 4   <-- THE VECTOR",
    "RL = S- x S+*": "(2,2)             dim 4   <-- and again",
    "total": 1 + 3 + 1 + 3 + 4 + 4,
}
res["verdict"] = (
    "HIS-SENTENCE-IS-CORRECT: reducible, and it DOES include a vector "
    "multiplet -- twice, in the two off-diagonal blocks. C181's "
    "'correction' applied only to a single-chirality reading his own "
    "section 2.2 rules out for n odd."
)

print(json.dumps(res, indent=2))
with open("results_c181b.json", "w", encoding="utf-8") as f:
    json.dump(res, f, indent=2)
