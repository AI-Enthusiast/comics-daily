#!/bin/bash

# Script to update the README with latest comics
# Date: December 4, 2025

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Get the project root directory (parent of bin)
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "Updating README with latest comics..."
python3 "$PROJECT_ROOT/src/update_readme.md.py"

