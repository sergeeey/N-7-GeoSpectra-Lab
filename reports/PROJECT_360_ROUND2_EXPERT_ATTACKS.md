# Project 360° Scientific Red Team — Round 2: Expert Lens Attacks

**Date:** 2026-07-15
**Method:** 7 independent agents, each given only project files (not each other's output,
not this session's narrative) — full Context Asymmetry per `falsification-ladder.md`.
Each attacked one of the branches Round 1 ranked as live: L3B-SPIN8-GAP/F4-route,
L4A/L4B kernel certification, and gauge/B-L/parent-action.
**Full raw output:** preserved in the conversation transcript; this file is the
synthesis. No code changed, no experiments run by me — this round is agent analysis
only (one agent attempted an independent pytest reproduction and was blocked by its
own tool config, see Finding R2-7 below).

---

## Headline result of this round: three independent lenses converged, unprompted, on the same objection from three different angles

None of the seven agents saw each other's output. Three of them — differential
geometry, index theory, and the adversarial skeptic — independently arrived at
**the same underlying objection**, stated in each one's own vocabulary:

| Lens | How they said it |
|---|---|
| **Geometry** | Proposed a Z₃-equivariant index (Atiyah–Bott–Lefschetz) as the untried escape route — then itself supplied the cheapest test: *"does the triality Z₃ descend to any isometric action on S⁶ at all?"* — and answered its own question: **no**, because G₂ = Fix(triality) is by construction the triality-fixed locus, so triality acts trivially on every G₂-invariant structure. |
| **Index theory** | Independently proposed the identical Z₃-equivariant-index mechanism as "the untried tool," on the grounds that G102 only rules out *continuous* symmetries in 𝔰𝔬(8), not the *outer* automorphism ℤ₃ ⊂ Out(Spin(8)) that triality actually is. |
| **Adversarial skeptic** (blind to both of the above) | Found a **circularity**: the "three channels" three-ness enters as an *external label* (the ℤ₃ orbit {v,s,c}) applied at the start of the construction, not derived from it — and E-L3B already proves the three labeled bundles are the *same bundle*, so "3×ind=1" is one geometric object counted three times under a label the geometry itself cannot see. |

Put together, these three findings are not three separate concerns — they are the
**same gap, triangulated**: the natural mathematical tool that would legitimize the
"×3" step (equivariant index under the ℤ₃ triality action) is not actually available,
because that same ℤ₃ is precisely the symmetry G₂ was built to be fixed under. The
"three channels" are a bookkeeping label on one object, not three geometrically
distinguishable objects — which is exactly what the project's own Theorem E-L3B
already proves, and what the L3B_SPIN8_INTERFACE_SPEC.md route is trying (so far
unsuccessfully) to fix with external Spin(8)/F4 input.

**This does not overturn anything the project claims** — `preprint.tex` already
labels this exact step "conjectured... conditional on L3b" and the project's own
`L3B_SPIN8_INTERFACE_SPEC.md` already frames the F4 route as "a candidate route, not
a solution." What this round adds is a sharper, convergently-confirmed diagnosis of
*why* L3b is hard, and a concrete (negative) answer to the geometric-symmetry escape
that all three agents independently reached for first.

---

## Ranked findings (highest priority first)

### R2-1 [HIGH, new, highest priority] — No stated parent physical action for the twisted Dirac operator (compactification-physics lens)

The twisting bundle is set to `E = S⁻` specifically (`preprint.tex:461`) — that
choice alone is what forces `c₃=2` and hence `ind=1`. But the paper's own
**Proposition T2** shows the *untwisted* internal Dirac operator has index 0 (zero
generations). The twist is doing 100% of the generation-counting work, and its
physical origin — Lawrence's spin-connection-as-gauge-field identification — is
established by Lawrence only for U(1) (6D) and SU(2) (7D); `preprint.tex:244-248`
explicitly concedes SU(3) was deferred by Lawrence and is asserted here without
derivation. Null result G34-D1 already shows flux quantization alone allows *any*
`c₃∈ℤ` — nothing topological pins `c₃=2` independent of the twist choice.

**Why this ranks above L3b:** it is logically *prior*. Even a fully resolved L3b
(Spin(8) input granted) would still leave open whether `D⊗S⁻` is a physical
operator or a mathematically convenient one selected for its index. The agent's
proposed test — symbolically reduce the 10D chiral kinetic term with the
spin-connection-as-gauge identification imposed, and check whether `D⊗S⁻` falls out
or whether the untwisted (index-0) operator is what a real reduction gives — is
cheap (symbolic, no external input, no Tom Lawrence dependency) and decisive for
whether N_gen=3 is a physical prediction or, in the agent's words, "a mathematical
analogy in physical dress."

### R2-2 [MEDIUM-HIGH] — "Fully exhausted" (G102) is stated more strongly than proved (rep-theory lens)

`preprint.tex:1242-1245` says the internal search for a distinguishing symmetry is
"fully exhausted." The rep-theory agent found this over-states G102: G102 only
proves no symmetry commuting with (preserving) G₂ exists — but the project's own
same-day `SO(4)×SO(4)` work (`L3B_SPIN8_INTERFACE_SPEC.md:374-421`) explicitly
distinguishes s from c precisely by *breaking* G₂, internal to 𝔰𝔬(8). "Exhausted"
should read "no G₂-*preserving* internal symmetry." The agent also flagged that
today's `SO(4)×SO(4)` work may not have been cross-checked against the project's
own earlier G68 result (the L/R octonion-multiplication pseudoscalar distinction,
`Ω_L=+I≠Ω_R=−I`) — worth a consistency check, since they may be the same
distinguishing mechanism rediscovered without citation. The agent also proposed a
cheaper, more physically-grounded alternative to `SO(4)×SO(4)`: `Spin(6)×Spin(2) =
SU(4)×U(1)`, where `SU(4)=Spin(6)` is *already* the genuine S⁶ tangent-spinor frame
group (not a postulated second SO(4) with no physical identification).

### R2-3 [MEDIUM] — L3B-INDEXARITH ("index jumps 1→7, no twist gives exactly 3") is oversold relative to its own source (index-theory lens)

The preprint states this as settled fact, but the underlying experiment
(`claim-A-index-map.md`) labels its own general formula `SUPPORTED ON CONTROLS —
GENERAL PROOF OPEN`, verified at only 3 points. Low stakes for the physics (the
headline N_gen=3 comes from 1+1+1 across three channels, never from a single
index-3 twist), but a rigor gap worth closing — the agent specified two additional
cheap test points, `(1,1)` and `(3,0)`, ~15 min in sympy.

### R2-4 [MEDIUM] — "Three independent verification routes" for L4A/L4B kernel is oversold on independence, though the underlying result is solid (spectral-analysis lens)

The trivial-component `dim ker=1` result itself is genuinely robust (reduces to a
nonzero Killing-spinor eigenvalue via a sum-of-squares certificate — convention/sign
errors cannot flip it). But the three "independent" routes share the same primary
source (AHL2023), the same CAS (sympy), and the same author/session — per the
project's own Independent Verification Strength Ladder, this is "Weak–Medium," not
the "Strong" rung the framing implies. Separately, the real (under-stated) ρ=14 risk
is **not** the flagged sign caveat (a norm-based bound is sign-immune) — it is that
decomposition completeness was verified symbolically only at ρ=7, never repeated at
ρ=14, so the certified 0.381 margin rests on an *inferred* completeness plus a
normalization convention that was itself initially disputed before being resolved.
Cheapest decisive test: repeat the exact symbolic D² decomposition check at ρ=14
(reuses existing matrices).

### R2-5 [MEDIUM] — Anomaly-cancellation claim presupposes the open B-L input; "3 clean chiral generations" is double-conditional (phenomenology lens)

The anomaly check (`preprint.tex:284-294`) verifies U(1)_Y anomalies using
`Y=T₃R+(B-L)/2` — but B-L is explicitly not derived (SU(4) absent from the
isometry group, G97). So "verified, anomaly-free per generation" silently assumes
the very open problem it should be independent of. Separately: "three purely
left-handed generations" depends on BOTH L3b (open) AND the L4A/L4B trivial-rank
result (internally certified, external review outstanding) — only the *net* +1
chiral asymmetry across all three channels combined is currently unconditional;
per-channel purity (ruling out a vector-like partner within a channel) is not yet
externally established. Cheapest test: run the anomaly check the project already
has machinery for, but on the group that's actually derived (SU(3)×SU(2)_L×SU(2)_R,
including the Witten SU(2)_R global anomaly) instead of assuming B-L/Y.

