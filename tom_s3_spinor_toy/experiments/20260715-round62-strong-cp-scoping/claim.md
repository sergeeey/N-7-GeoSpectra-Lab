# Round62-StrongCPScoping Claim — is a genuine θ_QCD resolution tractable here?

**Date:** 2026-07-15
**FL tier:** [x] Standard (scoping round — cost/tractability assessment,
matching the precedent of `20260713-round51-universality-scoping`, NOT a
commitment to a full derivation)
**Question type:** [x] descriptive (what would resolving this claim require,
and is that achievable with this project's existing machinery)

---

## Prior Result Gate

Checked: `null_results/INDEX.md`, `parked/INDEX.md`, repo-wide grep for
"theta_QCD", "Pontryagin", "strong CP", "eta-invariant", "APS index" — no
prior attempt at this specific question found. The preprint's own current
text (Open Problems, "Strong CP problem") already correctly states the
S³-sector result (η(0,D_{S³})=0, via the S³ Dirac spectrum
{±(n+3/2):n≥0}, reused from gate G34-B3 which computed it for a different
purpose — WZW level k_grav) and correctly scopes what remains: "a global
Pontryagin density analysis on S³×S⁶ including S⁶ sector and
non-perturbative effects."

**Why this round exists:** per Round 51's own lesson (Universality looked
like a "clean, ~1.5-priority, cheap follow-on" until scoping revealed the
true cost was comparable to the entire multi-round L4A/L4B program — a
2.5-3x mis-estimate), Strong CP's headline priority score (0.80, per the
Round-48 shortlist) was assigned WITHOUT a scoping pass. The user's own
prior assessment already flagged "physically heavy" — this round makes that
assessment precise instead of leaving it as a hunch, using the same cheap
method Round 51 used (literature + cost re-estimation, no new physics
computation attempted yet).

---

## Frozen claim

**This round does NOT attempt to compute θ_QCD or resolve the Strong CP
problem.** It answers a narrower, cheap, prerequisite question:

> What specific mathematical objects and results (on $S^6=G_2/\mathrm{SU}(3)$
> and on $S^3\times S^6$ jointly) would a "global Pontryagin density
> analysis" actually require, do any of them already exist inside this
> project's own machinery or in directly-applicable literature, and is the
> resulting effort comparable to (a) a single bounded round, (b) a multi-round
> program like L4A/L4B, or (c) genuinely open research beyond this project's
> scope?

---

## Method

1. Identify precisely what "Pontryagin density analysis" means for a
   gravitational contribution to $\theta_{QCD}$ in a Kaluza-Klein /
   dimensional-reduction context — ground this in real literature (adiabatic
   limit index theorems, APS $\eta$-invariant contributions to effective
   4D $\theta$-terms from compactification), not by assumption. Cite sources.
2. Check what characteristic-class data on $S^6=G_2/\mathrm{SU}(3)$ this
   project has ALREADY computed (Pontryagin classes $p_1,p_2$; instanton
   numbers; any $G_2$-instanton moduli data) — search the repo (already done,
   Prior Result Gate: none found) and identify the smallest new computation
   needed to get $p_1(S^6)$ or the relevant characteristic class.
3. Assess the "non-perturbative effects" clause specifically: does it
   require new input beyond this project's own established
   $\lambda$-non-perturbative-origin work (G83-G86B, already exhausted per
   the existing Open Problems item), or is it a separate, additional
   open-ended requirement?
4. Produce a cost estimate in the same units Round 51 used (rounds of
   comparable scope to L4A/L4B, or a fraction thereof), with an explicit
   confidence level.

## Kill criteria / PASS-equivalent outcomes (pre-registered, all informative)

| Outcome | Meaning |
|---|---|
| **CHEAP** | A bounded, single-round computation (comparable to Round 59/61) would materially advance the claim — proceed immediately in a follow-on round |
| **MODERATE** | Comparable to a 2-4 round program (e.g. L4B's Round 52-56 arc) — worth scoping into sub-rounds before committing, not attempted today |
| **EXPENSIVE (expected)** | Comparable to or exceeding the full L4A/L4B or L3b program — matches the user's own "physically heavy" hunch; demote in the priority list, same treatment Universality got in Round 51 |
| **OUT OF SCOPE** | Requires genuinely new physics/mathematics beyond what any internal round could produce (e.g. a full string-theoretic instanton sum, lattice QCD input, or experimental input) — record as a hard boundary, not a priority question at all |

No outcome here is a "failure" — this exactly matches Round 51's own template.

## What this does NOT mean

1. Does NOT change the preprint's existing Strong CP text — that text is
   already accurate and appropriately hedged; this round only informs
   whether/how to invest further effort.
2. Does NOT claim to resolve, or attempt to resolve, θ_QCD.
3. Does NOT commit to any follow-on round regardless of outcome.
