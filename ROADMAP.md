# 🗺️ LabsBakery Roadmap (version‑based, not date‑based)

> **Note:** This roadmap shows **what** we plan to build, not **when**.  Feature order can shift as the project—and contributors—evolve.

---

## 0.3.0 — Minimum Viable Pastry

* Stable drag‑and‑drop canvas
* Undo / redo & snap‑to‑grid
* Lifecycle REST API (`up`, `halt`, `status`, `destroy`)
* Generates `Vagrantfile` + `project.json`
* Unit tests & CI workflow
* Quick‑start docs in README

## 0.4.0 — Ingredient Marketplace

* **LabsBakery Box Registry** (open‑source images, checksummed)
* Template gallery inside UI (search, star, fork)
* Multipass provider plugin (Ubuntu cloud‑init)
* Provider abstraction refactor
* Basic analytics opt‑in (lab count, provider usage)

## 0.5.0 — Classroom Edition Alpha

* User roles: **Teacher / Student**
* Per‑student lab clones & auto‑teardown
* Embedded walkthrough & flag verification
* Gradebook export (CSV)
* Audit logs (who did what, when)

## 0.6.0 — Cloud Oven Beta

* **BakeryCloud** orchestrator (libvirt/KVM backend)
* Billing (Stripe) & auth (Supabase)
* Autosuspend idle labs; resume on demand
* CLI: `bakery login`, `bakery push`, `bakery deploy`

## 1.0.0 — General Availability

* Stable REST & WebSocket API (v1)
* Plugin SDK for custom providers & widgets
* UI/UX polish + accessibility pass (WCAG AA)
* Security audit & threat model
* Debian/Fedora image pipelines

---

## Parking‑Lot Ideas

*(Nice‑to‑haves, no promises)*

* OCI container backend (Docker Desktop, Podman)
* Terraform / Pulumi exporter
* AI “Lab Wizard” that generates starter topologies
* VS Code extension (graph view & live sync)
* Browser‑only web editor (no local install)
* Windows Hyper‑V provider

Contributions or suggestions? Open a discussion or issue—just tag it **`proposal`**.