### R2-6 [LOW-MEDIUM] — λ-dimensional-obstruction (Buckingham-Pi, G83-G86B/M104) is narrower than its framing suggests (compactification-physics lens)

The obstruction only rules out λ built purely from S³×S⁶ radii — it says nothing
about a standard string-scale constant λ~α′ (already in the project's own candidate
list, e.g. gaugino condensation λ~8π²/b₀). This is a framing/emphasis issue, not an
error — the project's null-results chain already correctly concluded "λ is a free
O(1) parameter," this just notes the "STRUCTURAL THEOREM" language over-sells what
was actually excluded. Also confirmed, positively: N_gen=3 does not secretly depend
on λ or ρ₆ (topological index vs. potential-minimization are cleanly separated) —
this is a finding *for* the project, not against it.

### R2-7 [PROCESS finding, not scientific] — Independent reproduction attempt was blocked by agent tooling, not by the project

The agent assigned to independently run `pytest tests/` was not given Bash access
in its tool configuration and correctly reported `BLOCKED-INFRASTRUCTURE` rather
than fabricating a result — this is the right behavior per the Substrate Gate, but
it means **no independent test-suite reproduction happened this round**. If a real
outside-reproduction pass matters before further promotion, it needs to be
re-run with an agent that has Bash/pytest access.

