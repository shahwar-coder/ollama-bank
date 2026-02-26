from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

# OllamaEmbedding instance
embedding_functions = OllamaEmbeddings(model="nomic-embed-text")

# Documents (chunks)
docs = [
    "The sun is the center of our solar system.",
    "Mercury is the smallest planet in our solar system.",
    "Venus is similar in size to Earth but very hot.",
    "Mars is known as the red planet because of iron oxide.",
    "Jupiter is the largest planet and has a Great Red Spot.",
]

# Vector Database
vector_store = Chroma.from_texts(
    texts=docs,
    embedding=embedding_functions
)

# Query
query = "Which planet is the biggest ?"

results = vector_store.similarity_search(query)

print(results[0].page_content) # closest vector

# OUTPUT:
# Jupiter is the largest planet and has a Great Red Spot.
# note : this is the closest vector

'''
Execution Flow (Concise)

1️⃣ Setup
- OllamaEmbeddings initialized → embedding model ready

2️⃣ Ingestion
Chroma.from_texts(...)
- Each document → OllamaEmbeddings → vector
- Chroma stores (document, vector, ID)

3️⃣ Query stage
query = "Which planet is the biggest?"
- Query passed to similarity_search()

4️⃣ Query embedding
- Same embedding model converts query → vector
👉 Shared embedding space

5️⃣ Retrieval
- Chroma compares query vector with stored vectors
- Similarity search (ANN + cosine/dot)
- Retrieves nearest document

6️⃣ Output
- Top result returned
- "Jupiter is the largest planet..." printed

⭐ Summary:
Docs → embed → store → query → embed → similarity search → retrieve answer
'''