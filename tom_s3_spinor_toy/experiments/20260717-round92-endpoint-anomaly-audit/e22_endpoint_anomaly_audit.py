"""E22 (round92): Endpoint anomaly audit for the frozen G_eff =
SU(3)_c x SU(2)_L x SU(2)_R.

Purpose (per claim.md): test whether the two Cartan-Schouten torsion-
connection endpoints (t=0, t=1) each carry a nonzero anomaly for the FROZEN
gauge group G_eff = SU(3)_c x SU(2)_L x SU(2)_R (Option (i), irrevocably
chosen in claim.md Section 2, BEFORE this computation), while their union is
anomaly-free -- the pre-registered PASS pattern -- or whether the
computation cannot proceed (BLOCKED) or shows no forcing (FAIL).

This is arithmetic/bookkeeping over ALREADY-established project facts, cited
by file:line in comments. No new physics is derived. Every number that
cannot be traced to an existing citation is explicitly marked NOT COMPUTABLE
rather than assumed or imported from the Standard Model.
"""

import sympy as sp

# =============================================================================
# PART 0 -- Frozen gauge group (claim.md Section 2, irrevocable)
# =============================================================================
print("=" * 92)
print("PART 0 -- Frozen G_eff (claim.md Section 2, chosen BEFORE this computation)")
print("=" * 92)
G_EFF = "SU(3)_c x SU(2)_L x SU(2)_R"
print(f"  G_eff = {G_EFF}   [FROZEN, claim.md Section 2 -- not switched to SU(4)_PS]")
print("  Reason: preprint.tex admits (gate G97, preprint.tex:280-285, :420-424)")
print("  no SU(4) subgroup exists in Iso(S3xS6) -- Option (ii) is not")
print("  geometrically realized in this project's own construction.")
print()

# =============================================================================
# PART 1 -- Kernel content, reused verbatim from E9/E12/E16/E17/G67/G73/G74A
# (NOT re-derived here -- per claim.md Section 3 step 1)
# =============================================================================
print("=" * 92)
print("PART 1 -- Endpoint kernel content (reused, not re-derived)")
print("=" * 92)

dim_ker_D_S3_t = 2
# t=0: unconditional (experiments/20260717-round73-e9-explicit-parallel-spinor/
#      decision.md:44-62); t=1: under c0=-2 only (CONVENTION_TABLE.md row 5,
#      experiments/20260717-round76-e9followup-right-invariant-frame/
#      decision.md:129-168); both reused as a fixed total by
#      experiments/20260717-round78-e12-multiplicity-gate/decision.md:12-18.
n_triality_channels = 3
# G67 (experiments/20260621-g67-octonion-triality/decision.md:11-19): three
# independent Z3-triality channels (8_v, 8_s, 8_c).
dim_ker_D_S6_twisted_per_channel = 1
# Current, authoritative citation (read directly this round):
# preprint.tex:806-831 -- the G2-trivial isotypic component of S+ (x) S- is a
# 2-dim space (multiplicity 2 of the trivial G2-rep, preprint.tex:806), D+
# restricts to a map C^2 -> C^1 on it, and rank(D+|_1) = 1 is established by
# explicit computation (preprint.tex:825-831, citing
# experiments/20260708-dolan-casimir-g2su3 and
# experiments/20260714-round59-trivial-rank-certification, "three mutually
# reinforcing certifications"). This SUPERSEDES G74A's own original
# Schur's-lemma "pinning" argument (preprint.tex:815-819 explicitly says
# Schur's lemma alone does NOT fix the rank), per this project's own
# 2026-07-17 provenance correction (reused, not re-litigated, from round90/
# round91's identical citation discipline).

joint_kernel_dim_per_channel = dim_ker_D_S3_t * dim_ker_D_S6_twisted_per_channel
doublets_per_channel = sp.Rational(joint_kernel_dim_per_channel, 2)
doublets_total_per_endpoint = doublets_per_channel * n_triality_channels

