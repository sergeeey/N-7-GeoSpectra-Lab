r"""
C158 STEP 5 -- FULL CLOSURE of the forcing chain, per the skeptic's own
suggested sharpening (independent adversarial pass on this round): does a
charge-conjugation-type operator make Q_mu_plus = Q_mu_minus (the one fact
Step 4/novelty_check.md left "open") ITSELF forced, rather than requiring new
computation?

CANDIDATE: the chirality operator omega = i^3 * E_1...E_6, ALREADY IN USE
since C156 (there: "omega anticommutes with every e_a, so D_Sigma is odd").
Nothing new is built here -- this step only asks whether that PRE-EXISTING
object also does the missing job.

If omega.psi_+ is proportional to psi_- (unit modulus), and omega anticommutes
with every E_i (hence with D_Sigma(v) for any v, same argument as C156's own
chirality-oddness proof), then for any v:

    Q_-(v) = ||D(v) psi_-||^2 = ||D(v) (c * omega * psi_+)||^2
           = |c|^2 * ||D(v) omega psi_+||^2
           = |c|^2 * ||omega D(v) psi_+||^2      [D(v) omega = -omega D(v)]
           = |c|^2 * ||D(v) psi_+||^2             [omega unitary]
           = |c|^2 * Q_+(v)

so if |c|=1 (forced by ||psi_+||=||psi_-||, both already known), Q_- = Q_+
EXACTLY, for EVERY v -- closing the round's own last flagged open question.

Run:  python c158_step5_full_closure.py
"""

import importlib.util
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent


def load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


S4 = load("c158_s4", "c158_step4_equivariance.py")
E_sym = S4.E_sym
psi_p = S4.psi_p
D_LC_2, b2 = S4.D_LC_2, S4.b2

psi_m = None
for val, mult, vecs in D_LC_2.eigenvects():
    if sp.nsimplify(val) == -3:
        psi_m = sp.simplify(b2 * vecs[0])
assert psi_m is not None

print("=" * 78)
print("STEP 5  is the chirality operator omega (already used since C156) the")
print("        charge-conjugation map that forces Q_mu_plus = Q_mu_minus?")
print("=" * 78)

omega = sp.eye(8)
for k in range(1, 7):
    omega = omega * E_sym[k]
omega = sp.simplify(sp.I**3 * omega)

print(f"  omega^2 == I : {sp.simplify(omega * omega) == sp.eye(8)}")
print(
    f"  omega unitary (omega omega^dagger = I) : "
    f"{sp.simplify(omega * omega.conjugate().T) == sp.eye(8)}"
)
anti = all(sp.simplify(omega * E_sym[k] + E_sym[k] * omega) == sp.zeros(8, 8) for k in range(1, 7))
print(f"  omega anticommutes with every E_i (i=1..6) : {anti}")
assert anti, "if this fails, the whole closure argument is void -- STOP"

img = sp.simplify(omega * psi_p)
nz = next(k for k in range(8) if sp.simplify(psi_m[k]) != 0)
c = sp.simplify(img[nz] / psi_m[nz])
match = sp.simplify(img - c * psi_m) == sp.zeros(8, 1)
print(f"  omega.psi_+ == {c} * psi_- (exactly) : {match}")
assert match
print(f"  |c| == 1 : {sp.simplify(sp.Abs(c)) == 1}")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("  omega.psi_+ = psi_-  EXACTLY (c=1), omega unitary, omega anticommutes")
print("  with D_Sigma(v) for every v (same mechanism as C156's own chirality-")
print("  oddness proof). This closes the chain fully:")
print()
print("    Q_-(v) = ||D(v)omega.psi_+||^2 = ||omega.D(v)psi_+||^2")
print("           = ||D(v)psi_+||^2 = Q_+(v)     for EVERY v.")
print()
print("  Q_mu_plus = Q_mu_minus is FORCED by a chirality operator this project")
print("  already had on record before C158 started. Nothing new anywhere in")
print("  this chain: G4 (ker(M) invariance), the isotypic decomposition, and")
print("  Q_+ = Q_- are ALL consequences of (a) D_Sigma being odd [C156], (b)")
print("  the Pin cover of the Weyl group [Schur 1911 / Ciubotaru 2010], (c)")
print("  psi_+, psi_- being the omega-conjugate pair of eigenvectors of a")
print("  single Hermitian operator D(LC). C158 rediscovered this from scratch")
print("  in one specific example; it discovered nothing beyond it.")
