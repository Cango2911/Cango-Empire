#!/bin/bash
# Trägt die n8n Jarvis-Webhook-URL in scripts/.env ein und testet sie
# Aufruf: bash scripts/set-jarvis-webhook.sh "https://n8n.domain.de/webhook/jarvis-analyze"
set -euo pipefail

WEBHOOK_URL="${1:-}"
ENV_FILE="$(dirname "$0")/.env"

if [ -z "$WEBHOOK_URL" ]; then
  echo "Aufruf: bash scripts/set-jarvis-webhook.sh <WEBHOOK_URL>"
  exit 1
fi

# URL in .env eintragen
if grep -q "^N8N_JARVIS_WEBHOOK=" "$ENV_FILE" 2>/dev/null; then
  sed -i '' "s|^N8N_JARVIS_WEBHOOK=.*|N8N_JARVIS_WEBHOOK=$WEBHOOK_URL|" "$ENV_FILE"
else
  echo "N8N_JARVIS_WEBHOOK=$WEBHOOK_URL" >> "$ENV_FILE"
fi

echo "✓ N8N_JARVIS_WEBHOOK gesetzt: $WEBHOOK_URL"

# Webhook testen
echo "── Teste Webhook …"
RESPONSE=$(curl -s --max-time 10 -X POST "$WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d '{"date":"'"$(date +%Y-%m-%d)"'","monthRevenue":0,"monthGoal":2870,"energyLevel":7,"test":true}' \
  2>&1) || true

if echo "$RESPONSE" | python3 -c "import json,sys; d=json.load(sys.stdin); print('✅ Jarvis antwortet:', d.get('daily_focus','ok'))" 2>/dev/null; then
  echo "── Webhook funktioniert."
else
  echo "⚠ Antwort: $RESPONSE"
  echo "── Workflow aktiv? Webhook-URL korrekt?"
fi
