---
title: "Project - StockBot"
aliases: [StockBot, Autonomous Inventory Refill Agent]
tags: [projects, ai-agents, langgraph, automation]
type: project
created: 2026-05-08
---
**Engine Directory:** `engine/agents/stockbot`

**Back to:** [[Project - Nexus Agentic Engine]]

# StockBot: Autonomous Inventory Refill Agent

An AI agent that monitors a local database, checks Amazon Business for pricing/stock, and automatically triggers procurement requisitions.

---

## 🏗️ Architecture Overview

1.  **State Manager (LangGraph):** Controls the flow from "Checking DB" to "Placing Order."
2.  **Inventory (Supabase/Postgres):** Tracks your current stock levels and thresholds.
3.  **Procurement (Amazon Business API):** Programmatically searches and orders items.
4.  **Human-in-the-Loop:** Optional breakpoint for orders exceeding a price limit.
5.  **Task Management & Master Sync:** Maintains a local `To Do - StockBot.md` file in its local directory and synchronizes pending restocking tasks bi-directionally with the global [[To Do List|Master To Do List]].

---

## 🛠️ The Tech Stack

*   **Orchestrator:** LangGraph
*   **LLM:** Claude 3.5 Sonnet or GPT-4o
*   **Database:** Supabase (Postgres)
*   **Shopping API:** Amazon Business API (via SP-API framework)
*   **Environment:** Python 3.10+

---

## 📊 1. Database Schema (SQL)

```sql
CREATE TABLE inventory (
    id SERIAL PRIMARY KEY,
    item_name TEXT NOT NULL,
    asin TEXT UNIQUE NOT NULL, -- Amazon Standard Identification Number
    current_qty INT DEFAULT 0,
    min_threshold INT NOT NULL,
    max_refill_price DECIMAL(10, 2),
    last_ordered_date DATE
);

-- Example Data
INSERT INTO inventory (item_name, asin, current_qty, min_threshold, max_refill_price)
VALUES ('AA Batteries 48pk', 'B00MNV8E0C', 5, 10, 25.00);
```

---

## 🤖 2. The LangGraph Logic (Conceptual Python)

```python
import operator
from typing import Annotated, TypedDict, List
from langgraph.graph import StateGraph, END

# 1. Define the Agent State
class AgentState(TypedDict):
    low_stock_items: List[dict]
    purchase_results: List[dict]
    requires_approval: bool

# 2. Node: Check Inventory
def check_inventory(state: AgentState):
    # Logic: SELECT * FROM inventory WHERE current_qty < min_threshold
    # Return list of items to refill
    return {"low_stock_items": [{"asin": "B00MNV8E0C", "qty": 1}]}

# 3. Node: Price Check (Amazon API)
def check_amazon_price(state: AgentState):
    # Logic: Call Amazon Business Search API for current price
    # Compare with max_refill_price in DB
    return {"requires_approval": False} # or True if price spiked

# 4. Node: Execute Purchase
def place_order(state: AgentState):
    # Logic: Call Amazon Business Purchase API
    # Create a requisition (Auto-approved if under your Amazon account limit)
    return {"purchase_results": [{"status": "success", "order_id": "123-456"}]}

# 5. Build the Graph
workflow = StateGraph(AgentState)

workflow.add_node("inventory_check", check_inventory)
workflow.add_node("price_check", check_amazon_price)
workflow.add_node("order_exec", place_order)

workflow.set_entry_point("inventory_check")
workflow.add_edge("inventory_check", "price_check")

# Conditional: Approve or Buy
workflow.add_conditional_edges(
    "price_check",
    lambda x: "human_approval" if x["requires_approval"] else "order_exec",
    {"human_approval": END, "order_exec": "order_exec"}
)

workflow.add_edge("order_exec", END)
app = workflow.compile()
```

---

## 🔑 3. Amazon Business API Configuration

To make this "Automatic," configure your **Amazon Business Account Settings**:

1.  **Direct Purchasing API:** Request the `Product Search` and `Purchase` scopes in the Developer Console.
2.  **Approval Rules:** 
    *   Go to **Business Settings** > **Buying Policies**.
    *   Set an **Approval Policy**: "Individual orders under $50.00 are automatically approved."
3.  **Authentication:** The agent must handle OAuth2.0 tokens to refresh the session without your intervention.

---

## 🚀 Execution Workflow

1.  **Scheduled Trigger:** A GitHub Action or Cron job runs the LangGraph agent every Monday at 8:00 AM.
2.  **Scout:** The agent identifies you are out of Printer Paper.
3.  **Verify:** It checks Amazon; price is $12.99 (matches your DB rule of <$15.00).
4.  **Purchase:** The agent calls the Purchase API.
5.  **Refill:** Amazon's internal rule auto-approves the request. 
6.  **Notify:** The agent pings your Slack: *"Ordered 1x Printer Paper. Expected delivery: Wednesday."*
