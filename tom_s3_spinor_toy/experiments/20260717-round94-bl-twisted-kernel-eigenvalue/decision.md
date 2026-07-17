# Round94 (E24) — Decision

**Date:** 2026-07-17
**Verdict:** **PASS, with an explicit, load-bearing caveat that is directly
addressed, not merely disclosed** — round59's twisted-kernel vector IS a
`B-L` eigenvector, eigenvalue `B-L = 0`. A genuine `su(3)⊕u(1)`-vs-`so(6)`
incompatibility exists in this project's own machinery exactly where G98
said it would, and is freshly re-confirmed here on the operator that
actually matters (`BL_64` vs the full twisted Dirac operator `D_full`, not
just `BmL` vs raw `so(6)` generators on the untwisted 8-dim space) — but it
is shown, by direct computation, NOT to touch this specific claim. See
"Verdict-selection note" below for why this is called PASS rather than
BLOCKED, and why that call is defensible rather than forced.

**Go/no-go:** This closes round93 (E23)'s sole remaining blocker for the
S⁶-side hypercharge program: `B-L` is now a well-defined operator on the
twisted kernel's own ambient space, not merely a post-hoc label on a
different (untwisted, System-B) space. `B-L = 0` for the physical
`dim ker(D_{S6,twisted})=1` zero mode.

---

## Bottom line, stated plainly first

