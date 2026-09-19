"""Independent brute-force oracle for the C200 classifier.

Compares find_iso / max_common_induced / find_surj_hom against exhaustive enumeration on 400
random labelled digraphs (<= 5 nodes), plus known-answer checks for the post-review fixes
(n/a homomorphism flags, core_size 0, label-twist quotient, calibrate UNCALIBRATED branches).
Same author as the classifier: this is not a second skeptic pass.
"""

import importlib.util
import itertools
import random
import sys
from pathlib import Path

P = Path(__file__).resolve().parent / "c200_morphism_audit.py"
spec = importlib.util.spec_from_file_location("c200", P)
c = importlib.util.module_from_spec(spec)
sys.modules["c200"] = c
spec.loader.exec_module(c)

rng = random.Random(12345)
LABELS = ["x", "y"]


def rand_graph(n, p, tag):
    nodes = [f"{tag}{i}" for i in range(n)]
    edges = [
        (u, v, lab) for u in nodes for v in nodes if u != v for lab in LABELS if rng.random() < p
    ]
    return c.make(nodes, edges)


def pm(g):
    return c._pm(g)


def brute_iso(a, b):
    if len(a.nodes) != len(b.nodes):
        return False
    ap, bp = pm(a), pm(b)
    for perm in itertools.permutations(b.nodes):
        m = dict(zip(a.nodes, perm))
        if all(
            ap.get((u, v), c.EMPTY) == bp.get((m[u], m[v]), c.EMPTY)
            for u in a.nodes
            for v in a.nodes
        ):
            return True
    return False


def brute_core(a, b):
    ap, bp = pm(a), pm(b)
    best = 0
    for k in range(min(len(a.nodes), len(b.nodes)), 1, -1):
        for sub in itertools.combinations(a.nodes, k):
            for img in itertools.permutations(b.nodes, k):
                m = dict(zip(sub, img))
                if all(
                    ap.get((u, v), c.EMPTY) == bp.get((m[u], m[v]), c.EMPTY)
                    for u in sub
                    for v in sub
                ):
                    return k
    return best


def brute_surj_hom(a, b):
    if len(a.nodes) <= len(b.nodes):
        return None
    ap, bp = pm(a), pm(b)
    for img in itertools.product(b.nodes, repeat=len(a.nodes)):
        m = dict(zip(a.nodes, img))
        if len(set(img)) != len(b.nodes):
            continue
        if not all(
            ap.get((u, v), c.EMPTY) <= bp.get((m[u], m[v]), c.EMPTY)
            for u in a.nodes
            for v in a.nodes
        ):
            continue
        image = {(m[u], m[v], lab) for u, v, lab in a.edges}
        if b.edges <= image:
            return True
    return False


bad = 0
N = 400
for t in range(N):
    n = rng.choice([3, 4, 5])
    a = rand_graph(n, rng.choice([0.1, 0.2, 0.3]), "a")
    # half of the time b is a shuffled relabelled copy (iso by construction), else independent
    if t % 2 == 0:
        b = c.shuffled_copy(a, rng)
    else:
        b = rand_graph(
            rng.choice([n, n - 1, n + 1]) if n > 3 else n, rng.choice([0.1, 0.2, 0.3]), "b"
        )
    got_iso = c.find_iso(a, b) is not None
    if got_iso != brute_iso(a, b):
        bad += 1
        print("ISO MISMATCH", t)
    got_core = c.max_common_induced(a, b, kmin=2)
    got_k = got_core[0] if got_core else 0
    bk = brute_core(a, b)
    if got_k != bk:
        bad += 1
        print("CORE MISMATCH", t, got_k, bk)
    if len(a.nodes) > len(b.nodes) and len(b.nodes) >= 1 and len(a.nodes) <= 5:
        h, _ = c.find_surj_hom(a, b)
        if (h is not None) != bool(brute_surj_hom(a, b)):
            bad += 1
            print("HOM MISMATCH", t)
print(f"random cross-checks: {N} pairs, mismatches = {bad}")

# label-permutation (quotient) case with a known answer
a = c.make(["p", "q"], [("p", "q", 1)])
b = c.make(["r", "s"], [("r", "s", 3)])
r = c.classify(a, b, label_group=[{1: 3, 3: 1}])
print("label twist:", r["raw"], r.get("quotient_kind", "")[:40])
assert r["raw"] == "QUOTIENT_RELATION"

# hom flags: n/a for equal size, computed when |A| > |B|
r_eq = c.classify(a, b)
assert r_eq["hom_ab"] is None and r_eq["hom_ba"] is None
print("hom n/a for equal-size pairs: ok")

# core_size 0 when no node labels match
ga = c.make(["u", "v"], [("u", "v", "e")], nlabel={"u": "A1", "v": "A2"})
gb = c.make(["w", "z"], [("w", "z", "e")], nlabel={"w": "B1", "z": "B2"})
assert c.classify(ga, gb)["core_size"] == 0
print("core_size 0 with disjoint node labels: ok")

# calibrate: uncalibrated on cap hits and on tiny null n
raw = {"raw": "PARTIAL_ISOMORPHISM"}
cal = c.calibrate(
    raw, {"n": 8, "cap_hits": 8, "exact_or_quotient_rate": 0.0, "core_ge_obs_rate": 0.0}
)
assert "UNCALIBRATED" in cal["calibrated"] and cal["null_rate"] is None
cal = c.calibrate(
    raw, {"n": 8, "cap_hits": 0, "exact_or_quotient_rate": 0.0, "core_ge_obs_rate": 0.0}
)
assert "UNCALIBRATED" in cal["calibrated"]
cal = c.calibrate(
    raw, {"n": 300, "cap_hits": 0, "exact_or_quotient_rate": 0.0, "core_ge_obs_rate": None}
)
assert "UNCALIBRATED" in cal["calibrated"]
cal = c.calibrate(
    {"raw": "EXACT_ISOMORPHISM"}, {"n": 300, "cap_hits": 0, "exact_or_quotient_rate": 1.0}
)
assert cal["calibrated"] == "VACUOUS_EXACT_ISOMORPHISM"
print("calibrate branches: ok")
print("ALL CHECKS DONE")
