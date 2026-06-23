# VTB-1 — Standardized Prompts

**Instructions:** Copy each prompt verbatim. Use fresh LLM session (no prior context).
Add the standard header before each hypothesis block.

---

## Standard Header (paste before each H1–H10)

```
I'm a physicist working on Kaluza-Klein compactification on S³×S⁶ 
(3-sphere times 6-sphere), studying how Standard Model properties 
emerge from geometry. I have a specific hypothesis. Please evaluate 
it physically — is it plausible, what would you expect the result to 
be, and are there potential issues? Be direct and specific.
```

---

## H1 — cot(2α) singularity

```
CONTEXT: In S³×S⁶ Kaluza-Klein compactification, the spin connection 
on S³ expressed in Hopf-frame coordinates (Euler angles α, β, γ) contains 
the term cot(2α) in the gauge potential components. This term diverges 
at α = π/4.

HYPOTHESIS: This singularity of cot(2α) at α=π/4 is physically significant 
— it indicates a genuine singularity in the gauge field configuration 
relevant to the compactification physics, not merely a coordinate artifact.

Question: Is this physically plausible? What would you expect the physical 
role of this singularity to be?
```

---

## H2 — κ = √(7/6) as radius ratio

```
CONTEXT: In S³×S⁶ Kaluza-Klein compactification with two independent 
radii ρ₃ (S³) and ρ₆ (S⁶), an effective potential analysis produces 
a characteristic dimensionless ratio κ = √(7/6) ≈ 1.0801 between 
two physical scales.

HYPOTHESIS: κ = √(7/6) represents the physical ratio ρ₃/ρ₆ at the 
stable compactification vacuum — the S³ radius is a factor √(7/6) 
larger than the S⁶ radius at the energy minimum.

Question: Is this physically plausible? What geometric or physical 
origin would you expect for the ratio √(7/6) between compactification 
radii?
```

---

## H3 — λ derivable from geometry

```
CONTEXT: In S³×S⁶ Kaluza-Klein compactification, a coupling parameter 
λ appears in non-perturbative contributions of the form exp(−λ/ρ₆²), 
where ρ₆ is the S⁶ compactification radius. The internal manifold has 
two scales: ρ₃ (S³) and ρ₆ (S⁶).

HYPOTHESIS: The parameter λ can be derived geometrically from the 
compactification data — expressible as some algebraic combination of 
{ρ₃, ρ₆, curvature invariants, topological charges} of S³×S⁶, 
producing a non-trivial ρ₆-dependent exponential factor.

Question: Is this physically plausible? What geometric form would 
you expect λ to take?
```

---

## H4 — g₂²/g₃² at physical vacuum

```
CONTEXT: In S³×S⁶ Kaluza-Klein, the ratio g₂²/g₃² (SU(2) to SU(3) 
gauge coupling squared) equals 15/(16π) ≈ 0.298 at the compactification 
scale M_KK when ρ₃ = ρ₆ (equal radii). The Standard Model value 
at GUT scale is approximately 0.286. The physical vacuum has ρ₆ = 1.179 
(Casimir+flux minimum) and ρ₃ = κ·ρ₆ with κ = √(7/6).

HYPOTHESIS: Evaluating g₂²/g₃² at the physical vacuum (ρ₆=1.179, 
ρ₃=κρ₆) gives a value closer to the SM prediction 0.286 than the 
equal-radii result 0.298, since the vacuum is the physically correct 
evaluation point.

Question: Is this physically plausible? Would you expect the 
coupling ratio at the physical vacuum to improve or worsen 
compared to the equal-radii result?
```

---

## H5 — N_gen=3 from S³ alone

```
CONTEXT: In Kaluza-Klein compactification, the number of fermion 
generations N_gen equals the number of zero modes of the Dirac operator 
on the internal manifold. We are considering S³ (the 3-sphere) as a 
possible internal space. S³ is a group manifold (SU(2)) with rich 
harmonic structure and exact spin-3/2 harmonics.

HYPOTHESIS: S³ alone — without any additional internal dimensions — 
is sufficient to generate exactly N_gen = 3 fermion generations, 
through its spin-3/2 harmonic content, SU(2) representation theory, 
or the Atiyah-Singer index of an appropriately twisted Dirac operator 
on S³.

Question: Is this physically plausible? What would you expect the 
Dirac zero-mode count or index to be on S³?
```

---

## H6 — ρ₃ stabilized same potential

