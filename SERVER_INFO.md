# Hetzner CX52 Server Info — GeoSpectra v0.1.24 Rerun

**Date started:** 2026-05-31 14:18 UTC  
**Status:** ✅ RUNNING — full rerun in progress

---

## 🖥️ Server Specs

```
IP:       46.224.28.128
Type:     Hetzner Cloud CX52
RAM:      32 GB (30 GiB available)
Swap:     32 GB (created)
CPU:      16 vCPU shared
Storage:  640 GB SSD (601 GB total, 542 GB free)
OS:       Ubuntu 24.04.4 LTS
Location: Nuremberg, Germany
Cost:     €29.95/месяц
```

---

## 🔑 Access

### SSH
```bash
ssh root@46.224.28.128
```

**Root password:** Проверь email от Hetzner (тема: "Your new server geospectra-run")  
**SSH key:** Добавлен (подключение без пароля работает)

---

## 📂 Project Location

```bash
/root/geospectra/
```

**Branch:** `main`  
**Commit:** `4b77684` (fix(gate-4b): parameterize batched rerun output namespace)  
**Operator:** S³ Dirac corrected at `093573b`

---

## 🧪 Tests Status

### ✅ Smoke Test (N=128 j_max=3 seed=123)
- **Time:** 120.8 seconds (~2 minutes)
- **Result:** ✅ PASSED
- **Peak RSS:** <2 GB (из 32 GB available — отличный margin)
- **IPR mean:** 0.0078
- **r-stat:** 1.0
- **Output:** `reports/RUNS/gate4_smoke_v0.1.24/smoke_result.json`

### 🚀 Full Rerun (216 cases)
- **Started:** 2026-05-31 14:28:10 UTC
- **Status:** IN PROGRESS (batch 1/9 running)
- **Estimated time:** ~1.8 hours (108 minutes)
- **Expected finish:** 2026-05-31 16:06 UTC (~4:06 PM local Kazakhstan time)
- **Output:** `reports/RUNS/gate4_fss_v0.1.24/`
- **Log:** `reports/RUNS/gate4_fss_v0.1.24_run.log`

---

## 📊 Monitoring Commands

### Check rerun progress
```bash
ssh root@46.224.28.128 'tail -f ~/geospectra/reports/RUNS/gate4_fss_v0.1.24_run.log'
```

### Attach to tmux session (interactive)
```bash
ssh root@46.224.28.128 'tmux attach -t rerun'
```
(Ctrl+B затем D — чтобы detach без остановки)

### Check memory/CPU usage
```bash
ssh root@46.224.28.128 'htop'
```

### Check completed batches
```bash
ssh root@46.224.28.128 'ls -lh ~/geospectra/reports/RUNS/gate4_fss_v0.1.24/batches/'
```

### Check if rerun still running
```bash
ssh root@46.224.28.128 'tmux ls && ps aux | grep python'
```

---

## ⚙️ Environment Config

```bash
export OPENBLAS_NUM_THREADS=8
export OMP_NUM_THREADS=8
export MKL_NUM_THREADS=8
export NUMEXPR_NUM_THREADS=8
```

**Configured correctly:** ✅ Verified in smoke test  
**CPU utilization:** 16 cores, 8 BLAS threads per process

---

## 📥 Download Results (after rerun completes)

### Option 1: rsync (recommended)
```bash
# From local Windows machine
rsync -avz --progress \
  root@46.224.28.128:~/geospectra/reports/RUNS/gate4_fss_v0.1.24/ \
  "E:/Проверка Гипотез/работаю над проверкой гипотез/N-7-GeoSpectra-Lab/reports/RUNS/gate4_fss_v0.1.24/"
```

### Option 2: scp (backup method)
```bash
scp -r root@46.224.28.128:~/geospectra/reports/RUNS/gate4_fss_v0.1.24 \
  "E:/Проверка Гипотез/работаю над проверкой гипотез/N-7-GeoSpectra-Lab/reports/RUNS/"
```

