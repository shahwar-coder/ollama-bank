'''
Q1. What does HNSW stand for?

A.
HNSW stands for Hierarchical Navigable Small World.
It is a smart way of organizing vectors
so we can search them quickly.
'''
# Example:
# H → Hierarchical (many layers)
# N → Navigable (we can move through it)
# SW → Small World (nodes are well connected)



'''
Q2. What is HNSW in simple terms?

A.
HNSW is a graph-based search method.
It connects vectors like a road network,
so we can quickly travel to the closest one.
'''
# Example:
# Imagine cities connected by highways.
# To reach a city, you:
# 1. Start from big highways
# 2. Move to smaller roads
# 3. Reach the exact street



'''
Q3. Why is it called “Hierarchical”?

A.
Because it has multiple layers.
Top layer = few nodes (big overview).
Bottom layer = all nodes (detailed level).
'''
# Example:
# Top → zoomed-out map
# Bottom → full street-level map



'''
Q4. Why is it called “Small World”?

A.
Because in the graph,
most nodes are connected through short paths.
You can reach far nodes with few steps.
'''
# Example:
# Like social networks:
# You can reach almost anyone
# through a few mutual friends



'''
Q5. Interview-ready simple definition of HNSW:

A.
HNSW is a graph-based Approximate Nearest Neighbor algorithm
that organizes vectors into layered networks,
allowing fast navigation to similar vectors
without scanning all data.
'''
# Example:
# Millions of vectors
# HNSW helps find closest ones in milliseconds
