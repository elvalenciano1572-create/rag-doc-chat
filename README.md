# rag-doc-chat

[![CI](https://github.com/elvalenciano1572-create/rag-doc-chat/actions/workflows/ci.yml/badge.svg)](https://github.com/elvalenciano1572-create/rag-doc-chat/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A lightweight, zero-hallucination Retrieval-Augmented Generation (RAG) semantic document question-answering engine in Python.

Generic LLMs hallucinate when asked specific questions about private company guidelines, PDF contracts, or internal standard operating procedures (SOPs). **rag-doc-chat** indexes unstructured documents into chunked vector segments, retrieves high-relevance semantic passages, and synthesizes answers strictly grounded in cited source materials.

## Features

- **Zero-Hallucination Grounding**: Answers are synthesized exclusively from retrieved document chunks with explicit source citations.
- **Out-of-Scope Protection**: Automatically flags queries where no supporting evidence exists in the indexed files rather than guessing.
- **Fast In-Memory Vector Search**: Lightweight tokenized BM25 & vector similarity retrieval with zero heavy external vector DB overhead.
- **Pluggable Architecture**: Ready for local deployment or enterprise cloud LLMs (OpenAI, Anthropic, Gemini).

## Quick Start

```bash
git clone https://github.com/elvalenciano1572-create/rag-doc-chat
cd rag-doc-chat
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest
rag-chat "What is the monthly stipend for remote work?"
```

## Example Output

```text
========================================================================
   RAG-DOC-CHAT: SEMANTIC DOCUMENT INTELLIGENCE ENGINE
========================================================================
[*] Indexed 4 document chunks across corporate policy PDFs.
[*] User Question: "What is the monthly stipend for remote work?"

--- GROUNDED SYNTHESIS ANSWER ---
Based on Employee Handbook 2026.pdf (Section 4.2 - Remote Work Policy):
"Employees are eligible for full remote work after completing their 90-day probationary period. The company provides a monthly 75 EUR home office and high-speed internet stipend."

Confidence Score: 82%
Cited Sources:
  * Employee Handbook 2026.pdf (Section 4.2 - Remote Work Policy)
========================================================================
```

## License

MIT
