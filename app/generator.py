from openai import OpenAI

from app.config import Config


client = OpenAI(api_key=Config.OPENAI_API_KEY)


def generate_answer(
    question: str,
    context: list[dict]
) -> str:
    """Generate an answer using the retrieved context."""

    context_text = "\n\n".join(
        f"- {item['text']}"
        for item in context
    )

    response = client.chat.completions.create(
        model=Config.OPENAI_LLM_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. "
                    "Answer the user's question using only "
                    "the provided context. "
                    "If the answer is not contained in the context, "
                    "say that there is not enough information."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Context:\n{context_text}\n\n"
                    f"Question:\n{question}"
                )
            }
        ]
    )

    return response.choices[0].message.content or ""