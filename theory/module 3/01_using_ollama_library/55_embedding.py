import ollama

emb = ollama.embeddings(
    model='nomic-embed-text',
    prompt='LLMs are powerful'
)

vector = emb['embedding']

# /=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=

'''
Q1. What is the purpose of ollama.embeddings()?

A.
It converts text into a numerical vector representation.
This vector captures the semantic meaning of the text.
'''
# Example:
# Text: "LLMs are powerful"
# Output: [0.021, -0.883, 0.441, ...]  # list of numbers



'''
Q2. Why are embeddings important for RAG?

A.
Because RAG (Retrieval-Augmented Generation) uses embeddings
to search and retrieve similar documents based on meaning.
'''
# Example:
# Query → converted to vector
# Compare with stored document vectors
# Retrieve most similar ones



'''
Q3. What type of data is returned by ollama.embeddings()?

A.
It returns a dictionary.
The actual vector is stored inside the key 'embedding'.
'''
# Example:
# emb = ollama.embeddings(...)
# vector = emb['embedding']



'''
Q4. What is the structure of the embedding output?

A.
The embedding is a list of floating-point numbers.
Each number represents one dimension in vector space.
'''
# Example:
# [0.12, -0.44, 0.98, 0.003, ...]
# Length might be 768 or 1024 depending on model



'''
Q5. Why do we use a special model like 'nomic-embed-text'?

A.
Because embedding models are trained specifically
to generate high-quality semantic vectors.
They are different from chat models.
'''
# Example:
# llama3 → text generation
# nomic-embed-text → vector generation



'''
Q6. What is the core mental model of embeddings?

A.
Text → Mathematical vector → Compare vectors → Measure similarity.
'''
# Example:
# "cat" and "kitten"
# Their vectors will be close in vector space
