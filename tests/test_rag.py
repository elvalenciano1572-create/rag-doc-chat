from rag_chat.cli import main
from rag_chat.engine import answer_query_with_rag
from rag_chat.kb import populate_sample_knowledge_base


def test_rag_retrieval_and_answer():
    store = populate_sample_knowledge_base()
    ans = answer_query_with_rag("remote work monthly stipend", store)

    assert ans.confidence_score > 0.5
    assert "75 EUR" in ans.answer
    assert any("Remote Work" in s for s in ans.cited_sources)


def test_rag_password_query():
    store = populate_sample_knowledge_base()
    ans = answer_query_with_rag("password length requirements MFA", store)

    assert "16 characters" in ans.answer
    assert any("Security" in s for s in ans.cited_sources)


def test_unrelated_query_no_hallucination():
    store = populate_sample_knowledge_base()
    ans = answer_query_with_rag("how to bake chocolate cookies", store)

    assert "could not find any relevant information" in ans.answer
    assert ans.confidence_score < 0.3
    assert len(ans.cited_sources) == 0


def test_cli_execution(capsys):
    exit_code = main(["remote work stipend"])
    assert exit_code == 0
    captured = capsys.readouterr()
    assert "RAG-DOC-CHAT" in captured.out
    assert "GROUNDED SYNTHESIS ANSWER" in captured.out
    assert "75 EUR" in captured.out
