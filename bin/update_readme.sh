#!/bin/bash

# Script to update the README with latest comics using Docker
# Date: December 7, 2025

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Get the project root directory (parent of bin)
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "Building Docker image..."
cd "$PROJECT_ROOT"
docker build -t comics-daily .

echo "Running Docker container to update comics and README..."
docker run --rm -v "$PROJECT_ROOT:/docker_testcontainer" comics-daily
