'''
Q1. What are the four main capabilities exposed by the Ollama Python library?

A.
The four main capabilities are:
- generate → for raw text generation
- chat → for conversation-style interaction
- embeddings → for vector generation
- list/pull → for model management
'''
# Example:
# generate → "Explain AI"
# chat → Multi-message conversation
# embeddings → Convert text to vector
# pull → Download a model



'''
Q2. What is "generate" used for?

A.
"generate" is used when you want simple text output from a model.
You give a prompt, and the model returns text.
'''
# Example:
# Prompt: "What is machine learning?"
# Output: Explanation paragraph



'''
Q3. What is "chat" used for?

A.
"chat" is used for conversation-based interaction.
It supports roles like system, user, and assistant.
'''
# Example:
# User: "Hello"
# Assistant: "Hi! How can I help?"
# Maintains conversational structure



'''
Q4. What are "embeddings"?

A.
Embeddings convert text into numerical vectors.
These vectors represent meaning in mathematical form.
'''
# Example:
# "cat" → [0.21, -0.44, 0.98, ...]
# Used in search, similarity, RAG systems



'''
Q5. What are "list" and "pull" used for?

A.
They are used for model management.
"list" shows available models.
"pull" downloads a model from Ollama registry.
'''
# Example:
# pull → Download llama3
# list → See installed models



'''
Q6. Why is this mental model important?

A.
Because once you understand these four functions,
you understand how to use the Ollama Python library effectively.
'''
# Example:
# Build chatbot → use chat
# Build RAG → use embeddings
# Simple text generation → use generate
