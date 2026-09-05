# C135 — Decision. Does C133's explicit triality `Z3` cyclically permute
# round119/L3b's `(Gamma_A, Gamma_B)` sign patterns of `v, s, c`?
#
# VERDICT (machine-readable, class-qualified in the first line per C124/C125/C133
# precedent):
#
#   `SIGN-PATTERN STATISTIC: NO Z3 ACTION (kill criterion (b) FIRES, claim FALSE)`
#   `SECTORS THEMSELVES:     Z3 ACTS CYCLICALLY (all three, as always expected)`
#   `NOT BLOCKED — the two constructions are directly comparable`
#   `ROW-40's next_check COLUMN: ANSWERED — NO`
#   `ROW-40's caveat COLUMN ("...permute these three SECTORS"): REFUTED`
#
# The two registry columns ask DIFFERENT questions and get OPPOSITE answers.
# That is the result, and the difference is one word.
#
#   * The `next_check` column asks about the `(Gamma_A, Gamma_B)` **sign
#     patterns** of `v,s,c`. There are only **two** distinct ones — `8_v` and
#     `8_c` both carry `Gamma_A = -Gamma_B`. Three patterns cannot be cyclically
#     permuted when there are two. **Answer: no.**
#   * The caveat column asks whether a single `Z3` cyclically permutes "these
#     three **sectors**". It does. **That half of the caveat is refuted**, and
#     so is its proposed explanation ("a convenient basis with no real symmetry
#     manifest").
#
# ⚠️ READ §8, §8a AND `skeptic_verdict.md` BEFORE QUOTING ANYTHING ABOVE.
# One context-blind FL Step 8a pass was run. Verdict `[WEAKENED]`. It did NOT
# change the verdict's direction — it confirms every component of the central
# mathematics — so per claim.md's own scope note a second paraphrased pass was
# not run. It found **11 defects not disclosed by the first draft**, all
# accepted, none dismissed. Four required re-running the script; one of those
# exposed a genuine numerical bug of mine (`np.real` on a complex Hermitian
# compression) that had silently emptied a control. **The headline arithmetic
# never moved.** What moved is what this round may claim as its own evidence:
#   * the top-line verdict string was INVERTED in the first draft (§2c);
#   * a quoted residual range was STALE and wrong (§5b);
#   * the "positive half" (three distinct pairings) is now MEASURED to be
#     generic to any 4+4 split and therefore carries no octonionic information
#     (§8b) — the first draft leaned on it to excuse the negative half's
#     one-sidedness, which it cannot do;
#   * the independence rung claimed for the `{6,3,3}` replication was too high.

---

## 0. Scope, stated before anything else

Convergent-mode, single-question round. Closes the long-standing `next_check`
on `pearl_registry/INDEX.md`'s `SO(4)xSO(4)` row. **No new physics is claimed**,
no blocker is closed, nothing about `N_gen=3`, `lambda`, or `safe_for_runtime`
moves. Registry files are deliberately **not** edited by this round.

---

## 1. Step −5 — Zero-Signal Gate, resolved BEFORE any computation

| Field | Filled |
|---|---|
| **Entity** | (1) C133's order-3 `sigma` on `J3(O)` and its `24x24` channel matrix `U24`; (2) the pair `(Gamma_A, Gamma_B)` of block-chirality operators and their per-channel signs |
| **Falsifiable predicate** | there is an explicit identification under which `sigma` cyclically permutes the three `(Gamma_A, Gamma_B)` sign patterns — or there is not |
| **Measurable outcome** | the number of **distinct** sign patterns across the three channels, and the order of the stabiliser of that pattern inside the triality `S3` |

Gate **PASSES**. Both objects are explicit matrices; the outcome is an integer
count, not a judgement.

---

## 2. Provenance correction — the construction is NOT in round119 [VERIFIED]

Gate 1 (artifact identity) run first; it caught a mislabel the task framing had
inherited.

* `experiments/20260717-round119-triality-distinguishability-gate/decision.md`
  was read **in full**. It contains **no `(Gamma_A, Gamma_B)` construction.** It
  is a rubric-application and registry-accuracy audit; its verdict is
  `GATE 1 OF 7 DONE / GATES 2-6 OPEN`, and it states: *"No new physics
  computation — this round is a rubric-application and registry-accuracy
  audit."* `Gamma_A/Gamma_B` appears once, as a citation inside a skeptic
  correction. *(Independently re-checked by the Step 8a skeptic.)*
* The construction lives in `L3B_SPIN8_INTERFACE_SPEC.md` §1.5, lines ~390-456,
  dated **2026-07-15** — two days before round119.
