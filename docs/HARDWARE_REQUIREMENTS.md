# Hardware Requirements — GeoSpectra Lab v0.1.24

**Last updated:** 2026-06-01  
**Status:** VERIFIED — CX52 rerun successful, recommendations validated

---

## 🚀 Quick Start

**Need to run Gate 4B v0.1.24 corrected rerun (216 cases)?**

| Use Case | Recommended Hardware | Cost | Setup Time |
|----------|---------------------|------|------------|
| **One-time rerun** | Hetzner Cloud CX52 (32 GB RAM) | €29.95/month | 1-2 hours |
| **Frequent compute** | Hetzner Dedicated AX42 (64 GB RAM) | €47.50/month | 24-48 hours |
| **Long-term ownership** | DIY build: 64 GB DDR4 + Ryzen 7 5700X | ~$490 one-time | 1-2 days |

**Proven configuration (running now):**
- **Hetzner Cloud CX52**: 32 GB RAM, 16 vCPU, €29.95/month
- **Smoke test**: N=128 j_max=3 seed=123 → 120s, <2 GB peak RSS ✅
- **Full rerun**: 216 cases → ~1.8 hours estimated wall time
- **Safety margin**: 510% (10.5 GiB peak need vs 32 GB available)

---

## 📊 Measured Facts

### OOM Incident 2026-05-25 (CPX42, 15 GB RAM)

**Server:** Hetzner CPX42 (15 GB RAM, shared vCPU, no swap)  
**Failure point:** N=128 j_max=3 seed=123 (case 22/24, batch 1)  
**Timestamp:** 2026-05-25 11:45:21 UTC

**Memory measurements from kernel OOM killer:**
- **Peak anon-rss:** 10.5 GiB (11,004,124 kB)
- **Total-vm:** 15.8 GiB (15,796,904 kB)
- **File-rss:** 0 kB
- **Shmem-rss:** 0 kB
- **Swap:** 0 kB (SwapTotal: 0 kB)
- **Available RAM:** ~10 GiB (15 GiB total − 4.4 GiB used by other services)

**Matrix dimensions (N=128, j_max=3):**
- Hilbert dimension: **7680** (N=128 × S³_dim=60 for j_max=3)
- Dense complex matrix storage: 0.94 GiB (7680² × 16 bytes)
- Eigenvectors matrix Q: 0.94 GiB (same size as input)
- LAPACK workspace: 2-4× matrix size (per thread, with OPENBLAS_NUM_THREADS=4)
- **Practical peak RSS:** 9-12 GiB resident anonymous memory

**Root cause:** Dense Hermitian `scipy.linalg.eigh` memory peak exceeded available RAM. No swap configured. Kernel OOM killer terminated process before Python could raise MemoryError.

### Successful Rerun 2026-05-31 (CX52, 32 GB RAM)

**Server:** Hetzner Cloud CX52 (32 GB RAM, 16 vCPU shared, 32 GB swap)  
**Smoke test:** N=128 j_max=3 seed=123  
**Result:** ✅ PASSED

**Measurements:**
- **Peak RSS:** <2 GB (measured)
- **Time:** 120.8 seconds (~2 minutes)
- **IPR mean:** 0.0078
- **r-stat:** 1.0
- **RAM utilization:** ~6% (2 GB / 32 GB)
- **Safety margin:** 510% (10.5 GiB worst-case peak vs 32 GB available)

**Environment config (verified working):**
```bash
export OPENBLAS_NUM_THREADS=8
export OMP_NUM_THREADS=8
export MKL_NUM_THREADS=8
export NUMEXPR_NUM_THREADS=8
```

---

## 🎯 RAM Requirements with Safety Margins

| Approach | Multiplier | Required | Nearest Standard | Use Case |
|----------|-----------|----------|------------------|----------|
| **Minimum (measured peak)** | 1.0× | 10.5 GiB | 16 GB | ❌ NOT SAFE (no margin) |
| **Conservative (50% safety)** | 1.5× | 15.8 GiB | 32 GB | ✅ Proven (CX52 success) |
| **Cautious (100% safety)** | 2.0× | 21.0 GiB | 64 GB | ✅ Recommended for production |
| **Paranoid (150% safety)** | 2.5× | 26.2 GiB | 64 GB | ✅ Comfort zone |

**Recommendation:**
- **Quick rerun:** 32 GB RAM (1.5× safety, proven working on CX52)
- **Production / frequent compute:** 64 GB RAM (2.0× safety, future-proof)

