from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Gungnir-Core Orchestrator", version="0.1.0")

class Query(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Gungnir-Core is operational. The All-Father watches."}

@app.post("/query")
async def handle_query(query: Query):
    # Future: Integrate LangGraph Supervisor here
    return {"status": "received", "query": query.text, "agent": "Odin-Alpha"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