* The pearl row's own `Source` column agrees: *"searched for a non-G2 SO(4)
  candidate for L3b, per user request"*, dated `2026-07-15`. It never said
  "round119".

**Consequence:** "round119's `(Gamma_A, Gamma_B)`" is a conversational nickname,
not an identifier. Round119 *cites* the construction; it did not produce it.
Everything below attaches to `L3B_SPIN8_INTERFACE_SPEC.md` §1.5, **not** to
round119's verdict, which is untouched.

### 2a. The two columns, quoted exactly [CITED, verbatim]

`next_check` column:

> `next concrete step: verify whether the known triality Z3 (already built this
> session via octonion/g2 tools) cyclically permutes the (Gamma_A,Gamma_B) sign
> patterns of v,s,c in a consistent single-symmetry way, before any physical
> interpretation is attempted`

`Falsifiable prediction` column (the caveat):

> `... triality's Z3 action has not been checked against this specific
> (Gamma_A,Gamma_B) sign structure -- if a single Z3 symmetry doesn't actually
> cyclically permute these three sectors, this may just be a convenient basis
> with no real symmetry manifest`

`L3B_SPIN8_INTERFACE_SPEC.md` §1.5 point 3 (lines 451-456) uses the caveat's
wording: *"whether a single order-3 symmetry actually cyclically permutes these
three sectors, or whether this `SO(4)xSO(4)`-adapted description is merely a
convenient basis with no such symmetry manifest in it."*

### 2c. The word that carries the whole result: *sectors* vs *sign patterns*

**This is the single most important correction the skeptic pass forced, and the
first draft got it backwards.**

Row 40's two columns are **not** paraphrases of each other. The caveat (and
L3b, its source) says **sectors**. The `next_check` silently narrows this to
the **`(Gamma_A, Gamma_B)` sign patterns**. The narrowing happened *inside
row 40*, between two of its own columns.

That narrowing is where the entire kill lives:

| question | answer | measured in |
|---|---|---|
| does a single `Z3` cyclically permute the three **sectors**? | **YES** | §5d, and C133's own `U^3 = I` + normaliser `2.32e-15` |
| does it cyclically permute the three **`(Gamma_A, Gamma_B)` sign patterns**? | **NO** | §5c, 2 distinct values, stabiliser `Z2` |

