"""Cross-check: C165 (2026-09-06) independently computed the SAME canonical-
connection curvature R^c(X,Y)=-[X,Y]_h for S6=G2/SU(3), via the SAME Nomizu
formula, using G96's RAW orthonormalized complement basis (no ambient-unit
tangent rescaling) -- reporting max|R^c|=0.431 (19/19 checks passed,
independent skeptic pass CONFIRMED-REAL). This script reuses C216's own
kn_curvature_torsion() at scale=1.0 (G96's native basis, matching C165's
convention exactly) instead of C216's scale=sqrt(3) (ambient-unit tangent,
matching C212-215's ladder) to check: (a) does max|R^c| match C165's 0.431?
(b) after converting to the ambient-unit scale via the KN curvature's known
scale dependence, is the resulting Ricci consistent with C216's own
scale=sqrt(3) result (Ric^c=4.0)?
"""

import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("c216", HERE / "c216_kn_ricci_check.py")
c216 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c216)

comp, su3, rescale = c216.g2su3_data()
print(f"C216's own ambient-unit rescale factor = {rescale:.6f} (expect sqrt(3)={np.sqrt(3):.6f})")

# C165's convention: scale=1.0 (G96's raw QR-orthonormalized complement basis)
riem1, tors1, leak1 = c216.kn_curvature_torsion(comp, su3, 1.0)
ricci1 = c216.ricci_from_riem(riem1)
print("\nscale=1.0 (C165's own basis convention):")
print(f"  max|R^c| (riemann tensor) = {np.max(np.abs(riem1)):.6f}  (C165 reported: 0.431)")
print(f"  Ric^c diag = {np.round(np.diag(ricci1), 6)}  leak={leak1:.2e}")
print(f"  |T|^2 from bracket = {np.sum(tors1**2):.6f}")

# C216's own convention: scale=rescale=sqrt(3) (ambient-unit tangent)
riem2, tors2, leak2 = c216.kn_curvature_torsion(comp, su3, rescale)
ricci2 = c216.ricci_from_riem(riem2)
print(f"\nscale={rescale:.6f} (C216's ambient-unit convention):")
print(f"  Ric^c diag = {np.round(np.diag(ricci2), 6)}  leak={leak2:.2e}")
print(f"  |T|^2 from bracket = {np.sum(tors2**2):.6f}")

print(
    f"\nRatio Ric^c(scale=1)/Ric^c(scale=rescale) = {ricci1[0, 0] / ricci2[0, 0]:.6f} (expect rescale^2={rescale**2:.6f} if Ric scales as 1/length^2 under e_a->scale*K_a... or check actual dependence)"
)
