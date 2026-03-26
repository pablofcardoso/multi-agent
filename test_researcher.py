# test_researcher.py
from dotenv import load_dotenv
load_dotenv()  # Carrega as variáveis do .env ANTES de qualquer import

from agents.researcher import researcher_node

# Simula um estado como se fosse o LangGraph passando
state = {
    "query": "What is LangGraph and how does it work?",
    "research_results": "",
    "final_summary": "",
    "messages": []
}

result = researcher_node(state)

print("✅ Resultado da pesquisa:")
print(result["research_results"])