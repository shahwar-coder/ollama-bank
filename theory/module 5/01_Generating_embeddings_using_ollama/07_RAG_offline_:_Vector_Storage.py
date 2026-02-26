'''
Q1. What happens in the vector storage step?

A.
Each chunk and its embedding are stored together
inside a vector database.
This allows fast similarity search later.
'''
# Example:
# ("Refund policy text...", [0.21, -0.88, ...])



'''
Q2. What exactly is stored in a vector database?

A.
Typically:
- The chunk text
- Its embedding vector
- Optional metadata (source, page number, etc.)
'''
# Example:
# {
#   text: "Shipping takes 5 days",
#   embedding: [...],
#   source: "policy.pdf"
# }



'''
Q3. Why do we need a vector database instead of a normal database?

A.
Because vector databases are optimized
for similarity search in high-dimensional space.
'''
# Example:
# Normal DB → exact keyword match
# Vector DB → semantic similarity match



'''
Q4. What are some popular vector databases?

A.
Examples include:
- FAISS
- Chroma
- Pinecone
- Weaviate
- Milvus
'''
# Example:
# Small local project → FAISS or Chroma
# Production cloud → Pinecone or Weaviate



'''
Q5. What does the vector store represent in RAG?

A.
It represents the system’s knowledge memory.
It holds all searchable semantic information.
'''
# Example:
# Ingest 10,000 document chunks
# Store in vector DB
# Now AI can search them



'''
Q6. What is the simple mental model of vector storage?

A.
Vector database = searchable semantic memory.
'''
# Example:
# Like a smart library index
# Instead of keyword search → meaning search
