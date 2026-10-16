# C179 — Claim

**Experiment ID:** `20260907-c179-spinor-multiplet-of-functions-nogo`
**Parent:** direct response to Tom Lawrence's 2026-09-07 request (notes
`Notes to Sergey re harmonics v5.pdf`, §3.3 italic ask + §1.4 italic
pointer): *"find harmonics of S² that form a basis for a two-component
spinor and then harmonics of S³ that form a basis for a four-component
spinor."* Before attempting the construction, this round tests whether
the construction is possible AT ALL in the setting his notes define.

## Step -5: Zero-Signal Gate

- **Entity:** Tom's own "ket space" as defined in his §1.1 — the space of
  square-integrable complex **functions** on `Sⁿ` (his eq 1), partitioned
  by the induced `SO(n+1)` action (his eq 12) into finite-dimensional
  ket spaces; and his "multiplet" (§1.3) — a set of `d` such functions
  carrying a `d`-dimensional representation `Γ_d` of the isometry group
  (his eq 40).
- **Falsifiable predicate:** can a multiplet in that sense carry a
  **spinor** representation — specifically `d=2` for `S²` (spinor rep of
  `Spin(3)`) or `d=4` for `S³` (spinor rep of `Spin(4)`)? Equivalently:
  does any spinor representation occur in the decomposition of `L²(Sⁿ)`
  under the induced action?
- **Measurable outcome:** explicit matrix computation of how the
  **kernel element** `z` of `Spin(n+1) → SO(n+1)` acts (a) on the vector
  representation, (b) on the spinor representation, (c) on functions via
  Tom's own induced-action definition (his eq 4). If (b) and (c)
  disagree, no such multiplet exists and the disagreement is the proof.

## Step -2/-1 (EstimandOps L0)

**Question type: Descriptive.** Does a specific, precisely-defined object
(a multiplet of functions carrying a spinor rep) exist within a specific,
precisely-defined space (`L²(Sⁿ)` with Tom's induced action) — not causal.

## Honest scope and provenance statement, BEFORE computing

1. **This round imports standard mathematics; it does not discover it.**
   That spinor representations are representations of `Spin(n+1)` and not
   of `SO(n+1)`, and that `L²(G/H)` decomposes into genuine irreps of `G`
   (Frobenius reciprocity / Peter–Weyl), is textbook representation
   theory. The contribution here is (a) applying it to a SPECIFIC external
   claim that a collaborator has explicitly flagged as unverified, and
   (b) exhibiting the obstruction **inside his own notation and
   equations**, so it is checkable by him without adopting new machinery.
   Per this project's own "forced not discovered" discipline (C144, C153,
   C154, C156, C158, C168), this is stated up front, not after the fact.
2. **Tom himself has already flagged the surrounding area twice** — his
   footnote 1 (p.3: global vs. local ket spaces) and footnote 2 (p.11:
   *"this is not a vector field... constructing these requires the use of
   local ket spaces"*), and his §2.2 tensor-product claim carries his own
   `[*check*]` marker. This round resolves that specific `[*check*]`.
   It is NOT a claim that his notes contain an error he was unaware of.
3. This round tests **existence within his stated setting only**. It says
   nothing about whether spinor harmonics exist as sections of a spinor
   bundle (they do), which is a different object than a multiplet of
   functions.

## Kill-criterion table (frozen before running the script)

| Verdict | Condition |
|---|---|
| `NOGO-CONFIRMED` | The kernel element `z` acts as the identity on vectors and on functions (via Tom's eq 4), but as `−Id` on the spinor rep, for BOTH `n=2` and `n=3` — forcing `Φ = −Φ ⟹ Φ = 0` for any putative spinor multiplet of functions. |
| `NOGO-FAILS` | `z` acts as `+Id` on the spinor rep (i.e. the spinor rep descends to `SO(n+1)`), so no obstruction exists and the construction Tom proposes may proceed as stated. |
| `DIMENSION-TRAP-CONFIRMED` (secondary, `n=3` only) | Dimension counting ALONE cannot decide the `n=3` case: `dim(½,½) = dim[(½,0)⊕(0,½)] = 4`, so a naive "is there a 4-dimensional block in `L²(S³)`?" check gives a FALSE PASS. Must be reported explicitly if true, since it is the exact trap a good-faith attempt would fall into. |
| `SUBSTRATE-MISMATCH` | The Clifford/Spin construction fails its own internal checks (Clifford relations, `z` not central, vector action not a rotation) — the computation is untrustworthy and no verdict may be reported. |

**Pre-registered expectation (written BEFORE running the script):**
`NOGO-CONFIRMED` **and** `DIMENSION-TRAP-CONFIRMED`. The obstruction is
expected because it is standard theory; the round is run anyway because
(a) an explicit matrix demonstration in Tom's notation is the deliverable,
not the abstract fact, and (b) the `n=3` dimension coincidence (4 = 4) is
a genuine trap worth documenting with numbers rather than asserting.
**A `NOGO-FAILS` outcome would mean this round's own reading of standard
theory is wrong** and would need to be resolved before anything is sent.

## AI-Hypothesis Pre-Gates (Steps -4/-3)

- **Source Trace:** the primary source is Tom's own PDF
  (`Notes to Sergey re harmonics v5.pdf`, 2026-09-07, 18pp, read directly
  this session — §1.1 eq 1, §1.3 eq 40, §1.4 eq 4/77, §2.2, §3.3).
  Clifford machinery reused from this project's own already-`[VERIFIED-tool]`
  round67 (`e2_s3_torsion_deformation.py`, Cl(3) generators).
- **Novelty Check:** `null_results/INDEX.md` pre-check hook fired on
  keyword overlap with `R45-Leibniz`, `Round114-AHL2023`, `C107-MeierKostant`,
  `C134-ECSKTorsion`, `C145-TwistedNotKostant`, `C154`, `C159` — all
  inspected, none concerns the question "does a spinor rep occur in
  `L²(Sⁿ)`". No prior round in this project asks this. The closest prior
  work is `experiments/20260728-tom-so3-harmonics-sign-check/` (same
  collaborator, same general topic) which treats **vector/scalar**
  harmonics only, never spinors — confirmed by direct read.

## What this does NOT mean (pre-registered)

1. Does NOT show spinor harmonics on `S²`/`S³` do not exist — they do, as
   sections of a spinor bundle; only the "multiplet of global functions"
   realization is excluded.
2. Does NOT invalidate Tom's §1–§2 general theory for **tensor**
   multiplets (vector, and by tensor products all integer-spin cases),
   which his §3.1–§3.2 already verifies concretely for `S²`.
3. Does NOT by itself tell us how to BUILD the spinor harmonics — that is
   the next round (item 2/3 of the agreed plan), not this one.
4. Does NOT constitute a submission to Tom. Anything sent externally must
   pass this project's own Submission Gate (`integrity.md`) separately.
