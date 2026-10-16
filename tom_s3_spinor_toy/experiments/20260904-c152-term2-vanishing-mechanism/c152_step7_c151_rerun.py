r"""
C152 STEP 7 -- re-run C151's pre-registered blind test on the CORRECTED
invariant sector.

WHY THIS FILE EXISTS
  Step 6 established, by an internal adjudicator ([D,G]=0) that is
  cross-validated on S^6 against C145's independently calibrated 1.154701,
  that C151's sector generator carried the wrong relative sign. On the
  corrected sector Term2 is NONZERO (1.0), so C151's "c == 0, VACUOUS"
  verdict was an artifact and its pre-registered question is LIVE again.

  The prediction was frozen in PREREGISTRATION.md before any c existed, and
  the CORRECTED c has never been computed by anyone, so the test is still
  blind. It is executed here.

THE FROZEN PREDICTION (verbatim from PREREGISTRATION.md)
  "c(J.nabla) = +- i . c(nabla)" -- as MATRICES, entry by entry, explicitly
  NOT weakened to norms or singular values.

DISCIPLINE CARRIED OVER FROM C151's OWN FAILURE
  C151 printed "PREDICTION CONFIRMED" over c == 0 because the non-vacuity
  check was computed but not wired into the verdict. Here the vacuity gate is
  FIRST and DOMINANT: if c is zero, nothing else is even evaluated.

Run:  python c152_step7_c151_rerun.py
"""

