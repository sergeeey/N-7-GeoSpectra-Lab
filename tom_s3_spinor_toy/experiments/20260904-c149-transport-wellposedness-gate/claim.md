# C149 — is OB11(ii)'s never-attempted next step well-posed, or a gauge artifact?

## L0 gate (EstimandOps)

**Question type:** Descriptive (well-posedness of a specified construction).
Not causal, not predictive.

## Trigger — an actual debt, found by auditing open blockers

User left for ~5h with instruction to work autonomously on existing
hypotheses and outstanding debts. Auditing `OPEN_BLOCKERS.md` surfaced a
step that is **named but has never been attempted**: OB11(ii)
(`OPEN_BLOCKERS.md:1782-1791`) specifies transporting `D`, `J`, `γ` through
the intertwiner `U` found in C70, then testing whether a Hermitian,
Clifford-compatible combined operator can be built. C72's own
`does_not_imply` records this as explicitly deferred.

**The unexamined problem:** C70's OWN `does_not_imply` states that `U` is
not unique — *"Inn(su(3)) acts transitively on the solution family (~8-real-
dim continuous orbit); C71 must fix one representative and use it
consistently."* C142 (2026-09-04) independently re-derived this and
sharpened it to "basis-matching GAUGE freedom, not independent data."

Nobody asked whether the planned test's OUTCOME depends on which
representative is picked. If it does, the test is ill-posed and any round
built on it would produce a gauge artifact.

## Falsifiable claim

**Criterion (proved, one line):** if `U' = U·g` for `g` in the residual
freedom, then `U'OU'⁻¹ = U(gOg⁻¹)U⁻¹`, so the transported operator is
representative-independent **exactly when** `gOg⁻¹ = O`, i.e. when `O`
commutes with the residual freedom's generators. Here that freedom is the
`su(3)` action, so:

> transport of `O` is well-posed ⟺ `[O, ρ_su3(a)] = 0` for all 8 generators.

**Claims to test:**
1. `D_Σ` (round59's own untwisted Dirac) satisfies the criterion, hence its
   transport is representative-independent.
2. `γ` (the `EVEN_IDX`/`ODD_IDX` chirality grading) likewise.
3. A random non-equivariant operator does NOT — the negative control must
   show order-1 gauge-dependence, or the test discriminates nothing.
4. The criterion and the directly-measured invariance agree in every case
   (i.e. the criterion is not merely asserted but confirmed as predictive).

**Kill criterion:** if `D_Σ` or `γ` shows gauge-dependence, OB11(ii)'s step
is ill-posed as specified for that operator and must be re-specified before
any round is built on it. If the negative control shows NO gauge-dependence,
the whole test is non-discriminating and its result must be discarded.

## Why this is cheap today and was not three weeks ago

C146 (2026-09-04, earlier this session) proved `D_Σ` is `SU(3)`-equivariant
— a fact never verified standalone anywhere in this project before today.
That is precisely the input this well-posedness question needs. Today's
theorem retroactively settles the status of a step planned on 2026-08-10.

## What this does NOT mean

1. Does NOT run OB11(ii)'s actual transport test — it only establishes
   whether that test is well-posed. The Hermiticity/Clifford-compatibility
   question itself remains untouched and open.
2. Does NOT settle `J`. `J` is not constructed in round59's own file; its
   `su(3)`-equivariance must be checked separately before this conclusion
   may be extended to it. Named explicitly, not silently folded in.
3. Does NOT re-open the user's 2026-08-11 deferral of OB11(ii) — this round
   answers a *prerequisite* question about that step, it does not execute it.
4. Does NOT change `N_gen=3`'s CONDITIONAL status, nor any registered value.
5. Does NOT claim the residual freedom is exactly `Inn(su(3))` as a group —
   it uses the `su(3)`-generated subgroup as the freedom actually reachable
   by C70's own construction, which is what the criterion needs; a larger
   residual freedom (if one existed) would require re-checking.
