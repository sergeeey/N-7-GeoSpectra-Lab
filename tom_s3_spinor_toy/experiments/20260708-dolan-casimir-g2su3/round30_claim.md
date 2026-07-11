---
experiment_id: 20260708-dolan-casimir-g2su3
round: 30
date: 2026-07-11
tier: Full-Ladder
status: twice_reviewed_FL8a_skeptics_then_boyko_triangle_audit_C1-C2_confirmed_C3_downgraded_to_corroboration_C4_gap_found_and_closed_twice_via_STEP_Cprime_calibration_recheck_no_falsification
parent: round29 (found Ch_tilde==Casimir_su3 exactly as a "bonus finding",
  verified numerically but flagged as normalization-dependent, not
  structurally explained)
---

# claim.md — Round 30: `C̃h == Casimir_su(3)` is a STRUCTURAL consequence
of Agricola's Casimir definition, not a numerical coincidence

## Background

Round 29's C5 found `Ch_tilde == Casimir_su3` exactly as 8×8 matrices,
both equal `Id + X/3`. Both skeptics + synthesis downgraded this from a
"structural finding" to "a verified numerical identity in this project's
specific SU(3)-generator normalization" — correctly noting Agricola's
Prop 3.3 + known SU(3)-Casimir eigenvalues were not actually used to
derive it. This round attempts exactly that derivation.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — structural/representation-theoretic argument,
tested computationally at every step where a concrete fact is claimed.
NOT empirical, NOT causal.

## Construction (code: `g2su3_round30_ch_casimir_structural.py`)

