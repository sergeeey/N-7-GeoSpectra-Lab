# C183 Decision — PROMOTE (the criterion), and the two pearls close as REFUTED-AS-STATED

**Date:** 2026-09-08
**Verdict:** **PROMOTE**, per `claim.md`'s own kill-criterion table: 4 of 4
agreement, no per-space branch in the decision path, both injected-error
controls flip. `efficiency = (4 - 3)/(4 - 3) = 1`.

All numbers below trace to `c183_duality_criterion.py` and its saved
`run_output.txt`. None are hand-typed independently of that file.

---

## 0. What this round is, and what it deliberately is not

The request that started it was "close the Round59 and Round65 pearls with one
round on `S^3xS^3`." The Prior Result Gate in `claim.md` found that round
already exists — twice — and that neither pearl was ever updated with it:

| | date | what it did | verdict |
|---|---|---|---|
| **Round70 Part B** | 2026-07-17 | the crux check on `S^3xS^3` (and on `CP^3`) | `S^3xS^3` **FAIL** — an isotropy-trivial slot IS available; `CP^3` PASS |
| **Round71** | 2026-07-17 | the explicit `Term2` value for `S^3xS^3` | **ILL-POSED** — CH2016's own p.18 data is not internally Hermitian-consistent; two repair attempts disagree |

So this round did **not** recompute `S^3xS^3`. Re-running a committed
computation because a later reader did not know it existed is the blind retry
the Adaptive Iteration Branch Rule forbids, and Round71's obstruction sits in
the primary source, not in the effort applied to it.

What it did instead: ask the question Round70's own summary table raises and
does not answer — why exactly one of the four fails.

---

## 1. Result

One criterion, one function of the isotropy data, no per-space branch:

| space | isotropy `H` | `Lambda^2` weights | zero-sum pairs | C183 | Round70 |
|---|---|---|---|---|---|
| `S^6 = G_2/SU(3)` | `SU(3)` | `(0,1) (1,-1) (-1,0)` | 0 | PASS | PASS |
| `SU(3)/T^2` | `T^2` | `(1,1) (1,-2) (-2,1)` | 0 | PASS | PASS |
| `CP^3` | `Sp(1)xU(1)` | `(0,2) (1,-1) (-1,-1)` | 0 | PASS | PASS |
| `S^3xS^3` | `SU(2)_diag` | `(2) (0) (-2)` | 3 | **FAIL** | **FAIL** |

**4 of 4 against a floor of 3 of 4.** The floor is not rhetorical: a criterion
that returns PASS unconditionally — containing no mechanism at all — scores 3
of 4, because three of the four spaces really do pass. That is why the
threshold was pre-registered at 4 and why "agrees with most of them" would
have been recorded as a null.

**The mechanism.** `dim (V (x) W)^H = dim Hom_H(V^*, W)`, so the trivial
component is absent exactly when `Lambda^2` shares no constituent with its own
dual; duality on a compact group negates torus weights. The step fails where
`Lambda^2`'s weight set is invariant under negation, and among the four that is
`S^3xS^3` alone.

**Why that one.** `SU(2)_diag` is the only one of the four isotropy groups with
no representation that fails to be isomorphic to its own dual. `SU(3)` has
`3 != 3bar`; `T^2`'s non-trivial characters are not their own inverses;
`Sp(1)xU(1)`'s `V(m,n)^* = V(m,-n)` differs whenever `n != 0`. Every `SU(2)`
irrep has a negation-symmetric weight set, so `Lambda^2` cannot avoid meeting
its own dual.

**And it is not a choice artefact.** Enumerating the negation-symmetric
3-element sub-multisets of `m_C = V2 (+) V2` returns exactly one, and it FAILs
— so no invariant almost-complex structure escapes; the failure is forced by
the isotropy group. Symmetrically, on `CP^3` — the one space where Round70 did
have to choose between splits — both admissible splits PASS, so its verdict is
not a choice artefact either.

---

## 2. Skeptic (FL Step 8a, context-asymmetric: `claim.md` + code only)

Verdict returned: **WEAKENED**, with `PROMOTE` under `claim.md`'s own kill
criterion. Three concerns, each answered below; two were real defects and are
**fixed in the artifact**, not merely noted.

| # | concern | response |
|---|---|---|
| 1 | **The script computes a torus-level check while `claim.md` advertises an `H`-level "exactly when".** These differ: for `H = SU(3)` and `Lambda^2 = 3 (+) 6` the torus check finds zero-sum pairs while the `H`-singlet count is 0. The one FAIL's `H`-level status was imported from Round70, not computed. | **FIXED.** The separating example is now run in the script and prints `T`-count 6 vs `H`-count 0, so the one-sidedness is demonstrated rather than described. The `S^3xS^3` `H`-level multiplicity is now computed here — `mult(V0) = m(0) - m(2) = 3 - 2 = 1` by the rank-1 highest-weight peel — reproducing Round70's Clebsch-Gordan from weights alone instead of citing it. `claim.md`'s Claim section carries a new paragraph stating exactly which half rests on the proxy (the three PASSes, rigorously) and which does not (the FAIL). |
| 2 | **Negative control (b) was not an admissible input.** `[(2,1),(0,1),(-2,1)]` has top-wedge sum `(0,3) != (0,0)`, violating the invariance the script demands of all four real inputs, and the control block never re-checked it. The flip was forced by the uniform charge shift alone. | **FIXED.** Both controls now run through one `control()` helper that asserts top-wedge invariance before anything else. Control (a) is the reviewer's own suggestion, `[(1,-1),(-1,1),(0,0)]` (PASS→FAIL, sum zero); control (b) is `[(3,),(-1,),(-2,)]` (FAIL→PASS, sum zero). The file states plainly that (b)'s multiset is not the weight set of any `SU(2)` representation — it is a corruption built to move the decision, satisfying the one structural constraint the script actually enforces. |
| 3 | **The `J`-independence assertion was tautological.** It fed one hard-coded multiset to `verdict()` and confirmed the singleton output; it could not have failed. | **FIXED.** Replaced by a real enumeration over the negation-symmetric 3-element sub-multisets of `m_C`'s weights — a search that could have returned a second candidate escaping the failure, and returns exactly one, which FAILs. |

