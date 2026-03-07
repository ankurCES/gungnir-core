from typing import Annotated, List, Tuple, TypedDict, Union
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langchain_core.messages import BaseMessage, HumanMessage

# Define the state for the multiagent system
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], "The messages in the conversation"]
    next_agent: str

def supervisor(state: AgentState):
    """The Supervisor agent that decides which worker should act next."""
    # Future: Real logic with a model
    # For now, it just passes to the orchestrator worker
    return {"next_agent": "worker"}

def worker(state: AgentState):
    """A worker agent that performs specific tasks."""
    last_message = state['messages'][-1].content
    response = f"Gungnir worker processed: {last_message}. The Spear is true."
    return {"messages": [HumanMessage(content=response)], "next_agent": END}

# Initialize the graph
workflow = StateGraph(AgentState)
workflow.add_node("supervisor", supervisor)
workflow.add_node("worker", worker)

workflow.set_entry_point("supervisor")
workflow.add_edge("supervisor", "worker")
workflow.add_edge("worker", END)

# Compile the graph
gungnir_app = workflow.compile()
