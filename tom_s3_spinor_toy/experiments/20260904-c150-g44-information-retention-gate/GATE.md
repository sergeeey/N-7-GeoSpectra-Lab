# G44 Information-Retention Gate — an operational filter, NOT a new theorem

**Created:** 2026-09-04 (autonomous session).
**Type:** SYNTHESIS / decision procedure. **No new mathematics.** Every fact
below is already registered; this file's only contribution is assembling
three scattered results into one filter that can be applied before building
anything.

**Numbering note:** the user's proposed ordering had `C149` = G44 theorem and
`C150` = Hom-multiplicity atlas. `C149` was instead used for a debt-audit
finding (OB11(ii) transport well-posedness), so this gate takes `C150`.
The atlas, if built, needs a new number.

---

## Why this is a gate and not a theorem — read first

The user proposed proving a functorial information-loss theorem: if
`R : Rep(Spin(8)) → Rep(G₂)` is restriction and `F = F̃ ∘ R`, then
`F(8_v) = F(8_s) = F(8_c)`.

**A novelty check found that content already registered, in a stronger form.**
Stating it as a "new theorem" would have been a restatement — the exact
failure mode this project tiered `[RESTATEMENT]` once before (C136). What
follows is therefore the *filter*, with each row pointing at the round that
already established it.

---

## The registered facts this gate rests on

### 1. The collapse is a measured filtration, not a binary fact — **C72**

`Hom(channel_i, channel_j)` shrinks monotonically as the equivariance
algebra grows:

| algebra | `dim Hom(channel_i, channel_j)` | meaning |
|---|---|---|
| `su(3)` (dim 8) | **6** | channels maximally identified |
| `g₂` (dim 14) | **2** | channels still isomorphic — matches Schur exactly, given `8_v│_{g₂} = 1⊕7` |
| `so(8)` (dim 28) | **0** | channels genuinely inequivalent |

C72 additionally constructed **explicit invertible `g₂`-equivariant
isomorphisms for all three channel pairs** (det 0.0129/0.0018/0.0047,
intertwining residual 5.0e-16 to 7.0e-16 across all 14 `g₂` generators).

**This is what makes the functorial statement a one-liner:** isomorphic
objects take equal values under *any* functor. Given an explicit `g₂`-
equivariant isomorphism `8_v ≅ 8_s ≅ 8_c`, every `g₂`-functorial observable
is automatically blind. No separate proof is needed.

### 2. The information genuinely survives at `so(8)` — **C63**

C63 built the "coincidental" `su(3)`-level identification `Φ : vec → sp`
explicitly and tested it: it intertwines `su(3)` essentially exactly
(residual 5.13e-16) but **fails against a generic `so(8)` element by order 1**
(residual 3.22, element norm 2.71). So the apparent redundancy is confined
to the restricted view and does not survive contact with `Spin(8)`.

### 3. The morphism/multilinear escape route was already tried — **C62**

The obvious red-team objection is that distinction might vanish at the
*object* level while surviving in morphism-level or monoidal data (the
triality trilinear form). **C62 took exactly that route** — Baez's octonion
trilinear-covariance construction, solving `a(x)·y + x·b(y) = c(x·y)` — and
found that for **all 8 `su(3)` generators** the solution is `(a, a, a)`:
the identical matrix on all three channels, deviation 1.6e-15. Negative
control (a generic non-`g₂` `so(8)` element) gives deviations 4.53 and 2.91.

**So the trilinear structure collapses together with the objects.** Object-
level and (this instance of) morphism-level information loss coincide here.

---

## THE GATE — apply before building any generation mechanism

> **Question:** does the proposed generation observable factor through
> `g₂`-restricted representation data?

```
Does the observable use ONLY data that survives Spin(8) -> G2 restriction
of a SINGLE channel (its isomorphism class, its g2-module structure,
or -- per C62 -- its trilinear covariance relations)?

    YES  -> CLOSED without computation. It cannot distinguish 8_v/8_s/8_c.
            Cite C72 (explicit g2-equivariant isomorphisms exist) and,
            for the trilinear variant, C62.

    NO   -> The proposal is admissible for testing. State explicitly WHICH
            datum it uses that does NOT factor through the restriction,
            and how that datum is realized in this project's own content.

    UNCLEAR -> Treat as YES until the "which datum" question is answered.
               C63 is the template for what a real answer looks like:
               exhibit something that breaks at order 1 against a generic
               so(8) element, not merely something that looks different.
```

**What the gate does NOT license.** Passing it is necessary, not
sufficient — the proposal still has to be built and tested. Failing it is
decisive: no computation is needed to reject.

---

## Scope, stated so the gate is not over-applied

1. **This is about `Spin(8) → G₂` restriction specifically.** It says
   nothing about mechanisms that never route triality data through `G₂` at
   all.
2. **"Morphism-level is closed" rests on ONE instance (C62's trilinear
   covariance), not on a general categorical argument.** A different
   morphism-level or extension-level datum could in principle escape; the
   gate's `NO` branch exists precisely for that case, and such a proposal
   must be evaluated on its merits, not waved through or waved away.
3. **The `so(8)`-level survival (C63) is about the algebra, not about
   physical realization.** Whether this project's actual compactification
   realizes the full `Spin(8)` action is `OB11(iii)`/`OB4`'s still-open
   question (`C_G67C3_THIRD_CHANNEL`) — the gate presupposes nothing about
   it.
4. **No claim that `N_gen=3` is closed or opened by this.** The gate filters
   *mechanisms*, and leaves the headline's `CONDITIONAL` status untouched.

---

## The constructive reading (why this is not only a no-go)

The gate's `NO` branch is the useful half. It converts G44 from a wall into
a specification:

> A viable generation mechanism must use a datum that does **not**
> factor through `Spin(8) → G₂` restriction — and must say which one.

C63 already shows such data exist at the `so(8)` level. What this project
lacks is not the existence of distinguishing information, but a construction
in which that information is physically realized — which is exactly
`OB4`/`OB11(iii)`, and exactly the reason `C_G67C3_THIRD_CHANNEL` is a
postulate rather than a derivation.