The reviewer also independently re-derived all four input transcriptions
against Round65/Round70 and found no defect, confirmed the uniqueness of
`SU(2)` among the four isotropies, and verified `CP^3`'s conjugate split — that
last check is now in the script as a robustness section.

**Note on the concern that is NOT dismissed but is worth stating precisely:**
the `H`-level *iff* is a general mathematical statement and remains true; what
was over-sold was the claim that this script establishes it in general. It
establishes it on this closed population of four. Any hypothetical fifth space
would need its own `H`-level completion wherever the torus count came out
nonzero.

---

## 3. What this changes for the two pearls

Both pearls state the same prediction: that the two-line argument goes through
on the remaining Butruille spaces. It does not.

- **Round59's pearl (2026-07-14)** — prediction: "On any other nearly-Kahler
  coset admitting Killing spinors with nonzero Killing constant (`CP3`,
  `SU(3)/T2`, `S3xS3`), the analogous trivial-block rank should also be 1 by
  the same two-line argument." → **REFUTED AS STATED.** True for two of the
  three named (`SU(3)/T^2`, `CP^3`), false for the third.
- **Round65's pearl (2026-07-15)** — prediction: the mechanism tested on the
  remaining two "should also go through — 2 of 4 now confirmed, a genuine
  positive signal for the Universality open problem." → **REFUTED AS STATED,**
  and the count it anchors on is superseded twice over: it is 3 of 4, not
  2-and-rising, and the fourth is a structural exception rather than an
  untested gap.

**What survives, and it is not nothing:**

1. The step holds on three of the four, `CP^3` included — one more space than
   either pearl ever recorded.
2. The isotropy-Schur bound `dim ker <= 1` holds on **all four**, independently
   of this criterion (Round70 Step 4). `S^3xS^3`'s trivial-block rank is still
   at most 1; what is missing there is the argument forcing it to equal 1.
3. The exception is now explained rather than merely observed, and explained by
   a property of the isotropy group that can be checked before any construction
   is attempted.

**What is NOT established** (carried from `claim.md`, repeated because this is
the sentence most likely to be misread downstream): none of this shows
`Term2 != 0` on `S^3xS^3`. The cheap argument fails to force vanishing; whether
the coefficient in the available slot is zero anyway is exactly the question
Round71 could not certify a substrate for, and it stays open.

---

## 4. Status propagation (research-methodology.md principle 5)

Checked this session, so that the finding does not sit in one folder the way
Round70's did for seven weeks:

- `pearl_registry/INDEX.md` — Round59 and Round65 rows updated to `refuted (as
  stated)` with the surviving statement; a new C183 row filed.
- `preprint.tex` §Universality (line ~1589) — **stale but not wrong.** It says
  CH2016's instanton-deformation route is not viable on `CP^3`, and that
  literal statement stands (Round70 reinforced it with a second, independent
  reason). What it is missing is Round70's positive finding that a *different*
  route is well-posed on `CP^3`. Flagged here, **not edited** — the preprint is
  an external-facing artifact and revising it belongs behind the Submission
  Gate, not in the margin of another round.
- `C175`'s pearl (2026-09-06) already qualified Round65's 2-of-4 count from a
  different direction (`H = SU(3)` only for `S^6`). The two asymmetries are
  independent and point the same way; neither subsumes the other.
- `C141`'s pearl (2026-09-04) is the same *shape* of finding in a different
  place — a quantity this project read as dynamical turned out to be fixed by
  representation theory. Cross-referenced, not merged: C141 is about kernel
  dimensions of twist bundles on `S^6`, this is about a vanishing step across
  four cosets. Different objects, same lesson.
- `null_results/` — **no entry.** Round70's `S^3xS^3` verdict is
  `OPEN_STRUCTURALLY_DISTINCT` and Round71's is `ILL-POSED`; per the
  Verification Substrate Gate neither is evidence against a claim, and a
  refuted *pearl prediction* is recorded in the registry's own status field,
  which is where a reader looks for it.

---

## 5. Revival condition for the refuted prediction

The kill here is **contingent, not theorem-level**, and the contingency is
named: the prediction fails because `Lambda^2(m^{1,0})` meets its own dual on
`S^3xS^3`. Two events would reopen it, both measurable:

1. **A computation of the coefficient in the available trivial slot showing it
   vanishes.** That restores the *conclusion* (rank forced to 1) on all four
   without restoring the *argument*. It requires a Hermitian-consistent basis
   for `S^3xS^3` from a source other than CH2016 p.18 — the specific thing
   Round71 lacked. A new primary source supplying one is the trigger.
2. **A different sufficient condition for `Term2 = 0`** that does not route
   through the no-trivial-slot shortcut. The criterion here says nothing about
   whether such a condition exists; it only says this one does not apply.

Not `hard_killed`: nothing in this round shows the trivial-block rank on
`S^3xS^3` is anything other than 1. What is dead is one route to proving it.

---

## 6. Reproduction

```
cd experiments/20260908-c183-butruille-duality-criterion
python c183_duality_criterion.py
```

Exit 0. Full suite at the time of this decision: `2537 passed, 4 skipped`
(`python -m pytest tests/ -q`). `ruff check` and `ruff format`: clean.
