# Repository instructions

SoukBid AI is a local-first tender decision-support project for Moroccan public procurement. Read the [roadmap](docs/ROADMAP.md) and [architecture](docs/ARCHITECTURE.md) before changing the project.

- Work within the current authorized phase. Ask the project owner before starting the next phase.
- Use English for code, paths, technical comments and repository documentation. Explain the work to the project owner in French.
- For every phase, explain its objective, concepts, technology choices and alternatives. Identify touched files, walk through the core code, provide PowerShell commands, run applicable tests, correct failures and update the documentation and roadmap with observed results.
- Preserve unrelated changes. Prefer a modular Python application and introduce packages as the phase needs them. Keep local development usable without a GPU or paid provider.
- Validate input at boundaries, keep original documents private, and require source references for factual findings. See [security](docs/SECURITY.md) for document and agent trust boundaries.
- Check Ruff lint and formatting and run Pytest before reporting work complete. Report the interpreter and configurations actually verified, along with any blocked checks.
- Keep credentials, company documents and private corpora outside Git. Obtain authorization before creating a remote, pushing code or transferring confidential data.
