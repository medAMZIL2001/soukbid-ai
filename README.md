# SoukBid AI

**Intelligent Tender Analysis & Agentic RAG Platform**

SoukBid AI is a local-first decision-support platform for Moroccan public procurement. Its goal is to help companies find relevant tenders, understand French and Arabic tender documents, compare requirements with company evidence, and prepare application materials with verifiable citations. Final decisions belong to a human reviewer. Offer submission and legal eligibility guarantees are outside the product scope.

## Project status

| Status | Scope |
| --- | --- |
| Implemented | FastAPI application and `GET /health` with an automated HTTP contract test |
| Configured | PostgreSQL, Qdrant and backend containers, Ruff, Pytest, pre-commit and GitHub Actions |
| Planned | Document ingestion, OCR, RAG, matching, LangGraph, MCP, evaluation, monitoring and React |

Phase 0 establishes the foundation. See the [roadmap](docs/ROADMAP.md) for validation and phase dependencies and the [architecture](docs/ARCHITECTURE.md) for diagrams.

## Run the API with PowerShell

Python 3.11 is the reference runtime. Python 3.12 and 3.13 are also accepted by the Phase 0 package. Use `python --version` to check the interpreter on PATH before creating the virtual environment. Git is used for version control. Docker and Node.js are unnecessary for this quick start.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```

Check liveness from a second PowerShell terminal.

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health | ConvertTo-Json -Compress
```

The API returns `200 OK` with `{"status":"ok"}`. Interactive OpenAPI documentation is at `http://127.0.0.1:8000/docs`. The endpoint measures HTTP process liveness independently of data services.

## Run the local Docker stack

Start Docker Desktop with Linux containers enabled. The following commands create the ignored configuration file on first run and open it for editing.

```powershell
if (-not (Test-Path .env)) { Copy-Item .env.example .env }
notepad .env
```

Set a non-empty `SOUKBID_POSTGRES_PASSWORD` in `.env`. The following commands validate, start, check and stop the stack.

```powershell
docker compose config --quiet
docker compose up --build --wait
docker compose ps
Invoke-RestMethod http://127.0.0.1:8000/health
docker compose down
```

Use the configured backend port if it differs from `8000`. The default loopback ports are `8000` for the API, `5432` for PostgreSQL and `6333` for Qdrant HTTP. Named volumes keep database data across normal shutdowns. PostgreSQL initialization variables apply to an empty data volume. Change existing roles through PostgreSQL if you rotate an initialized database password.

The API can start independently because Phase 0 has no database queries. Redis, Ollama and Langfuse are future integrations. The initial stack requires no GPU, model downloads or cloud API keys.

## Quality checks

```powershell
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m pre_commit install
```

The pre-commit hooks use Python on PATH. Activate the virtual environment before committing or running the hooks manually.

```powershell
. .\.venv\Scripts\Activate.ps1
python -m pre_commit run --all-files
```

## Repository guide

- `backend/app/` contains the API entry point.
- `tests/integration/` contains the HTTP contract test.
- `docker-compose.yml` defines the local stack. `backend/Dockerfile` builds the API image.
- `.github/workflows/ci.yml` runs lint, format checks and tests on Python 3.11 and 3.13.
- [Specification](docs/PROJECT_SPECIFICATION.md), [data sources](docs/DATA_SOURCES.md), [references](docs/REFERENCES.md), [security](docs/SECURITY.md) and the [learning guide](docs/LEARNING_GUIDE.md) describe later work.
