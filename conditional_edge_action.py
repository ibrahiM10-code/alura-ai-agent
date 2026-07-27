from agent_state import AgentState

def decision_rag(state: AgentState) -> str:
    if state['rag_success']:
        return "success"
    return "error"