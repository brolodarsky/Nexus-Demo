---
aliases: [Automated Maintenance Tracker Project, Sheets Tracker Built, Maintenance App Plan]
tags: [auto, project, sheets, tracking, dev]
type: plan
---

**Back to:** [[Table of Contents]]

---


This document outlines the requirements and build steps for building an automated car maintenance tracker, either via a macro-driven Google Sheet or a standalone application.

## 🎯 Objective
Create a living, low-friction tool that not only logs past maintenance (cost, date, odometer) but proactively calculates when future maintenance is due based on standardized mileage intervals for the 2005 Honda Pilot.

## 📱 Implementation Options

### Option A: Google Sheets (The "Lean" Builder)
- **Tech Stack:** Google Sheets, AppScript.
- **Pros:** Fast setup, native mobile app for entry, easy sharing.
- **Cons:** Limited UI customization, dependent on Google Ecosystem.

### Option B: Full-Blown App (The "Forge" Builder)
- **Tech Stack:** React/Next.js (Frontend), FastAPI/SQLite (Backend), or localized Mobile App.
- **Pros:** Premium UI/UX, push notifications, advanced data visualization, complete data sovereignty.
- **Cons:** Higher development overhead, maintenance of a separate codebase.

## 📋 Core Requirements (Agnostic)
- **Inputs Required:** Date, Service Description, Current Odometer, Cost, Shop/Location.
- **Calculated Outputs:** 
  - `Next Service Odometer` (Current + Interval)
  - `Miles Until Due` (Next Service - Latest Logged Odometer)
- **Features:**
  - Conditional formatting/alerts (e.g., UI turns red when `Miles Until Due` < 500).
  - Clean, mobile-friendly interface (since inputs happen at the mechanic).
  - Data Export/Backup (CSV).

## 🪜 Implementation Steps

### Phase 1: Structure & Schema
- [ ] Define the core `Log` schema: Date | Odometer | Service | Notes | Cost.
- [ ] Define the `Intervals` reference (Oil = 3k, Tires = 10k, Trans Fluid = 30k).

### Phase 2: Logic & Development
- **If Option A (Sheets):**
  - [ ] Build the `Dashboard` tab to query the `Log`.
  - [ ] Write AppScript for reminders and logic.
- **If Option B (App):**
  - [ ] Initialize the project (e.g., `npx create-next-app`).
  - [ ] Build the CRUD (Create, Read, Update, Delete) functionality for maintenance logs.
  - [ ] Implement service interval logic in the backend/frontend.

### Phase 3: Polish & Deployment
- [ ] Apply styling and UI alerts.
- [ ] Test data entry on a mobile device.
- [ ] Link the tracker output to the [[Maintenance Log]] note in the Vault.

## 🔗 Resources & Notes
*   *Link to AppScript documentation for sending email triggered reminders (if needed later).*
*   *Link to common Honda Pilot factory maintenance schedule thresholds.*
