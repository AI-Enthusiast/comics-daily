#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Get the project root directory (parent of bin)
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "========================================"
echo "Git fetch and pull..."
echo "========================================"
cd "$PROJECT_ROOT"
git fetch origin
git pull origin master

echo ""
echo "========================================"
echo "Building Docker image..."
echo "========================================"
docker build -t comics-daily .

echo ""
echo "========================================"
echo "Running Docker container to update comics and README..."
echo "========================================"
docker run --rm -v "$PROJECT_ROOT:/docker_testcontainer" comics-daily

echo ""
echo "========================================"
echo "Committing and pushing changes..."
echo "========================================"
cd "$PROJECT_ROOT"

# Add only the data directory and README
git add data/ README.md

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "No changes to commit."
else
    # Commit with timestamp
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
    git commit -m "Update comics and README - $TIMESTAMP"

    # Push to remote
    git push origin master
    echo "✓ Changes pushed successfully!"
fi

echo ""
echo "========================================"
echo "Update process completed!"
echo "========================================"