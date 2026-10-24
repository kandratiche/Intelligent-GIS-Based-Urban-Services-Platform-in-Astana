# Project Risks and Dependencies

## 1. Purpose

This document identifies the main risks and dependencies affecting the development of the Intelligent GIS-Based Urban Services Platform for Astana. It records each risk's probability, impact, mitigation strategy, and responsible owner. It also describes dependencies between project tasks and external parties.

The risk assessment is preliminary and should be reviewed as the project evolves.

## 2. Risk Assessment Method

Probability and impact are assessed on a three-level scale:

- **Low (L):** limited likelihood or limited effect on project delivery.
- **Medium (M):** a realistic possibility or a noticeable effect on scope, quality, or schedule.
- **High (H):** a likely occurrence or a major effect on project delivery.

The overall risk priority is estimated by combining probability and impact. High-priority risks should be reviewed first, followed by medium- and low-priority risks.

## 3. Risk Register

| ID | Risk | Probability | Impact | Mitigation strategy | Owner |
|---|---|---|---|---|---|
| R1 | Insufficient or unavailable data for training and evaluating AI modules | High | High | Identify available data sources early; use documented sample or synthetic data if real data cannot be obtained; clearly state limitations | AI/ML module owner |
| R2 | Poor data quality, missing fields, or inconsistent geographic information | Medium | High | Define data formats and validation rules; test representative examples; document data-cleaning steps | Data/GIS owner |
| R3 | AI classification or matching produces inaccurate results | Medium | High | Establish labelled test examples; evaluate using predefined metrics; compare against a simple baseline; document errors | AI/ML module owner |
| R4 | Parking prediction cannot be validated because suitable historical observations are unavailable | High | High | Define the prediction target early; investigate data availability; use an appropriate baseline and report limitations if only sample data are available | Parking module owner |
| R5 | Integration problems between the GIS interface, data storage, and AI modules | Medium | High | Define component interfaces; integrate incrementally; run integration tests after each major change | Technical lead |
| R6 | Scope expansion causes delays | Medium | High | Prioritize the three proposed modules; maintain a clear minimum viable prototype; approve major scope changes with the team | Project lead |
| R7 | Team members' schedules or task dependencies delay delivery | Medium | Medium | Track task status in YouTrack; identify blockers early; communicate changes and redistribute work when agreed | Project lead and task owners |
| R8 | External services, APIs, or data providers are unavailable or change their terms | Medium | Medium | Prefer documented interfaces; isolate external integrations; prepare a fallback or mock data source | Integration owner |
| R9 | User interviews or stakeholder feedback cannot be collected in time | Medium | Medium | Arrange discussions early; prepare concise questions; document recruitment limitations and avoid presenting assumptions as verified findings | Research owner |
| R10 | Privacy or security concerns arise when handling user-submitted reports or location data | Medium | High | Minimize personal data; use synthetic examples during development where appropriate; restrict access and document data-handling decisions | Project lead and data owner |
| R11 | The prototype is difficult for users to understand | Medium | Medium | Conduct usability checks with representative tasks; record errors and feedback; improve unclear workflows | UI/UX owner |
| R12 | Testing is incomplete before the final demonstration | Medium | High | Prepare a verification plan; reserve time for regression testing; record unresolved defects and avoid unsupported claims | Verification owner |

**Ownership note:** The role names above are proposed responsibilities, not confirmed assignments. Replace them with the actual team member names or agreed roles before final submission.

## 4. Risk Response and Monitoring

The team should review the risk register during project check-ins and whenever a major change affects scope, data availability, architecture, or schedule.

For each risk, the team should:

1. Check whether the risk has become more or less likely.
2. Record new evidence, blockers, or changes.
3. Confirm that the mitigation action has an owner.
4. Create or update a YouTrack task if follow-up work is needed.
5. Record whether the risk has occurred and what action was taken.

High-impact risks involving data availability, prediction validation, integration, and delivery schedule should receive particular attention.

