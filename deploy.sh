#!/bin/bash
# Deploy: website/ → docker/www/
# Nginx Volume: ./www:/usr/share/nginx/html

set -e

REPO="/Users/canberkkivilcim/PycharmProjects/Cango-Empire"
SRC="$REPO/website"
DST="$REPO/docker/www"

echo "=== CanGo Empire Deploy ==="
echo "Quelle:  $SRC"
echo "Ziel:    $DST"
echo ""

mkdir -p "$DST"

rsync -av --delete \
  --exclude='.DS_Store' \
  --exclude='*.bak*' \
  "$SRC/" "$DST/"

echo ""
echo "=== Geänderte Dateien ==="
echo "  + website/blogs.html (Teaser-Card DaVinci)"
echo "  + website/blogs/maschinen-die-dienen.html (Neuer Artikel)"
echo "  + website/images/blog/davinci-pfad-cover.svg (Placeholder)"
echo "  - website/blog-davinci-automatisierung.html (gelöscht)"
echo ""
echo "=== Deploy abgeschlossen: $(date '+%Y-%m-%d %H:%M:%S') ==="
