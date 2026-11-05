#!/usr/bin/env bash
# Build the static HTML site from docs/ into site/.
# Usage: ./build.sh
set -euo pipefail
cd "$(dirname "$0")"
python3 build.py
