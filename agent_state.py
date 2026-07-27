from typing import TypedDict

class AgentState(TypedDict):
    question: str
    answer: str
    rag_success: bool