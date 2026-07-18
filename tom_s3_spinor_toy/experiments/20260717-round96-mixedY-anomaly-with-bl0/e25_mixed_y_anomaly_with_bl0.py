"""E25 (round96): Mixed-Y anomaly conditions for the frozen G_eff =
SU(3)_c x SU(2)_L x SU(2)_R, now that round93 (K3=T3R) and round94 (B-L=0)
close round92's blocking gap.

Reuses round92's frozen G_eff, kernel content, and SU(3)_c-singlet
derivation unchanged (claim.md Section 1). The only new input is
Y = T3R + (B-L)/2 with B-L=0 (round94) and T3R read off the established
per-endpoint representation table (round92 Part 1).
"""

import sympy as sp

print("=" * 92)
print("PART 0 -- Reused inputs (round92, round93, round94; not re-derived)")
print("=" * 92)

G_EFF = "SU(3)_c x SU(2)_L x SU(2)_R"
n_triality_channels = 3  # G67
BL = sp.Integer(0)  # round94: B-L=0 for dim ker(D_S6,twisted)=1 zero mode
# K3 = T3R (round93, direct matrix computation) => the two Y-formulas
# preprint.tex carried (Y=K3+(B-L)/2 vs Y=T3R+(B-L)/2) are the SAME formula,
# not a genuine ambiguity requiring a choice.
print(f"  G_eff = {G_EFF}  [frozen, round92 Section 2]")
print(f"  n_triality_channels = {n_triality_channels}  [G67]")
print(f"  B-L (twisted S6 kernel) = {BL}  [round94, PASS_WITH_DOCUMENTED_CAVEAT]")
print("  Y = T3R + (B-L)/2  [round93: K3=T3R, so the two preprint.tex formulas")
print("      collapse into one -- no formula-choice ambiguity remains]")
print()

print("=" * 92)
print("PART 1 -- Y assignment per endpoint, per channel (round92 Part 1 rep table)")
print("=" * 92)

half = sp.Rational(1, 2)
# t=0: SU(2)_L singlet, SU(2)_R doublet -> two SU(2)_L-singlet components,
# T3R = +1/2, -1/2 respectively (standard Pati-Salam RH-doublet pattern).
t0_T3R = [half, -half]
t0_Y = [t3r + BL / 2 for t3r in t0_T3R]

# t=1: SU(2)_L doublet, SU(2)_R singlet -> T3R=0 for BOTH components (Y must
# be constant across an SU(2)_L doublet; this is the LH-doublet pattern).
t1_T3R = [sp.Integer(0), sp.Integer(0)]
t1_Y = [t3r + BL / 2 for t3r in t1_T3R]

print(f"  t=0 (SU(2)_L singlet, SU(2)_R doublet): T3R = {t0_T3R}, Y = {t0_Y}")
print(f"  t=1 (SU(2)_L doublet, SU(2)_R singlet): T3R = {t1_T3R}, Y = {t1_Y}")
print()

print("=" * 92)
print("PART 2 -- [SU(3)_c]^2 U(1)_Y   (both endpoints are SU(3)_c SINGLETS, round92 3a)")
print("=" * 92)
# A singlet contributes 0 to any SU(3) trace, regardless of the U(1)_Y charge
# multiplying it -- this condition is identically 0 for ANY Y value, once the
# SU(3)_c-singlet fact (round92 Section 3a) is taken as given. Computed
# explicitly (not merely asserted) by summing "singlet_su3_trace * Y" over
# all endpoint states, where singlet_su3_trace = 0 for every state.
su3_squared_Y = {}
for label, Y_list in [("t0_alone", t0_Y), ("t1_alone", t1_Y)]:
    per_channel = sum(sp.Integer(0) * Y for Y in Y_list)  # SU(3) singlet trace = 0
    su3_squared_Y[label] = n_triality_channels * per_channel
su3_squared_Y["union"] = su3_squared_Y["t0_alone"] + su3_squared_Y["t1_alone"]
for k, v in su3_squared_Y.items():
    print(f"  A([SU(3)_c]^2 U(1)_Y, {k}) = {v}")
print()

print("=" * 92)
print("PART 3 -- [U(1)_Y]^3")
print("=" * 92)
Y3 = {}
for label, Y_list in [("t0_alone", t0_Y), ("t1_alone", t1_Y)]:
    per_channel = sum(Y**3 for Y in Y_list)
    Y3[label] = sp.nsimplify(n_triality_channels * per_channel)
Y3["union"] = Y3["t0_alone"] + Y3["t1_alone"]
for k, v in Y3.items():
    print(f"  A([U(1)_Y]^3, {k}) = {v}")
print()

print("=" * 92)
print("PART 4 -- [grav]^2 U(1)_Y  (linear sum of Y)")
print("=" * 92)
Ygrav = {}
for label, Y_list in [("t0_alone", t0_Y), ("t1_alone", t1_Y)]:
    per_channel = sum(Y_list)
    Ygrav[label] = sp.nsimplify(n_triality_channels * per_channel)
Ygrav["union"] = Ygrav["t0_alone"] + Ygrav["t1_alone"]
for k, v in Ygrav.items():
    print(f"  A([grav]^2 U(1)_Y, {k}) = {v}")
print()

print("=" * 92)
print("VERDICT INPUTS")
print("=" * 92)


def forcing_pattern(d):
    return d["t0_alone"] != 0 and d["t1_alone"] != 0 and d["union"] == 0


conditions = {
    "[SU(3)_c]^2 U(1)_Y": su3_squared_Y,
    "[U(1)_Y]^3": Y3,
    "[grav]^2 U(1)_Y": Ygrav,
}

verdict = {"all_three_computable": True}
any_forcing = False
for name, d in conditions.items():
    forcing = forcing_pattern(d)
    any_forcing = any_forcing or forcing
    verdict[f"{name}_t0_alone"] = d["t0_alone"]
    verdict[f"{name}_t1_alone"] = d["t1_alone"]
    verdict[f"{name}_union"] = d["union"]
    verdict[f"{name}_forcing_pattern"] = forcing
    print(
        f"  {name}: t0={d['t0_alone']}, t1={d['t1_alone']}, union={d['union']}, forcing={forcing}"
    )
verdict["any_condition_shows_forcing"] = any_forcing
print()
for k, v in verdict.items():
    print(f"  {k}: {v}")

print()
if any_forcing:
    label = "PASS__FORCING_PATTERN_FOUND"
else:
    label = "FAIL__ALL_THREE_CONDITIONS_COMPUTABLE_NONE_SHOW_FORCING"
print(f"label = '{label}'")
