# Docs Reorganization Plan — Compute vs Science Separation

**Date:** 2026-06-01  
**Purpose:** Separate compute/infrastructure docs from scientific claims docs  
**Status:** PLAN (requires user review + approval before execution)

---

## Problem

Current docs/ and reports/ structure mixes:
- **Compute infrastructure** (hardware, scripts, OOM incidents, server setup)
- **Scientific claims** (hypotheses, experiments, results, caveats)
- **Methodology** (falsification ladder, controls, audit procedures)

This creates:
- ❌ Confusion: Is this doc about hardware or about physics?
- ❌ Mixed audience: DevOps engineer vs physicist need different docs
- ❌ Hard to find: "Where's the server setup guide?" vs "Where's the Gate 4B results?"

---

## Solution: Three-Tier Structure

```
docs/
├── compute/          ← Infrastructure, hardware, DevOps (NEW)
├── science/          ← Research, experiments, results (NEW)
└── methodology/      ← Falsification ladder, protocols (NEW)
```

---

## Proposed Reorganization

### Tier 1: `docs/compute/` — Infrastructure & DevOps

**Audience:** DevOps engineer, server admin, CI/CD maintainer  
**Purpose:** Set up server, run experiments, debug OOM, monitor compute

| Current Location | New Location | Description |
|------------------|--------------|-------------|
| `SERVER_INFO.md` | `docs/compute/server_info.md` | Hetzner CX52 access, specs |
| `hardware_requirements_calculation.md` | `docs/compute/hardware_requirements.md` | RAM calculations, server options |
| `PRE_RERUN_CHECKLIST.md` | `docs/compute/pre_rerun_checklist.md` | Setup validation |
| `PROJECT_STATUS_CHECKLIST.md` | `docs/compute/project_status_checklist.md` | Status tracking |
| `reports/INCIDENT_GATE4B_v0.1.24_OOM_2026-05-25.md` | `docs/compute/incidents/gate4b_v0.1.24_oom.md` | OOM postmortem |
| `reports/MEMORY_SAFE_RERUN_PLAN_v0.1.24.md` | `docs/compute/memory_safe_rerun_plan.md` | Batched execution strategy |
| `scripts/download_v0.1.24_results.sh` | `docs/compute/scripts/download_results.sh` | Download automation |
| `scripts/run_negative_controls_batches_3_6.sh` | `docs/compute/scripts/run_batched.sh` | Batched runner |
| `scripts/server_status_check.sh` | `docs/compute/scripts/server_status.sh` | Monitoring |
| (NEW) `scripts/server_bootstrap.sh` | `docs/compute/scripts/bootstrap.sh` | Server setup |
| (NEW) `scripts/server_cleanup.sh` | `docs/compute/scripts/cleanup.sh` | Post-run cleanup |
| (NEW) `scripts/server_smoke_test.sh` | `docs/compute/scripts/smoke_test.sh` | Smoke test |

**Quick-start docs to add:**
- `docs/compute/README.md` — "How to run GeoSpectra on a fresh server in 10 minutes"
- `docs/compute/troubleshooting.md` — Common issues (OOM, swap, Python deps, tmux)
- `docs/compute/monitoring.md` — htop, journalctl, RSS tracking

---

### Tier 2: `docs/science/` — Research & Experiments

**Audience:** Physicist, researcher, peer reviewer  
**Purpose:** Understand what was tested, what results mean, scientific claims

