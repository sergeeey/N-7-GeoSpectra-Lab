# Round114 — Decision

**Date:** 2026-07-17
**Verdict:** `FALSIFIED__NOT_INDEPENDENT__REPRODUCES_FRIEDRICH_1980_VIA_AHL2023_CITATION__ONE_MODEST_NEW_FACT_SURVIVES`
(skeptic: math internally correct, but the headline "independent cross-check"
claim is FALSIFIED, not merely weakened — the strongest correction of any
round this session)

**Go/no-go:** the pre-registered kill criterion's PASS branch
("magnitude matches → genuine independent evidence") was **not actually
earned**. What was computed is arithmetically correct but is a restatement
of a well-known classical fact (round S³ Killing spinor eigenvalue `1/2`,
Friedrich 1980), not new independent confirmation of round67's own
`h_H=3` calibration.

## What was computed [VERIFIED-tool: sympy, this round]

Built the Clifford representation for `S³=SU(2)/{e}` from
`Agricola_Hofmann_Lawn_2023_invariant_spinors.pdf`'s own stated formulas
(§2.1-2.2), confirmed `{eᵢ,eⱼ}=-2δᵢⱼ` for all 9 pairs, used the paper's
own `Theorem 3.13`/`Corollary 3.14`/`Proposition 3.17` (round-metric
Killing eigenvalue `λ₁=λ₂=1/2`, and the `s`-parameter torsion family's
endomorphism `A^s_+`), and computed `D^s(ψ_+)=Σᵢeᵢ·A^s_+(eᵢ)·ψ_+ =
s/2-3/2` — **at `s=0` (Levi-Civita), magnitude `3/2`, matching round67's
own cited value; zero crossing at `s=3`.**

## Skeptic review [context-asymmetric: claim.md + code only] — FALSIFIED

**The central finding: `D` reduces to `-tr(A^s)`, nothing more.** Since
`A^s_+` is diagonal in the `{e₁}`/`{e₂,e₃}` split (eigenvalues `α(s)` on
`m₁`, `β(s)` on `m₂`), and `eᵢ²=-1` for every basis vector regardless of
which specific Lagrangian-pairing normalization was chosen, the
construction `D=Σeᵢ·A(eᵢ)·ψ = -Σλᵢ·ψ = -tr(A)·ψ` collapses to a **pure
trace computation** — the entire Clifford-matrix apparatus (building
`E1,E2,E3` explicitly, the sanity check) is **decorative**: it does not
add or remove any information relative to just summing AHL2023's own
already-stated eigenvalues (`α(0)+2β(0) = 1/2+2·(1/2) = 3/2` directly from
`Corollary 3.14`'s own number, no Clifford construction needed at all).

**Why the magnitude match is NOT independent evidence:** `3/2` is the
classical round-`S³` Killing-spinor Dirac eigenvalue, a textbook fact
traceable to Friedrich (1980) — the SAME fact round67 already cites via
this project's own established `[VERIFIED-sympy, G8/G4]` S³ Dirac spectrum.
AHL2023's `Corollary 3.14` is itself a restatement of this same classical
fact (every Killing-spinor classification paper on the round sphere states
it), not an independent derivation. **Both round67 and this round finding
`3/2` is two sources correctly citing the same known constant, not two
independent computations agreeing.** The skeptic's summary: "3/2 is not
suspiciously good — it is comparatively FORCED. Neither convention choice
[Lagrangian pairing, D-from-A construction] affects it. Any correct
reading of AHL2023 gives 3/2."

**The pre-registered kill criterion's own gate was not actually met:**
the claim.md's kill criterion required the magnitude match to be genuine
NEW evidence; since the derivation mechanically reduces to citing AHL2023's
own already-stated Killing constant, the "CONFIRMED, genuine independent
cross-check" branch was claimed without the underlying computation actually
routing through anything independent of what AHL2023 already states in one
line (`Corollary 3.14`).

## Applying the corrected verdict

**Recommended relabel** (accepted): `REPRODUCTION_OF_FRIEDRICH_1980_VIA_AHL2023_KILLING_CONSTANT`
— not `CONFIRMED_INDEPENDENT_MAGNITUDE_MATCH` as originally labeled by the
script's own printed verdict. The original label is WITHDRAWN, not
retained with a caveat — this is a genuine overclaim, not a narrowing.

## What survives (modest, honestly scoped)

1. **The zero-crossing `s=3` is a valid, newly-computed algebraic fact**
   from AHL2023's own Proposition 3.17 formula — not previously stated in
   that paper or derived anywhere in this project before this round.
2. **Whether AHL2023's `s` and round67's `t` (or round99/111/113's `t`)
   are the same parameterization remains explicitly untested** — this
   round's claim.md correctly disclaimed this in advance, and it is not
   resolved here. `s=3` is therefore a disconnected fact, not yet linked
   to round67's own `t=0,1` crossings.
3. **Genuinely new, if modest:** confirms AHL2023's own general
   `SU(n+1)/SU(n)` torsion-family machinery, when specialized to `n=1`
   (`S³`), gives a *mathematically available* zero-crossing — structurally
   consistent with (not independent proof of) round67's own finding that
   the Cartan-Schouten-type torsion family on `S³` generically admits such
   crossings. This is weak, correlative support at best, not confirmation.

## Kill Analysis

- **What this kills:** the round's own headline claim
  ("genuine independent cross-check of round67's h_H=3 calibration") —
  falsified, the computation does not constitute independent evidence.
- **What this does NOT kill:** round67's own `h_H=3`/zero-crossing result
  itself — untouched, this round neither confirms nor refutes it
  independently; it merely fails to add the confirmatory weight originally
  claimed.
- **What survives:** the disconnected `s=3` fact (see above), and a
  methodological lesson (below) about mistaking "cite a paper, get the
  paper's own known number back" for independent verification.

## Standing lesson (new pattern, worth flagging explicitly)

This is a genuinely different failure mode than prior skeptic corrections
this session (which mostly narrowed physics conclusions while keeping the
math intact, e.g. rounds 102/103/111/112). Here, the MATH computation
itself is fine, but it is **content-free relative to what it claims to
verify** — the elaborate Clifford-matrix construction reduces algebraically
to citing one already-published number and adding, giving no genuine
independent check despite the appearance of a substantial computation.
**Lesson for future OB1 rounds citing external literature for a
cross-check:** before claiming "independent confirmation," check whether
the computation's OWN output is derivable in one line directly from the
source's stated theorem, with no intermediate step adding information not
already in that one citation — if so, it is a restatement, not a
cross-check, regardless of how much correct arithmetic surrounds it.

## What this does NOT mean

1. Does NOT supply a parent action or resolve why `t=0,1` (or any specific
   crossing) is physically selected — genuinely untouched by this round.
2. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.
3. Does NOT establish or refute a relationship between AHL2023's `s` and
   this project's own `t` — an open question, not attempted here.

## Check (reproduces the arithmetic, though not the withdrawn interpretive claim)

```
cd experiments/20260717-round114-ahl2023-torsion-killing-spinor-crosscheck
python e36_ahl2023_crosscheck.py
```
Expect: `clifford_relations_confirmed=True`, `D_0_value=-3/2`,
`zero_crossings_in_s=['3']`. The script's own printed final label
(`CONFIRMED_INDEPENDENT_MAGNITUDE_MATCH...`) is SUPERSEDED by this
decision.md — the arithmetic reproduces correctly, but the label is
withdrawn per the skeptic review above.
