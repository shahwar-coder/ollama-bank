import ollama

response = ollama.chat(
    model='llama3',
    messages=[
        {'role': 'system', 'content': 'You are helpful'},
        {'role': 'user', 'content': 'Explain attention'}
    ]
)

print(response['message']['content'])

'''
Q1. Why is the Chat API considered most important for LLM interaction?

A.
Because modern LLMs are trained to work with structured conversation messages.
The chat format gives clearer context and better responses.
'''
# Example:
# system → Sets behavior
# user → Asks question
# assistant → Responds accordingly



'''
Q2. What is the purpose of the "messages" list?

A.
It represents the conversation.
Each item contains a role and content.
The model reads this structured history to respond properly.
'''
# Example:
# [
#   {'role': 'system', 'content': 'You are helpful'},
#   {'role': 'user', 'content': 'Explain attention'}
# ]



'''
Q3. What is the role of "system" in the messages?

A.
The system role defines behavior or personality of the model.
It sets instructions before the conversation begins.
'''
# Example:
# system: "You are a strict teacher"
# Model responds more formally



'''
Q4. What is the role of "user"?

A.
The user role represents the human asking questions.
It contains the actual query.
'''
# Example:
# user: "Explain attention"



'''
Q5. Where is the generated answer stored in the response?

A.
It is stored inside:
response['message']['content']
'''
# Example:
# print(response['message']['content'])
# Outputs the assistant's reply text



'''
Q6. How is this similar to OpenAI’s chat format?

A.
It uses the same structured message format:
role + content.
This makes it easy to switch between providers.
'''
# Example:
# OpenAI and Ollama both use:
# {'role': 'user', 'content': 'Hello'}