The first draft's header read `ROW-40 CAVEAT: CONFIRMED IN LETTER, REFUTED IN
MECHANISM`. That is **inverted**: in *letter* the caveat speaks of sectors and
is **refuted**; what is confirmed is the *`next_check` column's* narrower
question. Corrected in the header above. The first draft also certified row 40
as "accurate to its source" without noting that the substitution occurred inside
row 40 itself — also corrected.

### 2b. The row was already partly superseded when written [VERIFIED]

Two later pearl rows, **same date, same session**:

* **the next row** built the explicit `12x12` order-3 matrix `T` on
  `so(4)_1 + so(4)_2` — `T^3 = I`, eigenvalues `{+1 x6, omega x3, omega-bar x3}`
  — establishing the subalgebra is triality-invariant **as a set**;
* **the row two later** (the `P, Q` intertwiner row — *not* the row immediately
  after; that one is the superseded *"not yet shown to be the same embedding"*
  entry, whose warning is directly relevant to §6a below) built the explicit
  `Cl(8)->Cl(8)` intertwiners, nullity exactly 1 over all 28 `so(8)` generators,
  residual `~1e-16`, transporting `Gamma_A|_{8_s} -> D_A`,
  `Gamma_A|_{8_c} -> -D_A`, `Gamma_B -> +D_A` on **both**.

So "no real symmetry manifest" was already half-refuted on 2026-07-15. The item
`L3B_SPIN8_INTERFACE_SPEC.md` names as still open (lines 505-511, 586-589) is:
*"The precise cyclic bookkeeping across all three roles simultaneously ... naive
relabeling failed, and the correct fix (almost certainly an octonion-conjugation
twist) was not tracked down."*

**Carefully stated (the first draft overstated this — see §7.7):** this round
answers the *question that open item poses* — whether a single `Z3` cyclically
permutes the sign structure — **structurally**, by exhibiting what the `Z3` does
act on instead. It does **not** execute the `(a,b,c) -> (b,c,a)` relabelling
programme L3b expected, and it never touches the covariance equation
`a(x)·y + x·b(y) = c(x·y)`. The conjectured octonion-conjugation twist is
neither found nor excluded.

---

## 3. Not BLOCKED — and why the negative half survives any basis mismatch

claim.md explicitly permitted `BLOCKED`. It is not warranted:

1. **The identification already exists in this project's own record** — the
   `P, Q` intertwiners bridge the Pauli-tensor `Cl(8)` (where `Gamma_A,
   Gamma_B` live) and the octonion-covariance `Cl(8)` (where `sigma` lives).
2. **The decisive facts are basis-independent:** `Gamma_A Gamma_B = Gamma_9` is
   a nontrivial *central* element of `Spin(8)`; the center is `Z2 x Z2`; each
   nontrivial central element is `+1` on exactly **one** of the three `8`s;
   triality permutes the three cyclically. No basis appears in any of these.

**Scope limit on that defence (skeptic defect 6, accepted):** it covers §5b and
§5c — the negative half. It does **not** cover §6a's *mechanism* story, which
does use a basis identification. See §6a.

---

## 4. What was computed

Script `c135_triality_vs_gamma_signs.py`, output `results_c135.json`, `ruff`
clean, exit 0, ~80 s.

**Side 1 reuses C133 verbatim.** C133's script is exec'd from a copy whose
`sha256` is checked equal to the committed file
(`ddc67bf9c75acfaff11e2280cb5a5c1e68dfd5cad66e3f82832b15c52bc8fe45`). The copy
exists only so that importing C133 — which writes `results_c133.json` next to
its own `__file__` at module level — **cannot overwrite another experiment's
committed artifact**. Reused objects re-reported to prove identity:
`sigma^3 = id` `0.0`; slot action `(x,y,z)->(z,x,y)` `0.0`; `sigma` a Jordan
automorphism `1.78e-15`; `U` normalises the `so(8)` image `2.32e-15`; 28
generators. These match `results_c133.json` exactly.

**Side 2 is rebuilt from L3b §1.5's own recipe:** eight anticommuting `16x16`
gammas (`{G_i,G_j} - 2delta_ij` max err `0.0`), `Gamma_A = G1G2G3G4`,
`Gamma_B = G5G6G7G8`. Reproduces both relations L3b records as VERIFIED:
`[Gamma_A, Gamma_B] = 0` (`0.0`) and `Gamma_A Gamma_B = Gamma_9 = G1...G8`
(`0.0`). All three channels come out of this one algebra, so no intertwiner is
needed to compare them with each other.

---

## 5. The result, in four measured facts

### 5a. `Gamma_B`'s vector image `D_A` is an octonion automorphism [VERIFIED]

`D_A` (fix `H = span(e0..e3)`, negate `H-ell = span(e4..e7)`) is an
**automorphism of `O`**, residual `0.0` against C133's own multiplication table
— so `D_A in G2 = Aut(O) = Fix(triality)`. Corroborated in C133's language:
`diag(D_A, D_A, D_A)` is a `J3(O)` automorphism (`0.0`) and commutes with `U24`
**exactly** (`0.0`).

Controls that genuinely fail: a `4+4` sign operator whose fixed subspace
(`span(e0,e1,e2,e4)`) is **not** a quaternion subalgebra → `22.99`; negating the
unit `1` → `17.97`; a random `SO(8)` rotation → `15.40`; replacing one slot by a
random `SO(8)` element → `13.12`.

*Verified side observation:* exactly **7** of the 35 four-subsets through `e0`
are quaternion subalgebras — the 7 Fano lines. **This cuts against the round's
own §6 conclusion and is recorded as such:** the `H/H-ell` split is one of a
`G2`-orbit of equivalent choices, so "not an arbitrary basis" is established
while **canonicity is not**. A second `G2` involution reproduces dim-12
centraliser, `T^3=I` and `{6,3,3}` identically.

### 5b. `Gamma_A = Gamma_9 * Gamma_B`, and `Gamma_9` is central [VERIFIED]

Scanning all eight sign triples `eps in {+-1}^3` for the `J3(O)`-automorphism
property: **exactly the four with `product = +1` pass** (`0.0`); the other four
fail at **`14.34`, `14.79`, `15.95`, `21.43`**. *(The first draft quoted "13.8
to 15.9" — a stale range from a pre-control-fix run, contradicting the JSON and
omitting the largest failure. Skeptic defect 1, confirmed by re-reading
`results_c135.json` and corrected here.)*

Those four are the center `Z2 x Z2` of `Spin(8)`, and **every nontrivial one has
exactly one `+` and two `-`**. Under `U24`-conjugation the three nontrivial ones
form one `3`-cycle `+-- -> -+- -> --+ -> +--`; the identity is fixed.

*Tier note:* the code never directly checks `Gamma_9` commutes with the 28
bivectors; centrality follows from the per-channel `max|a∓b| = 0.0` results plus
the standard identity. `[INFERRED]`, chain stated, not `[VERIFIED]`.

### 5c. The sign patterns take only TWO values [VERIFIED — the kill]

| channel | `Gamma_A - Gamma_B` | `Gamma_A + Gamma_B` | relation | `eps_X = rho_X(Gamma_9)` |
|---|---|---|---|---|
| `8_v` | `2.0` | `0.0` | `Gamma_A = -Gamma_B` | `-1` |
| `8_s` | `0.0` | `2.0` | `Gamma_A = +Gamma_B` | `+1` |
| `8_c` | `2.0` | `0.0` | `Gamma_A = -Gamma_B` | `-1` |

`rho_v(Gamma_B) = D_A` **exactly** (`0.0`); in every channel `Gamma_B` has
eigenvalue multiplicities `(+1)^4 (-1)^4`.

`8_s` and `8_c` reproduce L3b §1.5's own recorded finding. **The new entry is
`8_v`:** the relation there is `Gamma_A = -Gamma_B`, *the same as `8_c`*.

**Distinct sign patterns across three channels: `2`.** Stabiliser of that
**pattern** inside the triality `S3`: **order 2**, `{id, (v c)}`. No `3`-cycle
fixes it.

*Two scope notes, both from the skeptic pass:*
* Which channel is odd is an `S+/S-` labelling convention; only "exactly one
  channel is odd" is convention-free. Reordering the four factors of `Gamma_A`
  flips all three `eps` together, leaving `n_distinct = 2` and the stabiliser
  unchanged.
* What is measured is the stabiliser **of the sign pattern**, not of the pair
  `(Gamma_A, Gamma_B)` — fixing the pattern is necessary, not sufficient, for
  fixing the pair. The first draft's header and §6 said "of the fixed pair";
  corrected. The pair-level statement holds only via §6a, which is `[INFERRED]`.

### 5d. What the `Z3` acts on instead [VERIFIED, with §8b's limit]

Building `so(4)_1 + so(4)_2 = su(2)^4` explicitly (each factor dim `3`, bracket
closure `~2e-16`, the two factors of a block commuting to `0.0`), each channel
splits into two 4-dim pieces, each a doublet of exactly **two** of the four
`su(2)` factors:

| channel | pairing of `{1,2,3,4}` |
|---|---|
| `8_v` | `{1,2} \| {3,4}` |
| `8_s` | `{1,3} \| {2,4}` |
| `8_c` | `{1,4} \| {2,3}` |

— the three distinct perfect matchings, matching `hep-th/9804208` as recorded in
this project's registry. Brute-forcing all `24` relabellings of the four `su(2)`
factors: **8** induce a `3`-cycle of the channels, all of order 3.

*(The companion `predicted_fixed_subalgebra_dim = 6` is **hard-coded
arithmetic** — `3*(#fixed) + 3*[order==3]`, which returns 6 for every order-3
permutation of four labels. It is an expectation, not a corroborating
measurement. Skeptic defect 7; the JSON key is renamed accordingly.)*