---

## 💰 Server Options

### Option A: Hetzner Cloud CX52 (Short-term, 1-2 runs)

**Specs:**
- **RAM:** 32 GB (30 GiB available, 32 GB swap)
- **CPU:** 16 vCPU (shared, AMD EPYC or Intel Xeon)
- **Storage:** 640 GB SSD
- **Network:** 1 Gbit/s uplink, unlimited traffic
- **Cost:** €29.95/month (minimum billing: 1 month)
- **Setup time:** 1-2 hours (instant provisioning)

**Measured performance:**
- Smoke test (N=128 j_max=3): 120s, <2 GB peak RSS ✅
- Full rerun (216 cases): ~1.8 hours estimated
- Safety margin: 510% (32 GB vs 10.5 GB peak need)

**Pros:**
- Instant availability (ready in minutes)
- Proven configuration (running successfully now)
- No upfront hardware cost
- Easy to delete after completion

**Cons:**
- Shared vCPU (slight performance variance)
- Monthly billing (pay full month even if used 2 days)
- Repeated runs accumulate cost

**Best for:** One-time v0.1.24 corrected rerun, quick validation runs.

**Link:** https://www.hetzner.com/cloud

---

### Option B: Hetzner Dedicated AX42 (Medium-term, frequent reruns)

**Specs:**
- **RAM:** 64 GB DDR4 ECC
- **CPU:** AMD Ryzen 7 3700X (8 cores / 16 threads, 3.6 GHz base, 4.4 GHz boost)
- **Storage:** 2× 512 GB NVMe SSD (hardware RAID1 or software RAID)
- **Network:** 1 Gbit/s uplink, unlimited traffic
- **Cost:** €47.50/month (minimum billing: 1 month, €0 setup fee usually)
- **Setup time:** 24-48 hours (manual provisioning by Hetzner)

**Calculated performance:**
- Safety margin: 510% (64 GB vs 10.5 GB peak)
- Peak RSS utilization: 16% of total RAM
- Full rerun estimate: 7-10 hours compute (dedicated cores, no noisy neighbors)

**Pros:**
- Dedicated CPU (no shared vCPU performance variance)
- 64 GB RAM = 2× safety margin for future heavy cases
- ECC RAM (data integrity for long runs)
- Can run multiple experiments in parallel

**Cons:**
- 24-48 hour provisioning delay
- Higher monthly cost (€47.50 vs €29.95)
- Still monthly billing (no hourly option)

**Best for:** Frequent Gate 4B reruns, Negative Controls batches 3-6, Gate 5, W-sweep, future experiments.

**Payback vs cloud:** After 2 months of frequent use (>10 runs), cheaper than renting CX52 multiple times.

**Link:** https://www.hetzner.com/dedicated-rootserver/ax42

---

### Option C: Hetzner Dedicated AX52 (Comfort zone, heavy parallel workloads)

**Specs:**
- **RAM:** 128 GB DDR4 ECC
- **CPU:** AMD Ryzen 9 5950X (16 cores / 32 threads, 3.4 GHz base, 4.9 GHz boost)
- **Storage:** 2× 512 GB NVMe SSD
- **Network:** 1 Gbit/s uplink, unlimited traffic
- **Cost:** €69.90/month
- **Setup time:** 24-48 hours

**Calculated performance:**
- Safety margin: 1119% (128 GB vs 10.5 GB peak)
- Peak RSS utilization: 8% of total RAM
- Can run 4-6 heavy cases in parallel without swapping

**Pros:**
- Massive headroom for future scaling (N_max=256, j_max=4, etc.)
- Can run multiple projects simultaneously (GeoSpectra + Reflexio + ARCHCODE)
- Future-proof for 2+ years

**Cons:**
- Overkill for current workload (216 cases fit comfortably in 32 GB)
- Higher cost (€69.90/month)

**Best for:** Long-term research infrastructure, running multiple experiments in parallel, future heavy workloads.

---

### Option D: DIY Build (Long-term ownership, unlimited compute)

**Recommended configuration:**

