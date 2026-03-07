from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from gungnir_core.agent import gungnir_app
from langchain_core.messages import HumanMessage

app = FastAPI(title="Gungnir-Core Orchestrator", version="0.1.0")

class Query(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Gungnir-Core is operational. The All-Father watches."}

@app.post("/query")
async def handle_query(query: Query):
    # Run the LangGraph orchestration
    inputs = {"messages": [HumanMessage(content=query.text)], "data_context": ""}
    result = gungnir_app.invoke(inputs)
    
    # Extract the last message content
    final_response = result['messages'][-1].content if result['messages'] else "No response generated."
    context_found = result.get('data_context', 'No context')
    
    return {
        "status": "success",
        "query": query.text,
        "response": final_response,
        "context": context_found,
        "orchestrator": "Gungnir-LangGraph-v2"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
