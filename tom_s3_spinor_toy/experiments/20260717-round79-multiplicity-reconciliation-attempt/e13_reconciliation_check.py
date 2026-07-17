"""E13 (round79): Does the pre-existing G6 "32-state" bookkeeping already require
exactly the S3+/S3- structure the torsion-escape zero modes (E9-E12) supply?

Context (see decision.md for full citations):
  - E12 (round78) found dim ker(D_{S3,t=0}) = dim ker(D_{S3,t=1}) = 2, each an
    irreducible SU(2) doublet (E11/round77): t=0 -> SU(2)_L singlet / SU(2)_R doublet;
    t=1 (under c0=-2) -> SU(2)_L doublet / SU(2)_R singlet.
  - G6 (experiments/20260615-g6-s3xs6-spinor-content/g6_spinor_decomposition.py),
    written 2026-06-15 -- BEFORE the torsion-escape program existed (round66+,
    started 2026-07-17) -- already splits the S3-side "4-component SO(4) spinor
    representation" into two 2-dimensional blocks by chirality:
      chir_s3="+": (T3L=+-1/2, T3R=0)   -- SU(2)_L doublet, SU(2)_R singlet
      chir_s3="-": (T3L=0, T3R=+-1/2)   -- SU(2)_L singlet, SU(2)_R doublet
    This experiment checks, independently and computationally:
      (1) does dim(chir_s3="+") == dim(chir_s3="-") == 2, matching E12's dim ker=2
          at each of t=0, t=1? [dimension-match check]
      (2) does the representation LABEL match -- i.e. is chir_s3="-" really the
          SU(2)_L-singlet/SU(2)_R-doublet block (matching t=0's E11 label) and
          chir_s3="+" really the SU(2)_L-doublet/SU(2)_R-singlet block (matching
          t=1's E11 label)? [label-match check]
      (3) is the particle/antiparticle (CPT-conjugate) doubling that produces "32"
          from "16" carried ENTIRELY by the S6 factor (via the B-L sign / S+/S-
          chirality), with the S3-side chir_s3 assignment IDENTICAL for a particle
          and its own CPT conjugate? [tests whether option (b) -- "the doublet IS a
          particle+antiparticle pair" -- is even representationally possible under
          G6's own construction, independent of E9-E12]

The S3-side table (s3_states) and the SM_TABLE (including its own explicit
"Conjugates (anti-particles)" block) below are copied VERBATIM from
experiments/20260615-g6-s3xs6-spinor-content/g6_spinor_decomposition.py
(not imported, so this experiment's folder is self-contained and does not modify
that file) -- this is a cross-check against an existing, independent artifact,
not a new postulate.
"""

import sympy as sp
from itertools import product as iproduct

# ─── S3 spinor states (verbatim copy from G6) ───────────────────────────────
s3_states = [
    {"T3L": sp.Rational(1, 2), "T3R": sp.Integer(0), "chir_s3": "+"},
    {"T3L": sp.Rational(-1, 2), "T3R": sp.Integer(0), "chir_s3": "+"},
    {"T3L": sp.Integer(0), "T3R": sp.Rational(1, 2), "chir_s3": "-"},
    {"T3L": sp.Integer(0), "T3R": sp.Rational(-1, 2), "chir_s3": "-"},
]


def bl_charge(weight):
    """Verbatim copy of G6's bl_charge (B-L charge + SU(3) rep from S6 weight)."""
    n_minus = sum(1 for x in weight if x < 0)
    chirality = "+" if n_minus % 2 == 0 else "-"
    if chirality == "+":
        all_same = weight[0] == weight[1] == weight[2]
        if all_same:
            return sp.Integer(-1), "1", "nu/e (lepton)", chirality
        else:
            return sp.Rational(1, 3), "3", "q (quark)", chirality
    else:
        all_same = weight[0] == weight[1] == weight[2]
        if all_same:
            return sp.Integer(1), "1bar", "nubar/ebar (anti-lepton)", chirality
        else:
            return sp.Rational(-1, 3), "3bar", "qbar (anti-quark)", chirality


