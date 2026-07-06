-- trend-scout: optional Postgres state schema
-- Apply via psql (plain Postgres). RLS: scout data is internal — service-role only.

create table if not exists scout_items (
  id            bigint generated always as identity primary key,
  full_name     text not null unique,            -- e.g. "obra/superpowers" or registry id
  category      text not null check (category in ('skill','agent','plugin','mcp','framework','other')),
  layer         text,                            -- design|frontend|backend|data|platform|quality|sre|orchestration
  url           text not null,
  description   text,
  license       text,
  author_trust  numeric default 0.2,
  first_seen    timestamptz not null default now(),
  status        text not null default 'new'      -- new|watchlist|recommended|adopted|rejected
                check (status in ('new','watchlist','recommended','adopted','rejected')),
  reject_reason text,
  security_verdict text default 'unreviewed'     -- unreviewed|clean|review_required|rejected
                check (security_verdict in ('unreviewed','clean','review_required','rejected')),
  security_notes text
);

-- one row per item per scan run → velocity = diff between runs
create table if not exists scout_metrics (
  id          bigint generated always as identity primary key,
  item_id     bigint not null references scout_items(id) on delete cascade,
  run_at      timestamptz not null default now(),
  stars       integer,
  installs    integer,                            -- from official plugin directory when available
  pushed_at   timestamptz,
  contributors integer,
  hn_points   integer,
  sources     text[],                             -- which sources mentioned it this run
  score       numeric                             -- computed 0..1
);
create index if not exists scout_metrics_item_run on scout_metrics(item_id, run_at desc);

create table if not exists scout_digests (
  id        bigint generated always as identity primary key,
  run_at    timestamptz not null default now(),
  digest_md text not null,
  items_recommended int default 0
);

-- velocity helper: stars delta over last 7 days per item
create or replace view scout_velocity as
select i.full_name, i.category, i.layer,
       max(m.stars) filter (where m.run_at > now() - interval '1 day')  as stars_now,
       max(m.stars) filter (where m.run_at between now() - interval '8 days' and now() - interval '6 days') as stars_week_ago,
       max(m.stars) filter (where m.run_at > now() - interval '1 day')
     - max(m.stars) filter (where m.run_at between now() - interval '8 days' and now() - interval '6 days') as stars_delta_7d
from scout_items i join scout_metrics m on m.item_id = i.id
group by i.full_name, i.category, i.layer;

alter table scout_items   enable row level security;
alter table scout_metrics enable row level security;
alter table scout_digests enable row level security;
-- no policies on purpose: deny-by-default, access via service role key only