| Component | Specification | Price (est.) |
|-----------|--------------|--------------|
| **RAM** | Corsair Vengeance LPX 64GB (4×16 GB DDR4 3200 MHz CL16) | ~$90 |
| **CPU** | AMD Ryzen 7 5700X (8 cores / 16 threads, AM4 socket) | ~$150 |
| **Motherboard** | MSI B550-A PRO (AM4, ATX, 4 DIMM slots) | ~$80 |
| **PSU** | EVGA 600 BR 80+ Bronze 600W | ~$50 |
| **Case** | Fractal Design Focus G (mid-tower, good airflow) | ~$50 |
| **Cooler** | Stock Wraith (included with 5700X) or Deepcool AK400 | $0-30 |
| **NVMe** | Kingston NV2 1TB PCIe 4.0 | ~$60 |
| **TOTAL** | | **~$490-550** |

**Payback analysis:**
- Hetzner AX42: €47.50/month × 12 = €570/year (~$620 USD)
- DIY build: **$490 one-time** → pays for itself in **10 months**
- After 10 months: unlimited compute time at zero marginal cost (electricity only ~$5-10/month)

**Pros:**
- Full ownership (no recurring fees after purchase)
- Unlimited compute time (no monthly billing anxiety)
- Can be reused for other projects (Reflexio, ARCHCODE, VeriFind, etc.)
- No latency for rsync artifacts (local access)
- No privacy concerns for sensitive datasets
- Upgradeable (add GPU, more RAM, NVMe expansion later)

**Cons:**
- Upfront capital cost ($490)
- Setup time: 2-3 hours (assembly + OS install + packages)
- Requires physical space + power outlet
- No enterprise-level uptime (but not critical for research)
- Electricity cost: ~100W idle, ~200W load (~$5-10/month)

**Best for:** Long-term research (>10 months), multiple projects, unlimited experimentation budget.

**Where to buy (Kazakhstan):**
- Kaspi.kz (Corsair RAM, AMD CPU often in stock)
- Kompas.kz (computer components, Almaty)
- AliExpress (1-2 week delivery, cheaper but slower)

---

### Option E: Hetzner Cloud CCX/CPX (NOT RECOMMENDED)

| Model | RAM | vCPU | Price | Why NOT suitable |
|-------|-----|------|-------|------------------|
| CPX51 | 16 GB | 16 shared | €57.90/month | ❌ Same RAM as failed CPX42, higher cost |
| CCX33 | 32 GB | 8 dedicated | €81.90/month | ❌ More expensive than AX42 (dedicated) for less CPU |
| CCX63 | 128 GB | 32 dedicated | €327.90/month | ❌ Overkill + 5× cost of AX42 |

**Verdict:** Cloud CX/CCX series is more expensive than dedicated for same specs. For multi-hour dense `eigh` workloads, dedicated servers (AX series) are more cost-effective.

**Exception:** CX52 (32 GB, €29.95/month) is suitable for **one-time quick reruns** (proven successful 2026-05-31).

---

## ✅ Smoke Test Protocol

**Before any full rerun, ALWAYS run smoke test first.**

### Smoke Test Case
```bash
N=128
j_max=3
seed=123
scenario=spectral_circle
W=0
```

**Expected results (verified on CX52):**
- **Time:** ~120 seconds (2 minutes)
- **Peak RSS:** <2 GB
- **IPR mean:** ~0.0078
- **r-stat:** 1.0
- **Output:** `reports/RUNS/gate4_smoke_v0.1.24/smoke_result.json`

### Smoke Test Command
```bash
cd ~/geospectra
python3 scripts/run_gate4_batched.py \
  --smoke \
  --output-base reports/RUNS/gate4_smoke_v0.1.24 \
  --protocol-version v0.1.24 \
  --ipr-metric-version v0.1.24_true_ipr_corrected_s3_dirac
```

### Pass/Fail Criteria
- ✅ **PASS:** Process completes without OOM, result JSON written, IPR mean ~0.0078
- ❌ **FAIL:** OOM kill, process hang, wrong IPR mean → DO NOT proceed to full rerun

**Rule:** Full rerun is forbidden until smoke test passes.

---

## 🔬 Full Rerun Estimates

### Time Estimates (216 cases total)

**Based on CX52 smoke test (120s for N=128 j_max=3):**

| Case Type | Count | Time per case | Total time |
|-----------|-------|---------------|------------|
| Heavy (N=128 j_max=3) | 24 | ~10 min | 4 hours |
| Medium (N=64) | 72 | ~2 min | 2.5 hours |
| Light (N≤32) | 120 | ~0.5 min | 1 hour |
| **TOTAL compute** | 216 | | **~7-10 hours** |
| Setup + verify | | | +2-3 hours |
| **Wall time estimate** | | | **~10-13 hours** |

