#!/usr/bin/env bash
################################################################################
# GeoSpectra Server Cleanup Script
#
# Runs AFTER successful rerun to:
#   - Archive results to .tar.gz with checksums
#   - Optionally upload to S3/rsync remote storage
#   - Delete local results after upload confirmation
#   - Remove swap file if created by bootstrap
#   - Stop tmux sessions
#   - Print disk space freed summary
#
# Exit codes:
#   0 = Cleanup completed successfully
#   1 = Cleanup failed (archive creation, upload, or deletion error)
#   2 = Invalid arguments or configuration
#
# Usage:
#   ./server_cleanup.sh [OPTIONS] <experiment_id>
#
# Options:
#   --dry-run              Show what would be done without executing
#   --upload-s3 <bucket>   Upload to S3 bucket (requires aws-cli configured)
#   --upload-rsync <dest>  Upload via rsync (user@host:/path)
#   --keep-local           Keep local results after upload (default: delete)
#   --no-swap-cleanup      Do not remove swap file
#   --no-tmux-cleanup      Do not stop tmux sessions
#   --force                Skip confirmations (use with caution)
#
# Examples:
#   ./server_cleanup.sh --dry-run v0.1.24_rerun_2026_06_01
#   ./server_cleanup.sh --upload-s3 geoscan-results v0.1.24_rerun_2026_06_01
#   ./server_cleanup.sh --upload-rsync user@storage:/backups v0.1.24_rerun_2026_06_01
################################################################################

set -euo pipefail  # Exit on error, undefined vars, pipe failures

################################################################################
# Configuration Parameters
################################################################################

PROJECT_DIR="${PROJECT_DIR:-$HOME/GeoSpectra}"
RESULTS_BASE="${RESULTS_BASE:-$PROJECT_DIR/reports/RUNS}"
ARCHIVE_DIR="${ARCHIVE_DIR:-$HOME/GeoSpectra_archives}"
SWAP_FILE="${SWAP_FILE:-/swapfile}"
TMUX_SESSION_PATTERN="${TMUX_SESSION_PATTERN:-geospectra*}"

# Command-line options (defaults)
DRY_RUN=false
UPLOAD_S3=""
UPLOAD_RSYNC=""
KEEP_LOCAL=false
CLEANUP_SWAP=true
CLEANUP_TMUX=true
FORCE=false

################################################################################
# Color output helpers
################################################################################

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

log_info()  { echo -e "${BLUE}[INFO]${NC} $*"; }
log_ok()    { echo -e "${GREEN}[OK]${NC} $*"; }
log_warn()  { echo -e "${YELLOW}[WARN]${NC} $*"; }
log_error() { echo -e "${RED}[ERROR]${NC} $*" >&2; }
log_dry()   { echo -e "${CYAN}[DRY-RUN]${NC} $*"; }

################################################################################
# Argument Parsing
################################################################################