### R2-8 [Framing, from the skeptic] — Verdict on the headline claim as actually worded

Skeptic's explicit verdict: **WEAKENED**. The mathematical body survives adversarial
review at the conditional rung it explicitly claims (ind=1 rigorous; L4A/L4B
internally certified with external review correctly flagged as outstanding; L3b
honestly flagged as open, requiring external input). But the title *"Toward Three
Generations from the Geometry of S³×S⁶"* and the recurring phrase "N_gen=3 from the
geometry" oversell what the project's own results (E-L3B + G102, now reinforced by
R2-1's convergent finding) show: the geometry alone provably *cannot* produce the
three-ness without an external, non-geometric postulate. Suggested reframing
direction (skeptic's words): *"One generation from the geometry of S³×S⁶, three
generations conditional on external Spin(8) input."*

---

## What did NOT get shaken this round (positive/confirmed results)

- Core index arithmetic (`ind = Â·c₃/2 = 1`, per channel) is airtight — checked
  independently by 2 lenses, both re-derived it from Chern-Weil/Chern-Gauss-Bonnet
  rather than trusting the paper's statement, and found no error.
- E-L3B (E_v≅E_s≅E_c as G₂-equivariant bundles) and G102 (centralizer=0) are both
  correct as far as they go — all lenses agree, the only quarrel is with how the
  *implication* ("fully exhausted") is phrased (R2-2).
- N_gen=3's independence from λ/ρ₆ (topology vs. potential separation) — confirmed,
  not challenged.
- The project's own internal degeneracy theorem (no mass hierarchy from S⁶ alone,
  `preprint.tex` §sec:yukawa-deg) was checked by the phenomenology lens and found to
  already be stated more sharply than an external attacker could add to.
- Selection of S⁶ within the nearly-Kähler-6-manifold class is defended by two
  independent criteria (G₂ isometry + χ=2) and reads as a genuine one-of-four
  selection, not landscape cherry-picking — though the skeptic notes the *outer*
  choice of the NK6 class itself is harder to defend as bias-free (see R2-8).

---

## Recommendation for next step

R2-1 (no stated parent action) is the highest-value open item — it's cheap
(symbolic, no external dependency), decisive, and logically upstream of L3b. R2-2
and R2-5 are the cheapest wins (wording fixes + a machinery-reuse anomaly check).
The convergent ℤ₃-equivariant-index finding (R2 headline) suggests the F4/Spin(9)
route being pursued today should explicitly confront the "does triality act
nontrivially on S⁶ at all" question before investing further effort in conditions
2-5 of that route — three independent lenses now agree the answer is likely no.

Not yet done: Round 3 (cross-expert conflict beyond the convergences already found),
Round 5 (formal kill-table with cost/impact scoring), Round 6 (publication map).
Queued per the staged-execution plan.