print(f"  dim ker(D_S3,t)                    = {dim_ker_D_S3_t}  (both t=0, t=1)")
print(
    f"  dim ker(D_S6,twisted) per channel   = {dim_ker_D_S6_twisted_per_channel}  [preprint.tex:806-831]"
)
print(f"  n_triality_channels                 = {n_triality_channels}  [G67]")
print(f"  joint kernel dim per channel        = {joint_kernel_dim_per_channel}")
print(
    f"  => {doublets_per_channel} doublet per channel, {doublets_total_per_endpoint} total per endpoint (3 channels)"
)
print()
print("  Representation under SU(2)_L x SU(2)_R (Convention A, CONVENTION_TABLE.md")
print("  row 6; convention-independent up to an overall L<->R relabel, E17 Sec 1):")
print("    t=0 kernel: SU(2)_L SINGLET, SU(2)_R DOUBLET  -> (1,2)  per channel")
print("    t=1 kernel: SU(2)_L DOUBLET, SU(2)_R SINGLET  -> (2,1)  per channel")
print("  [E16 (round83): the 2-dim joint kernel per channel IS one irreducible")
print("   doublet, not two copies -- decision.md criteria table.]")
print()

# =============================================================================
# PART 2 -- G_eff representation assignment: SU(3)_c (derived) vs U(1)_Y (NOT
# established) -- claim.md Section 3 step 2
# =============================================================================
print("=" * 92)
print("PART 2 -- G_eff representation assignment: what is DERIVED vs UNESTABLISHED")
print("=" * 92)

# --- SU(3)_c: DERIVED from established facts ---------------------------------
# preprint.tex:440-441: "S6 carries a transitive action of G2 with isotropy
# subgroup SU(3), realizing S6 as the coset space G2/SU(3)" -- i.e. SU(3)_c is
# a SUBGROUP of G2. preprint.tex:806-831 (Part 1 above) establishes the
# dim-ker=1 zero mode lives inside, and IS, (a 1-dim subspace of) the
# G2-trivial isotypic component of S+ (x) S- -- i.e. G2 acts as the identity
# operator on the full 2-dim ambient space (multiplicity-2 trivial rep,
# preprint.tex:806), so ANY subspace of it, including whichever specific
# 1-dim subspace is the actual kernel (established by the later rank
# computation, not by this group-theory step), is automatically ALSO fixed
# pointwise by G2. A subgroup of a trivial-acting group also acts trivially.
# [INFERRED -- standard restriction-of-trivial-representation argument,
# combining preprint.tex:440-441 (SU(3) subset G2) with preprint.tex:806-831
# (the kernel's G2-triviality) -- not an independent new tool computation,
# but a direct, first-principles group-theoretic consequence of two
# already-established facts, reused per round91's identical inference
# (decision.md Section 1, "Direct group-theory consequence").]
su3_rep_of_s6_kernel = "SINGLET"
su3_derivation_is_established = True

print("  SU(3)_c representation of the S6-side twisted kernel (per channel):")
print(f"    = {su3_rep_of_s6_kernel}  [DERIVED: SU(3) subset G2 (preprint.tex:440-441)")
print("      + kernel lives in the G2-trivial isotypic component (preprint.tex:806-831)")
print("      => trivial subgroup restriction. Same for t=0 AND t=1 (S6 factor is")
print("      t-independent under the decoupling assumption D_full^2 = D_S3,t^2(x)I")
print("      + I(x)D_S6,twisted^2, E2/E12).]")
print(f"    su3_derivation_is_established = {su3_derivation_is_established}")
print()

# --- U(1)_Y / B-L: NOT established -------------------------------------------
# preprint.tex has TWO distinct, unreconciled Y-formulas:
#   (a) preprint.tex:302-305: Y = K3 + (B-L)/2, K3 "a U(1) quantum number
#       from the SU(3)-harmonic decomposition of S6" -- an S6-SIDE quantity,
#       used in the anomaly-verification computation preprint.tex:309-320.
#   (b) preprint.tex:408: Y = T3R + (B-L)/2 -- an S3-SIDE quantity (T3R is
#       exactly the quantum number E16/E17 use to label the t=0/t=1 kernels),
#       used ONLY in the Weinberg-angle section, which preprint.tex:420-431
#       itself calls "illustrative pending [SU(4) B-L] input, not a
#       computation with a well-defined completion path."
# g6_spinor_decomposition.py:20,163 uses formula (b) (Y = T3R + BL/2) with a
# NUMERIC B-L value assigned via bl_charge(), but bl_charge() (lines 40-69)
# is a function of an S6 WEIGHT VECTOR in the UNTWISTED 8-state decomposition
# -- it has never been evaluated on, or connected to, the specific twisted
# G2-singlet kernel vector from Part 1/preprint.tex:806-831 (a state of a
# DIFFERENT, twisted operator D_{S6,twisted}, not G6's plain weight-space
# operator). experiments/20260717-round83-joint-representation-decomposition/
# decision.md, "Assumptions carried, unresolved," item 3 (reused verbatim):
# "No explicit numeric B-L/SU(3)-representation value has ever been assigned
# in this project to the twisted S- kernel object specifically."
bl_value_of_s6_twisted_kernel = None  # NOT COMPUTABLE from established facts
y_formula_ambiguity_unreconciled = True  # two distinct Y-formulas, preprint.tex
# itself never states they are equal or which applies to System A's content

