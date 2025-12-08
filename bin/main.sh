#!/bin/bash

# Main script to initialize and update comic repositories
# Date: December 4, 2025

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Get the project root directory (parent of bin)
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "========================================"
echo "Comics Daily - Main Script"
echo "========================================"
echo "Project root: $PROJECT_ROOT"
echo ""

# Step 1: Initialize/Clone repositories
echo "========================================"
echo "Step 1: Initializing repositories..."
echo "========================================"
"$SCRIPT_DIR/init_pull.sh"

if [ $? -ne 0 ]; then
    echo "❌ Initialization failed!"
    exit 1
fi

echo ""
echo "✓ Initialization completed successfully!"
echo ""

# Step 2: Update README
echo "========================================"
echo "Step 2: Updating comics and README..."
echo "========================================"
"$SCRIPT_DIR/update_readme.sh"

if [ $? -ne 0 ]; then
    echo "❌ Update failed!"
    exit 1
fi

echo ""
echo "========================================"
echo "✅ All tasks completed successfully!"
echo "========================================"