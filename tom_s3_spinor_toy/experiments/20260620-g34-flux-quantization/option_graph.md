# Option Graph — G34: c₃=6 Selection Mechanisms

**Date:** 2026-06-20  
**Open question:** What independently forces c₃(V) = 6 = 3 × χ(S⁶) on S⁶?

Known null results: G27 (ℤ₃ Smith), G30 (G₂ symmetry), G31 (Lichnerowicz+parity), G33 (A1 circular).

---

## Tier 1 — Primary Mechanisms (testable this week)

### D1 — Flux Quantization / Tadpole
- **Changed assumption:** c₃ is selected by a dynamical/tadpole condition, not just topological
- **Mechanism type:** Geometric selection
- **Status:** WEAK (see G34 analysis)
- **Reason:** H⁶(S⁶;ℤ)=ℤ allows any c₃ ∈ ℤ. Flux quantization is NECESSARY (c₃ ∈ ℤ) but NOT SUFFICIENT. No natural topological invariant of S⁶ equals 3 independently.
- **Cheapest test:** Show ∫_{S⁶} G₆ = c₃/2 is quantized to any integer, not forced to 3. CHECK: does p₁, â, or any Pontryagin class of S⁶ equal 3? (Answer: H⁴(S⁶)=0, so p₁=0.)
- **Circularity risk:** LOW — flux quantization doesn't embed N_gen by construction
- **Next action:** Test tadpole in string compactification context (G35 if full D1 analysis needed)

### A2 — Global Anomaly / Cobordism
- **Changed assumption:** The *number* of generations is fixed by quantum consistency (not just topology)
- **Mechanism type:** Quantum consistency condition
- **Status:** ALIVE — distinct from local anomalies, less explored
- **Reason:** Cobordism group Ω^{Spin}_6 = 0 means S⁶ bounds, but bordism invariants can still constrain. The Dai-Freed theorem links η-invariants to anomaly cancellation.
- **Cheapest test:** Compute η(D_{S⁶}) for the standard Dirac operator on S⁶. If η has fractional value n/3, mod-3 selection is possible.
- **Circularity risk:** LOW if η computed from geometry alone
- **Next action:** G35 cobordism gate

### C1 — NCG Finite Algebra A_F = M₃(ℂ)
- **Changed assumption:** A_F can be derived from geometry of S⁶, not postulated
- **Mechanism type:** Algebraic derivation
- **Status:** ALIVE_IF_BRIDGE_EXISTS / CIRCULAR_IF_NOT
- **Reason:** End(T^{1,0}S⁶) = M₃(ℂ) naturally. But if we use this to say "dim=3 → N_gen=3", that's A1 revisited (circular). Non-circular requires showing M₃(ℂ) structure FORCES the finite spectral triple independently.
- **Cheapest test:** Can one derive A_F from a natural categorification of End(T^{1,0}S⁶) without assuming N_gen=3? Write explicit map: geometry → finite triple algebra.
- **Circularity risk:** HIGH — needs explicit non-circular bridge

### K-theory
- **Changed assumption:** K-theory charges rather than Chern classes are the fundamental data
- **Mechanism type:** Topological classification
- **Status:** ALIVE — K̃(S⁶) = ℤ with generator β, ch₃(β)=1
- **Reason:** K-theory is more refined than cohomology. Stable equivalence classes might constrain which bundles are physically realizable.
- **Cheapest test:** Does any K-theory stability condition force [V] = 3·[β] over [V] = [β]?
- **Circularity risk:** MEDIUM — K-theory generator has c₃=2 (same as T^{1,0}S⁶), so 3 copies give c₃=6, but "3 copies" embeds N_gen=3
- **Next action:** Check if there's a natural K-theory element with c₃=6 without being 3⊗(generator)

---

## Tier 2 — Secondary Mechanisms (require more setup)

### B3 — WZW Level from S³
- **Changed assumption:** The S³ Chern-Simons level k propagates to select c₃ on S⁶
- **Mechanism type:** Coupled boundary/bulk condition
- **Status:** WEAK
- **Reason:** S³ with round metric has CS level k=2 (from instanton). WZW level k=2 gives SU(2)₂. How does k=2 on S³ force c₃=6 on S⁶? Need explicit coupling mechanism. Also: k=2 not k=3.
- **Cheapest test:** Write coupling equation: k_{S³} × ind_{S⁶} = ? What equation gives ind_{S⁶}=3 from k=2?
- **Circularity risk:** MEDIUM — k=2 not 3, so "3" must appear elsewhere

