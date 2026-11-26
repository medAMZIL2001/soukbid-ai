# Development roadmap

Only Phase 0 is in the current scope. Each later phase requires owner approval. A phase is validated when its acceptance evidence has been recorded.

| Phase | Status | Dependencies | Deliverables and validation |
| --- | --- | --- | --- |
| 0. Foundation | Implemented with local validation | Empty workspace and local toolchain | Project docs, bootable API, health contract, Compose and CI. Run lint, tests and HTTP smoke checks. Validate Compose configuration and container startup. |
| 1. Data collection | Planned | Phase 0 and approved access and reuse terms | Manually curate a small corpus. Implement metadata and immutable import storage. Demonstrate source provenance and idempotent re-import. |
| 2. Document intelligence | Planned | Phase 1 corpus | Compare parsers, OCR and table extraction on French and Arabic samples. Verify text and evidence locations manually. |
| 3. RAG MVP | Planned | Phase 2 passages | Add provider interface, local model, embeddings, chunking and Qdrant retrieval. Establish a dense baseline with cited answers and abstention cases. |
| 4. Advanced RAG | Planned | Phase 3 baseline | Test lexical or sparse search, fusion, filters, query transformations, reranking and context compression. Compare recall, rank and latency on the same questions. |
| 5. Matching | Planned | Phase 2 requirements and company fixture | Version profiles and scoring rules. Demonstrate independently reported mandatory gaps, unknown states and evidence coverage. |
| 6. Agentic AI | Planned | Phases 3–5 | Add typed LangGraph state and specialized agents. Exercise verification, failure recovery and human approval before final reports. |
| 7. MCP | Planned | Phase 6 contracts | Expose scoped tools. Test validation, policy enforcement and tool failure for each contract. |
| 8. Evaluation and LLMOps | Planned | Baseline from Phase 3 and workflows from Phase 6 | Publish the evaluation protocol, compare variants with RAGAS and retrieval metrics, and verify redacted Langfuse traces. |
| 9. Application | Planned | Phase 5–8 interfaces | Expand API and database, add authorization and React dashboard. Exercise the end-to-end tender review flow with synthetic company data. |
| 10. Industrialization | Planned | Phase 9 | Harden deployment, backups, security and CI/CD. Reproduce the full demo and verify data recovery. |
| 11. ML extensions | Planned | MVP and enough labeled data | Compare classical and Transformer baselines, consider reranker training or LoRA/QLoRA and track results in MLflow. |

## Phase 0 validation record

- Windows 11 build 22631 (23H2), Windows PowerShell 5.1 and WSL 3.0.5. The workstation exposes eight logical CPUs, 15.74 GiB RAM, Intel Iris Xe graphics and 176 GiB free on the project drive at inspection. Available RAM was 1.08 GiB at the first check. Phase 0 starts without a model, GPU or optional services.
- Python 3.13.7 is on PATH. Python 3.11 is the container and CI reference. Git 2.50.1, Docker Engine 29.9.2, Compose 5.6.1, Node.js 24.16.0 and npm 11.13.0 were detected. Node is reserved for the frontend.
- Pytest verified the liveness contract with warnings treated as errors on Windows with Python 3.13.7 and in a Linux container with Python 3.11.18. Ruff lint and format checks passed on both. Both pre-commit hooks and `pip check` passed on Windows. An actual Windows loopback request to Uvicorn returned `200` and `{"status":"ok"}`.
- Compose accepted the resolved configuration for three services, two named volumes and a shared bridge network. Docker Desktop was initially stopped. After startup, Compose built the backend with Python 3.11.18 and reported all services healthy on temporary loopback ports. The API returned `200` with the expected payload, PostgreSQL returned `1` for `SELECT 1`, and Qdrant returned `200` on `/readyz`.
- Before the first commit, the credential pattern review covered all 22 project files and found no matches. Git ignore checks excluded local configuration, virtual environments, data and private keys.

## Phase 1 entry criteria

Confirm authorization to start. Select a source with accessible terms, then define a small corpus and record source, revision, access date and reuse evidence before importing files. Prioritize a born-digital PDF, a scanned sample and French and Arabic coverage where available.
