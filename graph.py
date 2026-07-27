from node_actions import consultar_rag, get_error_rag, get_respuesta_rag
from langgraph.graph import START, END, StateGraph
from conditional_edge_action import decision_rag
from agent_state import AgentState
import gradio as gr

workflow = StateGraph(AgentState)

workflow.add_node("consultar_rag", consultar_rag)
workflow.add_node("recibir_respuesta_rag", get_respuesta_rag)
workflow.add_node("recibir_error_rag", get_error_rag)

workflow.add_edge(START, "consultar_rag")
workflow.add_conditional_edges(
    "consultar_rag",
    decision_rag,
    {
        "success": "recibir_respuesta_rag",
        "error": "recibir_error_rag"
    }
)
workflow.add_edge("recibir_respuesta_rag", END)
workflow.add_edge("recibir_error_rag", END)

graph = workflow.compile()

def run_graph(question):
    response_graph = graph.invoke({"question": question})
    return response_graph["answer"]

custom_css = """
.container-centrado {
    max-width: 650px !important;
    margin: 40px auto !important;
}
"""

with gr.Blocks(theme=gr.Theme.from_hub("NeoPy/shadowthedgehog"), css=custom_css) as interface:
    
    with gr.Column(elem_classes="container-centrado"):
        gr.Markdown("# Agente del Colegio Nexo Digital")
        gr.Markdown("Responde a cualquier pregunta que tengas sobre las políticas y/o reglamento del colegio.")
        
        input_texto = gr.Textbox(
            label="Escribe tu pregunta", 
            placeholder="Ej: ¿Cuál es el código de conducta y convivencia?",
            lines=2
        )
        
        btn_enviar = gr.Button("Enviar pregunta", variant="primary")
        
        output_texto = gr.Textbox(
            label="Respuesta del Agente", 
            interactive=False,
            lines=4
        )
        
        btn_enviar.click(
            fn=run_graph,
            inputs=input_texto,
            outputs=output_texto
        )

interface.launch()