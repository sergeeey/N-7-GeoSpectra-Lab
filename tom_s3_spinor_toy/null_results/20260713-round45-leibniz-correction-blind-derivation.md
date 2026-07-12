# NULL: the "blind Leibniz-correction" test cannot discriminate fork (i)
[frame/Leibniz correction] from fork (ii) [F_{S^-} incomplete] — the
match is a structural tautology, not evidence

**Date:** 2026-07-13
**Source experiment:** experiments/20260708-dolan-casimir-g2su3/
(round45_claim.md carries full Skeptic Verdict; decision.md carries the
narrative Kill Analysis)
**Verdict:** REJECT the claim that this specific construction adjudicates
Round 24's original (i)-vs-(ii) fork for the trace-free residual
`K := [[0,4/3],[4,0]]` of `Delta_2x2`

## What was tested

Round 24 (2026-07-10-ish) found `Delta_2x2 = [[5/2,4/3],[4,5/2]]`, with
diagonal exactly `5/2` (matching `Scal/4`) and an unexplained trace-free
residual `K`, framed as an open fork: (i) a frame/Leibniz correction the
naive 3-term Weitzenböck formula doesn't capture, or (ii) evidence
`F_{S^-}` itself is incomplete. This round attempted a "blind" test: group
`Delta`'s already-known 5-piece decomposition (Round 41) into `UNTWISTED`
(the untwisted single-copy Lichnerowicz remainder, `kron(Dslash_mat²-Σ
M_p², Id8)`) vs `TWISTING_SPECIFIC` (T12+T21+TORSION_E+cross_casimir, the
pieces that exist only because D64 has a genuine two-factor Leibniz
connection term), with the grouping criterion fixed from D64's own
structure BEFORE checking against `K`.

`TWISTING_SPECIFIC`'s own off-diagonal, compressed on `span(w_a,w_b)`,
matched `K` exactly.

## Why this is a NULL, not a PASS

Two independent skeptics + a synthesis agent, working independently,
proved via arbitrary symbolic matrix substitution that `UNTWISTED`'s form
(`kron(X,Id8)`) has EXACTLY ZERO off-diagonal on `span(w_a,w_b)` for ANY
matrix `X` whatsoever — `w_a` and `w_b` have disjoint index support in
BOTH tensor factors (left: {0} vs {4,5,6}; right: {7} vs {1,2,3}), not
just one. Given the pre-existing identity `Delta = UNTWISTED +
TWISTING_SPECIFIC` (Round 41, predating this round), it follows FOR FREE
that `off-diag(TWISTING_SPECIFIC) = off-diag(Delta) = K`, regardless of
whether `TORSION_E`/`cross_casimir` are correct physics or whether
`F_{S^-}` is missing something — a genuinely missing `F_{S^-}` term would,
by its own physical nature, be a two-factor-mixing operator too, and would
land in `TWISTING_SPECIFIC` just as cleanly as the "correct" terms. The
synthesis agent additionally confirmed, via git timestamp, that Round 41's
individual piece values (commit `3bf6fc2`, 2026-07-12 20:22:21) predate
this round's script — the "blind" grouping had these exact numbers already
visible on disk.

## What survives (Kill Analysis)

**Killed:** the specific evidentiary claim that this construction
discriminates fork (i) from fork (ii) for the residual `K`. Any single-
tensor-factor-embedded split (`kron(X,Id8)` or `kron(Id8,X)`, for any `X`)
of `Delta`'s known decomposition is GUARANTEED to reproduce this exact
K-match on `span(w_a,w_b)` — the test has zero discriminating power, by
construction, not by numerical accident.

**NOT killed:**
- Round 41's own five-piece decomposition of `Delta` — independently
  re-verified here via a different grouping route, still exact.
- `D64`'s match to the textbook Leibniz-rule twisted-Dirac-operator
  template (`D64 = Σ_i (e_i⊗Id)·N_i`) — confirmed, though this is a
  content-free Kronecker mixed-product identity true for any matrices,
  not itself evidence about the specific physics.
- Round 24's original fork (i) vs (ii) question — remains completely open,
  exactly as it was before this round.

## Do NOT re-attempt without

A genuinely different test design, where the candidate "untwisted"
content is NOT structurally guaranteed to vanish off-diagonal on the
chosen subspace merely by virtue of being embedded on a single tensor
factor. Concretely: pick a 2-dim (or larger) SU(3)-invariant subspace
where `w_a`/`w_b`-analogues are NOT separable by tensor-factor index
alone (i.e. where at least one candidate basis vector has support
spanning BOTH factors in a way that a single-factor operator CAN connect
to another basis vector) — only then would a kron(X,Id8)-vs-remainder
split carry genuine discriminating power. Simply re-trying the SAME
`span(w_a,w_b)` subspace with a DIFFERENT grouping of the 5 known pieces
would not fix this — the disjoint-support tautology applies to ANY
single-factor-embedded candidate on THIS subspace, not just the specific
one tried here.
