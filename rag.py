from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

load_dotenv()

# Carga de los archivos PDF
pdf_files = DirectoryLoader(path="./archivos-escuela", glob="*.pdf", loader_kwargs={"languages": ["es"]}).load()

# Chunking
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
chunks = splitter.split_documents(pdf_files)

# Embedding
embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001",api_key=os.getenv("GEMINI_API_KEY"))

# Vectors
vector_store = FAISS.from_documents(chunks, embedding_model)
retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold", 
    search_kwargs={"score_threshold": 0.3, "k": 4}
)

# RAG prompt
rag_prompt = ChatPromptTemplate(
    [
        ("system", 
         """
         Eres un experto en las políticas internas del colegio Nexo Digital. Estás capacitado para responder cualquier
         pregunta que te haga un usuario, siempre y cuando, cuya respuesta pueda ser encontrada en el contexto que se
         te provea.
         En caso de no poder responder satisfactoriamente la pregunta del usuario, entonces hazle saber que no lograste
         responder su pregunta con la información que posees.
         """
        ),
        ("user",
        """
        Contexto: {context}
        Pregunta del usuario: {user_question}
        """
        )
    ]
)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=os.getenv("GEMINI_API_KEY"))

# Cadena de ejecución
rag_chain = rag_prompt | llm | StrOutputParser()

# Ejecuta RAG
def execute_rag(question: str) -> dict:
    retrieve_exc = retriever.invoke(question)
    if retrieve_exc:
        response = rag_chain.invoke({"context": retrieve_exc, "user_question": question})
        return {
            "success": True,
            "question": question,
            "answer": response
        }
    else:
        return {
            "success": False,
            "question": question,
            "answer": ""
        }