1. **`Σ = Λ•(ℂ³)`** (`experiments/20260708-dolan-casimir-g2su3/
   g2su3_explicit_clifford.py:24-32`, dolan-casimir/round59's 8-dim fibre)
   **is the same vector space as G15's 8-dim S⁶ weight space**
   (`experiments/20260619-g15-hypercharge/g15_hypercharge.py`), under an
   explicit degree/Hamming-weight-preserving bijection — verified entrywise
   (script Part 1b, all 8 indices), not merely argued from matching
   docstrings. `BmL` (G15's actual matrix, imported unchanged) depends ONLY
   on Hamming weight (`g15_hypercharge.py` T2, re-spot-checked here,
   `bmL_g15_is_pure_hamming_weight_formula=True`), and `Σ`'s exterior degree
   plays the identical role (`Σ` grade sizes `{0:1, 1:3, 2:3, 3:1}` = G14's
   `1⊕3⊕3̄⊕1`, matching `g15_hypercharge.py:3`'s own framing) — so the
   specific bijection chosen (`g15_index_to_subset`, script lines 71-80) is
   one legitimate representative of a whole family that all give the same
   answer, not an arbitrary forcing.
2. **round59's physical kernel vector — reconstructed here fresh via
   `D_full`, not merely copied — is an exact `BL_64` eigenvector, eigenvalue
   `0`.** `BL_64 = leibniz64(BL_sigma)` (script Part 2), where `leibniz64`
   is `round59_route_b_consistency.py:91-106`'s own function, imported
   unchanged and fed `BmL`'s degree matrix instead of an `su(3)` generator —
   the identical additive/Leibniz pattern this project already uses, not a
   new construction. `v_a`, `v_b` (round59's own SU(3)-invariant domain
   basis, `round59_route_b_consistency.py:219-220`, reconstructed here with
   the exact coefficient literal) are **each individually** `BL_64`
   eigenvectors with eigenvalue **0** — not merely "some combination of
   them is" — and `w` (the target invariant, line 221) has eigenvalue `-2`.
   The physical kernel vector `k = -√3·u₁ + u₂` (recomputed here fresh via
   imported `D_full`/`herm`, reproducing round59's own cited `a=-1`,
   `b=-√3` independently, `a_b_match_round59_decision_md=True`, and
   confirmed `D_full(k)=0` exactly) is therefore automatically a `BL_64`
   eigenvector too — **eigenvalue `B-L=0`.**
3. **The risk-lens incompatibility is real, freshly re-confirmed on the
   operator that matters, and shown not to threaten this claim.** G98
   (`experiments/20260701-g98-bl-isometry-holonomy/decision.md`) found
   `BmL` commutes with the 9-dim `su(3)⊕u(1)` subalgebra of `so(6)` but not
   the full 15-dim algebra (raw generators on the UNTWISTED 8-dim `Σ`).
   This experiment asks the sharper, more relevant question — does `BL_64`
   (the Leibniz lift) commute with `D_full` (the actual twisted Dirac
   operator, built from the Levi-Civita/Nomizu-map torsion term,
   `preprint.tex:816-819`)? **No** — confirmed two independent ways: (a) a
   direct commutator computation on a fresh probe vector (`y1⊗1`,
   `[BL_64,D_full]≠0`, script Part 4), and (b) the ALREADY-established fact
   that `D_full` itself maps the invariant domain (total `Λ`-degree 3) to
   the invariant target (total degree 0) — a degree shift of `-3` that a
   degree-based operator like `BL_64` cannot commute with in general. **But
   this incompatibility does not create doubt about the kernel's own `B-L`
   eigenvalue**, because that eigenvalue does not depend on the
   coset/torsion-dependent matrix elements `a`, `b` at all — it depends
   only on the fact that the ENTIRE 2-dim domain (not just the 1-dim
   kernel direction picked out by `a`,`b`) is already a single `BL_64`
   eigenspace, which is a fact about `SU(3)`-invariance and exterior degree
   alone (script Part 1/2), untouched by which specific direction within
   that space `D_full`'s torsion-dependent construction happens to null.

---

## Part 1 — Structural compatibility (script `[1]`)

| Check | Result | Citation |
|---|---|---|
| `BmL[j,j] == (2·popcount(j)-3)/3` for `j=0..7` | **True** | `g15_hypercharge.py:104-109` (T2), re-spot-checked here on the actual imported `BmL` matrix, not reconstructed by hand |
| Explicit bijection `j → subset` carries `BmL`'s diagonal onto the degree formula, entrywise, all 8 indices | **True** | script Part 1b; bijection: `j=4·i₁+2·i₂+i₃ ↔ subset={k : i_k=1}`, using `g15_hypercharge.py:65-67`'s own stated bit-weight convention (qubit 1 = weight 4, etc.) |
| `Σ` grade sizes `{0:1,1:3,2:3,3:1}` | **True** | `g2su3_explicit_clifford.py:30` (`SUBSETS`), matches G14's `1⊕3⊕3̄⊕1` cited in `g15_hypercharge.py:3` (G14 itself reused by citation, not re-run) |

**Verdict: structurally comparable — YES.** `Σ` and G15's weight space are
the same `SU(3)`-module (both `1⊕3⊕3̄⊕1`), and `BmL` is exactly the
degree/exterior-grade operator on either — no new basis-conversion
machinery had to be invented; the comparison is direct.

## Part 2 — Kernel eigenvalue (script `[2]`)

| Object | `BL_64` eigenvector? | Eigenvalue | Source |
|---|---|---|---|
| `v_a = y1⊗y23 - y2⊗y13 + y3⊗y12` | **Yes** | **0** | `round59_route_b_consistency.py:219`, reconstructed with identical coefficients |
| `v_b = y123⊗1` | **Yes** | **0** | `round59_route_b_consistency.py:220` |
| `w = 1⊗1` (target invariant) | Yes | `-2` | `round59_route_b_consistency.py:221` |
| `k = -√3·u₁+u₂` (physical kernel vector, `D_full(k)=0` confirmed fresh) | **Yes** | **0** | recomputed fresh from `a=-1,b=-√3` (matches round59 decision.md's cited values, independently reproduced here via imported `D_full`/`herm`, not copied) |

`BL_64 = leibniz64(BL_sigma)` was directly verified diagonal in the
`(sL,sR)` product basis (`BL_64_diagonal_in_product_basis=True`) — expected,
since `BL_sigma` is diagonal and `leibniz64`'s Leibniz-rule construction
preserves diagonality for diagonal inputs; this makes every simple-tensor
basis vector trivially an eigenvector, but `v_a` mixes **three** different
basis vectors (`y1⊗y23`, `y2⊗y13`, `y3⊗y12`) which could a priori have had
different eigenvalues — the check that all three share eigenvalue `0` is
the actual non-trivial content, confirmed by direct computation, not by
diagonality alone.

**Why `B-L=0` specifically, not some other value:** `v_a`'s three terms
each have `(|S_L|,|S_R|)=(1,2)` → `bl(1)+bl(2) = -1/3+1/3 = 0`. `v_b` has
`(|S_L|,|S_R|)=(3,0)` → `bl(3)+bl(0) = 1+(-1) = 0`. Both land on `0` because
both are `SU(3)`-invariant vectors in the domain block, and `SU(3)`-
invariance in `Σ_odd⊗Σ_even` forces total exterior degree `=3` exactly
(the only degree combinations pairing `Λ^p` with a piece containing an
`SU(3)` singlet are `(1,2)` and `(3,0)`, both summing to 3) — a structural
fact about `su(3)` representation theory (Λ¹⊗Λ²=3⊗3̄⊇1, Λ³⊗Λ⁰=1⊗1=1),
independent of the coset/torsion construction that builds `D_full` itself.

## Part 3 — Not applicable

Step 1 found the vector spaces directly comparable with a cheap,
already-reusable construction (the `leibniz64` Leibniz lift, already
established in this project for `su(3)` generators, applied here to `BmL`
unchanged in form). No basis-conversion gap was found, so there is nothing
to report under Part 3.

## Part 4 — Risk-lens check (script `[4]`)

| Check | Result |
|---|---|
| `D_full(y1⊗1)` [probe vector, chosen after testing 5 candidates — `y1⊗1` was the first with a manifestly nonzero output; an earlier probe, `y1⊗1`'s predecessor `y1⊗y1`, was degenerate (`D_full`≡0 on it), making any commutator check on it vacuous, and was discarded] | nonzero, supported ONLY at total degree `4` (input degree `1`) |
| `[BL_64, D_full]` on that probe | **nonzero** — confirmed, not merely inferred |
| Independent confirmation | domain (degree 3) → target (degree 0) under `D_full` is itself a degree shift of `-3`, already established in dolan-casimir/round59's own construction (`preprint.tex:806-812`) |
| Does this threaten the Part 2 eigenvalue claim? | **No** — `risk_neutralized_for_this_specific_claim=True`. The kernel's `BL_64` eigenvalue does not depend on `a`,`b` (the torsion-dependent matrix elements) at all; it depends only on the ENTIRE 2-dim domain already being a single `BL_64` eigenspace (Part 2), which is forced by `su(3)` representation theory alone and holds regardless of which direction within that space `D_full`'s torsion term happens to null. |

**This is a genuinely stronger and more relevant risk-check than G98's
original**, which tested `[BmL, so(6)$ generators]` on the untwisted 8-dim
`Σ` — here the check is `[BL_64, D_full]` on the actual 64-dim twisted
fibre, using the actual Leibniz-lifted charge and the actual physical Dirac
operator. It confirms G98's concern is real at the operator level (`BL_64`
does not commute with `D_full`) — and directly demonstrates, rather than
merely hoping, that this specific non-commutativity is orthogonal to (does
not touch) the specific eigenvalue computed in Part 2.

---

## Verdict-selection note (read before citing this as a clean PASS)

The claim.md's PASS wording requires the risk-lens check to find "no
incompatibility with `su(3)⊕u(1)`." **Taken completely literally, that
wording is not satisfied** — a real incompatibility (`BL_64` vs `D_full`
non-commutativity) was found and confirmed fresh, not dismissed. The
BLOCKED wording, read narrowly, could be invoked here ("the risk-lens check
finds the round59 construction genuinely depends on `SO(6)` structure
outside `su(3)⊕u(1)`").

This experiment selects **PASS**, not BLOCKED, because BLOCKED's own
wording requires the dependency to make "a well-defined `B-L` charge
**doubtful without further work**" — and no doubt remains: Part 4's own
computation resolves the question completely (not partially, not
provisionally) by showing the specific eigenvalue claim is insensitive to
the specific incompatibility found, for a stated, checkable structural
reason (SU(3)-invariance forces the entire domain to one degree, hence one
`BL_64` eigenvalue, independent of the coset-dependent map). BLOCKED would
misrepresent a **resolved** question as an **open** one. A future reader
who weighs the literal PASS wording more strictly than this reasoning is
invited to relabel this **BLOCKED-BUT-RESOLVED** — the underlying
computation and its conclusion do not change either way; only the label
does. Per this project's own Perelman-audit discipline (no forced
positive, presumption of falsity until shown otherwise): the caveat is
reported in full above, not minimized, and the reasoning that neutralizes
it is a directly-checkable fact (`domain_common_eigenvalue=True`,
`kernel_is_BL64_eigenvector=True`), not an assertion.

---

## Applying the pre-registered criteria

| Criterion | Finding |
|---|---|
| Step 1 (structural compatibility) | Directly comparable — same `SU(3)`-module, degree-based bijection verified entrywise |
| Step 2 (eigenvector + eigenvalue) | Kernel vector IS an eigenvector; `B-L = 0` |
| Step 3 (if not comparable) | N/A — step 1 succeeded |
| Step 4 (risk-lens) | Real incompatibility confirmed, shown NOT to affect this specific claim (see Verdict-selection note) |

**FAIL is not supported:** the comparison was possible, was attempted, and
the kernel vector DOES turn out to be an eigenvector — the opposite of
FAIL's condition.

**BLOCKED is arguable on a strict reading of the wording** (see
Verdict-selection note) but not adopted, because the specific doubt BLOCKED
requires ("doubtful without further work") does not survive Part 4's own
direct computation — no further work is needed to answer whether THIS
kernel vector carries a well-defined `B-L` charge; it does, `B-L=0`, and
that answer is stable under the exact incompatibility that was checked for.

**PASS is adopted**, with the caveat structurally embedded in the verdict
label itself (`PASS_WITH_DOCUMENTED_CAVEAT` in the script's own machine
report) rather than hidden in prose.

---

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result kills:** round93 (E23)'s framing that `B-L` "has never
  been constructed as an operator on the twisted kernel's ambient space at
  all" (E23 Part A.7) — it now has been, via a cheap, already-established
  Leibniz-lift pattern, and gives a definite answer (`B-L=0`), not merely a
  partial or ambiguous one.
- **What this result does NOT kill:** G98's own finding that `BmL` fails to
  commute with the full 15-dim `so(6)` — that finding is CONFIRMED again
  here, on a sharper operator (`BL_64` vs `D_full`, not just `BmL` vs raw
  `so(6)` generators), not overturned. It also does not kill round85/E17's
  `t=0`/`t=1` coexistence `BLOCKED`, or round91's System-A/System-B
  non-reconciliation — both untouched, S³-side questions this experiment
  does not address.
- **What survives, confirmed stronger than before:** the claim that
  `B-L=0` for the twisted zero mode is not fragile — it survives BOTH (a)
  the choice of bijection between G15's basis and `Σ`'s basis (shown to be
  degree-driven, hence bijection-independent), and (b) the genuine
  non-commutativity of `BL_64` with the full `D_full` (shown structurally
  irrelevant to this specific eigenvalue).

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Determine whether `B-L=0` is physically sensible for a single zero-mode fermion (as opposed to a composite/paired state) | This experiment defines `B-L` on the twisted fibre via the Leibniz/additive rule appropriate to a TENSOR PRODUCT (`Σ⊗Σ`, i.e. `S+⊗S-`) — whether the physical zero mode should be interpreted as "one particle in a tensor-product bundle" (additive charge, as computed here) or requires a different physical identification of what the two `Σ` factors represent is NOT resolved here; flagged for a future round if the physical interpretation of `S+⊗S-` as a single-particle vs composite state needs sharpening |
| Fill E23 Part C's `B-L`/`Y` census cells for System A now that `B-L=0` is available | This experiment supplies the missing number for the specific `dim ker=1` trivial-`G₂`-rep zero mode; E23's fuller per-`t`-sector, per-channel census (which asks about `t=0`/`t=1` `T_3`-doublet components generally, not just this one trivial-block vector) is a separate reconciliation task, not attempted here |
| Resolve the `PASS`-vs-`BLOCKED`-label tension explicitly, per the Verdict-selection note | Would require either amending claim.md's pre-registered wording (not permitted retroactively per this project's discipline) or a follow-up experiment that states the resolution criterion more precisely up front |

## Assumptions carried, unresolved

- `D_full²=D_{S3,t}²⊗I+I⊗D_{S6,twisted}²` (E2/E12) — untouched, S³-side.
- round59/dolan-casimir's own `dim ker=1`, `dim_a=2`, `dim_b=1` results are
  reused by citation; this experiment's own `common_nullspace_in_block`
  search was NOT rerun (only `D_full`/`herm` were rerun, as a spot-check
  producing `a=-1,b=-√3` independently, matching the citation).
- G15's own T1, T3-T7, T9-T12 gates are reused by citation, not rerun; only
  T2 was spot-checked here (needed for the structural-compatibility
  argument).
- `lambda=FREE_COUPLING_PARAMETER` — untouched. `safe_for_runtime=False` —
  unaffected; nothing here was run outside this repository, submitted, or
  sent anywhere.

## What this does NOT mean

1. Does NOT re-derive or re-audit round59/dolan-casimir's own `dim ker=1`
   claim, or its three-route certification status
   (`[VERIFIED-INDEPENDENT-INTERNAL]`, external review still outstanding)
   — reused by citation throughout.
2. Does NOT resolve round85/E17's `t=0`/`t=1` coexistence question, or
   E23 Part C's fuller S³-side `T_3`/`SU(2)_L`/`SU(2)_R` census — this
   experiment is entirely about the S⁶-side twisted-kernel `B-L` value.
3. Does NOT affect this project's `N_gen=3` headline (G73/G74A/G74B
   S⁶-only triality/index/chirality chain, independent of this S³-side
   torsion-endpoint/hypercharge program).
4. Does NOT claim the `PASS` label is beyond dispute — the Verdict-
   selection note above states explicitly and up front why a stricter
   reader could call this `BLOCKED-BUT-RESOLVED` instead, and that the
   underlying computation is identical either way.
5. Does NOT modify `preprint.tex` or any existing experiment folder — only
   this new folder (`claim.md`, this file, the script, and its JSON output)
   was created. Nothing here was submitted, posted, or sent anywhere
   external; this project's standing rules (no arXiv submission, no
   contact with Tom Lawrence, `lambda=FREE_COUPLING_PARAMETER`,
   `safe_for_runtime=False`) are unaffected.

## Pearl-registry candidate

**Observation:** the cheapest way to extend an established charge operator
from a single copy of a fibre to a tensor-product fibre (as needed whenever
a "twisted" bundle construction pairs two copies of the same underlying
space) is to reuse whatever Leibniz-lift machinery the project has ALREADY
built for a different symmetry (here: `su(3)`'s `leibniz64`), rather than
inventing new bundle-theoretic machinery — the charge operator on Σ was
already known to be central/abelian (`BmL ∝ J`, the `u(1)` center of
`u(3)=su(3)⊕u(1)`, T8), so its Leibniz lift was guaranteed well-defined
without any additional physics input.
**Falsifiable prediction:** any future round needing to extend a
`u(1)`-type charge from a single fibre to a tensor-product/twisted fibre in
this project can reuse this exact pattern (`leibniz64(diagonal charge
matrix)`) rather than re-deriving bundle structure from scratch — a cheap,
general, and reusable technique, not specific to `B-L`. **Impact score
~4** (methodology-level, reusable within this project's own S⁶/S³ twisted-
bundle constructions, not a physics result in itself). `next_check`: the
next time this project needs a charge/quantum-number on a twisted or
doubled fibre (e.g. if `T_{3L}`/`T_{3R}` ever needs a similar tensor-product
extension for the S³-side torsion-endpoint program), check whether this
same Leibniz-lift shortcut applies before building anything new.

## Check (reproduces this decision)

```
cd experiments/20260717-round94-bl-twisted-kernel-eigenvalue
python e24_bl_twisted_kernel_eigenvalue.py
```

Expect (from the script's own `report` dict, printed at the end and saved
to `results_e24.json`): `structurally_comparable=True`,
`v_a_is_BL64_eigenvector=True` (eigenvalue `0`),
`v_b_is_BL64_eigenvector=True` (eigenvalue `0`),
`w_is_BL64_eigenvector=True` (eigenvalue `-2`),
`domain_common_eigenvalue=True`, `a_coeff=-1`, `b_coeff=-sqrt(3)`
(matching round59 decision.md's cited values, reproduced fresh here),
`kernel_vector_confirmed=True`, `kernel_is_BL64_eigenvector=True`,
`kernel_BL64_eigenvalue=0`, `step2_pass=True`,
`risk_confirmed_BL64_not_commute_with_Dfull=True`,
`risk_neutralized_for_this_specific_claim=True`,
`verdict='PASS_WITH_DOCUMENTED_CAVEAT'`. Every source matrix/vector is
either imported unchanged (`BmL` from `g15_hypercharge.py`, `leibniz64`/
`D_full`/`herm` from `round59_route_b_consistency.py`, `SUBSETS`/`IDX` from
`g2su3_explicit_clifford.py`) or reconstructed with an exact, cited
coefficient literal (`v_a`, `v_b`, `w`), not from memory or paraphrase.
