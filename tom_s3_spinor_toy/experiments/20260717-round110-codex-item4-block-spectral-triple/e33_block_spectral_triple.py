"""E33 (round110): build and test the block spectral triple
D_block = diag(D^0, D^1) on H_block = C^2 (+) C^2, per Codex/round105's
item 4. Reuses E9/round73's own H=(3c/2)*omega (scalar, established) and
round106's D^t(psi)=t*H*psi for constant psi.
"""

import sympy as sp

I2 = sp.eye(2)
c = sp.symbols("c", positive=True)  # structure constant, established nonzero (c=2 calibrated, E2)


def pauli_matrices():
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    return [sx, sy, sz]


def clifford_generators():
    return [sp.I * s for s in pauli_matrices()]


print("=" * 92)
print("PART 0 -- Reused: H = (3c/2)*omega, omega = Z1*Z2*Z3 (E2/E9, re-verified)")
print("=" * 92)
Z = clifford_generators()
omega = sp.simplify(Z[0] * Z[1] * Z[2])
H = sp.simplify(sp.Rational(3, 2) * c * omega)
H_is_scalar = sp.simplify(H - H[0, 0] * I2) == sp.zeros(2, 2)
print(f"  omega = {omega.tolist()}")
print(f"  H = (3c/2)*omega = {H.tolist()}  (scalar multiple of I2? {H_is_scalar})")
print()

print("=" * 92)
print("PART 1 -- Explicit D_block = diag(D^0, D^1) on H_block = C^2 (+) C^2")
print("=" * 92)
D0 = 0 * H  # D^t(psi) = t*H*psi, t=0
D1 = 1 * H  # t=1
D_block = sp.diag(D0, D1)  # 4x4, block-diagonal
print(f"  D^0 = 0*H = {D0.tolist()}")
print(f"  D^1 = 1*H = {H.tolist()}")
print("  D_block (4x4) =")
sp.pprint(D_block)
print()

print("=" * 92)
print("PART 2 -- Basic finite-dim spectral-triple properties (Codex checklist)")
print("=" * 92)
D_block_selfadjoint = sp.simplify(D_block.H - D_block) == sp.zeros(4, 4)
print(f"  D_block self-adjoint (D^dagger = D)? {D_block_selfadjoint}")
print("  Bounded (finite matrix, always bounded operator)? True (trivial for finite dim)")
print("  Compact resolvent (finite matrix has discrete, finite spectrum)? True (trivial)")
eigenvals = D_block.eigenvals()
print(f"  Spectrum of D_block: {eigenvals}")
print()

print("=" * 92)
print("PART 3 -- Codex's own explicit question: does a symmetry S exchange the two")
print("BLOCKS AS A PAIR (S*D_block*S^-1 = D_block, with S permuting the two C^2")
print("summands) -- the CORRECT formulation (per skeptic review; conjugating D^0 into")
print("D^1 directly is a trivial/wrong sub-question, since D^0=0 and T*0*T^-1=0 for")
print("ANY invertible T, unitary or not -- not informative about block-EXCHANGE at all).")
print("=" * 92)
S = sp.Matrix.zeros(4, 4)
S[0:2, 2:4] = I2
S[2:4, 0:2] = I2  # the block-swap unitary: S(v1,v2) = (v2,v1)
S_is_unitary = sp.simplify(S.H * S - sp.eye(4)) == sp.zeros(4, 4)
D_block_conjugated = sp.simplify(S * D_block * S.H)
swap_is_symmetry = sp.simplify(D_block_conjugated - D_block) == sp.zeros(4, 4)
print(f"  S (block-swap operator) is unitary? {S_is_unitary}")
print("  S*D_block*S^-1 =")
sp.pprint(D_block_conjugated)
print(f"  S*D_block*S^-1 == D_block (i.e. is S a genuine symmetry of D_block)? {swap_is_symmetry}")
print("  NO -- the block-swap S conjugates D_block into diag((3c/2)I2, 0), the two")
print("  diagonal blocks EXCHANGED but not equal to the original (since D^0=0 !=")
print("  D^1=(3c/2)I2) -- confirming no block-exchange symmetry exists, via the")
print("  CORRECT formulation of the question this time.")
print()
print("  Honest calibration note: this conclusion rests on the SAME two established")
print("  inputs round106 already used (H is scalar; D^0=0 at t=0, D^1=(3c/2)I2 at t=1)")
print("  -- restated here in explicit block-spectral-triple/NCG language, per Codex's")
print("  own item-4 checklist, rather than supplying independent NEW evidence beyond")
print("  round106. Presentational/organizational value (answers Codex's specific")
print("  checklist item directly and correctly), not a fresh independent confirmation.")
print()

print("=" * 92)
print("PART 4 -- Minimal diagonal algebra A=C(+)C acting on H_block: does it commute")
print("with D_block? (informative negative -- shows the 'natural' minimal choice is")
print("dynamically inert, motivating why any interesting NCG content needs a LARGER,")
print("off-diagonal-capable algebra -- not constructed here, honestly left open)")
print("=" * 92)
lam0, lam1 = sp.symbols("lambda0 lambda1")
a_diag = sp.diag(lam0 * I2, lam1 * I2)  # generic element of A = C (+) C, acting scalar per block
comm = sp.simplify(D_block * a_diag - a_diag * D_block)
comm_is_zero = comm == sp.zeros(4, 4)
print(f"  [D_block, a] for generic diagonal a in A=C(+)C: commutator zero? {comm_is_zero}")
print("  (Both D_block and a are block-diagonal in the SAME 2+2 splitting -- trivially")
print("  commute. This is expected and not a new finding: it shows the minimal, most")
print("  natural algebra choice carries NO dynamical content in this construction; any")
print("  physically interesting first-order-condition/off-diagonal structure requires")
print("  a DIFFERENT, richer choice of A or an explicit D_F-type coupling term, neither")
print("  of which this project has specified -- honestly flagged as open, not invented")
print("  speculatively here.)")
print()

verdict = {
    "H_is_scalar_confirmed": bool(H_is_scalar),
    "D_block_self_adjoint": bool(D_block_selfadjoint),
    "bounded_and_compact_resolvent_trivial_finite_dim": True,
    "S_block_swap_is_unitary": bool(S_is_unitary),
    "block_swap_is_symmetry_of_D_block": bool(swap_is_symmetry),
    "minimal_diagonal_algebra_commutes_trivially": bool(comm_is_zero),
}
print("=" * 92)
print("VERDICT")
print("=" * 92)
for k, v in verdict.items():
    print(f"  {k}: {v}")
label = "BLOCK_CONSTRUCTION_WELL_DEFINED__NO_BLOCK_EXCHANGE_SYMMETRY__ALGEBRA_AND_OFFDIAGONAL_QUESTIONS_HONESTLY_OPEN"
print(f"  label = '{label}'")
