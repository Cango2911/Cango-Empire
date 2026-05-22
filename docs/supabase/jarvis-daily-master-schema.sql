-- CanGo App Empire · Jarvis Daily Master · Supabase Schema
-- Einmalig im SQL Editor ausführen (supabase.com → Projekt → SQL Editor)
-- Stand: Mai 2026

-- ────────────────────────────────────────────────────────────
-- 1. JARVIS MISSIONS (KI-Analyse-Ergebnisse, täglich gecacht)
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS jarvis_missions (
  id           uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  date         date UNIQUE,
  missions     jsonb,       -- Array: [{rank, task, pillar, why, tools}]
  daily_focus  text,
  alert        text,
  context      jsonb,       -- Vollständiger Kontext (energyLevel, revenueGap, etc.)
  created_at   timestamptz DEFAULT now()
);

-- Index für schnelle Datumsabfragen
CREATE INDEX IF NOT EXISTS idx_jarvis_missions_date ON jarvis_missions(date);

-- ────────────────────────────────────────────────────────────
-- 2. TASK CONFIRMATIONS (Telegram Start/Skip/Done Tracking)
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS task_confirmations (
  id           uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  date         date,
  task_rank    int,
  task_text    text,
  status       text DEFAULT 'pending',  -- pending | started | done | skipped
  skip_count   int DEFAULT 0,
  started_at   timestamptz,
  completed_at timestamptz,
  UNIQUE(date, task_rank)
);

CREATE INDEX IF NOT EXISTS idx_task_confirmations_date ON task_confirmations(date);

-- ────────────────────────────────────────────────────────────
-- 3. OUTREACH LEADS
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS outreach_leads (
  id         uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  company    text,
  email      text,
  status     text DEFAULT 'sent',  -- sent | replied | meeting | closed | rejected
  source     text,                 -- google_maps | branchenbuch | linkedin | referral
  notes      text,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
);

-- Trigger: updated_at automatisch setzen
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN NEW.updated_at = now(); RETURN NEW; END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_outreach_leads_updated
  BEFORE UPDATE ON outreach_leads
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();

-- ────────────────────────────────────────────────────────────
-- 4. AVATAR PRODUCTIONS (HeyGen Pipeline)
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS avatar_productions (
  id          uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  title       text,
  script      text,
  heygen_id   text,
  status      text DEFAULT 'queued',  -- queued | rendering | done | failed
  video_url   text,
  created_at  timestamptz DEFAULT now()
);

-- ────────────────────────────────────────────────────────────
-- 5. KNOWLEDGE BASE (Jarvis Langzeitgedächtnis)
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS knowledge_base (
  id         uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  category   text,   -- outreach | coaching | affiliate | ecommerce | personal
  content    text,
  embedding  vector(1536),  -- für spätere Vektor-Suche (pgvector)
  created_at timestamptz DEFAULT now()
);

-- ────────────────────────────────────────────────────────────
-- ROW LEVEL SECURITY (RLS) — alle Tabellen sichern
-- ────────────────────────────────────────────────────────────
ALTER TABLE jarvis_missions      ENABLE ROW LEVEL SECURITY;
ALTER TABLE task_confirmations   ENABLE ROW LEVEL SECURITY;
ALTER TABLE outreach_leads       ENABLE ROW LEVEL SECURITY;
ALTER TABLE avatar_productions   ENABLE ROW LEVEL SECURITY;
ALTER TABLE knowledge_base       ENABLE ROW LEVEL SECURITY;

-- Service-Role darf alles (für n8n Backend)
CREATE POLICY "service_role_all" ON jarvis_missions      FOR ALL USING (true);
CREATE POLICY "service_role_all" ON task_confirmations   FOR ALL USING (true);
CREATE POLICY "service_role_all" ON outreach_leads       FOR ALL USING (true);
CREATE POLICY "service_role_all" ON avatar_productions   FOR ALL USING (true);
CREATE POLICY "service_role_all" ON knowledge_base       FOR ALL USING (true);