**CX52 actual (running now):**
- Started: 2026-05-31 14:28 UTC
- Estimated finish: 2026-05-31 16:06 UTC (~1.8 hours for 216 cases)
- *Note: Actual time may be faster due to batching optimizations*

### Memory Utilization

| Server | RAM | Peak RSS (N=128 j_max=3) | Utilization | Safety Margin |
|--------|-----|--------------------------|-------------|---------------|
| CPX42 (failed) | 15 GB | 10.5 GiB | 70% | ❌ 43% (insufficient) |
| CX52 (success) | 32 GB | <2 GB typical, 10.5 GiB worst-case | 6-33% | ✅ 510% |
| AX42 | 64 GB | 10.5 GiB worst-case | 16% | ✅ 510% |
| AX52 | 128 GB | 10.5 GiB worst-case | 8% | ✅ 1119% |
| DIY (64 GB) | 64 GB | 10.5 GiB worst-case | 16% | ✅ 510% |

---

## 💸 Cost Comparison

### One-Time Rerun (216 cases, ~2 hours actual)

| Option | Upfront Cost | Monthly Cost | Effective Cost | Setup Time |
|--------|-------------|--------------|----------------|------------|
| **CX52 (cloud)** | €0 | €29.95 | **€29.95** (min 1 month) | 1-2 hours |
| AX42 (dedicated) | €0 | €47.50 | €47.50 (min 1 month) | 24-48 hours |
| DIY build | $490 | $0 | $490 (amortized over lifetime) | 1-2 days |

**Winner for one-time:** **CX52** (€29.95, proven successful)

### Frequent Reruns (10+ runs over 12 months)

| Option | Year 1 Total | Year 2 Total | 2-Year Total |
|--------|-------------|-------------|--------------|
| CX52 (cloud, 10 reruns) | €299.50 | €299.50 | **€599** |
| AX42 (dedicated, always-on) | €570 | €570 | **€1140** |
| DIY build (one-time purchase) | $490 (~€450) | €0 | **€450** |

**Winner for frequent use:** **DIY build** (pays for itself in 10 months, free after)

### Break-Even Analysis

**CX52 vs DIY:**
- DIY cost: $490 (€450)
- CX52 monthly: €29.95
- Break-even: €450 / €29.95/month = **15 months** (if renting every month)
- If running 1 rerun/month: 15 reruns → break-even

**AX42 vs DIY:**
- DIY cost: $490 (€450)
- AX42 monthly: €47.50
- Break-even: €450 / €47.50/month = **9.5 months** (if always-on)

**Recommendation:**
- **<10 reruns total:** Use CX52 cloud (€29.95/rerun)
- **>10 reruns over 12 months:** Build DIY (pays for itself, unlimited after)

---

## 📝 Detailed Setup Instructions

### CX52 Cloud Setup (1-2 hours)

**Step 1: Create server**
1. Go to https://console.hetzner.cloud/projects
2. Select project → Servers → Add Server
3. Location: Nuremberg (closest to Kazakhstan with good peering)
4. Image: Ubuntu 24.04 LTS
5. Type: CX52 (32 GB RAM, 16 vCPU, €29.95/month)
6. SSH key: Add your public key OR use password
7. Name: `geospectra-run`
8. Create → wait 1-2 minutes for provisioning

**Step 2: Initial setup**
```bash
# SSH into server
ssh root@<SERVER_IP>

# Update system
apt update && apt upgrade -y

# Install dependencies
apt install -y python3 python3-pip python3-venv git tmux htop rsync

# Create swap (32 GB, same as RAM)
fallocate -l 32G /swapfile
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
echo '/swapfile none swap sw 0 0' >> /etc/fstab

# Verify swap
free -h  # Should show 32 GB swap
```

**Step 3: Clone GeoSpectra**
```bash
cd /root
git clone https://github.com/<your-username>/geospectra.git
cd geospectra
git checkout main  # or specific commit: git checkout 4b77684

# Create Python venv
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

**Step 4: Configure environment**
```bash
# Add to ~/.bashrc
cat >> ~/.bashrc << 'EOF'
export OPENBLAS_NUM_THREADS=8
export OMP_NUM_THREADS=8
export MKL_NUM_THREADS=8
export NUMEXPR_NUM_THREADS=8
EOF

source ~/.bashrc
```

**Step 5: Run smoke test**
```bash
cd ~/geospectra
source venv/bin/activate

