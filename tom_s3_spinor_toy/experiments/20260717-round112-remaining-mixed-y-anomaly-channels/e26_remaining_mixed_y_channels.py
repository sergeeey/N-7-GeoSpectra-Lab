"""E26 (round112): the 2 mixed-U(1)_Y anomaly conditions round96/round92
never computed -- [SU(2)_L]^2 U(1)_Y and [SU(2)_R]^2 U(1)_Y -- closing
OB8 (flagged by Codex's round105 cross-model review). Reuses round92's
per-endpoint representation content and round96's Y=T3R+(B-L)/2 with
B-L=0 (round94) unchanged; no new field-content input.
"""

import sympy as sp

print("=" * 92)
print("PART 0 -- Reused inputs (round92, round93, round94, round96; not re-derived)")
print("=" * 92)

n_triality_channels = 3  # G67
BL = sp.Integer(0)  # round94

half = sp.Rational(1, 2)
zero = sp.Integer(0)

# t=0: SU(2)_L singlet (T3L=0 for both physical states), SU(2)_R doublet
# (T3R=+1/2,-1/2). Y = T3R + BL/2.
t0_T3L = [zero, zero]
t0_T3R = [half, -half]
t0_Y = [t3r + BL / 2 for t3r in t0_T3R]

# t=1: SU(2)_L doublet (T3L=+1/2,-1/2), SU(2)_R singlet (T3R=0 for both).
t1_T3L = [half, -half]
t1_T3R = [zero, zero]
t1_Y = [t3r + BL / 2 for t3r in t1_T3R]

print(f"  t=0: T3L={t0_T3L}, T3R={t0_T3R}, Y={t0_Y}")
print(f"  t=1: T3L={t1_T3L}, T3R={t1_T3R}, Y={t1_Y}")
print()

print("=" * 92)
print("SANITY CHECK -- formula reproduces the known SM cancellation")
print("A([SU(2)_L]^2 U(1)_Y) = sum_i (T3L_i)^2 * Y_i")
print("=" * 92)
# Q doublet: T3L=+-1/2, Y=1/6, x3 colors. L doublet: T3L=+-1/2, Y=-1/2.
Q_contrib = 3 * sum((half) ** 2 * sp.Rational(1, 6) for _ in range(2))
L_contrib = sum((half) ** 2 * sp.Rational(-1, 2) for _ in range(2))
sm_check = sp.simplify(Q_contrib + L_contrib)
print(f"  Q (x3 color) + L doublet contributions = {Q_contrib} + {L_contrib} = {sm_check}")
print(f"  Matches known SM cancellation (=0)? {sm_check == 0}")
print()

print("=" * 92)
print("PART 1 -- [SU(2)_L]^2 U(1)_Y = sum_i (T3L_i)^2 * Y_i")
print("=" * 92)
su2L2_Y = {}
for label, T3L_list, Y_list in [("t0_alone", t0_T3L, t0_Y), ("t1_alone", t1_T3L, t1_Y)]:
    per_channel = sum(t3l**2 * Y for t3l, Y in zip(T3L_list, Y_list))
    su2L2_Y[label] = sp.nsimplify(n_triality_channels * per_channel)
su2L2_Y["union"] = su2L2_Y["t0_alone"] + su2L2_Y["t1_alone"]
for k, v in su2L2_Y.items():
    print(f"  A([SU(2)_L]^2 U(1)_Y, {k}) = {v}")
print()

print("=" * 92)
print("PART 2 -- [SU(2)_R]^2 U(1)_Y = sum_i (T3R_i)^2 * Y_i")
print("=" * 92)
su2R2_Y = {}
for label, T3R_list, Y_list in [("t0_alone", t0_T3R, t0_Y), ("t1_alone", t1_T3R, t1_Y)]:
    per_channel = sum(t3r**2 * Y for t3r, Y in zip(T3R_list, Y_list))
    su2R2_Y[label] = sp.nsimplify(n_triality_channels * per_channel)
su2R2_Y["union"] = su2R2_Y["t0_alone"] + su2R2_Y["t1_alone"]
for k, v in su2R2_Y.items():
    print(f"  A([SU(2)_R]^2 U(1)_Y, {k}) = {v}")
print()

print("=" * 92)
print("VERDICT INPUTS")
print("=" * 92)


def forcing_pattern(d):
    return d["t0_alone"] != 0 and d["t1_alone"] != 0 and d["union"] == 0


conditions = {
    "[SU(2)_L]^2 U(1)_Y": su2L2_Y,
    "[SU(2)_R]^2 U(1)_Y": su2R2_Y,
}

verdict = {"sm_sanity_check_passed": bool(sm_check == 0), "both_conditions_computable": True}
any_forcing = False
for name, d in conditions.items():
    forcing = forcing_pattern(d)
    any_forcing = any_forcing or forcing
    verdict[f"{name}_t0_alone"] = str(d["t0_alone"])
    verdict[f"{name}_t1_alone"] = str(d["t1_alone"])
    verdict[f"{name}_union"] = str(d["union"])
    verdict[f"{name}_forcing_pattern"] = forcing
    print(
        f"  {name}: t0={d['t0_alone']}, t1={d['t1_alone']}, union={d['union']}, forcing={forcing}"
    )
verdict["any_new_condition_shows_forcing"] = any_forcing
print()
for k, v in verdict.items():
    print(f"  {k}: {v}")

print()
if any_forcing:
    label = "PASS__FORCING_PATTERN_FOUND_IN_REMAINING_CHANNELS"
else:
    label = "FAIL__BOTH_REMAINING_CONDITIONS_COMPUTABLE_NONE_SHOW_FORCING__EXTENDS_ROUND96"
print(f"label = '{label}'")