| Current Location | New Location | Description |
|------------------|--------------|-------------|
| `docs/OUTCOMES.md` | `docs/science/outcomes.md` | All experiment results |
| `docs/CLAIMS_AND_CAVEATS.md` | `docs/science/claims_and_caveats.md` | Allowed vs forbidden claims |
| `docs/RESEARCH_CONTEXT.md` | `docs/science/research_context.md` | Tom Lawrence attribution |
| `reports/GATE_4B_v0.1.24_COMPARISON_FINAL.md` | `docs/science/experiments/gate4b_v0.1.24_comparison.md` | Gate 4B corrected rerun |
| `reports/NEGATIVE_CONTROLS_FULL_PATTERN_AUDIT_v0.1.24.md` | `docs/science/experiments/negative_controls_v0.1.22_audit.md` | Negative Controls audit |
| `reports/LAWRENCE_CLAIM_TO_TEST_MATRIX_v0.1.md` | `docs/science/claim_to_test_matrix.md` | Tom Lawrence mapping |
| `reports/S3_S1_NEGATIVE_CONTROLS_PREREGISTRATION_v0.1.22.md` | `docs/science/experiments/negative_controls_v0.1.22_preregistration.md` | Pre-registration |
| `reports/S3_S1_GATE4B_FSS_RESULTS_v0.1.21.md` | `docs/science/experiments/gate4b_v0.1.21_results.md` | Original Gate 4B |
| `reports/NULL_RESULTS.md` | `docs/science/null_results.md` | Falsified experiments |
| All `reports/MILESTONE_*.md` | `docs/science/milestones/*.md` | Milestones |
| All `reports/RELEASE_NOTES_*.md` | `docs/science/releases/*.md` | Version history |

**Quick-start docs to add:**
- `docs/science/README.md` — "What GeoSpectra validates and what it does NOT"
- `docs/science/faq.md` — "Why harness nonspecific? What's next? Can I cite this?"

---

### Tier 3: `docs/methodology/` — Protocols & Standards

**Audience:** Methodologist, auditor, skeptic reviewer  
**Purpose:** Understand falsification ladder, controls, pre-registration, integrity checks

| Current Location | New Location | Description |
|------------------|--------------|-------------|
| `docs/ROADMAP.md` | `docs/methodology/roadmap.md` | Phase-by-phase plan |
| `experiments/_template/experiment.md` | `docs/methodology/experiment_template.md` | Standard experiment structure |
| (Implied from CLAUDE.md) Falsification Ladder | `docs/methodology/falsification_ladder.md` | FL tiers, decision rules |
| (Implied from CLAUDE.md) Evidence Policy | `docs/methodology/evidence_policy.md` | [VERIFIED] / [INFERRED] markers |
| (Implied from CLAUDE.md) Negative Controls | `docs/methodology/negative_controls_protocol.md` | Control construction rules |
| (NEW) Pre-registration template | `docs/methodology/preregistration_template.md` | Hypothesis + decision rule template |

**Quick-start docs to add:**
- `docs/methodology/README.md` — "How GeoSpectra prevents p-hacking and HARKing"
- `docs/methodology/peer_review_guide.md` — "What to check when auditing GeoSpectra claims"

---

## Migration Strategy

### Phase 1: Create new structure (no file moves yet)
```bash
mkdir -p docs/compute/{scripts,incidents}
mkdir -p docs/science/{experiments,milestones,releases}
mkdir -p docs/methodology
```

### Phase 2: Copy (not move) key docs to new locations
- Keep originals in place (backward compatibility)
- Add `MOVED_TO: docs/compute/...` header to old files
- Update cross-references in new files

### Phase 3: Update all references
- Search for `[link](../reports/GATE_4B_...)` → update to new paths
- Update ROADMAP.md to reference new structure
- Update README.md with new navigation

### Phase 4: Deprecate old locations (after 2-4 weeks)
- Add deprecation notice to old files
- Move old files to `_deprecated/` folder
- Keep for 1-2 months, then delete

---

## Quick Reference Table (Before → After)

