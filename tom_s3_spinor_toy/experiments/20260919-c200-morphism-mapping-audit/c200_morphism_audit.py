"""C200 -- run the 5-outcome morphism-mapping audit on every target, with controls.

Outcomes (precedence, prompt-literal): EXACT_ISOMORPHISM > QUOTIENT_RELATION >
PARTIAL_ISOMORPHISM > HOMOMORPHISM > NO_STRUCTURAL_BRIDGE.  Two amendments to
the prompt are measured, not assumed: a declared SIGNATURE and a same-size
random-graph NULL (a match is only "calibrated" if chance rarely produces it).

Two kinds of targets: COMPUTED (explicit matrices / weight diagrams, independent
ground truth) and ENCODED (hand-built graphs: verdict depends on the encoding).
"""

from __future__ import annotations

import importlib.util
import itertools
import json
import math
import random
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c200.json"
TOL = 1e-9
N_NULL = 300
ALPHA = 0.05
SEED = 200
HOM_NODE_CAP = 100_000
EMPTY: frozenset = frozenset()


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G102 = _load(
    "g102_spin8_fiber",
    HERE.parent / "20260705-g102-spin8-fiber-obstruction" / "g102_spin8_fiber.py",
)

# ---------------------------------------------------------------------------
# Labelled directed graphs and the classifier
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Graph:
    nodes: tuple
    edges: frozenset  # (u, v, label)
    nlabel: tuple = ()  # ((node, label), ...)
    sym: frozenset = EMPTY  # edge labels that are symmetric relations

    def nl(self, n):
        return dict(self.nlabel).get(n)

    def labels(self) -> list:
        return sorted({e[2] for e in self.edges}, key=str)


def make(nodes, edges, nlabel=None, sym=()) -> Graph:
    e = set()
    for u, v, lab in edges:
        e.add((u, v, lab))
        if lab in sym:
            e.add((v, u, lab))
    nlab = tuple(sorted(nlabel.items(), key=str)) if nlabel else ()
    return Graph(tuple(nodes), frozenset(e), nlab, frozenset(sym))


def _pm(g: Graph) -> dict:
    d: dict = {}
    for u, v, lab in g.edges:
        d.setdefault((u, v), set()).add(lab)
    return {k: frozenset(v) for k, v in d.items()}


def relabel_edges(g: Graph, perm: dict) -> Graph:
    return Graph(
        g.nodes,
        frozenset((u, v, perm.get(lab, lab)) for u, v, lab in g.edges),
        g.nlabel,
        frozenset(perm.get(lab, lab) for lab in g.sym),
    )


def coarsen_nodes(g: Graph, fn) -> Graph:
    return Graph(g.nodes, g.edges, tuple((n, fn(lab)) for n, lab in g.nlabel), g.sym)


def restrict_labels(g: Graph, keep: dict) -> Graph:
    """Keep only edge labels in `keep` and rename them via keep[label]."""
    return Graph(
        g.nodes,
        frozenset((u, v, keep[lab]) for u, v, lab in g.edges if lab in keep),
        g.nlabel,
        frozenset(keep[lab] for lab in g.sym if lab in keep),
    )


def _embed(
    a: Graph, sub: tuple, b: Graph, ap: dict, bp: dict, budget: dict | None = None
):
    """Injective f: sub -> b.nodes preserving node labels and the label sets of ALL pairs
    inside `sub` (induced).  Returns a mapping or None.  `budget` (optional, used only for
    null trials) is {"left": steps, "hit": bool}; exhausting it returns None and sets hit."""
    deg = {u: sum(1 for (x, y) in ap if x == u or y == u) for u in sub}
    order = sorted(sub, key=lambda u: -deg[u])
    assign: dict = {}
    taken: set = set()

    def ok(u, x) -> bool:
        if a.nl(u) != b.nl(x):
            return False
        if ap.get((u, u), EMPTY) != bp.get((x, x), EMPTY):
            return False
        for w, y in assign.items():
            if ap.get((u, w), EMPTY) != bp.get((x, y), EMPTY):
                return False
            if ap.get((w, u), EMPTY) != bp.get((y, x), EMPTY):
                return False
        return True

    def rec(i: int):
        if budget is not None:
            budget["left"] -= 1
            if budget["left"] < 0:
                budget["hit"] = True
                return None
        if i == len(order):
            return dict(assign)
        u = order[i]
        for x in b.nodes:
            if x in taken or not ok(u, x):
                continue
            assign[u] = x
            taken.add(x)
            r = rec(i + 1)
            if r is not None:
                return r
            del assign[u]
            taken.discard(x)
        return None

    return rec(0)


def find_iso(a: Graph, b: Graph):
    if len(a.nodes) != len(b.nodes) or len(a.edges) != len(b.edges):
        return None
    return _embed(a, a.nodes, b, _pm(a), _pm(b))


def max_common_induced(a: Graph, b: Graph, kmin: int = 2, budget: dict | None = None):
    """Largest k >= kmin such that an induced k-node subgraph of `a` embeds in `b`."""
    ap, bp = _pm(a), _pm(b)
    for k in range(min(len(a.nodes), len(b.nodes)), kmin - 1, -1):
        for sub in itertools.combinations(a.nodes, k):
            f = _embed(a, sub, b, ap, bp, budget)
            if f is not None:
                return k, sub, f
    return None


