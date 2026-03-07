from typing import Annotated, List, Tuple, TypedDict, Union
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langchain_core.messages import BaseMessage, HumanMessage
import os

# Define the state for the multiagent system
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], "The messages in the conversation"]
    next_agent: str
    data_context: str

def supervisor(state: AgentState):
    """The Supervisor agent that decides which worker should act next."""
    # Logic to check if we need to query the data fabric
    return {"next_agent": "fabric_worker"}

def fabric_worker(state: AgentState):
    """Worker that interacts with Mjolnir-Fabric."""
    # Simulate querying Mjolnir-Fabric (Qdrant/LakeFS)
    # Future: Real integration via mjolnir_fabric client
    context = "Found 3 vulnerabilities in unencrypted S3 buckets via LakeFS metadata."
    return {"data_context": context, "next_agent": "analyst"}

def analyst(state: AgentState):
    """Analyst worker that processes the context."""
    context = state.get("data_context", "No data found.")
    last_message = state['messages'][-1].content
    response = f"Gungnir Analysis: Based on '{last_message}', I accessed Mjolnir-Fabric. {context}"
    return {"messages": [HumanMessage(content=response)], "next_agent": END}

# Initialize the graph
workflow = StateGraph(AgentState)
workflow.add_node("supervisor", supervisor)
workflow.add_node("fabric_worker", fabric_worker)
workflow.add_node("analyst", analyst)

workflow.set_entry_point("supervisor")
workflow.add_edge("supervisor", "fabric_worker")
workflow.add_edge("fabric_worker", "analyst")
workflow.add_edge("analyst", END)

# Compile the graph
gungnir_app = workflow.compile()
