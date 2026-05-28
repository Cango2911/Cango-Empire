"""
CanGo Outreach Sniper — Google Maps Business Finder
Findet KMU im DACH-Raum ohne ordentliche Online-Präsenz.

Setup:
  pip install requests python-dotenv
  Erstelle .env mit GOOGLE_MAPS_API_KEY und N8N_WEBHOOK_URL

Aufruf:
  python outreach_sniper.py --city Celle --radius 20 --type Handwerk
"""

import os
import csv
import json
import time
import argparse
import requests
from datetime import date
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "")
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "")
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY", "")

BUSINESS_TYPES = {
    "Handwerk":     ["plumber", "electrician", "painter", "carpenter", "roofing_contractor"],
    "Gastronomie":  ["restaurant", "cafe", "bakery", "bar"],
    "Einzelhandel": ["clothing_store", "hardware_store", "furniture_store", "florist"],
    "Dienstleister":["hair_care", "spa", "gym", "laundry", "moving_company"],
    "Immobilien":   ["real_estate_agency"],
    "Finanz":       ["insurance_agency", "accounting"],
}

OUTPUT_DIR = Path(__file__).parent / "outreach_leads"
OUTPUT_DIR.mkdir(exist_ok=True)


# ── Google Places suchen ──────────────────────────────────────

def search_places(city: str, place_type: str, radius_km: int) -> list[dict]:
    """Sucht Unternehmen via Google Places API (Nearby Search)."""
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json"
    geo = requests.get(geocode_url, params={"address": city + ", Deutschland", "key": GOOGLE_API_KEY}, timeout=10)
    geo.raise_for_status()
    results = geo.json().get("results", [])
    if not results:
        print(f"  [WARN] Kein Geocode-Ergebnis für '{city}'")
        return []
    loc = results[0]["geometry"]["location"]

    nearby_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    places, page_token = [], None
    for _ in range(3):
        params = {
            "location": f"{loc['lat']},{loc['lng']}",
            "radius": radius_km * 1000,
            "type": place_type,
            "key": GOOGLE_API_KEY,
        }
        if page_token:
            params["pagetoken"] = page_token
            time.sleep(2)
        r = requests.get(nearby_url, params=params, timeout=15)
        r.raise_for_status()
        data = r.json()
        places.extend(data.get("results", []))
        page_token = data.get("next_page_token")
        if not page_token:
            break

    return places


def get_place_details(place_id: str) -> dict:
    """Holt Details zu einem Place (Website, Telefon, Bewertung)."""
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    fields = "name,website,formatted_phone_number,rating,user_ratings_total,formatted_address"
    r = requests.get(url, params={"place_id": place_id, "fields": fields, "key": GOOGLE_API_KEY}, timeout=10)
    r.raise_for_status()
    return r.json().get("result", {})


# ── Lead-Qualifizierung ───────────────────────────────────────

def is_weak_online_presence(details: dict) -> bool:
    """Gibt True zurück wenn kein / schwacher Online-Auftritt erkennbar."""
    website = details.get("website", "")
    rating = details.get("rating", 5.0)
    reviews = details.get("user_ratings_total", 999)

    no_website = not website or any(p in website.lower() for p in [
        "facebook.com", "instagram.com", "google.com", "yelp.com", "tripadvisor"
    ])
    low_ratings = reviews < 15
    low_score = rating < 3.8

    return no_website or (low_ratings and low_score)


# ── Ergebnisse speichern ──────────────────────────────────────