print("  U(1)_Y (hypercharge) of the S6-side twisted kernel (per channel):")
print(f"    B-L value = {bl_value_of_s6_twisted_kernel}  [NOT COMPUTABLE -- no numeric B-L")
print("      has ever been assigned to the twisted S6-kernel specifically,")
print("      per round83 decision.md 'Assumptions carried, unresolved' item 3.]")
print(f"    y_formula_ambiguity_unreconciled = {y_formula_ambiguity_unreconciled}")
print("      [preprint.tex:302-305 uses Y=K3+(B-L)/2 (S6-harmonic K3, used in the")
print("       anomaly check :309-320); preprint.tex:408 uses Y=T3R+(B-L)/2 (S3-side")
print("       T3R, used ONLY in the self-flagged-illustrative Weinberg section,")
print("       :420-431). preprint.tex never states these are the same quantity or")
print("       which one governs System A's t=0/t=1 endpoint content.]")
print()

# =============================================================================
# PART 3 -- Anomaly coefficients for G_eff's generators, per endpoint & union
# (claim.md Section 3 step 3)
# =============================================================================
print("=" * 92)
print("PART 3 -- Anomaly coefficients: [SU(3)_c]^3 (computable) vs U(1)_Y-mixed (blocked)")
print("=" * 92)

# [SU(3)_c]^3: computable directly from Part 2's DERIVED singlet assignment.
# The cubic Dynkin/anomaly coefficient of an SU(3) SINGLET is exactly 0 (a
# singlet contributes nothing to any SU(3) trace). This holds per channel,
# hence for the per-endpoint total (3 channels) and for the union, with no
# further input needed.
A_SU3c_cubed = {
    "t0_alone": 0,
    "t1_alone": 0,
    "union": 0,
}
print("  [SU(3)_c]^3 anomaly coefficient (computable -- both endpoints SU(3)_c singlets):")
for k, v in A_SU3c_cubed.items():
    print(f"    A([SU(3)_c]^3, {k}) = {v}")
su3c_cubed_forcing = (
    A_SU3c_cubed["t0_alone"] != 0 and A_SU3c_cubed["t1_alone"] != 0 and A_SU3c_cubed["union"] == 0
)
print(f"  Forcing pattern (PASS-shape: both endpoints != 0, union == 0)? {su3c_cubed_forcing}")
print("  -- both endpoints ALREADY zero alone: no forcing possible on this channel.")
print()

# [SU(3)_c]^2 U(1)_Y, [U(1)_Y]^3, [grav]^2 U(1)_Y: require the numeric B-L/Y
# value from Part 2, which is NOT COMPUTABLE. Explicitly mark as blocked
# rather than fabricating a placeholder number.
mixed_Y_conditions = ["[SU(3)_c]^2 U(1)_Y", "[U(1)_Y]^3", "[grav]^2 U(1)_Y"]
mixed_Y_computable = False
print("  U(1)_Y-mixed anomaly conditions (per claim.md Section 3 step 3):")
for cond in mixed_Y_conditions:
    print(f"    {cond}: NOT COMPUTABLE -- requires B-L value, Part 2 shows it is undetermined")
print(f"  mixed_Y_conditions_computable = {mixed_Y_computable}")
print()

