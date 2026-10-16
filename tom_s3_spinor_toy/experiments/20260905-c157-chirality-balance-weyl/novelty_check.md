# C157 — Novelty check (FL Step -3), run before the verdict

## Finding: the balance theorem is a direct special case of a 1998 formula

Pengpan, *Kostant's cubic Dirac operator of Lie superalgebras*
(arXiv:hep-th/9910119), reviewing Gross–Kostant–Ramond–Sternberg (GKRS 1998),
Eq. (2):

    V_lambda (x) S+ - V_lambda (x) S- = sum_{c in C} sgn(c) U_{c . lambda}

for an equal-rank embedding `r subset g`, `C = W(g)/W(r)`. **Setting `lambda = 0`
(trivial representation) and `r = t` (maximal torus, so `W(r) = 1`, `rho_r = 0`,
`C = W(g)`)** collapses this to

    ch(S+) - ch(S-) = sum_{w in W} sgn(w) e^{w(rho)}

which is **exactly** the Weyl denominator identity used in this round's proof,
in the **exact same construction** (`G/T`, `Sigma = S+ (+) S-`, Kostant's cubic
Dirac operator) that this project's own C144 already identified as the origin
of the whole `D_Sigma` construction used continuously since C139.

**Conclusion: NOT NEW.** The chirality-balance theorem is the `lambda=0` special
case of a formula already standard by 1998, itself reviewing even earlier
(Kostant's own original cubic Dirac operator papers, ~1999 and before in
preprint form). This matches the pre-registration's own stated expectation,
written down before any proof or census was run: *"the proof is a corollary of
the Weyl denominator formula; the prior expectation is that it is classical and
known to specialists."*

## What was searched and what was found

* Weyl denominator formula + zero-weight multiplicity + spin representation +
  Kostant — found the GKRS formula (above) and Kostant's cubic Dirac operator
  literature (Huang–Pandžić, *Dirac Operators in Representation Theory*;
  Landweber, *Multiplets of representations and Kostant's Dirac operator for
  equal rank loop groups*).
* Dirac cohomology + zero weight + half-spin + balanced even/odd — same
  literature cluster; Kostant's Dirac cohomology is computed as exactly the
  kernel of this operator, of which the chirality balance at weight 0 is an
  elementary consequence.
* No search surfaced the SPECIFIC phrase "chirality balance of invariant
  spinors on flag manifolds" as a named result — but given the derivation is
  three lines from a formula already in a 1998 paper (itself surveying older
  work), **absence of an exact phrase match is not evidence of novelty**; it is
  evidence the fact is considered too elementary to state as its own theorem.

## Consequence for this round's verdict

Per the user's mandate, a candidate discovery needs **all five**: theorem,
out-of-sample test, null model, literature novelty audit, independent skeptic
pass. **This gate fails explicitly.** The theorem is true, independently
re-derived, and computationally verified on 18 root systems — but it is not
new. This is reported as the correctly-run experiment's actual outcome, exactly
as the pre-registration predicted, not as a partial success to be talked up.
