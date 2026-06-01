#!/usr/bin/env bash
################################################################################
# GeoSpectra Server Bootstrap Script
#
# Provisions a fresh Ubuntu server for memory-safe GeoSpectra v0.1.24 rerun.
# Tested on: Ubuntu 22.04 LTS, Ubuntu 24.04 LTS
# Memory requirement: 32-64 GiB RAM recommended (will create swap if < 64GB)
#
# Exit codes:
#   0 = Server ready for production runs
#   1 = Setup failed (dependencies, repo clone, environment)
#   2 = Smoke test failed (computational verification)
#
# Usage:
#   ./server_bootstrap.sh [BRANCH]
#   Example: ./server_bootstrap.sh feat/memory-safe-rerun
################################################################################

set -euo pipefail  # Exit on error, undefined vars, pipe failures

################################################################################
# Configuration Parameters (override via environment variables)
################################################################################

REPO_URL="${REPO_URL:-https://github.com/sergeeey/N-7-GeoSpectra-Lab.git}"
TARGET_BRANCH="${TARGET_BRANCH:-${1:-main}}"  # First arg or env var or "main"
SWAP_SIZE="${SWAP_SIZE:-32G}"  # Swap size if RAM < 64GB
OPENBLAS_THREADS="${OPENBLAS_NUM_THREADS:-4}"  # Limit BLAS parallelism
PROJECT_DIR="${PROJECT_DIR:-$HOME/GeoSpectra}"
PYTHON_VERSION="3.11"

# Smoke test parameters (minimal resource use)
SMOKE_N=128
SMOKE_J_MAX=3

################################################################################
# Color output helpers
################################################################################

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log_info()  { echo -e "${BLUE}[INFO]${NC} $*"; }
log_ok()    { echo -e "${GREEN}[OK]${NC} $*"; }
log_warn()  { echo -e "${YELLOW}[WARN]${NC} $*"; }
log_error() { echo -e "${RED}[ERROR]${NC} $*" >&2; }

################################################################################
# Step 1: System Packages
################################################################################

install_system_packages() {
    log_info "Installing system packages..."

    sudo apt-get update -qq

    # Core dependencies
    sudo apt-get install -y \
        python${PYTHON_VERSION} \
        python${PYTHON_VERSION}-venv \
        python${PYTHON_VERSION}-dev \
        build-essential \
        git \
        tmux \
        htop \
        curl \
        wget \
        libopenblas-dev \
        liblapack-dev \
        gfortran \
        || { log_error "Failed to install system packages"; return 1; }

    log_ok "System packages installed"
}

################################################################################
# Step 2: Memory Check & Swap Creation
################################################################################

setup_swap() {
    log_info "Checking system memory..."

    # Get total RAM in GB
    total_ram_gb=$(free -g | awk '/^Mem:/{print $2}')
    log_info "Detected ${total_ram_gb}GB RAM"

    if [ "$total_ram_gb" -lt 64 ]; then
        log_warn "RAM < 64GB detected. Creating ${SWAP_SIZE} swap file..."

        # Check if swap already exists
        if [ -f /swapfile ]; then
            log_warn "Swap file already exists, skipping creation"
            sudo swapon /swapfile || true
        else
            # Create swap
            sudo fallocate -l "$SWAP_SIZE" /swapfile || \
                { log_error "Failed to allocate swap file"; return 1; }

            sudo chmod 600 /swapfile
            sudo mkswap /swapfile
            sudo swapon /swapfile

            # Make permanent
            if ! grep -q '/swapfile' /etc/fstab; then
                echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
            fi

            log_ok "Swap ${SWAP_SIZE} created and enabled"
        fi
    else
        log_ok "RAM ≥ 64GB, no swap needed"
    fi

    # Display memory status
    free -h
}

################################################################################
# Step 3: Clone Repository
################################################################################

clone_repository() {
    log_info "Cloning GeoSpectra repository..."

    if [ -d "$PROJECT_DIR" ]; then
        log_warn "Directory $PROJECT_DIR already exists"

        # Check if it's our repo
        if [ -d "$PROJECT_DIR/.git" ]; then
            log_info "Updating existing repository..."
            cd "$PROJECT_DIR"
            git fetch origin
            git checkout "$TARGET_BRANCH"
            git pull origin "$TARGET_BRANCH"
            log_ok "Repository updated to branch: $TARGET_BRANCH"
        else
            log_error "$PROJECT_DIR exists but is not a git repository"
            return 1
        fi
    else
        # Fresh clone
        git clone "$REPO_URL" "$PROJECT_DIR" || \
            { log_error "Failed to clone repository"; return 1; }

        cd "$PROJECT_DIR"
        git checkout "$TARGET_BRANCH"
        log_ok "Repository cloned, branch: $TARGET_BRANCH"
    fi

    # Display commit info
    log_info "Current commit: $(git rev-parse --short HEAD)"
    git log -1 --oneline
}

################################################################################
# Step 4: Python Environment Setup
################################################################################

