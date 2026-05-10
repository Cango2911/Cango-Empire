#!/usr/bin/env bash
# CanGo Empire – website/ per rsync+SSH auf den VPS (schneller & sicherer als FTP)
#
# Voraussetzung: SSH-Login funktioniert, z. B.:
#   ssh root@31.97.56.197
# Empfohlen: SSH-Key (ssh-copy-id), dann kein Passwort pro Deploy.
#
# Konfiguration in .env (siehe .env.example):
#   CANGO_SSH_HOST, CANGO_SSH_USER, CANGO_SSH_WWW
#
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"

if [[ -f "$REPO/.env" ]]; then
  set -a
  # shellcheck disable=SC1091
  source "$REPO/.env"
  set +a
fi

HOST="${CANGO_SSH_HOST:-31.97.56.197}"
USER="${CANGO_SSH_USER:-root}"
REMOTE="${CANGO_SSH_WWW:-/docker/nginx-proxy-manager-5tiw/www}"
SRC="$REPO/website/"

echo "=== CanGo Empire – rsync → VPS ==="
echo "Quelle:  $SRC"
echo "Ziel:    ${USER}@${HOST}:${REMOTE}/"
echo ""

if [[ ! -d "$SRC" ]]; then
  echo "❌ website/ nicht gefunden."
  exit 1
fi

rsync -avz \
  --delete \
  --exclude='.DS_Store' \
  --exclude='*.bak*' \
  -e "ssh -o BatchMode=no" \
  "$SRC" "${USER}@${HOST}:${REMOTE}/"

echo ""
echo "✅ Fertig: $(date '+%Y-%m-%d %H:%M:%S')"
echo "   Prüfen: https://automation-cango-app-empire.com (Cache leeren ggf. hart neu laden)."
