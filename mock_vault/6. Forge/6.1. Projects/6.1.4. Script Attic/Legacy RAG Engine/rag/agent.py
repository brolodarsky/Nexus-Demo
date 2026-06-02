import urllib.parse
from langchain_core.messages import HumanMessage
from .constants import CHROMA_PATH
from .graph import build_rag_graph

def execute_rag_query(query: str, thread_id: str = None, filters: dict = None) -> dict:
    """
    Core function to execute the RAG LangGraph agent and return the final state.

    Args:
        query:     The user's natural language question.
        thread_id: Optional thread ID for multi-turn continuity.
        filters:   Optional metadata filters (e.g. {"domain": "health", "tag": "medical"}).
    """
    app = build_rag_graph()
    
    config = {}
    if thread_id:
        config["configurable"] = {"thread_id": thread_id}
        
    initial_state = {
        "messages": [HumanMessage(content=query)],
        "context": [],
        "sources": [],
        "filters": filters or {},
    }
    
    return app.invoke(initial_state, config=config)

def run_ask_brain(query: str, filters: dict = None):
    """
    Standard interface for running the RAG agent and printing output.
    Used by CLI and Voice interfaces.
    """
    filter_parts = []
    if filters:
        for k, v in filters.items():
            if v:
                filter_parts.append(f"{k}={v}")

    filter_label = f" [{', '.join(filter_parts)}]" if filter_parts else ""
    print(f"\n[Nexus] Query: {query}{filter_label}\n")
    
    final_state = execute_rag_query(query, filters=filters)
    answer = final_state["messages"][-1].content
    
    print("=" * 60)
    print(answer)
    print("=" * 60)
    
    if final_state["sources"]:
        vault_name = urllib.parse.quote(CHROMA_PATH.parent.name)
        print("\n[Sources]")
        for src in dict.fromkeys(final_state["sources"]):
            # encoded = urllib.parse.quote(src.replace("\\", "/"))
            # obsidian_link = f"obsidian://open?vault={vault_name}&file={encoded}"
            print(f"  - {src}")
