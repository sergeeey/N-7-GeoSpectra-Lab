# C147 — Decision

## Result (`c147_zero_locus.py`)

```
Term1 at T1 = 0j        Term1 at T2 = 0j          (C146's prediction, confirmed)

real 2x2 matrix of (alpha,beta) -> alpha*c1 + beta*c2:
    [[ 0.8918535942, -0.7334374546],
     [ 0.7334374546,  0.8918535942]]
    det             = 1.333333333333        (= 4/3)
    singular values = [1.15470054, 1.15470054]
    condition number= 1.000000              (an EXACT similarity)

|c1| = |c2| = 1.154700538379 = 2*sqrt(3)/3
Re(c1 * conj(c2)) = 0.000e+00
c2/c1 = 1.0000000000000000j                  (exactly i, to 1e-16)

NOMIZU's own coordinates: (alpha,beta) = (-0.879080, 0.476674)
predicted c(NOMIZU) = -1.1336213214396014 - 0.2196270313756163j
|predicted| = 1.1547005384  ==  C139's own registered |c_exact| = 2*sqrt(3)/3
```

## Verdict: **PROMOTE — the robustness (no-go) branch.**

`c_W(∇) = 0` **only** at `∇ = 0`, over the entire 2-dimensional admissible
family — not merely at C139's 13 sampled angles. C139's `kernel = 0` is
therefore a **theorem over the family**, not a scan result.

**Why the answer is this clean.** The real 2×2 matrix is not merely
nonsingular — it is an exact similarity (condition number `1.000000`, both
singular values equal, `c₂ = i·c₁`). So

```
c(α, β) = c₁ · (α + iβ),     |c(α,β)| = (2√3/3) · sqrt(α² + β²)
```

i.e. `c` is **`C`-linear (holomorphic)** in the natural complex coordinate
`α+iβ` on the torsion family. A `C`-linear map `C → C` with nonzero
coefficient has zero locus exactly `{0}` — there is no room for a
zero-mode-creating direction anywhere in the family.

This also **explains** (rather than re-observes) C139's own numerical
finding that `|c(θ)|` is constant on the unit circle: constancy is exactly
the statement that the map is a similarity, which the computation here
confirms structurally (`|c₁|=|c₂|` and `Re(c₁c̄₂)=0`), not by sampling.

**The two-evaluation upgrade.** C139 needed 13 samples and still could not
close the gap its own comment identified. Here, C146's theorem (`Term1 ≡ 0`,
Schur-forced) collapses `c` to the manifestly `R`-linear `Term2`, so TWO
evaluations at basis directions determine the entire continuum. This is the
methodological content worth carrying forward: **when an operator's
restriction to an invariant sector is linear in a parameter, sample the
basis, not the circle.**

## Which of the user's two hoped-for outcomes this is

The user pre-registered both branches as valuable:
- *"If `c(α,β) ≠ 0` on the whole admissible space, this is a theorem-level
  robustness result."* ← **this is what happened.**
- *"If there exists a locus `c(α,β)=0`, you suddenly get a geometrically
  controlled appearance of a zero mode... a genuine dynamical mechanism."*
  ← **did not happen; this route is closed inside this family.**

So the "geometrically tunable zero mode" hoped for as a dynamical mechanism
does **not** exist within C73b's admissible equivariant-torsion family for
the `m` twist. Combined with C146 (Term1 forced to zero) and C141 (kernel =
graded floor in all four constructions tested), the picture is now: for this
whole class, **neither representation theory nor the connection geometry
inside the admissible family supplies a `Δ_dyn > 0`.**

## Kill Analysis (what this closes, what survives)

**Closed:** the specific hope that varying the connection inside C73b's
certified admissible family could tune `c` to zero and thereby create a
zero mode for the `m`-twist. It cannot — proven over the continuum.

**NOT closed (explicitly):**
- Connection families OUTSIDE `Hom_{su(3)}(m,Λ²m)` (non-equivariant
  connections; or the admissible family of a DIFFERENT twist bundle).
- Twist bundles other than `m` — the method transfers, the coefficient does
  not.
