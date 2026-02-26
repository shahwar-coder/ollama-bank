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

# Chroma import
from langchain_chroma import Chroma

# creating vector DB (observe docs sent)
vector_store = Chroma.from_texts(
    texts=docs,
    embedding=embedding_functions
)

# Let's include, things we want to view
print(vector_store.get(include=["embeddings", "documents"]))


# {'ids': ['2772b0de-0412-496f-a557-41ae481d48a4', 'd25660a8-a6f7-41b6-a728-808c768f9a0d', 'be4a7b68-28ab-4761-92e6-e7fbef497935', 'f73b2629-6800-4e19-89f3-4840f28102a4', '400fde7f-4ab6-4870-832d-cb8bce73067b'], 'embeddings': array([[ 0.02672174,  0.05009743, -0.14438115, ..., -0.02557331,
#         -0.03402628,  0.00548904],
#        [ 0.03901497,  0.07034627, -0.12148141, ..., -0.03879009,
#         -0.02108884,  0.00626686],
#        [ 0.0244995 ,  0.0315018 , -0.17647307, ..., -0.03408054,
#         -0.02840918, -0.03443585],
#        [ 0.03822244,  0.11493397, -0.16278915, ..., -0.05367164,
#         -0.03943541,  0.0075313 ],
#        [-0.00425757,  0.12322996, -0.15986174, ..., -0.04274162,
#         -0.03890765,  0.02324675]], shape=(5, 768)), 'documents': ['The sun is the center of our solar system.', 'Mercury is the smallest planet in our solar system.', 'Venus is similar in size to Earth but very hot.', 'Mars is known as the red planet because of iron oxide.', 'Jupiter is the largest planet and has a Great Red Spot.'], 'uris': None, 'included': ['embeddings', 'documents'], 'data': None, 'metadatas': None}

'''
What happened in this code (Concise)

1️⃣ Embedding model created
- OllamaEmbeddings("nomic-embed-text") initialized
- Used to convert text → vectors

2️⃣ Documents prepared
- 5 short texts treated as chunks

3️⃣ Vector DB created (Chroma.from_texts)
- Each text passed to embedding model
- Text → 768D embedding vector
- Chroma stored:
  ✓ embeddings
  ✓ original documents
  ✓ auto-generated IDs

4️⃣ Data inspection
- vector_store.get(include=["embeddings","documents"])
- Returned stored embeddings matrix (5 × 768)
- Returned corresponding documents

⭐ Summary:
Texts were embedded using Ollama, stored in Chroma with IDs, and retrieved showing document–embedding mapping.
'''

# if we want disk persistence:
# Chroma.from_texts(
#     texts=docs,
#     embedding=embedding_functions,
#     persist_directory="./chroma_db"
# )

# 👉 Chroma does NOT create embeddings
# It:
# calls embedding function we provided
# receives vectors
# stores them

# 2772b0de-0412-496f-a557-41ae481d48a4 etc..
# UUIDs -> Unique reference to each chunk
# This help identify chunks
# Vector DB operations need ID