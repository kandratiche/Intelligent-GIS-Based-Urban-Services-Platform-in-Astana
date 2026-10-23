# 1. Project Proposal and Scope

## Project title
**Intelligent GIS-Based Urban Services Platform in Astana**
*(working research title in the Midterm Research Proposal: "Development of an AI-Enhanced GIS-Based Smart City Platform for Integrated Urban Service Management in Astana")*

## Team and supervision
| Role | Name | Group |
|---|---|---|
| Team member (developer) | Arlan Aidarov (Айдаров Арлан Адилханулы) | SE-2412 |
| Team member (developer) | Ramazan Ashirbek (Аширбек Рамазан Толегенулы) | SE-2412 |
| Team member (developer) | Kairat Bulatov (Булатов Кайрат Булатович) | SE-2412 |
| Supervisor | Algys Saltanat | |
| University | Astana IT University | |

## Problem statement
Cities produce data from municipal databases, sensors, maps and citizen reports, but these data stay in separate systems, so urban services work as isolated tools instead of parts of one environment [1], [2]. Platform studies integrate data, but they are general or built for other cities and do not evaluate combined citizen services with AI modules; single-service studies give good methods, but each service has its own data and interface (see doc 03, research gap).

The problem investigated here is **the lack of tested, city-specific platforms that combine several citizen-facing location services with AI-based analysis on one GIS data model**. For Astana, the literature reviewed does not show such a platform.

> *Status of claims:* statements about the situation in Astana (for example that residents lose time looking for parking, or that reports are not handled well) are working hypotheses. Their verification is tracked in doc 02.

## Target users
1. **Drivers and residents** – look for parking and reserve a place.
2. **Citizen reporters** – report hazards (road damage, lighting, waste, snow and ice, other) with photo, GPS and text.
3. **Item owners and finders** – search and post lost and found items.
4. **City staff** – review reports, monitor parking load and use the decision-support map.
5. **Administrator** – manages users, roles and parking zones.

## Aim
To design, implement and evaluate a prototype of an AI-enhanced, GIS-based platform that integrates parking and reservation, hazard reporting and lost-and-found services on one data model, and to determine whether it performs better than baseline approaches on defined technical and user-oriented measures.

## Research question
To what extent does an AI-enhanced, GIS-based platform that integrates parking and reservation, hazard reporting, and lost-and-found services improve urban service analysis and decision support in Astana, compared with a baseline workflow?
Sub-questions: **SQ1** – how accurate are the three AI modules compared with simple non-AI baselines? **SQ2** – how do users rate usability and usefulness of the platform for completing service tasks?

## Objectives
1. Identify the data, functional, privacy and interoperability requirements for the four functions in Astana.
2. Design a common GIS data model and architecture with status and verification fields for sensor data and user reports.
3. Implement a prototype with three AI modules: hazard classification, lost-item matching, parking prediction.
4. Evaluate the prototype with technical and user-based measures against baselines in defined Astana scenarios, and record its limitations.

## Hypotheses
- **H1:** each AI module outperforms its baseline on held-out data — macro-F1 for hazard categories (baseline: keyword rules), top-5 retrieval rate for lost items (baseline: text filter), mean absolute error for 30-minute parking occupancy (baseline: historical average).
- **H2:** participants complete scenario tasks faster and with higher success on the platform than with the baseline workflow, and the mean SUS score exceeds 68.

## Scope
| Function | What it does |
|---|---|
| Parking availability and reservation | Map of parking zones with current and predicted (30 min) occupancy; reservation of a place for a time slot |
| Hazard reporting | Citizens submit reports (photo, GPS, text in Kazakh/Russian/English); AI suggests a category; staff verify |
| Lost-and-found search | Users post lost/found items; AI-assisted matching proposes top-5 candidates |
| Decision-support map for city staff | Map and statistics of reports, parking load and forecasts |

| AI module | Method (planned) | Baseline |
|---|---|---|
| Hazard-report classification | Multilingual pretrained text encoder + simple classifier, 5 categories | Keyword rules |
| Lost-item matching | Image embeddings from a pretrained network + text and location similarity | Text filter |
| Short-term parking prediction | Time-series regression, 30-minute horizon | Historical average |

## Out of scope
- Live deployment with the city, integration with real municipal systems.
- Other domains (energy, utilities, weather, events), full digital twin.
- Payments for parking; navigation/routing.
- Native mobile applications.

## Expected outcomes
- A shared GIS data model and a tested prototype showing how several citizen services and AI modules work on one platform.
- Measured accuracy of the three AI modules versus baselines (bootstrap confidence intervals).
- User-study results (task time, success, SUS, Likert items, themes) for 15–20 participants.
- Documented requirements, architecture, tests, and limitations; open repository.

## Scope realism and engineering complexity
| Area | Engineering content |
|---|---|
| Spatial data | PostGIS geometry types, spatial queries, GeoJSON API, common data model with status/verification fields |
| AI | Text classification (multilingual), image + text + location matching, time-series regression, evaluation with baselines |
| Backend | REST API, role-based access control, reservation logic with capacity checks, privacy layer |
| Frontend | Interactive map, forms, staff dashboard |
| Data | Synthetic data generation (parking series, reports, items), independent labelling and agreement (Cohen's kappa) |
| Evaluation | Technical tests, load tests, within-subject user study with statistical tests |

Open maps, open-source tools and **synthetic data** make the work feasible within one semester.

## Risks and mitigation
| Risk | Mitigation |
|---|---|
| Real municipal data unavailable | State assumptions, label synthetic data clearly, repeat key tests on real data if it becomes available |
| Synthetic data too easy / unrealistic | Generate from daily and weekly patterns with noise; report that results on synthetic data are indicative |
| Small user sample (15–20) | Use paired non-parametric tests where needed, report effect sizes, call results indicative |
| Privacy of photos and locations | No faces or number plates in images, aggregated location data, informed consent, anonymous responses |
| Scope too large for three people | Priorities (MoSCoW) in doc 06; reservation and staff statistics can be simplified first |
| Ethics approval delays user study | Do not collect participant data before approval; prepare consent form early |

## Work plan (from the Midterm Research Proposal; roles for Kairat to be confirmed)
| Weeks | Work | Responsible |
|---|---|---|
| 1–3 | Requirements | all |
| 4–8 | Database, API, map interface | Ramazan *(+ Kairat — to confirm)* |
| 5–9 | AI modules | Arlan *(+ Kairat — to confirm)* |
| 10–12 | User study | all |
| 13–14 | Analysis and article | all |

References [n] are listed in doc 03.
