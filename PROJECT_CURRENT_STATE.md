# Project Current State

**Last authoritative commit:** `c86b72a`
**Last authoritative date:** 2026-06-11
**Branch:** `main` (HEAD = origin/main, clean, no uncommitted changes)
**Tests:** 126/126 passing (`tom_s3_spinor_toy/tests/`)

---

## How to use this file

Before starting ANY work on ANY machine:

```bash
git fetch --all --prune
git pull --ff-only
python -m pytest tom_s3_spinor_toy/tests/ -q --tb=no
```

If tests fail or branch is behind → **stop and reconcile before doing anything else**.

After finishing work on any machine:

```bash
python -m pytest tom_s3_spinor_toy/tests/ -q --tb=no
git add <specific files>
git commit -m "type(scope): description"
git push
```

If leaving work unfinished, still commit and push with `WIP:` prefix:

```bash
git add .
git commit -m "WIP: checkpoint before switching machine"
git push
```

**Rule:** Any session summary older than the latest `origin/main` commit is a
historical checkpoint, not a current roadmap. Read this file first.

---

## Current Status by Track

### Track 1: AV-2 (Full Angular/Spinor Sector)

| Gate | Status | Commit |
|---|---|---|
| G0 — Source trace (C-H PDF) | **✅ PASS** | `c86b72a` |
| G1 — 2-component radial system | **OPEN** — next gate |
| G2 — Boundary exponent measurement | OPEN — after G1 |
| E1 — Sparse mixed bilinear dict | OPEN — after G2 |
| E2 — Angular singlet check | OPEN — after E1 PASS |

**Pre-registration:** `experiments/20260610-spinor-geometry-pivot-v0.2.0/claim_av2_angular.md`

G1 implementation plan (de-risked by G0):
- Build normalized `(phi_nl, g_nl)` 2-component modes using eqs 3.29-3.30 from C-H
- Verify λ = ±(n+3/2) recovery
- Uses `phi_nl_hopf` + `g_nl_hopf` (both PDF-verified); NO spin connection code needed
- ~50 lines; weight = `sin²θ dθ` (NOT the radial-proxy weight — see source_register_av2.md)
- Relevant source: `experiments/.../source_register_av2.md`, C-H eqs 3.29-3.30, 3.32-3.33

### Track 2: BG-1 (S³×S¹ Product Lattice)

Status: **PLANNED, not started**
H-BG-1 hypothesis: KK gap δ(R_S1) as geometry discriminant on S³×S¹ Dirac lattice.
Independent of AV-2. Can run in parallel.
Pre-registration not yet written.

### Track 3: E:-machine push (legacy items P5–P14)

Status: **PENDING, requires home PC**
Items P5–P14 from decision_record_v0.2.0.md are marked `[EP]` (E:-only).
These are V-operator scaffold and lambda no-go records from the E: machine.
Until pushed: 20 items cannot be independently verified from this machine.
When pushed: moves those items from [EP] to verifiable + unlocks honest 34-point re-audit.

---

## Item 40 — tom_ansatz Status

```
[RADIAL + DICTIONARY_ROBUST]
Angular identification: PENDING (AV-2)
```

Approved phrasing: *"The radial layer suggests a φ_ll boundary-family structure, with φ₁₁
dominant at the linear level, while the eq. 49 bilinear layer requires f^(φ) plus a dense
bilinear expansion."*

Forbidden phrasings: "Tom's ansatz solved" / "eq. 49 derived" / "φ₁₁ identified as full mode"

---

## Null Results

| ID | Date | Verdict | Slug |
|---|---|---|---|
| 20260610-ht1-sparse-bilinear | 2026-06-10 | **REJECT** | Boundary cos-exponent mismatch blocks sparse bilinear reconstruction |

Full record: `null_results/20260610-ht1-sparse-bilinear.md`

---

## Historical Checkpoints

These session summaries are useful for reconstruction, **not** for current planning:

| Date | File | Covers |
|---|---|---|
| 2026-06-10 | _(session transcript)_ | AV-1, AV-1c′, AV-2 G0; marks END of G0 phase |

Do not use a session summary as a next-step roadmap without checking:
1. Latest commit in this file
2. `git log --oneline -5`
3. `pytest` green

---

## Hard Constraints (non-negotiable)

```
λ = FREE_COUPLING_PARAMETER           — never fixed, never claimed
research_only = yes                   — no physical promotion
physical_promotion = no
S³×S¹_solved = no                     — KT-3 PASS ≠ old S³×S¹ problem resolved
tom_ansatz → phi₁₁ = radial_only      — angular not verified until AV-2 complete
```

---

## Architecture (key files)

| File | Role |
|---|---|
| `tom_s3_spinor_toy/reference_spinor_harmonics.py` | `phi_nl_hopf` — upper component (C-H eq 3.25) |
| `tom_s3_spinor_toy/discrete_radial_dirac_proxy.py` | `g_nl_hopf` (eq 3.27), E0 gate, kill-test |
| `tom_s3_spinor_toy/av1_angular_dictionary.py` | AV-1a/b/c, H-T1 exploratory |
| `tom_s3_spinor_toy/av1c_prime_cross_bilinear.py` | AV-1c′ kill-test; P1/P2 confirmation |
| `tom_s3_spinor_toy/tests/test_ch_first_order_system.py` | C-H eqs 3.27-3.30, 3.38 regression (24 tests) |
| `experiments/20260610-spinor-geometry-pivot-v0.2.0/` | All claims, reports, source registers |
| `null_results/` | REJECT entries + INDEX |
| `reports/ITEM40_ALPHA_RADIAL_DICTIONARY_STATUS.md` | Item 40 consolidated status |
| `references/camporesi_higuchi_grqc9505009.pdf` | Primary source for AV-2 |
