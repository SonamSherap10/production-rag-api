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

```text
production-rag-api/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── services/
│   ├── rag/
│   ├── middleware/
│   └── monitoring/
│
├── tests/
│
├── docs/
│
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── uv.lock
└── README.md
```

## Getting Started

### Prerequisites

Install the following:

- Python
- uv
- Ollama
- Docker
- PostgreSQL with the pgvector extension

### Clone the repository

```bash
git clone <your-repository-url>
cd production-rag-api
```

### Create the virtual environment

```bash
uv venv
source .venv/bin/activate
```

### Install dependencies

```bash
uv add langchain-ollama langgraph langsmith fastapi uvicorn slowapi pydantic-settings python-dotenv
```

### Configure environment variables

Create a `.env` file in the project root.

Example:

```env
APP_NAME=Production RAG API
APP_ENV=development
DATABASE_URL=postgresql://postgres:password@localhost:5432/ragdb
OLLAMA_BASE_URL=http://localhost:11434
CHAT_MODEL=llama3.2:3b
EMBEDDING_MODEL=nomic-embed-text
```

Adjust the database credentials and model names according to your environment.

### Start Ollama

```bash
ollama serve
```

Pull the required models:

```bash
ollama pull llama3.2:3b
ollama pull nomic-embed-text
```

### Run the API

```bash
uv run uvicorn app.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

Interactive API documentation:

```text
http://localhost:8000/docs
```

*The commands and module paths will be updated as the application structure is implemented.*

## Development Roadmap

The project will be developed incrementally.

- [ ] Initialize FastAPI application.
- [ ] Implement application configuration.
- [ ] Integrate Ollama chat and embedding models.
- [ ] Implement document ingestion and chunking.
- [ ] Integrate PostgreSQL and pgvector.
- [ ] Implement semantic retrieval.
- [ ] Build the RAG generation pipeline.
- [ ] Add request tracing with metadata.
- [ ] Implement prompt-injection protection.
- [ ] Implement PII detection and redaction.
- [ ] Add exponential backoff and model fallbacks.
- [ ] Implement in-memory caching.
- [ ] Add IP-based rate limiting.
- [ ] Implement structured JSON logging.
- [ ] Collect request, latency, and token metrics.
- [ ] Implement health-check endpoints.
- [ ] Write automated tests.
- [ ] Containerize the application with Docker.
- [ ] Test the complete deployment.

## Learning Objectives

Beyond implementing the application, this project focuses on understanding:

- How RAG systems work internally.
- How vector databases perform similarity searches.
- How to design reliable LLM-powered APIs.
- How to handle model failures and external dependencies.
- How to protect sensitive information.
- How to monitor and debug production applications.
- How to deploy AI applications using containers.

## Project Status

**Currently under development.**

This repository is both a practical learning project and an exploration of production-oriented AI application engineering.

Features will be documented as they are implemented and tested.
