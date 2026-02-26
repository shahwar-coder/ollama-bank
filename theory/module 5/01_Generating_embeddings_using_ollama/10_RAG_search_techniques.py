'''
Q1. Why can’t we use brute-force search in large vector databases?

A.
Because brute-force requires computing distance
between the query vector and every stored vector.
With millions of vectors, this becomes too slow.
Time complexity becomes O(N).
'''
# Example:
# 10M vectors
# Query → compute 10M cosine similarities
# Too slow for real-time systems



'''
Q2. What is Approximate Nearest Neighbor (ANN) search?

A.
ANN is a method that finds vectors that are
almost nearest instead of exactly nearest.
It sacrifices tiny accuracy for massive speed gains.
'''
# Example:
# Exact nearest similarity = 0.92
# ANN returns 0.91
# Practically same for RAG purposes



'''
Q3. Why is approximation acceptable in RAG?

A.
Because retrieval is inherently fuzzy.
We only need highly relevant chunks,
not mathematically perfect neighbors.
'''
# Example:
# Retrieve top 5 relevant chunks
# Small ordering difference doesn’t change answer quality



'''
Q4. What conceptual shift does ANN introduce?

A.
It converts a geometry problem
into a navigation problem.
Instead of scanning everything,
we navigate a structured space.
'''
# Example:
# Instead of checking every coffee shop in a country,
# you search nearby promising areas first.



'''
Q5. What is the intuition behind HNSW?

A.
HNSW builds a multi-layer graph.
Search starts at a coarse level
and progressively refines at lower levels.
'''
# Example:
# Highway → main road → local street
# Move from broad region to precise target



'''
Q6. Why is HNSW fast?

A.
Because it performs guided graph traversal,
leading to near logarithmic search behavior.
It avoids scanning all nodes.
'''
# Example:
# 10M vectors
# Instead of checking 10M,
# Navigate through connected nodes efficiently



'''
Q7. What is the intuition behind IVF?

A.
IVF clusters vectors into groups.
Search first selects nearest clusters,
then searches only within those clusters.
'''
# Example:
# Library divided by topic
# First choose topic
# Then search only that shelf



'''
Q8. How do HNSW and IVF differ conceptually?

A.
HNSW → graph navigation approach.
IVF → cluster-based region pruning.
Both reduce search space differently.
'''
# Example:
# HNSW → walk network
# IVF → pick region, search locally



'''
Q9. Why are ANN indexes essential at scale?

A.
Because brute-force search scales linearly (O(N)).
ANN reduces effective search cost
towards logarithmic-like behavior.
'''
# Example:
# 1M vectors → brute force slow
# ANN → milliseconds retrieval



'''
Q10. Interview-ready explanation: Why do vector DBs use ANN?

A.
Vector databases use ANN methods like HNSW and IVF
to organize embedding space into structured navigable forms,
allowing fast nearest-neighbor search
without scanning all vectors.
This enables scalable semantic retrieval.
'''
# Example:
# Millions of embeddings
# Millisecond similarity search
