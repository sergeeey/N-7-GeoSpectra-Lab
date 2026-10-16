# C188 Decision — PROMOTE. The quaternion-native construction works; C187's did not, and this shows why.

**Date:** 2026-09-09
**Verdict:** **PROMOTE** — the S³ Euler-angle Dirac operator, rebuilt directly
from the quaternion right-multiplication generators (no vielbein, no Cartan
connection), reproduces the known spectrum exactly at `k=0,1,2,3`. `16 of 16`
checks pass. Exact symbolic arithmetic (rational, half-integer, and
trigonometric identities), cross-checked at high numeric precision where
symbolic simplification proved unreliable.

All numbers trace to `c188_quaternion_native_dirac.py`, `run_output.txt`, and
`derive_mn_k23.py` (provenance script for the pre-registered candidates).

---

## 1. What was open, and what this closes

`C187b`'s `decision.md` §4c named the concrete next step: *"Rebuild `D` on
`S³` in Euler angles by starting from the quaternion structure directly …
rather than an independently-chosen geometric vielbein — this guarantees
agreement with `C184`/`C186`'s `D₀` by construction."* This round executes
exactly that.

| | `C187` (vielbein + Cartan connection) | `C188` (this round) |
|---|---|---|
| construction | independently chosen frame, connection solved from Cartan's equation | `D = -i Σₐ σₐ Xₐᴿ`, `Xₐᴿ` expressed in `(θ,φ,ψ)` via the embedding's Jacobian |
| internal checks | `9/9` passed (frame reproduces metric, connection zero-residual) | `Xₐᴿ` confirmed tangent + matches closed form, `< 1e-30` |
| matches `C184`/`C186`? | **No** — checked across 144 sign/pairing combinations, zero matches | **Yes** — `4/4` levels, exact |

**Why this one is guaranteed to agree, not merely checked to:** `Xₐᴿ` is not a
new object — it is literally the same right-multiplication generator used
throughout this project since `C184`. Expressing it in new coordinates via
the chain rule is a change of variables, not an independent construction.
`D = -i Σₐ σₐ Xₐᴿ` built from it is therefore the *same operator* as `D₀`,
re-coordinatized — the verification in section C confirms the chain rule was
applied correctly, not that two independent constructions happen to agree.

## 2. The generators, confirmed

Solved via least-squares against the embedding's own Jacobian (the same
technique `C187b` used to derive the `(m,n)` periodicity), verified
numerically to `< 1e-30` against a stated closed form — not assumed correct
because they look plausible:

```
X_0^R = 2 d/dpsi
X_1^R = 2 cos(psi) d/dtheta + 2 sin(psi)/sin(theta) d/dphi - 2 sin(psi)/tan(theta) d/dpsi
X_2^R = -2 sin(psi) d/dtheta + 2 cos(psi)/sin(theta) d/dphi - 2 cos(psi)/tan(theta) d/dpsi
```

## 3. The spectrum, confirmed at four levels

Candidates were **derived**, not guessed by extending the `k=1` pattern —
`derive_mn_k23.py` independently re-ran the i-axis Rosetta-stone technique at
each `k` and read off the exact `(m,n,F,G)`:

```
k=0  (m,n)=(0,0)      F=-1              G=1              lambda=0
k=1  (m,n)=(1/2,1/2)  F=-cos(th/2)      G=+cos(th/2)      lambda=-1
k=2  (m,n)=(1,1)      F=-cos(th/2)^2    G=+cos(th/2)^2    lambda=-2
k=3  (m,n)=(3/2,3/2)  F=-cos(th/2)^3    G=+cos(th/2)^3    lambda=-3
```

A clean, closed family: `(m,n)=(k/2,k/2)`, `F=-cos(θ/2)ᵏ`, `G=+cos(θ/2)ᵏ`,
`λ=-k`. All four confirmed by direct application of `D` to the candidate and
high-precision numeric evaluation at several random `(θ,φ,ψ)` — not a single
lucky point.

