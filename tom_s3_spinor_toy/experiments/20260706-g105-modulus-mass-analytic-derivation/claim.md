# G105 Claim — Analytic derivation of the modulus-mass power law (upgrades G103 from FITTED to DERIVED)

**Question type:** descriptive (closed-form mathematical property of an existing, already-defined
potential; no new physical input, no claim about lambda's value)

**Background:** G103 (2026-07-05) found, by curve-fitting a 9-point numerical sweep, that the
modulus mass scales as m_mod ~ lambda^0.4928 over lambda in [0.15, 0.60]. This was reported
correctly as a FITTED result (curve-fit exponent), not a DERIVED one. Separately, G66
(2026-06-21) proved kappa^2 = (N+1)/N analytically, by a different route, for the (3,6) case.

**Claim:** both of these are the SAME leading-order small-lambda expansion of ONE potential,
not two independent facts. Concretely, writing V(rho) in dimensionless form
f(x,mu) = x^-n*(1 - exp(mu*(1-x^-2))) (x=rho/rho_star, mu=lambda/rho_star^2, n=2N). Note
f(x,0)=0 identically for every x — mu=0 is where the whole potential vanishes (the G60
Minkowski-uplift construction), not a stationary point of a nonzero function. "x0" below is
lim_{mu->0} x_min(mu), taken from the O(mu) coefficient of f, not from f at mu=0 itself.

1. x0 = sqrt((n+2)/n) is EXACTLY G66's kappa^2=(N+1)/N, for every N tested (2 through 10) —
   this is why kappa/rho_min is lambda-blind at leading order. This is an ALGEBRAIC genericity
   claim only (true for any n in this functional FORM) — it does NOT independently prove that
   an actual S^a x S^N compactification reduces to this potential SHAPE for N outside the two
   values (2,6) and (3,6) this project has actually built and tested (G103, G104); that physical
   mapping is inherited from G104's own (a,N)-generalized construction, not re-derived here.
2. f''(x_min(mu), mu) = A*mu + B*mu^2 + O(mu^3), i.e. mass^2 ~ lambda^1 at leading order
   (mass ~ sqrt(lambda), exponent EXACTLY 0.5), with a computable O(mu^2) correction.

**Falsifiable predicate:**

| Check | Predicted | Kill if |
|---|---|---|
| D1: leading-order x0^2 = (N+1)/N for N=2..10 | exact match, all N | any N mismatches beyond float precision |
| D2: GLOBAL log-log fit exponent (this gate, EXACT non-perturbative f'', same 9 lambda points as G103) vs G103's own independently-fitted 0.4928 | within 0.01 | \|this-gate-fit - 0.4928\| > 0.01 |
| D3: this gate's independent (sympy+scipy) rho_min reproduces EVERY point in G103's own 9-point sweep | diff < 1e-5 for all 9 | any point differs by more |
| D4: predicted local exponent -> 0.5 monotonically as lambda -> 0 | monotonic approach | non-monotonic or does not approach 0.5 |
| D5: perturbative (A,B closed-form) local exponent vs EXACT local exponent at the TOP of G103's fit range (lambda=0.60, mu~0.505 — not small) | within 0.02 | perturbative and exact diverge, meaning the O(mu^2) truncation is untrustworthy across G103's actual range |

**Revision history:** original D2 (2026-07-06, first pass) compared the local closed-form
exponent AT lambda=1/3 to G103's range-averaged fit — a mismatched pair of observables that
happened to numerically agree. Caught by context-asymmetric skeptic review (FL Step 8a) the
same day; D2 fixed to compare fit-to-fit (both range-averaged, same methodology as G103); D5
added to directly bound the perturbative formula's error at the range's edge, which nothing
previously checked directly. See decision.md for the full response matrix.

**What this does NOT mean:**
1. Does NOT derive lambda's value — `lambda = FREE_COUPLING_PARAMETER` is untouched. This is a
   statement about the FUNCTIONAL FORM of mass-vs-lambda, given lambda as an input, not about
   what fixes lambda itself.
2. Does NOT explain WHY the potential has the exp(-lambda/rho^2) form physically — G103's NULL
   on UV-mechanisms stands; this gate assumes the form as given (as G60/G61/G103/G104 already do)
   and derives consequences of that assumed form.
3. Does NOT make the exponent-0.5 result a distinguishing fingerprint of THIS model's specific UV
   origin — D1 shows it is a GENERIC ALGEBRAIC consequence of any potential of this schematic
   shape (Freund-Rubin-like flux term minus one NP exponential correction), for any N. A different
   future model with the same SHAPE of potential would show the same exponent regardless of its
   own physical origin — this actually WEAKENS the exponent's diagnostic power as a UV-mechanism
   test (see decision.md Skeptic section).
4. Does NOT prove the potential SHAPE itself is physically generic across all N — only that IF a
   compactification reduces to this shape (as G104 explicitly builds for (a,N)=(2,6) and (3,6)),
   THEN the mass law follows. Whether every S^a x S^N pair actually reduces to this shape is a
   separate, unaddressed physics question (skeptic review, Probe 3).

**Kill criterion:** if D1 or D3 fails, the sympy model does not actually match the project's real
potential (implementation error) — fix before reading D2/D4. If D2 fails, the small-lambda
expansion is not the source of G103's fitted number (a genuine surprise, would need explaining).
If D4 fails, there is no clean asymptotic limit at all (the "0.4928 ~ 1/2" match would then be
a coincidence at the ONE tested (3,6) point, not a structural fact).
