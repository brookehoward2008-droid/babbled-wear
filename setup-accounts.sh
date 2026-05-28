#!/usr/bin/env bash
# Run this locally to set up multi-account gh auth and make repos private.
# Flags:
#   --write       actually make repos private (default is dry-run / status only)
#   --install-gh  install gh CLI if not found (Windows: uses winget)
# Supports bash on Windows (Git Bash / WSL), macOS, Linux.

set -e

WRITE=false
INSTALL_GH=false

for arg in "$@"; do
  case $arg in
    --write)      WRITE=true ;;
    --install-gh) INSTALL_GH=true ;;
  esac
done

echo "=== BaBBled Account Setup ==="
echo "Mode: $([ "$WRITE" = true ] && echo 'WRITE (live changes)' || echo 'read-only (dry run)')"
echo ""

# --- Install gh if needed ---
if ! command -v gh &>/dev/null; then
  if [ "$INSTALL_GH" = false ]; then
    echo "ERROR: gh not found."
    echo "  Windows:  winget install --id GitHub.cli"
    echo "  macOS:    brew install gh"
    echo "  Linux:    https://cli.github.com"
    echo "Re-run with --install-gh to auto-install on supported platforms."
    exit 1
  fi

  OS="$(uname -s)"
  case "$OS" in
    MINGW*|CYGWIN*|MSYS*)
      echo "Installing gh via winget (Windows)..."
      winget install --id GitHub.cli --silent
      ;;
    Darwin)
      echo "Installing gh via Homebrew (macOS)..."
      brew install gh
      ;;
    Linux)
      echo "Installing gh via apt (Linux/WSL)..."
      curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg \
        | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg 2>/dev/null
      echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
        | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
      sudo apt-get update -qq && sudo apt-get install gh -y -qq
      ;;
    *)
      echo "ERROR: Unknown OS '$OS'. Install gh manually from https://cli.github.com"
      exit 1
      ;;
  esac
fi

echo "gh: $(gh --version | head -1)"
echo ""

# --- Step 1: Auth status ---
echo "--- Step 1: Current auth status ---"
gh auth status 2>&1 || true
echo ""

# --- Step 2: Authenticate each account ---
echo "--- Step 2: Authenticate accounts ---"
echo "You will be prompted for each account. Use a browser or PAT token."
echo ""

for account in brookehoward2008-droid brookehoward2008 babbledllc; do
  if gh auth status --hostname github.com 2>&1 | grep -q "$account"; then
    echo "  $account: already authenticated, skipping"
  else
    echo ">> Logging in as $account"
    gh auth login --hostname github.com --git-protocol https
  fi
done

echo ""
echo "Authenticated accounts after setup:"
gh auth status 2>&1 || true
echo ""

# --- Step 3: Make repos private ---
REPOS=(clean26 history-of-internet spring2026 lilt sherwood-html)
ORG="brookehoward2008-droid"

echo "--- Step 3: Repo visibility ---"
echo "These repos will be made private: ${REPOS[*]}"
echo "Keep public: babbled-notes, Babbled-notes-v2"
echo ""

if [ "$WRITE" = false ]; then
  echo "DRY RUN — current visibility:"
  gh auth switch --user "$ORG" 2>/dev/null || true
  gh repo list "$ORG" --json name,visibility --limit 20 \
    | python3 -c "
import json,sys
repos=json.load(sys.stdin)
for r in repos:
    flag=' <-- will make private' if r['name'] in ['clean26','history-of-internet','spring2026','lilt','sherwood-html'] else ''
    print(f'  {r[\"name\"]:30s} {r[\"visibility\"]}{flag}')
"
  echo ""
  echo "To apply changes, re-run with --write"
  exit 0
fi

# Explicit confirmation before live changes
echo "CONFIRM: About to make these repos PRIVATE on $ORG:"
for repo in "${REPOS[@]}"; do
  echo "  - $repo"
done
echo ""
read -rp "Type 'yes' to continue: " confirm
if [ "$confirm" != "yes" ]; then
  echo "Aborted."
  exit 1
fi

gh auth switch --user "$ORG" 2>/dev/null || true

for repo in "${REPOS[@]}"; do
  echo "Making $ORG/$repo private..."
  gh repo edit "$ORG/$repo" \
    --visibility private \
    --accept-visibility-change-consequences
done

echo ""
echo "--- Step 4: Add collaborators to babbled-wear ---"
for user in brookehoward2008 babbledllc; do
  echo "Adding $user as admin to $ORG/babbled-wear..."
  gh api "repos/$ORG/babbled-wear/collaborators/$user" \
    --method PUT --field permission=admin 2>/dev/null && echo "  done" || echo "  failed (may need repo access)"
done

echo ""
echo "--- Step 5: Verify ---"
gh repo list "$ORG" --json name,visibility --limit 20 \
  | python3 -c "
import json,sys
repos=json.load(sys.stdin)
for r in repos:
    print(f'  {r[\"name\"]:30s} {r[\"visibility\"]}')
"

echo ""
echo "=== Done ==="