# =============================================================================
# PART 4 -- Witten SU(2) global-anomaly parity (mod-2 doublet count),
# reusing round91's already tool-verified counts (claim.md Section 3 step 4)
# =============================================================================
print("=" * 92)
print("PART 4 -- Witten SU(2)_L / SU(2)_R doublet-parity count")
print("=" * 92)

# Reused directly from experiments/20260717-round91-su2r-doublet-parity-check/
# e21_su2r_doublet_parity_count.py Parts 1-2 (verdict dict): t=0 alone gives
# 3 SU(2)_R doublets (ODD); t=1 alone gives 3 SU(2)_L doublets (ODD, and this
# SAME System-A methodology was shown there to FAIL its own SU(2)_L
# cross-check against the independently-known-EVEN true SM count of 12).
su2R_doublets = {"t0_alone": 3, "t1_alone": 0, "union": 3}
su2L_doublets = {"t0_alone": 0, "t1_alone": 3, "union": 3}
# t=0 is an SU(2)_L SINGLET (contributes 0 SU(2)_L doublets); t=1 is an
# SU(2)_R SINGLET (contributes 0 SU(2)_R doublets) -- Part 1's representation
# assignment. So the union's count, for EACH SU(2) factor separately, is
# supplied ENTIRELY by the one endpoint charged under that factor -- the
# other endpoint contributes exactly zero, not a partial cross-term.

for group, counts in [("SU(2)_R", su2R_doublets), ("SU(2)_L", su2L_doublets)]:
    print(f"  {group} doublet count:")
    for k, v in counts.items():
        parity = "EVEN" if v % 2 == 0 else "ODD"
        print(f"    {k}: {v} doublets -> {parity}")
    union_changes_parity = (counts["union"] % 2) != (
        counts["t0_alone" if group == "SU(2)_R" else "t1_alone"] % 2
    )
    print(
        f"    union changes parity relative to the charged endpoint alone? {union_changes_parity}"
    )
print()
print("  Interpretation: since each endpoint is a TOTAL SINGLET under the OTHER")
print("  SU(2) factor, the union does not, and structurally cannot, alter either")
print("  factor's own Witten parity -- there is no cross-endpoint cancellation")
print("  available for this specific quantity, for either SU(2)_L or SU(2)_R.")
print("  [Consistent with, and independently reinforcing, round90's own correction")
print("  that Witten SU(2) parity was never the right forcing mechanism for")
print("  'why both sectors are needed' -- it shows the union supplies no parity")
print("  cancellation here either, for either factor.]")
print()

# =============================================================================
# VERDICT
# =============================================================================
print("=" * 92)
print("VERDICT INPUTS")
print("=" * 92)

verdict = {
    "G_eff": G_EFF,
    "su3_derivation_is_established": su3_derivation_is_established,
    "su3_rep_of_s6_kernel": su3_rep_of_s6_kernel,
    "bl_value_of_s6_twisted_kernel_computable": bl_value_of_s6_twisted_kernel is not None,
    "y_formula_ambiguity_unreconciled": y_formula_ambiguity_unreconciled,
    "A_SU3c_cubed_t0_alone": A_SU3c_cubed["t0_alone"],
    "A_SU3c_cubed_t1_alone": A_SU3c_cubed["t1_alone"],
    "A_SU3c_cubed_union": A_SU3c_cubed["union"],
    "su3c_cubed_forcing_pattern_present": su3c_cubed_forcing,
    "mixed_Y_conditions_computable": mixed_Y_computable,
    "su2R_doublets_t0_alone": su2R_doublets["t0_alone"],
    "su2R_doublets_union": su2R_doublets["union"],
    "su2L_doublets_t1_alone": su2L_doublets["t1_alone"],
    "su2L_doublets_union": su2L_doublets["union"],
    "witten_parity_forcing_pattern_present": False,
}
for k, v in verdict.items():
    print(f"  {k}: {v}")

print()
print("label = 'BLOCKED__U1Y_MIXED_ANOMALY_CONDITIONS_NOT_COMPUTABLE")
print("         (BL_VALUE_OF_TWISTED_S6_KERNEL_UNESTABLISHED)__")
print("         SU3C_CUBED_CONDITION_COMPUTABLE_BUT_SHOWS_NO_FORCING__")
print("         WITTEN_PARITY_COMPUTABLE_BUT_SHOWS_NO_UNION_CANCELLATION'")
