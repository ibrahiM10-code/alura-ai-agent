# Agente de IA del Colegio Nexo Digital. (Challenge de Alura).

## Descripción general del proyecto.

Este es un agente de IA creado con LangChain y LangGraph que está capacitado para responder a preguntas del usuario mediante el uso de un RAG el cual utiliza archivos PDF con contenido simple sobre distintas políticas, reglamentos y guías que este colegio ficticio posee.

## Arquitectura de la solución implementada.

La arquitectura del proyecto está orientada a un agente de IA basado en RAG con un grafo de acciones y una interfaz ligera.

Componentes principales:

- .env: Configuración de variables de entorno para credenciales y parámetros de los modelos.
- archivos-escuela/: Contiene los PDFs de políticas, reglamentos y guías que se usan como base de conocimiento.
- rag.py: Gestiona la parte de Recuperación Augmentada por Generación, probablemente creando embeddings, vectores y buscando información relevante en los documentos.
- graph.py: Define el grafo de flujo de decisiones del agente usando LangGraph.
- agent_state.py: Mantiene el estado del agente durante la ejecución, controlando contexto y memoria de la conversación.
- node_actions.py: Implementa las acciones que se ejecutan en los nodos del grafo.
- conditional_edge_action.py: Maneja transiciones condicionales entre nodos según resultados o condiciones.
- .gradio/: Contiene la interfaz de usuario construida con Gradio para interactuar con el agente.
- readme.md: Describe el propósito del proyecto y su arquitectura general.

Flujo esperado:

1. El usuario hace una pregunta en la interfaz.
2. El agente usa rag.py para recuperar información relevante de los PDFs.
3. graph.py y los nodos/acciones (node_actions.py, conditional_edge_action.py) gestionan la lógica de decisión.
4. agent_state.py guarda el contexto y guía el siguiente paso.
5. La respuesta se entrega por la interfaz Gradio.

## Tecnologías y herramientas utilizadas.

Para este proyecto se utilizó Python como lenguaje principal.
LangChain y LangGraph para manejar la lógica de agentes y modelar el grafo de flujo de decisiones del agente.
RAG para recuperar información relevante desde los archivos PDF.
Gradio para la interfaz de usuario.

## Instrucciones para ejecutar el proyecto.

Idealmente crea un entorno virtual, la manera en la que yo lo hice para este proyecto fue ejecutando el comando: virtualenv -p python3 venv
Luego de crear el entorno virtual debes ejecutar (asegurate de estar en la raíz del proyecto): `pip install -r requirements.txt`
Finalmente, para poder interactuar con el agente ejecuta: `python graph.py`
Se puede acceder temporalmente mediante la siguiente URL: http://148.116.111.79:7860/

## Ejemplos de pregunta que el agente puede responder:

Cualquier pregunta que le hagas a partir de lo que hayas leído de los PDF el agente será capaz de responder, puedes usar las siguientes para probar:

- ¿Cuál es el código de conducta y convivencia?
- ¿Cuáles son las sanciones por plagio?
- ¿Cuáles son las condiciones para recibir un reembolso por una matrícula?

## Ejemplos de respuestas generadas por el agente.

A continuación te presento las respuestas que dejó el agente a cada pregunta de ejemplo presentada anteriormente:

1. El Código de Conducta y Convivencia del Colegio Nexo Digital establece lo siguiente:

- **Respeto e Inclusión:** Se prohíbe estrictamente cualquier tipo de discriminación, acoso o lenguaje ofensivo en los foros, chats en vivo y sesiones grupales.
- **Uso del Chat de Clases:** El chat durante las clases en vivo es de uso exclusivo para dudas académicas. El spam o la promoción de servicios externos resultará en la suspensión del chat por 7 días.

2. Las sanciones por plagio en el colegio Nexo Digital son las siguientes:

- **Primera infracción:** Calificación de 0 (cero) en la entrega y una advertencia escrita.
- **Segunda infracción:** Reprobación automática del curso sin derecho a reembolso.

