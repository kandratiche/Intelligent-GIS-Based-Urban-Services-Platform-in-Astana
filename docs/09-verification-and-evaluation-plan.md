# 9. Verification and Evaluation Plan

Goal: demonstrate that the project aim is achieved — an integrated, AI-enhanced GIS platform performs better than baselines on defined technical and user measures — and that mandatory requirements (doc 06) are met. The design follows the methodology of the Midterm Research Proposal (design science research, mixed methods).

## 1. Evaluation questions, metrics, baselines
| # | Question | Metric | Baseline | Target / hypothesis |
|---|---|---|---|---|
| Q1 | Does the hazard classifier beat simple rules? (SQ1, H1) | Precision, recall, macro-F1 on held-out test set | **B1: keyword rules** | macro-F1 higher than B1 (bootstrap CI) |
| Q2 | Does lost-item matching beat a text filter? (SQ1, H1) | Top-5 retrieval rate | **B2: text filter** | Top-5 higher than B2 |
| Q3 | Does parking prediction beat the historical average? (SQ1, H1) | Mean absolute error, 30-min horizon | **B3: historical average** | MAE lower than B3 |
| Q4 | Is the platform fast enough? | Median and 95th-percentile API response time under simulated load | Requirement thresholds | median ≤ 300 ms, p95 ≤ 1 s at 50 concurrent users |
| Q5 | Do users complete tasks faster and more successfully? (SQ2, H2) | Task time, task success per scenario | **B4: baseline workflow** (separate map application + plain list) | Faster and higher success than B4 |
| Q6 | Is the platform usable and trusted? (SQ2, H2) | SUS score; five Likert items (usefulness, trust); one open question | Average SUS = 68 | mean SUS > 68 |
| Q7 | Are annotations reliable? | Cohen's kappa for hazard labels | – | report value (target: substantial agreement) |
| Q8 | Do functional requirements hold? | Pass/fail of acceptance tests T-* | – | all mandatory tests pass |

## 2. Data and measurement conditions
| Dataset | Size (planned) | Creation | Labels | Split |
|---|---|---|---|---|
| Parking | ≈ 50 zones in 3 districts with different land use | **Synthetic** time series from daily/weekly patterns plus noise; clearly labelled synthetic; reproducible seed | Known by construction | chronological split (train/validation/test, no random mixing of time) |
| Hazard reports | ≈ 600 short reports in Kazakh, Russian, English with photo and GPS | Written by volunteers from realistic scenarios | 5 categories (road damage, lighting, waste, snow and ice, other); two members label independently, Cohen's kappa | 70/15/15 train/validation/test, stratified by category and language |
| Lost-and-found | ≈ 300 records (photo, text, location, time), 10 categories | Created by the team/volunteers; matched pairs built for testing | Known pairs | pairs kept together in the same split |
| Spatial base data | – | OpenStreetMap roads, buildings, parking points; official open data if available | – | – |

Rules: the test set is never used for tuning; fixed random seeds; report results per language and per category; state explicitly that synthetic data make results **indicative**; repeat key tests on real data if they become available.
Measurement environment (CPU/GPU, RAM, OS, library versions) is recorded in `docs/evidence/benchmark-environment.md`. Performance tests: warm-up, then ≥ 100 requests per endpoint; simulated load with 50 concurrent users (Locust or k6).

## 3. User study
- **Participants:** 15–20 adults (students and residents of Astana), purposive sampling; inclusion: lives or studies in Astana and uses smartphones or maps regularly. If possible, 2–3 city-service experts review the staff map.
- **Design:** within-subject. Each participant performs **four scenario tasks** with the platform and with the baseline workflow B4, **counterbalanced order**.
- **Task set (example):** (1) find a parking zone with free places now and in 30 minutes and reserve a place; (2) report a hazard with photo and location and find its status; (3) search for a lost item and select the best match; (4) *(staff/expert)* find the area with most open hazard reports and the most loaded parking zones.
- **Data:** task logs (time, success), SUS, five Likert items, one open question.
- **Analysis:** paired t-test or Wilcoxon signed-rank test depending on normality (α = 0.05), effect sizes; open comments coded by both team members and grouped into themes; **convergent design** — quantitative results and themes in a joint table; disagreement (for example fast but distrusted) is reported as a design finding.
- **Ethics:** no participant data before approval; informed consent; anonymous responses; images contain no faces or number plates; location data aggregated.
- With a small sample the results are indicative.

## 4. Test plan
| Level | What | Tools | Tests |
|---|---|---|---|
| Unit | Reservation capacity logic, privacy functions, validation, data generator reproducibility | pytest | T-R2, T-S4, T-D1 |
| Integration | API + PostGIS queries, reservation transactions (concurrent requests), role checks | pytest, test DB | T-P1, T-R1–R3, T-H1, T-H4–H6, T-L1, T-L5, T-C1 |
| Model evaluation | B1/B2/B3 vs AI modules on test sets; bootstrap CIs; per-language and per-category tables | Python scripts, scikit-learn | T-H3, T-L2, T-P2, T-A1 |
| System/acceptance | Every mandatory requirement against its acceptance criterion | Checklist + automation | all T-* in doc 06 |
| Non-functional | Load test, AI inference time | Locust/k6 | T-N1, T-N2 |
| Security/privacy | Auth, injection, role checks, image policy | pytest, manual review | T-S5, T-S6, T-H7 |
| Usability | User study as above | Task logs, SUS | T-U1, T-U2, T-U3 |
| Resilience | Stop an AI module / DB reconnect | Manual fault injection | T-R5 |

## 5. Mapping of tests to the methodology table
| Objective | Data | Method | Measure |
|---|---|---|---|
| 1 | Literature, open data, discussions | Requirements analysis | Requirement list (doc 06) |
| 2 | Requirements | Data modelling | Schema review (T-C2) |
| 3 | Reports, items, parking series | Model training | F1, top-5, MAE |
| 4 | Test sets, participants | Baseline comparison, user study | Tests, SUS, time |

## 6. Acceptance rule
Mandatory (M) requirements are accepted when all their acceptance criteria pass. Q1–Q3 and Q5–Q6 are reported **whether or not** the hypotheses are confirmed; a failed hypothesis is reported honestly and discussed (no change of targets after seeing results). Results are stored in `docs/evidence/results/`.

## 7. Schedule (from the work plan; weeks of the semester)
| Weeks | Step | Output |
|---|---|---|
| 1–3 | Requirements, data plan, ethics application | doc 06, consent form |
| 4–8 | Database, API, map interface; synthetic data generators | working core |
| 5–9 | AI modules and baselines | model comparison table |
| 10–12 | User study | task logs, SUS |
| 13–14 | Analysis and final article | results report |

## 8. Threats to validity
| Threat | Handling |
|---|---|
| Synthetic data too easy | Add noise and irregular events; state results are indicative; test on real data if available |
| Small data (600 reports, 300 items) | Report confidence intervals, avoid over-claiming |
| Small and homogeneous participant group (students) | State; include residents if possible |
| Annotator bias | Two independent annotators, Cohen's kappa |
| Learning effect in within-subject design | Counterbalanced order |
