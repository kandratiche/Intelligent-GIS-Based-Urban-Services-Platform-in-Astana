# Evidence of Progressive Contributions

Work from **every** team member must be visible over time, not one large commit before the deadline.

## Team
| Member | Group | Proposed main responsibility | YouTrack tasks |
|---|---|---|---|
| Arlan Aidarov | SE-2412 | AI modules (hazard classifier, matcher, parking predictor), data generation, evaluation | GIS-1, 3, 8, 10, 16, 19, 21, 23, 25, 28, 33, 35 |
| Ramazan Ashirbek | SE-2412 | Database, API, authentication, staff map, load tests | GIS-5, 6, 7, 12–15, 17, 24, 30–32, 36 |
| Kairat Bulatov | SE-2412 | Frontend forms, reservation, lost-and-found, system comparison, README | GIS-4, 9, 11, 18, 20, 22, 26, 27, 29 |
*(Roles for Kairat are proposed; confirm with the team and supervisor. The midterm proposal's plan names Ramazan for database/API/map and Arlan for the AI modules.)*

## Rules
1. `main` is protected; work in branches `feature/<module>-<name>`; merge via pull request with at least one review by another member.
2. Commit messages: `<type>(<scope>): <summary>` (for example `feat(reservation): add capacity check`).
3. Every commit/pull request references a YouTrack task (`GIS-18`).
4. Documents are committed in steps as they evolve.

## Generating evidence
```
git shortlog -sne --all
git log --since="2026-09-01" --pretty=format:"%h %an %ad %s" --date=short > docs/evidence/git-log.txt
```
Add screenshots of the repository contributors page and the YouTrack board (with assignees) to `docs/evidence/`.

## Contribution log
| Date | Member | Contribution | Link |
|---|---|---|---|
| TODO | | | |
