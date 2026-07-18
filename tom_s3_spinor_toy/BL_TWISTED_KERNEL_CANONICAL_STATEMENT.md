# Canonical Statement — B-L on the Twisted Kernel

**Purpose:** OB3 formalization. Consolidates round94 (E24), round107, G98,
and round61 into ONE canonical, scope-limited statement — no new
computation, pure write-up of already-adjudicated results. Companion to
`OPEN_BLOCKERS.md` (OB3, now resolved as "formalized" — the underlying
question was already answered; what was missing was a single canonical
citation, not a new result).

## The canonical statement

> On the physical, dim-1 twisted kernel of `D_{S⁶,twisted}` (round59/
> dolan-casimir-g2su3's zero mode, reconstructed independently in round94),
> the Leibniz-lifted operator `BL_64 = leibniz64(BL_sigma)` has eigenvalue
> **`B-L = 0`** on the physical kernel vector
> `k = -√3·u₁ + u₂` (`D_full(k) = 0`, confirmed).

This is the full, precise, and complete claim. Every clause below narrows
what it does and does not mean.

## The four constraints (per OB3's own framing)

### 1. The specific lifted operator

`BL_64 := leibniz64(BL_sigma)`, where `BL_sigma` is G15's own
`BmL` matrix (`experiments/20260619-g15-hypercharge/g15_hypercharge.py`,
a pure Hamming-weight formula on the 8-dim `Σ = Λ•(ℂ³)` fibre) and
`leibniz64` is round59/dolan-casimir's own tensor-product Leibniz-rule
lift (`round59_route_b_consistency.py:91-106`), reused unchanged — **not**
a new construction invented for `B-L` specifically. `BL_64` acts on the
64-dim `Σ⊗Σ` twisted fibre.

### 2. The specific zero mode

`k = -√3·u₁ + u₂` — the exact SAME vector round59/dolan-casimir
established as the physical `dim ker(D_{S6,twisted})=1` kernel (`a=-1`,
`b=-√3`), reconstructed fresh in round94 via the imported `D_full`/`herm`
operators, matching the citation independently. `BL_64(k) = 0·k` — `k` is
an exact `BL_64` eigenvector, eigenvalue `0`.

### 3. Full Dirac symmetry fails — confirmed, and shown irrelevant to this eigenvalue

`[BL_64, D_full] ≠ 0` — confirmed directly (round94 Part 4, two independent
ways: a nonzero commutator on a probe vector, and the structural fact that
`D_full` shifts total exterior degree by `-3` while `BL_64` is
degree-diagonal). This is a **real, confirmed non-commutativity**, not
dismissed. **But it does not touch the eigenvalue claim above**, because
that claim depends only on the ENTIRE 2-dimensional `SU(3)`-invariant
domain (not just the 1-dim kernel direction) already being a single
`BL_64` eigenspace — a fact forced by `su(3)` representation theory alone
(`Λ¹⊗Λ²⊇1` and `Λ³⊗Λ⁰=1` are the only degree-pairings containing an
`SU(3)` singlet, both giving `B-L=0`), independent of which specific
direction within that eigenspace the torsion-dependent `D_full`
construction happens to null.

### 4. Physical conserved `B-L` is not derived — it is a constructed label

`B-L=0` is a **consequence of the Leibniz-lift construction applied to
G15's own `BmL`**, not a derivation from an independent physical
conservation principle. Two separate, already-established facts bound this:

- **G98** (`experiments/20260701-g98-bl-isometry-holonomy/decision.md`):
  `BmL` commutes with the 9-dim `su(3)⊕u(1)` subalgebra of `so(6)` but
  **not** the full 15-dim algebra — reconfirmed on the sharper `BL_64`/
  `D_full` pairing in round94 (see constraint 3 above), not merely on the
  original untwisted `BmL`/raw-`so(6)` pairing.
- **Round61** (`bl-commutant-uniqueness`, `null_results/INDEX.md`):
  `B-L` is a **member**, not the unique element, of a `dim≥3` family of
  admissible `U(1)` charges compatible with commutant + chirality + real-
  structure + anomaly-freedom constraints. An additional physical principle
  (e.g. a specific UV embedding) would be needed to single `B-L` out
  uniquely — not supplied by this project's own geometry.

### 5. The mode is a singlet, not Pati-Salam matter

**Round107**: `k_vec` (the same physical kernel vector) is a genuine
singlet under the **full 15-generator** `SO(6)=SU(4)` action — all 15
generators of `so6_spin_gens` (Leibniz-lifted the same way as `BL_64`)
annihilate it, `span{k_vec, G_1·k_vec,...,G_15·k_vec}` has rank exactly 1.
This is **stronger** than being merely an `SU(3)_c` singlet (round92) — it
is not a `4` or `4̄` of `SU(4)`, and cannot itself be identified with a
Pati-Salam matter multiplet. Round107's own honest scope caveat (from its
second skeptic pass) applies here unchanged: 9 of the 15 generators
(`su(3)⊕u(1)`) were validated via an independent non-diagonal span check
against round59's own separately-built `su(3)` generators; the remaining
6 generators rest on `lift_to_spinor`'s internal consistency, not a third,
independently-built reference construction.

## What this canonical statement does NOT mean

1. Does NOT derive `B-L` from a physical conservation principle — it is
   constructed via the Leibniz lift of an already-chosen `U(1)` (G15's
   `BmL`), one member of a larger admissible family (round61).
2. Does NOT establish the twisted kernel carries any nontrivial `SU(4)`
   (or `SU(3)_c`, or any subgroup) charge — round107 shows the opposite,
   a genuine singlet under the full algebra.
3. Does NOT resolve whether the physical zero mode should be interpreted
   as "one particle in a tensor-product bundle" (the additive/Leibniz
   convention used throughout) versus requiring a different physical
   identification of what the two `Σ` factors in `Σ⊗Σ` represent — flagged
   as open in round94's own Relaxation Map, still open here.
4. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False` — this is entirely an S⁶-side twisted-kernel
   charge-assignment question, independent of the S³-side torsion/parent-
   action program (`OPEN_BLOCKERS.md` OB1/OB2) and the S⁶-only
   triality/index/chirality chain (G73/G74A/G74B).
5. Does NOT re-derive or re-audit round59/dolan-casimir's own `dim ker=1`
   result, round94's `PASS`-vs-`BLOCKED` label tension (explicitly
   unresolved by round94's own choice, see its Verdict-selection note), or
   round107's own second-pass skeptic caveat on the remaining 6 generators
   — all reused by citation, not re-verified in this write-up.

## Source files (all reused by citation, nothing re-run for this write-up)

- `tom_s3_spinor_toy/experiments/20260717-round94-bl-twisted-kernel-eigenvalue/decision.md`
- `tom_s3_spinor_toy/experiments/20260717-round107-su4-orbit-of-twisted-kernel/decision.md`
- `tom_s3_spinor_toy/experiments/20260701-g98-bl-isometry-holonomy/decision.md`
- `tom_s3_spinor_toy/null_results/INDEX.md` (Round61-BL entry)
