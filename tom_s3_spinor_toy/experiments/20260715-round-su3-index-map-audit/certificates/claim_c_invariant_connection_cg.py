"""Independent verification of the user's Clebsch-Gordan claims via GL(3)
Pieri's rule (horizontal strip = Sym^k, vertical strip = Lambda^k), restricted
to partitions with <=3 rows (SU(3)/GL(3) correspondence), then converted to
SU(3) Dynkin labels (p,q) = (row1-row2, row2-row3).

This does NOT trust memorized SU(3) product tables -- it re-derives each
decomposition combinatorially from the partition/Young-diagram definition.
"""


def su3_dim(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def to_pq(partition):
    r1, r2, r3 = partition
    return (r1 - r2, r2 - r3)


def horizontal_strip_add(mu, k):
    """mu tensor Sym^k(fund): all lambda (<=3 rows) with lambda/mu a horizontal
    strip of size k, i.e. lambda1>=mu1>=lambda2>=mu2>=lambda3>=mu3>=lambda4=0."""
    mu1, mu2, mu3 = mu
    results = []
    for l1 in range(mu1, mu1 + k + 1):
        for l2 in range(0, mu1 + 1):
            if l2 > l1:
                continue
            if not (mu2 <= l2):
                continue
            for l3 in range(0, mu2 + 1):
                if l3 > l2:
                    continue
                total = (l1 - mu1) + (l2 - mu2) + (l3 - mu3)
                if total == k and l3 >= mu3 and l1 >= l2 >= l3 >= 0:
                    results.append((l1, l2, l3))
    return sorted(set(results))


def vertical_strip_add(mu, k):
    """mu tensor Lambda^k(fund): all lambda (<=3 rows) with lambda/mu a vertical
    strip of size k, i.e. mu_i <= lambda_i <= mu_i+1 for each row, sum=k,
    still a valid partition."""
    mu1, mu2, mu3 = mu
    results = []
    for d1 in (0, 1):
        for d2 in (0, 1):
            for d3 in (0, 1):
                if d1 + d2 + d3 != k:
                    continue
                l1, l2, l3 = mu1 + d1, mu2 + d2, mu3 + d3
                if l1 >= l2 >= l3 >= 0:
                    results.append((l1, l2, l3))
    return sorted(set(results))


def describe(partitions):
    out = []
    for part in partitions:
        p, q = to_pq(part)
        out.append(f"({p},{q}) dim={su3_dim(p, q)}")
    return out


fund_3 = (1, 0, 0)  # 3
antifund_3bar = (1, 1, 0)  # 3bar = Lambda^2(3)
six = (2, 0, 0)  # 6 = Sym^2(3)

print("=== basic checks (re-deriving standard SU(3) tables from scratch) ===")
r = horizontal_strip_add(antifund_3bar, 1)  # 3 (x) 3bar
print("3 (x) 3bar =", describe(r))
assert set(to_pq(x) for x in r) == {(1, 1), (0, 0)}, "expected 8+1"

r = vertical_strip_add(antifund_3bar, 2)  # 3bar (x) 3bar
print("3bar (x) 3bar =", describe(r))
assert set(to_pq(x) for x in r) == {(0, 2), (1, 0)}, "expected 6bar+3"

r = horizontal_strip_add(six, 1)  # 3 (x) 6
print("3 (x) 6 =", describe(r))
assert set(to_pq(x) for x in r) == {(3, 0), (1, 1)}, "expected 10+8"

r = horizontal_strip_add(
    antifund_3bar, 2
)  # 3bar (x) 6  [6 = Sym^2, so add horiz strip of 2 to 3bar]
print("3bar (x) 6 =", describe(r))
assert set(to_pq(x) for x in r) == {(2, 1), (1, 0)}, "expected 15+3"

print()
print("=== the actual claim: m*_C (x) 3bar, does 6=(2,0) appear? ===")
term1 = horizontal_strip_add(antifund_3bar, 1)  # 3 (x) 3bar = 8+1
term2 = vertical_strip_add(antifund_3bar, 2)  # 3bar (x) 3bar = 6bar+3
combined = set(to_pq(x) for x in term1) | set(to_pq(x) for x in term2)
print(
    "m*_C (x) 3bar decomposes as:",
    sorted(combined),
    " dims:",
    [su3_dim(*x) for x in sorted(combined)],
)
print("Does (2,0)='6' appear?", (2, 0) in combined)
assert (2, 0) not in combined, "6 SHOULD be absent per the claim"

print()
print("=== reverse: m*_C (x) 6, does 3bar=(0,1) appear? ===")
term3 = horizontal_strip_add(six, 1)  # 3 (x) 6 = 10+8
term4 = horizontal_strip_add(antifund_3bar, 2)  # 3bar (x) 6 = 15+3
combined2 = set(to_pq(x) for x in term3) | set(to_pq(x) for x in term4)
print(
    "m*_C (x) 6 decomposes as:",
    sorted(combined2),
    " dims:",
    [su3_dim(*x) for x in sorted(combined2)],
)
print("Does (0,1)='3bar' appear?", (0, 1) in combined2)
assert (0, 1) not in combined2, "3bar SHOULD be absent per the claim"

print()
print("BOTH Hom-spaces independently confirmed to vanish:")
print("  Hom_SU(3)(m*_C (x) 3bar, 6) = 0   CONFIRMED")
print("  Hom_SU(3)(m*_C (x) 6, 3bar) = 0   CONFIRMED")
