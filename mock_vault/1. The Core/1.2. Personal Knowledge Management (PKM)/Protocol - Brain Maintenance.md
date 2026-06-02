---
aliases: [Maintenance Checklist, Vault Cleanup, System Admin]
tags: [maintenance, system, admin]
type: overview
---
**Back to:** [[Table of Contents]]

---


Use this note to track recurring administrative and maintenance tasks for Nexus.0.

> [!important] Recommendation
> Run through this checklist periodically to keep the system, the project files, and the repository in sync.

## Weekly Maintenance Checklist

- Sync [Google Keep Notes](https://keep.google.com/u/0/#home) with Nexus.

## Monthly Maintenance Checklist

- [ ] **[[Protocol - Hard Drive Backup]]**
  - Execute the FreeFileSync batch jobs to back up the system locally.
- [ ] **Run `/audit_inbox` Workflow**
  - Run the `audit_inbox` workflow to process any lingering thoughts or documents in `5.1. Brain Dump & Inbox`.
  - Approve the agent's routing plan to keep the inbox at zero.
- [ ] **Run `cleanup_orphans` Agent Skill**
  - Ask an agent to "run the cleanup orphans skill".
  - Review the agent's report.
  - Fix any broken `[[wiki-links]]`.
  - Delete or populate any empty folders (ignoring `.gitkeep`).
- [ ] **Review `README.md` and `AGENTS.md`**
  - Ensure any new scripts or workflows created this month are documented.
- [ ] **Verify Python Environment**
  - Ensure `.venv` is healthy and `requirements.txt` is strictly in sync with actual usage.
