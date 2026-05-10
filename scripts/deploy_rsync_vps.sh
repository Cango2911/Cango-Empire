#!/usr/bin/env bash
# CanGo Empire – website/ per rsync+SSH auf den VPS (schneller & sicherer als FTP)
#
# Voraussetzung: SSH-Login funktioniert, z. B.:
#   ssh -p 2222 root@31.97.56.197
# (Hostinger VPS: oft Port 2222, da 22 durch Firewall gesperrt sein kann.)
# Empfohlen: SSH-Key (ssh-copy-id -p 2222 …), dann kein Passwort pro Deploy.
#
# Konfiguration in .env (siehe .env.example):
#   CANGO_SSH_HOST, CANGO_SSH_PORT, CANGO_SSH_USER, CANGO_SSH_WWW
#
# Standard-Ziel: Container cango-empire-website mountet Host-Pfad
#   /opt/cango-empire-website/website → /usr/share/nginx/html
# (Nicht das NPM-Volume unter /docker/nginx-proxy-manager-… — dort landet
#  das Live-Site-Docker nicht.)
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
SSH_PORT="${CANGO_SSH_PORT:-22}"
REMOTE="${CANGO_SSH_WWW:-/opt/cango-empire-website/website}"
SRC="$REPO/website/"
RSYNC_SSH=(ssh -o BatchMode=no -p "$SSH_PORT")

echo "=== CanGo Empire – rsync → VPS ==="
echo "Quelle:  $SRC"
echo "SSH:     Port $SSH_PORT → ${USER}@${HOST}"
echo "Ziel:    ${REMOTE}/"
echo ""

if [[ ! -d "$SRC" ]]; then
  echo "❌ website/ nicht gefunden."
  exit 1
fi

rsync -avz \
  --delete \
  --exclude='.DS_Store' \
  --exclude='*.bak*' \
  --exclude='*-old.html' \
  --exclude='index-v*.html' \
  --exclude='index-[0-9].html' \
  --exclude='test_local.html' \
  --exclude='force_reload.html' \
  -e "${RSYNC_SSH[*]}" \
  "$SRC" "${USER}@${HOST}:${REMOTE}/"

echo ""
echo "✅ Fertig: $(date '+%Y-%m-%d %H:%M:%S')"
echo "   Prüfen: https://automation-cango-app-empire.com (Cache leeren ggf. hart neu laden)."
