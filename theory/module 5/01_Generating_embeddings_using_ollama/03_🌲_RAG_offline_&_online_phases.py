'''
Q1. What are the two main phases of a RAG system?

A.
RAG has two main phases:
1. Offline phase → Build the knowledge store
2. Online phase → Answer user questions
'''
# Example:
# Offline → Process documents and store embeddings
# Online → Retrieve relevant chunks and generate answer



'''
Q2. What happens in the Offline phase?

A.
In the offline phase, documents are:
- Collected
- Split into chunks
- Converted into embeddings
- Stored in a vector database
'''
# Example:
# PDF → split into paragraphs
# Paragraph → embedding vector
# Store in vector DB



'''
Q3. Why is the Offline phase done separately?

A.
Because embedding and indexing large data
is expensive and should not happen per user request.
'''
# Example:
# 10,000 documents embedded once
# Not embedded every time user asks a question



'''
Q4. What happens in the Online phase?

A.
In the online phase:
1. User sends question
2. Question converted to embedding
3. Similar documents retrieved
4. Retrieved text added to prompt
5. LLM generates answer
'''
# Example:
# User: "What is refund policy?"
# Retrieve relevant document chunk
# LLM answers using that chunk



'''
Q5. What components exist in a high-level RAG architecture?

A.
- Document storage
- Embedding model
- Vector database
- LLM
- Retrieval logic
'''
# Example:
# Docs → Embeddings → Vector DB
# Query → Embedding → Search → LLM



'''
Q6. What is the simple mental model of RAG architecture?

A.
Offline → Build searchable knowledge memory.
Online → Search memory and answer intelligently.
'''
# Example:
# Offline = Build library
# Online = Search library and respond



'''
Q7. Why is this separation important in production systems?

A.
It improves performance, scalability,
and cost efficiency.
Heavy processing is done once (offline),
fast retrieval happens during user interaction (online).
'''
# Example:
# Pre-index company documents overnight
# Users get instant answers during the day