def find_surj_hom(a: Graph, b: Graph):
    """Surjective (nodes and edges), NON-injective label-preserving homomorphism a -> b.
    Returns (mapping|None, cap_hit)."""
    if len(a.nodes) <= len(b.nodes):
        return None, False
    ap, bp = _pm(a), _pm(b)
    order = list(a.nodes)
    f: dict = {}
    counter = [0]
    cap = [False]
    n_b = len(b.nodes)

    def ok(u, x) -> bool:
        if a.nl(u) != b.nl(x):
            return False
        if ap.get((u, u), EMPTY) - bp.get((x, x), EMPTY):
            return False
        for w, y in f.items():
            if ap.get((u, w), EMPTY) - bp.get((x, y), EMPTY):
                return False
            if ap.get((w, u), EMPTY) - bp.get((y, x), EMPTY):
                return False
        return True

    def rec(i: int):
        counter[0] += 1
        if counter[0] > HOM_NODE_CAP:
            cap[0] = True
            return None
        covered = set(f.values())
        if n_b - len(covered) > len(order) - i:
            return None
        if i == len(order):
            img = {(f[u], f[v], lab) for u, v, lab in a.edges}
            return dict(f) if b.edges <= img else None
        u = order[i]
        for x in b.nodes:
            if ok(u, x):
                f[u] = x
                r = rec(i + 1)
                if r is not None:
                    return r
                del f[u]
            if cap[0]:
                return None
        return None

    return rec(0), cap[0]


def classify(
    a: Graph,
    b: Graph,
    label_group: list | None = None,
    core_frac: float = 0.5,
    core_min: int = 3,
) -> dict:
    """Prompt-literal classification.  Reports every level that holds."""
    out: dict = {"n_a": len(a.nodes), "n_b": len(b.nodes)}
    out["exact"] = find_iso(a, b) is not None
    out["quotient_label_perm"] = None
    for perm in label_group or []:
        if all(perm.get(k, k) == k for k in perm):
            continue
        if find_iso(a, relabel_edges(b, perm)) is not None:
            out["quotient_label_perm"] = {str(k): str(v) for k, v in perm.items()}
            break
    core = max_common_induced(a, b, kmin=2)
    any_node_match = any(a.nl(u) == b.nl(x) for u in a.nodes for x in b.nodes)
    out["core_size"] = core[0] if core else (1 if any_node_match else 0)
    out["core_nodes"] = [str(n) for n in core[1]] if core else []
    thr = max(core_min, math.ceil(core_frac * min(len(a.nodes), len(b.nodes))))
    out["core_threshold"] = thr
    hom_ab, cap1 = find_surj_hom(a, b)
    hom_ba, cap2 = find_surj_hom(b, a)
    # a surjective NON-injective map needs |source| > |target|; otherwise the test is "n/a", not False
    out["hom_ab"] = None if len(a.nodes) <= len(b.nodes) else hom_ab is not None
    out["hom_ba"] = None if len(b.nodes) <= len(a.nodes) else hom_ba is not None
    out["hom_cap_hit"] = bool(cap1 or cap2)
    if out["exact"]:
        out["raw"] = "EXACT_ISOMORPHISM"
    elif out["quotient_label_perm"]:
        out["raw"] = "QUOTIENT_RELATION"
        out["quotient_kind"] = (
            "twisted isomorphism: same-size graphs related by a declared automorphism of the "
            "edge-label alphabet (NOT a quotient map)"
        )
    elif out["core_size"] >= thr:
        out["raw"] = "PARTIAL_ISOMORPHISM"
    elif out["hom_ab"] or out["hom_ba"]:
        out["raw"] = "HOMOMORPHISM"
    else:
        out["raw"] = "NO_STRUCTURAL_BRIDGE"
    return out


