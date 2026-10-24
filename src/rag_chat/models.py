from pydantic import BaseModel, Field


class DocumentChunk(BaseModel):
    chunk_id: str
    source_document: str
    page_or_section: str
    text_content: str


class RetrievedPassage(BaseModel):
    chunk: DocumentChunk
    relevance_score: float = Field(ge=0.0, le=1.0)


class RAGAnswer(BaseModel):
    query: str
    answer: str
    confidence_score: float = Field(ge=0.0, le=1.0)
    cited_sources: list[str] = Field(default_factory=list)
    retrieved_passages: list[RetrievedPassage] = Field(default_factory=list)
