from agent_state import AgentState
from rag import execute_rag

def consultar_rag(state: AgentState) -> AgentState:
    rag_response = execute_rag(question=state["question"])
    update_state: AgentState = {
        "question": rag_response["question"],
        "answer": rag_response["answer"],
        "rag_success": rag_response["success"]
    }
    
    return update_state

def get_respuesta_rag(state: AgentState) -> dict:
    if state["rag_success"]:
        return {
            "agent_response": state["answer"]
        }
        
def get_error_rag(state: AgentState) -> dict:
    if state["rag_success"] == False:
        return {
            "question": state["question"],
            "response": state["answer"] + "Couldn't get a proper response from the RAG.",
        }