## 5. Task Dependencies

The following dependencies describe the expected logical order of project work. The team should verify them against the current YouTrack board and the actual implementation plan.

| ID | Upstream task or condition | Dependent task or activity | Dependency | Consequence if delayed |
|---|---|---|---|---|
| D1 | Project proposal and scope | Requirements specification | Requirements must reflect the agreed project scope | Requirements may need rework |
| D2 | Literature review and existing-system comparison | Final feature prioritization | Existing approaches help justify the selected scope | Feature choices may lack sufficient justification |
| D3 | Technology comparison and architecture decisions | Implementation setup | Technology choices affect interfaces and development tools | Implementation may be delayed or require rework |
| D4 | Requirements specification | Verification and evaluation plan | Tests must map to defined requirements | Evaluation coverage may be incomplete |
| D5 | Data source identification and data preparation | AI module implementation and evaluation | Modules need suitable input data and reference values | AI features may be limited to demonstrations or sample data |
| D6 | GIS interface and data model | Integration of hazard, lost-item, and parking modules | Modules need agreed data formats and integration points | Components may not work together consistently |
| D7 | Implemented modules | Integration and functional testing | Tests require runnable components | Testing and defect resolution may be delayed |
| D8 | Implemented prototype | Usability evaluation | Participants need a working interface to evaluate | User feedback may arrive too late |
| D9 | Verification results | Final report and demonstration preparation | Claims about performance must be supported by observed results | Final conclusions may be incomplete |

These are logical dependencies and do not necessarily represent the official YouTrack issue IDs. Replace the descriptions with exact issue IDs when the team confirms the mapping.

## 6. External Dependencies

| External dependency | Why it matters | Potential risk | Planned response |
|---|---|---|---|
| Access to relevant urban or parking data | Supports realistic GIS displays and evaluation | Data may be unavailable, restricted, outdated, or incomplete | Investigate access conditions early; document alternatives |
| External API or service availability | May support maps, geocoding, or other integrations | Rate limits, service changes, or outages | Check documentation and terms; isolate dependencies; provide a fallback where feasible |
| Target-user availability | Enables interviews and usability feedback | Participants may not be available before the deadline | Schedule discussions early and record recruitment limitations |
| Supervisor or stakeholder feedback | Helps validate scope and priorities | Delayed feedback may cause rework | Share concise drafts and questions early |
| Team member contributions | Several project components must be integrated | Delayed or incompatible changes may block other work | Agree on interfaces, ownership, and review checkpoints |

No external organization or data provider should be described as a confirmed partner unless the team has established that relationship.

## 7. Critical Dependencies and Priorities

The following areas should be monitored closely:

1. **Data availability:** Confirm which datasets are actually accessible before promising measurable AI performance.
2. **Requirements and evaluation alignment:** Every important requirement should have a corresponding verification method.
3. **Module integration:** Agree on shared data formats and interfaces before combining components.
4. **User evidence:** Schedule interviews and usability checks early enough to influence requirements.
5. **Delivery schedule:** Keep the prototype scope realistic and leave time for testing and final corrections.

If an upstream task is delayed, the owner should inform the affected task owners and agree on whether to wait, use a documented fallback, or adjust the scope.

## 8. Assumptions and Limitations

This register is a planning document based on foreseeable project risks and logical dependencies. It is not a record of confirmed incidents, and the listed probability and impact levels are initial estimates.

The team should update risk ratings using actual project progress, available datasets, implementation results, and feedback from the supervisor or target users. Dependencies should be revised when the architecture or project schedule changes.

## 9. Conclusion

The main risks for the proposed platform concern data availability and quality, the evaluation of AI-supported functions, component integration, user feedback, and schedule management.

Identifying these risks early allows the team to prepare mitigations, assign responsibility, and avoid making claims that cannot be supported by the available evidence. Maintaining an up-to-date risk register and dependency list will help coordinate implementation, testing, and delivery of the prototype.