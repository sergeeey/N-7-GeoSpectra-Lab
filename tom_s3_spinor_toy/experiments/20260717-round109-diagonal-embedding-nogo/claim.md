# Claim — Round109: Does a "Diagonal" `SU(4)` Embedding Combining
S³-Side and S⁶-Side Generators Exist?

**Question type:** Descriptive (a Lie-algebra-theory question with a
clean, general, provable answer — not requiring an exhaustive
case-by-case search).

## Section 1 — Background

Rounds 102 and 108 both closed the SAME-FACTOR question (does `SU(4)`
embed purely within the `S⁶`-side algebra — `so(7)`, `g₂`, or `su(3)`) —
all three give dimension `<15=dim(su(4))` under the physically relevant
readings (round108). Both rounds' skeptic reviews flagged the SAME
remaining gap: a "diagonal" embedding of `su(4)` into
`so(4)⊕so(7)` (or its restrictions), using generators from BOTH the
`S³`-side (`so(4)`, 6-dim) and `S⁶`-side factors TOGETHER, was never
checked and remains the one open route for gate G97.

## Section 2 — Method

This is answerable by a GENERAL, clean Lie-algebra-theoretic argument,
not an exhaustive computational search:

**Key lemma (standard, elementary):** any Lie algebra homomorphism
`φ: g→h` FROM A SIMPLE Lie algebra `g` is either the zero map or
INJECTIVE — because `ker(φ)` is an ideal of `g`, and a simple algebra's
only ideals are `{0}` and `g` itself.

**Application:** `su(4)` is simple (standard fact, `A₃` in the Cartan
classification — verified here, not merely cited, by checking its
Killing form is non-degenerate). A homomorphism
`φ=(φ₁,φ₂): su(4)→so(4)⊕so(7)` has two components,
`φ₁:su(4)→so(4)` and `φ₂:su(4)→so(7)`. Since `dim(so(4))=6<15=dim(su(4))`,
NO injective linear map `su(4)→so(4)` can exist (dimension mismatch alone
rules it out) — combined with the key lemma, this FORCES `φ₁=0`
identically, for ANY homomorphism, with no case-by-case search needed.

**Consequence:** every possible embedding of `su(4)` into
`so(4)⊕so(7)` (or any of its sub-restrictions, `so(4)⊕g₂`,
`so(4)⊕su(3)`) projects to ZERO on the `S³`-side factor automatically —
meaning there is NO genuine "diagonal" embedding possible at all; every
embedding necessarily reduces to a pure same-factor embedding into the
`S⁶`-side alone, already closed by rounds 102/108.

## Section 3 — Pre-registered criteria

- **DIAGONAL EMBEDDING PROVEN IMPOSSIBLE (general argument):** the
  simplicity-lemma argument above is verified to be logically sound and
  its input facts (`su(4)` simple, `dim(so(4))=6<15`) are tool-confirmed
  — this would fully close gate G97's remaining open route.
- **ARGUMENT HAS A GAP:** the simplicity lemma or its application is
  found to have an overlooked case (e.g., a non-Lie-algebra-homomorphism
  type of "embedding" that Codex/round102's language might have actually
  intended, which this clean argument would not cover).
- **BLOCKED:** the input facts (simplicity of `su(4)`, dimension counts)
  fail to verify cleanly.

## Section 4 — Escalation note

Given this would be the FINAL, decisive closure of gate G97's
last-remaining open route if correct, this round's conclusion goes
through mandatory context-asymmetric skeptic review — with particular
scrutiny on whether the general lemma is being applied correctly and
whether "diagonal embedding" as flagged by round102/Codex might mean
something subtly different from a literal Lie-algebra homomorphism
`su(4)→so(4)⊕so(7)` (e.g., an embedding that only needs to preserve
STRUCTURE relevant to the physical construction, not a literal abstract
Lie-algebra map in the naive sense).
