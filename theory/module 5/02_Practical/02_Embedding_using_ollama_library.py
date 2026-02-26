import ollama

def generate_embedding(text: str) -> list[float]:
    """
    Generate embedding for input text using Ollama.
    """

    # Ollama Embedding
    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )

    # Embedding
    embedding = response.embedding

    # Validate 
    if embedding is None:
        raise RuntimeError("Embedding not returned by model")

    return embedding


# Useing
if __name__ == "__main__":
    text_to_embed = "The sun is the center of our solar system."

    embedding = generate_embedding(text_to_embed)

    print("\n=== Embedding Generated ===")
    print(f"Dimension: {len(embedding)}")
    print(f"Preview (first 10 dims): {embedding[:10]}")

# OUTPUT

# === Embedding Generated ===
# Dimension: 768
# Preview (first 10 dims): [0.5617655515670776, 1.0531878471374512, -3.035295009613037, -0.030941616743803024, 0.16354578733444214, 0.5733382701873779, 0.10614123195409775, -1.6527913808822632, 0.9216956496238708, -1.0621384382247925]