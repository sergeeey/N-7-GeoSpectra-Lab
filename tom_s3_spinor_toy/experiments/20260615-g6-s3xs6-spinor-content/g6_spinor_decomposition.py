"""G6: 32-component spinor decomposition on S³×S⁶.

Claim: the Dirac spinor on S³×S⁶ decomposes under
  Pati-Salam: SU(2)_L × SU(2)_R × SU(4) → SU(2)_L × SU(3)_c × U(1)_{B-L}
into exactly ONE generation of SM fermions (16 left-handed Weyl + 16 right-handed).

Strategy:
  S³ Dirac spinor:  4 components, split by chirality under SO(4)≅SU(2)_L×SU(2)_R
    - Positive chirality: (T3L=±½, T3R=0)   — SU(2)_L doublet
    - Negative chirality: (T3L=0,  T3R=±½)  — SU(2)_R doublet

  S⁶ Dirac spinor:  8 components = weights (±½,±½,±½) of SO(6)≅SU(4)
    - S+ (positive chirality, 4 of SU(4)): even number of minus signs
    - S- (negative chirality, 4̄ of SU(4)): odd number of minus signs
    Under SU(4)→SU(3)×U(1)_{B-L}:
      4  → 3_{+1/3} + 1_{-1}      [color triplet quarks + lepton singlet]
      4̄ → 3̄_{-1/3} + 1_{+1}      [anti-quarks + anti-lepton]

  Hypercharge via Pati-Salam:
    Y = T3R + (B-L)/2

  Full product: (4 S³-states) × (8 S⁶-states) = 32 states
"""

import sympy as sp
from collections import Counter
from itertools import product as iproduct

# ─── S³ spinor states (4 components) ────────────────────────────────────────
# label: (T3L, T3R, chirality)
s3_states = [
    {"T3L": sp.Rational(1, 2), "T3R": sp.Integer(0), "chir_s3": "+"},
    {"T3L": sp.Rational(-1, 2), "T3R": sp.Integer(0), "chir_s3": "+"},
    {"T3L": sp.Integer(0), "T3R": sp.Rational(1, 2), "chir_s3": "-"},
    {"T3L": sp.Integer(0), "T3R": sp.Rational(-1, 2), "chir_s3": "-"},
]


# ─── S⁶ spinor states (8 components = weights (±½,±½,±½)) ──────────────────
def bl_charge(weight):
    """B-L charge from SU(4)⊂SO(6) embedding.

    Under SO(6)≅SU(4) → SU(3)×U(1)_{B-L}:
      4  = 3_{+1/3} + 1_{-1}  (positive chirality = even # of minus signs)
      4̄ = 3̄_{-1/3} + 1_{+1} (negative chirality = odd # of minus signs)

    Identification of lepton vs quark within each chirality sector:
      For S+ (4): the state with all same sign = SU(3) singlet = lepton (B-L=-1)
                  other 3 states = SU(3) triplet = quarks (B-L=+1/3)
      For S- (4̄): flipped.
    """
    n_minus = sum(1 for x in weight if x < 0)
    chirality = "+" if n_minus % 2 == 0 else "-"

    if chirality == "+":
        # Check if SU(3) singlet: all weights same sign within S+ sector
        # For S+: (+,+,+) is the SU(3) singlet [only all-same weight in S+]
        all_same = weight[0] == weight[1] == weight[2]
        if all_same:
            return sp.Integer(-1), "1", "ν/e (lepton)", chirality
        else:
            return sp.Rational(1, 3), "3", "q (quark)", chirality
    else:
        # For S-: (-,-,-) is the SU(3) anti-singlet
        all_same = weight[0] == weight[1] == weight[2]
        if all_same:
            return sp.Integer(1), "1̄", "ν̄/ē (anti-lepton)", chirality
        else:
            return sp.Rational(-1, 3), "3̄", "q̄ (anti-quark)", chirality


def su3_label(weight):
    """SU(3) color label from weight within the S+ or S- sector."""
    bl, rep, desc, chir = bl_charge(weight)
    colors = ["r", "g", "b"]
    if rep == "3":
        # 3 quark weights in S+ (all but the singlet)
        s_plus = [
            (sp.Rational(1, 2),) * 3,
            (sp.Rational(1, 2), sp.Rational(-1, 2), sp.Rational(-1, 2)),
            (sp.Rational(-1, 2), sp.Rational(1, 2), sp.Rational(-1, 2)),
            (sp.Rational(-1, 2), sp.Rational(-1, 2), sp.Rational(1, 2)),
        ]
        quark_weights = [
            w for w in s_plus if sum(1 for x in w if x < 0) % 2 == 0 and not (w[0] == w[1] == w[2])
        ]
        idx = quark_weights.index(weight) if weight in quark_weights else 0
        return colors[min(idx, 2)]
    elif rep == "3̄":
        s_minus = [
            (sp.Rational(-1, 2),) * 3,
            (sp.Rational(-1, 2), sp.Rational(1, 2), sp.Rational(1, 2)),
            (sp.Rational(1, 2), sp.Rational(-1, 2), sp.Rational(1, 2)),
            (sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(-1, 2)),
        ]
        anti_weights = [
            w for w in s_minus if sum(1 for x in w if x < 0) % 2 == 1 and not (w[0] == w[1] == w[2])
        ]
        idx = anti_weights.index(weight) if weight in anti_weights else 0
        return colors[min(idx, 2)] + "̄"
    else:
        return "—"