| Question | Before | After |
|----------|--------|-------|
| **How do I set up a server?** | Search through SERVER_INFO.md, hardware_requirements_calculation.md, multiple scripts | `docs/compute/README.md` |
| **What did Gate 4B show?** | Search through reports/GATE_4B_*.md, OUTCOMES.md | `docs/science/experiments/gate4b_v0.1.24_comparison.md` |
| **What can I claim?** | docs/CLAIMS_AND_CAVEATS.md | `docs/science/claims_and_caveats.md` (same, just moved) |
| **How does FL work?** | Implied in CLAUDE.md, not documented | `docs/methodology/falsification_ladder.md` |
| **What's the OOM fix?** | reports/INCIDENT_*, MEMORY_SAFE_RERUN_PLAN | `docs/compute/incidents/gate4b_v0.1.24_oom.md` + `memory_safe_rerun_plan.md` |

---

## Audience-Specific Entry Points

### For DevOps Engineer:
**Start here:** `docs/compute/README.md`  
**Common tasks:**
- Set up server → `docs/compute/scripts/bootstrap.sh`
- Debug OOM → `docs/compute/incidents/gate4b_v0.1.24_oom.md`
- Monitor run → `docs/compute/monitoring.md`
- Download results → `docs/compute/scripts/download_results.sh`

### For Physicist / Researcher:
**Start here:** `docs/science/README.md`  
**Common tasks:**
- Understand results → `docs/science/experiments/gate4b_v0.1.24_comparison.md`
- Check claims → `docs/science/claims_and_caveats.md`
- Review null results → `docs/science/null_results.md`
- Plan next experiment → `docs/methodology/experiment_template.md`

### For Peer Reviewer / Skeptic:
**Start here:** `docs/methodology/README.md`  
**Common tasks:**
- Understand FL → `docs/methodology/falsification_ladder.md`
- Check pre-registration → `docs/science/experiments/negative_controls_v0.1.22_preregistration.md`
- Audit claims → `docs/methodology/peer_review_guide.md`
- Review controls → `docs/methodology/negative_controls_protocol.md`

---

## Benefits

### For Users:
- ✅ Clear entry point by role (DevOps / Researcher / Reviewer)
- ✅ No confusion: "Is this about hardware or physics?"
- ✅ Faster navigation (3 dirs instead of 100+ mixed files)

### For Maintainers:
- ✅ Easier to find stale docs (compute/ changes often, methodology/ rarely)
- ✅ Cleaner git history (compute commits ≠ science commits)
- ✅ Better CI checks (can lint compute scripts separately from science docs)

### For External Collaborators:
- ✅ "I just want to reproduce the run" → `docs/compute/`
- ✅ "I want to review the science" → `docs/science/`
- ✅ "I want to understand the methodology" → `docs/methodology/`

---

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| **Broken links** after moving files | Phase 2: Copy first, move later. Add MOVED_TO headers. |
| **Users can't find old paths** | Keep originals for 2-4 weeks with deprecation notice |
| **Git history fragmented** | Use `git log --follow` to track renames |
| **Too much churn** in one PR | Migrate in 3 separate PRs (compute, science, methodology) |

---

## Implementation Checklist

- [ ] Phase 1: Create directory structure
- [ ] Phase 2: Copy key docs to new locations (keep originals)
- [ ] Phase 3: Update cross-references in new files
- [ ] Phase 4: Update README.md with new navigation
- [ ] Phase 5: Add deprecation notices to old files
- [ ] Phase 6 (2-4 weeks later): Move originals to `_deprecated/`
- [ ] Phase 7 (1-2 months later): Delete deprecated files

---

## Next Steps

1. **User review** — approve directory structure
2. **User classification** — confirm which docs are compute vs science (ambiguous cases)
3. **Phase 1 execution** — create dirs, no file moves yet
4. **Phase 2 PR** — copy docs to new locations
5. **User testing** — verify navigation works for all roles

---

**Status:** PLAN (NOT executed yet)  
**Requires:** User approval before any file moves  
**Estimated effort:** 2-3 hours (Phase 1-3), then 1 week deprecation period

---

**Last updated:** 2026-06-01  
**Next review:** After user approval
