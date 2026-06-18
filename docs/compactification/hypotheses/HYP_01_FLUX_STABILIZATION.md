# Hypothesis 1: Flux / Moduli Stabilization

**Status:** hypothesis (toy: coupled branch `hypothesis_supported`; decoupled falsifier `hypothesis_killed`)  
**Target:** Resolving P13/P14 No-Go (Fixing λ)  
**Tom Lawrence Q-Link:** Q3 (Where is λ fixed?)  
**XLSX Links:** Row 21 (BG-H1 S³×S¹), Row 16 (λ NO-GO S3)

* **<fact>:** In flux compactifications, quantized fluxes stabilize moduli fields, reducing continuous free parameters to discrete critical points determined by integer topological data.
* **<bridge>:** λ is not a parameter of the pure S³ algebra, but a modulus conjugate to a mixed topological sector in an extended geometry (e.g., S³×S¹ or S³×S⁶). Its value is locked at the extremum of a reduced effective potential V_eff(λ; N_a) built from integer fluxes N_a.
* **<assumption>:** The true compactification manifold contains non-trivial mixed cycles or torsion classes that couple to the V-sector, preventing λ from remaining a free integration constant.
* **<falsifier>:** If the dimensional reduction on the enlarged manifold yields ∂_λ V_eff ≡ 0 after imposing all Bianchi identities and flux quantization conditions (meaning no topological sector interacts with λ).
* **<toy_test>:** Construct a minimal V_eff toy model with one overall radius, one squashing mode, and two integer flux numbers. Solve for ∂_λ V_eff = 0 to find isolated real critical points.
* **<observable>:** The isolated critical value λ_*(N_a) and its corresponding Hessian eigenvalue to confirm stability.

**Experiment (2026-05-25):** `hyp01_flux_veff.py` — coupled sector yields discrete λ_*; removing κ coupling triggers falsifier (∂_λ V ≡ 0).
