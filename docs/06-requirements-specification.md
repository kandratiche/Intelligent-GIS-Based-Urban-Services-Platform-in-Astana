# 6. Requirements Specification

Priorities: **MoSCoW** — M must, S should, C could. "Source": where the requirement comes from (proposal objective, literature, or *assumption* to be re-checked in doc 02). Every mandatory requirement has an acceptance criterion that can be tested (doc 09 gives the test IDs).

## 1. Roles
Driver/resident, Citizen reporter, Item owner/finder (all three are "registered users"), City staff, Administrator. Anonymous visitors may view the public parking map only.

## 2. Functional requirements

### 2.1 Parking and reservation (P, R)
| ID | Requirement | Pri. | Acceptance criterion | Source | Test |
|---|---|---|---|---|---|
| FR-P1 | The system shall show parking zones on the map with capacity and current free places | M | For all seeded zones, the popup shows capacity, free places and time of last observation | Obj. 1, A1 | T-P1 |
| FR-P2 | The system shall show the predicted occupancy 30 minutes ahead for each zone | M | Forecast is shown for every zone; label says "forecast" and model version | Obj. 3, H1 | T-P2 |
| FR-P3 | Parking data shall be marked as real or synthetic | M | Each zone has `data_source`; UI shows "synthetic data" when applicable | Proposal (risk handling) | T-P3 |
| FR-P4 | Staff shall see parking load and forecasts for all zones | S | Staff view lists zones sorted by occupancy with forecast | Obj. 1 | T-P4 |
| FR-R1 | A registered driver shall reserve a place in a zone for a time slot | M | With free capacity the reservation is saved with status "confirmed"; user receives confirmation | Assumption A2 | T-R1 |
| FR-R2 | The system shall reject a reservation if capacity for the slot is exhausted, and suggest other zones | M | With a full zone, request is rejected; no overbooking in 50 concurrent requests test | Obj. 2 | T-R2 |
| FR-R3 | A driver shall cancel own reservation | M | Cancelled reservation frees capacity immediately | Assumption | T-R3 |
| FR-R4 | Reservations shall expire after a no-show period | C | Reservation older than limit is set to "expired" | Assumption | T-R4 |

### 2.2 Hazard reporting (H)
| ID | Requirement | Pri. | Acceptance criterion | Source | Test |
|---|---|---|---|---|---|
| FR-H1 | A registered user shall submit a report with photo, GPS point (map selection) and text | M | Valid report is stored; report without location is rejected with a message | [11], A3 | T-H1 |
| FR-H2 | Report text may be in Kazakh, Russian or English | M | Reports in all three languages are accepted and classified | A4 | T-H2 |
| FR-H3 | The system shall suggest one of five categories (road damage, lighting, waste, snow and ice, other) with a confidence value | M | On the held-out test set macro-F1 is above the keyword-rule baseline (H1); suggestion and confidence shown in API/UI | Obj. 3, H1 | T-H3 |
| FR-H4 | Staff shall confirm or correct the category and set the report status (new, in review, resolved, rejected) and verification status | M | Changes are stored with reviewer and time; history visible | [12] | T-H4 |
| FR-H5 | The reporter shall see the status of own reports | M | Status shown in "my reports" within 5 s after staff change | [13], A3 | T-H5 |
| FR-H6 | Reports shall appear on the staff map with filters by category, status, date | M | Filtering returns exactly matching reports | Obj. 1 | T-H6 |
| FR-H7 | Photos shall be checked so that faces and number plates are not published | S | Public views never show original photos of people/plates; policy documented and tested on test images | [15], NFR-S2 | T-H7 |

### 2.3 Lost-and-found (L)
| ID | Requirement | Pri. | Acceptance criterion | Source | Test |
|---|---|---|---|---|---|
| FR-L1 | A registered user shall post a lost or found item (category, text, photo, location, time) | M | Valid record saved; ten categories available | [20], A5 | T-L1 |
| FR-L2 | The system shall return the top-5 candidate matches for a record, using image, text and location | M | On the test pairs, top-5 retrieval rate is above the text-filter baseline (H1) | Obj. 3, H1 | T-L2 |
| FR-L3 | Users shall filter items by category, date and area | S | Filter returns exactly matching items | Assumption | T-L3 |
| FR-L4 | Owner and finder shall confirm or reject a proposed match; status is stored | S | Match status changes to confirmed/rejected; item closes when confirmed | [12] | T-L4 |
| FR-L5 | Contact details shall not be public; contact happens through the platform | M | Public API never returns contact data | [15] | T-L5 |

