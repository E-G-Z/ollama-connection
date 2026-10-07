from fastapi import APIRouter
from pydantic import BaseModel
from src.infrastructure.llm_client import LLMClient
from src.application.chat import ChatUseCase
from src.application.executor import ActionExecutor

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat(req: ChatRequest):
    llm = LLMClient()
    executor = ActionExecutor(base_url="")
    use_case = ChatUseCase(llm, executor)

    result = use_case.execute(req.message)

    return {"response": result}