r"""
C151 STAGE 1b -- invariant-sector dimensions for SU(3)/T^2. Still BEFORE c.

The restatement frozen in PREREGISTRATION.md (criterion #4) pre-committed:
"the invariant-sector dimensions must be reported BEFORE c, in the same way
this restatement reports the family dimension before c." This script does
exactly that and nothing else.

METHOD -- exact integer weight arithmetic, no floating point anywhere.
  Under the T^2 Cartan (H1 = i*diag(1,-1,0), H2 = i*diag(0,1,-1)) the three
  positive-root planes of m carry weights
        r1 (m_12) = (2,-1)      r2 (m_13) = (1,1)      r3 (m_23) = (-1,2)
  and m (x) C has weights {+-r1, +-r2, +-r3}.

  J_NK, pinned in Stage 1a by the Nijenhuis computation (eps = (-1,1,-1)),
  selects the (1,0) space V: plane k contributes weight eps_k * r_k.
  Per CH2016 Sec.2 (the source round65 used for SU(3)/T^2, and which builds
  the spinor/SU(3)-structure machinery from an ABSTRACT Killing spinor with
  no reference to a specific isotropy group) the spinor module is

        Sigma  =  Lambda^0 V  (+)  Lambda^1 V  (+)  Lambda^2 V  (+)  Lambda^3 V

  with the even/odd split Sigma_even = Lambda^0 (+) Lambda^2,
  Sigma_odd = Lambda^1 (+) Lambda^3 -- the same shape as S^6's Sigma.

  The twist is W = m (x) C, matching C139/C147's own choice on S^6, so the
  sectors to measure are (Sigma_odd (x) W)^{T^2} and (Sigma_even (x) W)^{T^2}.
  A tensor-product weight vector is invariant iff its total weight is zero.

WHY THIS IS SAFE TO REPORT BEFORE c
  Nothing here touches the connection, the Dirac operator, or c. It counts
  weight-zero vectors in a tensor product -- pure representation theory,
  fixed entirely by J_NK (already pinned) and the root system.

Run:  python c151_stage1b_sectors.py
"""

from itertools import combinations

Weight = tuple[int, int]

# positive roots of su(3) in the (H1,H2) basis
R1: Weight = (2, -1)  # m_12
R2: Weight = (1, 1)  # m_13
R3: Weight = (-1, 2)  # m_23
ROOTS = [R1, R2, R3]

EPS_NK = (-1, 1, -1)  # pinned in Stage 1a by the Nijenhuis computation


def add(*ws: Weight) -> Weight:
    return (sum(w[0] for w in ws), sum(w[1] for w in ws))


def neg(w: Weight) -> Weight:
    return (-w[0], -w[1])


# ---------------------------------------------------------------------------
# V = the (1,0) space selected by J_NK
# ---------------------------------------------------------------------------
V = [r if e > 0 else neg(r) for e, r in zip(EPS_NK, ROOTS)]
print("STAGE 1b -- invariant-sector dimensions for SU(3)/T^2 (before c)")
print()
print(f"  positive roots (H1,H2)      : r1={R1}  r2={R2}  r3={R3}")
print(f"  J_NK sign tuple (Stage 1a)  : {EPS_NK}")
print(f"  V = (1,0) space weights     : {V}")

# ---------------------------------------------------------------------------
# Sigma = Lambda^bullet V, with its even/odd split
# ---------------------------------------------------------------------------
LAM: dict[int, list[Weight]] = {
    0: [(0, 0)],
    1: list(V),
    2: [add(V[i], V[j]) for i, j in combinations(range(3), 2)],
    3: [add(*V)],
}
SIGMA_EVEN = LAM[0] + LAM[2]
SIGMA_ODD = LAM[1] + LAM[3]

print()
print("  Sigma = Lambda^bullet V :")
for k in range(4):
    print(f"    Lambda^{k} weights = {LAM[k]}")
print(f"    Sigma_even (Lam^0+Lam^2) = {SIGMA_EVEN}")
print(f"    Sigma_odd  (Lam^1+Lam^3) = {SIGMA_ODD}")
assert len(SIGMA_EVEN) == 4 and len(SIGMA_ODD) == 4, "Sigma must split 4+4"

sigma_invariants = [w for w in SIGMA_EVEN + SIGMA_ODD if w == (0, 0)]
print(f"    T^2-invariants inside Sigma itself: {len(sigma_invariants)}  (S^6 had 2)")

# ---------------------------------------------------------------------------
# W = m (x) C  -- the twist, matching C139/C147's own choice
# ---------------------------------------------------------------------------
W = [r for r in ROOTS] + [neg(r) for r in ROOTS]
print()
print(f"  W = m (x) C weights         : {W}")
print(
    f"    T^2-invariants inside W itself: {sum(1 for w in W if w == (0, 0))}  (m has no zero weight)"
)


def invariant_count(sector: list[Weight], twist: list[Weight]) -> int:
    """dim (sector (x) twist)^{T^2} = number of weight-cancelling pairs."""
    return sum(1 for s in sector for t in twist if add(s, t) == (0, 0))


dom = invariant_count(SIGMA_ODD, W)
tgt = invariant_count(SIGMA_EVEN, W)

print()
print("=" * 78)
print("INVARIANT SECTORS  (the criterion-#4 numbers, reported before c)")
print("=" * 78)
print(f"  domain  dim (Sigma_odd  (x) W)^T2 = {dom}")
print(f"  target  dim (Sigma_even (x) W)^T2 = {tgt}")
print()
print("  For comparison, S^6 = G2/SU(3) with the SAME twist W = m (C139,")
print("  certified): domain = 1, target = 1 -- so there c was a single SCALAR.")

print()
print("=" * 78)
print("CONSEQUENCE FOR THE FROZEN RESTATEMENT")
print("=" * 78)
if dom == 1 and tgt == 1:
    print("  Sectors are 1-dimensional here too: c is a SCALAR, and the S^6")
    print("  formulation transfers with only the family dimension changed.")
else:
    print(f"  Sectors are ({dom},{tgt}), NOT (1,1). So c is MATRIX-VALUED here,")
    print("  exactly as restatement consequence #1 pre-committed. The prediction")
    print("  c(J.nabla) = +-i c(nabla) is therefore to be tested AS MATRICES,")
    print("  entry-by-entry -- and explicitly NOT weakened to a statement about")
    print("  norms or singular values, per that same pre-commitment.")
print()
print("  c HAS STILL NOT BEEN COMPUTED. Stages 0, 1a and 1b are all")
print("  structure-only; every number above is fixed by the root system and")
print("  by J_NK, which was itself pinned by an objective computation.")