### 2.4 Decision-support map for staff (S)
| ID | Requirement | Pri. | Acceptance criterion | Source | Test |
|---|---|---|---|---|---|
| FR-S1 | Staff shall see one map with layers: hazard reports, parking zones, lost-and-found items | M | Layers can be switched on/off independently | A6, Obj. 1 | T-S1 |
| FR-S2 | The map shall show report density (clusters or heatmap) and counts by category | S | Counts equal database counts for the selected filters | [3] | T-S2 |
| FR-S3 | Staff shall export a summary (CSV) of filtered reports | C | CSV contains the filtered rows | Assumption | T-S3 |
| FR-S4 | Location data in staff statistics shall be aggregated | M | Statistics show aggregated areas, not exact personal locations | [15], ethics | T-S4 |

### 2.5 Common (C)
| ID | Requirement | Pri. | Acceptance criterion | Source | Test |
|---|---|---|---|---|---|
| FR-C1 | Registration, login and role-based access (driver/reporter/finder, staff, administrator) | M | Staff and admin endpoints return 403 for other roles | [15] | T-C1 |
| FR-C2 | One common spatial data model with status and verification fields for sensor data and user reports | M | Schema review: all entities have geometry (where applicable), status, verification fields (doc 07) | Obj. 2 | T-C2 |
| FR-C3 | Administrator manages parking zones and users | M | Zone create/edit/delete and role change work | Obj. 1 | T-C3 |
| FR-C4 | Documented REST API (OpenAPI) | S | `/docs` lists all endpoints | doc 05 | T-C4 |
| FR-C5 | Interface in English; Russian and Kazakh as extension | S | UI strings are externalised; at least two languages in the final version | A4 | T-C5 |

## 3. Non-functional requirements
| ID | Category | Requirement | Pri. | Acceptance criterion | Test |
|---|---|---|---|---|---|
| NFR-A1 | AI accuracy | Hazard classifier beats keyword rules (macro-F1), lost-item matcher beats text filter (top-5), parking predictor beats historical average (MAE) | M | Results on held-out test sets with bootstrap CI (H1) | T-A1 |
| NFR-A2 | AI transparency | Each AI output shows confidence/score and can be overridden by staff or user | M | Inspection of UI/API | T-A2 |
| NFR-P1 | Performance | API response time under simulated load | M | Median ≤ 300 ms and 95th percentile ≤ 1 s for list/map endpoints at 50 concurrent users | T-N1 |
| NFR-P2 | Performance | AI inference time | S | Hazard classification ≤ 1 s, lost-item matching ≤ 3 s per query on demo hardware | T-N2 |
| NFR-U1 | Usability | Mean SUS above the average of 68 | M | SUS from the user study | T-U1 |
| NFR-U2 | Usability | Task success and time better than baseline workflow | M | Paired test over four tasks (H2) | T-U2 |
| NFR-U3 | Transparency | Every status, forecast and AI suggestion shows source/time or confidence | M | Manual inspection | T-U3 |
| NFR-U4 | Usability | Responsive layout | S | Usable at 360 px width | T-U4 |
| NFR-S1 | Security | Hashed passwords, token expiry, input validation, role checks | M | Tests: no plaintext passwords; injection attempts rejected; 403 tests | T-S5 |
| NFR-S2 | Privacy | No faces or number plates in images; aggregated location data; anonymous user-study responses | M | Review checklist and tests | T-S6 |
| NFR-D1 | Data | Synthetic data are generated reproducibly and labelled; generator code and seed in the repository | M | Re-running generator gives identical datasets | T-D1 |
| NFR-D2 | Data | Hazard labels by two independent annotators; agreement reported (Cohen's kappa) | M | Kappa computed and reported | T-D2 |
| NFR-R1 | Reliability | Failure of an AI module must not break the rest of the platform | S | Stop each module; remaining functions work | T-R5 |
| NFR-M1 | Maintainability | Automated tests for backend logic | S | ≥ 60 % line coverage on backend | T-M1 |
| NFR-C1 | Constraint | Only open-source tools and open/synthetic data; no live deployment; no payments | M | Licence list and review | review |

## 4. Traceability
| Objective | Requirements |
|---|---|
| 1. Requirements | FR-P1, FR-H1, FR-L1, FR-S1, doc 02 |
| 2. Data model and architecture | FR-C2, FR-R2, NFR-S1, NFR-S2 |
| 3. AI modules | FR-P2, FR-H3, FR-L2, NFR-A1, NFR-A2 |
| 4. Evaluation | NFR-A1, NFR-P1, NFR-U1, NFR-U2, doc 09 |

## 5. Open questions
1. Reservation rules: maximum duration, no-show period, cancellation (decide after interview D1).
2. Exact hazard categories and ontology (confirm after D2/D4).
3. Which authentication method (e-mail, university account).
4. Ethics approval procedure for the user study.
