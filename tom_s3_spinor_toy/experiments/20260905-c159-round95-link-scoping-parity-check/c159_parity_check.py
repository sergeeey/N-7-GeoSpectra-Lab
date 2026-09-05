"""
C159 -- verify the elementary arithmetic behind round95's n_L=n_R anomaly
condition, and check whether n_L+n_R=3 with n_L=n_R has a non-negative
integer solution.

Inputs (re-cited from primary sources, re-verified against the actual files
this round -- see decision.md):
  A(4,2,1)  = +2   (round90 decision.md line 157, cited from the
                     retroactive correction at the top of that file, which
                     is the CURRENT/authoritative version of the anomaly
                     mechanism -- the file's original Witten-anomaly claim
                     in its uncorrected body is REFUTED by its own
                     retroactive correction block)
  A(4bar,1,2) = -2 (round90 decision.md line 157/159, same source)
  N_gen = 3        (G73/G74A/G74B, reused throughout -- not re-derived here)

This script does NOT assume the "exclusive pairing" framing is correct --
it only checks the pure arithmetic claim.md's Prior Result Gate rests on,
so the decision.md can cite a tool-run number rather than hand-typed
arithmetic.
"""

import sympy as sp

n_L, n_R = sp.symbols("n_L n_R", integer=True, nonnegative=True)
A_L = sp.Integer(2)  # A(4,2,1)
A_R = sp.Integer(-2)  # A(4bar,1,2)

# 1. Anomaly-cancellation condition: sum_i mult_i * A_i = 0
anomaly_eq = sp.Eq(n_L * A_L + n_R * A_R, 0)
anomaly_solution = sp.solve(anomaly_eq, n_L)
print("Anomaly condition:", anomaly_eq)
print("Solved for n_L:", anomaly_solution)
assert anomaly_solution == [n_R], "round95's n_L=n_R derivation does not check out"

# 2. If a pairing rule is EXCLUSIVE (each of the 3 channels assigned to
#    exactly one of the 2 t-sectors), then n_L+n_R=N_gen necessarily.
#    Does n_L=n_R combined with n_L+n_R=N_gen have a solution for N_gen=3?
N_gen = 3
exclusive_solutions = [
    (a, b) for a in range(N_gen + 1) for b in range(N_gen + 1) if a + b == N_gen and a == b
]
print(
    f"N_gen={N_gen}, exclusive-pairing solutions with n_L=n_R AND n_L+n_R=N_gen:",
    exclusive_solutions,
)
assert exclusive_solutions == [], (
    "unexpected: an integer solution exists, C159's core premise is wrong"
)

# 3. General odd/even sweep (matches C132/C133's own "every N_gen >= 1" framing)
print("\nGeneral sweep, N_gen=0..6, EXCLUSIVE pairing (n_L+n_R=N_gen):")
for N in range(7):
    sols = [(a, b) for a in range(N + 1) for b in range(N + 1) if a + b == N and a == b]
    print(f"  N_gen={N}: n_L=n_R solutions = {sols if sols else 'NONE (impossible)'}")

# 4. The escape hatch found in C132/C133: a NON-exclusive pattern where
#    every channel supplies content to BOTH sectors ("all->both").
#    Under this pattern, n_L = n_R = N_gen automatically (each channel
#    counted in BOTH totals), so n_L+n_R = 2*N_gen, NOT N_gen.
n_L_both = N_gen
n_R_both = N_gen
print(
    f"\n'all->both' pattern for N_gen={N_gen}: n_L={n_L_both}, n_R={n_R_both}"
    f" (n_L=n_R holds trivially: {n_L_both == n_R_both}); "
    f"n_L+n_R={n_L_both + n_R_both} != N_gen={N_gen}"
)
