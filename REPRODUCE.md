# Reproduce GeoSpectra v0.4a

**Status:** `PUBLICATION_FREEZE / REPRODUCIBILITY_LOCK_PENDING`  
**Tag:** `v0.4a-paper-complete`  
**Paper:** `paper/WHEN_GEOMETRY_BECOMES_UNRECOVERABLE.md`

---

## 1. Environment

```bash
python --version  # 3.10+
pip install -r requirements.txt
```

## 2. Run Core Experiments

Deterministic (JSON identical):

```bash
python experiments/hard_negatives_suite.py           # 3/4 PASS
python experiments/physics_rescue_track.py           # 4/4 KILLS
python experiments/phase4d_cross_geometry.py         # 3/3 DISTINCT
python experiments/phase4c_t4_baseline.py            # N-DEPENDENT
```

Structure-verified (stochastic numerical):

```bash
python experiments/phase4b_phase_diagram.py          # 35 cells, 3 regimes
```

## 3. Verify Artifacts

```bash
python experiments/verify_artifacts.py
```

Expected: `ALL_SUBSETS_VERIFIED`

## 4. Check Registry

```bash
cat CLAIMS_REGISTRY.md  # 26 claims, 0 L3
```

## 5. Read Paper

```bash
cat paper/WHEN_GEOMETRY_BECOMES_UNRECOVERABLE.md
```

---

## Expected Status

```
PAPER_COMPLETE: yes
PUBLICATION_READY: almost
PEER_REVIEW_READY: after reproducibility lock
L3 claims: 0
Scripts: 11
JSON artifacts: 6
Verified subsets: 7
```
