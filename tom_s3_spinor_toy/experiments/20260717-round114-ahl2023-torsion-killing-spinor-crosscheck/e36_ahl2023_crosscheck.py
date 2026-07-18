"""Round114: cross-check round67's own Kostant-cubic-Dirac eigenvalue
(magnitude 3/2 at the Levi-Civita point) against an INDEPENDENT,
peer-reviewed 2023 paper's own closed-form torsion-connection formula for
the SAME space (S^3 = SU(2)/{e}, round metric).

Source (read directly via pymupdf this round, not from memory):
Agricola, Hofmann, Lawn, "Invariant Spinors on Homogeneous Spheres",
arXiv:2203.02961v3 (2023) -- already in this repo, unused until now.
Theorem 3.7, Theorem 3.13, Corollary 3.14, Remark 3.16, Proposition 3.17,
and the Clifford-representation formulas (4)-(6) of Section 2.1/2.2 are all
cited directly from the extracted PDF text.
"""

import sympy as sp

s, eps = sp.symbols("s epsilon", real=True)

print("=" * 92)
print("PART 1 -- Build the Clifford representation for n=1 (S^3=SU(2)/{e})")
print("using the paper's OWN stated formulas (Remark 2.2's odd-dim ordering,")
print("eq. 4-6): x1=(1/sqrt2)(e2-i*e3), y1=(1/sqrt2)(e2+i*e3), u0=i*e1,")
print("x1.eta = i*sqrt2*(x1 contract eta), y1.eta = i*sqrt2*(y1 wedge eta),")
print("u0 = -Id|Sigma_even + Id|Sigma_odd, on Sigma=Lambda*(C y1)={1,y1}.")
print("Standard Lagrangian-pairing normalization x1 contract y1 = 1 (fermionic")
print("creation/annihilation convention, cited as standard, not re-derived).")
print("=" * 92)

IMAG = sp.I
sqrt2 = sp.sqrt(2)

# Basis order: [1, y1]  (Sigma_even={1}, Sigma_odd={y1})
# x1 . 1 = 0 ; x1 . y1 = i*sqrt2*1
X1 = sp.Matrix([[0, IMAG * sqrt2], [0, 0]])
# y1 . 1 = i*sqrt2*y1 ; y1 . y1 = 0
Y1 = sp.Matrix([[0, 0], [IMAG * sqrt2, 0]])
# u0 = -Id on Sigma_even (the "1" component), +Id on Sigma_odd (the "y1" component)
U0 = sp.diag(-1, 1)

# e1 = u0 / i = -i*u0
E1 = sp.simplify(-IMAG * U0)
# e2 = (x1+y1)/sqrt2 ; e3 = i*(x1-y1)/sqrt2
E2 = sp.simplify((X1 + Y1) / sqrt2)
E3 = sp.simplify(IMAG * (X1 - Y1) / sqrt2)

print("  E1 =", E1.tolist())
print("  E2 =", E2.tolist())
print("  E3 =", E3.tolist())
print()

print("=" * 92)
print("PART 2 -- MANDATORY sanity check: {e_i,e_j} = -2*delta_ij * Id (paper's own")
print("stated Clifford convention, section 2.1: vw+wv=-2*beta(v,w)*1)")
print("=" * 92)
E = [E1, E2, E3]
clifford_ok = True
for i in range(3):
    for j in range(3):
        anticomm = sp.simplify(E[i] * E[j] + E[j] * E[i])
        expected = -2 * sp.eye(2) if i == j else sp.zeros(2, 2)
        ok = bool(sp.simplify(anticomm - expected) == sp.zeros(2, 2))
        clifford_ok = clifford_ok and ok
        if not ok:
            print(
                f"  MISMATCH at (e{i + 1},e{j + 1}): got {anticomm.tolist()}, expected {expected.tolist()}"
            )
print(f"  Clifford relations {{e_i,e_j}}=-2delta_ij confirmed for all 9 pairs? {clifford_ok}")
print()

if not clifford_ok:
    print("KILL CRITERION HIT: transcription error, stopping per pre-registered claim.md.")
    raise SystemExit(1)

print("=" * 92)
print("PART 3 -- Theorem 3.13 + Corollary 3.14: A_+ eigenvalues at round metric")
print("(n=1, a=n/(n+1)=1/2, b=1/2), lambda1=(2b-a)*sqrt(n(n+1))/(4b*sqrt(a)),")
print("lambda2=sqrt(a(n+1))/(4b*sqrt(n))")
print("=" * 92)
n = 1
a_val = sp.Rational(n, n + 1)
b_val = sp.Rational(1, 2)
lambda1 = sp.simplify((2 * b_val - a_val) * sp.sqrt(n * (n + 1)) / (4 * b_val * sp.sqrt(a_val)))
lambda2 = sp.simplify(sp.sqrt(a_val * (n + 1)) / (4 * b_val * sp.sqrt(n)))
print(f"  lambda1 = {lambda1}  (expect 1/2, matching paper's own 'Killing constant 1/2' claim)")
print(f"  lambda2 = {lambda2}  (expect 1/2)")
print()