3. Para recibir un reembolso por una matrícula en el Colegio Nexo Digital, se deben cumplir las siguientes condiciones:
   1. **Periodo de Garantía de Satisfacción**: La solicitud debe realizarse dentro de los primeros 7 días calendario posteriores a la compra del curso.
   2. **Uso del Contenido**: El estudiante no debe haber visualizado más del 15% del contenido total del curso ni haber descargado recursos adjuntos (como plantillas, código base o ejercicios).

   Existe una excepción para estas condiciones:
   - **Problemas Técnicos Impeditivos**: Si el estudiante experimenta fallas técnicas atribuibles a la plataforma que impidan el acceso por más de 72 horas consecutivas, tendrá derecho a un reembolso total sin importar el porcentaje del curso avanzado.

## English Overview

## Project overview

This is an AI agent created with LangChain and LangGraph that is designed to answer user questions by using a RAG system that leverages PDF files containing simple content about different policies, regulations, and guides belonging to this fictional school.

## Architecture of the implemented solution

The project architecture is oriented toward an AI agent based on RAG, with an action graph and a lightweight interface.

Main components:

- .env: Configuration for environment variables related to credentials and model parameters.
- archivos-escuela/: Contains the PDFs of policies, regulations, and guides used as the knowledge base.
- rag.py: Manages the Retrieval-Augmented Generation layer, likely creating embeddings, vectors, and searching for relevant information in the documents.
- graph.py: Defines the decision flow graph of the agent using LangGraph.
- agent_state.py: Maintains the agent state during execution, controlling context and conversation memory.
- node_actions.py: Implements the actions executed in the graph nodes.
- conditional_edge_action.py: Handles conditional transitions between nodes based on results or conditions.
- .gradio/: Contains the user interface built with Gradio to interact with the agent.
- readme.md: Describes the purpose of the project and its general architecture.

Expected flow:

1. The user asks a question in the interface.
2. The agent uses rag.py to retrieve relevant information from the PDFs.
3. graph.py and the nodes/actions (node_actions.py, conditional_edge_action.py) manage the decision logic.
4. agent_state.py stores context and guides the next step.
5. The answer is delivered through the Gradio interface.

## Technologies and tools used

Python was used as the main language for this project.
LangChain and LangGraph were used to handle the agent logic and model the decision flow graph.
RAG was used to retrieve relevant information from the PDF files.
Gradio was used for the user interface.

## Instructions to run the project

Ideally, create a virtual environment. The way I did it for this project was by running the following command: `virtualenv -p python3 venv`
After creating the virtual environment, you must run the following command from the project root: `pip install -r requirements.txt`
Finally, to interact with the agent, run: `python graph.py`
It can be accessed temporarily at the following URL: http://148.116.111.79:7860/

## Example questions the agent can answer

Any question based on what you have read in the PDFs can be answered by the agent. You can use the following examples to test it:

- What is the code of conduct and coexistence?
- What are the sanctions for plagiarism?
- What are the conditions for receiving a tuition refund?

## Example responses generated by the agent

Below are the responses the agent produced for each of the example questions listed above:

1. The Code of Conduct and Coexistence of Colegio Nexo Digital states the following:

- **Respect and Inclusion:** Any form of discrimination, harassment, or offensive language is strictly prohibited in forums, live chats, and group sessions.
- **Use of the Class Chat:** The chat during live classes is exclusively for academic questions. Spam or promotion of external services will result in a 7-day suspension of the chat.

2. The sanctions for plagiarism at Colegio Nexo Digital are as follows:

- **First offense:** A grade of 0 (zero) on the submission and a written warning.
- **Second offense:** Automatic failure of the course without the right to a refund.

3. To receive a refund for tuition at Colegio Nexo Digital, the following conditions must be met:
   1. **Satisfaction Guarantee Period**: The request must be made within the first 7 calendar days after the purchase of the course.
   2. **Use of the Content**: The student must not have viewed more than 15% of the total course content or downloaded attached resources (such as templates, base code, or exercises).

   There is an exception to these conditions:
   - **Impeditive Technical Problems**: If the student experiences technical failures attributable to the platform that prevent access for more than 72 consecutive hours, they will be entitled to a full refund regardless of the percentage of the course completed.
