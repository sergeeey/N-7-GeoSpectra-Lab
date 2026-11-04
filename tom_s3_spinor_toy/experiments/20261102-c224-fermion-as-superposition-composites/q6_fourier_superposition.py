"""Q6: the correspondent's 18-20.10 claim: a half-integer-weight amplitude is a superposition of integer harmonics,
so 'fermions are superpositions of composite bosons'. Our 21.10 reply said: true on the interval,
false as a statement about periodic fields.

f(phi) = e^{i phi/2} on [0, 2 pi).  Checks:
  F1. c_k = (1/2pi) int_0^{2pi} f e^{-ik phi} dphi = i / (pi (1/2 - k))  for all integers k.
  F2. Parseval: sum_k |c_k|^2 = 1 = ||f||^2 (L^2 of the interval): f IS an L^2-convergent sum.
  F3. Periodic sum S(phi) = sum c_k e^{ik phi}: S = f on (0, 2 pi), S(0) = 0 (midpoint of the jump),
      but f(phi + 2 pi) = -f(phi) while S(phi + 2 pi) = S(phi): S is NOT the antiperiodic f on the circle.
  F4. Dragging by alpha on the circle with the seam: (R_alpha f)(phi) = f(phi - alpha mod 2 pi)
      equals S(phi - alpha) (integer weights e^{-ik alpha} c_k), and differs from e^{-i alpha/2} f by a
      step of size 2 on the arc (0, alpha). So dragging acts on f with integer phases, not by the
      half-integer phase e^{-i alpha/2}.
  F5. Composites: product of two weight-1/2 amplitudes has weight 1 (integer); weight 1/2 times -1/2 has weight 0.
      Span of integer-weight periodic functions does not contain e^{i phi/2} (F3, F4).
"""

import numpy as np

fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


K = np.arange(-400, 401)
# analytic coefficients vs quadrature
Nq = 400000
phi = (np.arange(Nq) + 0.5) * (2 * np.pi / Nq)
f = np.exp(1j * phi / 2)


def coef(k):
    return np.sum(f * np.exp(-1j * k * phi)) * (2 * np.pi / Nq) / (2 * np.pi)


err = max(abs(coef(k) - 1j / (np.pi * (0.5 - k))) for k in (-5, -2, -1, 0, 1, 2, 3, 7))
check("F1 c_k = i/(pi(1/2-k)) by midpoint quadrature (max error %.1e)" % err, err < 1e-4)

c = 1j / (np.pi * (0.5 - K))
parseval = np.sum(np.abs(c) ** 2)
check("F2 Parseval sum |c_k|^2 over |k|<=400 = %.6f (-> 1)" % parseval, abs(parseval - 1) < 3e-3)


def S(ph, Kmax=400):
    ph = np.asarray(ph, dtype=float)
    return np.sum(c[None, :] * np.exp(1j * np.outer(ph, K)), axis=1)


check("F3a S(0) = 0 (average of +1 and -1 at the seam)", abs(S([0.0])[0]) < 1e-2)
check(
    "F3b S(phi) ~ f(phi) on (0, 2 pi) at interior points",
    np.max(np.abs(S([0.7, 2.0, 4.5]) - np.exp(1j * np.array([0.7, 2.0, 4.5]) / 2))) < 1e-2,
)
check(
    "F3c f(phi+2pi) = -f(phi)  but  S(phi+2pi) = S(phi): S is not the antiperiodic f on the circle",
    abs(np.exp(1j * (2 * np.pi) / 2) + 1) < 1e-12
    and abs(S([1.3])[0] - S([1.3 + 2 * np.pi])[0]) < 1e-12,
)

# F4 dragging on the circle with seam
alpha = 1.2
phs = np.linspace(0.01, 2 * np.pi - 0.01, 2000)


def f_drag(ph):
    return np.exp(1j * np.mod(ph - alpha, 2 * np.pi) / 2)


step = f_drag(phs) - np.exp(-1j * alpha / 2) * np.exp(1j * phs / 2)
jd = np.mod(phs - alpha, 2 * np.pi)
away = (jd > 0.3) & (jd < 2 * np.pi - 0.3)  # error of the partial sum ~ 1/(K d) away from the jump
mask = phs < alpha
print(
    "   |R f - e^{-i a/2} f| on arc (0,alpha) (max) = %.3f ; off arc = %.2e"
    % (np.max(np.abs(step[mask])), np.max(np.abs(step[~mask])))
)
check(
    "F4a dragging does not multiply f by e^{-i alpha/2}: difference is a step of size 2 on (0, alpha)",
    np.max(np.abs(step[mask])) > 1.5 and np.max(np.abs(step[~mask])) < 1e-12,
)
check(
    "F4b dragged field equals S(phi - alpha) (integer-weight superposition, coefficients c_k e^{-ik alpha})",
    # Gibbs overshoot at the jump (size ~0.18 at K=400) is excluded: test only away from the jump
    np.max(np.abs(f_drag(phs) - S(phs - alpha))[away]) < 2e-2,
)

# F5 composites
ok = True
for ph in (0.4, 2.1, 5.0):
    a = np.exp(1j * ph / 2)
    ok &= abs(a * a - np.exp(1j * ph)) < 1e-12  # weight 1/2 + 1/2 = 1
    ok &= abs(a * np.conj(a) - 1) < 1e-12  # weight 1/2 - 1/2 = 0
check("F5 composites: (+1/2)+(+1/2) = 1 and (+1/2)+(-1/2) = 0 (integer weights)", ok)

print("\nFAILS:", fails if fails else "none")