**Core insight:** Agricola herself (page 10, immediately before Prop 3.3)
DEFINES `C̃h := -Σᵢ ẽad(Xᵢ)∘ẽad(Yᵢ)` for ANY `Qh`-DUAL bases `{Xᵢ},{Yᵢ}`
of `h`. If a basis is `Qh`-ORTHONORMAL (self-dual), this reduces to
`C̃h = -Σᵢ ẽad(Xᵢ)²` — i.e. `C̃h` **is**, by definition, the Casimir
operator of `h=su(3)` acting on spinors via Lemma 3.4's algebraic
representation. `Casimir_su3` (this project's own `-Σ su3_action(k,·)²`)
is constructed via the SAME type of object — `su3_action`'s own docstring
cites AHL2023 Remark 5.2's `ad(ν_i)|_m`, lifted via `clifford_mult_
bivector_direct`, exactly matching Parthasarathy's `ẽad` formula. So
`C̃h = Casimir_su3` follows IF `{ν_1,...,ν_8}` (this project's specific
su(3)-generator choice) is `Qh`-orthonormal.

**Logical chain** (full detail in the script's module docstring; REVISED
post-skeptic — see "Skeptic Verdict" below for what changed and why):
1. Agricola's `C̃h` definition, cited.
2. `g₂` is simple ⟹ its space of `Ad(G₂)`-invariant symmetric bilinear
   forms is 1-dimensional (standard Lie theory, cited) — so Agricola's
   `Q` is a scalar multiple of `B₀(X,Y):=Tr(ρ(X)^Tρ(Y))` for ANY faithful
   representation `ρ`.
3. **[VERIFIED, STEP A]** Using `g2su3_appendix_a_construction.py`'s
   `g₂⊂so(7)` construction (octonion/`rho`-generators, built in Round 13
   via a different concrete matrix realization than `su3_action`/
   `nabla_g` — see caveat below), `{ν_1,...,ν_8}` is FULLY `B₀`-
   orthonormal — ALL 64 pairs (`Tr(νₖ^Tνₗ)=δₖₗ`), not just the diagonal
   (previously the only documented fact, in `decompose_g2`'s own
   docstring).
4. **[VERIFIED, STEP B]** The FULL 14-dim `{ν_1,...,ν_14}` (all of `g₂`,
   including the 6 `m`-directions) is ALSO fully `B₀`-orthonormal —
   `B₀(e_p,e_p)=1` EXACTLY matches this project's metric convention
   (`⟨Z_p,Z_p⟩=1`, baked into `Z_i²=-1`), pinning the scalar in step 2 to
   exactly `λ=1` (not merely proportional).
5. Combining 3+4: `{ν_1,...,ν_8}` is `Qh`-orthonormal (`Q=B₀` exactly).
6. **[VERIFIED, STEP C — an INTERNAL CONSISTENCY CHECK, not the
   connecting step — see the SECOND correction below]** `ẽad(ν_k)`,
   Parthasarathy's spin-lift formula applied to the antisymmetrized
   matrix built from `SU3_GENERATORS[k]`'s own `(sign,a,b)` list, equals
   `su3_action(k,·)` EXACTLY, for all `k=1..8`. **This match is
   ALGEBRAICALLY FORCED for ANY `(sign,a,b)` table** (verified directly
   — see the FAKE-table computation in "Skeptic Verdict" below) via
   Clifford anticommutation, so it confirms `su3_action`'s coefficient
   normalization is a correctly-scaled instance of the general
   Parthasarathy recipe, but does NOT test whether `SU3_GENERATORS`'s
   specific entries represent the SAME abstract `ν_k` Appendix A's
   `ν(k)` represents.
6'. **[VERIFIED, STEP C' — the ACTUAL connecting step, added after a
   `/boyko-triangle-audit` pass found step 6 does not do this work]**
   RE-VERIFIED Round 13's own calibration (not merely cited from memory):
   Appendix A's `ν(i)` commutator action on its own `e(p)` matches
   `SU3_GENERATORS`/`AD_NU_M_BIVECTOR`'s `ad(ν_i)|_m` data EXACTLY, up to
   the already-documented sign convention, for ALL `8×6=48` `(i,p)`
   pairs. **This is what establishes** Appendix A's `{ν_1,...,ν_8}`
   (proven `Qh`-orthonormal, steps 3-5) and `su3_action`'s generators are
   the SAME abstract Lie algebra elements — not step 6.
7. `dim(m)=6` (even) ⟹ `C(m)⊗ℂ` has a UNIQUE irreducible 8-dim complex
   representation (standard Clifford-algebra fact, cited) — additional
   structural context, consistent with 6' but not independently
   load-bearing.
8. **[VERIFIED, STEP D — corroboration, not proof]** `-Σnu(k)²`
   (Appendix A) and `Casimir_su3` (`su3_action`) have the IDENTICAL
   eigenvalue spectrum `{0:×2, 4/3:×6}` — same multiset, differing only
   by WHICH basis index carries which eigenvalue. **Caveat (post-
   skeptic):** this spectrum match is EXPECTED from G₂→SU(3) branching
   theory (`Σ` decomposes as `1⊕3⊕3̄⊕1` on both sides regardless of
   realization details) and Casimir eigenvalues cannot distinguish `3`
   from `3̄` — so this is real, independent corroboration from a SECOND
   concrete construction, not proof of operator isomorphism by itself.
   The eigenvalue `4/3` matches the STANDARD, literature quadratic-
   Casimir eigenvalue of SU(3)'s fundamental representation (external
   cross-check).
9. Conclusion: `C̃h = -Σₖ ẽad(νₖ)² = -Σₖ su3_action(k,·)² = Casimir_su3`
   (by 1+5+6', NOT by 6+7+8, which are consistency checks/corroboration
   only).

**STEP E (sanity cross-check):** the structural argument's PREDICTION is
verified against Round 29's already-established numeric fact
(`Ch_tilde == Casimir_su3`) — match, confirming the argument is
consistent with (not contradicting) the empirical finding it explains.

## Falsifiable Claims

**C1:** `{ν_1,...,ν_8}` (Appendix A's independent g₂⊂so(7) realization)
is fully `B₀`-orthonormal — all 64 pairs, not just the 8 diagonal ones.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP A). This
is a STRONGER, newly-verified fact than what was previously documented
(`decompose_g2`'s own docstring only claimed the diagonal).

**C2:** The FULL 14-dim `{ν_1,...,ν_14}` (all of `g₂`, h+m) is fully
`B₀`-orthonormal, with `B₀(e_p,e_p)=1` matching this project's metric
convention exactly.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP B).

**C3 (REVISED post-skeptic — demoted from "step 6 evidence" to
"corroboration"):** `-Σₖnu(k)²` (Appendix A) and `Casimir_su3`
(`su3_action`) have the IDENTICAL eigenvalue spectrum, and the
fundamental-piece eigenvalue is `4/3` (matching the standard SU(3)
literature value).

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP D).
**Downgraded framing (both skeptics independently flagged this):** this
spectrum match is EXPECTED from G₂→SU(3) branching theory and cannot by
itself distinguish `3` from `3̄` (Casimir eigenvalues are the same for
both) — it is real, independent corroboration from a second construction,
NOT proof of the operator isomorphism the original version implied.

**C4 (the headline conclusion; TWO gaps found and closed in sequence —
see "Skeptic Verdict" below for the full history):** `C̃h = Casimir_su3`
follows STRUCTURALLY from Agricola's own Casimir definition applied to
the (verified) `Qh`-orthonormal basis `{ν_1,...,ν_8}` — not a numerical
coincidence specific to this S⁶ geometry.

RESULT: `[VERIFIED-tool]` for C1/C2 (orthonormality) + **[VERIFIED-tool]**
for the ACTUAL connecting link, step 6': Appendix A's `ν(k)` and
`SU3_GENERATORS` represent the same abstract elements, re-verified via
Round 13's own calibration re-run inside this round's own script (STEP
C') + `[VERIFIED-tool]` for step 6 (`ẽad(ν_k)=su3_action(k,·)` exactly,
STEP C — retained as a true but ALGEBRAICALLY-AUTOMATIC consistency
check, NOT the connecting step, after this framing was itself found
wrong by `/boyko-triangle-audit`). `[INFERRED]` for steps 1,2,7
(standard, cited Lie theory, not independently re-derived from scratch).
Cross-checked against the empirical fact it explains (STEP E) —
consistent.

## Kill Conditions

- C1/C2 killed if: skeptic finds `nu(k)` secretly imports/depends on
  `su3_action`/`nabla_g`/`LEVI_CIVITA_NOMIZU` anywhere (would make the
  "independent construction" claim false, undermining the corroboration
  value) — verify `g2su3_appendix_a_construction.py`'s only module-level
  import is `sympy`, nothing from `g2su3_twisted_kernel.py` or
  `g2su3_explicit_clifford.py`. **(Checked by both skeptics + synthesis
  via direct grep: confirmed true — module-level import is `sympy` only;
  one in-`main()`-only import of `g2su3_H_element` does not affect
  `nu()`/`NU`, which are fully defined before that line.)**
- C3 killed if: skeptic finds the eigenvalue match is coincidental rather
  than genuine corroboration — **addressed**: both skeptics correctly
  noted the match is EXPECTED from branching theory (not surprising), so
  its value is as an independent sanity check on the normalization, not
  as proof of anything beyond that.
- **C4's logical chain was found weak TWICE, in sequence, by two
  DIFFERENT review passes:**
  - **Round 1 (FL Step 8a, both skeptics independently):** the original
    chain relied on Clifford-module uniqueness as load-bearing — too
    weak, gives only an ABSTRACT isomorphism, not the SPECIFIC operator
    identity needed. **FIXED (STEP C):** a direct computation builds
    Parthasarathy's `ẽad(ν_k)` from `SU3_GENERATORS`+`e_action` and
    confirms it equals `su3_action(k,·)` EXACTLY.
  - **Round 2 (`/boyko-triangle-audit`, run AFTER both skeptics had
    already approved Round 1's fix):** found STEP C's "exact match" is
    ALGEBRAICALLY FORCED for ANY `(sign,a,b)` input table — verified
    directly by re-running STEP C's logic with a FABRICATED, arbitrary
    bivector table and confirming it STILL produces an exact match
    (`ead_parthasarathy == su3_action-clone? True` on fake data). Neither
    skeptic caught this (same-model-family blind spot — exactly what
    this project's own cross-model-review guidance exists to catch).
    **FIXED (STEP C'):** re-ran Round 13's OWN calibration (Appendix A's
    `ν(i)` commutator action on `e(p)` vs `SU3_GENERATORS`/
    `AD_NU_M_BIVECTOR`) inside this round's own script — confirmed
    exactly, 48/48 pairs — and this, not STEP C, is now documented as
    the actual connecting fact.

## What this does NOT mean

- Does NOT independently re-derive g₂'s simplicity or the uniqueness of
  the 8-dimensional irreducible Clifford module for `dim m=6` from first
  principles — these are STANDARD, textbook facts, cited rather than
  proven from scratch (analogous to how this whole project already relies
  on, e.g., sympy's linear algebra being correct, or Agricola's own
  Theorem 3.2 proof being valid).
- Does NOT change any previously-established spectrum, index, eigenvalue,
  or Diff value from Rounds 4-29 — this round explains an ALREADY-
  established fact (Round 29's C5) structurally, it does not compute
  anything new about the physics.
- Does NOT generalize beyond THIS specific `su3_action`/AHL2023-Remark-
  5.2 generator choice — a DIFFERENT (still valid) choice of su(3)
  generators would give a DIFFERENT-LOOKING `Casimir_su3` construction,
  though the SAME abstract Casimir operator (this is precisely the point
  of the "basis-independence of Casimir operators" argument, but it's
  worth being explicit this round is about THIS project's specific
  generator choice, not a universal restatement).
- Does NOT resolve the preprint's `8/45 vs ~1.03` norm-ratio tension or
  which of `M_p`/`Z_p` the preprint's own L4A convention intends — same
  standing open questions as Rounds 26-29.
- **Does NOT mean Appendix A's `nu(k)` and `su3_action`'s Remark-5.2 table
  are two independent LITERATURE sources** — they are the SAME AHL2023
  table (`AD_NU_M_BIVECTOR` and `SU3_GENERATORS` are byte-identical),
  realized via two different concrete matrix constructions (rho/octonion
  products vs direct bivector lift). "Independent" throughout this round
  means independent construction method, not independent data.
- **Does NOT mean Appendix A's `nu_8` was independently transcribed** —
  unlike `nu_1..nu_7` (verbatim page reads), `nu_8` was back-solved from
  a calibration equation (that file's own inline comment). This narrows,
  but does not void, `nu_8`'s contribution to STEP D's corroboration.

## Skeptic Verdict (FL Step 8a, 2026-07-11, two independent context-blind
skeptics + a tool-verified synthesis pass that independently re-ran the
script AND independently implemented and verified the fix both skeptics
identified as needed)

| Claim | Verdict | Note |
|---|---|---|
| C1 | CONFIRMED-REAL (both + synthesis, via direct grep) | `g2su3_appendix_a_construction.py`'s only module-level import is `sympy` — independence of CONSTRUCTION confirmed. Caveat: `AD_NU_M_BIVECTOR`/`SU3_GENERATORS` share the same literature table (not independent data); `nu_8` was back-solved, not verbatim. Neither caveat affects the orthonormality computation itself. |
| C2 | CONFIRMED-REAL (both) | 196/196-pair check re-confirmed by synthesis's own fresh run; `λ=1` pinning chain valid given C1+g₂-simplicity. |
| C3 | CONFIRMED-REAL as a fact; framing WEAKENED → downgraded (both) | Spectrum match re-confirmed, but demoted from "evidence for isomorphism" to "corroboration" — both skeptics independently noted Casimir eigenvalues can't distinguish `3` from `3̄`, so the match is expected from branching theory, not surprising. |
| C4 | **WEAKENED (round 1)** → fixed → **WEAKENED again (round 2)** → **CONFIRMED-REAL (fixed, re-verified)** | Two independent review passes, in sequence, each found a real gap in the SAME claim's proof route (not the claim itself, which held throughout). See "Second Review Pass" below for round 2. |

**FL Response Matrix, round 1 (FL Step 8a):** No claim was FALSIFIED.
C4's WEAKENED verdict (found independently by BOTH skeptics — a strong
signal the gap was real) was resolved as a **Fix**: the original chain
used Clifford-module uniqueness as load-bearing, too weak (abstract
isomorphism, not a specific operator identity). Synthesis implemented
the fix both skeptics proposed — `ẽad(ν_k)` built directly from
`SU3_GENERATORS`+`e_action`, confirmed EXACT match for all k=1..8 (STEP
C) — and this was committed to the script as (at the time) the PRIMARY
proof mechanism.

## Second Review Pass (`/boyko-triangle-audit`, run independently AFTER
round 1's fix had already been approved by both skeptics and the
synthesis agent)

The triangle-audit tool found that round 1's fix (STEP C) does NOT
actually do the connecting work it was credited with: `ead_parthasarathy`
and `su3_action` are built from the SAME `SU3_GENERATORS[k]` list via two
bookkeeping schemes that Clifford anticommutation (`Z_aZ_b=-Z_bZ_a`)
FORCES to agree, for ANY input data — so STEP C's "exact match" tests
`su3_action`'s normalization consistency, not whether `SU3_GENERATORS`
represents the same abstract elements Appendix A's `ν(k)` does.

**Independently re-verified** (not just accepted from the audit's
narrative): ran STEP C's exact logic with a FABRICATED, arbitrary
`(sign,a,b)` table and an arbitrary coefficient (not `1/2` or
`1/(2√3)`) — the match STILL held exactly:
```
With a FAKE, arbitrary (sign,a,b) table and arbitrary coeff:
  ead_parthasarathy == su3_action-clone? True
```
This definitively confirms the audit's finding: STEP C is algebraically
vacuous as a check on `SU3_GENERATORS`'s specific content.

**Root cause of the miss:** both FL Step 8a skeptics (and the synthesis
agent) are the same underlying model family — this project's own
CLAUDE.md explicitly flags this exact failure mode ("reviewer + sec-
auditor are BOTH Claude = shared blind spots... different model = no
confirmation bias on Claude's own code") for code review; this round
shows the SAME principle applies to mathematical-argument review, not
just code review.

**FIXED (STEP C'):** re-ran Round 13's OWN calibration — Appendix A's
`ν(i)` commutator action on its own `e(p)`, checked against
`SU3_GENERATORS`/`AD_NU_M_BIVECTOR`'s `ad(ν_i)|_m` data — inside THIS
round's own script (not merely cited from memory), confirmed exactly for
all 48 `(i,p)` pairs. This IS the fact that connects Appendix A's proven
`Qh`-orthonormal `{ν_1,...,ν_8}` to `su3_action`'s generators. STEP C is
RETAINED in the script (a true, non-vacuous fact about `su3_action`'s
internal normalization consistency) but explicitly RELABELED as an
internal consistency check, not the connecting step.

**Caveat on STEP C' itself:** for `k=8` specifically, Appendix A's own
`ν_8` was BACK-SOLVED from exactly the equation STEP C' checks (that
file's own inline comment) — so for `k=8`, STEP C' re-verifies internal
consistency rather than providing an independent confirmation. `k=1..7`
ARE genuinely independent (verbatim page transcriptions checked against
a table built via a completely different method).

**Overall:** the round's headline result — `C̃h = Casimir_su3` is a
structural, not coincidental, consequence of Agricola's own Casimir
definition — survives BOTH review passes, on a STRONGER footing than
originally submitted after either pass alone:
the proof mechanism is now a direct, computable, on-`Σ` identity (STEP C)
rather than an appeal to abstract representation uniqueness. Round 29's
C5 does NOT need to revert to "verified numerically, not structurally
explained" — the gap that would have justified that reversion has been
closed with tool-verified evidence.
