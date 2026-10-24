import math
import re

from rag_chat.models import DocumentChunk, RAGAnswer, RetrievedPassage


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"\b\w{3,}\b", text.lower()))


def compute_bm25_similarity(query_tokens: set[str], doc_tokens: set[str]) -> float:
    if not query_tokens or not doc_tokens:
        return 0.0
    common = query_tokens.intersection(doc_tokens)
    return len(common) / (math.sqrt(len(query_tokens)) * math.sqrt(len(doc_tokens)))


class SimpleVectorStore:
    def __init__(self):
        self.chunks: list[DocumentChunk] = []

    def add_document(self, title: str, section: str, text: str) -> None:
        chunk = DocumentChunk(
            chunk_id=f"chk-{len(self.chunks) + 1}",
            source_document=title,
            page_or_section=section,
            text_content=text.strip(),
        )
        self.chunks.append(chunk)

    def retrieve(self, query: str, top_k: int = 2) -> list[RetrievedPassage]:
        q_tokens = tokenize(query)
        scored: list[tuple[float, DocumentChunk]] = []

        for chk in self.chunks:
            d_tokens = tokenize(chk.text_content)
            score = compute_bm25_similarity(q_tokens, d_tokens)
            if score > 0.05:
                scored.append((score, chk))

        scored.sort(key=lambda x: x[0], reverse=True)
        top = scored[:top_k]

        return [
            RetrievedPassage(
                chunk=chk,
                relevance_score=round(min(1.0, sc * 2.5), 2),
            )
            for sc, chk in top
        ]


def answer_query_with_rag(query: str, store: SimpleVectorStore) -> RAGAnswer:
    passages = store.retrieve(query, top_k=2)

    if not passages:
        return RAGAnswer(
            query=query,
            answer="I could not find any relevant information regarding this in the uploaded documents.",
            confidence_score=0.1,
            cited_sources=[],
            retrieved_passages=[],
        )

    sources = list({f"{p.chunk.source_document} ({p.chunk.page_or_section})" for p in passages})

    # Synthesize answer grounded strictly in retrieved chunks
    best_text = passages[0].chunk.text_content
    best_source = passages[0].chunk.source_document
    best_section = passages[0].chunk.page_or_section

    answer = (
        f"Based on {best_source} ({best_section}):\n"
        f"\"{best_text}\""
    )

    return RAGAnswer(
        query=query,
        answer=answer,
        confidence_score=passages[0].relevance_score,
        cited_sources=sources,
        retrieved_passages=passages,
    )