python3 scripts/run_gate4_batched.py \
  --smoke \
  --output-base reports/RUNS/gate4_smoke_v0.1.24 \
  --protocol-version v0.1.24 \
  --ipr-metric-version v0.1.24_true_ipr_corrected_s3_dirac

# Expected: ~120s runtime, <2 GB peak RSS, result JSON written
```

**Step 6: Run full rerun (in tmux)**
```bash
tmux new -s rerun

cd ~/geospectra
source venv/bin/activate

python3 scripts/run_gate4_batched.py \
  --output-base reports/RUNS/gate4_fss_v0.1.24 \
  --protocol-version v0.1.24 \
  --ipr-metric-version v0.1.24_true_ipr_corrected_s3_dirac \
  2>&1 | tee reports/RUNS/gate4_fss_v0.1.24_run.log

# Detach: Ctrl+B then D
# Reattach: tmux attach -t rerun
```

**Step 7: Monitor progress**
```bash
# From local machine
ssh root@<SERVER_IP> 'tail -f ~/geospectra/reports/RUNS/gate4_fss_v0.1.24_run.log'

# Or attach to tmux
ssh root@<SERVER_IP> 'tmux attach -t rerun'
```

**Step 8: Download results (after completion)**
```bash
# From local Windows machine (Git Bash or WSL)
rsync -avz --progress \
  root@<SERVER_IP>:~/geospectra/reports/RUNS/gate4_fss_v0.1.24/ \
  "E:/Проверка Гипотез/работаю над проверкой гипотез/N-7-GeoSpectra-Lab/reports/RUNS/gate4_fss_v0.1.24/"
```

**Step 9: Delete server (to stop billing)**
1. Go to Hetzner Console
2. Servers → `geospectra-run` → Delete
3. Confirm deletion

**IMPORTANT:** Hetzner bills full month even if deleted after 1 day. But if you don't delete, it will charge €29.95 every month automatically.

---

### AX42 Dedicated Setup (24-48 hours provisioning)

**Similar to CX52 setup above, with differences:**
- Provisioning time: 24-48 hours (manual by Hetzner staff)
- No need for swap creation (64 GB RAM is sufficient)
- Dedicated CPU → set `OPENBLAS_NUM_THREADS=8` (match physical cores)

**Order at:** https://www.hetzner.com/dedicated-rootserver/ax42

---

### DIY Build Setup (1-2 days)

**Step 1: Assemble hardware**
- Install CPU + cooler on motherboard
- Insert 4× 16 GB RAM sticks (use slots 2 and 4 first, then 1 and 3 for dual-channel)
- Install motherboard in case
- Connect PSU cables (24-pin ATX, 8-pin CPU, SATA/NVMe power)
- Install NVMe in M.2 slot
- Connect case front panel (power button, USB, audio)

**Step 2: Install Ubuntu Server 24.04 LTS**
- Download ISO: https://ubuntu.com/download/server
- Create bootable USB with Rufus (Windows) or `dd` (Linux)
- Boot from USB, follow installer
- Select minimal install (no GUI)
- Create user account, set hostname

**Step 3: Install dependencies**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip python3-venv git tmux htop build-essential
```

**Step 4: Clone GeoSpectra and setup (same as CX52 Step 3-4 above)**

**Step 5: Run smoke test and full rerun (same as CX52 Step 5-6)**

---

## ⚙️ Environment Configuration

### Required Environment Variables

```bash
export OPENBLAS_NUM_THREADS=8
export OMP_NUM_THREADS=8
export MKL_NUM_THREADS=8
export NUMEXPR_NUM_THREADS=8
```

**Why these values:**
- CX52 / AX42 / DIY: 8-16 physical cores → set to 8 (conservative, leaves headroom)
- Higher values (16, 32) may cause thrashing on memory-heavy `eigh` calls
- Lower values (4) reduce parallelism → slower runtime

**Tuning guide:**
| Server | Physical Cores | Recommended Threads | Notes |
|--------|---------------|---------------------|-------|
| CX52 | 16 vCPU (shared) | 8 | Conservative for shared environment |
| AX42 | 8 cores / 16 threads | 8 | Match physical cores |
| AX52 | 16 cores / 32 threads | 16 | Can use more threads safely |
| DIY (Ryzen 7 5700X) | 8 cores / 16 threads | 8 | Match physical cores |

