'''
Q1. Where does Ollama Python sit inside an AI agent architecture?

A.
It sits in the inference layer.
It is responsible for sending prompts to the model
and receiving generated output.
'''
# Example:
# User → Agent logic → ollama.chat() → Model → Response



'''
Q2. What is the full high-level flow of an AI agent using Ollama?

A.
User → Agent → Tools (if needed) → Ollama Python → Model → Output
'''
# Example:
# User asks question
# Agent decides to call LLM
# LLM returns reasoning or JSON
# Agent executes tool if required



'''
Q3. What is the role of the Agent in this flow?

A.
The Agent controls decision-making.
It decides when to call the model
and when to use tools.
'''
# Example:
# If question requires calculation
# Agent calls calculator tool instead of only LLM



'''
Q4. What is the role of Tools in this architecture?

A.
Tools perform external actions.
They execute real-world tasks beyond text generation.
'''
# Example:
# Database query
# API call
# File read/write



'''
Q5. Why do we call Ollama Python the inference layer?

A.
Because it handles model inference.
It sends input to the model and retrieves output.
It does not manage reasoning logic itself.
'''
# Example:
# ollama.chat(...)
# Returns model output
# Agent decides what to do next



'''
Q6. What is the simple mental model of this architecture?

A.
User gives goal.
Agent thinks and decides.
Ollama generates reasoning.
Tools execute actions.
'''
# Example:
# User: "Book flight"
# Agent → LLM decides intent
# Tool → Calls booking API
# Output → Confirmation message
