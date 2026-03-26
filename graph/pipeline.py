# graph/pipeline.py
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator

# O estado é um dicionário tipado que todos os nós compartilham
class AgentState(TypedDict):
    query: str                    # Pergunta original do usuário
    research_results: str         # Output do agente pesquisador
    final_summary: str            # Output do agente resumidor
    messages: Annotated[list, operator.add]  # Histórico de mensagens

def build_graph():
    """Monta e compila o grafo com os dois agentes."""
    
    # Importamos aqui dentro para evitar problemas de importação circular
    from agents.researcher import researcher_node
    from agents.summarizer import summarizer_node

    # Cria o grafo passando o estado compartilhado
    graph = StateGraph(AgentState)

    # Adiciona os nós — cada nó é uma função
    graph.add_node("researcher", researcher_node)
    graph.add_node("summarizer", summarizer_node)

    # Define o fluxo: começa no researcher...
    graph.set_entry_point("researcher")

    # ...researcher passa para o summarizer...
    graph.add_edge("researcher", "summarizer")

    # ...summarizer encerra o pipeline
    graph.add_edge("summarizer", END)

    return graph.compile()