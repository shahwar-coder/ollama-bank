'''
Q1. What is the Ollama Python library?

A.
The Ollama Python library is a client that allows Python programs to talk to the Ollama server running locally.
It helps send prompts to models and receive responses.
'''
# Example:
# Python script → Ollama server → LLM → Response returned



'''
Q2. Does the Ollama Python library run the model itself?

A.
No.
The Ollama server runs the model.
The Python library only sends requests and receives responses.
'''
# Example:
# Python sends prompt
# Ollama server processes it
# Model generates output
# Python receives result



'''
Q3. How does communication happen internally?

A.
Communication happens through HTTP requests.
The Python library sends requests to:
http://localhost:11434
'''
# Example:
# Python → HTTP POST → localhost:11434 → Model → Response



'''
Q4. What is the role of localhost:11434?

A.
It is the default address where the Ollama server listens for requests.
It acts as the communication endpoint.
'''
# Example:
# Ollama server running
# Python connects to http://localhost:11434



'''
Q5. What is the basic flow when using Ollama with Python?

A.
The flow is:
Python code → HTTP API → Ollama runtime → Model → Response → Python
'''
# Example:
# prompt = "Explain AI"
# Python sends prompt
# Model processes it
# Text response returned



'''
Q6. Why is the Ollama Python library useful?

A.
It allows developers to integrate local LLMs into applications easily.
No need to manually send HTTP requests.
'''
# Example:
# Build chatbot
# Automate tasks
# Create AI agent using local model