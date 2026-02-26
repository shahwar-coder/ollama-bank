'''
Sentence → 768D vector → nearest neighbor retrieval (Explanation)

👉 Sentence
- A piece of text whose meaning we want to represent
Example:
"How to reverse a python list"

👉 768D vector
- The embedding model converts the sentence into a vector
- 768D = 768 numbers describing semantic meaning
- Each dimension captures some latent feature of meaning

Think:
Sentence → [0.12, -0.44, 0.98, ..., 0.07]  (768 values)

👉 Why 768 numbers?
- Model architecture defines embedding size
- More dimensions → richer representation of meaning

👉 Nearest neighbor retrieval
- Query vector compared with many stored vectors
- Similarity metric (cosine/dot) measures closeness
- Closest vectors = semantically similar documents

Example:
Query:
"How to invert a python list"
→ embedding

Database:
"Python list reverse method"
→ embedding

If vectors are close → retrieved

👉 Core idea:
Text meaning → point in high-dimensional space
Retrieval = find closest points
'''