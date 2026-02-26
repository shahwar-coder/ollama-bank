'''
Q1. How do you install the Ollama Python library?

A.
You install it using pip, the Python package manager.
'''
# Example:
# pip install ollama



'''
Q2. Does installing the Python library install the Ollama runtime?

A.
No.
The Python library and the Ollama runtime are separate.
The runtime must already be installed on your system.
'''
# Example:
# Step 1: Install Ollama from official website
# Step 2: pip install ollama



'''
Q3. Why is the Ollama runtime required?

A.
Because the runtime actually runs the LLM.
The Python library only communicates with it.
'''
# Example:
# Without runtime → No model execution
# With runtime running → Python can send prompts



'''
Q4. What happens if the runtime is not running?

A.
Python will not be able to connect to the server.
You will get a connection error.
'''
# Example:
# Error: Could not connect to localhost:11434
# Solution: Run "ollama serve" or start Ollama app



'''
Q5. What is the minimum setup required to use Ollama in Python?

A.
1. Ollama runtime installed and running
2. Model downloaded (e.g., llama3)
3. pip install ollama
'''
# Example:
# ollama pull llama3
# pip install ollama
# Then use it inside Python
