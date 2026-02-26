'''
Q1. What does ollama.list() do?

A.
It shows all models currently installed in your local Ollama environment.
'''
# Example:
# Output might include:
# llama3
# mistral
# nomic-embed-text



'''
Q2. What is the purpose of ollama.pull('llama3')?

A.
It downloads the specified model from the Ollama registry
into your local machine.
'''
# Example:
# ollama.pull('llama3')
# → Model files downloaded
# → Ready for use in generation or chat



'''
Q3. When should you use ollama.pull()?

A.
When a model is not installed locally
but you want to use it.
'''
# Example:
# Trying to use llama3 without pulling
# → Error
# After pull → Works correctly



'''
Q4. What does ollama.show('llama3') do?

A.
It displays detailed information about the model.
This may include size, parameters, and configuration.
'''
# Example:
# Model name: llama3
# Context length: 8192
# Parameters: 8B



'''
Q5. What is the core mental model of model management in Ollama?

A.
Models live locally.
You can:
- List what you have
- Pull new ones
- Inspect their details
'''
# Example:
# list → See models
# pull → Download model
# show → Inspect model
