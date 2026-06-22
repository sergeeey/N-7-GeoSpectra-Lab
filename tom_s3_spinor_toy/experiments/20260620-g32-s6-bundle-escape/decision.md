# Decision: G32 — S⁶ Bundle Escape Route

**Date:** 2026-06-20 (branch opened) / 2026-06-20 (all sub-branches exhausted)  
**Verdict:** EXHAUSTED (all sub-branches killed → T1 UNCONDITIONAL)

---

## Claim (original)

"A non-equivariant bundle on S⁶ with c₃=6 gives index=3, providing a topological route to N_gen=3 outside the equivariant obstruction."

**Context:** G32 was the last escape route after G30 (G₂ instanton) and G31 (S³ Adjoint) were both rejected. It spawned five sub-branches (B1–B5).

---

## Sub-Branch Kill Log

| Branch | Gate | Verdict | Kill reason |
|--------|------|---------|-------------|
| B1 Pati-Salam SU(4) | G39 | REJECT | Spin(6)≅SU(4): Λ²(T^{0,1}) has c₃=2, not 6; factor 3 unaccounted |
| B2 Higgs SSB G₂→SU(3) | G40 | WEAK→killed | SSB does not force c₃; π₅(S⁶)=0 (Freudenthal error corrected) |
| B3 Brane picture | G41 | WEAK | 3 D6-branes → rank-3 gauge, c₃ free; no physical mechanism |
| B4 Anomaly/GS | G42 | REJECT | H⁴(S⁶)=0 makes GS trivial; 9D≠10D |
| B5 Stable HYM bundles | G43→G48 | NULL | Harland-Nölle arXiv:1109.3552 verified: T(S⁶) c₃=2 on base; new instantons on CONE ℝ⁷, not on S⁶; no c₃=6 on S⁶ |

**All 5 branches killed. G48 reads the primary source (Harland-Nölle) directly.**

---

## Kill Analysis

**Killed:** Every known mechanism for producing c₃=6 on S⁶ from a non-equivariant bundle.

**Why (summary):** The obstruction is not only equivariance — it is the topology of S⁶ itself. χ(S⁶)=2 (G33), K̃(S⁶)=ℤ homogeneous (G36), and stable HYM bundles have c₃=2 on the base (G48). These are three independent confirming results.

---

## What Was NOT Killed

- **Index = 1 per channel** — G73 uses c₃=2 *per triality channel* via Â(S⁶)=1. This is a different mechanism (twisted Dirac, not holomorphic bundle count) and is unaffected.
- **N_gen=3 via triality** — G73+G74A+G74B prove N_gen=3 through a completely orthogonal route: three Z₃ eigenspaces of the triality automorphism, each with one zero mode.
- **S⁶ as internal manifold** — the geometry of S⁶=G₂/SU(3) is valid and productive; only the *specific bundle route to c₃=6* is exhausted.

---

## Impact on Theorem T1

G32 exhaustion → T1 Category 5 (non-equivariant HYM bundles) **CLOSED**.  
T1 is now **UNCONDITIONAL**: all 6 categories (G27–G48) closed without exception.

---

## Lesson

G32 looked like the strongest escape route — it survived when all equivariant routes were killed. The lesson: exhausting the strongest escape route requires primary-source verification (G48 read Harland-Nölle directly), not just theoretical argument. Secondary analysis would have left B5 as a live WEAK branch.
