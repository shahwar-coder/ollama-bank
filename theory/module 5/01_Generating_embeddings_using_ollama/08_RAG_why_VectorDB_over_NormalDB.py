'''
Q1. What core problem does a vector database solve in RAG?

A.
It solves the problem of semantic search.
Users and documents may use different words,
but mean the same thing.
Vector databases retrieve based on meaning.
'''
# Example:
# Query: "How do plants make food?"
# Doc: "Photosynthesis converts light into energy."
# Vector DB → Match
# Normal DB → No keyword match



'''
Q2. Why do normal databases fail for semantic search?

A.
Normal databases perform symbolic matching.
They compare exact words or patterns,
not meaning.
'''
# Example:
# Query: "car"
# Doc: "automobile"
# Normal DB → No match



'''
Q3. What does a vector database store differently?

A.
It stores embeddings.
Embeddings are numerical representations
of semantic meaning.
'''
# Example:
# "car" → [0.12, -0.8, 0.3]
# "automobile" → [0.11, -0.79, 0.32]
# These vectors are close in space



'''
Q4. What makes similarity search computationally hard?

A.
It requires distance calculations
across high-dimensional vectors.
This is expensive without specialized indexing.
'''
# Example:
# Compare query vector
# Against 1 million stored vectors
# Using cosine similarity



'''
Q5. What special techniques do vector databases use?

A.
They use Approximate Nearest Neighbor (ANN) indexes
like HNSW or IVF
to enable fast similarity search.
'''
# Example:
# Instead of scanning all vectors
# ANN quickly finds nearest neighbors



'''
Q6. What is the geometric intuition behind embeddings?

A.
Each embedding is a point in high-dimensional space.
Similar meanings are close together.
Different meanings are far apart.
'''
# Example:
# "child" and "kid" → close points
# "child" and "airplane" → far apart



'''
Q7. Why would RAG fail without a vector database?

A.
Because retrieval would rely only on keywords,
leading to low recall and brittle results.
Semantic retrieval is essential.
'''
# Example:
# Keyword search misses paraphrases
# Semantic search captures intent



'''
Q8. What is the strongest mental comparison?

A.
Normal DB searches symbols.
Vector DB searches meaning.
'''
# Example:
# Normal DB → match exact text
# Vector DB → match semantic intent



'''
Q9. What is the interview-ready explanation?

A.
Vector databases are required because semantic search
involves nearest-neighbor retrieval in high-dimensional
embedding space, which requires specialized indexing
and distance computation not supported efficiently
by traditional databases.
'''
# Example:
# Millions of embeddings
# Fast similarity retrieval using ANN index
