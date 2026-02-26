'''
Q1. What does IVF stand for?

A.
IVF stands for Inverted File Index.
It is a method used in vector databases
to make similarity search faster.
'''
# Example:
# Instead of searching all vectors,
# IVF narrows the search to a few groups first.



'''
Q2. What is the main idea behind IVF?

A.
IVF divides all vectors into clusters (groups).
When a query comes, it searches only inside
the most relevant clusters.
'''
# Example:
# 1 million vectors
# Divided into 100 clusters
# Query searches only 3–5 clusters



'''
Q3. Why does clustering help make search faster?

A.
Because similar vectors are placed in the same group.
So we don’t need to check every vector.
'''
# Example:
# Looking for science book
# Go to science section
# Not the entire library



'''
Q4. How does IVF search step-by-step?

A.
1. Find which cluster center is closest to the query.
2. Search inside that cluster.
3. Return nearest vectors.
'''
# Example:
# Query → compare with 100 cluster centers
# Choose nearest 3 clusters
# Search only those clusters



'''
Q5. What is the trade-off in IVF?

A.
If we search too few clusters,
we might miss the true closest vector.
If we search more clusters,
search becomes slower but more accurate.
'''
# Example:
# Search 1 cluster → fastest, less accurate
# Search 5 clusters → slower, more accurate



'''
Q6. When is IVF useful?

A.
IVF is useful when we have very large datasets.
It scales well and reduces search space.
'''
# Example:
# Millions of vectors
# IVF helps avoid checking all of them



'''
Q7. How is IVF different from HNSW in simple terms?

A.
IVF groups vectors first and searches by region.
HNSW builds a graph and searches by navigation.
'''
# Example:
# IVF → choose correct shelf, then search books
# HNSW → walk through connected roads to reach target



'''
Q8. Interview-ready simple definition of IVF:

A.
IVF is an Approximate Nearest Neighbor method
that speeds up similarity search by clustering vectors
and searching only the most relevant clusters
instead of the entire dataset.
'''
# Example:
# Divide space into regions
# Search only promising regions
