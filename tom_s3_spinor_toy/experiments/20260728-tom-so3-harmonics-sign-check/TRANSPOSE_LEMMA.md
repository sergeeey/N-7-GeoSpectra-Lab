# Lemma: matrix-times-combined-vector vs honest basis decomposition

**Statement.** Let `L` be a differential (or other linear) operator acting
on a function space, and let `{f_1,...,f_n}` be a basis of a finite
`L`-invariant subspace. Let `T` be a candidate abstract matrix intended to
represent `L` restricted to this subspace, in this basis.

Define two DIFFERENT comparisons:

1. **Honest decomposition** (correct): for each `k`, compute `L(f_k)` and
   decompose it in the basis `{f_1,...,f_n}`; the coefficients form column
   `k` of the true matrix `M` of `L` in this basis.
2. **Combined-vector product** (the pitfall): stack the basis functions into
   a single column `v = (f_1;...;f_n)` and compute `T . v` via ordinary
   matrix-vector multiplication, comparing the result entrywise to
   `(L(f_1); ...; L(f_n))`.

**These two comparisons are NOT the same operation.** `(T.v)_row = sum_col
T[row,col] * f_col` uses T's ROWS; the honest decomposition of `L(f_k)` uses
T's COLUMNS. If comparison (2) reports agreement, the honestly-built matrix
`M` satisfies `M = T^T` (or `M = -T^T`, etc., depending on sign
convention) -- NOT `M = T` -- whenever `T` is not symmetric. For a diagonal
(or otherwise symmetric) `T`, the two comparisons coincide, masking the
issue until an asymmetric generator (like `L_x`, `T_x` in an `so(3)` triplet)
is checked.

**Origin.** Found 2026-07-28 while verifying Tom Lawrence's own SO(3)
harmonics-vs-generators calculation
(`experiments/20260728-tom-so3-harmonics-sign-check/decision.md`): his
comparison (2)-style check gave `L_y = T'_y`, `L_z = T'_z` (both happen to
coincide, T'_z diagonal trivially; T'_y non-symmetric but numerically
coincides for these specific matrix entries), but `L_x = -T'_x` -- not an
arithmetic error, exactly this transpose artifact. **Verified via THREE
independent methods**, all agreeing exactly:
`experiments/20260728-tom-so3-harmonics-sign-check/verify_tom_calc.py`
(linear-system solving), `build_full_matrices.py` (exp(i*phi)-coefficient
decomposition), `verify_via_inner_product.py` (bra-ket integral projection).

**Audited against this project's own results** (round77/C26, round78/C27,
round73/round76): neither is vulnerable -- both use single-object
transformation checks or basis-independent eigenvalue facts, never the
combined-vector pattern. See
`experiments/20260728-transpose-artifact-audit-round77-78/decision.md`.

**Reusable tool.** `intertwiner_checker.py` (this folder) implements the
honest bra-ket construction (method 3 above) plus a classifier
(`compare_to_abstract_matrix`) reporting `EQUAL` / `TRANSPOSE` / `NEGATIVE`
/ `NEGATIVE_TRANSPOSE` / `NO_SIMPLE_RELATION`. Any future round in this
project comparing a differential/geometric operator to an abstract matrix
representation should use this directly rather than re-deriving the
comparison ad hoc.

**Pearl-registry entry:** logged in `pearl_registry/INDEX.md` (this update).
