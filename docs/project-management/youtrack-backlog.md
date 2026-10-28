# YouTrack Backlog

**YouTrack project link:** `https://<your-instance>.youtrack.cloud/projects/GIS` ← replace with the real link; give the supervisor (Algys Saltanat) and all three members access.
Import: `youtrack-import.csv` (YouTrack → Issues → Import → CSV). Assignees in the file are **proposed** — adjust with the team. Add the board screenshot to `docs/evidence/youtrack/`.

Priority: Critical = needed for the 24 October milestone; Major = mandatory (M) requirement; Normal = should (S); Minor = could (C).
Assignee code: **A** Arlan Aidarov, **R** Ramazan Ashirbek, **K** Kairat Bulatov (proposed split: Ramazan – database/API/map; Arlan – AI modules; Kairat – frontend, lost-and-found, reservation).

## Epic 0 — Analysis and documentation (until 24 Oct)
| ID | Task | Pri. | Assignee |
|---|---|---|---|
| GIS-1 | Project proposal and scope | Critical | A |
| GIS-2 | 3–5 discussions with users/client; fill log | Critical | A, R, K (one each) |
| GIS-3 | Literature review: add DOIs, search log | Critical | A |
| GIS-4 | Existing system comparison with screenshots | Critical | K |
| GIS-5 | Technology comparison, review with supervisor | Critical | R |
| GIS-6 | Requirements and acceptance criteria | Critical | R |
| GIS-7 | Architecture diagrams and description | Critical | R |
| GIS-8 | Verification and evaluation plan | Critical | A |
| GIS-9 | Wireframes (prototype materials) | Critical | K |
| GIS-10 | Supervisor review meeting and feedback log | Critical | A |
| GIS-11 | README, repository structure, contribution evidence | Critical | K |

## Epic 1 — Infrastructure and data model
| ID | Task | Pri. | Assignee |
|---|---|---|---|
| GIS-12 | Repository, branching rules, CI | Major | R |
| GIS-13 | Docker Compose: PostGIS + API + web | Major | R |
| GIS-14 | Common GIS data model and migrations (from ER diagram) | Major | R |
| GIS-15 | Authentication and role-based access (FR-C1) | Major | R |
| GIS-16 | Synthetic data generators with fixed seeds (NFR-D1) | Major | A |

## Epic 2 — Parking and reservation
| ID | Task | Pri. | Assignee |
|---|---|---|---|
| GIS-17 | Parking zones API and map layer (FR-P1, P3) | Major | R |
| GIS-18 | Reservation with capacity check in transaction (FR-R1–R3) | Major | K |
| GIS-19 | Parking predictor + baseline (FR-P2, NFR-A1) | Major | A |
| GIS-20 | Reservation expiry (FR-R4) | Minor | K |

## Epic 3 — Hazard reporting
| ID | Task | Pri. | Assignee |
|---|---|---|---|
| GIS-21 | Collect ≈ 600 reports, annotate, compute kappa | Major | A, K |
| GIS-22 | Report submission API and form (FR-H1, H2) | Major | K |
| GIS-23 | Hazard classifier + keyword baseline (FR-H3) | Major | A |
| GIS-24 | Staff review and status workflow (FR-H4, H5, H6) | Major | R |
| GIS-25 | Image privacy check (FR-H7) | Normal | A |

## Epic 4 — Lost-and-found
| ID | Task | Pri. | Assignee |
|---|---|---|---|
| GIS-26 | Create ≈ 300 item records and matched pairs | Major | K |
| GIS-27 | Item API and forms (FR-L1, L3, L5) | Major | K |
| GIS-28 | Matcher (embeddings + text + location) and text-filter baseline (FR-L2) | Major | A |
| GIS-29 | Match confirmation workflow (FR-L4) | Normal | K |

## Epic 5 — Staff decision-support map
| ID | Task | Pri. | Assignee |
|---|---|---|---|
| GIS-30 | Staff map with layers and filters (FR-S1) | Major | R |
| GIS-31 | Density/heatmap and counts (FR-S2) | Normal | R |
| GIS-32 | Aggregated location and CSV export (FR-S3, S4) | Normal | R |

## Epic 6 — Evaluation
| ID | Task | Pri. | Assignee |
|---|---|---|---|
| GIS-33 | Ethics application and consent form | Critical | A |
| GIS-34 | Automated functional/integration tests | Major | R, K |
| GIS-35 | Model evaluation report (CI, per language/category) | Major | A |
| GIS-36 | Load tests (p50/p95) | Major | R |
| GIS-37 | User study (15–20 participants), SUS, Likert | Major | A, R, K |
| GIS-38 | Analysis and final article | Major | A, R, K |
