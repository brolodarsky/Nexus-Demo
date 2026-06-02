---
aliases: [Agentic Law Startup, John's Startup Idea]
tags: [projects, startup, legal-tech, ai-agents]
type: workshop
---
**Back to:** [[Table of Contents#6.1. Projects|Table of Contents]]

## 1. The Partnership & Compensation
Since your buddy is currently broke, you are trading your technical labor for **sweat equity**. You need to formalize this early to avoid "founder fallout."

*   **Equity Split:** Discuss ownership percentages now. If you are building the entire technical core, you are a Co-Founder, not a contractor.
*   **Vesting Schedule:** Propose a 4-year vest with a 1-year cliff. This ensures everyone stays committed or loses their shares.
*   **Role Definition:** Clarify the "Business" major’s output. He should be handling market research, legal compliance, and entity formation while you code.
*   **The "Hobby" vs "Company" Talk:** Gauge his long-term commitment. Does his excitability survive a 3-month period with zero sales?

---

## 2. Strategic "Legal Tech" Reality Check
The legal field is high-stakes; "mostly right" is "completely wrong."

*   **Hallucination is Fatal:** In law, AI mistakes lead to disbarment. You must build "Human-in-the-loop" systems where the AI drafts, but a lawyer verifies.
*   **Security & Privacy:** Law firms have a fiduciary duty to protect data. You cannot use "out of the box" consumer AI settings. You need SOC2 compliance and private data silos.
*   **Workflow > RAG:** Simple "Chat with PDF" is a commodity. Real value lies in **Agentic Workflows** (e.g., automated discovery, contract redlining, or conflict checks).

---

## 3. Managing the "Excitable" Founder
ADHD/Excitable founders provide great energy but can cause "feature creep" that kills projects.

*   **The "Icebox":** Create a document where all his "2 AM ideas" go. Only move them to development after a feasibility and value assessment.
*   **Sprint Cycles:** Keep him focused on one goal per week (e.g., "This week we only talk about document ingestion").
*   **Weekly Demos:** Show him tangible progress frequently to keep his excitement fueled by reality rather than fantasy.

---

## 4. Technical Learning Path (RAG & LangChain)
Transition from basic RAG to Agentic RAG.

*   **Frameworks:** Move from basic LangChain to **LangGraph**. Agents need to be able to loop, self-correct, and use tools.
*   **Evaluation (LLM-as-a-judge):** Use tools like **RAGAS** or **LangSmith** to measure accuracy. If you can't measure your RAG's performance, you can't sell it to a law firm.
*   **Parsing:** Master high-quality PDF parsing (e.g., Unstructured.io). Legal documents are messy; the RAG is only as good as the text you feed it.

---

💡 **Key Anchor:** Success depends on balancing his vision with your technical skepticism. Do not build until you have defined a "Smallest Possible Product" that a lawyer would actually pay for.
