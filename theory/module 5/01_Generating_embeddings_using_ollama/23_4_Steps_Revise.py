'''
Q10. How are embeddings created? (Clear + simple revision notes)

👉 Step 1: Tokens → vectors (Embedding layer)
- Sentence is split into tokens (words/subwords)
- Each token is mapped to a numeric vector
Example:
"reverse python list" → ["reverse","python","list"] → vectors

👉 Step 2: Transformer self-attention → context understanding
- Tokens look at each other using attention
- Meaning gets refined based on neighbors
Example:
"list" understands programming context due to "python"

👉 Step 3: Pooling → single sentence vector
- All token vectors are combined (mean/CLS pooling)
- Produces ONE dense vector representing the whole sentence
Example:
3 token vectors → averaged → sentence embedding

👉 Step 4: Similarity comparison
- Query embedding compared with stored embeddings
- Cosine similarity measures semantic closeness
Example:
"invert python list" ≈ "reverse python list"

👉 Core insight:
Embeddings convert language meaning into geometry,
so semantically similar sentences lie close in vector space.

👉 Example summary:
Sentence → 768D vector → nearest neighbor retrieval
'''