**Replication of the `T`-matrix row [VERIFIED, rung corrected in §13].**
`so(4)+so(4)` is exactly the centraliser of `D_A` in `so(8)` (dim `12`). Pushed
through C133's triples: triality image stays inside (`2.24e-15`), `T^3 = I`
(`3.11e-15`), multiplicities **`{+1 x6, omega x3, omega-bar x3}`**. The control
— a non-quaternionic `4+4` split with the **same** dim-12 centraliser — does
*not* stay inside (`0.903`) and gives `T^3 != I` (`0.971`). **This control is
the round's single genuinely discriminating measurement**: it separates on
quaternionicity, not on dimension counting.

Explanation, not just measurement: `so(4)+so(4)` is the centraliser of `D_A`;
`D_A` is triality-fixed (§5a); the centraliser of a triality-fixed element is
triality-invariant. `{6,3,3}` is the signature of a `3`-cycle on four `su(2)`
summands — one fixed factor (3) plus the diagonal of the three cycled ones (3).
`[INFERRED]`, chain: §5a measured → centraliser invariance (standard) →
`{6,3,3}` measured, matching the combinatorial count.

---

## 6. The answer to row 40, stated precisely

**To the `next_check` column: no.** **To the caveat column: the caveat is
refuted.** (§2c.)

The `(Gamma_A, Gamma_B)` structure factorises into two pieces with *opposite*
triality behaviour:

1. `Gamma_B` is triality-**invariant** — the same `D_A` in all three channels.
2. `Gamma_A = Gamma_9 * Gamma_B`, and `Gamma_9` is a nontrivial **central**
   element, which triality does **not** fix: it 3-cycles the three.

