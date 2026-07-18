"""Round115: checks whether identifying the S3 torsion T^t with a genuine
NS-NS-type flux (subject to standard Dirac-type quantization) can select
t=0,1 without circularity -- i.e. without simply DEFINING the flux quantum
unit to be whatever makes t=0,1 come out, the exact trap round67's own
decision.md already self-flagged.

Key already-established facts used (cited, not re-derived):
  - Hodge corollary (lambda-dim-gate/decision.md): H^3(S3xS6)=R, entirely
    from the S3 factor -- a genuine quantized-flux-carrying cycle exists.
  - rho_3 is an UNSTABILIZED free modulus in this project (preprint.tex
    line 1008: "Dine-Seiberg runaway in the rho_3 direction" -- the
    established moduli potential's minimization condition dV/drho_6=0 does
    not involve rho_3 at all).
  - Standard, textbook fact (not project-specific, not re-derived from an
    external source): Vol(S^3 of radius rho) = 2*pi^2*rho^3.
"""

import sympy as sp

rho3, c, Q, n, t = sp.symbols("rho3 c Q n t", positive=True, real=True)
rho3_sym = sp.symbols("rho3", real=True)

print("=" * 92)
print("PART 1 -- Vol(S^3_rho) = 2*pi^2*rho^3, verified by direct integration")
print("(standard round-3-sphere volume formula; not a project-specific claim)")
print("=" * 92)
theta1, theta2, theta3 = sp.symbols("theta1 theta2 theta3", real=True)
# S^3 of radius rho embedded via standard hyperspherical angles; volume element
# rho^3 * sin(theta1)^2 * sin(theta2), theta1 in [0,pi], theta2 in [0,pi], theta3 in [0,2pi]
integrand = rho3**3 * sp.sin(theta1) ** 2 * sp.sin(theta2)
vol = sp.integrate(
    sp.integrate(sp.integrate(integrand, (theta3, 0, 2 * sp.pi)), (theta2, 0, sp.pi)),
    (theta1, 0, sp.pi),
)
vol = sp.simplify(vol)
print(f"  Vol(S^3_rho3) [direct integration] = {vol}")
expected = 2 * sp.pi**2 * rho3**3
matches = bool(sp.simplify(vol - expected) == 0)
print(f"  Matches standard formula 2*pi^2*rho3^3? {matches}")
print()

print("=" * 92)
print("PART 2 -- Schematic flux-quantization condition, IF torsion=flux")
print("(2t-1)*c*Vol(S3_rho3) = 2*pi*n*Q_unit  [n integer, Q_unit some fixed physical scale]")
print("=" * 92)
quantization_eq = sp.Eq((2 * t - 1) * c * vol, 2 * sp.pi * n * Q)
print(f"  {quantization_eq}")
t_solution = sp.solve(quantization_eq, t)[0]
print(f"  Solved for t: t(n, rho3) = {sp.simplify(t_solution)}")
print()

print("=" * 92)
print("PART 3 -- THE CIRCULARITY TEST: does this select t=0,1 specifically,")
print("or does ANY target t-value work equally well for SOME (n, rho3) pair?")
print("=" * 92)
# For t=0 (n fixed, say n=-1, WLOG): what rho3 is required?
target_ts = [sp.Integer(0), sp.Integer(1), sp.Rational(1, 3), sp.Integer(7)]
n_val = sp.Integer(1)  # WLOG try n=1 for each target t
c_val = sp.Symbol("c", positive=True)  # keep symbolic, no specific number assumed
Q_val = sp.Symbol("Q", positive=True)
print("  For each target t, pick n=sign(2t-1) (just a sign choice so the cube root")
print("  is real and positive -- the SAME freedom is available for ANY target t,")
print("  which is exactly the point) and solve for the rho3 that satisfies it:")
for tt in target_ts:
    n_signed = sp.sign(2 * tt - 1) if tt != sp.Rational(1, 2) else sp.Integer(1)
    eq_t = sp.Eq((2 * tt - 1) * c_val * (2 * sp.pi**2 * rho3_sym**3), 2 * sp.pi * n_signed * Q_val)
    sol = sp.solve(eq_t, rho3_sym)
    real_positive = [s for s in sol if sp.simplify(s).is_real and sp.simplify(s) > 0] if sol else []
    print(
        f"    t={tt} (n={n_signed}): rho3 = {sol} -> real positive root exists: {bool(real_positive)}"
    )

