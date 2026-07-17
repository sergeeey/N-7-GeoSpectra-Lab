# Decision — G16-T3R-FROM-K3

> **⚠️ CORRECTION (2026-07-17, added retroactively — original text below
> unchanged):** the line 9 statement "`K₃` is the Cartan generator of
> `SO(6)⊃SU(3)` on `S⁶`" is **wrong** and directly contradicts this
> experiment's own script (`g16_t3r_k3.py`, which builds `K3_32 =
> kron(K_S3[2], I8)` — explicitly S³-side, "trivial on S⁶", and whose own
> docstring frames the whole experiment as testing whether "`K₃`
> eigenvalues give `T3R=±1/2`"). `K_3` and `T_{3R}` are the SAME operator,
> proven by direct matrix computation (`experiments/20260717-round93-
> charge-operator-representation-lift/decision.md`). This wrong line
> propagated verbatim into `preprint_draft.md` and then `preprint.tex`
> (now corrected there too). The numeric result below (`Y` values, PASS)
> is unaffected — only this one line's description of `K_3`'s geometric
> origin was wrong. This note is additive; nothing below has been altered.

**Date:** 2026-06-19  
**Verdict:** PROMOTE  
**Go/no-go:** GO

## Result
PASS_G16_Y_GEOMETRIC — Y = K₃ + (B−L)/2 fully geometric; right-handed SM generation + CPT conjugates verified.  
K₃ is the Cartan generator of SO(6)⊃SU(3) on S⁶; B−L from K₃ via Pati-Salam. All Y values match SM for one right-handed generation.

## Scientific significance
Y is geometrically identified with a specific combination of S⁶ isometry generators. No additional U(1) needs to be postulated — hypercharge is already there in the S⁶ holonomy structure.

## Caveats
- Right-handed generation only; left-handed requires S³ contribution (G17)
- Does NOT explain why Y takes specific rational values (this follows from G14 color structure)