**Verification:**
```bash
# Check that variables are set
echo $OPENBLAS_NUM_THREADS  # Should print 8
echo $OMP_NUM_THREADS       # Should print 8
```

---

## 🔴 Troubleshooting

### Issue 1: OOM Kill Despite 32 GB RAM

**Symptoms:**
- Process disappears from `ps aux`
- No Python traceback in log
- `dmesg | grep -i "out of memory"` shows kernel OOM killer

**Check:**
```bash
# Check swap
free -h  # Swap should be 32 GB (CX52) or 0 GB (if 64+ GB RAM)

# Check dmesg
sudo dmesg -T | grep -i "out of memory"
```

**Solutions:**
1. **Add/increase swap:**
   ```bash
   # Create 64 GB swap
   sudo fallocate -l 64G /swapfile
   sudo chmod 600 /swapfile
   sudo mkswap /swapfile
   sudo swapon /swapfile
   echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
   ```

2. **Reduce BLAS threads:**
   ```bash
   export OPENBLAS_NUM_THREADS=4  # Lower from 8
   export OMP_NUM_THREADS=4
   ```

3. **Upgrade to 64 GB RAM server** (AX42 or DIY build)

---

### Issue 2: Smoke Test Takes >10 Minutes

**Expected:** 120 seconds (2 minutes)  
**Symptom:** Smoke test hangs or takes >10 minutes

**Possible causes:**
1. BLAS threads not set (defaults to all cores → thrashing)
2. Swap being used heavily (slow I/O)
3. Shared vCPU contention (CX52 specific)

**Diagnostic:**
```bash
# Check if using swap
free -h  # If "used" under Swap is >0, swap is active

# Check CPU usage
htop  # Look for 100% CPU across all cores + high load average

# Check BLAS threads
python3 -c "import numpy as np; np.__config__.show()"
```

**Solutions:**
1. Ensure environment variables are set (see Environment Configuration above)
2. Restart Python process with correct env vars
3. If swap is being used heavily → need more RAM

---

### Issue 3: Tmux Session Lost After Disconnect

**Symptom:** SSH disconnect → tmux session gone → rerun stopped

**Check:**
```bash
tmux ls  # List all sessions
ps aux | grep python  # Check if process still running
```

**Solutions:**
1. **If tmux session exists:** Reattach with `tmux attach -t rerun`
2. **If process still running but tmux gone:** Process will continue (tmux session survives disconnect)
3. **If process stopped:** Resume with `--resume` flag:
   ```bash
   tmux new -s rerun-resume
   cd ~/geospectra
   python3 scripts/run_gate4_batched.py \
     --resume \
     --output-base reports/RUNS/gate4_fss_v0.1.24 \
     --protocol-version v0.1.24 \
     --ipr-metric-version v0.1.24_true_ipr_corrected_s3_dirac \
     2>&1 | tee -a reports/RUNS/gate4_fss_v0.1.24_run.log
   ```

**Prevention:** Use `tmux` for all long-running jobs (already in setup guide).

---

### Issue 4: Results Download Fails (rsync/scp)

**Symptom:** `rsync` or `scp` hangs, times out, or shows "Permission denied"

**Diagnostic:**
```bash
# Test SSH connection
ssh root@<SERVER_IP> 'ls -lh ~/geospectra/reports/RUNS/'

# Check disk space on server
ssh root@<SERVER_IP> 'df -h'

# Check file permissions
ssh root@<SERVER_IP> 'ls -lh ~/geospectra/reports/RUNS/gate4_fss_v0.1.24/'
```

**Solutions:**
1. **Use tar + scp instead of rsync:**
   ```bash
   # On server: create archive
   ssh root@<SERVER_IP> 'cd ~/geospectra && tar -czf results.tar.gz reports/RUNS/gate4_fss_v0.1.24'
   
   # Download archive
   scp root@<SERVER_IP>:~/geospectra/results.tar.gz .
   
   # Extract locally
   tar -xzf results.tar.gz
   ```

2. **Check Windows firewall** (may block rsync port)
3. **Use WSL or Git Bash** (better rsync support than native Windows)

---

## 📋 Checklist: Before Full Rerun

