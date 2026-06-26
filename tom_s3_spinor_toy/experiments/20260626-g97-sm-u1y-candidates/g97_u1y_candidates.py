"""G97: U(1)_Y candidates from SO(4) × SO(7) Cartan generators.

Claim: Hypercharge U(1)_Y can be identified as a linear combination of Cartan
generators in SO(4) × SO(7) = Iso(S³) × Iso(S⁶).

Setup:
  SO(4) = SU(2)_L × SU(2)_R:  Cartan = {T3_L, T3_R}  (rank 2)
  SO(7) ⊃ G₂ ⊃ SU(3):         Cartan = {H1, H2, H3}  (rank 3)
  Total Cartan rank = 5: any U(1) = α·T3_L + β·T3_R + γ₁·H1 + γ₂·H2 + γ₃·H3

SM hypercharge facts:
  Y = T3_R + B-L/2  (Pati-Salam decomposition, if B-L from geometry)
  For quarks: Y(u_L)=1/6, Y(d_L)=1/6, Y(u_R)=2/3, Y(d_R)=-1/3
  For leptons: Y(e_L)=-1/2, Y(ν_L)=-1/2, Y(e_R)=-1

Approach:
  1. Build Cartan generators of SO(4) and SO(7) explicitly
  2. For each SO(4) factor: J±_3 = Cartan of SU(2)_L and SU(2)_R
  3. For SO(7) ⊃ G₂ ⊃ SU(3): identify H_3 and H_8 (SU(3) Cartan diagonal generators)
  4. Map SM fields to representations of SU(2)_L × SU(2)_R × SU(3)
  5. Find U(1)_Y as Y = f(T3_R, H_8, ...) that reproduces SM hypercharges
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g97.json"


# ===== SO(4) = SU(2)_L x SU(2)_R =====


def L_ab(a: int, b: int, n: int) -> np.ndarray:
    m = np.zeros((n, n))
    m[a, b] = 1.0
    m[b, a] = -1.0
    return m


def so4_su2_cartans() -> tuple[np.ndarray, np.ndarray]:
    """Return T3_L and T3_R (Cartan generators of SU(2)_L and SU(2)_R)."""
    L03 = L_ab(0, 3, 4)
    L12 = L_ab(1, 2, 4)
    s = 1.0 / np.sqrt(2)
    Jp3 = s * (L03 + L12)  # J+_3 = T3_L
    Jm3 = s * (L03 - L12)  # J-_3 = T3_R
    return Jp3, Jm3


# ===== SO(7) ⊃ G₂ ⊃ SU(3): Cartan generators =====

FANO = [(0, 1, 3), (1, 2, 4), (2, 3, 5), (3, 4, 6), (4, 5, 0), (5, 6, 1), (6, 0, 2)]


def build_phi() -> np.ndarray:
    phi = np.zeros((7, 7, 7))
    for a, b, c in FANO:
        for i, j, k in [(a, b, c), (b, c, a), (c, a, b)]:
            phi[i, j, k] = 1.0
            phi[j, i, k] = -1.0
    return phi


def find_g2_gens(phi: np.ndarray) -> list[np.ndarray]:
    rows = []
    for i in range(7):
        for j in range(7):
            row = np.zeros(49)
            row[i * 7 + j] = 1.0
            row[j * 7 + i] = 1.0
            rows.append(row)
    for i in range(7):
        for j in range(7):
            for ll in range(7):
                row = np.zeros(49)
                for k in range(7):
                    row[ll * 7 + k] += phi[i, j, k]
                for m in range(7):
                    row[m * 7 + i] -= phi[m, j, ll]
                for m in range(7):
                    row[m * 7 + j] -= phi[i, m, ll]
                rows.append(row)
    M = np.array(rows)
    _, _, Vt = np.linalg.svd(M, full_matrices=True)
    rank = int(np.sum(np.linalg.svd(M, compute_uv=False) > 1e-8))
    return [Vt[rank + i].reshape(7, 7) for i in range(49 - rank)]


def su3_cartans_from_g2(g2_gens: list[np.ndarray]) -> list[np.ndarray]:
    """Extract SU(3) Cartan generators = G₂ gens that stabilize e₇ AND are diagonal-like."""
    e7 = np.zeros(7)
    e7[6] = 1.0
    # SU(3) ⊂ G₂: stabilizer of e₇
    su3_gens = [
        G for G in g2_gens if np.max(np.abs(G @ e7)) < 1e-10 and np.max(np.abs(G[6, :])) < 1e-10
    ]
    if len(su3_gens) < 8:
        su3_gens = [
            G
            for G in g2_gens
            if np.max(np.abs(G[:, 6])) < 1e-10 and np.max(np.abs(G[6, :])) < 1e-10
        ]
    # From SU(3) generators, find Cartan = those that commute with each other
    cartans = []
    for i, Gi in enumerate(su3_gens):
        is_cartan = True
        for j, Gj in enumerate(su3_gens):
            if i != j:
                C = Gi @ Gj - Gj @ Gi
                if np.max(np.abs(C)) > 1e-9:
                    is_cartan = False
                    break
        if is_cartan:
            cartans.append(Gi)
    return cartans


def commutator(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return A @ B - B @ A


def main() -> None:
    print("\n=== G97: U(1)_Y candidates from SO(4)×SO(7) ===\n")

    # Step 1: SO(4) Cartan generators
    T3L, T3R = so4_su2_cartans()
    print("Step 1: SO(4) Cartan generators")
    print(f"  T3_L (J+_3) = SU(2)_L Cartan: norm = {np.linalg.norm(T3L):.4f}")
    print(f"  T3_R (J-_3) = SU(2)_R Cartan: norm = {np.linalg.norm(T3R):.4f}")

    # Verify T3_L ∈ SU(2)_L: [J+_1, J+_2] should give T3_L
    L01 = L_ab(0, 1, 4)
    L23 = L_ab(2, 3, 4)
    L02 = L_ab(0, 2, 4)
    L13 = L_ab(1, 3, 4)
    s = 1.0 / np.sqrt(2)
    Jp1 = s * (L01 + L23)
    Jp2 = s * (L02 - L13)
    err = np.max(np.abs(commutator(Jp1, Jp2) - T3L))
    print(f"  [J+_1, J+_2] = T3_L: err={err:.2e}  {'✓' if err<1e-12 else '✗'}")

    # Step 2: SO(7) ⊃ G₂ ⊃ SU(3) Cartan
    print("\nStep 2: G₂ ⊂ SO(7) — find SU(3) Cartan generators")
    phi = build_phi()
    g2_gens = find_g2_gens(phi)
    print(f"  dim(G₂) = {len(g2_gens)} [expected: 14]")

    su3_cart = su3_cartans_from_g2(g2_gens)
    print(f"  dim(SU(3) Cartan) = {len(su3_cart)} [expected: 2]")

    # Step 3: Full Cartan algebra of SO(4) × SO(7)
    print("\nStep 3: Full Cartan algebra of SO(4)×SO(7)")
    print("  SO(4) contributes: T3_L, T3_R  (rank 2)")
    print("  G₂ ⊂ SO(7) contributes: H3, H8  (rank 2 = SU(3) rank)")
    print("  Total U(1) space: dim = 4 (from G₂ Cartan)")
    print("  Full SO(7) rank = 3; via G₂ ⊂ SO(7): 2 from SU(3) + rest from SO(7)\\G₂")

    # Step 4: SM field assignments and U(1)_Y
    print("\nStep 4: SM hypercharge assignment — Pati-Salam route")
    print("  In Pati-Salam: SU(2)_L × SU(2)_R × SU(4) ⊃ SM")
    print("  Hypercharge: Y = T3_R + (B-L)/2")
    print()

    # Hypercharge values in SM:
    sm_fields = [
        ("u_L", 1 / 6, 1 / 2, 0, "(3,2,+1/6) under SU(3)xSU(2)_LxU(1)_Y"),
        ("d_L", 1 / 6, -1 / 2, 0, "(3,2,+1/6)"),
        ("u_R", 2 / 3, 0, +2 / 3, "(3,1,+2/3)"),
        ("d_R", -1 / 3, 0, -1 / 3, "(3,1,-1/3)"),
        ("e_L", -1 / 2, -1 / 2, 0, "(1,2,-1/2)"),
        ("nu_L", -1 / 2, +1 / 2, 0, "(1,2,-1/2)"),
        ("e_R", -1, 0, -1, "(1,1,-1)"),
    ]

    print(f"  {'Field':>8} {'Y_SM':>6} {'T3_L':>6} {'T3_R':>6} {'Y=T3R+(BL/2)':>14} {'Match':>6}")
    print("  " + "-" * 55)

    # B-L charges: quarks=1/3, leptons=-1
    # Y = T3_R + (B-L)/2
    BL = {"u_L": 1 / 3, "d_L": 1 / 3, "u_R": 1 / 3, "d_R": 1 / 3, "e_L": -1, "nu_L": -1, "e_R": -1}

    matches = []
    for field, Y_sm, T3L_val, T3R_val, rep in sm_fields:
        bl = BL[field]
        Y_ps = T3R_val + bl / 2
        match = abs(Y_ps - Y_sm) < 1e-10
        matches.append(match)
        print(
            f"  {field:>8} {Y_sm:>6.3f} {T3L_val:>6.3f} {T3R_val:>6.3f} {Y_ps:>14.3f}  {'✓' if match else '✗'}"
        )

    ps_works = all(matches)
    print(f"\n  Y = T3_R + (B-L)/2 reproduces ALL SM hypercharges: {'✓' if ps_works else '✗'}")

    # Step 5: What B-L corresponds to in the algebra
    print("\nStep 5: B-L charge in terms of SU(3)×SU(2)×... algebra")
    print("  B-L = baryon number - lepton number")
    print("  In SU(3) language:")
    print("    Quarks: SU(3)_color triplet → B-L = 1/3 (colour traced)")
    print("    Leptons: SU(3) singlet → B-L = -1")
    print("  B-L generator ∝ diag(1/3,1/3,1/3,-1) in SU(4) (Pati-Salam)")
    print("  In our algebra: B-L could come from U(1) ⊂ SO(7)\\G₂ or from SU(3) trace")
    print()
    print("  STRUCTURAL ANALYSIS:")
    print("    Known: T3_R from SO(4) ← G95 VERIFIED")
    print("    Known: SU(3) from G₂ ← G96 VERIFIED")
    print("    Unknown: B-L source in SO(4)×SO(7) ← needs Tom Part 4/5")
    print("    Candidate: U(1)_B-L = diagonal generator of SU(4) ⊃ SU(3)")
    print("      In D=13: does the compactification include SU(4) somewhere?")
    print("      S³: SO(4)=SU(2)_L×SU(2)_R (rank 2, no SU(4))")
    print("      S⁶: SO(7)⊃G₂ (rank 3, no SU(4) either)")
    print("    → B-L gap: NOT covered by Iso(S³×S⁶) = SO(4)×SO(7)")

    # Step 6: What IS covered
    print("\nStep 6: Coverage summary")
    covered = {
        "SU(3)_color": "SU(3) ⊂ G₂ ⊂ SO(7) [G96 VERIFIED]",
        "SU(2)_L": "SU(2)_L ⊂ SO(4) = Iso(S³) [G95 VERIFIED]",
        "SU(2)_R": "SU(2)_R ⊂ SO(4) = Iso(S³) [G95 VERIFIED]",
        "T3_R": "Cartan of SU(2)_R [G95 VERIFIED]",
        "U(1)_Y partial": "Y = T3_R + (B-L)/2 — T3_R term KNOWN, B-L term OPEN",
    }
    missing = {
        "B-L generator": "Not in Iso(S³×S⁶) = SO(4)×SO(7) directly",
        "SU(4) ⊃ SU(3)×U(1)_BL": "Pati-Salam route — needs extra structure",
        "3 generations": "Not determined by algebra alone — Tom anзac needed",
    }
    for k, v in covered.items():
        print(f"  ✓ {k}: {v}")
    print()
    for k, v in missing.items():
        print(f"  ✗ {k}: {v}")

    # Step 7: Best U(1)_Y candidate from current algebra
    print("\nStep 7: Best U(1)_Y candidate (incomplete)")
    print("  Y = T3_R + c·H_8_su3  where H_8 = diag(1,1,-2,0,0,0,0)/√3 in G₂ basis?")
    print("  Matching Y(quark) = T3_R + 1/6 → c = 1/2 (B-L/2 = 1/6 for quarks)")
    print("  Matching Y(lepton) = T3_R - 1/2 → c = -1/2 (B-L/2 = -1/2 for leptons)")
    print("  This requires B-L to distinguish quarks from leptons → needs SU(4)")
    print("  CONCLUSION: U(1)_Y is partially from T3_R [COVERED] + B-L [OPEN]")

    result = {
        "status": "PARTIAL",
        "so4_cartan_dim": 2,
        "g2_cartan_dim": len(su3_cart),
        "pati_salam_Y_works": bool(ps_works),
        "covered": {
            "SU3_color": "G96 VERIFIED: SU(3) ⊂ G₂ ⊂ SO(7)",
            "SU2_L": "G95 VERIFIED: SU(2)_L ⊂ SO(4)",
            "SU2_R": "G95 VERIFIED: SU(2)_R ⊂ SO(4)",
            "T3_R_for_Y": "G95: T3_R ⊂ SO(4)",
        },
        "missing": {
            "BL_generator": "B-L not in Iso(S3xS6) = SO(4)xSO(7)",
            "SU4": "Pati-Salam needs SU(4) which is NOT in SO(7) or SO(4)",
            "3_generations": "Tom ansatz needed",
        },
        "Y_formula": "Y = T3_R + (B-L)/2; T3_R covered by G95, B-L is open",
        "conclusion": (
            "SO(4)xSO(7) covers SU(3)xSU(2)_LxSU(2)_R but NOT U(1)_BL. "
            "Hypercharge requires additional structure (Tom ansatz or extra U(1) from "
            "the D=13 field content, not just the isometry group)."
        ),
    }

    print(f"\n=== RESULT: U(1)_Y PARTIALLY IDENTIFIED [{result['status']}] ===")
    print(f"  Pati-Salam Y = T3_R + (B-L)/2: {'✓' if ps_works else '✗'}")
    print("  T3_R available from G95: ✓")
    print("  B-L generator in SO(4)×SO(7): ✗ (not present, needs Tom input)")
    print("  Partial coverage: SU(3)×SU(2)_L×SU(2)_R confirmed; U(1)_Y = OPEN")

    RESULTS_PATH.write_text(json.dumps(result, indent=2))
    print(f"\n-> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
