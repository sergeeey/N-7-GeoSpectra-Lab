# Competitor Analysis: "A Discrete Universe" (Pollard 2026)

**Source:** zenodo.org/records/20768426  
**Author:** Lance Pollard  
**Date reviewed:** 2026-06-26  
**Found by:** research-pipeline (HN/Algolia scan)

---

## Their Claim

"A discrete, deterministic, reversible model that derives the architecture of the
Standard Model and a universal computer from one premise — a single reversible
distinction — on a forced hyperbolic mesh of 24-cells."

Mathematical substrate: octonions on a hyperbolic 24-cell lattice (TypeScript).

---

## Comparison with Our Approach

| Aspect | Pollard 2026 | Our approach (S³×S⁶) |
|---|---|---|
| Geometry | Discrete hyperbolic 24-cell lattice | Continuous Riemannian S³×S⁶ |
| Mathematical tool | Octonions (combinatorial) | Octonions via G₂=Aut(𝕆), S⁶=G₂/SU(3) |
| SM gauge group | Derived from lattice architecture | SU(3)×SU(2)_L×SU(2)_R from Iso(S⁶)×Iso(S³) |
| N_gen | Not mentioned | 3 via triality (G73+G74, proven) |
| U(1)_Y | Not specified | Partial: B-L absent, needs Tom Part 4/5 |
| Coupling constants | FREE parameters (explicit) | λ = FREE_COUPLING_PARAMETER (theorem G4) |
| Rigor level | "Exploratory, feasibility-stage" (self-declared) | Full falsification ladder, 29-31/N tests |
| Implementation | TypeScript (GitHub: cluesurf/vibe) | Python + SymPy + pytest |
| KK reduction | Not present | Full 4D reduction (G91, G95-G97) |

---

## Verdict

**Not a direct competitor.** Pollard's work is a combinatorial/discrete toy model
at feasibility stage. It shares our motivation (SM from octonions) but uses a
completely different mathematical framework (discrete lattice vs. continuous KK).

**Key distinguishing strength of our approach:**
1. Formal KK reduction D=13→D=4 with frame-independence proof (G91)
2. Atiyah-Singer index theorem → N_gen=3 (G73+G74, not an assumption)
3. Wigner-Eckart λ-free ratio R_B=√2 (first testable prediction)
4. Coupling constants = FREE by formal theorem (G4), not by assumption

**What to watch:** If Pollard derives N_gen=3 or a U(1)_Y mechanism from the
lattice, that would be worth deeper comparison. Current feasibility-stage status
means no immediate action required.