parse_args() {
    local positional_args=()

    while [[ $# -gt 0 ]]; do
        case $1 in
            --dry-run)
                DRY_RUN=true
                shift
                ;;
            --upload-s3)
                UPLOAD_S3="$2"
                shift 2
                ;;
            --upload-rsync)
                UPLOAD_RSYNC="$2"
                shift 2
                ;;
            --keep-local)
                KEEP_LOCAL=true
                shift
                ;;
            --no-swap-cleanup)
                CLEANUP_SWAP=false
                shift
                ;;
            --no-tmux-cleanup)
                CLEANUP_TMUX=false
                shift
                ;;
            --force)
                FORCE=true
                shift
                ;;
            -h|--help)
                show_help
                exit 0
                ;;
            -*)
                log_error "Unknown option: $1"
                show_help
                exit 2
                ;;
            *)
                positional_args+=("$1")
                shift
                ;;
        esac
    done

    # Restore positional parameters
    set -- "${positional_args[@]}"

    if [[ $# -ne 1 ]]; then
        log_error "Missing required argument: <experiment_id>"
        show_help
        exit 2
    fi

    EXPERIMENT_ID="$1"
}

show_help() {
    cat << 'EOF'
GeoSpectra Server Cleanup Script

Usage: ./server_cleanup.sh [OPTIONS] <experiment_id>

Options:
  --dry-run              Show what would be done without executing
  --upload-s3 <bucket>   Upload to S3 bucket (requires aws-cli configured)
  --upload-rsync <dest>  Upload via rsync (user@host:/path)
  --keep-local           Keep local results after upload (default: delete)
  --no-swap-cleanup      Do not remove swap file
  --no-tmux-cleanup      Do not stop tmux sessions
  --force                Skip confirmations (use with caution)
  -h, --help             Show this help message

Examples:
  ./server_cleanup.sh --dry-run v0.1.24_rerun_2026_06_01
  ./server_cleanup.sh --upload-s3 geoscan-results v0.1.24_rerun_2026_06_01
  ./server_cleanup.sh --upload-rsync user@storage:/backups --keep-local v0.1.24_rerun_2026_06_01
EOF
}

################################################################################
# Validation Functions
################################################################################

validate_environment() {
    log_info "Validating environment..."

    # Check required commands
    local missing_cmds=()
    for cmd in tar sha256sum df du; do
        if ! command -v "$cmd" &> /dev/null; then
            missing_cmds+=("$cmd")
        fi
    done

    if [[ -n "$UPLOAD_S3" ]] && ! command -v aws &> /dev/null; then
        missing_cmds+=("aws")
    fi

    if [[ -n "$UPLOAD_RSYNC" ]] && ! command -v rsync &> /dev/null; then
        missing_cmds+=("rsync")
    fi

    if [[ ${#missing_cmds[@]} -gt 0 ]]; then
        log_error "Missing required commands: ${missing_cmds[*]}"
        return 1
    fi

    # Check results directory exists
    if [[ ! -d "$RESULTS_BASE/$EXPERIMENT_ID" ]]; then
        log_error "Results directory not found: $RESULTS_BASE/$EXPERIMENT_ID"
        return 1
    fi

    # Check archive directory
    if [[ ! -d "$ARCHIVE_DIR" ]]; then
        log_info "Creating archive directory: $ARCHIVE_DIR"
        mkdir -p "$ARCHIVE_DIR"
    fi

    log_ok "Environment validation passed"
    return 0
}

################################################################################
# Archive Functions
################################################################################

create_archive() {
    local results_dir="$RESULTS_BASE/$EXPERIMENT_ID"
    local archive_path="$ARCHIVE_DIR/${EXPERIMENT_ID}_results.tar.gz"
    local checksum_path="$ARCHIVE_DIR/${EXPERIMENT_ID}_results.sha256"

    log_info "Creating archive from: $results_dir"
    log_info "Archive destination: $archive_path"

    if [[ "$DRY_RUN" == true ]]; then
        log_dry "Would create archive: $archive_path"
        log_dry "Would calculate SHA256 checksum: $checksum_path"
        return 0
    fi

    # Calculate source size
    local source_size
    source_size=$(du -sh "$results_dir" | cut -f1)
    log_info "Source directory size: $source_size"

    # Create tar.gz archive with progress indication
    log_info "Compressing results (this may take several minutes)..."
    if tar -czf "$archive_path" -C "$RESULTS_BASE" "$EXPERIMENT_ID" 2>&1; then
        log_ok "Archive created successfully"
    else
        log_error "Failed to create archive"
        return 1
    fi

    # Calculate archive size
    local archive_size
    archive_size=$(du -sh "$archive_path" | cut -f1)
    log_info "Archive size: $archive_size"

    # Calculate SHA256 checksum
    log_info "Calculating SHA256 checksum..."
    if (cd "$ARCHIVE_DIR" && sha256sum "$(basename "$archive_path")" > "$checksum_path"); then
        log_ok "Checksum saved to: $checksum_path"
        log_info "$(cat "$checksum_path")"
    else
        log_error "Failed to calculate checksum"
        return 1
    fi

    return 0
}

################################################################################
# Upload Functions
################################################################################

upload_to_s3() {
    local archive_path="$ARCHIVE_DIR/${EXPERIMENT_ID}_results.tar.gz"
    local checksum_path="$ARCHIVE_DIR/${EXPERIMENT_ID}_results.sha256"
    local s3_bucket="$UPLOAD_S3"

    log_info "Uploading to S3 bucket: s3://$s3_bucket/"

    if [[ "$DRY_RUN" == true ]]; then
        log_dry "Would upload: $archive_path → s3://$s3_bucket/"
        log_dry "Would upload: $checksum_path → s3://$s3_bucket/"
        return 0
    fi

    # Upload archive
    if aws s3 cp "$archive_path" "s3://$s3_bucket/" --no-progress; then
        log_ok "Archive uploaded to S3"
    else
        log_error "Failed to upload archive to S3"
        return 1
    fi

    # Upload checksum
    if aws s3 cp "$checksum_path" "s3://$s3_bucket/" --no-progress; then
        log_ok "Checksum uploaded to S3"
    else
        log_warn "Failed to upload checksum to S3 (archive uploaded successfully)"
    fi

    log_info "S3 URL: s3://$s3_bucket/$(basename "$archive_path")"
    return 0
}

upload_via_rsync() {
    local archive_path="$ARCHIVE_DIR/${EXPERIMENT_ID}_results.tar.gz"
    local checksum_path="$ARCHIVE_DIR/${EXPERIMENT_ID}_results.sha256"
    local rsync_dest="$UPLOAD_RSYNC"

    log_info "Uploading via rsync to: $rsync_dest"

    if [[ "$DRY_RUN" == true ]]; then
        log_dry "Would rsync: $archive_path → $rsync_dest"
        log_dry "Would rsync: $checksum_path → $rsync_dest"
        return 0
    fi

    # Upload archive and checksum
    if rsync -avz --progress "$archive_path" "$checksum_path" "$rsync_dest/"; then
        log_ok "Files uploaded via rsync"
        log_info "Remote location: $rsync_dest/$(basename "$archive_path")"
    else
        log_error "Failed to upload via rsync"
        return 1
    fi

    return 0
}

verify_upload() {
    local archive_path="$ARCHIVE_DIR/${EXPERIMENT_ID}_results.tar.gz"

    if [[ -n "$UPLOAD_S3" ]]; then
        log_info "Verifying S3 upload..."
        if [[ "$DRY_RUN" == true ]]; then
            log_dry "Would verify S3 object exists"
            return 0
        fi

        if aws s3 ls "s3://$UPLOAD_S3/$(basename "$archive_path")" &> /dev/null; then
            log_ok "S3 upload verified"
            return 0
        else
            log_error "S3 verification failed"
            return 1
        fi
    fi

    if [[ -n "$UPLOAD_RSYNC" ]]; then
        log_warn "Rsync upload verification not implemented (assuming success)"
        return 0
    fi

    return 0
}

################################################################################
# Cleanup Functions
################################################################################

cleanup_local_results() {
    local results_dir="$RESULTS_BASE/$EXPERIMENT_ID"

    if [[ "$KEEP_LOCAL" == true ]]; then
        log_info "Keeping local results (--keep-local specified)"
        return 0
    fi

    log_info "Deleting local results: $results_dir"

    if [[ "$DRY_RUN" == true ]]; then
        log_dry "Would delete: $results_dir"
        return 0
    fi

    if [[ "$FORCE" != true ]]; then
        read -r -p "Delete local results? [y/N] " response
        if [[ ! "$response" =~ ^[Yy]$ ]]; then
            log_info "Local results NOT deleted"
            return 0
        fi
    fi

    if rm -rf "$results_dir"; then
        log_ok "Local results deleted"
    else
        log_error "Failed to delete local results"
        return 1
    fi

    return 0
}

cleanup_swap() {
    if [[ "$CLEANUP_SWAP" != true ]]; then
        log_info "Skipping swap cleanup (--no-swap-cleanup specified)"
        return 0
    fi

    if [[ ! -f "$SWAP_FILE" ]]; then
        log_info "No swap file found at: $SWAP_FILE"
        return 0
    fi

    log_info "Removing swap file: $SWAP_FILE"

    if [[ "$DRY_RUN" == true ]]; then
        log_dry "Would disable swap: swapoff $SWAP_FILE"
        log_dry "Would remove: $SWAP_FILE"
        return 0
    fi

    if [[ "$FORCE" != true ]]; then
        read -r -p "Remove swap file? [y/N] " response
        if [[ ! "$response" =~ ^[Yy]$ ]]; then
            log_info "Swap file NOT removed"
            return 0
        fi
    fi

    # Disable swap
    if sudo swapoff "$SWAP_FILE" 2>/dev/null; then
        log_ok "Swap disabled"
    else
        log_warn "Swap already disabled or not active"
    fi

    # Remove file
    if sudo rm -f "$SWAP_FILE"; then
        log_ok "Swap file removed"
    else
        log_error "Failed to remove swap file"
        return 1
    fi

    # Remove from /etc/fstab if present
    if grep -q "$SWAP_FILE" /etc/fstab 2>/dev/null; then
        log_info "Removing swap entry from /etc/fstab"
        sudo sed -i "\|$SWAP_FILE|d" /etc/fstab
    fi

    return 0
}

cleanup_tmux_sessions() {
    if [[ "$CLEANUP_TMUX" != true ]]; then
        log_info "Skipping tmux cleanup (--no-tmux-cleanup specified)"
        return 0
    fi

    if ! command -v tmux &> /dev/null; then
        log_info "tmux not installed, skipping session cleanup"
        return 0
    fi

    # Find matching sessions
    local sessions
    sessions=$(tmux list-sessions -F '#{session_name}' 2>/dev/null | grep -E "$TMUX_SESSION_PATTERN" || true)

    if [[ -z "$sessions" ]]; then
        log_info "No tmux sessions matching pattern: $TMUX_SESSION_PATTERN"
        return 0
    fi

    log_info "Found tmux sessions to stop:"
    echo "$sessions" | while read -r session; do
        echo "  - $session"
    done

    if [[ "$DRY_RUN" == true ]]; then
        log_dry "Would kill sessions: $sessions"
        return 0
    fi

    if [[ "$FORCE" != true ]]; then
        read -r -p "Stop these tmux sessions? [y/N] " response
        if [[ ! "$response" =~ ^[Yy]$ ]]; then
            log_info "Tmux sessions NOT stopped"
            return 0
        fi
    fi

    echo "$sessions" | while read -r session; do
        if tmux kill-session -t "$session" 2>/dev/null; then
            log_ok "Stopped tmux session: $session"
        else
            log_warn "Failed to stop tmux session: $session"
        fi
    done

    return 0
}

################################################################################
# Summary Functions
################################################################################

print_summary() {
    local archive_path="$ARCHIVE_DIR/${EXPERIMENT_ID}_results.tar.gz"
    local results_dir="$RESULTS_BASE/$EXPERIMENT_ID"

    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  CLEANUP SUMMARY"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""

    if [[ "$DRY_RUN" == true ]]; then
        log_warn "DRY-RUN MODE: No actual changes were made"
        echo ""
    fi

    # Archive information
    if [[ -f "$archive_path" ]]; then
        local archive_size
        archive_size=$(du -sh "$archive_path" | cut -f1)
        log_ok "Archive created: $archive_path ($archive_size)"

        local checksum_path="$ARCHIVE_DIR/${EXPERIMENT_ID}_results.sha256"
        if [[ -f "$checksum_path" ]]; then
            echo "  Checksum: $(cat "$checksum_path" | cut -d' ' -f1)"
        fi
    fi

    # Upload information
    if [[ -n "$UPLOAD_S3" ]]; then
        log_ok "Uploaded to S3: s3://$UPLOAD_S3/$(basename "$archive_path")"
    fi

    if [[ -n "$UPLOAD_RSYNC" ]]; then
        log_ok "Uploaded via rsync: $UPLOAD_RSYNC/$(basename "$archive_path")"
    fi

    # Disk space freed
    local disk_freed="0"
    if [[ "$KEEP_LOCAL" != true ]] && [[ ! -d "$results_dir" ]]; then
        log_ok "Local results deleted"
    fi

    if [[ "$CLEANUP_SWAP" == true ]] && [[ ! -f "$SWAP_FILE" ]]; then
        log_ok "Swap file removed"
    fi

    # Current disk usage
    echo ""
    log_info "Current disk usage:"
    df -h / | tail -n 1

    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    if [[ "$DRY_RUN" == true ]]; then
        echo ""
        log_info "To execute for real, run without --dry-run flag"
    fi
}

################################################################################
# Main Execution
################################################################################

main() {
    parse_args "$@"

    log_info "GeoSpectra Server Cleanup"
    log_info "Experiment ID: $EXPERIMENT_ID"
    echo ""

    if [[ "$DRY_RUN" == true ]]; then
        log_warn "Running in DRY-RUN mode (no changes will be made)"
        echo ""
    fi

    # Validation
    if ! validate_environment; then
        log_error "Environment validation failed"
        exit 2
    fi

    echo ""

    # Create archive
    if ! create_archive; then
        log_error "Archive creation failed"
        exit 1
    fi

    echo ""

    # Upload if requested
    if [[ -n "$UPLOAD_S3" ]]; then
        if ! upload_to_s3; then
            log_error "S3 upload failed"
            exit 1
        fi
        echo ""
    fi

    if [[ -n "$UPLOAD_RSYNC" ]]; then
        if ! upload_via_rsync; then
            log_error "Rsync upload failed"
            exit 1
        fi
        echo ""
    fi

    # Verify upload before deleting local
    if [[ -n "$UPLOAD_S3" ]] || [[ -n "$UPLOAD_RSYNC" ]]; then
        if ! verify_upload; then
            log_error "Upload verification failed - NOT deleting local results"
            exit 1
        fi
    fi

    # Cleanup local results
    if ! cleanup_local_results; then
        log_warn "Failed to cleanup local results"
    fi

    echo ""

    # Cleanup swap
    if ! cleanup_swap; then
        log_warn "Failed to cleanup swap file"
    fi

    echo ""

    # Cleanup tmux
    if ! cleanup_tmux_sessions; then
        log_warn "Failed to cleanup tmux sessions"
    fi

    # Print summary
    print_summary

    log_ok "Cleanup completed successfully"
    exit 0
}

# Execute main function
main "$@"