all_weights = list(iproduct([sp.Rational(-1, 2), sp.Rational(1, 2)], repeat=3))
s6_states = []
for w in all_weights:
    bl, su3_rep, desc, chir6 = bl_charge(w)
    s6_states.append({"weight": w, "chir_s6": chir6, "BL": bl, "su3_rep": su3_rep})

# ─── SM_TABLE (verbatim copy from G6, including its own "Conjugates" block) ─
SM_TABLE = {
    (sp.Rational(1, 2), sp.Rational(1, 6), "3"): "uL",
    (sp.Rational(-1, 2), sp.Rational(1, 6), "3"): "dL",
    (sp.Integer(0), sp.Rational(2, 3), "3"): "uR",
    (sp.Integer(0), sp.Rational(-1, 3), "3"): "dR",
    (sp.Rational(1, 2), sp.Rational(-1, 2), "1"): "nuL",
    (sp.Rational(-1, 2), sp.Rational(-1, 2), "1"): "eL",
    (sp.Integer(0), sp.Integer(0), "1"): "nuR",
    (sp.Integer(0), sp.Integer(-1), "1"): "eR",
    # Conjugates (anti-particles) -- verbatim from G6
    (sp.Rational(1, 2), sp.Rational(-1, 6), "3bar"): "uLbar",
    (sp.Rational(-1, 2), sp.Rational(-1, 6), "3bar"): "dLbar",
    (sp.Integer(0), sp.Rational(-2, 3), "3bar"): "uRbar",
    (sp.Integer(0), sp.Rational(1, 3), "3bar"): "dRbar",
    (sp.Rational(1, 2), sp.Rational(1, 2), "1bar"): "nuLbar",
    (sp.Rational(-1, 2), sp.Rational(1, 2), "1bar"): "eLbar",
    (sp.Integer(0), sp.Integer(0), "1bar"): "nuRbar",
    (sp.Integer(0), sp.Integer(1), "1bar"): "eRbar",
}

# Particle <-> CPT-conjugate pairing, read directly off the SM_TABLE's own
# particle/antiparticle naming (X <-> Xbar), NOT a new postulate.
CONJUGATE_PAIRS = [
    ("uL", "uLbar"),
    ("dL", "dLbar"),
    ("uR", "uRbar"),
    ("dR", "dRbar"),
    ("nuL", "nuLbar"),
    ("eL", "eLbar"),
    ("nuR", "nuRbar"),
    ("eR", "eRbar"),
]

# ─── Regenerate the full 32-state table, recording (name, chir_s3, T3L, T3R) ─
records = []
for s3 in s3_states:
    for s6 in s6_states:
        T3L, T3R = s3["T3L"], s3["T3R"]
        BL = s6["BL"]
        Y = T3R + BL / 2
        sm_key = (T3L, Y, s6["su3_rep"])
        sm_name = SM_TABLE.get(sm_key, "???")
        records.append({"name": sm_name, "chir_s3": s3["chir_s3"], "T3L": T3L, "T3R": T3R})

matched = [r for r in records if r["name"] != "???"]
assert len(records) == 32, f"expected 32 total states, got {len(records)}"
assert len(matched) == 32, (
    f"expected 32/32 matched, got {len(matched)}/32 (G6 cross-check itself failed)"
)

# ─── Check 1: dimension of each chir_s3 block ───────────────────────────────
dim_plus = len(s3_states_plus := [s for s in s3_states if s["chir_s3"] == "+"])
dim_minus = len(s3_states_minus := [s for s in s3_states if s["chir_s3"] == "-"])
dimension_match_t1_su2L_doublet = dim_plus == 2  # t=1 candidate: SU(2)_L doublet
dimension_match_t0_su2R_doublet = dim_minus == 2  # t=0 candidate: SU(2)_R doublet

# ─── Check 2: representation LABEL of each block ───────────────────────────
plus_is_su2L_doublet_su2R_singlet = all(s["T3L"] != 0 and s["T3R"] == 0 for s in s3_states_plus)
minus_is_su2L_singlet_su2R_doublet = all(s["T3L"] == 0 and s["T3R"] != 0 for s in s3_states_minus)

