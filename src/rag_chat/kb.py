from rag_chat.engine import SimpleVectorStore


def populate_sample_knowledge_base() -> SimpleVectorStore:
    """Populates an in-memory knowledge store with sample enterprise policy documents."""
    store = SimpleVectorStore()

    store.add_document(
        title="Employee Handbook 2026.pdf",
        section="Section 4.2 - Remote Work Policy",
        text=(
            "Employees are eligible for full remote work after completing their 90-day probationary period. "
            "The company provides a monthly 75 EUR home office and high-speed internet stipend."
        ),
    )

    store.add_document(
        title="Employee Handbook 2026.pdf",
        section="Section 7.1 - Paid Time Off (PTO)",
        text=(
            "All full-time staff accrue 25 days of annual paid leave plus official national holidays. "
            "Vacation requests over 5 days require at least 14 days advance manager approval."
        ),
    )

    store.add_document(
        title="Information Security Guidelines.pdf",
        section="Section 2.4 - Password Requirements",
        text=(
            "Corporate credentials must be at least 16 characters long and use mandatory MFA. "
            "Passwords must never be stored in plaintext or shared across unencrypted channels."
        ),
    )

    store.add_document(
        title="Expense Reimbursement Policy.pdf",
        section="Section 3.1 - Travel Expenses",
        text=(
            "Meals during business travel are reimbursed up to 60 EUR per day. "
            "Original itemized receipts must be submitted within 30 days of the trip."
        ),
    )

    return store
