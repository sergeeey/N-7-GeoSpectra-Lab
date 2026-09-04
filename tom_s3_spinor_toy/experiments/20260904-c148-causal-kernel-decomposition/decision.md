# C148 — Decision

## The table (all inputs read from registered artifacts, not recomputed)

| construction | summands (`su(3)` types) | aggregate shape | `A` | `F` | `K` | `Δ_graded` | `Δ_geo` |
|---|---|---|---|---|---|---|---|
| round59 / T0 (`EVEN_IDX`) | `1 ⊕ 3̄` | `(2, 1)` | 1 | 1 | 1 | 0 | **0** |
| C139 (`m`) | `3 ⊕ 3̄` | `(1, 1)` | 0 | 0 | 0 | 0 | **0** |
| C141 (`m ⊕ 2·1`) | `(3⊕3̄)`, `1`, `1` | `(3, 3)` | 0 | 0 | 0 | 0 | **0** |
| T1 (`Σ` self-twist) | `(1⊕3̄)`, `(1⊕3)` | `(3, 3)` | 0 | 1 | 1 | **1** | **0** |

`A = max(0, dim_domain − dim_target)` · `F` = C141/C143 graded floor ·
`K` = observed kernel · `Δ_graded = F − A` · `Δ_geo = K − F`.

## Verdict: **PROMOTE** (accounting round, no new computation)

1. **`A ≤ F ≤ K` holds in all four cases** — the chain is well-ordered.
2. **`Δ_geo = 0` in all four.** No construction this project has ever built
   has a kernel exceeding what graded branching already forces. This is the
   quantitative form of what C141 found empirically and C143 proved for the
   `Hom`-dimension-1 case: in that regime the kernel is scalar-determined,
   so `Δ_geo = 0` is not merely observed here, it is *expected* — this table
   confirms the expectation across every case on record and gives it a
   number.
3. **`Δ_graded = 1` in exactly one row: T1** — with two precision caveats
   that a skeptic pass forced, both of which the first draft of this section
   got wrong:

   **(a) The nonzero row is T1, NOT C141.** C141's own row has
   `Δ_graded = 0`. T1 is a *comparison construction introduced inside*
   C141, not C141 itself. The first draft wrote "the sole nonzero `Δ`
   coincides with the most-corrected round", conflating the two objects.
   The accurate statement is narrower: C141 and T1 share the aggregate
   shape `(3,3)` but have *different* graded floors (`0` vs `1`), and
   C141's early drafts reasoned from the shared aggregate shape — which is
   exactly the inference the `Δ_graded` gap shows to be invalid.

   **(b) "`Δ_graded > 0` marks where aggregate reasoning is insufficient"
   is a definitional identity, not a discovery.** `Δ_graded := F − A` with
   `F ≥ A` always, so `Δ_graded > 0` *means* "the graded floor exceeds the
   aggregate one" — restating it as a "warning flag" dresses a definition
   as an empirical finding. The first draft did exactly that. What is
   genuinely empirical here is only the `n = 1` observation that the single
   row where this gap is nonzero is also the construction whose kernel two
   successive drafts inferred incorrectly from aggregate shape — suggestive,
   not a demonstrated predictor.

## Consequence for the research programme (supporting the user's stop-rule)

The user proposed: `Δ_geo = 0` **and** `dim Hom = 1` ⟹ do not invest in the
next heavy round. This table supplies the first half of that test for every
existing construction, and it is uniformly satisfied. Combined with C143
(Lemma 1: `Hom`-dim 1 ⟹ kernel scalar-determined), C146 (`Term1` Schur-
forced to zero), and C147 (`c ≠ 0` over the whole admissible connection
family), the position is now:

> **Empirically, here:** `Δ_geo = 0` in 4/4 constructions on record.
> **By citation, not by this round's own argument:** C143's Lemma 1 states
> that in the `Hom`-dimension-1 regime the kernel is scalar-determined, from
> which `Δ_geo = 0` would be *forced* rather than merely observed — but this
> round performs no computation and does not re-establish Lemma 1; it cites
> it. The strength of the "forced" reading is exactly the strength of C143,
> no more.
> **What this round does add:** each of three separate escape routes has now
> been closed by a different round — a different twist's branching (C141),
> a different connection inside the admissible family (C147), and a
> Kostant-style operator re-identification (C145) — so the `Δ_geo = 0`
> observation is not resting on a single mechanism.

