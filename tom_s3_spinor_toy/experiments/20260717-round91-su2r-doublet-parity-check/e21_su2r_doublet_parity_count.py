"""E21-followup (round91): SU(2)_R doublet-parity counting exercise.

Purpose (per claim.md): round90 (E21) found preprint.tex genuinely gauges
SU(2)_R, and flagged (Relaxation Map) that Witten's SU(2) global anomaly
(Phys. Lett. B117, 324, 1982) requires an EVEN number of gauged SU(2)_R
doublets. Round90 did NOT check whether this project's OWN already-established
fermion content actually gives an even or odd count. This script does that
count, using ONLY numbers already tool-verified in prior rounds (cited by
file:line in comments), and does NOT introduce any new physics.

This is arithmetic/bookkeeping, not a new derivation. Every number below is
imported from a cited source; nothing is fitted or assumed beyond what is
explicitly flagged as an assumption.
"""

import sympy as sp

# ---------------------------------------------------------------------------
# PART 0 — the two competing bookkeeping systems this project has never
# reconciled (E12 decision.md Section E.2; E17 decision.md Section 2, both
# reused verbatim below, not re-derived).
# ---------------------------------------------------------------------------

print("=" * 88)
print("PART 0 — Two distinct S3/S6 bookkeeping systems in this project")
print("=" * 88)

# System A: the torsion-escape-route zero-mode kernel bookkeeping (E9-E17).
# This is the ONLY bookkeeping that is actually indexed by the connection
# parameter t (t=0 vs t=1). Established numbers:
dim_ker_D_S3_t = 2  # E9 (t=0, unconditional) / E9-followup+round76 (t=1, under c0=-2 only);
# reused by E12 decision.md:12-18 ("Section D - total count")
n_triality_channels = 3  # G67 decision.md: three independent Z3-triality channels (8_v,8_s,8_c)
dim_ker_D_S6_twisted_per_channel = 1  # G74A decision.md Lemma B: "G2-rep content of S-:
# exactly one G2-singlet per triality channel ->
# dim ker <= 1 per channel"; combined with G73's
# ind=1 (>=1) gives dim ker == 1 EXACTLY.
# NOTE (provenance): the ORIGINAL two lemmas in
# G74A's file are now known to be insufficient
# (see G74A decision.md's own 2026-07-17 superseded-
# note); the dim-ker=1 NUMBER itself is unaffected,
# now attributed to dolan-casimir-g2su3/round59.

joint_kernel_dim_per_channel_system_A = dim_ker_D_S3_t * dim_ker_D_S6_twisted_per_channel
print("System A (torsion-kernel bookkeeping, E9-E17):")
print(f"  dim ker(D_S3,t)                         = {dim_ker_D_S3_t}   [E9/E12]")
print(
    f"  dim ker(D_S6,twisted) per channel        = {dim_ker_D_S6_twisted_per_channel}   [G74A Lemma B]"
)
print(f"  => joint kernel dim per channel, per t   = {joint_kernel_dim_per_channel_system_A}")
print("  E16 (round83) already tool-verified this 2-dim joint kernel IS one")
print("  irreducible SU(2) doublet (T3=+1/2 and T3=-1/2 of the SAME multiplet,")
print("  same S6-side quantum numbers) -- decision.md Section A + criteria table.")
print()

# G74A Lemma B's "G2-singlet" fact has a direct group-theory consequence used
# below: SU(3) is a subgroup of G2 (S6 = G2/SU(3), G9). A vector invariant
# under all of G2 is automatically invariant under any subgroup of G2,
# including SU(3)_c. So the dim=1 zero mode is an SU(3)_c SINGLET.
# [INFERRED from G74A Lemma B + G9's S6=G2/SU(3) fact -- standard restriction-
# of-trivial-representation argument, not independently re-derived by a new
# tool computation this round.]
system_A_is_su3_singlet = True
print("  System A's per-channel S6 zero mode is a G2-singlet (G74A Lemma B),")
print("  hence also an SU(3)_c-singlet (SU(3) subset G2, S6=G2/SU(3), G9):")
print(f"  is_su3_singlet = {system_A_is_su3_singlet}  [INFERRED, standard rep-theory]")
print("  => System A carries NO internal color multiplicity at all.")
print()

