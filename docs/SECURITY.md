# Security and privacy

## Initial development environment

Bind published ports to loopback and keep the stack on a development workstation. Qdrant's development HTTP API does not require authentication. Configure a local PostgreSQL password in the ignored `.env` file. The Docker build context is restricted to application sources and project metadata. Keep original corpora, local configuration and credential files outside Git. Treat synchronized folders such as OneDrive as potential external storage when choosing where to keep private documents. Avoid writing sensitive values into command output, traces or screenshots.

## Import and storage controls

- Treat source files, metadata and extracted content as untrusted. Enforce file size and type limits, validate content signatures, use server-generated paths and isolate parsers with restricted filesystem and network access.
- Keep original documents private with per-company scoping, retention settings, deletion and auditable access. Reconcile deletion across storage, PostgreSQL, Qdrant, backups and evaluation exports.
- Use parameterized queries or ORM bindings and scope reads and writes at the application boundary. Add access tests that cover cross-company retrieval and direct object access.
- Transfer company documents to external providers only after the owner authorizes the specific transfer. Redact logs and traces and minimize copies.

## Model and tool controls

Document passages are evidence. Keep tool permissions and system instructions outside retrieved content. Apply authorization independently of model output, validate structured results, constrain tool parameters and cap retries, fan-out and execution time. Default agents to read-only tools and route consequential actions to a person. Log tool intent and result without storing private payloads. Reject unknown citation identifiers and flag unsupported or contradictory claims for review.

## Release checks

Before handling real tenant data, exercise file validation, prompt injection resistance, tenant scoping, report review, secret handling and restore procedures. Version dependencies and review advisories for the build and container images before a release. Report suspected disclosure without posting the affected data. Revoke exposed credentials, then audit access and affected artifacts.
