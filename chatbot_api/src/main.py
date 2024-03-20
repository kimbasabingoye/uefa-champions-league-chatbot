from fastapi import FastAPI
from agents.ucl_rag_agent import ucl_rag_agent_executor
from models.ucl_rag_query import UclQueryInput, UclQueryOutput
from utils.async_utils import async_retry

app = FastAPI(
    title="UEFA Chmpions League 2023-2024 Chatbot",
    description="Endpoints for a UCL 2023-2024 system graph RAG chatbot",
)


@async_retry(max_retries=10, delay=1)
async def invoke_agent_with_retry(query: str):
    """
    Retry the agent if a tool fails to run. This can help when there
    are intermittent connection issues to external APIs.
    """

    return await ucl_rag_agent_executor.ainvoke({"input": query})


@app.get("/")
async def get_status():
    return {"status": "running"}


@app.post("/ucl-rag-agent")
async def ask_ucl_agent(query: UclQueryInput) -> UclQueryOutput:
    query_response = await invoke_agent_with_retry(query.text)
    query_response["intermediate_steps"] = [
        str(s) for s in query_response["intermediate_steps"]
    ]
    return query_response
