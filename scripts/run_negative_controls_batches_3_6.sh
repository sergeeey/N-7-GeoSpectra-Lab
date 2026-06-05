#!/bin/bash
# Run Negative Controls batches 3-6 (v0.1.22) on Hetzner server
# ONLY run this AFTER Gate 4B v0.1.24 verdict = SIGNAL_PRESERVED

SERVER="<user>@<hetzner-server-ip>"

echo "=== Negative Controls batches 3-6 launcher ==="
echo ""
echo "⚠️  WARNING: Only run this if Gate 4B v0.1.24 verdict = SIGNAL_PRESERVED"
echo ""
read -p "Have you verified v0.1.24 signal is PRESERVED? (yes/no): " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
    echo "Cancelled. Run comparison report first."
    exit 1
fi

echo ""
echo "Launching Negative Controls batches 3-6 on $SERVER..."
echo ""

ssh "$SERVER" 'bash -s' << 'ENDSSH'
cd ~/geospectra

# Check if v0.1.24 rerun completed
if [ ! -d "reports/RUNS/gate4_fss_v0.1.24/batches/batch_09" ]; then
    echo "❌ ERROR: v0.1.24 batch 9 not found. Rerun not complete?"
    exit 1
fi

echo "✅ v0.1.24 rerun verified complete"
echo ""

# Setup environment
export OPENBLAS_NUM_THREADS=8
export OMP_NUM_THREADS=8
export MKL_NUM_THREADS=8

echo "=== Starting Negative Controls batches 3-6 ==="
echo "Output: reports/RUNS/negative_controls_v0.1.22/"
echo "Batches: 3, 4, 5, 6 (36 cases total)"
echo "Estimated time: ~6 hours"
echo ""

# Start in tmux
tmux new-session -d -s negative_controls 'bash -c "
cd ~/geospectra
export OPENBLAS_NUM_THREADS=8
export OMP_NUM_THREADS=8

# Run batches 3-6
for BATCH_ID in 3 4 5 6; do
    echo \"\"
    echo \"=== Starting batch \$BATCH_ID ===\"
    python3 scripts/run_negative_controls_batched.py \
        --batch-id \$BATCH_ID \
        --output-base reports/RUNS/negative_controls_v0.1.22 \
        2>&1 | tee -a reports/RUNS/negative_controls_v0.1.22_batches_3_6.log

    if [ \$? -ne 0 ]; then
        echo \"❌ Batch \$BATCH_ID failed, stopping\"
        exit 1
    fi
done

echo \"\"
echo \"✅ All batches 3-6 completed\"
"'

echo "✅ Negative Controls launched in tmux session 'negative_controls'"
echo ""
echo "Monitor with:"
echo "  ssh $SERVER 'tmux attach -t negative_controls'"
echo "  ssh $SERVER 'tail -f ~/geospectra/reports/RUNS/negative_controls_v0.1.22_batches_3_6.log'"
ENDSSH

echo ""
echo "Done. Check progress in ~30 minutes."
