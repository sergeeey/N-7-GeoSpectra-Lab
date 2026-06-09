# P13 V Branch Detailed Chronology And Handoff

## 1. Purpose

This document records the full project chronology for the Part 3 / V-branch
work in the repo. It is the long-form version of the earlier short handoff.

The goal is not to prove Tom Lawrence's full theory. The goal is to keep a
frozen, auditable record of what was checked, what was repaired, what was
verified, and what remains open.

## 2. One-Line Status

```text
We built a strong research scaffold, verified its pattern and Hermiticity,
computed one explicit S^3 low-mode integral, and still did not fix lambda.
```

## 3. Current Bottom Line

What is established:
- the matrix-element pattern is real and externally supported
- the scaffold is Hermitian
- Ben Achour `E_i / E'_i` geometry is source-fixed at low mode
- one explicit `S^3` matrix element integral has been computed

What is not established:
- a physical `V` operator
- physical `V`-selection rules
- Standard Model reproduction
- fermion-generation claims
- runtime safety

The blocker is still the same:

```text
lambda is free.
```

## 4. Chronology

### 4.1 Early Part 3 reading

The project started from the Part 3 transcript / summary:
- fermions are discussed as compact-space harmonics
- `S^3` is treated with a Hopf/Lawrence chart
- `S^6` and `SO(6) ~ SU(4)` appear later in the story
- a 32-component fermion organization is discussed conceptually
- the old scalar-separable Lawrence path reaches a `cot(2 alpha)` obstruction

At this stage the main uncertainty was whether the old ansatz could be
salvaged or whether the project needed a replacement basis.

### 4.2 Lawrence ansatz diagnostics

The `cot(2 alpha)` issue was investigated and recorded as an unresolved
obstruction in the old path.

The important repo conclusion is:
- `cot(2 alpha)` is not treated as a solved physical derivation
- the old Lawrence scalar-separable route is not promoted
- the safer path is to replace it with standard `S^3` spinor harmonics and a
  repaired basis

This is the point where the project stopped trying to rescue the original
scalar-separable ansatz and moved to a cleaner scaffold.

### 4.3 Replacement basis and oracle path

The repo then moved to:
- standard `S^3` spinor harmonics
- repaired spinor-state basis
- Wigner / Clebsch-Gordan oracle matching
- Ben Achour one-form geometry
- explicit low-mode checks

This is the branch that survived testing.

### 4.4 P11 and P12

`P11` established that an external Wigner/CG oracle matches the frozen
matrix-element scaffold.

`P12` established that the match survives robustness checks on the tested
axes:
- basis ordering
- phase convention
- normalization
- low `k_max` extension
- Hermiticity

This is important because it means the scaffold is not a local artifact of one
arbitrary convention.

### 4.5 P13A to P13G

The P13 chain then froze the candidate V-like stack carefully:
- P13A: ansatz and conventions
- P13A1: executable Ben Achour low-mode `E_i / E'_i`
- P13B0: state / measure / selection-rule repair
- P13B1: repaired spinor basis and selection-rule repair
- P13C: exact Ben Achour source identities
- P13D: coefficient normalization and Hermiticity audit
- P13E: reduced coefficient scale no-go
- P13F: final V-operator no-go record
- P13G: handoff / limitations package

The consistent outcome across those gates was:
- source identities fixed
- convention stack fixed
- Hermiticity preserved
- external scaffold compatibility preserved
- exact reduced scale not fixed
- `lambda` remains free

### 4.6 P13H

P13H did one explicit low-mode `S^3` integral using the repaired basis, the
Ben Achour low-mode layer, and the Lawrence/Hopf measure.

The result was:

```text
<psi_i | V | psi_j> = (16*pi**2*rho**3/15) * lambda
```

So the integral gave a real coefficient, but it still multiplied `lambda`.
That means the integral confirms the scaffold and the low-mode normalization
path, but it does not close the physical coupling scale.

## 5. The 32 Directions

The list below is the clean project-level reading of the 32 directions you
summarized from Part 3.

