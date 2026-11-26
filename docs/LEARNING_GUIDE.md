# Learning guide

Use each phase to implement a small workflow and observe its behavior before adding dependencies.

| Phase | Concepts to learn | Practical exercise |
| --- | --- | --- |
| 0 | ASGI, FastAPI, virtual environments, editable installs, linting, Git, containers, health checks and CI | Run Uvicorn and inspect the response. Change a status locally and observe the contract test fail, then restore it. Explain why PostgreSQL is independent of the liveness endpoint. |
| 1 | Provenance, checksums, dates, metadata validation and idempotent storage | Import the same file twice and a revised file once. Explain the identity and revision records. |
| 2 | Reading order, OCR, Arabic text, tables and coordinates | Compare extraction on native and scanned pages. Annotate errors and trace a requirement to its original location. |
| 3 | Embeddings, cosine similarity, chunking, vector search and grounding | Compare two chunk sizes and cite the exact evidence used. Test a question without a source answer. |
| 4 | BM25, rank fusion, reranking, query rewriting and context compression | Compare dense, lexical and hybrid cases on named entities and paraphrases. Record Recall@K, MRR and latency. |
| 5 | Domain rules, semantic similarity, weights and uncertainty | Compare a strong technical profile with a missing mandatory certification and inspect both outputs. |
| 6 | LangGraph state, conditional edges, checkpointing and human approval | Pause and resume a review on a draft with missing evidence. |
| 7 | MCP transport, schemas, authorization and typed failures | Invoke a search tool with valid and invalid parameters and inspect both results. |
| 8 | Annotation, retrieval metrics, RAGAS, latency and Langfuse | Review a model score alongside human labels and inspect a redacted trace. |
| 9 | REST contracts, migrations, authentication and React state | Build the response lifecycle from tender import through reviewer approval. |
| 10 | Dependency hygiene, isolation, CI/CD, backups and rollback | Recreate the stack, recover a backup and verify the restored document provenance. |
| 11 | Data leakage, baseline classification, fine-tuning and MLflow | Compare a simple classifier with a Transformer on issuer- or time-separated splits. |

For Phase 0, start with the [FastAPI testing guide](https://fastapi.tiangolo.com/tutorial/testing/), the [Compose services reference](https://docs.docker.com/reference/compose-file/services/) and the [pre-commit documentation](https://pre-commit.com/).
