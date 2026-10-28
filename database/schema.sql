-- Draft common GIS data model (PostgreSQL + PostGIS). Matches diagrams/src/04-data-model.mmd.
-- Status: design draft for the 24 Oct milestone; not yet tested against a running database.
CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE app_user (
  id SERIAL PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  role TEXT NOT NULL CHECK (role IN ('citizen','staff','admin')),
  language TEXT CHECK (language IN ('kk','ru','en')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE district (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  polygon GEOMETRY(MultiPolygon, 4326)
);

CREATE TABLE parking_zone (
  id SERIAL PRIMARY KEY,
  district_id INT REFERENCES district(id),
  name TEXT NOT NULL,
  capacity INT NOT NULL CHECK (capacity > 0),
  location GEOMETRY(Point, 4326) NOT NULL,
  synthetic BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE parking_observation (
  id BIGSERIAL PRIMARY KEY,
  zone_id INT NOT NULL REFERENCES parking_zone(id),
  occupied INT NOT NULL CHECK (occupied >= 0),
  observed_at TIMESTAMPTZ NOT NULL,
  synthetic BOOLEAN NOT NULL DEFAULT TRUE
);
CREATE INDEX ON parking_observation (zone_id, observed_at);

CREATE TABLE parking_prediction (
  id BIGSERIAL PRIMARY KEY,
  zone_id INT NOT NULL REFERENCES parking_zone(id),
  target_time TIMESTAMPTZ NOT NULL,
  predicted_occupied REAL NOT NULL,
  model_version TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE reservation (
  id BIGSERIAL PRIMARY KEY,
  user_id INT NOT NULL REFERENCES app_user(id),
  zone_id INT NOT NULL REFERENCES parking_zone(id),
  start_time TIMESTAMPTZ NOT NULL,
  end_time TIMESTAMPTZ NOT NULL,
  status TEXT NOT NULL CHECK (status IN ('active','cancelled','expired')),
  CHECK (end_time > start_time)
);
-- Capacity rule (FR-P4/P5): enforced in the API inside a transaction by counting overlapping active reservations.

CREATE TABLE hazard_report (
  id BIGSERIAL PRIMARY KEY,
  user_id INT REFERENCES app_user(id),
  text TEXT NOT NULL,
  language TEXT CHECK (language IN ('kk','ru','en')),
  point GEOMETRY(Point, 4326) NOT NULL,
  photo_path TEXT,
  category_user TEXT,
  category_ai TEXT CHECK (category_ai IN ('road_damage','lighting','waste','snow_ice','other')),
  ai_confidence REAL,
  status TEXT NOT NULL DEFAULT 'new' CHECK (status IN ('new','in_review','closed')),
  verification_status TEXT NOT NULL DEFAULT 'unverified' CHECK (verification_status IN ('unverified','verified','rejected')),
  synthetic BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX ON hazard_report USING GIST (point);

CREATE TABLE hazard_review (
  id BIGSERIAL PRIMARY KEY,
  report_id BIGINT NOT NULL REFERENCES hazard_report(id),
  staff_id INT NOT NULL REFERENCES app_user(id),
  decision TEXT NOT NULL CHECK (decision IN ('verify','reject','close')),
  category_final TEXT,
  reviewed_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE lost_found_item (
  id BIGSERIAL PRIMARY KEY,
  user_id INT REFERENCES app_user(id),
  kind TEXT NOT NULL CHECK (kind IN ('lost','found')),
  category TEXT NOT NULL,            -- one of ten categories, fixed in Stage 1
  description TEXT NOT NULL,
  photo_path TEXT,
  point GEOMETRY(Point, 4326) NOT NULL,
  event_time TIMESTAMPTZ NOT NULL,
  status TEXT NOT NULL DEFAULT 'open' CHECK (status IN ('open','matched','closed')),
  verification_status TEXT NOT NULL DEFAULT 'unverified' CHECK (verification_status IN ('unverified','verified','rejected')),
  synthetic BOOLEAN NOT NULL DEFAULT FALSE
);
CREATE INDEX ON lost_found_item USING GIST (point);

CREATE TABLE item_match (
  id BIGSERIAL PRIMARY KEY,
  item_id BIGINT NOT NULL REFERENCES lost_found_item(id),
  candidate_id BIGINT NOT NULL REFERENCES lost_found_item(id),
  rank INT NOT NULL CHECK (rank BETWEEN 1 AND 5),
  score REAL NOT NULL,
  status TEXT NOT NULL DEFAULT 'suggested' CHECK (status IN ('suggested','confirmed','rejected'))
);
