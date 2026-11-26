# Project specification

## Problem and scope

Small procurement teams spend hours finding tenders, reading specifications in French and Arabic, checking mandatory requirements and assembling submissions. SoukBid AI helps a company decide where to invest that effort. The initial audience is a Moroccan IT or engineering company. The application provides evidence for review. Human staff own final eligibility judgments and external submission.

## Primary workflow

1. A company records its sectors, skills, team, references, experience, certifications and available administrative documents.
2. An operator imports a tender notice and attachments with their provenance. The service keeps the originals and identifies duplicate content.
3. A reviewer searches for relevant opportunities, reads structured requirements and asks questions with page or section citations.
4. Matching returns a technical score, per-criterion evidence, mandatory gaps and cases requiring manual verification.
5. The system produces an administrative checklist, a risk register, a draft technical response and a cited report for human approval.

## Functional requirements

| Area | Required behavior and acceptance |
| --- | --- |
| Collection | Accept approved public sources and manual PDF, DOCX and image imports. Capture reference, category, issuer, deadline and access provenance. Re-importing identical bytes must preserve the original and avoid duplicate assets. |
| Document intelligence | Extract native PDF text, scanned text with OCR, tables, sections and named entities in French and Arabic. Preserve evidence locations and mark uncertain extraction. Use source pages where they exist and stable paragraph or section anchors otherwise. |
| Retrieval | Compare dense baseline, advanced, hybrid and agentic RAG. Support semantic chunking, multilingual embeddings, dense and BM25 or sparse retrieval, metadata filters, query rewriting and expansion, reranking and context compression. Cite supporting passages and abstain when evidence is insufficient. |
| Matching | Combine semantic signals and rules for skills, experience, certifications, professional references, finance and administrative evidence. Return criterion weights and reasons. Track mandatory conditions with met, unmet and unknown states independently of the technical score. |
| Agents | Coordinate search, document analysis, matching, compliance, risk, writing and verification with a supervisor and explicit workflow state. Require human review for final reports and unresolved conditions. |
| MCP | Expose typed tools for tender and document search, profile lookup, vector retrieval, matching, deadline lookup and report generation with purpose-specific authorization. |
| Evaluation | Version annotated questions, expected answers and evidence spans. Compare faithfulness, answer relevance, context precision and recall, Recall@K, MRR, latency, citation accuracy and unsupported-claim rate. |
| Observability | Record redacted traces, prompt versions, model calls, tokens, latency, errors and costs when applicable. Support local measurements and a later Langfuse integration. |
| Application | Provide React views for search, chat, company profiles, document management, analysis, scores, checklists, reports, history and evaluation. |
| ML extensions | Explore tender and document classification, requirement extraction, Transformers baselines, reranker training and LoRA or QLoRA after the MVP and a data-quality review. Track experiments with MLflow. |

## Data and interfaces

A tender has an issuer, reference, source URL, published date, deadline, category and revision history. Document identity includes a cryptographic digest and original storage reference. A requirement has a category, mandatory status, original wording and evidence links. A company profile has verifiable records with optional expiry dates. An analysis records the tender revision, profile revision, scoring configuration, findings, citations and review status. Distinguish missing values from confirmed negative values.

Reports must point to a document version plus evidence location and quote or text span. Reviewers can correct extracted information and approve or reject report drafts. A correction preserves an audit record. Use bounded jobs, structured errors and clear retry behavior.

## Quality goals

Favor local open-source software and CPU-friendly defaults. Make provider, prompt, embedding and index changes explicit and measurable. Isolate company data, validate uploads, enforce scoped access and keep sensitive inputs out of logs. Use small, versioned test fixtures and reproducible commands. Establish measured baselines before setting retrieval or latency thresholds.
