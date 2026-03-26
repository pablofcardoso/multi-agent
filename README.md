# 🤖 Multi-Agent LangGraph Pipeline

> Pipeline de agentes de IA onde um agente **pesquisa** um assunto na web em tempo real,
> outro **resume** os resultados, e tudo é **avaliado automaticamente** por qualidade e coerência.
> Construído com LangGraph, avaliado com LangSmith + Ragas e deployado na AWS Lambda.

---

## 🏗️ Arquitetura
[Usuário] → [AWS Lambda] → [Agente Pesquisador] → [Agente Resumidor] → [Resposta]
↓
[LangSmith + Ragas avaliam]


---

## 🤖 Agentes

- **Researcher Agent** — busca informações na web em tempo real via Tavily
- **Summarizer Agent** — sintetiza os resultados em português usando Groq (LLaMA 3.3 70B)
- **Evaluator** — valida a qualidade e coerência das respostas com Ragas + LangSmith

---

## 🛠️ Stack

| Ferramenta | Função |
|---|---|
| [LangGraph](https://github.com/langchain-ai/langgraph) | Orquestração dos agentes em grafo |
| [Groq](https://groq.com) | LLM inference rápida com LLaMA 3.3 70B |
| [Tavily](https://tavily.com) | Busca web em tempo real para agentes de IA |
| [LangSmith](https://smith.langchain.com) | Tracing e monitoramento dos agentes |
| [Ragas](https://ragas.io) | Métricas automáticas de qualidade das respostas |
| [AWS Lambda](https://aws.amazon.com/lambda) | Deploy serverless |

---

## 🚀 Como rodar localmente

1. Clone o repositório
```bash
git clone https://github.com/pablofcardoso/multi-agent.git
cd multi-agent
```

2. Instale as dependências
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente
```bash
cp .env.example .env
# Edite o .env com suas chaves
```

```env
GROQ_API_KEY=sua_chave
TAVILY_API_KEY=sua_chave
LANGCHAIN_API_KEY=sua_chave
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=multi-agent
```

4. Rode o pipeline
```bash
python test_pipeline.py
```

---

## 📁 Estrutura do Projeto
multi-agent/
├── agents/
│ ├── researcher.py # Agente que busca na web
│ └── summarizer.py # Agente que resume os resultados
├── graph/
│ └── pipeline.py # Grafo LangGraph conectando os agentes
├── evaluation/
│ └── evaluate.py # Avaliação com Ragas + LangSmith
├── lambda_function.py # Entry point da AWS Lambda
├── .env.example # Variáveis necessárias (sem valores)
└── requirements.txt


---

## 📌 Status do Projeto

- [x] Agente Pesquisador
- [x] Agente Resumidor
- [x] Grafo LangGraph
- [x] Tracing com LangSmith
- [ ] Deploy na AWS Lambda
- [ ] Avaliação com Ragas

---

## 👤 Autor

**Pablo Cardoso** — [LinkedIn](https://www.linkedin.com/in/pablofcardoso/) · [GitHub](https://github.com/pablofcardoso)
