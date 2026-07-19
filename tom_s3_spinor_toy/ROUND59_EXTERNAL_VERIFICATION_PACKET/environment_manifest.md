# Environment Manifest — Round59 External Verification Packet

## Reference environment (this project's side)

- Python: `3.13.5`
- sympy: `1.14.0`
- OS: Windows (project development environment)
- Note: this manifest was recorded on 2026-07-19 (during PHASE P1.1
  hardening), not at round59's original run time (2026-07-14). This
  project's `requirements.txt` does not pin an exact `sympy` version, so
  this is the best available record of a verified-compatible environment,
  not a guaranteed exact reproduction of the original run's environment.
  `sympy`'s exact rational/radical arithmetic (the only class of operation
  this computation relies on for its "exact certificate" claims) has been
  stable across recent `sympy` minor versions; version drift risk is
  assessed as low but not zero.

## What you should record for your own submission

- Your Python version, your CAS/symbolic-math library and its version (or
  note if you used a different tool entirely — e.g. Mathematica, Maple,
  Sage, or hand computation; a genuinely different CAS is itself a
  stronger independence rung than the same one, per
  `verification_protocol.md`'s Verification Strength Ladder).
- Whether your computation used exact/symbolic arithmetic throughout, or
  floating-point at any stage (and if floating-point, your numerical
  tolerance for the final rank determination).
- OS/platform (unlikely to matter for symbolic computation, but record it
  anyway for completeness).

## Integrity hash of the sealed file

To confirm you are comparing against the same `expected_output_sealed.md`
this manifest was issued alongside (and that it was not altered after
being sealed), the SHA-256 hash of that file, computed at seal time, is:

```
366dfd3504d15e8e7bad581e8bbb0fbab6a65bd6037dd0775caffbdf5471ce7e  expected_output_sealed.md
```

**How to use this:** compute the hash yourself (e.g. `sha256sum
expected_output_sealed.md` or `Get-FileHash expected_output_sealed.md
-Algorithm SHA256` on Windows) immediately BEFORE you open the file (i.e.
after completing your own independent computation, per
`verification_protocol.md`'s sequencing) and confirm it matches the value
above. A mismatch means the file changed after this manifest was written —
stop and request a re-issued packet rather than proceeding.

**What this hash does NOT protect against:** it does not prove the sealed
content is correct — only that you are reading the same bytes this project
sealed on 2026-07-19. Correctness is exactly what your own independent
computation is testing.