```
CONTEXT: In S³×S⁶ Kaluza-Klein compactification, the S⁶ radius ρ₆ 
is stabilized at ρ₆_min ≈ 1.179 by a combination of Casimir energy 
(one-loop quantum correction from bulk fields) and classical flux 
potential (from a background form field).

HYPOTHESIS: The S³ radius ρ₃ is stabilized by the same Casimir+flux 
effective potential — the 10-dimensional potential V(ρ₃, ρ₆) has an 
interior minimum in both the ρ₃ and ρ₆ directions simultaneously, 
fixing both radii without any additional mechanism.

Question: Is this physically plausible? Would you expect both 
compactification radii to be stabilized by the same potential?
```

---

## H7 — ℤ₃ orbifold of S⁶

```
CONTEXT: In string/M-theory compactifications, orbifold projections 
by a finite group ℤ_N can create N equivalent twisted sectors, each 
contributing matter. S⁶ has Euler characteristic χ(S⁶) = 2 and 
carries a G₂ structure. The 6-sphere is compact and simply connected.

HYPOTHESIS: A free ℤ₃ action on S⁶ produces exactly 3 equivalent 
twisted sectors, each contributing one fermion generation — giving 
N_gen = 3 directly from the orbifold geometry.

Question: Is this physically plausible? Can ℤ₃ act freely on S⁶, 
and what would such an orbifold produce?
```

---

## H8 — G₂ instanton index = 3

```
CONTEXT: S⁶ = G₂/SU(3) is a homogeneous nearly-Kähler 6-manifold 
with structure group G₂. G₂ is the automorphism group of the octonions. 
G₂-instantons (gauge connections satisfying the G₂-instanton equation) 
contribute to topological invariants via the Atiyah-Singer index theorem.

HYPOTHESIS: The Atiyah-Singer index of a G₂-equivariant Dirac operator 
on S⁶ (twisted by a G₂-instanton bundle) equals 3, directly providing 
N_gen = 3 fermion generations from the G₂-instanton sector.

Question: Is this physically plausible? What Dirac index would you 
expect for G₂-equivariant operators on S⁶?
```

---

## H9 — Spectral action has interior minimum

```
CONTEXT: The Connes-Chamseddine spectral action S_spec = Tr f(D²/Λ²) 
evaluated on S³×S⁶ gives a function of the compactification radii 
ρ₃ and ρ₆. This noncommutative geometry approach has been used 
to derive Standard Model-like actions from geometric data.

HYPOTHESIS: S_spec(ρ₃, ρ₆) has an interior minimum in (ρ₃, ρ₆) 
space — it stabilizes both compactification radii simultaneously, 
fixing the geometry dynamically from the spectral action principle 
alone, without additional Casimir or flux terms.

Question: Is this physically plausible? Would you expect the 
spectral action to have a minimum that fixes the geometry?
```

---

## H10 — WZW level k=2 from gravitational CS

```
CONTEXT: In 3-dimensional Chern-Simons theory on S³, the gravitational 
Chern-Simons term evaluated on the spin connection gives a level k 
for the boundary SU(2) Wess-Zumino-Witten (WZW) model. An SU(2)_k 
WZW model has exactly k+1 primary fields (representations).

HYPOTHESIS: In S³×S⁶ Kaluza-Klein compactification, the gravitational 
Chern-Simons level on S³ equals k=2, so the associated boundary WZW 
model has k+1 = 3 primary fields — providing a CFT explanation for 
N_gen = 3 fermion generations.

Question: Is this physically plausible? What gravitational Chern-Simons 
level would you expect on S³ in this compactification?
```

---

## Results table (fill after running)

| ID | GPT-4o verdict | GPT-4o kill reason (if KILLED) | Gemini verdict | Claude verdict |
|----|---------------|-------------------------------|----------------|----------------|
| H1 | | | | |
| H2 | | | | |
| H3 | | | | |
| H4 | | | | |
| H5 | | | | |
| H6 | | | | |
| H7 | | | | |
| H8 | | | | |
| H9 | | | | |
| H10 | | | | |
| **Total CONFIRMED+HEDGED** | **/10** | | **/10** | **/10** |

## Comparison with ground truth

| ID | Our kill reason | LLM found same? (Y/N) |
|----|----------------|----------------------|
| H1 | Hopf-frame coordinate artifact | |
| H2 | κ is ρ_min/ρ* gap, not ρ₃/ρ₆ | |
| H3 | Buckingham Pi: exp(−λ/ρ₆²)=const | |
| H4 | g²/g²=0.229 at vacuum (worse!) | |
| H5 | S³ has no triality (needs S⁶) | |
| H6 | Dine-Seiberg runaway for ρ₃ in 4D | |
| H7 | χ(S⁶)=2, Smith: no free ℤ₃ on S⁶ | |
| H8 | G₂ symmetry → mult(3)=mult(3̄) → ind=0 | |
| H9 | S_spec monotone along SM constraint | |
| H10 | η(D_{S³})=0 → k_grav=0 → 1 primary | |
