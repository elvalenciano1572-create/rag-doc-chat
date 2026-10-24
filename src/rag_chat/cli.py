import argparse
import sys

from rag_chat.engine import answer_query_with_rag
from rag_chat.kb import populate_sample_knowledge_base


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Retrieval-Augmented Generation (RAG) semantic document QA engine."
    )
    parser.add_argument(
        "query",
        nargs="?",
        default="What is the monthly stipend for remote work?",
        help="Question to ask the document knowledge base",
    )
    args = parser.parse_args(argv)

    store = populate_sample_knowledge_base()

    print("=" * 72)
    print("   RAG-DOC-CHAT: SEMANTIC DOCUMENT INTELLIGENCE ENGINE")
    print("=" * 72)
    print(f"[*] Indexed {len(store.chunks)} document chunks across corporate policy PDFs.")
    print(f"[*] User Question: \"{args.query}\"\n")

    rag_answer = answer_query_with_rag(args.query, store)

    print("--- GROUNDED SYNTHESIS ANSWER ---")
    print(rag_answer.answer)
    print(f"\nConfidence Score: {rag_answer.confidence_score * 100:.0f}%")
    print("Cited Sources:")
    for s in rag_answer.cited_sources:
        print(f"  * {s}")

    print("\n" + "=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
