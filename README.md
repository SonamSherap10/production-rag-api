# Production RAG API

A production-oriented Retrieval-Augmented Generation (RAG) API built with Python, FastAPI, LangChain, LangGraph, PostgreSQL, pgvector, and locally hosted LLMs through Ollama.

The goal of this project is to explore how to build reliable, secure, observable, and scalable AI-powered backend applications rather than simply creating a basic chatbot.

## Project Goals

This project aims to implement a RAG API with production-oriented engineering practices, including:

- Document ingestion, processing, and chunking.
- Vector embeddings and semantic search.
- Retrieval-Augmented Generation using LangChain.
- Request tracing and metadata collection.
- Prompt-injection protection.
- Personally Identifiable Information (PII) detection and redaction.
- Exponential backoff and model fallback mechanisms.
- In-memory caching for duplicate requests.
- IP-based API rate limiting.
- Structured JSON logging.
- Request, latency, and token usage metrics.
- Health-check endpoints.
- Docker-based deployment.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Primary programming language |
| FastAPI | REST API framework |
| Uvicorn | ASGI application server |
| LangChain | RAG pipeline and LLM integration |
| LangGraph | Stateful AI workflows |
| LangSmith | Tracing and debugging |
| Ollama | Local LLM inference and embeddings |
| PostgreSQL | Relational database |
| pgvector | Vector similarity search |
| SlowAPI | API rate limiting |
| Pydantic Settings | Application configuration |
| Python-dotenv | Environment variable management |
| Docker | Application containerization |

## Architecture

The intended request flow:

```text
                 Client
                   |
                   v
              FastAPI API
                   |
          Request Validation
                   |
          Rate Limiting
                   |
          PII Detection
                   |
          Prompt Security
                   |
                   v
             RAG Pipeline
                   |
          +--------+--------+
          |                 |
          v                 v
      Retriever          Cache
          |
          v
     PostgreSQL
       pgvector
          |
          v
     Retrieved Context
          |
          v
       LLM Model
          |
     Retry / Fallback
          |
          v
     Generated Answer
          |
          v
        Response
```

Observability components will collect information throughout the request lifecycle.

## Project Structure

The project will gradually follow a modular structure:

## Project Structure

```text
production-rag-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app: /chat, /health, /metrics, /cache/stats
│   ├── config.py        # Settings loaded from environment variables
│   ├── models.py        # Pydantic request/response schemas
│   ├── security.py      # Prompt-injection checks, PII masking, output validation
│   ├── cache.py         # In-memory response cache with TTL
│   ├── monitoring.py    # JSON logging, metrics collector, request timer
│   └── agent.py         # LangGraph agent with retry and model fallback
│
├── tests/
│   ├── __init__.py
│   ├── test_security.py
│   ├── test_cache.py
│   └── test_api.py
│
├── .dockerignore
├── .env.example         # Placeholder environment variables
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── uv.lock
└── README.md
```
## Getting Started

### Prerequisites

- Python 3.12
- [uv](https://docs.astral.sh/uv/)
- [Ollama](https://ollama.com/)
- A PostgreSQL database with the pgvector extension (for example, a free Supabase project)
- Docker (optional, for containerized runs)

### Clone the repository

```bash
git clone <your-repository-url>
cd production-rag-api
```

### Install dependencies

```bash
uv sync
```

This creates `.venv` and installs the exact versions from `uv.lock`.

### Configure environment variables

Copy the example file and fill in your values:

```bash
cp .env.example .env
```

| Variable | Purpose | Example |
|---|---|---|
| `APP_ENV` | Environment name | `development` |
| `LOG_LEVEL` | Logging verbosity | `info` |
| `API_KEYS` | Keys clients use to call this API | generate with `python -c "import secrets; print(secrets.token_urlsafe(32))"` |
| `RATE_LIMIT` | Requests per client | `20/minute` |
| `MAX_RETRIES` | Retry limit before fallback or error | `3` |
| `SUPABASE_DATABASE_URL` | Postgres connection (use the Session pooler string) | `postgresql+psycopg://postgres.<ref>:<password>@<host>:5432/postgres` |
| `OLLAMA_BASE_URL` | Where Ollama listens | `http://localhost:11434` |
| `PRIMARY_MODEL` | Main chat model | `llama3.1:8b` |
| `FALLBACK_MODEL` | Backup chat model | `llama3.2:3b` |
| `EMBEDDING_MODEL` | Embedding model | `nomic-embed-text` |
| `LLM_TIMEOUT_SECONDS` | Wait time before fallback | `30` |
| `CACHE_TTL_SECONDS` | How long cached answers live | `3600` |
| `LANGSMITH_TRACING` | Enable tracing | `true` |
| `LANGSMITH_API_KEY` | LangSmith key (optional) | |
| `LANGSMITH_PROJECT` | LangSmith project name | `production-rag` |

### Start Ollama and pull the models

Check that Ollama is running (`ollama list`). If it isn't, start it with `ollama serve`.

```bash
ollama pull llama3.1:8b
ollama pull llama3.2:3b
ollama pull nomic-embed-text
```

### Run the API locally

```bash
uv run uvicorn app.main:app --reload
```

- API: `http://localhost:8000`
- Interactive docs: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/health`

### Run with Docker

```bash
docker compose up -d --build
curl http://localhost:8000/health
```

The container reaches Ollama on your machine through `host.docker.internal`, so Ollama must listen on all interfaces (`OLLAMA_HOST=0.0.0.0`).

### Run the tests

```bash
uv run pytest -v
```

## Development Roadmap

- [x] Initialize FastAPI application.
- [x] Implement application configuration.
- [x] Integrate Ollama chat models with fallback.
- [ ] Implement document ingestion and chunking.
- [ ] Integrate PostgreSQL and pgvector.
- [ ] Implement semantic retrieval.
- [ ] Build the RAG generation pipeline.
- [x] Add request tracing (LangSmith).
- [x] Implement prompt-injection protection.
- [x] Implement PII detection and redaction.
- [ ] Add exponential backoff between retries.
- [x] Implement in-memory caching.
- [x] Add IP-based rate limiting.
- [x] Implement structured JSON logging.
- [x] Collect request, latency, and token metrics.
- [x] Implement health-check endpoints.
- [ ] Add API key authentication to `/chat`.
- [ ] Complete automated tests (security done, cache and API in progress).
- [x] Containerize the application with Docker.
- [ ] Test the complete deployment.



## Project Status

**Currently under development.**

This repository is both a practical learning project and an exploration of production-oriented AI application engineering.

Features will be documented as they are implemented and tested.is this all true for this or needs editing
