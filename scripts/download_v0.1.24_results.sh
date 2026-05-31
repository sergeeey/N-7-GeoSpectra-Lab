#!/bin/bash
# Download Gate 4B v0.1.24 results from Hetzner CX52

SERVER="root@46.224.28.128"
REMOTE_PATH="~/geospectra/reports/RUNS/gate4_fss_v0.1.24"
LOCAL_PATH="reports/RUNS/gate4_fss_v0.1.24"

echo "=== Downloading Gate 4B v0.1.24 results ==="
echo "Server: $SERVER"
echo "Remote: $REMOTE_PATH"
echo "Local: $LOCAL_PATH"
echo ""

# Create local directory
mkdir -p "$LOCAL_PATH"

# Option 1: rsync (preferred - resumable)
echo "Method 1: rsync (trying...)"
rsync -avz --progress "$SERVER:$REMOTE_PATH/" "$LOCAL_PATH/" 2>&1

if [ $? -ne 0 ]; then
    echo ""
    echo "rsync failed, trying tar method..."
    echo ""

    # Option 2: tar + scp (fallback)
    echo "Method 2: tar + scp"

    # Create archive on server
    ssh "$SERVER" "cd ~/geospectra && tar -czf gate4_v0.1.24_results.tar.gz reports/RUNS/gate4_fss_v0.1.24"

    # Download archive
    scp "$SERVER:~/geospectra/gate4_v0.1.24_results.tar.gz" .

    # Extract
    tar -xzf gate4_v0.1.24_results.tar.gz

    # Cleanup
    rm gate4_v0.1.24_results.tar.gz
    ssh "$SERVER" "rm ~/geospectra/gate4_v0.1.24_results.tar.gz"
fi

echo ""
echo "=== Verifying download ==="
BATCH_COUNT=$(find "$LOCAL_PATH/batches" -name "results.json" 2>/dev/null | wc -l)
echo "Batches downloaded: $BATCH_COUNT / 9"

if [ "$BATCH_COUNT" -eq 9 ]; then
    echo "✅ All 9 batches downloaded successfully!"
    echo ""
    echo "Next steps:"
    echo "  1. Run comparison report: python scripts/compare_v0.1.21_vs_v0.1.24.py"
    echo "  2. Commit results: git add reports/RUNS/gate4_fss_v0.1.24/"
    echo "  3. Delete server: Hetzner Console -> geospectra-run -> Delete"
else
    echo "⚠️  Warning: Expected 9 batches, got $BATCH_COUNT"
    echo "Check server: ssh $SERVER 'ls ~/geospectra/reports/RUNS/gate4_fss_v0.1.24/batches/'"
fi
