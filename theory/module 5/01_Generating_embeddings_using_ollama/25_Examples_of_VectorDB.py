'''
Vector DB / ANN Tool Selection (Concise Summary)

FAISS
👉 Similarity search library
Use when: local experiments, research, custom pipelines
Think: ANN engine only

Chroma
👉 Lightweight developer vector DB
Use when: local RAG apps, prototypes, simple persistence
Think: SQLite for vectors

Pinecone
👉 Managed cloud vector DB
Use when: production apps, scaling, zero infra management
Think: SaaS vector database

Weaviate
👉 Feature-rich vector DB
Use when: hybrid search, structured data, self-hosted production
Think: Postgres + vectors + graph

⭐ Rule of thumb:
Learn → FAISS
Prototype → Chroma
Scale → Pinecone
Complex retrieval → Weaviate
'''