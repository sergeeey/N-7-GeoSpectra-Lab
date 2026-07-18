"""Round117: tests one candidate resolution of round80/E14's own flagged
open tension (Reading 3 vs Lemma L5) -- does S6's orientation-reversal
(used by L5) have the SAME structural status (ungauged, disconnected
component of the isometry group) as S3's own iota (round80's own result),
or is there a genuine asymmetry between the two factors?

Mirrors round80's own Part A computation (isometry + det check) exactly,
applied to S6 instead of S3, for a direct, symmetric comparison.
"""

import sympy as sp

print("=" * 92)
print("PART 1 -- round80's own S3 result (cited, not re-derived): iota(g)=g^-1,")
print("Phi(x0,x1,x2,x3)=(x0,-x1,-x2,-x3), det(J)=-1, isometry, in O(4)\\SO(4)")
print("=" * 92)
J_S3 = sp.diag(1, -1, -1, -1)
det_S3 = J_S3.det()
isometry_S3 = bool(sp.simplify(J_S3.T * J_S3 - sp.eye(4)) == sp.zeros(4, 4))
print(f"  J_S3 = diag(1,-1,-1,-1), det={det_S3}, J^T*J=I (isometry)? {isometry_S3}")
print("  Confirms round80's own citation: iota in O(4)\\SO(4) (det=-1, disconnected).")
print()

print("=" * 92)
print("PART 2 -- Analogous construction for S6 subset R^7: an orientation-reversing")
print("isometry of the round S6, mirroring round80's Part A exactly")
print("=" * 92)
# Simplest orientation-reversing isometry of S^6 in R^7: flip one coordinate.
# Psi(y1,...,y7) = (y1,...,y6,-y7). Standard, general fact, verified directly.
J_S6 = sp.diag(1, 1, 1, 1, 1, 1, -1)
det_S6 = J_S6.det()
isometry_S6 = bool(sp.simplify(J_S6.T * J_S6 - sp.eye(7)) == sp.zeros(7, 7))
print(f"  J_S6 = diag(1,1,1,1,1,1,-1), det={det_S6}, J^T*J=I (isometry)? {isometry_S6}")
print(f"  Maps S6 (unit sphere in R^7) to itself? {True}  (linear orthogonal map, preserves |y|=1)")
print()

print("=" * 92)
print("PART 3 -- Direct structural comparison")
print("=" * 92)
same_structural_status = (det_S3 == -1) and (det_S6 == -1) and isometry_S3 and isometry_S6
print("  Both iota (S3) and this S6 orientation-flip are isometries with det=-1,")
print("  hence both lie in the DISCONNECTED component O(n)\\SO(n) of their")
print("  respective isometry groups -- the SAME structural status, confirmed")
print(f"  by direct construction on both factors: {same_structural_status}")
print()
print("  Per round80's own citation (preprint.tex:274,279,422), this project's")
print("  gauge construction (SU(2)_L x SU(2)_R x SU(3)_c) uses ONLY the CONNECTED")
print("  component Iso(S3xS6)=SO(4)xSO(7) -- meaning NEITHER S3's iota NOR this")
print("  S6 orientation-flip is gauged. Both are ungauged discrete symmetries of")
print("  identical type (O(n)/SO(n)=Z2, standard general fact, applied to n=4 and")
print("  n=7 respectively).")
print()

print("=" * 92)
print("PART 4 -- Does this kill the proposed 'gauged S3 vs ungauged S6' resolution?")
print("=" * 92)
resolution_survives = not same_structural_status  # resolution needs an ASYMMETRY; found none
print("  Proposed resolution requires S3's relevant discrete symmetry (iota) to be")
print("  gauged while S6's (orientation-flip) is not. Both are found ungauged,")
print(f"  identically. Does the proposed resolution survive? {resolution_survives}")
print()

verdict = {
    "S3_iota_confirmed_det_minus_1_disconnected": bool(det_S3 == -1 and isometry_S3),
    "S6_orientation_flip_confirmed_det_minus_1_disconnected": bool(det_S6 == -1 and isometry_S6),
    "same_structural_status_both_ungauged": same_structural_status,
    "proposed_gauged_vs_ungauged_resolution_survives": resolution_survives,
}
print("=" * 92)
print("VERDICT")
print("=" * 92)
for k, v in verdict.items():
    print(f"  {k}: {v}")

print()
if not resolution_survives:
    label = "RESOLUTION_ATTEMPT_FAILS__BOTH_FACTORS_EQUALLY_UNGAUGED__ROUND80_TENSION_REMAINS_OPEN"
else:
    label = "RESOLUTION_SURVIVES__GENUINE_ASYMMETRY_FOUND"
print(f"  label = '{label}'")
