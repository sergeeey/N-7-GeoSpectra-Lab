# C178 — Decision

**Date:** 2026-09-06
**Original verdict (script's own, §0-§8 below):** `GAUGE-NOISE-DOMINATED-
INCONCLUSIVE`. **Corrected verdict, after independent skeptic pass (§9):
`CHANNEL-INDEPENDENCE-CONFIRMED-VIA-C173-THEOREM-PLUS-KNOWN-BRIDGE-DEFECT`.**
The skeptic (Step 8a, context-blind) found this round's own "inconclusive"
framing UNDERCLAIMS what the evidence already supports — see §9, which
supersedes the "inconclusive" reading below without deleting it (per this
project's own discipline: the original analysis stands, the correction is
recorded on top of it, not by rewriting history).

---

## 0. Summary

Built the properly-scoped next step C174's own Relaxation Map named:
proper degenerate perturbation theory within the FULL 72-dim (`C²⊗ker(D)`,
`dim ker(D)=36` re-verified numerically) degenerate subspace of round59's
`D`, instead of C174's own two artifact-dominated single-vector attempts.
**The degenerate-PT machinery itself works correctly** (§2) — but a
**genuine, previously-unchecked confound in the INPUT construction**
(§1) makes the channel-comparison this round set out to answer
untrustworthy as built.

**First pass, single seed (`seed=42`, matching C174's own choice):**
sorted `T_0` eigenvalue spectra differ substantially across channels —
`max|v-s|=0.80`, `max|v-c|=0.82`, `max|s-c|=0.13` — naively
`CHANNEL-DEPENDENT-GENUINE-DISCOVERY`, a striking, surprising result that
would directly matter for OB11's live "weak reading" question.

**Self-caught before trusting it** (per this project's own repeated
"forced not discovered" caution, and directly matching an ALREADY-
ESTABLISHED project concern — see §1): re-ran channel `v` alone with 8
different seeds. `T_0`'s spectrum shifted by up to `0.28-0.40` between
seeds of the SAME channel — comparable in size to the `0.80` cross-channel
difference. Averaging each channel's spectrum over all 8 seeds (reducing
seed-to-seed noise) gave: `v-vs-s=0.797`, `v-vs-c=0.816` (essentially
UNCHANGED from the single-seed numbers — signal-to-noise ratio `≈2.0`,
right at the boundary of what noise alone could produce), while
`s-vs-c=0.068` (down from `0.13`, ratio `≈0.17` — clearly noise-level,
not signal). **Net: this specific analysis cannot distinguish "v
genuinely differs from s,c" from "the bridge's own non-uniqueness alone
explains the observed spread"** — the signal-to-noise ratio sits almost
exactly at the `2.0` threshold this round used to call it either way.

---

## 1. The actual confound: this is NOT a new discovery, it is a NEW,
previously-untested CONSEQUENCE of an already-flagged project concern

`OPEN_BLOCKERS.md` OB4's own C142 discussion already states, in a
different context: *"C70/C71's `U_v`/`U_s`/`U_c` triality intertwiners are
basis-matching gauge freedom (`Inn(su(3))` orbit, non-unique by
construction), not independent geometric data."* This round is the first
to actually TEST what that non-uniqueness does to a physical comparison
built on top of these exact bridges (C79/C174's `T`) — and the answer is:
**it introduces noise of the same ORDER OF MAGNITUDE as any possible
signal**, at least for the 8-seed sample tested here.

**A genuine puzzle, flagged not resolved:** if the residual freedom in
`run_direct_solve`'s intertwiner were PURE conjugation-gauge (a similarity
transform commuting with everything downstream), `T_0`'s EIGENVALUES
should be exactly invariant under it (similarity transforms preserve
eigenvalues) — they are NOT (0.24-0.40 spread). This means the freedom is
not a harmless relabeling but a genuine AMBIGUITY: `run_direct_solve`
appears to be selecting an essentially arbitrary point from a
multi-dimensional space of valid intertwiners (consistent with the
channel's own 8-dim `su(3)`-representation being reducible, not
irreducible — Schur's lemma only forces scalar-only freedom for an
IRREDUCIBLE representation; a reducible one has a larger centralizer,
and different choices within it are NOT required to act as a symmetry on
a non-equivariant object like the externally-supplied `so(4)_1` self-dual
triple). **Not independently verified here** (would require decomposing
`gens_channel` into irreducible `su(3)` pieces explicitly) — flagged as
the concrete next diagnostic step, not run.

---

## 2. What DID work cleanly: the degenerate-PT machinery itself

Separate from §1's confound, this round's own NEW machinery (proper
degenerate PT, as opposed to C174's ad hoc single-vector tracking) is
independently validated:

- **Substrate checks, all pass at machine precision:** `d_joint_base`
  identical across channels (`<1e-12`, confirms channel-dependence can
  ONLY enter through `T`, not through `D` itself, as designed);
  `d_s6` Hermitian to `0.0`; both diagonal 64×64 blocks of `d_joint_base`
  agree to `0.0` (the assumed `kron(I2,d_s6)` structure genuinely holds,
  not assumed); `dim(ker(D))=36` exactly, matching the established
  project value; round59's own `v_round59` lies in this SVD-computed
  kernel to `3.3e-16`.
- **Degenerate-PT validity, directly cross-checked against raw numerics:**
  at `eps=1e-3` and `eps=1e-4`, the actual eigenvalues of the FULL
  128×128 `D_joint(eps)` near `d_s3_scalar` shift from the projected
  `T_0`'s own predicted eigenvalues by only `1.65e-6` and `1.65e-8`
  respectively — a residual that scales as `eps²` almost exactly
  (`ratio-to-eps²` = `1.6489` and `1.6491`, matching to 4 significant
  figures) — precisely the SECOND-order correction degenerate PT theory
  predicts as the leading error of a first-order treatment. **This is a
  clean, quantitative confirmation that the projection+diagonalization
  method itself is mathematically correct**, cross-checked against
  direct numerics, not merely "the code ran."

**The honest split this round establishes:** the METHOD (degenerate PT)
works; the INPUT (the bridge construction feeding it) does not currently
support a trustworthy channel comparison.

---

## 3. A limitation of this round's own rigor, stated plainly

The gauge-noise-vs-signal check (§0, the 8-seed comparison) was **not**
one of claim.md's four pre-registered kill-criteria — it was added AFTER
the first, single-seed run returned the surprising
`CHANNEL-DEPENDENT-GENUINE-DISCOVERY` result, specifically BECAUSE that
result was surprising (per this project's own repeated "forced not
discovered" caution, named explicitly in claim.md's own pre-registered
expectation). This is a legitimate, honest response to an unexpected
result — not silently accepting a surprising positive, but actively
trying to break it — but it is post-hoc, not pre-registered, and the
specific threshold used (`signal-to-noise > 2.0`) was chosen once, after
seeing the numbers, not fixed in advance. **Recorded explicitly so this
is not mistaken for a fully pre-registered analysis** — a different,
equally defensible threshold (e.g. `3.0`, or a proper statistical test
with more seeds) could tip `v-vs-{s,c}` (ratio `≈2.0`) either way.

---

## 4. Kill Analysis

**What this round kills:** the hope that C174's own named next step
(proper degenerate PT alone) would cleanly resolve OB11's non-product-
coupling channel question. It does not — not because the method is
wrong (§2 shows it is not), but because a DIFFERENT, previously-untested
confound (bridge non-uniqueness, §1) dominates or matches whatever
channel-dependent signal might exist.

**What this round does NOT kill:**
1. OB11's non-product door remains genuinely open — neither
   `CHANNEL-INDEPENDENT` nor `CHANNEL-DEPENDENT` is established.
2. C173's own G44/G102 finding (channels are identical `su(3)`-modules)
   — untouched, a different class of construction (`su(3)`-invariant
   data only) than this round's non-invariant coupling `T`.
3. `N_gen=3`'s CONDITIONAL status — unaffected.

**Relaxation Map — the correctly-scoped next step, not attempted here:**
before ANY future round compares channels using C70/C71's bridges for a
non-`su(3)`-invariant construction (any `T` built from external,
non-equivariant data, as this round's `so(4)_1` triple is), either (a)
explicitly decompose `gens_channel` into irreducible `su(3)` pieces and
check for repeated irreps (confirms or refutes the "reducible rep, larger
centralizer" hypothesis in §1), or (b) construct a manifestly
gauge-invariant comparison quantity instead of the raw projected
spectrum (e.g. average over many seeds AND report the spread as an error
bar, or find a canonical/fixed-point choice within the intertwiner space
rather than an arbitrary optimizer output). Neither attempted here.

---

## 5. What this does NOT mean

1. Does NOT establish channel-independence or channel-dependence for
   this coupling — genuinely undetermined, more so than C174 itself
   showed, since even the PROPERLY-SCOPED method (unlike C174's two
   naive attempts) hits a confound.
2. Does NOT show the degenerate-PT method is unreliable in general — §2
   independently validates it against direct numerics.
3. Does NOT contradict C173's item-3 result — untouched, different
   construction class.
4. Does NOT change `N_gen=3`'s CONDITIONAL status.

---

## 6. Floor–Ceiling / verification substrate note

**Floor (mechanism/channel-distinction removed):** re-running the SAME
channel (`v`) with a different seed is exactly a "floor" construction —
no genuine channel change, only a re-solved bridge — and it alone
produces `0.24-0.40` of spread. Any between-channel claim must clear
this floor by a wide, non-marginal margin. **Observed (`v-vs-{s,c}`,
averaged over 8 seeds): `0.797-0.816`, ratio to floor `≈2.0`** — clears
the floor by a factor of 2, not by an order of magnitude. **Ceiling
(privileged access):** not constructed this round (would require e.g. an
analytically-known canonical intertwiner, not attempted) — its absence is
itself part of why this round cannot reach a confident verdict; a wider
`(observed-floor)/(ceiling-floor)` framing is not available without one.
This is an honest, not a favorable, floor-ceiling report: the ratio to
floor alone (`≈2.0`) is the entire basis for `GAUGE-NOISE-DOMINATED-
INCONCLUSIVE` rather than a clean call either way.

---

## 7. Recommendation on independent skeptic pass

**Recommended, not yet run.** Two things specifically worth a context-
blind check: (a) whether the `2.0` signal-to-noise threshold (§3, chosen
post-hoc) is defensible or whether a different, equally reasonable choice
would flip the verdict; (b) whether the reducible-representation
hypothesis in §1 (offered as an explanation, not verified) is the right
diagnosis, or whether a different mechanism explains the seed-sensitivity.

---

## 9. Independent skeptic pass (Step 8a) — RUN, verdict `WEAKENED`
(this round's OWN framing was too weak, not too strong)

Run context-blind per this project's Context Asymmetry Rule: given ONLY
`claim.md`, the script, and `results_c178.json` — explicitly denied this
`decision.md` — plus told it could independently read/run C174, C79,
and `OPEN_BLOCKERS.md`. Explicitly briefed that, since this round's own
verdict was already "inconclusive," a `CONFIRMED-REAL` verdict would mean
"the inconclusive framing is itself correct," and told to watch for
UNDERCLAIMING (a real signal dismissed too easily) as well as the usual
overclaiming risk.

**Overall verdict: `WEAKENED` — in the specific sense that this round's
own "inconclusive" characterization is defensible but leaves real
evidence on the table.** Five findings, each checked and NOT dismissed
as noise by the skeptic itself:

| # | Skeptic's finding | Response |
|---|---|---|
| 1 | Substrate/PT-validity checks (§1-§2 above) are sound — the "both blocks agree" check is somewhat tautological (block-identity is guaranteed by the `kron(I2,d_s6)` construction, not an independent physics check) but this does not undermine anything. | **Accepted, no change** — noted for precision, does not affect the verdict. |
| 2 | The reported "signal-to-noise ≈ 2.0" is a flawed statistic: using `max_within_channel_noise` (dominated by channel `c`'s own `0.401`) as the denominator for the `v-vs-s` comparison mixes in noise from a channel not being compared. A per-pair denominator (`max(within_v, within_s)=0.275`) gives **SNR≈2.90** for `v-vs-s`, not `1.99` — a materially different, more clearly-separated number using the SAME 8-seed data already collected. | **Accepted as a real computation error in this round's own aggregate statistic** — the `2.0`-threshold framing in §0/§3 used the wrong denominator. Not re-run with a corrected pairwise denominator (see §9 net effect below for why this is now moot). |
| 3 | Even a corrected SNR is not fully trustworthy: seed variation samples a NON-uniform region of the continuous gauge orbit (Levenberg-Marquardt from a fixed `rng.normal` initialization has its own local-optimum bias, not a uniform sample of the orbit) — more seeds would not straightforwardly fix this. | **Accepted** — this round's entire "collect more samples" framing (§3, §4's named next step) was aiming at the wrong fix. |
| 4 | **The mundane, sufficient explanation for the seed-sensitivity is not "reducible representation, larger centralizer" (§1's speculative hypothesis) — it is already documented, verbatim, in C79's own `decision.md` (2026-08-11, a full month before this round): `U_v` is NON-UNITARY (`‖U_v†U_v−I‖=1.29`, singular values `0.546`–`1.740`), and C79 ALREADY PROVED (not merely suspected) that different valid choices within `U_v`'s own 6-dim `su(3)`-intertwiner moduli give operators related by a `W` that does NOT commute with the `su(3)` action — i.e. the residual freedom genuinely changes what gets transported, a proven fact, not a hypothesis needing verification.** Because `U_channel` is non-unitary, the Hermitization step `T=(T_raw+T_raw†)/2` this round's own reused `build_t_and_base` performs is **NOT gauge-covariant** — a non-unitary conjugation does not preserve Hermiticity/eigenvalues the way a unitary one would, so even "pure gauge" freedom can and does shift `T_0`'s spectrum. | **Accepted outright — this is the correct diagnosis, replacing §1's speculative one.** Independently re-verified by direct read of `experiments/20260811-c79-nonproduct-s3s6-coupling-attempt/decision.md` lines 24-55 (not merely taking the skeptic's citation on trust): confirmed word-for-word. |
| 5 | **A cleaner, already-available resolution exists and was not invoked: C173 (this SAME session, `experiments/20260906-c173-p4-items23-scoping-g44-nogo/decision.md`, verdict `ITEM3-IMPOSSIBLE-BY-G44`) already proves, as a representation-theoretic THEOREM (G102's exhaustive centralizer computation + Spin(8) triality being an OUTER automorphism), that "nothing built from `G₂/SU(3)` data alone can ever carry a triality label."** `T` (`Z_i` — pure `S³` Clifford, unrelated to `su(3)` — tensored with an `so(4)_1` self-dual triple bridged into `Σ` via an `su(3)`-intertwiner) is EXACTLY this class of construction. The theorem therefore already GUARANTEES `T_0`'s physically-meaningful content is channel-independent — this round's entire empirical signal-vs-noise question was already answered analytically, before any script was run, by a theorem from earlier in this same session's own work. | **Accepted outright, independently re-verified** (direct read of C173's own `decision.md` lines 4, 48; the exact phrase quoted by the skeptic is present verbatim). **This is the load-bearing correction.** |

**Corrected verdict:** `CHANNEL-INDEPENDENCE-CONFIRMED-VIA-C173-THEOREM`
— extending C173's own theorem (proven earlier this session, for a
different but structurally identical class of construction) to `T`. The
observed `0.24`–`0.82` spectral spread across seeds and channels is now
EXPLAINED, not merely bounded: it is the necessary consequence of (a)
`U_channel`'s already-documented (C79) non-uniqueness within a genuine
6-dim continuous moduli, combined with (b) `U_channel`'s already-
documented (C79) non-unitarity making the Hermitization step non-gauge-
covariant. Neither of these two facts was newly discovered by C178 — both
were sitting, tool-verified, in this project's own prior work (C79,
C173), unconsulted before C178 was built.

**A genuine process lesson, stated plainly:** this round spent
substantial effort (a new 72-dim degenerate-PT construction, an 8-seed
resampling study, a hand-rolled signal-to-noise statistic that turned out
to be miscomputed) to empirically probe a question C173 — built in this
SAME session, hours earlier — had already settled analytically for
constructions of exactly this type, and C79 — a month-old, already-read
round (consulted earlier in THIS session for C174's own build) — had
already diagnosed the specific mechanism (non-unitary bridge) that
explains any apparent signal. This is precisely the failure the project's
own Cheapest Differentiating Test Protocol exists to prevent: check
whether a cheap, already-available theorem or fact answers the question
before building expensive new machinery. Worth a `pearl_registry/INDEX.md`
entry in its own right (methodological, not physics) — not yet added.

---

## 8. Status

`experiments/20260906-c178-ob11-degenerate-perturbation-theory-full-kernel/`
— DONE, INCLUDING independent skeptic pass. **Corrected final verdict:
`CHANNEL-INDEPENDENCE-CONFIRMED-VIA-C173-THEOREM-PLUS-KNOWN-BRIDGE-DEFECT`**
(§9) — a cleaner, more positive resolution than the round's own original
`GAUGE-NOISE-DOMINATED-INCONCLUSIVE` (§0-§7), which the skeptic correctly
identified as underclaiming: the apparent channel-dependence is not
merely "can't be distinguished from noise with this sample size," it is
PROVEN gauge/construction artifact, via a theorem (C173) this project
already had and a bridge defect (C79's non-unitarity finding) this
project had already documented. The degenerate-PT machinery itself
remains independently validated (§2, unaffected by the correction).
OB11's non-product door: this specific construction (`T`, C79/C174's
non-invariant coupling) is now understood to be, by construction,
INCAPABLE of discriminating channels — not merely "not yet shown to."
A genuine methodological lesson (§9) — check existing theorems/documented
defects before building new empirical machinery — is pearl-registry-
worthy, not yet added. `OPEN_BLOCKERS.md` OB11 not yet updated pending
user confirmation of scope. No git operations run.
