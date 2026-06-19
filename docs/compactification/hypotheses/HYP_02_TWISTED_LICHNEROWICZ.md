# Hypothesis 2: Twisted Lichnerowicz Eigenvalue

**Status:** hypothesis (toy 2026-05-25: `hypothesis_supported` in 1D constrained subspace; does not override P13E global NO-GO)  
**Target:** Resolving Normalization Failure (P13 part 3)  
**Tom Lawrence Q-Link:** N/A (Direct computational attack)  
**XLSX Links:** Rows 8–14 (S3 Dirac E₀, Ben Achour E_i), Row 15 (V low-mode integral)

* **<fact>:** In principal-bundle formalisms, geometric couplings can be treated as eigenvalues of a twisted transversality problem constrained by curvature laws (e.g., dλ + ad*_ω λ = 0).
* **<bridge>:** The free prefactor λ is reinterpreted as an eigenvalue of a constrained differential operator L_tw = Δ_L + C(Ω), where Δ_L is the Lichnerowicz operator and C(Ω) is the curvature-induced coadjoint constraint.
* **<assumption>:** The dynamical vs. background field mismatch can be resolved by enforcing bundle-theoretic compatibility, simultaneously fixing the physical mode's normalization.
* **<falsifier>:** If the constrained kernel of the twisted operator L_tw remains multidimensional (> 1D up to rescaling) after all compatibility constraints are applied.
* **<toy_test>:** Assemble a finite-mode matrix version of the Lichnerowicz operator with curvature couplings on a left-invariant truncation. Impose linear transversality constraints and solve as a generalized eigenvalue problem.
* **<observable>:** The dimension of the constrained kernel and the specific value of the first admissible normalized eigenvalue.

**Experiment (2026-05-25):** `hyp02_twisted_lichnerowicz.py` — 2-mode P13B1 truncation with toy transversality constraint; compares admissible eigenvalue across Haar conventions.
