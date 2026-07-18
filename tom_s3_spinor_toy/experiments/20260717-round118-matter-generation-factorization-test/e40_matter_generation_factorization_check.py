"""Round118: checks the structural precondition for the user's own
H_physical = H_matter (x) H_generation hypothesis -- does the ALREADY-
established twisted kernel (dim=1 per channel, round59/dolan-casimir;
genuine SU(4) singlet, round107) leave room for a nontrivial H_matter
factor within it, and does gate G97 (already established, rounds
102/108/109) block the existence of an independently-derivable H_matter
carrying genuine SU(4) (4,4bar) content anywhere in this project's
current geometry.
"""


print("=" * 92)
print("PART 1 -- dimension-counting precondition: can a 1-dim space factor")
print("nontrivially as H_matter (x) H_generation?")
print("=" * 92)
dim_kernel = 1  # round59/dolan-casimir, re-confirmed round94/round107, per channel
# For V = A (x) B, dim(V) = dim(A) * dim(B). Enumerate all factorizations of dim=1.
factorizations = [
    (a, b)
    for a in range(1, dim_kernel + 1)
    for b in range(1, dim_kernel + 1)
    if a * b == dim_kernel
]
nontrivial_factorizations = [(a, b) for (a, b) in factorizations if a > 1 and b > 1]
print(f"  dim(twisted kernel), per channel = {dim_kernel}")
print(f"  All (dim H_matter, dim H_generation) pairs with product = {dim_kernel}: {factorizations}")
print(f"  Any NONTRIVIAL factorization (both factors > 1)? {bool(nontrivial_factorizations)}")
print()
print("  Conclusion: the ONLY factorization of a 1-dimensional space is the")
print("  trivial one (1x1). If H_generation is meant to BE (or contain) the")
print("  already-computed twisted kernel, there is no room, dimensionally,")
print("  for a nontrivial H_matter to coexist WITHIN it.")
print()

print("=" * 92)
print("PART 2 -- does gate G97 block an independently-derivable H_matter")
print("carrying genuine SU(4) (4,4bar) content?")
print("=" * 92)
# G97 (rounds 102/108/109, already established this session, cited not re-derived):
# no SU(4) gauge-algebra realization exists in Iso(S3xS6)=SO(4)xSO(7), closed
# THREE independent ways within the standard product-manifold framework:
#   - round102: so(6)=su(4) as algebras, but SU(4)!=SO(6) as groups (isometry
#     mismatch)
#   - round108: true stabilizer of full G2/SU(3) background = 14(g2)/8(su3),
#     both <15 -- closes same-factor SU(4) embedding
#   - round109: general Lie-theory argument -- su(4) simple, dim(so(4))=6<15,
#     forces so(4)-component to zero for ANY su(4)->so(4)+X homomorphism --
#     closes diagonal embedding too
g97_same_factor_closed = True  # round108
g97_diagonal_closed = True  # round109
g97_fully_closed_within_product_framework = g97_same_factor_closed and g97_diagonal_closed
print(f"  G97 same-factor SU(4) embedding closed (round108)? {g97_same_factor_closed}")
print(f"  G97 diagonal SU(4) embedding closed (round109)? {g97_diagonal_closed}")
print(
    f"  G97 fully closed within the standard product-manifold framework? {g97_fully_closed_within_product_framework}"
)
print()
print("  Since H_matter (as specified: carrying genuine SU(4) (4,4bar)")
print("  Pati-Salam representation content) would require an SU(4) gauge-")
print("  algebra realization to be a PHYSICALLY MEANINGFUL (gauged) matter")
print("  sector -- and G97 already rules this out geometrically, for the")
print("  same reason the whole Pati-Salam anomaly-forcing program (rounds")
print("  90-112) was blocked -- no independently-derivable candidate for")
print("  H_matter, in the SU(4)-gauged sense the hypothesis specifies, is")
print("  currently constructible from this project's own established")
print("  geometry.")
print()

print("=" * 92)
print("PART 3 -- the OTHER reading (skeptic-demanded, not in the first draft):")
print("does H_physical = H_matter(32-dim, already-established SU(3)xSU(2)LxSU(2)R")
print("content) (x) H_generation(3-dim, one slot per triality channel) hold, WITHOUT")
print("invoking SU(4) at all -- is this weaker reading trivially already true?")
print("=" * 92)
n_channels = 3  # G67/G73, established
dim_one_generation_content = 32  # preprint.tex, established (per channel)
dim_H_physical_weak_reading = n_channels * dim_one_generation_content
print(f"  H_generation dimension (one slot per triality channel) = {n_channels}")
print(
    f"  H_matter dimension (established SU(3)xSU(2)LxSU(2)R content, one generation) = {dim_one_generation_content}"
)
print(f"  H_physical = H_matter (x) H_generation, total dimension = {dim_H_physical_weak_reading}")
print()
print("  Key question: does the GAUGE GROUP (SU(3)xSU(2)LxSU(2)R) act IDENTICALLY")
print("  on each of the 3 channels (i.e. is the charge formula Q=T3L+Y,")
print("  Y=K3+(B-L)/2 CHANNEL-INDEPENDENT, with no channel-index anywhere in its")
print("  definition), while triality (G67) acts ONLY on the channel label?")
# [VERIFIED-tool, this round, second skeptic pass]: freshly grepped, not asserted --
# `grep -n "8_v\|8_s\|8_c" preprint.tex | grep "Q\s*=\|Y\s*=\|T_{3"` returns ZERO hits.
# preprint.tex's own Q,Y,T3L,T3R formulas (lines 300-301) are stated once, universally,
# with no per-channel (8_v/8_s/8_c) dependence anywhere in their definition.
charge_formula_has_channel_index = False
gauge_acts_uniformly_across_channels = not charge_formula_has_channel_index
print(f"  Charge formula has an explicit per-channel index? {charge_formula_has_channel_index}")
print(
    f"  Gauge group acts uniformly across all 3 channels (necessary condition for weak reading)? {gauge_acts_uniformly_across_channels}"
)
print()
print("  NECESSARY, NOT SUFFICIENT (per mandatory 2nd-pass skeptic review): charge-")
print("  uniformity alone does NOT establish a genuine tensor factorization. Also")
print("  needed, NOT checked here: (i) identical internal block structure of the 3")
print("  32-dim blocks, (ii) no channel-mixing terms in the Dirac operator, (iii)")
print("  triality acting purely as 1(x)t with no admixture on the matter factor.")
print("  See decision.md's three-way verdict -- this is UNVERIFIED, not 'already true'.")
print()

verdict = {
    "kernel_dimension_per_channel": dim_kernel,
    "nontrivial_factorization_of_1dim_kernel_exists": bool(nontrivial_factorizations),
    "STRONG_reading_SU4_Pati_Salam_matter__g97_blocks_it": g97_fully_closed_within_product_framework,
    "WEAK_reading_necessary_condition_charge_uniformity_VERIFIED": gauge_acts_uniformly_across_channels,
    "WEAK_reading_full_sufficiency_UNVERIFIED": True,
}
print("=" * 92)
print("VERDICT")
print("=" * 92)
for k, v in verdict.items():
    print(f"  {k}: {v}")

print()
label = (
    "THREE_WAY_SPLIT__STRONG_SU4_READING_BLOCKED_BY_G97__"
    "WEAK_READING_NECESSARY_CONDITION_VERIFIED_SUFFICIENCY_UNVERIFIED"
)
print(f"  label = '{label}'")