# System B: G6's own pre-existing "one generation" bookkeeping
# (g6_spinor_decomposition.py, dated 2026-06-15 -- PRE-DATES the entire t-
# parameter torsion-escape-route program, first introduced by E2/round67,
# dated 2026-06-22). G6 has NO "t" variable anywhere in the file: it lists
# the FULL 4-component S3 Dirac spinor (all 4 states = both chiralities),
# not a specific 2-dim kernel of a specific torsion-deformed operator.
print("System B (G6's pre-existing SM-content bookkeeping, pre-dates t entirely):")
print("  g6_spinor_decomposition.py:29-36 -- 4 S3-side states (ALL of them, not")
print("  restricted to any one t-value), tensored with 8 S6-side states (with")
print("  explicit SU(3) color + B-L structure via su3_label()/bl_charge(),")
print("  g6_spinor_decomposition.py:40-102).")
print()
print("  E17 (round85) decision.md Section 2/3 already established: G6's 4 S3-")
print("  states = EXACTLY the union {ker D^t=0} U {ker D^t=1} (2+2=4), i.e. each")
print("  INDIVIDUAL t-kernel maps onto HALF of G6's s3_states list (2 of the 4),")
print("  under either SU(2)_L/SU(2)_R labeling convention (CONVENTION_TABLE.md row 6).")
print()
print("  BUT: whether G6's SEPARATE 8-state s6-bookkeeping (color-carrying) is the")
print("  same object as G74A's 1-dim, colorless, twisted-operator kernel is NOT")
print("  established anywhere in this project -- flagged explicitly as open by")
print("  E12 decision.md Section E.2 and re-flagged by E17 decision.md Section 2")
print("  ('two logically separate bookkeeping exercises this project has never")
print("  reconciled').")
print()

# ---------------------------------------------------------------------------
# PART 1 — SU(2)_R doublet count from t=0 alone, System A only (the ONLY
# system that is actually t-indexed, hence the only one directly answering
# "what does t=0 SPECIFICALLY supply").
# ---------------------------------------------------------------------------

print("=" * 88)
print("PART 1 -- SU(2)_R doublet count from t=0 alone (System A, the only")
print("          t-indexed bookkeeping this project has)")
print("=" * 88)

doublets_per_channel_from_t0 = sp.Rational(joint_kernel_dim_per_channel_system_A, 2)
total_doublets_from_t0_system_A = doublets_per_channel_from_t0 * n_triality_channels

print(
    f"  Per channel: joint kernel dim = {joint_kernel_dim_per_channel_system_A}"
    f" => {doublets_per_channel_from_t0} SU(2)_R doublet(s) per channel"
)
print(
    f"  Across all {n_triality_channels} channels: "
    f"{doublets_per_channel_from_t0} x {n_triality_channels} = {total_doublets_from_t0_system_A}"
)

parity_per_channel = "EVEN" if (doublets_per_channel_from_t0 % 2 == 0) else "ODD"
parity_total = "EVEN" if (total_doublets_from_t0_system_A % 2 == 0) else "ODD"
print(f"  Per-generation parity:  {doublets_per_channel_from_t0} -> {parity_per_channel}")
print(f"  Total (3 gen) parity:   {total_doublets_from_t0_system_A} -> {parity_total}")
print()
print("  preprint.tex:317 ('All four conditions are satisfied with each")
print("  generation separately anomaly-free; no inter-generation cancellation")
print("  is required') is this project's OWN stated convention for how its")
print("  anomaly checks are structured -- per generation, not summed. Under")
print("  that convention, 1 doublet/generation is itself already the number")
print("  to check, and it is ODD regardless of how many generations exist.")
print()

# ---------------------------------------------------------------------------
# PART 2 — Cross-check: apply the IDENTICAL System-A methodology to SU(2)_L
# (t=1 sector), per the task's requested symmetry check.
# ---------------------------------------------------------------------------

print("=" * 88)
print("PART 2 -- Cross-check: apply the SAME System-A methodology to SU(2)_L (t=1)")
print("=" * 88)

# dim ker(D_S3,t=1) = 2 also (E12 decision.md:12-18), under c0=-2 only
# (CONVENTION_TABLE.md row 5). The decoupling assumption D_full^2 =
# D_S3,t^2 (x) I + I (x) D_S6,twisted^2 (E2/E12) means the SAME 1-dim,
# per-channel, colorless S6-twisted kernel tensors with t=1's 2-dim S3
# kernel exactly as it does with t=0's -- nothing in the S6 factor depends
# on t. So the count is structurally IDENTICAL.
dim_ker_D_S3_t1 = 2
joint_kernel_dim_per_channel_t1 = dim_ker_D_S3_t1 * dim_ker_D_S6_twisted_per_channel
doublets_per_channel_from_t1 = sp.Rational(joint_kernel_dim_per_channel_t1, 2)
total_doublets_from_t1_system_A = doublets_per_channel_from_t1 * n_triality_channels

print(f"  Per channel: {doublets_per_channel_from_t1} SU(2)_L doublet(s) per channel")
print(f"  Across {n_triality_channels} channels: {total_doublets_from_t1_system_A} total")
print(f"  Parity: {'EVEN' if total_doublets_from_t1_system_A % 2 == 0 else 'ODD'}")
print()
print("  Known-independently-true fact (real SM / this project's OWN separate")
print("  System B, preprint.tex:289-298 + g6_spinor_decomposition.py SM_TABLE):")
print("  SU(2)_L doublet count per generation = 3 color quark doublets")
print("  (u,d)_L x{r,g,b} + 1 lepton doublet (nu,e)_L = 4 doublets/generation,")
print("  EVEN; x 3 generations = 12, EVEN. This is required for the REAL")
print("  Standard Model to be Witten-anomaly-consistent, and is independently")
print("  well established (external, textbook fact -- SU(2)_L IS gauged and IS")
print("  known anomaly-free).")
print()
consistency_check_passes = total_doublets_from_t1_system_A % 2 == 0
print("  Does System-A's methodology reproduce this independently-known-even")
print(
    f"  count for SU(2)_L?  {total_doublets_from_t1_system_A} is "
    f"{'EVEN -> PASS' if consistency_check_passes else 'ODD -> METHODOLOGY FAILS ITS OWN CROSS-CHECK'}"
)

