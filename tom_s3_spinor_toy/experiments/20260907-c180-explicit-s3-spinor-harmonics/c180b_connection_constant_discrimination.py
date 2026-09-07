"""C180-B -- what does the connection-constant solve actually discriminate?

C180 reported `constant_was_solved_not_assumed: True` and the draft reply to Tom
turned that into "it drops out of the eigenvalue data rather than having to be
put in by hand". A context-blind adversarial read of that letter flagged the
wording, noting that the target magnitude `n + 3/2` is supplied from outside.

That flag is correct, and the situation is stronger than the flag stated. The
solve works by intersecting, over the (eigenvalue, multiplicity) pairs, the
candidate sets

    c in { val - (n + 3/2),  val + (n + 3/2) },   n read off the multiplicity.

For the negative branch the observed eigenvalue is exactly `-n`, so
`val + (n + 3/2) = 3/2` IDENTICALLY, for every n. For the positive branch the
eigenvalue is exactly `n + 3`, so `val - (n + 3/2) = 3/2` IDENTICALLY. The value
3/2 is therefore present in every candidate set as an algebraic identity, not as
a fact extracted from the data.

This script establishes what the solve CAN and CANNOT detect, by replaying its
logic on deliberately corrupted spectra. Run it before quoting the constant as
"solved" anywhere.
"""

import json


def n_from_multiplicity(m: int) -> int | None:
    """Invert m = (n+1)(n+2); None if m is not of that form."""
    n = 0
    while (n + 1) * (n + 2) < m:
        n += 1
    return n if (n + 1) * (n + 2) == m else None


def solve(pairs):
    """Exactly C180's connection_constant_check logic, on arbitrary input."""
    sets = []
    for val, mult in pairs:
        n = n_from_multiplicity(mult)
        if n is None:
            sets.append(set())
            continue
        mag = n + 1.5
        sets.append({round(val - mag, 9), round(val + mag, 9)})
    inter = set.intersection(*sets) if sets else set()
    return sorted(inter), len(inter) == 1


REAL = [(0, 2), (-1, 6), (3, 2), (-2, 12), (4, 6), (-3, 20), (5, 12)]

CASES = [
    ("real D0 spectrum", REAL),
    ("every eigenvalue shifted by +1", [(v + 1, m) for v, m in REAL]),
    ("every eigenvalue shifted by +0.37", [(v + 0.37, m) for v, m in REAL]),
    (
        "ONE eigenvalue moved by +0.6",
        [(v + (0.6 if i == 3 else 0), m) for i, (v, m) in enumerate(REAL)],
    ),
    ("spectrum rescaled by 1.2 (spacing broken)", [(v * 1.2, m) for v, m in REAL]),
    ("spectrum reflected", [(-v, m) for v, m in REAL]),
    # 6 -> 7 is NOT a valid (n+1)(n+2) product, so n_from_multiplicity returns
    # None and the intersection is empty via the FALLBACK path -- which would
    # report "detected" even if the mag arithmetic were broken. Flagged in an
    # independent code review. 6 -> 12 is a VALID product (n=2, hence a wrong
    # but well-formed mag of 3.5), so it exercises the arithmetic the test is
    # nominally about. Both are kept; only the second is load-bearing.
    (
        "one multiplicity broken (6 -> 7, INVALID product: fallback path)",
        [(0, 2), (-1, 7), (3, 2), (-2, 12), (4, 6), (-3, 20), (5, 12)],
    ),
    (
        "one multiplicity broken (6 -> 12, VALID product: arithmetic path)",
        [(0, 2), (-1, 12), (3, 2), (-2, 12), (4, 6), (-3, 20), (5, 12)],
    ),
]

rows = []
for label, pairs in CASES:
    inter, unique = solve(pairs)
    rows.append({"case": label, "intersection": inter, "unique": unique})

by = {r["case"]: r for r in rows}
res = {
    "cases": rows,
    # A uniform additive shift is the ONE corruption that still yields a unique
    # answer -- and it is exactly the quantity the solve purports to measure.
    "uniform_shift_still_unique": bool(
        by["every eigenvalue shifted by +1"]["unique"]
        and by["every eigenvalue shifted by +0.37"]["unique"]
    ),
    "broken_level_detected": not by["ONE eigenvalue moved by +0.6"]["unique"],
    "broken_spacing_detected": not by["spectrum rescaled by 1.2 (spacing broken)"]["unique"],
    # The load-bearing one: a VALID product with the wrong n, which forces the
    # mag arithmetic to run rather than short-circuiting on an invalid input.
    "broken_multiplicity_detected": not by[
        "one multiplicity broken (6 -> 12, VALID product: arithmetic path)"
    ]["unique"],
    "broken_multiplicity_detected_via_fallback_only": not by[
        "one multiplicity broken (6 -> 7, INVALID product: fallback path)"
    ]["unique"],
    "reflection_tracks_chirality": by["spectrum reflected"]["intersection"] == [-1.5],
}
res["verdict"] = (
    "NOT VACUOUS but NARROWER THAN CLAIMED. The solve detects a moved level, a "
    "broken spacing and a wrong multiplicity -- each destroys the intersection. "
    "It cannot detect a uniform additive shift: a spectrum shifted by +1 returns "
    "a unique 2.5, one shifted by +0.37 returns a unique 1.87. So the "
    "UNIQUENESS is carried by the algebra and the VALUE simply tracks the shift. "
    "Honest statement: D0's spectrum is the Dirac spectrum up to a single "
    "additive constant -- a real constraint, since any level/spacing/multiplicity "
    "corruption breaks it -- and that constant is 3/2. NOT: 'the constant drops "
    "out of the eigenvalue data'."
)

print(json.dumps(res, indent=2))
with open("results_c180b.json", "w", encoding="utf-8") as f:
    json.dump(res, f, indent=2)