- C142's `W_cand` (operator-level Hom-dimension ≥ 2) — a different object
  from this round's connection-space dimension 2; the two must not be
  conflated (named here because the coincidence of the number "2" invites
  exactly that confusion).
- The `Δ_geo > 0` search the user framed as the real target — this round
  removes one candidate route to it, and does so decisively, which is what
  makes the remaining routes worth stating precisely.

## Skeptic pass (Step 8a, context-blind: claim.md + script only)

**Verdict: CONFIRMED-REAL** on the headline no-go (Claim 2). No fatal
concern. The kill criterion did not fire (`det = 1.333` sits ~15 orders of
magnitude above the float64 noise floor).

The skeptic (no Bash in that environment) verified by reading the code
chain that (a) the R-linearity premise is sound — `build_twisted_dirac_np`
is manifestly linear in both connection arguments, `spin_lift` and
`rho_vector` are linear, and the sandwich by CONSTANT invariant vectors
preserves linearity, so no cross-term can exist; (b) the invariant sectors
are genuinely connection-independent (built from `ADNU` only, never from
`NOMIZU`/torsion); (c) the decisive quantities are phase-invariant — under
independent phase choices on the two 1-dim invariants, `c₁,c₂` rotate by
the SAME phase, so `det(M)` is *exactly* invariant (not merely its
vanishing) and `c₂/c₁` is invariant outright.

Two scope caveats were raised, **both now closed by `c147b`** rather than
merely documented:

| Concern | Skeptic severity | Response |
|---|---|---|
| Claim 3's "similarity / `c₂=i·c₁` / C-linear" is basis-invariant only under `SO(2)`, not general `GL(2,R)`; the rep-theory reason (`m=3⊕3̄` giving the family a natural complex structure) was named as plausible but NOT verified | scope (headline unaffected) | **Closed, not just documented.** `c147b` identifies the complex structure explicitly as the **nearly-Kähler `J`** fixed by AHL2023's own eq.(5) pairing (`Je₁=e₂`, etc. — exactly known, not fitted), builds `T_B := NOMIZU∘J` from NOMIZU's own exact data, and confirms `T_B` lies in C73b's family (residual 2.8e-16) and is independent of NOMIZU. In the family's own coordinates, `J` acts as an exact 90° rotation: `(-0.879080, 0.476674) → (-0.476674, -0.879080)`. So the complex structure is a **named geometric object**, not an SVD artifact. |
| "exactly"/"theorem" language applied to float64 values; sympy machinery was available (C139 uses it) and was not used | language/scope | **Closed.** `c147b` recomputes both coefficients in exact sympy: `c(NOMIZU) = -2√3/3` (reproducing C139's own registered exact value) and `c(NOMIZU∘J) = -2√3·i/3`, giving **`ratio = I` exactly** — symbolic, not float64. The similarity property is therefore now an exact statement. |
| Linearity premise, invariant-sector independence, phase invariance, scope of "does NOT mean" | none found | No action. |

**True kill condition: NOT met.** PROMOTE stands, and Claim 3 is upgraded
from a numerical observation in one basis to an exact statement attached to
the nearly-Kähler structure.

## Post-skeptic strengthening (`c147b_exact_and_complex_structure.py`)

```
T_B := NOMIZU o J  (J = nearly-Kahler, from AHL2023 eq.(5), exactly known)
  in C73b's admissible family        : True  (residual 2.776e-16)
  independent of NOMIZU              : True  (coordinate det = 1.000000)
  c(NOMIZU)        = -2*sqrt(3)/3        [EXACT sympy]
  c(NOMIZU o J)    = -2*sqrt(3)*I/3      [EXACT sympy]
  c(T_B)/c(NOMIZU) = I                   [EXACT, not 0.9999999999999997j]
```

**One honest residual, labelled not hidden:** the membership bridge (is
`T_B` in C73b's family?) is still NUMERICAL (residual 2.8e-16), because
C73b's family basis itself only exists numerically (SVD nullspace). Making
that leg exact would require re-deriving the whole equivariance nullspace
in sympy — deliberately not attempted here, and named as the one remaining
non-exact link in an otherwise exact chain.