setup_python_env() {
    log_info "Setting up Python ${PYTHON_VERSION} environment..."

    cd "$PROJECT_DIR"

    # Create virtual environment
    if [ ! -d "venv" ]; then
        python${PYTHON_VERSION} -m venv venv || \
            { log_error "Failed to create virtual environment"; return 1; }
        log_ok "Virtual environment created"
    else
        log_warn "Virtual environment already exists"
    fi

    # Activate venv
    source venv/bin/activate

    # Upgrade pip
    pip install --upgrade pip setuptools wheel || \
        { log_error "Failed to upgrade pip"; return 1; }

    # Install dependencies
    if [ -f "requirements.txt" ]; then
        log_info "Installing Python dependencies from requirements.txt..."
        pip install -r requirements.txt || \
            { log_error "Failed to install Python dependencies"; return 1; }
        log_ok "Python dependencies installed"
    else
        log_warn "No requirements.txt found, installing minimal deps..."
        pip install numpy scipy matplotlib scikit-learn pytest || \
            { log_error "Failed to install minimal dependencies"; return 1; }
    fi

    # Verify key packages
    python -c "import numpy, scipy, sklearn; print(f'numpy {numpy.__version__}, scipy {scipy.__version__}')"
}

################################################################################
# Step 5: Environment Variables Configuration
################################################################################

setup_environment() {
    log_info "Configuring environment variables..."

    # Create .env file
    cat > "$PROJECT_DIR/.env" <<EOF
# GeoSpectra Environment Configuration
# Generated by server_bootstrap.sh on $(date)

# BLAS threading (prevent memory explosion)
OPENBLAS_NUM_THREADS=${OPENBLAS_THREADS}
MKL_NUM_THREADS=${OPENBLAS_THREADS}
NUMEXPR_NUM_THREADS=${OPENBLAS_THREADS}
OMP_NUM_THREADS=${OPENBLAS_THREADS}

# Python optimization
PYTHONUNBUFFERED=1
PYTHONHASHSEED=0

# Project paths
PROJECT_ROOT=${PROJECT_DIR}
EOF

    # Source environment
    export OPENBLAS_NUM_THREADS="$OPENBLAS_THREADS"
    export MKL_NUM_THREADS="$OPENBLAS_THREADS"
    export NUMEXPR_NUM_THREADS="$OPENBLAS_THREADS"
    export OMP_NUM_THREADS="$OPENBLAS_THREADS"

    log_ok "Environment configured: OPENBLAS_NUM_THREADS=$OPENBLAS_THREADS"

    # Add to .bashrc for persistence
    if ! grep -q "GeoSpectra environment" "$HOME/.bashrc"; then
        cat >> "$HOME/.bashrc" <<EOF

# GeoSpectra environment
if [ -f ${PROJECT_DIR}/.env ]; then
    source ${PROJECT_DIR}/.env
fi
EOF
        log_ok "Environment variables added to ~/.bashrc"
    fi
}

################################################################################
# Step 6: Smoke Test (Critical Verification)
################################################################################

run_smoke_test() {
    log_info "Running smoke test (N=$SMOKE_N, j_max=$SMOKE_J_MAX)..."

    cd "$PROJECT_DIR"
    source venv/bin/activate

    # Find the main script (adjust path as needed)
    if [ -f "src/geospectra/main.py" ]; then
        MAIN_SCRIPT="src/geospectra/main.py"
    elif [ -f "geospectra/main.py" ]; then
        MAIN_SCRIPT="geospectra/main.py"
    elif [ -f "main.py" ]; then
        MAIN_SCRIPT="main.py"
    else
        log_error "Cannot find main script (main.py). Check repository structure."
        return 2
    fi

    log_info "Executing: python $MAIN_SCRIPT --N=$SMOKE_N --j_max=$SMOKE_J_MAX --smoke-test"

    # Run minimal test case
    python "$MAIN_SCRIPT" --N="$SMOKE_N" --j_max="$SMOKE_J_MAX" --smoke-test 2>&1 | tee smoke_test.log || \
        { log_error "Smoke test failed. Check smoke_test.log"; return 2; }

    # Check for success indicators in output
    if grep -q "SUCCESS\|COMPLETE\|PASS" smoke_test.log || [ ${PIPESTATUS[0]} -eq 0 ]; then
        log_ok "Smoke test PASSED"
        return 0
    else
        log_error "Smoke test produced unexpected output"
        return 2
    fi
}

################################################################################
# Step 7: Post-Setup Information
################################################################################

print_completion_info() {
    log_ok "========================================="
    log_ok "GeoSpectra Server Bootstrap COMPLETE"
    log_ok "========================================="
    echo
    log_info "Project directory: $PROJECT_DIR"
    log_info "Branch: $TARGET_BRANCH"
    log_info "Python venv: $PROJECT_DIR/venv"
    log_info "Environment: $PROJECT_DIR/.env"
    echo
    log_info "To start working:"
    echo "  cd $PROJECT_DIR"
    echo "  source venv/bin/activate"
    echo "  source .env"
    echo
    log_info "To run production job:"
    echo "  python <main_script> --N=4096 --j_max=40 --output=results/"
    echo
    log_info "Memory monitoring:"
    echo "  htop           # Interactive process viewer"
    echo "  free -h        # Memory usage"
    echo "  tmux           # Session manager for long runs"
    echo
    log_ok "Server is READY for GeoSpectra v0.1.24 rerun"
}

################################################################################
# Main Execution Flow
################################################################################

main() {
    log_info "Starting GeoSpectra server bootstrap..."
    log_info "Repository: $REPO_URL"
    log_info "Branch: $TARGET_BRANCH"
    log_info "Target directory: $PROJECT_DIR"
    echo

    # Execute setup steps
    install_system_packages || exit 1
    setup_swap || exit 1
    clone_repository || exit 1
    setup_python_env || exit 1
    setup_environment || exit 1

    # Critical verification
    run_smoke_test || exit 2

    # Success
    print_completion_info
    exit 0
}

# Execute main function
main "$@"