So `kernel = 1` on its own carries no information beyond branching, in
every case this project has built. The observable worth chasing is
`Δ_geo > 0`, which by C143's Lemma 2 requires `Hom`-dimension `≥ 2` — the
regime C142 identified as currently unreachable (`OB14`, `BLOCKED-INTERNAL`).

## The relabelling — and a correction to this round's own first draft of it

The user's framing labelled the first level "topology" (`|ind D|`). This
round's first draft rejected that label outright, on the grounds that
`dim(domain) − dim(target)` on an `su(3)`-invariant sector is "a
Clebsch–Gordan difference, i.e. representation theory, not topology."

**That rejection was too strong, and is withdrawn.** Both the orchestrating
session (checking Landweber `math/0005056` §3, already read this session for
C144/C145) and an independent context-blind skeptic pass reached the same
correction: by **Bott's theorem** the index of a homogeneous differential
operator depends only on its domain and range, not on the operator, and by
**Frobenius reciprocity** it is *computed* as
`Σ_λ [V_λ](dim Hom_H(V_λ,M) − dim Hom_H(V_λ,N))`. So the `λ = 0` component
is exactly `dim(domain_inv) − dim(target_inv)` — i.e. **`A` IS the trivial-
isotype component of the equivariant index**, which is a genuine
(equivariant-)topological invariant that *also* happens to be computable by
branching. "Topological" and "computed by branching multiplicities" are not
opposed in the equivariant setting; that coincidence is the content of the
equivariant index theorem.

**What survives from the correction, and why the relabelling is still
used:** in *this project's computational pipeline* both `A` and `F` are
extracted from the same branching data, so presenting their difference as
"representation theory beyond topology" would suggest an independence of
sources that does not exist here. The levels are therefore labelled
`aggregate branching → graded branching → geometry`, which describes what
was actually computed, while recording that `A` legitimately doubles as the
`λ = 0` equivariant index.

**One genuine distinction that does survive:** `A` is the *equivariant*
index at `λ = 0`, not the Atiyah–Singer index of a twisted Dirac operator on
the `S⁶` bundle — different numbers. This project already has a registered
null result touching the latter (`ind(D⊗E) = 7`, not 3, for the
`S⁻⊗T^{1,0}S⁶` candidate). Conflating the two would be a real error, and is
named here so it is not made later.

## Cost and honesty about novelty

This round performed **no new computation**. Every number is read from
`results_c139.json` and `results_c141.json`, both already committed and
skeptic-reviewed. The contribution is (a) the relabelling correction, (b)
the observation that the sole nonzero `Δ` in the project's history
coincides with its most-corrected round, and (c) the assembled table as a
standing reference. If a future reader wants "what did C148 discover", the
honest answer is: it did not discover a new fact about the geometry, it
made an existing set of facts comparable and caught a framing error before
it entered the registry.

## Follow-up completed same day: the retroscan C141 explicitly deferred

C141's own ledger entry states that it *"DOES flag, **without acting on it**,
that the INTERPRETIVE weight placed on those prior results as evidence of
`D_S6`'s dynamics (as opposed to branching arithmetic) **may need
re-examination**."* C148 supplies exactly the tool for that re-examination
(`Δ_geo`), so the deferred item was carried out.

**Method:** enumerate every claim depending on `C2_ROUND59_KERNEL_DIM1`
(9 of them, via `awk` over the ledger) and check whether any *statement*
asserts dynamical significance that `Δ_geo = 0` would undercut.

**Result: CLEAN — nothing needs correcting.** Three independent reasons:

1. `C2` itself states only a computed number (`dim ker = 1 exactly`), with
   no dynamical claim attached.
