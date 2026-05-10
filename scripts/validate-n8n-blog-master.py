#!/usr/bin/env python3
"""
Validiert n8n_Cango_Blog_Master_v2.json strukturell.
Kein API-Call — nur JSON-Logik-Checks.
"""
import json, sys, os

WORKFLOW_PATH = os.path.join(
    os.path.dirname(__file__),
    "../docs/n8n/workflows/n8n_Cango_Blog_Master_v2.json"
)
PLACEHOLDERS = [
    "DEIN_BROWSERACT_API_KEY",
    "DEINE_OPENAI_CREDENTIAL_ID",
    "DEINE-WORDPRESS-URL.de",
    "DEIN_WP_BASE64_AUTH",
    "DEINE_GOOGLE_SHEET_ID",
    "DEIN_SLACK_WEBHOOK_URL",
]

errors = []
warnings = []

with open(WORKFLOW_PATH) as f:
    wf = json.load(f)

raw = json.dumps(wf)
nodes_by_name = {n["name"]: n for n in wf["nodes"]}
connections = wf["connections"]

# 1. JSON-Struktur
assert "nodes" in wf and "connections" in wf, "nodes/connections fehlen"

# 2. Verbindungen: alle Quell- und Zielnodes müssen existieren
for src_name, conn_data in connections.items():
    if src_name not in nodes_by_name:
        errors.append(f"Verbindung: Source '{src_name}' nicht in nodes")
    for branch in conn_data.get("main", []):
        for target in branch:
            if target["node"] not in nodes_by_name:
                errors.append(f"Verbindung: Target '{target['node']}' nicht in nodes")

# 3. Merge
merge_nodes = [n for n in wf["nodes"] if n["type"] == "n8n-nodes-base.merge"]
for m in merge_nodes:
    ni = m["parameters"].get("numberInputs", 0)
    mode = m["parameters"].get("mode", "FEHLT")
    incoming = sum(
        1 for cd in connections.values()
        for b in cd.get("main", [])
        for t in b if t["node"] == m["name"]
    )
    if int(ni) != incoming:
        errors.append(f"Merge '{m['name']}': numberInputs={ni} aber {incoming} eingehende Verbindungen")
    if mode != "append":
        warnings.append(f"Merge '{m['name']}': mode='{mode}' — empfohlen: 'append'")
    else:
        print(f"  ✓ Merge '{m['name']}': mode=append, {incoming}/{ni} Verbindungen")

# 4. BA Ergebnis: task_id Fallback + method GET
for n in wf["nodes"]:
    if "BA Ergebnis" in n["name"]:
        method = n["parameters"].get("method", "GET")
        qp = n["parameters"].get("queryParameters", {}).get("parameters", [])
        task_id_val = next((p["value"] for p in qp if p["name"] == "task_id"), None)
        if not task_id_val:
            errors.append(f"{n['name']}: task_id Query-Parameter fehlt")
        elif "taskId" in task_id_val and "task_id" not in task_id_val:
            errors.append(f"{n['name']}: task_id nutzt nur $json.taskId (kein Fallback)")
        else:
            print(f"  ✓ {n['name']}: task_id={task_id_val[:50]}...")
        if method != "GET":
            warnings.append(f"{n['name']}: method='{method}' statt GET")

# 5. Aggregate: genau ein Code-Node nach Merge
aggregate_nodes = [n for n in wf["nodes"] if "Aggregate" in n["name"] or "aggregate" in n["name"]]
if not aggregate_nodes:
    errors.append("Kein Aggregate-Node gefunden — Slack könnte mehrfach feuern")
else:
    print(f"  ✓ Aggregate-Node: '{aggregate_nodes[0]['name']}'")

# 6. Platzhalter-Zählung (Info, kein Fehler)
print("\n  Platzhalter (vor n8n-Import zu ersetzen):")
for ph in PLACEHOLDERS:
    count = raw.count(ph)
    status = "⚠ noch nicht ersetzt" if count > 0 else "✓ ersetzt"
    print(f"    {status}: {ph} ({count}×)")

# Ergebnis
print()
if errors:
    print(f"FEHLER ({len(errors)}):")
    for e in errors:
        print(f"  ✗ {e}")
    sys.exit(1)
if warnings:
    print(f"WARNUNGEN ({len(warnings)}):")
    for w in warnings:
        print(f"  ⚠ {w}")
print("ERGEBNIS: OK — JSON-Struktur valide")
