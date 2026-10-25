# Decision — OB11 discriminator (2026-10-25)

**Verdict (structural, internal index only):** the triality channels form one irreducible su(3) triplet block (3 + 3bar + 1 + 1 on C^8). No G-invariant rank-1 projector onto a single channel exists. Under the admissible group, the three channels are not independent sectors.

**Scope:** this does not count physical generations. Zero modes of the differential operator are not yet decomposed under G. The 36-dimensional kernel of the algebraic 64x64 matrix D is not a zero-mode count.

**Correction recorded:** an earlier mapping of this discriminator to OB13 was wrong. OB13 is the t-selector. The triality-independence question is OB11.

**Next:** decompose the round59 zero modes under G; then decide whether OB11's WEAK reading is closed (factor 3 removable) or open (channels separated only if the physical action breaks su(3)).

**Not done:** no edit to OPEN_BLOCKERS.md, no commit.

## Zero-mode decomposition (run 2026-10-25, zero_mode_decomposition_ob11.py)

Fibre C^8 (x) C^8 under the Leibniz lift of su(3), Casimir blocks (value: dim, dim ker D|block):
- 0: dim 6, ker 2 (singlets)
- 4/3: dim 30, ker 6 (fundamental-type, 3/3bar)
- 3: dim 16, ker 16 (adjoint-type; D vanishes on it)
- 10/3: dim 12, ker 12 (sextet-type; D vanishes on it)
Total dim ker D on the fibre: 36. Verdict printed: ZERO_MODES_IN_NON_SINGLET_BLOCK.

**Reading:** the algebraic matrix D is highly degenerate and its kernel occupies every isotypic block. It does not identify the physical zero modes, so the zero-mode discriminator is INCONCLUSIVE with this object.

**Discrepancy to resolve before any generation count:** round59 quotes full-fibre invariant dims (2,1) for its SU(3)-invariant domain, whereas the singlet block here is 6-dimensional with ker 2. The group action on the fibre used in round59 (spin lift on the 64-dim fibre) must be reconciled with the Leibniz lift used here. Until then neither "the triplet carries the zero modes" nor "the singlets carry them" is established.

**Next:** reproduce round59's (2,1) invariant dims with its own fibre action; then repeat Z3 on the differential-operator zero modes (round59 routes A/B) with that same action.
