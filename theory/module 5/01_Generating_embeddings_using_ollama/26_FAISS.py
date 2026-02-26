'''
Q1. What is FAISS?

A.
FAISS stands for Facebook AI Similarity Search.
It is a library used to perform fast similarity search
over large collections of vectors.
'''
# Example:
# 1 million embeddings
# FAISS helps find nearest ones quickly



'''
Q2. What problem does FAISS solve?

A.
FAISS solves the problem of slow brute-force search.
Instead of comparing a query with every vector,
it uses smart indexing methods to speed up search.
'''
# Example:
# Without FAISS → compare against all 10M vectors
# With FAISS → search using ANN index



'''
Q3. Is FAISS a full database?

A.
No.
FAISS is mainly a similarity search library.
It focuses on fast nearest neighbor search.
It does not manage metadata like a full database.
'''
# Example:
# FAISS → stores vectors
# You store text separately in another DB



'''
Q4. How does FAISS make search fast?

A.
It uses Approximate Nearest Neighbor (ANN) methods
like IVF and HNSW to avoid scanning all vectors.
'''
# Example:
# Cluster vectors (IVF)
# Search only relevant clusters



'''
Q5. Where is FAISS commonly used?

A.
It is used in:
- RAG systems
- Recommendation systems
- Image search
- Large-scale similarity search
'''
# Example:
# Query embedding
# FAISS returns top 5 closest vectors



'''
Q6. Why is FAISS important in AI systems?

A.
Because embeddings are everywhere in modern AI.
FAISS enables scalable semantic search
over millions or billions of vectors.
'''
# Example:
# Vector DB backend
# Retrieval step in RAG pipeline



'''
Q7. Interview-ready definition of FAISS:

A.
FAISS is an open-source library developed by Meta
for efficient similarity search and clustering
of high-dimensional vectors,
commonly used to power semantic retrieval systems.
'''
# Example:
# RAG → embeddings stored in FAISS
# Query → nearest neighbor search