import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
S2A_PATH = HERE.parent / "20260904-c151-stage0-su3t2-scoping" / "c151_stage2_construct.py"
R59_PATH = (
    HERE.parent / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py"
)
C73B_PATH = (
    HERE.parent
    / "20260811-c73b-torsion-family-genuine-deformation-and-twist-control"
    / "c73b_torsion_family.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


S2A = load_module("c151_stage2_construct", S2A_PATH)
R59 = load_module("round59_route_a_independent", R59_PATH)
C73B = load_module("c73b_torsion_family", C73B_PATH)
E, spin, T2_M = S2A.E, S2A.spin_lift_np, S2A.T2_M
LAM = {i: S2A.NOMIZU_LC[i].astype(complex) for i in range(1, 7)}
I6, I8 = np.eye(6), np.eye(8)
n_pairs = len(C73B.PAIRS)

# --- corrected sector, with the adjudicator re-run as a gate -----------------
GENS = [np.kron(spin(T2_M[k]), I6) + np.kron(I8, -T2_M[k]) for k in range(2)]
D_LC = sum(np.kron(E[i] @ spin(LAM[i]), I6) + np.kron(E[i], -LAM[i]) for i in range(1, 7))
eq = max(float(np.max(np.abs(D_LC @ G - G @ D_LC))) for G in GENS)
print(f"GATE  equivariance of D for the corrected generator: max|[D,G]| = {eq:.3e}")
assert eq < 1e-10, "corrected generator is not the equivariant one -- STOP"


def sector(first_idx):
    bi = [i * 6 + j for i in first_idx for j in range(6)]
    proj = np.zeros((48, len(bi)))
    for col, g in enumerate(bi):
        proj[g, col] = 1
    _, s, vt = np.linalg.svd(np.vstack([proj.T @ g @ proj for g in GENS]))
    pad = np.concatenate([s, np.zeros(len(bi) - len(s))])
    return proj @ vt.conj().T[:, np.abs(pad) < 1e-8]


dom, tgt = sector(R59.ODD_IDX), sector(R59.EVEN_IDX)
print(f"GATE  corrected sector dims: ({dom.shape[1]}, {tgt.shape[1]})")
assert dom.shape[1] == 3 and tgt.shape[1] == 3


def row_to_6x6(row):
    M = np.zeros((6, 6), dtype=complex)
    for idx, (a, b) in enumerate(C73B.PAIRS):
        M[a, b] += row[idx]
        M[b, a] -= row[idx]
    return M


def c_of(vec):
    T = vec.reshape(6, n_pairs)
    lam = {i + 1: row_to_6x6(T[i]) for i in range(6)}
    D = sum(np.kron(E[i] @ spin(lam[i]), I6) + np.kron(E[i], -lam[i]) for i in range(1, 7))
    return tgt.conj().T @ D @ dom


J = np.zeros((6, 6))
for k in range(3):
    J[2 * k, 2 * k + 1], J[2 * k + 1, 2 * k] = -1, 1


def apply_J(vec):
    return (J.T @ vec.reshape(6, n_pairs)).reshape(-1)


family = C73B.equivariant_torsion_basis(T2_M)
assert family.shape[1] == 6, f"family dim drifted: {family.shape[1]}"

# --- VACUITY GATE, FIRST AND DOMINANT ----------------------------------------
print()
print("=" * 78)
print("VACUITY GATE (first and dominant -- C151's own lesson)")
print("=" * 78)
vals = [c_of(family[:, k]) for k in range(6)]
mags = [float(np.max(np.abs(v))) for v in vals]
print(f"  max|c| on the 6 family basis vectors: {[f'{m:.4f}' for m in mags]}")
nonvacuous = all(m > 1e-8 for m in mags)
print(f"  every basis vector gives a NONZERO c : {nonvacuous}")
if not nonvacuous:
    print()
    print("  *** VACUOUS -- NOT A CONFIRMATION. STOP. ***")
    raise SystemExit(0)

# --- the frozen prediction, as matrices, entry by entry ----------------------
print()
print("=" * 78)
print("THE FROZEN PREDICTION:  c(J.nabla) = +- i . c(nabla)   (as MATRICES)")
print("=" * 78)
rng = np.random.default_rng(152)
ok, ratios = [], []
for trial in range(8):
    v = family @ (rng.normal(size=6) if trial else np.ones(6))
    cv, cJ = c_of(v), c_of(apply_J(v))
    if np.max(np.abs(cv)) < 1e-8:
        continue
    for sgn in (1j, -1j):
        dev = float(np.max(np.abs(cJ - sgn * cv))) / float(np.max(np.abs(cv)))
        if dev < 1e-8:
            ok.append((trial, sgn))
            break
    else:
        dev_p = float(np.max(np.abs(cJ - 1j * cv))) / float(np.max(np.abs(cv)))
        dev_m = float(np.max(np.abs(cJ + 1j * cv))) / float(np.max(np.abs(cv)))
        ok.append((trial, None))
        ratios.append((dev_p, dev_m))
    print(f"  draw {trial}: max|c| = {np.max(np.abs(cv)):.4f}  max|c(Jv)| = "
          f"{np.max(np.abs(cJ)):.4f}  "
          f"{'C-LINEAR ('+('+i' if ok[-1][1]==1j else '-i')+')' if ok[-1][1] else 'NOT C-linear'}")

print()
print("=" * 78)
print("VERDICT ON C151's PRE-REGISTERED QUESTION")
print("=" * 78)
signs = {s for _, s in ok if s is not None}
if len(ok) and all(s is not None for _, s in ok) and len(signs) == 1:
    s = "+i" if 1j in signs else "-i"
    print(f"  CONFIRMED on the corrected sector: c(J.nabla) = {s} . c(nabla),")
    print("  exactly, as matrices, on every draw. The C-linearity found on S^6")
    print("  (C147) is therefore NOT a G2/SU(3) accident -- it recurs on the only")
    print("  independent homogeneous nearly-Kahler test space available.")
elif all(s is None for _, s in ok):
    print("  FALSIFIED on the corrected sector: c is NOT C-linear w.r.t. J here.")
    print("  Per the pre-registration this is equally informative -- it localises")
    print("  C147's structure to G2/SU(3).")
    for dp, dm in ratios[:3]:
        print(f"    relative deviation from +i: {dp:.4f}   from -i: {dm:.4f}")
else:
    print("  MIXED -- read the per-draw lines; do not summarise.")
