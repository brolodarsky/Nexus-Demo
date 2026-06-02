# Lesson 2 : LangGraph Components



from dotenv import load_dotenv
_ = load_dotenv()
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator
from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage, ToolMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
import json
from pygments import highlight, lexers, formatters

def format_to_json(data):
    def default_serializer(obj):
        if hasattr(obj, "dict"):
            return obj.model_dump()
        return str(obj)

    if isinstance(data, str):
        try:
            parsed_json = json.loads(data.replace("'", '"'))
        except (json.JSONDecodeError, AttributeError):
            parsed_json = data
    else:
        parsed_json = data

    formatted_json = json.dumps(parsed_json, indent=4, default=default_serializer)
    # Removing pygments highlighting so file redirection doesn't write raw ANSI escape codes
    return formatted_json

class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]


class Agent:

    def __init__(self, model, tools, system=""):
        self.system = system # System message
        graph = StateGraph(AgentState)
        graph.add_node("llm", self.call_openai)
        graph.add_node("action", self.take_action)
        graph.add_conditional_edges(
            "llm",
            self.exists_action, # Conditional check for action present
            {True: "action", False: END} # Dict maps how to map response of function to next node
        )
        graph.add_edge("action", "llm")
        graph.set_entry_point("llm")
        self.graph = graph.compile()
        self.tools = {t.name: t for t in tools}
        self.model = model.bind_tools(tools)

    def exists_action(self, state: AgentState):
        print("exists_action() called...")

        result = state['messages'][-1]

        print(f"state['messages'][-1]: {format_to_json(result)}")
        print(f"Tool calls: {format_to_json(result.tool_calls)}")
        print("End exists_action()\n")

        return len(result.tool_calls) > 0 # Return T/F if tool call is present

    def call_openai(self, state: AgentState):
        print("call_openai() called...")

        messages = state['messages']

        print(f"\ncall_openai() | messages:\n{format_to_json(messages)}\n")

        if self.system:
            print("\ncall_openai() | self.system: SYSTEM MESSAGE IS PRESENT\n")

            messages = [SystemMessage(content=self.system)] + messages
            print(f"\ncall_openai() | messages (updated): {format_to_json(messages)}")

        message = self.model.invoke(messages)

        print(f"\ncall_openai() | response from OpenAI: {format_to_json(message)}")
        print("End call_openai()\n")

        return {'messages': [message]}

    def take_action(self, state: AgentState):
        print("take_action() called....")

        tool_calls = state['messages'][-1].tool_calls # Tool call present on last message of AgentState

        print(f"Tool Calls:\n{format_to_json(tool_calls)}\n") # Added for debugging

        results = []
        for t in tool_calls:
            print(f"Calling:\n{format_to_json(t)}\n")
            result = self.tools[t['name']].invoke(t['args'])
            results.append(ToolMessage(tool_call_id=t['id'], name=t['name'], content=str(result)))

        print("End take_action()\n")
        return {'messages': results}

model = ChatOpenAI(model="gpt-5.4-nano")
tool = TavilySearch(max_results=2)
prompt = """You are a smart and concise research assistant. Use the search engine to look up information. \
You are allowed to make multiple calls (either together or in sequence). \
Only look up information when you are sure of what you want. \
If you need to look up some information before asking a follow up question, you are allowed to do that! \
Do not respond with markdown formatting or followup questions. \
Just answer the query.
"""
my_agent = Agent(model, [tool], system=prompt)

print("\n**********\n ITERATION 1 \n**********")
user_message = "What is the best career path for new CS grads right now, given the current market?"
print(f"Question: {user_message}")

messages = [HumanMessage(content=user_message)]
total_result = my_agent.graph.invoke({"messages": messages})
result = total_result['messages'][-1].content

print(f"\nResult: {type(total_result)}\n")
print(format_to_json(total_result))

print(f"\nFinal Result: {type(result)}\n")
print(result)

# print("\n**********\n ITERATION 2 \n**********")
# user_message = "What is the best career path for new CS grads right now in New Jersey, given the current market?"
# print(f"Question: {user_message}")

# messages = [HumanMessage(content=user_message)]
# result = my_agent.graph.invoke({"messages": messages})
# print("\n**********\nFinal Result:\n", result['messages'][-1].content, "\n**********")


# # Note, the query was modified to produce more consistent results. 
# # Results may vary per run and over time as search information and models change.

# query = "What is the current cost of a barrel of oil? \
# What is the current average price per gallon of regular unleaded gasoline in NJ? Answer each question." 
# messages = [HumanMessage(content=query)]

# model = ChatOpenAI(model="gpt-5.4-nano")  # requires more advanced model
# new_agent = Agent(model, [tool], system=prompt)
# result = new_agent.graph.invoke({"messages": messages})


# print("\n**********\nFinal Result:\n", result['messages'][-1].content, "\n**********")