def random_like(b: Graph, rng: random.Random) -> Graph:
    """Same nodes/node labels, same per-label edge counts, symmetric layers kept symmetric."""
    nodes = list(b.nodes)
    edges: set = set()
    for lab in b.labels():
        m = sum(1 for e in b.edges if e[2] == lab)
        if lab in b.sym:
            pool = [(u, v) for u, v in itertools.combinations(nodes, 2)]
            for u, v in rng.sample(pool, m // 2):
                edges.add((u, v, lab))
                edges.add((v, u, lab))
        else:
            pool = [(u, v) for u in nodes for v in nodes if u != v]
            for u, v in rng.sample(pool, m):
                edges.add((u, v, lab))
    return Graph(b.nodes, frozenset(edges), b.nlabel, b.sym)


def null_rates(
    a: Graph,
    b: Graph,
    n: int,
    seed: int,
    label_group=None,
    obs_core: int = 0,
    want_cores: bool = False,
    step_cap: int | None = None,
) -> dict:
    """Same-size random-graph null.  `want_cores` records the full core-size distribution (slow);
    `obs_core` records only P(core >= obs_core); `step_cap` bounds each trial's search and the
    number of trials that hit it is REPORTED (a hit counts as 'not found', i.e. it can only
    understate the null rate)."""
    rng = random.Random(seed)
    ex = qu = ge_core = cap_hits = 0
    cores: list[int] = []
    for _ in range(n):
        bn = random_like(b, rng)
        if find_iso(a, bn) is not None:
            ex += 1
            continue
        if any(
            find_iso(a, relabel_edges(bn, p)) is not None for p in (label_group or [])
        ):
            qu += 1
        if obs_core >= 2:
            budget = {"left": step_cap, "hit": False} if step_cap else None
            c = max_common_induced(a, bn, kmin=obs_core, budget=budget)
            cap_hits += int(bool(budget and budget["hit"]))
            if c is not None:
                ge_core += 1
        elif want_cores:
            c = max_common_induced(a, bn, kmin=2)
            cores.append(c[0] if c else 1)
    return {
        "n": n,
        "exact_rate": ex / n,
        "exact_or_quotient_rate": (ex + qu) / n,
        "core_ge_obs_rate": (ge_core / n) if obs_core >= 2 else None,
        "core_size_counts": {str(k): cores.count(k) for k in sorted(set(cores))}
        if cores
        else {},
        "cap_hits": cap_hits,
    }


def calibrate(raw: dict, nulls: dict) -> dict:
    """Null-calibrated verdict: a level is only credited if chance rarely produces it."""
    v = raw["raw"]
    chance = nulls.get("exact_or_quotient_rate")
    base = {"chance_exact_or_quotient_rate": chance}
    if nulls.get("cap_hits", 0) > 0:
        return {
            **base,
            "calibrated": f"{v}(UNCALIBRATED: null search budget exhausted in "
            f"{nulls['cap_hits']}/{nulls['n']} trials)",
            "null_rate": None,
        }
    if nulls["n"] * ALPHA < 3:
        return {
            **base,
            "calibrated": f"{v}(UNCALIBRATED: null n={nulls['n']} cannot resolve alpha={ALPHA})",
            "null_rate": None,
        }
    if v in ("EXACT_ISOMORPHISM", "QUOTIENT_RELATION"):
        rate = nulls["exact_or_quotient_rate"]
        return {
            **base,
            "calibrated": v if rate < ALPHA else "VACUOUS_" + v,
            "null_rate": rate,
        }
    if v == "PARTIAL_ISOMORPHISM":
        rate = nulls["core_ge_obs_rate"]
        if rate is None:
            return {
                **base,
                "calibrated": "PARTIAL_ISOMORPHISM(UNCALIBRATED: no core null measured)",
                "null_rate": None,
            }
        return {
            **base,
            "calibrated": v
            if rate < ALPHA
            else "NO_STRUCTURAL_BRIDGE(chance-level core)",
            "null_rate": rate,
        }
    return {**base, "calibrated": v, "null_rate": None}


# ---------------------------------------------------------------------------
# Module-level classifier (matrices)
# ---------------------------------------------------------------------------


def hom_basis(rep_a: list, rep_b: list) -> list:
    n_a, n_b = rep_a[0].shape[0], rep_b[0].shape[0]
    rows = [
        np.kron(a.T, np.eye(n_b)) - np.kron(np.eye(n_a), b)
        for a, b in zip(rep_a, rep_b, strict=True)
    ]
    return [v.reshape((n_b, n_a), order="F") for v in G102.nullspace(np.vstack(rows))]


def module_relation(rep_a: list, rep_b: list, seed: int = 0) -> dict:
    basis = hom_basis(rep_a, rep_b)
    hd = len(basis)
    ea = len(hom_basis(rep_a, rep_a))
    eb = len(hom_basis(rep_b, rep_b))
    out = {
        "hom": hd,
        "end_a": ea,
        "end_b": eb,
        "strict_cauchy_schwarz_nonisomorphic": hd * hd < ea * eb,
    }
    if hd == 0:
        out.update(
            verdict="NO_STRUCTURAL_BRIDGE", invertible=False, rank=0, residual=None
        )
        return out
    rng = np.random.default_rng(seed)
    s_mat = sum(c * m for c, m in zip(rng.normal(size=hd), basis, strict=True))
    sv = np.linalg.svd(s_mat, compute_uv=False)
    n = rep_a[0].shape[0]
    rank = int(np.sum(sv > 1e-8 * sv[0]))
    invertible = rank == n and rep_b[0].shape[0] == n
    residual = None
    if invertible:
        inv = np.linalg.inv(s_mat)
        residual = max(
            float(np.max(np.abs(s_mat @ a @ inv - b)))
            for a, b in zip(rep_a, rep_b, strict=True)
        )
        invertible = residual < 1e-7
    out.update(
        verdict="EXACT_ISOMORPHISM"
        if invertible
        else "PARTIAL_OR_HOMOMORPHISM(shared proper submodule)",
        invertible=invertible,
        rank=rank,
        residual=residual,
    )
    return out


def spin_reps() -> tuple:
    vec, sp, sm = G102.spin_rep_blocks()
    return vec, sp, sm


def restrict_named(sub: list) -> dict:
    v, s, c = G102.restrict_to_subalgebra(sub)
    return {"v": v, "s": s, "c": c}


def stabilizer_in_so8(rep_mats: list, vector_index: int = 0) -> list:
    """Elements of so(8) (F_ab basis) whose image in `rep_mats` annihilates basis vector `vector_index`."""
    so8 = G102.so8_basis()
    e = np.zeros(rep_mats[0].shape[0])
    e[vector_index] = 1.0
    cols = np.array([m @ e for m in rep_mats]).T
    coeffs = G102.nullspace(cols)
    return [sum(cf * f for cf, f in zip(row, so8, strict=True)) for row in coeffs]


# ---------------------------------------------------------------------------
# Weight graphs of the three 8-dimensional so(8) representations
# ---------------------------------------------------------------------------

H = Fraction(1, 2)
ALPHA_ROOTS = {
    1: (1, -1, 0, 0),
    2: (0, 1, -1, 0),
    3: (0, 0, 1, -1),
    4: (0, 0, 1, 1),
}


def _weights(kind: str) -> list[tuple]:
    if kind == "v":
        w = []
        for i in range(4):
            for sgn in (1, -1):
                t = [Fraction(0)] * 4
                t[i] = Fraction(sgn)
                w.append(tuple(t))
        return w
    out = []
    for signs in itertools.product((1, -1), repeat=4):
        minus = sum(1 for s in signs if s < 0)
        if (kind == "s" and minus % 2 == 0) or (kind == "c" and minus % 2 == 1):
            out.append(tuple(H * s for s in signs))
    return out


def weight_graph(kind: str) -> Graph:
    ws = _weights(kind)
    wset = set(ws)
    edges = []
    for u in ws:
        for lab, root in ALPHA_ROOTS.items():
            v = tuple(u[i] - root[i] for i in range(4))
            if v in wset:
                edges.append((u, v, lab))
    return make(ws, edges)


def s3_label_group() -> list[dict]:
    return [
        dict(zip((1, 3, 4), p, strict=True)) | {2: 2}
        for p in itertools.permutations((1, 3, 4))
    ]


def shuffled_copy(g: Graph, rng: random.Random) -> Graph:
    perm = list(g.nodes)
    rng.shuffle(perm)
    m = dict(zip(g.nodes, perm, strict=True))
    return Graph(
        tuple(m[n] for n in g.nodes),
        frozenset((m[u], m[v], lab) for u, v, lab in g.edges),
        tuple((m[n], lab) for n, lab in g.nlabel),
        g.sym,
    )


def wl_signature(g: Graph, rounds: int = 3) -> tuple:
    """1-WL colour-refinement multiset (edge labels + direction): an isomorphism invariant computed
    by an algorithm independent of the matcher, so a differing signature PROVES non-isomorphism."""
    col = {n: repr(g.nl(n)) for n in g.nodes}
    for _ in range(rounds):
        col = {
            n: repr(
                (
                    col[n],
                    sorted((str(lab), col[v]) for u, v, lab in g.edges if u == n),
                    sorted((str(lab), col[u]) for u, v, lab in g.edges if v == n),
                )
            )
            for n in g.nodes
        }
    return tuple(sorted(col.values()))


def edge_move(g: Graph, rng: random.Random) -> Graph:
    """Relocate ONE edge (same label, new endpoints) so that the WL signature changes, i.e. the
    result is provably NOT isomorphic to g (oracle independent of the matcher under test)."""
    base = wl_signature(g)
    edges = sorted(g.edges, key=str)
    for _ in range(2000):
        u, v, lab = rng.choice(edges)
        u2, v2 = rng.sample(list(g.nodes), 2)
        if (u2, v2, lab) in g.edges:
            continue
        cand = Graph(
            g.nodes,
            frozenset((set(g.edges) - {(u, v, lab)}) | {(u2, v2, lab)}),
            g.nlabel,
            g.sym,
        )
        if wl_signature(cand) != base:
            return cand
    raise RuntimeError("no invariant-changing edge move found")


# ---------------------------------------------------------------------------
# Runners
# ---------------------------------------------------------------------------


def run_controls(res: dict) -> bool:
    print("=== T0: instrument controls ===")
    ctl: dict = {}
    der = G102.derivation_basis()
    su3 = G102.stabilizer_basis(der)
    so8 = G102.so8_basis()
    rg2, rsu3, rso8 = restrict_named(der), restrict_named(su3), restrict_named(so8)
    pairs = [("v", "s"), ("s", "c"), ("c", "v")]

    for name, reps in (("g2", rg2), ("su3", rsu3)):
        for a, b in pairs:
            r = module_relation(reps[a], reps[b])
            ctl[f"PC-M_{name}_{a}{b}"] = r
            ok = r["verdict"] == "EXACT_ISOMORPHISM"
            print(
                f"  PC-M {name} {a}-{b}: hom={r['hom']} verdict={r['verdict']} residual={r['residual']} -> {'PASS' if ok else 'FAIL'}"
            )
            ctl[f"PC-M_{name}_{a}{b}"]["pass"] = ok

    rng = np.random.default_rng(7)
    q = rng.normal(size=(8, 8)) + 3 * np.eye(8)
    qi = np.linalg.inv(q)
    rep_q = [q @ m @ qi for m in rg2["v"]]
    r = module_relation(rg2["v"], rep_q)
    r["pass"] = r["verdict"] == "EXACT_ISOMORPHISM"
    ctl["PC-M3_basis_change"] = r
    print(
        f"  PC-M3 basis change: verdict={r['verdict']} residual={r['residual']} -> {'PASS' if r['pass'] else 'FAIL'}"
    )

    r = module_relation(rso8["v"], rso8["s"])
    r["pass"] = r["verdict"] == "NO_STRUCTURAL_BRIDGE"
    ctl["NC-M1_so8_v_s"] = r
    print(
        f"  NC-M1 so(8) v-s: hom={r['hom']} verdict={r['verdict']} strict-CS-nonisomorphic={r['strict_cauchy_schwarz_nonisomorphic']} -> {'PASS' if r['pass'] else 'FAIL'}"
    )

    # NC-M2 as PRE-REGISTERED (g2 8_v vs itself with the generator correspondence shifted, expected
    # Hom = 0) turned out to be a MALFORMED CHECK, not an instrument failure: 8_v|g2 = 7 + 1 and the
    # trivial summand is killed by every generator, so ANY correspondence shares it.  The corrected
    # expectation is derived from the invariant-vector count (independent of the classifier).
    shifted = rg2["v"][1:] + rg2["v"][:1]
    inv_dim = len(G102.nullspace(np.vstack(rg2["v"])))
    r = module_relation(rg2["v"], shifted)
    r["invariants_of_8v_under_g2"] = inv_dim
    r["preregistered_expectation_hom0_was_wrong"] = r["hom"] != 0
    r["pass"] = (
        r["verdict"].startswith("PARTIAL")
        and r["hom"] == inv_dim
        and r["rank"] == inv_dim
    )
    ctl["PC-M4_g2_shift_shares_only_trivial_summand"] = r
    print(
        f"  PC-M4 (was NC-M2) g2 8_v vs shifted correspondence: hom={r['hom']} rank={r['rank']} "
        f"invariants of 8_v={inv_dim} verdict={r['verdict']} -> {'PASS' if r['pass'] else 'FAIL'}"
        + (
            "  [pre-registered Hom=0 was WRONG: shared trivial summand; control added POST HOC]"
            if r["preregistered_expectation_hom0_was_wrong"]
            else ""
        )
    )
    shifted_so8 = rso8["v"][1:] + rso8["v"][:1]
    r = module_relation(rso8["v"], shifted_so8)
    r["pass"] = r["verdict"] == "NO_STRUCTURAL_BRIDGE"
    ctl["NC-M2a_so8_shift"] = r
    print(
        f"  NC-M2a so(8) 8_v (irreducible) vs shifted correspondence: hom={r['hom']} verdict={r['verdict']} -> {'PASS' if r['pass'] else 'FAIL'}"
    )

    rng_p = random.Random(SEED)
    wg = {k: weight_graph(k) for k in "vsc"}
    for k, g in wg.items():
        assert len(g.nodes) == 8 and len(g.edges) == 8, (k, len(g.nodes), len(g.edges))
    sh = shuffled_copy(wg["v"], rng_p)
    r = classify(wg["v"], sh)
    ok = r["raw"] == "EXACT_ISOMORPHISM"
    ctl["PC-G1_shuffle"] = {"raw": r["raw"], "pass": ok}
    print(f"  PC-G1 8_v vs node-shuffled 8_v: {r['raw']} -> {'PASS' if ok else 'FAIL'}")

    grp = s3_label_group()
    for a, b in (("v", "s"), ("s", "c"), ("c", "v")):
        r = classify(wg[a], wg[b], label_group=grp)
        ok = (not r["exact"]) and r["quotient_label_perm"] is not None
        ctl[f"PC-G2_{a}{b}"] = {
            "raw": r["raw"],
            "perm": r["quotient_label_perm"],
            "pass": ok,
        }
        print(
            f"  PC-G2 8_{a} vs 8_{b}: exact={r['exact']} quotient_perm={r['quotient_label_perm']} raw={r['raw']} -> {'PASS' if ok else 'FAIL'}"
        )

    # controls for the two levels the first version never exercised (added POST HOC after review;
    # graphs constructed by hand, answers derived by hand, independent of the matcher)
    pend = make((*wg["v"].nodes, "z"), [*wg["v"].edges, ("z", wg["v"].nodes[0], 1)])
    r = classify(wg["v"], pend, label_group=grp)
    ok = r["raw"] == "PARTIAL_ISOMORPHISM" and r["core_size"] == 8
    ctl["PC-P1_pendant_partial"] = {
        "raw": r["raw"],
        "core_size": r["core_size"],
        "pass": ok,
    }
    print(
        f"  PC-P1 8_v vs 8_v + pendant node (known core 8): raw={r['raw']} core={r['core_size']} -> {'PASS' if ok else 'FAIL'}"
    )
    p4 = make(range(4), [(0, 1, "x"), (1, 2, "x"), (2, 3, "x")])
    c3 = make(("p", "q", "r"), [("p", "q", "x"), ("q", "r", "x"), ("r", "p", "x")])
    r = classify(p4, c3)
    ok = r["raw"] == "HOMOMORPHISM" and r["hom_ab"] is True
    ctl["PC-H1_path4_onto_cycle3"] = {
        "raw": r["raw"],
        "hom_ab": r["hom_ab"],
        "pass": ok,
    }
    print(
        f"  PC-H1 directed path P4 onto directed 3-cycle (known surjective hom): raw={r['raw']} core={r['core_size']} -> {'PASS' if ok else 'FAIL'}"
    )
    edge2 = make(("p", "q"), [("p", "q", "x")])
    r = classify(p4, edge2)
    ok = r["raw"] == "NO_STRUCTURAL_BRIDGE" and r["hom_ab"] is False
    ctl["NC-H1_path4_onto_edge"] = {"raw": r["raw"], "hom_ab": r["hom_ab"], "pass": ok}
    print(
        f"  NC-H1 directed path P4 vs single edge (no surjective hom exists): raw={r['raw']} -> {'PASS' if ok else 'FAIL'}"
    )

    sw = edge_move(wg["v"], random.Random(SEED + 1))
    r = classify(wg["v"], sw, label_group=grp)
    ok = not r["exact"]
    ctl["NC-G1_edge_move"] = {"raw": r["raw"], "core_size": r["core_size"], "pass": ok}
    print(
        f"  NC-G1 one edge moved (WL-signature proves non-isomorphic): exact={r['exact']} raw={r['raw']} core={r['core_size']} -> {'PASS' if ok else 'FAIL'}"
    )

    nl = null_rates(wg["v"], wg["s"], N_NULL, SEED, label_group=grp, want_cores=True)
    ok = nl["exact_or_quotient_rate"] <= 0.01
    thr8 = max(3, math.ceil(0.5 * 8))
    chance_partial = (
        sum(v for k, v in nl["core_size_counts"].items() if int(k) >= thr8) / nl["n"]
    )
    ctl["NC-G2_random_wiring"] = {
        **nl,
        "chance_partial_rate": chance_partial,
        "pass": ok,
    }
    print(
        f"  NC-G2 random wiring x{N_NULL}: EXACT-or-QUOTIENT rate={nl['exact_or_quotient_rate']:.4f} "
        f"core-size counts={nl['core_size_counts']} -> {'PASS' if ok else 'FAIL'}"
    )
    print(
        f"        raw PARTIAL rule (core >= {thr8} of 8) fires on chance graphs at rate {chance_partial:.3f}"
        " -> the literal PARTIAL threshold has NO discriminating power at n=8"
        if chance_partial >= ALPHA
        else f"        raw PARTIAL rule fires by chance at rate {chance_partial:.3f}"
    )

    valid_keys = list(ctl)
    instrument_valid = all(ctl[k]["pass"] for k in valid_keys)
    res["controls"] = ctl
    res["instrument_valid"] = instrument_valid
    print(
        f"  -> instrument valid (all {len(valid_keys)} controls): {instrument_valid}\n"
    )
    return instrument_valid


def run_computed(res: dict) -> None:
    print(
        "=== T1a: signature ladder on {8_v, 8_s, 8_c} (module level, explicit matrices) ==="
    )
    der = G102.derivation_basis()
    su3 = G102.stabilizer_basis(der)
    so8 = G102.so8_basis()
    vec, sp, sm = spin_reps()
    so7 = {
        "so7_v": stabilizer_in_so8(vec),
        "so7_s": stabilizer_in_so8(sp),
        "so7_c": stabilizer_in_so8(sm),
    }
    sigs = {"su3": su3, "g2": der, **so7, "so8": so8}
    ladder: dict = {}
    for name, sub in sigs.items():
        reps = restrict_named(sub)
        row = {"dim": len(sub)}
        for a, b in (("v", "s"), ("s", "c"), ("c", "v")):
            row[f"{a}{b}"] = module_relation(reps[a], reps[b])
        ladder[name] = row
        summary = ", ".join(
            f"{a}{b}:{row[a + b]['verdict'].split('(')[0][:5]}(hom={row[a + b]['hom']},endA={row[a + b]['end_a']},endB={row[a + b]['end_b']})"
            for a, b in (("v", "s"), ("s", "c"), ("c", "v"))
        )
        print(f"  {name:6s} dim={len(sub):2d}: {summary}")
    res["T1a_ladder"] = ladder

    print(
        "\n=== T1b: so(8) weight graphs of the three channels (combinatorial level) ==="
    )
    wg = {k: weight_graph(k) for k in "vsc"}
    grp = s3_label_group()
    t1b: dict = {}
    for a, b in (("v", "s"), ("s", "c"), ("c", "v")):
        r = classify(wg[a], wg[b], label_group=grp)
        nl = null_rates(wg[a], wg[b], N_NULL, SEED + 2, label_group=grp)
        cal = calibrate(r, nl)
        t1b[f"{a}{b}"] = {"classify": r, "null": nl, "calibrated": cal}
        print(
            f"  8_{a} vs 8_{b}: raw={r['raw']} perm={r['quotient_label_perm']} null-rate={cal['null_rate']:.4f} calibrated={cal['calibrated']}"
        )
    res["T1b_weight_graphs"] = t1b
    print()


def _tournament(nodes, order_edges, label):
    return make(nodes, [(u, v, label) for u, v in order_edges])


def run_t2a(res: dict) -> None:
    print(
        "=== T2a: triality channels {v,s,c} vs SM generations {g1,g2,g3}  [ENCODING-CHOICE] ==="
    )
    A_nodes, B_nodes = ("v", "s", "c"), ("g1", "g2", "g3")
    a_full = make(
        A_nodes,
        [(i, j, "iso_h") for i, j in itertools.combinations(A_nodes, 2)]
        + [(i, j, "noniso_G") for i, j in itertools.combinations(A_nodes, 2)]
        + [("v", "s", "tau"), ("s", "c", "tau"), ("c", "v", "tau")],
        sym=("iso_h", "noniso_G"),
    )
    b_full = make(
        B_nodes,
        [(i, j, "same_gauge") for i, j in itertools.combinations(B_nodes, 2)]
        + [(i, j, "mass_distinct") for i, j in itertools.combinations(B_nodes, 2)]
        + [
            ("g1", "g2", "mass_order"),
            ("g2", "g3", "mass_order"),
            ("g1", "g3", "mass_order"),
        ],
        sym=("same_gauge", "mass_distinct"),
    )
    sigs = {
        "S1 unbroken-group indistinguishability": ({"iso_h": "X"}, {"same_gauge": "X"}),
        "S2 S1 + pairwise distinguishability (symmetric)": (
            {"iso_h": "X", "noniso_G": "Y"},
            {"same_gauge": "X", "mass_distinct": "Y"},
        ),
        "S3 cyclic triality action vs transitive mass order": (
            {"tau": "D"},
            {"mass_order": "D"},
        ),
        "S4 union of S2 and S3": (
            {"iso_h": "X", "noniso_G": "Y", "tau": "D"},
            {"same_gauge": "X", "mass_distinct": "Y", "mass_order": "D"},
        ),
    }
    out: dict = {}
    for name, (ka, kb) in sigs.items():
        ga, gb = restrict_labels(a_full, ka), restrict_labels(b_full, kb)
        raw = classify(ga, gb)
        nl = null_rates(
            ga,
            gb,
            N_NULL,
            SEED + 3,
            obs_core=raw["core_size"] if raw["raw"] == "PARTIAL_ISOMORPHISM" else 0,
        )
        cal = calibrate(raw, nl)
        out[name] = {"raw": raw, "null": nl, "calibrated": cal}
        print(
            f"  {name}: raw={raw['raw']} (core={raw['core_size']}, hom_ab={raw['hom_ab']}, hom_ba={raw['hom_ba']})"
            f" chance-EXACT-rate={cal['chance_exact_or_quotient_rate']:.3f} calibrated={cal['calibrated']}"
        )
    sym_a = make(A_nodes, [(i, j, "D") for i in A_nodes for j in A_nodes if i != j])
    sym_b = restrict_labels(b_full, {"mass_distinct": "D"})
    sym3 = classify(sym_a, sym_b)
    out["S3-symmetrised (direction thrown away)"] = {"raw": sym3["raw"]}
    s3_raw = out["S3 cyclic triality action vs transitive mass order"]["raw"]["raw"]
    print(
        f"  S3 with direction thrown away (both sides symmetric): raw={sym3['raw']}"
        + (
            "  <- direction is the only thing separating S3's verdict from an EXACT match"
            if sym3["raw"] == "EXACT_ISOMORPHISM" and s3_raw != "EXACT_ISOMORPHISM"
            else ""
        )
    )
    print(
        "  NOTE: on 3 nodes chance alone yields an exact match at the rates above, so no POSITIVE bridge"
        " on these encodings can be calibrated at alpha=0.05; the NO_BRIDGE verdicts are exhaustive facts"
        " about the encodings, not statistics."
    )
    res["T2a"] = out
    print()


def run_t2b(res: dict) -> None:
    print(
        "=== T2b: C198 pipeline, circulant/Lovasz (G_A) vs Dirac-on-S3xS6 kernel (G_B)  [ENCODING-CHOICE] ==="
    )
    roles = ["obj", "grp", "basis", "prob", "red", "ker", "shape", "concl"]
    edges = [
        ("obj", "grp", "sym"),
        ("grp", "basis", "irreps"),
        ("obj", "prob", "defines"),
        ("basis", "red", "reduce"),
        ("prob", "red", "reduce"),
        ("red", "ker", "kernel"),
        ("ker", "shape", "shape"),
        ("shape", "concl", "bound"),
    ]
    attrs_a = {
        "obj": "circulant graph",
        "grp": "abelian (Z_n)",
        "basis": "1-dim Fourier characters",
        "prob": "SDP (Lovasz theta)",
        "red": "1x1 blocks (LP)",
        "ker": "random Fourier kernel, dim varies",
        "shape": "null-space inequality PROVED",
        "concl": "numeric bound on invariant",
    }
    attrs_b = {
        "obj": "bundle on S3xS6 + connection family",
        "grp": "non-abelian (SU(2), SU(3) isotropy)",
        "basis": "multi-dim irreps (Peter-Weyl)",
        "prob": "Dirac operator D(nabla)",
        "red": "multiplicity matrix blocks A_lambda",
        "ker": "dim 1, stable over 13 angles",
        "shape": "kernel LINE fixed (C198, exact)",
        "concl": "Delta_geo diagnostic, no rotation",
    }
    g_attr_a = make(roles, edges, nlabel=attrs_a)
    g_attr_b = make(roles, edges, nlabel=attrs_b)
    out: dict = {}
    raw = classify(g_attr_a, g_attr_b)
    # Coarsening each attribute back to its own role gives IDENTICAL graphs, because both graphs were
    # written from one edge list: this "quotient" is an identity by construction, not a measurement,
    # and no null can make it informative.  The only content is the attribute table below.
    role_a = coarsen_nodes(
        g_attr_a, lambda lab: next(r for r in roles if attrs_a[r] == lab)
    )
    role_b = coarsen_nodes(
        g_attr_b, lambda lab: next(r for r in roles if attrs_b[r] == lab)
    )
    identity_by_construction = role_a == role_b
    out["attribute_level"] = {
        "exact": raw["exact"],
        "core_size": raw["core_size"],
        "raw": raw["raw"],
    }
    out["role_level_identical_by_construction"] = identity_by_construction
    forgotten = [
        f"{r}: '{attrs_a[r]}' ~ '{attrs_b[r]}'"
        for r in roles
        if attrs_a[r] != attrs_b[r]
    ]
    out["attribute_table_differences"] = forgotten
    print(
        f"  attribute level: exact={raw['exact']} core={raw['core_size']} raw={raw['raw']};"
        f" role-level graphs identical by construction (one shared edge list): {identity_by_construction}"
    )
    print(
        "  => NOT a test. The only content is the author's attribute table (where the analogy stops):"
    )
    for f in forgotten:
        print(f"    - {f}")
    res["T2b"] = out
    print()


def run_t2c(res: dict) -> None:
    print(
        "=== T2c: round89 Killing constants (project: +1/2, -1/2) vs AHL2023 S3 statement (+1/2, +1/2)  [ENCODING-CHOICE] ==="
    )
    a = make(
        ("psi0", "psi1"),
        [("psi0", "psi1", "opp"), ("psi1", "psi0", "opp")],
        nlabel={"psi0": "mag=1/2", "psi1": "mag=1/2"},
    )
    b = make(
        ("phi0", "phi1"),
        [("phi0", "phi1", "same"), ("phi1", "phi0", "same")],
        nlabel={"phi0": "mag=1/2", "phi1": "mag=1/2"},
    )
    mag_a = Graph(a.nodes, frozenset(), a.nlabel)
    mag_b = Graph(b.nodes, frozenset(), b.nlabel)
    r_mag = classify(mag_a, mag_b, core_min=2)
    r_sign = classify(a, b, label_group=[{"opp": "same", "same": "opp"}], core_min=2)
    r_sign_strict = classify(a, b, core_min=2)
    print(
        f"  magnitude layer only (two edgeless labelled nodes, trivially matchable): {r_mag['raw']}"
    )
    print(
        f"  full graph, strict edge labels: {r_sign_strict['raw']};"
        f" with the label alphabet twisted opp<->same (the identification round89 shows physics forbids): {r_sign['raw']}"
        " -> the verdict flips on an encoding convention, not on data"
    )
    a_sign = Graph(a.nodes, a.edges, (), a.sym)
    b_sign = Graph(b.nodes, b.edges, (), b.sym)
    r_signonly = classify(a_sign, b_sign, core_min=2)
    res["T2c"] = {
        "magnitude_layer": r_mag["raw"],
        "sign_relation_layer_strict": r_signonly["raw"],
        "single_graph_strict": r_sign_strict["raw"],
        "single_graph_with_sign_labels_identified": r_sign["raw"],
    }
    print(f"  sign-relation layer alone, strict labels: {r_signonly['raw']}")
    print(
        f"  LAYERED result = magnitude {r_mag['raw']} + sign relation {r_signonly['raw']}; the single-graph classifier returns "
        f"{r_sign_strict['raw']}. The 5-outcome taxonomy has no verdict for a layered result "
        "(round89's own documented verdict, PARTIAL_OPPOSITE_SIGN_STRUCTURAL, is a layered statement).\n"
    )


def run_t2d(res: dict) -> None:
    print(
        "=== T2d: MethodOps 8-stage proposal (G_A) vs this stack's meta-loop.md (G_B)  [ENCODING-CHOICE, CIRCULAR] ==="
    )
    a_nodes = [
        "CLASSIFY",
        "CONTRACT",
        "SUBSTRATE",
        "ROUTE",
        "EXECUTE",
        "VERIFY",
        "ADVERSARIAL",
        "DECIDE",
        "RECOMPOSE",
        "NULL_RESULT",
        "POSTMORTEM",
        "REPLAN",
        "NEEDS_HUMAN",
        "MEMORY",
        "METHOD_UPDATE",
    ]
    chain = [
        ("CLASSIFY", "CONTRACT"),
        ("CONTRACT", "SUBSTRATE"),
        ("SUBSTRATE", "ROUTE"),
        ("ROUTE", "EXECUTE"),
        ("EXECUTE", "VERIFY"),
        ("VERIFY", "ADVERSARIAL"),
        ("ADVERSARIAL", "DECIDE"),
        ("DECIDE", "RECOMPOSE"),
        ("DECIDE", "NULL_RESULT"),
        ("DECIDE", "REPLAN"),
        ("DECIDE", "NEEDS_HUMAN"),
        ("NULL_RESULT", "POSTMORTEM"),
        ("RECOMPOSE", "MEMORY"),
        ("POSTMORTEM", "MEMORY"),
        ("REPLAN", "MEMORY"),
        ("NEEDS_HUMAN", "MEMORY"),
        ("MEMORY", "METHOD_UPDATE"),
    ]
    g_a = make(a_nodes, [(u, v, "next") for u, v in chain])
    b_nodes = a_nodes + ["MECH_DEV"]
    chain_b = [e for e in chain if e != ("RECOMPOSE", "MEMORY")] + [
        ("RECOMPOSE", "MECH_DEV"),
        ("MECH_DEV", "MEMORY"),
        ("REPLAN", "CONTRACT"),
    ]
    g_b = make(b_nodes, [(u, v, "next") for u, v in chain_b])
    raw = classify(g_a, g_b)
    nl = null_rates(g_a, g_b, 8, SEED + 5, obs_core=raw["core_size"], step_cap=100_000)
    cal = calibrate(raw, nl)
    print(
        f"  |G_A|={raw['n_a']} |G_B|={raw['n_b']}: raw={raw['raw']} core={raw['core_size']}/{min(raw['n_a'], raw['n_b'])} hom_ab={raw['hom_ab']} hom_ba={raw['hom_ba']}(cap_hit={raw['hom_cap_hit']})"
    )
    print(
        f"  null: n={nl['n']} trials, step budget exhausted in {nl['cap_hits']}; verdict: {cal['calibrated']}"
    )
    print(
        "  CIRCULARITY: G_B was authored FROM G_A's vocabulary; the node correspondence is by construction, so the verdict is a check on my reading of the braces, not evidence about the world."
    )
    res["T2d"] = {"classify": raw, "null": nl, "calibrated": cal}
    print()


def main() -> None:
    res: dict = {"seed": SEED, "n_null": N_NULL, "alpha": ALPHA}
    valid = run_controls(res)
    if not valid:
        print(
            "INSTRUMENT INVALID -> ORACLE_INADEQUATE. Target verdicts NOT recorded as findings."
        )
        RESULTS_PATH.write_text(json.dumps(res, indent=2, default=str))
        return
    run_computed(res)
    run_t2a(res)
    run_t2b(res)
    run_t2c(res)
    run_t2d(res)
    RESULTS_PATH.write_text(json.dumps(res, indent=2, default=str))
    print(f"wrote {RESULTS_PATH.name}")


if __name__ == "__main__":
    main()