def save_leads_csv(leads: list[dict], city: str, biz_type: str) -> Path:
    today = date.today().isoformat()
    filename = OUTPUT_DIR / f"leads_{today}_{city}_{biz_type}.csv"
    fieldnames = ["name", "address", "phone", "website", "rating", "reviews", "place_id", "priority"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(leads)
    return filename


def push_to_n8n(leads: list[dict], city: str) -> bool:
    """Sendet Leads per Webhook an n8n für weitere Verarbeitung."""
    if not N8N_WEBHOOK_URL:
        return False
    payload = {"date": date.today().isoformat(), "city": city, "leads": leads[:20]}
    try:
        r = requests.post(N8N_WEBHOOK_URL, json=payload, timeout=10)
        return r.status_code < 300
    except Exception as e:
        print(f"  [WARN] n8n-Push fehlgeschlagen: {e}")
        return False


def push_to_supabase(leads: list[dict]) -> bool:
    """Schreibt Leads direkt in Supabase-Tabelle 'outreach_leads'."""
    if not SUPABASE_URL or not SUPABASE_KEY:
        return False
    url = f"{SUPABASE_URL}/rest/v1/outreach_leads"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "resolution=ignore-duplicates",
    }
    try:
        r = requests.post(url, headers=headers, json=leads, timeout=15)
        return r.status_code < 300
    except Exception as e:
        print(f"  [WARN] Supabase-Push fehlgeschlagen: {e}")
        return False


# ── Hauptlogik ────────────────────────────────────────────────

def run(city: str, radius_km: int, biz_category: str, limit: int = 50):
    if not GOOGLE_API_KEY:
        print("FEHLER: GOOGLE_MAPS_API_KEY fehlt in .env")
        return

    place_types = BUSINESS_TYPES.get(biz_category, ["establishment"])
    all_leads = []

    for pt in place_types:
        print(f"\n  Suche '{pt}' in {city} ({radius_km}km)...")
        places = search_places(city, pt, radius_km)
        print(f"  → {len(places)} Treffer gefunden")

        for p in places[:limit]:
            try:
                details = get_place_details(p["place_id"])
                if is_weak_online_presence(details):
                    lead = {
                        "name":     details.get("name", p.get("name", "")),
                        "address":  details.get("formatted_address", ""),
                        "phone":    details.get("formatted_phone_number", ""),
                        "website":  details.get("website", "KEIN WEBSITE"),
                        "rating":   details.get("rating", ""),
                        "reviews":  details.get("user_ratings_total", 0),
                        "place_id": p["place_id"],
                        "priority": "HOCH" if not details.get("website") else "MITTEL",
                    }
                    all_leads.append(lead)
                    print(f"    ✓ {lead['name']} — {lead['priority']} | {lead['website']}")
                time.sleep(0.3)
            except Exception as e:
                print(f"    [SKIP] {p.get('name', '?')}: {e}")

    print(f"\n{'='*50}")
    print(f"  GESAMT: {len(all_leads)} qualifizierte Leads in {city}")
    print(f"{'='*50}")

    if not all_leads:
        print("  Keine Leads gefunden. Radius oder Kategorie anpassen.")
        return

    csv_path = save_leads_csv(all_leads, city, biz_category)
    print(f"\n  CSV gespeichert: {csv_path}")

    if push_to_n8n(all_leads, city):
        print("  ✓ Leads an n8n-Webhook gesendet")
    if push_to_supabase(all_leads):
        print("  ✓ Leads in Supabase gespeichert")

    print(f"\n  TOP 5 LEADS:")
    for l in sorted(all_leads, key=lambda x: x["priority"])[:5]:
        print(f"  [{l['priority']}] {l['name']} | {l['phone']} | {l['website']}")

    print(f"\n  → Nächster Schritt: CSV öffnen, E-Mail-Vorlage anpassen, Outreach starten.\n")


# ── CLI ───────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CanGo Outreach Sniper – KMU ohne Website finden")
    parser.add_argument("--city",   default="Celle",     help="Stadt / Region (default: Celle)")
    parser.add_argument("--radius", default=20, type=int, help="Suchradius in km (default: 20)")
    parser.add_argument("--type",   default="Handwerk",  help=f"Kategorien: {', '.join(BUSINESS_TYPES)}")
    parser.add_argument("--limit",  default=50, type=int, help="Max. Places pro Typ (default: 50)")
    args = parser.parse_args()

    print(f"\n  CanGo Outreach Sniper — {date.today()}")
    print(f"  Stadt: {args.city} | Radius: {args.radius}km | Typ: {args.type}\n")
    run(args.city, args.radius, args.type, args.limit)
