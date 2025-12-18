#!/bin/bash

# Script to clone comic repository projects into the src directory
# Date: December 4, 2025

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Get the project root directory (parent of bin)
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
# Define the src directory
SRC_DIR="$PROJECT_ROOT/src"

# GitHub organization
GITHUB_ORG="https://github.com/AI-Enthusiast"

# Array of repositories to clone
REPOS=(
    "explosm-daily"
    "xkcd-daily"
    "exocomics-daily"
    "smbc-daily"
    "poorlydrawnlines-daily"
    "qwantz-daily"
    "thefarside-daily"
    "extrafabulous-daily"
    "safely_endangererd-daily"
)

echo "Starting repository cloning process..."
echo "Target directory: $SRC_DIR"
echo "========================================"

# Create src directory if it doesn't exist
mkdir -p "$SRC_DIR"

# Change to src directory
cd "$SRC_DIR" || exit 1

# Clone each repository
for repo in "${REPOS[@]}"; do
    echo ""
    echo "Processing $repo..."

    # Check if directory already exists
    if [ -d "$repo" ]; then
        echo "  → Directory '$repo' already exists. Pulling latest changes..."
        cd "$repo" || continue
        if git pull; then
            echo "  ✓ Successfully updated $repo"
        else
            echo "  ✗ Failed to update $repo"
        fi
        cd "$SRC_DIR" || exit 1
    else
        # Clone the repository
        if git clone "${GITHUB_ORG}/${repo}.git"; then
            echo "  ✓ Successfully cloned $repo"
        else
            echo "  ✗ Failed to clone $repo"
        fi
    fi
done

echo ""
echo "========================================"
echo "Cloning process completed!"
echo ""
echo "Repositories location: $SRC_DIR"
ls -1 "$SRC_DIR"
