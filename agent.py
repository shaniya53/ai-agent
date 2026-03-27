def summarize_text(text: str) -> str:
    # simple AI-like summarization (rule-based)
    sentences = text.split(".")
    summary = ".".join(sentences[:2]).strip()

    if not summary:
        return "No summary generated"

    return summary
