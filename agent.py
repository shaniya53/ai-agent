def summarize_text(text: str) -> str:
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    summary = ". ".join(sentences[:2])

    return summary if summary else "No summary generated"