# ─── Check 3: is CPT-conjugate doubling independent of chir_s3? ────────────
# For every (particle, antiparticle) pair, find every 32-state RECORD carrying
# that name (there may be several, since colour is an S6-side label reused
# across records with the same SM name; chir_s3 must be IDENTICAL across all
# of them, and identical between particle and antiparticle).
name_to_chir = {}
for r in matched:
    name_to_chir.setdefault(r["name"], set()).add(r["chir_s3"])

# Sanity: each SM name should map to exactly one chir_s3 value (no internal
# contradiction within G6's own table).
internally_consistent = all(len(v) == 1 for v in name_to_chir.values())

cpt_doubling_independent_of_chir_s3 = True
pair_report = []
for particle, antiparticle in CONJUGATE_PAIRS:
    chir_p = next(iter(name_to_chir[particle]))
    chir_a = next(iter(name_to_chir[antiparticle]))
    same = chir_p == chir_a
    pair_report.append((particle, antiparticle, chir_p, chir_a, same))
    if not same:
        cpt_doubling_independent_of_chir_s3 = False

# ─── Report ──────────────────────────────────────────────────────────────
print("=" * 78)
print("E13 (round79): S3+/S3- block vs torsion zero-mode dimension/label cross-check")
print("=" * 78)
print(f"dim(chir_s3='+')  = {dim_plus}  (t=1 SU(2)_L-doublet candidate needs 2)")
print(f"dim(chir_s3='-')  = {dim_minus}  (t=0 SU(2)_R-doublet candidate needs 2)")
print(f"plus block is SU(2)_L doublet / SU(2)_R singlet: {plus_is_su2L_doublet_su2R_singlet}")
print(f"minus block is SU(2)_L singlet / SU(2)_R doublet: {minus_is_su2L_singlet_su2R_doublet}")
print(f"internally_consistent (no name maps to 2 different chir_s3): {internally_consistent}")
print()
print(f"{'particle':>8} {'antiparticle':>12} {'chir(p)':>8} {'chir(anti)':>10} {'same?':>6}")
for particle, antiparticle, chir_p, chir_a, same in pair_report:
    print(f"{particle:>8} {antiparticle:>12} {chir_p:>8} {chir_a:>10} {str(same):>6}")
print()
print(f"cpt_doubling_independent_of_chir_s3 = {cpt_doubling_independent_of_chir_s3}")
print("  (True  => option (b) REFUTED: CPT/antiparticle doubling is carried entirely")
print("            by the S6 factor; chir_s3 [hence the S3 zero-mode's SU(2) content]")
print("            cannot be reinterpreted as 'particle vs antiparticle'.)")
print("  (False => option (b) would remain representation-theoretically possible.)")

verdict = {
    "g6_cross_check_32_of_32_matched": len(matched) == 32,
    "dimension_match_t0": dimension_match_t0_su2R_doublet,
    "dimension_match_t1": dimension_match_t1_su2L_doublet,
    "label_match_t0": minus_is_su2L_singlet_su2R_doublet,
    "label_match_t1": plus_is_su2L_doublet_su2R_singlet,
    "internally_consistent": internally_consistent,
    "cpt_doubling_independent_of_chir_s3": cpt_doubling_independent_of_chir_s3,
}
structural_option_a_confirmed = all(
    [
        verdict["dimension_match_t0"],
        verdict["dimension_match_t1"],
        verdict["label_match_t0"],
        verdict["label_match_t1"],
    ]
)
option_b_refuted = (
    verdict["internally_consistent"] and verdict["cpt_doubling_independent_of_chir_s3"]
)
verdict["structural_option_a_confirmed"] = structural_option_a_confirmed
verdict["option_b_refuted"] = option_b_refuted
verdict["label"] = (
    "STRUCTURAL_A_CONFIRMED__B_REFUTED__PHYSICAL_MECHANISM_STILL_OPEN"
    if structural_option_a_confirmed and option_b_refuted
    else "INCONCLUSIVE_SEE_DECISION_MD"
)

print()
print("verdict:", verdict)
