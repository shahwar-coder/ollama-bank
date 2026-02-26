'''
🧠 Semantic Search / Embedding Pipeline Steps

1️⃣ Token → vector projection
- Text is tokenized
- Each token converted into initial embedding vector

2️⃣ Contextualization via transformer layers
- Tokens interact using attention
- Embeddings become context-aware

3️⃣ Pooling into a single sentence vector
- Token embeddings aggregated (mean / CLS / max)
- Produces one dense vector per text

4️⃣ Similarity comparison
- Query vector compared with stored vectors
- Cosine / dot / L2 used to retrieve nearest neighbors

👉 Overall:
Text → Embedding → Similarity → Retrieval
'''

# ============

'''
Q1. What is the overall goal of creating an embedding?

A.
The goal is to convert a full sentence into one vector
that captures its meaning.
This vector should allow us to compare meanings using math.
'''
# Example:
# "Plants convert sunlight into energy"
# → [0.12, -0.55, 0.91, ...]
# This list of numbers represents the sentence meaning.



'''
Q2. What happens in Step 1: Token → vector projection?

A.
Each word (token) is converted into an ID.
That ID is used to look up a row in a big embedding table.
This gives the token its initial vector.
At this stage, meaning is not context-aware.
'''
# Example:
# "bank" → same initial vector
# Whether sentence is about money or river
# Context not applied yet.



'''
Q3. Why is Step 2 (Contextualization) the most important step?

A.
Because here tokens interact with each other
using self-attention.
Each word updates its vector based on surrounding words.
This creates context-aware meaning.
'''
# Example:
# "river bank" → bank learns about river
# "money bank" → bank learns about finance
# Same word, different final vectors.



'''
Q4. What does self-attention do in simple terms?

A.
Each word looks at other words
and decides which ones are important.
It then updates its meaning accordingly.
'''
# Example:
# In "Plants convert sunlight into energy"
# "sunlight" pays attention to "plants" and "energy"
# So its vector changes accordingly.



'''
Q5. Why do we need pooling (Step 3)?

A.
Because after contextualization,
we have one vector per token.
But for search, we need one vector per sentence.
Pooling combines all token vectors into one.
'''
# Example:
# 5 tokens → 5 vectors
# Mean pooling → 1 sentence vector



'''
Q6. What does pooling represent conceptually?

A.
Pooling is semantic compression.
It summarizes the whole sentence
into a single coordinate in meaning space.
'''
# Example:
# Like summarizing a paragraph
# But instead of text summary → numeric summary.



'''
Q7. What happens in Step 4: Similarity comparison?

A.
We compare two sentence vectors
using cosine similarity.
If they point in similar directions,
their meanings are similar.
'''
# Example:
# "Plants make food"
# "Photosynthesis produces energy"
# High cosine similarity → close meaning.



'''
Q8. Why does direction matter more than magnitude?

A.
Because meaning is encoded in vector direction.
Magnitude can change due to length or emphasis.
Cosine similarity focuses on direction only.
'''
# Example:
# Short sentence vs longer version
# Same idea → similar direction.



'''
Q9. What is the deep mental model of embedding creation?

A.
It is a pipeline of:
Lexical grounding → Meaning formation → Compression → Geometric comparison.
Each step builds toward usable semantic vectors.
'''
# Example:
# Tokens → Context-aware tokens → Sentence vector → Similarity search.



'''
Q10. Interview-ready explanation: How are embeddings created?

A.
Embeddings are created by first mapping tokens to vectors,
then refining them through transformer self-attention
to become context-aware,
then pooling them into a single sentence vector,
which can be compared geometrically using cosine similarity.
This process turns language into measurable semantic space.
'''
# Example:
# Sentence → 768D vector → nearest neighbor search.