2. `C4_NGEN3_HEADLINE` already carries `evidence_status: CONTESTED` and the
   explicit note *"NOT an established physical result per the project's own
   2026-07-17 correction"* — the guard was already in place.
3. `C21_G74B_CHIRALITY_SIGN` — the one dependent that does draw a physical
   conclusion (*"purely left-handed zero modes, matching observed SM
   chirality"*) — rests on **index-type** reasoning (`sign(ind(D⁺))` plus
   per-channel kernel dimensions). An index is *supposed* to be
   topological/representation-theoretic; that is C148's own central point.
   So this claim never asserted dynamical origin, and `Δ_geo = 0` does not
   undercut it.

**Why this is worth recording rather than leaving silent:** a retroscan that
finds nothing is easy to skip and expensive to re-do. The registry now shows
it was performed, when, by what method, and why each dependent survives —
so the next person to notice C141's deferred flag does not repeat it.

## Skeptic pass (Step 8a, context-blind: claim.md + this table only)

**Verdict: CONFIRMED-REAL on the arithmetic; WEAKENED on three framings.**
No fatal concern, kill criterion did not fire.

The skeptic verified **every cell of all four rows** against the two cited
JSON files, including the aggregate shapes this round did not itself
compute (`(3,3)` for C141 from `invariant_sector_dims.domain_ODD_x_W2 = 3`
/`target_EVEN_x_W2 = 3`, and for T1 from
`t0_t1_apples_to_apples_comparison.t1_domain = 3`/`t1_target = 3`), and
independently re-derived T1's graded floor from C141's own general formula
`domain − target = mult_W(3̄) − mult_W(3)` per summand: `max(0, 1−0) +
max(0, 0−1) = 1 + 0 = 1` ✓. It confirmed `A ≤ F ≤ K` in all four rows and
`Δ_geo = 0` throughout.

### Response Matrix (per FL Step 8a)

| Concern | Severity | Response |
|---|---|---|
| The relabelling's *stated justification* overreaches: an equivariant index computed by branching multiplicities is still a topological invariant (equivariant index theorem), so "this is not a topological index" is wrong even though the methodological point stands | scope, not fatal | **Accepted and fixed.** Section "The relabelling — and a correction to this round's own first draft of it" now withdraws the over-strong rejection, states Bott + Frobenius explicitly, and keeps only what survives: in *this pipeline* both `A` and `F` come from the same branching data. Independently reached by the orchestrating session (re-reading Landweber §3) before the skeptic report arrived — recorded as a convergent correction, not a solo catch. |
| "`Δ_graded > 0` marks where aggregate reasoning is insufficient" is definitional (`Δ_graded := F − A`, `F ≥ A` always), presented as an empirical warning flag | scope, not fatal | **Accepted and fixed.** Point 3(b) now states this is a definitional identity and that only the `n = 1` coincidence is empirical. |
| The narrative conflates C141 with T1: **C141's own row has `Δ_graded = 0`**; the nonzero row is T1, a comparison construction introduced *inside* C141 | scope, not fatal — but a real precision error | **Accepted and fixed.** Point 3(a) now states the distinction explicitly and rewrites the claim to the accurate, narrower version. This one was missed by the orchestrating session entirely and is a genuine skeptic catch. |
| `claim.md` says "an observation over four cases" while `decision.md` said "not an empirical regularity — it is forced"; the stronger reading leans on C143's Lemma 1, which this round cites but does not re-establish | scope, not fatal | **Accepted and fixed.** The programme-consequence block now separates *empirical here* (4/4) from *by citation* (C143's Lemma 1) from *what this round adds* (three independently-closed escape routes), and states plainly that the "forced" reading is exactly as strong as C143, no more. |
| Number-by-number verification, `A ≤ F ≤ K`, `Δ_geo = 0`, kill criterion | none found | No action. |

**True kill condition: NOT met.** PROMOTE stands for the accounting; the
three framing corrections above are incorporated rather than appended, and
the first-draft wordings they replace are described (not silently deleted)
per this project's Hindsight Distortion Gap Heuristic.
