'''
Chroma.from_texts() — What actually happened (Concise conclusion)

👉 Key line
Chroma.from_texts(texts=docs, embedding=embedding_functions)
is a high-level ingestion helper that hides multiple steps.

👉 Internal flow
1. Each document is taken from docs
2. LangChain calls embedding_functions.embed_documents()
3. OllamaEmbeddings creates vectors (embedding stage)
4. Chroma receives (text, vector) pairs
5. Chroma stores vectors + documents + auto IDs

👉 Important clarification
- Embeddings are created by OllamaEmbeddings
- Chroma does NOT create embeddings
- Chroma only stores and indexes them

👉 Mental model
Text → Embedding model → Vector DB

👉 Why confusion occurs
Helper APIs abstract the pipeline, making embedding generation appear part of Chroma.

⭐ Final takeaway:
During Chroma.from_texts() ingestion, LangChain first generated embeddings using OllamaEmbeddings and then stored the resulting vectors with documents inside Chroma.
'''