# C223 Decision -- Hopf map facts and the frame built from the SU(2) matrix elements g_ab

**Date:** 2026-11-02

## Result

Exact sympy plus numeric checks, 39 checks in five scripts. (1) For the Hopf map x_i = xi^dagger sigma_i xi: |x| = |xi|^2; the fibres over S^2 are circles xi -> e^{i phi} xi; Ad(-g) = Ad(g), so SU(2) -> SO(3) is two-to-one at group level only. (2) On S^3 = SU(2) the rows of the matrix g(x) form a frame of a two-dimensional bundle over S^2; under the left action by h it transforms by a constant matrix (h^T)^-1, independent of the point (covariance criterion: x-independence of M(h,x) = Phi(hx)^-1 Phi(x)); the Hopf U(1) acts as diag(t, conj t), so the frame descends to S^2 without a choice of lift. (3) A single line of this frame has winding +-1 (Chern number c1 = +-1): the north and south sections differ by e^{i phi} and no nowhere-zero global section exists; the full two-dimensional frame is global, given by an SU(2)-valued map. (4) A claim made earlier in the same working folder, that the frame is not SU(2)_L-covariant, used a wrong criterion (off-diagonal entries of M) and is withdrawn here.

## Scripts and outputs (re-run in this folder)

| script | output | outcome |
|---|---|---|
| `q2_hopf_map.py` | `run_output_q2_hopf_map.txt` | 12 PASS, 0 FAIL |
| `q5_bridge.py` | `run_output_q5_bridge.txt` | 6 PASS, 0 FAIL |
| `q5_obstructions.py` | `run_output_q5_obstructions.txt` | 8 PASS, 0 FAIL |
| `q5_local_kets.py` | `run_output_q5_local_kets.txt` | 10 PASS, 0 FAIL |
| `q5_descent_types.py` | `run_output_q5_descent_types.txt` | 3 PASS, 0 FAIL |

## Conventions

Frame representation h-bar = (h^T)^-1 for the left action; weights as in C182.

## What this does NOT imply

- that this frame is the 'local ket basis' the correspondent has in mind
- which SU(2) factor is physical spin
- that a rank-2 bundle with these transition functions is the right model of a spinor multiplet

## Caveat

q5_descent_types.py contains the withdrawn criterion on purpose (its check T3 shows it is the wrong test); about three checks are definitional (D5-type arithmetic, U4-type tautologies were removed from the tracked set).

## Notes

Result rows R02, R05 and the retraction R06 of the private correspondence layer. Status vocabulary follows the ledger; no result here is externally reviewed.
