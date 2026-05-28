#!/usr/bin/env bash
# Run this locally (not in CI) to set up multi-account gh auth
# and make the five listed repos private.
# Requires: gh CLI — https://cli.github.com

set -e

echo "=== BaBBled GitHub Account Setup ==="

if ! command -v gh &>/dev/null; then
  echo "ERROR: gh not found. Install from https://cli.github.com then re-run."
  exit 1
fi

echo ""
echo "--- Step 1: Authenticate accounts ---"
echo "You will be prompted three times. Log in to each account in order."
echo ""

echo ">> brookehoward2008-droid (primary)"
gh auth login --git-protocol https

echo ""
echo ">> brookehoward2008"
gh auth login --git-protocol https

echo ""
echo ">> babbledllc"
gh auth login --git-protocol https

echo ""
echo "Authenticated accounts:"
gh auth status

echo ""
echo "--- Step 2: Make repos private (brookehoward2008-droid) ---"
gh auth switch --user brookehoward2008-droid

for repo in clean26 history-of-internet spring2026 lilt sherwood-html; do
  echo "Making brookehoward2008-droid/$repo private..."
  gh repo edit "brookehoward2008-droid/$repo" \
    --visibility private \
    --accept-visibility-change-consequences
done

echo ""
echo "--- Step 3: Add collaborators to babbled-wear ---"
for user in brookehoward2008 babbledllc; do
  echo "Adding $user as admin to babbled-wear..."
  gh api "repos/brookehoward2008-droid/babbled-wear/collaborators/$user" \
    --method PUT --field permission=admin
done

echo ""
echo "--- Step 4: Verify repo visibility ---"
gh repo list brookehoward2008-droid --json name,visibility --limit 20 \
  | python3 -c "
import json, sys
repos = json.load(sys.stdin)
for r in repos:
    print(f\"  {r['name']:30s} {r['visibility']}\")"

echo ""
echo "=== Done ==="
echo ""
echo "Install the ai-setup alias for future projects:"
echo "  echo 'alias ai-setup=\"bash ~/.claude/setup-project.sh\"' >> ~/.bashrc"
echo "  source ~/.bashrc"