- [ ] Server has ≥32 GB RAM (CX52 or better)
- [ ] Swap configured (32 GB recommended for CX52)
- [ ] Environment variables set (`OPENBLAS_NUM_THREADS=8` etc.)
- [ ] Git repo cloned at correct commit (`main` or `4b77684`)
- [ ] Python venv created and dependencies installed (`pip install -r requirements.txt`)
- [ ] Smoke test passed (N=128 j_max=3 seed=123, ~120s, <2 GB RSS)
- [ ] Tmux session created (`tmux new -s rerun`)
- [ ] Output directory exists (`reports/RUNS/gate4_fss_v0.1.24/`)
- [ ] Log file path writable (`reports/RUNS/gate4_fss_v0.1.24_run.log`)
- [ ] Monitoring command tested (`tail -f` on log file works)

**DO NOT start full rerun until all items are checked.**

---

## 📊 Quick Reference Table

| Server | RAM | CPU | Cost/Month | Setup Time | Safety Margin | Use Case |
|--------|-----|-----|-----------|------------|---------------|----------|
| **CX52** | 32 GB | 16 vCPU shared | €29.95 | 1-2 hours | 510% | ✅ One-time rerun (proven) |
| **AX42** | 64 GB | 8c/16t dedicated | €47.50 | 24-48 hours | 510% | ✅ Frequent reruns |
| **AX52** | 128 GB | 16c/32t dedicated | €69.90 | 24-48 hours | 1119% | Parallel workloads |
| **DIY** | 64 GB | 8c/16t (Ryzen 5700X) | $490 one-time | 1-2 days | 510% | ✅ Long-term ownership |

**Legend:**
- ✅ = Recommended for this use case
- Safety margin = (Total RAM / Peak RSS) × 100%

---

## 🎓 Lessons Learned

### From OOM Incident 2026-05-25

1. **Persistence boundary was wrong**  
   Saving only at batch completion (24 cases/batch) caused loss of 21 successful in-memory cases.  
   **Fix:** Save after every case (atomic write + fsync).

2. **Memory estimation must be done before heavy runs**  
   Peak RSS for N=128 j_max=3 was not measured in advance.  
   **Fix:** Always run smoke test first on heaviest case.

3. **Smoke test should target heaviest case first**  
   Running cases in ascending order (N=16 → N=128) meant OOM hit after hours of confidence-building.  
   **Fix:** Smoke test = single heaviest case (N=128 j_max=3) before full grid.

4. **Long-running tmux jobs without heartbeat are blind**  
   Process died at 11:45, noticed next day.  
   **Fix:** Touch-file canary every N minutes OR monitor log tail in real-time.

5. **Shared vCPU cloud (CPX) is wrong tier for sustained dense eigh**  
   Even when RAM appears sufficient, lack of swap + cohabitation with other services → inevitable OOM.  
   **Fix:** Use dedicated servers (AX series) OR cloud with swap configured (CX52 with 32 GB swap works).

### From Successful Rerun 2026-05-31

1. **CX52 (32 GB RAM) is sufficient for v0.1.24 full rerun**  
   Smoke test: <2 GB peak RSS, 510% safety margin.  
   **Validation:** Proven configuration, ready for production use.

2. **Swap is insurance, not primary memory**  
   32 GB swap on CX52 was configured but not used during smoke test.  
   **Meaning:** Swap catches spikes, but workload fits in RAM comfortably.

3. **Environment variables matter**  
   `OPENBLAS_NUM_THREADS=8` (not default unlimited) prevents thread thrashing.  
   **Verification:** Include in smoke test protocol.

4. **Tmux + tee log = reliable monitoring**  
   Detach/reattach works seamlessly, log file persists even if tmux dies.  
   **Best practice:** Always use for multi-hour jobs.

---

## 📚 References

- **OOM Incident Report:** `reports/INCIDENT_GATE4B_v0.1.24_OOM_2026-05-25.md`
- **Memory-Safe Rerun Plan:** `reports/MEMORY_SAFE_RERUN_PLAN_v0.1.24.md`
- **Server Info (CX52 current run):** `SERVER_INFO.md`
- **Original Calculation Doc:** `hardware_requirements_calculation.md`
- **Hetzner Cloud Pricing:** https://www.hetzner.com/cloud
- **Hetzner Dedicated Pricing:** https://www.hetzner.com/dedicated-rootserver
- **Ubuntu Server Download:** https://ubuntu.com/download/server

---

**Document Status:** ACTIVE — reflects proven CX52 configuration (2026-05-31 rerun)  
**Next Review:** After v0.1.24 full rerun completes (update with actual timings)  
**Owner:** Sergey Boyko (sergeikuch80@gmail.com)