So triality moves `Gamma_A` to the other two admissible partners of the fixed
`Gamma_B` — it acts transitively on the three possible *choices of `Gamma_A`*,
not on the three channels' sign values. Holding `(Gamma_A, Gamma_B)` fixed is an
`S3 -> Z2` symmetry-breaking choice.

### 6a. The two steps in that story the code does NOT establish [INFERRED]

Recorded because §3's basis-independence defence does **not** reach here
(skeptic defect 6, accepted in full):

* **Spin lift.** `G2` is simply connected, so exactly one of `±Gamma_B` lies in
  the lifted `Fix(triality)`; for the other, `tau(-Gamma_B) = omega * Gamma_B`
  because `-1` is itself one of the cyclically-permuted central elements. Steps
  1 and 4 test the `8x8` matrix `D_A` on the octonion side, which cannot see the
  `Spin(8)` lift. The lift is pinned only by L3b's **cited** `Gamma_B -> +D_A`
  on both `S±` — which this round deliberately replaced (§8.2) with the strictly
  weaker `(+1)^4(-1)^4` signature, a property of every traceless involution.
* **Basis bridge.** `D_A` is used both as an octonion map (via C133's `omulf`)
  and as `rho_v(Gamma_B)` in the gamma-index basis. The identification "octonion
  index `i` ↔ gamma index `i`" is assumed, never verified; `is_subalgebra
  ([0,1,2,3]) = 0.0` is consistent with it but would pass for any of the 7 Fano
  splits. **This project's own registry warned in these exact terms** (the
  superseded row: *"TWO DIFFERENT, never-reconciled Cl(8) realizations ...
  asserting they are the same object would be an overclaim"*), and the fix built
  there was the `P, Q` intertwiners — which **C135 does not rebuild**.

*Partial rescue, not a repair:* the 7 quaternion splits form one `G2`-orbit
(§5a), so a compatible identification can always be arranged. The conclusion
therefore survives as `[INFERRED]`, **not** `[VERIFIED]`.

### 6b. Caveat adjudication

| the caveat's claim | verdict |
|---|---|
| "a single `Z3` doesn't cyclically permute these three **sectors**" | **REFUTED** — it does (§5d) |
| the same, read on the **sign statistic** (the `next_check` column) | **CONFIRMED** — 2 distinct values, stabiliser `Z2` |
| "this may just be a convenient basis" | **PARTLY REFUTED** — it is the centraliser of a `G2` element and is triality-invariant (`0.903` control). But §5a shows it is one of a `G2`-orbit of 7, so **canonicity remains open** and this round does not close it |
| "with no real symmetry manifest" | **REFUTED** — the `Z3` is manifest: it 3-cycles the center, and it 3-cycles the three sectors |

---

## 7. What this round does NOT show

1. Does **not** re-derive or re-verify C133's `9 -> 3 -> 1` ladder.
2. Does **not** re-open round119's verdict — round119 did not build this object
   (§2).
3. Does **not** weaken the `SO(4)xSO(4)` candidate's three-way distinguishing
   claim, which rests on the branching (§5d) and is intact. It clarifies that
   the `Gamma_A/Gamma_B` *relative sign* separates `8_s` from `{8_v, 8_c}` only.
   **Stated without inflation (skeptic defect 11):** L3b said that sign
   *"genuinely distinguishes `s` from `c`"* and supplied the three-way split via
   the branching — nobody claimed the sign separated three ways. This is a
   sharpening of the record, not a correction of an error in it.
4. Does **not** revive the `SO(4)xSO(4)` route physically. C77/C78 closed it
   against the physical `D` (commutant `= su(3)` exactly, dim 8). Untouched.
5. Does **not** supply a parent action, close `H1c`/`OB1`/round95's gap, or
   change `N_gen=3`'s CONDITIONAL status, `lambda = FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime = False`.
6. Does **not** solicit Tom Lawrence's Part 5.
7. Does **not** find or exclude L3b's conjectured octonion-conjugation twist,
   and does **not** execute the `(a,b,c) -> (b,c,a)` relabelling programme. The
   covariance equation is never touched. §2b is worded accordingly; the first
   draft's "**That** is what this round resolves" was too strong.
8. Does **not** establish canonicity of the `H/H-ell` split (§5a, §6b).

---

## 8. Defects in this round's own work

### Self-caught, before the skeptic pass

1. **Three "controls" that could not fail.** The first draft used
   `D = diag(1,1,-1,-1,1,1,-1,-1)` as the "not an automorphism" control in
   steps 1, 4 and 5. Residual `0.0` — because `span(e0,e1,e4,e5)` is *also* a
   quaternion subalgebra, making it a **second `G2` involution**. Fixed: the
   control is now selected programmatically as a `4+4` split verified
   non-quaternionic; it fails at `22.99 / 10.34 / 0.903`. The broken case is
   kept, relabelled honestly, and produced the 7-Fano-lines observation.
2. **A near-vacuous check.** `Gamma_B_is_plus_D_A` compared `|Gamma_B|` to
   `|D_A|` — both all-ones in absolute value. Replaced by the eigenvalue
   signature plus the exact `rho_v(Gamma_B) - D_A = 0.0`. *(This replacement is
   strictly weaker, and §6a is where that weakness bites.)*
3. **A dead duplicated line** computing `three_cycles` twice. Removed.

### Caught by the FL Step 8a skeptic pass — all accepted, none dismissed

4. **Stale residual range** `13.8–15.9` vs the JSON's `14.34–21.43`. Fixed §5b.
   [HIGH]
5. **Inverted top-line verdict** (`CONFIRMED IN LETTER`). Fixed header + §2c.
   [HIGH]
6. **The positive half had no control and is entailed.** Fixed by *running* the
   missing controls — see §8b. [HIGH]
7. **Independence rung overclaimed** for the `{6,3,3}` replication. Fixed §13.
8. **"Stabiliser of the fixed pair"** upgraded from what was measured
   ("stabiliser of the pattern"). Fixed §5c, §6.
9. **§6's mechanism rests on two uncomputed steps** (spin lift, basis bridge).
   Now §6a, marked `[INFERRED]`.
10. **`predicted_fixed_subalgebra_dim` is tautological arithmetic** presented
    under a corroboration-sounding key. Renamed in the JSON; flagged in §5d.
11. **Ordinal slip** — the `P, Q` intertwiner row is two rows later, not the
    next one. Fixed §2b.
12. **§5a/§6 unreconciled on canonicity.** Fixed §6b (now "PARTLY REFUTED").
13. **§2b/§9 contradicted §7.7** on whether L3b's open item is "resolved".
    Fixed §2b, §7.7.
14. **Unchecked scalarity/orthogonality** in `conj_by_U` and the `eps` trace
    shortcut. Both are rescued by the independent `max|a∓b| = 0.0` checks;
    recorded, not repaired. [LOW]

### Found while acting on the skeptic's request — a real numerical bug

15. **`np.real(op)` on a complex Hermitian compression.** `summand_pairing` took
    the real part of `R† (split_op) R` before diagonalising. Harmless on the
    quaternionic path (that compression happens to come out real) but it
    **silently emptied the eigenspaces on the new control**, which would have
    been reported as a finding ("the non-quaternionic split has no pairing
    structure"). Fixed to diagonalise the complex Hermitian matrix directly.
    The main result is unchanged; the control's answer **flipped** (§8b).

## 8a. One-sidedness — disclosed for BOTH halves, not just the losing one

**Negative half.** Once `Gamma_A Gamma_B = Gamma_9` is a nontrivial central
element, the sign triple is *forced* to have exactly one `+`. So
`n_distinct_values` **could never have been 3**: kill power, no rescue power.
Sharper still (skeptic T1): two of the three values are *definitional* — the
code cuts `8_s`, `8_c` as the `Gamma_9` eigenspaces — and the third follows from
the two-line identity `Gamma_9 Gamma_a Gamma_9 = -Gamma_a`. **The run
contributes essentially zero bits to the negative half.** It is true; it is not
news the computation produced.

**Positive half — and this is the correction that matters.** The first draft
repaired the above by pointing at §5d: a different statistic on the *same*
construction that *does* take three distinct values. §8b now **measures** that
this repair fails: three distinct pairings appear for a non-quaternionic `4+4`
split too. Distinctness is generic. The repair is withdrawn.

**What survives as genuinely contingent and measured:** the `0.903` control of
§5d — triality-*covariance* of the pairings, which the non-quaternionic split
does not have. That is the round's one discriminating number, and it is a
replication of a 2026-07-15 result rather than a new one.

## 8b. Controls for the pairing claim — run, not conceded

The skeptic observed step 8 had **no control at all** (the `0.903` belongs to
step 5 and never touches the pairing computation) and predicted distinctness
would survive a non-quaternionic split. Both suggested tests were run:

| test | result |
|---|---|
| **T4a** — collapse the four `su(2)` labels onto two; can the counter report `< 3`? | `n_distinct = 2` → **the counter can fail** |
| **T4b** — redo the whole pairing computation for the 4+4 split `{0,1,2,4}\|{3,5,6,7}`, whose fixed subspace is **not** a quaternion subalgebra | `n_distinct = 3`, with the *same* three matchings → **distinctness survives** |

**The skeptic's prediction is confirmed by direct computation.** Three distinct
pairings is a fact about *any* `4+4` split of the eight gamma indices — it
follows from `so(4)+so(4)` representation theory and says **nothing** about
octonions, quaternionicity, or the `H/H-ell` structure.

Corrected claim: *distinctness of the three pairings is generic; **triality-
covariance** of them is not* — and only the latter is evidence about this
construction. This also removes the temptation to read §5d as independent
support for §6.

---

## 9. Kill Analysis

**Kill criterion (b) FIRES.** Measured: 2 distinct patterns, stabiliser order 2,
no `3`-cycle fixes the pattern. **The claim as pre-registered is FALSE.**
Criterion (a) (`BLOCKED`) does not fire (§3).

**A pre-registration error, caught by the run that fired the criterion.**
Criterion (b) continues: *"in which case round119's own caveat about lacking a
'real symmetry manifest' basis is confirmed."* That bundled inference is
**wrong**, and the same computation that fires the test refutes it (§5a, §5d,
§6b). A kill criterion should state a *test*, not a test plus the conclusion the
author expects from it; this one assumed "no `Z3` on the sign statistic" implies
"no `Z3` anywhere in the structure". It does not.

### What this KILLS

* The reading of the `(Gamma_A, Gamma_B)` relative sign as a **three-valued**,
  triality-cycled statistic. It is `Z2`-valued; `S3` breaks to `Z2` on it.
* Row 40's `next_check` as a live question — it has an answer.
* The caveat column's proposed explanation ("convenient basis, no real symmetry
  manifest"), except for its canonicity component (§6b).
* **This round's own first-draft framing** that "three distinct pairings"
  is evidence about the octonionic structure (§8b).

### What this does NOT kill

* The `SO(4)xSO(4)` candidate's three-way algebraic distinguishability.
* The triality-invariance of `so(4)+so(4)` — re-verified with a discriminating
  control, and now explained rather than merely observed.
* C133's ladder, round119's verdict, or any physical status flag.
* L3b's conjectured octonion-conjugation twist — untested either way.

### Relaxation Map (one assumption changed per variant; none attempted here)

| Variant | Assumption changed | Cheapest test |
|---|---|---|
| V1 | ask about the **sectors** rather than the sign values | answered YES, §5d — no new work |
| V2 | is there any pair of `Spin(8)` elements whose per-channel relation IS three-valued? | a three-valued statistic cannot be the image of a single `Z2`-valued central element; would need a non-central invariant. Untested. |
| V3 | let `(Gamma_A, Gamma_B)` rotate with the channel instead of staying fixed | this is what triality does (§6); makes the description covariant but no longer a *fixed* `SO(4)xSO(4)` basis |
| V4 | close §6a by rebuilding the `P, Q` intertwiners and pinning the spin lift | moderate cost; would upgrade §6 from `[INFERRED]` to `[VERIFIED]` |

---

## 10. Pearl / Caveat-Gate candidates (PROPOSED — deliberately NOT written)

Registry edits are the orchestrating session's call. Proposed:

1. **Close row 40's `next_check`** — answered, with §2c's split verdict, and fix
   its `Source` attribution note so "round119" is not read as the origin (§2).
2. **Flag the `sectors` vs `sign patterns` mismatch between row 40's own two
   columns** — the columns ask different questions and get opposite answers.
3. **New pearl (reusable):** *before treating a per-channel `+/-` statistic as a
   triality-cycled invariant, check whether it is the image of a central element
   of `Spin(8)` — every nontrivial one is `+1` on exactly one channel and `-1`
   on the other two, so any such statistic is structurally `Z2`-valued and can
   never distinguish three channels.* Falsifiable prediction: any future
   `+/-`-valued per-channel statistic in this project built from `Spin(8)` group
   elements will separate `1` channel from `2`, never `3`. Impact 6.
4. **New pearl from §8b:** *"the three `SO(4)xSO(4)` branchings are distinct" is
   generic to any `4+4` split and is NOT evidence about octonionic structure;
   only their triality-covariance is.* Guards against re-quoting a generic fact
   as a finding. Impact 5.
5. **Caveat-Gate entry:** canonicity of the `H/H-ell` split among the 7 Fano
   splits is named-and-untested (§5a, §6b).
6. **Methodological pearl:** a kill criterion that appends "…in which case X is
   confirmed" is two claims wearing one label; the test can fire while the
   appended conclusion is false (§9).

---

## 11. Check (reproduces this round's numbers)

```
cd tom_s3_spinor_toy/experiments/20260902-c135-triality-vs-round119-sign-structure
python -m ruff check c135_triality_vs_gamma_signs.py     # All checks passed
python c135_triality_vs_gamma_signs.py                   # ~80 s, writes results_c135.json
```

Expect: `step0.sha256 = ddc67bf9...8fe45`; `step1.matches_7_Fano_lines = true`;
`step2.matches_Klein_four_group = true`, failures `14.34/14.79/15.95/21.43`;
`step3.three_nontrivial_elements_form_one_3_cycle = true`;
`step5.D_A_centralizer` → `{6,3,3}`, `rel_resid 2.24e-15`, control `0.903`;
`step6b.n_DISTINCT_sign_patterns = 2`;
`step7.stabiliser_of_the_pattern_in_S3_order = 2`,
`VERDICT_z3_cyclically_permutes_the_sign_patterns = false`;
`step8.all_three_pairings_distinct = true`;
**`step8b.T4a_counter_CAN_report_less_than_3 = true`** and
**`step8b.T4b_distinctness_survives_a_NON_quaternionic_split = true`**;
`step9.claim_as_preregistered_is = "FALSE"`.

C133's `results_c133.json` is **not** modified (hash-checked temp copy, §4) —
verify with `git status`.

---

## 12. FL Step 8a — skeptic pass

One context-blind pass (claim.md + decision.md + code + JSON only, no session
history), per the Context Asymmetry Rule. Verdict **`[WEAKENED]`**. Full record
in `skeptic_verdict.md`.

Per claim.md's own scope note, a second differently-worded pass
(Paraphrase-Sensitivity Probe) is required only if the pass changes the
verdict's direction. **It did not** — it explicitly confirms every component of
the central mathematics, including a convention attack (twisted vs untwisted
adjoint) that it ran and that *failed* to break `rho_v(Gamma_A) = -D_A`. The
14 defects are about evidentiary framing, one stale number, and one real code
bug, all fixed or recorded above. Second pass therefore not run.

---

## 13. Evidence tier of this round's central conclusion

**Central conclusion:** *the triality `Z3` does not cyclically permute the
`(Gamma_A, Gamma_B)` sign patterns — that statistic is the image of a central
element of `Spin(8)` and is `Z2`-valued — while the same `Z3` does cyclically
permute the three sectors.*

**Tier: `[VERIFIED]` for the mathematics, HIGH confidence — carried at
`[WEAK]` as this round's own contribution**, per the FL Step 8a Response Matrix
for a `[WEAKENED]` verdict.

The split is deliberate and is the honest reading:

* **The mathematics is `[VERIFIED]`.** Every load-bearing number is machine-
  computed, `ruff` clean, residuals `0.0`–`3e-15` against controls failing at
  `0.903`–`22.99`. Both sides were rebuilt from **their own** primary sources.
  An independent adversarial pass tried three convention attacks on
  `rho_v(Gamma_A) = -D_A` and could not break it.
* **The round's own evidential contribution is `[WEAK]`**, because:
  * the negative half is **one-sided and largely definitional** — two of the
    three sign values are fixed by how the eigenspaces are cut, the third by a
    two-line identity (§8a);
  * the positive half is **measured to be generic** (§8b), so it is not
    evidence about this construction;
  * the one genuinely discriminating number (`0.903`) **replicates** a
    2026-07-15 result rather than establishing a new one;
  * §6's mechanism story is `[INFERRED]`, not `[VERIFIED]` (§6a).

  The *answer* to row 40 is nonetheless correct and now settled.

Further scope limits, none optional: the `S+`/`S-` labelling of the odd channel
is a convention; the result is **representation-theoretic only** and says
nothing about the physical Dirac operator, which C77/C78 already settled against
this route; canonicity of the `H/H-ell` split is untested; and L3b's conjectured
twist is neither found nor excluded.

**Independent Verification Strength Ladder.** The `{6,3,3}` replication is
**"Same model, isolated context" (Weak–Medium)**, *not* "independently-written
code" as the first draft claimed: C133 solves `δ(X∘Y) = δ(X)∘Y + X∘δ(Y)` with an
entrywise `(A1,A2,A3)` ansatz on a Cayley-Dickson octonion table, and the
2026-07-15 row solved `a(x)·y + x·b(y) = c(x·y)` on a Cayley-Dickson octonion
table — **the same equation in two notations, on the same algebra, by the same
linear-nullspace method**. Agreement is guaranteed by correctness of either, not
by independence. The only genuinely external check in this round is the
branching cross-reference to `hep-th/9804208`, which is **"independently-written
source"** — and §8b shows that particular fact is generic anyway. The Step 8a
skeptic sits at **"Same model, isolated context"**. No higher rung was reached,
and none is claimed.
