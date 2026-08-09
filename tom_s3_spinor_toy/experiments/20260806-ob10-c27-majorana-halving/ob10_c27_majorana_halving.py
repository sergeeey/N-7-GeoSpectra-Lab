"""Does OB10's pseudo-real verdict CLOSE the Majorana branch of C27's
Relaxation Map?

C27/round78 established: dim ker(D_{S3,t=0}) = 2 (complex), giving 2 internal
zero modes per triality channel, 6 total instead of the needed 3. Its
Relaxation Map lists three escape routes; one is "a new reality/Majorana
condition" -- round78 only established that NONE IS CURRENTLY IMPOSED (an
absence statement, `preprint.tex` grep found nothing). It did NOT establish
whether one COULD be imposed.

OB10 (2026-08-03) established the geometric S3xS6 Clifford module is
PSEUDO-REAL: a unique factorized charge conjugation B = s2(x)s2(x)s1(x)s2 with
B*conj(B) = -I16.

This script asks the sharper question: does that pseudo-reality make the
Majorana halving IMPOSSIBLE (a positive no-go), rather than merely absent?

Structure of the argument to be tested:
  1. B factorizes as B_S3 (x) B_S6 -- the first Kronecker slot is exactly the
     2-dim S3 spinor factor (per OB10's own construction, E=[kron(Z_j,Gamma7)],
     F=[kron(I2,G6_i)]).
  2. If B_S3 * conj(B_S3) = -I2, the Majorana condition psi = B_S3 psi* has
     ONLY psi=0 -- checked here by explicit generic solve, not just the
     abstract two-line argument.
  3. The C27 excess lives ENTIRELY in the S3 factor (dim ker(D_S3)=2 vs
     dim ker(D_S6)=1 per channel), i.e. the same factor the pseudo-reality
     comes from -- so the no-go bites exactly where the problem is.
  4. NEGATIVE CONTROL (mandatory, per this project's Gate 3 discipline): the
     same solve on a genuinely REAL structure must FIND nonzero solutions.
     A test that cannot distinguish real from pseudo-real is not a test.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp
from sympy import I, Matrix, eye, simplify, symbols, zeros
from sympy import kronecker_product as kron

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_ob10_c27.json"

s1 = Matrix([[0, 1], [1, 0]])
s2 = Matrix([[0, -I], [I, 0]])
s3 = Matrix([[1, 0], [0, -1]])
I2 = eye(2)


def is_zero(m):
    return simplify(m) == zeros(*m.shape)


def majorana_solutions(B):
    """Solve psi = B*conj(psi) for a GENERIC complex vector psi, symbolically.

    Returns (n_free_real_params, solution_dict). n=0 means only psi=0.
    Splits into real+imaginary parts so `conjugate` is handled honestly rather
    than by sympy's symbolic conjugate() on unconstrained symbols.
    """
    n = B.shape[0]
    re = symbols(f"a0:{n}", real=True)
    im = symbols(f"b0:{n}", real=True)
    psi = Matrix([re[k] + I * im[k] for k in range(n)])
    psi_conj = Matrix([re[k] - I * im[k] for k in range(n)])
    residual = simplify(psi - B * psi_conj)

    eqs = []
    for k in range(n):
        eqs.append(sp.re(sp.expand(residual[k])))
        eqs.append(sp.im(sp.expand(residual[k])))
    unknowns = list(re) + list(im)
    sol = sp.solve(eqs, unknowns, dict=True)
    if not sol:
        return 0, {}
    s = sol[0]
    free = [u for u in unknowns if u not in s or s[u] not in (0, sp.S.Zero)]
    # count genuinely free params: unknowns not pinned to zero
    pinned_zero = sum(1 for u in unknowns if u in s and s[u] == 0)
    unconstrained = len(unknowns) - len(s)
    nonzero_solved = sum(1 for u in unknowns if u in s and s[u] != 0)
    n_free = unconstrained + nonzero_solved
    return n_free, {"pinned_zero": pinned_zero, "free_symbols_count": len(free)}


results = {}
print("=" * 72)
print("OB10 -> C27: can a Majorana condition halve the 2-dim S3 zero mode?")
print("=" * 72)

# --- Step 1: OB10's B, and its factorization ---------------------------------
print("\n=== Step 1: OB10's B factorizes into S3 (x) S6 pieces ===")
B_full = kron(s2, s2, s1, s2)  # OB10's unique found solution
B_S3 = s2  # first Kronecker slot = the 2-dim S3 spinor factor
B_S6 = kron(s2, s1, s2)  # remaining three slots = the 8-dim S6 spinor factor

factorizes = is_zero(B_full - kron(B_S3, B_S6))
print(f"B_full == B_S3 (x) B_S6 exactly: {factorizes}")
results["B_factorizes_S3_tensor_S6"] = bool(factorizes)

# --- Step 2: reality type of each factor separately --------------------------
print("\n=== Step 2: reality type of each factor SEPARATELY ===")
BBc_full = simplify(B_full * B_full.conjugate())
BBc_S3 = simplify(B_S3 * B_S3.conjugate())
BBc_S6 = simplify(B_S6 * B_S6.conjugate())

S3_pseudoreal = is_zero(BBc_S3 + eye(2))
S6_real = is_zero(BBc_S6 - eye(8))
full_pseudoreal = is_zero(BBc_full + eye(16))

print(f"S3 factor:   B_S3 * conj(B_S3) = -I2  -> PSEUDO-REAL: {S3_pseudoreal}")
print(f"S6 factor:   B_S6 * conj(B_S6) = +I8  -> REAL:        {S6_real}")
print(f"full 16-dim: B * conj(B) = -I16       -> PSEUDO-REAL: {full_pseudoreal}")
print("  => the pseudo-reality of the product comes ENTIRELY from the S3 factor,")
print("     since (-1)*(+1) = -1. The S6 factor is honestly real.")
results["S3_factor_pseudoreal"] = bool(S3_pseudoreal)
results["S6_factor_real"] = bool(S6_real)
results["full_module_pseudoreal"] = bool(full_pseudoreal)

# --- Step 3: THE TEST -- Majorana condition on the S3 zero mode --------------
print("\n=== Step 3: Majorana condition psi = B_S3 * conj(psi) on the 2-dim S3 space ===")
print("(C27's zero mode at t=0 IS the generic constant spinor (a,b) in C^2,")
print(" round78 Section B: the ENTIRE 2-dim space is the kernel.)")
n_free_S3, detail_S3 = majorana_solutions(B_S3)
print(f"free real parameters in the solution space: {n_free_S3} (0 => only psi=0)")
majorana_impossible_S3 = n_free_S3 == 0
print(f"Majorana halving IMPOSSIBLE on the S3 zero mode: {majorana_impossible_S3}")
results["S3_majorana_free_params"] = n_free_S3
results["S3_majorana_impossible"] = bool(majorana_impossible_S3)

# --- Step 3b: is OB10's B the ONLY candidate? EXHAUSTIVE search --------------
# The Step-3 result only rules out OB10's SPECIFIC B. A critic would rightly
# ask: could some OTHER antilinear structure on the same 2-dim space be REAL
# (J^2=+1) and so permit a Majorana condition? Search ALL of them: write the
# antilinear map as J = M . conj for a fully generic complex 2x2 M, impose
# compatibility with the S3 Clifford action (M conj(Z_i) = eta Z_i M, for a
# shared sign eta = +1 or -1), solve, and inspect the sign of M conj(M).
print("\n=== Step 3b: EXHAUSTIVE -- does ANY compatible antilinear J have J^2=+1? ===")
Zs = [I * s for s in (s1, s2, s3)]
m_re = symbols("mr0:4", real=True)
m_im = symbols("mi0:4", real=True)
M_gen = Matrix(2, 2, [m_re[k] + I * m_im[k] for k in range(4)])

exhaustive = {}
for eta in (1, -1):
    eqs = []
    for Zi in Zs:
        resid = sp.expand(M_gen * Zi.conjugate() - eta * Zi * M_gen)
        for k in range(4):
            eqs.append(sp.re(resid[k]))
            eqs.append(sp.im(resid[k]))
    sol = sp.solve(eqs, list(m_re) + list(m_im), dict=True)
    if not sol:
        exhaustive[f"eta={eta:+d}"] = "no compatible M at all"
        print(f"  eta={eta:+d}: no compatible antilinear structure exists")
        continue
    M_sol = simplify(M_gen.subs(sol[0]))
    if is_zero(M_sol):
        exhaustive[f"eta={eta:+d}"] = "only M=0 (trivial)"
        print(f"  eta={eta:+d}: only the trivial M=0 -- not a structure")
        continue
    MMc = simplify(M_sol * M_sol.conjugate())
    # MMc must be a scalar multiple of I2 for J^2 to be well defined
    scal = simplify(MMc[0, 0])
    is_scalar = is_zero(MMc - scal * eye(2))
    sign_str = (
        "POSITIVE (would allow Majorana)"
        if scal.is_positive
        else (
            "NEGATIVE (pseudo-real, forbids Majorana)"
            if scal.is_negative
            else f"indeterminate: {scal}"
        )
    )
    exhaustive[f"eta={eta:+d}"] = {
        "scalar_multiple_of_I": bool(is_scalar),
        "M_conj(M)_coefficient": str(scal),
        "reading": sign_str,
    }
    print(f"  eta={eta:+d}: M conj(M) = ({scal}) * I2, scalar={is_scalar} -> {sign_str}")


# WHY this is not just `not scal.is_positive`: sympy returns None (undecidable)
# for a symbolic expression like -mi2**2-mr2**2, and `not None` is True -- the
# flag would then PASS BY ACCIDENT rather than by proof. Caught on the first
# run. The rigorous statement is that the coefficient equals MINUS AN EXPLICIT
# SUM OF SQUARES of real symbols, hence <= 0 always and < 0 for any nonzero M.
# That is checkable exactly, so check it exactly.
def coefficient_is_minus_sum_of_squares(expr_str: str) -> bool:
    expr = sp.sympify(expr_str)
    neg = sp.expand(-expr)
    if neg == 0:
        return False
    poly = sp.Poly(neg, *sorted(neg.free_symbols, key=str))
    # every monomial must be an even power with a positive coefficient
    for monom, coeff in poly.terms():
        if any(p % 2 != 0 for p in monom):
            return False
        if not sp.sympify(coeff).is_positive:
            return False
    return True


no_real_structure_exists = True
for key, v in exhaustive.items():
    if isinstance(v, str):
        continue  # "no compatible M" / "only M=0" -- no real structure from here
    proven_negative = coefficient_is_minus_sum_of_squares(v["M_conj(M)_coefficient"])
    v["proven_negative_definite"] = proven_negative
    print(
        f"  {key}: coefficient is minus an explicit sum of squares "
        f"(hence < 0 for any nonzero M): {proven_negative}"
    )
    if not proven_negative:
        no_real_structure_exists = False
print(
    f"\nNO compatible REAL (J^2=+1) structure exists on the S3 spinor factor: "
    f"{no_real_structure_exists}"
)
print("  => the no-go is not about OB10's particular choice of B; it is a")
print("     property of the 2-dim Cl(0,3) module itself (textbook: the SU(2)")
print("     fundamental is quaternionic). Verified here rather than cited.")
results["exhaustive_antilinear_search"] = exhaustive
results["no_real_structure_exists_on_S3_factor"] = bool(no_real_structure_exists)

# --- Step 4: NEGATIVE CONTROL -- must FIND solutions for a real structure ----
print("\n=== Step 4: NEGATIVE CONTROL -- same solve on a genuinely REAL structure ===")
print("(A test that cannot distinguish real from pseudo-real is not a test.)")
B_real_ctrl = s1  # s1 is real, so s1*conj(s1) = s1^2 = +I2 -> REAL type
ctrl_is_real = is_zero(simplify(B_real_ctrl * B_real_ctrl.conjugate()) - eye(2))
n_free_ctrl, _ = majorana_solutions(B_real_ctrl)
print(f"control B=s1 is genuinely REAL (B*conj(B)=+I2): {ctrl_is_real}")
print(f"free real parameters for the control: {n_free_ctrl} (expect > 0)")
control_discriminates = ctrl_is_real and n_free_ctrl > 0
print(f"CONTROL PASSES (test can tell real from pseudo-real): {control_discriminates}")
results["control_is_real_type"] = bool(ctrl_is_real)
results["control_majorana_free_params"] = n_free_ctrl
results["control_discriminates"] = bool(control_discriminates)

# --- Step 5: does adding an arbitrary PHASE rescue it? -----------------------
print("\n=== Step 5: does a phase, psi = lambda * B_S3 * conj(psi), rescue it? ===")
lam = symbols("lam", complex=True)
n = 2
re_ = symbols("c0:2", real=True)
im_ = symbols("d0:2", real=True)
psi = Matrix([re_[k] + I * im_[k] for k in range(n)])
psi_c = Matrix([re_[k] - I * im_[k] for k in range(n)])
# iterate the condition twice: psi = lam*B*conj(psi) => psi = |lam|^2 * B*conj(B) * psi
BBc = simplify(B_S3 * B_S3.conjugate())
print("iterating twice gives psi = |lam|^2 * (B*conj(B)) * psi = -|lam|^2 * psi")
print("  => need -|lam|^2 = 1 for nonzero psi, impossible for a real modulus.")
phase_cannot_rescue = is_zero(BBc + eye(2))  # BBc = -I is what forces it
print(f"phase CANNOT rescue the condition: {phase_cannot_rescue}")
results["phase_cannot_rescue"] = bool(phase_cannot_rescue)

# --- Step 6: does it survive to t=1 (the x-dependent zero mode)? -------------
print("\n=== Step 6: t=1 zero mode psi(x) = gbar(x)*psi_0 -- same conclusion? ===")
x0, x1, x2, x3 = symbols("x0 x1 x2 x3", real=True)
Z = [I * s for s in (s1, s2, s3)]
gbar = x0 * I2 - x1 * Z[0] - x2 * Z[1] - x3 * Z[2]
# key identity: for gbar built from real coords in this quaternion model,
# B * conj(gbar) = gbar * B  (so the x-dependence passes through untouched)
lhs = simplify(B_S3 * gbar.conjugate())
rhs = simplify(gbar * B_S3)
passes_through = is_zero(lhs - rhs)
print(f"identity B_S3 * conj(gbar(x)) == gbar(x) * B_S3, identically in x: {passes_through}")
print(
    "  => psi(x) = B conj(psi(x))  <=>  gbar*psi_0 = gbar*B*conj(psi_0)  <=>  psi_0 = B conj(psi_0)"
)
print("     i.e. the t=1 case reduces EXACTLY to the t=0 case just tested.")
results["t1_reduces_to_t0"] = bool(passes_through)

# --- Step 7: the symplectic-Majorana alternative, and why 3 channels block it -
print("\n=== Step 7: symplectic-Majorana (the standard pseudo-real workaround) ===")
print("For a pseudo-real structure the standard fix pairs an EVEN number of")
print("flavors: psi^A = B conj(psi^B) eps_AB, A,B = 1..2k. This project has")
print("THREE triality channels (G67/G73), and 3 is odd -- so a channel-pairing")
print("symplectic-Majorana condition cannot be imposed symmetrically across all")
print("three. Pairing two and leaving one out would break the equal geometric")
print("status of the three channels, which is precisely what the N_gen=3 claim")
print("rests on (each channel index=1, C_G67C3).")
n_channels = 3
sympl_needs_even = n_channels % 2 == 0
print(
    f"n_triality_channels = {n_channels}; even (required for symmetric pairing)? {sympl_needs_even}"
)
results["n_triality_channels"] = n_channels
results["symplectic_pairing_possible_symmetrically"] = bool(sympl_needs_even)

# --- verdict ------------------------------------------------------------------
print("\n" + "=" * 72)
all_ok = (
    factorizes
    and S3_pseudoreal
    and S6_real
    and full_pseudoreal
    and majorana_impossible_S3
    and control_discriminates
    and phase_cannot_rescue
    and passes_through
)
verdict = "MAJORANA_BRANCH_CLOSED" if all_ok else "INCONCLUSIVE"
print(f"VERDICT: {verdict}")
if all_ok:
    print("\nThe 'new reality/Majorana condition' row of C27's Relaxation Map is")
    print("CLOSED as a route to halving multiplicity 2 -> 1: the S3 spinor factor")
    print("(where the excess lives) is pseudo-real, so no Majorana condition --")
    print("with or without a phase, at t=0 or t=1 -- has any nonzero solution.")
    print("The symplectic-Majorana workaround is separately blocked by the odd")
    print("channel count. The OTHER two rows (orbifold projection; 32-state")
    print("reconciliation) are UNTOUCHED and remain open.")
results["verdict"] = verdict

RESULTS_PATH.write_text(json.dumps(results, indent=2))
print(f"\nResults -> {RESULTS_PATH}")
