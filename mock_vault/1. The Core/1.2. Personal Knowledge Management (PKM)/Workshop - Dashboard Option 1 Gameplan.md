---
aliases: [Dashboard Option 1 Gameplan, Dashboard CSS Strategy]
tags: [pkm, meta, projects, strategy, ui]
type: overview
---
**Back to:** [[Table of Contents]]

---

## Objective
Execute "Option 1" for the Nexus.0 Dashboard: Create a native Obsidian Markdown note powered by Dataview queries, and style it with a custom, premium CSS snippet to achieve a "Command Center" aesthetic (glassmorphism, clean typography, widget-based layout).

## PKM Philosophy: Structure vs. State (The "Why")
This dashboard is the architectural solution to the "TOC Clutter" dilemma. Currently, the `Table of Contents.md` acting as a Map of Content attempts to track two conflicting things:
1. **Structure (The Map):** Permanent domains, foundational PDFs, and master templates.
2. **State (The HUD):** Ephemeral items like active projects, currently running protocols, and reading lists.

By relying on the Dataview plugin to auto-surface the **State**, we can remove the ephemeral clutter from the TOC. The TOC becomes a pristine blueprint of the vault's structure (~150 lines), while this Dashboard instantly gives you the 0-click visibility required to maintain momentum on active tasks.

## The Markdown Structure (`Dashboard.md`)
The dashboard itself will just be standard markdown utilizing Dataview for dynamic data fetching, wrapped in strategic CSS classes to form a grid.

```html
<!-- We use standard HTML divs to apply the CSS grid layout -->
<div class="dashboard-grid">

  <!-- Column 1: Focus & Tasks -->
  <div class="dashboard-col">
    <div class="dashboard-card focus-card">
       <h3>Current Focus</h3>
       <!-- To be populated via dataview pulling from Current Learning -->
    </div>
    
    <div class="dashboard-card tasks-card">
       <h3>Top Priorities</h3>
       <!-- To be populated via dataview pulling from To Do List -->
    </div>
  </div>

  <!-- Column 2: The Core Pulse -->
  <div class="dashboard-col main-col">
     <div class="dashboard-card pulse-card">
        <h2 class="pulse-quote">"The only way out is through."</h2>
        <!-- Dataview query pulling a random quote from Goals.md -->
     </div>
  </div>

  <!-- Column 3: System Status -->
  <div class="dashboard-col">
    <div class="dashboard-card status-card">
       <h3>Next Protocol</h3>
       <!-- Status indicators for Brain Maintenance and Career Maintenance -->
    </div>
    
    <div class="dashboard-card projects-card">
       <h3>Active Projects</h3>
       <!-- To be populated via dataview pulling 'Project -' files -->
    </div>
  </div>

</div>
```

## The CSS Strategy (`.obsidian/snippets/dashboard-theme.css`)
We will create a dedicated snippet, load it via settings, and it will target the `.dashboard-grid` class to bypass standard Obsidian formatting constraints.

### Core Variables to Define
```css
:root {
  --bg-widget: rgba(30, 30, 36, 0.6); /* Glassmorphism base */
  --border-widget: rgba(255, 255, 255, 0.1);
  --accent-primary: #a154ff; /* Vivid Purple */
  --accent-secondary: #00e5ff; /* Electric Blue */
  --text-primary: #f0f0f0;
  --text-muted: #888888;
  --blur-amount: blur(12px);
}
```

### Key Elements to Style:
1. **The Grid Layout:** Use CSS `display: grid` with `@media` queries so it stacks nicely on the mobile app but expands to 3 columns on desktop.
2. **Glassmorphism Cards:** Apply `backdrop-filter: var(--blur-amount)` and `background-color: var(--bg-widget)` to give the dashboard widgets a high-end, transparent feel over the vault background.
3. **Typography:** Override standard Obsidian headers inside the dashboard to use a sleek tech font (e.g., `Inter` or `system-ui`), and add subtle text-shadows to headers for depth.
4. **Micro-animations:** 
    * Add a slow hover effect on the cards (`transform: translateY(-2px); box-shadow: 0 10px 20px rgba(0,0,0,0.2)`).
    * Make the "pulse-quote" glow softly.

## Required Plugin Installations
For this system to fully articulate, the user must install:
1. **[Dataview](https://github.com/blacksmithgu/obsidian-dataview):** Crucial for pulling in the lists automatically so the dashboard is zero-maintenance.
2. **(Optional but recommended) [CSS Snippets Enabler]:** Ensure the local CSS can be customized.

---

## Mobile Strategy & Agentic Futures
A Second Brain must be highly functional away from the desktop. Because this Dashboard uses native Dataview and CSS, it will securely sync and render perfectly on the Obsidian mobile app (stacking into a single responsive column). 

Looking forward, agentic tinkering on mobile will evolve through three distinct phases:
1. **Phase 1: Asynchronous Capture (Current):** Use the phone purely for raw dictation and unformatted info-dumping into `Quick Capture.md`. When returning to the desktop, trigger the `/audit_inbox` agent to read, format, and route the data.
2. **Phase 2: Hosted Endpoints (Near Future):** Moving the agent off the IDE onto a local home server or cloud instance connected to a WhatsApp/Telegram bot. This allows SMS-based requests from the phone (e.g., "Add spark plugs to the Pilot project") to edit the vault via API in real-time, which then syncs to the Obsidian app.
3. **Phase 3: Edge Agents (Long Term):** Leveraging on-device Small Language Models (like Gemini Nano) directly via an Obsidian mobile plugin to format and link notes purely offline, without a desktop agent.

---

## Future Super Charging (The "Next Level")
Once the base structure is up and running natively in Obsidian, here are ideas to integrate Agentic behaviors:

1. **Agentic Pulse Updating:** Have an agent periodically rewrite the `pulse-quote` by scanning recent journal entries and feeding them to an LLM to generate a personalized morning briefing.
2. **The "Start Work" Button:** Embed a local URI link (`obsidian://run-script...`) that fires the `/weekly_review` or an `audit_inbox` workflow directly from a button on the dashboard.
3. **Data Visualization:** Use the Obsidian Charts plugin or Mermaid (which is already installed) combined with Dataview to render an actual progress graph on the dashboard (e.g., showing job applications sent over the past 30 days based on CRM updates).
4. **Hybrid Evolution:** If the CSS/Markdown limits are hit, we migrate the *entire structure* to a local Next.js/React app running alongside Obsidian, turning this UI into an actual clickable mission control.

---
*Last updated: 2026-04-05*
