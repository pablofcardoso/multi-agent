# 🤖 Multi-Agent LangGraph Pipeline

Pipeline de dois agentes de IA construído com LangGraph, avaliado com LangSmith e Ragas, e deployado na AWS Lambda.

## 🏗️ Arquitetura
[Usuário] → [AWS Lambda] → [Agente Pesquisador] → [Agente Resumidor] → [Resposta]
↓
[LangSmith / Ragas avalia]


## 🤖 Agentes

- **Researcher Agent:** busca informações na web em tempo real via Tavily
- **Summarizer Agent:** sintetiza os resultados em português usando Groq (LLaMA 3.3 70B)

## 🛠️ Stack

| Ferramenta | Função |
|---|---|
| [LangGraph](https://github.com/langchain-ai/langgraph) | Orquestração dos agentes em grafo |
| [Groq](https://groq.com) | LLM inference rápida e gratuita |
| [Tavily](https://tavily.com) | Busca web para agentes de IA |
| [LangSmith](https://smith.langchain.com) | Tracing e avaliação dos agentes |
| [Ragas](https://ragas.io) | Métricas de qualidade das respostas |
| [AWS Lambda](https://aws.amazon.com/lambda) | Deploy serverless |

## 🚀 Como rodar localmente

1. Clone o repositório
   ```bash
   git clone https://github.com/pablofcardoso/multi-agent.git
   cd multi-agent
   ```

2. Instale as dependências
   ```bash
   python -m pip install -r requirements.txt
   ```

3. Crie o arquivo `.env` com suas chaves
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
└── requirements.txt


## 📌 Status do Projeto

- [x] Agente Pesquisador
- [x] Agente Resumidor
- [x] Grafo LangGraph
- [x] Tracing com LangSmith
- [ ] Deploy na AWS Lambda
- [ ] Avaliação com Ragas