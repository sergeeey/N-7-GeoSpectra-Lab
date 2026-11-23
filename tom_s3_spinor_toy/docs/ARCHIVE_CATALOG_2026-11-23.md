# Archive catalog: branches and content absent from HEAD (2026-11-23)

Scope: git branches, tags and worktrees of this repository. Names and counts only; no correspondence text, no local paths outside the repository. A private companion (full local-folder inventory, ref manifest, restored private files) lives in the git-ignored `correspondence/branch_recovery_2026-11-23/` and is not part of this file.

Method: read-only. Scripts `branch_scan.py` and `branch_unique_files.py` (kept in the private session archive) walk every branch not merged into HEAD, take its patch-unique commits (`git cherry HEAD <branch>`), list the files those commits touch, and keep the paths that do not exist in HEAD. Evidence: [VERIFIED by command] unless marked.

## Counts

| item | value |
|---|---|
| local branches | 311 |
| remote-tracking branches | 20 |
| tags | 10 |
| extra worktrees (outside the repository folder) | 6 |
| local branches merged into HEAD (counted before the salvage branch existed) | 209 |
| local branches not merged into HEAD | 102 |
| of those 102: with patch-unique commits | 90 |
| of those 102: only added files, no patch-unique commit | 12 |
| distinct paths present on a branch tip, absent from HEAD, reached through a patch-unique commit | 213 (204 under `tom_s3_spinor_toy/`) |

The history was rewritten on 2026-08-10 (tags `backup-before-public-history-rewrite-20260810`, `backup-before-privacy-filter-20260810`). Most branches therefore show hundreds of commits "ahead" of `main`, but only 0 to 5 patch-unique commits. [INFERRED from tag names and `git cherry`]

## Content absent from HEAD, by source

| group | paths | where it lives | status |
|---|---|---|---|
| early scaffold of the p5 to p14 gate chain | 193 | branch `preserve/tom-s3-p5-p14-scaffold` (also on origin) | stored remotely; relevance to the Tom line unknown; not reviewed file by file |
| convention table (answers from the June 2026 Q&A round) | 1 | 85 local branches | contains verbatim quotes of a named person; kept private, restored only in the git-ignored folder |
| solution packet for the j = 1/2 group harmonics and a draft reply (two experiment folders) | 8 | 13 local branches (e.g. `b2-independent-reimplementation`) | packet = math; reply = correspondence; both restored only in the git-ignored folder |
| independent second implementation (parked mid-build) | 1 | `b2-independent-reimplementation` | restored privately; run did not finish in 280 s (see below) |
| Phase 4 recoverability benchmark | 6 | branch `phase4-recoverability-benchmark` and a worktree | older GeoSpectra work, not the Tom line |
| earlier letter drafts | 4 | one local backup branch, not on any remote ref | private; names withheld |

The other roughly 90 unmerged branches carry patch-unique commits whose files all exist in HEAD, so they add no path that HEAD lacks. [VERIFIED for the scan; not a statement that their content is identical]

## Re-run of the packet (2026-11-23)

- The packet script was run from a scratch copy together with its round-76 dependency: exit 0, 53 s. The fresh results json is identical to the stored one; verdict `ALL_CHECKS_PASS`. [VERIFIED by command]
- The independent second implementation did not finish in 280 s; a background run was started with a 25-minute limit. Until it finishes it is `[UNKNOWN]`, not verified.
- The packet computes the same j = 1/2 Peter-Weyl block as the ledger row `TOM_CERT_01_SPAN_GAB_SU2LR_HALFHALF_EXACT`, in a different chart. The weight labelling of the two is not reconciled.

## Worktrees

Six worktrees outside the repository folder, all Phase 4 audits of older GeoSpectra work. Four have one uncommitted file each and may belong to other sessions: not touched.

## Cleanup performed (2026-11-23, after explicit list approval)

- Deleted 207 local branches that were fully merged into HEAD (`git branch -d`, 0 refusals): 36 research, 28 feature, 13 docs, 11 null, 9 chore, 6 fix, 5 feat, 6 others. Before deletion: none checked out in a worktree, none pointed to by a tag, every tip an ancestor of HEAD (re-checked for all 207 SHAs: 0 unreachable afterwards). Local branches: 312 before, 105 after.
- Recovery: every name and SHA is in the private manifest (`refs_manifest_20261123.tsv`); `git branch <name> <sha>` recreates any of them. The commits themselves were never removed.
- Not touched: the 102 unmerged branches, `main`, `backup*`, `preserve*`, all tags, the six worktrees, remote branches.

## Limits

- Line-level content of the 90 branches with unique commits was not compared; only the paths absent from HEAD were collected.
- The 193 files of the `preserve` scaffold were counted, not read.
- `git fsck` and `git gc` were not run, so dangling objects are not accounted for.