**This is the exact candidate `C187` failed on** (`(m,n)=(-1/2,1/2)` at
`k=1` — the mirror state under `m↔-m`, `F↔-G`, same physics). `C187`'s
operator gave a non-constant ratio there under all 144 tested conventions.
This construction gives exactly `-1`, everywhere tested.

## 4. Floor–Ceiling (Step 4a), with numbers

The metric is **how much the ratio `Dψ/ψ` varies across `(θ,φ,ψ)`** — a
genuine eigenfunction gives a constant; anything else gives a ratio that
moves with the point. Measured at `k=2` (5 random `(θ,φ,ψ)` points, 30-digit
precision):

| | construction | spread of `Re(Dψ/ψ)` across 5 random points |
|---|---|---|
| **floor** | mechanism absent: apply `D` to a *generic* function of the same `(m,n)=(1,1)` shape but the WRONG radial part (`F=sin(θ/2)²`, `G=cos(θ/2)²` instead of the derived `F=-cos(θ/2)²`) | **13.54** (values ranged `-1.67` to `11.87` — not remotely constant) |
| **ceiling** | the best any eigenfunction claim could do: a ratio that is exactly, identically constant | **0** (by definition — zero spread is the only way a ratio is genuinely constant) |
| **observed** | the derived candidate, `F=-cos(θ/2)²`, `G=+cos(θ/2)²` | **0.0** — every one of 5 points gave `-2.000...0` to 30 digits, imaginary part `~1e-35` (floating-point noise, not a real deviation) |

```
efficiency = (floor - observed) / (floor - ceiling) = (13.54 - 0.0) / (13.54 - 0) = 1.0
```

**`efficiency = 1.0`, at the ceiling exactly.** The floor is not degenerate
(`13.54 ≫ 0`, so the criterion has real room to fail in) and the observed
result sits exactly at the ceiling, not partway — this is the same
qualitative reading `C187`'s own construction would have needed to reach and
did not (its ratios were non-constant across all 144 tested conventions,
i.e. floor-like, not ceiling-like).

## 5. Section D — a real limitation, recorded rather than hidden

The half-angle reduction technique (`C185`, generalised in `C187`) does
**not** transfer to this construction. `X₁ᴿ, X₂ᴿ`'s own `cos(ψ)`, `sin(ψ)`
prefactors survive division by the plane-wave phase, leaving an explicit
residual `ψ`-dependence in the reduced radial equations. A first attempt
(`k=0`, `N=0`) completed (kernel dim `2`, matching the known multiplicity);
`k=1..3` were killed after hanging for several minutes — not slow-but-correct,
a genuine combinatorial blow-up from sympy computing exact rank over a field
with `cos(ψ), sin(ψ)` as extra parameters rather than pure rationals.

**This is not a gap in claim (b)'s closure** — section C's direct evaluation
already confirms the operator exactly, independent of the reduction
technique. It is a separate, genuine finding about which construction
choices are compatible with the half-angle speed trick, recorded because a
future round reaching for that trick on a quaternion-native construction
should not have to rediscover this.

## 6. What this does NOT establish

- **Does not extend beyond `k=3`.** Verified at four levels; continuation is
  inference from `C184`'s independently-established general theorem, not
  computed here for arbitrary `k`.
- **Does not derive the `+(k+2)` branch.** Only the `-k` extreme state was
  checked; the other branch was already established by `C184`/`C186`.
- **Does not diagnose `C187`'s specific bug.** This round bypasses the
  vielbein/connection approach entirely rather than debugging it further.
- **Does not restore the half-angle speed trick** for this construction —
  see §5.

## 7. Reproduction

```
cd experiments/20260909-c188-s3-euler-quaternion-native-dirac
python c188_quaternion_native_dirac.py
```

`16/16`. `ruff check` and `ruff format`: clean.
