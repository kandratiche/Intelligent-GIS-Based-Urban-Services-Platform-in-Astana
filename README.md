# Astana City Map — Intelligent GIS-Based Urban Services Platform

A responsive, interactive front-end prototype for the Astana city-services concept. The implementation is aligned to the supplied six-page UX prototype PDF and the visible YouTrack project issue list (`DIP-2`–`DIP-18`).

## Start locally

Requirements: Node.js 20+ and npm.

```bash
npm install
npm run dev
```

For a production build:

```bash
npm run build
npm run preview
```

## Prototype screens and interactions

- **Map:** schematic Astana map with selectable parking markers, hazard overlays, wind-alert banner and selected-lot summary.
- **Parking:** occupancy legend, filters (free/filling/full/stale), camera-data timestamps, stale-data warning and sample occupancy history.
- **Hazards:** category filters and approved public reports.
- **Report a hazard:** category, location, description and optional sample-photo state; validates required fields and submits a pending report.
- **Weather:** wind alert, source timestamp and safety guidance.
- **Events:** sample events with status filtering.
- **Moderation:** approve/reject pending citizen hazard reports and events; decisions update the UI immediately.

All records are deterministic demo data held in client state. Refreshing the page resets changes. Authentication, file uploads, GPS, real map tiles, camera/weather feeds, persistence and server APIs are not connected; the UI explicitly uses illustrative/simulated data rather than claiming live service integration.

## Source of truth and project tracking

- `prototype/Astana-City-Map-UX-prototype.pdf` is the supplied UX prototype used for the current UI implementation. Page renders are in `prototype/pdf-pages/`.
- `docs/project-management/youtrack-visible-issues.md` transcribes the issue IDs and titles visible in the supplied YouTrack screenshot. The screenshot shows project key `DIP`, issues `DIP-2` through `DIP-18`; it does not expose issue descriptions, comments, attachments, or acceptance criteria.
- The existing academic documents and diagrams remain under `docs/`, `diagrams/`, and `pdf/`. Some older planning documents describe additional planned modules (reservation and lost-and-found) that are not present in this six-screen UX prototype; they are retained as future scope rather than falsely presented as implemented UI.

## Repository structure

```text
src/                 React + TypeScript application
  App.tsx             Pages and prototype interactions
  data/demo.ts        Sample parking, hazard and event records
  styles.css          Responsive styling matching the supplied UX PDF
prototype/            Original wireframes and supplied UX prototype PDF
prototype/pdf-pages/  Rendered pages of the supplied UX PDF
docs/                 Research, requirements, architecture and project-management docs
diagrams/             Editable diagram sources and exports
database/schema.sql   Existing proposed database schema
pdf/                  Existing academic deliverables
```

## Project context

**Project:** Intelligent GIS-Based Urban Services Platform in Astana

**Team shown in project documents:** Arlan Aidarov, Ramazan Ashirbek, Kairat Bulatov. **Supervisor:** Algys Saltanat. Astana IT University.

## Limitations

This repository contains a working UI prototype, not a deployed production GIS system. The map is a stylized schematic, and all values, alerts, timestamps, locations and events are illustrative. Do not treat the demo as a source of real-time safety or parking information.
