import ollama

response = ollama.generate(
    model='llama3',
    prompt='Explain transformers simply'
)

print(response['response'])

# =/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=

'''
Q1. What does ollama.generate() do?

A.
It sends a prompt to a selected model and returns generated text.
It is used for simple text generation.
'''
# Example:
# Prompt: "Explain transformers simply"
# Model returns an explanation paragraph



'''
Q2. What happens internally when we call ollama.generate()?

A.
The function sends the prompt to the Ollama server.
The server runs the model.
The model generates text.
The response is returned to Python.
'''
# Example:
# Python → Ollama server → llama3 model → Generated text → Python



'''
Q3. What type of object does ollama.generate() return?

A.
It returns a dictionary.
The generated text is stored inside a key called 'response'.
'''
# Example:
# response = ollama.generate(...)
# print(response['response'])



'''
Q4. Why do we access response['response']?

A.
Because the actual generated text is stored inside that key.
The full returned object contains additional metadata.
'''
# Example:
# response = {
#   'model': 'llama3',
#   'response': 'Transformers are neural networks...',
#   'done': True
# }



'''
Q5. When should we use generate instead of chat?

A.
Use generate when you only need single-prompt text output.
No conversation history required.
'''
# Example:
# Generate summary
# Generate explanation
# Generate paragraph


# =\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\


'''
Q1. What is the role of the ollama.generate() function in this code?

A.
It sends a prompt to the specified model and asks it to generate text.
The model processes the prompt and returns a response.
'''
# Example:
# Prompt: "Explain gravity simply"
# Model returns a simple explanation of gravity



'''
Q2. Why do we specify model='llama3'?

A.
Because Ollama can run multiple models.
We must tell it which model to use for generation.
'''
# Example:
# model='mistral' → uses Mistral
# model='llama3' → uses Llama 3



'''
Q3. What type of object is stored in the variable "response"?

A.
It is a dictionary returned by the Ollama server.
It contains generated text and other metadata.
'''
# Example:
# response = {
#   'model': 'llama3',
#   'response': 'Transformers are neural networks...',
#   'done': True
# }



'''
Q4. Why do we use response['response'] instead of just response?

A.
Because the generated text is stored inside the key named 'response'.
The full object contains more than just the text.
'''
# Example:
# response['response'] → Actual generated paragraph



'''
Q5. What will happen if the Ollama server is not running?

A.
The code will fail with a connection error.
Because Python cannot reach the local Ollama server.
'''
# Example:
# Error: Could not connect to localhost:11434
# Fix: Start Ollama runtime



'''
Q6. What is the complete flow of execution in this code?

A.
1. Python imports ollama
2. Prompt is sent to Ollama server
3. Model processes the prompt
4. Server returns dictionary
5. Printed output shows generated text
'''
# Example:
# Input: "Explain AI"
# Output printed: "AI is a field of computer science..."