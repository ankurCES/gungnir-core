from typing import Annotated, List, Tuple, TypedDict, Union
from langgraph.graph import StateGraph, END
from langchain_core.messages import BaseMessage, HumanMessage
import os

# Configuration for Local vs Cloud reasoning
REASONING_MODE = os.getenv("REASONING_MODE", "cloud") # 'local' or 'cloud'
LOCAL_OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://host.docker.internal:11434")
LOCAL_MODEL = os.getenv("LOCAL_MODEL_ID", "qwen2.5-coder:7b")

# Define the state for the multiagent system
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], "The messages in the conversation"]
    next_agent: str
    data_context: str

def supervisor(state: AgentState):
    """The Supervisor agent that decides which worker should act next."""
    # In 'local' mode, we simulate the Thor/Loki local offloading logic
    return {"next_agent": "fabric_worker"}

def fabric_worker(state: AgentState):
    """Worker that interacts with Mjolnir-Fabric."""
    context = "Found 3 vulnerabilities in unencrypted S3 buckets via LakeFS metadata."
    if REASONING_MODE == "local":
        context += f" [Reasoned via Edge Model: {LOCAL_MODEL}]"
    return {"data_context": context, "next_agent": "analyst"}

def analyst(state: AgentState):
    """Analyst worker that processes the context."""
    context = state.get("data_context", "No data found.")
    last_message = state['messages'][-1].content
    response = f"Gungnir Analysis ({REASONING_MODE}): Based on '{last_message}', I accessed Mjolnir-Fabric. {context}"
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