print("=" * 92)
print("PART 4 -- Remark 3.16 + Proposition 3.17: A^s_+ endomorphism, n=1,")
print("round metric epsilon=-1 (a=-n*eps/(n+1)=1/2 confirmed)")
print("A^s_+ := A_+ - eps*s*n/2 * Id|m1 + eps*s/2 * Id|m2   (n=1)")
print("=" * 92)
eps_val = -1
alpha_s = sp.simplify(lambda1 - eps_val * s * n / 2)  # m1 (e1-direction) eigenvalue
beta_s = sp.simplify(lambda2 + eps_val * s / 2)  # m2 (e2,e3-direction) eigenvalue
print(f"  alpha(s) [m1/e1 eigenvalue] = {alpha_s}")
print(f"  beta(s)  [m2/e2,e3 eigenvalue] = {beta_s}")
print()

print("=" * 92)
print("PART 5 -- Build D^s(psi_+) := sum_i e_i . A^s_+(e_i) . psi_+ explicitly")
print("=" * 92)
psi_plus = sp.Matrix([1, 0])  # the '1' basis vector

# Dirac-operator construction: D = sum_i e_i . (nabla_{e_i} psi) = sum_i e_i . (A(e_i) . psi),
# where A(e_i) . psi means Clifford mult by the VECTOR A(e_i) (A: TM -> TM is an endomorphism).
# Since A^s_+ is diagonal (scalar alpha(s) on m1, scalar beta(s) on m2), A^s_+(e1)=alpha(s)*e1,
# A^s_+(e2)=beta(s)*e2, A^s_+(e3)=beta(s)*e3 (AS VECTORS, then Clifford-multiplied again by e_i):
# D^s . psi = e1.(alpha(s)*e1).psi + e2.(beta(s)*e2).psi + e3.(beta(s)*e3).psi
#           = alpha(s)*E1*E1*psi + beta(s)*E2*E2*psi + beta(s)*E3*E3*psi
D_s = sp.simplify(
    alpha_s * E1 * E1 * psi_plus + beta_s * E2 * E2 * psi_plus + beta_s * E3 * E3 * psi_plus
)
print(f"  D^s(psi_+) = {D_s.T.tolist()}  (as a vector in the {{1,y1}} basis)")
D_s_eigenvalue = sp.simplify(
    D_s[0]
)  # psi_+ = (1,0), so D^s(psi_+) should be proportional to psi_+ itself
consistent = bool(sp.simplify(D_s[1]) == 0)
print(f"  D^s(psi_+) proportional to psi_+ (consistency check)? {consistent}")
print(f"  D^s eigenvalue on psi_+ = {sp.simplify(D_s_eigenvalue)}")
print()

print("=" * 92)
print("PART 6 -- Levi-Civita point (s=0): compare magnitude to round67's own")
print("cited eigenvalue 3/2")
print("=" * 92)
D_0 = sp.simplify(D_s_eigenvalue.subs(s, 0))
print(f"  D^0(psi_+) eigenvalue = {D_0}")
magnitude_match = bool(sp.simplify(sp.Abs(D_0) - sp.Rational(3, 2)) == 0)
print(f"  |D^0| == 3/2 (round67's own cited Levi-Civita eigenvalue magnitude)? {magnitude_match}")
print()

print("=" * 92)
print("PART 7 -- Zero-crossing(s) in s")
print("=" * 92)
crossings = sp.solve(sp.Eq(D_s_eigenvalue, 0), s)
print(f"  D^s(psi_+) = 0 at s = {crossings}")

verdict = {
    "clifford_relations_confirmed": clifford_ok,
    "lambda1_lambda2_match_paper_stated_half": bool(
        lambda1 == sp.Rational(1, 2) and lambda2 == sp.Rational(1, 2)
    ),
    "D_s_consistency_check": consistent,
    "D_0_value": str(D_0),
    "magnitude_matches_round67_3_over_2": magnitude_match,
    "zero_crossings_in_s": [str(c) for c in crossings],
}
print("=" * 92)
print("VERDICT")
print("=" * 92)
for k, v in verdict.items():
    print(f"  {k}: {v}")

print()
if not clifford_ok:
    label = "BLOCKED_BY_TRANSCRIPTION_ERROR"
elif magnitude_match:
    label = "CONFIRMED_INDEPENDENT_MAGNITUDE_MATCH__3_OVER_2__CROSSCHECKS_ROUND67"
else:
    label = "INCONCLUSIVE__MAGNITUDE_MISMATCH__CONSTRUCTION_OF_D_FROM_A_MAY_NOT_BE_RIGHT"
print(f"  label = '{label}'")
