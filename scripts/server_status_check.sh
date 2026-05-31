#!/bin/bash
# Quick server status check for Gate 4B v0.1.24 rerun

SERVER="root@46.224.28.128"

echo "=== Server Status Check ==="
echo "Server: $SERVER"
echo "Time: $(date)"
echo ""

ssh "$SERVER" 'bash -s' << 'ENDSSH'
echo "=== GATE 4B V0.1.24 RERUN STATUS ==="
echo ""

# Tmux sessions
echo "Tmux sessions:"
tmux ls 2>&1 || echo "No tmux sessions"
echo ""

# Python processes
echo "Python processes:"
ps aux | grep "python.*run_gate4" | grep -v grep || echo "No rerun processes"
echo ""

# Memory usage
echo "Memory:"
free -h | grep -E "Mem|Swap"
echo ""

# CPU load
echo "CPU load:"
uptime
echo ""

# Last 5 lines of log
echo "Last 5 log lines:"
if [ -f ~/geospectra/reports/RUNS/gate4_fss_v0.1.24_run.log ]; then
    tail -5 ~/geospectra/reports/RUNS/gate4_fss_v0.1.24_run.log
else
    echo "Log not found"
fi
echo ""

# Completed batches
echo "Completed batches:"
if [ -d ~/geospectra/reports/RUNS/gate4_fss_v0.1.24/batches ]; then
    ls ~/geospectra/reports/RUNS/gate4_fss_v0.1.24/batches/ | wc -l
    echo "out of 9"
else
    echo "0 (batches/ directory not created yet)"
fi
echo ""

# Disk usage
echo "Disk usage:"
df -h / | grep -E "Filesystem|/$"

ENDSSH

echo ""
echo "=== Check complete ==="
