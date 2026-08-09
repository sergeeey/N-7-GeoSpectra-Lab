# Repo-wide Clifford convention audit — no second math error, one systematic label bug

**Date:** 2026-08-10
**Verdict:** `NO_NEW_MIXING__ONE_SYSTEMATIC_LABEL_INVERSION__REGISTRY_WRITTEN`
**Closes:** the open next-check on the 2026-08-09 pearl
(*"repo-wide convention audit NOT yet run — OB10 was the first round to hit
this, it will not be the last"*), and item (a) of `activeContext`'s open list.

## The question

C32 found that OB10 mixed two opposite Clifford sign conventions. The pearl it
generated said the obvious follow-up had not been run: **where else in this
repo do the two conventions meet?**

## Answer, in one line

**Nowhere else.** The only two files in 370 that combine both conventions are
OB10's original and OB10's correction. But the audit found a different problem
that the sign question was hiding.

## What was actually run

Three passes over `experiments/` + `scripts/` + `tests/` (370 `.py` files),
then a computed check of every label the passes disputed.

| pass | question | result |
|---|---|---|
| 1 | what sign does each file **assert** (not what its prose says)? | 20 `Cl(0,n)`, 6 `Cl(n,0)`, 4 carrying both |
| 2 | of those carrying both — do they **combine**, or only mention? | 2 combine, both are the OB10 pair |
| 3 | does any cross-directory import **cross** the boundary? | **none** |

**Negative control:** the scanner must independently re-find the two known
mixed files. It does — both classified `MIXED`. A scan reporting zero mixed
files would have been a broken scanner, not a clean repo.

## The finding the sign question was hiding

`Cl(p,q)` means **two opposite things** in this repo:

```
round67 (S3):      Z_i = i*sigma_i,   Z_i^2 = -1   labeled Cl(0,3)   correct
s6-harm-g0 (S6):   Gamma_a hermitian, G_a^2 = +1   labeled Cl(6,0)   correct
g68/round34 (oct): L_i (Fano table),  L_i^2 = -1   labeled Cl(7,0)   WRONG
g69 (CSDR):        no generators built             "Cl(6,0) = M8(R)"  WRONG
```

The octonion and CSDR rows are **label bugs, not math bugs**. Every matrix and
every result there is correct. But the same label `Cl(n,0)` now means `e²=+1`
in one corner of the repo and `e²=−1` in another — which is exactly the
ambiguity a future round tensoring across sub-projects would resolve wrongly.

**And it is not hypothetical: the repo already contains both names for the same
object.** `g101` and `g102`, which build directly on `g68`'s matrices, write
`Cl(0,7)` and `Cl(0,8)` — correctly. Someone silently fixed the label
downstream and never fixed the source. `g102`'s own comment records that it
caught an anti-homomorphism from the sign on its first run (`residual 9.4`).

## How the labels were adjudicated [VERIFIED-numpy]

Computed, not recited from a periodicity table.

**n=7.** The pseudoscalar `ω = e₁…e₇` is central with `ω² = −ε⁷`. So `ε=−1`
gives `ω²=+1` and the algebra **splits** as `M₈(ℝ)⊕M₈(ℝ)` (`ω = ±I` picks the
summand); `ε=+1` gives `ω²=−1`, no real split. `g68`-D4 and `round34` both
claim the split — available only at `ε=−1`. Rebuilt the Fano `L_i`
independently: `L_i² = −1`, all 21 pairs anticommute, `ω = ±I` (reproducing
`g68`'s own `Ω_L`/`Ω_R` result). Contrast control: `i·L_i` (a true `Cl(7,0)`)
gives `ω² ≠ +I`.

**n=6.** The pseudoscalar does not discriminate (`ω² = −1` for both signs), so
the commutant does:

```
eps=+1 (a true Cl(6,0))  ->  J = s2(x)s1(x)s2 ... J^2 = -1  ->  M4(H)
eps=-1 (Cl(0,6))         ->  J = s1(x)s2(x)s1 ... J^2 = +1  ->  M8(R)
```

`M₈(ℝ)` belongs to `Cl(0,6)`. `g69`'s constant carries the other label.

## One near-miss worth recording

The `n=6` result **looked like it contradicted C33**, which had just found
`B_S6 conj(B_S6) = −I` (quaternionic) on the same uniformised generators where
this audit finds `J² = +1` (real). Checked before writing either down:

| | condition | measures |
|---|---|---|
| commutant `J` | `J conj(Γ) = +Γ J` | type of the **algebra** |
| charge conjugation `B` | `B conj(Γ) = −Γ B` | reality type of the **module** |

Verified explicitly: C33's `B` does **not** commute (it anti-intertwines), and
the audit's `J` does. Different objects, different questions, both correct, no
contradiction. Recorded because "two adjacent objects, one of them assumed" is
the same shape as the error that started this whole chain.

## My own scanner's false positive, and the fix

The first pass flagged `g102_spin8_fiber.py` as `MIXED`. It is not. Its check
reads

```python
ac = gi @ gj + gj @ gi + 2.0 * (1.0 if i == j else 0.0) * ident   # required == 0
```

which asserts `{G,G} = −2δ` — the **negative** convention, despite the visible
`+2`. **A residual-form check reads backwards.** Caught by opening the file the
scanner accused rather than trusting the accusation
(`audit-verification-gate.md`); added `RESIDUAL_FORM_RE` and re-ran, and `g102`
moves to `NEG_Cl(0,n)` with the negative control still passing. Worth stating
plainly: an audit tool's own verdict needs the same verification discipline as
the thing it audits.

## Deliverable

`docs/clifford_convention_registry.md` — the canonical table, the computed
adjudication, the `J`-vs-`B` warning, and five rules for future rounds. This is
what the audit was actually for: the sign fact was already known from C32; what
was missing was a place to look it up.

## What this does NOT establish

1. **Does not verify every one of the 370 files by hand.** Passes 1–3 are
   regex+AST heuristics over asserted anticommutator targets. A file that
   builds Clifford generators without ever asserting the relation would be
   invisible to the scan. The scan found 30 files that assert it; a
   construction that never checks its own algebra is a different (and worse)
   problem, not covered here.
2. **Does not change any result.** No number, no verdict, and no claim in any
   audited experiment moves. The label corrections are naming only.
3. **Does not fix `tests/`.** `tests/test_g68_octonion_channels.py` (10
   occurrences) and `test_g69_csdr_coset.py` (3) carry the inverted label in
   prose while asserting the correct relation. `tests/` is write-protected in
   this session; listed in the registry for a future pass.
4. **Does not rewrite history.** `decision.md` / `claim.md` files keep their
   original text per this repo's retract-in-place convention; the registry
   lists them and the affected source files carry a pointer.
5. **Says nothing about `l3b-so4xso4`'s `Cl(8)`**, which is unsigned in its
   label and `+1` in its code. Not wrong, just underspecified — flagged
   `⚠️ ambiguous` in the registry rather than called an error.

## Check

```
python experiments/20260810-clifford-convention-repo-audit/clifford_convention_scan.py
python experiments/20260810-clifford-convention-repo-audit/label_vs_code_check.py
```
Expect: pass 3 empty; negative control passes (both OB10 files `MIXED`);
`VERDICT: THREE_NAMING_STATES_FOUND__ONE_LABEL_BUG__NO_NEW_MATH_ERROR`.
