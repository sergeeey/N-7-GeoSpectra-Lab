# decision — the KO tuple, and the Pin choice that turned out not to matter

**Verdict:** `C57_REFUTED_AS_WORDED__PIN_CHOICE_CANCELS__C56_U5_CORRECTED` → **C57**.
**Date:** 2026-08-10 · L0: descriptive · ruff clean · `results_ko.json` persisted.

---

## The correction is to my own C56

C56's `U5` said: *"`J` is antilinear, so `J(cX)J⁻¹ = c̄·JXJ⁻¹`, and `c̄/c` is `+1` for real
`c`, `−1` for imaginary `c`. **The `ε''` sign of the KO tuple flips with the choice.**"*

**It does not.** That accounting looked only at the phase `γ` carries and never asked what
`J_M` does to `U_ι`.

Write `U_ι = c'·W` with `W` the **real** swap. C56's own condition (`γ† = γ`, `γ² = I`)
forces `c·c' = ±1`, so

```
γ = c·U_ι ⊗ s1 = (c c')·W ⊗ s1 = ±(W ⊗ s1)
```

— **the same real operator for both Pin choices** [VERIFIED-numpy]. And because `γ` is
real, `JγJ⁻¹ = M γ M⁻¹` carries no phase at all. The `c̄/c` flip is exactly compensated by

```
η = J_M U_ι J_M⁻¹ / U_ι = c̄'/c'
```

| | `c̄/c` | `η` | net |
|---|---|---|---|
| Pin⁺ (`U_ι² = +1`) | `+1` | `+1` | `+1` |
| Pin⁻ (`U_ι² = −1`) | `−1` | `−1` | `+1` |

Two flips, no net effect. **The Pin choice was a red herring — the second one this
session, after `U_ι²` itself.**

## What the tuple actually is

| step | result |
|---|---|
| `ε = J²` | **`−1`** for every **diagonal** `k`, inherited from `J_M² = −1` |
| `ε' = JD/DJ` | **`+1` is FORCED** — the `D_M` part cannot flip — and it forces `[k,s3]=0`, i.e. `k` diagonal. **`s1`, `s2` fail outright** |
| `ε'' = Jγ/γJ` | narrows `k` to `{I, s3}` up to phase. **`diag(1,i)` fails** |

```
k = I    →  (−1, +1, +1)  →  KO-dimension 4
k = s3   →  (−1, +1, −1)  →  KO-dimension 2
```

`diag(1,−1) = −s3` gives the same tuple as `s3` — a coherence check that the phase of `k`
does not matter, which it should not.

**The choice between KO 2 and KO 4 is internal to `J`, not geometric.** Nothing in the
construction selects one.

Metric dimension is **3** (Weyl asymptotics of `D_block` on `S³ ⊕ S³`), so the KO−metric
mismatch is `7` or `1` mod 8 — **reported, not interpreted**. (A mismatch is normal in
NCG; the Standard Model's is 6.)

## The control, and a test that was wider than its claim

**CTRL:** the machinery recovers the `S³` factor's own declared tuple — `J_M² = −1`,
`J_M D_M J_M⁻¹ = +D_M`, no `γ` → **KO-dim 3** ✓. That is the least it must do before its
other outputs are trusted.

**K3 scope fix, recorded rather than quietly adjusted.** `claim.md` predicted `ε = −1` for
`k` unitary **diagonal**; the first version of the assertion ran over **all** `k` and
reported `False` — because `s2` is *imaginary*, so `s2·conj(s2) = −I` and the two minus
signs cancel, giving `ε = +1`. **The claim was right; the test was wider than the claim.**
`s2` is excluded by `ε'` anyway, so nothing downstream moves.

---

## Kill Analysis

**Killed:** C57 as worded (the Pin choice does *not* change the tuple), and with it C56's
`U5`. **C56's statement is amended in place, not deleted** — it was a real observation
about one factor, incompletely accounted.

**What C56 got right and keeps:** `U_ι² = ±1` is a Pin choice, not determined by the
construction, and `γ` exists either way. Only the claim about `ε''` was wrong.

**Not killed:** nothing upstream. C49 (PD fails) and C52 (orientability fails) are
untouched, and they are why this whole tuple is **bookkeeping on a non-geometry**. A
KO-dimension does not make the object a spectral geometry.

**Remaining choice, now precisely located:** `k ∈ {I, s3}` → KO 4 or KO 2. Internal to
`J`. Nothing in the portfolio selects it, and nothing downstream depends on it.

## What this does NOT show

- **The KO table is not re-derived.** The identification of a sign tuple with a
  KO-dimension mod 8 follows CCM 2006 / Connes and is used as `[DOCS]` — the same handling
  `preprint.tex` gives `J_F` after C36 showed this is the step that goes wrong.
- It does **not** make the doubled triple a geometry; C49 and C52 stand.
- The KO−metric mismatch is reported as a number, with no physical reading attached.
- Nothing about `N_gen = 3` — **step 7 remains untouched by agreement.**
