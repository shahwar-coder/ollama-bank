'''
FAISS (Concise Summary)

👉 What does FAISS store?
- Dense embedding vectors (points in high-dimensional space)

👉 How does it store?
- Uses indexes (Flat, IVF, HNSW) to organize vectors for fast search
# Flat: 
One by one sequentially

# IVF: 
Cluster A → v1, v8, v12
Cluster B → v2, v3
Cluster C → v4, v5, v6

# HNSW
v1 — v2 — v3
 |     |
v5 — v7

👉 Why store vectors?
- Semantic similarity = geometric closeness
- Enables meaning-based retrieval

👉 What does FAISS do with them?
- Converts query → vector
- Finds nearest stored vectors using similarity metrics
- Returns semantically similar items

⭐ One-line:
FAISS stores embeddings, indexes them efficiently, and performs fast nearest neighbor similarity search.
'''