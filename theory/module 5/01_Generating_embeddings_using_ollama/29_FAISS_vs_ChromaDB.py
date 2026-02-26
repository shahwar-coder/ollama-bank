'''
FAISS vs Chroma (Clean Comparison)

+----------------------+---------------------------+-----------------------------+
| Feature              | FAISS                     | Chroma                      |
+----------------------+---------------------------+-----------------------------+
| Category             | ANN search library        | Vector database             |
| Main role            | Fast similarity search    | Storage + retrieval system  |
| Stores vectors       | Yes                       | Yes                         |
| Stores documents     | No                        | Yes                         |
| Stores metadata      | No                        | Yes                         |
| Persistence          | Limited/manual            | Built-in                    |
| Filtering            | No                        | Yes                         |
| API layer            | No                        | Yes                         |
| Production ready DB  | No                        | Moderate (dev-focused)      |
| Typical use          | Custom pipelines/research | Local RAG apps/prototypes   |
+----------------------+---------------------------+-----------------------------+

⭐ Core takeaway:
FAISS = search engine
Chroma = searchable vector storage system
'''

# =====

'''
FAISS vs Chroma — Feature Meanings

Category
👉 Type of tool
- Library, database, service, etc.

Main role
👉 Primary purpose of the tool
- What problem it mainly solves

Stores vectors
👉 Whether tool can hold embedding vectors
- Numeric representations used for similarity search

Stores documents
👉 Whether original text/data linked to embeddings is stored
- Needed to return actual content after retrieval

Stores metadata
👉 Ability to store extra attributes
Example:
source="pdf", author="john", page=3

Persistence
👉 Whether data survives restart
- Saved on disk automatically vs manual saving

Filtering
👉 Ability to search using metadata conditions
Example:
retrieve docs where source="blog"

API layer
👉 High-level interface for developers
- Functions/endpoints to insert, query, manage data

Production ready DB
👉 Suitable for scalable real-world deployments
- Reliability, scaling, infra features

Typical use
👉 Common real-world scenarios where tool is applied

⭐ Insight:
Features move from low-level engine capability → full database capability
'''