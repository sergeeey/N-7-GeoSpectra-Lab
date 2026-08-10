# Build provenance — preprint.pdf

Written 2026-08-10 after the C36 rebuild, in response to an external review
noting that the build was reproducible but not *self-certifying*: nothing tied
the artifact to a specific source state. This file closes that gap.

**Not tracked as a claim** — this is release hygiene, not a research result.

## Current build

```
git commit        abc2206c04e53ef6b071ac426ba1c6042a9e71f8
engine            MiKTeX-pdfTeX 4.18 (MiKTeX 24.1)
platform          Windows 11
command           pdflatex -interaction=nonstopmode preprint.tex   (x3)
bibliography      manual thebibliography env - no .bib, no bibtex pass
pages             30
latex errors      0        (grep -cE '^!' preprint.log)
unresolved cites  0        (no '[?]' in pdftotext output)
SHA256(preprint.tex)  9807b60f1cbf36f6bdbca2586dda91f5b497927daed43626db5ae92ecf18c42c
SHA256(preprint.pdf)  e47a4547ec7a907e893e585c48c976c3f1ec3558f22934589af3a351d91934ba
SHA256(prev build)    2bc353ea02b7d2ec914149b9aac0efb4735ffe2662b2440de6d9e9ec36bfce1b
```

## Content verification performed on this build

| check | method | result |
|---|---|---|
| the C36 fix reached the output | `pdftotext` + grep | `JF2 = +1` present, `JF2 = -1` **0 occurrences** |
| citation resolves | grep for `[?]` | 0 |
| scope of change vs previous build | `pdftotext` diff | 35 lines, all from one inserted sentence + its page reflow |
| **visual, changed pages only** | `pdftoppm -r 110` → render pages 7–8 → inspect | **clean**: no overfull spill, no clipping, no overlap, math and refs intact |

The visual step exists because `pdftotext` is blind to layout: it cannot see an
overfull box spilling into the margin, a clipped figure, a broken table, or a
formula that line-broke badly. Text-level checks passing is not the same as the
page being right.

## Reproduce

```bash
git checkout <commit above>
pdflatex -interaction=nonstopmode preprint.tex   # x3
sha256sum preprint.pdf
```

Byte-identical output is **not** expected across runs — pdflatex embeds a
timestamp — so compare the `pdftotext` output and page count rather than the
PDF hash. The hash above identifies *this* artifact, not a reproducibility
target.

## Known artifacts in the repo root

- `preprint.pdf` — current build, **untracked** (this repo does not version
  built artifacts).
- `preprint_PREV_20260718.pdf.bak` — the pre-C36 build, kept as a one-off
  comparison baseline. **Delete once no longer needed**: two PDFs in a root
  directory is exactly how an "which one is authoritative?" problem starts,
  which is the same failure family as the Cl(7,0) label and the J_F² prose.
