# agents/researcher.py
from tavily import TavilyClient
from graph.pipeline import AgentState
import os
from dotenv import load_dotenv

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def researcher_node(state: AgentState) -> AgentState:
    """Nó que recebe a query e busca informações na web."""
    
    query = state["query"]
    print(f"🔍 Pesquisando: {query}")
    
    # Tavily retorna resultados de busca já estruturados
    response = tavily.search(
        query=query,
        max_results=3,          # 3 fontes para economizar cota
        search_depth="basic"    # "advanced" usa mais cota
    )
    
    # Concatenamos o conteúdo das fontes em texto corrido
    results_text = "\n\n".join([
        f"Fonte: {r['url']}\nConteúdo: {r['content']}"
        for r in response["results"]
    ])
    
    # Escrevemos no estado — o summarizer vai ler daqui
    return {"research_results": results_text}