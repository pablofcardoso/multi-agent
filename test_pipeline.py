# test_pipeline.py
from dotenv import load_dotenv
load_dotenv()

from graph.pipeline import build_graph

graph = build_graph()

result = graph.invoke({
    "query": "What is LangGraph and how does it work?",
    "research_results": "",
    "final_summary": "",
    "messages": []
})

print("\n✅ RESUMO FINAL:")
print(result["final_summary"])