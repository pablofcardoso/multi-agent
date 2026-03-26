# agents/summarizer.py
from langchain_groq import ChatGroq
from graph.pipeline import AgentState
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",  # Modelo gratuito e potente
    temperature=0.3
)

def summarizer_node(state: AgentState) -> AgentState:
    """Nó que recebe os resultados da pesquisa e gera um resumo."""
    
    research = state["research_results"]
    query = state["query"]
    
    print(f"📝 Resumindo resultados...")
    
    prompt = f"""Você é um assistente especialista em síntese de informações.
    
Com base nos resultados de pesquisa abaixo, responda a pergunta de forma clara e objetiva em português.

Pergunta: {query}

Resultados da pesquisa:
{research}

Forneça uma resposta bem estruturada, citando as fontes quando relevante."""

    response = llm.invoke(prompt)
    
    return {"final_summary": response.content}