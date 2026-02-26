'''
✅ Step 4 — Retrieval (RAG Pipeline)

Flow:
Query → Vector DB → Retrieve relevant chunks

1️⃣ User question
Example:
"How does photosynthesis work?"

2️⃣ Query embedding
- Same embedding model used for documents
- Question converted into vector

👉 Important:
Query and documents lie in a shared embedding space

3️⃣ Similarity search
- Vector DB compares query vector with stored chunk vectors
- Uses cosine similarity / inner product
- ANN search enables fast retrieval

4️⃣ Output
👉 Top-k most similar chunks returned for generation
'''

# ==========

'''
Q1. What happens in Step 4 — Retrieval in the online phase?

A.
When the user asks a question,
the system converts that question into an embedding
and searches the vector database for similar chunks.
'''
# Example:
# User: "How does photosynthesis work?"
# → Convert to vector
# → Search vector DB
# → Return top relevant chunks



'''
Q2. Why must we use the same embedding model for documents and queries?

A.
Because both must live in the same embedding space.
If they are not in the same space,
their vectors cannot be compared correctly.
'''
# Example:
# Docs embedded using Model A
# Query embedded using Model B
# → Similarity comparison becomes unreliable



'''
Q3. What does “shared embedding space” mean?

A.
It means both document chunks and user queries
are converted into vectors using the same model,
so similar meanings land near each other.
'''
# Example:
# Doc: "Photosynthesis converts sunlight..."
# Query: "How do plants make food?"
# Same model → close vectors → successful retrieval



'''
Q4. What is similarity search in simple terms?

A.
It means finding vectors that are closest
to the query vector in meaning space.
'''
# Example:
# Query vector → compare with stored vectors
# Return top 3 closest ones



'''
Q5. What mathematical tools are used for similarity?

A.
Common methods include:
- Cosine similarity
- Inner product (dot product)
- L2 distance
'''
# Example:
# High cosine score → meanings aligned
# Low cosine score → meanings different



'''
Q6. What does “top-k chunks” mean?

A.
It means returning the top K most similar document chunks.
K is a chosen number like 3, 5, or 10.
'''
# Example:
# top_k = 5
# System returns 5 most relevant chunks



'''
Q7. Why is retrieval quality critical at this stage?

A.
Because these retrieved chunks
become the context for the LLM.
If retrieval is wrong,
generation will also be wrong.
'''
# Example:
# Wrong chunk retrieved
# → LLM answers incorrectly
# Correct chunk retrieved
# → Grounded accurate answer



'''
Q8. Strong mental model of Step 4:

A.
Think of it as asking:
“Which stored meanings are closest
to this new meaning?”
The vector DB finds neighbors in semantic space.
'''
# Example:
# Query meaning → semantic map
# Retrieve nearest semantic neighbors



'''
Q9. Interview-ready explanation of retrieval step:

A.
In the online phase of RAG,
the user query is embedded into the same semantic space
as stored document embeddings,
and a similarity search (often via ANN)
retrieves the top-k nearest chunks
to provide relevant context for generation.
'''
# Example:
# Query → embedding → ANN search → top-k chunks