# All 8 S⁶ spinor weights
all_weights = list(iproduct([sp.Rational(-1, 2), sp.Rational(1, 2)], repeat=3))

s6_states = []
for w in all_weights:
    bl, su3_rep, desc, chir6 = bl_charge(w)
    color = su3_label(w)
    s6_states.append(
        {
            "weight": w,
            "chir_s6": chir6,
            "BL": bl,
            "su3_rep": su3_rep,
            "color": color,
            "desc": desc,
        }
    )

# ─── Full 32-component tensor product ───────────────────────────────────────
print("=" * 90)
print("G6: S³×S⁶ Dirac spinor → SM quantum numbers  (32 states)")
print("    Y = T3R + (B-L)/2   [Pati-Salam hypercharge formula]")
print("=" * 90)
print(
    f"{'#':>3} | {'T3L':>4} {'T3R':>4} {'B-L':>5} {'Y':>5} | "
    f"{'SU(3)':>6} {'color':>5} | {'SM particle':>20}"
)
print("-" * 90)

SM_TABLE = {
    # (T3L, Y, su3_rep): SM name
    (sp.Rational(1, 2), sp.Rational(1, 6), "3"): "uL",
    (sp.Rational(-1, 2), sp.Rational(1, 6), "3"): "dL",
    (sp.Integer(0), sp.Rational(2, 3), "3"): "uR",
    (sp.Integer(0), sp.Rational(-1, 3), "3"): "dR",
    (sp.Rational(1, 2), sp.Rational(-1, 2), "1"): "νL",
    (sp.Rational(-1, 2), sp.Rational(-1, 2), "1"): "eL",
    (sp.Integer(0), sp.Integer(0), "1"): "νR",
    (sp.Integer(0), sp.Integer(-1), "1"): "eR",
    # Conjugates (anti-particles)
    (sp.Rational(1, 2), sp.Rational(-1, 6), "3̄"): "ūL",
    (sp.Rational(-1, 2), sp.Rational(-1, 6), "3̄"): "d̄L",
    (sp.Integer(0), sp.Rational(-2, 3), "3̄"): "ūR",
    (sp.Integer(0), sp.Rational(1, 3), "3̄"): "d̄R",
    (sp.Rational(1, 2), sp.Rational(1, 2), "1̄"): "ν̄L",
    (sp.Rational(-1, 2), sp.Rational(1, 2), "1̄"): "ēL",
    (sp.Integer(0), sp.Integer(0), "1̄"): "ν̄R",
    (sp.Integer(0), sp.Integer(1), "1̄"): "ēR",
}

results = []
n = 0
for s3 in s3_states:
    for s6 in s6_states:
        n += 1
        T3L = s3["T3L"]
        T3R = s3["T3R"]
        BL = s6["BL"]
        Y = T3R + BL / 2
        su3 = s6["su3_rep"]
        col = s6["color"]

        sm_key = (T3L, Y, su3)
        sm_name = SM_TABLE.get(sm_key, "???")

        print(
            f"{n:>3} | {str(T3L):>4} {str(T3R):>4} {str(BL):>5} {str(Y):>5} | "
            f"{su3:>6} {col:>5} | {sm_name:>20}"
        )
        results.append(sm_name)

print("=" * 90)
matched = [r for r in results if r != "???"]
unknown = [r for r in results if r == "???"]
print(f"\nTotal states:    {len(results)}")
print(f"Matched to SM:   {len(matched)}/{len(results)}")
print(f"Unidentified:    {len(unknown)}")

# Check completeness: all 16 SM particles appear?
sm_particles = set(matched)
print(f"\nUnique SM labels found ({len(sm_particles)}): {sorted(sm_particles)}")

expected = {
    "uL",
    "dL",
    "uR",
    "dR",
    "νL",
    "eL",
    "νR",
    "eR",
    "ūL",
    "d̄L",
    "ūR",
    "d̄R",
    "ν̄L",
    "ēL",
    "ν̄R",
    "ēR",
}
missing = expected - sm_particles
extra = sm_particles - expected
print(f"Missing from SM: {missing}")
print(f"Extra (not SM):  {extra}")

# Count multiplicities
counts = Counter(matched)
print("\nMultiplicities (should be 2 each = color×isospin for quarks, 1 for others):")
for name in sorted(counts):
    print(f"  {name}: {counts[name]}")

all_match = len(unknown) == 0 and missing == set() and extra == set()
print(f"\nVERDICT: {'PASS_G6_SM_CONTENT_CONFIRMED' if all_match else 'FAIL — mismatch found'}")
