'''
Q1. What happens in the embedding creation step?

A.
Each text chunk is converted into a numerical vector
using an embedding model.
'''
# Example:
# "Photosynthesis converts light..."
# → [0.12, -0.91, 0.44, ...]



'''
Q2. What is an embedding?

A.
An embedding is a list of numbers
that represents the semantic meaning of text.
'''
# Example:
# "cat" → vector A
# "kitten" → vector B
# A and B will be close in vector space



'''
Q3. Why do we create embeddings for each chunk?

A.
Because embeddings allow us to compare meaning mathematically.
This enables similarity search.
'''
# Example:
# User query → embedding
# Compare with stored chunk embeddings
# Retrieve most similar ones



'''
Q4. What is the transformation flow in this step?

A.
Text → Embedding model → Vector representation.
'''
# Example:
# Chunk text
# Passed to embedding model
# Returns 768-dimensional vector



'''
Q5. How does embedding enable similarity search?

A.
Vectors that represent similar meanings
are close to each other in vector space.
We measure distance between vectors.
'''
# Example:
# Query: "How do plants make food?"
# Close to chunk about photosynthesis



'''
Q6. What is the mental model of embedding creation?

A.
Convert meaning into numbers,
so computers can compare meanings efficiently.
'''
# Example:
# Words → Numbers
# Compare numbers → Find similar ideas

