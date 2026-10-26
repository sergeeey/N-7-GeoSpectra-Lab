# G94 action and flux-identity gate — 2026-10-27

**Status: UV-BLOCKED for a physical wrapped Euclidean D2 sector in the frozen 13D model; separate conditional topological obstruction if S3 carries NS–NS H3.** Evidence-only supplement to draft PR #9. Original `main` code and tracker remain unchanged.

## Primary repository evidence

- `preprint.tex` ~L987–991 explicitly says the effective potential is **supergravity-inspired by analogy** and that no consistent 13D supergravity is claimed; ~L1412–1456 acknowledges absent 13D parent action. `PARENT_ACTION_GATE.md` F6 agrees: no derived background equations of motion from an action.
- The project's **G102 already derived** the conditional `c_S3=1/(2*g_s)` on 2026-07-01 (`experiments/20260701-g102-cs3-dbrane-normalization/decision.md`). This is existing project prior work, not a new result of this audit. It fixes the exponent slope only; it does not derive the 4D prefactor, brane phase, zero-mode measure, sign, or parent action.
- The later `20260715-round63-wrapped-s3-instanton-channel` calculation is a **different**, one-field `lambda(rho6)` channel; it also does not supply a parent action or justify G94's bare positive potential contribution.
- **Flux provenance mismatch:** `experiments/20260621-g54a-freund-rubin/claim.md` explicitly uses **quantized F6 on S6** to get `Vflux=q6²*Vol(S3)/(2*Vol(S6))`. `preprint.tex` ~L987–995 calls the underlying mechanism a **3-form flux on S3** and ~L1117–1120 says the quantized harmonic 3-form's energy scales as `Vol(S3)/Vol(S6)`. For fixed 3-form period that is incorrect. `experiments/20260621-g55-two-flux-2d/decision.md` also distinguishes F3 on S3 and F6 on S6.

## Exact kinetic-energy check (before 4D Weyl rescaling)

On `X=S3(r3) × S6(r6)`, let `V3=2π²r3³`, `V6=16π³r6⁶/15`, and normalized unit-integral volume forms `omega3=vol3/V3`, `omega6=vol6/V6`. With **fixed integer charges** `q3,q6`:

```
F3=q3*omega3:
  (1/2)∫_X F3∧*F3 = q3²*V6/(2*V3) = (4π/15)*q3²*r6⁶/r3³.
F6=q6*omega6:
  (1/2)∫_X F6∧*F6 = q6²*V3/(2*V6) = (15/(16π))*q6²*r3³/r6⁶.
```

SymPy independent check: 7/7 exact equalities or inequalities PASS. At unit radii and charges, E3=0.837758, E6=0.298416. This is the direct F6 match to G54A. If `F6=*9 F3`, then `q6=q3*V6/V3` and the dual charges cannot simultaneously be independently fixed while freely varying both radii without extra conditions. A duality statement must explicitly distinguish its choice of quantized flux.

## Conditional Freed–Witten gate

A single closed Euclidean D2 wrapping `W=S3` in **ordinary Type IIA** must satisfy `W3(W)+[H_NS]|W=0∈H³(W,Z)`. Since S3 is spin, `W3=0`; if the preprint's quantized 3-form is a **nonzero NS–NS H3 flux through the same S3**, `[H_NS]|W≠0`, making that isolated instanton anomalous. This is the established Freed–Witten mechanism, not a new no-go result: https://arxiv.org/abs/hep-th/9907189 and https://www.slac.stanford.edu/pubs/slacpubs/12250/slac-pub-12266.pdf.

**Do not assert a universal obstruction:** G54A uses F6 through S6, which by itself does **not** establish nonzero H_NS on S3. In the F6-only scenario with `H_NS|S3=0`, this particular anomaly condition is satisfied. However ordinary IIA is 10D and the frozen background is 13D, so neither case derives a D2-brane sector for the actual project. The preprint's 3-form identity and source must be specified before choosing the FW branch.

## Action and decision

**Suggested status:** `G94 = PHENOMENOLOGICAL_TOY / UV-BLOCKED` pending a parent action. Separate claims: `F3/F6 fixed-flux energy identification = REFUTED as written`; `isolated E2 + nonzero NS H3 on S3 = REFUTED-CONDITIONAL`; `F6 only, H_NS=0 = no FW obstruction but sector UNDERIVED`.

**Single cheapest discriminating question:** Which exact gauge field carries the S3 3-form flux in the preprint, and what are its kinetic term, quantized period and relation (if any) to the G54A F6 field? Once answered, check NS–NS H3, anomaly cancellation, 13D-to-Type-IIA embedding, E2 zero modes and scalar-potential generation **before any new numerical c/A scans**.

Independent execution and complete report: local standalone SymPy `verify_flux_duality.py` (no project code executed), plus scientific decision in the associated ChatGPT research artifact. This PR entry is evidence only; do not interpret it as a proven universal no-go or a physical calculation in a completed 13D theory.
