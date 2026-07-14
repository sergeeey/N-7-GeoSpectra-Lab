# Round61-BLCommutantAudit Claim — is B-L the unique gauge U(1) commutant?

**Date:** 2026-07-14
**FL tier:** [x] Full (candidate headline addition to the paper if PASS; a real
mathematical claim about this project's own 32-dim fermion space either way)
**Question type:** [x] descriptive (existence/uniqueness of a linear-algebra
object under stated constraints — not causal, not predictive)

---

## Prior Result Gate

Not previously attempted as a blind search. The B-L generator's geometric
origin is the standing open item (gate G97, preprint Open Problems, "Gauge
coupling unification / U(1)_B-L origin"): SU(4) is absent from
Iso(S³×S⁶), so B-L cannot be embedded as an isometry generator; the preprint
currently states it is "identified from fermion charge content" (i.e.
reverse-engineered from the known SM charge table, `g16_t3r_k3.py`'s
`BmL_32`), not derived from a constraint search. This round asks a narrower,
answerable question: starting from ONLY the already-geometrically-derived
data (the 32-dim spinor, the SU(3)×SU(2)_L×SU(2)_R action, chirality γ_F,
real structure J_F — all already built and tested in `g11_block_generators.py`,
`g16_t3r_k3.py` §generators, `g18_ncg.py`) plus the model-independent physical
requirement of anomaly cancellation, is the space of admissible U(1)
generators forced down to (a multiple of) B-L, or not?

null_results check: no prior attempt at this specific search found in
`null_results/INDEX.md` or `parked/INDEX.md` (checked: no entry matches
"commutant", "B-L search", "hypercharge uniqueness").

---

## Frozen claim

Let $T$ range over Hermitian $32\times 32$ operators satisfying, in this
strict order (each is a hard constraint, not a preference):

1. **Commutant**: $[T, C_i] = 0$ ($i=1..8$, $\mathrm{SU}(3)_c$), $[T,J_a]=0$
   ($a=1,2,3$, $\mathrm{SU}(2)_L$), $[T,K_a]=0$ ($a=1,2,3$, $\mathrm{SU}(2)_R$)
   — all nine+ generators already built in `g11_block_generators.py`.
2. **Chirality-compatible**: $[T, \gamma_F] = 0$ ($\gamma_F$ from `g18_ncg.py`).
3. **Real-structure-compatible**: $J_F T J_F^{-1} = -T$ ($J_F$ from
   `g18_ncg.py` — the physical requirement that charge-conjugate states carry
   opposite $T$-charge; $J_F$ is a real symmetric permutation with
   $J_F^2=\mathbb{1}$ so $J_F^{-1}=J_F$).
4. **Anomaly-free** (per generation, no inter-generation cancellation
   assumed, matching the preprint's own existing hypercharge check style,
   eq. 286-291): gravitational-U(1) ($\sum T = 0$), cubic U(1)³
   ($\sum T^3=0$), $\mathrm{SU}(3)^2$-U(1) ($\sum_{\text{color-charged}} T=0$),
   $\mathrm{SU}(2)_L^2$-U(1) ($\sum_{\text{L-doublets}} T=0$),
   $\mathrm{SU}(2)_R^2$-U(1) ($\sum_{\text{R-doublets}} T=0$).

**Claim to test:** the solution space $V = \{T : \text{constraints 1-4 hold}\}$
is exactly 1-dimensional (a single line through the origin, i.e. $T$ is
unique up to real rescaling), and this line, when compared AFTER the fact
(not used as a search input) to the known $B{-}L$ generator already in
`g16_t3r_k3.py` (`BmL_32`), coincides with it up to normalization.

**Explicit prohibition (builder blindness for the search step):** the
constraint-solving code must NOT import, read, or hard-code `BmL_32`, `Y_32`,
or any value derived from them, while constructing or solving for $T$. Only
the comparison step at the very end (§ verdict) may reference `BmL_32`.

---

## Kill criteria (fixed before running)

| Outcome | Condition | Verdict |
|---|---|---|
| **PASS** | $\dim V = 1$ (over the reals, after imposing 1-3 as linear constraints then 4 as the anomaly system) AND the surviving direction is proportional to `BmL_32` (checked post hoc) | B-L is forced by these constraints; genuine derivation candidate |
| **PASS-DIFFERENT** | $\dim V = 1$ but the surviving direction is **not** proportional to `BmL_32` | A different, unexpected unique U(1) is forced — equally interesting, must be reported honestly, not silently discarded |
| **FAIL** | $\dim V \geq 2$ (a family of admissible generators survives) | B-L is not uniquely selected by these constraints alone; an additional physical principle is needed. Report the full family. |
| **NO-GO** | $\dim V = 0$ (only $T=0$ survives, i.e. constraints 1-4 are jointly incompatible with any nonzero generator) | Constraints as stated are too strong for this fermion content; report which specific constraint (3 vs 4) kills it, and whether relaxing chirality/real-structure alone (dropping constraint 3, keeping 1-2-4) already restores a solution, to localize the obstruction |

All three non-PASS outcomes are pre-registered as informative, not as
failures of the round — this matches the Anti-Overfitting Gate's stance:
each is a specific, falsifiable, reportable structural fact about this
project's own fermion content.

---

## Method (two independent routes + adversarial verify)

- **Route A — blind commutant + anomaly solve.** Build the 32×32 generators
  fresh from the existing, already-tested modules (import allowed: `J_S3`,
  `K_S3` lifted to 32×32 via `kron(·, I8)`; `C_i^{32}` from the SU(3) spinor
  lift already in the repo — reusing already-established geometric objects
  is legitimate, this is not what "blind" refers to). Compute the commutant
  of the full 14-generator Lie algebra via exact nullspace over general
  Hermitian $32\times32$ matrices restricted to those commuting with all 14
  (do not assume the block-diagonal-scalar structure — derive it). Then
  impose $[T,\gamma_F]=0$, then $J_F T J_F = -T$, then solve the anomaly
  system (linear constraints as a linear system on the remaining free
  parameters; the cubic $\sum T^3=0$ solved exactly over the reduced
  parameter space). Report $\dim V$ and, if $\dim V=1$, the explicit
  generator (up to scale).
- **Route B — independent state-by-state derivation.** Without reading Route
  A's code, independently derive the $\mathrm{SU}(3)\times\mathrm{SU}(2)_L\times
  \mathrm{SU}(2)_R$-irreducible block decomposition of the 32 states by hand
  from the existing state labels (`SM_LH_UP`, `SM_LH_DN`, and the analogous
  R-sector dicts in `g16_t3r_k3.py`/`g17_electric_charge.py` — reading the
  *labels*, not the *charges*, is allowed; the charges themselves must not be
  used to constrain $T$), construct the general ansatz (one real parameter
  per irreducible block) directly, impose the same 4 constraints
  independently, and cross-check $\dim V$ and the surviving generator(s)
  against Route A.
- **Verify** — adversarial skeptic pass: (1) an anomaly-completeness auditor
  checking whether any standard mixed-anomaly condition was omitted (e.g.
  $[\mathrm{grav}]^2$-$\mathrm{SU}(2)_R^2$, or Witten $\mathrm{SU}(2)$ global
  anomaly considerations) that could change the verdict; (2) an independence
  auditor confirming Route B did not leak charge information from Route
  A/the known table; (3) if PASS, a direct numeric confirmation that the
  surviving $T$ satisfies ALL of constraints 1-4 exactly (not just the
  subset used to derive it) — a closure check.

---

## What this does NOT mean

1. Does NOT touch L3b, L4B, or any other open problem — fully independent
   question.
2. A PASS does NOT mean $\mathrm{U}(1)_{B-L}$ is derived "from the isometry
   group" (gate G97's finding stands: no $\mathrm{SU}(4)$ isometry exists) —
   it would mean $B{-}L$ is the unique gauge-and-anomaly-consistent charge
   assignment on the already-geometrically-derived fermion representation
   content, a different and still nontrivial claim.
3. Does NOT claim completeness of the anomaly-condition list beyond the four
   standard mixed anomalies plus grav-U(1) and cubic U(1)³ (Witten's global
   $\mathrm{SU}(2)$ anomaly and gravitational mixed anomalies beyond
   grav²-U(1) are not separately checked unless the skeptic pass flags them
   as necessary).
4. Does NOT constitute external review even if PASS — internal certification
   only, same standing as Round 59's status.

## Fence

- λ = FREE_COUPLING_PARAMETER (untouched)
- safe_for_runtime = False
