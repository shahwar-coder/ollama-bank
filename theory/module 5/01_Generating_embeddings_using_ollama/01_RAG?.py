'''
Q1. What is RAG?

A.
RAG (Retrieval Augmented Generation) is a method where
an LLM first retrieves relevant information from external data,
then uses that information to generate an answer.
'''
# Example:
# User asks: "What is our refund policy?"
# System retrieves company document
# LLM generates answer using that document



'''
Q2. Why do we need RAG?

A.
Because LLMs do not know your private or latest data.
RAG allows them to use external knowledge sources.
'''
# Example:
# LLM alone → Cannot know your internal database
# RAG → Retrieves internal docs before answering



'''
Q3. What are the main steps in RAG?

A.
1. Convert query into embedding
2. Search similar documents (vector search)
3. Retrieve relevant text
4. Send retrieved text + question to LLM
5. Generate answer
'''
# Example:
# Query → embedding
# Compare with stored embeddings
# Retrieve top 3 documents
# Pass to model for final answer



'''
Q4. What problem does RAG solve?

A.
It reduces hallucination and improves accuracy
by grounding the model in real data.
'''
# Example:
# Without RAG → Model guesses answer
# With RAG → Model cites retrieved document



'''
Q5. What technologies are typically used in RAG?

A.
- Embedding model
- Vector database
- LLM
- Retrieval logic
'''
# Example:
# Text → embedding model
# Store in vector DB
# Query → similarity search → LLM answer



'''
Q6. What is the simple mental model of RAG?

A.
Search first.
Answer second.
'''
# Example:
# Like open-book exam:
# Look at book → then write answer