### Spectral Action Minimum
- **Changed assumption:** Spectral action S[D] has a minimum that selects c₃=6
- **Mechanism type:** Variational selection
- **Status:** ALIVE_CONDITIONAL
- **Reason:** If the spectral action functional on the space of bundles V on S⁶ has a minimum at c₃=6, this would select it. Requires: (a) action defined on bundle space, (b) minimum is at c₃=6 not c₃=2.
- **Cheapest test:** Write S[V] = Tr(f(D_V²)) and compute δS/δ[V] = 0. Is minimum at c₃=2 (ground state) or c₃=6?
- **Circularity risk:** LOW if computed without N_gen input

### Representation Theory G₂/SU(3)
- **Changed assumption:** The branching G₂ → SU(3) has a "3" hiding in root multiplicities
- **Mechanism type:** Group-theoretic constraint
- **Status:** PARKED
- **Reason:** G₂ has 14 generators, SU(3) has 8, coset = 6. No "3" from simple root counting. Would need index-3 subgroup or triality structure (which G₂ doesn't have — only D₄ has triality).
- **Cheapest test:** Check if G₂ has any ℤ₃ quotient or index-3 sub-structure. (G₂ has no ℤ₃ center; center is trivial.)
- **Circularity risk:** MEDIUM — G₂ root system is G₂ (A₂-type short roots), no "3" from group structure alone

---

## Tier 3 — Tools Only (not selection mechanisms)

### Markov Chains
- **Role:** Sampling/search over bundle space or hypothesis space
- **Status:** TOOL_ONLY — not a mechanism for selecting c₃
- **Why:** MC requires a state space, action S[A], transition kernel, and stationary distribution. None of these arise naturally from S⁶ topology. MC can EXPLORE {c₃=2,4,6,8,...} but cannot SELECT 6.
- **When useful:** If there's a natural measure on bundle space → MC explores the landscape

### Chernoff Bound
- **Role:** Statistical test to distinguish hypotheses H(c₃=2) vs H(c₃=6)
- **Status:** DETECTION_TOOL — for discriminating between models, not for selection
- **Why:** Chernoff gives sample complexity needed to distinguish two distributions. Relevant if we have multiple experiments and want to know how many are needed to rule out c₃=2 vs c₃=6.
- **When useful:** After finding both c₃=2 and c₃=6 bundles in nature, Chernoff tells how to distinguish them experimentally

### Information Criteria (AIC/BIC)
- **Role:** Model comparison
- **Status:** TOOL_ONLY — compares models, doesn't derive topology
- **When useful:** If two spectral triple models compete (c₃=6 vs c₃=2), BIC selects the simpler one

---

## Priority Order (for G35+)

```
1. A2 — cobordism / η-invariant (fresh approach, no circularity risk)
2. D1 — tadpole in string context (needs full string setup, D1 alone is weak)
3. C1 — NCG bridge (needs explicit geometry → algebra map)
4. K-theory — needs non-circular "3 copies" story
5. B3 — needs explicit S³→S⁶ coupling
6. Spectral action minimum — requires action functional on bundle space
7. Parked: G₂ rep theory (no "3" from group structure)
8. Tools: Markov, Chernoff, IC (useful later, not primary)
```

---

## Alive/Killed Summary

| Candidate | Status | Key blocker |
|-----------|--------|-------------|
| D1 flux quantization | WEAK | Allows c₃=6, doesn't select it |
| A2 cobordism/η | ALIVE | η(D_{S⁶}) not yet computed |
| C1 NCG M₃(ℂ) | ALIVE_IF_BRIDGE | Non-circular bridge missing |
| K-theory | ALIVE | "3 copies" story may be circular |
| B3 WZW | WEAK | k=2 on S³, not k=3 |
| Spectral action | ALIVE_CONDITIONAL | Action functional not yet defined |
| G₂ rep theory | PARKED | No ℤ₃ structure in G₂ |
| Markov chains | TOOL_ONLY | Not a mechanism |
| Chernoff | TOOL_ONLY | Not a mechanism |
| A1 (dim_ℂ=3) | KILLED | G33 — c₃=2 not 6 |