| # | Direction | Current status | Notes |
|---:|---|---|---|
| 1 | Part 3 shifts focus toward fermions | Fixed as context | This is the working framing for the branch. |
| 2 | One fermion generation as a 32-component spinor | Partial scaffold | Representation-level scaffold exists; physical claim is not proven. |
| 3 | Generators via Kronecker products | Scaffold | Algebraic layer exists, not promoted to physical proof. |
| 4 | Fermions related to compact-space harmonics | Scaffold / hypothesis | Working path, not a final claim. |
| 5 | Geometry like `S^4 x S^6` | Open | Not closed in the repo branch. |
| 6 | `S^3` associated with `SO(4)` | Fixed as geometry scaffold | Standard geometry layer. |
| 7 | `S^6` associated with `SO(7)/SO(6)` and `SO(6) ~ SU(4)` | Scaffold | Group-theory scaffold, not a SM proof. |
| 8 | S^3 points via Pauli / Clifford | Fixed | Established convention layer. |
| 9 | Pauli-form expression | Fixed | Recorded in the algebra scaffold. |
| 10 | Gamma-matrix expression | Fixed | Recorded in the Clifford / spinor scaffold. |
| 11 | S^3 coordinates | Fixed | Hopf/Lawrence chart recorded. |
| 12 | Dragging action shifts `theta` and `theta_tilde` | Scaffold | Part of the coordinate action picture. |
| 13 | `partial_theta + partial_theta_tilde` and `partial_theta - partial_theta_tilde` appear | Fixed as observed structure | Present in the convention layers. |
| 14 | Phase dependence `exp(i[i_L(...)+i_R(...)])` | Fixed as convention | Used in the Wigner / spinor layers. |
| 15 | `cot(2 alpha)` issue at non-Cartan part | Open in old path | Not solved as a rescue of the old Lawrence ansatz. |
| 16 | Separable ansatz `A(alpha) e^{...}` | Blocked / not promoted | The old scalar-separable route is not the chosen endpoint. |
| 17 | `O(4)`, parity, global-coordinate issues | Diagnostic only | Recorded as part of the warning layer. |
| 18 | Large-`rho` rotations resemble translations | Heuristic | Physics intuition only, not a proof. |
| 19 | `S^6` harmonic analysis not fully developed | Open | Still a missing branch. |
| 20 | `SU(3)` appears through `SU(4)` / `SO(6)` | Scaffold | Group connection recorded, not promoted. |
| 21 | Higgs / Forgacs-Manton connection | Mentioned only | Not established. |
| 22 | Part 3 ends with open points | Fixed observation | Correctly reflected in the handoff. |
| 23 | `S^3 x S^6` tensor scaffold | Scaffold | Present as a bridge, not a physical claim. |
| 24 | V matrix scaffold | Scaffold | Built and checked. |
| 25 | External Wigner/CG oracle | Fixed | Passed and matched the scaffold. |
| 26 | Robustness audit | Fixed | Passed on tested axes. |
| 27 | Known limitations record | Fixed | Stored in repo. |
| 28 | `V`-operator ansatz registry | Fixed as registry only | Not a promotion gate. |
| 29 | Ben Achour one-form source block | Fixed at low mode | Source-supported geometry layer exists. |
| 30 | Spinor-state repair | Fixed | Invalid spinor tuple removed from spinor tests. |
| 31 | Toy-gradient reduced element formula | Fixed as toy model | Useful, but not the physical operator. |
| 32 | Exact Ben Achour `E_i / E'_i` mode formula | Fixed as source identities | Exact source formula exists; normalization is still not a physical proof. |

## 6. What Was Actually Solved

This branch solved the following engineering / research questions:

- the old scalar-separable Lawrence path is not the active path
- the repaired spinor basis is consistent enough for the project scaffold
- the external oracle agrees with the pattern
- the pattern survives robustness testing
- the Ben Achour low-mode geometry is executable
- the exact low-mode source identities are available
- the exact low-mode integral can be computed explicitly

## 7. What Was Not Solved

The following remain open or deliberately unpromoted:

- the physical `V` operator
- the physical selection rules
- the absolute coupling scale
- `lambda` fixation from `S^3` alone
- `S^6` harmonic completion
- full Part 3 physical interpretation
- Standard Model claims
- fermion-generation claims

## 8. Why `cot(2 alpha)` Is Not A Closed Victory

The repo record does not say that the old Lawrence ansatz was fully rescued.
It says:

- the `cot(2 alpha)` issue was real in the old path
- the old path was not promoted
- the project moved to a different, safer scaffold
- the safe scaffold uses repaired spinor harmonics and Ben Achour one-forms

So the honest interpretation is:

```text
old ansatz = unresolved
replacement scaffold = working
```

## 9. Why The Branch Stops At `lambda`

The explicit low-mode integral shows that the operator matrix element reduces to
a coefficient times `lambda`.

That means the geometry and normalization work are good enough to recover the
shape of the matrix element, but not enough to fix its physical scale.

In plain language:

```text
the form is solved
the scale is not
```

## 10. Repository State

This branch is now frozen as a research result:

```text
scaffold = built
pattern = verified
Hermiticity = preserved
exact low-mode integral = computed
lambda = free
physical V-operator = not promoted
```

## 11. Current Fence

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

## 12. Next Safe Step

There is no next V-derivation gate on this branch.

The only valid continuations are:

1. a new external physical principle that actually fixes `lambda`
2. a different branch, such as a larger `S^3 x S^6` analysis
3. a final handoff / paper-style limitations package

## 13. Final Plain-Language Summary

```text
We solved the scaffold and the pattern.
We did not solve the absolute physical coupling.
So the branch is complete as a research handoff, but not as a physical proof.
```

## 14. Tom-Facing Wording

This is the softer wording to use if Tom asks for a short update. It keeps the
technical status accurate without using the internal fence language:

```text
In my S3-only reconstruction, I recovered a consistent low-mode scaffold and
one explicit matrix-element integral. The pattern and Hermiticity checks are
internally consistent, but I could not fix lambda from S3 alone.
If lambda is expected to be fixed later, or if I am missing a convention,
please point me to the missing source or normalization rule.
```

Do not send the long registry or the internal no-go language unless explicitly
asked for a technical handoff.
