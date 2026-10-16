# C174 — Claim

**Experiment ID:** `20260906-c174-ob11-nonproduct-d-channel-independence`
**Parent:** `OPEN_BLOCKERS.md` OB11 ("non-product `D`... the only live path,
still untouched beyond C79's single NULL attempt") + C79's own decision.md
§"what survives, as genuinely scoped next steps": (c) "restrict the search
to the physically-relevant `su(3)`-invariant sector specifically... to
avoid the artifact found here by construction" — not yet attempted.
Attempted per user's explicit direction ("го начни с OB11 итд все по
очереди"), applying today's C173 (G44/G102 centralizer no-go) reasoning to
this specific, still-open door.

## Step -5: Zero-Signal Gate

- **Entity:** C79's own non-product coupling construction (`T`, built from
  round67's `Z_i` (S³ Clifford index) and round119's `so(4)_1` self-dual
  triple, transported to round59's `Σ` via C70/C71's channel-specific
  bridge intertwiner `U_channel`), evaluated against round59's OWN
  physically-relevant kernel vector (not the raw 128-dim space, which
  C79 itself showed is dominated by a 36-dim non-physical artifact).
- **Falsifiable predicate:** does `D_joint(eps) = D_joint_base + eps·T`,
  evaluated ON the physically-relevant vector `w⊗v_round59` (`w` = S³'s
  n=0 constant spinor, `v_round59` = round59's own certified kernel vector,
  reused via `importlib` from C172's `reconcile_round59_vector_against_
  full_kernel`, not rebuilt), produce a DIFFERENT numerical result
  (crossing location, or norm-vs-eps curve) depending on which channel
  (`v`, `s`, or `c`) was used to build the bridge intertwiner `U_channel`
  inside `T`? If the three channels give IDENTICAL curves, this directly,
  empirically confirms (not just argues abstractly) that this class of
  non-product coupling cannot distinguish channels — extending C173's
  representation-theoretic no-go (G44: the three channels are IDENTICAL,
  not merely isomorphic, as `su(3)`-modules) to the one door C173 did not
  itself cover (constructions using NON-invariant generators from C78's
  20-dim complement, not just `su(3)`-invariant data).
- **Measurable outcome:** three eps-sweeps (channel v/s/c), each reporting
  the norm of `D_joint(eps)·(w⊗v_round59)` (or the nearest genuine
  eigenvalue restricted to this vector's own span/orbit) as a function of
  `eps`; compared for exact numerical agreement or genuine divergence.

## Step -2/-1 (EstimandOps L0)

**Question type: Descriptive.** Does a specific algebraic construction
(non-product coupling, restricted to the physically relevant sector)
produce channel-dependent or channel-independent output? Not causal, no
estimand canvas beyond the falsifiable predicate above, consistent with
every prior round in this arc (C70-C79, C173).

## Kill-criterion table (frozen before running `c174_channel_independence_check.py`)

| Verdict | Condition |
|---|---|
| `CHANNEL-INDEPENDENT-CONFIRMED-EXTENDS-G44-NOGO` | The three channels' eps-sweeps agree to numerical precision (e.g. `<1e-9` max difference) at every tested `eps` — directly confirms this class of non-product coupling cannot distinguish channels, extending C173's no-go to OB11's remaining door |
| `CHANNEL-DEPENDENT-GENUINE-DISCOVERY` | The three channels' sweeps genuinely differ (well above numerical noise) — an unexpected, high-priority finding requiring immediate independent skeptic scrutiny before any further step, per this project's Trigger 2 (unexpected success) discipline |
| `BLOCKED-BRIDGE-CONSTRUCTION-FAILS` | `U_s` or `U_c`'s own construction (via C71's `bridge_one_channel`) fails its own positive/negative controls when re-run this session — a substrate problem, not evidence either way |
| `ARTIFACT-STILL-PRESENT` | Restricting to `w⊗v_round59` does not actually avoid C79's raw-kernel artifact (e.g. the targeted vector itself turns out to lie inside the 36-dim raw-kernel subspace non-trivially in a way that reintroduces the same degeneracy) — requires diagnosis, not immediate acceptance of either channel-dependent or -independent readings |

## AI-Hypothesis Pre-Gates (Steps -4/-3)

- **Source Trace:** every object reused (`Z_i`, `so(4)_1`, `U_v`/`U_s`/
  `U_c`, round59's `D`, `v_round59`) is imported via `importlib` from
  already-committed project files (C79, C70, C71, C172), not
  re-transcribed or re-derived.
- **Novelty Check:** `grep`-checked this session — no prior round tests
  channel-INDEPENDENCE of a non-product coupling directly; C79 tested
  only channel `v`. C173 proved channel-independence for `su(3)`-invariant
  constructions abstractly; this round tests a NON-invariant-generator
  construction empirically, the specific gap C173 itself left open (see
  C173 decision.md §8 caveat about item 2 not exhausting non-product
  routes).

## What this does NOT mean (pre-registered)

1. Does NOT prove no non-product construction anywhere could ever
   distinguish channels — tests one specific coupling family (C79's own
   postulate: `Z_i` × `so(4)_1` self-dual triple), not all conceivable
   couplings.
2. A `CHANNEL-INDEPENDENT` result does NOT by itself prove the general
   claim "no non-product D can distinguish channels" — it is strong
   evidence for the specific mechanism argued (channels are identical
   `su(3)`-modules, so any construction built from `so(8)`'s
   representation-theoretic data, invariant or not, must act identically),
   consistent with and extending G44/G102/C173, not a fully independent
   new proof covering constructions that could use genuinely non-`so(8)`
   data.
3. Does NOT change `N_gen=3`'s CONDITIONAL status regardless of outcome.
4. Does NOT resolve OB1's `t=0` vs `t=1` selection question either way.
