"""Does the Majorana condition actually resolve C27's multiplicity-2?

Short answer computed below: NO -- and this CORRECTS MY OWN C32, which said
that row of C27's Relaxation Map was "OPEN". It is not. C31's original
CONCLUSION survives; only its reasoning was wrong.

THE CHAIN OF THREE STATEMENTS, and where each was right or wrong:

  C31 (2026-08-06): "Majorana row CLOSED, because the relevant factor is
      pseudo-real."  -> CONCLUSION right, REASONING wrong (it cited the
      9-dim product's type, which it had from C28, which was itself an
      artifact).
  C32 (2026-08-09): "C31 INVERTED -- on the corrected (REAL) structure the
      Majorana condition exists and halves the module, so the row is OPEN."
      -> OVER-CORRECTION. True of the MODULE, false of the ZERO MODE.
  this round: the condition does not RESTRICT to the zero mode as a real
      structure. Row is CLOSED after all, for a reason neither earlier
      claim gave.

WHY. C27's zero mode is not the whole 16-dim module. It is

    ker(D_full) = ker(D_S3) (x) ker(D_S6,twisted) = C^2 (x) (1-dim)

The 16-dim module IS real under the uniform convention (C32, correct). But
that reality is a product of TWO quaternionic factors:

    B_S3 conj(B_S3) = -I  (S3 factor, quaternionic)
    B_S6 conj(B_S6) = -I  (S6 factor, quaternionic)
    product          = +I  REAL, since (-1)*(-1) = +1

Restricting to C^2 (x) span(k) collapses the S6 factor to a SCALAR, and a
scalar cannot supply the second minus sign. The induced structure on the
zero mode is therefore quaternionic again, and a quaternionic structure
admits no Majorana condition.

The argument is deliberately made GENERAL in lambda -- it does not depend on
which vector k spans the S6 kernel, which matters because no explicit k
exists in this project (see the scope note at the bottom).
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_majorana_zero_mode.json"

I2 = np.eye(2, dtype=complex)
I8 = np.eye(8, dtype=complex)
I16 = np.eye(16, dtype=complex)
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
results: dict = {}


def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = np.kron(out, m)
    return out


def majorana_solution_dim(M):
    """Real dimension of {psi : psi = M conj(psi)} for an antilinear M.conj."""
    n = M.shape[0]
    Mr, Mi = np.real(M), np.imag(M)
    blk = np.block([[Mr - np.eye(n), Mi], [Mi, -Mr - np.eye(n)]])
    return 2 * n - np.linalg.matrix_rank(blk, tol=1e-9)


print("=" * 74)
print("Does Majorana resolve C27's multiplicity-2? (corrects my own C32)")
print("=" * 74)

# --- STEP 1: the module-level fact C32 established (reconfirm) ---------------
B = kron(s2, s1, s2, s1)  # uniform-convention charge conjugation, from C32
B_S3 = s2
B_S6 = kron(s1, s2, s1)
print("\nSTEP 1: reconfirm C32's module-level result and factor it")
print(f"  B factorizes as B_S3 (x) B_S6: {np.allclose(B, np.kron(B_S3, B_S6))}")
t3 = B_S3 @ np.conj(B_S3)
t6 = B_S6 @ np.conj(B_S6)
s3_quat = bool(np.allclose(t3, -I2))
s6_quat = bool(np.allclose(t6, -I8))
prod_real = bool(np.allclose(B @ np.conj(B), I16))
print(f"  B_S3 conj(B_S3) = -I  (S3 quaternionic): {s3_quat}")
print(f"  B_S6 conj(B_S6) = -I  (S6 quaternionic): {s6_quat}")
print(f"  product = +I (REAL): {prod_real}   <- because (-1)*(-1) = +1")
print(f"  module-level Majorana solution dim: {majorana_solution_dim(B)} of 32 real d.o.f.")
print("  => C32's MODULE-level statement is correct. The question is whether")
print("     it survives restriction to the zero mode.")
results["step1_S3_factor_quaternionic"] = s3_quat
results["step1_S6_factor_quaternionic"] = s6_quat
results["step1_product_real"] = prod_real
results["step1_module_majorana_dim"] = int(majorana_solution_dim(B))

# --- STEP 2: restrict to the zero mode --------------------------------------
print("\nSTEP 2: restrict to ker(D_full) = C^2 (x) span(k)")
print("  If B_S6 preserves span(k), i.e. B_S6 conj(k) = lambda*k, then on the")
print("  2-dim zero mode the induced antilinear map is psi -> lambda*B_S3*conj(psi).")
print("  Tested over a range of lambda (phase AND scale) -- the conclusion must")
print("  not depend on which k spans the kernel, since no explicit k exists.")
lambdas = [1, -1, 1j, -1j, 2.5, 0.3 + 0.7j, -1.4j, 0.01, 100.0]
per_lambda = {}
max_dim = 0
for lam in lambdas:
    M = lam * B_S3
    dim = majorana_solution_dim(M)
    sq_is_neg = bool(np.allclose(M @ np.conj(M), -(abs(lam) ** 2) * I2))
    per_lambda[str(lam)] = {"solution_dim": int(dim), "square_is_minus_mod2": sq_is_neg}
    max_dim = max(max_dim, dim)
    print(f"    lambda={lam!s:12s} dim={dim}   square = -|lambda|^2 * I: {sq_is_neg}")
no_solutions = max_dim == 0
print(f"\n  MAX solution dimension over all tested lambda: {max_dim}")
print(f"  Majorana condition on the ZERO MODE is trivial-only: {no_solutions}")
results["step2_per_lambda"] = per_lambda
results["step2_zero_mode_majorana_trivial_only"] = bool(no_solutions)

# --- STEP 3: why -- the algebraic reason, stated generally -------------------
print("\nSTEP 3: the general reason (independent of k and lambda)")
print("  (lambda B_S3) conj(lambda B_S3) = |lambda|^2 * B_S3 conj(B_S3) = -|lambda|^2 * I")
print("  A quaternionic structure J with J^2 = -c (c > 0) admits no fixed vector:")
print("  psi = J psi  =>  psi = J^2 psi = -c psi  =>  (1+c) psi = 0  =>  psi = 0.")
print("  The S6 factor collapses to a SCALAR on a 1-dim kernel, and a scalar")
print("  cannot supply the second minus sign that made the full module real.")
results["step3_reason"] = (
    "restricting a (quaternionic (x) quaternionic = real) structure to "
    "(full factor) (x) (1-dim subspace) leaves the quaternionic factor alone"
)

# --- STEP 4: NEGATIVE CONTROL ------------------------------------------------
print("\nSTEP 4: NEGATIVE CONTROL -- does the same machinery FIND solutions when")
print("        the structure really is real?")
ctrl_dim = majorana_solution_dim(s1)  # s1 conj(s1) = +I -> real type
ctrl_ok = ctrl_dim > 0
print(f"  real structure B=s1 (B conj(B)=+I): solution dim = {ctrl_dim}  (must be > 0)")
print(f"  CONTROL PASSES (machinery is not vacuously returning 0): {ctrl_ok}")
results["step4_control_real_structure_dim"] = int(ctrl_dim)
results["step4_control_passes"] = bool(ctrl_ok)

# --- STEP 5: the alternative branch -- what if B_S6 does NOT preserve span(k)?
print("\nSTEP 5: the other branch -- what if B_S6 does NOT preserve span(k)?")
print("  Then B maps the zero mode OUT of itself, so the Majorana condition")
print("  cannot be imposed on ker(D_full) at all. Also no halving.")
print("  => BOTH branches give the same answer. The conclusion does not depend")
print("     on the unknown k.")
results["step5_both_branches_agree"] = True

verdict = no_solutions and ctrl_ok and s3_quat and prod_real
print("\n" + "=" * 74)
print(
    f"VERDICT: {'MAJORANA_DOES_NOT_RESOLVE_MULTIPLICITY_2__C32_OVERCORRECTED' if verdict else 'INCONCLUSIVE'}"
)
print("=" * 74)
if verdict:
    print("C31's CONCLUSION survives: that Relaxation Map row is CLOSED.")
    print("C31's REASONING was still wrong (it cited C28's artifact type).")
    print("C32's INVERSION of C31 was itself an over-correction: true of the")
    print("16-dim module, false of the 2-dim zero mode that actually matters.")
    print("C27's multiplicity-2 blocker is UNCHANGED -- 6 modes, not 3.")
results["verdict"] = (
    "MAJORANA_DOES_NOT_RESOLVE_MULTIPLICITY_2__C32_OVERCORRECTED" if verdict else "INCONCLUSIVE"
)

RESULTS_PATH.write_text(json.dumps(results, indent=2))
print(f"\nResults -> {RESULTS_PATH}")
