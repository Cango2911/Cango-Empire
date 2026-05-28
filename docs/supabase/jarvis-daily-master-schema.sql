-- CanGo App Empire · Jarvis Daily Master · Supabase Schema
-- Projekt: kekmslytyttcipanwdop (eu-central-1) · Stand: Mai 2026
-- 8 Tabellen · bereits migriert, hier als Referenz / Neuaufsetzen

-- ────────────────────────────────────────────────────────────
-- 1. JARVIS MISSIONS (KI-Analyse-Ergebnisse, täglich gecacht)
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS jarvis_missions (
  id           uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  date         date UNIQUE,
  missions     jsonb,       -- [{rank, task, pillar, why, tools}]
  daily_focus  text,
  alert        text,
  context      jsonb,       -- energyLevel, revenueGap, maxTasksPensum, …
  created_at   timestamptz DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_jarvis_missions_date ON jarvis_missions(date);

-- ────────────────────────────────────────────────────────────
-- 2. TASK CONFIRMATIONS (Telegram Start/Skip/Done)
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
  created_at timestamptz DEFAULT now()
);

-- ────────────────────────────────────────────────────────────
-- 6. DAILY CONTEXT (Tageskontext: Umsatz, Phase, Energie)
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS daily_context (
  day            date PRIMARY KEY,
  phase          text DEFAULT 'phase1',
  revenue_month  numeric(12,2) DEFAULT 0,
  revenue_today  numeric(12,2) DEFAULT 0,
  vision_revenue numeric(14,2) DEFAULT 0,
  energy_level   smallint DEFAULT 7 CHECK (energy_level BETWEEN 1 AND 10),
  one_thing      text,
  context_json   jsonb,
  updated_at     timestamptz DEFAULT now()
);

-- ────────────────────────────────────────────────────────────
-- 7. EVENING REPORT (Abend-Review, Whisper-Transkript)
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS evening_report (
  day            date PRIMARY KEY,
  energy_level   smallint CHECK (energy_level BETWEEN 1 AND 10),
  work_hours     numeric(4,1),
  notes          text,
  mood_ok        boolean,
  jarvis_pct     smallint,      -- % der Jarvis-Missionen erledigt
  raw_transcript text,          -- Whisper-Transkript der Sprachnachricht
  created_at     timestamptz DEFAULT now()
);

-- ────────────────────────────────────────────────────────────
-- 8. MORNING BRIEFING (Telegram-Briefing-Log)
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS morning_briefing (
  id             bigserial PRIMARY KEY,
  day            date NOT NULL,
  briefing_text  text,
  missions_json  jsonb,
  sent_at        timestamptz DEFAULT now()
);

-- ────────────────────────────────────────────────────────────
-- ROW LEVEL SECURITY
-- ────────────────────────────────────────────────────────────
ALTER TABLE jarvis_missions    ENABLE ROW LEVEL SECURITY;
ALTER TABLE task_confirmations ENABLE ROW LEVEL SECURITY;
ALTER TABLE outreach_leads     ENABLE ROW LEVEL SECURITY;
ALTER TABLE avatar_productions ENABLE ROW LEVEL SECURITY;
ALTER TABLE knowledge_base     ENABLE ROW LEVEL SECURITY;
ALTER TABLE daily_context      ENABLE ROW LEVEL SECURITY;
ALTER TABLE evening_report     ENABLE ROW LEVEL SECURITY;
ALTER TABLE morning_briefing   ENABLE ROW LEVEL SECURITY;

CREATE POLICY "service_role_all" ON jarvis_missions    FOR ALL USING (true);
CREATE POLICY "service_role_all" ON task_confirmations FOR ALL USING (true);
CREATE POLICY "service_role_all" ON outreach_leads     FOR ALL USING (true);
CREATE POLICY "service_role_all" ON avatar_productions FOR ALL USING (true);
CREATE POLICY "service_role_all" ON knowledge_base     FOR ALL USING (true);
CREATE POLICY "service_role_all" ON daily_context      FOR ALL USING (true);
CREATE POLICY "service_role_all" ON evening_report     FOR ALL USING (true);
CREATE POLICY "service_role_all" ON morning_briefing   FOR ALL USING (true);
