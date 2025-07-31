# Project Development Plan: Children Without a Horizon

This plan outlines the concrete steps to build and refine the "Children Without a Horizon" web project. It covers technical tasks, content creation, design, and deployment. Use this as an evolving roadmap to track progress and guide your workflow.

---

## 1. Evaluate & Polish the Foundation

- [x] Review current directory structure and files.
- [x] Ensure homepage and initial dashboard (education) load and render as intended.

---

## 2. Data & Dashboard Development

- [ ] **A. Complete Dashboards**
  - [ ] Implement `dashboards/health.html` using health/nutrition indicators from `child_indicators.csv`.
  - [ ] Expand or add `global_compare.html` for broader country/indicator exploration.
  - [ ] Check dashboard links and remove duplicates in navigation.

- [ ] **B. Automate Data Handling**
  - [ ] Implement `src/fetch_data.py` to download source data (e.g., from UNICEF, World Bank).
  - [ ] Implement `src/transform_data.py` to clean and format data, outputting ready-to-use CSVs.
  - [ ] Implement `src/build_charts.py` to automate chart creation or prepare data visualizations.
  - [ ] Add a Makefile or shell script to run the full data pipeline.

---

## 3. Content & Narrative

- [ ] Write and publish essays:
  - [ ] `essays/fog_of_potential.html` — Reflect on childhood potential and systemic barriers.
  - [ ] `essays/classroom_lifeline.html` — Describe the classroom's transformative power.

- [ ] Integrate emotion and explanation into dashboards:
  - [ ] Add short quotes, headlines, or “Did you know?” facts to each dashboard.
  - [ ] Write brief explanatory captions linking statistics to lived experience.

---

## 4. UX, Visuals, and Internationalization

- [ ] **A. Visual Design**
  - [ ] Add a project logo and hero image in `static/images/`.
  - [ ] Refine mobile responsiveness, accessibility, and readability.
  - [ ] Ensure visual harmony across dashboards and essays.

- [ ] **B. Internationalization**
  - [ ] Expand language toggle to fully support English and Portuguese content.

---

## 5. Deployment & Documentation

- [ ] Add meta tags, favicon, and basic SEO to `index.html`.
- [ ] Prepare project for static deployment (e.g., GitHub Pages).
- [ ] Update `README.md` with:
  - [ ] Local development instructions.
  - [ ] Data update pipeline instructions.
  - [ ] Static site deployment steps.

---

## 6. Maintenance & Expansion

- [ ] Set up a way to track issues, improvements, and ideas (GitHub Issues, TODO.md, etc.).
- [ ] Consider collecting feedback from users/viewers for future iterations.
- [ ] Plan for regular updates of datasets and essays.

---

## Immediate Next Steps

1. Implement the health dashboard in `dashboards/health.html`.
2. Draft and add content for at least one essay.
3. Begin filling in the Python scripts for data automation.
4. Refine navigation and dashboard links.

---

**Keep this plan updated as you progress!**