### Option 3: tar + download
```bash
# On server: create archive
ssh root@46.224.28.128 'cd ~/geospectra && tar -czf gate4_v0.1.24_results.tar.gz reports/RUNS/gate4_fss_v0.1.24'

# Download
scp root@46.224.28.128:~/geospectra/gate4_v0.1.24_results.tar.gz .

# Extract locally
tar -xzf gate4_v0.1.24_results.tar.gz
```

---

## 🗑️ Cleanup (после скачивания результатов)

### Verify results downloaded
```bash
ls -lh "E:/Проверка Гипотез/работаю над проверкой гипотез/N-7-GeoSpectra-Lab/reports/RUNS/gate4_fss_v0.1.24/batches/"
# Должно быть 9 папок: batch_01 ... batch_09
```

### Delete server (чтобы не платить дальше)
1. Зайди в Hetzner Console: https://console.hetzner.cloud/projects
2. Выбери `Default` project
3. Найди сервер `geospectra-run` (46.224.28.128)
4. Нажми **Delete** → подтверди

**ВАЖНО:** Hetzner берёт деньги за полный месяц, даже если удалишь через день. Но если не удалишь — будет списывать €29.95 каждый месяц.

---

## 🔴 Troubleshooting

### Rerun stopped / tmux session gone
```bash
# Check if process still running
ssh root@46.224.28.128 'ps aux | grep python'

# Check last lines of log
ssh root@46.224.28.128 'tail -50 ~/geospectra/reports/RUNS/gate4_fss_v0.1.24_run.log'

# If stopped — restart with --resume
ssh root@46.224.28.128 'cd ~/geospectra && tmux new -s rerun-resume "python3 scripts/run_gate4_batched.py --resume --output-base reports/RUNS/gate4_fss_v0.1.24 --protocol-version v0.1.24 --ipr-metric-version v0.1.24_true_ipr_corrected_s3_dirac 2>&1 | tee -a reports/RUNS/gate4_fss_v0.1.24_run.log"'
```

### OOM despite 32 GB RAM
**Unlikely** (smoke test used <2 GB), but if happens:
```bash
# Check dmesg for OOM killer
ssh root@46.224.28.128 'dmesg -T | grep -i "out of memory"'

# Check swap usage
ssh root@46.224.28.128 'free -h'

# If swap is full (31 GiB used) — need larger server
```

### Server not responding
```bash
# Check server status in Hetzner Console
# Power → Reset (reboot without data loss)

# After reboot — check tmux
ssh root@46.224.28.128 'tmux ls'
# Tmux sessions DON'T survive reboot — need to resume manually
```

---

## 📝 Next Steps (after rerun completes)

1. **Download results** (rsync команда выше)
2. **Verify 216 cases completed:**
   ```bash
   find reports/RUNS/gate4_fss_v0.1.24/batches/ -name "results.json" | wc -l
   # Должно быть 9 (по одному на batch)
   ```
3. **Run comparison report:**
   ```bash
   # Локально
   python scripts/compare_v0.1.21_vs_v0.1.24.py  # (если есть)
   # Или вручную проверь reports/RUNS/gate4_fss_v0.1.24/batches/*/results.json
   ```
4. **Update status docs:**
   - `reports/GATE_4B_v0.1.24_COMPARISON_v0.1.21_vs_v0.1.24.md` (create if signal preserved/weakened/disappeared)
   - `PRE_RERUN_CHECKLIST.md` (mark all 9 items ✅ DONE)
5. **Delete server** (Hetzner Console)
6. **Commit results to git:**
   ```bash
   git add reports/RUNS/gate4_fss_v0.1.24/
   git commit -m "feat(gate-4b): complete v0.1.24 corrected rerun (216 cases)"
   git push
   ```

---

## 💰 Cost Summary

| Item | Cost | Notes |
|------|------|-------|
| Hetzner CX52 | €29.95/месяц | Minimum billing: 1 month |
| Total | **€29.95** | ~$32 USD |

**Actual usage:** ~2 hours (smoke test 2 min + full rerun 1.8h)  
**Effective hourly rate:** €29.95 / 720 hours/month = €0.04/hour

---

**Created:** 2026-05-31  
**Last updated:** 2026-05-31 14:28 UTC  
**Owner:** Sergey Boyko (sergeikuch80@gmail.com)
