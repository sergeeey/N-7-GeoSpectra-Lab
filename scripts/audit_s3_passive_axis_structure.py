"""Static (no-eigensolve) structural audit of the S³ axis in H = (D_S³)² ⊗ I + I ⊗ P_S¹.

PURPOSE:
    Replace the invalidated SVD test (see
    `reports/CROSS_DOMAIN_SVD_PHANTOM_TEST_INVALIDATION_2026-06-04.md`).
    Use only matrix-algebra checks — NO eigensolve, NO heavy compute.

TESTS (all static, all cheap):

  A. Block-structure test
     Split H into s3_dim × s3_dim blocks of size s1_dim × s1_dim.
     Measure Frobenius norm of off-diagonal blocks (i ≠ i').
     If ||off-diag||_F / ||diag||_F ≈ 0 → no coupling between S³ sectors.

  B. Partial-trace test
     Compute Tr_{S¹}(H) and Tr_{S³}(H).
     - Tr_{S¹}(H) lives in the S³ basis; if it is diagonal → S³ is structurally trivial.
     - Tr_{S³}(H) lives in the S¹ basis; if it has nontrivial off-diagonal → S¹ is structured.

  C. Commutator / projector test (cheap, optional but included)
     For each S³ projector P_i = |i⟩⟨i| ⊗ I_{S¹}, compute ||[H, P_i]||_F.
     If commutator ≈ 0 for all i → S³ sectors are exactly conserved by H.

GUARDRAILS:
    - smoke profile only, single tiny case (N=112)
    - no eigensolve anywhere — full matrix algebra only
    - script must finish in < 10 seconds total
    - writes one report, does not commit anything

SAFE PHRASING for outputs:
    "Current evidence suggests the S³ sector may be structurally passive
     or weakly coupled in the current toy operator, but this requires
     further verification."

USAGE:
    python scripts/audit_s3_passive_axis_structure.py
    python scripts/audit_s3_passive_axis_structure.py --dry-run

OUTPUT:
    reports/S3_PASSIVE_AXIS_STRUCTURAL_AUDIT_SMOKE_2026-06-04.md
    reports/S3_PASSIVE_AXIS_STRUCTURAL_AUDIT_SMOKE_2026-06-04.json
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from cc_toy_lab.spectral.dirac_s3 import s3_dimension
from cc_toy_lab.spectral.s3_s1_product_discretized import build_s3_s1_product_operator

S1_FAMILIES = ("spectral_circle", "ring", "wilson_ring")
W_VALUES = (0.0, 20.0)

# Smoke only — single tiny size. NO eigensolve happens, but keep N small anyway.
SMOKE_CASE = {"label": "N=112", "j_max": 3, "s1_size": 16}


def block_structure_test(H: np.ndarray, s3_dim: int, s1_dim: int) -> dict:
    """Test A: Frobenius norm of off-diagonal vs diagonal S³ blocks.

    H is a (s3_dim * s1_dim, s3_dim * s1_dim) matrix.
    Split into s3_dim × s3_dim grid of (s1_dim × s1_dim) blocks.
    """
    diag_sum_sq = 0.0
    off_sum_sq = 0.0
    max_offdiag_block_norm = 0.0
    n_diag = 0
    n_off = 0
    for i in range(s3_dim):
        for j in range(s3_dim):
            block = H[i * s1_dim : (i + 1) * s1_dim, j * s1_dim : (j + 1) * s1_dim]
            sq = float(np.sum(np.abs(block) ** 2))
            if i == j:
                diag_sum_sq += sq
                n_diag += 1
            else:
                off_sum_sq += sq
                max_offdiag_block_norm = max(
                    max_offdiag_block_norm, float(np.linalg.norm(block, "fro"))
                )
                n_off += 1
    diag_fro = float(np.sqrt(diag_sum_sq))
    off_fro = float(np.sqrt(off_sum_sq))
    ratio = (off_fro / diag_fro) if diag_fro > 0 else float("inf")
    return {
        "diag_blocks_fro": diag_fro,
        "offdiag_blocks_fro": off_fro,
        "ratio_off_over_diag": ratio,
        "max_single_offdiag_block_fro": max_offdiag_block_norm,
        "n_diag_blocks": n_diag,
        "n_offdiag_blocks": n_off,
        "verdict": (
            "ZERO_OFFDIAG"
            if off_fro < 1e-10
            else "NEAR_ZERO_OFFDIAG"
            if ratio < 1e-6
            else "WEAK_OFFDIAG"
            if ratio < 1e-2
            else "NONTRIVIAL_OFFDIAG"
        ),
    }


def partial_trace_test(H: np.ndarray, s3_dim: int, s1_dim: int) -> dict:
    """Test B: partial traces over S¹ and over S³."""
    # T_s1[i, i'] = Σ_j H[i*s1+j, i'*s1+j]
    T_s1 = np.zeros((s3_dim, s3_dim), dtype=H.dtype)
    for i in range(s3_dim):
        for ip in range(s3_dim):
            block = H[i * s1_dim : (i + 1) * s1_dim, ip * s1_dim : (ip + 1) * s1_dim]
            T_s1[i, ip] = np.trace(block)

    # T_s3[j, j'] = Σ_i H[i*s1+j, i*s1+j']
    T_s3 = np.zeros((s1_dim, s1_dim), dtype=H.dtype)
    for i in range(s3_dim):
        T_s3 += H[i * s1_dim : (i + 1) * s1_dim, i * s1_dim : (i + 1) * s1_dim]

    def diagonality(M: np.ndarray) -> float:
        """Fraction of Frobenius norm on the diagonal."""
        total = float(np.linalg.norm(M, "fro"))
        if total == 0.0:
            return 1.0
        diag = float(np.linalg.norm(np.diag(M), 2))
        return diag / total

    T_s1_diagonality = diagonality(T_s1)
    T_s3_diagonality = diagonality(T_s3)

    # Is T_s3 close to a scalar multiple of identity? (would mean S¹ part also trivial)
    T_s3_diag = np.diag(T_s3)
    is_scalar = bool(np.std(T_s3_diag.real) < 1e-9 and T_s3_diagonality > 0.999)

    return {
        "Tr_S1_reduced_to_S3": {
            "shape": list(T_s1.shape),
            "frobenius_norm": float(np.linalg.norm(T_s1, "fro")),
            "diagonality_fraction": T_s1_diagonality,
            "verdict": "DIAGONAL"
            if T_s1_diagonality > 0.9999
            else "NEAR_DIAGONAL"
            if T_s1_diagonality > 0.99
            else "NONDIAGONAL",
            "diagonal_values": [complex(x).real for x in np.diag(T_s1)],
        },
        "Tr_S3_reduced_to_S1": {
            "shape": list(T_s3.shape),
            "frobenius_norm": float(np.linalg.norm(T_s3, "fro")),
            "diagonality_fraction": T_s3_diagonality,
            "is_scalar_identity": is_scalar,
            "verdict": "TRIVIAL_SCALAR"
            if is_scalar
            else ("DIAGONAL_NONSCALAR" if T_s3_diagonality > 0.9999 else "NONDIAGONAL"),
        },
    }


def commutator_test(H: np.ndarray, s3_dim: int, s1_dim: int) -> dict:
    """Test C: ||[H, P_i]||_F for each S³ sector projector P_i = |i⟩⟨i| ⊗ I_{s1}."""
    N = s3_dim * s1_dim
    eye_s1 = np.eye(s1_dim, dtype=H.dtype)
    max_commutator_norm = 0.0
    per_sector = []
    for i in range(s3_dim):
        # P_i: zeros except identity in the i-th S³ block
        P = np.zeros((N, N), dtype=H.dtype)
        P[i * s1_dim : (i + 1) * s1_dim, i * s1_dim : (i + 1) * s1_dim] = eye_s1
        commutator = H @ P - P @ H
        norm = float(np.linalg.norm(commutator, "fro"))
        per_sector.append({"sector": int(i), "commutator_fro_norm": norm})
        if norm > max_commutator_norm:
            max_commutator_norm = norm

    return {
        "max_commutator_norm": max_commutator_norm,
        "per_sector": per_sector,
        "verdict": (
            "ALL_ZERO"
            if max_commutator_norm < 1e-10
            else "NEAR_ZERO"
            if max_commutator_norm < 1e-6
            else "NONZERO"
        ),
    }


def run_one_case(j_max: int, s1_size: int, s1_family: str, W: float, seed: int = 123) -> dict:
    s3_dim = s3_dimension(int(j_max))
    s1_dim = int(s1_size)

    t0 = time.perf_counter()
    mode = "clean" if W == 0.0 else "geometric_weight"
    H, _lifted, meta = build_s3_s1_product_operator(
        j_max=j_max,
        s1_size=s1_size,
        alpha=0.0,
        mode=mode,
        disorder_strength=float(W),
        seed=int(seed),
        radius=1.0,
        s1_family=s1_family,
    )
    t_build = time.perf_counter() - t0

    t0 = time.perf_counter()
    A = block_structure_test(H, s3_dim, s1_dim)
    B = partial_trace_test(H, s3_dim, s1_dim)
    C = commutator_test(H, s3_dim, s1_dim)
    t_audit = time.perf_counter() - t0

    return {
        "family": s1_family,
        "W": float(W),
        "j_max": int(j_max),
        "s1_size": int(s1_size),
        "s3_dim": s3_dim,
        "s1_dim": s1_dim,
        "N_total": s3_dim * s1_dim,
        "seed": int(seed),
        "build_seconds": t_build,
        "audit_seconds": t_audit,
        "block_structure": A,
        "partial_trace": B,
        "commutator": C,
    }


def aggregate_verdict(results: list[dict]) -> str:
    """Conservative aggregation across all cases. No physics claims."""
    block_verdicts = {r["block_structure"]["verdict"] for r in results}
    commutator_verdicts = {r["commutator"]["verdict"] for r in results}
    if block_verdicts.issubset(
        {"ZERO_OFFDIAG", "NEAR_ZERO_OFFDIAG"}
    ) and commutator_verdicts.issubset({"ALL_ZERO", "NEAR_ZERO"}):
        return "STRUCTURAL_AUDIT_SMOKE_COMPLETED"
    if "NONTRIVIAL_OFFDIAG" in block_verdicts or "NONZERO" in commutator_verdicts:
        return "STRUCTURAL_AUDIT_NEEDS_FIX"
    return "STRUCTURAL_AUDIT_INCONCLUSIVE"


def write_markdown(
    results: list[dict], verdict: str, total_seconds: float, output_path: Path
) -> None:
    lines = [
        "# S³ Passive-Axis Structural Audit — Smoke",
        "",
        "## Purpose",
        "",
        "Replace the invalidated SVD phantom-factor test (see",
        "`CROSS_DOMAIN_SVD_PHANTOM_TEST_INVALIDATION_2026-06-04.md`).",
        "Probe the S³ axis structure inside `H = (D_S³)² ⊗ I + I ⊗ P_S¹` using only",
        "static matrix-algebra checks — no eigensolve, no heavy compute.",
        "",
        "## Invalidated Prior SVD Test",
        "",
        "Prior SVD test was invalid by construction: mode-1 and mode-2 unfolding",
        "matrices are transpose pairs, so their singular value spectra are identical.",
        "That test could not distinguish the two axes. The current audit avoids",
        "the issue by not using SVD at all.",
        "",
        "## Methods (no eigensolve)",
        "",
        "- **A. Block-structure test** — partition `H` into `s3_dim × s3_dim` grid of",
        "  `s1_dim × s1_dim` blocks. Compare Frobenius norm of off-diagonal vs",
        "  diagonal blocks.",
        "- **B. Partial-trace test** — `Tr_{S¹}(H)` (lives in S³ basis) and `Tr_{S³}(H)`",
        "  (lives in S¹ basis). Check diagonality and triviality.",
        "- **C. Commutator/projector test** — for each S³ sector projector `P_i`,",
        "  compute `||[H, P_i]||_F`.",
        "",
        f"## Smoke Cases ({len(results)} total)",
        "",
        f"Single size: `j_max={SMOKE_CASE['j_max']}, s1_size={SMOKE_CASE['s1_size']}`",
        f"→ `N = {SMOKE_CASE['j_max']}` (S³ dim = `s3_dimension(j_max)`) × `s1_size`.",
        "",
        "## Results",
        "",
        "### Block-structure test (off-diagonal S³ blocks)",
        "",
        "| Family | W | ||off||_F | ||diag||_F | ratio off/diag | max single off-block | verdict |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for r in results:
        bs = r["block_structure"]
        lines.append(
            f"| {r['family']} | {r['W']:.0f} | {bs['offdiag_blocks_fro']:.2e} | "
            f"{bs['diag_blocks_fro']:.4f} | {bs['ratio_off_over_diag']:.2e} | "
            f"{bs['max_single_offdiag_block_fro']:.2e} | {bs['verdict']} |"
        )

    lines += [
        "",
        "### Partial-trace test",
        "",
        "| Family | W | Tr_{S¹}→S³ diag-fraction | verdict | Tr_{S³}→S¹ diag-fraction | scalar identity? | verdict |",
        "|---|---:|---:|---|---:|---|---|",
    ]
    for r in results:
        pt = r["partial_trace"]
        ts1 = pt["Tr_S1_reduced_to_S3"]
        ts3 = pt["Tr_S3_reduced_to_S1"]
        lines.append(
            f"| {r['family']} | {r['W']:.0f} | {ts1['diagonality_fraction']:.6f} | {ts1['verdict']} | "
            f"{ts3['diagonality_fraction']:.6f} | {ts3['is_scalar_identity']} | {ts3['verdict']} |"
        )

    lines += [
        "",
        "### Commutator / projector test",
        "",
        "| Family | W | max ||[H, P_i]||_F | verdict |",
        "|---|---:|---:|---|",
    ]
    for r in results:
        c = r["commutator"]
        lines.append(
            f"| {r['family']} | {r['W']:.0f} | {c['max_commutator_norm']:.2e} | {c['verdict']} |"
        )

    lines += [
        "",
        "## Interpretation Limits",
        "",
        "These tests measure structural properties of one specific construction:",
        "`H = (D_S³)² ⊗ I + I ⊗ P_S¹` with `D_S³` implemented as a diagonal mockup",
        "(see `cc_toy_lab/spectral/dirac_s3.py`).",
        "",
        "- They do NOT validate or refute any physical claim about S³×S¹ geometry.",
        "- They do NOT extend to a Dirac operator with a real spin-connection.",
        "- They do NOT make any statement about the Gate 4B IPR contrast or the",
        "  `DISCRETIZATION_SENSITIVE / GEOMETRY_AGNOSTIC` verdict.",
        "- They are a smoke probe of a specific architectural property of the",
        "  current toy operator, nothing more.",
        "",
        "## Safe phrasing for downstream use",
        "",
        '> "Current evidence suggests the S³ sector may be structurally passive or',
        "> weakly coupled in the current toy operator, but this requires further",
        '> verification."',
        "",
        'Stronger phrasings (e.g. "all sensitivity comes from S¹", "S³ is irrelevant")',
        "are NOT supported by these tests and must NOT be used.",
        "",
        f"## Verdict\n\n**{verdict}**",
        "",
        f"Total audit time: {total_seconds:.3f} seconds for {len(results)} cases (no eigensolve).",
        "",
        "## Provenance",
        "",
        "- Script: `scripts/audit_s3_passive_axis_structure.py`",
        "- Replaces: `scripts/cross_domain_svd_phantom_test.py` (see invalidation report)",
        "- No commits, no push, no external claims.",
        "",
    ]
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Static no-eigensolve audit of S³ axis structure")
    parser.add_argument("--dry-run", action="store_true", help="Print plan only, no compute")
    parser.add_argument("--output-dir", default="reports", help="Where to write reports")
    parser.add_argument(
        "--time-limit-seconds", type=float, default=60.0, help="Hard cap; stop if exceeded"
    )
    args = parser.parse_args()

    cases_plan = [{"family": fam, "W": W} for fam in S1_FAMILIES for W in W_VALUES]

    print(
        json.dumps(
            {
                "smoke_case": SMOKE_CASE,
                "subcases": cases_plan,
                "total_subcases": len(cases_plan),
                "eigensolve": False,
                "time_limit_seconds": args.time_limit_seconds,
            },
            indent=2,
        )
    )

    if args.dry_run:
        print("\n--dry-run: not executing")
        return 0

    output_dir = REPO_ROOT / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    t_start = time.perf_counter()
    results = []
    for sub in cases_plan:
        elapsed = time.perf_counter() - t_start
        if elapsed > args.time_limit_seconds:
            print(f"TIME LIMIT exceeded at {elapsed:.2f}s — stopping early.")
            break
        print(f"Running family={sub['family']} W={sub['W']} ...", flush=True)
        r = run_one_case(
            j_max=SMOKE_CASE["j_max"],
            s1_size=SMOKE_CASE["s1_size"],
            s1_family=sub["family"],
            W=sub["W"],
        )
        results.append(r)
        bs = r["block_structure"]
        pt = r["partial_trace"]
        cc = r["commutator"]
        print(
            f"  block={bs['verdict']} (off/diag={bs['ratio_off_over_diag']:.2e})  "
            f"trS¹={pt['Tr_S1_reduced_to_S3']['verdict']}  "
            f"trS³={pt['Tr_S3_reduced_to_S1']['verdict']}  "
            f"comm={cc['verdict']} (max={cc['max_commutator_norm']:.2e})",
            flush=True,
        )

    t_total = time.perf_counter() - t_start
    verdict = aggregate_verdict(results)

    json_path = output_dir / "S3_PASSIVE_AXIS_STRUCTURAL_AUDIT_SMOKE_2026-06-04.json"
    json_path.write_text(
        json.dumps(
            {
                "protocol_version": "structural-audit-smoke-v1",
                "verdict": verdict,
                "total_seconds": t_total,
                "n_cases": len(results),
                "smoke_case": SMOKE_CASE,
                "results": results,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    md_path = output_dir / "S3_PASSIVE_AXIS_STRUCTURAL_AUDIT_SMOKE_2026-06-04.md"
    write_markdown(results, verdict, t_total, md_path)

    print()
    print(f"Total: {t_total:.3f}s for {len(results)} cases")
    print(f"VERDICT: {verdict}")
    print(f"Wrote: {md_path}")
    print(f"Wrote: {json_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
