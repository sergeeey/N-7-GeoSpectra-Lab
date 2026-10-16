"""Scratch check: are C212's tangent vectors v_a=K_a@N orthonormal under the
ambient R^7 dot product, as needed for Russo's Ric_g=5*mu^2 / |T|^2=24*mu^2
formulas (which assume an orthonormal frame in the AMBIENT metric g, not
necessarily G96's Frobenius-norm-orthonormal Lie-algebra generators)."""

import importlib.util

import numpy as np

spec = importlib.util.spec_from_file_location(
    "g96", "experiments/20260626-g96-s6-g2-su3/g96_g2_su3.py"
)
g96 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g96)

phi = g96.build_phi()
gens = g96.find_g2_generators(phi)
e6 = np.zeros(7)
e6[6] = 1.0
A = np.column_stack([G @ e6 for G in gens])
_, sv, Vt = np.linalg.svd(A, full_matrices=True)
rank = int(np.sum(sv > 1e-10))
null = Vt[rank:]
gm = np.array([G.flatten() for G in gens])
su3 = [row.reshape(7, 7) for row in (null @ gm)]
Qsu3, _ = np.linalg.qr(np.column_stack([g.flatten() for g in su3]), mode="reduced")
comp_vecs = []
for G in gens:
    gf = G.flatten()
    res = gf - Qsu3 @ (Qsu3.T @ gf)
    if np.linalg.norm(res) > 1e-10:
        comp_vecs.append(res)
Qc, Rc = np.linalg.qr(np.column_stack(comp_vecs), mode="reduced")
ncomp = int(np.sum(np.abs(np.diag(Rc)) > 1e-10))
comp = [Qc[:, k].reshape(7, 7) for k in range(ncomp)]

tangent = np.array([G @ e6 for G in comp])
gram = tangent @ tangent.T
print("Gram matrix v_a . v_b (ambient R^7 dot product):")
print(np.round(gram, 6))
print("norms^2 (diag):", np.round(np.diag(gram), 6))
print("off-diag max:", np.max(np.abs(gram - np.diag(np.diag(gram)))))