# ---------------------------------------------------------------------------
# PART 3 — What System B (G6's bookkeeping) would give, IF it could be
# validly substituted for System A (an assumption this project has NOT
# established -- shown here only to make the size of the gap concrete).
# ---------------------------------------------------------------------------

print()
print("=" * 88)
print("PART 3 -- For reference only: what System B (G6, color-carrying) would")
print("          give IF (unestablished) it could stand in for System A")
print("=" * 88)

# G6's s3_states split cleanly into 2 chir_s3="+" (SU(2)_L doublet, T3L=+-1/2,
# T3R=0) and 2 chir_s3="-" (SU(2)_R doublet, T3L=0, T3R=+-1/2) states
# (g6_spinor_decomposition.py:29-36, docstring lines 8-10).
# Per E17 decision.md Section 1's Convention-A table (round77/E11 T3
# eigenvalues, reused): t=0 <-> (1,2) = SU(2)_L singlet / SU(2)_R doublet;
# t=1 <-> (2,1) = SU(2)_L doublet / SU(2)_R singlet. So under Convention A,
# t=0's "System B analogue" is G6's chir_s3="-" pair.
s6_state_count = 8  # g6_spinor_decomposition.py:106 (all_weights, 2**3=8)
lepton_and_color_doublets_per_generation = 1 + 3  # 1 lepton doublet + 3 quark-color
# doublets, from bl_charge()/
# su3_label() structure
# (g6_spinor_decomposition.py:40-102)
# G6's 8 s6-states ALREADY include the CPT-conjugate ("antiparticle") states
# (preprint.tex:296-298: "32 = one generation ... plus their CPT conjugates";
# E13/round79 established CPT-doubling is carried entirely by the S6 factor's
# B-L sign). So the 8 s6-states = 4 "particle" + 4 "antiparticle" states,
# meaning the chir_s3="-" x 8-s6-states tensor product (16 states = 8
# doublets) already counts each independent physical Weyl fermion TWICE
# (once as itself, once as its own CPT conjugate) if CPT conjugates are not
# separately gauge-charged degrees of freedom.
doublets_including_cpt_conjugates = lepton_and_color_doublets_per_generation * 2  # = 8
doublets_excluding_cpt_conjugates = lepton_and_color_doublets_per_generation  # = 4

print(
    f"  System B, per generation, INCLUDING CPT-conjugate duplicates: "
    f"{doublets_including_cpt_conjugates} doublets"
)
print(
    f"  System B, per generation, EXCLUDING CPT-conjugate duplicates "
    f"(only independent d.o.f.): {doublets_excluding_cpt_conjugates} doublets"
)
for label, per_gen in [
    ("including CPT dup.", doublets_including_cpt_conjugates),
    ("excluding CPT dup.", doublets_excluding_cpt_conjugates),
]:
    total = per_gen * n_triality_channels
    parity = "EVEN" if total % 2 == 0 else "ODD"
    print(f"    x {n_triality_channels} channels ({label}): {total} total -> {parity}")

print()
print("  Both System-B readings give EVEN totals -- but System B is NOT")
print("  established as the correct target for the t=0/t=1 zero-mode")
print("  construction (E12 Section E.2 / E17 Section 2, unresolved).")

# ---------------------------------------------------------------------------
# VERDICT
# ---------------------------------------------------------------------------

print()
print("=" * 88)
print("VERDICT INPUTS")
print("=" * 88)
verdict = {
    "system_A_doublets_from_t0_per_channel": int(doublets_per_channel_from_t0),
    "system_A_doublets_from_t0_total": int(total_doublets_from_t0_system_A),
    "system_A_su2R_count_parity": parity_total,
    "system_A_su2L_crosscheck_total": int(total_doublets_from_t1_system_A),
    "system_A_su2L_crosscheck_parity": "EVEN"
    if total_doublets_from_t1_system_A % 2 == 0
    else "ODD",
    "system_A_su2L_crosscheck_matches_known_truth": consistency_check_passes,
    "system_B_doublets_incl_cpt_total": int(
        doublets_including_cpt_conjugates * n_triality_channels
    ),
    "system_B_doublets_excl_cpt_total": int(
        doublets_excluding_cpt_conjugates * n_triality_channels
    ),
    "system_A_and_system_B_reconciled_in_project_text": False,  # E12 Sec E.2 / E17 Sec 2
}
for k, v in verdict.items():
    print(f"  {k}: {v}")

print()
print("label = 'BLOCKED__SYSTEM_A_METHODOLOGY_FAILS_SU2L_CROSSCHECK__")
print("         SYSTEM_B_NOT_ESTABLISHED_AS_APPLICABLE_TO_T0_T1_SPLIT'")
