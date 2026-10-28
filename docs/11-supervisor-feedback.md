# 11. Supervisor Feedback and How It Was Addressed

**Supervisor:** Algys Saltanat

## 1. Meeting / Review Log

| # | Date | Format | Materials Shown | Attendees |
|---|---|---|---|---|
| 1 | 24 October 2026 | Project progress review | Project topic, scope, research question and objectives | Supervisor and project team |
| 2 | 24 October 2026 | Requirements review | Research proposal, technology comparison and functional requirements (docs 01–06) | Supervisor and project team |
| 3 | 24 October 2026 | Technical review | System diagrams, interface wireframes and verification plan (docs 07, 09) | Supervisor and project team |

## 2. Feedback and Response

| # | Deliverable | Supervisor Comment | Decision | Change Made (File / Commit / Task) | Status |
|---|---|---|---|---|---|
| 1 | Project scope and requirements | The project scope should remain realistic for a team of three developers. The team should prioritise the core urban-service functions before implementing advanced AI features. | Prioritise the main user workflows and treat the three AI modules as separate components that can be implemented and evaluated incrementally. | Requirements documentation and project task board | Planned |
| 2 | Data strategy and parking prediction | If reliable real-world parking data is unavailable, synthetic data may be considered for initial testing, provided that its limitations are clearly explained. | Use synthetic data only for prototype development and preliminary testing. Document the data-generation approach and avoid presenting synthetic-data results as evidence of real-world accuracy. | Data design documentation and evaluation plan | Planned |
| 3 | Technology comparison | The backend framework should be selected based on project requirements, development time, integration needs and the team's existing skills. | Compare FastAPI and Django REST Framework using the same criteria and document the reasons for the final choice before backend implementation. | Technology comparison document (doc 05) | In progress |

## 3. Questions to Bring to the Supervisor

1. Is the scope of four service functions and three AI modules acceptable for a team of three developers?
2. Is synthetic parking data acceptable for prototype testing if real data cannot be obtained?
3. Which backend framework is more appropriate for this project: FastAPI or Django REST Framework?
4. What ethics approval is required for the planned user study, and when should the application be submitted?
5. What level of user or stakeholder consultation would be sufficient for the project requirements?

## 4. Follow-up Actions

The team will refine the functional requirements, prioritise the core prototype workflows and document the limitations of the available data. The technology comparison will be completed before the backend framework is finalised. The system diagrams and verification plan will also be reviewed to ensure consistency with the implementation.

The team will track the resulting changes through repository commits and project tasks. Evaluation results will be reported only after the relevant tests have been completed.

