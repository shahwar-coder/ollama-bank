from langchain_ollama import OllamaEmbeddings

# instance
embedding_functions = OllamaEmbeddings(model="nomic-embed-text")

# docs or consider them small chunks
docs = [
    "The sun is the center of our solar system.",
    "Mercury is the smallest planet in our solar system.",
    "Venus is similar in size to Earth but very hot.",
    "Mars is known as the red planet because of iron oxide.",
    "Jupiter is the largest planet and has a Great Red Spot.",
]

# docs embedding
docs_embeddings = embedding_functions.embed_documents(docs)

print(len(docs_embeddings))
# print(docs_embeddings[0])

# OUTPUT:
# 5