print()
print("  Interpretation: a REAL, positive rho3 solving the quantization condition")
print("  exists for t=0, t=1, AND for t=1/3 and t=7 (any nonzero t != 1/2) --")
print("  the mechanism does not distinguish t=0,1 from any other value UNLESS")
print("  rho3 is independently fixed FIRST by some other, separate principle.")
print("  Since rho3 is an established UNSTABILIZED free modulus in this project")
print("  (preprint.tex:1008, Dine-Seiberg runaway), no such independent fixing")
print("  exists yet -- selecting t=0,1 this way would require CHOOSING rho3")
print("  after the fact to match, exactly the circularity round67 self-flagged.")
print()

print("=" * 92)
print("PART 4 -- Skeptic-requested numerical check: plug in G94's own CANDIDATE")
print("rho3 value (NOT a fully free modulus after all -- a candidate stabilization")
print("mechanism exists, experiments/20260626-g94-s3-np-instanton/decision.md,")
print("rho3=1.9281, itself CONDITIONAL on an admitted free coupling c_S3=0.235,")
print("'does NOT prove c_S3=0.235 is the physical value', per that file's own line 76)")
print("=" * 92)
c_structure_const = 2  # |<[Z1,Z2]_m,Z3>| in the Z_i=i*sigma_i, <X,Y>=-1/2 Tr(XY) frame
# (verified: [Z1,Z2]=-2i*sigma3=-2*Z3/i... direct check below)
Z1 = sp.I * sp.Matrix([[0, 1], [1, 0]])
Z2 = sp.I * sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z3 = sp.I * sp.Matrix([[1, 0], [0, -1]])
bracket_12 = sp.expand(Z1 * Z2 - Z2 * Z1)


def inner(X, Y):
    return sp.simplify(-sp.Rational(1, 2) * sp.trace(X * Y))


c_computed = inner(bracket_12, Z3)
print(f"  c := <[Z1,Z2],Z3> [directly recomputed, same frame as round99/111/113] = {c_computed}")

rho3_G94 = sp.Rational(19281, 10000)  # G94's own cited value, rho3=1.9281
Q_natural = (2 * sp.pi) ** 2  # standard NS-NS quantization unit, alpha'=1 natural units
# [WEAK -- this specific normalization is a standard convention from memory, NOT
# independently tool-verified against a cited primary source for THIS construction]
K_val = sp.simplify(sp.Abs(c_computed) * sp.pi * rho3_G94**3 / Q_natural)
K_float = float(K_val)
print(f"  K = |c|*pi*rho3_G94^3 / Q_natural = {K_val} = {K_float:.4f}")
print(
    f"  Distance from nearest integer (1): {abs(K_float - 1):.4f} ({abs(K_float - 1) * 100:.1f}%)"
)
print()
print("  Interpretation: K~1.14 is SUGGESTIVELY close to 1 but NOT an exact match,")
print("  and rests on THREE stacked, independently-unverified inputs: (a) the")
print("  torsion=flux identification itself (this round's own tested hypothesis),")
print("  (b) the specific Q=(2pi)^2*alpha' normalization (recalled, not tool-verified")
print("  for this construction), (c) G94's own rho3=1.9281, which is ITSELF")
print("  conditional on an admittedly free coupling c_S3 (G94 decision.md line 76:")
print("  'Does NOT prove c_S3=0.235 is the physical value -- this is a free coupling').")
print("  A near-miss built on three stacked unverified/free inputs is NOT confirmation;")
print("  tuning any ONE of the three could move K to exactly 1 or away from it just")
print("  as easily -- this is the numerological-coincidence risk, not evidence.")
print()

verdict = {
    "vol_S3_formula_confirmed": matches,
    "quantization_condition_solvable_for_t_given_rho3": True,
    "rho3_has_a_CANDIDATE_value_G94_not_fully_free__but_that_value_is_itself_coupling_conditional": True,
    "K_at_G94_candidate_rho3": str(K_val),
    "K_close_to_integer_1_but_not_exact__rests_on_3_stacked_unverified_inputs": True,
    "mechanism_gives_genuine_nonvacuous_conditional_t_rho3_correlation": True,
    "mechanism_does_NOT_yet_independently_select_t_0_1": True,
}
print("=" * 92)
print("VERDICT")
print("=" * 92)
for k, v in verdict.items():
    print(f"  {k}: {v}")

print()
label = "NULL_FOR_UNCONDITIONAL_SELECTION__GENUINE_CONDITIONAL_(T,RHO3)_CORRELATION__SUGGESTIVE_NOT_CONFIRMED_NEAR_INTEGER"
print(f"  label = '{label}'")
