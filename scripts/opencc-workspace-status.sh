#!/usr/bin/env bash
set -euo pipefail

workspace="${OPENCC_WORKSPACE:-.}"

echo "STABLE_BUILD_SCM_REVISION $(git -C "$workspace" rev-parse HEAD)"
echo "STABLE_BUILD_SCM_REMOTE $(git -C "$workspace" config --get remote.origin.url || true)"

if git -C "$workspace" diff --quiet && git -C "$workspace" diff --cached --quiet; then
  echo "STABLE_BUILD_SCM_DIRTY 0"
else
  echo "STABLE_BUILD_SCM_DIRTY 1"
fi
